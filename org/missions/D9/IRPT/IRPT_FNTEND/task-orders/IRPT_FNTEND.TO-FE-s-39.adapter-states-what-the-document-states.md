# TO IRPT_FNTEND.TO-FE-s-39 -- the adapter never substitutes a value the document did not state

<to_id>IRPT_FNTEND.TO-FE-s-39</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~3</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-14</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F6, F7; CONTRACTS consumed) | **Decomp cell:** `FE-s-39` (round 6, v0.6 @d4d8ae6f9a) | **outcome_ref:** FWD-5, FWD-6 | **depends_on:** FE-s-37 (sequencing) | **slot:** ~3 | **rows:** C-S83 (W3-S22, W3-S25, W3-S26), W2-S29

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-39` -- **three places where the frontend shows something the document did not say.** `1.0.0_SA_CTO` RULING V (the business-date plane, under RULING R) and RULING W's W2-S29 (round-5 analysis @942e4ff992 s.3). One axis: the adapter hands the view what the document states -- no more, no less, and never a substitute.

Measured by the issuer at portal DEV 741bb54b:
- **W3-S26.** `readingFromValue(null)` returns fact `NULL` (`contracts/adapt.ts:161`), and `carryDocumentReading` (`:316`) applies it to VIEW documents. The view contract defines a null `businessAsOf` as "no clock" (`contracts/index.ts:147`), so a view document's null reads "Source date malformed" (`state/status.ts:332`, `:476`) -- 3 of 134 view documents, all in `fixtures/smoke/fe-s-3-loading.json`. **RULING V:** it renders as "no clock" -- the panel names the absence (RULING R), never "malformed". On the WIRE plane a null business date stays a producer defect and keeps reading malformed.
- **W3-S22.** `__tests__/fe-s-21/source-age.test.ts` builds its envelope from the status's `sourceAsOf` (`panelFor`, `:77-81`) and grades that AS_OF instant's age under the business-date label (`:171`) -- a test asserting the very mislabel RULING R removed. **RULING V:** the test asserts the document's own business date.
- **W3-S25 is ALREADY MET.** `businessDateOf` keys its provenance on `producerState` (`state/availability.ts:108`, FE-s-34 amendment 3, portal c6ee044e). This cell adds the guarding test; `state/availability.ts` is NOT in your grant.
- **W2-S29.** `ADVISORY_FOR_WIRE[...] ?? 'unknown'` (`contracts/adapt.ts:558`, `:865`) maps an out-of-enum `advisory_status` -- `'ADVISORY'`, emitted by `__tests__/fe-s-18/gen-fixtures.ts:317` into the observed and target Holdings maps -- to "unknown". On the READY observed answer Advisory reads "unknown" on 3 of 3 rows with nothing qualifying it (F32-AC9's qualification). **RULING W:** an out-of-enum value on a READY answer is shown VERBATIM and FLAGGED, never as "unknown". The enum itself is IRPT_BCKEND's (row IRPT_BCKEND-S52), not this cell's.

### ACCEPTANCE

<criterion id="F39-AC1" cell_refs="FE-s-39" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F39-AC1` -- the whole portal typechecks.

<criterion id="F39-AC2" cell_refs="FE-s-39" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-39/adapter-plane.test.ts</invocation><expect>VIEW DOCUMENT WITH A NULL businessAsOf -> ABSENCE NAMED, NOT MALFORMED: 3 of 3(?![0-9])</expect></criterion>
`F39-AC2` -- W3-S26, over the three view documents in `fe-s-3-loading.json` served through `FixtureAdapter`; the test prints each rendered string.

<criterion id="F39-AC3" cell_refs="FE-s-39" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-39/adapter-plane.test.ts</invocation><expect>WIRE NULL business_date STILL READS MALFORMED: yes</expect></criterion>
`F39-AC3` -- the control: a whole v1 body whose status carries a null `business_date` still reads malformed.

