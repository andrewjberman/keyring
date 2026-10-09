# NFRA_OPLGTW task order -- `OG-ab-1` -- take dell2 ADVI_BILLING packet E2 (copy_site_file_to_s3) onto box/sitez and build its required carry; NO release

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ab-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ab-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~47</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a code build on a branch; nothing is deployed, applied, scheduled or invoked. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE -- the IAM file `advi_billing_gateway_iam.tf` rides in from the packet unapplied; this cell reads and applies no policy. Its plan and apply belong to the later release cell under a never-widen pair.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is `1.0.0_SA_CTO~Z`'s ruling msg 32663 (TAKE, on COO~O's rec) on dell2 COO~B2's packet `org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~7/RELEASE_PACKET_E2.md` @9828e7761f (relay MSTR~Z msg 32658).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ab-1` (decomposition addendum R3-T.34)

dell2's ADVI_BILLING built one new gateway WRITE tool, `copy_site_file_to_s3`, which copies one SharePoint `.xlsx` to
the bronze `fee_statement` prefix by a conditional put. Site Z ships it in a later release, after r29 and NFRA_MCPINDEX
MX-r-9. This cell puts the code on box/sitez and builds what the packet says is missing. It does NOT cut a release.

READ the packet first, all of it:
`MSYS_NO_PATHCONV=1 git show 9828e7761f:org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~7/RELEASE_PACKET_E2.md`.
Gateway root: `G` = `infra/aws/ec2/opal-gateway/`. Commit `931774fb11` (the module and its tests) is already on box/sitez.

1. **Take the registration commit's code, nothing else.** `git cherry-pick -n e8290dd5fe`, then restore from the
   index and the tree every path outside `<paths>` (the commit also carries
   `org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~7/AB_R3_PLAN.txt` and an ADVI_BILLING
   surprise-channel edit; those stay dell2's). Keep: `G/app/tools.py`, `G/tests/test_advi_site_to_s3_registration.py`,
   `infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf`. Commit, naming `e8290dd5fe` as the source.
2. **The required carry (row ADVI_BILLING-D2-W7-S1), exactly as the packet's section 2 states:**
   - `G/app/destructive_ops.py`: `DESTRUCTIVE_OPS["copy_site_file_to_s3"]`, class `WRITE_REVERSIBLE`, native undo =
     delete the written key, conditional put so it never overwrites, `blast_dimensions: ["files:1"]`; and
     `TOOL_WRITE_CLASS["copy_site_file_to_s3"] = "write_files"`. Follow the `upload_text_to_site` entries' shape.
   - `G/app/data_entitlement.py`: the name in `NATIVE_TOOLS`.
3. **The env line (packet section 3).** In `G/deploy-to-ec2.sh`, the single `.env` printf (~line 417): add
   `ADVI_FEE_STATEMENT_S3_ROOT=%s\n` to the format and one trailing argument `"${ADVI_FEE_STATEMENT_S3_ROOT}"`, and compute
   that variable earlier in the script from `lib/opal_naming.py` `address("smartx","49financial","bronze","fee_statement","quarter=X")`
   with `quarter=X` removed. It is never typed as a literal. Fail closed (exit non-zero before any write) if it is empty
   or does not end in `/bronze/fee_statement/`.
4. **Tests**, `G/tests/test_og_ab1_carry.py`, offline, named exactly `test_ogab1_ac01` (the two destructive_ops
   entries), `test_ogab1_ac02` (NATIVE_TOOLS), `test_ogab1_ac03` (the printf carries the key from the variable, and
   `address()` with `quarter=X` removed ends in `/bronze/fee_statement/`). Style: `G/tests/test_data_entitlement_family.py`.
5. Run every gateway suite that imports `destructive_ops` or `data_entitlement` whole, in its own process, and report
   pass counts before and after. A test that fails only because the tool count moved (e.g. 42 -> 43) is updated to
   the new count and named in your report. Never weaken an assertion.

## 2. BOUNDS

- No release, deploy, plan, apply or upload. The `.tf` file arrives unapplied and stays so.
- No edit to the module `site_to_s3.py` or its round-2 tests; a defect there is a row, not a fix.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into your branch (row Z-W41-S5); override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/tests/
infra/aws/terraform/opal-gateway/advi_billing_gateway_iam.tf
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~47/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W47-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ab-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ab1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 3 of 3; failed/error lines 0.*tests/test_advi_site_to_s3\.py: pytest rc=0.*tests/test_advi_site_to_s3_registration\.py: pytest rc=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ab-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/ab1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)copy_site_file_to_s3 registered in tools\.py: 1 \(want 1\); listed unclassified: 0 \(want 0\); census reports 0 unclassified: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the carry exists and is pinned; the packet's own suites still pass.
- `AC2`: the new tool is registered and classified, so the gateway will not fail-close it.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~47/`.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ab-1.advi-billing-e2-carry.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the suites' counts before and after; any test updated for the tool count; commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- CTO~Z ruling msg 32663: TAKE dell2 packet E2 after r29 and MX-r-9; the worker builds the required carry; a later
  release cell runs under its own never-widen pair (CTO~Z + COO~O, CVO for the widening); 0.7.0_AE_CloudOps~Z applies.
- This cell is the build only, cut now because it depends on nothing (width); the release cell follows MX-r-9.
- Pre-cut: ab1.AC1 base FAIL as expected (test_og_ab1_carry.py and the registration test absent; test_advi_site_to_s3.py
  27 passed); ab1.AC2 base FAIL as expected (tool not registered; census 42 of 42 classified).

<status>pending</status>
<round>33</round>
<workstream>ADVI-E2</workstream>
<slot>~47</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
