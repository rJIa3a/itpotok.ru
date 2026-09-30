Add-Type -AssemblyName System.Drawing

$width = 1600
$height = 900
$bitmap = [System.Drawing.Bitmap]::new($width, $height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit

function Color([int]$r, [int]$g, [int]$b) {
    [System.Drawing.Color]::FromArgb($r, $g, $b)
}

function Brush([int]$r, [int]$g, [int]$b) {
    [System.Drawing.SolidBrush]::new((Color $r $g $b))
}

function FillRound($brush, [int]$x, [int]$y, [int]$w, [int]$h, [int]$radius) {
    $path = [System.Drawing.Drawing2D.GraphicsPath]::new()
    $d = $radius * 2
    $path.AddArc($x, $y, $d, $d, 180, 90)
    $path.AddArc($x + $w - $d, $y, $d, $d, 270, 90)
    $path.AddArc($x + $w - $d, $y + $h - $d, $d, $d, 0, 90)
    $path.AddArc($x, $y + $h - $d, $d, $d, 90, 90)
    $path.CloseFigure()
    $graphics.FillPath($brush, $path)
    $path.Dispose()
}

$background = [System.Drawing.Drawing2D.LinearGradientBrush]::new(
    [System.Drawing.Point]::new(0, 0),
    [System.Drawing.Point]::new($width, $height),
    (Color 13 27 55),
    (Color 25 69 110)
)
$graphics.FillRectangle($background, 0, 0, $width, $height)

$accent = Brush 62 184 255
$white = Brush 245 250 255
$muted = Brush 178 207 229
$keyBrush = Brush 237 246 253
$keyText = Brush 20 48 76
$panelBrush = Brush 26 81 132
$outline = [System.Drawing.Pen]::new((Color 70 191 255), 6)
$outline.DashStyle = [System.Drawing.Drawing2D.DashStyle]::Dash
$thin = [System.Drawing.Pen]::new((Color 125 211 255), 3)

$titleFont = [System.Drawing.Font]::new('Segoe UI', 70, [System.Drawing.FontStyle]::Bold)
$subtitleFont = [System.Drawing.Font]::new('Segoe UI', 31, [System.Drawing.FontStyle]::Regular)
$keyFont = [System.Drawing.Font]::new('Segoe UI', 32, [System.Drawing.FontStyle]::Bold)
$hintFont = [System.Drawing.Font]::new('Segoe UI', 24, [System.Drawing.FontStyle]::Regular)
$badgeFont = [System.Drawing.Font]::new('Segoe UI', 25, [System.Drawing.FontStyle]::Bold)

FillRound $panelBrush 85 78 1430 744 36
$graphics.DrawString('Скриншот', $titleFont, $white, 250, 112)
$graphics.DrawString('в Windows 11', $titleFont, $accent, 250, 205)
$graphics.DrawString('Быстрые сочетания клавиш', $subtitleFont, $muted, 255, 310)

function Key($x, $y, $w, $label) {
    FillRound $keyBrush $x $y $w 76 14
    $size = $graphics.MeasureString($label, $keyFont)
    $graphics.DrawString($label, $keyFont, $keyText, ($x + ($w - $size.Width) / 2), ($y + 12))
}

Key 250 413 110 'Win'
Key 379 413 145 'Shift'
Key 543 413 90 'S'
$graphics.DrawString('область', $hintFont, $white, 660, 435)

Key 250 518 110 'Win'
Key 379 518 205 'PrtSc'
$graphics.DrawString('весь экран', $hintFont, $white, 610, 540)

Key 250 623 110 'Alt'
Key 379 623 205 'PrtSc'
$graphics.DrawString('одно окно', $hintFont, $white, 610, 645)

FillRound (Brush 18 50 84) 990 382 405 300 24
$graphics.DrawRectangle($outline, 1022, 415, 342, 232)
$graphics.DrawLine($thin, 1022, 430, 1364, 430)
$graphics.DrawString('ВЫБРАТЬ', $badgeFont, $accent, 1062, 496)
$graphics.DrawString('ОБЛАСТЬ', $badgeFont, $white, 1062, 547)

$graphics.DrawString('Иллюстрация сочетаний, не снимок интерфейса', $hintFont, $muted, 250, 755)

$path = Join-Path $PSScriptRoot 'keyboard-shortcuts-cover.png'
$bitmap.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
$graphics.Dispose()
$bitmap.Dispose()
Write-Output $path
