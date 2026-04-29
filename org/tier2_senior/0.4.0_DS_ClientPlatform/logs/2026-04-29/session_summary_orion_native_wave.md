# DS — Session Summary: Orion-native Wave (DIAGFIX.008 Step 1 → .010 → .011 → .009-NEW Phase 1)

**Agent serial:** `0.4.0_DS_ClientPlatform`
**Date:** 2026-04-29 (PM)
**Session window:** ~3.5 hours of code + investigation across 4 TOs
**Outcome:** Inflection portal classification and advisor attribution went from regex-keyword fallback to Orion-native truth in one continuous wave. Bond-ETF over-classification killed. Brandenburg surfaced. Daily MV path discovered.

---

## Session Arc

This session evolved through three distinct phases as Andrew + COO surfaced fresh constraints / evidence:

1. **DIAGFIX.008 Step 1 (composer ship)** — published `platinum/firm/mix_summary.json` from existing `firm_composition.json`. Started with regex-keyword `classification_method='keyword_regex_v1'` metadata.

2. **DIAGFIX.009 (Morningstar hunt) → DIAGFIX.010 (refactor)** — Andrew's HAR file (api.cloud.orionadvisor.com(6).har) revealed `/api/v1/Portfolio/Clients/{cid}/Assets/{date}` returns 100% Morningstar Category coverage. Replaced INF_I_D03 keyword classifier with Orion-native lookup. Deleted 4 functions + 5 keyword constants. Composer auto-flipped to `orion_native_v1`. Bond ETFs (HTRB/BAGIX/BSIIX/BSNIX/TFEBX) correctly classified.

3. **DIAGFIX.011 (Brandenburg attribution)** — Andrew flagged "Joe Brandenberg" missing. Discovery: his $16.22M was IN our data the whole time, just mis-attributed to "Inflection Wealth Management" because NewPortfolio API only carries firm-level rep, not servicing rep. Built `pull_inflection_representatives.py` + augmented `build_accounts_v2()` with household_rep mapping. Surgical INF_I_D03 advisor_key override avoided 30-60min INF_B_00 re-bake.

4. **DIAGFIX.009-NEW Phase 1 (holdings pricing probe)** — AE 0.6.1 filed parallel TO addressing the deeper $8M holdings-vs-aum_snapshot delta. Probe revealed the SAME endpoint we already use for assets_v2 supports historical dates → Path A (no Yahoo Finance fallback needed). Phase 2-5 deferred to DIAGFIX.012, GO timing pending Andrew.

---

## TO Coverage

| TO | Type | Status | Ship commit | Sub-log |
|----|------|--------|-------------|---------|
| ADVI_INFLEC.DIAGFIX.008 Step 1 | Build, composer | SHIPPED | `15a8f8591` (Step 1) + `6f60a47eb` (metadata fix) | `advi_inflec_diagfix_008_step1_mix_summary_composer.md` |
| ADVI_INFLEC.DIAGFIX.009 (Morningstar hunt) | Investigation, HAR | VERDICT A | `8d8be1bcd` | covered in `advi_inflec_diagfix_009_010_orion_native_classifier.md` |
| ADVI_INFLEC.DIAGFIX.010 (Orion-native classifier) | Refactor | SHIPPED | `2979c12a7` (Phase 1+2) + `e106bc7b8` (Phase 3) | covered in `advi_inflec_diagfix_009_010_orion_native_classifier.md` |
| ADVI_INFLEC.DIAGFIX.011 (Brandenburg attribution) | Build, attribution | SHIPPED | `72628a1df` (Phase 1+2+3) + `f21ab4b44` (Phase 5 surgical) | `advi_inflec_diagfix_011_brandenburg_attribution.md` |
| ADVI_INFLEC.DIAGFIX.009-NEW Phase 1 (pricing probe) | Investigation | VERDICT A | `91da4d6a1` | `advi_inflec_diagfix_009_new_phase1_pricing_probe.md` |

Plus session-log commits.

---

## Files Touched

