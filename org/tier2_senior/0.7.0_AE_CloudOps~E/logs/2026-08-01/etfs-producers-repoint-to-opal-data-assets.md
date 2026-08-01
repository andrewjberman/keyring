# ETFS_PRODUCERS_REPOINT_TO_OPAL_DATA_ASSETS -- 0.7.0_AE_CloudOps~E

**Date:** 2026-08-01
**Task Order:** ETFS_PRODUCERS_REPOINT_TO_OPAL_DATA_ASSETS (CTO GO @4f34addd74, Andrew-direct)
**Status:** COMPLETE for 49F (already-correct, reverified) + cottonwood (repointed, deployed, verified).
INFLECTION LEG CANCELLED (CTO-ratified) after I found its proposed source is not clean.

---

## Objective

Andrew-direct: repoint the three ETFS write-out producers (inflection, 49financial,
cottonwood) from their per-firm gold layers onto the consolidated `opal-data-assets`
monolith's silver layer -- "lock the pattern for all while they're at it." The
motivating defect: `inf-etf-ownership-daily`'s gold source relabels one book onto
multiple dates (a false-vintage class); the monolith's Hive-partitioned tables were
believed clean and structurally immune (partition key IS the date).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | "list the partitions and schema of opal-data-assets orion inflection silver fact_positions" | NO-MATCH (correctly reported) | no comp-tool covers monolith table schema/partition inspection; routed to rail-checked raw `aws s3api` |
| comp-grep | `bd-49f-etf-ownership-scheduled-floor` / `inf-etf-ownership-daily` / `cot_bd_session_daily_et` etc. | PASS | source-map, TF-file, and core-doc lookups throughout |
| comp-iam service | `cot-etf-ownership-daily` | PASS (DESIRED-plane only, as documented) | 5 operations found, all UNRESOLVABLE-RESOURCE (dynamic bucket/key) -- correctly insufficient alone per Rule 22a; followed with live `get-role-policy` + `simulate-principal-policy` |

**What worked:** comp-grep localized every TF/source-map/schema lookup fast; comp-iam correctly declined to claim more than its DESIRED-plane view supports.
**What failed:** nothing outright, but the class of question this task needed most -- "is data X identical to data Y across two dates, at the VALUE axis" -- has no comp-tool at all. That gap is exactly where the day's central finding (inflection's monolith source is not clean) was made, using raw pandas comparisons instead.
**Gap found:** no comp-tool for cross-partition value-level data-quality comparison (as opposed to freshness/existence). Worth a future comp-tool if this class of check recurs (it recurred twice today, on two different firms' data).

---

## Work Completed

### 1. Inflection leg -- investigated, found not clean, CANCELLED (not implemented)

Before writing code, verified the spec's S1 layer table (bronze clean / silver clean
/ gold DEFECT) against `orion/inflection/silver/fact_positions` and
`orion/inflection/bronze/positions`. Method: download both partitions of each named
slip pair, diff excluding only columns that encode the snapshot date itself, and
independently compute the ETF-universe value vector (the axis that actually matters
for the rebate basis, not a whole-file hash).

Findings (escalated to CTO 20260801T231113Z):
- `orion/inflection/silver/fact_positions/` date=2026-07-18 vs date=2026-07-20:
  34867 rows both sides, EVERY substantive column (ticker, currentShares,
  currentPrice, currentValue, accountNumber) byte-identical; only the
  vintage-echoing columns (asOfDate/snapshot_date/_source_file/_source_as_of)
  differ. ETF-universe sum IDENTICAL to the cent both dates.
- Same pattern for date=2026-07-25 vs date=2026-07-27.
- Negative control (2026-07-06 vs 2026-07-08, unrelated dates): row counts and
  sums genuinely differ -- method is not broken.
- Traced ONE layer lower: `orion/inflection/bronze/positions/{date}.jsonl.gz`.
  Compressed ETags/sizes differ, but decompressed JSON content is byte-identical
  (excluding embedded asOfDate/snapshot_date fields) for the same slip pair --
  **the duplication is present in BRONZE**, not introduced by monolith silver
  conversion.
- Pattern noted (both failing pairs are Saturday->Monday) but explicitly labeled
  a hypothesis, not a proven mechanism -- CTO's own re-run later showed the
  supposedly-clean third pair (07-14/07-16) was ALSO frozen on the universe-ticker
  axis specifically (other securities moved, the 4 ETF tickers did not), so the
  weekend hypothesis does not hold as a full explanation either.

