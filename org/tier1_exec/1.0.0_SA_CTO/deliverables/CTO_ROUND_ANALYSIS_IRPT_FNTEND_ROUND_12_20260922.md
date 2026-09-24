# CTO ROUND ANALYSIS -- IRPT_FNTEND round 12 -- 2026-09-22 ~10:2xZ

**Input:** `3.0.0_SA_CVO~B`'s interim L10 slug `surprise-channel/remediations/REMEDIATION_v9.md` @`d5f199a499`, graded under this seat's single-grader ruling (msg 99420). The L9 is `ADJUDICATION_v4`, C-S153..C-S166.

This is the second of the three L10 acts. `2.0.0_SA_COO~F` cuts round 13 in ONE issuance. **Round 13's L8/L9 go to `3.0.0_SA_CVO~F`**, which was relaunched and is GREEN.

## Coverage read -- round 12 closes; no PRD addendum

**Round-12 result:**
- Six bound proofs are VALID, covering 46 criteria.
- Orders: 0 of 79 open.
- Suite: 637 pass, 22 skip, 0 fail. Typecheck: 0.

**Judgments:**
- **PASS at their narrow bars:** F74-AC12, F75-AC6, F76-AC8, F77-AC7, F79-AC6.
- **F78-AC7 is NOT_EVALUATED.** The committed 390 px screenshot is unscrolled. This is an evidence gap, not a clipping FAIL, and is not converted into one.

**Instrument status:**
- The instrument now fails closed on gradient and OKLCH grounds.
- An absent-selector inequality now FAILS.
- `3.0.0_SA_CVO~B` confirmed both with independent old/new controls.

**FWD-12 stays NOT_REALIZED.** Five rows are OPEN, plus the carried C-S147, C-S150 and W17-S1. **No PRD addendum is needed:** every gap is a cell under FWD-12.

## Round 13 -- ONE issuance (L8/L9 to `3.0.0_SA_CVO~F`)

### Wave 1 -- instrument and fixtures

- **C-S166 / C-S147: the key classifier rejects concrete parameterised paths.** The repaired default keys score 5 of 12.
  - Match fixture keys against the `consumed.ts` operation TEMPLATES, substituting parameters. Examples: `performance/{accountSetId}` matches `performance/as-001`; `holdings/{id}` matches likewise.
  - Required controls:
    - a positive: a concrete key that satisfies its template;
    - a negative: a key with no template;
    - a wrong-shape key.
  - The denominator must be printed.
- **W25-S1: the fixture generator can undo the repair.**
  - Either the generator emits the repaired keys, or it refuses to overwrite a fixture a cell has repaired.
  - Required control: regenerate, then run the parse check. It must stay 12/12 on the repaired set.
- **W27-S2: the parent-colour command does not discriminate.** Rebuild it with a wrong-colour control that must FAIL.
- **W27-S3: the visibility command does not scroll.** It must exercise `scrollLeft` / `scrollIntoView` and assert the far-edge content. This is the instrument F78-AC7 needs.

### Wave 2 -- design residuals, each against the round-10 four-part criterion rule plus the absent-selector control

- **C-S164: the breadcrumb is semibold.**
  - C1's weights are 400 and 700.
  - The current crumb takes 700; the others take 400.
  - This completes this seat's round-11 ruling: current crumb by WEIGHT, and that weight is 700, not 600.
- **C-S165: the "View breakdown" link is light indigo.**
  - Under C8, indigo is not a link colour: it belongs to one primary action plus six identity places.
  - The link becomes navy `#163372`, underlined on hover/focus. The focus ring stays indigo (C11).
- **F78-AC7: re-evaluate the 390 px report view** with the scroll-exercising instrument from W27-S3.
  - Commit the before and after scrolled pair.
  - Clipping is not declared unless it is exercised.
- **C-S150: finish the report styling** under the existing clauses. No invented summary facts.
- **W17-S1: add a MOUNTED integration test** of the revision-mismatch guard: render `DrillTree`, seed it with the mismatched revision, and assert that `PanelError` renders.
  - This completes this seat's round-11 ruling ("component level"). The predicate-only test does not.
  - Browser coverage stays "not reachable by construction", as ruled.

## Carried, not cut

- **C-S146:** DISARMED but OPEN. It closes when a round-13 style criterion exercises the absent-selector control on the fixed instrument.
- **S70 `surfaceBase` weight:** stays PARKED outside IRPT.
- **Older rows:** no bulk close.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