| File | Action | TOs |
|------|--------|-----|
| `data/orion/scripts/gold/INF_I_D02d.firm_mix_summary.py` | NEW (~270 LOC) → metadata-inheritance fix | .008, .010 |
| `data/orion/manual_api/PATH_DISCOVERY_MSTAR.md` | NEW — endpoint contract for /Portfolio/Clients/{cid}/Assets/{date} | .009 |
| `data/orion/manual_api/probe_mstar_paths.py` | NEW — TRACK 1 Verbose-API FAIL-pattern artifact | .009 |
| `data/orion/manual_api/pull_inflection_assets_v2.py` | NEW — Orion REST asset pull (296 households, all 58 cols) | .010 |
| `data/orion/scripts/silver/convert_assets_v2_to_silver.py` | NEW — bronze→silver type-coercion + camelCase→snake_case | .010 |
| `data/orion/scripts/gold/INF_I_D03.composition_artifacts.py` | REFACTOR (Phase 3) → ADD advisor_key override (Phase 5) | .010, .011 |
| `data/orion/manual_api/pull_inflection_representatives.py` | NEW — bronze pull (Reps + per-rep clients) | .011 |
| `data/orion/scripts/silver/convert_orion_api_to_silver.py` | EDIT — added build_representatives + build_household_rep_mapping; augmented build_accounts_v2 with JOIN | .011 |
| `data/orion/manual_api/probe_positions_mv_daily.py` | NEW — 4-probe pricing investigation | .009-NEW |

---

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| 1 — before write (each script) | `comp-pipescript io <script>` | SKIPPED — Orion scripts not in BD-pipeline graph (documented gap, applies to all DIAGFIX TOs) |
| 2 — before commit (each script) | `.tools/ds-commit-gate.sh <files>` | PASS on every modified file |
| 3 — after S3 upload | manual MD5 verify (registry gap precedent) | MATCH on every uploaded script |

Pre-commit gate ran 10+ times across the wave. Caught and auto-fixed:
- 1× ruff F401 (unused `BytesIO` in INF_I_D02d composer)
- 1× ruff F401 (unused `date` in convert_assets_v2_to_silver)
- 2× ruff F541 (f-string-without-placeholders in probe_mstar_paths and probe_positions_mv_daily)
- 1× ruff F541 (f-string in probe_positions_mv_daily; round 2)

No `--force` audit entries. No bypasses. No contamination aborts.

---

## Deploy Cycle Summary

| TO / Phase | Commit | Push | S3 (script) MD5 |
|---|---|---|---|
| .008 Step 1 — composer | `15a8f8591` | CLOUD | `c35f1b42…` MATCH |
| .008 docs (logs) | `74d4a9163` | CLOUD | (docs only) |
| .009 — PATH_DISCOVERY_MSTAR + probe | `8d8be1bcd` | CLOUD | (docs/probe) |
| .010 Phase 1+2 — bronze + silver | `2979c12a7` | CLOUD | `d8e57b16…` + `6b7d3f7c…` MATCH |
| .010 Phase 3 — INF_I_D03 refactor | `e106bc7b8` | CLOUD | `dc28bc14…` MATCH |
| .010 Phase 4 — composer metadata-inheritance | `6f60a47eb` | CLOUD | `e8ed80f0…` MATCH |
| .010 docs | `03fb28ea0` | CLOUD | (docs only) |
| .011 Phase 1+2+3 — bronze + silver + accounts_v2 augment + TO | `72628a1df` | CLOUD | `19dcaf38…` + `4f89eb0f…` MATCH |
| .011 Phase 5 — INF_I_D03 advisor_key override | `f21ab4b44` | CLOUD | `ce40874a…` MATCH |
| .011 docs | `484bf0895` | CLOUD | (docs only) |
| .009-NEW Phase 1 — pricing probe | `91da4d6a1` | CLOUD | (probe only) |

All commits authored as `0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>` via `.tools/safe-commit.sh`. Zero bare `git commit`, zero contamination aborts, zero hook bypasses.

---

## Live S3 State (post-wave)

