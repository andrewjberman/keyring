# CTO ROUND ANALYSIS -- IRPT_FNTEND round 10 -- 2026-09-21 ~23:3xZ

**Inputs:**
- `3.0.0_SA_CVO~F`'s L10 slug `surprise-channel/remediations/REMEDIATION_v7.md` @`e1fbcf38d0` (14 rows).
- L9 `ADJUDICATION_v3.md` (C-S116..C-S131).
- `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND10_L8_L9_20260921.md`, same commit.

This is the second of the three L10 acts (Rule 27). Round 11 is cut by `2.0.0_SA_COO~F` in ONE issuance.

## Coverage read -- round 10 closes; no PRD addendum

**Closure:**
- The gate reads 0 open of 64 orders and 0 undispositioned of 276 items.
- The suite reads 612 pass / 22 skip / 0 fail; typecheck rc=0.

**Judgments:**
- F61-AC5 and F62-AC9 are NOT_EVALUATED: the named renderings are missing.
- F63-AC8 and F64-AC6 PASS as evidence-record criteria ONLY, not as brand conformance.

**FWD-12 (design and reuse conformance) is NOT_REALIZED:**
- Grounded C3, C8 and C12 violations remain on shipped surfaces.
- The Reporting tab's answer-bearing state has never been rendered.

**The other seven outcomes stay NOT_EVALUATED** on the IRPT_BCKEND crossing, as graded @`4030dac`:
- Round 10 did not target them.
- This analysis does not re-grade them.

**Why there is no addendum.** Every gap is a cell the endpoint already covers. None reveals an outcome the endpoint mis-states.

**The one near-miss is C-S129.** The Analysis request LIST has no declared backend route (`NoDeclaredRoute`). Ruling:
- FNTEND must NOT invent that route.
- If an FWD's DONE WHEN needs the list, it is a CROSSING dependency on IRPT_BCKEND, routed to `2.0.0_SA_COO~B` as information.
- The FE cell renders the unavailable state honestly as a disclosed limitation.

## THE CRITERION RULE for round 11 -- binds every visual criterion COO~F cuts

Round 10 proved twice that a color-only or click-only line passes on the wrong page:
- The canvas passed on "Scope could not be resolved".
- The CANVAS line read the page field while the print root was silver.
- My own acceptance of the anchored canvas criterion (msg 99287) was part of that miss, and COO~F corrected it (99297).

So every visual criterion in round 11 carries ALL of the following:
- **(a) WIRE MATCH:** the fixture's keys equal the operation keys in `contracts/wire/consumed.ts`. It prints `matched N of N`.
- **(b) NAMED CONTENT:** the specific cards, values or text the state must show. Each is asserted by a selector or text, not by eye.
- **(c) A WRONG-STATE NEGATIVE CONTROL:** the same assertion run against the error/unresolved fixture, which must FAIL.
- **(d) GROUND MEASURED ON THE ACTUAL ROUTE CONTAINER** (e.g. `.ir-print-root`), not the app page field. This closes W13-S2's class hazard.

A criterion missing any of the four is refused at the cut.

## Round 11 -- ONE issuance, parallel where write surfaces are disjoint

**A. Fixtures -- blocks C, and everything visual depends on it.**
- Rows: W11-S1 and W12-S1 (duplicates of one defect; one cell).
- Repair or RETIRE `fe-s-10-global`, `fe-s-6-ready` and `fe-s-7-smartx` to the live wire keys.
- Author the answer-bearing Reporting fixture (W11-S2's precondition).
- Keep the failed-state captures as the negative-control arm.

**B. C12 error presentation -- shared.**
- Rows: W11-S3, W12-S3.
- Surfaces: the scope-failure text in `index.tsx`; the safe actions from `StatusPanel`; the red-only error text in `GenerateComposer` and `DrillTree`.
- One coherent grant; before/after at 1440 and 390.
- W12-S3's table overflow is EXERCISED (horizontal access), not prescribed from a cropped still.

**C. Reporting, answer-bearing -- depends on A.**
- Row: W11-S2.
- Cards, chart and period results, plus the scope strip's partial-disclosure fact, at 1440 and 390.
- The judgment criterion replaces F61-AC5's unevaluable bar.

**D. Shared-surface style -- the three rows owned by this seat, now dispositioned.**
- **W11-S4:**
  - `PageSurfaceControl` is shared by `FirmDropdown` AND `ModelPortfolios`.
  - It is RULED IN SCOPE for round 11 as one change to the shared component. It is never an IRPT-local look-alike: that would be the duplicate the reuse law forbids.
  - The grant names BOTH consumers' exact-class tests.
  - Before/after captures of the Model Portfolios page ride with it, so the second consumer is proven unbroken.
  - `ScopeSummary`'s cohort/ink residuals ride in the same cell.
- **W12-S2:**
  - The dark gradient `CategoryViewTree` container nested in a white panel violates C3. Fix it at the shared component.
  - The purple breadcrumb is `DrillTree.tsx`'s, reviewed against C8.
  - Canonical data colours are RETAINED. CVO~F correctly scoped out the chart legend.
- **C-S130:**
  - The export modal's `Panel variant=chart` and the filled-primary branding chips fall under the same C3/C8 cell.
  - Same shared-grant rule.
  - Preview scrolling is verified, not inferred.
- **W11-S3:** carried in B above.
- **Conflict rule:** D and B may touch neighbouring files. COO~F decides from the decomposition whether they chain or run in parallel. Two workers never share a write path.

**E. Receipt idle state.**
- Row: S69.
- Idle (no receipt) is distinct from in-flight. Exercise idle, then submitting, then received.
- The smallest correct surface: local submission state first. A shared enum only if that cannot express it.

**F. Holdings withheld, plus reachable Analysis states.**
- Row: C-S129.
- Name which requested states the current contract can reach, and render each at both widths, withheld included.
- The request-list limitation is disclosed, not built (see the coverage read).

**G. Census reasons.**
- Row: W14-S2.
- Correct `UnnamedReasonCodeFlag`'s copied reason.
- Each of the 45 NEW entries states a component-specific need against the nearest existing candidate. A role label is not a reason.

## Not re-dispatched

- **W13-S1 and W13-S3:** REMEDIATED and DISARMED at round 10.
- **W13-S2:** its local print-ground fix stands. The class hazard is carried by the criterion rule's (d) above, which is its remedy; it disarms when a round-11 criterion exercises (d) with a wrong-ground control.
- **The 65 older OPEN remediation rows** (gate warning, unchanged for two or more rounds): no bulk close. COO~F lists in the round-11 issuance which of them any cell touches.

**PUSH STATE:** LOCAL on CLOUD; `0.0.0_AB_MSTR` pushes.
