# TO IRPT_FNTEND.TO-FE-s-35 -- a body with no envelope identity is refused by name

<to_id>IRPT_FNTEND.TO-FE-s-35</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~5</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-13</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F12; CONTRACTS consumed) | **Decomp cell:** `FE-s-35` (round 5, v0.5 @a4ac61a1cf) | **outcome_ref:** FWD-1, FWD-4, FWD-6 | **depends_on:** FE-s-29 (sequencing) | **slot:** ~5 | **rows:** W1-S39, W2-S11, C-S65, W1-S20

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-35` -- **the client still accepts, silently, the one kind of body the contract says cannot exist.**

`1.0.0_SA_CTO` ruling P, adopted: **a response body carrying none of `contract_version`, `operation` or `firm_id` is REFUSED.** The contract already rules it: `docs/contracts/investor-reporting/v1/CONTRACT.md:142` -- *"ONE ENVELOPE FOR EVERY ROUTE"* -- and `routes.json:171`, every response on every declared route is `{contract_version, operation, firm_id, data, status?}`.

Measured by the issuer at portal DEV `c2eb8eb4`, in `src/api/endpoints/investor-reporting.ts`:

- `:907` -- `if (isEnvelopeShaped(payload))` admits an envelope-shaped body to the parser, where a refusal inside a well-formed envelope is raised by name.
- `:936-943` -- everything else takes **the pre-envelope plane**: `this.preEnvelopeResponses += 1`, `adapt(payload)`, and the result is returned as a view. Counted, adapted, never refused.

`__tests__/fe-s-19/pre-envelope.test.ts` (F19-AC6) refuses three bodies today -- but each of the three carries TWO of the three identifiers, so each was already envelope-shaped. It says so itself: it prints `PRE-ENVELOPE BYPASS STILL OPEN (row W2-S11, NOT graded here)`. This cell closes that hole. Refuse at `:936-943` with `EnvelopeMismatch` naming `body`, rendered as a state through `envelopeFromRefusal` like F19-AC6's three, so `preEnvelopeResponses` reads 0.

**The suites that serve bare bodies**, measured: of the 6 test files that construct `LiveClient`, **2 carry no `contract_version`** -- `__tests__/fe-s-1/adapter.test.ts` and `__tests__/fe-s-13/no-route.test.ts`. W1-S39 measured three tests red in those two when the branch refuses. Re-base them onto enveloped bodies. `__tests__/fe-s-19/network-state.test.ts` builds v1 envelopes and is safe.

**W1-S20 rides here.** `contracts/adapt.ts` types the analysis request's `report_title` as `string` (`:1098`) while `tabs/analysis/composer.ts` types the same body's `report_title` as `string | null` (`:107`) -- two builders of one body. Make them agree with the contract's schema for that field.

### ACCEPTANCE

<criterion id="F35-AC1" cell_refs="FE-s-35" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F35-AC1` -- the whole portal typechecks.

<criterion id="F35-AC2" cell_refs="FE-s-35" drives="network"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/pre-envelope.test.ts</invocation><expect>PRE-ENVELOPE BODIES REFUSED: 4 of 4(?![0-9])</expect></criterion>
`F35-AC2` -- F19-AC6 gains a fourth body carrying none of the three identifiers, refused by name through `LiveClient` and its transport, and rendered as a state. The test prints each body's reason and state.

<criterion id="F35-AC3" cell_refs="FE-s-35" drives="network"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/pre-envelope.test.ts</invocation><expect>CONTROL: a whole v1 envelope on the same path -> ACCEPTED</expect></criterion>
`F35-AC3` -- the whole-envelope positive control, UNCHANGED: the refusal is not indiscriminate.

<criterion id="F35-AC4" cell_refs="FE-s-35" drives="network"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-35/no-identity.test.ts</invocation><expect>PRE-ENVELOPE PLANE ADAPTED: 0(?![0-9])</expect></criterion>
`F35-AC4` -- after a no-identity body is served, `LiveClient.preEnvelopeResponses` reads 0. The test also prints the refusal's public reason naming `body`.