| Artifact | State |
|---|---|
| `silver/api_dims/assets_v2/snapshot_date=2026-04-29/data.parquet` | NEW — 23,699 rows, 58 cols, 100% asset_class + product_category coverage |
| `silver/api_dims/representatives/snapshot_date=2026-04-29/data.parquet` | NEW — 18 rows (Inflection rep master) |
| `silver/api_dims/household_rep_mapping/snapshot_date=2026-04-29/data.parquet` | NEW — 313 rows (one per household with primary servicing rep + additional_rep_ids) |
| `silver/api_dims/accounts_v2/snapshot_date=2026-04-29/data.parquet` | REPUBLISHED — 849 rows, rep_id 100% populated (was 0%), 4 distinct rep names |
| `bronze/orion-api-v2/2026-04-29/representatives.json` | NEW |
| `bronze/orion-api-v2/2026-04-29/household_rep_mapping.json` | NEW |
| `bronze/orion-api-v2/2026-04-29/assets.parquet` | NEW |
| `bronze/orion-api/probe/probe_diagfix009_findings.json` | NEW (probe output) |
| `bronze/orion-api/probe/positions_mv_30d.csv` | NEW (probe sample) |
| `platinum/firm/firm_composition.json` | REPUBLISHED — Orion-native classifications, 4 advisors aggregated |
| `platinum/firm/mix_summary.json` | REPUBLISHED — `classification_method=orion_native_v1` (was `keyword_regex_v1`) |
| `platinum/advisors/joe_brandenburg/composition.json` | NEW — first time Brandenburg appears as a first-class advisor |
| `platinum/advisors/inflection_wealth_management/composition.json` | REPUBLISHED |
| `platinum/advisors/peter_lee/composition.json` | REPUBLISHED |
| `platinum/advisors/patrick_scanlan/composition.json` | REPUBLISHED |
| `code/manual_api/pull_inflection_assets_v2.py` | NEW |
| `code/manual_api/pull_inflection_representatives.py` | NEW |
| `code/silver/convert_assets_v2_to_silver.py` | NEW |
| `code/silver/convert_orion_api_to_silver.py` | UPDATED |
| `code/gold/INF_I_D03.composition_artifacts.py` | UPDATED twice (Orion-native classifier + advisor_key override) |
| `code/gold/INF_I_D02d.firm_mix_summary.py` | UPDATED (metadata-inheritance) |

---

## Math Reconciliation (locked across DIAGFIX.010 + .011)

| View | Value | Source |
|------|-------|--------|
| Andrew UI without Brandenburg | $182.55M | UI screenshot (initial COO target) |
| Andrew UI with Brandenburg | $198.87M | Andrew chat 2026-04-29 |
| accounts_v2 total | $197.69M | post-DIAGFIX.011 silver dim |
| Orion bronze positions | $197.86M | DIAGFIX.010 pull (296 households × all assets) |
| Holdings parquet (TRN-reconstructed) | $190.54M | INF_B_00 post nav>0 fix |
| aum_snapshot.managed_value | $182.6M | Orion AUM API canonical |

The $7-15M deltas across these are SOURCING differences. DIAGFIX.009-NEW Phase 1 confirmed the path to resolve them (Path A — daily per-position MV from `/Portfolio/Clients/{cid}/Assets/{date}` historical-date support). Brandenburg's $14.62M-vs-$16.15M (composition vs accounts_v2) is the same pattern at advisor-level scope.

---

## Mix-percentage Evolution (firm-level)

| Source | equity | fixed_income | cash | alternatives |
|---|---|---|---|---|
| Andrew UI top-9 + "Other" residual (initial target) | 44.8% | 21.3% | 5.4% | 28.5% |
| Regex classifier (pre-DIAGFIX.010) | 70.29% | 15.22% | 12.70% | 1.79% |
| **Orion-native classifier (post-DIAGFIX.010)** | **53.93%** | **30.93%** | **6.53%** | **8.08%** |

The "Other 28.5%" UI target was a TOP-9-RESIDUAL UI display artifact (long-tail named Morningstar Categories like Foreign Large Blend, Small Blend, Mid-Cap Value, Real Estate, etc.), NOT a true alternatives bucket. Andrew + COO accepted the Orion-truth answer. Bond-ETF over-classification fully resolved.

---

## RAVC Loops (chronological)

The wave generated 18 inter-agent messages across COO + AE 0.6.1:

