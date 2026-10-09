# TO TCKT_VNEXT.TO-F10-l4 -- the ticket-center build script gains a real build-only mode that writes nothing to S3

<to_id>TCKT_VNEXT.TO-F10-l4</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~5</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>F10</workstream>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL (a build script; its test never touches AWS) | **Decomp cell:** `F10-l-4` |
**outcome_ref:** FWD-6 (deploy hygiene, row TCKT_VNEXT-D2-S7) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~5`. Your worktree is `C:/tmp/tckt-f10-r4` (branch `wk-tckt_vnext-f10-r4`, cut from box/dell2 at the
issuance commit). Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~5 <0.9.0_WK_TCKT_VNEXT~5@opal.agent>" -F
<msgfile> -- <paths>`; write the message file with the Write tool.

### THE CELL

`F10-l-4`. `infra/aws/terraform/ticket-center/build-and-upload.sh` (32 lines) ALWAYS uploads. Tonight a hash-only build overwrote the
live artifact key (row TCKT_VNEXT-D2-S7).

1. When `BUILD_ONLY=1` is set, the script zips and hashes exactly as today, then prints `local sha256 (b64): <hash>`, the
   `lambda_function.py` sha256 (hex), and `BUILD_ONLY: nothing uploaded`. It makes NO `aws` call of any kind, and it exits 0.
2. Without `BUILD_ONLY`, the behaviour is byte-for-byte as today.
3. Also print the `lambda_function.py` sha256 (hex) in the normal path, because the CTO's deploy halves bind that hash.

**Test:** `infra/aws/terraform/ticket-center/tests/test_build_only.sh` (new).
- It puts a FAKE `aws` first on PATH, which appends its argv to a temp log and exits 0.
- It runs the script once with `BUILD_ONLY=1` and asserts the log is EMPTY and the output carries the hex hash and the
  `nothing uploaded` line.
- It runs the script once without `BUILD_ONLY` and asserts the fake `aws` logged an `s3 cp` (the negative control: the fake bites).
- It prints `BUILD-ONLY-TEST-PASS` only if every assertion holds, and exits non-zero otherwise.
- It never reaches real AWS. Assert that the resolved `aws` is the fake one before running.

### ACCEPTANCE

<criterion id="F10-l4-AC1" cell_refs="F10-l-4"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_CHECKS/f10_checks.py f10-buildonly</invocation><expect>F10-BUILDONLY-OK</expect></criterion>
`F10-l4-AC1`: the test exists and prints BUILD-ONLY-TEST-PASS.

<expected_criteria>F10-l4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, your deliverables folder `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~5/`, and
  this order's file (status flip only).
- Never run the script without the fake `aws` first on PATH. Never call AWS.
- No non-ASCII. If you need a row, append it in BINARY mode as `TCKT_VNEXT-D2-W5-S<k>`, keeping its line endings.

<paths>
infra/aws/terraform/ticket-center/build-and-upload.sh
infra/aws/terraform/ticket-center/tests/test_build_only.sh
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_F10.md</decomp_doc> (workstream F10, round 4), cell `F10-l-4`.
<owned_cells>F10-l-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: F10-l4-AC1. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~5/TCKT_VNEXT.TO-F10-l4.build-only-mode.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> F10-l4-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** the check line verbatim, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE.
comp-iam: DECLARED-NOT-APPLICABLE -- the test never reaches AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- the negative control (the fake aws logs s3 cp without BUILD_ONLY) is the adversarial arm.
lane: infra/aws/terraform/** build helper; nothing applied.
</preflight>

Source: row TCKT_VNEXT-D2-S7; the /next-calls --drive assessment of ~02:0xZ (OPTION 2).

# pipeline-override: round 4's issuance covers both worker cells (F10-p-2, F10-l-4); no issuer act rides this order.
