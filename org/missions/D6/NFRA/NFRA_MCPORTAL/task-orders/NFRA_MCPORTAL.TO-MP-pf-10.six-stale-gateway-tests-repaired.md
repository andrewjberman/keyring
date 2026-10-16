# NFRA_MCPORTAL task order -- `MP-pf-10` -- WORKSTREAM PF ROUND 7: six stale gateway tests repaired against the landed catalog

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pf-10</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pf-10</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~39</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- two test files; no cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- two test files; no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1 runs the six tests against the real catalog and against a planted empty one; AC3 is the bound that nothing else changed.
EGRESS CLASS, declared: none. Make no network call. The tests use fakes for DynamoDB and the grant store.
</preflight>

## 1. THE CELL -- `MP-pf-10` (workstream PF round 7, decomposition section PF7.1)

Your worktree is `C:/tmp/mp-pf-39`, branch `wk-NFRA_MCPORTAL-39`. Every shell call of yours resets to the primary checkout: begin each call with `cd C:/tmp/mp-pf-39 &&`.
Commit with `.tools/safe-commit.sh --author "0.9.0_WK_NFRA_MCPORTAL~39 <0.9.0_WK_NFRA_MCPORTAL~39@opal.agent>" -F <msgfile> -- <paths>` (message file written with a non-shell writer). Never push. Make NO network call.

**The defect.** Six gateway tests fail at the base (run `cd C:/tmp/mp-pf-39/infra/aws/ec2/opal-gateway && python -m pytest tests/test_admin_gateway_breakdown.py tests/test_admin_people.py -q --color=no -p no:cacheprovider`: 6 failed). The gateway code is correct; the tests are stale. The real `app/refs/DATA_CATALOG.yaml` now declares a source group for every live tool, and `bd.CATALOG_YAML` (module `app/admin_gateway_breakdown.py`, imported in the tests as `app_mods.bd`) defaults to that real file. The tests still assume the old catalog:
- the breakdown `world` fixture patches no catalog, so a planted tool such as `list_calendar` or `send_email` now lands in the `m365` channel (a declared source), not in `undeclared`;
- the people `world` fixture patches only `ap.CATALOG_YAML` (a copy of the path taken at import) and leaves `bd.CATALOG_YAML` real, and the placement rule lives in `bd`;
- the two real-inventory tests pin a channel list that the real catalog no longer yields.

Repair (tests only):
1. `tests/test_admin_gateway_breakdown.py`
   - `test_every_live_tool_in_exactly_one_channel`: before it plants tools, call the file's own helper `_plant_catalog(world, app_mods.bd, "tool_index: []\n")`, so a tool with no spec, declaration or Graph scope reads `undeclared` again. Keep every other assertion as it is; if one of them fails for a reason other than the catalog, stop and file a row.
   - `test_real_server_tool_inventory`: it uses the real catalog (leave that). Replace the pinned `want = sorted(specs) + ["m365"] + ...` list and the pinned `len(body["channels"]) == 5` with invariants derived from the real catalog through `app_mods.bd._group_ids_for_tools(live)` (it returns, per tool name, a list of group dicts with an `id`): (a) every live tool appears in the body exactly once and none is invented (already asserted; keep); (b) the SET of channel ids equals the union of every live tool's group ids; (c) channel ids are unique; (d) an integration channel holds only tools whose active spec has that channel's id (already asserted; keep). Do the same replacement for the count after `register_enabled`: compare `len(body["channels"])` with the size of that union, not 5.
2. `tests/test_admin_people.py`
   - the `world` fixture: record the real catalog path on the namespace before patching (`w.real_catalog = bd.CATALOG_YAML`), then also patch `bd.CATALOG_YAML` to the same empty catalog file it already gives `ap.CATALOG_YAML` (`monkeypatch.setattr(bd, "CATALOG_YAML", str(cat))`). This should restore `test_people_lists_every_candidate_even_holding_nothing`, `test_cadence_reads_absent_with_reason` and `test_people_principal_never_leaks_into_other_fields` without editing their bodies. If one still fails, find out why and fix only its expectation, naming it in your report.
   - `test_real_server_people_inventory`: this test needs the REAL catalog in both modules: set `bd.CATALOG_YAML` and `ap.CATALOG_YAML` to `world.real_catalog` with `monkeypatch`. Replace `allowed_channels = {"m365", "undeclared"} | specs` with the union of the group ids that `groups` (already computed in the test) holds over all tools, plus `specs`. Keep the other assertions.
All other tests in both files keep their names and still pass.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No `app/` file, no catalog, no Terraform, no manifest.
2. Do NOT flip this order's `<status>`: the order file is outside your `<paths>`; the issuer flips it. (This face overrides the worker rule that says to flip.)
3. If a criterion cannot be met without a file outside section 3, REFUSE it with what you measured and file a BLOCKING row. Never edit a check script; they are the issuer's.
4. Do not print or commit any real index name or account number; these tests use planted names only.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/test_admin_gateway_breakdown.py
infra/aws/ec2/opal-gateway/tests/test_admin_people.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~39/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: everything else under `infra/aws/ec2/opal-gateway/` and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id `NFRA_MCPORTAL-Z-W39-S<k>` (k from 1). APPEND ONLY: add your row after the last one and leave every earlier byte untouched (the file carries some Windows line endings; do not rewrite or normalise them).
`surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run after your commits)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pf-10"><invocation>cd C:/tmp/mp-pf-39 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf10.AC1.sh; echo "exit=$?"</invocation><expect>breakdown: .*named tests PASSED 2 of 2.*people: .*named tests PASSED 4 of 4.*breakdown rc=0 people rc=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-pf-10"><invocation>cd C:/tmp/mp-pf-39 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pe/checks/pf3.AC2.sh; echo "exit=$?"</invocation><expect>failed=0; seam test failures=0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-pf-10"><invocation>cd C:/tmp/mp-pf-39 && bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pf/checks/pf10.AC3.sh; echo "exit=$?"</invocation><expect>outside the two test files: 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~39/NFRA_MCPORTAL.TO-MP-pf-10.six-stale-gateway-tests-repaired.proof_of_spec.json`,
run `proof-of-spec-check.py` on it as the worker rules say, and report once, with:
- the check output of AC1, AC2 and AC3;
- the workspace commit hash;
- every assertion you changed beyond the ones named in section 1 (file, test, old, new), or none;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PF round-7 issuance (decomposition v17) from row Z-S67 and A1 to MP-pf-9 (`66a4be01d8`). Checks dry-run at the base (from /c/Users): pf10.AC1 FAIL as expected (breakdown and people each 0 named tests PASSED); pf3.AC2 FAIL as expected (6 failed, 110 passed); pf10.AC3 PASS as expected (a bound; nothing changed yet).
The cell is tests-only, so it is not part of the MP-pf-9 release and never reaches the host by itself. The status flip is the issuer's.

<status>pending</status>
<status>complete</status>
<round>7</round>
<workstream>PF</workstream>
<slot>~39</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
