# TO IRPT_FNTEND.TO-FE-s-34 -- the age names the business date it measures

<to_id>IRPT_FNTEND.TO-FE-s-34</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~3</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-13</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F5, F7; CONTRACTS `StatusEnvelope` consumed) | **Decomp cell:** `FE-s-34` (round 5, v0.5 @a4ac61a1cf) | **outcome_ref:** FWD-4, FWD-6 | **depends_on:** FE-s-29 (sequencing) | **slot:** ~3 | **rows:** F25-AC12, W1-S46, C-S65

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-34` -- **the figure is right and its label is wrong, and two panels still measure the wrong field.**

Measured by the issuer at portal DEV `c2eb8eb4`:

- **Ruling K.** Since FE-s-25, the source age is computed from `business_date`, correctly. But `formatSourceAge` (`state/status.ts:274`) still labels its figure **"Updated N ago"** (`:280-287`). "Updated" names a refresh instant; the figure now measures a business-date age. Relabel it to name the business date and its age.
- **Ruling O.** `formatSourceAge(` has **3 call sites** across the tab tree's non-test files. One is `state/status.ts:465`, inside `formatSourceAgeForState` -- the fixed path. The other two, `tabs/analysis/StageDisplay.tsx:51` and `tabs/analysis/VariantSelector.tsx:61`, still call `formatSourceAge(envelope.sourceAsOf)`: they age the `as_of` instant, not the `business_date` the clause governs. Route both through `formatSourceAgeForState`, so they carry the same field and the corrected label.

`1.0.0_SA_CTO`'s outcome (ruling O, stated so the cell cannot grade its own key): **zero `formatSourceAge(` call sites outside `state/status.ts`, with the denominator printed, and a fixture whose `as_of` and `business_date` differ shows the business-date age on both panels.**

### ACCEPTANCE

<criterion id="F34-AC1" cell_refs="FE-s-34" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F34-AC1` -- the whole portal typechecks.

<criterion id="F34-AC2" cell_refs="FE-s-34" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-34/label.test.ts</invocation><expect>formatSourceAge\( CALL SITES OUTSIDE state/status.ts: 0(?![0-9])</expect></criterion>
`F34-AC2` -- ruling O's first outcome. A source scan of every non-test file under `src/pages/InvestorReporting/`, the file denominator printed, with a POSITIVE CONTROL proving the scan fires on a seeded call site.

<criterion id="F34-AC3" cell_refs="FE-s-34" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-34/label.test.ts</invocation><expect>ANALYSIS PANELS AGE THE BUSINESS DATE: 2 of 2(?![0-9])</expect></criterion>
`F34-AC3` -- ruling O's second outcome. With a fixture whose `as_of` and `business_date` differ by days, StageDisplay and VariantSelector each render the `business_date` age. The test prints both dates and both rendered strings.

<criterion id="F34-AC4" cell_refs="FE-s-34" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-34/label.test.ts</invocation><expect>THE LABEL NAMES THE BUSINESS DATE: yes</expect></criterion>
`F34-AC4` -- ruling K. The rendered age names the business date it measures. The test prints the label for a fresh, an hours-old and a days-old business date.

<criterion id="F34-AC5" cell_refs="FE-s-34" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-34/label.test.ts</invocation><expect>"UPDATED" ON A BUSINESS-DATE AGE: 0(?![0-9])</expect></criterion>
`F34-AC5` -- the old word is gone from every business-date age the portal renders, by source scan and by render, with a positive control.

<criterion id="F34-AC6" cell_refs="FE-s-34" drives="none"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-3 src/pages/InvestorReporting/__tests__/fe-s-6 src/pages/InvestorReporting/__tests__/fe-s-21 src/pages/InvestorReporting/__tests__/fe-s-25 src/pages/InvestorReporting/__tests__/fe-s-34</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F34-AC6` -- the folders that render or compute source ages stay green. FE-s-21 and FE-s-25 compute their expected strings through `formatSourceAge` itself, so the label flows through them rather than breaking them (measured at the cut: no test asserts the literal "Updated"). **PRECONDITION: none required.**

<criterion id="F34-AC7" cell_refs="FE-s-34" judgment="true" drives="none"/>
`F34-AC7` -- graded at L9: a reader reads the label as the age of a business date, not as a refresh time. RECORD; NO VERDICT.

<expected_criteria>F34-AC1, F34-AC2, F34-AC3, F34-AC4, F34-AC5, F34-AC6, F34-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **`state/status.ts` IS YOURS FOR THE LABEL AND THE AGE PATH ONLY.** `isCompleteState`, the state labels, `STATE_FOR_WIRE` and every other function in that file stay as they are. FE-s-30 is building a separate availability module in parallel and never edits this file.
- ⛔ **Under `tabs/analysis/` you own `StageDisplay.tsx` and `VariantSelector.tsx` ONLY.** `composer.ts` is FE-s-35's this round.
- **No derivation.** Where the business date is absent, render its absence the way `formatSourceAgeForState` already does -- never an `as_of` fallback.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W3-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/state/status.ts
portal/src/pages/InvestorReporting/tabs/analysis/StageDisplay.tsx
portal/src/pages/InvestorReporting/tabs/analysis/VariantSelector.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-34/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.5 @a4ac61a1cf, cell `FE-s-34`.
<owned_cells>FE-s-34</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F34-AC1` .. `F34-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-34.business-date-label.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F34-AC1,F34-AC2,F34-AC3,F34-AC4,F34-AC5,F34-AC6,F34-AC7` BEFORE the `complete` flip. `F34-AC7` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `business-date-label.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the label: RUN by the issuer at portal DEV c2eb8eb4 -- status.ts:280-287 "Updated ..." inside formatSourceAge (:274).
the call sites: RUN -- formatSourceAge( at status.ts:465 (fixed path), StageDisplay.tsx:51, VariantSelector.tsx:61; matches 1.0.0_SA_CTO's census.
overturned tests: RUN -- no test asserts the literal "Updated"; fe-s-21 and fe-s-25 compute expected strings through formatSourceAge.
lane: the <paths> block IS the grant; composer.ts excluded (FE-s-35's).
</preflight>

Seating: slot ~3; wave B -- seated only after FE-s-29 is drained, on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the pair is cut (row S26).
