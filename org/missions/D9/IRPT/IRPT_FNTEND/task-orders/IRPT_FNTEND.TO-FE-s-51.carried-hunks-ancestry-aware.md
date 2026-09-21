# TO IRPT_FNTEND.TO-FE-s-51 -- the carried-hunks arm is keyed to ancestry, not hardcoded to zero

<to_id>IRPT_FNTEND.TO-FE-s-51</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~2</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.9 @5fd2dc9ab5 | **Decomp cell:** `FE-s-51` (round 9, v0.9) | **outcome_ref:** FWD-12 (evidence) | **depends_on:** none | **slot:** ~2 | **rows:** F49-AC8 (round-8 analysis item 9)

<placeholders>WS</placeholders>

---

## WORKER FACE

### THE CELL

`FE-s-51` -- **`F49-AC8` (`portal/src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts:576-582`)
hardcodes `expect(carried.length).toBe(0)`: it asserts NO "unrelated" hunk (a diff hunk outside FE-s-49's own
three admin-gate lines) is ever carried into HEAD's `App.tsx`.** The issuer's round-8 analysis (item 9) found
this is too strict on a checkout descended from commit `c29a8b86` (the `d13-visual-elevation` branch, per
`.worktrees/d13-visual-elevation` — confirm the exact commit by `git log --oneline c29a8b86 -1`): that commit's
merge legitimately carries **2 unrelated hunks** into `App.tsx` (visual-elevation changes near the same lines),
which are EXPECTED there and must not fail this test. On a checkout NOT descended from `c29a8b86`, 0 unrelated
hunks remain the correct expectation.

**THE REMEDY:** replace the hardcoded `expect(carried.length).toBe(0)` at `:582` with an ancestry-aware
expectation:
```
const c29a8b86IsAncestor = <run `git merge-base --is-ancestor c29a8b86 HEAD` from the test, via the same
  child-process helper this test file already uses for its other git reads (see the file's own `S.head` /
  `S.before` setup) -- rc 0 = true, rc 1 = false>
const expectedCarried = c29a8b86IsAncestor ? 2 : 0
expect(carried.length).toBe(expectedCarried)
```
Print which branch fired and why (`c29a8b86 IS / IS NOT an ancestor of HEAD; expecting N unrelated hunk(s)`).
**Green at BOTH commits named in the analysis:** portal DEV `9adad7ce` (promote candidate, descended from
`c29a8b86`, expects 2) AND `10c2f07d` (FE-s-49's own drain point, verify its ancestry independently rather
than assuming) — read each via a detached checkout or `git show <ref>:src/App.tsx`, never by switching this
worktree's own branch.

### ACCEPTANCE

<criterion id="F51-AC1" cell_refs="FE-s-51" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F51-AC1` -- the whole portal typechecks.

<criterion id="F51-AC2" cell_refs="FE-s-51" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F51-AC2` -- the whole admin-gate suite, at THIS worktree's own HEAD, passes with the new ancestry-aware
expectation.

<criterion id="F51-AC3" cell_refs="FE-s-51" drives="none"><invocation>cd <WS>/portal && git show 9adad7ce:src/App.tsx > <WS>/.scratch/apptsx-9adad7ce.txt 2>&1; git merge-base --is-ancestor c29a8b86 9adad7ce; echo ancestor_rc=$?</invocation><expect>ancestor_rc=0(?![0-9])</expect></criterion>
`F51-AC3` -- confirms `9adad7ce` descends from `c29a8b86` (the analysis's own premise) before you rely on it.

<criterion id="F51-AC4" cell_refs="FE-s-51" drives="none"><invocation>cd <WS>/portal && git merge-base --is-ancestor c29a8b86 10c2f07d; echo ancestor_rc=$?</invocation><expect>ancestor_rc=[01](?![0-9])</expect></criterion>
`F51-AC4` -- measures (never assumes) whether `10c2f07d` is also a `c29a8b86` descendant; print which branch of
the expectation this implies and confirm the test's own run against that ref (via a scratch harness reading
`git show 10c2f07d:src/App.tsx`, not a live checkout switch) matches.

<criterion id="F51-AC5" cell_refs="FE-s-51" judgment="true" drives="none"/>
`F51-AC5` -- graded at L9: the ancestry check reuses the file's existing git-read helper rather than
introducing a second way to shell out, and the test still fails loudly if a future unrelated hunk appears that
neither branch of the expectation names. RECORD; NO VERDICT.

<expected_criteria>F51-AC1, F51-AC2, F51-AC3, F51-AC4, F51-AC5</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/`
  and this order's own file.
- ⛔ **`admin-gate.test.ts` IS YOURS FOR THE `F49-AC8` EXPECTATION ONLY (`:576-582`).** No other test in the
  file changes; `F49-AC9` and every other criterion in this suite are NOT yours.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or
  `clean` on either repo's tracked branch. Reading another ref's blob is via `git show <ref>:<path>`, never a
  branch switch. Never stage `portal` in the workspace repo. `node_modules` is a junction; do not run
  `bun install`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W1-S<k>`; read both investigation files before minting.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-49/admin-gate.test.ts
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.9, cell `FE-s-51`.
<owned_cells>FE-s-51</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F51-AC1` .. `F51-AC5`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~2/IRPT_FNTEND.TO-FE-s-51.carried-hunks-ancestry-aware.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F51-AC1,F51-AC2,F51-AC3,F51-AC4,F51-AC5 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-51.carried-hunks-ancestry-aware.md`
BEFORE the `complete` flip. `F51-AC5` recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file
`carried-hunks-ancestry-aware.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.9 (both L4-R halves SIGNED).
the defect: RUN by the issuer, round-8 analysis item 9 (F49-AC8) -- admin-gate.test.ts:576-582 read at source; hardcoded `toBe(0)` confirmed.
lane: the <paths> block IS the grant; admin-gate.test.ts is yours for :576-582 only.
</preflight>

Seating: wave A, slot ~2; ready root, no dependency edge with any other round-9 cell.
