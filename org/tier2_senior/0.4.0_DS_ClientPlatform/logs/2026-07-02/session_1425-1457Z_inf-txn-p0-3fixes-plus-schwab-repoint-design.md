# INF txn P0 (3 fixes) + Schwab -> daily-box re-point design
**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, DEPLOY, COORDINATE

**Serial:** 0.4.0_DS_ClientPlatform~A | **Window:** 2026-07-02T14:25Z -> 14:57Z | **Driver:** COO [DRIVE] redirect (P0 preempts) then resume; CTO arch-gate ruling; 0.6.1 handoffs.

## Current State (handoff surface)

### A. INF nightly P0 -- daily gold chain hard-failing at step 10/63 since 06-30 (RESOLVED, 3 fixes)

Root cause (two-layer, both landed): the ADVI_INFREF LEG-2 de-convert (94042ebf1) switched the txn bronze from `.parquet` to raw `{date}.jsonl.gz` but left two `.parquet`-era assumptions:

1. **Txn-pull root bug (the deterministic cause of absent bronze).** `data/inf/manual_api/pull_inflection_transactions_rest.py:461` did `.replace(".parquet","")` -- a NO-OP on a `.jsonl.gz` key -> `prior_date="2026-06-30.jsonl.gz"` -> `dt.date.fromisoformat()` ValueError -> `INF_API_PULL_TXN` exited 1 at 296.9s BEFORE writing bronze. Fix: `-> .split(".")[0]`. **Commit 6aaa395f5**, deployed `s3://opal-data-inf/code/manual_api/...` (ETag 78f60cc7==md5). Diagnosed by 0.6.1_AE_PartnerETL (owned-paths blocked their commit -- POD4 = DS rule-13 lane); I verified the staged diff was EXACTLY the 1-line fix + comment before committing under my author line.

2. **Converter crash-fix (the amplifier).** `data/inf/scripts/silver/convert_transactions_to_silver.py` `_read_bronze` did an unguarded `s3.get_object` -> NoSuchKey on absent bronze -> this NON-pull silver step returned rc!=0 -> `orion-gold-dispatch.sh` HARD-ABORTED the 63-step chain at 10/63 (dispatch tolerates `INF_API_PULL_*` but not silver steps). Fix: `_read_bronze` returns None on NoSuchKey (mirrors the INF_C_* idiom); `main()` DEFERs. **Commit 0addf7c7f**, deployed `code/silver/`.

3. **CTO-policy detection-limb** (per the CTO arch-gate ruling + CVO verify-channel finding that a WARN-only DEFER silently rolls forward stale txn behind a GREEN sentinel). The DEFER path now: carry-forward the prior partition (INF_A_-1 `_load_canonical_snapshot` latest-selects by LastModified -- verified) + emit `ChainStepDegraded=1` + `TxnSilverStalenessDays` gauge to **Inflection/GoldChain** (dims `Service=inf-gold-layer-runner,Step=INF_API_SILVER_TXN` -- the IAM-scoped namespace) + FAIL-LOUD-BLOCK (rc=1) if the latest partition is > **N=2 trading days** behind (env `TXN_SILVER_STALENESS_CEILING_DAYS`, TUNABLE) or if no prior partition exists. **Commit b7dc964db**, deployed `code/silver/` (ETag 70110fbe==md5). Tested live: DEFER @2-days-stale -> rc=0 + metric; BLOCK @>ceiling -> rc=1.

**Live effect:** `sync_scripts` pulls both from S3 each run. 0.6.1 re-dispatches `--chain full` -> fresh 07-01 txn bronze (their extended-timeout pull + the pull-fix) -> clean 63-step + sentinel = the 2-page (Inflection + MDPF) un-freeze. If a future pull slips, the guard degrades gracefully (carry-forward + alarm + N=2 ceiling) instead of freezing 2 pages. NB: 07-02 bronze is currently absent, so tonight's chain would DEFER at 2-days-stale (within ceiling) if not re-pulled -- exactly the intended graceful degradation. RAVC'd CTO (arch-gate) + 0.6.1 + COO + CVO.

### B. Schwab -> daily-box (SchwabAutoDownload) re-point -- enumeration + durability design (DELIVERED)

