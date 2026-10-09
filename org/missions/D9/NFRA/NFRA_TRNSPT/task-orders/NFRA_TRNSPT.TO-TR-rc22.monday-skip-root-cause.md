# TO NFRA_TRNSPT.TO-TR-rc22 -- why did the pull skip the 4 oldest Monday meetings? Name the code line, replay the skip, state the scheduled verdict

<to_id>NFRA_TRNSPT.TO-TR-rc22</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>census</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-rc-22` (`decompositions/NFRA_TRNSPT_DECOMP_R22.md`, AMENDMENT 1) | **outcome_ref:** FWD-3 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-rc-22` (CTO ADDENDUM 13.1): the gateway lists 20 `monday_meeting` transcripts. 16 landed in bronze and silver. The 4 OLDEST never did:
created 2026-04-10, 04-13, 05-04 and 06-01. Every one from 2026-06-08 on landed. The full listing, ids and times only, is the fixture
`org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R22_MONDAY_LISTING_FIXTURE.json`.

Two code paths could have landed them; READ both:
- **The scheduled pull:** `data/transcripts/scripts/teams/` (the pull handler and its listing/selection; `listing_snapshot.py`).
- **The earlier 365-day backfill (TO-RUN-b17):** find its entry point from that order under `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/`
  and its result file.

Candidate causes: a lookback window, occurrence enumeration, recurring-series expansion, or a filter.

**Build:**
1. `data/transcripts/scripts/tests/test_monday_skip_replay.py`. It loads the fixture and replays it through the REAL selection functions,
   with the clock and any state injected; no AWS, no HTTP:
   - `test_replay_skips_exactly_the_four`: the selection that decided what to land drops exactly those 4 ids and keeps the other 16.
   - `test_skip_names_its_code_line`: it asserts the cause through the function and constant you identify, so a change to that line flips
     the test. Write the file:line in the test's docstring.
   - `test_scheduled_path_verdict_stated`: it asserts whether the SCHEDULED pull, run tomorrow, would skip a meeting that is older than its
     window yet still listed, or whether it lands only new ones by design. The assertion encodes your verdict, and the docstring states it.
2. `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/R22_ROOT_CAUSE.md`: the code line, which path skipped them, the
   verdict for the scheduled path, and the smallest fix if the scheduled path would skip again. Do not make the fix.

### ACCEPTANCE

<criterion id="TR22-rc22-AC1" cell_refs="TR-rc-22"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R22_CHECKS/r22_checks.py rc22</invocation><expect>R22-RC22-OK</expect></criterion>
`TR22-rc22-AC1` -- the three named tests pass and the file is green.

<expected_criteria>TR22-rc22-AC1</expected_criteria>

Dry-run at the base: `R22-RC22-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL, read-only.** No code change to the pull or the backfill. No AWS or HTTP. No transcript text anywhere: ids and times only.
- If the cause cannot be pinned from the code, file a surprise row (`NFRA_TRNSPT-D2-W2-S<k>`, next unused across every document under
  `surprise-channel/`) naming what is missing, and stop.

<paths>
data/transcripts/scripts/tests/test_monday_skip_replay.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R22.md</decomp_doc> (round 22, AMENDMENT 1), cell `TR-rc-22`.
<owned_cells>TR-rc-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR22-rc22-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-rc22.monday-skip-root-cause.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR22-rc22-AC1` BEFORE the flip. Commit first, then pin.
</proof_of_spec>

**REPORT:** the code line, which path skipped, the scheduled verdict, the smallest fix if needed, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only replay.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- sources: CTO ADDENDUM 13.1 @5d09b81be3, the census @ac982db915, the listing fixture; BLIND to Graph state. Traps: a cause asserted without replay, a fix slipped into a diagnosis cell, content in the fixture; the tests and the bounds fix each.
lane: the paths block.
</preflight>

Source: CTO msg 3840 (ADDENDUM 13.1); decomposition round 22 AMENDMENT 1, cell TR-rc-22.
