# TO IRPT_FNTEND.TO-FE-s-48 -- a cohort fact the producer does not assert reads withheld, never unknown

<to_id>IRPT_FNTEND.TO-FE-s-48</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~4</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-15</issued_date>
<status>staged</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.6 @d1479bc5f0 (F6, F7; CONTRACTS consumed) | **Decomp cell:** `FE-s-48` (round 8, v0.8 @734eb61ac1) | **outcome_ref:** FWD-5, FWD-6 | **depends_on:** none | **slot:** ~4 | **rows:** C-S93 (F42-AC10's qualification)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-48` -- **the header shows every cohort axis the producer does not assert as "unknown", when the truer word is "withheld".** 3.0.0_SA_CVO graded F42-AC10 MET WITH A NAMED QUALIFICATION (grade record C-S93): a non-authoritative cohort renders every axis as `<axis>: unknown` under "Cohort (not asserted)". `1.0.0_SA_CTO` ruled it in the round-7 analysis (msg 96865, item 6): **a non-authoritative cohort's axes read "withheld", never "unknown"**. RULING W keeps "unknown" out of any state that has a truer word, and a value the panel declines to assert is withheld, not unknown.

Measured by the issuer at portal DEV 1f3ce9f0:
- `header/ScopeSummary.tsx`:
  - `:67-68` splits the entry's cohort facts: `assertable = cohorts.filter((c) => c.authoritative)` and `withheld = cohorts.filter((c) => !c.authoritative)`.
  - `:117-119` renders the withheld ones: `<Fact label="Cohort (not asserted)" value={withheld.map((c) => `${c.axis}: unknown`).join(', ')} />`.
  - The file's header comment at `:9-12` says those axes "are shown as 'unknown' text with no affordance".
- **The assertable path is different and unchanged.** It renders each value's token (`:86-115`). A producer's own UNKNOWN advisory there is a VALUE the producer asserted, not a withholding, and it keeps rendering as `unknown`.
- **Round 7's census of `CohortFact` values outside `__tests__/`** finds two consumers: `contracts/validate.ts:164-171`, which checks and does not render, and `header/ScopeSummary.tsx`, which renders. Re-run it at your vintage.
- A committed fixture already carries a non-authoritative cohort: `fixtures/directory.unknown-cohort.json`, with the partialReason "Cohort facts for this relationship are not authoritative."
- **The issuer's probe.** The one-word change turned 0 tests red in the whole suite: 559 pass, 18 skip, 1 fail of 578. The 1 fail is F41-AC5's control timing out under load, which is FE-s-46's and unrelated.

**THE REMEDY:**
- The "Cohort (not asserted)" fact renders each withheld axis as `<axis>: withheld`, and the header comment says so.
- The assertable path, including a producer's own UNKNOWN token, is unchanged.
- Text only: no class, colour or element changes, so no contrast surface moves.

### ACCEPTANCE

<criterion id="F48-AC1" cell_refs="FE-s-48" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F48-AC1` -- the whole portal typechecks.

<criterion id="F48-AC2" cell_refs="FE-s-48" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-48/withheld.test.ts</invocation><expect>NON-AUTHORITATIVE COHORT READS WITHHELD ON EVERY AXIS: (\d+) of \1(?![0-9])</expect></criterion>
`F48-AC2` -- the ruling.
- Render `ScopeSummary` in memory with a directory entry whose cohort axes are ALL non-authoritative. Build it from the committed fixture `fixtures/directory.unknown-cohort.json` (read with `git cat-file blob HEAD:<path>`) or from a wire body through the real adapter.
- Print the rendered "Cohort (not asserted)" text.
- Each axis reads `<axis>: withheld`, and the word "unknown" does not appear in that fact. The denominator is the axes the entry carries.

<criterion id="F48-AC3" cell_refs="FE-s-48" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-48/withheld.test.ts</invocation><expect>IN-ENUM AUTHORITATIVE ADVISORY UNCHANGED: 3 of 3(?![0-9])</expect></criterion>
`F48-AC3` -- the control. An AUTHORITATIVE cohort whose advisory is ADVISED, RESIDUAL and UNKNOWN in turn renders exactly as at DEV 1f3ce9f0. UNKNOWN keeps reading `unknown`, because that is the producer's asserted value.

<criterion id="F48-AC4" cell_refs="FE-s-48" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-48/withheld.test.ts</invocation><expect>BEFORE \(DEV 1f3ce9f0\): THE WITHHELD FACT READ unknown: yes</expect></criterion>
`F48-AC4` -- the arm that can say no. Read DEV 1f3ce9f0's committed `ScopeSummary.tsx` (`git cat-file blob 1f3ce9f0:<path>`) and show its withheld fact built `: unknown`. HEAD's committed blob builds `: withheld`. Print both lines.

<criterion id="F48-AC5" cell_refs="FE-s-48" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-48/withheld.test.ts</invocation><expect>EVERY RENDER OF A WITHHELD COHORT VALUE READS withheld: (\d+) of \1(?![0-9])</expect></criterion>
`F48-AC5` -- the reach, BY SUBTRACTION over the corpus (RULING X), from the COMMITTED tree.
- Enumerate every consumer of a `CohortFact` (or of `authoritative`) outside `__tests__/`, and print the denominator.
- Subtract the ones that do not render, printing each with its reason (`validate.ts`'s checks).
- Every remaining render of a non-authoritative value reads "withheld".

<criterion id="F48-AC6" cell_refs="FE-s-48" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F48-AC6` -- **the whole-suite census of record**, with `IRPT_FE_DEV_PORT` exported to a port you have measured closed. If F41-AC5's control times out under load (FE-s-46's row, not yours), report it and re-run; never edit it.

