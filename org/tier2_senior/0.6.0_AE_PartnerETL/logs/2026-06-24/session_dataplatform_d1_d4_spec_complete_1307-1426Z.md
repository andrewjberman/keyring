# 0.6.0_AE_PartnerETL -- 06-24 DATA_PLATFORM D1 + D4 BOTH SPEC-COMPLETE (Schwab field-spec + SmartX sweep) + SS4c pair-verify
**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT (2 audit specs), COORDINATE (DS/CVO/CTO/COO/base-AE RAVC loops), VALIDATE (SS4c pair-verify), DIAGNOSE (SS4c metric-IAM finding + live SmartX probing)

## Window
06-24 ~1307Z-1426Z. Session start -> /watcher + org/XXX.md startup -> MSTR orient (2nd AE lane for DATA_PLATFORM D1/D4) -> COO GO -> drove BOTH assigned TOs (D1 Schwab field-spec + D4 SmartX sweep) to spec-complete in-session, + the standing SS4c 06-24 pair-verify.

## What landed
**D1 Schwab field spec -- SPEC-COMPLETE** (docs/briefs/DATA_PLATFORM_D1_SCHWAB_FIELD_SPEC.md; commits 41d2744e2 draft -> 7fda2ea32 v0.2; TOs re-homed 0.7.0->0.6.0).
- Full SI2 17-extension catalog (6 captured ACC/RPS/TRN/ULN/ULT/RLD, 11 un-captured) grounded vs LIVE raw + raw H1/H2 headers (not the Nov-2025 dict). 6-converter capture maps + drops + grain + join model + ingest-automation scoping (manual SI2-desktop deficiency -> options A/B/C + multi-firm prereqs).
- Findings: TCF=CONFIRM trade-confirm NOT tax/cash-flow (dict drift, raw-header-corrected); trn_nna = the ONE real recurring-skill orphan (Layer-B never run -> trn_nna/ live-absent -> C_01.canonical_nna silently zero Schwab flow; CVO P2-dormant served-confirmed source_system=bd/0 schwab_imputed); ULN Rule-17 shorts-filter violation (uln_to_silver:209) -> DS canonical ruling (lots_to_silver); TRN Layer-A reads LOCAL OneDrive = the server-side automation-blocker; opal-data-schwab/silver = dead vestige (canonical=opal-data-bd/schwab/silver).
- DS field-modeling consult (gold-consumers + join + §13 field-grain verify-pass, e2b3f4227/fa88a725c) -> AC1/AC2 DS-VERIFIED. CVO reconcile-to-live = PASS (AC4). Completeness-basis (b) observed-delivered-to-49F. ULT-not-orphan corrected per CVO.

**D4 SmartX endpoint+structure sweep -- SPEC-COMPLETE + CTO-ACCEPTED** (docs/briefs/DATA_PLATFORM_D4_SMARTX_ENDPOINT_SWEEP.md; a07590cb2 draft -> 6d7d30ba0 v0.2; CTO canonicalizing briefs->architecture).
- Full 5-surface map (REST api/3.1 core, performance svc, GraphQL=compliance-flags-only, legacy-3.0-drop, portal-internal) + the partnership-slot map + build-vs-buy/LEVERAGE boundary + named dependency tradeoff.
- COO/Andrew RIGOR-UPGRADE (reframe "all endpoints" -> stated completeness-basis): spec-hunt LIVE 06-24 = NO vendor API spec (swagger/openapi/api-docs all 404; only OIDC discovery); fresh api/3.1 exhaustion sweep 06-24 (<=17/min, live parked JWT) = 14 known re-confirmed 200 + 22+ candidates incl. ALL attribution/risk/per-segment/trade-rebalance screens -> all confirmed-absent 404. Per-surface basis taxonomy (CVO: GraphQL=(a) provably-complete; REST=(b) best-effort-bounded).
- NET-NEW from the live probing: model roster 11 (HAR had 7); **api/3.2 + api/4.0 EXIST (401 -- 3.1-scoped JWT rejected, newer-version surface UNMAPPED)**; the model/trade plane is NOT on api/3.1 (all 404, trade-subdomains no-DNS). CVO reconcile = PASS + basis-verified; CTO ACCEPTED.

**SS4c 06-24 weekly pair-verify (standing item, COO-directed) -- DELTA=0 CLEAN + 1 grounded finding.**
- First weekly run (05:23Z) scorecard gold/_parity/load_flows/ss4c/2026-06-24/scorecard.json: max_abs_diff=0.0, exact_match_rate=100%, key_sym=0, row_delta=0, oracle 79326==incremental 79326, targets_met=true, clean_night_counter=1. Cutover VERIFIED clean (genuine DELTA, not by-construction). CVO/DS concurred.
- FINDING (IAM+code grounded): WeeklyScorecardClean CW metric NOT publishing -- gldinc_ss4c_weekly.py emits it (line 120) but the gold-runner role bd-exporter-ec2-role LACKS cloudwatch:PutMetricData (live-IAM-checked: 10 inline + 2 managed, none grant it; the canary publishes via a different Lambda role) -> _emit denied, main() swallows + returns 2 -> weekly divergence/absence alarms blind (compounds the known egress-inert SNS). COO-APPROVED fast-follow (post-D1/D4, before 07-01): ns-conditioned cw:PutMetricData TF grant + _emit-non-fatal hardening.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-to DATA_PLATFORM.D1 / .D4 | per-session TO context (race-free) | OK |
| comp-freshness artifact (SS4c parity prefix; schwab/silver/rps) | SS4c run-fired check + ingest currency | PASS (parity 7.8h) / WARN (rps 46.9h manual cadence) |
| aws s3 inventory (raw 17-ext enum; silver-path compare) -- `# rail-checked` override | D1 capture-vs-available + bucket-lineage; comp-freshness can't enumerate extensions/compare prefixes | resolved 17-ext + empty-canonical-RPS vestige |
| aws iam (gold-runner role cw:PutMetricData) -- `# rail-checked` | SS4c metric-emission mechanism (EC2-role, comp-iam is lambda-oriented) | grounded the IAM gap |

