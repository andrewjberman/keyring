# model-policy.ps1 -- the ONE reader of org/ref/MODEL_POLICY.json for the PowerShell launchers.
# Dot-sourced by .tools/ajb.ps1 and .tools/spawn-agent.ps1 so both resolve a seat's model the same way.
#
# Get-OpalModelPolicy <serial> returns a hashtable {Model, Effort, Role, Device, PolicyId} when THIS box
# is a treatment device AND the serial's base matches a role; otherwise $null, and the caller keeps its
# pre-policy defaults (the control arm). Device = AGENTBUS_DEVICE (process env, else persisted user env),
# the same claim lib/devices.py reads. A missing or unreadable policy file returns $null (control) and
# says so once: a launch must never fail on this file.
# Record: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261010_23xxZ_MODEL_POLICY_BY_ROLE_AND_TEST_PLAN.md

function Get-OpalModelPolicy {
    param([Parameter(Mandatory = $true)][string]$Serial)
    # $PSScriptRoot here is .tools/ (where this function is defined), whichever script dot-sources it.
    $policyPath = Join-Path (Split-Path -Parent $PSScriptRoot) 'org\ref\MODEL_POLICY.json'
    if (-not (Test-Path $policyPath)) {
        Write-Host "[model-policy] WARN: $policyPath absent -- pre-policy defaults apply" -ForegroundColor Yellow
        return $null
    }
    try {
        $p = Get-Content -Raw -Encoding UTF8 $policyPath | ConvertFrom-Json
    } catch {
        Write-Host "[model-policy] WARN: $policyPath unreadable ($($_.Exception.Message)) -- pre-policy defaults apply" -ForegroundColor Yellow
        return $null
    }
    $device = "$env:AGENTBUS_DEVICE".Trim()
    if (-not $device) { $device = "$([Environment]::GetEnvironmentVariable('AGENTBUS_DEVICE', 'User'))".Trim() }
    if (-not $device -or -not (@($p.treatment_devices) -contains $device)) { return $null }
    $base = $Serial -replace '~[A-Za-z0-9]+$', ''
    foreach ($r in @($p.roles)) {
        if ($base -match $r.serial_regex) {
            return @{ Model = $r.model; Effort = $r.effort; Role = $r.role; Device = $device; PolicyId = $p.policy_id }
        }
    }
    return $null
}
