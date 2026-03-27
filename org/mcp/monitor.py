"""
Opal Broker Monitor — Live telemetry feed for the agent broker.

Renders a continuously-updating terminal display showing:
  - Connected agents with liveness, PIDs, and work summaries
  - Message queue (pending deliveries)
  - Live event stream (registrations, messages, deliveries, disconnects)
  - Broker uptime and throughput stats

Usage:
  python org/mcp/monitor.py              # default: poll every 2s
  python org/mcp/monitor.py --interval 1 # poll every 1s
  python org/mcp/monitor.py --events-only # show only the event stream
  python org/mcp/monitor.py --no-clear    # append mode (no screen clear)
  python org/mcp/monitor.py --pod 4      # filter to Pod 4 agents + CTO/COO
  python org/mcp/monitor.py --project ADVI_MVPLVL  # filter events by project code

Designed for a dedicated PowerShell/terminal window alongside Claude Code sessions.
Ctrl+C to exit.
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

BROKER_PORT = int(os.environ.get("OPAL_BROKER_PORT", "7800"))
BROKER_URL = f"http://127.0.0.1:{BROKER_PORT}"

# Tier 1 serials always pass pod filters (CTO/COO span all pods)
TIER1_PREFIXES = ("1.0.0_", "2.0.0_")


def _serial_matches_pod(serial: str, pod: int | None) -> bool:
    """Check if an agent serial belongs to a pod (or is Tier 1)."""
    if pod is None:
        return True
    # Tier 1 agents (CTO, COO) are in all pods
    if serial.startswith(TIER1_PREFIXES):
        return True
    # Pod is encoded in the first segment: 0.{pod}.0_*
    try:
        parts = serial.split("_", 1)[0].split(".")
        return int(parts[1]) == pod
    except (IndexError, ValueError):
        return True  # unknown format, include by default


def _event_matches_project(event: dict, project: str | None) -> bool:
    """Check if an event's detail references a project code."""
    if project is None:
        return True
    detail = event.get("detail", "")
    subject = event.get("subject", "")
    # Check if the project code appears in the event detail or subject
    return project.lower() in detail.lower() or project.lower() in subject.lower()

# ---------------------------------------------------------------------------
# Terminal helpers
# ---------------------------------------------------------------------------

def clear_screen():
    os.system("cls" if sys.platform == "win32" else "clear")


def _fetch_json(path: str, timeout: float = 3.0):
    """GET JSON from broker."""
    try:
        req = urllib.request.Request(f"{BROKER_URL}{path}")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except Exception:
        return None


def _format_elapsed(seconds: int) -> str:
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        return f"{seconds // 60}m {seconds % 60}s"
    else:
        h = seconds // 3600
        m = (seconds % 3600) // 60
        return f"{h}h {m}m"


def _format_ts(iso_ts: str) -> str:
    """Extract HH:MM:SS from ISO timestamp."""
    try:
        if "T" in iso_ts:
            time_part = iso_ts.split("T")[1]
            return time_part[:8]
    except Exception:
        pass
    return iso_ts[:19]


# ---------------------------------------------------------------------------
# Event type styling
# ---------------------------------------------------------------------------

EVENT_ICONS = {
    "register":     ">>",
    "unregister":   "<<",
    "agent_stale":  "XX",
    "message":      "->",
    "deliver":      "OK",
    "summary":      "..",
    "broker_start": "UP",
    "broker_stop":  "DN",
}


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------

def render_full(status: dict, events: list, last_event_id: int,
                pod: int | None = None, project: str | None = None):
    """Render the full dashboard view with optional pod/project filtering."""
    now = datetime.now(timezone.utc).strftime("%H:%M:%S")
    uptime = _format_elapsed(status.get("uptime_s", 0))

    # Build filter label
    filter_parts = []
    if pod is not None:
        filter_parts.append(f"pod {pod}")
    if project:
        filter_parts.append(project)
    filter_label = f"  |  filter: {', '.join(filter_parts)}" if filter_parts else ""

    lines = []
    lines.append(f"  OPAL BROKER MONITOR  |  {now} UTC  |  uptime {uptime}  |  port {BROKER_PORT}{filter_label}")
    lines.append("=" * 78)

    # Agents section (filtered by pod)
    all_agents = status.get("agents", [])
    agents = [a for a in all_agents if _serial_matches_pod(a["serial"], pod)]
    hidden = len(all_agents) - len(agents)

    label = f"  AGENTS ({len(agents)} shown"
    if hidden:
        label += f", {hidden} filtered"
    label += ")"
    lines.append("")
    lines.append(label)
    lines.append("  " + "-" * 74)

    if agents:
        for a in agents:
            alive = "LIVE" if a.get("alive") else "DEAD"
            elapsed = _format_elapsed(a.get("elapsed_s", 0))
            serial = a["serial"]
            pid = a.get("pid", "?")
            summary = a.get("summary", "")

            lines.append(f"  [{alive:4s}]  {serial:<35s}  PID {pid:<6}  {elapsed:>6s} ago")
            if summary:
                lines.append(f"          {summary[:68]}")
    else:
        lines.append("  (none)")

    # Queue section (filtered by pod — show messages where either party matches)
    all_queue = status.get("queue", [])
    queue = [m for m in all_queue
             if _serial_matches_pod(m.get("from_serial", ""), pod)
             or _serial_matches_pod(m.get("to_serial", ""), pod)]
    lines.append("")
    lines.append(f"  PENDING QUEUE ({len(queue)} message{'s' if len(queue) != 1 else ''})")
    lines.append("  " + "-" * 74)

    if queue:
        for msg in queue[:10]:
            ts = _format_ts(msg.get("sent_at", ""))
            subj = msg.get("subject", "")[:30]
            lines.append(f"  {ts}  {msg['from_serial']} -> {msg['to_serial']}  [{subj}]")
        if len(queue) > 10:
            lines.append(f"  ... and {len(queue) - 10} more")
    else:
        lines.append("  (empty)")

    # Event stream (filtered by pod + project)
    filtered_events = events
    if pod is not None:
        filtered_events = [e for e in filtered_events
                           if _serial_matches_pod(e.get("agent", ""), pod)
                           or e.get("event_type", "") in ("broker_start", "broker_stop")]
    if project:
        # For project filter, only filter message/deliver events (not registrations)
        filtered_events = [e for e in filtered_events
                           if e.get("event_type", "") in ("register", "unregister", "agent_stale",
                                                           "summary", "broker_start", "broker_stop")
                           or _event_matches_project(e, project)]

    lines.append("")
    lines.append("  EVENT STREAM")
    lines.append("  " + "-" * 74)

    if filtered_events:
        for ev in filtered_events[-20:]:
            ts = _format_ts(ev.get("ts", ""))
            etype = ev.get("event_type", "?")
            icon = EVENT_ICONS.get(etype, "  ")
            agent = ev.get("agent", "")
            detail = ev.get("detail", "")

            agent_str = f" {agent}" if agent else ""
            detail_str = f"  {detail[:50]}" if detail else ""
            lines.append(f"  {ts}  {icon}{agent_str}{detail_str}")
    else:
        lines.append("  (no events)")

    lines.append("")
    lines.append("  Ctrl+C to exit")

    return "\n".join(lines)


