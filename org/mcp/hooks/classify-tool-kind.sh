#!/bin/bash
# classify-tool-kind.sh -- canonical TELEMETRY_LIVENESS_FRAMEWORK.md v0.4 §3.2 + §3.3 binding
# Classifies a tool call into one of: work / watcher / upkeep.
#
# CANONICAL SOURCE: org/mcp/hooks/classify-tool-kind.sh (version-controlled)
# INSTALL TARGET:   .tools/hooks/classify-tool-kind.sh (gitignored, copied via install)
#
# CV-B1 binding inside classifier: classifier MAY read tool_input.command for routing,
# but the read happens in-memory and IS NOT echoed anywhere. Returns only the kind tag.

TOOL_NAME="$1"
HOOK_INPUT="$(cat)"

case "${TOOL_NAME}" in
    Bash)
        # §3.3 Bash kind detection
        CMD="$(echo "${HOOK_INPUT}" | jq -r '.tool_input.command // empty')"
        # NOTE: CMD is read here for classification ONLY; never written to jsonl per CV-B1.
        case "${CMD}" in
            *inbox-watch*|*watcher-status*|*kill-orphans*|*cleanup-poller*|*check-inbox*)
                echo "watcher" ;;
            *)
                echo "work" ;;
        esac
        ;;
    Read|Write|Edit|MultiEdit|NotebookEdit|Grep|Glob)
        echo "work" ;;
    WebFetch|WebSearch|Agent|RemoteTrigger|AskUserQuestion|SendUserFile|ShareOnboardingGuide)
        echo "work" ;;
    Skill)
        SKILL_NAME="$(echo "${HOOK_INPUT}" | jq -r '.tool_input.skill // empty')"
        case "${SKILL_NAME}" in
            watcher) echo "watcher" ;;
            *)       echo "work" ;;
        esac
        ;;
    ToolSearch|TaskCreate|TaskUpdate|TaskGet|TaskList|TaskStop|TaskOutput|TaskRead)
        echo "upkeep" ;;
    ScheduleWakeup|CronCreate|CronDelete|CronList|Monitor|PushNotification)
        echo "upkeep" ;;
    EnterPlanMode|ExitPlanMode|EnterWorktree|ExitWorktree)
        echo "upkeep" ;;
    ListMcpResourcesTool|ReadMcpResourceTool)
        echo "upkeep" ;;
    mcp__opal-agent-comms__send_message|mcp__opal-agent-comms__read_agent_latest_log|mcp__opal-agent-comms__query_project)
        echo "work" ;;
    mcp__opal-agent-comms__register_agent|mcp__opal-agent-comms__heartbeat)
        echo "upkeep" ;;
    mcp__opal-agent-comms__get_agent_status|mcp__opal-agent-comms__check_inbox|mcp__opal-agent-comms__get_live_agents|mcp__opal-agent-comms__get_org_summary|mcp__opal-agent-comms__list_agents|mcp__opal-agent-comms__list_task_orders)
        echo "upkeep" ;;
    mcp__opal-agent-comms__set_summary|mcp__opal-agent-comms__deregister_agent|mcp__opal-agent-comms__deregister_all_stale)
        echo "upkeep" ;;
    *)
        echo "work" ;;
esac
