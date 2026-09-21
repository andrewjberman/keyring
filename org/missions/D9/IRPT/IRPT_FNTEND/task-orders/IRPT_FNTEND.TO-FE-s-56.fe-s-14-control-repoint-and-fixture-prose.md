# TO IRPT_FNTEND.TO-FE-s-56 -- the fe-s-14 control re-points to committed trees; the withheld-cohort fixture prose is corrected

<to_id>IRPT_FNTEND.TO-FE-s-56</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~6</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete</status>

⛔ **COO DRAIN NOTE (2.0.0_SA_COO~F, 2026-09-21 ~14:30Z).** The worker correctly left this `pending`: F56-AC5
measured FAIL at its own worktree's vintage on the same `fe-s-49` F49-AC8 residual, filed as row `W6-S2`
(OBSERVATION, and correctly named `FE-s-51` as the sibling cell owning it). Verified independently in the
MERGED tree after this cell's drain (portal `2e69645c`, workspace `f079b3f61b`): `bun test
src/pages/InvestorReporting` reads `592 pass / 21 skip / 0 fail`. All six mechanical criteria hold at the
merged vintage; flipping to `complete` on that measurement.

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-56` (round 9, v0.9) | **outcome_ref:** FWD-12 (evidence) | **depends_on:** none | **slot:** ~7 | **rows:** W2-S35, W4-S20 (round-8 analysis item 7)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-56` -- **round-8's analysis, item 7, VERBATIM:** *"W2-S35 and W4-S20 -- 2.0.0_SA_COO~F's rows, one cell
(G). The fe-s-14 control is re-pointed to the re-pointed test's own git form (committed trees), over a known
pair where `firmAccess.ts` GAINED 3 entries, so it can return an answer the test would refuse. `fixtures/index.ts:77`'s
`proves` prose reads 'renders as withheld'."*

**TWO HALVES, VERIFY BOTH BEFORE EDITING.**

**Half 1 -- the fixtures prose (CONFIRMED STALE by the issuer's own read).**
`portal/src/pages/InvestorReporting/fixtures/index.ts:77` currently reads: `proves: 'a non-authoritative cohort
fact -- unknown renders as unknown, never as false and never as Client'`. Since FE-s-48 (round 7) changed
non-authoritative cohort rendering to `'withheld'` (`header/ScopeSummary.tsx`'s own comment: "a value the panel
declines to assert is withheld, not unknown"), this prose describes the SUPERSEDED behavior. **Fix:** change
the `proves` string to describe the CURRENT behavior -- a non-authoritative cohort fact renders as `'withheld'`,
never as `'unknown'`, `false` or `Client`. This is prose only; the fixture's own JSON data
(`directory.unknown-cohort.json`) is not a `<paths>` grant here and is NOT to be edited unless your read of it
shows the prose change requires a matching data change (check first, edit only if needed, and say which).

**Half 2 -- the fe-s-14 control re-point. VERIFY BEFORE ASSUMING A FIX IS OWED.** The issuer read
`__tests__/fe-s-14/allowlist.test.ts` (the file whose docstring most plausibly matches "re-pointed... to
committed trees, over a known pair") and found it ALREADY documents and asserts a `+0 -3` diff between
`RETIREMENT_BASE` (`1f3ce9f0`) and HEAD, consistent with FE-s-49's retirement of the three-firm grant -- i.e.
it may ALREADY BE the re-pointed, correct control the analysis describes, not a stale one. **Your first act:**
run `bun test __tests__/fe-s-14/allowlist.test.ts` at THIS worktree's HEAD and read whether it passes and
whether its printed diff matches `+0 -3` against the CURRENT `firmAccess.ts`. If it already passes correctly,
**search the REST of `__tests__/fe-s-14/`** (`published-map.test.ts`, `header.test.ts`, `one-firm.test.ts`,
`envelope.test.ts`) for a DIFFERENT committed-tree-diff control whose expected delta is stale by +3 entries
against a more recent base -- that is the one the analysis means. **If you cannot locate a genuinely stale
control anywhere in `__tests__/fe-s-14/` after this search, REFUSE this half of the order** with your full
search trace (every file checked, what each asserts, why none is stale) rather than editing a control that is
already correct.

### ACCEPTANCE

<criterion id="F56-AC1" cell_refs="FE-s-56" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F56-AC1` -- the whole portal typechecks.

<criterion id="F56-AC2" cell_refs="FE-s-56" drives="none"><invocation>cd <WS>/portal && grep -n "proves:" src/pages/InvestorReporting/fixtures/index.ts | grep -i withheld</invocation><expect>withheld</expect></criterion>
`F56-AC2` -- the `directory.unknown-cohort.json` row's `proves` prose now says "withheld", not "renders as
unknown".

<criterion id="F56-AC3" cell_refs="FE-s-56" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-1/fixtures.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F56-AC3` -- the fixtures manifest test still passes (the prose change does not break the denominator count).

<criterion id="F56-AC4" cell_refs="FE-s-56" drives="none"><invocation>cd <WS>/portal && timeout 300 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-14</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F56-AC4` -- the whole fe-s-14 suite passes -- either because your search found and fixed the genuinely stale
control, or because you REFUSED half 2 with a full search trace and this criterion is graded on the
UNMODIFIED, already-passing suite.

<criterion id="F56-AC5" cell_refs="FE-s-56" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F56-AC5` -- the whole IRPT_FNTEND suite is green.

<criterion id="F56-AC6" cell_refs="FE-s-56" judgment="true" drives="none"/>
`F56-AC6` -- graded at L9: the prose fix accurately describes current behavior, and the control search (fix or
honest refusal) is grounded in what the tests actually assert, never a guess. RECORD; NO VERDICT.

<expected_criteria>F56-AC1, F56-AC2, F56-AC3, F56-AC4, F56-AC5, F56-AC6</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/`
  and this order's own file.
- ⛔ **`fixtures/index.ts` IS YOURS FOR THE ONE `proves` STRING AT THE `directory.unknown-cohort.json` ROW
  ONLY.** No other row's prose changes.
- ⛔ **DO NOT EDIT A CONTROL THAT ALREADY PASSES FOR THE RIGHT REASON.** REFUSE with your search trace instead.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or
  `clean`. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`; read both investigation files before minting.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/fixtures/index.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-14/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.9, cell `FE-s-56`.
<owned_cells>FE-s-56</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F56-AC1` .. `F56-AC6`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~6/IRPT_FNTEND.TO-FE-s-56.fe-s-14-control-repoint-and-fixture-prose.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F56-AC1,F56-AC2,F56-AC3,F56-AC4,F56-AC5,F56-AC6 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-56.fe-s-14-control-repoint-and-fixture-prose.md`
BEFORE the `complete` flip. `F56-AC6` recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file
`fe-s-14-control-repoint-and-fixture-prose.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED).
half 1: RUN by the issuer -- fixtures/index.ts:77 read at source, confirmed stale against FE-s-48's withheld-not-unknown precedent.
half 2: PARTIALLY RUN by the issuer -- __tests__/fe-s-14/allowlist.test.ts read at source, appears ALREADY re-pointed (+0 -3 against 1f3ce9f0); the genuinely stale control this row names, if it exists elsewhere in fe-s-14, is UNCONFIRMED and handed to the worker's own search.
lane: the <paths> block IS the grant.
</preflight>

Seating: wave A, slot ~7; ready root, no dependency edge with any other round-9 cell.