1. ACK DIAGFIX.008 scope amendment received → STEP 0 starting
2. VERDICT DIAGFIX.008 STEP 0 (Orion classification investigation + Opal scan)
3. EVIDENCE DIAGFIX.008 Step 1 SHIPPED (composer + mix_summary.json)
4. FYI to AE — INF_I_D02d composer needs orion-gold-dispatch.sh registration
5. ACK DIAGFIX.009 Morningstar hunt — Track 1 starting
6. VERDICT A DIAGFIX.009 — Orion REST endpoint found (HAR analysis)
7. ACK DIAGFIX.010 GO received — Phase 1 starting
8. EVIDENCE DIAGFIX.010 Phase 1+2 SHIPPED — bronze + silver assets_v2 + Brandenburg note
9. FYI to AE — DIAGFIX.010 Phase 1+2 scripts need chain registration
10. EVIDENCE DIAGFIX.010 Phase 3+4+5 SHIPPED — Orion-native classifier live
11. ACK DIAGFIX.011 GO + Andrew direct authorization — starting Phase 1
12. EVIDENCE DIAGFIX.011 Phase 1+2+3 SHIPPED (code) — Phase 4-6 BLOCKED on JWT
13. FYI to AE — DIAGFIX.011 Phase 1+2 scripts need chain registration
14. ACK JWT trigger already invoked direct (Andrew "run it now")
15. EVIDENCE DIAGFIX.011 Phase 4-6 SHIPPED (Brandenburg surfaces as 4th advisor)
16. ACK KMS-grant fix understood + Phase 4-6 already shipped
17. ACK DIAGFIX.011 close received — starting DIAGFIX.009-NEW Phase 1
18. EVIDENCE DIAGFIX.009-NEW Phase 1 — VERDICT PATH A
19. ACK Phase 1 acceptance received; standing by for GO/stage call

Inbox: 5 inbound (4 COO + 1 AE). All ACK'd within same wake. No silent receipts.

---

## Andrew Direct Interactions (chronological)

1. "i JUST WENT ON THEIR HOMEPAGE DASHBOARD..." → HAR file 6 provided → DIAGFIX.009 VERDICT A path
2. "197.86m as of when exactly" → answered: asOfDate=2026-04-29, intra-day snapshot
3. "i also fuond this top clients pag... HAR file 7" → flagged /Reporting/Scope endpoint for future Books-tab work
4. "i just noticed a new advisor appeared... Joe Brandenberg" → DIAGFIX.011 self-scoped
5. "Are you sure about that because when i add joe brandenberg we are back up to 198.87m" → math reconciliation locked
6. "I think he has his own advisor number and we need to figure it out" → rep_id=6 confirmed
7. "yes scope it and start build" → DIAGFIX.011 GO
8. "WE SHOULDNT NEED TO USE OUR BD-SECURITIES OR ETF CLASSIFIER OR REGEX OR ANY OF THAT BULLSHIT IT SHOULD JUST BE WHAT ORION USES HERE" → DIAGFIX.010 deleted all of that
9. "run it now" → JWT trigger Lambda directly invoked
10. "go get the jwt" (via COO) → JWT refresh triggered
11. "just run it" → manual JWT trigger authorized

11 direct authorizations / clarifications / pivots from Andrew across the wave.

---

## Watcher Activity

`org/mcp/inbox-watch.sh 0.4.0_DS_ClientPlatform` relaunched ~10 times across the session. All went via Bash tool with `run_in_background: true`. Several stale orphans reaped from prior sessions during early relaunches. No deliveries lost — belt-and-suspenders `check_inbox` + `get_agent_status` at every wake caught everything.

---

## Notable Architectural Wins

1. **Regex classifier deleted, not refactored.** Andrew's "no fallback paths just in case" directive landed cleanly. INF_I_D03 lost 4 functions + 5 keyword constants without backwards-compat shims. Pure Orion-native lookup against `silver/api_dims/assets_v2`.

2. **Composer metadata-inheritance pattern.** Composer reads `classification_method` + `classification_caveats` from upstream `firm_composition.json` instead of hardcoding. Future classifier upgrades auto-propagate without composer code changes. Pattern reusable for any DIAGFIX.012+ work that flips classification semantics.

3. **Servicing-rep priority.** Primary-rep priority (`{6,10,11,12} > {7,8} > {3}`) — "specific advisor wins" preserves attribution. Brandenburg's 21 households surface as his book; only un-attributed households roll up to firm bucket.

4. **Surgical advisor_key override.** Recognized that `gold/canonical/holdings_*.parquet` had stale baked-in `advisor_key` from prior INF_B_00. Chose JOIN-at-resolution-time override over 30-60min EC2 re-bake. Future INF_B_00 re-runs bake corrected `advisor_key` from the start; until then the override keeps gold artifacts current.

