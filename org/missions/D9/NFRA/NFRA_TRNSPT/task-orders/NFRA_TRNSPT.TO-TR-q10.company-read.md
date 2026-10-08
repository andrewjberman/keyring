# TO NFRA_TRNSPT.TO-TR-q10 -- the analyst's company read over Research silver (held_out=false only)

<to_id>NFRA_TRNSPT.TO-TR-q10</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-q-10` (`decompositions/NFRA_TRNSPT_DECOMP_R10.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-q-10` (CTO round-9 analysis @9c6c91c505, E1): "a tested function that, given a company (name or ticker), returns the matching speaker
turns across the stored meetings (meeting, date, speaker, time, the wiped text), reading `held_out=false` rows only ... (2) a test showing
a held-out row is never returned; (3) a company named in no meeting returns an empty result with that reason."

**The data:** 29 parquet objects under `s3://opal-data-transcripts/teams/transcripts/silver/research_meeting/date=<YYYY-MM-DD>/<id>.parquet`,
columns `transcript_id, series, meeting_date, turn_index, speaker, start_utc, end_utc, start_s, end_s, text, held_out` (written by
`data/transcripts/scripts/teams/research_fold.py` `write_all`; schema `parse_silver._schema()` + `held_out`). The prefix and the per-key
address come from `parse_silver._address("silver", "research_meeting", <date>, <name>)` / `lib.opal_naming.address`; list the prefix with
the s3 client's `list_objects_v2` (paginate), read each with `get_object`. See `data/transcripts/scripts/teams/read_meeting.py` for the
existing list-and-read pattern and `research_fold.verify_stored` for the read-back pattern.

**Build:**
1. `data/transcripts/scripts/teams/research_read.py`: `company_turns(s3, company, *, aliases=(), bucket_prefix=<from the builder>)` ->
   `{"company", "terms", "meetings_scanned", "rows_scanned", "held_out_skipped", "matches": [{"transcript_id", "meeting_date", "speaker",
   "start_s", "text"}], "count", "reason"}`. Terms = `company` + `aliases`; a row matches when any term appears as a whole word,
   case-insensitive, in `text`. Rows with `held_out` TRUE are never examined for a match and never returned (count them in
   `held_out_skipped`). With no match: `matches` empty, `count` 0, `reason` = `"no stored non-held-out turn mentions <terms>"` (the text is
   wiped; say so in the reason). `main --company X [--alias Y ...] --counts-only`: prints counts per meeting and the total, never text,
   when `--counts-only`.
2. `data/transcripts/scripts/tests/test_research_read.py` on a dict-backed fake s3 holding two SYNTHETIC parquets (use `research_fold`'s
   schema), with at least: `test_held_out_row_never_returned` (a held_out=TRUE row that mentions the company is not in `matches`, and
   `held_out_skipped` counts it); `test_unnamed_company_empty_with_reason`; a positive test (an alias matches); a whole-word test ("ACME"
   does not match "ACMEX").

### ACCEPTANCE

<criterion id="TR10-q10-AC1" cell_refs="TR-q-10"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R10_CHECKS/r10_checks.py q10-read</invocation><expect>R10-Q10-READ-OK</expect></criterion>
`TR10-q10-AC1` -- the held-out and empty-with-reason tests pass by name.

<expected_criteria>TR10-q10-AC1</expected_criteria>

Dry-run at the base (box/dell2 f62d3f661e): AC1 `R10-Q10-READ-FAIL absent` -- FAIL as expected. The one real company query against S3 is the issuer's close.

## BOUNDS

- **Grant.** The two files below, this order's file, your deliverables folder and the investigation file.
- **LOCAL.** No AWS, gateway or HTTP call; synthetic test data only; never print or store real transcript text. Do not edit another
  order's proof instance.
- **Refusal clause.** If the stored schema cannot be read as described, file a surprise row (id `NFRA_TRNSPT-D2-W1-S<k>`, next unused
  across every document under `surprise-channel/`) and stop.

<paths>
data/transcripts/scripts/teams/research_read.py
data/transcripts/scripts/tests/test_research_read.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R10.md</decomp_doc> (round 10), cell `TR-q-10`.
<owned_cells>TR-q-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR10-q10-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-q10.company-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR10-q10-AC1` BEFORE the flip. Commit the code first, then pin each
artifact to a commit that actually contains it.
</proof_of_spec>

**REPORT:** the function signature, the test names, the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read function tested on a fake s3.
comp-iam: DECLARED-NOT-APPLICABLE for the worker; the issuer's live query uses dell2's Decrypt grant on the transcripts key (measured working at the round-9 read-back).
comp-adversary: RUN -- 3 modules read (research_fold write_all/verify_stored, parse_silver _schema/_address, read_meeting); BLIND to which companies the wiped text still names (the issuer picks one at close). Traps: a held-out row leaking through, a substring match, real text in a test or report; the face fixes each.
lane: one new module, one new test, the investigation file.
</preflight>

Source: CTO round-9 analysis @9c6c91c505 E1; decomposition round 10 cell TR-q-10.
