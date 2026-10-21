# TO NFRA_SCHWABBF.TO-BF-j7 -- the schwab fan-in fence variant's tag value uses only characters IAM accepts (Terraform text only)

<to_id>NFRA_SCHWABBF.TO-BF-j7</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-21</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>release-tag</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-j-7` (`decompositions/NFRA_SCHWABBF_DECOMP_R6.md`, AMENDMENT 2) |
**outcome_ref:** FWD-1, FWD-6 | **depends_on:** `BF-j-6` (merged)

---

## WORKER FACE

### THE CELL

`BF-j-7` (surprise row `NFRA_SCHWABBF-S11`, raised by `0.7.0_AE_CloudOps~NFRA1` at the live apply of `BF-r-3` step B1). IAM refused `CreatePolicy` for `aws_iam_policy.one_way_fan_in_fence_schwab`: `ValidationError, tags.2 value "one-way fan-in fence (schwab variant)"`. IAM tag values may contain only letters, digits, space and `_ . : / = + - @`; parentheses are refused. The tag is the last line of that policy resource in `infra/aws/terraform/opal-assets/silver.tf` (about line 608): `tags = { System = "OpalAssets", Project = "OPAL_ASSETS", Purpose = "one-way fan-in fence (schwab variant)" }`. The policy does not exist in AWS; nothing else of `BF-j-6` was applied. This cell fixes the value and adds a test that catches the whole class. It edits Terraform TEXT and one test file; it runs no `terraform init`, `plan` or `apply` and no `aws` command.

**Build.**
1. In `silver.tf` change ONLY the `Purpose` value of that one `tags` line to `one-way fan-in fence - schwab variant`. No other line of the file changes (check `git diff --numstat` for the file: 1 added, 1 deleted).
2. In `data/canonical/schwab/tests/test_converter_fan_in_fence.py` add arms whose function names contain `fan_in_fence_tag`: (a) the new policy's tag values (parse the `tags = { ... }` line of the `one_way_fan_in_fence_schwab` resource) each match `^[A-Za-z0-9 _.:/=+@-]*$` and the `Purpose` equals the string above; (b) EVERY literal tag value in `infra/aws/terraform/opal-assets/silver.tf` and in `infra/aws/terraform/canonical-schwab-ec2/monolith-iam.tf` (strings inside a `tags = { ... }` block that contain no `${`) matches that charset, with the count of values checked asserted greater than zero and printed in the assertion message. A value that reads from a variable or local is skipped, not guessed.

### ACCEPTANCE

<criterion id="BF6-j7-AC1" cell_refs="BF-j-7"><invocation>python -m pytest data/canonical/schwab/tests/test_converter_fan_in_fence.py -q -p no:cacheprovider --color=no -k fan_in_fence_tag</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF6-j7-AC1` -- the variant policy's tag value is IAM-legal and every literal tag value of the two roots' files is too.

<criterion id="BF6-j7-AC2" cell_refs="BF-j-7"><invocation>python -m pytest data/canonical/schwab/tests/test_converter_fan_in_fence.py data/canonical/schwab/tests/test_firm_prefix_grants.py data/canonical/schwab/tests/test_schwab_build_pin.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF6-j7-AC2` -- the control: the fence-variant arms (10 at the base), the grant arms (23, including the `terraform fmt` arm) and the build-pin arms (5) still pass with the edited `silver.tf`.

<expected_criteria>BF6-j7-AC1,BF6-j7-AC2</expected_criteria>

Dry-run at the base: AC1 "deselected" (rc 5, no test named `fan_in_fence_tag`) -- FAIL as expected; AC2 `38 passed` -- PASS as expected (a control that must stay green).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit.
- **WORLD floor, nothing applied.** No `terraform init`, `plan` or `apply`, no `aws` command. The re-apply is the NFRA CloudOps lane's act (`BF-r-3` step B1, retried). TIME-CRITICAL: the cutover window is open; do nothing the order does not ask for.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W1-S<k>`; read the investigation file for the highest `W1-S<k>` and use the next; the gate may renumber it). Append the row to `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` at the BYTE level (the file mixes CRLF and LF: do not use the Edit tool on it; insert before the closing `]`; the previous last row gains a trailing comma). Do not weaken the test to pass.

<paths>
infra/aws/terraform/opal-assets/silver.tf
data/canonical/schwab/tests/test_converter_fan_in_fence.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md</decomp_doc> (round 6, AMENDMENT 2), cell `BF-j-7`.
<owned_cells>BF-j-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF6-j7-AC1, BF6-j7-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~1/NFRA_SCHWABBF.TO-BF-j7.fan-in-fence-tag-charset.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF6-j7-AC1,BF6-j7-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the changed line, the `git diff --numstat` line for `silver.tf`, the count of tag values checked, the two pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Terraform text; no schedule.
comp-iam: DECLARED-NOT-APPLICABLE as a tool run -- the cell changes a tag value only and adds no grant (scanned silver.tf and monolith-iam.tf for literal tag values, 2 Terraform files; BLIND: the live IAM plane).
comp-adversary: DECLARED-NOT-APPLICABLE -- finding inlined: the live apply is the only instrument that enforces IAM's tag charset, so the test pins the charset it enforces.
lane: the <paths> block IS the grant.
</preflight>

Source: row NFRA_SCHWABBF-S11 (`0.7.0_AE_CloudOps~NFRA1`, msg 110093); `BF-j-6` merge `988e6b8529`; decomposition round 6.
