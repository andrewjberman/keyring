# MDPF_TAXSMA L4 authoring checks

Author `1.0.0_SA_CTO~A`, 2026-09-15. These checks support the new PRD's shape and declared interfaces. They do not certify an implementation. The standing CVO certificate remains limited to the original 24-cell documentary rectangle; this supplement does not change its packet, verdict or exclusions.

## Canonical shape and coverage

`authoring-checks.json` records the final check time and exact ID sets. The author imported the existing `.tools/to-pipeline-gate.py` `_prd_conformance` and `.tools/prd-manifest-gate.py` `grade` functions, supplying the checked-in PRD header schema and the project's D8/laptop identity. Both returned no violations. The first check correctly refused the proposal's bold outcome headings because they were not canonical FWD card definitions. Only those heading layouts were normalized to `FWD-n` followed by two spaces; DONE WHEN, ACCEPT and SOURCE text remains byte-identical to the approved pin after that documented layout transformation. No outcome, threshold or approval changed and no gate was altered.

The author separately compared expected S01-S18 to actual rows, D01-D08 to all dependency references, checked the dependency graph for cycles, and compared manifest primary components to the full owned set. All eight FWD IDs have owned rows. The pinned brief has one level-1 title, nine level-2 headings and eight level-3 outcome headings; the PRD maps all 18 of 18, including the title/preamble and non-outcome status context. These are structural and authorial coverage checks. Independent CVO/CRO content reviews remain required.

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

## v0.2 bounded review corrections

CRO notice 96983 refused the v0.1 brief half at `de5ebb73c7`, with grounds in `docs/briefs/sources/MDPF_TAXSMA_L4_BRIEF_REVIEW_v0_1_20260915.md@eda74adacc`. R1 is closed by selecting the reviewer's ATTESTED-only v1 option: §3.3, A03, the coverage summary and the normative membership rule consistently require an explicit dated operator disposition while discovering and retaining new claims automatically. The unused automatic status is removed from the enum. R2 is closed by counting the pinned level-1 title and mapping its preamble, giving 18/18 coverage. The §3.9 activation summary also now spells out Traded, which was already one of the seven authorized projection fields in §3.2 and the normative contract; this does not add a field to the capability.

PRD/manifest are v0.2 and the proposed data contract/wire marker are 0.2.0. The eight approved ENDPOINT cards are unchanged. Only the contract companion's evidence hash is refreshed in the manifest; the historical source census is not reasserted as a new live measurement. Canonical conformance, endpoint equality, owned/dependency completeness, acyclicity and all 18 brief heading mappings were rechecked. The prior 17-heading claim was incomplete and is superseded by this correction, not represented as an earlier PASS. Independent CVO/CRO review of the current package remains required; no runtime test or production activation is claimed.

CVO notice 96985 refused the v0.1 ratified-text half at `8699f4ba7c`, with its sole blocking R1 in `org/tier1_exec/3.0.0_SA_CVO/deliverables/PRD_REVIEW_MDPF_TAXSMA_v0.1_RATIFIED_TEXT_HALF_20260915.md@e53b06bd38`. The final v0.2 CONTRACTS row cites Andrew's superseding `39aae459ed` nearest-$10,000 display rule and retains `fe76e3e036` only for the surviving L1 zero/null visibility rule. Known values alone are rounded; unknown/stale Tax remains a dated exception and canonical values retain cents (N1). The naming row now pins 96960 to its durable `GOVERNING_CONTRACTS.md@48befbfcbf` carrier (N2). N3/N4 remain explicit limits: the review read schedule declarations, not applied schedules, and the CANON owner's future prose amendment is not represented as completed. Neither requires a new cloud action to correct this document. The final contract-row edit was followed by canonical conformance and exact endpoint comparison again; both half hashes in `authoring-checks.json` describe the final v0.2 text.

## L4-R admission

Both current halves are independently SIGNED: CVO at `214982df0b` and CRO at `905d2df375`, against v0.2 `8ab2dc2bc6`. The canonical status oracle reads ADMITTED. The author changed only the PRD header status from DRAFT to RATIFIED; both signed section hashes remain identical. The data contract state metadata changed from PROPOSED_L4_REVIEW to RATIFIED, following this PRD's declared approval mechanism. A parsed comparison proves every other contract field identical to the reviewed pin. The manifest companion hash and final artifact hashes reflect that metadata update. No new rule, endpoint or deployed capability is introduced. `L4_ADMISSION.md` records the signatures, limits and L5 handoff routing condition.


## v0.3 LGIC addendum and review boundary, CTO97152

The v0.3 PRD and 0.3.0 contract carry CTO97115 F1-F3, the gateway source identity from97131, and granted R20 X7/X2 from97126 at9cf4a274db. F2 adds S19 complete typed Silver between S02 and S03; F3 declares both existing served homes as historical addresses and prevents a dual write or migration. All shipped columns/rows and response lineage are retained at the typed boundary, with immutable raw body captures and replay identity that separates the logical snapshot from its acquisition envelope. The contract explicitly labels knowledge_date partitions and no-expiry disposition audit history.

The current candidate was checked again before landing: zero canonical shape/manifest violations; all eight approved endpoint cards byte-identical; all18 brief headings carried;19 owned engines,49 components,9 artifacts; dependencies acyclic. `authoring-checks.json` carries the current half and artifact hashes, while its `prior_v02_admission` is historical. `LGIC_V03_BUILDER_EVIDENCE.json` records every exact artifact constructor attempt and the runtime role output at its stated source vintage.