<criterion id="F48-AC7" cell_refs="FE-s-48" judgment="true" drives="none"/>
`F48-AC7` -- graded at L9: a cohort value the panel declines to assert reads "withheld" at every render site, never "unknown", and a value the producer asserted is unchanged. RECORD; NO VERDICT.

<expected_criteria>F48-AC1, F48-AC2, F48-AC3, F48-AC4, F48-AC5, F48-AC6, F48-AC7</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file. A path you need that is not named is a BLOCKING row; never an override.
- ⛔ **`header/ScopeSummary.tsx` IS YOURS FOR TWO THINGS ONLY:**
  - the withheld fact's rendered word (`:118`);
  - the header comment that describes it (`:9-12`).
  - No class, colour, element, label or assertable-path change.
- ⛔ **NOT YOURS:**
  - `contracts/`, `validate.ts` and `tabs/holdings/slices.ts`;
  - every fixture;
  - FE-s-42's tests (`__tests__/fe-s-42/`).
  - If one of them asserts the old word, that is a BLOCKING row. The issuer's probe found none.
- ⛔ **THE WHOLE-SUITE RUN IS THE CENSUS OF RECORD** (F48-AC6). A red test outside your grant is a BLOCKING row with the list, never an edit.
- **RULING AC.** Every file your tests inspect is read as the committed blob (`git cat-file blob HEAD:<path>` or `<commit>:<path>`) or the committed tree, or the test says why it reads the working copy.
- **Servers.** No dev server is needed: the render is in memory, the way the existing mounted tests render. Export `IRPT_FE_DEV_PORT` on EVERY `bun test` run to a port you have measured closed (5265 is this slot's). A closed loopback port refuses in about 0.3 to 2 s here, so any probe timeout must exceed 2 s. Sibling slots use 5261 and 5263; never touch them.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Portal commit pathspec: the files you changed, named individually. Workspace records under `org/` only. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Anchors and evidence.** Counts your tests print are anchorable; each row's `output_evidence` carries the deciding run only.
- **Bound every invocation** with `timeout` as written. **Scratch:** `<WS>/.scratch/` only.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W4-S<k>`, starting at W4-S18. Read the WHOLE channel PLANE (`INVESTIGATION_v1.md` AND `_v2.md`) before minting; an INERT row OMITS the `disarm_owner` key; write with `newline='\n'` and READ THE DIFFSTAT of your commit.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/header/ScopeSummary.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-48/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.8 @734eb61ac1, cell `FE-s-48`.
<owned_cells>FE-s-48</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F48-AC1` .. `F48-AC7`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~4/IRPT_FNTEND.TO-FE-s-48.non-authoritative-cohort-reads-withheld.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F48-AC1,F48-AC2,F48-AC3,F48-AC4,F48-AC5,F48-AC6,F48-AC7 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-48.non-authoritative-cohort-reads-withheld.md` BEFORE the `complete` flip. `F48-AC7` recorded `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming the CVO at L9. Result file `non-authoritative-cohort-reads-withheld.result.md` beside it. Flip only when every mechanical criterion PASSES by output.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.6 -- carried; PRD unchanged this round (round-7 analysis, msg 96865, no addendum).
the site: RUN by the issuer at portal DEV 1f3ce9f0 -- ScopeSummary.tsx:67-68 assertable/withheld split; :117-119 withheld rendered `${c.axis}: unknown`; header comment :9-12.
the render census: RUN -- round 7's CohortFact consumers outside __tests__ = validate.ts:164-171 (checks) and ScopeSummary.tsx (renders); the non-authoritative fixture fixtures/directory.unknown-cohort.json.
the reach: RUN -- the issuer's whole-suite probe (decomp R8.1) with the one-word change: 559 pass, 18 skip, 1 fail of 578; the fail is F41-AC5's control timing out (FE-s-46's), so the change turns 0 tests red.
lane: the <paths> block IS the grant; text only in ScopeSummary.tsx; contracts/, validate.ts, slices.ts, fixtures and FE-s-42's tests excluded.
</preflight>

Seating: slot ~4; one wave -- round 8 has no dependency edge, seated on a fresh worktree pair cut from HEAD with the `<status>` flip committed BEFORE the pair is cut (row S26).
