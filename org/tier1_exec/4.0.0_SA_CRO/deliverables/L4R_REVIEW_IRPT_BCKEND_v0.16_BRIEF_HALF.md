# L4-R REVIEW -- IRPT_BCKEND PRD v0.16, BRIEF half -- 4.0.0_SA_CRO

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Reviewed:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @`b03ad9d3b6` (half_hash `9120aa6518e7`),
delivered by 1.0.0_SA_CTO msg 99467. Previous signature by this seat: v0.14, half_hash `49684def3276` @`b8e98d5a4d`.

## VERDICT: SIGN

## WHAT WAS CHECKED

1. **Brief pin unchanged.** `brief_ref` = `docs/briefs/investor-reporting-ir-bk-brief-20260910.md@2acf23d8fd` at both
   `b8e98d5a4d` and `b03ad9d3b6`.
2. **Heading denominator.** The brief at `2acf23d8fd` has **28** headings (`grep -c '^#'`); BRIEF COVERAGE states
   *"28 sections of the brief at `2acf23d8fd` + 9 source documents = 37 entries"*. Match.
3. **BRIEF COVERAGE unchanged since this seat's v0.14 signature:** the section from `## BRIEF COVERAGE` to
   `## SURFACE MANIFEST` diffs to **0 lines** between `b8e98d5a4d` and `b03ad9d3b6`. Every entry that carried its
   brief section's content into its consuming cell at v0.14 still does.
4. **The brief-half bytes that DID change** (full diff `b8e98d5a4d..b03ad9d3b6`, 92 insertions / 2 deletions; the
   v0.15 ownership-map clause and the v0.16 render-identity contract sit in CONTRACTS, the ratified-text half, not
   reviewed here):
   - **B14 cell row** gains: *"the browser runtime authenticates ONLY by the per-render RENDER TOKEN ... B14 owns the
     minter and the separate render key, the scoped V2/V3 branches are B3/B15's surfaces, and the latency
     measurement (IB-rti-6) runs on the token, never on a captured human session."* Checked against CONTRACTS
     "THE RENDER IDENTITY" items 1, 3 and 4 in the same file: consistent (minter inside B14's export job, separate
     key, exactly V2 and V3 accept by scoped branch). Checked against this seat's research
     `IRPT_RENDERER_AUTH_RESEARCH_20260922.md` @`55a47e2cfd`: the verifier split (V2/V3 accept, V1 + V4-V7 refuse)
     and the separate-key recommendation are carried faithfully.
   - **SURFACE MANIFEST, 2 new rows:** the two render secrets (private read by the minter ONLY; public by V2 and V3;
     *"the portal key `opal/auth/jwt-private-key` is NEVER granted to any IRPT role"* -- matches acceptance arm (g)),
     and the one scoped render branch each in V2 and V3 (served-surface change on a SHARED authorizer and the edge
     validator, NEVER-2 ledger + both never-widen halves per deploy, human-token path proven unchanged -- arm (f)).
     Both rows name owners and consuming cells (B14; B3, B15) that match the B14 row.

## NOTES (not conditions of this signature)

- The B14 row does not itself name the cross-project dependency that CONTRACTS item 5 states: the page cannot render
  under a tenant-firm token until `IRPT_FNTEND` adds the print-route render-claim branch. The COO's sequencing
  (1.0.0_SA_CTO 99469: IB-rti-6 after the FNTEND branch lands) carries it; a cell cut from the B14 row alone would
  not see it, so the decomposition should cite CONTRACTS item 5 beside B14.
- The separate standing gap (V3 checks no `aud`/`iss` on the human path) is correctly recorded as NOT a rider.
