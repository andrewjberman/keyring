# ajb.ps1 -- instant Opal-agent launcher for ajb_workspace (PowerShell).
#
# Ported from corporeal's mcp_runner/launch-agent.sh, adapted for ajb_workspace:
#   - The agent self-identifies from the first message and registers via
#     register_agent(). The launcher drops `claude` into the workspace with the
#     serial as the opening message.
#   - It ALSO sets $env:OPAL_AGENT_SERIAL so the PostToolUse telemetry hook
#     (.tools/hooks/post-tool-telemetry.sh -> org/mcp/agent_telemetry/<serial>.jsonl)
#     attributes this session's tool calls correctly. The hook can fall back to
#     .comp-graph/.agent_context, but that file is shared across the workspace --
#     the per-process env var is what makes attribution correct when several
#     agents run concurrently. Launching via ajb is the clean way to get it.
#
# SETUP (one time): dot-source this from your PowerShell profile so `ajb`
# is always available. Add this line to $PROFILE:
#
#   . "C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\ajb.ps1"
#
# (Open the profile with:  notepad $PROFILE   -- create it if it does not exist.)
# To use it immediately in the current session without editing the profile,
# just run that same dot-source line once.
#
# USAGE:
#   ajb <Serial>                 launch an agent; first message = the serial
#   ajb <Serial> <extra words>   first message = serial + the extra text
#
# EXAMPLES:
#   ajb 2.0.0_SA_COO
#   ajb 1.0.0_SA_CTO
#   ajb 0.4.0_DE_ClientPlatform
#   ajb 0.4.0_DS_ClientPlatform~B
#   ajb 2.0.0_SA_COO "/loop ADVI"
#
# WHAT IT DOES:
#   1. Validates a serial was given.
#   2. cd's into the ajb_workspace root (so .mcp.json + CLAUDE.md load).
#   3. Launches `claude` --dangerously-skip-permissions (fully hands-free: no
#      folder-trust prompt, no mid-session per-tool permission stall, so an
#      autonomously-spawned agent never hangs) with the opal-agent-comms
#      development channel enabled (MCP push -- instant inter-agent delivery)
#      and the serial as the first user message. The agent self-identifies,
#      reads CLAUDE.md -> org/XXX.md, and runs the startup protocol.
#   4. Injects an Andrew global ruling (2026-05-22) into the first message:
#      every agent runs the /watcher skill at startup to self-heal its
#      inbox-watcher + broker registration before anything else.

