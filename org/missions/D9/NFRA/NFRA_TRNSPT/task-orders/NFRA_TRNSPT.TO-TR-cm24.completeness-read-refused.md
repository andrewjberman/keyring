# TO NFRA_TRNSPT.TO-TR-cm24 -- the completeness table answers `refused` for a meeting that is listed and whose content read was refused

<to_id>NFRA_TRNSPT.TO-TR-cm24</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>completeness</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-cm-24` (`decompositions/NFRA_TRNSPT_DECOMP_R24.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-cm-24` (CTO round-24 analysis, item 2). One module and three tests in the transcripts scripts.

**The defect.** `data/transcripts/scripts/teams/completeness.py` gives every meeting occurrence exactly one cause from `CAUSES`
(`here`, `refused`, `not_allowlisted`, `expired`, `never_recorded`). `build(inputs)` reaches `refused` only through `series_refused` (a whole
series whose LISTING was refused). A meeting that Microsoft LISTS but whose CONTENT read the gateway refuses (502, "READ-REFUSED") is in
`listed_now`, its series is on the allowlist, and it is not in bronze, so `build` falls to the line
`raise ValueError("unclassifiable: listed, allowlisted, not in bronze")`. Four real meetings (monday_meeting 2026-04-10, 04-13, 05-04,
06-01) are in exactly this state, so `python data/transcripts/scripts/teams/completeness.py --live --series monday_meeting --date 2026-04-10`
crashes with that ValueError today. The table must answer `refused`, never crash and never a blank.

**The evidence that exists.** Every Teams pull writes a run record at
`opal_naming.address("teams", "transcripts", "state", "pull_runs", "run=<started_utc>", "run.json")` (see `pull.py` line 230). Its
`series` list holds one dict per series with `table` and `outcomes`; a refused content read is an outcome
`{"transcript_id": "MM-20260601-0843", "outcome": "READ-REFUSED", "detail": "GatewayGraphError status=502"}`. The meeting date is the
8-digit group inside the transcript id (`-20260601-` -> `2026-06-01`). The latest run record (the greatest `run=<started_utc>` key) is the
evidence for the latest stored pull, the same vintage `live_inputs` already uses for `listed_now` (the latest listing snapshot).

**What to build.**

1. `build(inputs)` accepts an optional input `read_refused`: a list of `{"series", "date"}` (default empty). Precedence: right after the
   `series_refused` branch and before `not_allowlisted`, a meeting whose `(series, date)` is matched by `read_refused` (use the existing
   `_match` with the same tolerance, as `listed_now` does) gets cause `refused` and basis `"read_refused at the latest stored pull"` (with
   the existing `_basis` shift text when the match is one day off). `here` still beats it. A listed, allowlisted meeting with NO read-refusal
   evidence still raises `unclassifiable` exactly as today (that is the control; do not weaken it).
2. `live_inputs(s3, series, date)` fills `read_refused`: list the `pull_runs` class prefix (derive it from the builder's own output for a
   run address, the way `listing_snapshot.prefix_address()` derives its prefix; type no address), take the greatest `run.json` key, read it,
   and for the entry of `series` whose `table` equals the `series` argument collect each outcome `READ-REFUSED` as `{"series", "date"}` from
   its `transcript_id`. No run record present -> an empty list (no error). Read-only calls only: `list_objects_v2`, `get_object`.
3. Tests, three named exactly:
   - In `data/transcripts/scripts/tests/test_completeness.py`: `test_read_refused_listed_meeting_is_refused` (a listed, allowlisted meeting
     absent from bronze with a matching `read_refused` entry gives cause `refused`, a basis containing `read_refused`, and `validate_rows`
     passes) and `test_listed_without_read_refusal_still_raises` (the same meeting with `read_refused` empty raises `ValueError` with
     `unclassifiable`).
   - In `data/transcripts/scripts/tests/test_live_readers_exercise.py`: `test_completeness_cli_read_refused_from_run_record`, on the file's
     `RecordingS3` fake: seed one listing snapshot that lists `monday_meeting` on `2026-06-01` and one `run.json` whose `monday_meeting` entry
     has a `READ-REFUSED` outcome with transcript id `MM-20260601-0843`; `cp.main(["--series", "monday_meeting", "--date", "2026-06-01",
     "--live"], s3=s3)` prints exactly `monday_meeting 2026-06-01 refused`; the fake saw only `get_object` and `list_objects_v2` calls
     (reuse the file's `_assert_reads_only`). Add the seed as a small `_seed_run_record` helper beside `_seed_snapshots`; do not change the
     existing seeds, so the existing tests there keep their current expectations.
4. Do NOT edit `pull.py` or any Lambda handler. Do NOT deploy. The pull's own record is the evidence; nothing writes new state.

### ACCEPTANCE

<criterion id="TR24-cm24-AC1" cell_refs="TR-cm-24"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R24_CHECKS/r24_checks.py cm24</invocation><expect>R24-CM24-OK</expect></criterion>
`TR24-cm24-AC1` -- the three named tests exist and the three completeness test files (`test_completeness.py`,
`test_live_readers_exercise.py`, `test_listing_snapshot_expired.py`) pass together.

<criterion id="TR24-cm24-AC2" cell_refs="TR-cm-24"><invocation>python data/transcripts/scripts/teams/completeness.py --live --series monday_meeting --date 2026-06-01</invocation><expect>monday_meeting 2026-06-01 refused</expect></criterion>
`TR24-cm24-AC2` -- the seam against its real neighbour: the stored S3 state (read-only list and get). If this shell has no AWS credentials,
report that in the final message and file a surprise row; the issuer re-grades AC2 at the drain.

<expected_criteria>TR24-cm24-AC1,TR24-cm24-AC2</expected_criteria>

Dry-run at the base: AC1 `R24-CM24-FAIL missing test_read_refused_listed_meeting_is_refused, test_listed_without_read_refusal_still_raises,
test_completeness_cli_read_refused_from_run_record` -- FAIL as expected. AC2 raises `ValueError: unclassifiable: listed, allowlisted, not in
bronze` -- FAIL as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **LOCAL.** The only outside contact is AC2's read-only S3 list and get through the module's own boto3 client. No put, no copy, no delete,
  no Lambda or Terraform call, no deploy. ASCII only. No transcript text: dates, series and ids only.
- Run ONLY the acceptance checks and the three named test files. Do NOT run the whole tests directory: another test there rewrites a tracked
  fixture. If `git status` shows a path outside your grant modified, restore it with `git checkout -- <path>` before committing.
- If the run record does not carry what step 2 needs (a different shape from the one named above), file a surprise row
  (`NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document under `surprise-channel/`) naming the shape you found, and stop on that
  criterion.

