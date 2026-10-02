# CTO product-file review -- portal 5a42f2df (branch cro-rv-mp-explain): Model Portfolios category cards explain on hover

**Reviewer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~19:0xZ. **Ask:** `4.0.0_SA_CRO~RV` msg 28670.
**Authority:** Andrew-direct ~17:0xZ (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261002_17xxZ_RIVALFUNDS_LAYOUT_WALK_AND_BUILD.md`):
"same action in Model Portfolios portal page for the Models/SMAs/Client cards".
**Candidate:** ac766035 + 5a42f2df, a fast-forward over remote DEV ec65c5d637. It changes 2 files, +41 / -4.

## Diff read in full

- **`CategoryViewTree.tsx`:**
  - a new `ExplainOnHoverContext`, default `false`;
  - a prop `explainOnHover = false`, provided at the tree root;
  - a tile explains ONLY when the context is true AND its name has an `L0_COPY` entry, so every other tile renders exactly as
    before (the `flex-1` class and the wrapper both sit behind `explain`);
  - the explanation ("What it is", "How it is counted") rides the portal's one `Tooltip` (`side="bottom"`, `delay=150`,
    `triggerClassName`, `className`). All four props exist on `TooltipProps` at 5a42f2df (Tooltip.tsx:13-29). The tooltip is
    portal-rendered, so the graphic card's overflow cannot clip it, which is the fix in 5a42f2df.
- **`ModelPortfolios.tsx`:** the one caller that passes `explainOnHover`. Investor Reporting's call sites pass nothing, so they read
  `false` and stay byte-identical in behaviour.
- **Keyboard reach:** the tile's existing focus handlers and the click-to-breakdown dialog carry the same text.
- No non-ASCII, no device path, no new dependency.

## Evidence accepted

- `tsc -b` rc=0, beside a planted type mutant at rc=2 (CRO~RV).
- A /ui-walk hover on 5174 shows the tip with no occlusion. This is development evidence, not acceptance.
- **Five IR guard tests fail on DEV ec65c5d637 BEFORE this candidate.** They are pinned to 72fe8393 / 8242412d, and Model
  Portfolios changed in 370d2fe8. This candidate does not touch the files they guard, so it does not cause them. It is a standing
  DEV defect in the IR lane and is named here so it is not lost. It does not block this candidate.

## Verdict

**APPROVED.** It lands by the standing route: merged onto the CURRENT remote DEV head at push time, by `0.0.0_AB_MSTR~Z` or a live
FAST lease's seat, with VALGATE on the push. The PROD promote stays Andrew's to name.
