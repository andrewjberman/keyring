# MDPF Model Portfolios — per-segment data-layer linkage audit (DS~B)
2026-06-01 ~1320Z · MDPF_SCOPED Phase 1 · COO [DRIVE] dispatch 1300Z

## Serving artifact
- **One JSON per date:** `s3://opal-data-portal-v2/platinum/mdpf/aggregate_aua/{date}.json` (CloudFront-served).
- Top-level: `aggregate` (GLOBAL headline), `partners[]` (one entry per firm), `etf_decomposition`, `reconciliation`, `meta`, `methodology_version`.
- **3 segments all derive from this ONE artifact:**
  - GLOBAL = `aggregate.opal_aggregate_aua` = cohort 1a+1b+1c+**2a** (includes inflection MODELS; EXCLUDES inflection non-model 2b — Andrew-confirmed 2026-06-01).
  - 49 (49financial) = `partners[]` entry firm_id=49financial = cohort 1a+1b+1c.
  - INFLECTION = `partners[]` entry firm_id=inflection = cohort 2a+2b.

## EXISTS / FRESH / SHAPE — per segment (latest served = 2026-05-29.json)

| Segment | EXISTS | FRESH | SHAPE-COMPARABLE | Verdict |
|---|---|---|---|---|
| GLOBAL (aggregate) | YES | latest 5/29 (weekend 5/30-31 + today 6/01 not yet emitted — expected daily cadence) | keys stable | **UNDERSTATED** — missing inflection 2a (~$96M) on backfilled dates |
| 49financial | YES | 5/29 | full key-set, by_model present | OK |
| INFLECTION | **NO (latest)** | n/a | partner entry ABSENT | **MISSING — per-firm panel renders EMPTY** |

## Root finding — Inflection partner dropped by the 5/29 backfill re-emit
Partner presence by date:

| Date | partners[] | gen | source |
|---|---|---|---|
| 5/21, 5/28 | 49financial + inflection | own-date 15:03 | original daily run |
| 5/18,19,20,22,25,26,27,**29** | **49financial ONLY** | 2026-05-29 19:25-26 | backfill re-emit |

The **2026-05-29 backfill re-emit dropped Inflection from every date it touched.** The 2 surviving dates (5/21, 5/28) are the only ones the backfill did NOT overwrite.

### Root cause (conclusive)
`data/mdpf/scripts/backfill/build_mdpf_process_backfill.py` is a **49financial-only historical backfiller**:
- L120 `PARTNER = "49financial"` (hardcoded single partner)
- L491-492 comment: *"The historical series is 49F-only (no Inflection partner; 2a=0)"*
- L496 `opal_aggregate_aua = partner["total_aua"]` (assumes 2a=0)

It is a **pre-5/18 (pre-Inflection-onboard) tool**. On 5/29 it was run across **post-onboard dates 5/18-5/29**, where Inflection is a live partner (2a≠0) — overwriting good multi-partner artifacts with 49F-only, zeroing inflection 2a out of GLOBAL and emptying the inflection segment.
- NOT a feeder race: inflection feeder partitions exist for every affected date (e.g. 5/29 `model_aua_positions/inflection/2026-05-29.parquet` written 11:00; backfill ran 19:25).

## Cohort-correct impact (Andrew framing 2026-06-01)
Inflection on 5/28 (last date present): 2a model=**$96.21M**, 2b non-model=**$107.77M**, total=**$203.98M**.
- GLOBAL understated by inflection **2a only ≈ $96M** (NOT the full $204M — 2b is never in global).
- INFLECTION segment panel: empty (would show $204M total + 7-model by_model).
- 49: unaffected.

## Proposed fix (DS~B owns per Rule 13; COO nod requested — F4-snapshot interaction)
Re-emit the 8 affected dates (5/18,19,20,22,25,26,27,29) with the **canonical aggregator `mdpf_aggregate_aua.py`** per-date (feeds exist for all → produces correct multi-partner artifact with S2 expected-partners sentinel active). Do NOT re-use the 49F-only backfiller on post-onboard dates.
- Coordinate with F4 period-end-roll snapshot fix (CVO-resolved as TAGGING BUG) so the re-emit doesn't reintroduce the 12/26 reclass artifact.
- Guardrail proposal: add an onboard-date assertion to `build_mdpf_process_backfill.py` so it refuses to run on dates >= INFLECTION_PARTNER_ONBOARD_DATE (2026-05-18).

