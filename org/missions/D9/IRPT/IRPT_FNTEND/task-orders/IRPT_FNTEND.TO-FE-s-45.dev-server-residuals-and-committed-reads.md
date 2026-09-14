# TO IRPT_FNTEND.TO-FE-s-45 -- RULING U's residuals, and a criterion that says committed reads the committed blob

<to_id>IRPT_FNTEND.TO-FE-s-45</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~1</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-14</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (FIXTURES AND EVIDENCE) | **Decomp cell:** `FE-s-45` (round 7, v0.7 @0ad0ea1fa9) | **outcome_ref:** FWD-1, FWD-11 (evidence) | **depends_on:** none | **slot:** ~1 | **rows:** C-S91 (W1-S63, W1-S64, W1-S65), C-S90 (W5-S7)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-45` -- **one server per worktree left three residuals, and one criterion still grades the working copy where it says committed.** This is `1.0.0_SA_CTO` RULING U's residuals and RULING AC (round-6 analysis @4713211d87 s.3). 3.0.0_SA_CVO graduated them as C-S91 and C-S90.

Measured by the issuer at portal DEV 35797660:
- **W1-S63.** vite's config loader writes a transient bundled config under `node_modules/.vite-temp`, through the junction and into the MAIN checkout's `node_modules`. No config setting moves it. `package.json:13` reads `"dev": "vite"`, and the dev script is the one lever, so it is granted.
- **W1-S64.** `__tests__/fe-s-19/mounted-from-wire.test.ts:56` still reads *"`../fe-s-27/_dev-server.ts` -- environment first, documented default second."* RULING U removed that default.
- **W1-S65, and the census found FOUR, not the two the row names.** Per-cell vite overrides that send the cache somewhere other than FE-s-38's by-config location:
  - `__tests__/fe-s-31/vite.worktree.config.mjs`
  - `__tests__/fe-s-32/vite.worktree.config.ts`
  - `__tests__/fe-s-39/vite.worktree.config.mjs`
  - `__tests__/fe-s-40/vite.worktree.config.mjs`
  Each carries `cacheDir`. Each is referenced only by its own header comment; no test or driver imports it. FE-s-38's `fe-s-38/resolve-config.mjs` and `isolation.test.ts` READ the config; they are not overrides and are not yours.
- **W5-S7.** `__tests__/fe-s-41/one-writer.test.ts` F41-AC5 reads the maps from the working copy (`readFileSync` at `:81`), while its criterion says "read from the committed frozen map". JSON parsing ignores EOL, so no checkout turns it red. But it would grade an uncommitted in-place edit as committed. RULING AC: a criterion that reads a file reads `git cat-file blob HEAD:<path>`, or says why it reads the working copy.

**THE REMEDY:**
- The dev script loads vite's config without writing through the junction.
- fe-s-19's comment says what the helper now does.
- The four overrides are retired.
- F41-AC5 reads the committed blob.

### ACCEPTANCE

<criterion id="F45-AC1" cell_refs="FE-s-45" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F45-AC1` -- the whole portal typechecks after the four overrides are removed.

<criterion id="F45-AC2" cell_refs="FE-s-45" drives="network"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-45/residuals.test.ts</invocation><expect>DEV SCRIPT WRITES NOTHING THROUGH THE JUNCTION: yes</expect></criterion>
`F45-AC2` -- W1-S63.
- The test starts the portal's OWN `dev` script on a port it has measured closed, waits until the server answers, then stops it.
- It reads `<WS>/portal/node_modules/.vite-temp` (through the junction) before and after, and prints both.
- A positive control shows the old script DOES write there.

<criterion id="F45-AC3" cell_refs="FE-s-45" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-45/residuals.test.ts</invocation><expect>PER-CELL VITE OVERRIDES REMAINING: 0 of 4(?![0-9])</expect></criterion>
`F45-AC3` -- W1-S65, read from the COMMITTED tree (`git ls-tree -r HEAD`), so an uncommitted deletion cannot pass it.

<criterion id="F45-AC4" cell_refs="FE-s-45" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-45/residuals.test.ts</invocation><expect>fe-s-19 NAMES NO DEFAULT PORT: yes</expect></criterion>
`F45-AC4` -- W1-S64, read from the committed blob of `fe-s-19/mounted-from-wire.test.ts`.

<criterion id="F45-AC5" cell_refs="FE-s-45" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-41/one-writer.test.ts</invocation><expect>F41-AC5 READS THE COMMITTED BLOB: 5 of 5(?![0-9])</expect></criterion>
`F45-AC5` -- W5-S7. F41-AC5's maps are read with `git cat-file blob HEAD:<path>`. Add a seeded control: an uncommitted in-place edit that names `perf-9` must NOT move the verdict.

<criterion id="F45-AC6" cell_refs="FE-s-45" drives="network"><invocation>cd <WS>/portal && timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-19/mounted-from-wire.test.ts</invocation><expect>BODIES MOUNTED: 2 of 2(?![0-9])</expect></criterion>
`F45-AC6` -- the changed dev script, exercised end to end. **PRECONDITION: your own dev server, started with `bun run dev` under the new script** from `<WS>/portal`.