<criterion id="F39-AC4" cell_refs="FE-s-39" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-39/adapter-plane.test.ts</invocation><expect>businessDateOf PROVENANCE KEYS ON producerState: 2 of 2(?![0-9])</expect></criterion>
`F39-AC4` -- W3-S25's guard: a no-status document reports `document`, a status-carried date reports `status`.

<criterion id="F39-AC5" cell_refs="FE-s-39" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-21/source-age.test.ts</invocation><expect>F21 GRADES THE DOCUMENT'S BUSINESS DATE, NOT AN INSTANT: yes</expect></criterion>
`F39-AC5` -- W3-S22: the amended fe-s-21 check prints this line only when the age it grades is the business date's.

<criterion id="F39-AC6" cell_refs="FE-s-39" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-39/adapter-plane.test.ts</invocation><expect>OUT-OF-ENUM ADVISORY ON A READY ANSWER -> VERBATIM AND FLAGGED: 3 of 3(?![0-9])</expect></criterion>
`F39-AC6` -- W2-S29 on the observed map's three rows, through the real adapter into the rendered Holdings markup.

<criterion id="F39-AC7" cell_refs="FE-s-39" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-39/adapter-plane.test.ts</invocation><expect>IN-ENUM ADVISORY UNCHANGED: yes</expect></criterion>
`F39-AC7` -- the control: `ADVISED`, `RESIDUAL` and `UNKNOWN` render exactly as before.

<criterion id="F39-AC8" cell_refs="FE-s-39" drives="network"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts</invocation><expect>HOLDINGS UNDER THE GATE, IN A BROWSER: 4 of 4(?![0-9])</expect></criterion>
`F39-AC8` -- FE-s-32's browser arm still holds with the advisory rendered verbatim, in a real browser on your own server. **PRECONDITION: your own dev server** (the `servers` bound below).

<criterion id="F39-AC9" cell_refs="FE-s-39" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F39-AC9` -- **the whole-suite census of record**, with `IRPT_FE_DEV_PORT` exported to a port you have measured closed.

<criterion id="F39-AC10" cell_refs="FE-s-39" judgment="true" drives="none"/>
`F39-AC10` -- graded at L9: nothing the adapter hands the view says more, or less, than the document did. RECORD; NO VERDICT.

<expected_criteria>F39-AC1, F39-AC2, F39-AC3, F39-AC4, F39-AC5, F39-AC6, F39-AC7, F39-AC8, F39-AC9, F39-AC10</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **ONE PURPOSE PER SHARED FILE.** `contracts/adapt.ts`: the view plane's null rule inside `carryDocumentReading`, and the out-of-enum advisory at the `ADVISORY_FOR_WIRE` use sites -- nothing else. `contracts/index.ts`: the advisory view type, so a verbatim value can travel -- nothing else. `state/status.ts`: the absence wording, if one is needed -- nothing else. `tabs/holdings/`: the flag's display.
- ⛔ **ONE RULE, NEVER A SECOND COPY.** The view plane's "no clock" and the wire plane's "malformed" are the two contracts' own definitions; state in the result file where each is decided, and prove the wire control (AC3) unchanged.
- ⛔ **`__tests__/fe-s-21/source-age.test.ts` IS YOURS FOR W3-S22 ONLY**: re-point its graded age to the document's business date, cite RULING V, show it both ways, leave every other assertion.
- ⛔ **NOT YOURS:** `state/availability.ts` (W3-S25 is met; guard it by test), `tabs/reporting/AnswerStatus.tsx`, `tabs/StatusPanel.tsx`, `render/Page.tsx` (FE-s-40's), and every fixture map and generator (FE-s-41's -- the `'ADVISORY'` token stays in the maps, since it is what exercises your flag).
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F39-AC9). Any test outside your grant that your change turns red is a BLOCKING row with the list, never an edit.
- **servers** (until FE-s-38 drains): run vite on a worktree-local cache through `__tests__/fe-s-39/vite.worktree.config.mjs`, which LOADS the portal config at runtime and merges only `cacheDir` to `<WS>/.scratch/vite-cache-fe-s-39` (a `.ts` override under `src/` breaks the portal typecheck -- rows W1-S59, W2-S28); launch `/c/Users/AndrewBerman/.bun/bin/bun run dev --port <a free port> --strictPort --config src/pages/InvestorReporting/__tests__/fe-s-39/vite.worktree.config.mjs`. Export `IRPT_FE_DEV_PORT` on EVERY `bun test` run -- your server's port while up, a measured-closed port while down; never unset. Browser tests run chromium under NODE. **Kill the server before your final report.**
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W3-S<k>`. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- ⛔ **AMENDMENT 1 (2.0.0_SA_COO~F, 2026-09-14, on rows W3-S27 and W3-S28; criteria unchanged).** Two tests outside the first grant assert exactly what RULINGS V and W remove, and each is now yours for ONE purpose:
  - `__tests__/fe-s-34/no-status.test.ts`: F34-AC9's path 1 NULL arm (the VIEW plane) only. It expects the absence wording RULING V names in place of `SOURCE_DATE_MALFORMED`. Path 2, the WIRE arm, stays exactly as written and must still read malformed. Cite RULING V beside the change and show the arm both ways.
  - `__tests__/fe-s-32/holdings-in-a-browser.test.ts`: F32-AC5's classification reader only (the `ADVISORY` list and `CLAIM_READERS.classification`). It accepts an Advisory cell that shows an out-of-enum value VERBATIM AND FLAGGED (RULING W), and still rejects an out-of-enum value shown without the flag. Cite RULING W and prove both arms. Change nothing else in that file. `holdings-no-answer.json` beside it is FE-s-41's, not yours.
  - F39-AC8's run must end with 0 fail, not only print its anchor; report its pass and fail counts. The whole suite (F39-AC9) stays the census of record.
  - FE-s-38 has DRAINED into portal DEV, and DEV is merged into your portal branch. vite now caches inside the worktree by config, so run `bun run dev` directly on a measured-free port with `--strictPort`; the `.mjs` override is no longer needed. Export `IRPT_FE_DEV_PORT` on every `bun test` run, as before.

