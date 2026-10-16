# NFRA_OPLGTW task order -- `OG-ad-1` -- the five client_* tools are the DATA-GRANT class, master_admin only (PRD v3.14 @f2b066d9ad; PRD v3.1 Ruling 2; CVO refusal row Z-S162)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ad-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ad-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~113</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests; no deploy, no schedule. The release is the later applier order OG-ap-23.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; this narrows who may call five tools.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling in PRD v3.14 @f2b066d9ad ("the five client_* tools go into DATA_GRANT_TOOLS AND TIER_ADMITTED_TOOLS, so they are master_admin only; the served negative arm: an unprofiled, non-admin Opal principal calling client_get_holdings is refused with 0 reads") on the ratified PRD v3.1 Ruling 2 ("Every client_* tool goes in DATA_GRANT_TOOLS, never NATIVE_TOOLS ... Being an Opal user is not enough for client data") and the CVO's refusal of the OG-ap-23 half (`deliverables/3.0.0_SA_CVO~Z/NEVER_WIDEN_HALF_CVO_OG-ap-23_20261016.md`).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ad-1` (decomposition addendum R3-T.87, workstream CLIENT-ADMISSION, FWD-22)

Today the five tools `client_resolve_account`, `client_get_holdings`, `client_get_transactions`, `client_get_allocation` and `client_get_fees` sit in `NATIVE_TOOLS` of `infra/aws/ec2/opal-gateway/app/data_entitlement.py` (lines ~158-162, "read class, legacy: Opal principals only"), so any Opal user passes. Ruling 2 forbids that. The model to copy is `blackdiamond_list_fees`: it is in `INDEX_TOOLS` (class legacy), in `DATA_GRANT_TOOLS` and in `TIER_ADMITTED_TOOLS`; `decide()` (line ~668) denies an unprofiled principal a `TIER_ADMITTED_TOOLS` member unless the resolved tier is master_admin, and a profiled principal is confined on `DATA_GRANT_TOOLS` (passes only if its active grant names the tool, or the tier is master_admin).

1. In `app/data_entitlement.py`: move the five names OUT of `NATIVE_TOOLS` into a new `frozenset` `CLIENT_TOOLS`; keep them CLASSIFIED (add `CLIENT_TOOLS` to the union that builds `TOOL_CLASSES` with `CLASS_LEGACY`, exactly as `INDEX_TOOLS` is, so none becomes `tool_unclassified`); make `DATA_GRANT_TOOLS = frozenset(SCHWAB_TOOLS) | frozenset({"blackdiamond_list_fees"}) | CLIENT_TOOLS` and `TIER_ADMITTED_TOOLS = frozenset({"blackdiamond_list_fees"}) | CLIENT_TOOLS`. Update the comments that name the data-grant family (the block at lines ~196-209 lists its members) to name the five and cite this order. Change nothing else in the module.
2. Tests, named, in a new `tests/test_og_ad1.py` (use the `de.Access(False, None, None, frozenset())` form of `tests/test_og_bd2.py` for an unprofiled principal; read `tests/test_og_bd2.py` and `tests/test_og_bd3.py` as the model):
   - `test_ogad1_ac01`: each of the five is in `DATA_GRANT_TOOLS` and in `TIER_ADMITTED_TOOLS`, in none of `NATIVE_TOOLS`, and `classify()` is not None for each.
   - `test_ogad1_ac02`: an unprofiled principal with tier STANDARD_EMPLOYEE, READ_ONLY and tier unknown (None) is denied each of the five (`entitlement_denied`).
   - `test_ogad1_ac03`: an unprofiled principal with tier MASTER_ADMIN passes each of the five (`decide` returns None).
   - `test_ogad1_ac04`: a principal with an ACTIVE profile whose grant does not name the tool is denied each of the five unless its tier is MASTER_ADMIN (build the profile and grant the way `tests/test_og_bd3.py` does).
   - `test_ogad1_ac05`: nothing else moved: the five `schwab_*` tools and `blackdiamond_list_fees` keep their class and their decisions, and every other tool of `NATIVE_TOOLS` is still outside `DATA_GRANT_TOOLS` (compare the family set with the pre-change set plus exactly the five).
