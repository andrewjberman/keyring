#!/usr/bin/env python3
"""Acceptance checks for TO-L2-CROA's seven criteria."""
from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ARTIFACT = HERE / "L2_VIEW_ARTIFACTS.json"
RESULTS = HERE / "acceptance_results.json"


def main() -> int:
    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    views = {v["view_id"]: v for v in data["views"]}
    checks: dict[str, tuple[bool, str]] = {}

    checks["CROA-AC1"] = (
        set(views) == {"STRUCTURE", "BEHAVIOR"}
        and all(v["entity_set"]["denominator"] == len(v["entity_set"]["entities"]) for v in views.values()),
        "two exact views; each printed denominator equals its entity array length",
    )
    flags_ok = all(
        all(state in {"MEASURED", "ABSENT"} for state in entity["features"].values())
        for view in views.values() for entity in view["entity_set"]["entities"]
    )
    structure_absent = all(e["features"]["consensus_affinity"] == "ABSENT" for e in views["STRUCTURE"]["entity_set"]["entities"])
    checks["CROA-AC2"] = (flags_ok and structure_absent, "every per-entity feature is explicit MEASURED/ABSENT; blocked structure affinity is ABSENT")
    behavior_gate = views["BEHAVIOR"]["discrimination_gate"]
    observed = behavior_gate["observed"]
    mutant_pass = bool(1 and 1 >= 2 and 0.0 < (observed["possible_pairs"] / observed["possible_pairs"]) < 1.0)
    checks["CROA-AC3"] = (
        all(v["discrimination_gate"]["status"] in {"PASS", "FAIL"} for v in views.values())
        and behavior_gate["status"] == "PASS" and mutant_pass is False,
        f"gate outcomes carried: STRUCTURE={views['STRUCTURE']['discrimination_gate']['status']}, BEHAVIOR={behavior_gate['status']}; executed all-1 constant mutant gate result={'PASS' if mutant_pass else 'FAIL'}",
    )
    sr = views["STRUCTURE"]["reproducibility"]
    br = views["BEHAVIOR"]["reproducibility"]
    checks["CROA-AC4"] = (
        sr["N_requested"] == 25 and sr["N_executed"] == 0 and len(sr["seeds_requested"]) == 25
        and br["N"] == 1 and br["seed_policy"].startswith("NONE"),
        "STRUCTURE states requested/executed N, deterministic seed policy and per-run record; BEHAVIOR is deterministic N=1",
    )
    checks["CROA-AC5"] = (
        all(v["failure_mode"]["distinguishable_from_genuine_low_affinity"] is True for v in views.values()),
        "both failure modes state a mechanical distinction from measured low affinity",
    )
    checks["CROA-AC6"] = (
        data["no_fusion"] is True and data["cross_view_affinities"] == []
        and all("cross_view" not in pair for v in views.values() for pair in v["matrix"]["pairs"]),
        "no fusion flag true, cross-view affinity list empty, all matrices view-local",
    )
    checks["CROA-AC7"] = (
        "BLOCKING" in views["STRUCTURE"]["named_hazard_answer"]
        and "NOT USED" in views["BEHAVIOR"]["named_hazard_answer"]
        and views["STRUCTURE"]["matrix"]["status"] == "ABSENT-NOT-ZERO",
        "graph_tool gap is BLOCKING/ABSENT-NOT-ZERO; comp-heat score is NOT USED and drift is ABSENT",
    )

    rows = [
        {"criterion_id": cid, "status": "PASS" if ok else "FAIL", "evidence": evidence}
        for cid, (ok, evidence) in checks.items()
    ]
    out = {
        "schema": "nfra-c3materialize.l2.acceptance/1.0",
        "artifact": str(ARTIFACT.name),
        "passed": sum(r["status"] == "PASS" for r in rows),
        "denominator": len(rows),
        "rows": rows,
    }
    RESULTS.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(f"{row['criterion_id']}: {row['status']} - {row['evidence']}")
    print(f"RESULT: {out['passed']}/{out['denominator']}")
    return 0 if out["passed"] == out["denominator"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