Andrew-strategic (COO [DRIVE]): design re-pointing schwab-fed processes to the daily box vs the lagging manual batch. Brief: **docs/briefs/schwab-daily-box-repoint-durability-design-20260702.md** (368c3ad0b). Enumeration (2 Explore agents): ~15 consumers of `opal-data-bd/schwab/silver/*` (prime `schwab/silver/rps` -> MDPF WS-E + leg-2 + 3 BD gold + 3 Lambdas; portal zero direct reads). Lag root-cause: PATH A has NO auto-trigger (manual /49-schwab-conv); SI2 daily box lands to `01_raw_quartz_validation/` (prod-`01_raw` repoint HELD N=5); TRN Layer-A reads LOCAL disk. 3-component design (C1 automate the daily conversion trigger; C2 resolve the raw-source seam w/ 0.6.2; C3 fix the TRN local-disk read) + 4 open arch-gate decisions. Non-blocking-on / complementary-to DATA_SSOTMG (cadence vs shape). NO implementation until the CTO arch-gate. RAVC'd COO CC CTO+CVO. Also shared the SI2-runs-to-validation finding with 0.6.2 (CC CVO) -> they ground-truthed it live (box running, repoint held; re-fired SchwabS3Sync so CRS20260701 now in the validation prefix).

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| comp-grep | INF_API_SILVER_TXN / bronze/transactions / silver/transactions | PASS | located the chain step + converter + downstream consumers |
| comp-grep/comp-glob | schwab/silver, canonical/schwab, DATA_SSOTMG docs | PASS | seeded the 2 Explore enum agents + found the SSOTMG PRD |
| comp-pipescript deployed | --pipeline inf | PASS | converter deploy target = code/silver/; MATCH post-deploy |
| ds-commit-gate | convert_transactions_to_silver.py, pull_inflection...rest.py | PASS | clean on all commits |

**What worked:** mirroring the existing INF_C_* NoSuchKey idiom + the dispatch's own INF_API_PULL_* tolerate-contract made the guard idiomatic; grounding INF_A_-1's latest-select (Rule 22) proved option-b safe before committing. **What failed:** none. **Gap:** none new.

## MCP Traffic (summary)
~14 messages. Significant received: COO [DRIVE] P0 redirect + [DRIVE] prioritize pull-fix + RAVC-ACKs; CTO [RULING] chain-robustness policy (arch-gate); CVO [verify-channel] detection-limb finding; 0.6.1 [COORD] + [HANDOFF] pull-fix; 0.6.2 confirm. Sent: RAVCs to CTO/COO/CVO/0.6.1 (both P0 fixes), 0.6.2 SI2 finding, brief RAVC to COO CC CTO+CVO.

## Files Modified (see commit messages)
- `data/inf/scripts/silver/convert_transactions_to_silver.py` @ 0addf7c7f (crash-fix) + b7dc964db (CTO-policy detection-limb) -- deployed code/silver/ (ETag 70110fbe==md5).
- `data/inf/manual_api/pull_inflection_transactions_rest.py` @ 6aaa395f5 (ext-strip root fix) -- deployed code/manual_api/ (ETag 78f60cc7==md5).
- `docs/briefs/schwab-daily-box-repoint-durability-design-20260702.md` @ 368c3ad0b (design brief).

## Blockers
NONE. INF P0 fixes all landed+verified; 0.6.1 owns the `--chain full` re-dispatch + sentinel confirm. Schwab re-point awaits the CTO arch-gate (COO convening) -- IMPORTANT-not-urgent, not a blocker.

## Next Steps
- [0.6.1_AE_PartnerETL] Re-dispatch `--chain full` -> confirm fresh 07-01 txn bronze + clean 63-step + sentinel = the 2-page un-freeze; ping the chain result.
- [1.0.0_SA_CTO] Arch-gate: (a) the INF_API_SILVER_TXN guard vs the ruled policy + confirm N=2 vs gold txn-consumer tolerance; (b) the schwab re-point brief (4 open decisions).
- [3.0.0_SA_CVO] Verify-channel: the guard's alarm+ceiling on the next INF nightly; the ChainStepDegraded metric needs an AE-wired alarm (currently emitted, no alarm yet).
- [2.0.0_SA_COO] Convene the schwab re-point arch-gate when ready; C2/C3 depend on 0.6.2 (SI2->01_raw repoint + the box's CRS*.TRN delivery set).
- [0.4.0_DS_ClientPlatform~A] MDPF flip preempts if post-flip parity/rollback co-witness needed (leg-2 fully landed earlier this session, log 7907d70fc).
