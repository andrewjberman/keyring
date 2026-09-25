# ANDREW-DIRECT 2026-09-24 ~21:4xZ -- the IRPT UI brief's three calls answered: cash green, progressive disclosure portal-wide, shared picker components

**Channel:** the 1.0.0_SA_CTO terminal, in answer to the calls C1-C3 of
`docs/briefs/irpt-ui-finish-design-brief-20260924.md` @`20f90739bd` (4.0.0_SA_CRO msg 100892). **Recorded by:**
1.0.0_SA_CTO, same turn.

## The questions and answers, verbatim

1. **C1:** "C1, cash colour. Your design note says "green for fixed income and cash". The Positioning page's colour
   ruling keeps cash amber. Which colour should cash be? The answer applies to Positioning as well, so advisors never
   see two cash colours."
   - Options: "Amber (Recommended)", "Green, as in my note".
   - **Answer: "Green, as in my note"**
2. **C2:** "C2, progressive disclosure: a rule for Investor Reporting only, or for the whole portal? (Progressive
   disclosure means a short page at rest, with detail behind toggles, tiles and dialogs.)"
   - Options: "Portal-wide rule (Recommended)", "Investor Reporting only".
   - **Answer: "Portal-wide rule (Recommended)"**
3. **C3:** "C3: the client search box and the paged client list. Build them once as shared portal components, or only
   inside Investor Reporting?"
   - Options: "Shared components (Recommended)", "Investor Reporting only".
   - **Answer: "Shared components (Recommended)"**

## What it binds

- **Cash is green on every surface, Positioning included.**
  - It supersedes the POSN_ASTTAX PRD section 3 line "amber stays Cash"
    (`org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md:185-188`) for this colour only.
  - The change lands in `portal/src/lib/chartColors.ts` `ASSET_CLASS` as DSGN_IRPTV1 cell C18, whose criterion names
    Positioning.
  - Fixed income stays green too; sub-asset shades keep the two apart.
- **Progressive disclosure is portal law.**
  - It becomes one clause in `portal/DESIGN.md`, written under DSGN_REBRND by its COO lane `2.0.0_SA_COO~D`
    (DSGN_IRPTV1 cell C21). Investor Reporting applies it first.
  - Other pages adopt it through their own work, never as a rider.
- **The searchable dropdown and the paginator are shared portal components** under `portal/src/components/ui/`
  (DSGN_IRPTV1 cell C15). Other pages may adopt them through their own work.
- Carried in `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.6 (FWD-13, FWD-16, FWD-3).
