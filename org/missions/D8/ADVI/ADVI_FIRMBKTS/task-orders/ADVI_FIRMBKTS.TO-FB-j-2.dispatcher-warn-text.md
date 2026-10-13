# ADVI_FIRMBKTS task order -- `FB-j-2` -- THE DISPATCHER'S CHAIN-COMPLETE WARN PRINTS THE CLI'S ERROR TEXT (300 CHARACTERS), AND NOTHING ELSE CHANGES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~69</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a shell function body only; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act and no grant; the check stubs `aws` as a shell function.
comp-adversary: RUN by the issuer -- at the base `r7_emit_test.sh` reads 1 of 3 (E2 passes as a control; E1 and E3 FAIL as expected); on a reference patch it reads 3 of 3; `awsdiff` reads OK on the reference patch and FAIL on a patch that also adds `--region` to another call. Blindness: the stub proves the function's output logic, not the real CLI's text on the runner.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-j-2` (round 7, enrichment item 2, step 1; rows `D1-W65-S1`, `D1-C-S46`)

The dispatcher's chain-close emit, `emit_chain_complete` in `data/black_diamond/scripts/gold/gold_dispatch.sh` (about lines 835-855), runs
`aws events put-events ... 2>&1 | grep -q '"FailedEntryCount": 0'` and, when the test fails, prints a WARN WITHOUT the CLI's own error text,
so nobody has ever read why it fails (it has failed at every chain close since 2026-04-22). You change that function so the WARN carries
the CLI's error text, and NOTHING else. This is the measurement step: it is deployed first, with no region change, so the next chain
prints the real error.

### 1a. The edit (ONE file: `data/black_diamond/scripts/gold/gold_dispatch.sh`, inside `emit_chain_complete` only)

1. Capture the call's combined output in a variable (`out=$(aws events put-events --entries "file://$entries_file" 2>&1); rc=$?`).
2. The success predicate is unchanged: the output contains `"FailedEntryCount": 0`; the success line is unchanged.
3. On failure print ONE line: `  WARN: EventBridge chain-complete put-events failed (non-fatal to chain close): rc=<rc> <text>` where
   `<text>` is the output with every non-printable character (newlines included) replaced by a space and cut to its first 300 characters.
4. The function still returns 0 (non-fatal). No other line of the script changes. No `--region`, no `AWS_DEFAULT_REGION`, no new variable
   outside the function: the region change is a LATER cell.

### 1b. Rules

1. Your two checks are issuer files, already written: `bash org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_emit_test.sh <the script>` (3 arms against a stubbed `aws`; at the
   base it reads 1 of 3) and the diff bound (AC2). Do not edit them. ASCII only; keep the file's line endings as they are.
2. `bash -n` the script after your edit.

## 2. BOUNDS

1. One commit of the script only (plus your rows and instance). No deploy, no push, no AWS call.
2. If the function does not look as described, STOP before editing and file a BLOCKING row.

## 3. SURFACES

<paths>
data/black_diamond/scripts/gold/gold_dispatch.sh
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~69/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~69/ADVI_FIRMBKTS.TO-FB-j-2.dispatcher-warn-text.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-2"><invocation>cd /c/dev/wk-firmbkts-69 &amp;&amp; timeout 60 bash C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_emit_test.sh data/black_diamond/scripts/gold/gold_dispatch.sh</invocation><expect>^EMIT TEST: 3 of 3 arms$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-j-2"><invocation>cd /c/dev/wk-firmbkts-69 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py awsdiff --root /c/dev/wk-firmbkts-69 --file data/black_diamond/scripts/gold/gold_dispatch.sh</invocation><expect>^AWSDIFF: OK$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-j-2"><invocation>cd /c/dev/wk-firmbkts-69 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-69 --allow data/black_diamond/scripts/gold/gold_dispatch.sh --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~69/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 is the function test against a stubbed `aws`, AC2 the diff bound (every other `aws` line byte-unchanged, hunks inside the function only), AC3 the write-surface bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~69/ADVI_FIRMBKTS.TO-FB-j-2.dispatcher-warn-text.proof_of_spec.json`. Commit the script edit FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W69-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 to AC3 outputs and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-6 analysis section 2 item 1 ("measure first, no write") and ADDENDUM 1; the SSM route to the runner is barred by its manifest (row D1-S44), so the measurement is this text-only deploy, read from the next chain (FB-j-3). Class WORLD by the path floor (a production pipeline script); the change moves no served output. The two bash checks and `r7_checks.py awsdiff` are the issuer's, dry-run at the base and on a reference patch (L5_FACTS).

<status>pending</status>
<round>7</round>
<workstream>EXECSUMFIX</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-2</to_id>
<slot>~69</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
