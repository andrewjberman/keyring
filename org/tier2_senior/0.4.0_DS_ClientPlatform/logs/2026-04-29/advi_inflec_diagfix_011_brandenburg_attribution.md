# DS — ADVI_INFLEC.DIAGFIX.011: Advisor attribution fix (Joe Brandenburg + servicing rep population)

**Agent serial:** `0.4.0_DS_ClientPlatform`
**Date:** 2026-04-29 (session 4, post `/clear` cycle 3)
**Session shape:** Andrew-flagged advisor missing from data → self-scoped 6-phase TO → Andrew "run it now" → JWT refresh + full pipeline live execution
**Outcome:** Brandenburg surfaces as 4th first-class advisor with rep_id=6, 67 accounts, $16.15M, Orion-native composition.json live on S3. accounts_v2 rep_id 100% populated (was 0%).

---

## Mandate Origin

Andrew direct chat 2026-04-29 (post DIAGFIX.010 RAVC):
- "Are you sure about that because when i add joe brandenberg we are back up to 198.87m which is more reasonable of a number"
- "I think he has his own advisor number and we need to figure it out"
- "yes scope it and start build"
- "run it now"

DS self-scoped TO `ADVI_INFLEC.DIAGFIX.011.ds-advisor-attribution-fix.md`. COO ACK confirmed Andrew authorization + clean numbering hygiene (.011 avoids .009 collision with AE-filed pricing-strategy TO). Aligned with COO's independently-flagged follow-on candidate from DIAGFIX.010 close.

---

## Investigation Findings

**Joe Brandenburg = rep_id=6** in Orion (`TAN Inflection Brandenburg`, 21 households). Discovered via `GET /api/v1/Portfolio/Representatives` (returns all 18 reps); confirmed via `GET /api/v1/Portfolio/Clients?representativeId=6` returning 21 client records (cids 24, 32, 51, 63, 126, 141, 161, 190, 219, 221, 223, 284, 334, 394, 403, 449, 481, 497, 515, 540, 550).

**Root cause located:** `data/orion/scripts/silver/convert_orion_api_to_silver.py:410` — `build_accounts_v2()` explicitly set `out['rep_id'] = None`. The NewPortfolio API (`GET /Portfolio/Accounts/NewPortfolio`) only carries the firm-level `representativeName` field which shows 3 values (Inflection Wealth Management 818 / Peter Lee 29 / Patrick Scanlan 3). Brandenburg's 67 accounts rolled up under "Inflection Wealth Management" because servicing rep is captured in a separate Orion endpoint (`/Portfolio/Representatives` + `/Portfolio/Clients?representativeId=N`).

**Math reconciliation:** my DIAGFIX.010 pull at $197.86M ≈ Andrew's UI-with-Brandenburg figure $198.87M (~$1M intra-day delta). Original $182.55M target was the scope-incomplete UI view that excluded him. Brandenburg's data was IN our dataset the whole time, just mis-attributed.

**Bonus:** the rep master endpoint surfaces 18 reps total; 7 Inflection-relevant (3, 6, 7, 8, 10, 11, 12). Reps 7/8/10 are 0-household joint placeholders today (Brandenburg/IWM, Brandenburg/Lee, Soderblom).

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/manual_api/pull_inflection_representatives.py` | NEW — bronze pull: `/Portfolio/Representatives` (18 reps) + per-rep `/Portfolio/Clients?representativeId=N` for Inflection-relevant `[3,6,7,8,10,11,12]`. Outputs to `bronze/orion-api-v2/{date}/representatives.json` + `household_rep_mapping.json` |
| `data/orion/scripts/silver/convert_orion_api_to_silver.py` | EDIT — Added `build_representatives()` + `build_household_rep_mapping()` builders. Augmented `build_accounts_v2()` to JOIN household_rep_mapping → populate `rep_id` (Int64) + override `representative_name` via combine_first. Removed line 410 `out['rep_id'] = None` |
| `data/orion/scripts/gold/INF_I_D03.composition_artifacts.py` | EDIT — Added accounts_v2 advisor_key override at lookup time. Without re-running INF_B_00 (30-60min EC2), Brandenburg's accounts continued to roll under IWM because the canonical holdings parquet had stale `advisor_key` baked in. Override JOINs lots with accounts_v2 on account_id, slugifies representative_name, and uses combine_first to write the new advisor_key |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFLEC.DIAGFIX.011.ds-advisor-attribution-fix.md` | NEW — TO authored, 6 phases, COO ACK'd |

---

## 6-Phase Execution

### Phase 1 — Bronze pull (live)

