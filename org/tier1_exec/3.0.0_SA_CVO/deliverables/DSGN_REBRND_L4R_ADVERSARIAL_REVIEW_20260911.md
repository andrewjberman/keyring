# DSGN_REBRND v0.1: adversarial L4-R review

Reviewer: `3.0.0_SA_CVO`. Date: 2026-09-11 UTC. Archetype: VALIDATE.

**REFUSED, ratified-text half.** All 33 DONE WHEN / ACCEPT / PROOF fields match the endpoint source, but textual fidelity does not resolve the conflicting requirements below. The whole PRD was reviewed on the explicit instruction in CTO message 95913; C5-C6 and N1 also return brief-half corrections to the CTO. The brief signature remains the designated `2.0.0_SA_COO~D`'s.

Reviewed PRD: `org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md@9769e40c6fc3deb25b037794f93f4ff792144eaf`, v0.1. All PRD line numbers below bind to that commit.

Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_080xZ_DSGN_REBRND_COO_D_SIGNS_CVO_ADVERSARIAL_SELF_DRIVE_WIDENED.md@2daf4d8b85d146784ab262f29d67effb222f6990`; spine v3.15 `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md@e7e552f7c4752c4e78d196684ca8b76f3bb3d754`, L4-R lines 146-198. The canonical stamp is `prd-signoff.py`, and it signs only the CVO half.

## C1 — Amendment history is inside ENDPOINT

**Ratified-text; lines 28, 42, 68, 81.** The section includes the Andrew-direct date, the superseded 2026-07-15 archetype's historical quotation, parenthetical attributions, and the account of O9 being renumbered O11. These came from the endpoint carrier; the PRD did not invent them. L4-R nevertheless excludes history and annotation from the entire section, heading to next heading.

Move provenance and renumbering history under a separate top-level heading. Preserve the operative light-canvas ruling, the required in-place rewrites of the named archetype files, chart colour preservation, source references, FWD identities and Andrew's exclusive grading of FWD-9. Clean the source carrier consistently. No outcome renumbering is requested.

## C2 — The accent rule rejects the focus and selection rules

**Ratified-text and cells; lines 45-47, 51-53, 109-110, 125.** FWD-4 spends the accent on one primary action and nothing else, and counts exactly one element carrying it. R6 requires the website's purple focus ring on every focused control; R5 additionally puts text selection on the accent. The measured source explicitly gives the accent both roles: `design/brand/opalinvest.com.json@d4b20a28ba67ed96e5ce74327273c54a3df33dbe`, line 14, says "single action accent + focus ring".

Counterexample: leave the purple primary button visible and Tab to a secondary control. A correct purple focus ring makes two elements carry the accent. Selecting text creates another permitted accent use. Removing either focus or selection to satisfy the count would implement the wrong product.

Define the budget by role: one persistent primary-action emphasis; explicitly preserve transient focus and selection feedback and the separate data palette. Grade persistent chrome separately from those states. Carry the qualification in the endpoint, contract, R5 and R6, with a keyboard/selection counterexample in the existing render loop. This reconciles the supplied rules; it does not introduce a second primary action.

## C3 — Reaching the fold is stronger than the density outcome

**Ratified-text and R10; lines 85-89, 114.** The new FWD-10 ACCEPT and R10 require content to reach the fold on every route, even with populated data. The brief's O9 requires generous space inside containers, disciplined space between sections, and an explicit end when content runs out (`portal-visual-elevation-brief-20260911.md@bed01b226a15d80d05269b84dae94f18a1fecfc1`, lines 87-92). It does not require a sparse but valid page to occupy a viewport.

Counterexample: an authorized populated fixture with one short row, existing panels intact, correct spacing and an explicit terminator naturally ends above the fold. The current ACCEPT fails it, or rewards stretching the row/adding filler, despite information architecture being excluded.

Qualify the fold observation for the named representative populated fixtures; grade genuinely short content by the contract's spacing and explicit end state. Add a sparse-populated negative control. Preserve the before/after whitespace measurements and the 1440x900 baseline; no invented minimum occupancy or additional panels are requested. FWD-10's plain-English problem is specifically "any route ... content reach the fold", not its density direction.

## C4 — The contract's source rule leaves new values and contrast without a defined basis

**Ratified-text and R3/R7/R8; lines 107, 111-112, 121, 125, 127-128.** CONTRACTS declares the website the source of every non-brand value, while the new contract must supply status/data families, dark-mode values and a minimum text contrast. The measured website JSON has no status family, data palette, dark-mode contract or minimum-contrast criterion. Its measurements cannot be cited as if they supplied those choices. R8 correctly reuses the existing model data palette, another source beyond the two allowed by line 121.

R3 then accepts every pair meeting whatever minimum R7 states. A contract that states a 1:1 minimum would pass that sentence without providing readable text. This is a missing acceptance basis, not a claim that such a contract or implementation already exists.

Distinguish fixed brand values, measured website values, preserved existing data colours, and newly derived design choices. Name the derivation/ratification rule for the latter and a pinned accessibility criterion for the text classes and backgrounds being tested. Keep the measured values and the single token writer; do not label invented status/contrast values as captured observations. R3 must test that independent stated bar, including inverted-band and selected-mode pairs.

## C5 — Unconditional light-canvas acceptance conflicts with the retained dark toggle

**Brief-half correction; lines 105, 107, 125-126.** R1 preserves the user-selectable dark theme and DesignTokens carries `darkMode`, while R3 requires the resolved canvas on every route to be `#F4F6FA` and permits dark fields only as enumerated bands. A user selecting the retained dark mode fails the unconditional R3 acceptance.

