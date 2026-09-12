# TO IRPT_FNTEND.TO-FE-s-25 -- the consumer boundary: a distinction the contract makes must survive arrival

<to_id>IRPT_FNTEND.TO-FE-s-25</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-12</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F1, F7, F12; CONTRACTS `StatusEnvelope` consumed) | **Decomp cell:** `FE-s-25` (round 4, v0.4 @1d9839797c) | **outcome_ref:** FWD-1, FWD-5, FWD-6 | **depends_on:** none -- READY ROOT | **slot:** ~1 | **rows:** W1-S26, W1-S41, W1-S42, W1-S43, C-S50

---

## WORKER FACE

### THE CELL

`FE-s-25` -- **the v0.14 contract is SOUND and four independent measurements say its semantics do not reach the view.**

`3.0.0_SA_CVO` filed this against a PRD half it had itself signed, and `1.0.0_SA_CTO` adopted the formulation verbatim and ruled it against its own amendment:

> **THE SIGNATURE IS NOT FALSIFIED; WHAT IS FALSIFIED IS THE INFERENCE THAT ADMITTED MEANS THE DESCRIBED BEHAVIOUR EXISTS.**

The producer contract STANDS and is NOT re-cut (ruling A). Everything below is the consumer's half. Take them in this order; the first is the one that bites hardest.

**1. `W1-S43` -- `?? null` collapses ABSENT and null.** `contracts/adapt.ts:376`, inside `adaptStatusEnvelope` (`:375`), reads `const asOf = wire.source_dates.as_of ?? null`. v0.14 says `business_date` is **ABSENT, NEVER NULL** on the four no-answer states, and the CTO wrote the reason into the schema's own `$comment`: *an absent field says no value exists; a null invites "we had one and lost it"*. The consumer erases that on arrival. **`?? null` is REFUSED AS A PATTERN wherever the contract distinguishes absent from null** -- not just here.

**2. `W1-S42` -- the age surface reads a different field than the clause governs.** The v0.14 clause governs `business_date`. `adapt.ts:376` computes the age from `source_dates.as_of`, while `state/status.ts:343`'s `sourceDateFact` reads `sourceDates.business_date`. So a **READY** envelope carrying the REQUIRED `business_date` renders *"Source time unknown"* -- the amendment's success case rendering as its failure case.

**3. `W1-S41` -- two different nines.** `adapt.ts:222`'s `STATE_FOR_WIRE` maps the producer's nine-state enum onto the view's CLOSED `EnvelopeState` (`contracts/index.ts:68`), and QUEUED/RUNNING collapse onto `LOADING`. A queued job renders the label **"Loading"**, distinguishable from an unanswered browser only by `IR-JOB-QUEUED`. ⛔ This is Rule 24 landing on the seat that wrote the ruling: the subtraction `9 minus 5` was correct and its DOMAIN was the producer's enum while the claim's population was the view's. **Name which plane you are partitioning and prove the image lands in the other.**

**4. `W1-S26` -- the generator degrades on a valid conditional.** `__tests__/fe-s-13/gen-wire.ts` tests `allOf` BEFORE `type`/`properties`, so regenerating StatusEnvelope at v0.14 emitted `export interface StatusEnvelopeWire unknown` and dropped all seven properties. The CONTRACT is sound; the GENERATOR cannot render an `if/then`.

⛔ **EVERY CRITERION HERE ASSERTS THE DISTINCTION SURVIVES AT THE VIEW.** A test proving the producer emits the right bytes proves nothing this cell exists for. Drive from a wire value and assert what a reader of the page can tell apart.

### ACCEPTANCE

