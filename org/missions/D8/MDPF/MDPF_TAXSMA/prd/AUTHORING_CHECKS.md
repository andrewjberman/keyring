# MDPF_TAXSMA L4 authoring checks

Author `1.0.0_SA_CTO~A`, 2026-09-15. These checks support the new PRD's shape and declared interfaces. They do not certify an implementation. The standing CVO certificate remains limited to the original 24-cell documentary rectangle; this supplement does not change its packet, verdict or exclusions.

## Canonical shape and coverage

`authoring-checks.json` records the final check time and exact ID sets. The author imported the existing `.tools/to-pipeline-gate.py` `_prd_conformance` and `.tools/prd-manifest-gate.py` `grade` functions, supplying the checked-in PRD header schema and the project's D8/laptop identity. Both returned no violations. The first check correctly refused the proposal's bold outcome headings because they were not canonical FWD card definitions. Only those heading layouts were normalized to `FWD-n` followed by two spaces; DONE WHEN, ACCEPT and SOURCE text remains byte-identical to the approved pin after that documented layout transformation. No outcome, threshold or approval changed and no gate was altered.

The author separately compared expected S01-S18 to actual rows, D01-D08 to all dependency references, checked the dependency graph for cycles, and compared manifest primary components to the full owned set. All eight FWD IDs have owned rows. The pinned brief has nine top-level headings and eight nested outcome headings; the PRD maps all 17, including non-outcome status context. These are structural and authorial coverage checks. Independent CVO/CRO content reviews remain required.

## Supplemental source checks after documentary certification

| Check | Measurement | Boundary |
|---|---|---|
| CVO terminal placement | `certification.json@b79ced9360cae48123f50812a7515915c38254fb`, author CVO, exactly equals its signed source at `9af8072cd827e3d4871f6fcfeca845185f3a4162`; SHA-256 `e54cb35c39646a15146573cc3e18f4c57c27fa4a9222d8d943a152a034c3bea7` | Empty certified patch set; only dry-derived consumable is eligible. Run/index closure at `717f49f6ea`; zero terminal deviations/violations. |
| `comp-routes trace /api/general/mdpf/49financial/category-views.json` and Global equivalent | Two actual `.json` paths resolve in the desired static route model to portal-v2 `platinum/mdpf/<scope>/category-views.json` with auth-validator-edge/public-data-router/cache-control-injector | Earlier scratch traces omitted `.json` and are not cited as the actual consumer route. Neither desired trace measures deployed edge versions, actual authorization or served content. |
| `comp-cache collisions` | 634 files / 119 useQuery calls fully scanned, 17 shared keys, zero type mismatch/unparseable calls | Does not cover every hook family or the accessor's TTL behavior. |
| `comp-iam service opal-gateway` | Three calls, all resource-unresolvable, desired plane | 473 TF files/three trees; 27 policies unattached in the parser and two deny overlays unparsed. No grant PASS inferred. |
| `comp-iam service mdpf-gold-lambda` | Role view with 11 statements | Not an operation census. New exact-source/runtime-role access remains part of implementation proof. |
| `comp-iam service opal-assets-mdpf-portal-publisher` | Seven operations: six resource-unresolvable; one desired GetObject resource mismatch on portal-v2 pointer read | This is a source/declaration finding, not proof of a live denied call. Destination-readback permission is made explicit in the target contract. |
| `.tools/check-lambda-layer-deps` through Python, `--function` Gold and publisher | Each: one function audited, zero FAIL, one OK | Existing declared layer closure; future source/package imports require their own pinned proof. |
| `comp-platinum reverse taxsma_assets` | Zero of 57 payload paths; no indexed producer/route/component | Query routed as FIELD; empty graph result is not an estate absence proof. PRD declares the producer explicitly and requires exact-path/current-capability checks. |
| Canonical builder vectors | 49financial `taxsma_assets` resolves in the firm bucket; Global category Gold resolves in product bucket | Read-only library calls. CTO 96960 resolves stale CANON prose under R7, not a deployment/migration action. |
| Exact proposed file checks | Component manifest records existence, last source commit and current source SHA for every local primary/companion path; portal paths use the portal repository | New paths are proposed, not deployed. Current uncommitted work does not establish prior usable capability. No proposed target file was overwritten by this census. |

## Deployed Gateway existence check

At 2026-09-15T07:31:52Z the author used read-only SSM command `c8fbe036-1c5a-4073-947c-b8fb5eeb7740` on the manifest's Gateway instance `i-07dccb1615503ac99`. A preceding EC2 describe confirmed the live Name tag `opal-gateway` and running state. The command scanned only Python source under `/opt/opal-gateway/app`, recording relative paths, matched token line numbers and file SHA-256. It read no environment file, credential store, token, customer rows or log contents and changed no service or configuration.

Denominator: **43 Python files**. Tokens: `taxsma`, `taxsma-workbook`, `/ms/ingest`, `usedRange`, `read_site_workbook`. The output found Tax-related source and the existing general workbook reader (`tools.py`, deployed SHA-256 `9a95dd96a7a37257dbeb5ae788821d10b6ae9a9f1bbdccbbe9c765a52c826f49`), with no literal `taxsma-workbook` or `/ms/ingest` hit. SSM returned Success / response code 0. This is a bounded token census of the deployed app, meeting the protocol's on-box existence-check form; it does not prove that a dynamic or differently named capability is absent. S01 must read actual route registration before adding a module and reuse an existing usable implementation if found.

The checked-in `ms_ingest.py` precedent is not inferred to be deployed from this result. Its role in this PRD is the owning CTO's approved capability/identity architecture pattern; its structure-only boundary remains unchanged. The new route's content access requires its own named-person activation record.

## Review boundary

No user-facing capability is graded EXERCISED by these checks. No cloud data, workbook, BD roster, deployed function or portal gitlink was changed. The only remote command was a scoped source read. The PRD's future test harness and deployments remain unimplemented. All authoring commits are LOCAL; shared-branch push and production promotion remain under their existing holds.