5. **DIAGFIX.009-NEW Phase 1 Path A discovery.** The same endpoint we already use for assets_v2 supports historical dates. Avoided new endpoint discovery, Yahoo Finance integration, A/B/C tier resolution. Discovery cost: 1 Python probe script.

---

## Infrastructure Lessons (for AE 0.7.0 follow-on)

1. **JWT-trigger KMS grant.** AWS-side `Server.InternalError` masked `Client.InvalidKMSKey` on EBS attach. CMK had zero grants; Lambda role had zero KMS perms. COO shipped manual `aws iam put-role-policy` with `kms:CreateGrant` (guarded by `kms:GrantIsForAWSResource:true`) + key-use ops. **Needs Terraform lift** by AE 0.7.0.

2. **Diagnostic guidance.** `aws ec2 describe-instances --query "Reservations[0].Instances[0].StateReason"` shows the real cause; top-level `StateTransitionReason` lies with `Server.InternalError`. Bookmark for future EC2 start failures.

3. **JWT-trigger SSM gap.** Lambda docstring claims `systemd inf-jwt-fetch.service` handles `jwt-extract` mode on EC2 boot, but no such unit exists. SSM document `opal-inf-export-run` only handles bronze export (no `Mode`/`EXPORT_MODE` param). Workaround used today: COO manually dispatched `EXPORT_MODE=jwt-extract` via SSM RunCommand. **AE 0.7.0 follow-on needed: extend SSM doc with Mode param + Lambda `_handle_jwt_extract()` calls `_send_export_command(Mode=jwt-extract)`.**

---

## Standing State

| TO | Status | Disposition |
|----|--------|-------------|
| DIAGFIX.008 Step 1 | SHIPPED + COO-CLOSED | mix_summary.json composer live |
| DIAGFIX.008 Step 2 | QUEUED | INF_D_04 timeseries.mix integration; deferred behind DIAGFIX.012 (would benefit from new positions_mv silver dim) |
| DIAGFIX.009 (Morningstar hunt) | VERDICT A → COO-CLOSED | endpoint found; absorbed into .010 |
| DIAGFIX.010 (Orion-native classifier) | SHIPPED + COO-CLOSED | regex deleted; classifier Orion-native |
| DIAGFIX.011 (Brandenburg attribution) | SHIPPED + COO-CLOSED | 4 advisors live; rep_id 100% populated |
| DIAGFIX.009-NEW (holdings pricing) Phase 1 | VERDICT A → COO-CLOSED | path A confirmed; Phase 2-5 → DIAGFIX.012 |
| DIAGFIX.012 (planned Path A implementation) | AWAITING ANDREW GO/STAGE CALL | TO scaffold authoring queued at COO |

Heartbeat current. Inbox watcher running. No active execution; standby for either Andrew's GO timing call on DIAGFIX.012 or any new directive.

---

## Sub-logs

| Topic | File |
|-------|------|
| DIAGFIX.008 Step 1 — full detail | `advi_inflec_diagfix_008_step1_mix_summary_composer.md` |
| DIAGFIX.009 + .010 — Orion-native classifier wave | `advi_inflec_diagfix_009_010_orion_native_classifier.md` |
| DIAGFIX.011 — Brandenburg attribution full detail | `advi_inflec_diagfix_011_brandenburg_attribution.md` |
| DIAGFIX.009-NEW Phase 1 — pricing probe | `advi_inflec_diagfix_009_new_phase1_pricing_probe.md` |
| THIS SUMMARY | `session_summary_orion_native_wave.md` |

---

## Next Steps

### Andrew (timing decisions)

- [Andrew] **GO-vs-stage timing call on DIAGFIX.012** (Path A implementation: `silver/positions_mv` daily layer + INF_B_00 refactor). Option A: ship tonight, ~150 min backfill window. Option B (COO lean): stage TO + GO tomorrow morning fresh context.
- [Andrew] Confirm Bucket-percentage interpretation locked: Orion-native 4-bucket (53.93/30.93/8.08/6.53) is the answer; UI top-9-residual "Other 28.5%" was a display artifact, not a true alternatives bucket.
- [Andrew] Optional: provide HAR file capturing the asset-class breakdown screenshot timestamp Inflection UI showed $182.55M (so we can confirm what scope filter excluded Brandenburg in that screenshot, for documentation purposes).

