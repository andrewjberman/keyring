# TO IRPT_FNTEND.TO-FE-s-42 -- RULING W at every site it names, and no test rewrites committed evidence

<to_id>IRPT_FNTEND.TO-FE-s-42</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~3</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-14</issued_date>
<status>staged</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F6, F7; CONTRACTS consumed) | **Decomp cell:** `FE-s-42` (round 7, v0.7 @0ad0ea1fa9) | **outcome_ref:** FWD-5, FWD-6 | **depends_on:** none | **slot:** ~3 | **rows:** C-S92 (W3-S29, W3-S30, W2-S33, W3-S31)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-42` -- **RULING W was applied on Holdings only.** Two further sites rename or print bare what the document did not name, and two browser tests rewrite committed evidence on every run. This is `1.0.0_SA_CTO` RULING Z (round-6 analysis @4713211d87 s.3). It carries the F39-AC10 FAIL graded by 3.0.0_SA_CVO at L9 (record @3d8fda2d73).

Measured by the issuer at portal DEV 35797660:
- **W3-S29 (the F39-AC10 FAIL).**
  - `contracts/adapt.ts:585` builds the DIRECTORY cohort's advisory as `ADVISORY_FOR_WIRE[wire.cohort.advisory_status] ?? 'unknown'`. That renames an out-of-enum token onto the producer's own UNKNOWN.
  - The Holdings path already carries it verbatim as `{ outOfEnum: token }` (`advisoryFromWire`, `:464-466`).
  - `CohortValue` (`contracts/index.ts:310`) is shared by three axes: supervision, billing and advisory.
  - A census of `CohortFact` values outside `__tests__/` finds two consumers: `contracts/validate.ts:164-171` and `header/ScopeSummary.tsx:79`. The latter renders `{c.axis}: {c.value}` as a string.
  - No test under `__tests__/` asserts the directory cohort's advisory: the word "cohort" appears in 2 files there, a netlog and `fe-s-32/holdings-no-answer.json`.
  - No emitter sends an out-of-enum directory advisory today, so your test builds its own wire body.
- **W3-S30.** `contracts/validate.ts:448` pins the advisory: `oneOf(c, cp, 'advisory', ['advised', 'residual', 'unknown'], p)`.
- **W2-S33.** `export/ReceiptPanel.tsx:47` prints `Reason: <span className="ir-mono">{reasonCode}</span>` bare. FE-s-40's one rule for a code the contract does not name is `UNNAMED_REASON_CODE_WORDS` (`render/Page.tsx:95`), together with the named set in `render/Page.tsx`'s marked region.
- **W3-S31, and the census found a second writer of the same class.** Two browser tests write their captures into the COMMITTED deliverables folder `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/` on every run, so any later cell that re-runs them dirties a folder outside its grant:
  - `__tests__/fe-s-32/holdings-in-a-browser.test.ts:68` with `holdings-driver.mjs:197`, `:210`, `:224`;
  - `__tests__/fe-s-40/band-at-390.test.ts:52` with `band-driver.mjs:147`, `:154`, `:167`.
  Six tests name a deliverables folder; subtracting these two leaves four that only READ (fe-s-11 `census.test.ts`, fe-s-18 `manifest.test.ts`, fe-s-22 `capture-hash.test.ts`, fe-s-26 `not-defective.test.ts`). The four readers are not yours.

**THE REMEDY:** RULING W at every named site.
- An out-of-enum advisory reaches the DIRECTORY cohort verbatim and flagged: through adapt, `CohortValue` and `ScopeSummary`.
- `validate` accepts the flagged shape and still refuses an unflagged out-of-enum value.
- ReceiptPanel's reason line flags a code the contract does not name, through FE-s-40's rule.
- The two browser tests write their captures OUTSIDE every committed deliverables folder by default. They write into a committed folder only when the run names that folder explicitly.

### ACCEPTANCE

<criterion id="F42-AC1" cell_refs="FE-s-42" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F42-AC1` -- the whole portal typechecks.

<criterion id="F42-AC2" cell_refs="FE-s-42" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-42/every-site.test.ts</invocation><expect>OUT-OF-ENUM DIRECTORY ADVISORY -> VERBATIM AND FLAGGED IN THE HEADER: yes</expect></criterion>
`F42-AC2` -- W3-S29 and F39-AC10's clause at the directory site. A wire directory body whose `cohort.advisory_status` is out of enum goes through the real adapter into `ScopeSummary`'s rendered markup. The test prints the rendered cohort text.

