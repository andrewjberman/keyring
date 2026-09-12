# TO IRPT_FNTEND.TO-FE-s-19 -- the envelope-to-view seam: the state the wire sends is the state the view gets

<to_id>IRPT_FNTEND.TO-FE-s-19</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-12</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F1, F7, F12; CONTRACTS `StatusEnvelope` consumed) | **Decomp cell:** `FE-s-19` (round 3, v0.3 @38f68b965c) | **outcome_ref:** FWD-1, FWD-5, FWD-6 | **depends_on:** none -- READY ROOT | **slot:** ~1, queue position 1 | **rows:** W1-S33, S30, W2-S11

---

## WORKER FACE

### THE CELL

`FE-s-19` -- **the Reporting and Holdings tab bodies cannot mount from any network response, and the whole test suite is blind to it.**

The chain, read at source and confirmed twice (by `0.9.0_WK_IRPT_FNTEND~1` in round 2 and independently by the issuer and by `1.0.0_SA_CTO`):

- `contracts/envelope.ts` parses the v1 envelope and DOES build the real state: `state: status?.state ?? 'READY'`.
- `src/api/endpoints/investor-reporting.ts:932` returns `parsed.data` on the non-status branch -- the parsed envelope, and its state, is DISCARDED. The sibling at `:930` returns `parsed.status`, so the state EXISTS on that code path and is dropped on this one.
- `contracts/adapt.ts:157` then fills `availability.state` from `parts.state ?? EXPLICIT_UNKNOWN_STATE`, and `:103` defines `EXPLICIT_UNKNOWN_STATE = 'UNCERTAIN'`.
- `tabs/TabShell.tsx:133`, `:148` and `:150` gate the Reporting and Holdings bodies on `envelopeFromAvailability(<x>.availability)`.

So every network-sourced response reaches the tabs as `UNCERTAIN` and the bodies render the status panel instead of content. Round 1's own committed captures show both bodies rendering, so this is a REGRESSION that arrived with the envelope plane.

**THE DESIGN QUESTION IS YOURS TO ANSWER AND IT IS THE POINT OF THIS CELL.** What should the view's state derive from once the envelope carries it -- does `availability` remain the carrier and get filled from the envelope, or does the envelope's state reach `TabShell` directly and `availability` keep only its source timestamps? Decide it, implement it, and STATE THE DECISION AND ITS REASON in the result file. Do not preserve a shape merely because it is there. What is NOT open: the browser never derives a state the wire did not send, and an absent state still renders as the explicit unknown rather than as a default.

**Also carried: `W2-S11`.** `LiveClient` still ACCEPTS a body carrying none of `contract_version` / `operation` / `firm_id`, so the strict v1 envelope parser has a pre-envelope bypass on this same plane. A body that is not a v1 envelope is refused with a named reason; the refusal is a state, not an exception that reaches a panel.

### ⛔ TWO CLAUSES BIND EVERY CRITERION BELOW. READ THEM BEFORE YOU WRITE A TEST.

**1. NETWORK, NOT SEEDED.** Every criterion here DRIVES FROM A NETWORK RESPONSE -- the value enters through the client/transport boundary and travels the path a browser takes. **A test satisfiable by seeding `initialEnvelope`, `initialHoldingsEnvelope`, `initialReport` or `initialSnapshot` DOES NOT SATISFY ANY CRITERION IN THIS ORDER**, and writing one is a refusal, not a pass. This is not stylistic: round 2's suite ran 420 passing tests over this exact defect because every arm seeded the thing the arms share. Stub the transport, not the component.

**2. NEGATIVE CONTROL -- EVERY NEW TEST IS SHOWN RED FIRST.** Your worktree starts at the PRE-FIX bytes, which is the only moment this is free. **Write each new test file, run it BEFORE you change any source, and record its failing output. Then fix. Then run it again.** The instance records BOTH runs for every new test file. A seam criterion that has never failed is a seeded test wearing different clothes, and you cannot tell the two apart after the fact.

