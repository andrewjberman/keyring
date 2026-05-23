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

    $ws = 'C:\Users\AndrewBerman\Desktop\ajb_workspace'
    if (-not (Test-Path $ws)) {
        Write-Error "ajb: ajb_workspace not found at $ws"
        return
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
    $watcherDirective = "FIRST, run the /watcher skill to self-heal your inbox-watcher + broker registration (Andrew global ruling 2026-05-22 -- every agent runs /watcher at startup). THEN proceed with the org/XXX.md startup protocol."
    if ($Extra) {
        $firstMessage = "$Serial $($Extra -join ' ')`n`n$watcherDirective"
    } else {
        $firstMessage = "$Serial`n`n$watcherDirective"
    }

    Write-Host "[ajb] launching $Serial in ajb_workspace ..." -ForegroundColor Cyan

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
        if (-not $Headless) {
            $claudeArgs += @('--dangerously-load-development-channels', 'server:opal-agent-comms')
        }
        $claudeArgs += @('--', $firstMessage)

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