# Get-AgentLoopDirective: serial -> role-specific CronCreate directive string,
# baked into the launcher first-message so canonical loops are armed
# deterministically at every launch (LD-0082).
#
# Tilde-lane suffixes (~B/~C/~D/~E) are stripped for role detection; lane
# variants share the same role + loop set as the base serial.
#
# SUPERSESSION (LD-0157 2026-06-05 + LD-0164/LD-0166 2026-06-06..08 + LD-0175 2026-06-10, Andrew direct):
# the LD-0082 self-tick loop set below is RETIRED. The fabric is now fully event-driven
# (persistent inbox Monitor) with ZERO loops armed at launch (LD-0175, Andrew direct:
# "I don't want any loops initiated at launch ... if I want a loop to run, I will
# initiate the looped skill").
#
# SUPERSESSION-2 (LD-0288/0289/0293, Andrew-direct 2026-07-13/14): the COO /drive
# auto-arm carve-out (LD-0204, 2026-06-18) is RETRACTED and was DELETED from org/XXX.md
# at 014de1937. THERE IS NOW NO STANDING EXCEPTION TO THE ZERO-CRONS RULE -- not even the
# COO's. The COO coordinates and routes; he does not re-drive the estate.
#   >> THIS LAUNCHER ENFORCED THE RETRACTED CARVE-OUT FOR ~2 DAYS AFTER ITS DELETION
#   >> (found 2026-07-16 ~14:4xZ by 2.0.0_SA_COO, whose own launch prompt cited the dead
#   >> LD-0204 as live authority). A RETRACTED RULE IS ONLY AS DEAD AS ITS LAST-SURVIVING
#   >> COPY: deleting it from XXX.md did not delete it here, and this file is what a fresh
#   >> session reads FIRST. Same class as 0.4.0_DS's prompt.md retracted-hold correction
#   >> (454c816ec). Do not re-add a loop carve-out here from memory or an older copy.
#
# DESIGN RULE (why this file no longer names a cadence): a SCOPED, TIME-BOUNDED loop
# authorization lives ONLY in the org/XXX.md Step 1b-F role row, which carries its stop
# condition and its date. If this launcher hardcoded one, it would keep arming the loop
# after the authorization expired -- re-acquiring the exact bug above. The launcher states
# the standing law and DEFERS; XXX.md 1b-F is the single source of truth.
#
# Per-role posture now:
#   - /watcher: arm-at-load ONCE, NOT a cron (LD-0166). No serial arms a /watcher cron.
#   - /work (all workers) + /ws-charter (ws CTO): RETIRED to ad-hoc (LD-0157).
#   - /drive (COO): NOT auto-armed. OFF by default (LD-0288/0289/0293). Any live scoped
#     authorization is read from org/XXX.md 1b-F at startup, honored to its stop
#     condition, and turned off when that condition reads true.
#   - /mstr-review (MSTR) + /spot-check (both CVOs): RETIRED to ad-hoc (LD-0164).
#   - /cl-charter (CL CTO) + /verify-channel (both CVOs) + /case-find (CL CVO):
#     RETIRED to ad-hoc (LD-0175).
#   - Standing crons armed at launch: NONE, for every serial. Every loop is
#     Andrew/operator-initiated on demand; skills retain their loop bodies when invoked.
#   - Workers announce blocks via broker STATUS (WORKING:/IDLE:/BLOCKED:), NOT a
#     [BLOCKED-ASK] polling-announce. THERE IS NO CENTRALIZED TICK: blocked-agent
#     discovery is event-driven, and COO/CTO run /fabric-check + /stimulus-scan ad hoc,
#     on signals rather than on a timer.
# Original LD-0082 design notes (historical): Q1 per-skill CronCreate; Q2 /watcher
# cron for MSTR+COO; Q3 /stimulus-scan retired; Q4 /verify-channel 2h; Q5 /case-find
# chains /case-mgmt; Q6 /comp-ferry event-triggered; Q7 /work 20m uniform.
function Get-AgentLoopDirective {
    [CmdletBinding()]
    param([Parameter(Mandatory=$true)] [string]$Serial)

    # Strip tilde-lane suffix for role detection.
    $base = $Serial -replace '~[A-Za-z0-9]+$', ''

    $header = "Loop arming (LD-0157/0164/0166/0175 + LD-0288/0289/0293 -- ALL self-tick loops retired; EVERY serial arms ZERO crons at launch, INCLUDING the COO: there is no standing exception. /watcher arms ONCE at load and is NOT a loop. A SCOPED, TIME-BOUNDED loop authorization (if one is live) is recorded in org/XXX.md Step 1b-F -- that row is the ONLY source of truth; this launcher never carries one):"

    switch -Regex ($base) {
        '^0\.0\.0_AB_MSTR$' {
            return "$header`n  MSTR -- arms ZERO crons (LD-0164 + LD-0166).`n  1. Run /watcher ONCE (arm-at-load; no /watcher cron).`n  2. Run /mstr-review ONCE at startup as an ad-hoc pass (LD-0164 -- no 12h cron).`n  Event-triggered: /mstr-spawn, /mstr-kill, /mstr-charter, /comp-ferry, /govern (Andrew-discretion, LD-0147), embedded LD ratification."
        }
        '^1\.0\.0_SA_CTO$' {
            return "$header`n  ws CTO -- arms ZERO crons (LD-0157).`n  1. Run /watcher ONCE (arm-at-load).`n  /ws-charter is AD-HOC -- run it when you have charter work, not as a loop. Event-driven: Andrew directives + CVO findings via the Monitor. THERE IS NO CENTRALIZED TICK -- /drive is OFF by standing order (LD-0288/0289/0293); run /fabric-check + /stimulus-scan ad hoc, on signals, not on a timer. Event-triggered: REPAIR-AMENDMENT scribes (gated on CVO finding)."
        }
        '^1\.1\.0_SA_CTO$' {
            return "$header`n  CL CTO -- arms ZERO crons (LD-0175, Andrew direct 2026-06-10).`n  1. Run /watcher ONCE (arm-at-load).`n  /cl-charter is AD-HOC -- run it when you have CL charter / queue-pull work, not as a launch loop. Event-driven: CL queue items + Andrew directives via the Monitor. If a stale /cl-charter cron exists from a prior session, CronList->CronDelete it."
        }
        '^2\.[01]\.0_SA_COO$' {
            return "$header`n  COO -- arms ZERO crons (LD-0288/0289/0293, Andrew-direct standing). /drive is OFF by default. The COO COORDINATES and ROUTES; he does NOT re-drive the estate, and the old 'PRIMARY OPERATIONAL DRIVER' auto-arm carve-out (LD-0204) was DELETED from org/XXX.md at 014de1937 -- do not reinstate it from memory or from an older launcher/prompt copy.`n  1. Run /watcher ONCE (arm-at-load; no /watcher cron -- LD-0166).`n  2. DO NOT arm /drive from this launcher. READ the org/XXX.md Step 1b-F COO row: if a SCOPED, TIME-BOUNDED /drive authorization is live there, it states its own cadence AND its stop condition -- honor both, and turn /drive OFF the moment the stop condition reads true. If that row carries no live scoped authorization, arm nothing.`n  WHY THIS IS NOT A NICETY: /drive's own gate treats 'all standing by' as a GATE FAILURE, so it is structurally unable to conclude 'dispatch nothing'. Armed during a dispatch hold it is obligated to break the hold on a timer, reasoning correctly from a stale mandate. Dispatch authority during a hold belongs to the GO-issuing owner, never to a timer."
        }
        '^3\.0\.0_SA_CVO$' {
            return "$header`n  ws CVO -- arms ZERO crons (LD-0175, Andrew direct 2026-06-10; /spot-check + /verify-channel both AD-HOC).`n  1. Run /watcher ONCE (arm-at-load).`n  2. MAIN-fabric verify ONLY (LD-0325 restructure, 2026-07-20): PORTAL_AUTHHARD W2+, smartx first-conversion, MDPF 49F parity, general main-fabric closeout verify. SYSPARITY IS NOT YOURS -- LD-0318/0319 ('verify parity FIRST' + the 30-min cron) MOVED to 3.0.0_SA_CVO~Z. Do NOT arm the SYSPARITY cron and do NOT adopt 'verify parity FIRST' on load. XXX.md 1b-F base-CVO row + LD-0325 are authoritative over any older launcher/prompt copy that says otherwise.`n  /verify-channel + /spot-check: run on-demand / at closeout-class signals -- NOT a launch cron. If a stale /verify-channel or /spot-check cron exists from a prior session, CronList->CronDelete it."
        }
        '^3\.1\.0_SA_CVO$' {
            return "$header`n  CL CVO -- arms ZERO crons (LD-0175, Andrew direct 2026-06-10; /spot-check + /verify-channel + /case-find all AD-HOC).`n  1. Run /watcher ONCE (arm-at-load).`n  /verify-channel + /case-find + /spot-check: run on-demand -- NOT launch crons. If a stale cron for any exists from a prior session, CronList->CronDelete it."
        }
        '^0\.[0-9]+\.[0-9]+_AE_CloudOps(~[A-Za-z0-9]+)?$' {
            return "$header`n  AE_CloudOps lane (ws fabric) -- arms ZERO crons (LD-0157; event-driven).`n  0. FIRST after /watcher: invoke /cloud-ops once to load operational reference + permissions profile + current CLAUDE.md Rules 1-19 cross-reference + LD-cycle pointers + pipeline/bucket/secrets/KMS inventory (skill at .claude/skills/cloud-ops/SKILL.md). Not a cron -- session-orient one-shot.`n  1. Run /watcher ONCE (arm-at-load).`n  Event-driven: act on Monitor-delivered TOs; keep broker STATUS accurate (WORKING:/IDLE:/BLOCKED:) so COO/CTO find blocks (escalate blockers by MCP too -- /drive is OFF by standing order, so there is no timer that will come find you). /work is AD-HOC (off-cycle pass if useful)."
        }
        '^0\.8\.0_AE_CloudComp(~[A-Za-z0-9]+)?$' {
            return "$header`n  AE_CloudComp lane (ws fabric tester for CL compiler tools) -- arms ZERO crons (LD-0157; event-driven).`n  0. FIRST after /watcher: invoke /cloud-ops once to load operational reference (you do cloud-ops-class work testing compilers on real ws workload).`n  1. Run /watcher ONCE (arm-at-load).`n  Event-driven: act on Monitor-delivered TOs; keep broker STATUS accurate so COO/CTO find blocks (escalate blockers by MCP too -- /drive is OFF by standing order, so there is no timer that will come find you). /work is AD-HOC. Read MSTR queue at org/mcp/comp_ferry_queue.json for ferry test scheduling context."
        }
        '^0\.[0-9]+\.[0-9]+_(DS|AE|DE|DT|RD)_' {
            return "$header`n  Tier-2/3 worker (ws fabric) -- arms ZERO crons (LD-0157; event-driven).`n  1. Run /watcher ONCE (arm-at-load).`n  Event-driven: act on Monitor-delivered dispatches/TOs as they arrive; keep broker STATUS accurate (WORKING:/IDLE:/BLOCKED:) so COO/CTO find blocks (escalate blockers by MCP too -- /drive is OFF by standing order, so there is no timer that will come find you). /work is AD-HOC (off-cycle pass if useful)."
        }
        '^1\.[0-9]+\.[0-9]+_DS_CompLearns(~[A-Za-z0-9]+)?$' {
            return "$header`n  CL Tier-2 DS (CompLearns) -- arms ZERO crons (LD-0157; event-driven).`n  1. Run /watcher ONCE (arm-at-load).`n  Event-driven: act on Monitor-delivered TOs; keep broker STATUS accurate so CL COO finds blocks. /work is AD-HOC."
        }
        '^2\.1\.0_SC_CompLearns(~[A-Za-z0-9]+)?$' {
            return "$header`n  CL Tier-2 SC (CompLearns) -- arms ZERO crons (LD-0157; event-driven).`n  1. Run /watcher ONCE (arm-at-load).`n  Event-driven: act on Monitor-delivered TOs; keep broker STATUS accurate so CL COO finds blocks. /work is AD-HOC."
        }
        '^0\.0\.[0-9]+_UA_' {
            return "$header`n  Tier-0 Utility Agent (UA) -- principal-facing tool surface (LD-0220, 2026-06-26). Arms ZERO crons; pre-armed via its launcher skills.`n  1. Run /watcher ONCE (arm-at-load).`n  2. Run the launcher skill(s) in your prompt.md 'On Launch' section (e.g. mstools arms /teams-assist; awstools arms its portal/AWS read tools) so your toolset is live the moment you launch.`n  Event-driven + on-demand: act on Monitor-delivered notifications; draft-and-ask on anything outward-facing/irreversible; not part of the PRD->TO dispatch hierarchy. Identity/brief: org/tier0_utility/$base/."
        }
        default {
            return "$header`n  UNRECOGNIZED ('$Serial' matched no role pattern)`n  1. Run /watcher ONCE (arm-at-load).`n  WARN MSTR: 'role-mapping gap for $Serial in ajb.ps1'."
        }
    }
}

