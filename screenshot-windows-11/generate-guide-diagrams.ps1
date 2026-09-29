Add-Type -AssemblyName System.Drawing

function C([int]$r, [int]$g, [int]$b) { [System.Drawing.Color]::FromArgb($r, $g, $b) }
function B([int]$r, [int]$g, [int]$b) { [System.Drawing.SolidBrush]::new((C $r $g $b)) }
function F([int]$size, [bool]$bold = $false) {
    $style = if ($bold) { [System.Drawing.FontStyle]::Bold } else { [System.Drawing.FontStyle]::Regular }
    [System.Drawing.Font]::new('Segoe UI', $size, $style)
}
function RoundRect($g, $brush, [int]$x, [int]$y, [int]$w, [int]$h, [int]$r) {
    $p = [System.Drawing.Drawing2D.GraphicsPath]::new()
    $d = 2 * $r
    $p.AddArc($x, $y, $d, $d, 180, 90)
    $p.AddArc($x + $w - $d, $y, $d, $d, 270, 90)
    $p.AddArc($x + $w - $d, $y + $h - $d, $d, $d, 0, 90)
    $p.AddArc($x, $y + $h - $d, $d, $d, 90, 90)
    $p.CloseFigure()
    $g.FillPath($brush, $p)
    $p.Dispose()
}
function Canvas {
    $bmp = [System.Drawing.Bitmap]::new(1600, 900)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
    $g.Clear((C 244 249 253))
    return @{ Bitmap = $bmp; G = $g }
}
function Label($g, $text, $font, $brush, [int]$x, [int]$y) { $g.DrawString($text, $font, $brush, $x, $y) }
function Footer($g) { Label $g 'Схема редакции · не снимок интерфейса Windows' (F 21) (B 85 104 125) 76 835 }

$blue = B 21 75 125
$dark = B 24 42 67
$muted = B 83 107 133
$cyan = B 29 159 220
$pale = B 222 240 251
$white = B 255 255 255
$border = [System.Drawing.Pen]::new((C 49 129 185), 4)

# Four choices shown by Snipping Tool. These drawings explain the modes; they do not mimic its UI.
$c = Canvas
$g = $c.G
Label $g 'Четыре режима захвата' (F 58 $true) $dark 70 52
Label $g 'Выберите область, форму, окно или весь экран' (F 27) $muted 75 137
$cards = @(
    @{ X=72; Title='Прямоугольник'; Text='Выделите нужный участок'; Mode=1 },
    @{ X=455; Title='Произвольная форма'; Text='Обведите объект мышью'; Mode=2 },
    @{ X=838; Title='Окно'; Text='Щёлкните нужное окно'; Mode=3 },
    @{ X=1221; Title='Весь экран'; Text='Снимок без выделения'; Mode=4 }
)
foreach ($card in $cards) {
    $x = [int]$card.X
    RoundRect $g $white $x 230 315 495 25
    RoundRect $g $pale ($x + 24) 255 267 272 16
    $g.DrawRectangle($border, $x + 47, 282, 221, 218)
    $g.DrawLine($border, $x + 47, 312, $x + 268, 312)
    switch ($card.Mode) {
        1 { RoundRect $g $cyan ($x + 92) 355 130 95 7 }
        2 {
            $pts = [System.Drawing.Point[]]@(
                [System.Drawing.Point]::new($x+89,385), [System.Drawing.Point]::new($x+130,344),
                [System.Drawing.Point]::new($x+208,361), [System.Drawing.Point]::new($x+229,415),
                [System.Drawing.Point]::new($x+181,461), [System.Drawing.Point]::new($x+111,445)
            )
            $g.FillPolygon($cyan, $pts)
        }
        3 {
            RoundRect $g $cyan ($x + 84) 341 153 131 8
            $g.DrawLine([System.Drawing.Pen]::new((C 255 255 255), 3), $x+84, 367, $x+237, 367)
        }
        4 { RoundRect $g $cyan ($x + 55) 322 205 170 5 }
    }
    Label $g $card.Title (F 24 $true) $dark ($x + 22) 557
    Label $g $card.Text (F 19) $muted ($x + 22) 608
}
Footer $g
$c.Bitmap.Save((Join-Path $PSScriptRoot 'capture-modes.png'), [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose(); $c.Bitmap.Dispose()

# The decisive distinction: a file and a clipboard image are different outcomes.
$c = Canvas
$g = $c.G
Label $g 'Куда попадает снимок?' (F 58 $true) $dark 70 52
Label $g 'Сначала проверьте результат, потом ищите файл' (F 27) $muted 75 137
$rows = @(
    @{Y=225;Key='Win + PrtSc';Result='Файл';Detail='Изображения → Снимки экрана';Color=(B 37 139 190)},
    @{Y=410;Key='Win + Shift + S';Result='Буфер + «Ножницы»';Detail='Файл — если включено автосохранение';Color=(B 64 127 180)},
    @{Y=595;Key='Alt + PrtSc';Result='Буфер обмена';Detail='Ctrl + V → Paint → Ctrl + S';Color=(B 104 113 179)}
)
foreach ($row in $rows) {
    $y = [int]$row.Y
    RoundRect $g $white 72 $y 1450 147 22
    RoundRect $g $row.Color 94 ($y+27) 426 93 15
    Label $g $row.Key (F 33 $true) $white 117 ($y+47)
    Label $g '→' (F 46 $true) $cyan 550 ($y+31)
    Label $g $row.Result (F 31 $true) $dark 625 ($y+24)
    Label $g $row.Detail (F 23) $muted 625 ($y+78)
}
Footer $g
$c.Bitmap.Save((Join-Path $PSScriptRoot 'where-screenshot-goes.png'), [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose(); $c.Bitmap.Dispose()

Write-Output 'Created capture-modes.png and where-screenshot-goes.png'