What worked: comp-freshness PASS/WARN grounded both the SS4c run-fired check + ingest currency cheaply; the comp-rail correctly gated my aws s3 ls (I used the `# rail-checked:` override where no comp-tool fits structural extension-enumeration / prefix-compare). What failed: nothing tool-side. Gap: comp-freshness can't enumerate distinct raw feed-extensions nor compare two prefixes' population (the rail-checked S3 inventory was the right call); comp-iam is lambda-oriented (no EC2-instance-role cw-grant reconcile) -- the gold-runner IAM check went raw-aws-rail-checked. (D4's SmartX work is live external-API probing -- curl, not comp-tools.)

## MCP traffic
~45 messages this window (heavy COORDINATE). Significant: MSTR orient (2nd AE lane) -> ACK+ground-truth-correction (SS4c already shipped, NOT a deadline -- COO accepted, retracted the stale flag). COO GO D1/D4 + the rigor-upgrade (reverse ref-date -> spec-hunt+fresh-sweep) + the 3-message SmartX framing churn settling to LEVERAGE-not-supplant. DS consult delivered + §13 field-grain verify + ULN ruling + cutover concur. CVO reconciles: D4 PASS + completeness-basis addendum; D1 AC4 PASS; trn_nna/ULT verdict. CTO D4 ACCEPTED + canonicalizing. RAVC2: D4 (COO+CTO), D1 (COO+CTO). base-AE crawl-split CONFIRMED (DC0 harness / DC-LEV mine).

## Blockers
None. DC-LEV comprehensive-crawl is GATED (not blocked) on COO's formal DC0 harness TO (base-AE builds DC0; Orion-vendor-1 then SmartX-vendor-2 per CTO sequencing). 2 fast-follows approved + queued (not blocked).

## Current State (zero-prior-context handoff)
- **D1 + D4 BOTH spec-complete.** D1 = docs/briefs/DATA_PLATFORM_D1_SCHWAB_FIELD_SPEC.md @7fda2ea32 (DS-verified §13 + CVO AC4 PASS). D4 = docs/briefs/DATA_PLATFORM_D4_SMARTX_ENDPOINT_SWEEP.md @6d7d30ba0 (CVO PASS + CTO-ACCEPTED, CTO canonicalizing to docs/architecture). Both TOs re-homed to org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ (status active).
- **SS4c:** cutover verified clean (DELTA=0). WeeklyScorecardClean metric blind on TWO counts -- bd-exporter-ec2-role missing cw:PutMetricData (my fast-follow TF fix) + the egress-inert opal-critical-surface-alerts SNS (Andrew-gated, track alongside). Non-urgent (next weekly 07-01).
- **DC-LEV (downstream, mine):** SmartX = LEVERAGE-track (long-term partner, NOT supplant). Built on base-AE's DC0 crawl-harness (scoped docs/briefs/comprehensive-crawl-harness-scope-20260624.md 8bcc64522; CTO-arch settled; gated on COO's TO). My open SmartX gaps the crawl resolves: api/3.2+4.0 scope, the model/trade plane location. Catalog schema agreed (+ data_plane tag, GraphQL ops, consumption_status).

## Next Steps
1. [0.6.0_AE_PartnerETL] Stage the vendor-2 SmartX adapter-input brief for base-AE's DC0 crawl (data-bearing screen-list + auth path + api-version surface) -- while gated on COO's harness TO.
2. [0.6.0_AE_PartnerETL] Fast-follow (post-spec, COO-approved): ULN cutover step-2 -- repoint /49-schwab-conv Step-5 -> `convert_schwab_lots_to_silver.py uln` (uln-ONLY) + retire convert_schwab_uln_to_silver.py + add the trn_nna Layer-B step (convert_schwab_trn_to_nna_silver.py) + fix the SKILL.md "(NNA enrichment)" comment. DS step-1 (lots_to_silver widen, 0571c6dcc) done; DS co-verifies B_02 + canonical_nna source_system flip on next nightly.
3. [0.6.0_AE_PartnerETL] Fast-follow: SS4c IAM -- add ns-conditioned cloudwatch:PutMetricData (GLDINC/SS4c) to bd-exporter-ec2-role via BD-pipeline TF (mirror the canary role) + _emit-non-fatal hardening; deploy-completion ledger entry; before 07-01.
4. [2.0.0_SA_COO] formal DC0 harness TO (base-AE) -> unblocks the SmartX crawl (Orion-first).
5. [1.0.0_SA_CTO] D4 canonicalization briefs->docs/architecture (in progress).
6. [0.6.0_AE_PartnerETL] DC-LEV capability-leverage map -- built off base-AE's per-vendor endpoint catalog once the SmartX crawl runs.
</content>