CTO independently re-ran the check, found his own layer table was produced by a
broken instrument (measuring "is the file different" via hash instead of "is the
ETF VALUE different"), ratified the HALT, and CANCELLED the inflection leg (not
paused -- a new source is now an open architecture question, not a repoint). No
code or Terraform for `inf-etf-ownership-daily` was touched.

### 2. 49F leg -- already correct (07-29 revival), reverified live

`bd-49f-etf-ownership-daily` was already repointed to
`opal-data-assets/schwab/08242234/silver/fact_rps` on 2026-07-29 (a prior AE~A
revival, unrelated to this task). Verified rather than re-implemented:
- IAM live (`get-role-policy`) matches Terraform: `MonolithFactRpsRead`/`List`
  scoped exactly to `schwab/08242234/silver/fact_rps/*` -- 0824 only, no 0833.
- AC4 (0824 declared, not derived): `RPS_PREFIX` constant + an explicit
  "NEVER summed with, never substituted for 0833" comment in the vendored
  compute module.
- AC7 (vintage from partition key): `source_as_of = day` (the partition
  identifier), never a payload column.
- **AC2 reproduced live against the deployed source**, via the real column
  selection (`ticker_symbol` + `market_value_settled_unsettled`): 2026-07-20 sums
  to **$528,132,730.04** across DIVZ/IDVZ/PFDE/PFOE -- exact match to the
  published CSV, 92,838 source rows (denominator).

No code, Terraform, or deploy needed for this leg -- confirmed already green.

### 3. Cottonwood leg -- repointed, deployed, verified

**Column resolution (3b), with evidence, before writing code:**
- Downloaded `blackdiamond/cottonwood/silver/fact_holdings` for 2026-07-20.
  `Symbol`: 0 nulls, 1169 universe-ticker rows. `Ticker`: 1298 nulls (~8% of
  16762 rows, e.g. cash-equivalent lines), 1169 universe-ticker rows on the
  populated subset -- and 0 disagreements with Symbol wherever both exist.
  **Chose Symbol** (strictly more complete).
