# TO DSGN_RBNDV2.TO-RV-y-3 -- FWD-3/FWD-5: the design tests typecheck and run with no workspace above the portal

<to_id>DSGN_RBNDV2.TO-RV-y-3</to_id>
<project>DSGN_RBNDV2</project>
<issued_to>0.9.0_WK_DSGN_RBNDV2~21</issued_to>
<issued_by>2.0.0_SA_COO~RB</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.1 @e71a48e4b0 | **Decomp cell:** `RV-y-3` (decomp v6 addendum 1) | **outcome_ref:** FWD-3, FWD-5 | **depends_on:** -- | **slot:** ~21, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`RV-y-3` -- two instrument defects found at the round-6 drain, both in the design tests under `portal/src/__tests__/dsgn-rbndv2/`.

(1) **A type error.** `portal/src/__tests__/dsgn-rbndv2/rb-5-x5.hover-resolve.test.ts` line about 30 passes `maxBuffer` to `execSync`, and `tsc -p tsconfig.app.json --noEmit` (run from the portal root) reports `error TS2769: No overload matches this call ... 'maxBuffer' does not exist` there. Fix it with the smallest change that keeps the test's meaning (remove the `maxBuffer` option, or read the walk's output another way), keep every arm of that test passing and its printed lines (`INLINE-WHITE-BEFORE`, `INLINE-WHITE-AFTER`, `VERDICT: HOVER-RESOLVE-OK`).

(2) **A test that needs the workspace around the portal.** `portal/src/__tests__/dsgn-rbndv2/rb-6-y1.border-sweep.test.ts` reads the sweep list from the workspace tree (`org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~19/BORDER_SWEEP_LIST.md`). Run from the portal repository alone (the integration checkout has no workspace above it) three of its arms fail. Copy that list file (it exists in your worktree at that workspace path) to `portal/src/__tests__/dsgn-rbndv2/fixtures/border-sweep-list.md` unchanged, and change the test to read the fixture from its own directory (the way the other tests in that folder locate files relative to themselves), so the test passes with no workspace path. Keep its arms, its printed `BORDER-WHITE-BEFORE`/`BORDER-WHITE-AFTER` lines and its `VERDICT: BORDER-SWEEP-OK`.

**New test.** Write `portal/src/__tests__/dsgn-rbndv2/rb-6-y3.standalone.test.ts`: it reads every `.ts` and `.tsx` file in `src/__tests__/dsgn-rbndv2/` (excluding itself) as text and requires that none contains the string `org/missions` or the string `deliverables/0.9.0`, requires that `fixtures/border-sweep-list.md` exists, and requires that `rb-5-x5.hover-resolve.test.ts` does not contain `maxBuffer`; it PRINTS `STANDALONE-FILES <n>` and `VERDICT: STANDALONE-OK` only when every arm holds; the difference control runs the same arms on `git show d0cb67d0:src/__tests__/dsgn-rbndv2/rb-6-y1.border-sweep.test.ts` and `git show d0cb67d0:src/__tests__/dsgn-rbndv2/rb-5-x5.hover-resolve.test.ts` and they must report at least one failing arm (the y1 test names `org/missions`, the x5 test names `maxBuffer`). The tests under `src/__tests__/dsgn-rbndv2/` must contain no path that begins `org/` (a test may use `git show <commit>:<portal path>`).

**TOKEN FORMATS (read before touching a colour).** The `--rb-*` tokens are HEX values, read as `var(--rb-X)`, NEVER `hsl(var(--rb-X))`: `--rb-ink` #0A1733 (body ink, "black on white"), `--rb-ink-2` #163372, `--rb-ink-3` #4A5878 (secondary ink), `--rb-quiet` #6B7590, `--rb-rule` #E3E7EF, `--rb-row-rule` #EEF1F6, `--rb-accent` #5F3BE3 (indigo). `--bg-surface`, `--bg-page`, `--hairline` and `--semantic-*` are HSL triples, read as `hsl(var(--X))`. In a recharts prop or an SVG attribute use the form RV-c-1 used in `portal/src/components/market-performance/FearGreedModal.tsx` (a chart prop such as `tick={{ fill: 'var(--rb-ink-3)' }}`; for an SVG attribute `fill="var(--rb-ink)"` or `style={{ fill: 'var(--rb-ink)' }}`); where a translucent ink is needed write `rgba(10, 23, 51, <alpha>)`.

