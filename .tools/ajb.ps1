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
        # --dangerously-load-development-channels enables the opal-agent-comms
        # MCP push channel (instant inter-agent message delivery). The `--`
        # terminates the greedy channel-list parse so $firstMessage is the first
        # user message, not another channel entry.
        claude --dangerously-skip-permissions --dangerously-load-development-channels server:opal-agent-comms -- $firstMessage
    } finally {
        Pop-Location
    }
}
