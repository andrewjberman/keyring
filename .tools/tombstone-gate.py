#!/usr/bin/env python3
"""tombstone-gate -- block a terraform apply that would RESURRECT a deliberately-deleted resource.

THE HAZARD (measured 2026-07-30, four instances in one estate):
  A resource deleted OUT-OF-BAND -- by CLI or console, not by removing its Terraform
  declaration -- leaves the declaration armed. The next apply of that stack RECREATES it.
  Worst observed form: immediately after `terraform destroy` on crawl-harness, `plan` read
  "20 to add" -- every resource gone, every one still declared, the whole stack primed to
  rebuild an EC2 box nobody was watching any more.

WHY A PLAN ALONE CANNOT DETECT IT:
  "deliberately deleted, about to be resurrected" and "new work, not created yet" are
  BYTE-IDENTICAL in a plan -- both render as `to add`. A gate firing on every create would
  block all new infrastructure and be switched off within a day. The missing input is a
  record of INTENT, which is what infra/aws/terraform/tombstones.json supplies.

WHAT THIS GATE DOES:
  Reads a terraform plan as JSON (stdin, or --plan-json FILE), extracts every resource the
  plan would CREATE, and fails if any of their names appear in the tombstone register.

MATCHING (deliberately narrow):
  On the resource's OWN NAME attribute -- bucket name, table name -- which is globally unique
  and stable. NOT on the Terraform resource address (`aws_s3_bucket.foo`), which can be
  renamed freely without changing what actually gets created. C-15: full identifier, never a
  prefix or substring.

FAIL-CLOSED, DELIBERATELY:
  A register it cannot read, or a plan it cannot parse, is rc=3 BLOCKED -- not a pass. A gate
  that fails open is the failure class this estate keeps paying for (a live gate printing
  "No such file or directory" and letting the commit through, 2026-07-29). Override is
  audited: TOMBSTONE_OVERRIDE="<reason>".

EXIT CODES:  0 = clean · 2 = BLOCKED (resurrection) · 3 = BLOCKED (gate could not run)

Owner: 0.7.0_AE_CloudOps · Built 2026-07-30 on Andrew's direct "build the gate".
"""
from __future__ import annotations

import argparse
import json
import os
import sys

DEFAULT_REGISTER = os.path.join("infra", "aws", "terraform", "tombstones.json")

# Which attribute carries the resource's real-world name, per type. A plan's `after` block
# is the created-state, so this is where the name lives. Order matters: first hit wins.
NAME_ATTRS = ("bucket", "name", "table_name", "function_name")

AUDIT_LOG = os.path.join("org", "tombstone-gate-audit.log")


def _log(msg: str) -> None:
    print("[tombstone-gate] %s" % msg, flush=True)


def load_register(path: str) -> dict:
    """Load the tombstone register. FAIL-CLOSED: an unreadable register is rc=3, never a pass."""
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    stones = {}
    for row in data.get("tombstones", []):
        nm = (row.get("name") or "").strip()
        if nm:
            stones[nm] = row
    if not stones:
        raise ValueError("register parsed but contains ZERO tombstones -- refusing to "
                         "report a pass off an empty register (an instrument that cannot "
                         "fail is not an instrument)")
    return stones


def creates_from_plan(plan: dict) -> list:
    """Every resource this plan would CREATE, as (address, type, name).

    A replace renders as ["delete","create"]; that still creates, so it counts.
    """
    out = []
    for rc in plan.get("resource_changes", []) or []:
        actions = (rc.get("change") or {}).get("actions") or []
        if "create" not in actions:
            continue
        after = (rc.get("change") or {}).get("after") or {}
        name = ""
        for attr in NAME_ATTRS:
            val = after.get(attr)
            if isinstance(val, str) and val.strip():
                name = val.strip()
                break
        out.append((rc.get("address", "?"), rc.get("type", "?"), name))
    return out


def audit(reason: str, hits: list) -> None:
    try:
        os.makedirs(os.path.dirname(AUDIT_LOG), exist_ok=True)
        with open(AUDIT_LOG, "a", encoding="utf-8") as fh:
            fh.write("OVERRIDE reason=%r resurrected=%s\n"
                     % (reason, ",".join(h[2] for h in hits)))
    except OSError as exc:  # an unwritable audit log must not silently swallow the override
        _log("WARN: could not write the override audit log (%s)" % exc)


def main(argv: list | None = None) -> int:
    ap = argparse.ArgumentParser(description="Block a resurrecting terraform apply")
    ap.add_argument("--plan-json", help="terraform show -json output (default: stdin)")
    ap.add_argument("--register", default=DEFAULT_REGISTER, help="tombstone register path")
    ap.add_argument("--workspace-root", default=".", help="repo root the paths resolve against")
    args = ap.parse_args(argv)

    reg_path = args.register
    if not os.path.isabs(reg_path):
        reg_path = os.path.join(args.workspace_root, reg_path)

    try:
        stones = load_register(reg_path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        _log("BLOCKED (rc=3): cannot read the tombstone register at %s -- %s" % (reg_path, exc))
        _log("  FAIL-CLOSED BY DESIGN. A gate that cannot read its own rules must not report a pass.")
        return 3

    try:
        raw = open(args.plan_json, encoding="utf-8").read() if args.plan_json else sys.stdin.read()
        plan = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        _log("BLOCKED (rc=3): cannot parse the plan JSON -- %s" % exc)
        _log("  Render it with: terraform show -json <planfile>")
        return 3

    creates = creates_from_plan(plan)
    hits = [c for c in creates if c[2] and c[2] in stones]

    # DENOMINATOR, always printed: a silent pass is indistinguishable from a gate that
    # examined nothing. State what was checked, not just the verdict.
    _log("checked %d create(s) in this plan against %d tombstone(s)" % (len(creates), len(stones)))

    if not hits:
        _log("CLEAN: no planned create matches a tombstoned resource.")
        return 0

    _log("*** BLOCKED (rc=2): THIS APPLY WOULD RESURRECT %d DELETED RESOURCE(S) ***" % len(hits))
    for addr, rtype, name in hits:
        row = stones[name]
        _log("  %s  (%s)" % (name, rtype))
        _log("      plan address : %s" % addr)
        _log("      deleted      : %s" % row.get("deleted", "?"))
        _log("      verified     : %s" % row.get("verified_absent", "?"))
        _log("      why          : %s" % row.get("why", "?"))
        if row.get("caution"):
            _log("      CAUTION      : %s" % row["caution"])
    _log("")
    _log("  THE FIX IS ALMOST NEVER TO OVERRIDE. It is to REMOVE THE DECLARATION from the")
    _log("  stack -- the resource is gone on purpose and the config still asks for it.")
    _log("  Zero-window retirement: delete the resource block, plan (reads 'N to destroy'),")
    _log("  then safe-apply. Source and state go clean in ONE operation.")
    _log("  If the resurrection IS intended, remove the tombstone entry -- that is a real")
    _log("  decision, and the entry existing is what forces it to be made deliberately.")
    _log("  Audited bypass: TOMBSTONE_OVERRIDE=\"<reason>\"")

    override = (os.environ.get("TOMBSTONE_OVERRIDE") or "").strip()
    if override:
        audit(override, hits)
        _log("OVERRIDDEN (audited to %s): %s" % (AUDIT_LOG, override))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
