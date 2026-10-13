# ADVI_FIRMBKTS task order -- `FB-j-2` -- THE DISPATCHER'S CHAIN-COMPLETE WARN PRINTS THE CLI'S ERROR TEXT (300 CHARACTERS), AND NOTHING ELSE CHANGES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~72</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a shell function body only; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act and no grant; the check stubs `aws` as a shell function.
comp-adversary: RUN by the issuer -- `r7_emit_test.sh` (4 arms) reads 1 of 4 at the original base, 3 of 4 on the already-merged edit (arm E4, the `set -e` arm, FAILS) and 4 of 4 on the corrected reference; `awsdiff` reads OK on the reference and FAIL on a patch that also adds `--region` to another call. Blindness: the stub proves the function's output logic under `set -e`, not the real CLI's text on the runner.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-j-2` (round 7, enrichment item 2, step 1; rows `D1-W65-S1`, `D1-C-S46`)

The dispatcher's chain-close emit, `emit_chain_complete` in `data/black_diamond/scripts/gold/gold_dispatch.sh` (about lines 835-855), runs
`aws events put-events ... 2>&1 | grep -q '"FailedEntryCount": 0'` and, when the test fails, prints a WARN WITHOUT the CLI's own error text,
so nobody has ever read why it fails (it has failed at every chain close since 2026-04-22). You change that function so the WARN carries
the CLI's error text, and NOTHING else. This is the measurement step: it is deployed first, with no region change, so the next chain
prints the real error.

### 1a. The edit (ONE file: `data/black_diamond/scripts/gold/gold_dispatch.sh`, inside `emit_chain_complete` only)

**State you start from:** an earlier worker's edit (commit `e33708f50b`) is ALREADY in your tree: the function captures the call's output in
`out`, prints the WARN with `rc=<rc>` and the first 300 printable characters, and keeps the success predicate and line. It has ONE defect, which
you correct: the dispatcher runs under `set -e` (`gold_dispatch.sh` line 57), and the line

    out=$(aws events put-events --entries "file://$entries_file" 2>&1); rc=$?

is a plain assignment, so when put-events FAILS the script EXITS at that line (no WARN; the CDN invalidation, the recon harness and the
`SHUTDOWN_ARMED` step after it are skipped). The original code tested inside an `if`, which `set -e` exempts.

1. Change that one line to the command-list form `set -e` exempts:
   `out=$(aws events put-events --entries "file://$entries_file" 2>&1) && rc=0 || rc=$?`
2. Nothing else changes: the success predicate (`"FailedEntryCount": 0`), the success line, the WARN format
   (`  WARN: EventBridge chain-complete put-events failed (non-fatal to chain close): rc=<rc> <text>`, `<text>` = the output with every
   non-printable character replaced by a space, first 300 characters), and the function still returns 0.
3. No `--region`, no `AWS_DEFAULT_REGION`, no new variable outside the function; no other line of the script changes.

### 1b. Rules

1. Your two checks are issuer files, already written: `bash org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_emit_test.sh <the script>` (4 arms against a stubbed `aws`; arm E4 runs the function under `set -e`) and the diff bound (AC2). Do not edit them. ASCII only; keep the file's line endings as they are.
2. `bash -n` the script after your edit. Run AC1 BEFORE your edit once (expect 3 of 4, E4 FAIL), then after (4 of 4).

## 2. BOUNDS

1. One commit of the script only (plus your rows and instance). No deploy, no push, no AWS call.
2. If the function does not look as described, STOP before editing and file a BLOCKING row.

## 3. SURFACES

<paths>
data/black_diamond/scripts/gold/gold_dispatch.sh
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~72/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~72/ADVI_FIRMBKTS.TO-FB-j-2.dispatcher-warn-text.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-2"><invocation>cd /c/dev/wk-firmbkts-72 &amp;&amp; timeout 60 bash C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_emit_test.sh data/black_diamond/scripts/gold/gold_dispatch.sh</invocation><expect>^EMIT TEST: 4 of 4 arms$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-j-2"><invocation>cd /c/dev/wk-firmbkts-72 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py awsdiff --root /c/dev/wk-firmbkts-72 --file data/black_diamond/scripts/gold/gold_dispatch.sh</invocation><expect>^AWSDIFF: OK$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-j-2"><invocation>cd /c/dev/wk-firmbkts-72 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-72 --allow data/black_diamond/scripts/gold/gold_dispatch.sh --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~72/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the function test against a stubbed `aws`, AC2 the diff bound (every other `aws` line byte-unchanged, hunks inside the function only), AC3 the write-surface bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~72/ADVI_FIRMBKTS.TO-FB-j-2.dispatcher-warn-text.proof_of_spec.json`. Commit the script edit FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W72-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-6 analysis section 2 item 1 ("measure first, no write") and ADDENDUM 1; the SSM route to the runner is barred by its manifest (row D1-S44), so the measurement is this text-only deploy, read from the next chain (FB-j-3). Class WORLD by the path floor (a production pipeline script); the change moves no served output. The two bash checks and `r7_checks.py awsdiff` are the issuer's, dry-run at the base and on a reference patch (L5_FACTS).

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-13 ~09:3xZ) -- RE-OPENED: THE SET -E DEFECT (row `D1-S45`, found by `0.7.0_AE_CloudOps~FB1` before any deploy):** the dispatcher runs under `set -e` (`gold_dispatch.sh` line 57). The merged edit (`e33708f50b`, worker `~69`) wrote `out=$(aws events put-events ... 2>&1); rc=$?`, a plain assignment, so when put-events FAILS (the very failure this order measures) the script EXITS at that line: no WARN, and the CDN invalidation, the recon harness and `SHUTDOWN_ARMED` after it are skipped. The original test sat inside an `if`, which `set -e` exempts. The issuer's check sourced the function WITHOUT `set -e` and could not see it: the check had a blind spot, now closed as arm E4 (the function runs under `set -e` with a failing stub; the marker after the call and rc 0 must both appear). **The correction (one line, inside `emit_chain_complete`):** `out=$(aws events put-events --entries "file://$entries_file" 2>&1) && rc=0 || rc=$?` (a command list with `||` is exempt from `set -e`). Everything else of the merged edit stays. The worker re-seated for this amendment is `0.9.0_WK_ADVI_FIRMBKTS~72` (a finished worker is not resumed): its prior state is the merged commit e33708f50b; it commits the one-line correction on top. AC1 now reads `EMIT TEST: 4 of 4 arms` (base 1 of 4; merged e33708f50b 3 of 4; the corrected reference 4 of 4, dry-run by the issuer). AC2 and AC3 are unchanged. A criterion edit of the issuer's own order and a re-open of a complete order; GATE viii reads `<placeholders>NONE</placeholders>` and no token.

<status>complete</status>
<round>7</round>
<workstream>EXECSUMFIX</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-2</to_id>
<slot>~72</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
