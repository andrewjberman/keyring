# DEPLOY LEDGER: non_model_assets.json FULL RETIREMENT (teardown-wave member #1)

**Opened:** 2026-07-29T03:45Z by 0.7.0_AE_CloudOps~A
**Status:** **CLOSED 2026-07-29T15:25Z by 0.7.0_AE_CloudOps~A -- STEP 4 NO-REGEN: PASS.** Both required
limbs satisfied and read under my own hand; see Step 4 CLOSURE below. One ADJACENT DEFECT surfaced by
the same run and routed separately (it does not block this close): Step 2's claim that the
aum-timeseries leg "keeps emitting unchanged" is FALSIFIED -- see Step 4 CLOSURE item C.

## Authorization
**ANDREW-DIRECT ~0336Z (relayed by 1.0.0_SA_CTO 033738Z, VERBATIM):** *"Ok have 0.7.0_AE_CloudOps~A
get rid of that non_model_assets.json and make sure that there is no producer who is going to
generate that shit again."* CTO co-sign for the NEVER#3 S3-deletion leg is in the same message;
COO cc'd. Sovereign-ordered freeze exception (same class as tonight's ETFS apply).

## Step 1 -- WRITER CENSUS (writers-to-the-KEY, not grep-for-names)
Key: `s3://opal-data-portal-v2/json/portfolios/non_model_assets.json`
| Writer candidate | Verdict | Evidence |
|---|---|---|
| mdpf chain Stage 3.5 -> `build_legacy_compat_emit.py --upload` (deployed dispatch `:363-385`, EC2 pulls `s3://opal-data-mdpf/code/scripts/`) | **THE live scheduled writer** | put_object @ script `:899` (pre-edit); object LastModified 2026-07-27T15:10:07Z == Stage 3.5 emit time to the second |
| smartx 11:30Z rule `smartx-account-distribution-daily` -> opal-smartx-ingestion-pipeline `{"job":"account_distribution"}` | **READER only** (CTO's unverified item RESOLVED) | lambda source: only get_object on the key (`load_enterprise_totals` :121-131); zero put_object refs |
| `build_aggregate_aua_timeseries.py` (ROLLUP, dispatch `:391`) | NOT a writer of this key | grep "non_model_assets" = 0 (series-name refs only) |
| `data/smartx/scripts/backfill_non_model_assets.py --prod` | manual-only writer-CAPABLE, unscheduled | prod key @ `:38`; no schedule anywhere |
| `data/smartx/scripts/compute_non_model_assets.py` | DEAD (raises on invoke, retired 2026-05-13 TO-5) | `:32` hard deprecation |
| `dim_mdpf_non_model_assets.py` (dispatch 6c) | different key -- writes `gold/mdpf_revamp/global/non_model_assets.json` (revamp staging; NOT the legacy served artifact; out of scope, untouched) | script `:89` |

## Step 2 -- WRITE-LEVEL RETIREMENT (C1: unit of retirement is the WRITE)
- `build_legacy_compat_emit.py`: NM put_object REMOVED from the upload block; NM read made
  absence-tolerant (NoSuchKey -> {}) so the aum-timeseries.json leg keeps emitting unchanged;
  docstring re-written to the retirement truth. Producer keeps running (aum leg intact).
- `backfill_non_model_assets.py`: ALL S3 writes refused (rc=3 with retirement message);
  --dry-run analysis preserved. Closes the last writer-capable path (both prod + preview keys).
- commit-gate PASS on both files. NOT a {gold,silver,bronze} path (Rule-13 enumeration) --
  AE lane; DS base notified (CTO cc'd them in the order).

## Step 3 -- OBJECT DELETION (NEVER#3 leg: Andrew explicit word + CTO co-sign, above)
Family census on S3 (`aws s3 ls json/portfolios/ | grep non_model`): exactly 2 objects --
- `json/portfolios/non_model_assets.json` (114,553 B, LastModified 2026-07-27T15:10:07Z) -- THE target
- `json/portfolios/non_model_assets_preview.json` (84,760 B, 2026-05-13) -- same-family QA residue,
  written only by the now-retired manual backfill; not served (portal route serves only the main key,
  portal_data_proxy `:2204`). Deleted under the same order, disclosed here.
Bucket is versioned: deletes create delete markers (restorable; deliberate -- reversibility preserved).
- EXECUTED ~03:52Z: both objects deleted; residual family listing EMPTY (grep rc=1). Retired
  emit script deployed to `s3://opal-data-mdpf/code/scripts/backfill/` BEFORE deletion,
  round-trip md5 verified repo==S3 (edc291408982b16d80ad4be72cba2b4e) -- the 15:00Z sync
  pulls the retired writer, so the fire cannot re-emit.

## Step 3a -- REVERSIBILITY, MEASURED (added 2026-07-29T14:04:53Z by 0.7.0_AE_CloudOps~A; CTO-directed 140338Z)
The rollback line in Step 3 was an assertion from the record. It is now MEASURED on the version plane
(`aws s3api list-object-versions`, read-only):

| Key | Delete marker (IsLatest) | Marker time | Live object versions | Restorable noncurrent |
|---|---|---|---|---|
| `json/portfolios/non_model_assets.json` | `pWisyjN7J1yefr_dk9Ow.nszyab69X7g` | 2026-07-29T03:49:16Z | **NONE** | **9** |
| `json/portfolios/non_model_assets_preview.json` | `zh1iM5PlJZI6E1M4fOr78UyROzq2zK0Y` | 2026-07-29T03:49:18Z | **NONE** | **1** |

**Both keys are held not-served by ONE DELETE MARKER EACH, with real content intact underneath.**
Consequence, ruled by CTO 140338Z and binding beyond this ledger: **DELETING EITHER MARKER REPUBLISHES
A CLIENT-FACING ARTIFACT ANDREW ORDERED GONE -- instantly, with real content, reporting success.**
A blanket prohibition now stands on removing ANY delete marker anywhere in tonight's seven-leg wave,
on any bucket, for any reason; a leg that appears to need one STOPS and goes to CTO. Rollback for a
15:15Z FAIL therefore needs no improvisation: restore from the listed noncurrent versions.

## Step 4 -- NO-REGEN PROOF (closes this ledger)
The 15:00Z unattended fire is the natural test: after chain completion (~15:15Z), the key must NOT
be SERVED. Anything recreating it = a writer the census missed -> STOP + report per CTO spec. D2 note:
the retirement touches no trigger/schedule -- the fire's schedule evidence is unaffected.

**SEMANTICS, made explicit (CTO 140338Z) -- "must NOT exist" means NOT SERVED, not destroyed:**
- PASS = a GET 404s because a delete marker is latest. **Noncurrent versions surviving underneath is
  NOT a partial failure and must not be reported as one.**
- FAIL = a LIVE object version at either key -> the writer census missed a producer. STOP, do **not**
  re-delete (a re-delete erases which writer did it), escalate to CTO.

**EXERCISE DISCIPLINE (COO 135337Z, adopted):** the check is **KEY-EXACT** on the two keys above,
never a name grep over a prefix. Measured basis: a bucket-wide `non.model` sweep returns exactly one
legitimate hit -- `platinum/mdpf/global/non-model-assets.json` (81,931 B @ 00:35:22Z), the
platinum-plane hyphenated artifact from the later wave, already scoped OUT by Step 1 (dispatch 6c
revamp lineage). A "no non-model object exists" phrasing would read DIRTY on a healthy estate.

**⚠ PREREQUISITE -- THE FIRE IS NOT SCHEDULED, SO ABSENCE ALONE PROVES NOTHING.**
`mdpf-daily-refresh-trigger` has `ScheduleExpression: None`; it is event-driven on
`opal-data-inf/gold/meta/pipeline-complete.json` ObjectCreated and its own description records that it
REPLACED `cron(0 15 ? * MON-FRI *)`. If the INF spine does not complete, the chain never dispatches,
the key stays absent, and this step would read PASS having proven nothing -- a PASS-shaped reading of
a dead pipeline. **Discriminator baselined 2026-07-29T13:56Z, BEFORE the fact:** that marker was
135 B, ETag `5ff381b4bc3b0b529a7dffc528f21d58`, LastModified **2026-07-28T15:04:07Z (yesterday)**.
Closing this ledger requires BOTH: (i) that marker ADVANCED to today, AND (ii) the chain's own run log
showing completion. Marker unadvanced -> **NOT-YET-PROVEN**, ledger stays OPEN, reported as such.

## Step 4 CLOSURE -- 2026-07-29T15:25Z, 0.7.0_AE_CloudOps~A. VERDICT: **PASS. LEDGER CLOSED.**

**A. LIMB 1 -- THE CHAIN ACTUALLY RAN (the prerequisite; absence alone proves nothing).**
- INF completion marker ADVANCED: `2026-07-29T15:02:30Z`, ETag `1b39d06d5d54a919c7a3bc0f43d28a17`,
  135 B -- vs my pre-fact 13:56Z baseline `5ff381b4bc3b0b529a7dffc528f21d58` @ 2026-07-28T15:04:07Z.
  Payload carries `chain:"full"`, `run_date:"2026-07-29"`, `completed_at:"2026-07-29T15:02:29Z"`
  (independently grounded by 0.4.0_DS_ClientPlatform, relayed 151316Z; retrieval-verified 135==135).
- THE RUN'S OWN LOG, read by me (not rc, not a config, not a self-report):
  `/aws/lambda/mdpf-daily-trigger` RequestId `421dd1ec-e7aa-491e-8806-1968cadb44a8` --
  event etag matches the marker I measured; `OK: mdpf convergence gate passed -- dispatched`,
  runner `i-02448edb624a7a7cf`, ssm_command_id `34f8056f-25fa-4ff4-ad47-c6ef3b5a301c`, `all_fresh: true`.
- CHAIN telemetry (the dispatch log's own named location, so this is the chain's log not the trigger's):
  `s3://opal-data-mdpf/telemetry/mdpf-daily-runner/logs/mdpf_daily_20260729_150255.log` ->
  `[mdpf-dispatch] CHAIN complete run_id=mdpf_daily_20260729_150255`; `status.json` = `"status":"complete"`.

**B. LIMB 2 -- THE KEY WAS NOT REGENERATED. And the producer's OWN LOG says so in words.**
- Key-exact ListObjectsV2 at 15:13:31Z (AFTER the 15:05Z chain writes), both keys -> no Contents:
  `json/portfolios/non_model_assets.json`, `json/portfolios/non_model_assets_preview.json`.
  POSITIVE CONTROL as a SEPARATE invocation: `json/portfolios/aum-timeseries.json` -> returned a row.
  So the instrument discriminates present from absent; the two absences are real.
  (Independently corroborated by base lane 0.7.0_AE_CloudOps at 15:11:15Z, its own control passed.)
- STRONGEST EVIDENCE, from the retired producer itself, run log line 226:
  `[2026-07-29T15:04:40Z] RETIRED: json/portfolios/non_model_assets.json absent (expected
   post-retirement) -- nm leg builds from platinum only and is NOT uploaded`
  The retirement is not merely observed from outside; the producer announces the retired behaviour.
- **DEFENCE IN DEPTH (discovered at close, not designed here): the retirement is held by TWO
  INDEPENDENT MECHANISMS.** (1) the code edit (put_object removed, Step 2); (2) an IAM explicit Deny --
  statement Sid `P0DenyLegacyPortfoliosClobber20260728` inside inline policy `mdpf-runner-scoped` on
  `mdpf-daily-runner-ec2-role`, denying `s3:PutObject` on this exact key. Either alone would hold.

**C. ADJACENT DEFECT SURFACED BY THIS RUN -- ROUTED, NOT SWALLOWED. Step 2 CONTAINS A FALSE CLAIM.**
Step 2 states the NM read was made absence-tolerant *"so the aum-timeseries.json leg keeps emitting
unchanged."* **That is FALSIFIED.** Stage 3.5 now fails every run:
```
[2026-07-29T15:04:53Z] UPLOADING to s3://opal-data-portal-v2/json/portfolios/aum-timeseries.json ...
botocore.errorfactory.AccessDenied: ... mdpf-daily-runner-ec2-role/i-02448edb624a7a7cf is not
authorized to perform: s3:PutObject on .../json/portfolios/aum-timeseries.json
with an explicit deny in an identity-based policy
[mdpf-dispatch] step LEGACY-EMIT rc=1 dur=15s status=error
```
- CAUSE IS **NOT** THIS RETIREMENT. The SAME Sid `P0DenyLegacyPortfoliosClobber20260728` lists BOTH
  `non_model_assets.json` AND `aum-timeseries.json`. It was installed 2026-07-28 (WO-2 D-controls),
  i.e. it PREDATES this retirement (03:45Z 07-29). The Step-2 claim was **untested when written and
  already false at that moment** -- the leg it promised to preserve was fenced hours earlier.
- CONSEQUENCE: `json/portfolios/aum-timeseries.json` is FROZEN at 2026-07-27T15:10:07Z (295,300 B) and
  this producer cannot advance it. **Whether that is intended (legacy json plane deliberately
  superseded by platinum) or a gap (a live consumer still reading a 2-day-stale key) is NOT mine to
  rule -- routed to CTO + COO at close.** Not a freshness verdict here: no trading-calendar claim is
  being made, only that the writer is denied.
- SECOND-ORDER, and the more dangerous half: the dispatch's own error text says
  *"non_model_assets.json stale until next run"* -- **it names the RETIRED key as the casualty.** That
  wording is stale: non_model is gone deliberately and can never be "stale", while the ACTUAL casualty
  (aum-timeseries.json) goes unnamed. A responder reading that line at 03:00 would chase a retired
  artifact and miss the frozen one. Flagged for correction with the Stage-3.5 owner.

**D. WHAT I DID NOT DO.** No delete marker touched (CTO 140338Z wave-wide prohibition). No re-delete.
No object restored. Nothing applied. Freeze intact.

## Known consequence (surfaced by CTO to Andrew; not mine to fix)
Until DE's queued chart fix promotes, Global trend/band surfaces reading this file render
reduced/absent non-model -- honest absence over the wrong 232.31 composition.
