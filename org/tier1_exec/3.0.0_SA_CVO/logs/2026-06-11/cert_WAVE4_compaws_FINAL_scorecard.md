# CVO Certification — comp-aws WAVE-4 (53816378a + CVO fix 01bbd166a) — FINAL SCORECARD

**Certifier:** 3.0.0_SA_CVO · **Date:** 2026-06-11 · **Verdict: CERTIFIED — 9/9 new classes at existence-F1 = 1.0 vs live hand-audit oracles; 0 untyped; genuine-dangling 0; GRAIN PASS. One real compiler bug found, fixed, and re-measured in the loop (the cert working as designed).**

## Per-class scorecard (live boto3 oracle vs derive)
| class | derived | live oracle | F1 | note |
|---|---|---|---|---|
| apigw | 6 | 6 | **1.0** | exact ID match |
| api_route | 97 | 97 | **1.0** | **post-fix** — see finding F-W4-1 |
| ecs_task | 2 | 2 | **1.0** | globgrph-nessie + derive-runner, exact |
| ecs_cluster | 1 | 1 | **1.0** | |
| security_group | 16 | 16 | **1.0** | see oracle-lesson OL-2 (multi-region) |
| vpc_endpoint | 3 | 3 | **1.0** | exact ID match |
| ssm_document | 19 | 19 | **1.0** | Self-owned docs |
| scheduler | 3 | 3 | **1.0** | |
| lambda_layer | 13 | 13 | **1.0** | account-owned; 3 external-acct attached layers (AWSSDKPandas, 336392948345) = documented scope boundary, not a miss |
| *(s3 regression)* | 30 | 30 | **1.0** | oracle v1.1 re-snapshot; was false-stale 0.8276 |

Structural bars: **0 untyped** · **genuine-dangling 0** (wildcard/transient-exempt, via the stitch's shared definition) · **GRAIN-SENTINEL PASS** on the complete derive.

## F-W4-1 — REAL COMPILER BUG (found by this cert, fixed, re-measured)
`live_api_routes`/`live_apigw` used **unpaginated** apigatewayv2 `get_apis`/`get_integrations`/`get_routes` — these default to MaxResults=25 and **silently truncate**. Cost: **38/63 routes + their ROUTES_TO integration targets on opal-portal-data-proxy-api** (derived 59 vs live 97; api_route recall 0.61 → F1 0.76, NOT-CERTIFIED). Fix `01bbd166a` (`_apigw_paged` NextToken drain on all 3 calls); re-measured live: **97/97 routes, 63/63 portal routes w/ integration_uri**. This resolves CTO's "59 live vs 83 TF" puzzle: the 83 TF span 4 gateways; the true live set is **97** (the 59 was the truncation artifact, not multi-env drift).

## Propagation (the fix carried through the whole chain)
Fresh full derive (1330n/3141e/0-untyped/grain-PASS) → snapshot published (`aws-shape_20260611T2130Z-cvo-postpagfix.tar.gz` + latest.txt) → `derive_stitch` re-run → kuzu reload (aws 1330/pipeline 1532/portal 226, unioned 3088n/5223e, 0 dangling) → **AC5 re-confirmed: components-reaching-bucket = 15 (unchanged — honest: the portal-side join was already complete; the +38 routes enrich the AWS serving layer, pipeline→aws edges 840→985)**. COO's "15 likely grows" hypothesis falsified — recorded as-is.

**First production AC-GRAIN.2 firing (the D5 sentinel working day-one):** the re-stitch REFUSED to emit on CLOUDFRONT_DISTRIBUTION 1-vs-4 (0.25×) + SERVICE_PRINCIPAL 15-vs-5 (3.0×). Both investigated + verified live-legitimate (today's CDN decom → only EVTSA9VEHNZVH remains; WAVE-4 CAN_ASSUME typing → 15 real service principals) → baseline re-certified (v2, 35 classes, from the complete graph) → re-run PASS. The violation→investigate→re-baseline workflow held exactly as designed.

## Trade-recon disposition (Andrew-directed, CLOSED)
Fresh derive + `terraform state list` both show **0 trade-recon anywhere** — base-AE's ground-truth confirmed: the 4 "orphans" were **stale-graph phantoms** (incremental-updater never propagated the deletes), not tfstate entries. My earlier state-rm routing was moot (mis-read of the pre-fix derive's drift_class). s3 oracle now 30 = live = derive. The stale Kuzu/Nessie cache clears via the published snapshot + tonight's nightly.

## Oracle-method lessons (banked for the methodology)
- **OL-1:** a `git grep 'resource'` TF count is a LOWER BOUND (count/for_each/name_prefix) — oracle denominators come from terraform-state + live boto3. (Pre-ratified by CTO.)
- **OL-2:** the live-enum oracle must match the compiler's **REGION scope** — my single-region (us-east-1) enum undercounted security_group by the us-east-2 default SG; the compiler (multi-region REGIONS loop) was RIGHT and the oracle wrong. Corrects my earlier "time-skew deletion" read. An oracle disagreement is evidence about *either* side until ground-truthed per-item.
- **OL-3:** grant-vs-usage (CAN_ASSUME/data-access as capability-by-design, usage in the trace graph) — adversarially reviewed, disposition CONFIRMED as documented in NFRA_COMPAWS_SCHEMA §3.13.
- **Brittleness:** real-world perturbation absorbed correctly during the pass itself (CDN decom 4→1 reflected; trade-recon phantoms absent; +10 s3 buckets; AC-GRAIN.2 fired and was dispositioned) — stronger evidence than a synthetic perturbation.

## Disposition
**comp-aws WAVE-4: CERTIFIED.** 9/9 classes existence-F1 1.0 + structural bars green + the certified-13 regression intact (s3 restored to 1.0 on the honest oracle). The cert loop earned its keep: it found a real silent-truncation bug (F-W4-1), fixed it, and re-measured — the build/certify split working as intended. Residual observation for CTO (non-blocking): the unioned graph carries API_ROUTE at two grains (166 portal-derived + 97 cloud-derived, unmerged) — a stitch-join candidate, not a defect.
