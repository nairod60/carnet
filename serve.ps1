# Serveur de test minimal (Python absent sur cette machine) : .\serve.ps1 puis ouvrir http://localhost:8765
param([string]$Root = (Join-Path $PSScriptRoot "dist"), [int]$Port = 8765)
$l = New-Object Net.HttpListener
$l.Prefixes.Add("http://localhost:$Port/")
$l.Start()
Write-Host "serving $Root on http://localhost:$Port/"
$mime = @{ ".html"="text/html; charset=utf-8"; ".js"="application/javascript"; ".json"="application/json"; ".png"="image/png"; ".css"="text/css" }
while ($l.IsListening) {
  $c = $l.GetContext()
  $p = $c.Request.Url.AbsolutePath; if ($p -eq "/") { $p = "/index.html" }
  $f = Join-Path $Root $p.TrimStart("/")
  if (Test-Path $f -PathType Leaf) {
    $b = [IO.File]::ReadAllBytes($f)
    $ext = [IO.Path]::GetExtension($f); $c.Response.ContentType = if ($mime[$ext]) { $mime[$ext] } else { "application/octet-stream" }
    $c.Response.ContentLength64 = $b.Length; $c.Response.OutputStream.Write($b, 0, $b.Length)
  } else { $c.Response.StatusCode = 404 }
  $c.Response.Close()
}
