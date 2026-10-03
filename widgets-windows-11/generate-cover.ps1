Add-Type -AssemblyName System.Drawing
$bitmap = [System.Drawing.Bitmap]::new(1600,900)
$g = [System.Drawing.Graphics]::FromImage($bitmap)
$g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
$bg = [System.Drawing.Drawing2D.LinearGradientBrush]::new([System.Drawing.Point]::new(0,0),[System.Drawing.Point]::new(1600,900),[System.Drawing.Color]::FromArgb(13,26,54),[System.Drawing.Color]::FromArgb(23,83,110))
$g.FillRectangle($bg,0,0,1600,900)
function B($hex){[System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml($hex))}
function Round($brush,$x,$y,$w,$h,$r){
 $p=[System.Drawing.Drawing2D.GraphicsPath]::new();$d=2*$r
 $p.AddArc($x,$y,$d,$d,180,90);$p.AddArc($x+$w-$d,$y,$d,$d,270,90)
 $p.AddArc($x+$w-$d,$y+$h-$d,$d,$d,0,90);$p.AddArc($x,$y+$h-$d,$d,$d,90,90);$p.CloseFigure()
 $g.FillPath($brush,$p);$p.Dispose()
}
function Center($text,$size,$brush,$y,$bold=$false){
 $style=[System.Drawing.FontStyle]::Regular;if($bold){$style=[System.Drawing.FontStyle]::Bold}
 $font=[System.Drawing.Font]::new('Segoe UI',$size,$style);$s=$g.MeasureString($text,$font)
 $g.DrawString($text,$font,$brush,(1600-$s.Width)/2,$y);$font.Dispose()
}
$white=B '#F3FAFF';$muted=B '#B7D7E7';$mint=B '#76E4C8';$panel=B '#1D486A'
# Decorative cards are an editorial illustration, not Windows UI.
Round (B '#173752') 92 142 350 220 28
Round (B '#204962') 1158 438 350 220 28
Round (B '#245572') 140 455 300 245 28
Round (B '#163A59') 1160 135 280 235 28
$pen=[System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml('#76E4C8'),7)
$g.DrawEllipse($pen,210,210,82,82)
$g.FillEllipse($white,259,259,92,42);$g.FillEllipse($white,236,248,66,55)
for($i=0;$i -lt 4;$i++){$g.FillRectangle($mint,1220+42*$i,580-22*$i,25,22*$i+28)}
$g.DrawEllipse($pen,215,515,122,122);$g.DrawLine($pen,276,576,276,539);$g.DrawLine($pen,276,576,309,594)
for($i=0;$i -lt 3;$i++){Round $mint 1216 (195+40*$i) 165 12 6}
Round $panel 525 100 550 700 36
Center 'ВИДЖЕТЫ' 46 $white 163 $true
Center 'Windows 11' 35 $mint 254 $true
Center 'Настроить под себя' 21 $muted 341
Round (B '#EDF8FC') 603 427 394 205 28
$ink=B '#173D5A';$g.FillEllipse((B '#FFC65C'),644,464,54,54)
$g.FillEllipse((B '#5EACD5'),680,493,95,38)
$g.FillRectangle((B '#D5E5EF'),802,468,142,13);$g.FillRectangle((B '#D5E5EF'),802,500,103,13)
$g.DrawLines([System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml('#299C86'),5),[System.Drawing.Point[]]@([System.Drawing.Point]::new(645,594),[System.Drawing.Point]::new(700,568),[System.Drawing.Point]::new(756,579),[System.Drawing.Point]::new(810,545),[System.Drawing.Point]::new(868,554),[System.Drawing.Point]::new(941,536)))
Center 'Панель · экран блокировки' 17 $white 672
Center 'Рабочий стол' 17 $white 715
Center 'ITpotok.ru' 16 $muted 829
$bitmap.Save((Join-Path $PSScriptRoot 'widgets-windows-11-cover-20261003.png'),[System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose();$bitmap.Dispose()
