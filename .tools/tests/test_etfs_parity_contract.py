#!/usr/bin/env python3
"""THE EXIT-CODE CONTRACT of .tools/etfs-parity-check.py, exercised.

WHY THIS FILE EXISTS
--------------------
The parity gate protects the ETF net-assets cutover -- 4 of Opal's 14 AUM
cohorts, 27% of fee-paying AUM. Its whole job is to REFUSE a cutover until
3 trading days of value-by-value parity are proven ON THE ARTIFACT.

A gate is only a gate if a bad result STOPS something. That means the exit code
is not a detail -- it IS the gate. And until now, the only way to check it was to
run the tool and read $? at a shell.

On 2026-07-14 I did exactly that, and I did it wrong:

    python .tools/etfs-parity-check.py | tail -25 ; echo $?     -> 0

That 0 is TAIL'S exit code. Not the gate's. It is meaningless. The gate was in
fact returning 1 (correctly refusing a 1-of-3-day cutover) -- so my CLAIM was
true, but MY CHECK OF IT WAS BROKEN, AND WOULD HAVE PRINTED THE SAME 0 IF THE
GATE HAD BEEN DEAD. The instrument could not have told me the truth in either
direction. Being right was luck.

It is the same rc-through-a-pipe class I had reported against MYSELF the previous
session (an `aws s3 cp | tail` that printed rc=0 over a FAILED upload), and been
credited for finding. Knowing a failure mode by name does not immunize you
against writing it.

    CARE IS NOT A CONTROL. CARE IS WHAT YOU HAVE INSTEAD OF ONE.

So the contract stops living in my head, in a commit message, and in a shell
one-liner -- and starts living here, where it is exercised.

Run:  python .tools/tests/test_etfs_parity_contract.py
"""
from __future__ import annotations

import importlib.util
import pathlib

GATE = pathlib.Path(__file__).resolve().parents[1] / "etfs-parity-check.py"

spec = importlib.util.spec_from_file_location("parity_gate", GATE)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

REQ = gate.REQUIRED_TRADING_DAYS

# (green, total, expected_exit, why)
# EXIT 0 IS REACHABLE ONLY ON all-green AND green >= REQUIRED. Everything else 1.
CASES = [
    (0, 0, 1, "no overlapping days -- nothing proven, must refuse"),
    (1, 1, 1, "day-1 EXACT -- the seductive case. 1 < 3. MUST STILL REFUSE."),
    (2, 2, 1, "two green days -- still short of the threshold"),
    (3, 3, 0, "THE ONLY PASS: 3 of 3 green, threshold met"),
    (4, 4, 0, "more than enough, all green"),
    (2, 3, 1, "a day went RED -- refuse regardless of the count"),
    (0, 3, 1, "all three RED"),
    (3, 4, 1, "3 green but one RED -- a RED is not cancelled by a quorum"),
]


def main() -> int:
    failures = []

    print(f"THE EXIT-CODE CONTRACT (required trading days = {REQ})")
    print("=" * 70)
    for green, total, expected, why in CASES:
        code, lines = gate.verdict(green, total)
        ok = code == expected
        print(f"  green={green} total={total} -> exit {code} "
              f"(want {expected})  {'OK ' if ok else 'FAIL'}  {why}")
        if not ok:
            failures.append((green, total, expected, code, why))
        # a refusal must SAY the laptop stays on -- the verdict text is the
        # operator-facing half of the gate, and a silent refusal gets ignored
        if expected == 1 and not any("LAPTOP STAYS ON" in ln
                                     or "NOT CUTOVER-READY" in ln
                                     for ln in lines):
            failures.append((green, total, expected, code,
                             "refusal did not SAY it was refusing"))

    print()
    print("THE INVARIANT: exit 0 requires all-green AND >= threshold")
    print("-" * 70)
    for green in range(0, REQ + 3):
        for total in range(green, REQ + 3):
            code, _ = gate.verdict(green, total)
            should_pass = (green == total and green >= REQ)
            if (code == 0) != should_pass:
                failures.append((green, total, 0 if should_pass else 1, code,
                                 "INVARIANT BREACH"))
    print(f"  swept {(REQ + 3) ** 2} (green,total) combinations -- "
          f"no exit-0 outside the all-green/>={REQ} region"
          if not failures else "  INVARIANT BREACHED")

    # -------------------------------------------------------------------
    # THE MUTANT. A passing assertion never made to fail has never been tested.
    # Break the gate on purpose and prove THIS FILE CATCHES IT. Without this,
    # the suite above is just eight lines that happen to print OK.
    # -------------------------------------------------------------------
    print()
    print("MUTANT -- break the gate on purpose; this suite MUST catch it")
    print("-" * 70)
    real = gate.verdict
    gate.verdict = lambda g, t, required=REQ: (0, ["  (mutant: always passes)"])
    caught = False
    for green, total, expected, _why in CASES:
        code, _ = gate.verdict(green, total)
        if expected == 1 and code != expected:
            caught = True
            break
    gate.verdict = real
    if caught:
        print("  OK: an always-pass gate IS caught by this suite.")
    else:
        print("  FAIL: the mutant SURVIVED. This suite proves nothing.")
        failures.append((None, None, None, None, "MUTANT SURVIVED"))

    print()
    if failures:
        print(f"FAILED -- {len(failures)} problem(s):")
        for f in failures:
            print(f"   {f}")
        return 1
    print("ALL CONTRACT TESTS PASS -- the gate blocks, and this proves it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