<criterion id="F45-AC7" cell_refs="FE-s-45" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F45-AC7` -- **the whole-suite census of record**, with `IRPT_FE_DEV_PORT` exported to a port you have measured closed.

<criterion id="F45-AC8" cell_refs="FE-s-45" judgment="true" drives="none"/>
`F45-AC8` -- graded at L9: RULING U leaves no residual, and F41-AC5 grades what is committed. RECORD; NO VERDICT.

<expected_criteria>F45-AC1, F45-AC2, F45-AC3, F45-AC4, F45-AC5, F45-AC6, F45-AC7, F45-AC8</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **`package.json` IS YOURS FOR THE `dev` SCRIPT ONLY.**
  - Your diff of it must be exactly the one `dev` line. Paste that diff into the result file.
  - The main portal checkout carries ANOTHER SEAT'S uncommitted edit to `package.json`'s `overrides` block. Never touch that block, and never copy that edit into your worktree.
  - Choose the mechanism from the vite that is installed (`node_modules/vite`, its `--help` and its own docs), and say which one and why.
- ⛔ **THE FOUR OVERRIDES ARE RETIRED BY DELETION** (`git -C <WS>/portal rm <each file>`).
  - Before deleting, census every reference to them across `<WS>/portal/src` and `<WS>/portal/scripts` and print the denominator.
  - A reference outside the four files themselves is a BLOCKING row, never an edit.
- ⛔ **`fe-s-19/mounted-from-wire.test.ts`: the comment at `:56` only.** `fe-s-41/one-writer.test.ts`: F41-AC5's read, and its control, only. Cite RULING U or RULING AC beside each change.
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F45-AC7). A red test outside your grant is a BLOCKING row with the list, never an edit.
- ⛔ **NOT YOURS:** `fe-s-27/` and `fe-s-38/` (FE-s-38's, drained); every other file in the four override folders (FE-s-42 changes fe-s-32's and fe-s-40's tests and drivers this round); `scripts/ui-smoke.mjs`.
- **RULING AC.** Every file your tests inspect is read as the committed blob or tree, or the test states why it reads the working copy. F45-AC2 reads the working tree deliberately: the defect is a write to it.
- **Servers.** FE-s-38 has drained.
  - Launch your server with the NEW script, `/c/Users/AndrewBerman/.bun/bin/bun run dev --port 5261 --strictPort`, from `<WS>/portal`, after measuring 5261 closed. A closed loopback port refuses in about 0.3 to 2 s here, so any probe timeout must exceed 2 s.
  - Export `IRPT_FE_DEV_PORT` on EVERY `bun test` run: 5261 while your server is up, and a port you have measured closed while it is down. Never leave it unset. Sibling slots use 5263; never touch it.
  - Browser tests run chromium under NODE. **Kill the server before your final report.**
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed or deleted, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/package.json
portal/src/pages/InvestorReporting/__tests__/fe-s-19/mounted-from-wire.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-31/vite.worktree.config.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-32/vite.worktree.config.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-39/vite.worktree.config.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-40/vite.worktree.config.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-41/one-writer.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-45/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.7 @0ad0ea1fa9, cell `FE-s-45`.
<owned_cells>FE-s-45</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F45-AC1` .. `F45-AC8`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~1/IRPT_FNTEND.TO-FE-s-45.dev-server-residuals-and-committed-reads.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F45-AC1,F45-AC2,F45-AC3,F45-AC4,F45-AC5,F45-AC6,F45-AC7,F45-AC8` BEFORE the `complete` flip. `F45-AC8` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `dev-server-residuals-and-committed-reads.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round (round-6 analysis s.1, no addendum).
the dev script: RUN by the issuer at portal DEV 35797660 -- package.json:13 "dev": "vite"; the main checkout carries another seat's uncommitted overrides-block edit (+2/-1).
the stale comment: RUN -- fe-s-19/mounted-from-wire.test.ts:56 "environment first, documented default second."
the overrides: RUN -- cacheDir in __tests__ = 6 files; minus fe-s-38's two readers = 4 overrides (fe-s-31 .mjs, fe-s-32 .ts, fe-s-39 .mjs, fe-s-40 .mjs), each referenced only by its own header.
the committed read: RUN -- fe-s-41/one-writer.test.ts readFileSync at :81 feeds F41-AC5.
lane: the <paths> block IS the grant; fe-s-27/, fe-s-38/, the other files in the override folders and scripts/ui-smoke.mjs excluded.
</preflight>

Seating: slot ~1; one wave -- round 7 has no dependency edge, seated on a fresh worktree pair cut from HEAD with the `<status>` flip committed BEFORE the pair is cut (row S26). DRAIN HOLD (decomp R7.8): the main portal checkout's uncommitted package.json edit belongs to another seat, and git refuses a merge that touches a locally modified file, so this order's portal drain waits on that edit's owner.
