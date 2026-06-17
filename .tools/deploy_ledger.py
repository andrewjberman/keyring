#!/usr/bin/env python3
"""deploy_ledger.py -- the deploy-completion ledger contract (TO #5).

ADVI_INFETL.BRONZE-FIX structural #5: every multi-leg deploy OPENS a
change_management ledger entry at deploy-START declaring its COMPLETE
manifest, CLOSES only when every leg carries verification proof, and an
entry left OPEN past its window BLARES (RED inbox delivery to COO).
Enforcement rides COO /drive + fabric-check chaining `check --red` each
cycle -- a half-finished deploy cannot slip past a /drive tick.

NEVER-law anchor: CLAUDE.md "NEVER leave a confirmed deploy half-landed"
(e38cc2b16, Andrew-direct 2026-06-12 after the inf-ADVI P0: one cutover
bundle stranded THREE legs + an invisible FATAL with no structural signal).

Leg kinds (AE 0.6 amendment 2 included):
  git             commit/tag pushed              proof: hash / tag name
  s3-prefix       code landed on a code prefix   proof: the TOOL-03 output
                  line (`comp-pipescript deployed` MATCH row -- machine-
                  greppable, carries bucket attribution; NOT a bare ETag)
  activation      container rebuild / task-def / trigger arm
  ec2-baked-asset on-instance baked copy         proof: SSM cat/md5 of the
                  RUNNING path (S3 ETag is NOT valid proof -- the S3 copy
                  can be current while the baked copy is stale)
  verify          post-deploy live-state check (0-diff plan, smoke, served
                  artifact read)

Usage:
  deploy_ledger.py open  --slug mdpf-vintage --title "..." --author 0.7.0_AE_CloudOps \
      --leg "L1|git|CLOUD commit|hash pushed" --leg "L2|s3-prefix|opal-data-mdpf code/gold|TOOL-03 MATCH line" \
      [--pipeline inf]            # adds the canonical PIPELINE_MAP x VALID_LAYERS
                                  # + AUX_CODE_PREFIXES legs for that firm
      [--window-hours 4]
  deploy_ledger.py close-leg --slug mdpf-vintage --leg-id L2 --proof "<evidence>"
  deploy_ledger.py close     --slug mdpf-vintage        # refuses if any leg unproven
  deploy_ledger.py check [--red] [--window-hours N]     # exit 1 if any entry OPEN
                                  # ALSO sweeps change_management/*.md for an
                                  # OPEN/non-terminal ledger with NO sentinel
                                  # (the false-clean gate-bypass class) -> BYPASS
                                  # line + (--red) RED-to-COO.
  deploy_ledger.py list

CORRELATION-ID TOKEN FORMAT (pinned with DS for BRONZE-FIX #7 interop,
2026-06-12): embed `ssm:<command_id>` and `lock:<run_id>` tokens in --proof
strings when they exist. The #7 FATAL SNS payload carries the SAME tokens, so
a FATAL alert grep-joins to its open ledger entry mechanically.

v1.1 RATCHET LIST (DS contract review 225806Z, non-blocking):
  R1. per-kind proof-shape validation -- s3-prefix proof must match a TOOL-03
      MATCH-line regex; ec2-baked-asset proof must carry an ssm:/md5 token
      (proof quality must not ride culture; this tool exists because culture
      fails).
  R2. AUX['inf'] None-home prefixes (runner/exporter/cleanup) render
      UNCOVERED -- the residual stranded-deploy surface; map repo homes or
      retire the prefixes (small follow-on, AE 0.6 lane interface).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
CM_DIR = WORKSPACE / "org" / "critical_paths" / "change_management"
STATE_DIR = WORKSPACE / "org" / "critical_paths" / ".open_deploys"
COO_INBOX = WORKSPACE / "org" / "mcp" / "inbox" / "2.0.0_SA_COO"
LEG_KINDS = {"git", "s3-prefix", "activation", "ec2-baked-asset", "verify"}
DEFAULT_WINDOW_HOURS = 4.0

# Gate-bypass scan (false-clean hardening 2026-06-17, CTO-author / AE-review /
# COO-track). The sentinel-only `check --red` enumerates ONLY .open_deploys/*.json,
# so a HAND-AUTHORED markdown deploy-completion ledger (no sentinel) is structurally
# INVISIBLE to the gate + auto-RED + COO alert -- the false-clean class (anchor: the
# 2026-06-16 causality teardown ledger was content-complete but unindexed). cmd_check
# now ALSO sweeps the rendered change_management/*.md ledgers for an OPEN/non-terminal
# status carrying NO matching sentinel. A ledger status that LEADS with one of these
# tokens is a terminal (nothing-stranded) state and is skipped.
TERMINAL_STATUS_TOKENS = (
    "CLOSED", "COMPLETE", "DONE", "ROLLBACK", "ROLLED",
    "CANCEL", "SUPERSEDED", "ABANDONED", "RESOLVED", "VOID",
)
# Re-alert suppression for unindexed ledgers (they have no sentinel to carry
# last_red_at). Leading-dot name -> excluded from the STATE_DIR.glob("*.json")
# sentinel enumeration (pathlib `*` skips dotfiles; cmd_check also guards).
UNINDEXED_RED_STATE = STATE_DIR / ".unindexed_red_state.json"


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _ts(dt: datetime | None = None) -> str:
    return (dt or _now()).strftime("%Y%m%dT%H%M%SZ")


def _state_path(slug: str) -> Path:
    return STATE_DIR / f"{slug}.json"


def _load(slug: str) -> dict:
    p = _state_path(slug)
    if not p.exists():
        sys.exit(f"ERROR: no open deploy ledger for slug '{slug}' ({p})")
    return json.loads(p.read_text(encoding="utf-8"))


def _save(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    _state_path(state["slug"]).write_text(
        json.dumps(state, indent=2), encoding="utf-8")


def _render_entry(state: dict) -> str:
    """The human-readable s10.6 change_management entry, regenerated from
    state on every mutation so the .md and the sentinel can never drift."""
    lines = [
        "# Deploy Completion Record",
        f"**Date opened:** {state['opened_at']}",
        f"**Status:** {state['status']}"
        + (f" -- closed {state.get('closed_at')}" if state.get("closed_at") else ""),
        f"**Deploy:** {state['title']}",
        f"**Authored by:** {state['author']}",
        "**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)",
        f"**Window:** {state['window_hours']}h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)",
        "",
        "---",
        "",
        "## Manifest (every leg must carry proof before CLOSE)",
        "",
        "| leg | kind | target | proof required | proof | state |",
        "|---|---|---|---|---|---|",
    ]
    for leg in state["legs"]:
        proof = (leg.get("proof") or "").replace("|", "\\|")
        st = "CLOSED " + (leg.get("closed_at") or "") if leg.get("proof") else "OPEN"
        lines.append(
            f"| {leg['id']} | {leg['kind']} | {leg['target'].replace('|', chr(92) + '|')} "
            f"| {leg['proof_required'].replace('|', chr(92) + '|')} | {proof} | {st} |")
    lines += ["", "## Log", ""]
    for ev in state.get("log", []):
        lines.append(f"- {ev}")
    lines.append("")
    return "\n".join(lines)


def _write_entry(state: dict) -> None:
    Path(WORKSPACE / state["entry_path"]).write_text(
        _render_entry(state), encoding="utf-8", newline="\n")


def _canonical_pipeline_legs(pipeline_dir: str) -> list[dict]:
    """Standard legs from the BRONZE-FIX #1 canonical map (safe_deploy_core:
    PIPELINE_MAP x VALID_LAYERS + AUX_CODE_PREFIXES). ad1f03b7f interface."""
    sys.path.insert(0, str(WORKSPACE / ".tools"))
    import safe_deploy_core as core
    if pipeline_dir not in core.PIPELINE_MAP:
        sys.exit(f"ERROR: unknown pipeline dir '{pipeline_dir}' "
                 f"(known: {sorted(core.PIPELINE_MAP)})")
    bucket, firm = core.PIPELINE_MAP[pipeline_dir]
    legs = []
    for layer in sorted(core.VALID_LAYERS):
        legs.append({
            "id": f"{firm}-{layer}",
            "kind": "s3-prefix",
            "target": f"s3://{bucket}/code/{layer}/",
            "proof_required": f"comp-pipescript deployed --pipeline {firm}-{layer} MATCH line",
            "proof": None, "closed_at": None,
        })
    for prefix, home in (core.AUX_CODE_PREFIXES.get(firm) or {}).items():
        legs.append({
            "id": f"{firm}-aux-{prefix}",
            "kind": "s3-prefix",
            "target": f"s3://{bucket}/code/{prefix}/ (aux; repo home: {home or 'NONE -- UNCOVERED'})",
            "proof_required": f"comp-pipescript deployed [aux:{prefix}] MATCH line",
            "proof": None, "closed_at": None,
        })
    return legs


def cmd_open(args) -> int:
    if _state_path(args.slug).exists():
        sys.exit(f"ERROR: deploy ledger '{args.slug}' is already OPEN -- "
                 "close it or pick a new slug")
    legs: list[dict] = []
    for spec in args.leg or []:
        parts = [p.strip() for p in spec.split("|")]
        if len(parts) != 4:
            sys.exit(f"ERROR: --leg must be 'id|kind|target|proof_required', got: {spec}")
        lid, kind, target, proof_req = parts
        if kind not in LEG_KINDS:
            sys.exit(f"ERROR: leg kind '{kind}' not in {sorted(LEG_KINDS)}")
        legs.append({"id": lid, "kind": kind, "target": target,
                     "proof_required": proof_req, "proof": None, "closed_at": None})
    if args.pipeline:
        legs.extend(_canonical_pipeline_legs(args.pipeline))
    if not legs:
        sys.exit("ERROR: a deploy ledger needs at least one leg "
                 "(--leg and/or --pipeline)")
    ids = [leg["id"] for leg in legs]
    if len(ids) != len(set(ids)):
        sys.exit(f"ERROR: duplicate leg ids: {ids}")
    opened = _now()
    safe_slug = re.sub(r"[^A-Za-z0-9_-]", "-", args.slug)
    entry_rel = (f"org/critical_paths/change_management/"
                 f"{opened.strftime('%Y%m%dT%H%M')}Z_{safe_slug}_deploy_completion.md")
    state = {
        "slug": args.slug,
        "title": args.title,
        "author": args.author,
        "status": "OPEN",
        "opened_at": opened.isoformat(),
        "window_hours": args.window_hours,
        "entry_path": entry_rel,
        "legs": legs,
        "log": [f"{_ts(opened)} OPENED by {args.author} with {len(legs)} leg(s)"],
        "last_red_at": None,
    }
    _save(state)
    _write_entry(state)
    print(f"OK: OPENED deploy ledger '{args.slug}' ({len(legs)} legs) -> {entry_rel}")
    for leg in legs:
        print(f"  OPEN {leg['id']} [{leg['kind']}] {leg['target']}")
    return 0


def cmd_close_leg(args) -> int:
    state = _load(args.slug)
    for leg in state["legs"]:
        if leg["id"] == args.leg_id:
            leg["proof"] = args.proof
            leg["closed_at"] = _ts()
            state["log"].append(f"{_ts()} LEG {args.leg_id} closed: {args.proof[:120]}")
            _save(state)
            _write_entry(state)
            open_left = [leg["id"] for leg in state["legs"] if not leg.get("proof")]
            print(f"OK: leg {args.leg_id} closed. Remaining open: {open_left or 'NONE'}")
            return 0
    sys.exit(f"ERROR: leg '{args.leg_id}' not in ledger '{args.slug}' "
             f"(legs: {[leg['id'] for leg in state['legs']]})")


def cmd_close(args) -> int:
    state = _load(args.slug)
    unproven = [leg["id"] for leg in state["legs"] if not leg.get("proof")]
    if unproven:
        print(f"REFUSED: ledger '{args.slug}' has unproven leg(s): {unproven}")
        print("A leg without proof = the deploy is NOT complete. Close every "
              "leg with evidence, or the entry stays OPEN and blares.")
        return 2
    state["status"] = "CLOSED -- nothing stranded"
    state["closed_at"] = _ts()
    state["log"].append(f"{_ts()} CLOSED -- all {len(state['legs'])} legs proven")
    _write_entry(state)
    _state_path(args.slug).unlink()
    print(f"OK: CLOSED deploy ledger '{args.slug}' -- all {len(state['legs'])} "
          f"legs proven; sentinel removed; entry: {state['entry_path']}")
    return 0


def _red_alert(state: dict, age_h: float) -> None:
    """RED delivery: write the alert file directly into the COO inbox dir --
    the COO's persistent inbox Monitor streams it as an [INBOX] event. RED is
    alert-not-block (HALTGT [STOP]/[HALT] reserved for deploy-blocking)."""
    COO_INBOX.mkdir(parents=True, exist_ok=True)
    open_legs = [leg["id"] for leg in state["legs"] if not leg.get("proof")]
    subject = f"RED__deploy_ledger_OPEN_past_window__{state['slug']}"
    fname = f"{_ts()}_deploy-ledger_{subject}.md"
    body = (
        f"# Message from deploy_ledger.py (on behalf of {state['author']})\n"
        f"**To:** 2.0.0_SA_COO\n**Date:** {_ts()}\n"
        f"**Subject:** RED: deploy-completion ledger '{state['slug']}' OPEN "
        f"{age_h:.1f}h (window {state['window_hours']}h) -- POSSIBLE HALF-LANDED DEPLOY\n\n"
        f"Deploy: {state['title']}\nAuthor: {state['author']}\n"
        f"Opened: {state['opened_at']}\n"
        f"Stranded leg(s): {', '.join(open_legs)}\n"
        f"Entry: {state['entry_path']}\n\n"
        "NEVER-law e38cc2b16: a begun deploy FINISHES in-session or rolls back "
        "+ escalates loud. Route to the author or escalate.\n")
    (COO_INBOX / fname).write_text(body, encoding="utf-8", newline="\n")
    print(f"RED: alert delivered to COO inbox: {fname}")


def _md_status(md_path: Path) -> str | None:
    """First '**Status:**' value in a change_management ledger -- case-insensitive,
    and tolerant of a leading markdown bullet / blockquote marker ('- **Status:**',
    the bulleted hand-authored form). None if the file carries no status line."""
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    for line in text.splitlines():
        m = re.match(r"^\s*(?:[-*+>]\s+)?\*\*status:\*\*\s*(.*)$", line, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return None


def _has_close_marker(md_path: Path) -> bool:
    """True if the ledger carries an explicit, non-empty close-date marker
    ('**Date closed:**' / '**Closed:**' / '**closed:**'). Hand-authored ledgers
    that omit a **Status:** line (globgrph-style) signal a terminal state this way
    instead -- without this check they false-trip as 'no status line'."""
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    for line in text.splitlines():
        if re.match(r"^\s*(?:[-*+>]\s+)?\*\*(?:date\s+closed|closed):\*\*\s*\S",
                    line, re.IGNORECASE):
            return True
    return False


def _is_terminal_status(status: str) -> bool:
    """True if a ledger status LEADS with a terminal-state token (CLOSED /
    COMPLETE / ROLLBACK / ...) -- i.e. the deploy is not still open. Match on the
    leading word only, so a mid-string token (e.g. 'OPEN -- issue RESOLVED') does
    not false-terminal an open ledger."""
    head = status.lstrip().upper()
    return any(head.startswith(tok) for tok in TERMINAL_STATUS_TOKENS)


def _unindexed_open_ledgers(covered: set) -> list:
    """change_management/*_deploy_completion.md ledgers that represent an OPEN
    (non-terminal) deploy yet carry NO matching .open_deploys sentinel -- the
    false-clean gate-bypass class. `covered` = resolved .md paths already tracked
    by a live sentinel (reported via the sentinel scan). A ledger is treated as
    TERMINAL (skipped) when EITHER a **Status:** line leads with a terminal token
    OR an explicit close-date marker is present -- biased toward terminal so the
    loud RED never false-fires on the many CLOSED hand-authored ledgers. Returns
    [(path, reason, age_h), ...]."""
    out: list = []
    if not CM_DIR.is_dir():
        return out
    now = _now()
    for md in sorted(CM_DIR.glob("*_deploy_completion.md")):
        try:
            if md.resolve() in covered:
                continue  # tracked by a live sentinel -- already reported above
        except OSError:
            pass
        status = _md_status(md)
        if status is not None and _is_terminal_status(status):
            continue  # CLOSED / COMPLETE / ROLLED-BACK status -- nothing stranded
        if _has_close_marker(md):
            continue  # explicit close-date marker (globgrph-style hand ledger)
        if status is None:
            reason = "no **Status:** and no close-date marker (open or malformed)"
        else:
            reason = f"status='{status[:60]}' (not a terminal/closed state)"
        try:
            mtime = datetime.fromtimestamp(md.stat().st_mtime, timezone.utc)
            age_h = (now - mtime).total_seconds() / 3600.0
        except OSError:
            age_h = -1.0
        out.append((md, reason, age_h))
    return out


def _load_unindexed_red_state() -> dict:
    if UNINDEXED_RED_STATE.exists():
        try:
            return json.loads(UNINDEXED_RED_STATE.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}
    return {}


def _save_unindexed_red_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    UNINDEXED_RED_STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def _red_alert_unindexed(md: Path, reason: str, age_h: float) -> None:
    """RED delivery for an UNINDEXED open ledger -- the gate-bypass that the
    sentinel-only scan was blind to. Same alert-not-block class as _red_alert."""
    COO_INBOX.mkdir(parents=True, exist_ok=True)
    try:
        rel = md.relative_to(WORKSPACE)
    except ValueError:
        rel = md
    subject = f"RED__UNINDEXED_open_deploy_ledger__gate_bypass__{md.stem}"
    fname = f"{_ts()}_deploy-ledger_{subject}.md"
    body = (
        "# Message from deploy_ledger.py (gate-bypass scan)\n"
        "**To:** 2.0.0_SA_COO\n"
        f"**Date:** {_ts()}\n"
        "**Subject:** RED: UNINDEXED open deploy-completion ledger -- gate-bypass "
        "(invisible to the sentinel-only --red scan)\n\n"
        f"Ledger: {rel}\n"
        f"Reason: {reason}\n"
        f"Age (file mtime): {age_h:.1f}h\n\n"
        "This deploy-completion ledger declares an OPEN/non-terminal deploy but has "
        "NO .open_deploys/*.json sentinel, so the sentinel-only `check --red` scan "
        "was structurally blind to it (the false-clean class: a hand-authored "
        "markdown ledger is content-complete but INVISIBLE to the gate).\n\n"
        "NEVER-law e38cc2b16: a begun deploy FINISHES in-session or rolls back + "
        "escalates loud. RESOLVE by either:\n"
        "  (a) closing it -- set the ledger's **Status:** to a terminal state "
        "(CLOSED / COMPLETE / ROLLED BACK) once every leg is proven; or\n"
        "  (b) re-homing it onto the tracked path -- open via `deploy_ledger.py "
        "open ...` so it carries a sentinel the gate can see.\n")
    (COO_INBOX / fname).write_text(body, encoding="utf-8", newline="\n")
    print(f"RED: unindexed-ledger alert delivered to COO inbox: {fname}")


def cmd_check(args) -> int:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    now = _now()
    any_open = False
    covered: set = set()

    # --- Layer 1: tracked sentinels (the original, sound, in-window scan) ---
    sentinels = [sp for sp in sorted(STATE_DIR.glob("*.json"))
                 if not sp.name.startswith(".")]
    for sp in sentinels:
        state = json.loads(sp.read_text(encoding="utf-8"))
        any_open = True
        opened = datetime.fromisoformat(state["opened_at"])
        age_h = (now - opened).total_seconds() / 3600.0
        window = args.window_hours or state.get("window_hours", DEFAULT_WINDOW_HOURS)
        open_legs = [leg["id"] for leg in state["legs"] if not leg.get("proof")]
        flag = "PAST-WINDOW" if age_h > window else "in-window"
        print(f"OPEN: {state['slug']} age={age_h:.1f}h window={window}h [{flag}] "
              f"stranded={open_legs} author={state['author']}")
        try:
            covered.add((WORKSPACE / state["entry_path"]).resolve())
        except (KeyError, OSError):
            pass
        if args.red and age_h > window:
            last_red = state.get("last_red_at")
            if last_red and (now - datetime.fromisoformat(last_red)).total_seconds() < window * 3600:
                print(f"  (RED suppressed -- last alert {last_red}, re-alerts each {window}h)")
            else:
                _red_alert(state, age_h)
                state["last_red_at"] = now.isoformat()
                _save(state)

    # --- Layer 2: gate-bypass scan -- OPEN markdown ledgers with NO sentinel ---
    # (the false-clean class the sentinel-only scan was structurally blind to).
    bypass = _unindexed_open_ledgers(covered)
    if bypass:
        red_state = _load_unindexed_red_state() if args.red else {}
        changed = False
        for md, reason, age_h in bypass:
            try:
                shown = md.relative_to(WORKSPACE)
            except ValueError:
                shown = md
            print(f"BYPASS: UNINDEXED OPEN LEDGER {shown} age={age_h:.1f}h -- {reason}")
            if args.red:
                key = str(md.resolve())
                last = red_state.get(key)
                if last and (now - datetime.fromisoformat(last)).total_seconds() < DEFAULT_WINDOW_HOURS * 3600:
                    print(f"  (RED suppressed -- last alert {last}, re-alerts each {DEFAULT_WINDOW_HOURS}h)")
                else:
                    _red_alert_unindexed(md, reason, age_h)
                    red_state[key] = now.isoformat()
                    changed = True
        if args.red and changed:
            _save_unindexed_red_state(red_state)

    if not any_open and not bypass:
        print("OK: no open deploy ledgers + no unindexed open ledgers -- nothing half-landed")
        return 0
    return 1


def cmd_list(args) -> int:
    return cmd_check(argparse.Namespace(window_hours=None, red=False))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("open", help="open a completion ledger at deploy START")
    p.add_argument("--slug", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--author", required=True)
    p.add_argument("--leg", action="append",
                   help="'id|kind|target|proof_required' (repeatable)")
    p.add_argument("--pipeline", help="add canonical legs for this pipeline dir "
                                      "(PIPELINE_MAP x VALID_LAYERS + AUX_CODE_PREFIXES)")
    p.add_argument("--window-hours", type=float, default=DEFAULT_WINDOW_HOURS)
    p.set_defaults(fn=cmd_open)

    p = sub.add_parser("close-leg", help="record one leg's verification proof")
    p.add_argument("--slug", required=True)
    p.add_argument("--leg-id", required=True)
    p.add_argument("--proof", required=True)
    p.set_defaults(fn=cmd_close_leg)

    p = sub.add_parser("close", help="close the ledger (refuses if any leg unproven)")
    p.add_argument("--slug", required=True)
    p.set_defaults(fn=cmd_close)

    p = sub.add_parser("check", help="report OPEN ledgers; exit 1 if any; --red alerts COO")
    p.add_argument("--red", action="store_true")
    p.add_argument("--window-hours", type=float, default=None)
    p.set_defaults(fn=cmd_check)

    p = sub.add_parser("list", help="alias for check (no RED)")
    p.set_defaults(fn=cmd_list)

    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