<criterion id="F42-AC3" cell_refs="FE-s-42" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-42/every-site.test.ts</invocation><expect>IN-ENUM DIRECTORY ADVISORY UNCHANGED: 3 of 3(?![0-9])</expect></criterion>
`F42-AC3` -- the control. ADVISED, RESIDUAL and UNKNOWN render in the header exactly as at DEV 35797660, and the supervision axis is unchanged.

<criterion id="F42-AC4" cell_refs="FE-s-42" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-42/every-site.test.ts</invocation><expect>VALIDATE: FLAGGED OUT-OF-ENUM ACCEPTED, UNFLAGGED REFUSED: yes</expect></criterion>
`F42-AC4` -- W3-S30. `validate` accepts the carried shape and still refuses an unflagged value outside the enum.

<criterion id="F42-AC5" cell_refs="FE-s-42" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-42/every-site.test.ts</invocation><expect>RECEIPT REASON: UNNAMED CODE FLAGGED, NAMED CODE BARE: yes</expect></criterion>
`F42-AC5` -- W2-S33, through FE-s-40's one rule, imported and never re-typed.

<criterion id="F42-AC6" cell_refs="FE-s-42" drives="network"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts</invocation><expect>HOLDINGS UNDER THE GATE, IN A BROWSER: 4 of 4(?![0-9])</expect></criterion>
`F42-AC6` -- FE-s-32's browser arm still holds with its capture destination changed. **PRECONDITION: your own dev server.**

<criterion id="F42-AC7" cell_refs="FE-s-42" drives="network"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts</invocation><expect>CAPTURES OUTSIDE EVERY COMMITTED DELIVERABLES FOLDER: yes</expect></criterion>
`F42-AC7` -- W3-S31, on the same run. The test prints where its captures went. It reads `git status --porcelain` of the deliverables tree after the run and prints this line only when that tree is unchanged.

<criterion id="F42-AC8" cell_refs="FE-s-42" drives="network"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-40/band-at-390.test.ts</invocation><expect>CAPTURES OUTSIDE EVERY COMMITTED DELIVERABLES FOLDER: yes</expect></criterion>
`F42-AC8` -- the second writer of the class, same rule, same server.

