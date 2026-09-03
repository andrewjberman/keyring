#!/usr/bin/env python3
"""to-liveness-join -- find TASK ORDERS DISPATCHED INTO DEAD LANES.

THE GAP THIS CLOSES:
  /to-check   reads <status>.          It cannot see whether the assignee exists.
  fabric-check reads agent liveness.   It cannot see what work is pointed at an agent.
  NEITHER JOINS THEM.

So a TO in <status>pending</status> (= DISPATCHED) assigned to a serial that is not
registered is invisible to both -- and it reads as HEALTHY ACTIVITY in the registry.
The more diligently a TO is marked dispatched, the healthier a dead lane looks.

Found 2026-07-13 by 2.0.0_SA_COO: four of my own TOs had sat `pending` against
NOT-REGISTERED assignees for six days. I verified lane-liveness before every dispatch
I fired that night and never once for the TOs I had authored days earlier. The check
was applied going forward and never backward.

F-008 family: the fabric cannot detect that something is dead. This does not fix that
-- liveness here is still ABSENCE-derived (a serial missing from liveness.json). It
only joins two absences that were never compared.

  ZOMBIE  = <status>pending</status>  + assignee absent/stale in liveness.json
            -> the work is NOT moving and the board says it is.
  STRANDED= <status>staged</status>   + assignee absent  -> harmless today (staged = not
            dispatched, awaiting GO) but it will become a ZOMBIE the moment someone GOes
            it without checking the lane. Reported separately, never as an alarm.

Exit 0 always. This REPORTS; it does not gate. A gate on an absence-derived signal
would fire on every legitimately-offline worker.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIVENESS = ROOT / "org" / "mcp" / "liveness.json"
STALE_MIN = 10.0

STATUS_RE = re.compile(r"<status>\s*([a-z-]+)\s*</status>", re.I)
ISSUED_RE = re.compile(r"<issued_to>\s*([^<]+?)\s*</issued_to>", re.I)
SERIAL_RE = re.compile(r"\d+\.\d+\.\d+_[A-Z]+_[A-Za-z]+(?:~[A-Z])?")


def load_live() -> dict[str, float]:
    """serial -> minutes since last_seen. Absent serial = not registered at all."""
    try:
        raw = json.loads(LIVENESS.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"WARN: cannot read liveness.json ({exc}) -- every lane will read ABSENT.")
        return {}
    agents = raw.get("agents", raw)
    now = datetime.now(timezone.utc)
    out: dict[str, float] = {}
    for serial, rec in agents.items():
        if not isinstance(rec, dict):
            continue
        try:
            seen = datetime.fromisoformat(rec.get("last_seen", ""))
            out[serial] = (now - seen).total_seconds() / 60.0
        except Exception:  # noqa: BLE001, S112
            continue
    return out


def assignees(raw: str) -> list[str]:
    """A TO may name several serials (co-owned / window / cert). Every one must be alive."""
    return SERIAL_RE.findall(raw) or []


def main() -> int:
    live = load_live()
    tos = sorted(list(ROOT.glob("org/**/task_orders/*.md")) + list(ROOT.glob("org/missions/D*/*/*/task-orders/*.md")))  # R-ii: both roots

    zombies: list[tuple[str, str, str]] = []
    stranded: list[tuple[str, str, str]] = []
    ok = 0

    for path in tos:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001, S112
            continue
        st_m = STATUS_RE.search(text)
        is_m = ISSUED_RE.search(text)
        if not st_m or not is_m:
            continue
        status = st_m.group(1).lower()
        if status not in ("pending", "staged"):
            continue

        serials = assignees(is_m.group(1))
        if not serials:
            continue

        dead = [
            s for s in serials
            if s not in live or live[s] > STALE_MIN
        ]
        rel = str(path.relative_to(ROOT))
        if not dead:
            ok += 1
            continue
        why = ", ".join(
            f"{s}={'ABSENT' if s not in live else f'{live[s]:.0f}min'}" for s in dead
        )
        (zombies if status == "pending" else stranded).append((rel, status, why))

    print(f"TO-LIVENESS JOIN -- {len(tos)} task orders scanned (the denominator)")
    print(f"  pending/staged with a LIVE assignee : {ok}")
    print(f"  ZOMBIE   (pending -> dead lane)     : {len(zombies)}")
    print(f"  stranded (staged  -> dead lane)     : {len(stranded)}")

    if zombies:
        print("\nZOMBIES -- DISPATCHED, and nobody is there. The board reads these as ACTIVE:")
        for rel, _st, why in zombies:
            print(f"  [{why}]\n     {rel}")
        print("\n  RESOLVE each: respawn the lane, reroute to a live one, or flip back to staged.")
        print("  Do NOT simply mark them complete -- the work was never done.")

    if stranded:
        print("\nstranded (staged -> dead lane) -- NOT an alarm; staged means not dispatched.")
        print("  But each becomes a ZOMBIE the moment someone GOes it without checking the lane:")
        for rel, _st, why in stranded:
            print(f"  [{why}]  {rel}")

    if not zombies and not stranded:
        print("\n  No task order is pointed at a dead lane.")

    print(
        "\nNOTE: liveness here is ABSENCE-derived (F-008 -- the fabric still cannot detect "
        "death).\n      An absent serial may be legitimately offline. This REPORTS; it does "
        "not gate."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
