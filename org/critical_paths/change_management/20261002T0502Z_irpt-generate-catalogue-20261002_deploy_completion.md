# Deploy Completion Record
**Date opened:** 2026-10-02T05:02:56.692867+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261002T060404Z
**Deploy:** irpt-ycharts-generate whole bundle at CLOUD 97eaff05ff (item 18: the catalogue reads etf-classifications once per window) and the catalogue route GET analysis/comparisons on the api root; never-widen packet, both halves
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | re-pin the irpt-ycharts-generate source-map row to the pin, build-and-upload, read the uploaded object back by version, member census against the live function | artifact sha256 and S3 version; downloaded by version, hash equal; census | re-pinned at 97eaff05ff (@02626fa6fb, 83 staged entries); built at 775a387b4c: sha256 E+FqSWwETrwJ9Gd1JZwvB/VY7xZNSpjt6WUPRt/clmE=, 570086 bytes, S3 version rtq1e9oTWYgCvsz8F0wgjoeEOw7dcTZr downloaded BY VERSION, hash equal; census vs live arC65KbDPPss: 112 members, 100 identical, 12 changed, 0 added/removed; built members equal the pin except fixtures/har/report.pdf (read by no reachable module); reach from generate_installed: of 8 changed .py only comparison_catalogue and recipe reachable, recipe's change unreachable (step_read_back has no reachable caller) (CATALOGUE/census_irpt-ycharts-generate.json) | CLOSED 20261002T052555Z |
| D1 | verify | ONE targeted safe-apply of the generate function after both halves | apply output; CodeSha256 equals the built hash; a re-plan of the same target reads no changes | targeted plan (CATALOGUE/plan_d1_generate.txt): 1 change, only last_modified, s3_object_version J52XmUEj..->rtq1e9oT.., source_code_hash arC65KbD..->E+FqSWwE..; HALT_ACK=1 safe-apply of the saved plan after the gate listed 40 routine items (none STOP-class): Modifications complete after 6s, Apply complete 0/1/0 (apply_d1_generate.txt); CodeSha256 E+FqSWwETrwJ9Gd1JZwvB/VY7xZNSpjt6WUPRt/clmE= LastModified 2026-10-02T05:54:19Z Active Successful (d1_readback.json); re-plan of the same target: No changes (replan_d1_generate.txt) | CLOSED 20261002T055527Z |
| D2 | verify | ONE targeted safe-apply of aws_apigatewayv2_route.irpt for GET /api/scoped/investor-reporting/analysis/comparisons after both halves | apply output; get-routes shows the route on the portal API with the authorizer; a re-plan reads no changes | targeted plan (CATALOGUE/plan_d2_route.txt): 1 to add, route GET /api/scoped/investor-reporting/analysis/comparisons on 7k3ed8px20, CUSTOM naqxlm, target integrations/wtho3v4; served-reads check between D1 and D2 (SERVED_READS_AFTER_D1_20261002.json): POST analysis own firm INVALID_INPUT and foreign firm FIRM_BINDING, SAME as SERVED_READS_AFTER_GENERATE_20261001; HALT_ACK=1 safe-apply: Creation complete id bh7ynom, Apply complete 1/0/0; get-route bh7ynom reads the key, CUSTOM, naqxlm, integrations/wtho3v4 (d2_get_route.json); re-plan: No changes | CLOSED 20261002T060109Z |
| V1 | verify | served read-back as svc-irpt-analysis: GET analysis/comparisons lists the model entries and named tickers; POST analysis (empty body) and the upload route answer as before | the route outputs, read for values before commit | as svc-irpt-analysis 06:01Z (CATALOGUE/V1_CATALOGUE_20261002.json): GET analysis/comparisons?selected_tenant=cottonwood x3 -> HTTP 200, catalogue_version v1, 341 entries (model_catalogue 4, etf_classifications 337) each; selected_tenant=inflection -> UNAVAILABLE FIRM_BINDING; server Duration by order 719.63 ms (the Scan), 220.64 and 259.61 ms (inside the window, no Scan), 90.84 ms (refusal); no Init Duration (warm). Condition 11 read live | CLOSED 20261002T060404Z |

## Log

- 20261002T050256Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261002T052555Z LEG U1 closed: re-pinned at 97eaff05ff (@02626fa6fb, 83 staged entries); built at 775a387b4c: sha256 E+FqSWwETrwJ9Gd1JZwvB/VY7xZNSpjt6W
- 20261002T055527Z LEG D1 closed: targeted plan (CATALOGUE/plan_d1_generate.txt): 1 change, only last_modified, s3_object_version J52XmUEj..->rtq1e9oT.., 
- 20261002T060109Z LEG D2 closed: targeted plan (CATALOGUE/plan_d2_route.txt): 1 to add, route GET /api/scoped/investor-reporting/analysis/comparisons on 
- 20261002T060404Z LEG V1 closed: as svc-irpt-analysis 06:01Z (CATALOGUE/V1_CATALOGUE_20261002.json): GET analysis/comparisons?selected_tenant=cottonwood 
- 20261002T060404Z CLOSED -- all 4 legs proven