### COO 2.0.0_SA_COO

- [COO] **Author DIAGFIX.012 TO scaffold** (per their 23:26Z message; will land regardless of timing). Should include Phase 2-5 from the Phase 1 RAVC: bronze pull script + silver positions_mv builder + INF_B_00 refactor + re-run + validation.
- [COO] Issue formal GO when Andrew picks timing (or stage TO with clear "DS waiting on GO" note).
- [COO] Decide on DIAGFIX.008 Step 2 sequencing — INF_D_04 `timeseries_overview.mix.quarterly/monthly` integration. May want to defer behind DIAGFIX.012 since the new positions_mv silver dim will give us per-day per-asset MV for true multi-period backfill (vs the V1-current-period-only that DIAGFIX.008 Step 1 ships).
- [COO] Audit AE 0.6.1's chain-registration completion of DIAGFIX.010 + .011 scripts (two FYI messages sent; if AE silent, prompt).

### AE 0.6.1_AE_PartnerETL

- [AE 0.6.1] **Chain-register DIAGFIX.010 scripts** in `data/orion/scripts/gold/orion-gold-dispatch.sh`:
  - `pull_inflection_assets_v2.py` (bronze, FIRST in chain — no upstream deps; reads silver/api_dims/accounts_v2 for clientId list)
  - `convert_assets_v2_to_silver.py` (silver, depends on bronze pull above)
  - Suggested CATALOG entries given in earlier FYI message (20260429T221940Z)
- [AE 0.6.1] **Chain-register DIAGFIX.011 scripts** in same dispatch:
  - `pull_inflection_representatives.py` (bronze, FIRST in chain — no upstream deps)
  - `convert_orion_api_to_silver.py --dim representatives` (new dim name; same script as before)
  - `convert_orion_api_to_silver.py --dim household_rep_mapping` (new dim name; same script)
  - Sequencing: `representatives` + `household_rep_mapping` must run BEFORE `accounts_v2` (which now JOINs the mapping)
  - Suggested CATALOG entries in FYI message (20260429T224424Z)
- [AE 0.6.1] **DIAGFIX.012 follow-on (when authored):** chain-register the new positions_mv bronze pull + silver builder.
- [AE 0.6.1] **Awaiting:** the JWT pipeline diagnostic feedback to `0.7.0_AE_CloudOps` — KMS grant + SSM `Mode` extension. Cross-reference COO's filing.

### AE 0.7.0_AE_CloudOps

- [AE 0.7.0] **Terraform-ize the inline KMS IAM policy** that COO shipped manually 2026-04-29. Add to `infra/aws/terraform/inf-pipeline/iam.tf` for `inf-jwt-trigger-lambda-role`:
  - Inline policy `inf-jwt-trigger-kms` with `kms:CreateGrant` (guarded by `kms:GrantIsForAWSResource:true`) + key-use ops (`kms:Decrypt`, `kms:Encrypt`, `kms:ReEncrypt*`, `kms:GenerateDataKey*`, `kms:DescribeKey`) on `arn:aws:kms:us-east-1:313476888478:key/4ba4753c-98f4-47c0-9a47-6dacaa1b6370` (alias `alias/inf-ebs-key`)
  - Without Terraform: future `terraform apply --replace` on the role will wipe it. Recurrence of "Server.InternalError" on next `inf-jwt-trigger` invoke.