State explicitly that the light-canvas and inversion measurements apply to the default light mode. Preserve the deliberate dark selection, its mode-specific token values and matching native-control `color-scheme`; include a light -> dark -> light exercise with no residual dark declaration after switching back. This implements the brief's V.3 and III.7 without changing the default ruling.

## C6 — Three representative renders do not cover the product-wide claims

**Brief-half correction; lines 101, 107, 109-110, 114, 155-158, 198.** R3 claims the canvas and controls on every route; FWD-4/5 and their cells promise product-wide action/focus behavior. The evidence repeatedly limits rendering and keyboard walks to three routes. The listed tree-wide censuses cover mono classes, scales, palettes, imports and empty states; they do not establish rendered canvas, focus traversal or native controls on the other routes.

This also weakens the existing loop the PRD promises to retain. `design/process/UI_VERIFICATION.md@210f70a9aafe3f896ba39fb9e5cc5d5daf87fdc6`, lines 6-8 and 15-16, requires a read screenshot for client-facing visual changes and every state touched.

Keep the three routes as the fixed before/after comparison set. Add an affected-route/state inventory with a denominator, fixture source and a read-render/keyboard obligation for each touched surface; explicitly retain the existing loop's coverage rule. Component reuse is evidence to record, not permission to silently skip distinct layouts. No new verification framework, live backend access or competitor capture is requested.

## N1 — Defect accounting repeats an inconsistent source total

**Brief-half accounting correction; lines 165 and 202.** The brief's Appendix A contains 23 rows, with exactly two rows showing no outcome: A15 and A22. Its prose says three. A21 explicitly maps to O11; the PRD invents an A21 "cosmetic half" to explain the discrepancy. The PRD does map all 23 rows to cells, so this is not an omitted defect.

Report 21 outcome-bearing rows and two cleanup-only rows, or explicitly identify a different authorized classification. Keep A21's actual O11 mapping and the no-outcome status of A15/A22. Do not manufacture a third row from a partial label.

## Checks that passed and boundaries retained

Read the complete PRD, complete pinned brief, endpoint record, designated-review authority, measured website JSON, existing token JSON/CSS at portal `787015e8`, the existing verification loop, and the relevant IRPT_FNTEND v0.6 consumer clauses at `d1479bc5f07c24359246ce460f586bc705ca7010`. The large legacy DESIGN_SYSTEM.md was inspected for its old colour law and structure, not represented as fully re-read or implementation-validated.

The adjacent `DSGN_REBRND_L4R_COMPARISON_20260911.json` records all 33 matching field pairs at PRD/source commit `9769e40c6fc3deb25b037794f93f4ff792144eaf`, the 32 brief headings, 23 defect rows and a changed-proof control. Both HEAD and working-tree PRD text matched that pin when compared. This proves the copy is faithful, not that all copied requirements are mutually satisfiable.

The 11 outcomes preserve FWD-9's identity and correctly add FWD-10/FWD-11 for the inserted brief outcomes. FWD-11's four states and no-duplicate-message bar are plain and disputable. FWD-9 expressly assigns the final act to Andrew; R13 prepares the pack and does not commission competitor access or substitute a self-grade. No objection is raised to that essential human act.

The one-writer intent, in-place archetype replacement, third-party provenance limits, existing design/verification reuse, draft DESIGN.md's lack of authority, and IRPT_FNTEND's consumer boundary are all carried. The absent D13 directive document remains the register owner's item. Lato's actual shipped font files still need the coverage check already required by R2. Chart migration must preserve meaning and route surprises; no product data, auth or API implementation is commissioned by this review.

## Unknown unknowns and disposition

No portal rendering, source implementation, deployment, font download or external site capture was performed in this document review. The examples above expose incompatible requirements and insufficient planned evidence; they are not invented observations of broken future code. The canonical `python .tools/prd-signoff.py status DSGN_REBRND` initially reports both halves MISSING and the project WITHHELD.

The CTO should reconcile C1-C4 in the endpoint/contract carriers and C5-C6/N1 in the cells/coverage, then return the changed halves for delta review. The CVO refuses only its ratified-text half through the canonical stamp, with this pinned review and a one-line reason; COO~D retains the brief-half decision. Push state: LOCAL; no push performed.

Signed: `3.0.0_SA_CVO`.
