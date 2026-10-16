# AMGT_HARVST task order -- `HVST-cc-4` -- ROUND 88, workstream BBG-CAUSE: THE `bbg` PAGE CLOSURE IS TRACED ON ONE LOCAL LEG AND ITS CAUSE IS NAMED (CTO round-87 analysis, item 4)

<!-- ===================== SEAT FACE -- read by 0.7.0_AE_CloudOps~SC1 ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cc-4.the-bbg-page-closure-is-traced-to-its-cause</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cc-4</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- this cell changes NO scheduled task: the registered `Opal Data Harvest - Continuous Cycle` is neither stopped, started nor re-registered by this order.
comp-iam: RUN at L5 -- the leg reads the stored `bloomberg/session` secret exactly as the runner's own `bbg` job did (`token_source secrets:bloomberg/session`); NO Google credential, NO Kimi key, NO sign-in, NO S3 write, NO Terminal or queue use (`ledger/CTO_CONDITION_C-i_BLOOMBERG_READ_HERE_20261015.md`: the `bbg` harvest is the bloomberg.com web session, not the Terminal).
comp-adversary: RUN at L5 -- the adversary is a trace that cannot tell the two closers apart (so it names the wrong one), a control that fails for the same reason as the case (so it proves nothing), and a leg that costs the account more vendor calls than the budget.
</preflight>

## 0. THE CELL

Branch G took `bbg` out of the dell1 runner (`ledger/ROUND87_BBG_BRANCH_G_PRESS_AND_HOLD_20261016.md`): two jobs on one article (`/opinion/articles/2026-10-15/bp-can-solve-its-debt-problem-once-and-for-all`, run records `20261016T081953Z-run-44138fa3` and `20261016T083553Z-run-6f00a52f`) each got a `403` of class `bot_check` signature `bloomberg_press_and_hold`, then `TargetClosedError: Locator.count: Target page, context or browser has been closed`. Not measured: WHO closed the page, the vendor's challenge page or this runner (the window is minimised by `tab_transport.TabSession._minimize_window` through the debug protocol, `HVST-cb-5`). The CTO ruled (round-87 analysis, `ledger/ROUND_ANALYSIS.round87.md`): `bbg` stays out of the list; this cell runs ONE traced local leg and names the closer; read-only for the schedule; no Terminal or queue use; no new vendor leg.

## 1. START CONDITIONS (read at the start; any false: DO NOT START, file one row, and the issuer reads it)