<criterion id="F35-AC5" cell_refs="FE-s-35" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-35/no-identity.test.ts</invocation><expect>REPORT_TITLE AGREES WITH THE CONTRACT IN BOTH BUILDERS: 2 of 2(?![0-9])</expect></criterion>
`F35-AC5` -- W1-S20. The test reads the contract schema's type for `report_title` and both builders' types and prints all three.

<criterion id="F35-AC6" cell_refs="FE-s-35" drives="none"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-1 src/pages/InvestorReporting/__tests__/fe-s-13 src/pages/InvestorReporting/__tests__/fe-s-14 src/pages/InvestorReporting/__tests__/fe-s-19 src/pages/InvestorReporting/__tests__/fe-s-35</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F35-AC6` -- every folder that constructs `LiveClient` stays green, with the round-1 suites re-based. **PRECONDITION: none required** -- fe-s-19's browser tests report SKIPPED without a server. Record which way you ran it.

<criterion id="F35-AC7" cell_refs="FE-s-35" judgment="true" drives="none"/>
`F35-AC7` -- graded at L9: a response with no envelope reaches a user as a named refusal, never as a blank page or a guessed view. RECORD; NO VERDICT.

<expected_criteria>F35-AC1, F35-AC2, F35-AC3, F35-AC4, F35-AC5, F35-AC6, F35-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **`contracts/adapt.ts` AND `tabs/analysis/composer.ts` ARE YOURS FOR `report_title` ONLY.** `STATE_FOR_WIRE`, the envelope adapters and everything else in `adapt.ts` stay as they are; `StageDisplay.tsx` and `VariantSelector.tsx` are FE-s-34's.
- ⛔ **DO NOT TOUCH `docs/contracts/investor-reporting/v1/`.** The contract already rules this; a contract defect is a row for `1.0.0_SA_CTO`.
- ⛔ **RE-BASE, DO NOT WEAKEN.** In `fe-s-1/` and `fe-s-13/`, change a test's served body from bare to enveloped and keep what it asserts. A test that only passed because the bare plane existed is a row naming it, not a deletion.
- **`contracts/envelope.ts`** describes the pre-envelope plane in its header (`:34-40`). Correct that description to match the refusal; no other change there.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W5-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/InvestorReporting/contracts/envelope.ts
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/tabs/analysis/composer.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-1/
portal/src/pages/InvestorReporting/__tests__/fe-s-13/
portal/src/pages/InvestorReporting/__tests__/fe-s-19/pre-envelope.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-35/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.5 @a4ac61a1cf, cell `FE-s-35`.
<owned_cells>FE-s-35</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F35-AC1` .. `F35-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~5/IRPT_FNTEND.TO-FE-s-35.envelope-refusal.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F35-AC1,F35-AC2,F35-AC3,F35-AC4,F35-AC5,F35-AC6,F35-AC7` BEFORE the `complete` flip. `F35-AC7` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `envelope-refusal.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the branch: RUN by the issuer at portal DEV c2eb8eb4 -- investor-reporting.ts:907 isEnvelopeShaped; :936-943 the pre-envelope plane (counted, adapted, returned).
the suites: RUN -- 6 LiveClient suites; fe-s-1/adapter and fe-s-13/no-route carry no contract_version; fe-s-19/network-state builds v1 envelopes.
the test's vocabulary: RUN -- pre-envelope.test.ts prints PRE-ENVELOPE BODIES REFUSED: 3 of 3 and CONTROL: ... ACCEPTED at DEV.
W1-S20: RUN -- adapt.ts:1098 report_title: string; composer.ts:107 report_title: string | null.
lane: the <paths> block IS the grant; adapt.ts and composer.ts for report_title only.
</preflight>

Seating: slot ~5; wave B -- seated only after FE-s-29 is drained, on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the pair is cut (row S26).