## Hand-off
- DE (0.4.0_DE_ClientPlatform): BE-fit — the inflection partner entry is absent from served JSON on latest date; any per-firm/inflection panel keying on `partners[].firm_id=='inflection'` gets nothing. Confirm FE behavior on absent-partner.
- COO: RAVC2 + fix authorization.

## RESOLUTION (2026-06-01 ~1325Z — COO NOD granted, executed)
**Re-emit DONE + S3-verified.** Re-emitted the 8 affected dates via canonical `mdpf_aggregate_aua.py --date {d} --source s3 --upload`. All 8 overall=PASS (sentinel_2 expected-partners + sentinel_3 cross-validation PASS). S3 ground-truth: all 10 dates 5/18-5/29 now carry **both partners**. Inflection 2a $93.6M (5/18) → $96.6M (5/29), smooth.

| Date | partners (after) | infl 2a | global agg |
|---|---|---|---|
| 5/18 | 49f+inflection | 93.60M | 1,742,451,012 |
| 5/19 | 49f+inflection | 93.70M | 1,742,546,667 |
| 5/20 | 49f+inflection | 93.70M | 1,748,030,393 |
| 5/22 | 49f+inflection | 94.74M | 1,766,397,553 |
| 5/25 | 49f+inflection | 94.91M | 1,774,606,803 |
| 5/26 | 49f+inflection | 95.64M | 1,779,865,325 |
| 5/27 | 49f+inflection | 95.64M | 1,779,865,325 |
| 5/29 | 49f+inflection | 96.60M | 1,783,772,321 |

(5/21, 5/28 untouched — were always both-partners.)

**Corrected-global note:** canonical 5/29 global $1,783.77M is LOWER than the bad 49F-only value $1,847.97M — the bad backfill also used a different 49f basis, so the net delta is not a clean +2a; canonical + sentinels are system-of-record.

**Guard committed** (a9352506f, pushed CLOUD): `build_mdpf_process_backfill.py` now refuses dates >= INFLECTION_PARTNER_ONBOARD_DATE — the 49F-only path can never overwrite post-onboard multi-partner artifacts again. ds-commit-gate clean.

**F4 constraint honored:** re-emit window is all-May, date-disjoint from the F4 12/26 (Dec) partition; F4 patch f44ab785d untouched. No independent F4-class period-roll artifact on any of the 8 dates (all DoD sentinels PASS).

**Pending:** CVO /verify-channel (3.0.0_SA_CVO) independent confirm; DE linkage-matrix flip inflection→fixed.

## ROLLUP COMPLETION (2026-06-01 ~1334Z — AE caught partition-fix != serving-fix)
AE (0.7.0_AE_CloudOps) verified the FE-facing feeds and found the partition re-emit had NOT propagated: the ROLLUP stage `build_aggregate_aua_timeseries.py` reads the partitions and builds the actual FE trend feeds (`platinum/mdpf/aggregate_aua_timeseries.json` + `json/mdpf/{global,49financial,inflection}/aggregate-aua-timeseries.json`). Those still carried the 5/29 19:38Z post-clobber rollup (inflection tail null).

**Re-ran `build_aggregate_aua_timeseries.py --upload`** — read 402 restored partitions, rebuilt + uploaded all timeseries + per-firm FE slices (gen 2026-06-01T13:34:20Z). VERIFIED: inflection FE slice tail now non-null all dates — 5/22=94.74M, 5/25=94.91M, 5/26=95.64M, 5/27=95.64M, 5/28=96.21M, 5/29=96.60M (1 null in full 402-pt series). **The empty-inflection-panel defect is now fixed in the FE-FACING feeds, not just partitions.**

LESSON: `comp-pipescript postdeps` would have flagged the rollup as a required post-step — should have run it before signaling. Partition emit has a downstream rollup dependency.

## CVO VERDICT: PASS 4/4 (9b54e8453) — independent S3 read. Inflection matrix-cell clear→confirmed.

## FOLLOW-ON (non-blocking, upstream): CVO Step-3.5 note (5/26=5/27 identical) root-caused
Inflection feeder partition `inflection/2026-05-27.parquet` carries `as_of_date=2026-05-26` (stale carry-forward, 402 rows == 5/26). 49f feeder fresh per-date but artifact 49f total also identical → parallel carry at 49f non-model/1b layer. UPSTREAM WS-C feeder freshness, pre-existing, NOT the re-emit. Routed COO+AE.

## GUARD: keep all 3 layers (COO + AE concur). a9352506f (onboard-date) stays. My next leg = version-monotonic write-guard in the shared emit helper (refuse write with methodology_version older than existing). AE owns IAM s3:PutObject runner-role lock.
