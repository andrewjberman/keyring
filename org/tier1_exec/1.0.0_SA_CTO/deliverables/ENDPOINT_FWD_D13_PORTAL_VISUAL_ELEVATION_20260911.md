# ENDPOINT (step 2, /endpoint --forward) — D13 Design: Portal Visual Elevation

**Brief:** `docs/briefs/portal-visual-elevation-brief-20260911.md` @`d4b20a28ba` (22,051 bytes; authored by
`0.1.1_RD_MarketPerformance` on Andrew's direct word, adopted as the L1 input on that word).
**Directive:** D13 Design, LAPTOP (Andrew-ruled 2026-09-11). **Macro:** `DSGN` — RATIFIED by Andrew-direct 2026-09-11 ~07:1xZ at the
`0.0.0_AB_MSTR` terminal ("First macro will be DSGN, obviously"; scope "design system, branding, aesthetic frontend"; LD-0552).
**Project code:** `DSGN_PORTALVIS`, minted at L3 the same turn. **Lead:** `2.0.0_SA_COO~D` (Andrew-direct ~07:5xZ at this terminal:
`0.1.1_RD_MarketPerformance` promoted to `2.0.0_SA_COO~D` to lead the DSGN project).
**Written by:** `1.0.0_SA_CTO`, 2026-09-11 ~07:5xZ. **NOT YET LANDED in a PRD** — a PRD does not exist; this block is
the ENDPOINT section that PRD will carry verbatim once L3 mints the code.

---

## THE OUTCOMES

```
  FWD-1  A prospect moving from the website into the portal does not experience a change of firm
         DONE WHEN  EXERCISED -- one person who has never seen the portal is walked from opalinvest.com into a portal route and asked what changed
         ACCEPT     the person names capability differences (it does more, it shows my data) and no visual ones; typeface, canvas colour, corner radius, focus visibility and the role of navy read as one system across the boundary
         PROOF      the website's measured values (design/brand/opalinvest.com.json) beside the same measurements taken headlessly on three portal routes; every dimension in the brief's IV.3 table reads the same on both sides, or the difference is a deliberate inverted band
         SOURCE     brief O1; IV.2 (the website is a measured system); IV.3 (the portal contradicts it on every dimension but shadows)
         CONSTRAINT Andrew-direct 2026-09-11: THE CANVAS IS LIGHT #F4F6FA with #0A1733 reserved for deliberate inverted bands. This SUPERSEDES the 2026-07-15 archetype in design/brand/COLOR_ARCHETYPES.md and design/systems/portal/DESIGN_SYSTEM.md ("light silver #C3CADA canvas, dark navy containers floating on it"); those files are REWRITTEN under this project, never left standing beside a new contract

  FWD-2  An advisor reads a figure without the typeface telling them it came out of a terminal
         DONE WHEN  APPLIED -- every numeral in the product renders in the firm's typeface with tabular alignment
         ACCEPT     an advisor reading a return, a value or a date cannot tell from its letterforms whether it came from the product or a developer's console, and columns of figures still line up
         PROOF      the 222 font-mono occurrences at the cut are zero in portal/src/ or each remaining one is a code sample, not a figure; three routes rendered before and after with the figure columns compared by eye and by pixel alignment
         SOURCE     brief O2; IV.3 (Numerals row); III.2
         CONSTRAINT Lato self-hosted at the weights the website ships (400/700); the licence is VERIFIED before it is relied on (brief V.1 did not verify it)

  FWD-3  An advisor reads the ORDER of an ordered scale off its colour, without a legend
         DONE WHEN  APPLIED -- every ordered quantity in the product is one hue ramped light to dark
         ACCEPT     shown a duration ladder, a performance band or an over/under-weight scale with the legend covered, an advisor puts the steps in the right order
         PROOF      a census of every ordered scale in portal/src/ (denominator printed) and, for each, the ramp it now uses; the /positioning five-hue segmented control (UST/ST/INT/LT/ULT) is the named positive case
         SOURCE     brief O3; III.4; VI (the five-hue segmented control)
         CONSTRAINT the charts keep their colour: "don't forego the color of the charts themselves" (Andrew). What goes quiet is the chrome; a ramp replaces unordered hue on ORDERED quantities only

  FWD-4  An advisor can tell at a glance which single thing on a screen is the action to take
         DONE WHEN  APPLIED -- each view spends the accent on one primary action and nothing else
         ACCEPT     on any screen an advisor points at the one thing that is clearly the action; tabs, segmented controls and toggles mark their active state by weight and rule, never by a filled accent chip per option
         PROOF      three routes rendered; the accent colour's share of pixels per route printed and the elements carrying it enumerated -- one per view
         SOURCE     brief O4; III.3; IV.2 (accent never above 1.0 % on the website)

  FWD-5  An advisor working by keyboard can see where they are
         DONE WHEN  APPLIED -- focus is visible on every interactive element, with the ring the website ships
         ACCEPT     tabbing through any route, the advisor always sees which element is focused
         PROOF      a keyboard walk of three routes recorded as screenshots at each stop; the `outline: none !important` at portal/src/index.css:166 is gone
         SOURCE     brief O5; IV.3 (Focus ring row); III.9

  FWD-6  A builder derives every visual decision from one written contract, and a reviewer can FAIL a page by citing its clause
         DONE WHEN  EXERCISED -- one new page has been built from the contract alone by someone who has not seen the portal, and one page has been rejected by clause
         ACCEPT     the contract resolves typeface, colour role, spacing, shape, elevation, focus and layout split; it is the file the estate's design tooling reads; a rejected page's author agrees the clause was violated without further argument
         PROOF      the contract (portal/DESIGN.md, RATIFIED by the PRD, not the RD-authored draft as-is) and the token files it governs agree byte-for-byte on every value the contract names; the three token writers of brief V.2 are one; one build-from-contract and one rejection-by-clause are on record
         SOURCE     brief O6; III.6; III.8; IV.4 (the token architecture is already correct); IV.5 (one writer is dead code); IV.7 (the estate already has the pattern; no parallel structure); IV.8 (DESIGN.md is the container the tooling reads)
         CONSTRAINT populate and enforce the EXISTING design/ repository and the frontend-dev verification loop; a second design repository or a second verification mechanism is the shadow system the estate bans; the existing archetype documents are rewritten in place (FWD-1 CONSTRAINT)

  FWD-7  A chart series is never painted in the colour the product reserves for "something is wrong"
         DONE WHEN  APPLIED -- status colour and data colour are two separate token systems with no aliasing
         ACCEPT     no series on any chart shares a colour with an error, warning or success state; a reviewer can show the two systems and where they are kept apart
         PROOF      the aliasing at portal/src/index.css:111-115 is gone; every chart palette token and every status token listed with no intersection (both denominators printed)
         SOURCE     brief O7; IV.3 (Chart colours aliased onto status)
         CONSTRAINT the charts stay as colourful as today (Andrew's constraint carried on FWD-3)

  FWD-8  Two charts on the same screen share their axis, tick, tooltip and legend treatment
         DONE WHEN  APPLIED -- a screen's charts come from one rendering system
         ACCEPT     an advisor looking at two charts on one screen sees one product, not two libraries
         PROOF      the import census of brief IV.6 (four charting libraries: recharts 36 files, apexcharts 4, nivo 1, visx 1; two icon sets; two animation libraries) re-run after the change reads ONE charting library, ONE icon set, ONE animation library, with the migrated files enumerated
         SOURCE     brief O8; IV.6
         CONSTRAINT consolidation, never a fifth renderer; a chart that cannot be migrated without changing what it shows is a surprise row, not a quiet exception

  FWD-9  Andrew puts the portal on screen beside an institutional competitor and the difference is not that ours looks generated
         DONE WHEN  EXERCISED -- Andrew has made that comparison and said so
         ACCEPT     the comparison turns on capability rather than on finish
         PROOF      Andrew's word, on the record, after a side-by-side he chooses; graded by him, never self-graded
         SOURCE     brief O9 (the outcome the other eight serve)
         CONSTRAINT this is the one outcome graded by the person it is for; FWD-1..8 are its mechanism, and a grade of REALIZED on all eight does not substitute for his word here
```

**Denominator:** 9 outcomes from 9 brief outcomes (O1-O9), one to one; 9 of 9 carried; 0 dropped; 0 invented.
**Bar:** FWD-1, FWD-6, FWD-9 EXERCISED (a person acts); FWD-2, 3, 4, 5, 7, 8 APPLIED (the change is in place and measured).
**No FWD is a wait** (Rule 27): every proof is an act a seat can take on demand; FWD-9's proof is Andrew's act and is expressly qualified as such on the outcome.

## THE L2 FINDINGS THE PRD MUST CARRY

1. **The brief's largest declared gap is CLOSED at L2.** `design/systems/portal/DESIGN_SYSTEM.md` (34 KB, 2026-07-15),
   `design/brand/COLOR_ARCHETYPES.md` and `design/process/UI_VERIFICATION.md` were read. They carry the 07-15
   archetype "light SILVER canvas #C3CADA, dark navy containers floating on it" as Andrew-direct law of that date, and
   `portal/CLAUDE.md`'s colour law binds the same. **Andrew's 2026-09-11 ruling (canvas #F4F6FA; navy is a text and
   hairline colour, not a surface; #0A1733 only as deliberate inverted bands) SUPERSEDES it.** The PRD names those
   three files and `portal/CLAUDE.md`'s colour law as REWRITE targets in a cell, so the estate never carries two
   archetypes. The verification loop (`UI_VERIFICATION.md`, `frontend-dev`, `ui-smoke.mjs`) is kept as-is.
2. **`ADHC_DESIGN` does not collide.** `org/projects/ADHC_DESIGN.json` reads `status: complete`, CLOSED 2026-04-21.
   The brief's boundary stands; nothing to resolve at L3.
3. **`IRPT_FNTEND` is a consumer, not a sub-scope.** Its round 1 grades design conformity against the PRD v0.6
   sources (brand.json, the guidelines PDF, the logo package, the portal colour law). When this project's contract
   ratifies, IRPT_FNTEND's later rounds inherit it through the token files; `portal/DESIGN.md` (RD draft at portal
   DEV 10236236, LOCAL) carries no authority until this PRD ratifies a version of it.
4. **The register names a directive doc that does not exist:** `DIRECTIVES.yaml` D13 points at
   `docs/architecture/D13_DESIGN_PRD.md`, ABSENT at HEAD. `0.0.0_AB_MSTR`'s to write at mint; surfaced.
5. **Provenance of third-party design tooling:** 29 skills installed under `.claude/skills/` from six repositories;
   unlicensed ones gitignored with a pinned repo+SHA manifest (`design/SKILLS_MANIFEST.md`), licensed ones NOT
   vendored either, because Rule 14's universal `.py` gate cannot admit upstream code (brief V.6). The PRD relies on
   the manifest, never on vendored code.

## L3 (the next limb) -- NOTHING OPEN

The D13 macro enum in `org/missions/MACROS.yaml` already reads `macros: [DSGN]`, RATIFIED on Andrew's word (LD-0552) before this
endpoint was written. The tree row lands as `org/missions/D13/DSGN/DSGN_PORTALVIS/` with `coo_lane: 2.0.0_SA_COO~D`, and this
block becomes the PRD's ENDPOINT section verbatim.

**Provenance.** READ: the brief at `d4b20a28ba` in full; `design/brand/COLOR_ARCHETYPES.md`,
`design/systems/portal/DESIGN_SYSTEM.md` (head), `design/process/UI_VERIFICATION.md`; `org/projects/ADHC_DESIGN.json`;
`org/missions/DIRECTIVES.yaml` D13 row; `org/missions/MACROS.yaml` header and grammar. **NOT READ:** the TO register;
the portal source itself (the brief's measurements are carried, not re-measured); `portal/DESIGN.md` (the draft is
input to L4, not to L2).
