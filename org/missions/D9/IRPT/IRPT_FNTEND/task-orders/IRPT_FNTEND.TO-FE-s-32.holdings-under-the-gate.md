# TO IRPT_FNTEND.TO-FE-s-32 -- Holdings shows a qualified answer, and a real render proves it

<to_id>IRPT_FNTEND.TO-FE-s-32</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-13</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F6, F7; CONTRACTS `HoldingsSnapshot` consumed) | **Decomp cell:** `FE-s-32` (round 5, v0.5 @a4ac61a1cf) | **outcome_ref:** FWD-5, FWD-6 | **depends_on:** FE-s-30 (its predicate), FE-s-33 (the parented tree) | **slot:** ~2 | **rows:** W2-S21, W1-S35, C-S57

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-32` -- **0 of 3 Holdings captures render the basis or the classification their claims declare** (the CVO's measurement, stronger than W2-S21's 1 of 3), because `tabs/holdings/HoldingsTab.tsx:90` mounts the body on READY only:

```
if (!snapshot || envelope.state !== 'READY') { return <StatusPanel tabId="holdings" envelope={envelope} /> }
```

`1.0.0_SA_CTO` ruling I, adopted: **none of W2-S21's three disarms is the fix -- the gate is.**

- **The fix is Holdings under FE-s-30's predicate:** a PARTIAL snapshot (missing attribution) renders the holdings with the classification gap visible as unknown; an UNCERTAIN snapshot (target basis) renders the weights with the unnamed model revision stated. No-answer states keep the panel.
- **Then (a) is the check:** does each Holdings capture render the field its claim declares -- **read from a REAL render, never from seeded state** (S42: this portal has no DOM test environment, so a seeded body and a mounted one are indistinguishable).
- **(b) is REJECTED.** Withdrawing the claim for the captures a READY-only mount cannot draw would ratify a FWD-5 violation. **The claims model is not edited.**
- **(c) holds for NO-ANSWER states only.** A status panel carrying its reason is the honest capture of UNAVAILABLE or FAILED; it is not a capture of an answer.

**W1-S35 rides here.** The pie labels clip at `tabs/holdings/DrillTree.tsx:194` (`outerRadius={100}`, with a label callback drawing `name: value` outside the arc). Round 2's layout-only bound excluded that prop by name. You own it now.

**The FE-s-18 bound-5 DISTINCTION verdict is frozen here.** In `__tests__/fe-s-22/capture-hash.test.ts`, the DISTINCTION test's round-2-shaped verdict still reads LIVE capture digests. Its one assertion counts defective fixtures and does not read digests, so it passes either way, and FE-s-18's worker declared that exclusion. Your re-captures are the next change to those digests, so point that verdict's digest input at the frozen round-2 set (`__tests__/fe-s-22/round2-captures.frozen.json`) and move it whole.

### ACCEPTANCE

<criterion id="F32-AC1" cell_refs="FE-s-32" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F32-AC1` -- the whole portal typechecks.

<criterion id="F32-AC2" cell_refs="FE-s-32" drives="network"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts</invocation><expect>HOLDINGS UNDER THE GATE, IN A BROWSER: 4 of 4(?![0-9])</expect></criterion>
`F32-AC2` -- **the arm the ruling exists for.** In a real browser, through the dev server: the observed map (READY) renders the body; the target map (UNCERTAIN) renders the body; the missing-attribution map (PARTIAL) renders the body; and a no-answer map you write inside `__tests__/fe-s-32/` renders the panel. **PRECONDITION: a dev server**, declared in the test's own output and read through FE-s-27's helper; absent, it reports SKIPPED, never FAILED. Run the page under NODE.

<criterion id="F32-AC3" cell_refs="FE-s-32" drives="network"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts</invocation><expect>PARTIAL: CLASSIFICATION GAP SHOWN AS UNKNOWN</expect></criterion>
`F32-AC3` -- read from the rendered page: the unattributed holdings are shown, and the gap is labelled as unknown. Same precondition.

<criterion id="F32-AC4" cell_refs="FE-s-32" drives="network"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts</invocation><expect>UNCERTAIN: MODEL REVISION STATED AS UNNAMED</expect></criterion>
`F32-AC4` -- read from the rendered page: the target weights are shown, and the unnamed model revision is stated. Same precondition.

<criterion id="F32-AC5" cell_refs="FE-s-32" drives="network"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts</invocation><expect>CLAIMED FIELD PRESENT IN THE RENDERED DOM: (\d+) of \1(?![0-9])</expect></criterion>
`F32-AC5` -- the mechanical half of (a): for each answer-bearing Holdings capture, the DOM of the real render carries the field its claim declares, read against FE-s-22's claims model unedited. The test prints each capture, its claimed fields and what it found. Same precondition.

<criterion id="F32-AC6" cell_refs="FE-s-32" drives="network"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts</invocation><expect>PIE LABELS INSIDE THE CHART: (\d+) of \1(?![0-9])</expect></criterion>
`F32-AC6` -- W1-S35, read from the real render at 390 and 1440: every pie label's bounding box lies inside its chart's. Same precondition.

