# TO IRPT_FNTEND.TO-FE-s-59 -- ScopeSummary renders the resolved scope's carried unprojected_grant

<to_id>IRPT_FNTEND.TO-FE-s-59</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~9</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

⛔ **COO DRAIN NOTE (2.0.0_SA_COO~F, 2026-09-21 ~17:35Z).** The worker correctly left this `pending`: F59-AC5
genuinely failed at its own vintage (portal `61dbe93c`) on `fe-s-48/withheld.test.ts`'s F48-AC4, a naive
positional-index self-test that requires `header/ScopeSummary.tsx`'s total line count to never change since
DEV `1f3ce9f0` -- any correct, additive edit to the file fails it regardless of content. The worker correctly
refused rather than self-grade past a real failure and filed row `IRPT_FNTEND-W9-S1` (ARMED, disarm_owner this
seat) naming the exact mechanism. Disarmed directly (portal `21d71733`, independent of this drain): pinned the
self-test's "after" read to `FE-s-48`'s own landing commit (`a06252ee`) instead of floating `HEAD`, preserving
its original claim without asserting anything about commits after it -- `fe-s-48` suite 4 of 4 pass. Verified
independently in the merged tree (workspace `3d7043af50`, portal `baad86f0`): whole `src/pages/
InvestorReporting` suite `609 pass / 21 skip / 0 fail`; `bun run typecheck` clean. Flipping to `complete` on
that measurement, on my own authority as issuer, not the worker's. Row `W9-S1` stays recorded ARMED at its own
birth vintage (a row's `hazard_standing` is a birth property, never retrofitted); the disarm is evidenced by
portal commit `21d71733` and this note, not by editing the row.

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-59` (round 9, v0.9, wave B) | **outcome_ref:** FWD-1, FWD-11 | **depends_on:** FE-s-57 (merged, workspace `22f8ee08be`, portal `15ceef79`) | **slot:** ~2 | **rows:** R9.2 `FE-s-59`

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-59` -- **round 9's decomposition, `R9.2`, VERBATIM:** *"`header/ScopeSummary.tsx` takes `scope:
ResolvedScope | null` directly (`:41`); render the same badge idiom reading
`scope?.availability.unprojectedGrant`, placed beside the existing `Fact` grid (`:72-86`), never inside the
cohort blocks (a different concern, not to be conflated per this file's own withheld/unknown distinction)."*

`FE-s-57` (this cell's dependency) has landed: `ResolvedScope extends ContractEnvelope`, and
`ContractEnvelope.availability: Availability` (`contracts/index.ts:242-248`) now carries the optional
`unprojectedGrant?: UnprojectedGrant | null` member (`:111-115`, `:157`). This cell is the RENDERING half only
-- it never re-derives the count, denominator or kinds; it reads what `scope.availability.unprojectedGrant`
already carries.

**Read the PRD's own `unprojected_grant` paragraph** (`org/missions/D9/IRPT/IRPT_FNTEND/prd/IRPT_FNTEND_PRD.md`,
`CONTRACTS` section) before you start -- it is the ratified spec; where this cell's text and the PRD differ, the
PRD governs.

**EXACT CHANGES, at portal DEV `15ceef79`'s current shape (confirm each line number against YOUR checkout before
editing -- cite what you actually find, not this order's numbers, if they have drifted):**

1. **`header/ScopeSummary.tsx`**:
   - `ScopeSummaryProps.scope` is already `ResolvedScope | null` (`:40-41`); no type change needed there.
   - Inside `ScopeSummary` (`:62-125`), add ONE new fact node reading `scope?.availability.unprojectedGrant`,
     rendered ONLY when the grant is present and `count > 0`, sited beside the existing `Fact` grid
     (`:75-86`), using the SAME `Fact` helper component (`:46-53`) where its `{label, value}` shape fits, or a
     dedicated node carrying `data-slot="partial-disclosure"` if the count/denominator/kinds shape does not
     fit `Fact`'s single-string-value contract cleanly -- your call, but the marker `data-slot=
     "partial-disclosure"` must be present on whichever element you choose, matching `FE-s-58`'s own slot name
     so the two surfaces are queryable the same way.
   - **Placement bound (verbatim from the cell text): NEVER inside the `assertable`/`withheld` cohort blocks
     (`:88-121`)** -- those are a different concern (`authoritative` cohort facts), and conflating the two
     is exactly the mistake this order's own text warns against.
   - Text idiom: navy-on-white per portal `CLAUDE.md`'s color law (this component already uses
     `text-slate-900`/`text-slate-600` on the `Panel` surface -- match that, never a light-on-light style).

### ACCEPTANCE

<criterion id="F59-AC1" cell_refs="FE-s-59" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F59-AC1` -- the whole portal typechecks.

<criterion id="F59-AC2" cell_refs="FE-s-59" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-59/scope-summary-badge.test.ts</invocation><expect>PARTIAL-DISCLOSURE RENDERS WHEN count>0: yes(?![0-9])</expect></criterion>
`F59-AC2` -- a `ResolvedScope` whose `.availability.unprojectedGrant` carries `{count: 2, denominator: 8,
kinds: ['accounts']}` renders the `data-slot="partial-disclosure"` node, and its text names `2`, `8` and
`accounts` verbatim.

<criterion id="F59-AC3" cell_refs="FE-s-59" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-59/scope-summary-badge.test.ts</invocation><expect>PARTIAL-DISCLOSURE ABSENT WHEN count=0, NULL, OR scope=null: yes(?![0-9])</expect></criterion>
`F59-AC3` -- THREE arms: `unprojectedGrant: {count: 0, ...}`, `unprojectedGrant: null|undefined`, and
`scope: null` (the whole prop absent) ALL render no `data-slot="partial-disclosure"` node and no crash. Print
all three arms, never a subset.

<criterion id="F59-AC4" cell_refs="FE-s-59" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-59/scope-summary-badge.test.ts</invocation><expect>PARTIAL-DISCLOSURE OUTSIDE COHORT BLOCKS: yes(?![0-9])</expect></criterion>
`F59-AC4` -- the new node's DOM position is a SIBLING of (never a descendant of) the `assertable`/`withheld`
cohort container nodes -- confirm by DOM structure, not by eye.

<criterion id="F59-AC5" cell_refs="FE-s-59" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F59-AC5` -- the whole IRPT_FNTEND suite is green.

<criterion id="F59-AC6" cell_refs="FE-s-59" judgment="true" drives="none"/>
`F59-AC6` -- graded at L9: the badge idiom matches `portal/CLAUDE.md`'s color law (navy ink on the white
panel) -- render and read the screenshot per that file's Verification law, cite the clause number beside your
evidence; the cohort-block separation is genuine (not merely a different CSS class on the same container).
RECORD; NO VERDICT.

<expected_criteria>F59-AC1, F59-AC2, F59-AC3, F59-AC4, F59-AC5, F59-AC6</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/`
  and this order's own file.
- ⛔ **NEVER re-derive `count`/`denominator`/`kinds`.** This cell reads `.availability.unprojectedGrant` as
  carried by FE-s-57; it does not compute, default-guess or infer any of the three fields.
- ⛔ **NEVER place the new node inside the cohort (`assertable`/`withheld`) blocks.** Verbatim bound from the
  cell text.
- ⛔ **Color law (portal `CLAUDE.md`).** Navy-on-white text, never light text on light background; run
  `/frontend-dev` (or an equivalent headless render) and read the screenshot before reporting F59-AC6.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or
  `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W9-S<k>`; read both investigation files before minting.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Disjoint by file from FE-s-58/FE-s-60** (this cell touches `header/ScopeSummary.tsx` only); the three
  wave-B cells run concurrently.

<paths>
portal/src/pages/InvestorReporting/header/ScopeSummary.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-59/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.9, cell `FE-s-59`.
<owned_cells>FE-s-59</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F59-AC1` .. `F59-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~9/IRPT_FNTEND.TO-FE-s-59.scope-summary-unprojected-grant-badge.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F59-AC1,F59-AC2,F59-AC3,F59-AC4,F59-AC5,F59-AC6 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-59.scope-summary-unprojected-grant-badge.md`
BEFORE the `complete` flip. `F59-AC6` recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file
`scope-summary-unprojected-grant-badge.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED, prd-signoff.py status).
the design: RUN by the issuer -- header/ScopeSummary.tsx:1-128 read at source (portal DEV 15ceef79); ResolvedScope extends ContractEnvelope confirmed at contracts/index.ts:242-248,421-424; FE-s-57's Availability.unprojectedGrant confirmed present.
the spec: RUN -- PRD v0.7/v0.8/v0.9's unprojected_grant paragraph read in full at HEAD (@5fd2dc9ab5), both halves SIGNED.
lane: the <paths> block IS the grant.
</preflight>

Seating: wave B, slot ~2; seated on FE-s-57's drain (workspace `22f8ee08be`, portal `15ceef79`), disjoint by
file from FE-s-58/FE-s-60.