```
GET /api/v1/Portfolio/Representatives → 18 rows
GET /api/v1/Portfolio/Clients?representativeId=N for [3,6,7,8,10,11,12] → 313 (household, rep) tuples
```

Per-rep household counts confirmed:

| rep_id | name | households |
|---|---|---|
| 3 | Inflection Wealth Management | 13 |
| **6** | **Joe Brandenburg** | **21** |
| 7 | Joe Brandenburg/IWM | 0 |
| 8 | Joe Brandenburg/Lee | 0 |
| 10 | Noel Soderblom | 0 |
| 11 | Patrick Scanlan | 76 |
| 12 | Peter Lee | 203 |

Bronze artifacts: `bronze/orion-api-v2/2026-04-29/representatives.json` (25,778 bytes) + `household_rep_mapping.json` (42,605 bytes).

### Phase 2 — Silver dim builders

Added two new builders to `convert_orion_api_to_silver.py`:

- `build_representatives()` — silver/api_dims/representatives/snapshot_date={date}/data.parquet — 18 rows, 16 keep-columns (rep_id Int64, full_name, repNo, household_count, isActive, status, brokerDealer, riaName, etc.)
- `build_household_rep_mapping()` — silver/api_dims/household_rep_mapping/snapshot_date={date}/data.parquet — 313 rows (one per household), with primary servicing rep picked via priority:
  1. Individual servicing reps `{6, 10, 11, 12}` (Brandenburg / Soderblom / Scanlan / Lee)
  2. Joint placeholder reps `{7, 8}` (Brandenburg/IWM, Brandenburg/Lee)
  3. Firm-level rep `3` (Inflection Wealth Management catch-all)
  Additional rep_ids preserved as semicolon-joined string for joint coverage.

### Phase 3 — accounts_v2 augment

`build_accounts_v2()`:
- REMOVED line 410 `out['rep_id'] = None`
- ADDED household_rep_mapping JOIN on `household_id` when bronze available
- Populates `rep_id` (Int64) from mapping
- Override `representative_name` via `combine_first` (mapping's rep_name wins; fallback to NewPortfolio's representativeName for households outside mapping)
- Backward-compat fallback: when mapping bronze is absent for a snapshot_date, falls through to prior behavior (`rep_id=NA`)

### Phase 4 — Live silver re-run

```
DIM representatives:        18 rows  → silver/api_dims/representatives/snapshot_date=2026-04-29/data.parquet
DIM household_rep_mapping:  313 rows → silver/api_dims/household_rep_mapping/snapshot_date=2026-04-29/data.parquet
DIM accounts_v2:            849 rows → silver/api_dims/accounts_v2/snapshot_date=2026-04-29/data.parquet
```

**accounts_v2 verification (the headline):**

| representative_name | accounts | rep_id |
|---|---|---|
| Peter Lee | 617 | 12 |
| Patrick Scanlan | 152 | 11 |
| **Joe Brandenburg** | **67** | **6** |
| Inflection Wealth Management | 13 | 3 |

`rep_id` non-null: **849/849 (100%)** — was 0/850 before DIAGFIX.011.

Brandenburg breakdown: 21/21 households (100% coverage), 67 accounts, $16,152,464.27 firm AUA contribution.

Total firm AUA: $197,686,462.71 ≈ Andrew's UI-with-Brandenburg target $198.87M.

### Phase 5 — Gold re-run + surgical override fix

First run of INF_I_D03 with new accounts_v2 silver dim showed only 3 advisor_keys (still). Root cause: `gold/canonical/holdings_2026-04-28.parquet` (input to INF_I_D03) had `advisor_key` baked in from a prior INF_B_00 run with the OLD accounts_v2. Without re-running INF_B_00 (30-60min EC2), Brandenburg would continue rolling under IWM downstream.

Surgical fix added to INF_I_D03 at advisor_key resolution time:
1. Load latest silver/api_dims/accounts_v2
2. Build per-account_id slug from representative_name (lower-case, regex-replace non-alphanumeric with underscore)
3. JOIN with lots, override existing advisor_key via combine_first

Re-run result: **3 → 4 unique advisor_keys**.

### Phase 6 — Verification

`platinum/advisors/joe_brandenburg/composition.json` LIVE on S3:

| Field | Value |
|---|---|
| scope | {advisor_id: joe_brandenburg, firm_id: inflection} |
| classification_method | orion_native_v1 |
| total_market_value | $14,622,237.23 |
| mix.equity | $8,321,324.84 (56.91%) |
| mix.fixed_income | $4,245,128.69 (29.03%) |
| mix.alternatives | $1,134,792.83 (7.76%) |
| mix.cash | $920,990.88 (6.30%) |
| top_holdings | VOO $2.46M, HTRB $962K, BAGIX $900K, FDRXX $879K, CIVIX $868K |
| unclassified | 0 |