<criterion id="F25-AC1" cell_refs="FE-s-25"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F25-AC1` -- the whole portal typechecks. No environmental precondition.

<criterion id="F25-AC2" cell_refs="FE-s-25"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-25/absent-vs-null.test.ts</invocation><expect>ABSENT AND NULL DISTINGUISHED AT THE VIEW: 4 of 4</expect></criterion>
`F25-AC2` -- `W1-S43`. On all four no-answer states, an envelope whose `business_date` is ABSENT and one whose `business_date` is `null` produce OUTPUTS A READER CAN TELL APART at the view -- not merely different internal values. The test prints, per state, the two rendered strings side by side.

<criterion id="F25-AC3" cell_refs="FE-s-25"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-25/absent-vs-null.test.ts</invocation><expect>NULLISH-COALESCE ON A DISTINGUISHED FIELD: 0</expect></criterion>
`F25-AC3` -- the pattern, not the instance: a source scan of `contracts/` and `state/` for `?? null` applied to a field the contract distinguishes returns zero, printed with its denominator and a POSITIVE CONTROL proving the scan fires on a seeded one.

<criterion id="F25-AC4" cell_refs="FE-s-25"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-25/source-age-field.test.ts</invocation><expect>READY WITH business_date: renders an age</expect></criterion>
`F25-AC4` -- `W1-S42`. A READY envelope carrying the REQUIRED `business_date` renders a real age and NOT "Source time unknown". The test prints the field it read and the string it rendered.

<criterion id="F25-AC5" cell_refs="FE-s-25"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-25/source-age-field.test.ts</invocation><expect>FIELD AGREEMENT: adapt and status read the same field</expect></criterion>
`F25-AC5` -- the two readers agree: whatever field the age surface computes from is the field the v0.14 clause governs, asserted by reading both call sites rather than by one of them.

<criterion id="F25-AC6" cell_refs="FE-s-25"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-25/state-planes.test.ts</invocation><expect>PRODUCER STATES DISTINGUISHABLE AT THE VIEW: 9 of 9</expect></criterion>
`F25-AC6` -- `W1-S41`. Each of the producer's nine states is distinguishable at the view from every other. If two legitimately share a LABEL, the test prints what else distinguishes them and asserts THAT is present and reachable; a pair distinguishable only by a code a reader never sees is a FAIL.

<criterion id="F25-AC7" cell_refs="FE-s-25"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-25/state-planes.test.ts</invocation><expect>PLANES NAMED: producer 9, view</expect></criterion>
`F25-AC7` -- the domain is stated, not assumed: the test prints BOTH enums with their own denominators and the mapping between them, so a later reader can see which plane any partition was taken over.

<criterion id="F25-AC8" cell_refs="FE-s-25"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-25/generator.test.ts</invocation><expect>CONDITIONAL SCHEMA RENDERED: 7 of 7 properties</expect></criterion>
`F25-AC8` -- `W1-S26`. Regenerating StatusEnvelope at the current contract emits an interface carrying all seven properties, not `unknown`. The test prints the generated shape.

<criterion id="F25-AC9" cell_refs="FE-s-25"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-25/generator.test.ts</invocation><expect>DEGRADES LOUDLY: 1 of 1</expect></criterion>
`F25-AC9` -- **the difference control.** A seeded schema construct the generator genuinely cannot render makes it FAIL rather than silently emit `unknown`. A generator that cannot say "I could not render this" is how `W1-S26` reached a signed contract unnoticed.

<criterion id="F25-AC10" cell_refs="FE-s-25"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-25</invocation><expect>0 fail</expect></criterion>
`F25-AC10` -- the whole fe-s-25 folder is green. **PRECONDITION: none** -- this folder must not require a dev server, a browser or a network; if one of your tests does, that is a `BLOCKING` row, because ruling C forbids an undeclared environmental dependency.

<criterion id="F25-AC11" cell_refs="FE-s-25"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-13 src/pages/InvestorReporting/__tests__/fe-s-21</invocation><expect>0 fail</expect></criterion>
`F25-AC11` -- the two batteries your changes reach most directly -- the seam's and the source-age cell's -- stay green. **PRECONDITION: none; both are pure bun tests.** ⛔ This order carries NO whole-suite bar: ruling C forbids one without a declared precondition, and the suite's count is environment-dependent.

<criterion id="F25-AC12" cell_refs="FE-s-25" judgment="true"/>
`F25-AC12` -- graded at L9: the four fixes preserve what the contract distinguishes without inventing a distinction the contract does not make. RECORD; NO VERDICT.

<expected_criteria>F25-AC1, F25-AC2, F25-AC3, F25-AC4, F25-AC5, F25-AC6, F25-AC7, F25-AC8, F25-AC9, F25-AC10, F25-AC11, F25-AC12</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- ⛔ **DO NOT TOUCH `docs/contracts/investor-reporting/v1/`.** Ruling A stands the producer contract and this cell is the consumer's half only. A genuine contract defect is a surprise row for `1.0.0_SA_CTO`, never an edit.
- **No derivation.** You render what the wire carries or you render its absence, distinguishably. Never fabricate a value to make a distinction visible.
- **Every criterion here is a pure bun test by design.** If you believe one needs a server or a browser, DECLARE it and file a row -- do not add an undeclared dependency (ruling C).
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed under `src/`, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md`, id `IRPT_FNTEND-W1-S<k>`. ⛔ **Read the WHOLE channel PLANE -- `INVESTIGATION_v1.md` AND `_v2.md` -- for the last W1 id before minting.** The gate allocates across both documents and a starting number named in a face was wrong once this project (row S36), so this face names none. Write the file with `newline='\n'` and **read the diffstat of your commit**: an append that touches lines it did not write is doing something else (row S47).
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Every round of this project so far, the refusals were right.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/contracts/index.ts
portal/src/pages/InvestorReporting/contracts/wire/
portal/src/pages/InvestorReporting/state/status.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-25/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.4 @1d9839797c, cell `FE-s-25`.
<owned_cells>FE-s-25</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F25-AC1` .. `F25-AC12`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-25.consumer-boundary.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F25-AC1,F25-AC2,F25-AC3,F25-AC4,F25-AC5,F25-AC6,F25-AC7,F25-AC8,F25-AC9,F25-AC10,F25-AC11,F25-AC12` BEFORE the `complete` flip. `F25-AC12` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `consumer-boundary.result.md` beside it, stating for each of the four rows what a reader of the page can now tell apart that they could not before. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 (both halves SIGNED, ADMITTED) -- carried; the PRD is unchanged this round and ruling A explicitly does NOT re-cut the producer contract.
the four defects: RUN by the issuer AT THE PIN before cutting -- adaptStatusEnvelope adapt.ts:375 with `source_dates.as_of ?? null` at :376; STATE_FOR_WIRE adapt.ts:222 against ENVELOPE_STATES contracts/index.ts:68; sourceDateFact state/status.ts:343 reading business_date; the generator at __tests__/fe-s-13/gen-wire.ts (comp-find --name: 1 hit of 325 files).
provenance: C-S50 was filed by 3.0.0_SA_CVO AGAINST A HALF IT HAD SIGNED, and 1.0.0_SA_CTO adopted it verbatim against its own amendment. Neither is this seat's finding and both are cited as theirs.
lane: the <paths> block IS the grant; contracts/ is wholly this cell's this round (FE-s-20 and FE-s-23 are terminal). Portal paths bind by reading; workspace paths bind mechanically.
</preflight>

Seating: slot ~1; READY ROOT, seated at issuance on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the worktree is cut (row S26).
