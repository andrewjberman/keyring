# DSGN_RBNDV2 -- ROUND-6 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~17:3xZ)

**On:** the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v7.md` @e18c44c360 (MAY-CLOSE). **Branch:**
`feature/dsgn-rbndv2-light`, unpushed.

## 1. What round 6 moved

- **The Trending Topics rows are unboxed again** (RB6Y1-AC3 MET). This cures round 5's regression, C-S18.
- **Footer sources are in proper case,** for example "Source: Global News." (RB6Y2-AC3 MET).
- **The typecheck is real now:** `tsc -p tsconfig.app.json --noEmit` reads rc=0 at 3509eae8. The earlier rc=0 lines came from an
  empty check, as the issuer corrected and the CVO confirmed.

## 2. Ruling on W19-S2 -- C-BRANCH and `portal/CONTRIBUTING-BOXES.md` both hold, at different moments

- **While building, C-BRANCH governs:** all of this project's work lives on `feature/dsgn-rbndv2-light`, on this laptop, unpushed.
  Andrew's words were "stays on a feature tree on this box and is only pushed when i say so" and "all stays on one specific
  feature branch".
- **At the merge forward, `CONTRIBUTING-BOXES.md` governs:** on Andrew's push word, the candidate
  `cand/laptop/dsgn-rbndv2-light` is cut from the last PROD and carries the feature branch's commits. That candidate is what
  `portal-merge-forward.sh` and the approval row see. The feature branch itself is never pushed as DEV or PROD.
- **Neither text changes,** so nothing re-opens for sign-off. The page is client-facing, so the push and the approval are both
  Andrew's.
- **The risk is in the replay:** whether the feature branch's commits apply cleanly onto the last PROD. That is measured now, ahead
  of his word (round 7, item 1).

## 3. Open (Andrew's)

- `002b`: where the tooltips go.
- FWD-4: the heat maps.
- His comments on the pages after Market Overview, for the FWD-5 walk.

## 4. ENRICHMENT LIST for round 7 (one issuance; C-BRANCH binds)

1. **A LOCAL candidate rehearsal:** cut `cand/laptop/dsgn-rbndv2-light` locally from the last PROD with the feature branch's commits,
   then run the real typecheck and one Market Overview walk on it.
   - Nothing is pushed.
   - Print every conflict and how it was resolved.
   - Delete the local candidate afterwards, or keep it for Andrew's word. It is not pushed either way.
2. **Andrew's next page's comments and `002b`'s answer, when he gives them.** Nothing else is cut.