3. Pins: `tests/test_data_entitlement_family.py` pins the non-data tool count (`len(non_data) == 113` and its comments "discovery: all 113 non-data tools" / "the profile denies none of the 113"). The five leave the non-data set, so the pin becomes 108 and the comments follow (113 to 108). Change only those numbers. Do NOT change `tests/test_entitlement_admin.py` (the registered-tool count 122 is unchanged) and do NOT touch `app/tools.py` or `app/destructive_ops.py`.
4. Run the entitlement suites (`ad1.AC2.sh` runs them): `test_data_entitlement_family`, `test_entitlement_admin`, `test_og_bd2`, `test_og_bd3`, plus your new file; any other entitlement test that pins the five in `NATIVE_TOOLS` is yours to update to the new truth and name in the report.

## 2. BOUNDS

- `app/data_entitlement.py`, `tests/test_og_ad1.py`, the pin numbers in `tests/test_data_entitlement_family.py`, and the record files. No other module, no release, no deploy, no IAM.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test to make it pass; print an account number or a person's name; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/data_entitlement.py
infra/aws/ec2/opal-gateway/tests/test_og_ad1.py
infra/aws/ec2/opal-gateway/tests/test_data_entitlement_family.py
infra/aws/ec2/opal-gateway/tests/test_og_bd2.py
infra/aws/ec2/opal-gateway/tests/test_og_bd3.py
infra/aws/ec2/opal-gateway/tests/test_entitlement_admin.py
infra/aws/ec2/opal-gateway/app/tier.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

You WRITE only `data_entitlement.py`, `tests/test_og_ad1.py`, `tests/test_data_entitlement_family.py` (the numbers), the files under `W/` and the investigation file (append rows only if you hit a surprise); the rest you only READ (an entitlement test elsewhere that must follow, you name in the report and the issuer adds it to the order). `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~113/`. Rows: id `NFRA_OPLGTW-Z-W113-S<k>` (continue after your last), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ad-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ad1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)data-grant class: in DATA_GRANT_TOOLS 5 of 5; in TIER_ADMITTED_TOOLS 5 of 5; in NATIVE_TOOLS 0 \(want 0\); classified 5 of 5.*decide\(\): unprofiled standard_employee denied 5 of 5; unprofiled read_only denied 5 of 5; unprofiled master_admin passes 5 of 5.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ad-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ad1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 5 of 5; failed/error lines 0.*entitlement suites: pytest rc=0; passed \d+; failed 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the five tools are the data-grant class and master_admin-only for an unprofiled principal. `AC2`: the five named tests pass and the entitlement suites that pin the sets still pass.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ad-1.client-tools-data-grant-class.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, every test you had to update and why).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream CLIENT-ADMISSION (decomposition addendum R3-T.87). My hookup (`d398a799bc` and the first hookup `09ba70ca30`) placed the five client tools in `NATIVE_TOOLS` by the default pattern, and I signed the COO half of OG-ap-23 without reading Ruling 2 (PRD v3.1 lines 1144-1146); the CVO refused its half on it (row Z-S162, ARMED on me). The CTO ruled the fix in PRD v3.14 @f2b066d9ad: master_admin only until a per-firm grant shape exists.
- After this merges, the issuer names a new `trunk_sha` for the OG-ap-23 re-cut (which also carries the CTO's tar-line fix, msg 34787), and `OG-ap-23`'s served read gains the negative arm.
- Pre-cut: ad1.AC1 and ad1.AC2 base FAIL as expected (the five are in NATIVE_TOOLS; the test file is absent).

<status>pending</status>
<round>37</round>
<workstream>CLIENT-ADMISSION</workstream>
<slot>~113</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