<criterion id="F32-AC7" cell_refs="FE-s-32" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-22/capture-hash.test.ts</invocation><expect>DISTINCTION VERDICT DIGESTS: frozen round-2 set</expect></criterion>
`F32-AC7` -- the freeze: the DISTINCTION verdict reads the frozen digests, printed by the test. Every other FE-s-22 assertion stays as written.

<criterion id="F32-AC8" cell_refs="FE-s-32" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-7 src/pages/InvestorReporting/__tests__/fe-s-10 src/pages/InvestorReporting/__tests__/fe-s-22 src/pages/InvestorReporting/__tests__/fe-s-26 src/pages/InvestorReporting/__tests__/fe-s-32</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F32-AC8` -- the Holdings suites stay green: fe-s-10's LOADING negative control is still a panel, and fe-s-26 is re-pointed as the bounds say. **PRECONDITION: none required** -- your browser test reports SKIPPED without a server. Record which way you ran it.

<criterion id="F32-AC9" cell_refs="FE-s-32" judgment="true" drives="none"/>
`F32-AC9` -- **(a), graded at L9 from your captures:** each Holdings capture renders the field its claim declares, and a reader can tell a qualified holdings answer from a complete one. RECORD; NO VERDICT.

<expected_criteria>F32-AC1, F32-AC2, F32-AC3, F32-AC4, F32-AC5, F32-AC6, F32-AC7, F32-AC8, F32-AC9</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **CONSUME THE PREDICATE, DO NOT COPY IT.** FE-s-30 built it in `state/availability.ts`. Read it; never edit it.
- ⛔ **THE CLAIMS MODEL IS NOT EDITED** -- ruling I rejects (b). If a claim cannot be drawn under the gate, that is a row with the measurement.
- ⛔ **TWO TESTS OF OTHER CELLS ARE YOURS, EACH FOR ONE PURPOSE.**
  - `__tests__/fe-s-26/renders-differently.test.ts` classifies Holdings renders as status panels, which ruling I overturns for PARTIAL and UNCERTAIN. Change only those classifications, cite ruling I beside each, and show both ways.
  - `__tests__/fe-s-22/capture-hash.test.ts` is yours for the DISTINCTION verdict's digest input only. Move that verdict whole; every other assertion stays as written.
- ⛔ **CAPTURES GO TO YOUR OWN DELIVERABLES FOLDER.** FE-s-18's folder and its manifest are complete and read by other cells' tests; you never write there.
- ⛔ **`scripts/ui-smoke.mjs` IS NOT YOURS.** Drive the browser from your own test, under node.
- **The precondition is declared, never silent** (ruling C).
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`, ON A WORKTREE-LOCAL VITE CACHE (AMENDMENT on rows W1-S56 and W1-S57, 2.0.0_SA_COO~F, before this order was cut): write `__tests__/fe-s-32/vite.worktree.config.ts`, which imports the portal's `vite.config.ts` and `mergeConfig`s ONLY `cacheDir`, set to `<WS>/.scratch/vite-cache-fe-s-32` (derived from the config file's own location, never a hardcoded drive), and launch `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <a free port> --strictPort --config src/pages/InvestorReporting/__tests__/fe-s-32/vite.worktree.config.ts`. Vite's default cache is `node_modules/.vite`, which through the junction is the MAIN checkout's and is rebuilt for every dev server on the box (W1-S56). If vite refuses the override, file a row with the measurement and launch without it. Export `IRPT_FE_DEV_PORT` for EVERY `bun test` run you make -- your own server's port while it is up, a port you have measured closed while it is down -- and NEVER leave it unset: the helper's default 5181 can be another seat's server, so an unset run can grade someone else's page (W1-S57). **Kill the server before your final report.** Say which criteria were measured with it up and which with it down.
- ⚠ **`chromium.launch` fails under bun on this box**; the identical launch under node returns in seconds.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W2-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/
portal/src/pages/InvestorReporting/__tests__/fe-s-26/renders-differently.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-22/capture-hash.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-32/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.5 @a4ac61a1cf, cell `FE-s-32`.
<owned_cells>FE-s-32</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F32-AC1` .. `F32-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-32.holdings-under-the-gate.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F32-AC1,F32-AC2,F32-AC3,F32-AC4,F32-AC5,F32-AC6,F32-AC7,F32-AC8,F32-AC9` BEFORE the `complete` flip. `F32-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9, with the capture files it is graded from. Result file `holdings-under-the-gate.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the gate: RUN by the issuer at portal DEV c2eb8eb4 -- HoldingsTab.tsx:90 READY-only.
W1-S35: RUN -- DrillTree.tsx:194 outerRadius={100}.
overturned tests: RUN -- fe-s-26/renders-differently.test.ts:82-83 classifies status panels (granted); fe-s-10/tabs-mounted.test.ts:106 negative control is LOADING (no snapshot seeded), stays a panel.
the maps: RUN -- FE-s-26's Holdings statuses: observed READY, target UNCERTAIN, missing-attribution PARTIAL; the parentless tree is FE-s-33's, which lands before this cell is seated.
lane: the <paths> block IS the grant; captures to this worker's own deliverables folder.
</preflight>

Seating: slot ~2; wave C -- seated only after BOTH FE-s-30 and FE-s-33 are drained, on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the pair is cut (row S26).
