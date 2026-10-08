# TO NFRA_TRNSPT.TO-TR-h7 -- FWD-4 completeness: match within +/-1 day, never 2

<to_id>NFRA_TRNSPT.TO-TR-h7</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-h-7` (`decompositions/NFRA_TRNSPT_DECOMP_R7.md`) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-h-7` (CTO round-6 analysis @57d1574255, E3): "FWD-4's date matching ... occurrences matched with a stated plus or minus 1-day
tolerance ... (2) a test showing a 2-day offset is NOT matched." Round 6's live record graded two Monday occurrences (2026-07-20,
2026-09-07) `never_recorded` while the same series holds a transcript dated the NEXT day (2026-07-21, 2026-09-08): the builder matched
exact dates only.

**The code:** `data/transcripts/scripts/teams/completeness.py` -- `build(inputs)` classifies each occurrence by exact `(series, date)`
membership in `bronze`, `listed_now` and `previously_listed`; precedence here > refused > not_allowlisted > expired > never_recorded;
`validate_rows`; `main`. Its tests: `data/transcripts/scripts/tests/test_completeness.py` and the fixture
`data/transcripts/scripts/tests/fixtures/completeness/inputs.json` (do not change the fixture's existing rows' expected causes).

**Build:**
1. `completeness.py`: add `match_tolerance_days` (input key, default 1; refuse a value < 0 or > 1 with `ValueError`). An occurrence matches
   an evidence entry (bronze, listing or prior listing) of the SAME series whose date is within `match_tolerance_days` of it. Nearest date
   first (exact before +/-1; on a tie, the earlier date). ONE evidence entry satisfies at most ONE occurrence (consume it). When a match is
   not exact, the row's `basis` says so (e.g. `"bronze (+1 day: 2026-07-21)"`). The record carries `"match_tolerance_days"`.
2. `test_completeness.py`, adding by name:
   - `test_one_day_shift_matched` -- an occurrence on D with bronze on D+1 (no evidence on D) is `here`, basis names the shift;
   - `test_two_day_offset_not_matched` -- an occurrence on D with bronze only on D+2 is NOT `here` (it is `never_recorded`);
   - a consume test: two occurrences D and D+1 with ONE bronze entry on D+1 -> exactly one `here`.
   All existing tests stay green.

### ACCEPTANCE

<criterion id="TR7-h7-AC1" cell_refs="TR-h-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R7_CHECKS/r7_checks.py h7-match</invocation><expect>R7-H7-MATCH-OK</expect></criterion>
`TR7-h7-AC1` -- the completeness tests pass, including the one-day-shift and two-day-negative tests by name.

<expected_criteria>TR7-h7-AC1</expected_criteria>

Dry-run at the base (CLOUD 4839b6f2d2): AC1 `R7-H7-MATCH-FAIL missing test_one_day_shift_matched, test_two_day_offset_not_matched` -- FAIL
as expected. The live record's re-run (the two suspected shifts printed, counts per cause) is the issuer's close act.

## BOUNDS

- **Grant.** `completeness.py`, `test_completeness.py`, this order's file, your deliverables folder and the investigation file.
- **LOCAL.** No AWS, gateway or HTTP call. Do not edit another order's proof instance.
- **Refusal clause.** If the consume rule makes an existing fixture expectation change, stop on AC1 and file a surprise row
  (id `NFRA_TRNSPT-D2-W2-S<k>`, next unused across every document under `surprise-channel/`).

<paths>
data/transcripts/scripts/teams/completeness.py
data/transcripts/scripts/tests/test_completeness.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R7.md</decomp_doc> (round 7), cell `TR-h-7`.
<owned_cells>TR-h-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR7-h7-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-h7.date-matching.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR7-h7-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the matching rule as built (one line), the new test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- an offline builder.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- 3 files read (completeness.py, its test, its fixture); BLIND to the live inputs (the issuer's close re-run). Traps: one bronze entry satisfying two occurrences, a tolerance quietly wider than 1, and a changed fixture expectation; the face fixes the consume rule, caps the tolerance and freezes the fixture.
lane: two files under data/transcripts/scripts/, the investigation file.
</preflight>

Source: CTO round-6 analysis @57d1574255 E3; decomposition round 7 cell TR-h-7 and issuer ruling 4.
