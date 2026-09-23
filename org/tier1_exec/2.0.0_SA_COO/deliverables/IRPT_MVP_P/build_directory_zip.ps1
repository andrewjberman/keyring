param([Parameter(Mandatory=$true)][string]$PreparedDirectory)
$ErrorActionPreference = 'Stop'
$prepared = (Resolve-Path -LiteralPath $PreparedDirectory).Path
$manifest = Get-Content -LiteralPath (Join-Path $prepared 'manifest.json') -Raw | ConvertFrom-Json
$destination = Join-Path $prepared 'irpt-directory-search.zip'
if (Test-Path -LiteralPath $destination) { throw 'Refusing to overwrite prepared artifact' }
# The same .NET ZIP construction as canonical build-and-upload.sh:481-508,
# kept separate because that canonical command uploads and has no dry-run mode.
Add-Type -Assembly 'System.IO.Compression.FileSystem'
$zip = [System.IO.Compression.ZipFile]::Open($destination, 'Create')
try {
    foreach ($member in ($manifest.members.member | Sort-Object)) {
        $entry = $zip.CreateEntry($member, [System.IO.Compression.CompressionLevel]::Optimal)
        $entry.LastWriteTime = [DateTime]::new(2020, 1, 1, 0, 0, 0)
        $stream = $entry.Open()
        try {
            $bytes = [System.IO.File]::ReadAllBytes((Join-Path (Join-Path $prepared 'payload') $member))
            $stream.Write($bytes, 0, $bytes.Length)
        } finally { $stream.Dispose() }
    }
} finally { $zip.Dispose() }
Get-FileHash -LiteralPath $destination -Algorithm SHA256