<paths>
data/transcripts/scripts/teams/completeness.py
data/transcripts/scripts/tests/test_completeness.py
data/transcripts/scripts/tests/test_live_readers_exercise.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R24.md</decomp_doc> (round 24), cell `TR-cm-24`.
<owned_cells>TR-cm-24</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR24-cm24-AC1, TR24-cm24-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-cm24.completeness-read-refused.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR24-cm24-AC1 TR24-cm24-AC2` BEFORE the flip. Commit first, then pin.
</proof_of_spec>

**REPORT:** the lines changed in `completeness.py`, each test touched and why, the three new test names with pass or fail, the two check
lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a repo build with no deploy; the table is a CLI a seat runs.
comp-iam: DECLARED-NOT-APPLICABLE -- the only AWS contact is a read-only S3 list/get by the seat's own credentials through the module's existing client.
comp-adversary: RUN -- sources: the CTO round-24 analysis @8905ffd1fa item 2, the issuer's base run of AC2 (ValueError unclassifiable) and of the four round-23 run records (`READ-REFUSED` x4 on every fire since 2026-10-11T03:38Z). Traps: reading the FIRST run record instead of the latest (sorted key order is the vintage); a series entry matched by position instead of `table`; a one-day-shifted match consuming a neighbour's entry. BLIND: a meeting refused on an earlier pull and no longer listed (it reaches `expired`, not `refused`, by the existing rule).
lane: the paths block.
</preflight>

Source: CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_24_20261012.md section 4 item 2; decomposition round 24, cell TR-cm-24.
