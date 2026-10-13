# TO IRPT_BCKEND.TO-IB-pr-502 -- the portal's `fe-s-18` generator reproduces the committed bytes the portal's tests consume (rows D2-W350-S1, D2-W346-S3)

<to_id>IRPT_BCKEND.TO-IB-pr-502</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~353</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>172</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-172 ANALYSIS (msg 6783) section 3 (row D2-W350-S1) and section 4 item 2 | **Decomp cell:** `IB-pr-502` (decomposition section 164) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-502` (inlined):** `portal/src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts` cannot be run: it throws at `clone(wire[HOLDINGS_KEY])` (`:424`, `HOLDINGS_KEY` at `:220` is the BARE prefix; `fixtures/smoke/fe-s-13-wire.json` carries the HASHED key), and it writes `fixtures/smoke/fe-s-18-frozen.json` (`:331`) BEFORE it throws, so every run dirties a committed fixture. The previous worker also found the committed outputs mutually inconsistent: `fe-s-18-frozen.json` carries `directory/resolve` `verified_request_firm_id` `F-49F`, while `fe-s-18-holdings-observed.json`, `-target.json`, `-missing-attribution.json` and `__tests__/fe-s-32/holdings-no-answer.json` carry `fir_4f9c1a7b2e6d03518ca47b90` for the same key, and the generator copies the frozen map's keys into every holdings map, so no single run writes both. The CTO's ruling: **the truth is the committed bytes the portal's tests consume at HEAD; repair the GENERATOR to reproduce them; change no output.** You work in the PORTAL repo (your worktree's `portal/` directory, `node_modules` linked, `bun` on PATH). This is a candidate for portal DEV.

**The six outputs the generator writes** (portal-relative to `src/pages/InvestorReporting/`): `fixtures/smoke/fe-s-18-frozen.json`, `fixtures/smoke/fe-s-18-holdings-observed.json`, `fixtures/smoke/fe-s-18-holdings-target.json`, `fixtures/smoke/fe-s-18-holdings-missing-attribution.json`, `__tests__/fe-s-32/holdings-no-answer.json`, `fixtures/smoke/fe-s-16-print-prehistory.json`.

**Do:**
1. For EACH of the six outputs find the portal test or tests that consume it at HEAD (the files that read it, directly or through a helper such as `_maps.ts`, `_scenarios.ts` or `_wire.ts`), and cite one consumer per output as `test` (portal-relative path), `line` and an exact one-line `quote`. Which bytes a test requires (for example which firm id it expects) is read from the test, not guessed.
2. Repair `fe-s-18/gen-fixtures.ts` (and only it) so that a run writes each of the six outputs with exactly its committed bytes: resolve the hashed holdings key from the wire map's own keys by prefix where the bare constant fails; do not write `fe-s-18-frozen.json` before every input it needs has been read; write each holdings map's firm id from what its consumers require rather than copying the frozen map's. Where the wire map and the committed outputs differ in a figure (the committed maps key routes by the bare prefix, the wire copy by hash or id; the status operation is `status-summary` committed and `status-job` in the wire; `covered_account_ids` is absent committed), the committed bytes win: the generator maps the wire's shape to the committed shape.
3. Keep each committed file's EXISTING line endings (compare with `git diff --ignore-cr-at-eol`); do not mass-convert; do not edit any output file (the generator must reproduce them; hand-editing an output to match is the failure this order exists to end).
4. Commit the portal change BEFORE you run the criterion that runs the generator (it checks for a clean tree). Record `portal_base` as the portal HEAD at your start.
5. Write the decision record to `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~353/IB172-2_fe_s_18_truth_decision.json`: `{"portal_base":"<commit id at start>","outputs":[{"file":"src/pages/InvestorReporting/fixtures/smoke/fe-s-18-frozen.json","consumed_by":[{"test":"src/pages/InvestorReporting/__tests__/...","line":N,"quote":"..."}],"truth":"committed bytes kept","what_the_generator_changed":"..."}, ...six entries...]}`.

**Criteria (run each under `timeout 120` from your WORKSPACE root, the parent of `portal/`, record the output and exit code verbatim):**

<criterion id="IB172-2-AC1" cell_refs="IB-pr-502"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r172/p172_cells.py" . IB172-2-AC1</invocation><expect>IB172-2-AC1 PASS</expect></criterion>
<criterion id="IB172-2-AC2" cell_refs="IB-pr-502"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r172/p172_cells.py" . IB172-2-AC2</invocation><expect>IB172-2-AC2 PASS</expect></criterion>
<criterion id="IB172-2-AC3" cell_refs="IB-pr-502"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r172/p172_cells.py" . IB172-2-AC3</invocation><expect>IB172-2-AC3 PASS</expect></criterion>

<expected_criteria>IB172-2-AC1, IB172-2-AC2, IB172-2-AC3</expected_criteria>

What the checks grade: AC1 the check RUNS the `fe-s-18` generator (`bun run <generator>` from `portal/`) and then `git diff --ignore-cr-at-eol --stat` over the smoke, fe-s-16 and fe-s-32 fixture folders must be EMPTY; AC2 six portal tests that consume the maps pass (28 or more pass, none fail: they read 28 pass, 8 skip, 0 fail at the base); AC3 the decision record names exactly the six outputs, each with a consumer whose quote sits within 3 lines of the cited line, and `git diff` of the six outputs from `portal_base` to HEAD is empty. Do not edit the checks. Run `bun test src/pages/InvestorReporting` ONCE at the end and report its counts against your base run (the base is 1213 pass, 27 skip, 4 fail; the four are pre-existing).

## BOUNDS

- **Grant:** the `paths` block and nothing else. Portal repo: only `src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts`. No output file, no other generator, no product code, no `package.json` or lockfile; run no `bun install`; push nothing.
- **Refusal clause:** STOP, file a row, change nothing more, if two tests require different bytes for the SAME output file (name both tests and the two requirements), or if reproducing a committed file would need a change to any file other than the generator.
- **Commit** in BOTH repos per your definition: the workspace commit (deliverables, order flip, rows) with `.tools/safe-commit.sh`, and the portal commit with plain `git -C portal commit` (same author and committer values, message file from the Write tool outside the worktree); ASCII only; never stage the workspace's `portal` gitlink.
- **Row ids** are `IRPT_BCKEND-D2-W353-S<k>` (the next free `k`). Report once, under 150 words.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-18/gen-fixtures.ts
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~353/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-502.fe-s-18-generator-reproduces-the-consumed-bytes.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 164 (round 172, workstream ~P), cell `IB-pr-502`.
<owned_cells>IB-pr-502</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB172-2-AC1, IB172-2-AC2, IB172-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~353/IRPT_BCKEND.TO-IB-pr-502.fe-s-18-generator-reproduces-the-consumed-bytes.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one test-folder generator of one portal page; no product file, no served artifact; the candidate lands on portal DEV through the CTO review lane (PROD rides the held promote `dell1-e7f2`). No live DSGN_IRPTV1 order names this file.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p172_cells.py dry-run at base on dell2 2026-10-13 ~04:3xZ: IB172-2 AC3 FAIL (no record); AC2 reads PASS at the base (28 pass, 8 skip, 0 fail: a regression guard, not a progress mark); AC1 (running the generator) is known to fail at the base from round 171's trial (the generator throws at gen-fixtures.ts:424 after writing the frozen map).
lane: the paths block IS the grant; worker slot ~353 of IRPT_BCKEND, a portal worktree pair. Class LOCAL.
</preflight>
