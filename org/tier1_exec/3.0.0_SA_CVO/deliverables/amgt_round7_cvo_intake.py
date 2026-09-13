"""Capture the round-7 review corpus and verify proof structure without grading truth."""

import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
HOME = Path(__file__).parent
PROJECT = "org/missions/D5/AMGT/AMGT_RESAPP"


def run(args):
    p = subprocess.run(
        args, cwd=ROOT, capture_output=True, encoding="utf-8", errors="replace"
    )
    return {"args": args, "rc": p.returncode, "stdout": p.stdout, "stderr": p.stderr}


def records(text):
    out = []
    for block in re.findall(r"```json\s*(.*?)```", text, re.S):
        value = json.loads(block)
        out.extend(value if isinstance(value, list) else [value])
    return out


def main():
    spec = importlib.util.spec_from_file_location(
        "gate", ROOT / ".tools/surprise-row-gate.py"
    )
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    pin = run(["git", "rev-parse", "HEAD"])["stdout"].strip()
    paths = run(["git", "ls-tree", "-r", "--name-only", pin, PROJECT])[
        "stdout"
    ].splitlines()

    def blob(p):
        return subprocess.check_output(["git", "show", pin + ":" + p], cwd=ROOT).decode(
            "utf-8"
        )

    channel = [
        (p, records(blob(p)))
        for p in paths
        if "/surprise-channel/" in p and p.endswith(".md")
    ]
    rem_ids = [r["id"] for p, rr in channel if "/remediations/" in p for r in rr]
    latest, unknown = gate._resolve_latest(
        [(p, rr) for p, rr in channel if "/remediations/" not in p], rem_ids
    )
    pending = [
        dict(r, source=p)
        for p, rr in channel
        if "/investigations/" in p
        for r in rr
        if latest.get(r["id"]) == "UNDER_INVESTIGATION"
    ]
    tos = [p for p in paths if "/task-orders/" in p and ".TO-AMGT-rf-" in p]
    proofs = [p for p in paths if p.endswith(".proof_of_spec.json")]
    proof_checks = {}
    round_proofs = {}
    for p in proofs:
        order_name = Path(p).name.replace(".proof_of_spec.json", ".md")
        order_path = next(
            (t for t in paths if "/task-orders/" in t and Path(t).name == order_name),
            None,
        )
        if order_path is None:
            proof_checks[p] = {"rc": None, "reason": "No exact named task order found"}
            continue
        order = blob(order_path)
        ids = re.findall(r'<criterion\s+id="([^"]+)"', order)
        proof_checks[p] = run(
            [sys.executable, ".tools/proof-of-spec-check.py", p, ",".join(ids)]
        )
        proof_checks[p]["issued_ids"] = ids
        proof_checks[p]["working_matches_pin"] = (ROOT / p).read_text(
            encoding="utf-8"
        ) == blob(p)
        if ".TO-AMGT-rf-" in p:
            round_proofs[p] = json.loads(blob(p))
    out = {
        "utc": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "pin": pin,
        "packet_pin": "6a50ce1832",
        "orders": {
            p: gate._open_tos_for_project(str(ROOT), p)
            for p in ["AMGT_RESAPP", "POSN_ASTTAX", "ZZZZ_NOSUCH"]
        },
        "original_count": len(latest),
        "pending": pending,
        "unknown_targets": unknown,
        "task_orders": {p: blob(p) for p in tos},
        "round_proofs": round_proofs,
        "proof_checks": proof_checks,
        "channel_sha256": {
            p: hashlib.sha256(blob(p).encode()).hexdigest() for p, _ in channel
        },
        "limits": "Source pinned; proof checker runs in current main tree and verifies structure, not truth. No AWS or portal publication. Prior adjudications retained.",
    }
    target = HOME / "AMGT_RESAPP_ROUND7_CVO_INTAKE_20260912_Z.json"
    target.write_text(
        json.dumps(out, indent=2, ensure_ascii=True) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "pin": pin,
                "originals": len(latest),
                "pending": [r["id"] for r in pending],
                "orders": out["orders"],
                "proof_count": len(proofs),
                "nonvalid": {p: c for p, c in proof_checks.items() if c["rc"] != 0},
                "round_orders": tos,
                "path": str(target),
            }
        )
    )


if __name__ == "__main__":
    main()
