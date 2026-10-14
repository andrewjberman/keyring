# NFRA_OPLGTW task order -- `OG-pt-4` -- the hookup of the eight G3 portal tools and the five G6 news tools: registrations, SAFE and NATIVE lists, the two re-pinned counts

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pt-4</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-pt-4</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~89</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and tests only; no deploy. The release is NFRA_OPLGTW.TO-OG-ap-18 (the release order this cell rides).
comp-iam: DECLARED-NOT-APPLICABLE -- this cell registers and counts tools already merged; it adds no AWS call and changes no IAM. The grants the G3 and G6 tools need are Phase A of the release order (NFRA_OPLGTW.TO-OG-ap-19).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the G3 and G6 plan of decomposition addendum R3-T.52 (PRD v3.7, FWD-22) and the CTO's Friday set (msg 34198).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-pt-4` (decomposition addendum R3-T.54, workstream G3G6-HOOKUP, FWD-22)

The hookup of the eight G3 portal tools (builds OG-pt-1, OG-pt-2) and the five G6 news tools (build OG-nw-1), all merged on your HEAD: `tools.py` registrations,
the `SAFE_TOOLS` and `NATIVE_TOOLS` lists, the registry count 75 -> 88 and the non-data count 66 -> 79. Registration belongs to no tool cell (CUT BY WRITE SET), so this
cell is the one place it lands. Applied by the issuer's prepared script.

1. **Apply the prepared hookup.** From your worktree root run:
   `python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_g3g6.py infra/aws/ec2/opal-gateway`. It makes exactly these edits and nothing else:
   - `app/tools.py`: one import line after the G1 import (`portal_models as _ptm, portal_macro as _ptc, news_typed as _nws`) and thirteen `@mcp.tool()` registrations after `harvest_get_peers_and_scores`, each
     `return _run("<name>", {<audit args>}, lambda t: <alias>.<name>(<args>))`;
   - `app/data_entitlement.py`: the thirteen names into `NATIVE_TOOLS` (read class, `legacy`; NOT `DATA_GRANT_TOOLS`);
   - `app/destructive_ops.py`: the thirteen names into `SAFE_TOOLS`;
   - `tests/test_entitlement_admin.py`: the registry count pin 75 -> 88;
   - `tests/test_data_entitlement_family.py`: the non-data count pin 66 -> 79, in the assertion and in its two comments.
   The thirteen names: `portal_get_model_positioning`, `portal_get_model_attribution`, `portal_get_market_returns`, `portal_get_market_regime`, `portal_get_macro`, `portal_get_valuation`, `portal_get_security_scan`, `portal_get_pipeline_freshness`, `news_search_articles`, `news_trending_topics`, `news_keyword_intelligence`, `news_market_mood`, `news_for_security`.
   If the script refuses (an expected line has moved), STOP, file a BLOCKING row naming the file, and change nothing by hand.
2. **Check that every registration's arguments match the module function it calls.** For each of the thirteen, read the module function's signature
   (`app/portal_models.py`, `app/portal_macro.py`, `app/news_typed.py`) and compare it with the registration. A mismatch is a BLOCKING row; do not edit a tool module (not in your `<paths>`).
3. **Run, in `infra/aws/ec2/opal-gateway`:** `tests/test_entitlement_admin.py`, `tests/test_data_entitlement_family.py`, `tests/test_data_entitlement_guard.py`, `tests/test_og_hv1.py`, `tests/test_og_gt0.py` to `tests/test_og_gt4.py`,
   `tests/test_og_gt6.py`, and the offline tests of the three modules (`tests/test_og_pt1.py`, `tests/test_og_pt2.py`, `tests/test_og_nw1.py` if present). The only failure allowed is `test_ogz1_ac08`, which is in `tests/baseline/failing_ids_full.txt`. Print the pass and fail counts.
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
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/hookup_g3g6.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~89/`. Rows: id `NFRA_OPLGTW-Z-W89-S<k>`, fabric `site-z`,
disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pt-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/pt4.AC1.sh; echo "exit=$?"</invocation><expect>(?s)tools registered in app/tools\.py: 13 of 13.*entitlement-admin suite \(the registry count pin is 88\): passed 9 of 9, failed lines 0, rc 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pt-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/pt4.AC2.sh; echo "exit=$?"</invocation><expect>(?s)classified: SAFE 13 of 13, NATIVE 13 of 13, in DATA_GRANT_TOOLS 0 \(want 0\); files outside this cell's five \(and its records\) 0 \(want 0\).*pytest rc=0; named tests passed 1 of 1; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: all thirteen tools are registered and the registry count test passes at 88.
- `AC2`: the thirteen names are classified read-class, none in DATA_GRANT_TOOLS, nothing outside the five files changed, and the non-data family test passes at 79.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-pt-4.g3g6-hookup.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if both PASS, and report once. Your report names the signature check result and the pass and fail counts of step 3.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G3G6-HOOKUP (decomposition addendum R3-T.54). Plan: R3-T.52 (PRD v3.7). The hookup the issuer owes at the merge (CUT BY WRITE SET); the gateway app files are in lane CLOUD_OPS_OR_ETL, which the COO cannot commit, so a worker order grants them and no lane escape is taken. Rides `OG-ap-19`.
- Script dry-run by the issuer on HEAD copies of the five files: applied, `py_compile` clean, 65 `@mcp.tool()` after (52 + 13).
- Pre-cut: pt4.AC1 and pt4.AC2 base FAIL as expected (0 of 13 registered, 0 of 13 classified).

<status>pending</status>
<round>37</round>
<workstream>G3G6-HOOKUP</workstream>
<slot>~89</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