def render_events_only(events: list):
    """Render just new events as they arrive (append mode)."""
    lines = []
    for ev in events:
        ts = _format_ts(ev.get("ts", ""))
        etype = ev.get("event_type", "?")
        icon = EVENT_ICONS.get(etype, "  ")
        agent = ev.get("agent", "")
        detail = ev.get("detail", "")

        agent_str = f" {agent}" if agent else ""
        detail_str = f"  {detail}" if detail else ""
        lines.append(f"[{ts}] {icon}{agent_str}{detail_str}")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Opal Broker Monitor")
    parser.add_argument("--interval", type=float, default=2.0, help="Poll interval in seconds (default: 2)")
    parser.add_argument("--events-only", action="store_true", help="Show only the event stream (append mode)")
    parser.add_argument("--no-clear", action="store_true", help="Don't clear screen between refreshes")
    parser.add_argument("--pod", type=int, default=None, help="Filter to a specific pod number (e.g., --pod 4). CTO/COO always shown.")
    parser.add_argument("--project", type=str, default=None, help="Filter events by project code (e.g., --project ADVI_MVPLVL)")
    args = parser.parse_args()

    last_event_id = 0
    all_events = []  # running buffer for full-screen mode

    # Initial header for events-only mode
    if args.events_only:
        filter_str = ""
        if args.pod is not None:
            filter_str += f"  |  pod {args.pod}"
        if args.project:
            filter_str += f"  |  project {args.project}"
        print(f"OPAL BROKER EVENT STREAM  |  polling every {args.interval}s  |  port {BROKER_PORT}{filter_str}")
        print("=" * 78)
        print("Waiting for events... (Ctrl+C to exit)")
        print()

    try:
        while True:
            # Check broker health
            health = _fetch_json("/health")
            if not health:
                if not args.events_only and not args.no_clear:
                    clear_screen()
                    print(f"  OPAL BROKER MONITOR  |  Broker not reachable at {BROKER_URL}")
                    print(f"  Retrying in {args.interval}s... (Ctrl+C to exit)")
                elif args.events_only:
                    pass  # silent retry
                else:
                    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}] Broker not reachable")
                time.sleep(args.interval)
                continue

            # Fetch new events
            new_events = _fetch_json(f"/events?since_id={last_event_id}") or []
            if new_events:
                last_event_id = max(ev["id"] for ev in new_events)
                all_events.extend(new_events)
                # Keep buffer bounded
                if len(all_events) > 100:
                    all_events = all_events[-100:]

            if args.events_only:
                # Append mode: only print new events (filtered)
                filtered = new_events
                if args.pod is not None:
                    filtered = [e for e in filtered
                                if _serial_matches_pod(e.get("agent", ""), args.pod)
                                or e.get("event_type", "") in ("broker_start", "broker_stop")]
                if args.project:
                    filtered = [e for e in filtered
                                if e.get("event_type", "") in ("register", "unregister", "agent_stale",
                                                                "summary", "broker_start", "broker_stop")
                                or _event_matches_project(e, args.project)]
                if filtered:
                    print(render_events_only(filtered))
            else:
                # Full dashboard mode
                status = _fetch_json("/status") or {}

                output = render_full(status, all_events, last_event_id,
                                     pod=args.pod, project=args.project)
                if not args.no_clear:
                    clear_screen()
                print(output)

            time.sleep(args.interval)

    except KeyboardInterrupt:
        print("\nMonitor stopped.")


if __name__ == "__main__":
    main()
