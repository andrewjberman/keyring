# ADVI_FIRMBKTS task order -- `FB-j-4` -- THE PUT-EVENTS CALL TAKES ITS REGION FROM ONE VARIABLE, EVENTS_REGION; NO OTHER CALL CHANGES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R7.md</decomp_doc>
<owned_cells>FB-j-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~71</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a shell variable and one call's argument; no cron, rule, schedule or cadence is added or changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS act and no grant; the checks read the script text.
comp-adversary: RUN by the issuer -- at the base `r7_region_test.sh` reads 1 of 3 (R3 passes as a control) and on a reference patch 3 of 3; `awsdiff` reads OK on a good patch and FAIL on a patch that also adds `--region` to another call. Blindness: the text checks prove the argument, not the CLI's resolution on the runner.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-j-4` (round 7, enrichment item 2, step 2; the CTO's ruling, ROUND_ANALYSIS.round6.md ADDENDUM 1 item 2)

Once `FB-j-3`'s measured text names the cause, the dispatcher's `put-events` call takes its region from ONE variable and NO other call in the
script changes how it resolves a region. **Not a global export.** `export AWS_DEFAULT_REGION` at the top would change the region resolution
of EVERY call in the chain and widens the blast radius; the CTO refused it.

### 1a. The edit (ONE file: `data/black_diamond/scripts/gold/gold_dispatch.sh`)

1. Define ONE variable at the top of `emit_chain_complete` (or immediately above it): `EVENTS_REGION="${EVENTS_REGION:-us-east-1}"`.
   The value `us-east-1` is the event bus's own region, read live by the issuer at the cut from the bus ARN
   (`arn:aws:events:us-east-1:313476888478:event-bus/default`, `events describe-event-bus --name default`); it is typed here ONCE, in this one
   line, with that provenance in a one-line comment above it. It is overridable by the environment.
2. The `put-events` call becomes `aws events put-events --region "$EVENTS_REGION" --entries "file://$entries_file"` (the capture and the WARN
   text of `FB-j-2` stay). It is the ONLY call in the script that names a region.
3. No `AWS_DEFAULT_REGION`, no `AWS_REGION`, no `aws configure`, anywhere. Every other line of the script stays byte-unchanged.

### 1b. Rules

1. Your checks are issuer files: `bash org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_region_test.sh <the script>` (3 arms; base 1 of 3: R3 passes as a control), `bash org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_emit_test.sh <the script>`
   must still read 4 of 4 (the stub tolerates the extra argument), and `r7_checks.py awsdiff` (every other `aws` line byte-unchanged). Do not
   edit them. `bash -n` the script.

## 2. BOUNDS

1. One commit of the script only (plus rows and instance). No deploy, no push, no AWS call.
2. **Sequencing (the CTO's condition on the dry-run pair, `NEVER_WIDEN_ROUND7_EXEC_SUMMARY_DRYRUN_DEPLOY_CTO_HALF.md`):** this change is the TRIGGER that makes chain-complete reach EventBridge; once it is DEPLOYED the next chain serves up to 158 client-facing summaries. Merging it to the branch is fine; it is NOT deployed to `code/gold/` by anyone until the dry-run sample (`FB-j-6`) has been read by the CTO AND the regeneration pair (`FB-j-7`) is signed on both halves citing that sample. The deploy is `FB-j-7`'s, never this cell's.

## 3. SURFACES

<paths>
data/black_diamond/scripts/gold/gold_dispatch.sh
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~71/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~71/ADVI_FIRMBKTS.TO-FB-j-4.events-region.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-j-4"><invocation>cd /c/dev/wk-firmbkts-71 &amp;&amp; timeout 60 bash C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_region_test.sh data/black_diamond/scripts/gold/gold_dispatch.sh</invocation><expect>^REGION TEST: 3 of 3 arms$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-j-4"><invocation>cd /c/dev/wk-firmbkts-71 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round7/checks/r7_checks.py awsdiff --root /c/dev/wk-firmbkts-71 --file data/black_diamond/scripts/gold/gold_dispatch.sh</invocation><expect>^AWSDIFF: OK$</expect></criterion>
  <criterion id="AC3" cell_refs="FB-j-4"><invocation>cd /c/dev/wk-firmbkts-71 &amp;&amp; timeout 60 python C:/dev/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-71 --allow data/black_diamond/scripts/gold/gold_dispatch.sh --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~71/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md</invocation><expect>^ROUND 4 SCOPE: OK [0-9]+ changed, 0 outside, 0 required missing$</expect></criterion>
</proof_of_spec>

AC1 reads the three region arms, AC2 the byte-unchanged bound on every other `aws` line, AC3 the write-surface bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~71/ADVI_FIRMBKTS.TO-FB-j-4.events-region.proof_of_spec.json`. Commit the script edit FIRST, your rows and the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W71-S<k>`. Report once: AC1 to AC3 outputs and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PARKED at the cut: owner `2.0.0_SA_COO~B1`; un-park condition: `FB-j-3` read (the measured text names the cause; if it names a DIFFERENT cause the issuer re-cuts this cell on that cause, never on the hypothesis) and `FB-j-2` merged (same file). The CTO's ADDENDUM 1 item 2 replaced the issuer's first proposal (a top-of-file export). The grader's `--region` count of 1 is the byte-unchanged proof for the other calls.

**AMENDMENT 1 (2.0.0_SA_COO~B1, 2026-10-13 ~09:1xZ):** the CTO's ordering (his half of the FB-j-6 pair) is stated in section 2: the edit may merge; the deploy waits for the sample read and the FB-j-7 pair. Un-park condition now also names it: this cell is cut AFTER `FB-j-3` is read, and its merge is not a deploy.

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-14 ~01:3xZ) -- UN-PARKED:** the first BD gold chain after the text-only dispatcher deploy closed at 01:20Z and its WARN line reads `rc=255 You must specify a region. You can also configure your region by running "aws configure".` (class NO_REGION; the issuer's read, `ledger/FB_J_3_ISSUER_READ_20261014.md`; the order record is FB1's). The cause is the one this cell was cut on. `FB-j-2` is merged. Section 2 stands: merging is fine, the deploy is `FB-j-7`'s after the sample read and the signed pair. No criterion changed.

<status>complete</status>
<round>7</round>
<workstream>EXECSUMFIX</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-j-4</to_id>
<slot>~71</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
