# ajb.ps1 -- instant Opal-agent launcher for ajb_workspace (PowerShell).
#
# Drops `claude` into the workspace with the serial as the opening message; the
# agent self-identifies, registers via register_agent(), and runs the org/XXX.md
# startup protocol. Also sets $env:OPAL_AGENT_SERIAL so the PostToolUse telemetry
# hook attributes this session's tool calls correctly (the per-process env var
# wins over the shared .comp-graph/.agent_context when agents run concurrently).
#
# SETUP (one time): dot-source from your PowerShell profile ($PROFILE):
#   . "<your-clone-of-ajb_workspace>\.tools\ajb.ps1"
#
# USAGE:
#   ajb <Serial>                 launch an agent; first message = the serial
#   ajb <Serial> <extra words>   first message = serial + the extra text
#
# EXAMPLES:
#   ajb 2.0.0_SA_COO
#   ajb 0.4.0_DS_ClientPlatform~B
#   ajb 2.0.0_SA_COO "/loop ADVI"

# ---------------------------------------------------------------------------
# REPO ROOT -- resolved ONCE, from THIS FILE'S OWN LOCATION. Never a user path:
# a second device clones to a different absolute path, so everything below must
# follow the clone. Deliberately NOT `git rev-parse` (must work before/without
# git, and a CWD-sensitive resolver re-introduces ambient-state coupling).
#
# OPAL_WS_ROOT is the device-level escape hatch, checked FIRST. An env var lives
# OUTSIDE the repo, per machine, and can never be pushed -- the one place a
# device-specific path can live without two sites silently overwriting each
# other. Leave it UNSET normally; derivation handles the standard layout.
#   [Environment]::SetEnvironmentVariable('OPAL_WS_ROOT','<clone path>','User')
# ---------------------------------------------------------------------------
if ($env:OPAL_WS_ROOT -and (Test-Path -LiteralPath $env:OPAL_WS_ROOT)) {
    $Global:AjbRepoRoot = (Resolve-Path -LiteralPath $env:OPAL_WS_ROOT).Path
} elseif ($env:OPAL_WS_ROOT) {
    Write-Host "[ajb] WARN: OPAL_WS_ROOT is set but does not exist: $env:OPAL_WS_ROOT -- ignoring it and deriving instead." -ForegroundColor Yellow
    $Global:AjbRepoRoot = Split-Path -Parent $PSScriptRoot
} elseif ($PSScriptRoot) {
    $Global:AjbRepoRoot = Split-Path -Parent $PSScriptRoot
} elseif (-not $Global:AjbRepoRoot) {
    # Only reachable if this file is pasted into a session rather than dot-sourced.
    $Global:AjbRepoRoot = (Get-Location).Path
    Write-Host "[ajb] WARN: no `$PSScriptRoot -- repo root guessed from CWD: $Global:AjbRepoRoot" -ForegroundColor Yellow
}

