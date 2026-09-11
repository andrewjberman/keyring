# TO IRPT_FNTEND.TO-FE-s-14 -- the route reachable by a partner firm; the Global proof recut

<to_id>IRPT_FNTEND.TO-FE-s-14</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-11</issued_date>
<status>blocked</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F1, F11) | **Decomp cell:** `FE-s-14` (round 2, v0.2) | **outcome_ref:** FWD-1, FWD-11 | **depends_on:** `FE-s-13` | **slot:** ~2, queue position 2 | **slug rows:** W1-S10

---

## WORKER FACE

### THE CELL

`FE-s-14` -- no partner firm can reach `/investor-reporting`: `portal/src/lib/firmAccess.ts` `FIRM_ALLOWED_PATHS` lists four firms (49financial, inflection, cottonwood, demo) and `/investor-reporting` is in none, so `ProtectedRoute`'s firm-matrix guard bounces every firm session to `/market`. The CTO ruled this file IN SCOPE for exactly this: add `'/investor-reporting'` to the `49financial`, `inflection` and `cottonwood` sets and change nothing else in that file (demo is not onboarded; no other path; the header comment's "to onboard a new partner firm" note stays true).

Then recut the F10 proof on a REACHABLE route, with the wire smoke fixtures FE-s-13 left under `fixtures/smoke/`:
- a firm session (`ui-smoke --firm <id>`, which renders a partner session with `firmId` = that id) reaches `/investor-reporting` and renders the Holdings tab from a one-firm wire resolve-scope fixture for that firm (`fe-s-14-<firm>.json`, one per registry firm, each naming the page's whole needs);
- the firm sees only its own scope: the dropdown is absent when the catalogue has one entry; `?firm=global`, a persisted `'global'` and a forced selector value each resolve to that one firm (the FE-s-10 rule in `global/firms.ts`, unchanged); the header test prints `GLOBAL PATH: absent`;
- a non-registry firm id is still refused (`--firm nonregistry` lands on `/market`: ui-smoke prints `DID NOT LAND`);
- Global with two firms still renders (`fe-s-13-wire.json` or a two-firm copy).

No Global behaviour changes; no component is added. Edits under `global/` and `header/` only where the proof needs a test seam, stated in a row if so.

### ACCEPTANCE

<criterion id="F14-AC1" cell_refs="FE-s-14"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0</expect></criterion>
`F14-AC1` -- the whole portal typechecks.

<criterion id="F14-AC2" cell_refs="FE-s-14"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts</invocation><expect>ALLOWED: 3 of 3</expect></criterion>
`F14-AC2` -- `isPathAllowedForFirm('49financial' | 'inflection' | 'cottonwood', '/investor-reporting')` is true for all three.

<criterion id="F14-AC3" cell_refs="FE-s-14"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-14/allowlist.test.ts</invocation><expect>REFUSED: 2 of 2</expect></criterion>
`F14-AC3` -- the same call is false for `demo` and for an unknown id; the diff of `firmAccess.ts` against `edab15b5` adds exactly three lines (the test runs `git diff --numstat` and prints `FIRMACCESS DIFF: +3 -0`).

<criterion id="F14-AC4" cell_refs="FE-s-14"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-14_firm_49financial_1440.png --port <PORT> --width 1440 --firm 49financial --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-14-49financial.json --click Holdings --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Holdings</expect></criterion>
`F14-AC4` -- a 49 Financial session reaches the route and the Holdings tab renders.

<criterion id="F14-AC5" cell_refs="FE-s-14"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-14_firm_inflection_1440.png --port <PORT> --width 1440 --firm inflection --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-14-inflection.json --click Holdings --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Holdings</expect></criterion>
`F14-AC5` -- an Inflection session reaches the route.

<criterion id="F14-AC6" cell_refs="FE-s-14"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-14_firm_cottonwood_1440.png --port <PORT> --width 1440 --firm cottonwood --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-14-cottonwood.json --click Holdings --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Holdings</expect></criterion>
`F14-AC6` -- a Cottonwood session reaches the route.

<criterion id="F14-AC7" cell_refs="FE-s-14"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-14_firm_nonregistry_1440.png --port <PORT> --width 1440 --firm nonregistry --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-14-49financial.json; echo rc=$?</invocation><expect>DID NOT LAND</expect></criterion>
`F14-AC7` -- an unknown firm is still refused (lands on /market; the PNG shows Market Overview).

<criterion id="F14-AC8" cell_refs="FE-s-14"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-14/one-firm.test.ts</invocation><expect>GLOBAL PATH: absent</expect></criterion>
`F14-AC8` -- with a one-firm wire scope the rendered header carries no dropdown and `?firm=global`, a persisted `'global'` and a forced selector value each resolve to the single firm (the test enumerates the three candidates and prints each resolution).

<criterion id="F14-AC9" cell_refs="FE-s-14"><invocation>cd <WS>/portal && timeout 120 node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/fe-s-14_global_two_firms_1440.png --port <PORT> --width 1440 --fixtures src/pages/InvestorReporting/fixtures/smoke/fe-s-14-global.json --click Holdings --console "Maximum update depth"; echo rc=$?</invocation><expect>CLICKED: Holdings</expect></criterion>
`F14-AC9` -- the internal Global session with two firms still renders the tab.

<criterion id="F14-AC10" cell_refs="FE-s-14"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>0 fail</expect></criterion>
`F14-AC10` -- the whole Investor Reporting set is green.

<criterion id="F14-AC11" cell_refs="FE-s-14" judgment="true"/>
`F14-AC11` -- graded at L9 from the three firm PNGs and the Global PNG: a firm session sees only its own scope with no Global path; the internal user sees the catalogue. RECORD; NO VERDICT.

<expected_criteria>F14-AC1, F14-AC2, F14-AC3, F14-AC4, F14-AC5, F14-AC6, F14-AC7, F14-AC8, F14-AC9, F14-AC10, F14-AC11</expected_criteria>

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. `firmAccess.ts`: three added lines and nothing else. A path you need that is not named is a BLOCKING row on that criterion; never an override.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal` as in your identity line. Portal commit pathspec: `src/lib/firmAccess.ts src/pages/InvestorReporting/global/ src/pages/InvestorReporting/header/ src/pages/InvestorReporting/fixtures/smoke/ src/pages/InvestorReporting/__tests__/fe-s-14/`. Workspace records under org/ only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo.
- **Dev server.** `node_modules` is a junction; do not run `bun install`. Start once in the background from `<WS>/portal`: `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <PORT>`; use the port it prints; kill it before your final report. Routes without a leading slash.
- **Numbers.** 1440 is a test setup, not an acceptance value.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only. PNGs to your deliverables folder, named as the criteria name them.
- **Surprise.** ONE row per finding in `org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md`, id `IRPT_FNTEND-W2-S<k>` continuing from `IRPT_FNTEND-W2-S7` (read the file for the last W2 id; if it does not exist, create it with a one-line header and a fenced `json` array holding your row); never edit an existing row; keep working.
- Report push state as LOCAL.

<paths>
portal/src/lib/firmAccess.ts
portal/src/pages/InvestorReporting/global/
portal/src/pages/InvestorReporting/header/
portal/src/pages/InvestorReporting/fixtures/smoke/
portal/src/pages/InvestorReporting/__tests__/fe-s-14/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.2 @430c5fcb4a, cell `FE-s-14`.
<owned_cells>FE-s-14</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F14-AC1` .. `F14-AC11`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-14.firm-route-global-proof.proof_of_spec.json`
(phase `BUILD-GENERAL` -- AMENDED BY THE ISSUER at the FE-s-12 drain on row IRPT_FNTEND-W1-S15: the schema's phase enum has no BUILD member, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F14-AC1,F14-AC2,F14-AC3,F14-AC4,F14-AC5,F14-AC6,F14-AC7,F14-AC8,F14-AC9,F14-AC10,F14-AC11` BEFORE the `complete` flip. `F14-AC11` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `firm-route-global-proof.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- firmAccess.ts is a client-side allow-list read by ProtectedRoute; the entitlement grant is the counterpart's.
comp-adversary: RUN at L4 on PRD v0.6 (ADMITTED) -- carried.
firm matrix: RUN by the issuer -- FIRM_ALLOWED_PATHS 4 entries; /investor-reporting in 0 of 4 at edab15b5.
lane: the <paths> block IS the grant; firmAccess.ts is granted on the CTO's ruling 2 (ROUND_ANALYSIS.round1.md @0d57ceb2f9) for three lines; portal paths bind by reading; workspace paths bind mechanically.
</preflight>

Seating: slot ~2, queue position 2; seated when `FE-s-13` is terminal and drained (and `FE-s-17`, the slot's first order, is terminal), fresh worktree pair from HEAD.
