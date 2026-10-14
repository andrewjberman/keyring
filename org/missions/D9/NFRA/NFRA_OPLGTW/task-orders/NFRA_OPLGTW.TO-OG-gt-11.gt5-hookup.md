# NFRA_OPLGTW task order -- `OG-gt-11` -- the hookup of the published-analysis tool: registration, SAFE and NATIVE lists, the two re-pinned counts

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-11</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-11</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~91</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: DECLARED-NOT-APPLICABLE -- this cell registers and counts a tool already merged; it adds no AWS call and changes no IAM. The invoke grant (`harvest_published_invoke_iam.tf`) is Phase A of the release order that carries this tool.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the G1 plan (OG-gt-5 rides its own ask) of decomposition addendum R3-T.50 and PRD v3.0 (FWD-22).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-11` (decomposition addendum R3-T.59, workstream GT5-HOOKUP, FWD-22)

The hookup of the published-analysis tool `harvest_get_published_analysis` (build OG-gt-5, merged `640c8a55f7`; module `app/harvest_published.py`, scope seam `app/typed_scope.py` merged with OG-gt-6): the `tools.py` registration, the `SAFE_TOOLS` and `NATIVE_TOOLS`
entries, the registry count 88 -> 89 and the non-data count 79 -> 80. Registration belongs to no tool cell (CUT BY WRITE SET), so this cell is the one place it lands. Applied by the issuer's prepared script.

1. **Apply the prepared hookup.** From your worktree root run:
   `python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_gt5.py infra/aws/ec2/opal-gateway`. It makes exactly these edits and nothing else:
   - `app/tools.py`: one import line after the G3 + G6 import (`harvest_published as _hvpub`) and ONE `@mcp.tool()` registration after `news_for_security`:
     `return _run("harvest_get_published_analysis", {...}, lambda t: _hvpub.harvest_get_published_analysis(security_key, sections))`;
   - `app/data_entitlement.py`: the name into `NATIVE_TOOLS` (read class, `legacy`; NOT `DATA_GRANT_TOOLS`); `app/destructive_ops.py`: the name into `SAFE_TOOLS`;
   - `tests/test_entitlement_admin.py`: the registry count pin 88 -> 89; `tests/test_data_entitlement_family.py`: the non-data count pin 79 -> 80, in the assertion and in its two comments.
   If the script refuses (an expected line has moved), STOP, file a BLOCKING row naming the file, and change nothing by hand.
2. **Check the registration's arguments match the module function** (`security_key: str, sections: str = "overlay"`). A mismatch is a BLOCKING row; do not edit the module (not in your `<paths>`).
3. **Run, in `infra/aws/ec2/opal-gateway`:** `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py`, `tests/test_data_entitlement_guard.py`, `tests/test_og_gt5.py` and `tests/test_og_gt6.py`. The only failure allowed is `test_ogz1_ac08`, which is in `tests/baseline/failing_ids_full.txt`. Print the pass and fail counts.
4. Commit the five files only. The commit-time naming gate and the non-ASCII WARN are expected to print; neither may be overridden.

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py` and the pinned-count tests are NOT yours: the issuer
  registers every tool and re-pins the counts at the merge, in one commit. Do not edit them; name the registration you
  expect in your report.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address, or an object's
  text body into a report, a row or a log; write the catalog file (`app/refs/DATA_CATALOG.yaml` is NFRA_MCPINDEX's alone);
  override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/app/destructive_ops.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_family.py
infra/aws/ec2/opal-gateway/tests/baseline/failing_ids_full.txt
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_gt5.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~91/`. Rows: id `NFRA_OPLGTW-Z-W91-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-11"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt11.AC1.sh; echo "exit=$?"</invocation><expect>(?s)tools registered in app/tools\.py: 1 of 1.*entitlement-admin suite \(the registry count pin is 89\): passed 9 of 9, failed lines 0, rc 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-11"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt11.AC2.sh; echo "exit=$?"</invocation><expect>(?s)classified: SAFE 1 of 1, NATIVE 1 of 1, in DATA_GRANT_TOOLS 0 \(want 0\); files outside this cell's five \(and its records\) 0 \(want 0\).*pytest rc=0; named tests passed 1 of 1; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the tool is registered and the registry count test passes at 89.
- `AC2`: the name is classified read-class, none in DATA_GRANT_TOOLS, nothing outside the five files changed, and the non-data family test passes at 80.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-11.gt5-hookup.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the signature check result and the pass and fail counts of step 3.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream GT5-HOOKUP (decomposition addendum R3-T.59). The gateway app files are in lane CLOUD_OPS_OR_ETL, which the COO cannot commit: a worker order grants them. Rides its own release after `OG-ap-19`.
- Script dry-run by the issuer on HEAD copies of the five files before the cut. Pre-cut: gt11.AC1 and gt11.AC2 base FAIL as expected (0 of 1 registered, 0 of 1 classified).

<status>pending</status>
<round>37</round>
<workstream>GT5-HOOKUP</workstream>
<slot>~91</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
