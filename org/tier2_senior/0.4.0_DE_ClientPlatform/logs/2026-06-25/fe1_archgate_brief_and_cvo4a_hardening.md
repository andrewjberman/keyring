# FE1 — CTO arch-gate brief + CVO-4a 404 hardening (lane close)

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, IMPLEMENT
**Serial:** 0.4.0_DE_ClientPlatform | **Date:** 2026-06-25 | **Window:** 1537Z -> 1542Z

## Summary
FE1 = CVO-CERT-PASS (fully done). On COO authorization, authored the CTO arch-gate brief folding the unified
portal contract into the Schwab-raw-native rebuild; then shipped the CVO-surfaced 4a FE-hardening (COT 404 gate).

## Current State
- **FE1 = CVO-CERT-PASS** (COO msg 153854Z): completeness + per-partner correctness verified; both gaps ruled INTENDED-ABSENT/AGNOSTIC (do NOT build COT D_00f or 49F/COT fresh-equiv for the rebuild). FE1 fully DONE (delivered 98764fb65 + COO-RAVC2 + CVO-cert).
- **CTO arch-gate brief v1.0** `docs/briefs/DATA_ANALYTICS_canonize_gold_archgate_brief_v1.0.md` @ committed. G1-G3 arch-gate decisions (D-tier-as-waist; bronze=Schwab-raw / silver=purpose-built / gold=incremental; excise set = B_01 FIFO + B_00 reconcile + patches; keep set = the analytics; 49F-first sequencing). N1 fees = known fee-feed dep; **N2 household-grouping = SOVEREIGN, PENDING ANDREW** (COO surfacing; brief NOT blocked). §6 ends at "contract LOCKS -> COO decomposes build-TOs."
- **CVO-4a hardening SHIPPED** portal DEV `757f4d99`: `DistributionTab.tsx:925-931` getAdvisorNnaCanonical `enabled` gated on `layout.tabs.distribution.cohorts.adv !== 'disabled'` -> COT/geo-only partners no longer fire the avoidable live 404 (advisor_nna_canonical is an advisor-dim artifact; COT has no D_00f producer). Non-fatal before (RQ error->undefined->unused); now no network 404. Verified: `tsc --noEmit` exit 0, `comp-transform schema-check DistributionTab` clean (no MISSING). DT (0.4.0_DT) requested to QA-gate + push origin/DEV. Portal returned to base (DEV, root cwd).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-transform schema-check` | DistributionTab | PASS | clean, no MISSING — DE mandate for the touched component (query-enablement change, not a data-prop change) |
| `bun run tsc --noEmit` | portal | PASS (exit 0) | no DistributionTab / no new TS errors |

**What worked:** schema-check + tsc gave a fast pre-commit confidence gate on the 1-line enablement fix; `useTenantLayout(firmId).tabs.distribution.cohorts.adv` was already in-scope in the component, so the gate is a clean COT-only behavior change (49F/INF adv-enabled keep firing). **What failed:** none. **Gap:** none new.

## Blockers
None. All remainders event-gated: DS co-sign (unified contract); CTO arch-gate (brief queued); Andrew N2 household-source (sovereign); DT push of 757f4d99.

## Next Steps
- **[0.4.0_DT_ClientPlatform]** QA-gate + push portal DEV 757f4d99 (non-urgent, non-fatal).
- **[1.0.0_SA_CTO]** arch-gate the brief (G1-G3 + N1 fee-feed scope).
- **[0.4.0_DS_ClientPlatform]** co-sign unified portal contract v1.0.
- **[Andrew]** N2 household-grouping source ruling.
- **[2.0.0_SA_COO]** on contract-lock, decompose the rebuild build-TO set; I'm available to support that decomposition (FE-side field list per build-TO).
- **[0.4.0_DE]** event-driven; amend contract->v1.1 on DS co-sign corrections; P2-1 close-verify still gated on P2-2 materialize.
