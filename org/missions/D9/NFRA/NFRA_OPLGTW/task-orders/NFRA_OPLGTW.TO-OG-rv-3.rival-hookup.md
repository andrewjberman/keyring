# NFRA_OPLGTW task order -- `OG-rv-3` -- the batch hookup of the ten rival-funds tools: registrations, SAFE and NATIVE lists, the two re-pinned counts

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rv-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-rv-3</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~102</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-22 (not yet cut).
comp-iam: DECLARED-NOT-APPLICABLE -- this cell registers and counts tools already merged; it adds no AWS call and changes no IAM. The read grant for the rival prefixes is already in NFRA_OPLGTW.TO-OG-ap-20's ask.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is decomposition addendum R3-T.70 (PRD v3.7, FWD-22; CTO msgs 34190, 34198).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-rv-3` (decomposition addendum R3-T.70, workstream RIVAL-HOOKUP, FWD-22)

The batch hookup of ten tools whose builds are merged on your HEAD: `etfs_get_peer_group`, `etfs_get_rival_fund_holdings`, `etfs_who_holds`, `etfs_get_security_reference`, `etfs_get_coverage` (OG-rv-1, `app/etfs_rivals.py`) and `etfs_get_fund_trades`, `etfs_get_fund_flows`, `etfs_compare_peers`, `etfs_get_research_notes`, `etfs_get_rival_page_status` (OG-rv-2, `app/etfs_rivals_flow.py`): the `tools.py` registrations, the `SAFE_TOOLS` and `NATIVE_TOOLS` entries, the registry count 95 -> 105 and the non-data count 86 -> 96. Registration belongs to no tool cell (CUT BY WRITE SET). Applied by the issuer's prepared script.

1. **Apply the prepared hookup.** From your worktree root run:
   `python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_rv.py infra/aws/ec2/opal-gateway`. It makes exactly these edits and nothing else: one import line after the G5 import (`etfs_rivals as _rv1, etfs_rivals_flow as _rv2`) and ten `@mcp.tool()` registrations after `mdpf_get_category_views`, each
   `return _run("<name>", {<audit args>}, lambda t: <alias>.<name>(<args>))`; the ten names into `NATIVE_TOOLS` (read class, `legacy`; NOT `DATA_GRANT_TOOLS`) and into `SAFE_TOOLS`; the registry pin 95 -> 105 and the non-data pin 86 -> 96 (assertion and comments).
   If the script refuses (an expected line has moved), STOP, file a BLOCKING row naming the file, and change nothing by hand.
2. **Check that every registration's arguments match the module function it calls** (`app/etfs_rivals.py`, `app/etfs_rivals_flow.py`). A mismatch is a BLOCKING row; do not edit a tool module (not in your `<paths>`).
3. **Run, in `infra/aws/ec2/opal-gateway`:** `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py`, `tests/test_data_entitlement_guard.py`, `tests/test_og_rv1.py`, `tests/test_og_rv2.py`. The only failure allowed is `test_ogz1_ac08`, which is in `tests/baseline/failing_ids_full.txt`. Print the pass and fail counts.
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
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_rv.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~102/`. Rows: id `NFRA_OPLGTW-Z-W102-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rv-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt12.AC1.sh; echo "exit=$?"</invocation><expect>(?s)tools registered in app/tools\.py: 10 of 10.*entitlement-admin suite \(the registry count pin is 105\): passed 9 of 9, failed lines 0, rc 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rv-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt12.AC2.sh; echo "exit=$?"</invocation><expect>(?s)classified: SAFE 10 of 10, NATIVE 10 of 10, in DATA_GRANT_TOOLS 0 \(want 0\); files outside this cell's five \(and its records\) 0 \(want 0\).*pytest rc=0; named tests passed 1 of 1; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the ten tools are registered and the registry count test passes at 105.
- `AC2`: the ten names are classified read-class, none in DATA_GRANT_TOOLS, nothing outside the five files changed, and the non-data family test passes at 96.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rv-3.rival-hookup.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the signature check result and the pass and fail counts of step 3.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream RIVAL-HOOKUP (decomposition addendum R3-T.70, cell `OG-rv-3`). The gateway app files are in lane CLOUD_OPS_OR_ETL, which the COO cannot commit: a worker order grants them. Rides `OG-ap-22`.
- Script dry-run by the issuer on a copy of the gateway tree with the org/standards files beside it before the cut: hookup applied, the two pinned suites pass (13 of 13). Pre-cut: rv3.AC1 and rv3.AC2 base FAIL as expected (0 of 10 registered, 0 of 10 classified).

<status>` tag to
`complete` only if both PASS, and report once. Your report names the signature check result and the pass and fail counts of step 3.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream RIVAL-HOOKUP (decomposition addendum R3-T.70). The gateway app files are in lane CLOUD_OPS_OR_ETL, which the COO cannot commit: a worker order grants them. Rides `OG-ap-20`.
- Script dry-run by the issuer on HEAD copies of the five files before the cut. Pre-cut: gt12.AC1 and gt12.AC2 base FAIL as expected (0 of 6 registered, 0 of 6 classified).

<status>pending</status>
<round>37</round>
<workstream>RIVAL-HOOKUP</workstream>
<slot>~102</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
