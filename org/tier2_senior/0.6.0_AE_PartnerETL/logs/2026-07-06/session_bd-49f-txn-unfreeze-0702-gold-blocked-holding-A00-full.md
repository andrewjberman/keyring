# BD 49F txn un-freeze -> 07-02: SOURCE+silver DELIVERED; served flip BLOCKED in gold (account_is_open str-dtype, 3 crashes); HOLDING for DS A_00 --full verified-bool

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, COORDINATE
**serial:** 0.6.0_AE_PartnerETL | **window:** 2026-07-06 ~13:06Z (session start) -> 18:43Z | **status:** IN-FLIGHT (held on DS)

> REBOOT-RESILIENT HANDOFF (Andrew: "we may need to reboot the device"). Current State + Next Steps
> below are written to resume the P0 from exactly here. The un-freeze SOURCE @07-02 is DURABLE on S3;
> only the gold re-dispatch + served flip remain.

## Summary
COO DRIVE GO (P0, Andrew-watching): un-freeze the Black-Diamond 49F TRANSACTION source, frozen since
07-03 (root: bd-49f-runner-role lacked s3:PutObject on opal-data-bd/bronze/* -> sentinel AccessDenied ->
bd-silver-merge STARVED; 0.7.0 fixed via bd-v2.47.0). DELIVERED the SOURCE: bronze + all-4 silver
(transactions/realized/unrealized/allocations) @07-02, A_00 accounts_dimension rebuilt, sentinel emitted
(0.7.0's IAM grant EXERCISED+PROVEN), 0.7.0~A silver-parity verdict GREEN. The SERVED platinum flip is
BLOCKED in the gold layer by a single-root incremental dtype bug (account_is_open written as STRING not
bool), which crashed the gold chain 3x (B_00, C_07 x2). Root fully grounded; do-BOTH fix plan GO'd by COO;
currently HOLDING for DS to re-baseline A_00 to bool + verify-on-parquet, then I re-dispatch B/C/D.

## Timeline (what happened)
1. **Bridge un-freeze (13:06-14:47Z):** Grounded cookie LIVE (auth-probe), root=IAM sentinel gap (NOT cookie-
   death, NOT txn-export), frontier=07-02 (07-03=July-4 market holiday; sharp-tested all 4 tables real @07-02).
   Force-invoke bd-49f-runner FAILED (bearer-token expiry mid heavy sweep, mis-classified as auth_dead ->
   3/4 tables aborted; F3/F4 finding). LIGHT recovery: session-pulled the 2 stub snapshot tables (unrealized
   37.8MB/allocations 12.9MB) with fresh tokens + verified real, then NO-FORCE runner invoke -> sentinel
   bronze/2026-07-02/_BRONZE_COMPLETE.json emitted 14:31:47Z (runner-role PutObject = 0.7.0 bd-v2.47.0 grant
   PROVEN) -> bd-silver-merge -> ALL 4 SILVER PASS @07-02 + A_00 rebuilt (PASS). 0.7.0~A silver-parity = GREEN.
2. **Gold saga (14:44-17:40Z):** GoldLayerPricesTrigger -> bd-gold-trigger -> gold runner. Crashed at
   B_00.canonical_holdings (`~df['account_is_open']` on STRING). DS coerce-fixed B_00 (04c733de5) -> re-dispatch
   #1 (incremental) crashed at C_07.advisor_attribution (`arch_tier` KeyError -- same str root via `==True`
   empty). mode=FULL re-dispatch #2 RE-CRASHED at C_07 -- DS's A_00 dtype-gate NEVER RAN.
3. **Root grounded (18:00-18:15Z):** parquet mtime 14:46:44Z < A_00.done 17:07:49Z = A_00 ran --INCREMENTAL
   (dispatch mode=full does NOT propagate as --full), found 0 NEW txns (07-02 already loaded @14:46), and
   RETURNED WITHOUT save_dimension -> the dtype-gate (correct, lives in save_dimension) never executed ->
   accounts_dimension_latest.parquet stayed the 14:46 STR version. NOT a gate bug -- a NO-SAVE short-circuit.
   do-BOTH plan GO'd by COO 18:15Z.

## Compiler Tools
| Tool | Call | Result | Note |
|---|---|---|---|
| comp-freshness | `chain bd` (x5+) | PASS(read) | grounded the freeze, the silver FAIL->PASS @07-02 flips, + the gold FAILs |
| Grep/Glob (native) | A_00/B_00/C_07/merge/save_dimension locates | PASS | found the gold-script crash loci + the dtype-gate |
| raw aws (rail-checked) | lambda invoke / ec2 describe / s3 forensics / logs / parquet reads | PASS | dispatch-log tracebacks, checkpoint mtimes, parquet dtype -- NO comp-tool covers these |

What worked: comp-freshness cleanly tracked the silver flip; the log+checkpoint+parquet-mtime triangulation
grounded the no-save root decisively (stopped a wasted crash #3 re-fire). What failed: n/a. Gap: no comp-tool
reads a gold dispatch crash traceback / a parquet column dtype / a Lambda invoke response -- all rail-checked
raw aws; a `comp-gold-run <instance>` (stage cursor + crash locus + served-flip watch) remains the coverage gap.

## Files Modified (this window)
- `org/critical_paths/change_management/20260706T1355Z_bd-49f-txn-unfreeze-bridge-0702-coherent_deploy_completion.md` -- the deploy-ledger, OPEN, committed through **8ffc8b1fa** (full timeline in its status log).
- `org/tier2_senior/0.6.0_AE_PartnerETL/staging/bd-49f-durable-hardening-findings-20260706.md` -- 3 durable findings.
- `org/tier2_senior/0.6.0_AE_PartnerETL/staging/pathA-runner-401-remint-fix-draft.md` -- Path A runner fix (CTO pre-approved, post-served).
- (this log)

## Blockers
**BLOCKED (gold-dtype, DS lane, held on verified-bool):** served platinum flip cannot land until
gold/dimensions/accounts_dimension_latest.parquet account_is_open is BOOL (currently STRING, mtime 14:46:44Z).
DS (0.4.0) owns + is running A_00 --full to fix. COO condition (binding): NO re-dispatch until DS verifies
dtype==bool ON THE LIVE PARQUET (code/ETag claims were trusted twice + didn't hold). Not infra (no 0.7.0).

## Current State (zero-context, reboot-resilient)
- **Un-freeze SOURCE @07-02 = DONE + DURABLE on S3** (survives a device reboot; do NOT re-do): silver
  txn/realized/unrealized/allocations all PASS @07-02; bronze forwardfill_v2/{table}_DAILY_2026-07-02.xlsx all
  REAL; sentinel bronze/2026-07-02/_BRONZE_COMPLETE.json fresh (14:31:47Z); 0.7.0 bd-v2.47.0 IAM grant PROVEN.
- **Served = STILL 07-01** (platinum/firm/header_metrics.json + dashboard.json data_as_of=2026-07-01; AUA
  $1,828,588,878.71 / 2913 clients / 6238 accts). TARGET = 07-02 (the frozen-07-01 baseline is the no-widen anchor).
- **THE BLOCKER (grounded):** gold/dimensions/accounts_dimension_latest.parquet account_is_open dtype=STRING
  ('True'/'False'), mtime 14:46:44Z. Gold str-consumers: B_00 (`~`, coerce deployed 04c733de5) / C_07.advisor_
  attribution (`==True` -> empty -> arch_tier KeyError; coerce+empty-guard deployed 954d48555) / B_02 (`.eq(False)`,
  coerce deployed 94383024e -- but B_02 ran on str BEFORE its coerce, so its 17:xx output is WRONG).
- **gold runner i-01003b035d2988dfb = STOPPED** (crashed at C_07 17:40:47Z).
- **Coordination:** DS (0.4.0, LIVE) OWNS the gold fix + is running A_00 --full NOW. COO GO'd do-BOTH 18:15Z
  (NOT go-fastest). 0.7.0/~A: silver+IAM leg CLOSED (box-retire gated on served + N-nightly). I HOLD the
  re-dispatch on DS's verified-bool GO.
- **Ledger:** 20260706T1355Z...bridge-0702-coherent, OPEN, @8ffc8b1fa.

## Next Steps (RESUME-FROM-HERE)
1. **[0.4.0_DS_ClientPlatform]** Run A_00.accounts_dimension.py --full -> re-saves accounts_dimension_latest.parquet
   -> save_dimension dtype-gate (L636-643) fires -> account_is_open=BOOL. VERIFY on the LIVE parquet
   (`pd.read_parquet(...).account_is_open.dtype == bool`) -- NOT code/ETag. Then hand 0.6.0 the exact re-dispatch
   recipe (mode + which stale checkpoints to clear: B_02.done/C_07.done/C_06.done/D_*.done that ran on str).
2. **[0.6.0_AE_PartnerETL = ME on resume]** On DS's verified-bool GO + recipe, FIRE the re-dispatch (PROD-trigger,
   rule-13). Command (v1 CLI, env AWS_EC2_METADATA_DISABLED=true AWS_PAGER=""; runner must be STOPPED):
   `aws lambda invoke --function-name bd-gold-trigger --invocation-type RequestResponse --payload '{"mode":"full"}' /tmp/o.json`
   (do NOT use --cli-binary-format -- CLI is v1). If DS says clear checkpoints first: delete the named
   gold/.checkpoints/2026-07-06/{script}.done S3 objects then fire. WATCH: gold/.checkpoints/2026-07-06/C_07.done
   FRESH (mtime > fire-time) = C_07 passed; then served header_metrics.json data_as_of -> 07-02.
3. **[0.6.0 = ME]** On served @07-02: verify AUA NO-WIDEN sanity (~$1.83B / ~2900 clients / ~6200 accts, no
   implausible jump vs 07-01 $1,828,588,878.71). CLOSE the ledger (close entry + REGISTRY n/a -- it's a deploy-
   ledger) + RAVC COO + DS joint-confirm (me: AUA/no-widen; DS: served-vintage).
4. **[0.6.0 = ME, POST-served]** Durable-hardening: author Path A (staging/pathA-runner-401-remint-fix-draft.md,
   CTO pre-approved) -> 0.7.0 deploys via TF. Route the finding bundle (staging/bd-49f-durable-hardening-findings-
   20260706.md: token-refresh / heavy-pull-off-Lambda / bd-silver-merge 838s-of-900s + the NEW gold-incremental
   dtype family: dispatch-mode=full != A_00 --full, and account_is_open str systemic) to COO/CTO for WS-5. DS owns
   the gold-incremental durable fix.

**REBOOT NOTE:** device reboot => (a) I re-register + /watcher on restart; (b) gold runner is EC2 (survives a
device reboot) -- re-check its state; (c) DS's A_00 --full may need re-running if it was device-local; (d) the
SOURCE @07-02 (silver/bronze/sentinel on S3) is durable -- NO re-do. Resume at Next Step 1 (confirm DS verified-bool)
or Step 2 (if already verified -> fire the re-dispatch).