function ajb {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Serial,

        # -Headless: drop --dangerously-load-development-channels so the agent
        # launches fully hands-free (no Y/N startup confirmation prompt). Used
        # by spawn-agent.ps1 for autonomous MSTR-driven spawns where no human
        # is at the keyboard to clear the prompt. Safe to drop: org/mcp/server.py
        # lines 299-300 confirm Claude Code silently ignores the custom
        # notifications/claude/channel mechanism the flag enables -- current
        # push uses standard MCP send_log_message + piggyback, neither of which
        # requires the flag. Without -Headless, the legacy ad-hoc launch path
        # is unchanged (flag still set, Y prompt still surfaces for the human).
        [switch]$Headless,

        [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
        [string[]]$Extra
    )

    # CL-serial cwd routing per LD-0088 A.1 (Andrew sovereign ratify 5c399a27f
    # + LD-0089 AC1 standing authorization). CL-fabric agents launch in the
    # feature_clb worktree so feature_clb/.claude/skills/ + feature_clb/.mcp.json
    # are the discovered configs; ws-fabric agents launch in ajb_workspace. CL
    # serials enumerated: 1.1.0_SA_CTO + 2.1.0_SA_COO + 3.1.0_SA_CVO + 2.1.0_SC_CompLearns
    # + 1.[1-4].0_DS_CompLearns (matches Get-AgentLoopDirective CL pattern + the
    # owned-paths COMP_LEARNS lane in .owned-paths.yaml).
    $base = $Serial -replace '~[A-Za-z0-9]+$', ''
    if ($env:AJB_FORCE_WS -eq '1') {
        $ws = 'C:\Users\AndrewBerman\Desktop\ajb_workspace'
        Write-Host "[ajb] AJB_FORCE_WS=1 -> ajb_workspace cwd (LD-0088 A.1 bypass; Andrew-direct framework-3 fallback)" -ForegroundColor Yellow
    } else {
        switch -Regex ($base) {
            '^(1\.1\.0_SA_CTO|2\.1\.0_SA_COO|3\.1\.0_SA_CVO|2\.1\.0_SC_CompLearns|1\.[1-4]\.0_DS_CompLearns)$' {
                # feature_clb worktree RETIRED (LD-0222, Andrew-direct 2026-06-29) + CL agents PAUSED.
                # Route CL serials to ws-root as the fallback so a launch does NOT hard-error on the
                # deleted worktree (was: $ws = ...\feature_clb -> Test-Path fail -> Write-Error). The CL
                # serial-routing identity (this case + the pattern) is PRESERVED for re-home if CL resumes.
                $ws = 'C:\Users\AndrewBerman\Desktop\ajb_workspace'
                Write-Host "[ajb] CL worktree RETIRED (LD-0222); CL paused -> ws-root fallback (re-home TBD)" -ForegroundColor Yellow
            }
            default {
                $ws = 'C:\Users\AndrewBerman\Desktop\ajb_workspace'
            }
        }
    }
    if (-not (Test-Path $ws)) {
        Write-Error "ajb: workspace not found at $ws"
        return
    }

    # RELIABLE TAB TITLE for MANUAL launches (Andrew direct 2026-06-11).
    # Problem: when `ajb <Serial>` is typed in an EXISTING Windows Terminal tab,
    # the in-tab title set below (OSC 0 + $Host.UI.RawUI.WindowTitle) does NOT
    # stick -- the user's WT has `suppressApplicationTitle: true`, which makes WT
    # ignore tab-title writes from the running process (PowerShell's OSC included).
    # That same setting is WHY spawn-agent.ps1 works: it sets the title via
    # `wt.exe --title` at tab CREATION (terminal layer), which suppression then
    # protects from claude.exe's runtime title writes. The only mechanism that
    # survives is a creation-time `wt --title`, i.e. a NEW tab.
    #
    # So: when invoked interactively inside Windows Terminal (NOT the -Headless
    # spawn-agent path, NOT an already-relaunched inner call), re-launch this same
    # `ajb <Serial>` in a new titled tab of the CURRENT window (`-w 0`). This
    # mirrors spawn-agent's proven mechanism for the manual case. Outside WT
    # (legacy conhost, ssh) the in-tab OSC path below still works, so we skip the
    # relaunch and fall through. Escape hatch: set $env:AJB_NO_WT_RELAUNCH = '1'
    # to keep claude in the current tab (accepting that the serial won't show
    # under suppressApplicationTitle).
    if (-not $Headless -and $env:WT_SESSION -and $env:AJB_NO_WT_RELAUNCH -ne '1') {
        $wtCmd = Get-Command wt.exe -ErrorAction SilentlyContinue
        if ($wtCmd) {
            $ajbPath = 'C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\ajb.ps1'
            # Quote extras as a single-quoted PS literal so metacharacters in the
            # extra words don't get re-parsed by the inner shell (LD-0078 class).
            $extraLit = ''
            if ($Extra) { $extraLit = " '" + (($Extra -join ' ').Replace("'", "''")) + "'" }
            # Inner command: mark the relaunch so the inner `ajb` doesn't recurse,
            # dot-source ajb.ps1, then run the same ajb invocation in the new tab.
            # Backtick-escape $env: + the inner quotes so the OUTER string doesn't
            # expand them; $Serial + $extraLit DO interpolate (baked in).
            $inner = "`$env:AJB_NO_WT_RELAUNCH='1'; . `"$ajbPath`"; ajb $Serial$extraLit"
            # wt parses `;` as its action-separator -> escape every `;` as `\;`
            # so the whole statement reaches powershell.exe intact.
            $innerForWt = $inner -replace ';', '\;'
            & wt.exe -w 0 new-tab --title $Serial powershell.exe -NoProfile -NoExit -Command $innerForWt
            Write-Host "[ajb] opened $Serial in a new titled Windows Terminal tab (current window)" -ForegroundColor Cyan
            return
        }
        # No wt.exe on PATH -> fall through to the in-tab OSC best-effort below.
    }

    # First message: the bare serial by default. The agent self-identifies from
    # it and runs the org/XXX.md startup protocol (this is exactly how an Opal
    # agent session is opened -- the operator types the serial). Any extra words
    # after the serial are appended (e.g. a /loop directive).
    #
    # GLOBAL RULING (Andrew, 2026-05-22): every agent runs the /watcher skill at
    # session start -- it self-heals the inbox-watcher + broker registration so
    # the agent is never silently deaf to message pushes. The launcher injects
    # the directive into the first message so it is automatic, not reliant on
    # the agent remembering it from org/XXX.md.
    $watcherDirective = "FIRST: run /watcher to self-heal inbox-watcher + broker registration. THEN: org/XXX.md startup protocol."

    # DETERMINISTIC LOOP ARMING (LD-0082): map serial to role; emit CronCreate
    # directives so canonical loops are armed at launch, not relied on the
    # agent reading org/XXX.md and remembering to arm them. XXX.md remains
    # the source of truth; launcher injection guarantees mechanical execution.
    $loopDirective = Get-AgentLoopDirective $Serial

    if ($Extra) {
        $firstMessage = "$Serial $($Extra -join ' ')`n`n$watcherDirective`n`n$loopDirective"
    } else {
        $firstMessage = "$Serial`n`n$watcherDirective`n`n$loopDirective"
    }

    Write-Host "[ajb] launching $Serial in ajb_workspace ..." -ForegroundColor Cyan

    # Set the PowerShell window title to the agent serial so the operator can
    # identify each agent's tab at a glance in Windows Terminal (LD-0079).
    # Applies whether ajb is invoked from spawn-agent.ps1 (autonomous spawn) or
    # typed manually in a fresh terminal -- title gets set in either path.
    #
    # Belt-and-suspenders: emit OSC 0 escape sequence directly via [Console]::Write
    # AND set $Host.UI.RawUI.WindowTitle. Windows Terminal natively binds OSC 0
    # (ESC ] 0 ; TEXT BEL) for tab titles; $Host.UI.RawUI.WindowTitle sets the
    # underlying Win32 console title which WT also reads. claude.exe's console
    # writes may transiently overwrite either path, but the OSC escape is the
    # last-write-wins terminal protocol -- emitting it immediately before
    # `& claude` gives the spawned agent's tab the highest probability of
    # displaying the serial through the session. Andrew direct 2026-05-26
    # "I want their serial in the tab title of powershell by default. When you
    # load 1.0.0_SA_CTO, it should literally display 1.0.0_SA_CTO in the
    # powershell tab of the new window."
    #
    # **STRUCTURAL FIX (2026-05-26 Andrew direct follow-on):** the OSC escape +
    # WindowTitle pair alone was empirically insufficient -- claude.exe issues
    # its own OSC 0/2 sequences during interactive runtime that override the
    # launch-time title. The complete fix REQUIRES Windows Terminal's
    # `suppressApplicationTitle: true` setting under `profiles.defaults` in
    # `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`.
    # With that flag set, WT IGNORES tab-title OSC sequences from running
    # applications AND keeps whatever was set via PowerShell at launch ($Host.UI.RawUI.WindowTitle
    # or OSC emit before the application started). The user-local settings.json
    # edit is one-time + reversible (set flag to false to restore default). This
    # ajb.ps1 launch-time title-set then sticks through the entire session.
    # Verify the setting is present if tab titles fail to display agent serial
    # automatically on a fresh spawn.
    $esc = [char]27
    $bel = [char]7
    [Console]::Write("${esc}]0;${Serial}${bel}")
    $Host.UI.RawUI.WindowTitle = $Serial

    # Per-process serial -> the PostToolUse telemetry hook reads $OPAL_AGENT_SERIAL
    # first (it wins over the shared .comp-graph/.agent_context file), so this
    # session's tool calls land in org/mcp/agent_telemetry/<serial>.jsonl correctly
    # even when other agents share the workspace.
    $env:OPAL_AGENT_SERIAL = $Serial

    Push-Location $ws
    try {
        # --dangerously-skip-permissions: launch fully hands-free -- no
        # folder-trust prompt, no mid-session per-tool permission stall. An
        # autonomously-spawned agent must never hang on a prompt. This disables
        # Claude Code's permission LAYER only; the CLAUDE.md non-negotiables
        # (owned-paths pre-commit, safe-commit, safe-deploy/safe-apply, HALTGT)
        # are git-hook + wrapper enforced and remain fully in force.
        # --dangerously-load-development-channels: legacy flag that surfaces a
        # Y/N startup confirmation prompt. It enabled a custom
        # notifications/claude/channel push mechanism that Claude Code silently
        # ignores (see org/mcp/server.py:299-300). Skipped in -Headless mode so
        # autonomous spawns never stall on the Y prompt.
        $claudeArgs = @('--dangerously-skip-permissions')
        # HEADLESS = no user present to answer a fork -> HARD-REMOVE the user-BLOCKING tools so an
        # autonomous agent can never strand on an unanswerable prompt (the 0.6.1 2026-07-07
        # frozen-user-fork retire). --skip-permissions covers permission prompts, NOT these
        # deliberate user-CHOICE tools. Exempt-by-INTERACTIVITY (a non-headless session keeps them),
        # NOT by identity -- even MSTR, if headless, must not strand. Disable the plan-mode PAIR
        # (Enter+Exit): removing Exit ALONE would strand an agent stuck-in-plan-mode (CTO catch).
        # A headless agent routes decisions to its exec via the broker instead. (CTO-cleared
        # 20260707 w/ 2 refinements: interactivity-not-identity + plan-mode-pair; Andrew-direct.)
        if ($Headless) {
            $claudeArgs += @('--disallowedTools', 'AskUserQuestion', 'EnterPlanMode', 'ExitPlanMode')
        }
        if (-not $Headless) {
            $claudeArgs += @('--dangerously-load-development-channels', 'server:opal-agent-comms')
        }
        $claudeArgs += @('--', $firstMessage)

        # COLOR FIX (MSTR test 2026-07-20, pending CTO~A formalize): WT 1.24 (auto-updated 07-17)
        # stopped handing the color-capable-terminal signal (WT_SESSION) to raw-commandline new-tabs,
        # so Claude Code auto-detects no-color and renders monochrome in spawned windows. Force color
        # on so claude always emits ANSI regardless of terminal auto-detection. Harmless on interactive
        # launches (already color-capable). '3' = truecolor (WT supports it).
        $env:FORCE_COLOR = '3'

        & claude @claudeArgs
    } finally {
        Pop-Location
    }
}

# spawn-agent: terminal-global wrapper that invokes .tools\spawn-agent.ps1 with
# its absolute path. Means you can type `spawn-agent 0.0.0_AB_MSTR` from any
# directory in PowerShell after this file is dot-sourced (typically once via
# $PROFILE -- see top of file). Otherwise the bare `.tools\spawn-agent.ps1`
# form fails from non-workspace cwds because PowerShell's auto-module-load
# misreads the leading `.tools` as a module name unless preceded by `.\`.
function spawn-agent {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory = $true, Position = 0)]
        [string]$Serial,

        [Parameter(Position = 1, ValueFromRemainingArguments = $true)]
        [string[]]$Extra
    )

    $script = 'C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\spawn-agent.ps1'
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

# kill-agent: terminal-global wrapper for .tools\kill-agent.ps1. MSTR's
# reallocation capability -- when an agent's chartered work is done, kill the
# window to release a slot under the 8-process concurrency cap. Forwards args
# (Serial or -All, optional -Reason).
function kill-agent {
    [CmdletBinding()]
    param(
        [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
        [string[]]$Args
    )

    $script = 'C:\Users\AndrewBerman\Desktop\ajb_workspace\.tools\kill-agent.ps1'
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
