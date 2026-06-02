<task_order>
<metadata>
  <to_id>ADVI_INFPRM.PROMOTE</to_id>
  <project>ADVI_INFPRM (bundle: + ADVI_INFOTD + ADVI_INFNNA)</project>
  <title>DT: portal DEV->PROD promote of the stacked Inflection FE (c009f98c) — tree cleanup + DEV push + PROD deploy. Andrew-direct GO.</title>
  <assigned_to>0.4.0_DT_ClientPlatform</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-02</issued_date>
  <status>PRE-STAGED — ready-to-consume on spawn. Andrew GO ("yep this works" + "tree cleaned up, dev pushed, prod deployed"). DT requested from MSTR. Execute on spawn after CTO hands the 5-phase plan.</status>
  <dispatch_held>false</dispatch_held>
  <priority>HIGH — Andrew-direct, live critical path. The full Inflection surface is CVO-cleared + Andrew-pixel-green.</priority>
  <references>
    <ref type="andrew">2026-06-02 verbatim: "yep this works, ask MSTR for 0.4.0_DT and get the tree cleaned up, dev pushed, prod deployed"</ref>
    <ref type="dev-head">portal DEV c009f98c (ci-green; RD~C pre-stage warm; rollback a33c230f)</ref>
    <ref type="rule">CLAUDE.md Rule 19 (portal main worktree stays DEV; promote in ephemeral worktree + cleanup) + Rule 18 (safe-apply/HALTGT if any terraform) + the EC2/portal deploy standards</ref>
    <ref type="process">portal-promote.sh + the canonical 5-phase portal DEV->PROD deploy (CTO hands the staged plan)</ref>
  </references>
</metadata>

<scope>
Andrew GREEN on the full Inflection surface (Peter admin + Joe non-admin login/Profile/Distribution all render on fresh logins). Promote the stacked FE to PROD.

BUNDLE (all on DEV head c009f98c, all CVO-cleared; backend/data ALREADY live — partners-api-v1.16.2 PROD, opal-partner-inflection provisioning live, canonical NNA served):
- ADVI_INFPRM: W1 + W2-FE + W4b + W4c + W4f + P2a/P2b (admin/non-admin access model, Segment firmId-resolution, tab-gating).
- ADVI_INFOTD: W1 + W2-FE (Model Portfolios AUM relabel + account_count).
- ADVI_INFNNA: W2-FE (canonical GEO/ADV NNA repoint).
- + MDPF S5 + NNA tooltip (already on DEV).

## Steps:
1. TREE CLEANUP (Rule 19): confirm the portal main worktree is on DEV (`cd portal && git branch --show-current` = DEV; if stranded on PROD, `git checkout DEV` first). Clean any stranded/ephemeral `.runtmp/portal-*` worktrees. Confirm DEV head = c009f98c (ci-green) + working tree clean.
2. PUSH DEV: push the portal DEV branch to origin (--follow-tags if tags).
3. PROMOTE DEV->PROD: run the canonical 5-phase portal promote (CTO hands the staged plan) — ephemeral `git worktree add` for PROD, merge/promote DEV->PROD, deploy (build + S3 + CloudFront invalidation per the portal deploy process), clean up the temp worktree on exit. Main tree returns to DEV.
4. VERIFY: PROD serves the new FE; spot-check the deploy completed (CloudFront invalidation done, build artifacts live).

## NOT in this promote (fast-follow):
- The cross-advisor Distribution edge-untier (Andrew no-tiering ruling) is a SEPARATE Lambda@Edge .004a change (AE, on CTO's artifact-tier spec) — lands independently. Until then PROD non-admins still hit the cross-advisor 403 (known fast-follow gap).
</scope>

<acceptance>
- [ ] Portal main worktree on DEV (Rule 19); DEV head c009f98c pushed to origin; no stranded ephemeral worktrees.
- [ ] PROD deployed (5-phase complete, CloudFront invalidated); PROD serves the stacked FE.
- [ ] Post-deploy smoke (DT or hand to CVO/Andrew): Peter admin + Joe non-admin render correctly on PROD (fresh logins).
- RAVC2 to CTO+COO+CVO with the deploy evidence (commit/tag, CloudFront invalidation id, PROD verify). CVO e2e-verifies post-promote on served PROD.
- Coordinate with CTO (owns the 5-phase plan + promote sequencing) before executing. RD~C pre-stage feeds it; RD~C does NOT execute (Andrew wants DT).
</acceptance>

<notes>
Authored by COO ready-to-consume on DT spawn (Andrew-direct, MSTR spawn requested 212911Z). DT is the portal-deploy owner per Rule 19. The edge-untier fast-follow is tracked separately (AE/CTO). CC CTO+CVO+RD~C+AE.
</notes>
</task_order>
