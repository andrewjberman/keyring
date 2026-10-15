# DSGN_RBNDV2 -- ROUND-1 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~08:0xZ)

**On:** the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v1.md` @b7a4c85064. It was graded at L9 under DEC-5 on
the CVO's own walk of the feature-branch build: 2 of 5 judgment criteria MET, 3 NOT MET. **PRD:** v0.1. **Branch:**
`feature/dsgn-rbndv2-light` (laptop, unpushed).

## 1. What round 1 moved

- **The ground and ink are right.** The lavender ground `rgb(234,234,247)` and navy ink are in. Panels are white with a silver
  edge, the violet eyebrow underline works on panels, there are no dark strips and the captions are quiet.
- **Controls and tables pass.** The Period chips and panel buttons read navy on white (RB1R-AC2 MET). The heat tables and tiles
  read white and silver, legibly (RB1R2-AC2 MET).

## 2. The three NOT MET, and what each needs

1. **RB1S-AC3, sidebar accent: a token bug, one fix.** `index.css:141` defines `--rb-accent` as hex `#5F3BE3`, while the
   sidebar wraps it in `hsl(...)`, which is invalid. The eyebrow underline therefore falls back to navy, and the current page's
   underline is dropped.
   - Fix: define the token as HSL components, or use it without `hsl()`. Do the same everywhere the token is read.
   - The sidebar test read source text, so it could not see this. The fix's proof is a computed-style read in the rendered
     page: the current link's `border-bottom-color` equals `rgb(95,59,227)`.
2. **RB1P-AC3, inset cards: one clause.** Trending Topics and Top/Bottom Performers still frame bordered inset cards with a
   coloured left bar inside the panel. That is the box-in-box C-PANEL retires.
   - Fix: these two panels' inner cards become hairline-divided sections.
   - They are page-level components, so this is a permitted per-file edit, named in the order.
3. **RB1H-AC3, heat maps: blocked on Andrew's design call.** The CVO's W4-S1 and W4-S2 graduate to this seat.
   - FWD-4's premise ("instead of the blue scaling") has no target: none of the eight heat maps is blue. They use
     emerald/red/yellow overlays, traffic-light bins or diverging pink/green, and the Returns heatmap has no shading.
   - A single white-to-silver ramp shows size but not sign.
   - FWD-4 needs a PRD addendum after Andrew picks a shape. It is carded to him with a recommendation.

## 3. Process rows

- **W6-S2:** the order template puts the RECORD face into the worker's copy, a spine departure. The COO's next issuance gives
  workers the worker face only.
- **RV-r-1 and RV-r-2 lack a `<round>` tag:** fixed at the next issuance; round-close-check now reads the issuance round
  (NFRA_CTLPLN round 16).

## 4. ENRICHMENT LIST for round 2 (one issuance; C-BRANCH binds)

1. The `--rb-accent` token fix, with a computed-style proof (2.1).
2. The two inset-card panels (2.2).
3. C-MODAL, the shared modal frame and the adoption list (PRD round 2, as planned).
4. FWD-4 is cut only after the addendum lands on Andrew's answer.
