# NFRA_OPLGTW task order -- `OG-gt-12` -- the batch hookup of the five G5 wave A etfs tools and mdpf_get_category_views: registrations, SAFE and NATIVE lists, the two re-pinned counts

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-gt-12</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-gt-12</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~93</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: DECLARED-NOT-APPLICABLE -- this cell registers and counts tools already merged; it adds no AWS call and changes no IAM. The G5 read grant is Phase A of the release order that carries these tools (NFRA_OPLGTW.TO-OG-ap-20).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the G5 wave A plan of decomposition addendum R3-T.52 (PRD v3.7, FWD-22) and the CTO's Friday set (msg 34198).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-gt-12` (decomposition addendum R3-T.61, workstream G5CV-HOOKUP, FWD-22)

The batch hookup of six tools whose builds are merged on your HEAD: `etfs_get_partner_ownership`, `etfs_get_ownership_rollup`, `etfs_get_monthly_report` (OG-et-1, `app/etfs_ownership.py`), `etfs_get_fund_nav_history`, `etfs_get_fund_holdings` (OG-et-2, `app/etfs_funds.py`)
and `mdpf_get_category_views` (OG-pt-5, `app/portal_mdpf.py`): the `tools.py` registrations, the `SAFE_TOOLS` and `NATIVE_TOOLS` entries, the registry count 89 -> 95 and the non-data count 80 -> 86. Registration belongs to no tool cell (CUT BY WRITE SET). Applied by the issuer's prepared script.

1. **Apply the prepared hookup.** From your worktree root run:
   `python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_g5cv.py infra/aws/ec2/opal-gateway`. It makes exactly these edits and nothing else: one import line after the published-analysis import (`etfs_ownership as _eto, etfs_funds as _etf, portal_mdpf as _mdc`) and six `@mcp.tool()` registrations after `harvest_get_published_analysis`, each
   `return _run("<name>", {<audit args>}, lambda t: <alias>.<name>(<args>))`; the six names into `NATIVE_TOOLS` (read class, `legacy`; NOT `DATA_GRANT_TOOLS`) and into `SAFE_TOOLS`; the registry pin 89 -> 95 and the non-data pin 80 -> 86 (assertion and two comments).
   If the script refuses (an expected line has moved), STOP, file a BLOCKING row naming the file, and change nothing by hand.
2. **Check that every registration's arguments match the module function it calls** (`app/etfs_ownership.py`, `app/etfs_funds.py`, `app/portal_mdpf.py`). A mismatch is a BLOCKING row; do not edit a tool module (not in your `<paths>`).
3. **Run, in `infra/aws/ec2/opal-gateway`:** `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py`, `tests/test_data_entitlement_guard.py`, `tests/test_og_et1.py`, `tests/test_og_et2.py`, `tests/test_og_pt5.py`. The only failure allowed is `test_ogz1_ac08`, which is in `tests/baseline/failing_ids_full.txt`. Print the pass and fail counts.
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
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_g5cv.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~93/`. Rows: id `NFRA_OPLGTW-Z-W93-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-gt-12"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt12.AC1.sh; echo "exit=$?"</invocation><expect>(?s)tools registered in app/tools\.py: 6 of 6.*entitlement-admin suite \(the registry count pin is 95\): passed 9 of 9, failed lines 0, rc 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-gt-12"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/gt12.AC2.sh; echo "exit=$?"</invocation><expect>(?s)classified: SAFE 6 of 6, NATIVE 6 of 6, in DATA_GRANT_TOOLS 0 \(want 0\); files outside this cell's five \(and its records\) 0 \(want 0\).*pytest rc=0; named tests passed 1 of 1; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the six tools are registered and the registry count test passes at 95.
- `AC2`: the six names are classified read-class, none in DATA_GRANT_TOOLS, nothing outside the five files changed, and the non-data family test passes at 86.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-gt-12.g5cv-hookup.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the signature check result and the pass and fail counts of step 3.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G5CV-HOOKUP (decomposition addendum R3-T.61). The gateway app files are in lane CLOUD_OPS_OR_ETL, which the COO cannot commit: a worker order grants them. Rides `OG-ap-20`.
- Script dry-run by the issuer on HEAD copies of the five files before the cut. Pre-cut: gt12.AC1 and gt12.AC2 base FAIL as expected (0 of 6 registered, 0 of 6 classified).

<status>complete</status>
<round>37</round>
<workstream>G5CV-HOOKUP</workstream>
<slot>~93</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
