# Cross-Org TO Reconciliation Close-Out — 2026-04-13

**Author:** 2.0.0_SA_COO
**Directive:** Andrew via CTO (1.0.0_SA_CTO). Single consolidated close-out pass across open TOs on the 6 active projects (LIVE MCP agents only).
**Synthesis input:** CTO reconciliation replies from 0.4.0_DE_ClientPlatform, 0.4.0_DS_ClientPlatform, 0.6.0_AE_PartnerETL.

---

## Summary

10 TOs retired (DEPRECATED / COMPLETE-IN-FACT / SUPERSEDED). 1 genuine KEEP (already in flight). 2 RD TOs flipped provisionally (agent not LIVE — may be re-opened on next session). 2 pod-0.4 ADHC_DESIGN KEEPs queued.

**Project health after flip:**
- ADVI_REBORN — near-closure. Only W6-002 final validation remains + portal DEV→PROD.
- ADHC_DESIGN — pod 0.4 reduced to .028 + .032 (KEEP).
- ADVI_OTHDED, ADVI_HDRSPL, ADVI_INCMTL, ADHC_TMSTEL — untouched by this pass (no open-TO noise).

---

## ADVI_REBORN

### DEPRECATED (5 DE) — flipped to complete with superseded-by evidence

| TO | Evidence |
|----|----------|
| W1-005 de-endpoint-component-map | Superseded by comp-* tool suite (comp-routes/comp-transform/comp-platinum) |
| W2-003 de-fee-scorecard-window-types | Fee scorecard contract owned by ADVI_PROFIL (portal-v2.1.39 / d2e78631) |
| W3-003 de-rd-reconciliation-matrix | Reconciliation happened organically during PROFIL ship |
| W3-005 de-rd-portal-mismatch-fix | Resolved in PROFIL Wave 1/2/3 |
| W4-002 de-leaderboard-role-types | Leaderboard typing rebuilt in PROFIL AdvisorsTab |

### COMPLETE-IN-FACT (1 DE + 1 DS) — flipped to complete with commit pointer

| TO | Commit |
|----|--------|
| W5-005 de-advisors-tab-data-path | d2e78631 / portal-v2.1.39 PROD |
| W6-001 ds-d04-leaderboard-role-fee-buckets | 87557c33, S3 `platinum/firm/leaderboard.json` refreshed 2026-04-13T16:40:48Z |

### SUPERSEDED (1 AE)

| TO | Superseded by |
|----|---------------|
| W1-003 ae-s3-path-verification | ADVI_GLDRST.014 + comp-pipescript / comp-routes (never GOed) |

### DEPRECATED provisional (2 RD — 0.4.2 not LIVE at reconciliation)

| TO | Evidence |
|----|----------|
| W5-002 rd-advisors-tab-case-fix | PROFIL AdvisorsTab rewrite (d2e78631) + DE W5-005 COMPLETE-IN-FACT. Re-open if RD disagrees. |
| W5-006 rd-advisors-tab-rendering | Rendering rebuilt in PROFIL (d2e78631 PROD). Re-open if RD disagrees. |

### KEEP (1 DE)

| TO | State |
|----|-------|
| W6-002 de-advisors-tab-remove-fee-fallback | Code landed portal DEV bf475f8. 3/4 Travis audit cells match; 4th (Fee-Paying + Implementor off) = 365.55M vs expected <=341M — **flagged back to DS for revalidation**. Possible D_04 emit drift from the invariant `fee_paying.aua + no_fee.aua == role.aua`. |

### ADVI_REBORN post-state

Only W6-002 final validation remains + portal DEV→PROD deploy. Project closable after those two lands.

---

## ADHC_DESIGN — pod 0.4 only (pods 0.1/0.2/0.3 agents not LIVE)

| TO | Disposition |
|----|-------------|
| .025 de-tooltip-foundation-and-pilot | COMPLETE-IN-FACT (pilot migrated, DataTooltip canonical, COO-confirmed on DEV 2026-04-10). Flipped. |
| .028 de-tooltip-advi-cleanup-and-lint-guard | KEEP. Single Variant E site in DistributionTab.tsx:2629 + lint rule not yet added. DE picks up after W6-002 / HDRSPL. |
| .032 de-lint-cleanup-pod-0.4 | KEEP. ~200 ESLint warnings in AdvisorIntelligence/**. Parallelizable. |

### ADHC_DESIGN post-state (pod 0.4 slice)

.028 + .032 queued; other 5 pod-0.4 Phase 2 TOs already complete from prior sessions.

---

## Not assessed (agents not LIVE at reconciliation time)

- 0.4.2_RD_AdvisorIntelligence — W5-002 + W5-006 (flipped provisionally).
- 0.1.0_DE / 0.2.0_DE / 0.3.0_DE — ADHC_DESIGN Phase 2 pod work (not in scope this pass).
- 0.2.2_RD_Attribution — ADHC_DESIGN .001/.015/.024 (staged, carried forward).
- 0.2.4_RD_Valuation — ADHC_DESIGN .007 (staged, carried forward).

**Recommend second reconciliation pass when RD 0.4.2 + these RD agents next register.** CTO framed this pass as "LIVE on MCP" so the non-LIVE agents are deliberately out of scope.

---

## Flags back to CTO

- **W6-002 Travis cell 4 mismatch (365.55M vs <=341M).** DE committed bf475f8; inline metadata flags DS revalidation needed. Likely an edge case on how D_04 computes `no_fee` vs `fee_paying` when an advisor has mixed roles. CTO may want to scope a quick follow-up DS investigation TO (W6-003) or treat as an audit artifact depending on whether the invariant `fee_paying.aua + no_fee.aua == role.aua` actually holds on Travis's implementor row.

## Files touched

Task order status flips (11 files):
- `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_REBORN.W{1-005,2-003,3-003,3-005,4-002,5-005}.*.md`
- `org/tier2_senior/0.4.2_RD_AdvisorIntelligence/task_orders/ADVI_REBORN.W5-{002,006}.*.md`
- `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_REBORN.W1-003.*.md`
- `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADHC_DESIGN.025.*.md`
- (W6-001 DS was already flipped complete by DS self-attribution; no COO flip needed.)

Project JSONs:
- `org/projects/ADVI_REBORN.json` (phase + blocking rewritten).
- `org/projects/ADHC_DESIGN.json` (phase + blocking rewritten, pod 0.4 slice).

CTO will fold REGISTRY.md phase/blocking columns in the next CTO org commit.