### ACCEPTANCE

<criterion id="F19-AC1" cell_refs="FE-s-19"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F19-AC1` -- the whole portal typechecks.

<criterion id="F19-AC2" cell_refs="FE-s-19"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/network-state.test.ts</invocation><expect>NETWORK STATES CARRIED: 9 of 9</expect></criterion>
`F19-AC2` -- a v1 envelope delivered THROUGH THE TRANSPORT for each of the nine `StatusEnvelope` states arrives at the view carrying that same state. The test prints the state it sent and the state the view received, per state.

<criterion id="F19-AC3" cell_refs="FE-s-19"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/network-state.test.ts</invocation><expect>SEEDED PROPS USED: 0</expect></criterion>
`F19-AC3` -- the test file itself asserts it seeds nothing: a source scan of `__tests__/fe-s-19/` for `initialEnvelope`, `initialHoldingsEnvelope`, `initialReport` and `initialSnapshot` returns zero hits, printed with the four tokens it scanned for and a positive control proving the scan can find one.

<criterion id="F19-AC4" cell_refs="FE-s-19"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/mounted-from-wire.test.ts</invocation><expect>BODIES MOUNTED: 2 of 2</expect></criterion>
`F19-AC4` -- with a READY envelope delivered through the transport, the Reporting tab body and the Holdings tab body both render their content rather than the status panel. The test prints, per tab, the slot it found.

<criterion id="F19-AC5" cell_refs="FE-s-19"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/mounted-from-wire.test.ts</invocation><expect>UNCERTAIN WITHOUT A WIRE STATE: 2 of 2</expect></criterion>
`F19-AC5` -- the discrimination arm: an envelope whose `status` carries NO state still reaches both tabs as the explicit unknown, so the fix carries the wire's state without inventing one when the wire has none.

<criterion id="F19-AC6" cell_refs="FE-s-19"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/pre-envelope.test.ts</invocation><expect>PRE-ENVELOPE BODIES REFUSED: 3 of 3</expect></criterion>
`F19-AC6` -- `W2-S11`: three bodies missing `contract_version`, `operation` and `firm_id` respectively are each REFUSED with a named public reason, and the refusal renders as a state. A positive control shows a well-formed v1 envelope on the same path is accepted.

<criterion id="F19-AC7" cell_refs="FE-s-19"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19</invocation><expect>0 fail</expect></criterion>
`F19-AC7` -- the whole fe-s-19 folder is green.

<criterion id="F19-AC8" cell_refs="FE-s-19"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>1 fail</expect></criterion>
`F19-AC8` (BAR CORRECTED BY THE ISSUER, row IRPT_FNTEND-S41 -- it read `0 fail` on a PREDICTION I made and the worker MEASURED FALSE). The set reads **exactly one** remaining failure and it is `F18-AC3`'s capture collision; **print the failing test's name**, and if it is anything else, or if a second appears, that is a BLOCKING row. ⛔ **WHY THE COLLISION DOES NOT CLEAR WHEN THIS CELL LANDS, which is what I got wrong:** `F18-AC3` grades ELEVEN COMMITTED PNG FILES and a source change cannot move image bytes -- re-capturing is `FE-s-18`'s cell and `__tests__/fe-s-18/` is in nobody's round-3 grant. AND a re-take would STILL collide: all three Holdings smoke maps carry NINE v1 envelopes and ZERO `status` members (issuer's own census: 84 envelopes across 36 maps, 3 carrying `status`), and `status` is the only wire carrier of a state on this plane -- so under your now-correct bytes those three maps render three identical panels BY THE CONTRACT. Clearing it needs a FIXTURE cell, which is a round-3 input and not yours. The stale-pin failure is `FE-s-20`'s and has already drained.

<criterion id="F19-AC9" cell_refs="FE-s-19"><invocation>cd <WS> && timeout 120 python -c "import io; p='org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/envelope-to-view-seam.result.md'; print('PRE-FIX RED HEADINGS:', io.open(p, encoding='utf-8').read().count('PRE-FIX RED'))"</invocation><expect>PRE-FIX RED HEADINGS: 3</expect></criterion>
`F19-AC9` -- the NEGATIVE-CONTROL LEDGER: the result file records, under a `PRE-FIX RED` heading for each of the three new test files, the failing output that file produced against the unmodified bytes BEFORE any source change, and beside it the passing output after. Three headings, three pairs.

<criterion id="F19-AC10" cell_refs="FE-s-19" judgment="true"/>
`F19-AC10` -- graded at L9: the design decision recorded in the result file (what the view's state derives from, and why) is coherent with the contract and does not reintroduce a browser-side derivation. RECORD; NO VERDICT.

<expected_criteria>F19-AC1, F19-AC2, F19-AC3, F19-AC4, F19-AC5, F19-AC6, F19-AC7, F19-AC8, F19-AC9, F19-AC10</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. ⛔ **`contracts/` IS SPLIT THIS ROUND: you own `adapt.ts` and `envelope.ts`; `contracts/wire/` is `FE-s-20`'s and is READ ONLY to you.** `state/status.ts` is yours this wave and `FE-s-21` is sequenced behind you on it. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **No derivation.** A wire->view adapter renames and restructures. It never derives, averages, infers or defaults a value; a value the wire does not carry renders as the explicit unknown.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal` as in your identity line. Portal commit pathspec: the files you changed under `src/`, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. If you need one: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>` from `<WS>/portal`, once, in the background; kill it before your final report.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Producer vintage is DATA.** `docs/contracts/investor-reporting/v1/` is at `58e387b454` in your tree. Record that vintage in the result file. **Do not add a byte or sha pin on it** -- that is the practice `FE-s-20` is retiring, and it moved four times during round 2, once inside a worker's pass.
- **Surprise.** ONE row per finding in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md`, id `IRPT_FNTEND-W1-S<k>` continuing the W1 sequence (last is `W1-S36`, so yours start at `W1-S37`). Re-read the file immediately before minting each id; never edit an existing row; keep working.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Never repair a criterion, widen it, or satisfy it by a route this cut did not name.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/contracts/envelope.ts
portal/src/pages/InvestorReporting/tabs/TabShell.tsx
portal/src/pages/InvestorReporting/state/status.ts
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-19/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.3 @38f68b965c, cell `FE-s-19`.
<owned_cells>FE-s-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F19-AC1` .. `F19-AC10`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-19.envelope-to-view-seam.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F19-AC1,F19-AC2,F19-AC3,F19-AC4,F19-AC5,F19-AC6,F19-AC7,F19-AC8,F19-AC9,F19-AC10` BEFORE the `complete` flip. `F19-AC10` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `envelope-to-view-seam.result.md` beside it, carrying the design decision, the producer vintage as data, and the three `PRE-FIX RED` pairs. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 (both halves SIGNED, ADMITTED) -- carried; the PRD is unchanged this round (1.0.0_SA_CTO 96062).
defect: RUN by the issuer -- source read at the pin (investor-reporting.ts:932 against the sibling :930; TabShell.tsx:133/:148/:150; adapt.ts:103/:157; envelope.ts) plus a comp-find census of envelopeFromAvailability (34 hits / 305 files, DEF=3).
blindness: RUN -- every tab-body test seeds its envelope (fe-s-5/controls, fe-s-5/fields, fe-s-5/states, fe-s-10/parity via initialEnvelope; fe-s-10/tabs-mounted via initialHoldingsEnvelope); 0 traverse the network path.
lane: the <paths> block IS the grant; contracts/ is SPLIT BY FILE against FE-s-20; state/status.ts is shared with FE-s-21 and sequenced. Portal paths bind by reading; workspace paths bind mechanically.
</preflight>

Seating: slot ~1, queue position 1; READY ROOT, seated at issuance on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the worktree is cut (row IRPT_FNTEND-S26).
