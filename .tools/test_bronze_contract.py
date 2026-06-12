#!/usr/bin/env python3
"""Replay tests for the bronze required-dim contract (ADVI_INFETL.BRONZE-FIX #2).

AC5: the 2026-06-12 inf-ADVI incident scenario (stale orchestrator catalog
missing the transactions dim, every dim it DID run succeeding) must now
evaluate to INCOMPLETE with the success sentinel withheld -- never success.

Pure-logic tests against orchestrator.evaluate_contract + the contract module;
no AWS, no subprocess. Run: python .tools/test_bronze_contract.py
"""
from __future__ import annotations

import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
BRONZE_DIR = WORKSPACE / "data" / "inf" / "scripts" / "bronze"
sys.path.insert(0, str(BRONZE_DIR))

from bronze_required_dims import REQUIRED_DIMS, get_contract  # noqa: E402
from orchestrator import evaluate_contract  # noqa: E402

FAILURES: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        print(f"  OK:   {name}")
    else:
        print(f"  FAIL: {name} {detail}")
        FAILURES.append(name)


def main() -> int:
    contract = get_contract("inf", "orion-api")
    required = contract["required_attempted"]

    print("[1] AC5 replay -- 2026-06-12 incident: stale catalog missing transactions")
    # The May-8 orchestrator ran these dims; all its OWN dims succeeded.
    may8_attempted = {"unified_account_dim", "billing", "tax", "accounts_v2",
                      "performance", "assets", "geo"}
    missing = evaluate_contract(may8_attempted, required)
    check("transactions reported MISSING", missing == ["transactions"], f"got {missing}")
    check("overall would be incomplete (missing non-empty)", bool(missing))

    print("[2] Full catalog -> contract satisfied")
    full = may8_attempted | {"transactions"}
    check("no missing dims", evaluate_contract(full, required) == [])

    print("[3] AC3 attempted-vs-nonempty -- a 0-row ok dim is COMPLETE-with-empty")
    # evaluate_contract sees only attempted-dim NAMES; row counts are not an
    # input. A dim that ran with 0 rows is in the attempted set -> not missing.
    check("0-row attempted dim not missing", evaluate_contract(full, required) == [])

    print("[4] Failed dim is ATTEMPTED (feeds failure path, not missing path)")
    # transactions ran and FAILED: it has a run-record -> not 'missing'.
    check("failed-but-attempted dim not missing",
          evaluate_contract(full, required) == [])

    print("[5] Subset re-fire alone (the sentinel-overwrite wart) -- a 1-dim run")
    subset_only = {"transactions"}
    missing = evaluate_contract(subset_only, required)
    check("subset alone is incomplete (6 missing)", len(missing) == 6, f"got {missing}")
    # With the day's prior markers merged (load_prior_marker_dims), the same
    # subset run evaluates the full set:
    merged = subset_only | may8_attempted
    check("subset + prior markers merged -> complete",
          evaluate_contract(merged, required) == [])

    print("[6] Contract fail-closed on unknown firm/pipeline")
    try:
        get_contract("inf", "no-such-pipeline")
        check("KeyError raised", False, "(no exception)")
    except KeyError:
        check("KeyError raised", True)

    print("[7] Contract shape sanity")
    check("inf/orion-api requires 7 dims", len(required) == 7, f"got {len(required)}")
    check("transactions in required set", "transactions" in required)
    check("geo NOT required (documented not_required)",
          "geo" not in required and "geo" in contract["not_required"])
    check("bd/cot have no false coverage claim",
          "bd" not in REQUIRED_DIMS and "cot" not in REQUIRED_DIMS)

    print()
    if FAILURES:
        print(f"RESULT: {len(FAILURES)} FAILURE(S): {FAILURES}")
        return 1
    print("RESULT: ALL PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
