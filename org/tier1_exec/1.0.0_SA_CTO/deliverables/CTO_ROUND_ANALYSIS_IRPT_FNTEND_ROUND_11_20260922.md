# CTO ROUND ANALYSIS -- IRPT_FNTEND round 11 -- 2026-09-22 ~05:3xZ

**Input:** `3.0.0_SA_CVO~F`'s L10 slug, `surprise-channel/remediations/REMEDIATION_v8.md` @`631b1308cb` (18 rows: 12 OPEN, 6 REMEDIATED).
- The L9 is `ADJUDICATION_v3` C-S132..C-S152, with nine pinned grades.
- The detail file is `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND11_L8_L9_20260922.md`.

This is the second of the three L10 acts. `2.0.0_SA_COO~F` cuts round 12 in ONE issuance.

## Coverage read -- round 11 closes; no PRD addendum

**Round-11 results**
- Grades: 7 PASS, 2 FAIL (F65-AC18, F71-AC17).
- Suite: 627 pass, 22 skip, 0 fail. Typecheck: 0.
- Gate: 0 of 73 orders open.

**What advanced toward FWD-12**
- The Reporting tab's answer-bearing state is rendered (FE-s-68).
- The shared C12 error presentation, the dropdown, Holdings' withheld state, the receipt idle state, and the tree light variant all landed.

**FWD-12 stays NOT_REALIZED.** Two things keep it there:
- 12 OPEN rows remain.
- The instrument itself still has two false-pass classes: W20-S2 (gradient and OKLCH grounds) and C-S146 (a missing selector that passes an inequality check). A PASS it prints cannot yet be trusted on those paths.

The other seven FWDs stay NOT_EVALUATED, on the IRPT_BCKEND crossing. **No PRD addendum is needed:** every gap is a cell under FWD-12.

## RULINGS -- the two calls routed to this seat

### W17-S1 -- the unreachable revision-mismatch branch

**Facts.** `adaptHoldingsSnapshot` assigns one `sourceSetRevision` to every node. So no truthful wire payload can produce the mismatch that the `PanelError` guard catches.

**Ruling:** KEEP the guard as defence-in-depth, and cover it at the COMPONENT level, on the same basis as C-S129 in round 10:
- a unit test that drives the adapter's output, or seeds the component with a mismatched revision, and asserts `PanelError`;
- no wire field is invented;
- no fixture pretends the backend emits it;
- no claim that a browser rendered it.

Browser coverage of this branch is recorded as **not reachable by construction**, citing the adapter line. That is a disclosed limitation, not a gap.

**Un-park:** if IRPT_BCKEND ever sends per-node revisions, this becomes a browser-covered state.

### C-S149 and the DrillTree breadcrumb colour -- NAVY, not purple

**Law.** `portal/DESIGN.md` C8 (lines :352-361) spends `#5F3BE3` on exactly one persistent primary action per view, plus six named identity places:
- the page-title rule
- the header subtext
- the active tab
- the sidebar active item
- the rail edge
- the avatar

It says: *"It is not a chip fill, not a panel border."* A breadcrumb is none of these.

**Ruling:**
- Breadcrumb ink is **navy `#163372`**.
- The current crumb is distinguished by WEIGHT, not colour.
- Links take an underline on hover and focus. The focus ring stays indigo (C11, transient).

**The same clause decides C-S149's top rule.** The indigo top rule at `CategoryViewTree.tsx:936` is a panel border, so it is REMOVED. The in-code comments claiming a "one-accent-link allowance" (`:563-570`, `:665-666`) are false and are corrected.

**Preserved:**
- the data palette (lilac, teal, amber: C6)
- Model Portfolios' default-dark variant

## Round 12 -- ONE issuance

### Wave 1 -- the instrument, which every visual cell depends on

- **W20-S2 and C-S146:** ui-smoke must fail CLOSED.
  - If a ground's paint is unsupported or composited (a gradient, opaque OKLCH, or a layered background), it prints UNMEASURABLE and exits non-zero. It never passes white.
  - Every `--expect-style` (equality AND inequality) requires the selector to resolve. A missing element FAILS.
  - Negative controls must include the real dark-gradient case, an opaque-OKLCH case, an absent selector and a wrong colour. An injected solid silver alone is insufficient, per W20-S2.
- **C-S147:** split key validity from fulfilment.
  - Key validity means the fixture keys are valid operation keys of `consumed.ts`.
  - Fulfilment means each state's expected requests are actually served.
  - Bind the validator to every fixture it certifies. Print the denominator, and print delayed and failed routes.
  - Wire-hit counts alone never validate keys.
- **W16-S1:** the decomposition names FE-s-65-class instrument cells as the explicit predecessor of every cell that invokes them.

### Wave 2 -- design residuals, in parallel on disjoint files

- **W17-S3:** repair or retire the default fixture, which is missing `unprojected_grant` in 12 of 12 cases.
  - Census its consumers.
  - Add a parse control.
- **C-S148:** the modal's C5 inversion, with the actual measured ground.
  - Before-and-after comparison.
  - Exercise `scrollLeft` and the far-edge content.
- **C-S149 and the breadcrumb:** per the ruling above.
- **C-S150:** screen report styling under the existing clauses.
  - Exercise narrow-width reachability before declaring clipping.
  - Do not invent summary facts.
- **C-S151:** the received state has ONE primary action (C8). The other is demoted to the existing secondary `buttonClass`. Exercised on the actual received view.
- **W18-S1:** use an admitted radius on the cohort control, plus a truthful cohort fixture.
- **W22-S1:** measure converted colours against the actual grounds, and replace noncanonical text roles.
  - OKLCH serialisation is gradeable under C3/C9. No DESIGN.md addendum.
- **W17-S1:** the component-level test, per the ruling above.

### Criterion rule

The round-10 four-part rule stands: wire match, named content, wrong-state control, and route-container ground.

**Added:** any colour or style criterion must also carry an absent-selector control.

## Carried, not cut

- The S70 `surfaceBase` weight issue stays PARKED outside IRPT scope.
- The 67 older OPEN rows are not bulk-closed. Cells name any they touch.

**PUSH STATE:** LOCAL on CLOUD; `0.0.0_AB_MSTR` pushes.