# Get-AgentLoopDirective: serial -> slim role directive injected into the launch
# first message.
#
# LAUNCHER LAW (Andrew-direct 2026-08-20): launch scripts stay SLIM, to the
# point, SESSION-AGNOSTIC -- key loops and skills for the role only.
#   - ZERO crons armed at launch, every serial. Loops are operator-initiated.
#   - This launcher NEVER carries a scoped loop authorization, a cadence, or a
#     standing-duty writeup: org/XXX.md Step 1b-F is the single source of truth
#     (each row states its own stop condition). A cadence hardcoded here would
#     keep arming after its authorization expired.
#   - No dated incidents, verbatims, or supersession history in launch text: a
#     retracted rule is only as dead as its last-surviving copy, and this file
#     is what a fresh session reads FIRST. History: git log + org/tier0/ledger/.
function Get-AgentLoopDirective {
    [CmdletBinding()]
    param([Parameter(Mandatory=$true)] [string]$Serial)

    # Lane suffixes (~B/~C/...) share the base serial's role.
    $base = $Serial -replace '~[A-Za-z0-9]+$', ''

    $header = "Loop arming: ZERO crons at launch, every serial -- loops are operator-initiated. /watcher arms ONCE at load and is NOT a loop. Any live scoped loop authorization is recorded in org/ref/LIVE_ARMS.md -- that file is the only source of truth."

    switch -Regex ($base) {
        '^0\.0\.0_AB_MSTR$' {
            return "$header`n  MSTR:`n  1. /watcher ONCE (inbox Monitor, arm-at-load).`n  2. /agentbus ONCE (this device's cross-device SQS consumer; an rc=3 refusal naming a live pid means a consumer already holds this device -- that IS success, do not work around it).`n  3. /integrate ONCE (joint fabric parity ASSESSMENT; assess-only at load -- /integrate merge only on explicit direction).`n  Event-triggered: /mstr-review, /mstr-spawn, /mstr-kill, /mstr-charter, /comp-ferry, /govern (Andrew-discretion).`n  Spawn/kill of WORK-population seats is the COO's own function (MSTR keeps the primitive for infra-class population: reboots, fleet relaunch, cross-fabric seats).`n  Standing duties + any scoped arming: org/XXX.md Step 1b-F MSTR row."
        }
        '^1\.0\.0_SA_CTO$' {
            return "$header`n  ws CTO: /watcher ONCE. /ws-charter ad-hoc. Event-driven via the inbox Monitor; /fabric-check + /stimulus-scan on signals, not timers."
        }
        '^1\.1\.0_SA_CTO$' {
            return "$header`n  CL CTO: /watcher ONCE. /cl-charter ad-hoc. Event-driven via the inbox Monitor."
        }
        '^2\.0\.0_SA_COO$' {
            return "$header`n  COO: /watcher ONCE. /drive is OFF by default. Arm /drive ONLY per a live scoped authorization in the org/XXX.md Step 1b-F COO row (honor its cadence AND its stop condition); if none is live, arm nothing.`n  Event-triggered: /mstr-spawn, /mstr-kill (a COO function in addition to 0.0.0_AB_MSTR -- Andrew-direct 2026-08-28; seat and release work-population lanes directly, no request to MSTR)."
        }
        '^3\.0\.0_SA_CVO$' {
            return "$header`n  ws CVO: /watcher ONCE. /spot-check + /verify-channel ad-hoc / closeout-triggered. Scope (base vs ~Z) + any scoped arming: org/XXX.md Step 1b-F CVO rows."
        }
        '^0\.[0-9]+\.[0-9]+_AE_CloudOps(~[A-Za-z0-9]+)?$' {
            return "$header`n  AE_CloudOps: /watcher ONCE, then /cloud-ops ONCE (session-orient one-shot, not a cron). Event-driven. /work ad-hoc."
        }
        '^0\.8\.0_AE_CloudComp(~[A-Za-z0-9]+)?$' {
            return "$header`n  AE_CloudComp: /watcher ONCE, then /cloud-ops ONCE. Event-driven. /work ad-hoc."
        }
        '^0\.[0-9]+\.[0-9]+_(DS|AE|DE|DT|RD)_' {
            return "$header`n  Tier-2/3: /watcher ONCE. Event-driven. /work ad-hoc."
        }
        '^0\.[0-9]+\.[0-9]+_WK_' {
            return "$header`n  Worker: /watcher ONCE. Your task order is your whole instruction."
        }
        '^4\.0\.0_SA_CRO(~[A-Za-z0-9]+)?$' {
            return "$header`n  ws CRO (does NOT dispatch): /watcher ONCE. Event-driven: research/RCG program work + Andrew directives via the inbox Monitor."
        }
        '^0\.0\.[0-9]+_(UA|BG)_' {
            return "$header`n  Tier-0 Utility Agent: /watcher ONCE, then the launcher skill(s) in your prompt.md 'On Launch' section. Event-driven + on-demand; draft-and-ask on anything outward-facing or irreversible."
        }
        default {
            return "$header`n  UNRECOGNIZED ('$Serial' matched no role pattern)`n  1. Run /watcher ONCE (arm-at-load).`n  WARN MSTR: 'role-mapping gap for $Serial in ajb.ps1'."
        }
    }
}

