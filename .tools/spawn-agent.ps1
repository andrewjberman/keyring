# spawn-agent.ps1 -- spawn an Opal agent in its own PowerShell window.
#
# Usage:  .tools\spawn-agent.ps1 <Serial> [extra first-message words]
#
# Opens a NEW detached PowerShell window, dot-sources cclaude.ps1, and runs
# `cclaude <Serial>` -- which cd's into ajb_workspace and launches `claude`
# hands-free (cclaude carries --dangerously-skip-permissions, so the spawned
# agent never stalls on a folder-trust or per-tool permission prompt). Each
# spawn is appended to org/mcp/agent-spawn-audit.log.
#
# This is the agent-provisioning capability for 0.0.0_AB_MSTR: MSTR runs
# `spawn-agent.ps1 <Serial>` to staff a chartered workstream. Provisioning ONLY
# -- task orders and direction still flow through Tier 1 (Constitution Art. VI:
# spawn != dispatch). A spawn is an S1 action MSTR ledgers like any commitment.
#
# EXAMPLES:
#   .tools\spawn-agent.ps1 0.0.0_AB_MSTR
#   .tools\spawn-agent.ps1 0.4.0_DS_ClientPlatform
#   .tools\spawn-agent.ps1 2.0.0_SA_COO "/loop ADVI"

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Serial,

    [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
    [string[]]$Extra
)

$ws = 'C:\Users\AndrewBerman\Desktop\ajb_workspace'
$cclaude = Join-Path $ws '.tools\cclaude.ps1'

if (-not (Test-Path $cclaude)) {
    Write-Error "spawn-agent: cclaude.ps1 not found at $cclaude"
    exit 1
}

# Loose serial sanity check -- {N.N.N}_{ROLE}_{Name}[~lane]
if ($Serial -notmatch '^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$') {
    Write-Error "spawn-agent: '$Serial' does not look like an agent serial (e.g. 0.4.0_DS_ClientPlatform)"
    exit 1
}

$extraStr = if ($Extra) { ' ' + ($Extra -join ' ') } else { '' }

# New window: -NoProfile (deterministic -- does not depend on $PROFILE setup),
# -NoExit (window persists so the session stays visible). Dot-source cclaude.ps1
# explicitly so the `cclaude` function exists regardless of profile setup.
$inner = ". `"$cclaude`"; cclaude $Serial$extraStr"
Start-Process powershell -ArgumentList '-NoProfile', '-NoExit', '-Command', $inner

# Audit -- every spawn is recorded.
$log = Join-Path $ws 'org\mcp\agent-spawn-audit.log'
$ts  = [DateTime]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ')
$by  = if ($env:OPAL_AGENT_SERIAL) { $env:OPAL_AGENT_SERIAL } else { 'unknown' }
Add-Content -Path $log -Value "$ts  SPAWN  $Serial  by $by"

Write-Host "[spawn-agent] launched $Serial in a new window (spawned by $by)" -ForegroundColor Green