The $14.62M (composition) vs $16.15M (accounts_v2) delta is the holdings-vs-accounts_v2 sourcing gap also seen at firm level — separate from DIAGFIX.011 scope (AE 0.6.1's pending DIAGFIX.009 pricing-strategy territory).

**4 advisor compositions now live on S3:** inflection_wealth_management, joe_brandenburg, patrick_scanlan, peter_lee. mix_summary.json republished (firm-level unchanged: equity 53.93 / fixed_income 30.93 / alternatives 8.08 / cash 6.53; orion_native_v1 propagation verified).

---

## JWT Refresh Cycle

JWT had expired at 22:26Z, 17 min before my first Phase 4 attempt. Andrew authorized direct invoke ("run it now"). I invoked `inf-jwt-trigger` Lambda at 22:50Z; COO independently fired at 22:51Z (one minute later — same instance, no duplicate harm).

EC2 stuck at "stopped" for ~12 min before transitioning to "pending" at 23:02:43Z and "running" at 23:02:54Z. Initial state transition reported as `Server.InternalError`.

COO diagnosed root cause **separately and shipped fix while my work continued**:
- Top-level `StateTransitionReason: Server.InternalError` masked underlying `StateReason: Client.InvalidKMSKey: Invalid KMS key provided`
- CMK `arn:aws:kms:us-east-1:313476888478:key/4ba4753c-98f4-47c0-9a47-6dacaa1b6370` (alias `alias/inf-ebs-key`) had ZERO grants
- Lambda role `inf-jwt-trigger-lambda-role` had no KMS permissions at all
- Volume attach failed → instance rolled back to stopped

COO's fix (manual `aws iam put-role-policy` — Terraform-ize follow-on filed for AE 0.7.0): inline policy `inf-jwt-trigger-kms` with `kms:CreateGrant` (guarded by `kms:GrantIsForAWSResource: true`) + key-use ops. AWS now auto-creates per-instance grant on Lambda invoke.

Verified: grant created at 23:02:45Z (KMS) → instance reached running at 23:02:54Z (EC2). New JWT landed in S3 at 23:08:26Z (issued; expires 2026-04-30T09:09:26Z). Phase 4-6 ran 23:09Z-23:12Z.

---

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| 1 — before write (each script) | `comp-pipescript io <script>` | SKIPPED — Orion scripts not in BD-pipeline graph |
| 2 — before commit (each script) | `.tools/ds-commit-gate.sh <files>` | PASS on every file |
| 3 — after S3 upload | manual MD5 verify | MATCH on every uploaded script |

Pre-commit gate ran 5+ times this session. No `--force` audit entries. No bypasses.

---

## Deploy Cycle Summary

| Commit | Phase | Push | S3 (script) MD5 |
|---|---|---|---|
| `72628a1df` | Phase 1+2+3 (bronze + silver + accounts_v2 augment + TO file) | CLOUD | `pull_inflection_representatives.py 19dcaf38…` MATCH; `convert_orion_api_to_silver.py 4f89eb0f…` MATCH |
| `f21ab4b44` | Phase 5 surgical fix (INF_I_D03 advisor_key override) | CLOUD | `INF_I_D03.composition_artifacts.py ce40874a…` MATCH |

All commits authored as `0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>` via `.tools/safe-commit.sh`. No bare `git commit`. No contamination aborts.

S3 artifacts written this session:
- `bronze/orion-api-v2/2026-04-29/representatives.json`
- `bronze/orion-api-v2/2026-04-29/household_rep_mapping.json`
- `bronze/orion-api/2026-04-29/new_portfolio_accounts.json` (refreshed for snapshot_date alignment)
- `silver/api_dims/representatives/snapshot_date=2026-04-29/data.parquet`
- `silver/api_dims/household_rep_mapping/snapshot_date=2026-04-29/data.parquet`
- `silver/api_dims/accounts_v2/snapshot_date=2026-04-29/data.parquet`
- `platinum/firm/firm_composition.json` + 4 advisor compositions
- `platinum/firm/mix_summary.json`

---

## RAVC Loops

| To | Subject | Time |
|----|---------|------|
| 2.0.0_SA_COO | RAVC ACK — DIAGFIX.010 close received; DIAGFIX.011 Andrew-authorized | 20260429T223800Z |
| 2.0.0_SA_COO | RAVC EVIDENCE — DIAGFIX.011 Phase 1+2+3 SHIPPED (code) — Phase 4-6 BLOCKED on JWT | 20260429T224407Z |
| 0.6.1_AE_PartnerETL | FYI — DIAGFIX.011 Phase 1+2 scripts shipped; chain registration request | 20260429T224424Z |
| 2.0.0_SA_COO | RAVC ACK — JWT trigger already invoked direct (Andrew "run it now") | 20260429T225133Z |
| 2.0.0_SA_COO | RAVC EVIDENCE — DIAGFIX.011 Phase 4-6 SHIPPED (Brandenburg surfaces) | 20260429T231239Z |
| 2.0.0_SA_COO | RAVC ACK — KMS-grant fix understood + Phase 4-6 already shipped | (this session close) |

Inbox: 5 inbound (4 COO + 1 AE). All ACK'd within session.

---

## Acceptance Criteria

| # | Criterion | Status |
|---|---|---|
| 1 | bronze JSON files on S3 (representatives + household_rep_mapping) | PASS |
| 2 | silver/api_dims/representatives 18 rows + Brandenburg rep_id=6 | PASS |
| 3 | silver/api_dims/household_rep_mapping 21 Brandenburg households | PASS — 313 total |
| 4 | accounts_v2 rep_id non-null + Brandenburg surfacing | PASS — 100% populated, 67 accounts under "Joe Brandenburg" |
| 5 | platinum/advisors/joe_brandenburg/composition.json with orion_native_v1 | PASS — $14.62M, 4-bucket Orion-truth split |
| 6 | Pre-commit gate exit 0 + S3 deploy MATCH for each script | PASS |
| 7 | RAVC to COO with full evidence | DELIVERED |

---

## Standing State

DIAGFIX.011 fully shipped (all 6 phases). 4 advisors now first-class on S3. accounts_v2 attribution complete.

**Queued:**
- AE 0.6.1's DIAGFIX.009 (`ds-holdings-pricing-strategy.md`) Phase 1 probe — Orion `Activity.Value(EndingMV)` daily-coverage assessment over 30-day window. Two surface candidates: existing Verbose API harness OR `/Reporting/Scope` endpoint from HAR (7) Activity-series calc. Will RAVC after probe.
- AE 0.6.1 chain registration of DIAGFIX.011 scripts in `orion-gold-dispatch.sh` CATALOG / CHAIN_FULL / CHAIN_INCREMENTAL — FYI sent earlier.
- AE 0.7.0 follow-on (filed by COO): Terraform-ize the inline KMS IAM policy for `inf-jwt-trigger-lambda-role`.
- DIAGFIX.008 Step 2 (INF_D_04 timeseries.mix integration) — still queued from earlier session.

Heartbeat current. Inbox watcher running.

---

## Files Modified (table)

| File | Change |
|------|--------|
| `data/orion/manual_api/pull_inflection_representatives.py` | NEW — Phase 1 bronze pull (representatives + per-rep clients) |
| `data/orion/scripts/silver/convert_orion_api_to_silver.py` | EDIT — Phase 2 builders + Phase 3 accounts_v2 augment |
| `data/orion/scripts/gold/INF_I_D03.composition_artifacts.py` | EDIT — Phase 5 surgical advisor_key override from accounts_v2 |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFLEC.DIAGFIX.011.ds-advisor-attribution-fix.md` | NEW — TO file |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-29/advi_inflec_diagfix_011_brandenburg_attribution.md` | THIS LOG |

---

## Next Steps

- [DS / NEXT] AE 0.6.1's DIAGFIX.009 (holdings pricing strategy) Phase 1 — probe Orion `Activity.Value(EndingMV)` daily coverage
- [AE 0.6.1] Chain-register DIAGFIX.011 scripts in `orion-gold-dispatch.sh` (FYI sent)
- [AE 0.7.0] Terraform-ize the inline KMS IAM policy for `inf-jwt-trigger-lambda-role` (COO-filed follow-on)
- [DE 0.4.0] Optional: verify Brandenburg's drilldown page renders correctly with the new composition.json
- [Future / Optional] Re-run INF_B_00 to bake the corrected advisor_key into canonical holdings (currently mitigated by Phase 5 override; INF_B_00 re-bake is an optimization, not a correctness fix)

---

*Authored by `0.4.0_DS_ClientPlatform`. Session arc: ~50 min for 6 phases including JWT-refresh wait. 2 commits, 3 S3 script uploads, 8+ S3 artifact publishes, 6 RAVC messages, 0 destructive ops, 0 contamination aborts, 0 hook bypasses.*
