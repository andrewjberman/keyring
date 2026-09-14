# TO IRPT_FNTEND.TO-FE-s-38 -- one server per worktree, and every browser verdict names it

<to_id>IRPT_FNTEND.TO-FE-s-38</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-38` (round 6, v0.6 @d4d8ae6f9a) | **outcome_ref:** FWD-1, FWD-6 (evidence) | **depends_on:** FE-s-37 (sequencing: the bound checker must be in your worktree) | **slot:** ~1 | **rows:** C-S81, W1-S56, W1-S57, W5-S1, W5-S4

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-38` -- **a browser verdict graded whatever answered on the default port, and once it was another project's page.** `1.0.0_SA_CTO` RULING U (round-5 analysis @942e4ff992 s.3), graduated by 3.0.0_SA_CVO as C-S81.

Measured by the issuer at portal DEV 741bb54b:
- The fe-s-27 helper defaults its port: `DEFAULT_DEV_PORT = '5181'` (`__tests__/fe-s-27/_dev-server.ts:40`); `devPort()` reads `IRPT_FE_DEV_PORT` first and the default second (`:43-45`). Its own `__tests__/fe-s-27/precondition.test.ts` pins that default (`:40`, `:216`, `:251`).
- Row W5-S1: fe-s-19's browser criteria graded a DSGN worktree's vite on 5181 (0 of 2, 0 of 2). Row W1-S57: a server the worker did not start answered 5181.
- `vite.config.ts` sets no `cacheDir`, so vite caches in `node_modules/.vite` -- through the junction, the MAIN checkout's cache, rebuilt by every worktree's server (W1-S56, W5-S4). `.gitignore:17` already ignores `.vite`.
- Both tsconfigs write their build info through the same junction: `"tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo"` (`tsconfig.app.json:3`) and `./node_modules/.tmp/tsconfig.node.tsbuildinfo` (`tsconfig.node.json:3`).
- F35-AC6's round-5 deciding run met no server on 5181 and SKIPPED F19-AC4/AC5 by name (`envelope-refusal.result.md:51`); its only mounted evidence is a supplementary run. **That browser arm is carried to this cell** and re-run on this worktree's own server; it decides F35's "never seen mounted" qualification.

**THE REMEDY:** the helper refuses without `IRPT_FE_DEV_PORT` or a port derived from its own worktree -- never a fixed default. vite's `cacheDir` and `tsbuildinfo` live inside the worktree **by config**, never through the junction, so no cell needs a per-cell override again. Every browser run's precondition line names its port AND the worktree it served from.

### ACCEPTANCE

<criterion id="F38-AC1" cell_refs="FE-s-38" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F38-AC1` -- the whole portal typechecks with the tsconfigs changed.

<criterion id="F38-AC2" cell_refs="FE-s-38" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-38/isolation.test.ts</invocation><expect>HELPER WITH NO PORT GIVEN AND NONE DERIVABLE: REFUSED</expect></criterion>
`F38-AC2` -- the helper refuses rather than default; the test also prints the port it derives from a real worktree when one is derivable.

<criterion id="F38-AC3" cell_refs="FE-s-38" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-38/isolation.test.ts</invocation><expect>VITE cacheDir INSIDE THE WORKTREE, NOT THROUGH THE JUNCTION: yes</expect></criterion>
`F38-AC3` -- read from vite's OWN resolved config (its `resolveConfig`), never by reading the file's text; the test prints the resolved path.

<criterion id="F38-AC4" cell_refs="FE-s-38" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-38/isolation.test.ts</invocation><expect>tsbuildinfo INSIDE THE WORKTREE, NOT THROUGH THE JUNCTION: 2 of 2(?![0-9])</expect></criterion>
`F38-AC4` -- both tsconfigs, each resolved path printed.

<criterion id="F38-AC5" cell_refs="FE-s-38" drives="network"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/mounted-from-wire.test.ts</invocation><expect>BODIES MOUNTED: 2 of 2(?![0-9])</expect></criterion>
`F38-AC5` -- **F35-AC6's carried browser arm, F19-AC4, re-run on THIS worktree's own server** after FE-s-35's refusal of no-identity bodies (portal 850d7718). **PRECONDITION: your own dev server**, started from `<WS>/portal` under the new config.

<criterion id="F38-AC6" cell_refs="FE-s-38" drives="network"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/mounted-from-wire.test.ts</invocation><expect>UNCERTAIN WITHOUT A WIRE STATE: 2 of 2(?![0-9])</expect></criterion>
`F38-AC6` -- F19-AC5 on the same run and server.

<criterion id="F38-AC7" cell_refs="FE-s-38" drives="network"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/mounted-from-wire.test.ts</invocation><expect>PRECONDITION: dev server on http://localhost:[0-9]+ -- MET[^\n]*worktree</expect></criterion>
`F38-AC7` -- the same run's precondition line names the port and the worktree it served from (RULING U's recording half, closed at the source).

<criterion id="F38-AC8" cell_refs="FE-s-38" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F38-AC8` -- **the whole-suite census of record**, with `IRPT_FE_DEV_PORT` exported to a port you have measured closed. Under the new helper a browser test with no port must REFUSE loudly or SKIP by name -- say which, and prove it on this run.

