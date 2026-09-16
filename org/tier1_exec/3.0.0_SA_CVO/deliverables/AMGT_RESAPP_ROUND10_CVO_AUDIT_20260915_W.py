"""Read-only evidence census; writes only the CVO's audit JSON beside this script."""

import collections
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
PROJECT = ROOT / "org/missions/D5/AMGT/AMGT_RESAPP"
OUT = Path(__file__).with_suffix(".json")


def run(*args):
    p = subprocess.run(
        args,
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return {"rc": p.returncode, "stdout": p.stdout, "stderr": p.stderr}


def rows(path):
    out = []
    for block in re.findall(
        r"```json\s*(.*?)```", path.read_text(encoding="utf-8-sig"), re.S
    ):
        obj = json.loads(block)
        out.extend(obj if isinstance(obj, list) else [obj])
    return out


def main():
    previous = (
        json.loads(OUT.read_text(encoding="utf-8"))
        if "--reuse-unchanged-checks" in sys.argv and OUT.exists()
        else {}
    )
    old_checks = {p["path"]: p for p in previous.get("proofs", [])}
    a = {
        "seat": "3.0.0_SA_CVO~W",
        "captured_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "head": run("git", "rev-parse", "HEAD"),
        "files": {},
        "roots": {},
        "orders": [],
        "proofs": [],
    }
    channel = PROJECT / "surprise-channel"
    legacy = ROOT / "org/surprise_channel/AMGT_RESAPP"
    a["roots"] = {str(p.relative_to(ROOT)): p.exists() for p in (channel, legacy)}
    inv, adj, rem = [], [], []
    for kind, target in [
        ("investigations", inv),
        ("adjudications", adj),
        ("remediations", rem),
    ]:
        for p in sorted((channel / kind).glob("*.md")):
            name = p.relative_to(ROOT).as_posix()
            a["files"][name] = {
                "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
                "rows": rows(p),
            }
            target.extend(rows(p))
    a["investigation_count"] = len(inv)
    a["duplicate_investigation_ids"] = [
        i for i, n in collections.Counter(r["id"] for r in inv).items() if n > 1
    ]
    disposed = {
        i
        for r in adj
        if r.get("disposition")
        in (
            "GRADUATED",
            "DISMISSED_WITH_REASON",
            "DECOMP_INVALIDATING",
            "UNDER_INVESTIGATION",
        )
        for i in r.get("adjudicates", [])
    }
    a["new_items"] = [r for r in inv if r["id"] not in disposed]
    a["previously_adjudicated"] = len({r["id"] for r in inv} & disposed)
    order_map = {}
    for p in sorted((PROJECT / "task-orders").glob("*.md")):
        txt = p.read_text(encoding="utf-8-sig")
        status = re.findall(r"^\s*<status>\s*([^<\r\n]+)\s*</status>\s*$", txt, re.M)
        ids = re.findall(r'<criterion\b[^>]*\bid="([^"]+)"', txt)
        order = {
            "path": p.relative_to(ROOT).as_posix(),
            "status": status,
            "criterion_ids": ids,
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        }
        a["orders"].append(order)
        order_map[p.stem] = order
    for p in sorted((PROJECT / "deliverables").rglob("*.proof_of_spec.json")):
        order = order_map.get(p.name.removesuffix(".proof_of_spec.json"))
        args = [sys.executable, ".tools/proof-of-spec-check.py", str(p)]
        if order and order["criterion_ids"]:
            args.append(",".join(order["criterion_ids"]))
        name = p.relative_to(ROOT).as_posix()
        sha = hashlib.sha256(p.read_bytes()).hexdigest()
        old = old_checks.get(name)
        old_order = next(
            (
                o
                for o in previous.get("orders", [])
                if order and o["path"] == order["path"]
            ),
            None,
        )
        reuse = (
            old
            and old["sha256"] == sha
            and old_order
            and old_order["sha256"] == order["sha256"]
        )
        result = old["check"] if reuse else run(*args)
        a["proofs"].append(
            {
                "path": name,
                "sha256": sha,
                "check_reused_at_identical_proof_and_order_bytes": bool(reuse),
                "order": order["path"] if order else None,
                "data": json.loads(p.read_text(encoding="utf-8-sig")),
                "check": result,
            }
        )
    a["nonterminal_orders"] = [
        o
        for o in a["orders"]
        if not o["status"]
        or o["status"][-1].lower()
        not in ("complete", "completed", "superseded", "cancelled", "canceled")
    ]
    a["complete_orders_without_proof"] = [
        o["path"]
        for o in a["orders"]
        if o["status"][-1].lower() in ("complete", "completed")
        and not any(x["order"] == o["path"] for x in a["proofs"])
    ]
    OUT.write_text(json.dumps(a, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "audit": str(OUT),
                "roots": a["roots"],
                "investigations": len(inv),
                "previously_adjudicated": a["previously_adjudicated"],
                "new_items": [r["id"] for r in a["new_items"]],
                "orders": len(a["orders"]),
                "status_counts": dict(
                    collections.Counter(o["status"][-1] for o in a["orders"])
                ),
                "nonterminal": a["nonterminal_orders"],
                "proofs": len(a["proofs"]),
                "proof_failures": [p["path"] for p in a["proofs"] if p["check"]["rc"]],
                "complete_orders_without_proof": a["complete_orders_without_proof"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
