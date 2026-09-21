# TO IRPT_FNTEND.TO-FE-s-55 -- a non-authoritative Holdings classification reads "withheld", never "unknown"

<to_id>IRPT_FNTEND.TO-FE-s-55</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~5</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

⛔ **COO DRAIN NOTE (2.0.0_SA_COO~F, 2026-09-21 ~14:30Z).** The worker correctly left this `pending`: F55-AC5
measured FAIL at its own worktree's vintage on the same `fe-s-49` F49-AC8 residual, filed as row `W5-S8`
(INERT), already fixed upstream by `FE-s-51`. It also correctly filed `W5-S9` (ARMED, disarm_owner this seat --
`fe-s-32/holdings-in-a-browser.test.ts`'s latent stale assertion, tracked separately, not a blocker on this
order). Verified independently in the MERGED tree after this cell's drain (portal `8fb94607`, workspace
`7737c8356e`): `bun test src/pages/InvestorReporting` reads `592 pass / 21 skip / 0 fail`. All seven mechanical
criteria hold at the merged vintage; flipping to `complete` on that measurement.

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-55` (round 9, v0.9) | **outcome_ref:** FWD-5 | **depends_on:** none | **slot:** ~6 | **rows:** W4-S19 (round-8 analysis item 5)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-55` -- **round-8's analysis, item 5, VERBATIM:** *"W4-S19 -- RULING W reaches Holdings: a classification
the producer does not assert reads 'withheld'. Both PRDs' CONTRACTS line reads: 'Both only when authoritative;
an unknown value is an explicit unknown state, never false and never Client.' So 'unknown' is a value the
producer ASSERTS. A partition the panel declines to assert is not that value, and printing it as 'unknown'
makes it indistinguishable from one. `tabs/holdings/slices.ts:100-102` renders every partition of a
non-authoritative classification as 'withheld'. 'Render every partition above as unknown' is the portal's OWN
comment (`contracts/index.ts:708`), not ratified text. So this is a cell, not an L4 amendment. That comment and
`slices.ts`'s header (:21-25) change with the code. `SliceTable`'s `data-classification-authoritative` marker
stays. Before the edit, a WHOLE-SUITE run finds every test that asserts 'unknown' for a non-authoritative
classification. A grep cannot see what a test asserts through a helper."*

**Measured by the issuer at portal DEV be8cf21874:** `renderedClassification()` (`tabs/holdings/slices.ts:100-109`):
```ts
export function renderedClassification(classification: HoldingsClassification): RenderedClassification {
  if (!classification.authoritative) {
    return { supervision: 'unknown', advisory: 'unknown', authoritative: false }
  }
  ...
}
```
**This is the EXACT precedent FE-s-48 already applied to `ScopeSummary.tsx`'s cohort display** (that fix's own
comment, still live: "a value the panel declines to assert is withheld, not unknown" -- `header/ScopeSummary.tsx:9-14`).
This cell applies the SAME distinction to Holdings.

**THE REMEDY:**
1. **Before any edit**, run the whole IRPT_FNTEND suite and grep its OWN ASSERTIONS (never a source grep --
   "a grep cannot see what a test asserts through a helper") for every test that currently expects `'unknown'`
   on a non-authoritative classification's `supervision` or `advisory` field. Print the denominator: N tests
   found, by file:line.
2. Introduce a `'withheld'` member distinct from `'unknown'` on `RenderedClassification`'s `supervision` and
   `advisory` fields (extend the type; `'unknown'` remains a legitimate value for an AUTHORITATIVE-but-unknown
   producer assertion elsewhere in the type -- confirm this by reading how `SUPERVISION_FOR_WIRE`/`advisoryFromWire`
   in `contracts/adapt.ts` already produce an asserted `'unknown'`, and do not collapse that case into
   `'withheld'`).
3. Change `slices.ts:100-109`'s non-authoritative branch to return `'withheld'` for both fields.
4. Update EVERY test found in step 1 to expect `'withheld'` instead, and add at least one NEW test asserting the
   AUTHORITATIVE + producer-asserted-`'unknown'` case is STILL `'unknown'`, unchanged (the discriminator that
   proves the two are not conflated).
5. `SliceTable.tsx` (the render consumer) must render `'withheld'` distinctly from `'unknown'` in its own text
   (read how it currently renders the field before assuming a one-line change suffices); its
   `data-classification-authoritative` marker is UNCHANGED per the analysis's own instruction.
