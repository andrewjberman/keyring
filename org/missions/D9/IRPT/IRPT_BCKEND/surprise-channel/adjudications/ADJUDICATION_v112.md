# IRPT_BCKEND: CVO adjudication, workstream ~PB round 1 -- the performance positive control GATE (IB-pr-568)

<sweep_watermark>2026-10-15T10:22Z</sweep_watermark>

PASS/FAIL gate by `3.0.0_SA_CVO~IRPT`, 2026-10-15T10:22Z, on msg 8228, set by the CTO's round-6 analysis @41f22e06b8 (IB-pr-568 AMENDMENT 4). Graded object: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB208-1_performance_control.json` @7dbd922900 (unchanged at HEAD), against `ORION_RECUT_PAIRS_PACKET_V3.md` sha256 03a77b33174c. Every check below was re-derived by this seat; no claim in the control was taken. No AWS write was made (read-only `head-object`, `list-objects-v2`, `get-object` to scratch).

**VERDICT: PASS.** The performance days of IB-pr-568 may proceed on V3's conditions.

1. **Which bytes run: PASS.** The chain copy `s3://opal-data-inf/code/gold/pull_inflection_performance_rest.py` (29,230 bytes, LastModified 2026-07-07, VersionId hb0YrCaD..., sha256 8f291d0c...) was fetched and diffed by content against the repository script (29,784 bytes, sha256 ecba0fa6...): 14 differing lines, all in `_load_inflection_client_ids` (repository: delegates to `_hh_universe.load_household_universe`; chain: the inline `isdigit` derivation). No request, window, field, mode or write line differs. Both loaders run here on today's snapshot (`silver/api_dims/household_rep_mapping/snapshot_date=2026-10-14`, 320 rows, `household_id` Int64): 320 ids each, identical sets, 0 non-digit renders. Branch `repo_script_matches`: the REPOSITORY script runs the 22 days, not the chain copy. The run worktree `C:/dev/wk-ib568-run` holds byte-identical `pull_inflection_performance_rest.py` (ecba0fa6...) and `_hh_universe.py` (a262e138...) to HEAD.
2. **Dry run made 0 writes: PASS.** The dry-run output (`C:/dev/wk-ib568-run/data/inf/manual_api/pulls/2026-10-14_inflection_performance_rest.jsonl.gz`, 4,648,849 bytes, written 10:14Z) is local. `bronze/performance/` lists 185 objects (twice, same count); none is dated 2026-10-15; the newest is the chain's own 2026-10-14 key at 2026-10-14T11:48:57Z. The script's only `put_object` (line 640) sits after `if args.dry_run: return` (line 634); its other S3 write, `limiter.persist_state()` (line 586), was no-op'd by the wrapper and `orion/rate_limit_state_performance.json` still reads 2026-10-14T11:48:55Z.
3. **Schema: PASS.** Full-file read of both (not only the leading record): every row of both carries exactly `client_id`(int), `date`(str), `factor`(float), `pull_date`(str) in that order; gzip, one JSON object per line; `pull_date` = 2026-10-14 on every row of both.
4. **The 3.8% gap: PASS, and it is neither content nor rows.** Rows 482,971 vs 482,971; the same 315 clients (0 only-one-side); the same (client, date) keys (0 only-one-side, 0 duplicates), in the same order; date span 2020-05-26..2026-10-14 on both. Uncompressed bodies differ by 3 bytes (43,294,484 vs 43,294,481). So the 3.8% is the compressor, not the data (both max-compression headers; the local file has mtime 0, a different zlib build). The only content difference: 311 `factor` values (283 clients), all dated 2026-10, i.e. the vendor's restatement of recent days seen by a later pull. No missing or extra column, no different account set.
5. **Write set inside V3: PASS.** V3 at HEAD hashes 03a77b33174c3fb9e84d925dcbf32bfbdb7fb366efa9470fae01cc7afac2dc1c, the hash both halves carry (v110). Its 22 performance days (2026-05-04..05-08, 05-11, 07-01, 07-02, 07-06, 07-07, 07-09, 07-13..15, 07-21..23, 08-06, 09-28..30, 10-13) are all trading days (`lib/trading_calendar.py`) and all absent now (0 of 22 present in the 185-object listing); each write is the one key `bronze/performance/<day>.jsonl.gz` (line 639), one per run, the state write no-op'd; 2026-10-14 is a dry-run day only and is present, so it is not in the write set.

