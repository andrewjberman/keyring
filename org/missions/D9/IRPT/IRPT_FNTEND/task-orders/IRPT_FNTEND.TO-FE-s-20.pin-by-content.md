# TO IRPT_FNTEND.TO-FE-s-20 -- pin by CONTENT; the byte pin is retired for consumer cells

<to_id>IRPT_FNTEND.TO-FE-s-20</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-12</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F1; CONTRACTS, the consumer half) | **Decomp cell:** `FE-s-20` (round 3, v0.3 @38f68b965c) | **outcome_ref:** FWD-1, FWD-6 | **depends_on:** none -- READY ROOT | **slot:** ~2, queue position 1 | **rows:** S20, S21, S28, S33, S35, W2-S10

---

## WORKER FACE

### THE CELL

`FE-s-20` -- **the consumer pins the producer's BYTES, and the producer moved four times in one round.**

`contracts/wire/index.ts:48` defines `WIRE_SCHEMA_PINS`, a sha-per-schema table, and `__tests__/fe-s-13/producer-fixtures.test.ts:104` asserts every live digest equals its pin (`expect(stale).toEqual([])`). Measured cost, in one round:

- `S20`, `S21` -- two moves, six consumer tests red, one whole re-pin cell each time.
- `S28` -- a third move, caught only because the issuer measured the tree at seating time.
- `S33` -- a fourth, `58e387b454`, which landed **fourteen minutes after** a worktree was cut and **while its worker was running**. `git merge-base --is-ancestor 58e387b454 7b04394dcb` returns NO. A worker in a frozen worktree cannot see that and must not.
- `S35` -- and the damage from the fourth was ONE file: `WIRE SCHEMA PINS FRESH: 10 of 11`. One non-breaking producer edit reds the consumer suite.

`1.0.0_SA_CTO` ruling 3 retires the byte pin for consumer cells. **Replace the digest table with the CONTENT this consumer actually depends on** -- the operation ids it calls, the route keys it uses, and the REQUIRED FIELD SETS it reads out of each schema -- so that an additive, non-breaking producer change does not red a single consumer test, while a change that removes or renames something the client consumes still does.

**The producer vintage becomes DATA.** The test PRINTS the vintage it read (`git log -1 --format=%h -- docs/contracts/investor-reporting/v1`) and NEVER asserts on it. A vintage in the output is provenance a reader can act on; a vintage in an assertion is a tripwire on someone else's commit cadence.

**Also carried: `W2-S10`.** Re-basing `fixtures/smoke/default.json` to v1 DECLARED paths (done in round 2 under F14-AC16) broke two pins on the counterpart's replay corpus. Resolve it in the same idiom: the corpus binds the CONTENT it replays, not the bytes of the map.

⛔ **THIS CELL'S SUBJECT IS THE PINNING PRACTICE, NOT THE PRODUCT'S BEHAVIOUR.** You change what the consumer ASSERTS about the producer. You do not change an adapter, a view, or a route, and you do not "fix" a consumer field to match a schema -- a genuine mismatch between what the client reads and what the contract offers is a surprise row for round 3's seam cell, never an edit here.

### ACCEPTANCE

