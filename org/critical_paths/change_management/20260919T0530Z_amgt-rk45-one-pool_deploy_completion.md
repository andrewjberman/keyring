# Deploy Completion Record
**Date opened:** 2026-09-19T05:30:47.160153+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T061943Z
**Deploy:** AMGT-rk-45: compute_pool newest-object-per-name + one pool write + adapter no-as_of redeploy
**Authored by:** 0.9.0_WK_AMGT_RESAPP~47
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | management/v1/_pool/<as-of>.json | read-back of the written pool object matching AC3's dry line byte-for-byte | python -m lib.research.management.enrich --pool-only --as-of 2026-09-19 --write-pool: OK: uploaded s3://opal-data-harvest/management/v1/_pool/2026-09-19.json content-length 216 read-back sha256 dee6a647358af0ca. Read-back verify: document-sha256 dee6a647358af0ca matches; body {as_of:2026-09-19, pool_avg_tenure_years:4.09, pool_denominator:{names_in_union:250,names_with_roster:7,officers_with_role_start:40}, universe_vintage:2026-09-16} equals AC3's dry POOL line byte-for-byte in every field. Pre-act key was ABSENT (404, no pre-act bytes -- filed AMGT_RESAPP-Z-W47-S1); post-act management/v1/ key count 15 = pre-act 14 + this one new key, every other key unchanged (listed and diffed). | CLOSED 20260919T054128Z |
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | HALT-GATE: 182 routine (non-STOP, none AMGT-related) pending messages surfaced; HALT_ACK=1 re-run acknowledged and proceeded. TF apply -target=module.scoped_amgt_api.aws_lambda_function.this -auto-approve: Apply complete! Resources: 0 added, 1 changed, 0 destroyed. Post-apply get-function-configuration: CodeSha256 baiKT5I+k7ciCX/rtQzYy7bTSWgApSeAXYtSZhe4fUE= (pre-act OOsJzs7BDkgtOUogdG39/BZNw3PlRrLatxCFVI528qY=), LastModified 2026-09-19T06:14:41.000+0000, LastUpdateStatus Successful -- matches build-and-upload-scoped-amgt.sh local sha256 exactly. s3 VersionId Av11PsPOZh87INPUaV10ic2t4Gd8MtAf. Targeted 0-diff replan: terraform plan -target=module.scoped_amgt_api.aws_lambda_function.this: 'No changes. Your infrastructure matches the configuration.'. Verify-on-served: 8 of 8 GET routes on opal-amgt-scoped-api invoked live post-act (lead-panel/rankings, lead-panel/timeseries, watchlist, security/{key}/overlay,thesis,peers,coverage,print) -- 0 FunctionError, 0 5xx (2 expected-shape 400s on the lead-panel routes' movement-param validation, 6x 200). AC5 (this order's own criterion): BA_US_Equity (2026-09-15 object) and NU_US_Equity (2026-09-18 object) BOTH serve pool_object_key management/v1/_pool/2026-09-19.json, SAME pool_avg_tenure_years 4.09, SAME pool_denominator {names_in_union:250,names_with_roster:7,officers_with_role_start:40}; planted HOLLOW_NONEXISTENT_KEY_Equity serves management_status ABSENT, pool_avg null. NOTE: the module currently mounts 8 GET + 3 POST = 11 routes total (not 13); POST routes (watchlist/star, watchlist/unstar, refresh) were NOT invoked (mutating / vendor-call-adjacent, out of this order's BOUNDS). | CLOSED 20260919T061926Z |

## Post-close correction (0.9.0_WK_AMGT_RESAPP~47, 2026-09-19 ~06:2xZ)

The closed leg's "NOTE: the module currently mounts 8 GET + 3 POST = 11 routes total (not 13)" was measured
against `module.scoped_amgt_api`'s own Terraform OUTPUT BLOCK only, which is a partial list. Querying the LIVE
API Gateway directly (`aws apigatewayv2 get-routes --api-id 7k3ed8px20 --query "Items[?contains(RouteKey,
'amgt')].RouteKey"`) returns **16 routes: 13 GET + 3 POST** -- matching the rk-19/rk-43 precedent's "13 of 13 GET
routes" shape exactly (the 5 routes the module output omits: `compare`, `versions`, `lists`, `freshness`,
`ledger`). Re-ran verify-on-served against all 13 live GET routes post-act: `security/BA_US_Equity/{compare,
versions,print,peers,coverage,overlay,ledger,thesis}`, `lead-panel/{timeseries,rankings}/up/BA_US_Equity`,
`watchlist`, `lists`, `freshness` -- **13 of 13 invoked, 0 FunctionError, LOST=[]** (11 of 13 statusCode 200; the
2 lead-panel routes return statusCode 400 on the placeholder movement value `up`, an expected parameter-validation
shape, not a crash). This supersedes the closed leg's route count; the leg's PASS verdict is unaffected (its own
proof requirement was TF apply + 0-diff replan + sha match + verify-on-served, all of which held under either
count).

## Log

- 20260919T053047Z OPENED by 0.9.0_WK_AMGT_RESAPP~47 with 2 leg(s)
- 20260919T054128Z LEG L1 closed: python -m lib.research.management.enrich --pool-only --as-of 2026-09-19 --write-pool: OK: uploaded s3://opal-data-harves
- 20260919T061926Z LEG opal-amgt-scoped-api closed: HALT-GATE: 182 routine (non-STOP, none AMGT-related) pending messages surfaced; HALT_ACK=1 re-run acknowledged and proce
- 20260919T061943Z CLOSED -- all 2 legs proven
