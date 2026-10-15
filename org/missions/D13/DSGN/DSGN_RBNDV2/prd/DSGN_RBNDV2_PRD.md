# DSGN_RBNDV2 -- the portal's light re-skin in three targeted steps and a closing walk, on one laptop feature branch

```json
{
 "project": "DSGN_RBNDV2",
 "directive": "D13",
 "fabric": "laptop",
 "prd_version": "v0.1",
 "step": 4,
 "brief_ref": "docs/briefs/dsgn-rbndv2-sidebar-panel-reskin-brief-20261014.md@7c44838003",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6"],
 "status": "RATIFIED"
}
```

**Author and owner:** `1.0.0_SA_CTO` (L2-L4), 2026-10-15.
**COO lane:** one new laptop COO lane, seated by `0.0.0_AB_MSTR` on this PRD. The laptop then holds three COOs, its limit.
**Macro:** DSGN (D13).
**Registered** @a56aa966ed (tree row `org/missions/D13/DSGN/DSGN_RBNDV2/project.json`).
**Brief:** `docs/briefs/dsgn-rbndv2-sidebar-panel-reskin-brief-20261014.md`, Part I-R @7c44838003, by `4.0.0_SA_CRO~A`.
**Andrew's words** (record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_201xZ_DSGN_RBNDV2_SURGICAL_SIDEBAR_AND_PANEL_RESKIN.md`
and its addenda; this seat's endpoint record):
- ~00:1xZ: "lets do this whole project on the laptop. it should be extremely targeted, I think its just 3 steps. 1.) Sidebar flip to
  this color + background same color #EAEAF7. 2.) Panels flip to this fixture type, including solution for modals. 3.)
  White-&-silver-scaling for heat maps instead of the blue scaling. Once these three are done we just look page by page, modal by
  modal, and point out if reds/greens etc have to be darker."
- ~00:0xZ: "This whole light mode build needs to stay on a feature tree on this box and is only pushed when i say so. also yes, i
  like EAEAF7"
- ~03:5xZ, at the 1.0.0_SA_CTO terminal: "Yes, confirmed, register it on the laptop" and "keep in mind this all stays on one
  specific feature branch"

**Sign-off:** `3.0.0_SA_CVO~L` signs the ratified-text half (ENDPOINT and CONTRACTS). The brief half is accepted because the
CRO wrote the brief (proportionate sign-off).

## ENDPOINT (step 2, /endpoint --forward)

Carried verbatim from `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_DSGN_RBNDV2_20261014.md` @381bba5f54. CONFIRMED by
Andrew ~03:5xZ 2026-10-15.

```
  FWD-1  Andrew opens Market Overview on the laptop's local build of the design branch, signed in with real
         data, and sees the new sidebar, background, panels and heat maps together on a real page
         DONE WHEN  EXERCISED -- Andrew has looked at it and said yes or no
         ACCEPT     the page shows real figures; the new look came from the shared pieces, not from
                    rewriting that page; Andrew can say whether it reads as Opal's work
         SOURCE     brief Part I (the Market Overview thread) with R1-R3

  FWD-2  The sidebar and the page background are the lavender silver Andrew chose
         DONE WHEN  APPLIED -- on every page that uses the standard layout
         ACCEPT     the sidebar and the page behind the panels are both #EAEAF7 on every standard page,
                    and the sidebar's text and active item are still easy to read
         SOURCE     R1

  FWD-3  Panels and pop-up windows use the new panel style
         DONE WHEN  APPLIED -- on every standard panel and every standard pop-up
         ACCEPT     panels are white with a thin silver-grey edge, with no stacked dark strips and no box
                    inside a box; pop-up windows match the panels instead of keeping the old dark look
         SOURCE     R2 ("including solution for modals")

  FWD-4  Heat maps shade from white to silver instead of blue
         DONE WHEN  APPLIED -- every heat map on the standard pieces
         ACCEPT     a reader can still tell high from low at a glance, and no heat map is left in the old
                    blue scale
         SOURCE     R3

  FWD-5  Every page and pop-up has been walked, and any red, green or other signal colour that is too
         faint on the new background is darkened
         DONE WHEN  EXERCISED -- the walk is done and its list is answered
         ACCEPT     there is a list naming each page and pop-up looked at, each colour that needed
                    darkening, and that it was darkened; Andrew agrees nothing on it still reads faint
         SOURCE     R4 ("page by page, modal by modal")

  FWD-6  Nothing leaves the laptop's design branch until Andrew says so
         DONE WHEN  APPLIED -- the branch exists on the laptop and no push of it has happened without his word
         ACCEPT     neither the shared development site nor the live site shows any of this until he
                    says to push it
         SOURCE     Andrew ~00:0xZ ("only pushed when i say so"); his 2026-10-06 light-panel hold
```

## CONTRACTS

