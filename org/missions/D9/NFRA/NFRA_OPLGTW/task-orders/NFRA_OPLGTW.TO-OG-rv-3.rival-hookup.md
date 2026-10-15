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

The batch hookup of ten tools whose builds are merged on your HEAD: `etfs_get_peer_group_members`, `etfs_get_rival_fund_holdings`, `etfs_who_holds`, `etfs_get_security_reference`, `etfs_get_coverage` (OG-rv-1, `app/etfs_rivals.py`) and `etfs_get_fund_trades`, `etfs_get_fund_flows`, `etfs_compare_peers`, `etfs_get_research_notes`, `etfs_get_rival_page_status` (OG-rv-2, `app/etfs_rivals_flow.py`): the `tools.py` registrations, the `SAFE_TOOLS` and `NATIVE_TOOLS` entries, the registry count 95 -> 105 and the non-data count 86 -> 96. Registration belongs to no tool cell (CUT BY WRITE SET). Applied by the issuer's prepared script.

1. **Apply the prepared hookup.** From your worktree root run:
   `python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_rv.py infra/aws/ec2/opal-gateway`. It makes exactly these edits and nothing else: one import line after the G5 import (`etfs_rivals as _rv1, etfs_rivals_flow as _rv2`) and ten `@mcp.tool()` registrations after `mdpf_get_category_views`, each
   `return _run("<name>", {<audit args>}, lambda t: <alias>.<name>(<args>))`; the ten names into `NATIVE_TOOLS` (read class, `legacy`; NOT `DATA_GRANT_TOOLS`) and into `SAFE_TOOLS`; the registry pin 95 -> 105 and the non-data pin 86 -> 96 (assertion and comments).
   If the script refuses (an expected line has moved), STOP, file a BLOCKING row naming the file, and change nothing by hand.
2. **Check that every registration's arguments match the module function it calls** (`app/etfs_rivals.py`, `app/etfs_rivals_flow.py`). A mismatch is a BLOCKING row; do not edit a tool module (not in your `<paths>`).
3. **Run, in `infra/aws/ec2/opal-gateway`:** `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py`, `tests/test_data_entitlement_guard.py`, `tests/test_og_rv1.py`, `tests/test_og_rv2.py`. The only failure allowed is `test_ogz1_ac08`, which is in `tests/baseline/failing_ids_full.txt`. Print the pass and fail counts.
4. Commit the five files only. The commit-time naming gate and the non-ASCII WARN are expected to print; neither may be overridden.

## 2. BOUNDS

- Code, tests and your probe only. No release, no deploy, no IAM or Terraform change, no write to any bucket, no grant written.
- The five files of `<paths>` (`app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py`, `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py`) are YOURS for this one cell, through the issuer's script and nothing else: no hand edit, no other file.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name or a full email address, or an object's
  text body into a report, a row or a log; write the catalog file (`app/refs/DATA_CATALOG.yaml` is NFRA_MCPINDEX's alone);
  override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/app/etfs_rivals.py
infra/aws/ec2/opal-gateway/tests/test_og_rv1.py
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
  <criterion id="AC1" cell_refs="OG-rv-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/rv3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)tools registered in app/tools\.py: 10 of 10.*entitlement-admin suite \(the registry count pin is 105\): passed 9 of 9, failed lines 0, rc 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rv-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/rv3.AC2.sh; echo "exit=$?"</invocation><expect>(?s)classified: SAFE 10 of 10, NATIVE 10 of 10, in DATA_GRANT_TOOLS 0 \(want 0\); files outside this cell's five \(and its records\) 0 \(want 0\).*pytest rc=0; named tests passed 1 of 1; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
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

- A1 (issuer, 2026-10-15 ~10:4xZ, worker rows Z-W102-S1..S4, all read): the first seat BLOCKED, rightly. (S1) the provisioned worktree's sparse cone omitted `infra/aws/ec2/opal-gateway` (the provision call carried no `--order`): the ISSUER added the folder to the cone (`git sparse-checkout add infra/aws/ec2/opal-gateway`, the provisioner's own act) and the worker rebuilds nothing. (S2) the proof invocations still named the six-tool `gt12.AC1.sh` and `gt12.AC2.sh` (a template carry-over): they now name `rv3.AC1.sh` and `rv3.AC2.sh`, which grade ten of ten. (S3) accepted: rv3.AC2's outside-files zero is read AFTER your commit, against the base of the branch. (S4) the bounds bullet forbade editing the five files that step 1 directs the script to edit, and the record face carried a duplicate fragment: both repaired. The order is re-issued on the same branch (inherited commit `fac4ca01c3`, a BLOCKED proof instance and rows S1-S4: re-record the instance from the real outputs). Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A2 (issuer, 2026-10-15 ~11:1xZ, found at the issuer's verify of the first complete run): the naming gate in ENFORCE REFUSES the string `etfs_get_peer_group` (3 verdicts, `tools.py:1513`, `data_entitlement.py:148`, `destructive_ops.py:102`: NEW and OUT-OF-PATTERN as IAM_GROUP; the gate types any name ending `_group` as an IAM group). The worker's commit passed only because its sparse cone carried no `org/mcp/naming-gate.enforce` (WARN window, row Z-S142's class); the release commit and the drain are in ENFORCE. RULED: the tool is renamed `etfs_get_peer_group_members` (a probe of eight candidate names against the gate in ENFORCE: only the `_group` ending refuses). The CRO's name `etfs_get_peer_group` is retired for this tool. DO THIS, in your worktree, as the first act: replace the WHOLE WORD `etfs_get_peer_group` with `etfs_get_peer_group_members` in exactly these seven files: `app/etfs_rivals.py` (the function and its internal labels), `tests/test_og_rv1.py`, `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py`, and the two pinned tests only if they name it (they do not today). A word-boundary replace never touches `peer_group` the parameter or `etfs_get_peer_group_members` itself. Then re-run `rv1.AC1.sh`, `rv1.AC2.sh`, `rv3.AC1.sh` and `rv3.AC2.sh` (the issuer's copies already name the new tool) and run the naming gate over your diff by hand: `python .tools/naming-gate.py --diff <your diff vs the branch base> --staged-paths <a file listing your five files plus one path under org/missions/D9/NFRA/NFRA_OPLGTW/> --enforce` (the flag stands in for the sentinel your cone lacks): it must print no REFUSE. Re-record the proof instance. The paths of this order now also name `app/etfs_rivals.py` and `tests/test_og_rv1.py`. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>RIVAL-HOOKUP</workstream>
<slot>~102</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
