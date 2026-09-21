# TO IRPT_FNTEND.TO-FE-s-52 -- five lint errors clear; portal DEV CI reads green for the first time since 09-11

<to_id>IRPT_FNTEND.TO-FE-s-52</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~3</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

⛔ **COO DRAIN NOTE (2.0.0_SA_COO~F, 2026-09-21 ~14:30Z).** The worker correctly left this `pending`: F52-AC4
measured FAIL at its own worktree's vintage on `fe-s-49/admin-gate.test.ts` F49-AC8, filed as row
`IRPT_FNTEND-W3-S42` (INERT). That vintage predates `FE-s-51`'s drain (portal `1ba704fb`), which fixed exactly
that assertion. Verified independently in the MERGED tree after this cell's own drain (portal `06ab95e4`,
workspace `bb4b40a80c`): `bun test src/pages/InvestorReporting` reads `592 pass / 21 skip / 0 fail`. All five
mechanical criteria hold at the merged vintage; flipping to `complete` on that measurement, not the worker's.

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-52` (round 9, v0.9) | **outcome_ref:** FWD-12 | **depends_on:** none | **slot:** ~3 | **rows:** round-8 analysis item 8 + ADDENDUM ~12:3xZ (0.0.0_AB_MSTR 97061)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-52` -- **five lint errors, named exactly by the issuer's round-8 analysis, are the only thing keeping
portal DEV CI red.** Three are this project's own test files; two are `SentimentGauge.tsx`, a DSGN_REBRND file
carried under this ruling because DSGN_REBRND has no live seat to route them to.

1. `fe-s-5/alias-probe.test.ts:16:20` -- `no-constant-binary-expression`.
2. `fe-s-19/pre-envelope.test.ts:43:28` -- unused `PERFORMANCE_KEY`.
3. `export/ExportButton.tsx:246:5` -- `react-hooks/immutability`. The code is RUNTIME-CORRECT: an effect hides
   a DOM node and restores it on cleanup. **The remedy MOVES the hide/restore into `useExportAnchor`** (the
   hook that obtains the node), rather than suppressing the lint rule or changing the runtime behavior.
4. `src/components/market-performance/SentimentGauge.tsx:6:10` -- unused `PanelEmpty` import.
5. `src/components/market-performance/SentimentGauge.tsx:6:22` -- unused `PanelError` import.

**THE REMEDY, per finding:**
1. Read the flagged expression at `alias-probe.test.ts:16:20`; if the constant comparison is dead test scaffold,
   delete it; if it is testing something real, restructure it so the compared values are not both statically
   constant (e.g. read one side from a runtime-computed value already in scope).
2. Delete the unused `PERFORMANCE_KEY` import/declaration at `pre-envelope.test.ts:43`, or use it if a nearby
   assertion was meant to reference it and does not (read the surrounding 20 lines before choosing).
3. In `export/ExportButton.tsx`, find where `useExportAnchor` obtains its DOM node ref, move the hide-on-mount
   and restore-on-cleanup logic that currently sits in the flagged effect (around `:246`) into that hook, and
   have the component consume the hook's return rather than performing the DOM mutation itself.
4-5. Delete the two unused import specifiers (`PanelEmpty`, `PanelError`) from `SentimentGauge.tsx:6`. **This
   file belongs to DSGN_REBRND, which has no live seat** — the round-8 analysis carries this fix under this
   ruling explicitly so it does not wait on a seat that does not exist; touch ONLY the import line, nothing
   else in the file.

### ACCEPTANCE

<criterion id="F52-AC1" cell_refs="FE-s-52" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F52-AC1` -- the whole portal typechecks.

<criterion id="F52-AC2" cell_refs="FE-s-52" drives="none"><invocation>cd <WS>/portal && timeout 300 bun run lint 2>&1 | tail -40; echo rc=${PIPESTATUS[0]}</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F52-AC2` -- the portal's own lint script (read `package.json` for its exact name if not `lint`) returns clean.
Print the FULL error count before your fix (baseline) and after (must be the pre-fix count minus exactly 5,
with 0 new errors introduced), never a bare "passed".

<criterion id="F52-AC3" cell_refs="FE-s-52" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-5 src/pages/InvestorReporting/__tests__/fe-s-19</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F52-AC3` -- the two edited test files' own suites still pass on content, unaffected by the lint fix.

<criterion id="F52-AC4" cell_refs="FE-s-52" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F52-AC4` -- the whole IRPT_FNTEND suite is unaffected by the `ExportButton`/`useExportAnchor` refactor
(F52's own `export/` tests included).

<criterion id="F52-AC5" cell_refs="FE-s-52" drives="none"><invocation>cd <WS>/portal && git diff --stat src/components/market-performance/SentimentGauge.tsx</invocation><expect>1 file changed(?![0-9])</expect></criterion>
`F52-AC5` -- the DSGN_REBRND file's diff touches ONLY the import line; paste the full diff into your result
file for the record.

<criterion id="F52-AC6" cell_refs="FE-s-52" judgment="true" drives="none"/>
`F52-AC6` -- graded at L9: `ExportButton`'s DOM hide/restore is genuinely relocated into `useExportAnchor`
(behavioral parity), not merely rule-suppressed; the SentimentGauge touch is minimal and correctly scoped as a
carried fix. RECORD; NO VERDICT.

<expected_criteria>F52-AC1, F52-AC2, F52-AC3, F52-AC4, F52-AC5, F52-AC6</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/`
  and this order's own file.
- ⛔ **`SentimentGauge.tsx` IS YOURS FOR THE TWO UNUSED IMPORT SPECIFIERS ONLY (`:6:10`, `:6:22`).** No other
  line in that file changes; it is DSGN_REBRND's file, carried under this ruling and this ruling only.
- ⛔ **`ExportButton.tsx`'s effect MOVES, IT DOES NOT DISAPPEAR.** The hide/restore behavior must still occur,
  now inside `useExportAnchor`; a fix that merely disables/suppresses the lint rule is a REFUSAL, not a pass.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or
  `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`; read both investigation files before minting.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-5/alias-probe.test.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-19/pre-envelope.test.ts
portal/src/pages/InvestorReporting/export/ExportButton.tsx
portal/src/pages/InvestorReporting/export/
portal/src/components/market-performance/SentimentGauge.tsx
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.9, cell `FE-s-52`.
<owned_cells>FE-s-52</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F52-AC1` .. `F52-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~3/IRPT_FNTEND.TO-FE-s-52.five-lint-errors-portal-dev-green.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F52-AC1,F52-AC2,F52-AC3,F52-AC4,F52-AC5,F52-AC6 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-52.five-lint-errors-portal-dev-green.md`
BEFORE the `complete` flip. `F52-AC6` recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file
`five-lint-errors-portal-dev-green.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED).
the defect: RUN by the issuer, round-8 analysis item 8 + ADDENDUM 97061 -- five lint sites named exactly, each confirmed reachable in the current portal tree.
lane: the <paths> block IS the grant; SentimentGauge.tsx is yours for :6:10/:6:22 only.
</preflight>

Seating: wave A, slot ~3; ready root, no dependency edge with any other round-9 cell.