<criterion id="F38-AC9" cell_refs="FE-s-38" judgment="true" drives="none"/>
`F38-AC9` -- graded at L9: every browser verdict names the server it hit, and F35's ENVELOPE_BODY qualification ("never seen mounted") is decided by AC5 and AC6. RECORD; NO VERDICT.

<expected_criteria>F38-AC1, F38-AC2, F38-AC3, F38-AC4, F38-AC5, F38-AC6, F38-AC7, F38-AC8, F38-AC9</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **THE PORTAL ROOT FILES ARE SHARED BY EVERY DEV SERVER ON THIS BOX.** `vite.config.ts`, the two tsconfigs and `.gitignore` are yours for RULING U's purpose ONLY: `cacheDir` and `tsBuildInfoFile` inside the worktree, and the ignore entries they need. Change nothing else in them; say in the result file where the main checkout's cache and build info now live.
- ⛔ **`__tests__/fe-s-27/` IS YOURS**, including `precondition.test.ts`, which pins the default RULING U removes. Change only the claims the ruling changes, cite RULING U beside each, show each both ways.
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F38-AC8). Any test outside your grant that your change turns red is a BLOCKING row with the list, never an edit.
- ⛔ **`scripts/ui-smoke.mjs` IS NOT YOURS.** If it relies on the helper's default, that is a row.
- **Your own dev server runs under the config you write** -- no per-cell override. Export `IRPT_FE_DEV_PORT` on EVERY `bun test` run you make: your server's port while it is up, a port you have measured closed while it is down; never leave it unset. A closed loopback port answers after ~2 s on this box, so any probe timeout must exceed 2 s. Browser tests run chromium under NODE (under bun, chromium.launch fails here). **Kill the server before your final report.**
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/vite.config.ts
portal/tsconfig.app.json
portal/tsconfig.node.json
portal/.gitignore
portal/src/pages/InvestorReporting/__tests__/fe-s-27/
portal/src/pages/InvestorReporting/__tests__/fe-s-38/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.6 @d4d8ae6f9a, cell `FE-s-38`.
<owned_cells>FE-s-38</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F38-AC1` .. `F38-AC9`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-38.one-server-per-worktree.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F38-AC1,F38-AC2,F38-AC3,F38-AC4,F38-AC5,F38-AC6,F38-AC7,F38-AC8,F38-AC9` BEFORE the `complete` flip. `F38-AC9` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `one-server-per-worktree.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the helper: RUN by the issuer at portal DEV 741bb54b -- DEFAULT_DEV_PORT '5181' at _dev-server.ts:40; devPort() env then default at :43-45; precondition.test.ts pins it at :40, :216, :251.
the caches: RUN -- vite.config.ts sets no cacheDir; .gitignore:17 ignores .vite; tsBuildInfoFile ./node_modules/.tmp/ in tsconfig.app.json:3 and tsconfig.node.json:3.
the carried arm: RUN -- F35-AC6's deciding run skipped F19-AC4/AC5 by name (envelope-refusal.result.md:51); fe-s-19/mounted-from-wire.test.ts prints BODIES MOUNTED and UNCERTAIN WITHOUT A WIRE STATE.
lane: the <paths> block IS the grant; scripts/ui-smoke.mjs excluded.
</preflight>

Seating: slot ~1; wave B -- seated only after FE-s-37 is drained, on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the pair is cut (row S26).
