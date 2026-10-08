# TO NFRA_TRNSPT.TO-TR-s8 -- FWD-5 first slice: the 29 Research transcripts as structured silver rows, under the wipe

<to_id>NFRA_TRNSPT.TO-TR-s8</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~2</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-s-8` (`decompositions/NFRA_TRNSPT_DECOMP_R8.md`, addendum 1) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-s-8` (CTO round-7 analysis @117ee1fa17, E2): "FWD-5, first slice: fold the 29 existing Research Meeting transcripts and their parser
into silver as structured speech (speaker, time, text), under the PII wipe. (1) 29 of 29 transcripts parsed into silver rows, with
per-file counts printed and 0 parse failures, or each failure named; (2) the planted-token wipe test passes on these rows; (3) one
transcript is read back as structured speech (speaker turns, counts only)." PRD FWD-5 (`org/missions/D9/NFRA/NFRA_TRNSPT/prd/NFRA_TRNSPT_PRD.md:46-49`):
"An analyst reads a transcript as structured speech, not a raw file".

**Inputs (read-only):**
- `research_transcripts/structured/*.json` -- 29 files. Keys: `transcript_id`, `meeting` (`date`, `series`, `start_utc`,
  `start_basis`, ...), `date_assignment`, `speakers`, `utterances` (each `seq`, `speaker`, `offset_s`, `offset_hms`, `derived_utc`,
  `text`), `counts`, `unparsed_lines`. Read `research_transcripts/README.md` (the three-clock trap: `derived_utc` is DERIVED from an
  operator-stated start, never observed).
- The silver row shape: `data/transcripts/scripts/teams/parse_silver.py:34-35` `COLUMNS = ["transcript_id", "series", "meeting_date",
  "turn_index", "speaker", "start_utc", "end_utc", "start_s", "end_s", "text"]`.
- The wipe: `data/transcripts/scripts/outlook/wipe.py` -- `load_assets()` (:147) and `wipe_blocks(blocks, assets)` (:343) ->
  `(wiped_blocks, residual_flags, counts)`; blocks are `{"kind", "text"}`. Its planted-token tests:
  `data/transcripts/scripts/tests/test_wipe_planted.py` (how tokens are planted and asserted).

**Issuer rulings for this cell:**
- **Speaker is kept; utterance TEXT is wiped.** `parse_silver.py:5-6` keeps staff names ("staff names are the data"); the analysis asks
  for the wipe. Both hold: the `speaker` column passes through unchanged; `text` goes through `wipe_blocks` (one block per utterance).
- **No observed wall clock exists for these files:** `start_utc` and `end_utc` are `None`; `start_s` = `offset_s`; `end_s` = the next
  utterance's `offset_s` in the same transcript, `None` for the last. `series` = `"research_meeting"`; `meeting_date` = `meeting.date`;
  `turn_index` = `seq`.
- **LOCAL:** rows are built in memory and written only to a local `--out` directory you pass; nothing goes to S3. The store's later home
  is undecided (PRD :154).

**Build:**
1. `data/transcripts/scripts/teams/research_fold.py` (stdlib + the existing `wipe` and `parse_silver.COLUMNS`):
   `build(paths) -> {"rows": [dict with exactly COLUMNS, in order], "per_file": {"<transcript_id>": n_rows}, "failures": [{"file",
   "error"}], "wipe_counts": {...summed}, "residual_flags": n}`. A file that fails to parse is listed in `failures` with its error, never
   skipped silently. `main --out <dir>`: writes `research_meeting_silver.parquet` (if pyarrow is importable; else JSONL) and
   `summary.json` (per-file counts, failures, wipe counts -- no text) into `<dir>`.
2. `data/transcripts/scripts/tests/test_research_fold.py`, at least: `test_planted_tokens_wiped_speaker_kept` (a SYNTHETIC structured
   json in `tmp_path` whose utterance text plants the token classes `test_wipe_planted.py` plants, and whose speaker is a staff-style
   name: after `build`, every planted token is gone from `text`, the speaker is unchanged); a test that rows carry exactly `COLUMNS` with
   `start_utc` `None`; a test that a malformed file is listed in `failures`.

### ACCEPTANCE

<criterion id="TR8-s8-AC1" cell_refs="TR-s-8"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R8_CHECKS/r8s_checks.py s8-all</invocation><expect>R8-S8-ALL-OK</expect></criterion>
`TR8-s8-AC1` -- 29 of 29 parse, 0 failures, rows carry exactly the silver COLUMNS, per-file counts sum to rows.

<criterion id="TR8-s8-AC2" cell_refs="TR-s-8"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R8_CHECKS/r8s_checks.py s8-wipe</invocation><expect>R8-S8-WIPE-OK</expect></criterion>
`TR8-s8-AC2` -- the planted-token wipe test passes on research rows; speaker kept.

<expected_criteria>TR8-s8-AC1, TR8-s8-AC2</expected_criteria>

Dry-run at the base (box/dell2 a1f2d9f43c): AC1 `FAIL import: ModuleNotFoundError`, AC2 `FAIL absent` -- FAIL as expected. If AC1 finds a
file that cannot parse, name it in `failures` and leave AC1 failing; do not drop the file. The read-back of one transcript as speaker turns
is the issuer's close act.

## BOUNDS

- **Grant.** The two new files below, this order's file, your deliverables folder and the investigation file. `research_transcripts/`,
  `parse_silver.py` and `wipe.py` are READ only.
- **LOCAL.** No AWS, gateway or HTTP call. Never print or record utterance text in your report, your deliverables or a row: counts only.
  Do not edit another order's proof instance.
- **Refusal clause.** If a ruled rule above cannot hold for some file, list the file in `failures` and file a surprise row (id
  `NFRA_TRNSPT-D2-W2-S<k>`, next unused across every document under `surprise-channel/`).

<paths>
data/transcripts/scripts/teams/research_fold.py
data/transcripts/scripts/tests/test_research_fold.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R8.md</decomp_doc> (round 8, addendum 1), cell `TR-s-8`.
<owned_cells>TR-s-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR8-s8-AC1, TR8-s8-AC2. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/NFRA_TRNSPT.TO-TR-s8.research-fold.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR8-s8-AC1,TR8-s8-AC2` BEFORE the flip. Commit the code first, then pin each
artifact to a commit that actually contains it.
</proof_of_spec>

**REPORT:** files parsed / failures, total rows, wipe counts by class (numbers only), the two check lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- an offline fold to a local directory.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- 4 sources read (29 structured JSON keys, README, parse_silver COLUMNS, wipe interface); BLIND to the transcripts' text quality and to the store's later home. Traps: derived_utc passed off as observed (ruled None), speaker names wiped (ruled kept), utterance text leaking into a report; the face fixes all three.
lane: one new module, one new test, the investigation file.
</preflight>

Source: CTO round-7 analysis @117ee1fa17 E2; decomposition round 8 addendum 1, cell TR-s-8.