**CTO97152 authorizes landing and both reviews before the gateway systems row commits.** The source choice is closed as gateway, PLATFORM_SUBSYSTEM, owner D9; COO~G owns its row. S02 states: address() resolves once the systems.json gateway row lands. Any recorded gateway refusal is this build prerequisite, not an unresolved design question or a reason to hold L4-R. Base CTO will rerun conformance when the row is at HEAD. The author has neither modified the registry nor overridden the builder.

Both v0.3 halves require their own current-byte signatures; v0.2 admission is not reused. X7/X2 are already granted, so no new Andrew E1/E2 answer is required. No runtime build, worker issuance, deployment, data read/write or capability activation is certified by this authoring pass. S16 remains a separate named-person activation prerequisite.

## v0.3 L4-R admission, 2026-09-15T17:10:49.777890+00:00

v0.3 is ADMITTED: both current halves SIGNED, CVO at294bd175ce and CRO at1db20a3624, against61748ba2e0. Approval metadata alone is finalized to RATIFIED; signed section bytes and all substantive contract fields remain unchanged. Under CTO97126 the signature hold on L6 is cleared. COO~T owns L5 and its subsequent canonical task-order process. The gateway row and builder readback remain an S02 build prerequisite; S16 remains a separate named-person activation prerequisite. This record does not certify decomposition, runtime implementation or EXERCISED endpoints.

Canonical header/manifest shape checks returned zero violations. Both half hashes are checked against the signed61748ba2e0 text, and parsed contract equality excludes only the state field. The conditional operations.l6_release wording is retained as reviewed; its condition is now satisfied by both signatures. The manifest contract evidence hash and current artifact hashes reflect the metadata update. CRO97161 defers the S19 coverage-index omissions to the next substantive bump only. CVO N5/N6 and activation limits are carried in L4_ADMISSION.md.

## v0.4 Traded-key addendum, 2026-09-15T18:46:25.355797+00:00

Andrew1729cef85e makes existing Traded the automatic live-membership key; f95470f384 still names the Entra identity. No new field or workbook-owner request. The contract separates current live count from dated verified value coverage, uses first-observed UTC history and retains seven-field acquisition/Silver. The attester question and uncommitted active-column proposal are superseded. Identity MATCH is relayed measurement; actual workbook access remains believed but UNMEASURED after the pre-Graph guard refusal. No additional probe or scope change was ordered.

Current documentary checks: zero canonical shape violations; unchanged endpoint cards and source headers/projection/response/Silver;19 surfaces,49 components,9 artifacts,18 brief headings, acyclic dependencies. Artifact addresses/readers/writers, schedules, grants and X7/X2 unchanged. Both halves change and require independent signatures. TRADED_FIELD_ADDENDUM_97192.md carries exact choices/cell map; IDENTITY_ACCESS_PROOF_97190.json distinguishes identity from actual access. No runtime/live capability test claimed.

## v0.5 Gateway repair, 2026-09-15T19:25:50.181639+00:00

CRO97206 signs the v0.4 brief at5e2089e99b; CVO refuses its Gateway row at91875c897c. Independently read both reviews/stamps and canonical WITHHELD status. This revision restores guard ordering before generic /ms/* and validated Entra tid/oid binding, with email designation only and pinned NFRA_OPLMCP/CTO96946/NFRA_OPLGTW counterparts. The non-blocking UTC/session-date note is made explicit and exercised in the required A03 case. A07 includes same-email/different-principal and dispatch-order controls. No live probe was performed.

Both halves change; no reviewer stamp is author-edited. Current checks: zero canonical shape violations,19/49 surfaces/components,18 headings,9 artifacts and acyclic dependencies. Eight endpoint cards and seven-field source/Silver interface unchanged. All artifact definitions, grants and schedules match v0.4. REVIEW_REPAIR_V05.md supplies precise provenance and cell deltas.

## v0.5 L4-R admission, 2026-09-15T19:59:10.238375+00:00

v0.5 is ADMITTED: both independent halves SIGNED/current against5061a43a46, CVO2560f51f83 and CROd4b71666ff. Header/state metadata alone is finalized to RATIFIED; signed halves and every normative contract field remain unchanged. The L4 signature hold is cleared. Canonical release97212 was READ by exact COO~T at19:53:15.906645Z. COO~T owns the L5 v2 recut and subsequent one L6 issuance; the frozen v1 remains historical. This is requirements admission, not implemented or EXERCISED endpoints.

G-A names the existing opalbloomberg account; actual validated tid/oid binding and workbook access remain UNMEASURED until TX-r-3 controlled proof under existing release conditions. No metadata probe, tool widening or access grant is added. CVO N5 carries gateway registry/builder evidence with EN-r-5; N6 leaves the Gold-placement question as a question, preserving96960; N8 carries NFRA_OPLGTW principal-model landing and shared Gateway sequencing. N-1/G-S/G-O/G-W/G-P remain. All seven source fields, Traded/date/count rules, storage addresses and grant scopes remain as signed.

Validated metadata-only change: both signed half hashes unchanged; parsed contract equality excluding only state; zero canonical header/manifest shape violations. Manifest/current artifact hashes updated to the finalized bytes. The source code and all deliberate exercises remain downstream work; neither reviewer signature claims runtime proof. The CRO97218 exact notice, both committed reviews/stamps and broker97212 READ receipt were independently read. No duplicate canonical release was sent after its outstanding row retired normally.
