# TO NFRA_TRNSPT.TO-TR-x20 -- live read-only wiring so FWD-4 and FWD-9 can be exercised

<to_id>NFRA_TRNSPT.TO-TR-x20</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>communications</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-x-20` (`decompositions/NFRA_TRNSPT_DECOMP_R20.md`) | **outcome_ref:** FWD-4, FWD-9 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-x-20` (CTO ADDENDUM 10 item 2): FWD-4 and FWD-9 must be exercised once each on real stored bytes, but the tools built in round 19 take
injected readers only (`data/transcripts/scripts/query/securities_across.py`, TR-q-19) and `data/transcripts/scripts/teams/completeness.py`
has no one-meeting CLI. The issuer runs the exercises (TR-f-20) with this wiring; you build it on fakes.

**Build:**
1. `query/securities_across.py`: add READ-ONLY S3 reader factories (boto3 `get_object` / paginated `list_objects_v2` only) for the three sources:
   Teams + Research silver (non-held-out turns, through `teams/holdout.py` `visible_rows`), outlook `analysis_commentary` silver, and the
   commentary DRAFT store (a reader that returns no rows when the store is absent, stated in its docstring). The CLI `python -m
   data.transcripts.scripts.query.securities_across 2026Q3 --live` wires them; output is the per-security count table only.
2. `teams/completeness.py`: a CLI `--series <s> --date <YYYY-MM-DD> --live` that answers ONE meeting: "here" or its cause
   (never_recorded / expired / not_allowlisted / refused), loading `previously_listed` from the TR-e-19 snapshot loader; output is the cause line only.
3. `data/transcripts/scripts/tests/test_live_readers_exercise.py` (new, a fake S3 that RECORDS every call): `test_s3_readers_read_only` (no put,
   copy or delete call is ever made); `test_completeness_cli_one_meeting_cause` (one line, the cause); `test_securities_cli_counts_only` (no input
   text appears in the output).

### ACCEPTANCE

<criterion id="TR20-x20-AC1" cell_refs="TR-x-20"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R20_CHECKS/r20_checks.py x20</invocation><expect>R20-X20-OK</expect></criterion>
`TR20-x20-AC1` -- the three named tests pass and the file is green.

<expected_criteria>TR20-x20-AC1</expected_criteria>

Dry-run at the base (box/dell2 31b9816847): `R20-X20-FAIL absent` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** Fakes and synthetic fixtures only; no AWS, HTTP, plan or apply; no transcript, email or client content anywhere.
- **Refusal clause.** A builder refusal for a new name or address: add nothing typed; file a surprise row (`NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece.

<paths>
data/transcripts/scripts/query/securities_across.py
data/transcripts/scripts/teams/completeness.py
data/transcripts/scripts/tests/test_live_readers_exercise.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R20.md</decomp_doc> (round 20), cell `TR-x-20`.
<owned_cells>TR-x-20</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR20-x20-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-x20.live-readers-exercise.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR20-x20-AC1` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a local build, no schedule created.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no grant change.
comp-adversary: RUN -- sources: CTO ADDENDUM 10 @200cbac519, TR-q-19 and TR-e-19 as merged and the modules named in the face; BLIND to live data (fakes only). Traps: content in output or fixtures, a typed address, a behavior change in an existing reader; the face and the three named tests fix each.
lane: the paths block.
</preflight>

Source: CTO msg 3012 (ADDENDUM 10); decomposition round 20 cell TR-x-20.
