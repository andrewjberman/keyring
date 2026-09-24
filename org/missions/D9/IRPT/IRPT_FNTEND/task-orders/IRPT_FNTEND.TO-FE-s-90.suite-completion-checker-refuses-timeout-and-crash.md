# TO IRPT_FNTEND.TO-FE-s-90 -- a reusable suite-completion checker that refuses a timeout, crash or incomplete run

<to_id>IRPT_FNTEND.TO-FE-s-90</to_id>
<project>IRPT_FNTEND</project>
<issued_to>0.9.0_WK_IRPT_FNTEND~40</issued_to>
<issued_by>2.0.0_SA_COO~F</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2 | **Decomp cell:** `FE-s-90` (round 15, v0.15) | **outcome_ref:** FWD-12 | **depends_on:** none -- READY ROOT | **slot:** ~2 | **rows:** C-S188 | **base:** workspace = the round-15 issuance commit on CLOUD (your worktree branches from it), portal DEV `7dd3d067` (round 14's close)

<placeholders>WS, PORT</placeholders>

---

## WORKER FACE
### THE CELL

`FE-s-90` -- every round-14 cell's whole-suite criterion used an ad-hoc shell filter
(`bun test ... | grep "^✗" | grep -vc <known-id>`) to isolate cross-cell noise from genuine regressions. The
CVO's own negative control found the filter's REMAINING hole: a `bun test` run held open and killed by
`timeout 1` returns producer `rc=124` with NO completion summary (no "Ran N tests across M files" line, no
pass/skip/fail counts) -- yet the exact filter still prints `UNEXPECTED-FAIL-COUNT=0`, because a timed-out
process that never got to run any test prints ZERO `✗` lines, and zero minus zero is still zero. A crash or
truncated/empty log has the identical blind spot. **This is the "control that cannot fail" class named in this
project's own doctrine** -- a check that reads the same regardless of whether the thing it is checking for is
true.

**Build a real, reusable, tested checker** (not another shell one-liner) that a future whole-suite criterion
calls instead of hand-rolling the filter again. Suggested shape, `scripts/suite-complete-check.mjs`
(node, no new dependency -- the project already avoids adding frameworks for a script like this):

- **Invocation:** `node scripts/suite-complete-check.mjs <bun-test-command...> [--allow <criterion-id>]...`
  (repeatable `--allow`) -- runs the given command as a child process, capturing stdout+stderr and the REAL
  exit code (never discard it).
- **Completion is REQUIRED, not inferred from silence.** The captured output MUST contain bun's own
  `Ran <N> tests across <M> files` line (or whatever the current bun version's exact completion marker is --
  read it directly from a real run, do not guess the format). Its ABSENCE is an automatic REFUSE
  (`SUITE-INCOMPLETE: <reason>`), regardless of exit code or how many `✗` lines exist -- this is the exact
  gap the timeout case exposed.
- **Exit code is read, never ignored.** A non-zero exit code that is NOT explained by an allowed, reconciled
  failure count is a REFUSE. `rc=124` (the `timeout` command's own signal for "I killed this") is always a
  hard REFUSE regardless of what the captured output otherwise looks like.
- **Reconcile IDENTITY, not just count.** Strip ANSI (the exact round-14 bug: `NO_COLOR` does not suppress
  bun's codes here), extract every `✗ <name>` line, and compare the SET of failing names against the
  `--allow`-listed criterion-id substrings. A failure whose name matches an allowed id does not count against
  the unexpected total; ANY other failure -- including one that happens to keep the total count the same as
  before -- does. Print both: `DECLARED-KEY VALIDITY: <the allow-listed ids the summary line syntactically names>`
  and `EXERCISED FULFILMENT: <n of m allowed failures actually matched by name>` as separate figures, matching
  this round's own C-S176 discipline (never conflate the two).
- **Output, unambiguous:** a single final line a caller's acceptance regex can anchor on, e.g.
  `SUITE-COMPLETE: yes | PASS: <n> SKIP: <n> UNEXPECTED-FAIL: <n>` on success, or
  `SUITE-COMPLETE: no | REASON: <timeout|crash|incomplete-output|unreconciled-failure: <name>>` on refusal --
  your exact format, but it must be ONE line, grep-able, and must never print a misleadingly clean summary on
  a run that did not genuinely finish.

**Required controls, ALL FOUR, in your own test file, each a REAL subprocess run (not a mocked one) against a
tiny fixture test file you author under your own grant, exactly mirroring the CVO's own four cases:**
1. a completed, fully-passing run -> `SUITE-COMPLETE: yes`, `UNEXPECTED-FAIL: 0`.
2. a completed run with one genuinely unexpected failure -> `SUITE-COMPLETE: yes`, `UNEXPECTED-FAIL: 1`.
3. a completed run whose one failure matches an `--allow`-listed id -> `SUITE-COMPLETE: yes`, `UNEXPECTED-FAIL: 0`.
4. **a run killed by `timeout` mid-execution** (the exact case that broke the old filter) -> `SUITE-COMPLETE: no`,
   naming the timeout reason -- THIS is the control that proves you closed the gap; if your checker cannot make
   this one fail, you have not fixed C-S188.

**Your surface.** A new `scripts/suite-complete-check.mjs` (or equivalent single new file under `scripts/`), and
your own `__tests__/fe-s-90/`. You do NOT need to retrofit round-14's already-drained task orders' criteria --
this cell delivers the INSTRUMENT; a future round adopts it in new criteria.

**HOW (the same for every cell of this round; read once, then do your cell).**

1. **Read first, in full:** `<WS>/portal/DESIGN.md`, `<WS>/portal/CLAUDE.md`; the PRD's ENDPOINT/CONTRACTS text
   (`../prd/IRPT_FNTEND_PRD.md` v0.10 @4bc62712f2); the CTO's round-14 analysis (`org/missions/D9/IRPT/IRPT_FNTEND/ledger/ROUND_ANALYSIS.round14.md`
   @8b1b0d6832); the CVO's round-14 slug (`org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/remediations/REMEDIATION_v11.md`)
   and its full review (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND14_L8_L9_20260922.md`) -- your
   cell's remedy is quoted from these; read the SURROUNDING text too, not just your own paragraph.
2. **Start your worktree's own dev server** on a port from YOUR BLOCK, 6015-6019 (outside every prior round's
   range): `IRPT_FE_DEV_PORT=<n> bun run dev --port <n>` in `<WS>/portal`, background, INLINE PREFIX, NEVER
   exported. Test with `curl` first; that number is `<PORT>`.
3. **A control is a claim.** Before trusting a passing assertion, run its wrong-state / negative arm and confirm
   it fails or reads UNMEASURABLE as required.
4. **Regression is the safety net.** This round FIXES instruments and fixtures that other cells' criteria already
   depend on -- the whole-suite criterion is not a formality, it is the proof you did not silently break a
   currently-passing test while fixing your own defect.
5. **Stop your dev server before the whole-suite criterion, verify the port closed** (`curl` returns `000`).
6. **Fixes.** A defect on YOUR write surface may be fixed with a BEFORE capture kept and an AFTER beside it. A
   defect needing another cell's file is ONE surprise row, never a wider grant.
7. **Result file** (`<slug>.result.md` in your deliverables folder), disclosure paragraph first.
8. **Keep your context small:** write long outputs to files and read their tails.

### ACCEPTANCE

<criterion id="F90-AC1" cell_refs="FE-s-90" drives="none"><invocation>cd <WS>/portal && timeout 180 /c/Users/AndrewBerman/.bun/bin/bun run typecheck; echo rc=$?</invocation><expect>rc=0(?![0-9])</expect></criterion>
`F90-AC1` -- the whole portal typechecks.

<criterion id="F90-AC2" cell_refs="FE-s-90" drives="none"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/fe-s-90</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F90-AC2` -- all four required controls pass in your own test file, including the timeout control genuinely invoking a real subprocess killed by `timeout` and asserting SUITE-COMPLETE: no.

<criterion id="F90-AC3" cell_refs="FE-s-90" drives="none"><invocation>cd <WS>/portal && /c/Users/AndrewBerman/.bun/bin/bun scripts/suite-complete-check.mjs --help; echo rc=$?</invocation><expect>.</expect></criterion>
`F90-AC3` -- the checker runs standalone (not only inside your own test harness) and prints usage/help output when invoked without a command -- proving it is a real, independently invocable tool, not test-only glue code. Any non-crashing output satisfies this; the point is it RUNS.

<criterion id="F90-AC4" cell_refs="FE-s-90" drives="none"><invocation>cd <WS>/portal && timeout 600 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting</invocation><expect>(?<![0-9])0 fail</expect></criterion>
`F90-AC4` -- the whole IRPT_FNTEND suite is green.

<criterion id="F90-AC5" cell_refs="FE-s-90" judgment="true" drives="none"/>
`F90-AC5` -- graded at L9 by the CVO: the checker genuinely refuses a timeout/crash/incomplete run (not merely asserted to in a comment), reconciles failure IDENTITY not just count, and its output format is unambiguous enough for a future task order's acceptance regex to anchor on reliably. RECORD; NO VERDICT.

<expected_criteria>F90-AC1, F90-AC2, F90-AC3, F90-AC4, F90-AC5</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus `org/missions/D9/IRPT/IRPT_FNTEND/deliverables/<your serial>/` and this order's own file.
- **You decide nothing about the verdict.** The last criterion is JUDGMENT: RECORD the evidence, give NO verdict; the CVO grades it at L9.
- **Two repos, one worktree pair.** `<WS>` / `<WS>/portal`. Never push, merge, rebase, `checkout --` or `clean`. Never stage `portal` in the workspace
  repo. `node_modules` is a junction; do not run `bun install`. Never bare `git commit` in the workspace: use `.tools/safe-commit.sh` with a message
  file written by your Write tool. Portal commits: `git -C <WS>/portal commit --author "<your serial> <<your serial>@opal.agent>" -F <msgfile>`.
- **Surprise.** ONE row per finding, id `IRPT_FNTEND-W40-S<k>`; read the investigation file before minting and append to its one JSON array.
- **REFUSE** any criterion you cannot satisfy as written and report the refusal with its measurement. Do not self-grade past a failure, do not weaken
  a criterion: an order defect is reported, and the issuer amends it.
- Report push state as LOCAL. **PORTAL IS FROZEN**: local commits only.
- **Two workers never share a write path.** Every file not in your `<paths>` is read-only to you, including every other cell's surface.
- **This cell delivers a NEW, standalone tool -- it does not edit any existing criterion's invocation** in
  any already-drained round-14 task order (those are closed).
- **C-S176 declared N/A, with reason, at cut time:** this cell builds and tests a command-line instrument, not
  a rendered visual assertion -- the five-part visual control rule does not apply. The four required controls
  above ARE this cell's control set.
<paths>
portal/scripts/suite-complete-check.mjs
portal/src/pages/InvestorReporting/__tests__/fe-s-90/
org/missions/D9/IRPT/IRPT_FNTEND/surprise-channel/investigations/INVESTIGATION_v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_FNTEND/decompositions/IRPT_FNTEND_DECOMP.md</decomp_doc> v0.15, cell `FE-s-90`.
<owned_cells>FE-s-90</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `F90-AC1`, `F90-AC2`, `F90-AC3`, `F90-AC4`, `F90-AC5`. Instance at
`org/missions/D9/IRPT/IRPT_FNTEND/deliverables/0.9.0_WK_IRPT_FNTEND~<n>/IRPT_FNTEND.TO-FE-s-90.suite-completion-checker-refuses-timeout-and-crash.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> F90-AC1,F90-AC2,F90-AC3,F90-AC4,F90-AC5 --governing-order org/missions/D9/IRPT/IRPT_FNTEND/task-orders/IRPT_FNTEND.TO-FE-s-90.suite-completion-checker-refuses-timeout-and-crash.md`
BEFORE the `complete` flip. The judgment criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT`. Result file `suite-completion-checker-refuses-timeout-and-crash.result.md` beside it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no scheduled producer among this order's surfaces.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM-gated resource is written.
comp-adversary: RUN at L4 on PRD v0.10 (both L4-R halves SIGNED, prd-signoff.py status ADMITTED).
the design: RUN by the issuer -- REMEDIATION_v11.md @f7546b6aec, the CVO's round-14 review, and ROUND_ANALYSIS.round14.md @8b1b0d6832, all read at HEAD.
the spec: RUN -- PRD FWD-12 ENDPOINT row and the CTO's round-14 analysis, both read at HEAD.
lane: the <paths> block IS the grant.
</preflight>

Seating: round 15, wave 1, slot ~FE-s-90.
