"""Pin both canonical channel roots and check every changed/new proof at L8."""

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
        args,
        cwd=ROOT,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
    )
    return {"args": args, "rc": p.returncode, "stdout": p.stdout, "stderr": p.stderr}


def records(text):
    result = []
    for block in re.findall(r"```json\s*(.*?)```", text, re.S):
        value = json.loads(block)
        assert isinstance(value, (dict, list))
        result.extend(value if isinstance(value, list) else [value])
    return result


def main():
    spec = importlib.util.spec_from_file_location(
        "gate", ROOT / ".tools/surprise-row-gate.py"
    )
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    pin = run(["git", "rev-parse", "HEAD"])["stdout"].strip()

    def blob(path, revision=pin):
        return subprocess.check_output(
            ["git", "show", revision + ":" + path], cwd=ROOT
        ).decode("utf-8")

    paths = run(["git", "ls-tree", "-r", "--name-only", pin, PROJECT])[
        "stdout"
    ].splitlines()
    channel_paths = set()
    for pattern in (
        gate.INVESTIGATION_PATTERNS
        + gate.ADJUDICATION_PATTERNS
        + gate.REMEDIATION_PATTERNS
    ):
        found, note = gate._index_paths(str(ROOT), [pattern % "AMGT_RESAPP"])
        assert found is not None, note
        channel_paths.update(found)
    channel = [(p, records(blob(p))) for p in sorted(channel_paths)]
    remids = [
        r["id"] for p, rr in channel if gate._kind(p) == "REMEDIATION" for r in rr
    ]
    latest, unknown = gate._resolve_latest(
        [(p, rr) for p, rr in channel if gate._kind(p) != "REMEDIATION"], remids
    )
    pending = [
        dict(r, source=p)
        for p, rr in channel
        if gate._kind(p) == "INVESTIGATION"
        for r in rr
        if latest.get(r["id"]) == "UNDER_INVESTIGATION"
    ]
    old = json.loads(
        (HOME / "AMGT_RESAPP_ROUND7_CVO_INTAKE_20260912_Z.json").read_text()
    )
    proofs = [p for p in paths if p.endswith(".proof_of_spec.json")]
    checks = {}
    for p in proofs:
        name = Path(p).name.replace(".proof_of_spec.json", ".md")
        order = next(t for t in paths if "/task-orders/" in t and Path(t).name == name)
        ids = re.findall(r'<criterion\s+id="([^"]+)"', blob(order))
        assert (ROOT / p).read_text(encoding="utf-8") == blob(p).replace(
            "\r\n", "\n"
        ), p
        assert (ROOT / order).read_text(encoding="utf-8") == blob(order).replace(
            "\r\n", "\n"
        ), order
        inherited = (
            p in old["proof_checks"]
            and old["proof_checks"][p]["rc"] == 0
            and blob(p) == blob(p, old["pin"])
            and blob(order) == blob(order, old["pin"])
        )
        checks[p] = (
            {
                "rc": 0,
                "basis": "Prior rc0; exact proof AND matching issued order bytes unchanged",
                "prior_intake": "AMGT_RESAPP_ROUND7_CVO_INTAKE_20260912_Z.json",
                "prior_pin": old["pin"],
            }
            if inherited
            else run(
                [sys.executable, ".tools/proof-of-spec-check.py", p, ",".join(ids)]
            )
        )
        checks[p].update(
            issued_ids=ids,
            proof_sha256=hashlib.sha256(blob(p).encode()).hexdigest(),
            order_sha256=hashlib.sha256(blob(order).encode()).hexdigest(),
        )
    out = {
        "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "pin": pin,
        "packet_pin": "790607c9ef",
        "orders": {
            p: gate._open_tos_for_project(str(ROOT), p)
            for p in ["AMGT_RESAPP", "POSN_ASTTAX", "ZZZZ_NOSUCH"]
        },
        "original_count": len(latest),
        "pending": pending,
        "unknown_targets": unknown,
        "task_orders": {
            p: blob(p) for p in paths if "/task-orders/" in p and ".TO-AMGT-rg-" in p
        },
        "round_proofs": {p: json.loads(blob(p)) for p in proofs if ".TO-AMGT-rg-" in p},
        "proof_checks": checks,
        "channel_sha256": {
            p: hashlib.sha256(blob(p).encode()).hexdigest()
            for p in sorted(channel_paths)
        },
        "limits": "Both canonical roots, each JSON fence parsed separately including single objects; parsing errors fail closed. Structure checks are not truth grades. No AWS or publication.",
    }
    (HOME / "AMGT_RESAPP_ROUND8_CVO_INTAKE_20260913_Z.json").write_text(
        json.dumps(out, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "pin": pin,
                "originals": len(latest),
                "pending": [r["id"] for r in pending],
                "orders": out["orders"],
                "proofs": len(checks),
                "inherited": sum("prior_pin" in c for c in checks.values()),
                "nonvalid": {p: c for p, c in checks.items() if c["rc"] != 0},
                "channel_files": len(channel_paths),
            }
        )
    )


if __name__ == "__main__":
    main()