- [AE 0.7.0] **Extend SSM doc `opal-inf-export-run`** with a `Mode` parameter (Option A from COO's diagnosis):
  - Current: only handles bronze export, no Mode param
  - Lambda `_handle_jwt_extract()` should call `_send_export_command(Mode='jwt-extract')` for the JWT path
  - Without this fix: `inf-jwt-trigger --mode jwt-extract` is a stub — only writes a mode marker, doesn't actually fire the Playwright login. Manual SSM dispatch (as COO did tonight) remains required.
- [AE 0.7.0] **Diagnostic note for AE runbook:** AWS top-level `Reservations[0].Instances[0].StateTransitionReason` lies with `Server.InternalError`. The real cause lives in `Reservations[0].Instances[0].StateReason.Message`. Bookmark for future EC2 start failures.
- [AE 0.7.0] **Tag inf-pipeline-v1.6.6 or v1.7.0** after KMS Terraform lift + SSM extension land.

### DE 0.4.0_DE_ClientPlatform

- [DE 0.4.0] **Verify Brandenburg's drilldown page renders correctly** at the advisor route for `slug=joe_brandenburg`. Check:
  - composition.json fetch returns 200 (artifact already live on S3)
  - Mix donut renders with new 4-class breakdown (56.91 / 29.03 / 7.76 / 6.30)
  - Top holdings table shows VOO / HTRB / BAGIX / FDRXX / CIVIX
  - Advisor select dropdown / list includes Joe Brandenburg as 4th option (was 3)
- [DE 0.4.0] Optional: add Brandenburg to any hardcoded advisor lists (constants, mock data, test fixtures) if any exist outside the dynamic advisor-list logic.
- [DE 0.4.0] Verify mix_summary.json `classification_method` propagation visible in any UI debug output (if exposed). Should now read `orion_native_v1`.

### DS / 0.4.0_DS_ClientPlatform (self-queued)

- [DS / WHEN GO LANDS] **DIAGFIX.012 Phase 2:** build `pull_inflection_positions_daily.py` extending DIAGFIX.011 pattern with `(clientId, date)` iterator. ~150 min for 30-day backfill / ~5 min/day forward maintenance.
- [DS / WHEN GO LANDS] **DIAGFIX.012 Phase 3:** new silver `silver/positions_mv/snapshot_date={date}/data.parquet` builder. One row per `(account_id, ticker, date)` with `current_value` (= EndingMV), `current_shares`, `current_price`, plus optional `cost_basis` when `includeCostBasis=true`.
- [DS / WHEN GO LANDS] **DIAGFIX.012 Phase 4:** INF_B_00 refactor — replace `units × nav_price` reconstruction with direct `current_value` lookup from new silver dim. Eliminate TRN-as-price-source entirely. Likely net code reduction (similar diff shape to DIAGFIX.010 Phase 3).
- [DS / WHEN GO LANDS] **DIAGFIX.012 Phase 5:** re-run cascade + validation. Confirm position-level daily MV correct (no drift between consecutive days unless trades happened). Confirm firm-level rollup matches Orion UI total. timeseries / concentration_risk / composition all auto-correct via INF_B_00 → INF_I_D03 → INF_I_D02d cascade.
- [DS] **DIAGFIX.008 Step 2 follow-on:** INF_D_04 `timeseries_overview.mix.quarterly/monthly` integration once positions_mv silver dim lands. Multi-period mix backfill becomes trivial (per-day per-asset MV available).
- [DS] **W4.14 (queued):** B-chain holdings-lots scripts (I_A01, I_A02 fee data, I_A03 with memory mitigation, I_B01) on Orion data — separate from DIAGFIX wave; consider sequencing once positions_mv lands.
- [DS] **BDPL_CNPRCS.WP-10b (queued):** Nightly gold↔silver reconciliation harness (BD pipeline). Independent diagnostic. Lower urgency than INF chain.
- [DS] **Optional follow-on TOs surfaced this wave:**
  - `Probe E`: longer Orion historical depth test if 30d ever proves insufficient (currently no need)
  - Books-tab investigation using `/Reporting/Scope` endpoint surfaced in HAR (7) — flexible calc engine for Activity series + Performance vs benchmark + grouping by Asset Category
  - Re-run INF_B_00 to bake corrected `advisor_key` into canonical holdings (currently mitigated by Phase 5 override; INF_B_00 re-bake is optimization, not correctness fix)
  - V2 classifier upgrade — if any Orion-native classification ever proves insufficient at long-tail buckets (alternatives discrimination is keyword-based; could sharpen with explicit `productSubType` + Orion `riskCategory` / `managementStyle` joins from the assets_v2 schema)

### Watching / standby

- DS heartbeat current. Inbox watcher running. No active execution loop.
- Will fire on any new GO from COO or direct directive from Andrew.

---

*Authored by `0.4.0_DS_ClientPlatform`. Wave arc: ~3.5 hours across 4 TOs. 11 commits this session, 10+ S3 script uploads, 12+ S3 artifact publishes, 19 RAVC messages, 0 destructive ops, 0 contamination aborts, 0 hook bypasses. Andrew's commit-before-deploy invariant respected on every cycle. Brandenburg surfaces. Bond ETFs correctly classified. Path A discovered.*
