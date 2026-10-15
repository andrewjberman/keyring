# ANDREW DIRECT -- the unmatched-ticker decision tree at filing: Did you mean? Yes / Replace / No (2026-10-15 ~21:5xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `3.0.0_SA_CVO~DELL2`, directly after this seat signed IRPT_ANLREQ PRD v0.18
(review @5c103ee2d3).

**Verbatim:**

> The issue is that there is contradictory information being presented. The frontend has text pop up that says replace the missing ticker with a proxy, but there is no input to do so. What needs to happen is simple, it is a decision tree. If there is a ticker that doesn't connect, we check it. If the ticker doesn't exist outright, we assume it may be a typo and the agent can do a "did you mean?" prompt and the user can say yes, replace, or no. If yes, we accept the swap, if replace we try it with the replaced ticker(s) and rerun the process for those, if no, then we say that Opal Staff will manage the replacement.

## What it touches (surfaced, not adjudicated)

- **The live defect he names.** The filing form shows the words "replace the missing ticker with a proxy" (the door's `NAME_PROXY`
  finding) with no input to do so. That is the PROD refusal behind v0.17.
- **IRPT_ANLREQ C-FILING-HINT (v0.18).** The current text is Use or Keep, with a kept or unpriceable holding filing UNRESOLVED. His tree
  has three answers at the "did you mean?" prompt:
  - **Yes:** accept the suggested symbol.
  - **Replace:** the filer enters replacement ticker(s), and the check runs again for those.
  - **No:** the filer is told that Opal Staff will manage the replacement.

  The REPLACE branch is an input the form does not have today. The NO branch's words differ from v0.18's informational sentence ("The
  analysis will use a similar security in its place ...").
- **C-SWAP.** The NO branch hands the holding to Opal's backend or staff. How that relates to C-SWAP's automatic replacement, and to
  "swaps are not up to the filer" (10-15 ~14:xxZ), is the CTO's to rule.
- **Owners.** `2.0.0_SA_COO~Y2` (the form); `2.0.0_SA_COO~G2` (the door's findings and words, in r33).

-- recorded by 3.0.0_SA_CVO~DELL2
