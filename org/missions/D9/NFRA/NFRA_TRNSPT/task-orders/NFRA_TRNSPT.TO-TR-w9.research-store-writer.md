# TO NFRA_TRNSPT.TO-TR-w9 -- the Research rows' store writer: held_out, stored-bytes verifier, reader compatibility (fake s3)

<to_id>NFRA_TRNSPT.TO-TR-w9</to_id>
<project>NFRA_TRNSPT</project>
<issued_to>0.9.0_WK_NFRA_TRNSPT~1</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>transcripts</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `TR-w-9` (`decompositions/NFRA_TRNSPT_DECOMP_R9.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`TR-w-9` (CTO round-8 analysis @08ff07562f, E1; ruling msg 1542): the 20,473 wiped Research rows land in `opal-data-transcripts` silver at
`lib/opal_naming.py address()`'s key, with residual-flag rows held out. You build and test the WRITER on a fake s3; the issuer runs the
real write after your merge.

**The code:**
- `data/transcripts/scripts/teams/research_fold.py` -- `build(paths)` -> `rows` (exactly `parse_silver.COLUMNS`), `per_file`,
  `failures`, `wipe_counts`, `residual_flags`. Utterance text goes through `outlook/wipe.py` `wipe_blocks(blocks, assets)` ->
  `(wiped_blocks, residual_flags, counts)`.
- `data/transcripts/scripts/teams/parse_silver.py` -- `_schema()` (:118), `_address(tier, series, meeting_date, name)` (:127),
  `write(...)` (:138, one KMS-encrypted parquet per transcript via `s3.put_object(..., ServerSideEncryption="aws:kms", SSEKMSKeyId=...)`).
- `data/transcripts/scripts/teams/read_meeting.py` -- `read_meeting(s3, series, meeting_date, speaker=None, grep=None)` (:58) lists the
  silver prefix and reads each parquet; `_clock(start_utc)` (:45).

**Build:**
1. `research_fold.py`:
   - add a per-row `held_out` (bool): TRUE when that utterance's wipe produced at least one residual flag. Rows now carry
     `COLUMNS + ["held_out"]`. Keep `build`'s other outputs; add `held_out_rows` (the count).
   - `write_all(result, *, s3, kms_key_arn, apply)` -> list of keys: one parquet per transcript at
     `parse_silver._address("silver", "research_meeting", meeting_date, "<transcript_id>.parquet")`, schema = `parse_silver._schema()`
     plus `("held_out", pa.bool_())`, written exactly like `parse_silver.write` (KMS, content type). `apply=False` builds and returns keys
     only. Refuse an empty transcript.
   - `verify_stored(s3, keys, assets=None)` -> `{"objects", "rows", "held_out_rows", "rewipe_counts"}`: reads each key back, and re-runs
     `wipe_blocks` on every NON-held-out row's text; `rewipe_counts` sums `name`, `id`, `email`, `phone`.
   - `main`: `--apply` (otherwise dry), `--verify`; the KMS key resolved like `parse_silver` (alias `alias/opal-data-transcripts`). Prints
     counts and keys only, never text.
2. `read_meeting.py`: ONLY if needed so it reads a research parquet whose `start_utc` is `None` (e.g. `_clock(None)` returns `None`).
   Change nothing else; its existing tests stay green.
3. `data/transcripts/scripts/tests/test_research_store.py`, using a fake s3 (a dict-backed client with `put_object`, `get_object`,
   `list_objects_v2`) and a synthetic structured json -- never real transcript text in the test:
   - `test_keys_equal_builder_and_held_out_column` -- `write_all(..., apply=True)` writes one object per transcript at exactly
     `lib.opal_naming.address("teams","transcripts","silver","research_meeting","date=<d>","<id>.parquet")`'s key, and the stored parquet
     has a `held_out` bool column with the right count;
   - `test_stored_bytes_rewipe_clean` -- after the write, `verify_stored` reports `rewipe_counts` name/id/email/phone all 0 on rows that
     carried planted tokens before the fold;
   - `test_read_meeting_reads_research_parquet` -- `read_meeting(fake_s3, "research_meeting", <d>)` returns the turns (start_utc None).

### ACCEPTANCE

<criterion id="TR9-w9-AC1" cell_refs="TR-w-9"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R9_CHECKS/r9_checks.py w9-write</invocation><expect>R9-W9-WRITE-OK</expect></criterion>
`TR9-w9-AC1` -- the three named tests pass on a fake s3.

<expected_criteria>TR9-w9-AC1</expected_criteria>

Dry-run at the base (box/dell2 2e53d2f87c): AC1 `R9-W9-WRITE-FAIL absent` -- FAIL as expected. Also keep `test_research_fold.py`,
`test_teams_read_meeting.py` and `test_teams_parse_silver.py` green. The real write, read-back and stored-bytes check are the issuer's.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder. Nothing else.
- **LOCAL.** No AWS call of any kind (no real s3, no KMS), no gateway, no HTTP. Never print, store or report transcript text. Do not edit
  another order's proof instance.
- **Refusal clause.** If `read_meeting` cannot read a research parquet without changing its behavior for Teams parquets, stop on that
  test and file a surprise row (id `NFRA_TRNSPT-D2-W1-S<k>`, next unused across every document under `surprise-channel/`).

<paths>
data/transcripts/scripts/teams/research_fold.py
data/transcripts/scripts/teams/read_meeting.py
data/transcripts/scripts/tests/test_research_store.py
data/transcripts/scripts/tests/test_research_fold.py
org/missions/D9/NFRA/NFRA_TRNSPT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_TRNSPT/decompositions/NFRA_TRNSPT_DECOMP_R9.md</decomp_doc> (round 9), cell `TR-w-9`.
<owned_cells>TR-w-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: TR9-w9-AC1. Instance at `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~1/NFRA_TRNSPT.TO-TR-w9.research-store-writer.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> TR9-w9-AC1` BEFORE the flip. Commit the code first, then pin each artifact to
a commit that actually contains it.
</proof_of_spec>

**REPORT:** the held_out row count from a dry `build` over the 29 files (a number), the check line, the three related suites' lines, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a writer tested on a fake s3; the served write is the issuer's TR-x-9.
comp-iam: DECLARED-NOT-APPLICABLE for the worker; the issuer measures PutObject and KMS encrypt at the act.
comp-adversary: RUN -- 4 modules read (research_fold, parse_silver :118-156, read_meeting :45-70, wipe :343); BLIND to the live bucket's prefix state and the dell2 user's KMS encrypt grant (both measured at the issuer's act). Traps: held_out counted as flags not rows, a hand-typed key, a Teams reader regression, transcript text in a test; the face fixes each.
lane: two teams modules, two test files, the investigation file.
</preflight>

Source: CTO round-8 analysis @08ff07562f E1; ruling msg 1542; decomposition round 9 cell TR-w-9 and issuer rulings 1-3.