| contract | holder | what must hold | measured state behind it |
|---|---|---|---|
| **C-BRANCH (FWD-6)** | the COO lane | ALL of this project's work lives on ONE branch: `feature/dsgn-rbndv2-light` in the portal repo on the laptop, cut from portal DEV's tip at the first issuance. Every worker worktree branches FROM it and merges BACK INTO it, by merge and never rebase. No `cand/*` branch. No merge-forward, no push of this branch or to origin DEV/PROD, without Andrew's word, recorded verbatim. The pre-push payload limb already refuses an unapproved DEV push; this contract adds that the branch itself is not pushed. | Andrew ~00:0xZ and ~03:5xZ; the 2026-10-06 light-panel hold |
| **C-SIDEBAR (FWD-2)** | builder | The sidebar moves out of `App.tsx` into its own component, carrying the same nav data with behaviour unchanged. The sidebar and the page ground read ONE token for `#EAEAF7`. Navy ink; small-caps section labels with the violet underline; the current page marked by an underline, not a filled tile. The round avatar is retired. | brief F1 (sidebar inline at `App.tsx`:93-435) |
| **C-PANEL (FWD-3)** | builder | The panel primitives (`Panel`, `PanelHeader`, `PanelContent` and siblings in `portal/src/ui/components/panels/`) render the "A light" fixture: a white surface, a 1px `#C4CBDB` border, square corners per the radius ladder, a small-caps title with the violet underline, hairline rules, a source caption, and no shadow. The navy header strip, the inset box-in-box and the HelpCircle-title pattern are gone. Edits go to the primitives and at most one token block; no page file is edited for FWD-3's panel half. | brief F2, F3, F5 (Panel 96 importers, PanelHeader 85) |
| **C-MODAL (FWD-3)** | builder | ONE shared modal frame carrying the same fixture. Each modal adopts it. This is the one permitted per-file edit, because modals have no shared frame today. The adoption list names every modal with its file, and a modal not on the list is the defect. | brief F9 (10 `catalyst/dialog` importers; 32 overlay files, not de-duplicated) |
| **C-HEAT (FWD-4)** | builder | ONE white-to-silver scale, defined once as tokens, that every heat map reads. High and low stay distinguishable: the scale's ends differ by a contrast an ordinary reader sees at a glance, and the walk confirms it. | brief F10 (BenchmarkHeatmap, ReturnsHeatmap, percentileColor, ValuationSummaryPanel, Correlation, `Panel variant="heatmap"`; name search, not exhaustive) |
| **C-WALK (FWD-5)** | builder, then Andrew | After FWD-2 to FWD-4, a page-by-page, modal-by-modal walk of the local build on the branch:<br>- every page in the nav, and every modal on C-MODAL's list, screenshotted;<br>- each red, green or other signal colour that reads faint on `#EAEAF7` or white is named;<br>- the darkening is made at the semantic token, never per page, unless a page hard-codes the colour, in which case that page is named.<br>The list is the deliverable Andrew reads. | brief R4 |
| **C-LIVE (FWD-1)** | builder | The thread runs on the LOCAL dev build at port 5174 against the real backend with a real login (`bun run dev:live`), never on fixtures. A panel in its error state because fixtures are absent does not count. | brief Part IV preamble (fixtures absent in the measuring run) |

## 1. The arc

Round 1 builds the thread: FWD-1 on `/market`, with C-SIDEBAR, C-PANEL and C-HEAT landing on the branch. Later rounds enrich:
- round 2: C-MODAL across every modal;
- round 3: the C-WALK and its darkenings, ending in Andrew's read;
- round 4, if needed: any page the walk found drawing its own frame, on Andrew's word page by page.

## 2. Rulings closed at L4 (no decide-first question enters L5)

- **DEC-1 "This fixture type"** is the "A light" board Andrew edited (brief Part I-R). The builder reads it from the board
  artifact the brief cites and reproduces its tokens. It invents nothing.
- **DEC-2 Ground colour:** `#EAEAF7` for the page and sidebar; panels white (Andrew ~00:0xZ). This replaces the 2026-09-11
  `#F4F6FA` canvas inside this build only.
- **DEC-3 No shadows, radius ladder 2/3/4px:** `portal/DESIGN.md` C11 stands. The Hex half borrows hairlines and mono labels,
  never Hex's shadows, grid canvas or serif.
- **DEC-4 DSGN_REBRND's held work is not reused** unless Andrew asks.
- **DEC-5 Andrew's eye is the grade** for FWD-1 and FWD-5, a judgement criterion graded at L9 or by him, never self-graded.

## 3. SURFACE MANIFEST (step 4 -> step 5)

| id | outcome_ref | surface | claim | evidence | verb | depends_on | bound |
|---|---|---|---|---|---|---|---|
| S01 | FWD-6 | portal branch `feature/dsgn-rbndv2-light` (laptop) | held | C-BRANCH | build | -- | one branch; workers merge back into it; no push |
| S02 | FWD-2 | `portal/src/App.tsx` sidebar (:93-435) moved to its own component; one ground token in `portal/src/index.css` | measured (F1) | C-SIDEBAR | build | S01 | behaviour unchanged; one token |
| S03 | FWD-3 | `portal/src/ui/components/panels/` primitives (`Panel`, `PanelHeader`, `PanelContent`, `NestedCard`, `SectionCard`, `DarkCard`) | measured (F2, F5) | C-PANEL | build | S01 | primitives plus one token block; no page file |
| S04 | FWD-4 | the heat-map scale tokens, plus each heat map in F10's list pointed at them | measured (F10, partial) | C-HEAT | build | S01 | one scale; the list is extended if the build finds more |
| S05 | FWD-3 | one shared modal frame, plus each modal on the adoption list | measured (F9) | C-MODAL | build | S03 | the one permitted per-file edit |
| S06 | FWD-5 | the walk list (every nav page and every listed modal), and the semantic colour tokens | held | C-WALK | build | S02-S05 | darken at the token; a hard-coded colour names its page |
| S07 | FWD-1 | `/market` on the local build, live data | held | C-LIVE | wire | S02-S04 | the thread's live trace, read by Andrew |

## 4. BRIEF COVERAGE

R1 maps to FWD-2; R2 to FWD-3 (panels and modals); R3 to FWD-4; R4 to FWD-5. Placement and branch map to FWD-6. The Part I
`/market` thread maps to FWD-1.

**Dropped by Andrew's cut (endpoint v2):** the separate bypass-page list (old O4) and the design-law clause (old O6), as the
endpoint record states. Part I-R's line "O6 still holds" is superseded by his three-step scope as confirmed.
