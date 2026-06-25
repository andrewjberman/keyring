# Deploy-completion ledger -- portal DEV->PROD promote v2.1.125

- **Opened:** 20260625T2035Z (deploy-start)
- **Owner:** 0.4.0_DT_ClientPlatform
- **Trigger:** Andrew-direct /prod-deploy
- **Target tag:** portal-v2.1.125
- **Bundle (FULL = 7 DE commits ahead of origin/PROD; promote ships all of DEV, not just the 3 DE flagged):**
  - 757f4d99 -- CVO-4a: DistributionTab getAdvisorNnaCanonical gated on adv-cohort (COT 404 kill)
  - c529f0e6 -- Andrew-direct: remove 'Estimated History' graphic (ModelPortfolios AUA/AUM Trend)
  - 7d71fbe0 -- COT go-live P0: ROUTER_FIRM_SUFFIX cottonwood->cot (advisor-intelligence.ts)
  - c02809b6 -- ADVI_NNAATTR.TO-2 AC4: INFMVP.F5 override retained load-bearing
  - a647e8dd -- ADVI_NNAATTR carry-forward: fix ClientsTab getHeaderMetrics dead path
  - b24cd040 -- ADVI_NNAATTR.TO-2 AC4: grep-document INFMVP.F5 adv-donut override (comment-only)
  - 6e95f05c -- ADVI_NNAATTR.TO-2 F-1b/c/F-3: AdvisorPublicProfile exec-flows canonical fee-split
  - All 7 authored 0.4.0_DE_ClientPlatform; FE-only; no infra/served-output; no cross-firm widen.
  - Merge commit: 206f4a60 (--no-ff, base 90054baa, rollback 90054baa). Parity gate (diff origin/DEV HEAD) EMPTY.
- **Pre-gates:** DEV tree clean; DEV==origin/DEV; tsc typecheck exit 0; comp-transform schema-check DistributionTab clean.
- **Freeze:** declared to 2.0.0_SA_COO 20260625T2035Z (hold DEV pushes).

## Steps
- [x] Step 3 re-assert local PROD from origin (90054baa)
- [x] Step 4 ephemeral worktree merge --no-ff (206f4a60) + push origin PROD (90054baa..206f4a60, VALGATE+tsc PASS)
- [x] Step 5 CI run 28199040447 conclusion: SUCCESS; tag portal-v2.1.125 peeled=206f4a60=PROD head (verified)
- [x] Step 6 workspace pointer bump d725f7f3->757f4d99 on CLOUD (6bf5947fe, pushed)
- [x] Step 7 teardown: worktree prune clean (list shows only main DEV tree); physical .runtmp dir persists (Windows Filename-too-long, gitignored/inert -- acceptable); main tree on DEV; at workspace root
- [x] Step 8 RAVC to COO + freeze release (this entry + COO message)

- **Closed:** 20260625T2042Z -- LANDED. PROD=206f4a60, tag portal-v2.1.125, CI 28199040447 SUCCESS, pointer 6bf5947fe. All legs complete, no strand.