6. Update `slices.ts:21-25`'s header comment and `contracts/index.ts:708`'s comment to describe the new
   behavior -- they are PROSE, not ratified text, and change with the code per the analysis.

### ACCEPTANCE

<criterion id="F55-AC1" cell_refs="FE-s-55" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F55-AC1` -- the whole portal typechecks.

<criterion id="F55-AC2" cell_refs="FE-s-55" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-7</invocation><expect>PRE-EDIT DENOMINATOR -- TESTS ASSERTING 'unknown' ON NON-AUTHORITATIVE: (\d+)(?![0-9])</expect></criterion>
`F55-AC2` -- step 1's denominator, printed BEFORE your edit (run this once against the unmodified checkout,
capture the output, then make your changes).

<criterion id="F55-AC3" cell_refs="FE-s-55" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-7</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F55-AC3` -- the whole fe-s-7 (Holdings) suite passes AFTER your edit, with every test from step 1 updated to
`'withheld'` and the new authoritative-`'unknown'` discriminator test added.

<criterion id="F55-AC4" cell_refs="FE-s-55" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-55/withheld-vs-unknown.test.ts</invocation><expect>WITHHELD DISTINCT FROM ASSERTED UNKNOWN: yes(?![0-9])</expect></criterion>
`F55-AC4` -- your new discriminator test: a non-authoritative classification renders `'withheld'`; an
authoritative classification whose producer value is the asserted `'unknown'` token STILL renders `'unknown'`;
the two are never the same rendered value.

<criterion id="F55-AC5" cell_refs="FE-s-55" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F55-AC5` -- the whole IRPT_FNTEND suite is green.

<criterion id="F55-AC6" cell_refs="FE-s-55" drives="none"><invocation>cd <WS>/portal && grep -n 'data-classification-authoritative' src/pages/InvestorReporting/tabs/holdings/SliceTable.tsx</invocation><expect>data-classification-authoritative</expect></criterion>
`F55-AC6` -- the marker is present and unchanged (still reads the `authoritative` boolean, never the new
`'withheld'`/`'unknown'` split).

<criterion id="F55-AC7" cell_refs="FE-s-55" judgment="true" drives="none"/>
`F55-AC7` -- graded at L9: `'withheld'` and an asserted `'unknown'` never collapse into each other anywhere in
the render path, and the pre/post denominators in F55-AC2/AC3 account for every test touched. RECORD; NO
VERDICT.

<expected_criteria>F55-AC1, F55-AC2, F55-AC3, F55-AC4, F55-AC5, F55-AC6, F55-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/`
  and this order's own file.
- ⛔ **`data-classification-authoritative` DOES NOT CHANGE.** Per the analysis's own instruction.
- ⛔ **`'unknown'` STAYS A LEGITIMATE, DISTINCT VALUE** for an authoritative producer assertion; this cell adds
  `'withheld'`, it does not delete or repurpose `'unknown'`.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or
  `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`; read both investigation files before minting.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/slices.ts
portal/src/pages/InvestorReporting/tabs/holdings/SliceTable.tsx
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsSummary.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx
portal/src/pages/InvestorReporting/contracts/index.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-7/
portal/src/pages/InvestorReporting/__tests__/fe-s-55/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.9, cell `FE-s-55`.
<owned_cells>FE-s-55</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F55-AC1` .. `F55-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~5/IRPT_FNTEND.TO-FE-s-55.holdings-non-authoritative-withheld.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F55-AC1,F55-AC2,F55-AC3,F55-AC4,F55-AC5,F55-AC6,F55-AC7 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-55.holdings-non-authoritative-withheld.md`
BEFORE the `complete` flip. `F55-AC7` recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file
`holdings-non-authoritative-withheld.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED).
the defect: RUN by the issuer, round-8 analysis item 5 (W4-S19) -- slices.ts:100-109 read at source, confirmed the non-authoritative branch returns 'unknown' for both fields.
the precedent: RUN -- header/ScopeSummary.tsx already applies the identical withheld-vs-unknown distinction (FE-s-48, round 7), confirmed by source read.
lane: the <paths> block IS the grant.
</preflight>

Seating: wave A, slot ~6; ready root, no dependency edge with any other round-9 cell.