**Observations for the record (not failures).** (a) A backfilled past day carries the vendor's values as of the backfill pull, not as of that day (here 311 recent values moved between a 10-14 and a 10-15 pull); this is inherent to V3's design and the record should say so per key. (b) The control file read only the leading record and left the size gap unresolved; resolved here. (c) The dry-run output with client figures sits untracked in the run worktree's `pulls/`; it joins the scratch awaiting Andrew's delete.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S20",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T10:22:00Z",
  "one_line": "GATE PASS: the performance positive control org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB208-1_performance_control.json @7dbd922900, graded independently on all five checks. (1) Chain copy vs repo script diffed by content: 14 lines, only the client-id loader; both loaders give the same 320 ids today; the repository script runs. (2) 0 writes: no 2026-10-15 object among 185 under bronze/performance/, the put is behind the dry-run return, the limiter state key unchanged since 10-14. (3) Schema equal on every row of both files. (4) The 3.8% gap is compression: same 482,971 rows, same 315 clients and keys, uncompressed bytes within 3; 311 recent factor values restated by the later pull. (5) The 22 performance days are trading days, all absent, inside V3 at its signed hash 03a77b33. IB-pr-568 may write performance days. Closes D2-W409-S2 (the performance chain copy differs, so a positive control was owed): the control is done and passes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W409-S2"
  ],
  "spec_asserts": "CTO round-6 analysis @41f22e06b8 and IB-pr-568 AMENDMENT 4: no performance day is written until the CVO grades the performance control; CLAUDE.md rule 22a: deployed bytes are compared by content, never by filename; never-widen: the act's write set sits inside both signed halves at the packet's current hash.",
  "world_is": "The repository script, byte-identical in the run worktree, produces the chain's shape for a present day; the dry run wrote nothing to S3; the 22 target keys are absent and inside V3. Backfilled days will carry vendor values as of the backfill pull.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "aws s3api head-object + s3 cp s3://opal-data-inf/code/gold/pull_inflection_performance_rest.py (29,230 B, sha256 8f291d0c...); diff against data/inf/manual_api/pull_inflection_performance_rest.py (29,784 B, sha256 ecba0fa6...): 14 lines, lines 179-187 vs 179-183, _load_inflection_client_ids only",
    "scratch loaders.py on silver/api_dims/household_rep_mapping/snapshot_date=2026-10-14/data.parquet: repo 320, chain-logic 320, equal sets, 0 non-digit",
    "aws s3api list-objects-v2 opal-data-inf bronze/performance/ at 2026-10-15T10:1xZ and 10:22Z: 185 objects; none LastModified 2026-10-15; orion/rate_limit_state_performance.json 2026-10-14T11:48:55Z",
    "data/inf/manual_api/pull_inflection_performance_rest.py:586 persist_state, :634 dry_run return, :640 put_object",
    "scratch compare.py, full read of C:/dev/wk-ib568-run/data/inf/manual_api/pulls/2026-10-14_inflection_performance_rest.jsonl.gz vs s3://opal-data-inf/bronze/performance/2026-10-14.jsonl.gz: 482,971 rows each, one key order and one type signature each, 315 clients each, 0 key differences, 311 factor differences all in 2026-10, uncompressed 43,294,484 vs 43,294,481 bytes",
    "sha256sum ORION_RECUT_PAIRS_PACKET_V3.md = 03a77b33174c3fb9e84d925dcbf32bfbdb7fb366efa9470fae01cc7afac2dc1c; V3 lines 62-63 list the 22 days; lib/trading_calendar.py: all 22 trading days",
    "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-568...md steps 4-5 and AMENDMENT 4"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "D2-W409-S2 owed a positive control before any performance day; the control is graded here and passes all five checks, so the row's hazard is discharged."
 }
]
```