# Get-SeatStatement: serial -> the seat's statement of what it IS (org/ref/SEAT_ROLES.json, read only by
# lib/seat_roles.py). A LAUNCH AID, NEVER A LAUNCH DEPENDENCY: every failure (no python, no module, a
# malformed file, an unknown kind, a hang past 20 s, an exception) returns Text=$null with a Reason and the
# caller launches on the existing role text. Reads only; writes nothing.
function Get-SeatStatement {
    [CmdletBinding()]
    param([Parameter(Mandatory=$true)] [string]$Serial)

    $result = @{ Text = $null; Reason = 'unknown failure' }
    try {
        $module = Join-Path $Global:AjbRepoRoot 'lib\seat_roles.py'
        if ($Serial -notmatch '^[A-Za-z0-9._~-]+$') { $result.Reason = 'serial has characters outside A-Za-z0-9._~-'; return $result }
        if (-not (Test-Path -LiteralPath $module)) { $result.Reason = 'lib/seat_roles.py not found'; return $result }
        $py = Get-Command python -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
        if (-not $py) { $py = Get-Command py -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1 }
        if (-not $py) { $result.Reason = 'python not found on PATH'; return $result }
        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName = $py.Source
        $psi.Arguments = '"' + $module + '" statement ' + $Serial
        $psi.WorkingDirectory = $Global:AjbRepoRoot
        $psi.UseShellExecute = $false
        $psi.CreateNoWindow = $true
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError = $true
        $proc = [System.Diagnostics.Process]::Start($psi)
        $outTask = $proc.StandardOutput.ReadToEndAsync()
        $errTask = $proc.StandardError.ReadToEndAsync()
        if (-not $proc.WaitForExit(20000)) {
            try { $proc.Kill() } catch { }
            $result.Reason = 'timed out after 20 s'
            return $result
        }
        $out = ($outTask.Result).Trim()
        $err = ($errTask.Result).Trim()
        if ($proc.ExitCode -ne 0) {
            $why = $err
            if ($why.Length -gt 120) { $why = $why.Substring(0, 120) }
            $result.Reason = "python exit $($proc.ExitCode): $why"
            return $result
        }
        if (-not $out) { $result.Reason = 'python printed nothing'; return $result }
        $result.Text = $out -replace "`r`n", "`n"
        $result.Reason = ''
        return $result
    } catch {
        $result.Text = $null
        $result.Reason = "exception: $($_.Exception.Message)"
        return $result
    }
}

