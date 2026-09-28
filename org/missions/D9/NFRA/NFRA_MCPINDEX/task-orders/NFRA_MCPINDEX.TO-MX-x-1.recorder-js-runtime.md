# NFRA_MCPINDEX task order -- `MX-x-1` -- the deploy recorder derives its tools and runs its JavaScript CHANGELOG writer under a JavaScript runtime (rows Z-S22 + Z-W7-S2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-x-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~12</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a CI tool repair; no schedule, cron, alarm or monitor.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- two measured rows, one shared cause.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-x-1` (round 3, enrichment item 6, part 1)

**The file:** `infra/aws/lambda/ci/record-terraform-deploy.sh`.

**The defect, measured by the issuer at the cut. Two rows, one cause:**
- At :217-229 the script picks `JSON_TOOL`. It tries `/c/Users/AndrewBerman/.bun/bin/bun` first: a hardcoded,
  device-specific path (row Z-S22). Where that path is absent (site Z), `JSON_TOOL` resolves to `python3`.
- At :808 the CHANGELOG writer runs `"$JSON_TOOL" "$TMPJS_CHANGELOG"`. `$TMPJS_CHANGELOG` is a temp **JavaScript**
  file, written from the heredoc at :571. Under python3 that raises a SyntaxError (row Z-W7-S2).
- The JS itself is valid: `node --check` on the extracted heredoc returns 0.
- The other `$JSON_TOOL` users (:249, :446) branch correctly on python versus JS. Only :808 hands JS to whatever
  `JSON_TOOL` resolved to.

**The fix:**
1. Remove the hardcoded user-home path. Where the script wants bun or node, it DERIVES them with `command -v`.
2. The CHANGELOG writer runs under a JavaScript runtime: `node` or `bun`, found with `command -v`. If neither exists,
   the recorder says so LOUDLY and skips the CHANGELOG write the way it already handles that write's failure. It never
   hands the .js to python.
3. Change nothing else in the recorder's behaviour. Run `bash -n` on the file, then AC1 and AC2. Commit under your
   serial.

## 2. BOUNDS

1. Only `record-terraform-deploy.sh`. No deploy is run with it.
2. No AWS, no push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/lambda/ci/record-terraform-deploy.sh
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~12/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W12-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-x-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/x1.AC1.sh; echo "exit=$?"</invocation><expect>user-home literal paths in infra/aws/lambda/ci/record-terraform-deploy.sh: 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-x-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round3/checks/x1.AC2.sh; echo "exit=$?"</invocation><expect>CHANGELOG writer invocations>=1; started by $JSON_TOOL=0; extracted JS lines>0; node --check rc=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~12/NFRA_MCPINDEX.TO-MX-x-1.recorder-js-runtime.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-2 analysis s.5 item 6 @e4445020f5.
- The CTO listed one tooling cell of four rows. Three mechanical criteria per build TO cannot hold four rows without
  compounding, so it is cut as two cells:
  - MX-x-1 carries Z-S22 + Z-W7-S2, one cause, measured at the cut;
  - MX-x-2 carries Z-W3-S4;
  - Z-W3-S12 (the pytest_named helper) is fixed by the issuer in the round-3 battery's own `_root.sh`: the verdicts
    are read from pytest's `-rA` summary.
- Dry-run at base: x1.AC1 FAIL (2 user-home paths); x1.AC2 FAIL (1 invocation, started by $JSON_TOOL; the JS is 208
  lines and node --check returns 0).

<status>complete -- issuer-graded on CLOUD after the drain @5ca1404ec3 by 2.0.0_SA_COO~MI, 2026-09-28 ~21:4xZ: x1.AC1 PASS (0 user-home paths), x1.AC2 PASS (writer started by $JSON_TOOL=0, node --check rc=0), instance VALID. Worker controls: both checks FAIL on planted mutants. Rows Z-S22 and Z-W7-S2 are remedied by 139a478be4 (disposition at L8). Was: pending.</status>
<round>3</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