<paths>
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/contracts/index.ts
portal/src/pages/InvestorReporting/state/status.ts
portal/src/pages/InvestorReporting/tabs/holdings/
portal/src/pages/InvestorReporting/__tests__/fe-s-21/source-age.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-39/
portal/src/pages/InvestorReporting/__tests__/fe-s-34/no-status.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-32/holdings-in-a-browser.test.ts
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.6 @d4d8ae6f9a, cell `FE-s-39`.
<owned_cells>FE-s-39</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F39-AC1` .. `F39-AC10`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-39.adapter-states-what-the-document-states.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F39-AC1,F39-AC2,F39-AC3,F39-AC4,F39-AC5,F39-AC6,F39-AC7,F39-AC8,F39-AC9,F39-AC10` BEFORE the `complete` flip. `F39-AC10` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `adapter-states-what-the-document-states.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round.
the null: RUN by the issuer at portal DEV 741bb54b -- readingFromValue(null) NULL at adapt.ts:161; carryDocumentReading at :316; SOURCE_DATE_MALFORMED at status.ts:332 and :476; the view contract's null at contracts/index.ts:147.
the test: RUN -- fe-s-21/source-age.test.ts panelFor at :77-81 builds from status.sourceAsOf; :171 compares with formatSourceAge(AS_OF).
the provenance: RUN -- availability.ts:108 keys on producerState at DEV (W3-S25 met by FE-s-34 amendment 3).
the advisory: RUN -- ADVISORY_FOR_WIRE ?? 'unknown' at adapt.ts:558 and :865; 'ADVISORY' at gen-fixtures.ts:317.
lane: the <paths> block IS the grant; availability.ts, the band surfaces and the fixture maps excluded.
</preflight>

Seating: slot ~3; wave B -- seated only after FE-s-37 is drained, on a fresh worktree pair cut from HEAD, with the `<status>` flip committed BEFORE the pair is cut (row S26).