function ajb {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Serial,

        # -Headless: drop --dangerously-load-development-channels so autonomous
        # spawns never stall on its Y/N startup prompt (Claude Code ignores the
        # push mechanism that flag enables; current push works without it).
        [switch]$Headless,

        # -Model / -Effort: optional per-session overrides passed straight to
        # `claude --model` / `claude --effort`. Unset = claude's own default.
        [string]$Model,
        [string]$Effort,

        # -PrintPrompt: print the assembled first message to standard output and return. Nothing
        # after the assembly runs: no claude, no window or tab, no env var, no file written.
        [switch]$PrintPrompt,

        [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
        [string[]]$Extra
    )

    # CL-serial cwd routing: the feature_clb worktree is RETIRED (LD-0222) and CL
    # agents are paused, so CL serials fall back to ws-root instead of hard-erroring
    # on the deleted worktree. The routing identity is preserved for a future re-home.
    $base = $Serial -replace '~[A-Za-z0-9]+$', ''
    if ($env:AJB_FORCE_WS -eq '1') {
        $ws = $Global:AjbRepoRoot
        Write-Host "[ajb] AJB_FORCE_WS=1 -> ajb_workspace cwd" -ForegroundColor Yellow
    } else {
        switch -Regex ($base) {
            '^(1\.1\.0_SA_CTO|2\.1\.0_SA_COO|3\.1\.0_SA_CVO|2\.1\.0_SC_CompLearns|1\.[1-4]\.0_DS_CompLearns)$' {
                $ws = $Global:AjbRepoRoot
                Write-Host "[ajb] CL worktree RETIRED (LD-0222); CL paused -> ws-root fallback (re-home TBD)" -ForegroundColor Yellow
            }
            default {
                $ws = $Global:AjbRepoRoot
            }
        }
    }
    if (-not (Test-Path $ws)) {
        Write-Error "ajb: workspace not found at $ws"
        return
    }

    # Manual launches inside Windows Terminal: an in-tab title write does not
    # stick (suppressApplicationTitle ignores runtime OSC writes), so re-launch
    # this same `ajb <Serial>` in a NEW titled tab of the current window --
    # `wt --title` at tab CREATION is the only mechanism that survives. Headless
    # spawns already get this from spawn-agent.ps1. Outside WT the in-tab OSC
    # path below still works. Escape hatch: $env:AJB_NO_WT_RELAUNCH = '1'.
    if (-not $PrintPrompt -and -not $Headless -and $env:WT_SESSION -and $env:AJB_NO_WT_RELAUNCH -ne '1') {
        $wtCmd = Get-Command wt.exe -ErrorAction SilentlyContinue
        if ($wtCmd) {
            $ajbPath = Join-Path $Global:AjbRepoRoot '.tools\ajb.ps1'
            # SINGLE-quoted PS literals throughout: powershell.exe's native-argument
            # layer strips inner DOUBLE quotes from a -Command string, so a root
            # containing a space would arrive split. Embedded single quotes are
            # doubled (the PS escape). Hand the child OPAL_WS_ROOT so it resolves
            # the root from an env value rather than another quoting layer.
            $extraLit = ''
            if ($Extra) { $extraLit = " '" + (($Extra -join ' ').Replace("'", "''")) + "'" }
            $ajbLit  = "'" + $ajbPath.Replace("'", "''") + "'"
            $rootLit = "'" + $Global:AjbRepoRoot.Replace("'", "''") + "'"
            $inner = "`$env:AJB_NO_WT_RELAUNCH='1'; `$env:OPAL_WS_ROOT=$rootLit; . $ajbLit; ajb $Serial$extraLit"
            # wt parses `;` as its action-separator -> escape every `;` as `\;`.
            $innerForWt = $inner -replace ';', '\;'
            & wt.exe -w 0 new-tab --title $Serial powershell.exe -NoProfile -NoExit -Command $innerForWt
            Write-Host "[ajb] opened $Serial in a new titled Windows Terminal tab (current window)" -ForegroundColor Cyan
            return
        }
        # No wt.exe on PATH -> fall through to the in-tab OSC best-effort below.
    }

    # First message: the serial (+ any extra words), then the standing startup
    # directives -- injected so they are mechanical, not reliant on the agent
    # remembering them from org/XXX.md.
    $watcherDirective = "FIRST: run /watcher to self-heal inbox-watcher + broker registration. THEN: org/XXX.md startup protocol."
    $loopDirective = Get-AgentLoopDirective $Serial

    # The seat's statement of what it IS (org/ref/SEAT_ROLES.json), after the watcher line and BEFORE the
    # role text. Any failure: one loud line, and the launch proceeds on the existing text unchanged.
    $statementBlock = ''
    $stmt = Get-SeatStatement $Serial
    if ($stmt.Text) {
        $statementBlock = "$($stmt.Text)`n`n"
    } else {
        Write-Host "SEAT-ROLES: no statement for $Serial ($($stmt.Reason))" -ForegroundColor Red
    }

    if ($Extra) {
        $firstMessage = "$Serial $($Extra -join ' ')`n`n$watcherDirective`n`n$statementBlock$loopDirective"
    } else {
        $firstMessage = "$Serial`n`n$watcherDirective`n`n$statementBlock$loopDirective"
    }

    if ($PrintPrompt) {
        Write-Output $firstMessage
        return
    }

    Write-Host "[ajb] launching $Serial in ajb_workspace ..." -ForegroundColor Cyan

    # Tab title = the serial, so the operator identifies each agent's tab at a
    # glance. OSC 0 + WindowTitle at launch; Windows Terminal must have
    # `suppressApplicationTitle: true` under profiles.defaults for it to stick
    # (claude.exe overwrites runtime titles otherwise).
    $esc = [char]27
    $bel = [char]7
    # A spawn may set a display title (a COO's project code); registration stays $Serial.
    $tabTitle = if ($env:OPAL_TAB_TITLE) { $env:OPAL_TAB_TITLE } else { $Serial }
    [Console]::Write("${esc}]0;${tabTitle}${bel}")
    $Host.UI.RawUI.WindowTitle = $tabTitle

    # Per-process serial -> the PostToolUse telemetry hook attributes this
    # session's tool calls to the right serial even with concurrent agents.
    $env:OPAL_AGENT_SERIAL = $Serial

    # Box identity for every writer that keys a per-box file on $AGENTBUS_DEVICE (the override audit log among them,
    # CTO~Z ruling msg 33351). A session started before the persisted user value existed never inherited it and wrote the
    # legacy shared log. Derived from the persisted value, never typed; an env value already set wins.
    if (-not $env:AGENTBUS_DEVICE) {
        $persistedDevice = [Environment]::GetEnvironmentVariable('AGENTBUS_DEVICE', 'User')
        if ($persistedDevice) { $env:AGENTBUS_DEVICE = $persistedDevice.Trim() }
        else { Write-Host "[ajb] WARN: AGENTBUS_DEVICE is unset in the env and the user setting; per-box logs fall back to the shared file." -ForegroundColor Yellow }
    }

    Push-Location $ws
    try {
        # --dangerously-skip-permissions: fully hands-free -- no folder-trust
        # prompt, no per-tool permission stall; an autonomously-spawned agent
        # must never hang on a prompt. This disables the permission LAYER only;
        # CLAUDE.md non-negotiables stay git-hook + wrapper enforced.
        $claudeArgs = @('--dangerously-skip-permissions')
        # Per-serial model/effort defaults. Keyed on BASE serial so lanes
        # inherit. Extend ONLY on Andrew's word.
        #
        # PRECEDENCE: this EXPLICIT table wins over the tier rule below, so a
        # named seat can always be pinned against the tier default.
        $modelBySerial = @{
            '0.0.3_BG_BBGTerminal' = @('--model', 'claude-opus-5', '--effort', 'high')
        }
        # TIER-2 DEFAULT -- Andrew-direct 2026-08-24 ~19:5xZ at the CTO~Z terminal, VERBATIM:
        #   "For future reference, tier2 agents should always be instantiated with opus 5 model
        #    on extra high effort."
        # ("extra high" = the harness effort vocab's `xhigh`: low|medium|high|xhigh|max.)
        #
        # DERIVED FROM THE SERIAL, NOT ENUMERATED, and the grammar is ORG_CHART.md:12-14's own:
        #     0.0.0        Tier 0 (MSTR)
        #     0.0.N  N>0   Tier 0 UTILITY (BG / UA)      <- NOT tier 2
        #     0.Y.0  Y>0   TIER 2 (Senior)               <- his rule lands here
        #     0.Y.Z  Y>0,Z>0  Tier 3 (Junior, RD)        <- ADDED 2026-08-26, see below
        #     N.0.0  N>0   Tier 1 (SA: CTO/COO/CVO/CRO)  <- NOT named by his word
        # WHY DERIVED: he said "ALWAYS". An enumerated list of today's tier-2 serials silently
        # omits the next one minted -- the stale-hand-copied-list class this estate keeps paying
        # for. The numeric triple already encodes tier, so deriving makes a new tier-2 seat
        # inherit the rule by construction, with no edit and no one remembering.
        # SCOPE: TIER 3 ADDED 2026-08-26 by Andrew-direct, asked and answered explicitly -- not
        # inferred. The 08-24 word said "tier2"; 0.6.2_AE_PartnerETL~A is Tier 3 by ORG_CHART
        # grammar and came up without the default while four Tier-2 peers had it. TIER 1 IS
        # STILL NOT WIDENED INTO -- he was offered that option and did not take it.
        # MODEL POLICY MP-20261010 (Andrew-direct 2026-10-10; org/ref/MODEL_POLICY.json, reader
        # .tools/model-policy.ps1). On a TREATMENT device a serial matching a role takes the policy's
        # model/effort and SKIPS the pre-policy table and tier rule below; on a control device, or for
        # an unmatched serial, those apply unchanged. An explicit -Model/-Effort still wins: the policy
        # then adds nothing, so claude never sees two --model flags.
        . (Join-Path $PSScriptRoot 'model-policy.ps1')
        $mp = Get-OpalModelPolicy -Serial $Serial
        if ($mp -and -not $Model -and -not $Effort) {
            $claudeArgs += @('--model', $mp.Model, '--effort', $mp.Effort)
            Write-Host "[ajb] $($mp.PolicyId) $($mp.Role) on $($mp.Device) for ${base}: --model $($mp.Model) --effort $($mp.Effort)" -ForegroundColor Cyan
        }
        elseif ($mp) {
            Write-Host "[ajb] $($mp.PolicyId): explicit -Model/-Effort given for ${base}; policy $($mp.Role) not applied (override)" -ForegroundColor Yellow
        }
        elseif ($modelBySerial.ContainsKey($base)) {
            $claudeArgs += $modelBySerial[$base]
            Write-Host "[ajb] model default for ${base}: $($modelBySerial[$base] -join ' ')" -ForegroundColor Cyan
        }
        elseif ($base -match '^0\.([1-9][0-9]*)\.[0-9]+_') {
            $tier2 = @('--model', 'claude-opus-5', '--effort', 'xhigh')
            $claudeArgs += $tier2
            Write-Host "[ajb] TIER-2 default for ${base}: $($tier2 -join ' ') (Andrew-direct 2026-08-24)" -ForegroundColor Cyan
        }
        # F8 (Andrew-direct 2026-08-20 "rec approved" @ad2585793c, OPAL_ANALYST.W6-T1): the BG seat's
        # identity is BOUND AT LAUNCH. Its own fence (bg-concierge-gate G1) forbids it the XXX.md A.1
        # session-serial write, so the launcher mints the session id, writes the launch-path MARKER
        # first and the serial file SECOND (a failure between leaves marker-without-serial, which the
        # fence reads as LOUD-CLOSED -- the correct failure), and pins claude to that session id.
        # BG-scoped on purpose: every other seat writes its own serial at A.1.
        if ($base -eq '0.0.3_BG_BBGTerminal') {
            # sec11 S2 (CTO~Z ruling msg 2618, Andrew-direct speed addendum @208a4f3b57): the BG
            # seat's MCP tool schemas load RESIDENT, not deferred -- process-scoped so only the
            # BG child inherits it. auto:25 = defer only past 25% of context (safety valve if a
            # future server bloats the seat); acceptance = a real exchange with zero ToolSearch
            # calls before the ACK. Takes effect at the NEXT BG launch, not the live session.
            $env:ENABLE_TOOL_SEARCH = 'auto:25'
            $bgSid   = [guid]::NewGuid().ToString()
            $sessDir = Join-Path $ws 'org\mcp\sessions'
            New-Item -ItemType Directory -Force -Path $sessDir | Out-Null
            $stamp = (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ')
            [System.IO.File]::WriteAllText((Join-Path $sessDir "$bgSid.launch-path"), "bg-concierge $stamp launcher=ajb.ps1 host=$env:COMPUTERNAME`n")
            [System.IO.File]::WriteAllText((Join-Path $sessDir "$bgSid.serial"), "0.0.3_BG_BBGTerminal`n")
            $claudeArgs += @('--session-id', $bgSid)
            Write-Host "[ajb] F8: BG identity bound at launch -- session $bgSid -> 0.0.3_BG_BBGTerminal (launch-path marker + serial file written)" -ForegroundColor Cyan
            # opal-gateway-bbg is this seat's only (Andrew-direct 2026-10-08 ~17:4xZ at 0.0.0_AB_MSTR~Z, row
            # NFRA_OPLGTW-Z-S67): no longer user-level, so no other session loads the Bloomberg account's sign-in.
            # STRICT set (1.0.0_SA_CTO~Z ruling @e46928ecc8, msg 32189, on Andrew's ~00:4xZ "adjudicated by the CTO
            # internally", record @6938d82aad): the seat loads EXACTLY opal-gateway-bbg, bloomberg, opal-agent-comms,
            # so it never holds Andrew's opalgateway identity. Assembled at launch into the session folder: bbg from
            # .tools/bg-gateway.mcp.json, opal-agent-comms from the repo .mcp.json, bloomberg from ~/.claude.json
            # (never typed into the repo). A missing piece falls back to the additive launch and says so.
            $bgMcp = Join-Path $ws '.tools\bg-gateway.mcp.json'
            $bgSet = [ordered]@{}
            try {
                $bbg = (Get-Content -LiteralPath $bgMcp -Raw | ConvertFrom-Json).mcpServers.'opal-gateway-bbg'
                $comms = (Get-Content -LiteralPath (Join-Path $ws '.mcp.json') -Raw | ConvertFrom-Json).mcpServers.'opal-agent-comms'
                $blp = (Get-Content -LiteralPath (Join-Path $env:USERPROFILE '.claude.json') -Raw | ConvertFrom-Json).mcpServers.bloomberg
                if ($bbg) { $bgSet['opal-gateway-bbg'] = $bbg }
                if ($comms) { $bgSet['opal-agent-comms'] = $comms }
                if ($blp) { $bgSet['bloomberg'] = $blp }
            } catch { Write-Host "[ajb] WARN: BG strict MCP set could not be read: $($_.Exception.Message)" -ForegroundColor Yellow }
            if ($bgSet.Count -eq 3) {
                $bgStrict = Join-Path $sessDir "$bgSid.mcp.json"   # session folder, gitignored (AMENDMENT 1 @6abc00a2d5)
                [System.IO.File]::WriteAllText($bgStrict, (@{ mcpServers = $bgSet } | ConvertTo-Json -Depth 10))
                $claudeArgs += @('--strict-mcp-config', '--mcp-config', $bgStrict)
                Write-Host "[ajb] BG MCP: STRICT, exactly $($bgSet.Keys -join ', ') ($bgStrict)" -ForegroundColor Cyan
            } elseif (Test-Path -LiteralPath $bgMcp) {
                $claudeArgs += @('--mcp-config', $bgMcp)
                Write-Host "[ajb] WARN: BG strict set has $($bgSet.Count) of 3 ($($bgSet.Keys -join ', ')) -- launching ADDITIVE (opalgateway also loads)" -ForegroundColor Yellow
            }
            else { Write-Host "[ajb] WARN: $bgMcp is missing -- the BG seat launches WITHOUT opal-gateway-bbg" -ForegroundColor Yellow }
        }
        # Headless = no user present to answer a fork -> hard-remove the
        # user-BLOCKING tools so an autonomous agent can never strand on an
        # unanswerable prompt. Exempt by INTERACTIVITY, not identity. The
        # plan-mode tools go as a PAIR (removing Exit alone strands an agent
        # stuck in plan mode). A headless agent routes decisions to its exec
        # via the broker instead.
        if ($Headless) {
            $claudeArgs += @('--disallowedTools', 'AskUserQuestion', 'EnterPlanMode', 'ExitPlanMode')
        }
        if (-not $Headless) {
            $claudeArgs += @('--dangerously-load-development-channels', 'server:opal-agent-comms')
        }
        if ($Model)  { $claudeArgs += @('--model', $Model) }
        if ($Effort) { $claudeArgs += @('--effort', $Effort) }
        $claudeArgs += @('--', $firstMessage)

        # WT raw-commandline new-tabs may not receive the color-capable-terminal
        # signal, so claude auto-detects no-color. Force truecolor; harmless when
        # the terminal is already color-capable.
        $env:FORCE_COLOR = '3'

        & claude @claudeArgs
    } finally {
        Pop-Location
    }
}

# spawn-agent: terminal-global wrapper for .tools\spawn-agent.ps1 (absolute
# path), so `spawn-agent <Serial>` works from any cwd once this file is
# dot-sourced. (Bare `.tools\spawn-agent.ps1` fails from non-workspace cwds --
# PowerShell misreads the leading `.tools` as a module name without `.\`.)
function spawn-agent {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Serial,

        [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
        [string[]]$Extra
    )

    $script = Join-Path $Global:AjbRepoRoot '.tools\spawn-agent.ps1'
    if (-not (Test-Path $script)) {
        Write-Error "spawn-agent: script not found at $script"
        return
    }
    if ($Extra) {
        & $script $Serial @Extra
    } else {
        & $script $Serial
    }
}

# kill-agent: terminal-global wrapper for .tools\kill-agent.ps1 -- MSTR's
# reallocation capability: kill a finished agent's window to release a slot
# under the concurrency cap. Forwards args (Serial or -All, optional -Reason).
function kill-agent {
    [CmdletBinding()]
    param(
        [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
        [string[]]$Args
    )

    $script = Join-Path $Global:AjbRepoRoot '.tools\kill-agent.ps1'
    if (-not (Test-Path $script)) {
        Write-Error "kill-agent: script not found at $script"
        return
    }
    if ($Args) {
        & $script @Args
    } else {
        & $script
    }
}
