# NFRA_SCHWABBF -- Alongside Schwab Box build (order TO-AL-r1): never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO` (laptop), 2026-10-20 ~17:2xZ, on `2.0.0_SA_COO~SA`'s ask (msg 109955).
**COO half (its pair):** `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/2.0.0_SA_COO~SA/NEVER_WIDEN_HALF_COO_NFRA_SCHWABBF_ALONGSIDE_BOX_BUILD_20261020.md` @d95613759f.
It is filed here because the owned-paths gate refuses this seat a write in the COO's folder.

## CTO half -- SIGNED

Signed on pin `7ce88d5bdd9`. It covers the COO half's blast radius (section 1), both branches (section 3), the rollback (section 4) and conditions 1-5.

**Read at signing:**
- The plan file `PLAN_READONLY_20261020_pin7ce88d5bdd9_MERGED.txt` reads `Plan: 1 to import, 17 to add, 0 to change, 0 to destroy.` It has no `updated`, `destroyed` or `replaced` line, and 18 resources are created or imported.
- Every resource name carries the `alongside` scope: `schwab-alongside-si2-box-runner`, `-role`, `-profile`, `-policy`, `-sg` and `-events-role`, plus `schwab-alongside-send-daily-pull-policy`.
- The pin resolves to a commit.
- The 49F Schwab Box `i-0f3d57a97f14727af` is `t3.large` and running, and this act does not touch it. The new box's `t3.large` matches it, which makes it the exact copy Andrew asked for.

**Added condition 6:**
- No EventBridge rule is enabled, and no pull runs beyond the single first-day trace, until the box role's bronze, silver, meta and `_ops` statements match PRD v0.9 C-TIERS.
- C-TIERS means firm scope `schwab/cottonwood/<tier>/`, fenced per master by file name, so no Cottonwood object is ever written at master scope.
- This act enables nothing, so the condition binds the later enable act, not this one.

**Andrew's acts that follow:** the RDP sign-in sitting, and any later delete under the COO half's section 4.

-- 1.0.0_SA_CTO (laptop)
