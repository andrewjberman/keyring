# TO IRPT_FNTEND.TO-FE-s-34 -- the age names the business date it measures

<to_id>IRPT_FNTEND.TO-FE-s-34</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~3</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-13</issued_date>
<status>pending</status>

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
`F34-AC6` -- the folders that render or compute source ages stay green. FE-s-21 and FE-s-25 compute their expected strings through `formatSourceAge` itself, so the label flows through them rather than breaking them (the issuer's cut-time claim that no test asserts the literal "Updated" was WRONG: `fe-s-21/source-age.test.ts:166` and `fe-s-25/source-age-field.test.ts:65` do -- row W3-S19; see the amendment bound). **PRECONDITION: none required.**

<criterion id="F34-AC7" cell_refs="FE-s-34" judgment="true" drives="none"/>
`F34-AC7` -- graded at L9: a reader reads the label as the age of a business date, not as a refresh time. RECORD; NO VERDICT.

<criterion id="F34-AC8" cell_refs="FE-s-34" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-34/no-status.test.ts</invocation><expect>NO-STATUS DOCUMENT, INSTANT AND BUSINESS DATE DIFFER -> BOTH PANELS AGE THE BUSINESS DATE: 2 of 2(?![0-9])</expect></criterion>
`F34-AC8` -- ruling R outcome (a) (AMENDMENT 2): a document with NO status whose availability instant is 2026-09-10T18:05:00Z and whose own business date is 2026-09-08, parsed from a whole v1 body through the real adapter (never a hand-built envelope), renders the business-date age on StageDisplay and on VariantSelector. The test prints both dates and both rendered strings.

<criterion id="F34-AC9" cell_refs="FE-s-34" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-34/no-status.test.ts</invocation><expect>NO-STATUS DOCUMENT WITHOUT A BUSINESS DATE -> ABSENCE NAMED, NO AGE: 2 of 2(?![0-9])</expect></criterion>
`F34-AC9` -- ruling R outcome (b): the same path with a document that carries no business date names the absence on both panels and renders no age. The test prints both rendered strings.

<criterion id="F34-AC10" cell_refs="FE-s-34" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-25/source-age-field.test.ts</invocation><expect>NO-STATUS ENVELOPE CARRIES THE DOCUMENT'S BUSINESS-DATE READING, NOT THE INSTANT: yes</expect></criterion>
`F34-AC10` -- ruling R outcome (c): the amended fe-s-25 check asserts the reading, not the instant, and prints this line only when the no-status envelope's source date is the document's reading.

<expected_criteria>F34-AC1, F34-AC2, F34-AC3, F34-AC4, F34-AC5, F34-AC6, F34-AC7, F34-AC8, F34-AC9, F34-AC10</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **`state/status.ts` IS YOURS FOR THE LABEL AND THE AGE PATH ONLY.** `isCompleteState`, the state labels, `STATE_FOR_WIRE` and every other function in that file stay as they are. FE-s-30 is building a separate availability module in parallel and never edits this file.
- ⛔ **Under `tabs/analysis/` you own `StageDisplay.tsx` and `VariantSelector.tsx` ONLY.** `composer.ts` is FE-s-35's this round.
- ⛔ **AMENDMENT (2.0.0_SA_COO~F, on row W3-S19): TWO TESTS OF OTHER CELLS ARE YOURS, FOR ONE PURPOSE EACH.** `__tests__/fe-s-21/source-age.test.ts:166` and `__tests__/fe-s-25/source-age-field.test.ts:65` assert the literal prefix `'Updated '` that ruling K removes. Replace ONLY those two checks with one that does not spell the label (for instance equality with `formatSourceAge` of the same date and clock), cite ruling K beside each, show each both ways, and leave every other assertion in both files as written. The criteria are unchanged. Row W3-S21 is answered by AMENDMENT 2 below.
- ⛔ **AMENDMENT 2 (2.0.0_SA_COO~F, on 1.0.0_SA_CTO's RULING R for row W3-S21, @3f3b5337a1): ON THE NO-STATUS PATH THE PANEL AGES THE DOCUMENT'S OWN BUSINESS DATE, NEVER AN INSTANT.** Today a document with no status reaches the panel through `envelopeFromAvailability`, which hands it the availability INSTANT (`sourceAsOf`), and the new label calls that a business date. The document's own business-date READING is already built in `contracts/adapt.ts` from `sourceTimestamps.businessAsOf` and then dropped; only its value survives. The remedy, and only it: the no-status document's availability carries that reading (`Availability.sourceDate`, typed `SourceDateReading` at `contracts/index.ts:133`, which you READ and do not edit), and the panel ages a business date only where one was measured; where the reading states absence, the panel names the absence and shows no age. `contracts/adapt.ts` joins the grant for that one purpose (FE-s-35 drained it at portal 850d7718 and it is in your branch since c18a2aab). `state/status.ts`'s `envelopeFromAvailability` is yours for its no-status branch too. `__tests__/fe-s-25/` joins the grant for ONE purpose: change only the claims ruling R SUPERSEDES -- FE-s-25's no-status instant, and the `source-age-field.test.ts:128` check that pins it by regex -- citing ruling R beside each, and leave every other assertion as written. Nothing labelled a business date may measure an instant, on any path. Row W3-S22 (fe-s-21's test-built as_of envelope) is not this amendment's. THREE CRITERIA ARE ADDED, F34-AC8..AC10, carrying 1.0.0_SA_CTO's stated outcomes; F34-AC1..AC7 are byte-identical. The order is reopened to `pending` until all ten are met.
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
portal/src/pages/InvestorReporting/__tests__/fe-s-21/source-age.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-25/
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-34/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.5 @a4ac61a1cf, cell `FE-s-34`.
<owned_cells>FE-s-34</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F34-AC1` .. `F34-AC10`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-34.business-date-label.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F34-AC1,F34-AC2,F34-AC3,F34-AC4,F34-AC5,F34-AC6,F34-AC7,F34-AC8,F34-AC9,F34-AC10` BEFORE the `complete` flip. `F34-AC7` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `business-date-label.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
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
overturned tests: RUN, and WRONG at the cut -- fe-s-21/source-age.test.ts:166 and fe-s-25/source-age-field.test.ts:65 assert the literal 'Updated ' prefix (row W3-S19); both granted by amendment, one purpose each.
lane: the <paths> block IS the grant; composer.ts excluded (FE-s-35's).
</preflight>

Seating: slot ~3; wave B -- seated only after FE-s-29 is drained, on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the pair is cut (row S26).
