# DSGN_RBNDV2 -- a surgical re-skin of the portal sidebar and default panel cards (L1 brief)

**Author:** `4.0.0_SA_CRO~A`, 2026-10-14. **Mode:** NEW (a successor project to the closed `DSGN_REBRND`, not a midstream
reopening of it). **Order:** Andrew-direct ~20:1xZ, verbatim in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_201xZ_DSGN_RBNDV2_SURGICAL_SIDEBAR_AND_PANEL_RESKIN.md`
(commit d8fd2d8a32). **Seats:** dell1, per Andrew ("the design project can be handled on DELL1 box"). Seating is the CTO's
act at L3.

**Andrew's premise, verbatim:** "there should be a surgical mechanism for just hitting the sidebar and default panel cards,
using some kind of blend of the hextech and opal website fixtures."

---

## PART I -- THE OUTCOME TERRITORY

### Candidate thread (becomes FWD-1)

Andrew opens ONE page of the portal, `/market` (Market Overview), on the dev build. He sees the new sidebar and the new
default panel, and judges that the page reads as Opal-built rather than as a stock AI-generated dashboard. Both changes
arrive through the shared mechanism (O3). No change is written into the page file itself. `/market` is the right first page:
it carries the most panel kinds (full-width panels, a row of four small panels, a tabbed light panel) and the default sidebar.

### O1 -- A viewer recognises the sidebar as Opal's own, not a template rail

A person who has seen opalinvest.com, opening any portal page, finds that the left navigation shares that site's visual
grammar: labels, rules and type. The portal's current rail reads as a generic admin template: an icon strip, a filled
violet tile for the active item, and a round avatar.

### O2 -- A viewer recognises a panel card as Opal's own, not a stock React card

The same person, reading any default panel, finds that its frame (title, edge, body and source line) shares the
site's grammar and the precision of Hex's analytic surfaces. The current frame has three stacked navy strips with a second
bordered box nested inside the body, and a bold uppercase title followed by a help-circle icon. That frame reads as the
default output of a code generator.

### O3 -- A front-end builder re-skins both through one seam, without touching pages

A front-end builder who changes the sidebar's look or the default panel's look edits the sidebar component and the panel
primitives, plus at most one token block. Every page that uses those primitives follows. No page file is edited to carry
the new look.

### O4 -- A page that bypasses the primitives is visible as such, not silently left behind

A reviewer can name which pages still draw their own card frame outside the primitives, and so did NOT receive the new
panel. This lets "every default panel is new" be checked by hand rather than assumed. The project brings such pages to the
primitive only where Andrew rules it in scope (Part II).

### O5 -- Andrew compares old and new and chooses, before anything reaches a client

Andrew can see the current and the new sidebar and panel on the same page, side by side or one after the other, and give his
word before any of it reaches PROD. Portal PROD pages are client-facing by default under the push law.

### O6 -- The design law says what the new sidebar and panel are, so the next page built inherits them

A builder starting a new page reads the new sidebar and panel grammar as clauses in `portal/DESIGN.md`, not as a memory of
this project. The front-end verification skill checks the new grammar rather than the old one.

---

## PART II -- WHERE THE BOUNDARY SITS

**Owns:**
- the sidebar: today written inline in `portal/src/App.tsx`, no separate component;
- the default panel primitives: `Panel.tsx`, `PanelHeader.tsx` and `PanelContent.tsx` in `portal/src/ui/components/panels/`,
  and their sibling card primitives (`NestedCard.tsx`, `SectionCard.tsx`, `DarkCard.tsx`);
- the token rows those read: radius, border, sidebar ground;
- the DESIGN.md clauses for those two surfaces.

**Does not own:**
- page content, charts, tables, tabs, buttons, inputs, modals;
- the colour of the panel ground. Today it is navy on most panels and white on the "nested/heatmap" variants;
- typography beyond the sidebar and panel title;
- the hero and graphic cards (`HeroGraphic.tsx`, `PhilosophyPillars.tsx`), which already borrow opalinvest.com.

**OPEN FOR ANDREW:** whether panel ground colour is in scope. Andrew's 2026-10-06 hold keeps the light-panel experiment off
the main branch: "the light `/market` is an experiment kept off the main branch without his explicit approval". The record
is `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20261006_1414Z_LIGHT_MARKET_EXPERIMENT_OFF_MAIN_BRANCH.md`.
This brief treats SHAPE and FRAME as in scope and GROUND COLOUR as out, until he says otherwise.

**Siblings, named:**
- `DSGN_REBRND` (D13/DSGN, `project.json` status `closed`). Andrew stopped it on 2026-10-06 ~14:35Z: "Stop work on REBRND".
  He also ruled: "Any work on DSGN_REBRND from this point forward is on hold and not to be merged to the main branch unless
  I explicitly ask for it." RBNDV2 is a new project on Andrew's own new order, not that work resumed. Whether any REBRND
  worktree commit is reused is Andrew's call; this brief proposes none.
- `DSGN_IRPTV1` and `DSGN_AMGTV1` (D13/DSGN): page-level design work. They consume the primitives and inherit the change; they
  do not own it.
- Any project holding a portal FAST lease on a page file. RBNDV2 should not need a page lease (O3); if it does, the lease
  overlap check is the mechanism.

**Pages that bypass the primitives (O4):** bringing them onto `Panel` is a per-page edit, which O3 rules out by default. Pulling
any of them in is Andrew's scope call, not the decomposition's.

---

## PART III -- THE QUALITATIVE BAR

- **Recognisability (O1, O2):** a person shown the portal page beside opalinvest.com says they are the same firm's work. A
  person shown it beside a generic dashboard built from a default component library says they are not.
- **The Hex half is precision, not costume (O2):** what is borrowed from hex.tech reads as analytic instrumentation, for
  example a mono label or a hairline header row. It does not read as Hex's brand: no grid-paper canvas, no crop-mark
  buttons, no editorial serif. A viewer should not say "this looks like Hex".
- **Surgical (O3):** the change lands without editing a page file. A reviewer reading the change finds only the sidebar,
  the primitives and the token block.
- **Nothing regresses:** panel titles still do not overlap their actions at high zoom (Andrew-direct 2026-09-14), focus
  rings stay visible, and the band and canvas contrast law holds.
- **Andrew's eye is the grade (O5):** this is a judgement criterion, graded at L9 or by Andrew, never self-graded by the builder.

---

## PART IV -- THE SUBSTRATE (findings, each measured)

Portal measured at DEV @97c66c93 on 2026-10-14 ~20:3xZ, by reading the source and by headless screenshots of `/market`,
`/positioning` and `/portfolio-management` on the local dev build at port 5174 (fixtures absent, so panels show their error
state; shape is unaffected).

**F1. The sidebar has no component of its own.**
- It is inline in `portal/src/App.tsx`: `SidebarLink` at :165-232, the `<aside>` at :296-435, the nav data `NAV_SECTIONS`
  at :93-151.
- Collapsed it is a 48px icon rail (`w-12`); expanded it is 224px.
- The active item is `rounded-[3px]` with a solid `--semantic-action-primary` (#5F3BE3) fill (:203-206).
- Icons are lucide-react at size 18, stroke 1.5. Section labels are `text-[11px] uppercase tracking-wider text-white/40`.
- The avatar at the foot is a round violet circle.
- Catalyst `sidebar.tsx` and `sidebar-layout.tsx` exist and are imported by nothing.
- Pulling the sidebar into its own file is the first step of O3.

**F2. The panel primitive is used widely; the header has one shape.**
- `Panel.tsx` is imported by 96 files and `PanelHeader.tsx` by 85 files (153 uses). These counts come from the survey and
  were not re-counted.
- `PanelHeader` hardcodes `px-[30px] py-4 border-b border-white/10 bg-[hsl(var(--bg-header))] rounded-t-[4px]`. Its title
  is `text-sm font-bold text-white uppercase tracking-wide` plus a HelpCircle icon (`PanelHeader.tsx`:62, :75-81).
- The header is navy even on the white "nested" variant.
- `PanelContent` uses `rounded-b-lg`, an 8px corner inside a 4px panel.

**F3. The radius token exists but is unread, and one control is.**
- `index.css`:236-240 defines `--radius: 4px` and its siblings. No primitive reads them; each hardcodes `rounded-[4px]` or
  `rounded-[3px]`.
- Tailwind is 4.2.1 with no config and no `@theme` block. The compiled `.rounded-lg` reads `var(--radius-lg)`. So one
  `@theme` block re-shapes every raw `rounded-lg/xl/2xl` class in the product at build time.
- Measured: that radius classes resolve through variables. Inferred, not tested: that the same holds for shadow
  utilities.

**F4. Some pages draw their own card frames.**
- Of 236 non-test page `.tsx` files, 104 contain `rounded-(lg|xl|2xl)`, an upper bound since some hits are buttons.
- 48 of them carry such a radius and import no panel primitive. These are mostly modals, auth pages, TradeSubmission,
  InvestorReporting analysis and DataRefresh.
- These are the O4 population. They still breach `DESIGN.md` C11 (2, 3 and 4px radii only; no shadows).

**F5. The served panel is three navy strips with a second box nested inside.**
- The `/market` and `/positioning` screenshots show a navy header strip, a lighter navy body holding a further bordered
  inset box, and a navy "Source:" footer strip.
- The inset box-within-a-box and the bold uppercase title with a help-circle icon are the two strongest stock-generator
  tells on the panel.

**F6. opalinvest.com fixtures, measured live 2026-10-14 ~20:23Z.**
- Lato only.
- **No `box-shadow` on any element.** Radii are 4px on buttons, 0 elsewhere.
- Dividers are 1px black rules, for example the numbered list "01 / 02 / 03" between full-width rules.
- Eyebrow labels are small uppercase letter-spaced text with a 2px violet (#5F3BE3) underline ("WHY WE EXIST").
- The navy band is #0A1733 and the canvas #F4F6FA. Card frames are borderless with zero radius.
- A prior measurement file exists at `design/brand/opalinvest.com.json`.

**F7. hex.tech fixtures, measured live 2026-10-14 ~20:22Z.**
- Radii cluster at 1-3px; the most common non-zero radius is 3px.
- Hairline borders; a mono face (Cinetype Mono) for section labels set in uppercase between bracket ticks.
- Each panel carries a small mono **tab label attached to its top-left edge** ("Chat with the Hex Agent").
- Inner sub-panels have a hairline header row with the title left and one action right ("Explore").
- Shadows are soft and multi-layer. Opal's no-shadow law wins this conflict.
- Brand-specific, and not to be borrowed: the grid-paper canvas, crop-mark corner handles on buttons, and an editorial
  serif italic.

**F8. Earlier work already borrowed opalinvest.com in a few places.**
- `DSGN_REBRND` established the 2/3/4px radius ladder, no shadows, Lato, and one band per page (`portal/DESIGN.md` C3, C11).
- `HeroGraphic.tsx` and `PhilosophyPillars.tsx` already borrow the site's indigo-underlined eyebrow and numbered rules.
- So the Opal half of the blend has prior art in the estate. It has never been applied to the sidebar or the panel frame.

**Angles for the blend (findings, not a design decision):**
- **Sidebar.**
  - From Opal: text-led labelled navigation, eyebrow section labels with the violet underline, and the active item marked
    by a rule rather than a filled tile.
  - From Hex: mono section labels, square corners and hairline dividers.
  - Retire the filled-tile active state and the round avatar.
- **Panel.**
  - From Opal: a 1px rule as the panel's top edge, and an eyebrow-style title in place of the bold uppercase title plus
    icon.
  - From Hex: an attached tab label, a hairline header row with actions on the right, and the source line as a quiet mono
    caption.
  - Retire the nested inset box.

The choice among these angles belongs to the PRD and to Andrew's eye (O5).

---

## PART V -- WHAT MUST BE TRUE (named, not sequenced)

- Andrew's word on panel ground colour in or out of scope (Part II), given the 2026-10-06 light-panel hold.
- Andrew's word on the bypassing pages in or out of scope (O4).
- A way for Andrew to see old and new on one page (O5). The no-shadow-pipeline law (CLAUDE.md section 5) is written for
  pipelines. Whether a design comparison may use a runtime toggle, a branch preview or a static mock is the CTO's call, not
  this brief's.
- Portal DEV is written only through `.tools/portal-merge-forward.sh` on an approved row. PROD needs Andrew's word for a
  client-facing page, and every portal page with the sidebar is client-facing by default.
- The dell1 seats need a portal checkout and the 5174 dev build there.
- The Yang Liu Teams thread is read and its design asks folded in (Part VII).

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-14 ~20:2xZ-20:3xZ UTC:
- Portal DEV @97c66c93.
- `DSGN_REBRND` status `closed`, stopped by Andrew 2026-10-06.
- No `DSGN_RBNDV2` row anywhere in the repo (`comp-find "DSGN_RBND"`: 0 project hits across 258,453 files scanned).
- The local dev build serves `/market`, `/positioning` and `/portfolio-management` with no fixtures (panels in their error
  state).

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **The Yang Liu Teams thread was NOT READ.** The Opal M365 gateway needed Andrew's sign-in, which was pending at writing.
  That thread is a named input of Andrew's order, and its design points may add to or reorder O1-O2. The CRO owes an
  addendum to this brief once it is read.
- The Hex product app itself (behind login) was not seen; only the marketing site's product renders were.
- File counts in F2 and F4 come from a survey subagent's reads and were spot-checked at the cited lines, not re-counted.
- The shadow half of F3 is inferred.
- No light-ground variant, mobile width or high-zoom state was screenshotted.
- No design was drawn; the angles in Part IV are candidates.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/dsgn-rbndv2-sidebar-panel-reskin-brief-20261014.md
  PROJECT           DSGN_RBNDV2 (NONE-YET registered; D13/DSGN by family)
  EXISTING PRD      NONE (predecessor: org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md)
  ANDREW RECORD     org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_201xZ_DSGN_RBNDV2_SURGICAL_SIDEBAR_AND_PANEL_RESKIN.md
  SIBLING PROJECTS  DSGN_REBRND (closed, merge-held), DSGN_IRPTV1, DSGN_AMGTV1
  PRIOR ART         portal/DESIGN.md C3, C11; portal/src/index.css:230-240; design/brand/opalinvest.com.json;
                    portal/src/ui/components/graphic/HeroGraphic.tsx; portal/src/pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx
  SEAM FILES        portal/src/App.tsx:93-151, :165-232, :296-435; portal/src/ui/components/panels/{Panel,PanelHeader,PanelContent,NestedCard,SectionCard,DarkCard}.tsx
  MEASURED AT       2026-10-14 ~20:2xZ-20:3xZ UTC; portal DEV @97c66c93
```