**Out of this cell:** every file except the ones named in the BOUNDS paths.

**The rules:** this is ONE branch's work and nothing leaves the laptop: you commit to your worktree branch only and never push, merge, rebase, `checkout --` or `clean`. No shadow, radii 2/3/4px only, no non-ASCII in code. Typecheck rule for a test: from `node:child_process` use `execSync` (not `execFileSync`), from `node:path` use `join` (not `relative`), type any `process.env` read through a cast. The design principle Andrew gave in round 5: text resolves to black ink on a white ground and to white on a coloured fill (an indigo tooltip, a coloured tile), and a line is grey on white and black on a colour; never white on white, never black on indigo. You are given the worker face only: open your order file only to edit its status, and do NOT read anything below the horizontal rule that follows the REPORT paragraph (the record of the issuer, not yours).

**Environment:** the portal worktree is `<WS>/portal`, branched from the feature branch `feature/dsgn-rbndv2-light` at `d0cb67d0` (the difference-control base). Do not start any server.

### ACCEPTANCE

<criterion id="RB6Y3-AC1" cell_refs="RV-y-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~21; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2/rb-6-y3.standalone.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: STANDALONE-OK</expect></criterion>
`RB6Y3-AC1` -- no design test names a workspace path, the sweep list fixture exists, the x5 test no longer names `maxBuffer`, the difference control fails on the two base texts, and the test prints `VERDICT: STANDALONE-OK` only when every arm holds.

<criterion id="RB6Y3-AC2" cell_refs="RV-y-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~21; timeout 300 /c/Users/AndrewBerman/.bun/bin/bun x tsc -p tsconfig.app.json --noEmit > /tmp/rb6y3-tsc.txt 2>&1; echo TSC-RC=$?</invocation><expect>TSC-RC=0</expect></criterion>
`RB6Y3-AC2` -- the application typecheck, which includes the design tests, exits 0: the printed line reads `TSC-RC=0`.

<criterion id="RB6Y3-AC3" cell_refs="RV-y-3"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_RBNDV2~21; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/__tests__/dsgn-rbndv2 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`RB6Y3-AC3` -- every test under `src/__tests__/dsgn-rbndv2/` passes: the summary line reads `0 fail`.

<expected_criteria>RB6Y3-AC1, RB6Y3-AC2, RB6Y3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. A file outside it is a wall: write a surprise row naming it and keep working on what you can.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit workspace files through `.tools/safe-commit.sh`; commit the portal files inside `<WS>/portal` on your worktree branch. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/__tests__/dsgn-rbndv2/
org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_RBNDV2/decompositions/DSGN_RBNDV2_DECOMP_v6.md</decomp_doc> v6 addendum 1, cell `RV-y-3`.
<owned_cells>RV-y-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: RB6Y3-AC1, RB6Y3-AC2, RB6Y3-AC3. Instance at `org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/0.9.0_WK_DSGN_RBNDV2~21/DSGN_RBNDV2.TO-RV-y-3.tests-standalone.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> RB6Y3-AC1,RB6Y3-AC2,RB6Y3-AC3` BEFORE the flip, run from inside your worktree (pin every artifact row to the commit that carried it).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_RBNDV2-W21-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v6 addendum 1 -- the paths of this cell are written by no other open order (RV-y-2 writes its own new test file in the same folder, a different file); the files were read at the feature tip d0cb67d0.
lane: the <paths> block IS the grant.
</preflight>

Seating: slot ~21, direct act (round-less, one cell, LOCAL, about 20 product lines); worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_RBNDV2 21 --portal-ref feature/dsgn-rbndv2-light`.
