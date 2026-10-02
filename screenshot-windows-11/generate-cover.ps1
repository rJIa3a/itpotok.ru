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

$titleFont = [System.Drawing.Font]::new('Segoe UI', 46, [System.Drawing.FontStyle]::Bold)
$subtitleFont = [System.Drawing.Font]::new('Segoe UI', 25, [System.Drawing.FontStyle]::Regular)
$keyFont = [System.Drawing.Font]::new('Segoe UI', 30, [System.Drawing.FontStyle]::Bold)
$hintFont = [System.Drawing.Font]::new('Segoe UI', 22, [System.Drawing.FontStyle]::Regular)
$badgeFont = [System.Drawing.Font]::new('Segoe UI', 25, [System.Drawing.FontStyle]::Bold)

FillRound $panelBrush 85 48 1430 804 36

function CenterText($label, $font, $brush, $y) {
    $size = $graphics.MeasureString($label, $font)
    $graphics.DrawString($label, $font, $brush, (($width - $size.Width) / 2), $y)
}

# The theme crops the wide image to a portrait card. Keep all text within
# the central 500 pixels so it survives that crop.
CenterText 'Скриншот' $titleFont $white 106
CenterText 'Windows 11' $titleFont $accent 185
CenterText '3 быстрых способа' $subtitleFont $muted 280

function Key($x, $y, $w, $label) {
    FillRound $keyBrush $x $y $w 76 14
    $size = $graphics.MeasureString($label, $keyFont)
    $graphics.DrawString($label, $keyFont, $keyText, ($x + ($w - $size.Width) / 2), ($y + 12))
}

Key 550 368 500 'Win + Shift + S'
CenterText 'выбранная область' $hintFont $white 447

Key 550 502 500 'Win + PrtSc'
CenterText 'весь экран в файл' $hintFont $white 581

Key 550 636 500 'Alt + PrtSc'
CenterText 'одно окно в буфер' $hintFont $white 715

CenterText 'Схема редакции' $hintFont $muted 792

$path = Join-Path $PSScriptRoot 'keyboard-shortcuts-cover.png'
$bitmap.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
$graphics.Dispose()
$bitmap.Dispose()
Write-Output $path