- `Market Value` vs `Unaccrued Market Value`: byte-identical for every universe
  row (max abs diff = 0.0, Accrual = 0 for ETFs). **Chose Market Value** (the
  plain concept, matches every sibling producer's semantic).

**Slip-pair re-verification** (CTO explicitly asked this be redone with a
value-axis method before I wrote code, given the broken-instrument risk applied
fabric-wide): ran the ETF-vector comparison on cottonwood's `fact_holdings` for
07-17/07-20 (CTO-named), 07-06/07-08, and 07-13/07-24. All three DISTINCT with
real, differing sums and row counts -- no relabel-across-dates defect found here.

**Code** (`infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py`):
rewrote to read `opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/date=
YYYY-MM-DD/data.parquet` (Hive-partitioned), Symbol/Market Value columns,
`source_as_of` derived from the partition key. Old `opal-data-cot` read path left
callable (unused) per the spec's retirement policy. Verified locally against live
data via the real `lambda_handler` code path (not a standalone re-implementation)
before touching Terraform: 2026-07-20 -> `total_ownership: 50292778.58` (AC3
exact), and an explicit-date request for the known-absent 2026-07-31 correctly
raises `RuntimeError` rather than fabricating a slice.

**IAM**: new `MonolithFactHoldingsRead`/`MonolithFactHoldingsList` statements
scoped exactly to `blackdiamond/cottonwood/silver/fact_holdings/*` -- no
statement anywhere touches `blackdiamond/49f/` (NEVER#2).

---

## Deployment Sequence (cottonwood)

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source (lambda_function.py + cot-etf-ownership-daily.tf) | `dbff7603bf` |
| 2 | `build-and-upload.sh cot-pipeline cot-etf-ownership-daily` | SHA256 `Ht/QnhqhueF1lx719zrYuJWMCHwMBsLaf9JyePZeNqw=`, upload VERIFIED |
| 3 | Commit source map | `2c0b5a3c20` |
| 4 | `terraform plan` (untargeted) | Showed 4 add / 3 change / 3 destroy -- but MOST of that was UNRELATED, already-committed, never-applied drift from 2026-07-29 (`schedule-et.tf`'s `cot_bd_session_daily_et` scheduler, `ssm.tf`'s `cot_bronze_run` doc) that I did not create and don't own |
| 5 | Re-planned SCOPED via `-target=aws_iam_role_policy.cot_etf_ownership_daily_s3 -target=module.cot_etf_ownership_daily` | Clean: 0 add / 2 change / 0 destroy -- exactly my intended change, isolated |
| 6 | `terraform apply` (scoped plan) via `safe-apply.sh` (unset `MSYS_NO_PATHCONV` first) | comp-tagauthz PASSED, tombstone-gate CLEAN, Apply complete: 0 added, 2 changed, 0 destroyed |
| 7 | 0-diff plan (same `-target` scope) | "No changes. Your infrastructure matches the configuration." |
| 8 | Update core doc `pipeline_inventory.xml` | `f4c1126aa5` |
| 9 | `record-terraform-deploy.sh cot-pipeline` | `cb8d4e1f60` -- correctly scoped by the script itself to only functions whose SOURCE changed in range (verified: `cot_bd_session_trigger`'s incidentally-reconciled entry matches its LIVE `CodeSha256` exactly -- a genuine parity fix, not a false stamp) |
| 10 | Tag | `cot-pipeline-v0.7.3` |
| 11 | Push | Not yet -- lanes commit, MSTR integrates (LD-0367/0368); commits sit local on `CLOUD` |

## Verification (evidence, paste of actual output)

**AC2 (49F)** -- live compute against `schwab/08242234/silver/fact_rps` date=2026-07-20,
`ticker_symbol` + `market_value_settled_unsettled`: DIVZ 178,535,302.26 / IDVZ
152,318,861.24 / PFDE 126,302,397.71 / PFOE 70,976,168.83 = **528,132,730.04**
(92,838 source rows, denominator). Matches the published CSV to the cent.

**AC3 (cottonwood)** -- deployed `cot-etf-ownership-daily` invoked live with
`{"date":"2026-07-20"}`: response `{"status":"ok","key":"daily/cottonwood/2026-07-20.json",
"slices":4,"total_ownership":50292778.58,"source_as_of":"2026-07-20"}`. Independently
confirmed via `s3api head-object` (LastModified 2026-08-01T23:29:12Z) and the served
artifact's content (per-ETF rows sum to 50,292,778.58, `source_artifact` cites the
monolith key). Differs from the stale published $48,391,202.69 -- the required outcome.

**AC4** -- 49F: `RPS_PREFIX = "schwab/08242234/silver/fact_rps"` with an inline
"NEVER summed with, never substituted for 0833" note (pre-existing, verified).
Cottonwood: N/A (0824/0833 hazard is Schwab-specific; cottonwood's hazard is 3c,
covered below).

**AC5 (no cross-firm read)** -- cottonwood: `simulate-principal-policy` against
the live role, one `--resource-arns` per call, positive control as a separate
invocation: `s3:GetObject` on the granted `fact_holdings` key = `allowed`
(2 separate invocations, both allowed); `s3:GetObject` on
`blackdiamond/49f/silver/fact_rps/...` = `implicitDeny`. `s3:ListBucket` with
`s3:prefix` context set to the cottonwood prefix = `allowed`; same call with the
49f prefix = `implicitDeny`. Live `get-role-policy` confirms no statement anywhere
references `blackdiamond/49f/`.

**AC6 (Terraform-only, IAM verified)** -- `safe-apply.sh` used throughout, never
`update-function-code`. IAM verified per AC5 above (comp-iam run first, correctly
insufficient for the new dynamic-resource grants per Rule 22a, followed by live
`get-role-policy` + `simulate-principal-policy`).

**AC7 (vintage from partition key)** -- both 49F (`source_as_of = day`, the
enumerated `date=` partition) and cottonwood (`source_as_of = day`, same pattern)
derive vintage from the Hive partition key, never a payload column. Enforced by
construction: neither producer's code path ever reads a `date`-like column off
the parquet body for this field.

**AC8 (no alert/monitor)** -- `git show dbff7603bf | grep -iE "alarm|sns|send_email|monitor|alerter"` -> no output.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Halted and escalated the inflection leg instead of implementing the spec as written | Independently verified the spec's S1 layer table against live data BEFORE writing code; found the claimed-clean monolith source carries the identical defect at bronze. Shipping the repoint would have made AC1 look closed while silently deepening the defect (partition-key vintage looks structurally immune but isn't, if the partition itself is duplicated). |
| Ran the cottonwood slip-pair check with a value-axis method (ETF sum), not a file hash | CTO's own instrument (whole-file hash after dropping "date-ish" columns) was proven biased toward "clean" on the inflection leg; the same instrument produced 49F's/cottonwood's "clean" claims and had not been independently re-verified. Redid it correctly before trusting it. |
| Chose `Symbol` over `Ticker`, `Market Value` over `Unaccrued Market Value` for cottonwood | Evidenced: Symbol has 0 nulls vs Ticker's ~8%, with 0 disagreements where both exist (strictly more complete, never loses coverage). Market Value == Unaccrued Market Value for every universe row (ETFs carry zero accrual) -- Market Value is the plain, cross-producer-consistent concept. |
| Left the old `opal-data-cot` IAM grant + env vars in place, unremoved | Spec's explicit retirement policy: retire the old read path only after all three producers verify green on the monolith, in a follow-on. Not touching it now avoids scope creep and keeps a trivial rollback path open. |
| Applied cottonwood's Terraform via a SCOPED `-target`, not the full untargeted plan | The untargeted plan bundled unrelated, already-committed-but-unapplied drift from 2026-07-29 (a scheduler + an SSM document, Andrew-direct via CTO, unrelated to this task) that I did not build and don't own the context for. Bundling it into a revenue-basis producer's targeted fix would have muddied the evidence trail and risked deploying someone else's in-flight work as an unreviewed side effect. |
| Did not attempt to fix or silently apply the stale cot-pipeline drift | Not my task, not my context on whether it's still wanted as-is 3 days later. Flagging to CTO/COO as a separate item instead (see Next Steps). |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/cot-pipeline/cot-etf-ownership-daily/lambda_function.py` | Repointed to monolith `fact_holdings`, Symbol/Market Value columns, partition-key vintage | Yes -- `dbff7603bf` |
| `infra/aws/terraform/cot-pipeline/cot-etf-ownership-daily.tf` | New IAM grant scoped to `blackdiamond/cottonwood/silver/fact_holdings/*`; old grant + env vars left in place; new env vars added | Yes -- `dbff7603bf` |
| `infra/aws/lambda/ci/lambda-source-map.json` | Artifact SHA256 update (cot-etf-ownership-daily) + an incidental correct reconcile of `cot-bd-session-trigger`'s stale record to its true live state | Yes -- `2c0b5a3c20`, `cb8d4e1f60` |
| `infra/aws/terraform/cot-pipeline/CHANGELOG.json` | record-terraform-deploy append | Yes -- `cb8d4e1f60` |
| `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/pipeline_inventory.xml` | cottonwood + 49F entries corrected; inflection cancellation noted | Yes -- `f4c1126aa5` |

`infra/aws/lambda/inf-pipeline/inf-etf-ownership-daily/*` and
`infra/aws/terraform/inf-pipeline/inf-etf-ownership-daily.tf`: **NOT touched.**

All commits local on `CLOUD`, un-pushed by design (integrator-only push, LD-0367/0368).

---

## Blockers

None on my side. Two items routed elsewhere, not blocking this task's close:
1. **[Andrew / CTO]** New source for inflection's ETF-ownership producer is an
   open architectural question (the monolith source is disqualified; the old
   inf-gold source has the original defect). Not mine to resolve unilaterally.
2. **[CTO / COO]** `cot-pipeline`'s Terraform carries ~3-day-old committed-but-
   unapplied drift (`schedule-et.tf`'s `cot_bd_session_daily_et` Scheduler move +
   `ssm.tf`'s `cot_bronze_run` retry-net, both Andrew-direct via CTO 2026-07-29)
   that I deliberately did not apply alongside my scoped change. Someone should
   apply it (or confirm it's intentionally held) -- I'm flagging discovery, not
   claiming to know its current intended status.

---

## Current State

`bd-49f-etf-ownership-daily`: unchanged, reverified green (AC2 exact match live).
`cot-etf-ownership-daily`: repointed, deployed, 0-diff on the resources I own,
AC3/AC5/AC6/AC7/AC8 all confirmed against live/deployed state, tag
`cot-pipeline-v0.7.3` cut locally. `inf-etf-ownership-daily`: untouched, task
CANCELLED by CTO ruling. Evidence report going to CTO next; cot-pipeline's
unrelated stale drift flagged separately.

---

## Next Steps

1. **[1.0.0_SA_CTO]** Validate AC2-AC8 evidence (49F + cottonwood) and close the
   repoint task for those two legs, or REWORK with a named gap.
2. **[0.0.0_AB_MSTR]** Pull the local `CLOUD` commits (`dbff7603bf`..`f4c1126aa5`)
   + tag `cot-pipeline-v0.7.3` at the next integration window.
3. **[CTO / COO]** Decide what to do about the ~3-day-old unapplied
   `schedule-et.tf`/`ssm.tf` drift in cot-pipeline (not part of this task; flagged
   as a discovery).
4. **[Andrew / CTO]** Rule on inflection's replacement source -- open architecture
   question, not an AE call.