- (a) `<main>` is `C:\dev\ajb_workspace`; `<pin>` is `C:\dev\wk-harvest-runner-pin-ddd7dcdc38` (the registered task's `WorkingDirectory`); read both, do not assume.
- (b) The failing security file exists: `<main>\.runtime\harvest-cycle\state\cycles\bbg\securities\security-7f993eb1cab6b5ea.json`; and a security whose `bbg` job ended `no_new_articles` exists in the same folder, `security-b0fe721e1f2a0d8b.json` (the first job of the 08:11Z leg), as the control.
- (c) The runner is whatever it is: this cell never stops, starts or edits it, and takes no stop file. `HVST-cc-5` (`task-orders/AMGT_HARVST.TO-HVST-cc-5.wsj-and-barrons-run-their-first-productive-dell1-cycles.md`) is held by `0.7.0_AE_CloudOps~HV1`, which re-registers the runner (its steps 1 to 3) and holds it; this cell never touches the runner, its stop file or its scheduled task, so it can run at once and in parallel; the two never touch the same file or process.

## 2. THE ACT (dell1, `<pin>` as the working directory)

1. Fix a scratch runtime root `<main>\.runtime\cc4-bbg-trace\runtime` (new, empty; never the runner's `<main>\.runtime\harvest-cycle\runtime`) so the trace touches neither the runner's `progress.sqlite3` nor its ledger. Never run `upload-harvest`; no S3 write of any kind.
2. Read `tab_transport.py`, the `bbg` contract in `contracts.json` and the runner's own spawn of a job (`backfill_driver.Collector._spawn`) at `<pin>`, and write the exact command line the runner used for the failed job, copied from the log or the process record, in `cc4_command.txt`. Your legs run THAT command with only `--runtime-root` changed (and the security file changed for the control).
3. **Arm A (the case, as the runner ran it):** the failed job's security file, window minimised as the runner sets it, with a trace that records WHO ends the page: at least (i) the vendor response for the article request (status, class, signature), (ii) the page's own `close` and `crash` events and the context's `close` event with a monotonic timestamp each, (iii) whether `_minimize_window`'s `Browser.setWindowBounds` call returned before the closure and its timestamp, (iv) the exception and the line that raised it, (v) the browser process's exit state. Write the harness you need as a small script in your deliverables folder and say what it hooks; do NOT edit any file under `<pin>` (it is a locked worktree).
4. **Arm B (the difference control):** the SAME job with the minimise call DISABLED (`TabSession(..., minimize=False)` or the equivalent switch you find at `<pin>`; say which), so the only difference from Arm A is the window state. If the closure persists in Arm B the runner's minimise is not the closer; if it vanishes, it is.
5. **Arm C (the positive control):** the control security (`security-b0fe721e1f2a0d8b`), Arm A's settings. It must end without an error (`no_new_articles` or `new_articles`); if it errors the same way, the harness or the account is at fault, not the article, and you stop and write that.
6. **Budget:** at most 3 job runs in total (one per arm) and no retry of an arm. Stop at once, and write it, on any `429`, a `login_redirect`, a sign-in prompt, or a vendor message about the account; do not sign in by any hand and do not send any key.
7. Write `cc4_trace.out` (see PROOF OF SPEC) with, per arm, the lines above and a final block:
   `CLOSED_BY=<vendor_page|runner_minimise|runner_timeout|other>`, then `EVIDENCE=` lines (the monotonic timestamps and events that decide it), `CONTROL_ARM_C=PASS|FAIL`, `ARM_B_DIFFERS=yes|no`, and `NOT_ESTABLISHED=` for anything the three runs could not separate. If the arms do not separate the causes, `CLOSED_BY=other` with the reason: a named inconclusive result is a result.
8. Write `cc4_budget.out` with `JOBS_RUN=<n>` (1 to 3) and the three run ids.
9. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Commit your files with `.tools/safe-commit.sh`.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round88/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round88/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cc-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round88/cc4_trace.out</invocation><expect>(?m)^CLOSED_BY=(vendor_page|runner_minimise|runner_timeout|other)$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cc-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round88/cc4_trace.out</invocation><expect>(?m)^CONTROL_ARM_C=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cc-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round88/cc4_budget.out</invocation><expect>(?m)^JOBS_RUN=[1-3]$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base the three files do not exist (all FAIL as expected). AC2 can read `FAIL` only if the harness or the account is at fault; then the cell stays `pending` and the issuer reads your note.
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cc-4.the-bbg-page-closure-is-traced-to-its-cause.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cc-4.the-bbg-page-closure-is-traced-to-its-cause` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cc-4.the-bbg-page-closure-is-traced-to-its-cause.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-87 analysis (`ledger/ROUND_ANALYSIS.round87.md`, msg 6766), item 4 and the section "bbg: the cause, as a named cell"; C-i (`ledger/CTO_CONDITION_C-i_BLOOMBERG_READ_HERE_20261015.md`) and C-j stand. `bbg` stays OFF the schedule; a fix is a later cell, "proven on one leg".
- The three arms are the difference control the CTO's wording asks for ("names which closed the page: the press-and-hold challenge, or the runner's own timeout or close"). The minimise call is the one runner-side action that touches the window during a job (`tab_transport.py:101-121`, `HVST-cb-5`); Arm B removes only it.
- Z-S32 (2026-09-27) already measured a hard-refusal regime on the site Z box (search 403 while the session check 200); that is the vendor-side prior, not a finding of this cell.
- **Not covered, named:** a fix (a handler that skips the article and keeps the job); re-adding `bbg` to the runner; a human solving the challenge; the Bloomberg Terms of use at this cadence (not read).
- **SENT:** with the round-88 issuance.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>88</round>
<workstream>BBG-CAUSE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
