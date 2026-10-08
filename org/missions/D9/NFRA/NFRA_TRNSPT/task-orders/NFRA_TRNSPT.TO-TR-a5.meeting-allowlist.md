# TO NFRA_TRNSPT.TO-TR-a5 -- the meeting allowlist data asset (Monday meeting first)

<to_id>NFRA_TRNSPT.TO-TR-a5</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-a-5` (`decompositions/NFRA_TRNSPT_DECOMP_R5.md`) |
**outcome_ref:** FWD-1, FWD-2 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-a-5` (CTO round-4 analysis @856673477a, section 2, E1): "The meeting allowlist data asset (FWD-1, then FWD-2). A versioned file
in this project naming each regular investment meeting series by its stable identifier (the Monday meeting first), with the source
of each row." The gateway route `/hx/transcripts` is released but serves no meeting because its allowlist
(`TRANSCRIPT_MEETING_ALLOWLIST`, a whitespace/comma list of Graph online-meeting ids, `infra/aws/ec2/opal-gateway/app/config.py:238`,
read by `meeting_allowlist()` at `infra/aws/ec2/opal-gateway/app/transcript_route.py:87-89`) is empty. This file is the data the
gateway's owner will load; you do not touch the gateway.

**Where the identifiers come from (read-only):**
- `data/transcripts/scripts/teams/series.json` -- four rows under `"series"`, fields `table`, `online_meeting_id`, `teams_subject`,
  `organizer_name`, `id_prefix`. `table` values: `monday_meeting` (Teams subject "Morning Meeting"), `ocio_ic`,
  `asset_management_ic`, `research_meeting`.
- `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/TRANSCRIPT_REACH_RUN.json` -- the live run that read the same ids
  back from Graph: `meetings[]` with `meeting_id`, `teams_subject`, `list_status` (200 for the first three); `negative_arm` for the
  Research Team Meeting (403, not invited).

**Build:**
1. `data/transcripts/scripts/teams/meeting_allowlist.json`:
   ```
   {"_provenance": "<one line: what this is, who made it, from which files>",
    "version": 1,
    "meetings": [
      {"series": "monday_meeting", "teams_subject": "...", "online_meeting_id": "<exactly the series.json value>",
       "source": "data/transcripts/scripts/teams/series.json:<the line holding this row's online_meeting_id>",
       "reach": "200 <path>:<line of the reach-run row's list_status>"},
      ... ocio_ic, asset_management_ic, research_meeting (reach "403 <path>:<line>") ...
    ]}
   ```
   Order: `monday_meeting` FIRST, then the other three. All four rows: PRD FWD-2 reads "Every regular investment meeting arrives on
   its own, the Research Meeting included" (`org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md:32`). Copy each id from
   series.json byte for byte (load it with Python; never retype a 148-character id). Print the bytes at each cited line before you
   write it; the line must be the one that carries the value.
2. `data/transcripts/scripts/teams/meeting_allowlist.py`: `load(path=<the json above>) -> list[dict]`. It raises `ValueError` for a
   row with no or empty `online_meeting_id`, no or empty `source`, a `source` not of the form `<path>:<line>`, or a duplicate id;
   and `as_env_value(rows) -> str`, the ids joined by a single space (the shape `TRANSCRIPT_MEETING_ALLOWLIST` reads). Stdlib only.
3. `data/transcripts/scripts/tests/test_meeting_allowlist.py`, with at least: `test_reject_row_without_identifier`,
   `test_reject_row_without_source` (each against a temporary file), a test that the shipped file loads, has `monday_meeting`
   first, and its ids equal series.json's; and a test that `as_env_value` returns four space-separated ids.

### ACCEPTANCE

<criterion id="TR5-a5-AC1" cell_refs="TR-a-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R5_CHECKS/r5_checks.py a5-file</invocation><expect>R5-A5-FILE-OK</expect></criterion>
`TR5-a5-AC1` -- the file lists the Monday meeting first; every id equals series.json's; every source is a path:line that exists.

<criterion id="TR5-a5-AC2" cell_refs="TR-a-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R5_CHECKS/r5_checks.py a5-test</invocation><expect>R5-A5-TEST-OK</expect></criterion>
`TR5-a5-AC2` -- the test file passes and holds the two rejection tests by name.

<expected_criteria>TR5-a5-AC1, TR5-a5-AC2</expected_criteria>

Dry-run at the base (CLOUD 1e02ea542a): AC1 `R5-A5-FILE-FAIL absent`, AC2 `R5-A5-TEST-FAIL absent` -- FAIL as expected. The analysis's
third criterion (the handoff message id to MSTR) is the issuer's act after the merge; it is not yours.

## BOUNDS

- **Grant.** The three files above, this order's file, your deliverables folder and the investigation file. Nothing else is written.
- **LOCAL.** No gateway call, no Graph call, no HTTP request, no AWS call. The repo record only.
- Run `python -m pytest data/transcripts/scripts/tests/test_meeting_allowlist.py -q -p no:cacheprovider` from the worktree root.
- **Refusal clause.** If series.json and the reach-run record disagree on an id, use series.json's, write the row, and file a surprise
  row (id `NFRA_TRNSPT-W1-S<k>`, next unused across every document under `surprise-channel/`) naming both values' sources; never
  invent an identifier.

<paths>
data/transcripts/scripts/teams/meeting_allowlist.json
data/transcripts/scripts/teams/meeting_allowlist.py
data/transcripts/scripts/tests/test_meeting_allowlist.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ and
never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R5.md</decomp_doc> (round 5), cell `TR-a-5`.
<owned_cells>TR-a-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR5-a5-AC1, TR5-a5-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-a5.meeting-allowlist.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR5-a5-AC1,TR5-a5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the four rows (series, id first 6 characters, source, reach), the two check lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a data file and its loader; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- the trap is a retyped or truncated id; the face makes the copy programmatic and AC1 compares byte for byte against series.json.
lane: three new files under data/transcripts/scripts/, the investigation file.
</preflight>

Source: CTO round-4 analysis @856673477a section 2 E1; decomposition round 5 cell TR-a-5 and issuer rulings 1-3.
