# ADVI_NNAATTR.TO-1 — unify per-advisor NNA to ONE all-roles canonical source + buckets-preserved

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Current State

FRESH 0.4.0_DS_ClientPlatform spawn, standing DS lane. Picked up ADVI_NNAATTR.TO-1 on COO's
exact-serial GO (190431Z). Implemented + deployed F-0/F-1a/F-2/F-4/F-5 — the fix for the silent
route-dependent per-advisor NNA divergence (Travis architect $4.14M via D_00f vs $6.95M via D_00c).

**Commit 0bca5a46a** -> origin/CLOUD; all 6 gold files **MATCH on s3://opal-data-bd/code/gold/**
(md5 byte-verified S3-vs-local); deploy-completion ledger **CLOSED**
(`20260617T1952Z_advi_nnaattr_to1_allroles_nna`). CVO design-reviewed + CONCUR'd the architecture
(191916Z) incl. the 49F-House-excluded-from-Layer-2 refinement.

**Status = CODE-COMPLETE + DEPLOYED, NOT yet served-verified.** AC1–AC4 verify on the SERVED
`platinum/firm/advisor_nna_canonical.json`, which I will NOT produce via an ad-hoc gold run
(validate-on-nightly compute-discipline). Verification = the SCHEDULED NIGHTLY artifact, reviewed
NEXT MORNING (event-driven). AC5 (D_02 logging) is done.

## Architecture (CVO-blessed option A)

- **NEW `lib/advisor_nna_attribution.py`** — ONE shared all-roles attribution melt imported by BOTH
  D_00f + D_00c → cross-route identity (AC1) **by construction**. Per-advisor = ALL ROLES, counted
  once per account, NON-additive. 49F House + Unassigned = own `is_bucket` rows; individuals exclude.
- **C_07** — ADDITIVE `architect_no_infer` column: Layer-1+2 (49F House EXCLUDED from Layer-2 resolve,
  preserved literally), Layer-3 impl-pairing OFF. Legacy `architect` (resolved) unchanged for the 14
  other account_team consumers (zero blast). Also added the missing `from __future__ import annotations`.
- **D_00f** — advisors block architect-only → all-roles+buckets via the shared melt; REMOVED the
  `advisors_sum==firm` reconciliation assertion (NON-additive per NFRA_GCONTR NNA value-limb inv-4);
  firm+geo stay account-once additive (geo partition is the firm-additive proof). MAX → 2021-01-01.
- **D_00c** — REMOVED the rel_advisors→primary_architect Layer-3 override block (removed, not bypassed —
  AC2); architect role sourced from `architect_no_infer`; bucket rows excluded from individual
  employees; per-day gate dropped for the SNAPSHOT tenure rule (one rule both routes). MAX → 2021-01-01.
- **D_00 (F-4)** — `build_clients_tab` headline now emits additive-account-once NNA (mtd/qtd/ytd/12m)
  so `dashboard.json` (D_04 copies the headline) serves real firm NNA, retiring the FE zeroing
  fallback's data side; header_metrics NNA documented as the additive basis.
- **D_02 (F-5)** — `_nna_since` logs once per advisor when the C_03 cum-diff fallback fires.

## Files Modified

| File | Change |
|------|--------|
| data/black_diamond/scripts/gold/lib/advisor_nna_attribution.py | NEW — shared all-roles attribution melt + buckets (F-0/F-1a) |
| data/black_diamond/scripts/gold/C_07.advisor_attribution.py | ADDITIVE architect_no_infer col (Layer-3 off, 49F House preserved); + future-import |
| data/black_diamond/scripts/gold/D_00f.advisor_nna_canonical.py | advisors block → all-roles+buckets; removed Σ(advisors)==firm assert; MAX=2021-01-01 (F-0/F-1a/F-2) |
| data/black_diamond/scripts/gold/D_00c.portal_leaderboard.py | removed Layer-3 override; architect_no_infer; buckets excluded; snapshot rule; MAX=2021-01-01 (F-0/F-1a/F-2) |
| data/black_diamond/scripts/gold/D_00.portal_aggregates.py | clients_tab headline additive-account-once NNA → dashboard.json (F-4) |
| data/black_diamond/scripts/gold/D_02.advisor_client_detail.py | C_03 cum-diff fallback now logs per advisor (F-5) |
| org/critical_paths/change_management/20260617T1952Z_advi_nnaattr_to1_allroles_nna_deploy_completion.md | deploy-completion ledger (opened+closed) |

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| comp-which | "which gold script emits advisor_nna_canonical" | no tool matched (router); resolved via grep + filename map |
| comp-pipescript io (D_00f, C_07, D_00, D_00c, D_02) | column gaps + portal consumers before/after edit | account_team consumers mapped (14 readers); additive col = no break; no new column gaps |
| comp-blast account_team | blast radius of touching C_07 output | 15 gold + 7 Lambda + 63 S3 consumers → confirmed ADDITIVE column = zero blast; chose A over a C_07 architect rewrite |
| comp-pipescript deployed + md5 byte-verify | post-push S3 MATCH confirmation | all 6 files MATCH (byte-equal S3-vs-local) |
| ds-commit-gate.sh (all 6) | py_compile + AST + ruff FA before commit | my changes PASS; C_07 carries 6 PRE-EXISTING ruff E/F violations (not mine) → Rule A bypass + cleanup TO recommended to CTO |
| deploy_ledger.py | open/close deploy-completion ledger | 3 legs proven; CLOSED in-session (L3 verify deferred-by-design to scheduled nightly) |

## Blockers

None assumption-blocked. AC1–AC4 served verification is PENDING the scheduled nightly (event-driven
next-morning review — per validate-on-nightly + no-overnight-watcher). cot ADVI_COTETL.CHAINFIX
remains PARKED (BD-source-gated; COO has not GO'd it).

## Next Steps

1. **[self, next-morning, event-driven]** Review the SERVED advisor_nna_canonical.json + leaderboard.json
   post the scheduled nightly: prove cross-route byte-equality (Travis + 2 advisors, all-roles, per
   window), 49F House ~$357.6M MAX preserved, Unassigned bounded-transient, nna==inflows-outflows,
   MAX=2021-01-01. Report to COO (CC CTO+CVO) to close TO-1; CVO owns the close-gate re-verify.
2. **[self → COO]** Author TO-2 (DE/RD leg: F-1b/F-1c repoint + drop ADVI_INFMVP.F5 architect override +
   nna==inflows-outflows on the card; F-3 Inflection fee-split; F-4 FE zeroing-fallback removal in
   advisor-intelligence.ts) — stage after the nightly confirms the all-roles number on the served artifact.
3. **[1.0.0_SA_CTO]** Rule-A call on the C_07 per-class ruff cleanup TO (F401 sys / 4× E701 / E712).
4. **[2.0.0_SA_COO]** cot ADVI_COTETL.CHAINFIX — I execute on your GO once the BD-source call clears.
