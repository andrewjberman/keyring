# NFRA_OPLGTW task order -- `OG-ts-1` -- the OG-gp-1 and OG-gf-1 classification pins follow the NFRA_MCPINDEX v2 catalog (round 38 remediation; two tests red at HEAD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ts-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ts-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~122</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- offline tests only; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- a test-maintenance cell: the catalog these tests read changed under them (NFRA_MCPINDEX landed its v2 catalog, `cd2eb0e26f`); the issuer's measurement is in `org/tier1_exec/2.0.0_SA_COO~O/deliverables/CLASSIFIED_ROWS_ABSENT_FROM_V2_CATALOG_20261016.json`.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ts-1` (decomposition addendum R3-T.93, round 38 remediation, workstream ENRICH-R38, FWD-22)

THE DEFECT. Two tests in the gateway suite pass on the tree before NFRA_MCPINDEX's v2 catalog and FAIL at HEAD: `tests/test_og_gp1.py::test_oggp1_ac01` and `tests/test_og_gf1.py::test_oggf1_ac01`. Each pins "the classification names exactly the catalog's ASSIGNED rows": `assigned_rows()` / `_assigned_from_catalog()` take the catalog rows of the portal-v2, mdpf (gp1) and etfs (gf1) buckets that carry NO `read_tool`. In the v2 catalog the rows are linked to tools (`read_tool` is set), so the computed assigned set is EMPTY while the classification files (`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~109/CLASSIFICATION.json` for gp1, the gf1 one beside `tests/test_og_gf1.py`'s `W`) still name 32 and N rows. The issuer measured: of gp1's 32 classified rows, 14 are still in the catalog (all now with `read_tool`) and 18 are ABSENT from it (list in the measurement file above).

THE FIX (tests only; the catalog is NFRA_MCPINDEX's file and the classification files are history). Rewrite the two pins to the new truth with the smallest edits that keep their INTENT (the classification must not silently diverge from the catalog):
1. The classification keys are a FROZEN set (read them from the classification file) and each key is, at HEAD, exactly one of: (a) present in the catalog with a `read_tool` that names a registered tool (`app/tools.py`), or (b) absent from the catalog and listed by name in a new constant `ABSENT_FROM_V2_CATALOG` in the test with the measurement file's list (for gp1; do the same for gf1 with its own measured list).
2. Nothing else may be unaccounted for: a classified key neither in (a) nor (b) fails the test (so a future catalog change that drops or renames a row again is caught, not absorbed).
3. Keep the count assertions in step with the truth (`len(cls) == 32` for gp1 stays 32 as the frozen set size; add the counts of (a) and (b)).
Do NOT delete the tests, do NOT loosen them to `>=`, do NOT change the catalog or the classification files. Add one difference-control test per file (`test_ogts1_control_gp1`, `test_ogts1_control_gf1` inside the same files or a new `tests/test_og_ts1.py`): an in-process planted classification key that is in neither (a) nor (b) makes the pin FAIL (assert the pin helper reports it).
Print, in your report, the two lists (a) and (b) for each file by entity name, and the full gateway suite's failing-id count before and after (`cd infra/aws/ec2/opal-gateway && python -m pytest tests -q -p no:cacheprovider`): the two ids leave the failing set and nothing enters it.

## 2. BOUNDS

- Write only the files in `<paths>`. No app code, no catalog, no classification file, no release.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; weaken a test; print an account number or a person's name.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/tests/test_og_gp1.py
infra/aws/ec2/opal-gateway/tests/test_og_gf1.py
infra/aws/ec2/opal-gateway/tests/test_og_ts1.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~122/`. Rows: id `NFRA_OPLGTW-Z-W122-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`; a row's `disposition` is one of `UNDER_INVESTIGATION`, `GRADUATED`, `DISMISSED_WITH_REASON` (the last needs a `dismissal_reason`), `DECOMP_INVALIDATING`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ts-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/ts1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)gp1 and gf1 suites: pytest rc=0; passed [1-9]\d*; failed 0 \(want 0\); named: ac01 pins 2 of 2, controls [1-9]\d* \(want 1 or more\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ts-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r38/checks/_wkbound.sh 0.9.0_WK_NFRA_OPLGTW~122 '^infra/aws/ec2/opal-gateway/tests/test_og_(gp1|gf1|ts1)\.py$'; echo "exit=$?"</invocation><expect>(?s)write-set bound for 0\.9\.0_WK_NFRA_OPLGTW~122: files touched [1-9]\d*; product files [1-9]\d*; outside the allowed set 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: both gp1 and gf1 suites pass, both `ac01` pins pass, and the difference controls exist and pass. `AC2`: the commits of this serial touch only those test files.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ts-1.tests-follow-the-v2-catalog.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once (commit hashes, the two AC lines, the (a)/(b) lists, the suite failing-id counts before and after).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 38 remediation (found at the OG-ng-3 A1 re-seat: `ng3.AC2` reads FAIL in the main tree at HEAD, 9 passed 2 failed, since the MCPINDEX v2 catalog landed). Workstream ENRICH-R38 (decomposition addendum R3-T.93). The v2 catalog dropped 18 of the 32 rows OG-gp-1 classified; whether those drops are intended renames is NFRA_MCPINDEX's answer (asked of `2.0.0_SA_COO~MI`); this cell makes the pins honest either way.
- Pre-cut: ts1.AC1 base FAIL as expected (the two ac01 tests fail at HEAD); ts1 AC2 base FAIL as expected (no commit of this serial yet).

<status>complete</status>
<round>38</round>
<workstream>ENRICH-R38</workstream>
<slot>~122</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