<criterion id="F20-AC1" cell_refs="FE-s-20"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F20-AC1` -- the whole portal typechecks.

<criterion id="F20-AC2" cell_refs="FE-s-20"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-13/producer-fixtures.test.ts</invocation><expect>0 fail</expect></criterion>
`F20-AC2` -- the producer-fixtures battery passes against the contract as it stands at `58e387b454`, with no digest assertion remaining.

<criterion id="F20-AC3" cell_refs="FE-s-20"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-13/producer-fixtures.test.ts</invocation><expect>PRODUCER VINTAGE PRINTED, NOT ASSERTED</expect></criterion>
`F20-AC3` -- the battery prints the producer vintage it read and states in the same line that nothing asserts on it. A source scan of `__tests__/fe-s-13/` for `WIRE_SCHEMA_PINS` and for `.sha256`/`digest(` in an `expect(` returns zero, printed with its denominator and a positive control.

<criterion id="F20-AC4" cell_refs="FE-s-20"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-13/content-pins.test.ts</invocation><expect>CONSUMED CONTENT PINNED: operations, route keys, required fields</expect></criterion>
`F20-AC4` -- the new content pin exists and names all three axes: every operation id the client calls, every route key it uses, and the required field set it reads per schema. The test prints each axis with its denominator.

<criterion id="F20-AC5" cell_refs="FE-s-20"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-13/content-pins.test.ts</invocation><expect>ADDITIVE CHANGE TOLERATED: 3 of 3</expect></criterion>
`F20-AC5` -- **the difference control.** Three synthetic producer mutations that are ADDITIVE and non-breaking (a new optional field on a consumed schema; a new route the client does not call; a new enum member on a field the client does not branch on) each leave the battery GREEN. Run in the same harness as AC6.

<criterion id="F20-AC6" cell_refs="FE-s-20"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-13/content-pins.test.ts</invocation><expect>BREAKING CHANGE CAUGHT: 3 of 3</expect></criterion>
`F20-AC6` -- **the other arm of the same control, and the one that makes AC5 mean something.** Three synthetic mutations that DO break this consumer (a required field the client reads removed; an operation the client calls renamed; a route key it uses deleted) each turn the battery RED. A pin that tolerates everything is not a pin.

<criterion id="F20-AC7" cell_refs="FE-s-20"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-13</invocation><expect>0 fail</expect></criterion>
`F20-AC7` -- the whole fe-s-13 seam battery is green, including the request corpus and `W2-S10`'s two repaired pins.

<criterion id="F20-AC8" cell_refs="FE-s-20"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>1 fail</expect></criterion>
`F20-AC8` -- the whole Investor Reporting set reads **exactly one** remaining failure, and it is `F18-AC3`'s capture collision, which is `FE-s-19`'s to clear and not yours. The bar is deliberately `1 fail` rather than `0 fail`: your cell removes the stale-pin failure and cannot remove the other, and a criterion that demanded zero would be unsatisfiable inside this grant. Print the failing test's name so the identity is on the record, and if the remaining failure is anything OTHER than the capture collision, that is a BLOCKING row.

<criterion id="F20-AC9" cell_refs="FE-s-20" judgment="true"/>
`F20-AC9` -- graded at L9: the content pin names what this consumer genuinely depends on -- not so narrow that a real break slips through, not so wide that it re-creates the byte pin under another name. RECORD; NO VERDICT.

<expected_criteria>F20-AC1, F20-AC2, F20-AC3, F20-AC4, F20-AC5, F20-AC6, F20-AC7, F20-AC8, F20-AC9</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. ⛔ **`contracts/` IS SPLIT THIS ROUND: you own `contracts/wire/` ONLY. `contracts/adapt.ts` and `contracts/envelope.ts` are `FE-s-19`'s and are READ ONLY to you**, and `FE-s-19` is running concurrently in its own worktree. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Synthetic mutations are TEST-LOCAL.** AC5 and AC6 mutate copies inside the test's own fixtures. **Never edit `docs/contracts/investor-reporting/v1/`** -- it is the counterpart's artifact and it is not in your grant in any direction.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal` as in your identity line. Portal commit pathspec: the files you changed under `src/`, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. This cell should not need a dev server; if you start one, kill it before your final report.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md`, id `IRPT_FNTEND-W2-S<k>` continuing the W2 sequence (last is `W2-S14`, so yours start at `W2-S15`). Re-read the file immediately before minting each id; never edit an existing row; keep working.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Never repair a criterion, widen it, or satisfy it by a route this cut did not name.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/contracts/wire/
portal/src/pages/InvestorReporting/fixtures/wire/
portal/src/pages/InvestorReporting/fixtures/smoke/default.json
portal/src/pages/InvestorReporting/__tests__/fe-s-13/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.3 @38f68b965c, cell `FE-s-20`.
<owned_cells>FE-s-20</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F20-AC1` .. `F20-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-20.pin-by-content.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F20-AC1,F20-AC2,F20-AC3,F20-AC4,F20-AC5,F20-AC6,F20-AC7,F20-AC8,F20-AC9` BEFORE the `complete` flip. `F20-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `pin-by-content.result.md` beside it, naming each of the six synthetic mutations and which arm it served. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 (both halves SIGNED, ADMITTED) -- carried; PRD unchanged this round.
producer history: RUN by the issuer -- four moves during round 2 (S20, S21, S28 @b8e98d5a4d, S33 @58e387b454); the fourth is not an ancestor of the worktree cut that preceded it; damage from the fourth measured as `WIRE SCHEMA PINS FRESH: 10 of 11` (S35 corrects an earlier miscount of 3).
symbol location: RUN -- WIRE_SCHEMA_PINS at contracts/wire/index.ts:48 (comp-find, DEF band, 3 of 10 hits); the asserting arm at __tests__/fe-s-13/producer-fixtures.test.ts:104.
lane: the <paths> block IS the grant; contracts/ is SPLIT BY FILE against FE-s-19, which runs concurrently. Portal paths bind by reading.
</preflight>

Seating: slot ~2, queue position 1; READY ROOT, seated at issuance on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the worktree is cut (row IRPT_FNTEND-S26).