<criterion id="F42-AC9" cell_refs="FE-s-42" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F42-AC9` -- **the whole-suite census of record**, with `IRPT_FE_DEV_PORT` exported to a port you have measured closed.

<criterion id="F42-AC10" cell_refs="FE-s-42" judgment="true" drives="none"/>
`F42-AC10` -- graded at L9: an out-of-enum advisory is shown verbatim and flagged at every use site, and F39-AC10's clause is re-graded at the directory site. RECORD; NO VERDICT.

<expected_criteria>F42-AC1, F42-AC2, F42-AC3, F42-AC4, F42-AC5, F42-AC6, F42-AC7, F42-AC8, F42-AC9, F42-AC10</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **ONE PURPOSE PER SHARED FILE.**
  - `contracts/adapt.ts`: the directory cohort's advisory at `:585` only.
  - `contracts/index.ts`: `CohortValue`, so the directory can carry a verbatim value, and nothing else.
  - `contracts/validate.ts`: the advisory pin and the cohort-value checks it needs, and nothing else.
  - `header/ScopeSummary.tsx`: how a cohort value renders.
  - `export/ReceiptPanel.tsx`: its reason line.
  - The two capture writers (test plus driver, in fe-s-32 and fe-s-40): the capture destination only.
- ⛔ **ONE RULE, NEVER A SECOND COPY.**
  - The out-of-enum flag words are `ADVISORY_OUT_OF_ENUM_WORDS` (`tabs/holdings/slices.ts:98`). The unnamed-code words and the named set are FE-s-40's, in `render/Page.tsx`.
  - Import both. `tabs/holdings/` and `render/Page.tsx` are NOT in your grant; if an import needs a change there, that is a BLOCKING row.
- ⛔ **RULING X -- THE CUT'S CENSUS NAMED THESE TESTS, EACH YOURS FOR THE CLAIMS RULING Z CHANGES ONLY:**
  - `__tests__/fe-s-1/fixtures.test.ts`, the one test that imports `validate`;
  - `__tests__/fe-s-9/receipt.test.ts` and `__tests__/fe-s-16/mounted-states.test.ts`, the tests that render ReceiptPanel.
  Cite RULING Z beside each change and show it both ways. Leave every other assertion in them.
- ⛔ **THE WHOLE-SUITE RUN IS STILL THE CENSUS OF RECORD** (F42-AC9). A red test outside your grant is a BLOCKING row with the list, never an edit.
- ⛔ **NOT YOURS:**
  - the four reader tests named above;
  - `fe-s-32/holdings-no-answer.json` and every fixture map (FE-s-41's, drained);
  - `fe-s-32/vite.worktree.config.ts` and `fe-s-40/vite.worktree.config.mjs` (FE-s-45's, which retires them);
  - `package.json`.
- **RULING AC.** F42-AC7 and F42-AC8 read the WORKING TREE, and that is deliberate: the defect is dirt in the working tree. Every other file your tests inspect is read as the committed blob (`git cat-file blob HEAD:<path>`), or the test says why it reads the working copy.
- **Servers.** FE-s-38 has drained, so vite caches inside the worktree by config.
  - Launch with `/c/Users/AndrewBerman/.bun/bin/bun run dev --port 5263 --strictPort` from `<WS>/portal`, after measuring 5263 closed. A closed loopback port refuses in about 0.3 to 2 s here, so any probe timeout must exceed 2 s.
  - Export `IRPT_FE_DEV_PORT` on EVERY `bun test` run: 5263 while your server is up, and a port you have measured closed while it is down. Never leave it unset. Sibling slots use 5261; never touch it.
  - Browser tests run chromium under NODE. **Kill the server before your final report.**
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W3-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/contracts/index.ts
portal/src/pages/InvestorReporting/contracts/validate.ts
portal/src/pages/InvestorReporting/header/ScopeSummary.tsx
portal/src/pages/InvestorReporting/export/ReceiptPanel.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-32/holdings-driver.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-40/band-at-390.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-40/band-driver.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-1/fixtures.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-9/receipt.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-16/mounted-states.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-42/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.7 @0ad0ea1fa9, cell `FE-s-42`.
<owned_cells>FE-s-42</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F42-AC1` .. `F42-AC10`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-42.advisory-verbatim-at-every-site.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F42-AC1,F42-AC2,F42-AC3,F42-AC4,F42-AC5,F42-AC6,F42-AC7,F42-AC8,F42-AC9,F42-AC10` BEFORE the `complete` flip. `F42-AC10` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `advisory-verbatim-at-every-site.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round (round-6 analysis s.1, no addendum).
the directory site: RUN by the issuer at portal DEV 35797660 -- adapt.ts:585 ADVISORY_FOR_WIRE[...] ?? 'unknown'; advisoryFromWire at :464-466; CohortValue at contracts/index.ts:310.
the cohort consumers: RUN -- CohortFact value outside __tests__ read at validate.ts:164-171 and ScopeSummary.tsx:79; "cohort" in __tests__ = 2 files (fe-s-17 netlog, fe-s-32/holdings-no-answer.json), none asserting the directory advisory.
the pin and the reason line: RUN -- validate.ts:448 oneOf advised/residual/unknown; ReceiptPanel.tsx:47 bare; UNNAMED_REASON_CODE_WORDS at render/Page.tsx:95.
the capture writers: RUN -- 6 tests name a deliverables folder; 2 write into ~2's (fe-s-32 :68 with its driver; fe-s-40 :52 with its driver); 4 only read.
RULING X census: RUN -- tests importing validate = fe-s-1/fixtures.test.ts; tests rendering ReceiptPanel = fe-s-9/receipt.test.ts, fe-s-16/mounted-states.test.ts; each granted by name.
lane: the <paths> block IS the grant; tabs/holdings/, render/Page.tsx, every fixture map, the vite overrides and package.json excluded.
</preflight>

Seating: slot ~3; one wave -- round 7 has no dependency edge, seated on a fresh worktree pair cut from HEAD with the `<status>` flip committed BEFORE the pair is cut (row S26).
