# TO-CE-T-25 -- comp-dataflow gate under FWD-10 (verdict-bearing rc) -- 0.8.0_AE_CloudComp~A

**Date:** 2026-09-03
**Task Order:** NFRA_COMPEFFICACY.TO-CE-T-25.comp-dataflow-gate-under-fwd10
**Status:** COMPLETE (pending CVO grade + MSTR push)

---

## Objective

This TO is the direct follow-up to my own CE-t-7 finding F4: a budget-limited (partial) `gate`
sweep with zero findings among the reached files still returned rc=0, byte-identical to a genuinely
complete clean sweep, on a tool whose rc IS its verdict. Routed SCOPE_CHANGE (S14), adjudicated by
`1.0.0_SA_CTO`, PRD re-issued as v0.5 with FWD-10. This TO fixes it: `cmd_gate` now returns a
fourth, distinct rc (`RC_NOT_DECIDABLE=4`) at BUDGET REACHED, always, never the clean or failing rc.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `comp-read org/modules/graph/comp_dataflow.py --for "cmd_gate's return paths..."` (before write) | PASS | located the three existing return points exactly |
| comp-read | `comp-read org/modules/graph/iam_cli.py --for "how STATE_NOT_DECIDABLE maps to the process exit code"` | PASS | found the family precedent (rc=2) |
| grep (rc enumeration) | `grep -n "return [0-9]" org/modules/graph/comp_dataflow.py` | PASS | confirmed rc=2 already occupied (CE-t-7's own --budget usage error) before choosing rc=4 |
| commit-gate.sh | on comp_dataflow.py, test_comp_dataflow_battery.py | PASS | clean, 2 of 2 |
| surprise-row-gate.py | on the updated INVESTIGATION_v1.md | PASS | rc=0, the S16 append validated |
| proof-of-spec-check.py | on this instance | see below | validated before the complete flip |

**What worked:** reading `iam_cli.py` directly (not from memory) before choosing an rc value paid
off immediately -- `STATE_NOT_DECIDABLE = "NOT-DECIDABLE"` is the exact enum tool-voice token, and
its rc=2 usage confirmed the "family precedent" the TO named, in the tool's own source, at the
exact line the TO cited (`:50`).

**What failed, found, and fixed while EXERCISING the fix (not asked for, required to build it):**
the FIRST attempt at "follow the cursor to completion" (T25-AC2's own DONE WHEN) did not produce a
true verdict -- it kept reading `rc=4` no matter how large the budget. Root cause: `total_units`
was measured **before** the `--cursor` filter reassigned `units`, so the denominator stayed pinned
at the pre-cursor population size forever, and a cursor-resumed run could never show `n == N`. This
is a real, pre-existing bug (present since CE-t-7, never exercised end-to-end until this cell's own
acceptance test forced it), and it directly threatened this TO's own DONE WHEN -- without the fix,
FWD-10's resume promise would have been unbuildable. Fixed by moving `total_units = len(units)`
to after the cursor filter, matching `comp-find`'s own established precedent for the identical
shape (verified: `comp-find`'s `_search_aws` does the same). Re-verified: the identical exercise now
returns the true verdict.

---

## Work Completed

### 1. The verdict-bearing rc, commit `72e7846ca7`

`cmd_gate`'s rc vocabulary is now five named constants (`RC_CLEAN=0`, `RC_FINDINGS=1`, `RC_USAGE=2`,
`RC_REFUSED=3`, `RC_NOT_DECIDABLE=4`), all stated on `gate --help` via a new epilog including WHY
rc=4 was chosen over the `iam_cli.py` family precedent's rc=2. The BUDGET REACHED line prints
exactly as CE-t-7 landed it; a new `STATE: NOT-DECIDABLE` line carries the enum's own tool-voice
token, and the state also rides the `--json` budget block. `origin`'s body carries zero diff lines.

### 2. The cursor-denominator bug, same commit

Found and fixed while exercising T25-AC2 (see above) -- `total_units` now measured after the
`--cursor` filter, matching `comp-find`'s own precedent.

### 3. EXERCISED end-to-end (T25-AC2)

A real rc-only consumer (a shell `&&`) correctly does not proceed on a budget-cut sweep over the
full 532-file `data/` tree (rc=4); the printed cursor followed with an ample budget completes (531
of 531, 0 deferred, WITHIN BUDGET) and returns rc=1, the true verdict -- confirmed by a second `&&`
check. Both runs, including the pre-fix failure, are quoted verbatim in the deliverable.

### 4. Battery: 3 new arms, 11/11 PASS

`.tools/tests/test_comp_dataflow_battery.py` gains `VERDICT-RC-CONSUMER` (a real subprocess rc-only
check), `VERDICT-RC-VOCABULARY` (three real invocations, pairwise-distinct rc, no mutant needed),
and `MUTANT-VERDICT-RC` (a planted build that returns the clean rc at expiry regardless reproduces
the exact FWD-10 violation on demand, RED-first). All 8 round-4 arms re-confirmed green.

### 5. Deliverable + proof instance + surprise disarm

`comp-dataflow.fwd10.result.md` (a new, focused deliverable beside the round-4 audit, which stands
unmodified) quotes FWD-10 and the s.4.4 row verbatim, the rc vocabulary table, both EXERCISED runs,
and the bug-fix narrative. `NFRA_COMPEFFICACY-S16` appended to `INVESTIGATION_v1.md` as the S14
disarm carrier (hazard_standing INERT, disposition left for `3.0.0_SA_CVO`'s own L9 adjudication
per the TO's own words). Proof instance validated against `PROOF_OF_SPEC.schema.json` and
`.tools/proof-of-spec-check.py` before the `<status>` complete flip, which this seat commits itself.

---

## Acceptance (summary; full evidence in the deliverable + proof instance)

T25-AC1 (the bar quoted, rc vocabulary on --help + deliverable) PASS · T25-AC2 (EXERCISED, both
runs quoted, the pre-fix failure not hidden) PASS · T25-AC3 (origin zero-diff, cursor skip still
exact, item-9 untouched) PASS · T25-AC4 (battery 11/11, directory grain stated, commit-gate clean)
PASS · T25-AC5 (proof VALID, surprises entry resolves to S14 + S16, push state measured at report).

---

## Push State

Measured in the commit report to `2.0.0_SA_COO`, not asserted here.
