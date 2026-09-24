# IRPT completion — CTO session rulings

Authority: AUTHORITY.md, Andrew's direct session open-call/fork delegation recorded at `ecf350639a`. These rulings apply to this completion effort. They do not restart held canonical rounds or replace independent acceptance evidence.

## IRPT-S7-01 — conditional private reporting placement

Date: 2026-09-22. Decider and condition owner: `1.0.0_SA_CTO`, acting under Andrew's explicit session delegation. Raised by COO~M at 21:16:01Z.

**Decision: approve the proposed A2 bucket-placement exception conditionally.** Register the exact exception through `infra/logic/06_CONFORMANCE_LEDGER.md` section 6 before the destination policy becomes writable. CRO owns the existing register carrier. This ruling is the decision record, not a second exception register. The canonical entry identifier and committed carrier must be returned to M/P/Y and their reviewers.

Basis read: `infra/logic/02_DOCTRINE.md` R20, R21 and section 4; conformance ledger section 6 (including its delegated-CTO decider precedent); CONTRACT.md S7; COO~M's 73-line proposal at `C:/Users/AndrewBerman/Desktop/ajb_irpt_m/org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/STORAGE_POLICY_PROPOSAL.md`, SHA256 `23375afbb74ded78d0c2b2c12ec8058067fac0faeadaa9f55b952e138a5c8413` as read. M must preserve a committed proposal before candidate handoff.

The current user delegation authorizes CTO to adjudicate this session fork. Record acknowledgement accurately as **CTO under Andrew's explicit delegation**, linking AUTHORITY.md at `ecf350639a`; do not invent a quote saying Andrew personally approved this particular bucket. No additional user round trip is required for this bounded decision.

### Exact allowed departure

Private reporting artifacts for `49financial`, `cottonwood`, and `inflection` may reside in registered product bucket `opal-data-irpt`, with canonical firm identity retained in every key. This is an A2 placement departure from the normal firm home, not permission to label private data global, change naming grammar, or waive required upstream custody processing.

Exactly these eleven families are in scope: ORIGINAL_CSV, NORMALIZED_PORTFOLIO, REQUEST_COMPOSITION, ORIGINAL_VENDOR_PDF, EXTRACTION_EVIDENCE, PERFORMANCE, ANALYSIS, EXPORT_BUNDLE, EXPORT_PDF, EXPORT_RECEIPT, SELECTED_ACCOUNTS. PERFORMANCE and ANALYSIS are bounded JSON report payloads under platinum; the other nine are per-request/input/export state families. Canonical custody, directory, holdings and model Gold/Platinum remain in their existing long-form firm destinations. DynamoDB remains the process-state authority under the shared contract; this placement does not create a second state machine.

### Conditions and implementation responsibilities

- M implements the closed family/firm policy through the canonical registry and naming builder, with server-only validated IDs, digest and key construction. Existing default destinations remain unchanged. No browser-supplied bucket/key or fallback destination is admitted.
- P implements owner/firm isolation, current selected-account or prospect authorization before and after retrieval, least-privilege producer access, immutable accepted versions, and exact object-version/hash verification. Inaccessible interrupted objects cannot become visible reports.
- P supplies a concrete family-by-family retention/expiry policy and IAM/IaC plan before provisioning or live writes. This decision approves placement only; it does not waive R21 expiry requirements or approve indefinite storage. Preserve existing evidence while that policy is prepared; no cleanup/deletion is authorized by this ruling.
- Every affected reader/writer consumes the same registered policy revision. Cutover is coordinated and bounded; no standing dual-write fallback, estate-wide migration, or deletion. Naming owners review the registry/builder change; CVOs independently verify it with actual reader/writer evidence.
- Until the canonical entry is recorded and the implementation enforces these conditions, policy remains pending and cannot yield a writable destination. If a condition ceases to hold, disable affected publication/retrieval as appropriate and route the failure to CTO; do not silently revert or broaden access.
- End condition: this conditional exception ceases when CTO supersedes it through the same canonical register, the named product placement is retired, or required conditions no longer hold. CTO owns condition review upon owner/reviewer reports.

M can complete the candidate builder, tests and interfaces now. P can complete repository composition, least-privilege plans and retention specification now. Existing live/vendor, production, and R18-e render gates remain separate and unchanged. No product criterion receives PASS from this policy decision alone.

## IRPT-S7-02 — one documentary issuance exception

Date: 2026-09-22. Decider: `1.0.0_SA_CTO` under the same committed Andrew session delegation. Raised by COO~M at 21:28:56Z.

The exact drafted CRO seat-home order `org/tier1_exec/4.0.0_SA_CRO/task_orders/IRPT-S7-01_REGISTER_20260922.md` names only the canonical conformance ledger and implements IRPT-S7-01 at `bcd38bba00`. Its filename resolves to `IRPT`, a macro without `org/projects/IRPT.json`; it is intentionally not a newly registered implementation pipeline or a resumption of the held B/F cycles. CTO reviewed the complete draft and the existing `to-pipeline-gate.py` documented override mechanism.

**Approve the canonical audited `pipeline-override` for this exact documentary order only.** COO~M remains issuer and committer; CRO remains the register executor. Add this line to that order and use ordinary safe-commit:

```text
# pipeline-override: CTO IRPT-S7-02 under Andrew session delegation ecf350639a; exact CRO register-carrier act implementing IRPT-S7-01 bcd38bba00, not a registered IRPT pipeline or B/F round; sole work surface infra/logic/06_CONFORMANCE_LEDGER.md; no runtime/deploy or product acceptance authority.
```

The established gate appends its record to `org/to-pipeline-override-audit.log`. Confirm that the record was actually written as well as the issuance commit, then route the exact committed order to CRO. An unwritable audit sink is not accepted as evidence of completed audit recording. Keep the drafted paths, preflight declarations, acceptance, private-data conditions and retention prerequisites. No renamed fake project, new project registration, global exemption, gate edit, no-verify, or force is authorized. A new refusal outside this narrowly adjudicated registration mismatch must be reported on its own evidence.

## IRPT-P-BUILD-01 — shared source-map integration permission

Date: 2026-09-22. Raised by COO~P at 21:35:24Z. Decider/grantor: CTO under Andrew's session delegation; grantee is exact `2.0.0_SA_COO~P`.

Approve P's source-commit permission for the single file `infra/aws/lambda/ci/lambda-source-map.json`, implementing its existing shared packaging responsibility. Canonical validator reproduced P's refusal. A dedicated lane preserves all twelve incumbent YANG_PIPELINE_DEPLOY members and adds only P; the YANG deployment lane itself, other CI files, other COOs and CVOs are unchanged. SOURCE_MAP_GRANT_EVIDENCE.json records 67 positive/negative checks including three actual hook controls.

P's authorized edits are IRPT function build composition only: required files/dependencies, exact staged source paths/pins/hashes, and directly associated build notes. Existing or newly required `irpt-*` entries must describe the assigned Investor Reporting product and agreed M/Y consumers. Root descriptive provenance may identify the update, but deployed hashes, artifact versions and `_last_deploy_recorded` must not be invented or advanced by offline packaging work. Non-IRPT function objects must remain semantically identical. No Lambda upload, cloud write, production rollout, broad CI tool change or render prerequisite lift is granted.

The ownership hook grants at **file granularity**; it does not enforce JSON-member ownership. Therefore P must attach an exact before/after function-member diff, a non-IRPT equality check, and offline flat-package import/entry proof covering each changed consumer. CVO~P independently checks those boundaries; M/Y and their reviewers verify their consumed interfaces. Reconcile fresh shared-map changes immediately before integration rather than overwriting another lane's updates. P preserves the grantor commit when consuming it into its worktree. Additional concrete files require their own ownership ruling, not a global infrastructure grant.

## IRPT-S7-03 — finite candidate retention and performance source evidence

Date: 2026-09-22. Decider: CTO under Andrew's session delegation at `ecf350639a`. Raised by COO~P at 21:41:18Z. Basis: full 123-line STORAGE_PROVISIONING_PLAN.md in COO's IRPT_MVP_P deliverables, and doctrine R20/R21. P must preserve the reviewed plan in a source commit before candidate handoff.

Approve `irpt-retention-v1` as the implementation policy for candidate development: 30 days for unreferenced inputs and selection references; 7 days for unfinished exports; 2555-day creation-based ceilings for accepted artifacts, with each report/export expiring no later than its earliest required dependency. Selection references stay at 30 days; accepted reports retain their frozen member/revision provenance and require fresh current authorization. These are product policy values, not a legal records-retention determination. Never extend an expired artifact or renew the creation-based ceiling through reads, retries, copying or later report creation. Promotion must be conditional, reject already-expired evidence, and complete before publication; concurrent expiration/promotion must fail closed. P and CVO~P must prove these boundaries with a controlled clock and actual repository paths.

Approve addition of exactly `PERFORMANCE_SOURCE_EVIDENCE` to the S7 family allowlist: request-scoped original SmartX/Black Diamond/Orion performance response bytes plus a separately identified redacted request/response receipt, under state family/table `performance_source_evidence`, opaque server IDs, 30-day unreferenced lifetime and 2555-day original-creation ceiling. This makes twelve allowed families, ten state families and two platinum report families. It is not a general vendor ingestion archive or a replacement for required custody processing. Credentials, cookies and authentication headers must never be persisted; refuse/quarantine safely without persisting sensitive bytes if a response cannot satisfy that rule. Do not silently alter bytes while claiming an original-source hash.

M owns the canonical registry/builder revision; P owns the provider writer and retention enforcement; Y consumes only agreed references where applicable. M must issue a bounded amendment to the same CRO register task, referencing this ruling. CRO must record the additional family and retention conditions in the single canonical exception carrier, preserving history and recounting actual entries. IRPT-S7-02 remains limited to that exact documentary order and existing audited mechanism. No second register or change to the global canon is authorized. Unknown or unregistered family/policy revisions remain non-writable; all readers/writers must consume the same accepted revision.

Approve the proposed least-privilege role matrix as the implementation direction, subject to concrete policy evaluation and independent negative controls; this does not assert that IAM, KMS context, DynamoDB LeadingKeys, versioned S3 operations or flat packages already work. P must reconcile permissions against actual keys and calls, and retain the previous source-map diff/import proof obligations. Missing prescribed `.tools/terraform.exe` is a repository provisioning defect, not grounds to replace the tool or label syntax checks a Terraform plan.

No provisioning, vendor execution, deployment, lifecycle activation or deletion is authorized here. The implementation may enforce logical expiry while preserving existing evidence, but physical-retention completion remains OPEN until a bounded reference-aware disposal design and separately authorized execution are established. It must not be advertised as complete finite physical retention or indefinite storage approval. Existing R18-e render and live-action gates remain unchanged. No criterion receives PASS from this ruling alone.
## IRPT-M-REGISTRY-01 — exact registry implementation permission

Date: 2026-09-22. CTO grantor under Andrew's `ecf350639a` delegation; exact grantee `2.0.0_SA_COO~M`. COO~M raised the reproduced refusal at 22:02:57Z.

Grant M source-commit access to exactly `infra/logic/registry/scopes.json` and `infra/logic/registry/reporting_policies.json`. Dedicated IRPT_COMPLETION_REGISTRY preserves the five existing PLATFORM_LOGIC_DOCS members and adds only exact M; the existing lane and every existing path rule are unchanged. Canonical validator independently reproduced both refusals. REGISTRY_GRANT_EVIDENCE.json records 417 passing controls including four actual canonical CLI checks. Already admitted builder/test paths require no new grant.

Scope is the unprovisioned `irpt` product row and the closed X10 twelve-family reporting policy at canonical amendment `705dae3202`, implementing S7-03. Preserve all existing non-IRPT rows, firm homes, naming rules, bucket-provisioned facts, and unrelated policy members. Do not mark a bucket provisioned from local implementation. This is a file-level permission: the hook does not enforce JSON-member scope. M must deliver exact member diff, non-IRPT semantic equality, actual builder/registry validation and negative controls for unknown family/firm/policy, stale policy and unauthorized destination. Reconcile fresh shared registry changes before integration; retain original CTO grantor attribution on consumption.

CRO is assigned registry-owner review of the exact candidate. COO~G is requested to confirm current canonical builder ownership and supply or identify its naming-owner reviewer; M routes an exact pinned package and records the owner response before integration. If the owner is unavailable or ownership has transferred, report it to CTO for assignment rather than infer sign-off. Matching CVO~M independently tests the builder and P/Y consumer contract; owner review is not a substitute for independent product acceptance. No broad naming-library refactor, global registry/rule change, cloud write, provisioning or acceptance lift is authorized. Additional concrete generated carriers, if required by canonical validation, must be named and adjudicated separately before committing beyond the current grant.
## IRPT-Y-REPLAY-01 — accepted upload retry is replay, refresh is explicit

Date: 2026-09-22. CTO under Andrew's session delegation. Raised by CVO~Y's Y-U01 review `ae005da18e` at 22:03:31Z on candidate `bf50e40359`: unchanged token/bytes/options returned a new normalized input when security or same-date price revision changed. CONTRACT S3 freezes normalized input and S4 binds immutable revisions with idempotency and explicit correction.

Decide replay semantics for an already accepted upload: same owner-scoped idempotency token and same semantic request resolve to the originally accepted upload/input IDs, frozen resolver/price revisions, quantities and hashes. Do not renormalize against current sources, create a new accepted input or repeat dispatch merely because the request is retried. Current authorization, expiry and availability checks still run; refused or unavailable replay must be explicit, never replaced with freshly computed content. Incomplete attempts resume safely through conditional state/recovery using their recorded dependencies; this ruling does not claim all retries necessarily return READY.

A deliberate correction or refresh creates a new request/revision with a new idempotency identity and explicit user intent, preserving the old accepted input and recording lineage. A raw upload handle may be reused for an explicit correction when the canonical request identity also binds the changed semantic options and produces a new immutable input. An actual idempotency key that already binds one semantic request cannot be rebound to different bytes/options; that is an explicit conflict. Do not conflate the upload handle with the complete request identity. Coordinate wire/UI semantics with P and publish exact examples in Y INTERFACES.md. Do not make hidden browser retries mint fresh identities.

COO~Y implements; CVO~Y reruns the original changed-resolver/changed-price failing probe unchanged and adds same-token payload-conflict, explicit-refresh positive, current-access/expiry refusal and interrupted/concurrent-retry controls through the actual consumer/repository boundary. CVO~P verifies integrated browser request identity behavior. Update received at 22:06:34Z: CVO~Y independently closed Y-U01 at `9da7d87f99` in `6401215f60` using the unchanged dependency-change probe and thirteen supplied tests. That bounded closure is retained; actual concurrent transaction/crash, lifecycle, browser and integrated evidence remain outstanding. No runtime/deploy/product acceptance is granted by this decision.
## IRPT-M-REGISTRY-02 — bounded CRO owner-review activation

Date: 2026-09-22. CTO under Andrew's session delegation. CRO reported at 22:15:06Z that registry-owner review is not activated by the candidate message; its previous ledger-only order is closed. This is an activation requirement, not a negative candidate verdict.

COO~M issues `org/tier1_exec/4.0.0_SA_CRO/task_orders/IRPT-X10_REGISTRY_REVIEW_20260922.md` for read-only owner review of exact candidate `587e782bc6`, generated evidence `3c14153eeb`, baseline `78a4859664`, and canonical X10 `705dae3202`. Sole writable review surface: `org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_X10_REGISTRY_REVIEW_20260922/` for bounded report/proof; no source, carrier, ledger or runtime writes. Acceptance: C1 exact pin/provenance and baseline identity; C2 only admitted IRPT row/twelve-family semantics, private firms, pending policy and retained conditions; C3 non-IRPT equality and explicit classification of all ten generated deltas including independently reproduced inherited drift; C4 bounded PASS/FAIL/NOT_EVALUATED owner verdict with exact defects/limits, committed report and M/CTO/CVO-M receipts. This does not substitute for builder-owner integration or CVO independent product acceptance.

The known IRPT macro has no registered project file. For this exact documentary review order only, authorize the existing audited pipeline-override mechanism under the same rationale as S7-02. M includes the following line, complete proof-of-spec contract, and uses ordinary safe-commit; verify actual issuance audit append and exact order delivery. No new project, altered global gate or forced commit is authorized. Any different gate refusal returns with its evidence.

`# pipeline-override: CTO IRPT-M-REGISTRY-02 under Andrew delegation ecf350639a; exact CRO read-only X10 registry-owner review of 587e782bc6 and generated evidence 3c14153eeb; sole writable surface org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_X10_REGISTRY_REVIEW_20260922/; no source/ledger/runtime/deploy write, no B/F canonical round restart.`
## IRPT-M-LEGACY-READ-01 — historical cutoff repair and existing input reads

Date: 2026-09-22. CTO under Andrew's `ecf350639a` session delegation. Raised by M at 23:21:05Z. CTO read SOURCE_INPUT_EVIDENCE.md and the actual HEAD diff in M's isolated worktree, then independently ran its checked-in naming-gate.py with --enforce against that runner diff. Evidence: `.runtime/codex-seats/1.0.0_SA_CTO/legacy_read_gate/candidate.diff` and `gate-output.txt`; rc1, six literals graded. SmartX `smartx/platform/silver/fact_allocation_account_map/` is RAISE/WARN, not the blocking refusal. The blocker is unchanged Inflection `silver/api_dims/accounts_v2/`, classified EXISTING OUT-OF-PATTERN in live ADVI_FIRMBKTS remediation.

Approve bounded continuation of the existing source reads in `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` while M adds requested-business-date cutoffs and exact upstream version/hash receipts. The two cited prefix bytes, source buckets, account scope and existing read direction must remain unchanged. No newly invented legacy alias, source repoint, broader population or current-data substitution is permitted. Canonical destination selection remains a separate implementation change subject to its existing publication tests and independent review. This decision does not grade legacy inputs conformant or close ADVI_FIRMBKTS; it permits a correctness repair without pretending the source migration occurred.

The currently checked-in gate deliberately refuses an existing remediation-surface literal when touched; it has no per-case naming exception mechanism. Disabling enforcement, moving/splitting strings to evade inspection, changing remediation status, force/no-verify, or substituting a guessed canonical read location is not the remedy. This is a repository capability gap for the specifically adjudicated read-only repair. MSTR is asked to name the repository-tooling implementer; G reviews the gate/naming semantics. They must return a concrete narrowly bounded, auditable implementation proposal to CTO: preserve rejection of new/changed offending literals and writes, bind any exception to the exact authorized file/read/purpose, require durable authority and exercised positive/negative controls, and leave all unrelated naming checks active. No broad read-call exemption or new override flag is approved in advance.

M retains its patch and failure evidence, continues independent reconciliation and source-coverage work, and awaits the sanctioned implementation before retrying this blocked commit. CVO~M must independently verify historical cutoff/version receipts and no source/destination widening at the eventual exact candidate; producer counts are not acceptance. No source migration, live write, deploy or canonical B/F cycle is authorized by this ruling.

## IRPT-M-BASIS-01 — custody reconciliation and distinct SmartX valuation facts

Date: 2026-09-22. CTO under Andrew's `ecf350639a` session delegation; resolves M's 23:31:29Z request. CTO read CONTRACT S2, COO_M M1/M3/M7, and SMARTX_INGESTION_ARCHITECTURE.md section 7b. That source records Andrew's canonical SmartX AUM basis as longEquity plus cash, gross of shorts; vendor equity already includes signed shortEquity and cash. Its historical unexplained residuals and short-book characterization remain findings, not accepted tolerances.

The current M contract determines the ownership-tree boundary: independently enumerated unique custody values supply the root and the model/non-model/unresolved reconciliation. SmartX overlay membership and its separately named valuation facts must not replace or inflate that custody root. Preserve original longEquity, shortEquity, cash and equity with source date/version, units and scope. Preserve Andrew's canonical SmartX gross AUM as longEquity plus cash. Separately named net valuation reconciles signed positions plus cash to equity when the same-scope, same-date source evidence supports that identity. Do not compute equity plus cash, relabel net as canonical gross AUM, reinterpret gross-of-shorts as absolute long-plus-short exposure, or splice a provider allocation total into custody. This is not a change to P's provider-calculated returns or its primary/verification policy.

COO~M may implement the evidenced double-count correction and explicit basis separation now under its existing mandate. Missing or incompatible custody, position, mapping, clock or valuation evidence remains an explicit unresolved/failed finding; no cash plug, rescaling, invented residual assignment or whole-book acceptance from matching totals. Independently assess each account and parent partition, including shorts, zero/negative totals, cash, duplicate allocations and missing values. CVO~M reruns the original failing cases unchanged, verifies source lineage and named gross/net outputs, and tests the complete source-backed custody/overlay reconciliation. P and Y consume the declared custody basis; incompatible inputs are explicit rather than silently converted.

M's reported full-firm build (5917 accounts, 127925 nodes, approximately 98.45 MB JSON, 7479 failing parent partitions) is diagnostic evidence, not accepted publication. Bounded parts with selected-account reads are authorized within existing M4/S2, without another design approval round. M publishes concrete schema and byte/count/request limits in INTERFACES.md, pins the complete part inventory by revision/version/hash, and keeps all selected-account pages on one accepted revision with current authorization. No unbounded cap increase, silent truncation, partial acceptance or full-firm payload returned for a subset. Oversized selections need an explicit bounded continuation or refusal. Coordinate changed loader/manifest packaging with P and the Y consumer; CVO~M tests missing/corrupt/mixed parts, interrupted publication, oversized selections and revocation. Existing publication ambiguity findings remain open until fixed and independently retested. No live write, deploy, new storage family or old B/F cycle is authorized.

Related receipts received 23:29–23:32Z: CVO~P reports bounded holdings packaging PASS at review `57f0a0ef3c` on `0fb7e56629`, and R-P09 consumer field-binding closure at `65a3aedf72` on portal `c86a5eb53df6e48906def496df2d4dcdc0f47404` / backend `5add22ca9f` (11 unchanged independent assertions and 24 supplied tests PASS). These do not establish effective IAM, a mounted/live upload route, publication correctness or full product acceptance. MSTR has named itself the repository-tooling implementer for LEGACY-READ-01 under LD-0602, is checking the Site Z same-file collision, and owes the concrete bounded mechanism proposal; the blocked source commit remains blocked.

## IRPT-M-LEGACY-READ-02 — bounded mechanism implementation shape

Date: 2026-09-22. CTO under Andrew's `ecf350639a` delegation. Read MSTR message 99604 and the complete proposal `org/tier0_exec/0.0.0_AB_MSTR/deliverables/NAMING_GATE_LEGACY_READ_WAIVER_PROPOSAL_20260922.md` at reported pin `b13d5d24d3`. Approve isolated implementation by MSTR with the following required refinement; this is not approval to integrate, activate the exception on CLOUD, or retry M's blocked commit yet. MSTR returns exact candidate, complete diff, carrier and exercised control results before integration. G's naming-semantics review remains part of that review. Site Z clearance is accepted for this session; recheck it if implementation crosses the session boundary as proposed.

Retain the single existing-remediation branch, exact file/whole literal/remediation/authority/purpose/owner carrier, and visible WAIVED-READ warning and verdict-log entry. Initial entry is only the LEGACY-READ-01 Inflection read in `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`; no SmartX or other blanket entries. Answerable owner is CTO. Set initial as_of_cutoff to 2026-09-23 inclusive UTC, expiring at 2026-09-24T00:00:00Z; this is waiver expiry, not the requested business-data cutoff. Renewal requires a new recorded adjudication. Missing, malformed, ambiguous, duplicate or expired matching authority must not enable an exception. Bind the record to the actual durable ruling; authority prose alone is not a grant for arbitrary additional cases.

Required N2 refinement: a write-verb denylist is insufficient. Positively recognize the exact authorized read use and its relevant call/helper context; unknown, indirect or ambiguous use remains REFUSE. Inspect the actual candidate source and relevant helper behavior, not only one diff line. Existing literal membership alone must not authorize a new occurrence, an unchanged literal moved into a write, a shared variable reaching both read and write, or a changed read helper that now writes. The same bucket/prefix/account-scope restrictions from LEGACY-READ-01 still apply. If a sound narrow recognizer cannot support this case, report that limit and return a revised proposal; do not broaden to arbitrary apparent reads.

Keep all proposed positive, five negative, absent/empty-carrier and baseline regression controls. Add exercised cases for ambiguous helper/alias use, mixed read/write use, a new occurrence of the same existing literal, relevant helper behavior changed to write, malformed/duplicate authority records, and the UTC expiry boundary. Every unauthorized use must remain a refusal; the five unrelated verdicts in the original real diff remain byte-identical. Verify that normal canonical safe-commit execution consumes the same candidate source/carrier that the controls exercised. Return exact results and limitations; no claim of general Python dataflow soundness is required or accepted. No gate disable, source migration, remediation closure, live action, or B/F cycle is authorized.

## IRPT-X10-INTEGRATION-01 — option A and two owned-file stamp repairs

Date: 2026-09-22. CTO under Andrew's `ecf350639a` delegation. Read G message 99605 and the complete X10_NAMING_OWNER_REVIEW.md at reported LOCAL `136624e660`, in response to `cc827b4f82`. Accept G's assigned builder-owner review as bounded PASS for the PENDING_ENFORCEMENT candidate only, alongside the separately recorded CRO and CVO reviews. G's partial extraction has 11 harness failures plus 5 inherited failures at every tested baseline/candidate; it is not a clean full-checkout suite. No claim of registry-defined universal builder ownership is made.

Choose option A for the X10 integration unit: reviewed changes to `lib/opal_naming.py`, `lib/tests/test_irpt_destination.py`, `infra/logic/registry/scopes.json` and `infra/logic/registry/reporting_policies.json`. Do not integrate the ten-carrier inventory bytes from `3c14153eeb`, the inherited harvest/fmt changes, or the four CLOUD_OPS_OR_ETL paths. Preserve PENDING_ENFORCEMENT, null enforcement_ref, unprovisioned product status, non-IRPT semantics and existing writer refusal. The absent generated IRPT mappings are not a runtime or provisioning completion claim. Future actual consumer requirements must be measured and separately integrated by the relevant owner.

Separately authorize M to regenerate exactly `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` and `infra/aws/lambda/investor-reporting/_authz/loaders.py` through the canonical generator in its existing lanes. These files already carry M feature work; stale registry stamps obstruct their ordinary integration under every option. Generate from the actual reconciled source/registry tree, never copy a historical whole-file inventory over newer source. G measured two stamp lines per file at its reviewed pins. Require exact before/after evidence showing only the generated stamp changes for this repair; any broader delta returns for adjudication. Preserve all independently accepted feature changes and keep the distinct LEGACY-READ-01 source-cutoff blocker visible.

M prepares the bounded integration candidate and fresh ordinary gate evidence, including the staged generated-file checks against the actual reconciled tree, registry validation, relevant full-checkout tests and non-IRPT equality. G's successful scratch trial at `c462d8b4df` is diagnostic, not proof for a later merged head. Resolve the reported RULINGS.md add/add conflict by preserving the current CTO record and all legitimately accepted historical rulings; never replace it with M's older branch copy. Return any substantive governance-text conflict to CTO. CVO~M verifies the exact candidate and retained refusal boundaries. Existing shared integration rules and MSTR-owned pushes apply; this disposition is not a blanket drain of all unreviewed M work, policy activation, provisioning, deployment, full S7 acceptance or a restart of B/F rounds.

## IRPT-M-LEGACY-READ-03 — authoritative carrier and exact recognizer

Date: 2026-09-23 UTC. CTO under Andrew's `ecf350639a` delegation. G message 99610 is implementation pre-review, not a candidate verdict. Adopt its authority-boundary recommendations as required refinements to LEGACY-READ-02. The gate's whole-pre-image string membership does not prove an occurrence is old; preserve the explicit new-occurrence/moved-use refusal controls already required. The authorized cutoff change itself modifies the read helper, so an unchanged-from-HEAD helper test alone would incorrectly refuse the authorized repair.

Require a positive recognizer for the reviewed direct call site and reviewed candidate helper behavior, including the exact bucket binding, argument position, enclosing function and a single whole-literal occurrence. Pin the independently reviewed candidate helper's normalized AST hash in the case record, in addition to recognizing allowed read interactions; do not accept a producer-supplied hash as self-authorization. Unknown bindings, aliases, alternate helpers, changed helper behavior, duplicate occurrences and mixed read/write uses refuse. G's suggested different-read-helper negative control must also refuse. This remains a narrow recognizer, not a claim of general static dataflow proof.

The authoritative `org/standards/NAMING_LEGACY_READS.json` must have an exact-file commit lane restricted to `1.0.0_SA_CTO`, with measured denial for MSTR, COO/CVO/CRO base and suffixed seats, and unrelated lane behavior unchanged. MSTR may prepare the implementation, proposed lane change, carrier specimen and tests in isolation for CTO review; it may not grant itself a carrier-writing override. CTO will land the reviewed protection and exact authority record through the canonical commit path. No lane change or active entry is enacted by this document alone.

Production gate evaluation must load the authority carrier from the repository's committed HEAD, never the worktree or index being graded. The active entry must precede the source-repair commit. Verify the full 40-hex authority commit resolves and the specified pinned RULINGS.md contains the exact ruling; combine this with the protected carrier rather than treating arbitrary prose as authorization. Preserve expiry at 2026-09-24T00:00:00Z, exclusive and evaluated in UTC. Controls must show unstaged, staged and same-commit attempted grants cannot enable the exception; absent/invalid prior authority must fail closed. Candidate source/helper recognition still uses the actual post-image being committed, so HEAD authority is never confused with stale HEAD source. Isolated fixtures may simulate prior commits for these controls, but cannot activate a production waiver. MSTR returns the exact implementation and protection proposal plus evidence; G reviews the pinned candidate before activation.

## IRPT-Y-DATES-01 — truthful prospect-analysis status dates

Date: 2026-09-23 UTC. CTO under Andrew's `ecf350639a` delegation; resolves P's 00:16:26Z request after reading the complete `docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json`. Its existing answer-bearing states require a non-null business_date. That rule correctly prevents a dated answer from losing its date, but does not express accepted prospect input that has no single source business date. Approve the following narrow current-completion contract amendment; do not recut or restart the held B/F canonical rounds, and do not attribute this amendment to the historical PRD pin.

For explicitly identified prospect-analysis status only, admit `source_dates.date_basis` values `UNDATED_INPUT` and `PER_SECTION` with business_date absent, never null. The discriminated branch must require the exact agreed analysis operation/input lane and immutable accepted input/report revision; an arbitrary operation_kind string or absent date is not enough to opt in. UNDATED_INPUT means the accepted source genuinely declares no applicable business date, not that lookup, parsing, retention or provenance failed. PER_SECTION means no single date represents the accepted analysis: preserve each available source date against its stable section identity and explicitly represent any undated section without fabrication. Do not pick a convenient section date as the whole report date. If a valid single business date exists, retain it under the ordinary dated contract. Dated custody and performance retain the existing business_date requirement, including their negative controls.

Accepted, queued, lease, generation and retrieval timestamps remain process timestamps, never substitutes for source business dates. Do not convert source_completion_date or as_of into invented business dates. UI and export must truthfully label undated or per-section dates, preserve every actual source date, and avoid showing today's date as a default. This extension does not relax requirements for dated compatible prices, actual custody clocks, report certification, retained immutable evidence, current access or READY release. When a required date is genuinely missing, remain unavailable or needs-correction as appropriate; the new basis is not a success fallback.

P owns shared schema/provenance, generated types, validation and frontend integration; Y owns accepted-input/status derivation and paired examples, with direct agreement recorded in INTERFACES.md. Preserve the six existing semantic obligations and closed schema validation. Cite this ruling as the new authority and keep historical PRD provenance truthful. Because older closed-schema consumers reject added fields, update every in-scope producer/consumer and use the repository's explicit compatibility/version mechanism as needed; do not expose a new wire form to an old consumer. Continue fail-closed UNAVAILABLE at the incompatible boundary until the paired change is integrated, while implementation proceeds now under this decision.

CVO~P and CVO~Y independently verify the actual handler-to-schema-to-wire-to-UI boundary: valid undated prospect, multiple dated sections, mixed dated/undated sections, retained dated prospect/custody/performance behavior, missing or null/invalid basis/date, malformed section identity/date, process-timestamp substitution, unauthorized operation opting into the exception, frozen retry/reopen and old-consumer compatibility. A READY status still requires the independently accepted report; status/schema PASS alone does not prove runtime or full product completion. Return exact paired pins and evidence; no new vendor call, live deployment or acceptance lift is authorized.

## IRPT-LIVE-FIRST-20260923 — contract v1.3 intake and work sequencing

CTO, 2026-09-23 after CTO~C message 99679 at 16:53:56Z. Read the exact notice and contract v1.3 section 0. Adopt its priority and coordination rules for the existing Andrew-authorized completion effort. Andrew's session instruction that CTO is the reviewer remains controlling; no CVO relaunch or independent review wait is introduced.

The first milestone is the real login -> shared auth/scope/bootstrap -> real firm/investor data -> screen thread. COO~P owns the first hop under the existing exception. Frontend may be localhost/DEV. Prior offline review records remain valid only at their stated source/artifact boundaries; none closes S1-S7 or establishes a live journey. Do not restart the held split canonical cycles or retire those project rows before actual hand-back.

P's next active work is to measure and fix the current first-hop failure using the existing localhost:5174 setup and actual authorized data path. Record the exact served frontend/backend revisions, request route/status and sanitized response structure, and the first failing boundary in the current STATUS.md. Retain real authentication and tenant restrictions; no fabricated scope, user token copying, invented data or auth bypass. Ordinary local implementation continues within existing ownership. If a reserved backend/runtime change is required, return the exact concrete change and relevant existing authority; the hold lift alone does not authorize promotion, provisioning or vendor egress.

Park the deeper accepted-custody source-admission and package-review chain, including the next correction request in 155213fedf, until the first hop is live OR a measured first-hop trace demonstrates that a named part of that chain is necessary to unblock it. Owners: P package/current authorization, M actual-source/publication semantics, Y normalization/recipe consumer. Preserve all pinned code, defects and reviews; do not discard acceptance IDs. Already-running atomic work may be checkpointed before parking. No new general registry/naming/storage review chain starts for this milestone.

Current offline checkpoints: publication3539ad2ae5/correction200ba442f5 reviewed bb43292167/194e3a25c3; P binding e36b007fa1 reviewed d8d88388ab; Y consumer10627906f2 reviewed36131adb48; package source e3ad48ca23 reviewed155213fedf with packaged-M and evidence corrections still open. These are reusable prerequisites, not live acceptance.

Use fixed current STATUS.md and one current schema/example in INTERFACES.md, with superseded interface prose in INTERFACES_HISTORY.md. Append future CTO decisions here. Batch decision notices; peers send only interface publications, concrete blockers or review handoffs. No peer ACK required for this ruling.

## IRPT-FIRST-HOP-PAIR-20260923 - bounded local integration and runtime preparation

CTO direct review of P handoff 6cd8adb582, 2026-09-23. Three fresh sanitized browser responses report bearer present, resolve-scope HTTP 200, UNAVAILABLE/UNEXPECTED and no data. P measured the downloaded deployed directory artifact at iqLKa1RWk9hlcSlAheuoAMgIY4R3VrStPX1eG5Qwq/s=, 149956 bytes. This is implementer live evidence; CTO read its pinned report and JSON, not a new independent AWS measurement. The exact internal exception is not established by that response. Both served frontend and backend lack the prepared Global bootstrap behavior.

CTO checked the local frontend is clean, its scope baseline equals the parent of 09d5d5ea, the three-commit scope delta has exactly the reported 17 paths, and 910ebf36 is an ancestor of previously reviewed e0531491. Reuse the bounded paired source/parser evidence in 8653eb6cd4; it remains offline evidence. No new source or live PASS is inferred from ancestry.

Authorize COO~P to integrate only 09d5d5ea68d94198ac7f24beabe3de2fb7fb6b48, f0e7e362410aec04dc8443da60285330143497ee and 910ebf360d7e38b2ff86f500b472097048c5fed5, in order, into C:/Users/AndrewBerman/Desktop/portal-local-live-20260923. This is the narrow exception to the earlier instruction not to edit CTO's local tree. Recheck HEAD and cleanliness immediately before mutation; preserve the existing launcher, trace and any intervening user changes. Use the canonical integration/commit path; no reset, whole-tree replacement, hook bypass or unrelated custody-generation patch. A conflicting change returns to CTO. Run typecheck and focused scope/parser, mounted-selector and context/race controls on the actual resulting tree, and report exact served pin. This local integration requires no additional Andrew confirmation and authorizes no remote push or Portal production promotion.

In parallel within the first-hop work, P prepares one concrete irpt-directory-search runtime candidate from the reported six-member delta and its unchanged closure. The later owner-read imports must either be included and verified or removed through a separately reviewed narrow source change; do not omit dependencies. Return the exact ZIP bytes/hash, member-to-source manifest, installed dependency/layer closure, actual handler cold-start proof in the matching Lambda runtime, and paired positive/negative Global/partner/forged-selector/warm-process controls. Record existing configuration/role/route equality or every required delta, current function revision precondition, rollback artifact and exact apply/recording route. Do not broaden this into the parked generation-package chain or assume a source-only ZIP is deployable. This is local artifact/plan preparation, not cloud apply authority.

After CTO adjudicates that concrete runtime plan and the paired code is actually served, measure the real signed-in first hop again: firm choices, attributed investor list and pagination, tenant-bound selection, and reload. Preserve auth enforcement; no token replay, invented data or frontend-only scope workaround. CLOUD push remains held under MSTR 99698 pending Andrew's word. No new CVO wait and no ACK required.

## IRPT-OPAL-FULL-ACCESS-20260923 - Andrew corrects the Opal permission model

Andrew's direct instruction in this CTO session: "No, Opal Users have free reign for all functions. Opal Users can create any reports they want, view anything they want." This is the controlling Investor Reporting product-access requirement. CTO's preceding explanation that Global was browsing-only with a mandatory single-firm reporting permission limit was incorrect.

Verified Opal users have access to all IRPT functions across all firms, including browsing, performance, model overlay, sensitivity/YCharts, report creation, prospect/upload workflows, history, viewing and export/download. Global (All) is their default view. A chosen firm filters the view or report inputs; it does not reduce their underlying authority. Do not deny an Opal action because the actor's home firm differs from the data firm, because another user owns the report, because the input is prospect rather than custody, or merely because selected inputs span firms. Existing implementation gaps in an otherwise requested workflow are capability gaps, not permission policy. This does not invent a new report format or assert that cross-firm economic aggregation is already implemented.

This explicitly supersedes conflicting discovery-only, custody-only, partner-advisor-required and mandatory-single-firm authorization language in prior rulings, LOCAL_LIVE_PARTNER_SCOPE_20260923.md, mandates and tests. Preserve the real actor identity, each input's firm/account/source attribution, exact report input selection and audit history. Data placement and accounting identities remain meaningful even though an Opal user may access all of them. Do not impersonate a partner advisor or erase firm provenance to implement broad access.

Firm-specific users remain limited to their authorized firm/accounts and functions. The backend must distinguish verified Opal identity from ordinary firm identity on every applicable request using the established trusted identity boundary. Browser dropdowns and supplied role/owner/tenant strings confer no authority. Authentication failures and forged Opal claims still refuse; valid Opal access across firms/functions must succeed. Viewer authority does not turn a scoped render/service token into an interactive Opal user.

P owns the shared authorization/UI/API implementation under existing ownership, updates the current interface and positive/negative access tests, and coordinates exact dependent changes with M (data/selection) and Y (generation/upload/retained reads). Review tests that intentionally refuse valid Opal prospect, foreign-owner report or cross-firm access: those expectations now contradict Andrew's requirement and must change, while equivalent ordinary-firm and forged-identity refusals remain. Capture actual missing capabilities rather than hiding them behind permission errors. CTO reviews directly; no new independent-review wait.

Continue the live-first milestone and the already authorized narrow local integration/runtime preparation in d2fd024d72. This access correction is implementation authority, not a claim of deployed behavior. It does not release the separate CLOUD push hold or change infrastructure publication controls. Send one coordinated interface/blocker/review handoff when concrete; no ACK required.

## IRPT-DIRECTORY-STAGE-20260923 - exact bootstrap artifact review

CTO directly reviewed P handoff 7009b2456e and executed its pinned probe. Verified localhost tree10141b6d0bbb007d5dd9e758f11f785216e11339 clean; src equals910ebf36 and launcher equals3b15871b. Actual HTTP module readback200 contains Global context and Select Firm. P's actual-tree typecheck/parser/mounted/race results remain attributed to P.

CTO verified candidate ZIP155747bytes, SHA256 a39f74ba1e688ac0ad1cf2b3a2b18c27f93d5493dc82d2d283848a7dee0a618b, Lambda hash o590uh5oisCtHPKzorGMJ/k9VJPcgtLSg4SKfe4KYYs=: exactly20 unique members, all identical to declared Git bytes. Preparation and probe hashes match their committed provenance. Direct Docker execution in public.ecr.aws/lambda/python@sha256:5f188ce6104ab76d1a9a44b9b53fd0d72ea5ccec94eb4cbccf5c9b0ef485f9f8, network none, read-only mounts/filesystem, passed cold actual handler,41 unchanged tests in0.98s, synthetic Global actual-handler response and all runtime module origins. Runtime SDK boto3/botocore1.42.97, no added runtime test dependencies. Scratch C:/Users/ANDREW~1/AppData/Local/Temp/irpt-cto-directory-684o_eas. First Docker invocation failed creating a nested read-only mountpoint; created that empty local directory and reran unchanged probe successfully. No live data/authentication acceptance follows from this test.

Policy adjudication: a concrete selected_tenant on a per-firm API call is a routing/input binding, not a cap on Opal authority. The Global UI may enumerate every firm through separately scoped requests; no requirement to replace every API with an aggregate endpoint follows from Andrew's instruction. The test rejecting selected_tenant=global on a per-firm browse operation is therefore not, by itself, proof of an Opal permission defect. Its paired UI must actually provide access across all firms, without forcing an Opal user to acquire partner identity. Do not waive the actual different-owner/prospect/function restrictions identified in0152bf7bfb; those remain implementation work under5ad99c7d30. Separate trusted-viewer interface9a3ec2a11f is not in this ZIP and has not received CTO implementation review here.

Admit this artifact as a bounded bootstrap improvement, not full Opal-function compliance. Under the existing first-hop repair and CTO adjudication authority, P may now open the canonical change ledger, recheck the precise live code/revision/configuration/role/routes and stage only this irpt-directory-search artifact through the canonical single-function build-and-upload route documented at7009b2456e. Existing artifact bucket/key only; no new infrastructure or serving change. Verify the uploaded immutable version downloads to the exact reviewed hash; stop for any difference. Prepare the new targeted saved Terraform plan and submit its hash/JSON with the staged version for CTO apply adjudication. Only the existing directory function artifact version/hash may change in that proposed plan. No apply is authorized by this ruling, and the old baseline zero-change plan is not a candidate plan.

Retain immutable rollback version RXChd66RsDjV1jhG1ZsFlOGnXeIDxApp and expected baseline code iqLKa1RWk9hlcSlAheuoAMgIY4R3VrStPX1eG5Qwq/s= / RevisionId8851109e-7f1f-4915-ae2b-0dff01d276c5; any drift returns for review. No IAM, route, environment, layer, schedule, other Lambda or Portal production change. No direct Lambda update or recorder bypass. CLOUD remote push remains held. Actual signed-in bootstrap/list/selection/reload proof still follows serving the paired candidate. Continue the shared full-access correction without requiring its unrelated generation package to block this first hop. No ACK or CVO wait.

## IRPT-DIRECTORY-APPLY-20260923 - exact saved-plan authority

CTO adjudication under Andrew's standing first-hop repair and worker-fork delegation. Read P handoff fc32f94ba7. Directly hashed the actual candidate.tfplan and candidate-plan.json files under C:/Users/AndrewBerman/Desktop/irpt-smoke-p-backend-20260923/.runtime/directory-review, and freshly executed provisioned Terraform show -json on the saved binary. Its parsed output exactly equals the recorded JSON. Plan SHA256 c5ef7ef7357ad194bdc38dabd827dd170cc5544e923fd573cb9436c0d40348ca; JSON SHA2564589a8d29ddc9b39e1d86f5e53a2f8f481c466884a4742d934b766f546d88acb.

Direct machine comparison found precisely one planned resource mutation: module.irpt_directory_search.aws_lambda_function.this, in-place update. Changed fields are s3_object_version and source_code_hash plus computed last_modified. Destination immutable version1ogxCxUa61vTvMPtXB.BehRWB7aJTCnj in existing opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-search.zip; expected deployed code o590uh5oisCtHPKzorGMJ/k9VJPcgtLSg4SKfe4KYYs=. This is the exact artifact reviewed in18e2835c5f.

The initial blanket no-resource-drift check failed. Investigated the sole drift row: aws_iam_role.irpt_directory.inline_policy refresh adds the already-live selection policy to cached state. Its complete refreshed three-policy set equals the role evidence at7009b2456e; the actual role resource action is no-op. This is not a proposed IAM mutation. Targeted-plan unrelated module checks are unknown, not claimed passed. No new apply scope is inferred from either observation.

Authorize COO~P to apply only that saved plan via .tools/safe-apply.sh with directory root infra/aws/terraform/investor-reporting/directory, against canonical ledger4917bed568 (irpt-directory-bootstrap-20260923). Immediately before apply, verify saved-plan hash and the baseline live code/revision/configuration/environment/role/policy/four routes in fc32f94ba7. Baseline RevisionId8851109e-7f1f-4915-ae2b-0dff01d276c5 and code iqLKa1RWk9hlcSlAheuoAMgIY4R3VrStPX1eG5Qwq/s= must still match. Any drift, changed plan or expanded gate request returns to CTO; no direct Lambda update, bypass or implicit approval of a regenerated plan.

After apply, wait for Active/Successful and independently read the deployed CodeSha256 against o590uh5oisCtHPKzorGMJ/k9VJPcgtLSg4SKfe4KYYs=, recheck unchanged configuration/role/routes, run the targeted zero-change plan, and complete scoped canonical recording and ledger closure. Stop and report any recorder widening/failure rather than reusing an old exception. Preserve rollback RXChd66RsDjV1jhG1ZsFlOGnXeIDxApp; rollback execution needs its concrete plan adjudicated if required. No other function, IAM, route, environment, layer, schedule or Portal production mutation is authorized. CLOUD push hold remains.

Then measure the actual normal-login localhost5174 first hop with the paired served frontend: Global/firm choices, investor list/pagination, firm/client/account selection and reload. Report sanitized request outcomes without copied tokens or investor payloads. Deployment success alone is not live-user success, full Opal permission completion or MVP closure. Continue the shared full-access implementation. No ACK or independent-review wait.

## IRPT-Y-ACTUAL-VIEWER-20260923 - bounded direct source review

CTO reviewed Y handoff0a1c8121ac and production changes at85af5eb95d72051c363727229981c4dc1a35cad9, together with the actual pinned P InteractiveAccess implementation9a3ec2a11f. Accept as a bounded consumer-source improvement under Andrew's full-access requirement; do not claim Entry/storage wiring or live completion.

CTO independently extracted immutable Y source into C:/Users/ANDREW~1/AppData/Local/Temp/irpt-cto-opal-y-3fi1ypef/source, extracted P InteractiveAccess9a3ec2a11f with asserted SHA256 bba07a3f4eeb947bf33845653bde95d47bbb8037d65db4059f4f8b70ebabdf56, and extracted the three P reader/test modules from8845b7ef23. Ran suites in separate processes: ops169 PASS18.10s, intake94 PASS plus18subtests1.70s, generation212 PASS plus32subtests21.73s. Total475tests plus50subtests, zero skips. These are CTO executions against immutable source, not a quotation of Y's counts.

The change removes unconditional viewer-equals-creator refusal before authorization, retains actual viewer through current access and storage callbacks, separates data_firm placement, and admits correctly attributed Opal prospect input. Current trusted predicate and final-release checks remain; stored input/report creator is preserved. Cursor placement stays firm-specific. New uploads correctly record the acting Opal user rather than impersonating an advisor. The twelve paired controls use the real P predicate with offline external state. Same-firm other-creator report/date coverage uses actual repository code; Global storage coverage still uses port doubles. Neither demonstrates the pending shared cross-firm repository/retention implementation or HTTP entry path.

P may integrate this exact thirteen-file Y change with its owned storage/Entry implementation after completing the current atomic directory apply/readback. Preserve current live-first priority. P and Y must replay the actual combined Entry -> viewer -> request/report/artifact/retention path with real implementations and controlled external services, including Opal Global/selected-firm access to another creator, ordinary/forged identity refusals and context change. Do not turn missing data placement into an Opal permission denial or substitute retained creator for the viewer.

Y explicitly leaves new submission using another creator's retained input unresolved. This remains a required capability under Andrew's instruction: implement separate acting submitter and original input attribution through the shared resolver/composition schema, rather than requiring the user to impersonate the creator or upload the same input again. P owns the shared interface, Y consumes it, M supplies maintained actor/source profile requirements. Preserve the frozen source/profile evidence and actual submitter in the composed request. No extra product-policy decision is required; return concrete interface/implementation blockers to CTO. This review adds no deployment, CLOUD push or separate CVO gate.

## IRPT-LIVE-BOOTSTRAP-20260923 - user observation and next combined candidate

P's exact17:50:52Z message relays Andrew's normal existing-session reload confirmation: Global/Select Firm and investor list now appear on served frontend10141b6d and deployed directory artifacto590uh5oisCtHPKzorGMJ/k9VJPcgtLSg4SKfe4KYYs=. Accept that user-observed bootstrap symptom closure with its provenance. CTO has not separately observed the browser. P's fresh sanitized request is HTTP200/bearer-present/298616bytes, beyond tracer JSON limit; it does not independently establish response contents. Do not expand the relayed confirmation to pagination, accepted selection, persistence across later reloads, tabs, generation or full Opal access. The first-hop login/firm/list thread has user confirmation; S1-S7/full product acceptance remains bounded by the outstanding journeys.

P reports exact apply Active/Successful with downloaded live ZIP parity, unchanged configuration/role/routes and zero-change target plan. Canonical recording remains open: CTO independently inspected the wrapper/diff and confirmed that explicit --function scope is lost in CHANGELOG history-derived functions_updated (five functions), its nine-artifact list and downstream reconciliation, which altered the unrelated Y hash. Routed canonical tooling repair to MSTR at17:50:50Z. P preserves evidence and quiescent partial outputs; no broad record commit, historical exception reuse, tree reset or audit erasure. This bookkeeping defect does not block live testing or isolated source integration.

Next direct review is one combined actual-access candidate, not separate approval chains for each helper. P integrates its storagedd6edfc3aa and Entry4ec461a2e9 with Y85af5eb95d plus test descendant4ea95d1117, preserving ownership and isolated source work. Y's latest16 viewer/173ops controls and real-storage claims at handoffd34893bc83 are implementer evidence pending combined CTO replay; prior CTO475+50 remains tied to its exact earlier source. Supply exact combined pins and tests through actual Entry, verified Opal viewer, storage/retention and Y consumers, including ordinary/forged refusal. Do not wait for the recorder to finish before local source work. Preserve the first milestone and validate remaining real-user steps; no unrelated naming/storage-policy chain resumes by default. No new runtime apply or CLOUD push is granted here.

## IRPT-RECORDER-CONTAINMENT-20260923 - preserve evidence, remove accidental sibling edit

MSTR99709 reports recorder owner lane CLOUD_OPS_OR_ETL, CloudOps base unregistered, repair parked to that owner pending seating raised at MSTR. No tooling edit is assigned to an unauthorized lane. P's175351 report confirms recorder children quiescent and deployment proof pinnede07a5ca692; ledger V1 recording and B1 broader live selection/persistence remain open.

Authorize P to contain only its stopped recorder's accidental local output: first preserve byte-exact copies/hashes of the affected source map, generated CHANGELOG, reconcile audit and diff in its isolated runtime evidence directory. Recheck that the Y function's sole changed field is the measured artifact_sha256 CJ6aBh7BWJFcT2Vv0/cJFSXHaH5cs1LvqXvJRfkXHm8= -> 1L60sG1G9IaFfwe+LPNdE84DarlWCHKkdE8M5CyVI8o=, with no intervening legitimate edit. Then restore only that field to the pre-recorder value. Verify all other function rows and directory deployment facts remain byte/semantically unchanged as applicable; do not replace the whole file or reset the worktree. If the measured precondition differs, report rather than overwrite.

The bad generated CHANGELOG is not an accepted deployment record and must stay excluded from normal source commits; preserve it as forensic evidence for the eventual owner. Preserve the audit of the actual accidental reconciliation with its recovery explanation; do not erase history or claim the Y function was deployed. Pending directory-only record facts remain uncommitted until canonical repair/review; no manual recorder substitute or reuse of a past exception. This local containment is not a cloud action and does not close V1. P continues isolated combined source work and live tests. CLOUD push remains held.

## IRPT-Y-ACCESS-INTEGRATION-20260923 - exact integration grant and recorder issuer route

P180405 reports combined Y85af5eb95d/4ea95d1117/104d9472f11 with P4ec461a2e9/dd6edfc3aa passes implementer tests, but its canonical source commit is refused on thirteen Y-owned paths. Grant exact COO~P integration and narrow compatibility authority on precisely the thirteen changed files of85af5eb95d, enumerated individually in .owned-paths.yaml under new IRPT_Y_ACCESS_INTEGRATION_P. Preserve all Y/AE incumbents and Y semantic ownership. No wildcard expansion, base COO, other COO/CVO, recorder edit or deployment authority. Consume the committed grant through the canonical path before ordinary pathspec safe-commit. Preserve recorder partial outputs outside the source commit. P returns the exact combined source pin for CTO review; this temporary integration permission is to be removed after the accepted integration handoff.

CTO ran the actual owned-path resolver: all thirteen permit P and incumbent Y/AE identities; base COO, M and CVO P/Y refuse. Unlisted intake/parser.py, generation/job.py and the recorder still refuse P. All original lanes/path rules are unchanged; registry validator passes81lanes/316rules. This is measured permission repair, not a hook override or a source review verdict.

MSTR99710 relays Andrew's explicit authorization to bring CloudOps online for the bounded recorder repair and instructs CTO to message it once live. MSTR99711 confirms exact0.7.0_AE_CloudOps~O live at18:05:16Z. The canonical send guard refused CTO's ACT message because LD-0529 requires a COO-issued task order in that Tier-2 seat's own home; no message was delivered. Route the repair through COO~P as issuer: cut the bounded supporting task order for exact CloudOps~O and dispatch with its canonical order reference. This does not restart held B/F rounds or change the product's closer status. Work scope is solely the canonical recorder's explicit scope propagation and offline sibling-isolation regression proof already described in RECORDER-CONTAINMENT and CTO message to MSTR17:50:50Z. Coordinate with P before touching its evidence, preserve all records, no AWS mutation, no rerun until CTO reviews the pinned repair, no remote push. CloudOps prepares the fix; CTO remains direct reviewer. No user reauthorization is required for this already requested repair.

## IRPT-ANALYSIS-UPLOAD-OWNER-20260923 -- CRO99712 intake and bounded ownership

Authority: Andrew's standing delegation to CTO to adjudicate worker forks; CRO99712 reports Andrew's direction for brief fa42eb206f, org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_ANALYSIS_UPLOAD_AND_TICKER_RESOLUTION_BRIEF_20260923.md. This entry records the exact message body; the linked brief and its source measurements have not yet been directly reviewed by CTO. They are reported findings, not CTO-verified results.

Decision: COO~Y owns the IRPT security-resolution service and upload/ticker-resolution proposal. Existing P ownership of shared contracts/runtime and existing M ownership of source semantics remain; Y must identify exact shared paths and obtain the ordinary coordinated integration route. Live-first section0 remains the priority. This intake does not interrupt the current combined actual-viewer/acting-submitter closure or restart B/F canonical rounds.

Record of reported Andrew authorization: Kimi check/swap should mirror estate_report_runner.call_kimi_sub using the existing astn/kimi/api-key, with exact-ARN secret read for the resolver role. This is the requested design authority, not evidence that provider web search works, a new IAM grant has been applied, or a deployment is approved. Kimi suggestions/substitutions require explicit user acceptance on a new revision and report/PDF disclosure. Do not automatically substitute holdings. Preserve Target Weight versus Current Weight bases and show all findings.

Y proposal must preserve deterministic cache -> Opal reference -> one securities_info batch before the two Kimi call types; check suggestions shown only when FOUND; proposed check/suggest/substitute endpoints and standalone harness; shared IRPT session-broker lease, no second YCharts login; bounded three-round vendor-rejection retry. Directly measure the reported parser/route gaps and candidate compatibility before claiming closure. Kimi web-search support and credential/session-user identity remain unproven.

Boundary: live YCharts rejection-shape capture of3-5 symbols remains an explicit per-use Andrew call as reported by CRO; this receipt grants no such capture. No cloud mutation, secret access, live vendor call or CLOUD push is initiated by this intake. CTO remains the direct reviewer under Andrew's latest instruction; return a concrete pinned proposal and exact paths before shared-surface implementation/deployment adjudication.

## IRPT-DUAL-OWNER-SOURCE-20260923 -- direct CTO review and integration delta

BOUNDED SOURCE PASS: Y1385a126e7d9bbc9b4fe211cc708a52a93ce64e6 paired with exact P37526d36ae schema/storage, P9a3 access/P4ec Entry, M485b69c061 maintained sources, prior dd6 storage controls and8845 reader controls. CTO extracted fresh committed bytes into an isolated temporary archive and ran the unchanged suites separately with every declared environment installed: generation232+32subtests (29.11s), ops179 (20.15s), intake94+18subtests (1.10s). Total505 tests and50 subtests, no skips. Evidence DUAL_OWNER_CTO_REVIEW_20260923.json records full pins, extraction environment, output and hashes.

Reviewed behavior: verified actual submitter owns the new accepted request; original normalized input bytes/ref/creator and storage firm are preserved; retained input access/owner/expiry are rechecked before acceptance and dispatch entry. Frozen retry skips maintained profile/organization/recipe reads, worker/date reads use original input owner, recipe attribution follows actual submitter. Source descriptors preserve their explicit owner bindings. Actual guarded Entry is exercised offline. This does not establish a queue lease/send, live vendor generation, browser continuity, complete report/export, or full product acceptance. The30 earlier paired-seam failures reported by P remain carried findings, not closed by these505 tests.

Integration adjudication: P may consume exact Y1385a126e7 and M485b69c061 into its combined runtime candidate through ordinary owner gates. Added only three literal Y rules: ycharts/generate/frozen_worker.py, ycharts/generate/prospect_submission.py and ycharts/generate/tests/test_prospect_submission.py under infra/aws/lambda/investor-reporting/. Prior thirteen-file grant retained. Actual resolver confirmed existing IRPT_LIVE_SCOPE_P already permits maintained_sources.py; no additional M grant is needed. Semantic ownership remains Y/M; integration does not authorize unrelated edits. Registry validation and positive/negative actual-resolver checks passed; all incumbents preserved, base COO/M/CVO denied on the three new Y paths, unrelated parser/job/recorder paths still denied to P. Temporary integration membership is removed after accepted handoff.

Next: P returns the committed combined pin, real installer/port mapping and exact package manifest/cold-import proof. Preserve original authorizer semantics and carry the30 seam failures with precise applicability. No new deployment/vendor use/CLOUD push is authorized by this source verdict. CTO reviews the resulting artifact directly.

Recorder: P reports canonical supporting order45a93c3ae90b86ac224596a9e76d015a005fc260 delivered to exact CloudOps~O by receipt181819. This is dispatch evidence, not completed repair; fixed recorder/regressions/recovery proposal remain due for CTO review.

## IRPT-UPLOAD-RESOLUTION-IMPLEMENTATION-20260923 -- direct proposal adjudication

Reviewed pinned Y proposal c083bfdd5d (UPLOAD_RESOLUTION_PROPOSAL_20260923.md and reproduction JSON) and CRO brief fa42eb206f, including Andrew's verbatim section0 instructions. Authorize bounded LOCAL implementation under the existing IRPT completion mandate and CTO fork authority. This supersedes4cdac345db's proposal-only boundary for the work below. Existing paired runtime integration remains P's first priority. No new independent reviewer gate.

Approved design: dedicated A/B-only CSV/XLSX template adapter (not a change to generic attachment parsing); four explicit B1 bases; Dollars is USD by declared template contract; current/target weights stay distinct. Preserve original file and row provenance; v2 normalized inputs with unchanged v1 replay; mutually exclusive new file_base64/file_type and legacy csv_base64 arms. Approve declared initial bounds1MiB file/8MiB expansion/2000 rows/200 symbols with explicit findings, no truncation; +/-0.001 weight tolerance, disclosed proportional factor/residual/reference notional, no implicit cash plug; percentage conversion and other corrections require a new approved revision. Cash-label normalization and duplicates retain census and notices. Shares need dated canonical price evidence. Existing signed custody-source policy is unchanged; this is the prospect template contract.

Approve complete findings, deterministic cache -> canonical Opal reference -> one unresolved YCharts batch; identity evidence is not provider-availability evidence. UNKNOWN/UNAVAILABLE cannot become NOT_FOUND. Check and swap are separate advisory call kinds; suggestions/proxies displayed only after deterministic FOUND validation. Each correction/substitution/exclusion is user-approved on a new revision bound to original bytes, actual actor and retained proposal/provider evidence. Screen and PDF disclosures are mandatory for publication. Preserve original input creator and actual submitter separation already reviewed583d2da. Approve asynchronous Kimi work and authorized polling, three generation-rejection rounds with new request/input lineage, and offline-default standalone endpoint harness.

Kimi authority correction/confirmation: CRO section0 records Andrew explicitly authorizing Kimi for this feature using the same API key. Record this as feature-specific RUNTIME model-use authority (not merely design preference), limited to unresolved symbols and optional other symbols, no amounts/client/firm/actor identifiers. Exact-ARN resolver-role read of existing astn/kimi/api-key belongs in P's concrete plan; no applied IAM/deployment or secret read is established here. Preserve existing estate call mechanics while bounding retries to transient failures. Kimi web-search capability is unproven; propose exact provider QA invocation and expected evidence before execution. No silent alternate vendor. Agent-initiated YCharts calls still require Andrew's distinct per-use word; no capture/probe is granted by this ruling.

Writer adjudication: Y owns its proposal's template/normalization, resolver/advisory, worker/rejection/status, analysis-UI and focused test/harness paths. P owns public schema/wire/client/adapt/display/export integration, retained storage and runtime/infra installation. M supplies canonical security identity/classification/dated-price reader interfaces with exact source/path provenance; no parallel Y crosswalk or invented prices. Coordinate pin/path claims before overlapping file edits, using established ordinary commit gates.

Shared lease decision: actual current ownership maps ycharts/session/broker.py to IRPT_COMPLETION_Y, not P. Y is the single writer of provider-operation arbitration and broker/generation/resolver consumers; P supplies the shared conditional storage/runtime/resource installer and records the exact interface. Existing session publication fence and per-job lease remain distinct and are not misrepresented as global operation serialization. Start with broker.py and an explicitly named ycharts/session/operation_lease.py plus focused tests if needed; no capture-host/login rewrite. One account/session operation boundary must gate all these consumers, enforce globally shared2s spacing, renew/assert/release with fencing and bounded timeout, and refuse stale ownership. Release before waiting on Kimi, reacquire/revalidate for provider candidate checks. Offline concurrent-job/resolver, expiry, stale-fence, contention and crash-recovery controls are required. Return the pinned shared interface and exact storage/resource requirements; no cloud mutation authorized. No P-on-Y broker grant is necessary or granted.

Acceptance remains the proposal's exact paired offline matrix plus actual package/runtime evidence and subsequently authorized live trace; proposal reproduction findings are Y-reported and source-attributed, not a new CTO-run template test. Current served route availability must be measured on P's current runtime instead of assuming the older NO-HANDLER source observation still describes it. CLOUD push remains held. Missing live evidence is not a reason to park authorized local implementation.

## IRPT-LOOKUP-CAPTURE-20260923 -- CRO99713 evidence and runtime direction

Read CRO99713, pinned authorization/updated brief d7d044ba7a, and committed securities_info/ALPPL fixtures. Andrew's recorded per-use word authorized CRO's small lookup test; it was performed. The earlier blanket statement that lookup capture still awaits authorization is superseded for this completed capture only. Do not repeat it or expand it into upload/report/vendor mutations. Holdings-upload rejection capture remains a separate per-use call; no new vendor action here.

Fixture scope: the completed five-symbol HTTP200 batch returned AAPL/VNQ/$:CASH and omitted ALPPL/BREIT. ALPPL typeahead returned ten empty lists. These establish those concrete cases, not a universal theorem that YCharts never tolerates typos. For a validated complete successful batch, compute absent identifiers from the requested-versus-returned set; malformed/incomplete/error responses stay UNAVAILABLE. Exact lookup absence is not proof a security does not exist under another identifier. CRO reports BREIT typeahead with nine M:BREIT.* classes requiring evergreenFundData: distinguish identity from availability/entitlement, preserve class/namespace, do not invent a share class or infer entitlement from HTTP200. Namespaced retries must be explicit, bounded and evidenced, not an unmeasured live probe. Y consumes the committed capture as offline regression fixtures.

Andrew pins kimi-k3 for BOTH check and swap, using the estate request/JSON/API mechanics and same key. No faster-model substitution without a new direction. Web-search capability remains unproved; source-shaped mocks are not proof of tools or grounded citations.

Runtime architecture decision: retain the canonical IRPT broker/session contract and complete the existing runner deployment path, rather than add a resolver-only credential/login bypass. P prepares an exact runner artifact/configuration/role/SSM installation and rollback plan for CTO review with the incumbent owner; Y supplies broker compatibility and shared operation-lease requirements. Any required CloudOps execution is a separately scoped COO-issued order, not an expansion of its recorder-repair order. Before any browser/login action the plan must identify the shared provider account, existing gateway/Alyssa consumers and how one session authority avoids eviction; if this cannot be demonstrated, return that concrete blocker before applying. The observed working credentials session is QA evidence, not permission to copy secrets or start a second login. No install, login, IAM change, host stop, capture or CLOUD push is authorized by this design decision.

CRO-reported runtime state: no AWSCURRENT on ycharts/session/current; SSM command05309085-4a7a-41d4-b070-b8d1b76832cf on i-0167fd745ad906a66 failed127 due to missing /opt/investor-reporting-ycharts/run-ycharts-session.sh. This shows a currently unavailable path, not by itself proof that the secret was never populated historically. Host remains running after CRO's test. CRO retains the originating test/cleanup disposition record and routes its outstanding host-stop decision to Andrew; CTO has neither stopped it nor reused the per-use capture word as deployment authority.

Current paired Opal runtime integration and authorized offline upload-resolution implementation continue; live generation readiness is not established by the lookup capture.

## IRPT-SESSION-DELTA-20260923 -- CRO99714 and Andrew availability rulings

Read exact CRO99714 and pinned delta brief d401c1a768. CRO confirms prior evidence corrections applied. Andrew's reported explicit product direction supersedes any flow distinction that would leave a missing or feature-gated security stranded: a symbol absent from a completed valid lookup triggers Kimi check; a security unusable behind entitlement/paywall enters the same check/swap resolution path. Retain internal provenance/reason (exact miss, known gated identity, namespace/class) for cache policy, explanation and disclosure; do not pretend the security does not exist. Service outage, malformed response or route error remains UNAVAILABLE, not a symbol miss.

Session implementation delta: retain existing ycharts/login/credentials and ycharts/session/current; preserve legacy credentials consumers. No new secret namespace, second runner or Lambda login. Existing library/broker/SSM/IAM artifacts are reused after exact inventory; CRO's source/deployment statements remain attributed pending P's concrete artifact/runtime check. D1 is the missing runner installation plus bounded first session run, D2 the missing durable refresh controller, W1 caller recovery wiring. P's existing plan assignment57c263bee4 includes D1 exact artifact/config/SSM/rollback plus runtime/resource/control-plane installer for D2. Y remains single writer of session/broker/operation-arbitration logic and W1 generation/resolver consumers, and may implement D2 controller logic offline within ycharts/session/ with a pinned exact-path/interface manifest coordinated with P. Do not reimplement library login, fencing or publication rules. No new CloudOps execution without separately issued bounded order.

Recovery contract: classify EACH failed pull by status and verified response shape/body; a healthy probe cannot override a failed application endpoint. Verified concurrent-sign-in or signed-out response may request one existing bounded refresh; verify new session generation/fence before idempotent continuation. Recognizable login-page response is distinct from generic HTML/WAF. Entitlement is not staleness and never requests login. WAF uses the existing browser/challenge path, not a password retry loop.429/timeouts back off within limits; ambiguous mutations reconcile before replay. Unknown401/403, unclassified HTML or a possibly wrong-route404 require bounded diagnostic/attention behavior, not an automatic login or a false NOT_FOUND. This narrows the brief's proposed unknown-body SIGNED_OUT default and its blanket404 lookup classification; return concrete contrary measured evidence for adjudication. Never contest a human login with repeated reacquisition.

D2 durable wait/continuation and shared operation lease must be reviewed together: one refresh in flight per shared account, monotonically fenced completion, idempotent resumes, bounded retry/timeout and concurrency tests. Host stop logic must distinguish a host started by this operation from an already-running/operator-owned host and must not stop work belonging to another owner. This is offline implementation authority only; it does not activate EC2/SSM/host-stop/login permissions. D1 sign-in and the proposed two failed-pull captures remain Andrew's separate pending per-use calls; CRO retains current host disposition. Offline D2/W1 work may proceed while D1's concrete plan is prepared; deployment/live exercise follows actual prerequisites, not a new approval waterfall for local work.

## IRPT-PUSH-HOLD-RELEASE-20260923 -- Andrew-direct via MSTR99715

Read exact MSTR99715 (20260923T184102Z). Andrew directs laptop-led DEV and CLOUD pushes, with SITEZ pulling/merging laptop CLOUD; no reverse SITEZ integration on this device. Record pointer supplied by MSTR: org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260923_1845Z_PUSH_DEV_AND_CLOUD_LAPTOP_LEADS_SITEZ_MERGES.md @5c70b8a322. The earlier push hold is RELEASED. Prior rulings saying CLOUD push remains held are historical and superseded on this point.

MSTR is the single push coordinator and reports CLOUD push underway; this entry is not proof that either remote push completed. CTO replied with prior directly reviewed localhost frontend10141b6d0bbb007d5dd9e758f11f785216e11339 as the DEV candidate, with no newer reviewed frontend substitute known. P must name any concrete newer candidate to MSTR. Source parity and bounded Global/SelectFirm bootstrap evidence do not establish full IRPT generation readiness. Backend dual-owner/runtime and upload/session implementation continue under their exact review boundaries. No duplicate push from this seat; cloud apply/login/vendor/host-stop authority is unchanged by this repository push direction.

Y184114 acknowledges078349 and claims ycharts/session/controller.py plus ycharts/session/tests/test_controller.py under the investor-reporting root for local D2 implementation; P supplies runtime/SSM/host ownership proof. This is an implementation claim/ACK, not a completed controller or control-plane action.

## IRPT-UPLOAD-RESOLUTION-SOURCE-20260923 — direct CTO partial review

Read exact Y190653; reviewed source6cfe01c3e238e9a90e88d3a501b25ac0eaf41540 and handoff8228a253e2. Fresh archived source with pinned paired dependencies passed435 tests+50subtests, no skips. Offline CRO fixture and synthetic harness replays completed. Evidence: UPLOAD_RESOLUTION_REVIEW_20260923/REVIEW.md and retained outputs. This is partial-source evidence, not feature/runtime/global-account-serialization acceptance.

CTO-Y-KIMI-DEADLINE-01 is OPEN: fake-clock check returns success after238s against promised120s total limit because retry resets its budget. Y receives bounded local repair with one absolute deadline, remaining-time transport budget, telemetry/exhaustion/late-result controls for both kinds. Receipt191250. Known W1 status-only legacy broker fallback stays OPEN; controller and legacy-regression passes cannot close it.

P proceeds with concrete shared admission/storage/CAS/outbox/transport/D2 runtime mapping and exact artifact evidence under its existing scope, carrying this defect until repaired. Y completes caller wiring, approval/revision/lineage and UI under its existing mandate. M canonical identity/dated-share-class price facade remains missing; Shares explicitly unavailable. No live QA, secret access, cloud mutation, login, host stop or broad acceptance granted by this review. CTO remains reviewer.

## IRPT-KIMI-DEADLINE-CLOSURE-20260923 — CTO-Y-KIMI-DEADLINE-01

Direct review of Y5609c2e46a2d36716743f21a8e6a5eec6876e5d8 (handoffc0867388b4) closes the bounded SOURCE defect opened7c8484466c. Fresh archive focused43 PASS; full intake190 PASS+18subtests, no skips (focused suite is a subset). Original CTO119s503+119s valid-response control now passes only1s remaining to retry and returns null/KIMI_TIMEOUT. One total monotonic deadline covers preparation, telemetry, both attempts and parsing. Evidence KIMI_DEADLINE_CLOSURE_20260923/REVIEW.md and outputs.

This does not prove real I/O interruption: injected blocking callbacks cannot be interrupted by this synchronous source; installed transport must enforce remaining wall time. P may consume this exact repaired source under existing local integration authority. All other partial-source/runtime/W1/canonical-price/UI gaps remain open. No live vendor, secret, deploy, session or host action authorized by this bounded closure.

## IRPT-HOLDINGS-JOURNEY-RESTART-20260923 — Andrew-direct record via M

Consumed exact M192923 and HOLDINGS_RESTART_20260923.md@b14966e203, including the recorded verbatim Andrew instruction to decide and implement the Holdings journey. Preserve M's sequence: first real Cottonwood custody account, then49F08335338 custody with SmartX as sole model authority, then INF Orion custody with Eclipse overlay. All three remain required; custody census must include assets outside model-platform coverage. No targets relabeled actual, missing value inferred zero, assumed currency or invented strategy/model mapping. Accepted and blocked accounts remain explicit.

Existing CONTRACT.md ownership applies: M custody/overlay adapters and Holdings presentation; P shared runtime/package/status/selection/accepted-reader integration under current exception. P notified193013 to coordinate exact M candidate and complete source revision -> publication -> authorized API -> real-login rendered screen. No new canonical round. Security-reference/analysis-export enrichment is off the Holdings critical path; preserve it in respective lanes without making it a Holdings prerequisite. Prepare exact candidates and apply existing review/operational gates; tests do not activate schedules. CTO remains direct reviewer.

M reports empty serving prefixes and accepted indexes, disabled schedule and September21 Lambda plus specific COT/INF source defects. These are attributed observations from its private source audit, not independently remeasured CTO live findings. Source and live acceptance remain open.

## IRPT-W1-BROKER-REVIEW-20260923 — actual body observation and correlation gap

Direct fresh-archive review of4173322f457aeeb390033b410e85bebadc49a3e3 (handoff92fbf25c76):54 session tests PASS; separate rotation/eviction/controls/network-guard regression all_pass true. Status-only/self-reported refresh fallback removal is substantiated within run_with_recovery. Full W1 remains OPEN.

CTO-Y-W1-CORRELATION-01 OPEN: actual wrapper with a synthetic job receiving known signed-out application401 then unrelated healthy diagnostic200 returns NOT_AN_EVICTION despite the application failure. Existing078349 says healthy probes cannot override failed application endpoints. Y193152 receives bounded causal-request correlation repair, with stale/contract/mutation negative controls. This is an offline boundary finding, not a deployed-path claim. Evidence W1_BROKER_REVIEW_20260923/REVIEW.md, exact outputs and probe. No live action/new operational authority from this review.


## IRPT-THREE-TAB-DRIVE-20260923 - Andrew-direct closer orchestration

Andrew's current CTO-session instruction: "COO~Y should be driving /closer on "Analysis" (YCharts product), COO~M should be working on "Holdings" (model overlay and holdings product), and lastly COO~P should be working on "Reporting" (the performance reporting project)." He directs CTO as master control plane to keep agents organized and drive E2E completion, with targeted CRO research. Earlier direct-CTO-review instruction remains; no new independent reviewer.

Reviewed desktop package index and all six briefs against current source/handoffs. CONTRACT.md v1.4, COO_P/M/Y.md and CONTROL.md implement this direction without new seats, canonical rounds or path-grant expansion. Historical v1.3 detail preserved in CONTRACT_V1_3_REFERENCE.md. Existing canonical B/F project.json rows already point to this contract; generated index copies omit the field and are not hand-edited here.

First milestones: P Cottonwood BD actual-account report to screen while CRO targets49F SmartX actual-performance uncertainty; M Cottonwood actual custody publication/drill then49F/INF; Y valid dollar-upload Overview through real worker/vendor/certified report/screen. All prior three-firm, unit/variant/export acceptance stays required. SmartX remains49F primary, BD verification only. P retains shared writer responsibilities with explicit integration queue; M/Y remain owners of complete product assembly and consuming the result. Security-reference enrichment is parked off Holdings critical path; other Analysis units remain required later. No ACK-only messages; publish current STATUS and interface/blocker/review handoffs.

Current source confirms Reporting still deliberately returns source-unproven for all providers and export submit NOT_READY. Analysis has bounded source proofs, not installed live chain; Holdings source gaps/live emptiness are M's attributed audit. No fresh deployed-byte or browser completion certification is claimed. Existing reserved operational authority and push coordinator remain; prepare exact actionable runs, do not ask Andrew to repeat existing permissions.

Latest M193625 evidence changes the first Holdings proof to one unambiguous INF account: M reports876/876 account totals reconcile to positions, while COT currency and null-value coverage block truthful acceptance. CTO accepts this sequencing fork within delegated authority; COT/49F remain mandatory and proceed on source gaps. This supersedes the COT-first sentence immediately above. Contract v1.4, CONTROL and M mandate already reflect INF-first.

Routing receipts194210(P/M),194211(Y),194212(CRO) delivered c7265d2bef instructions. New candidates M35999d31a4, Yfe0ec628c2 and CloudOps0116b83bc0 are queued for direct CTO review, not accepted by this dispatch. CloudOps broader JSON_TOOL fallback surprise is parked with tooling owner pending a concrete platform need; its exact recorder repair/recovery candidate remains on the active review queue.


## 2026-09-23 20:20 UTC - reviewed deltas and SmartX method boundary

CTO accepts bounded source deltas Y84c6, M Portal e560 and recorder0b8784 per DIRECT_REVIEW_2020_20260923/REVIEW.md. P integrates exact files through existing grants; no live product PASS. P delivery failure is measured frame-cap saturation, MSTR recovery owner; preserve handoff/edits.

Andrew at CRO, record ebf1a0f6b5, verbatim: "All approved, go now". Capture and named personal-login calls were approved; selected-set SmartX unavailability accepted. Do not fabricate custom-window account returns by summing or averaging sleeves. Provider period-to-date statistics may be implemented with their own verified units/as-of/identity; allocation decimal evidence does not automatically establish account-statistic units. Carry method/fee basis as not stated. Current-roster absence is insufficient to prove historical completeness; explain the two missing allocations from retained opening dates/historical census, and distinguish provider date semantics from UTC timestamp equality. Nine unexplained monthly formula exceptions remain evidence, not a license to relabel method as TWR. CRO clarifies using retained capture; no further call or general personal-credential runtime grant inferred from this bounded capture.


## 2026-09-23 20:27 UTC - COT external identity parity

P a70f6e3b71 returns contract_validated=true when accountInfo.externalId is absent or conflicts with the mapping. P repairs both period/series checks and pre-I/O mapping completeness; numeric ID alone does not settle the unproven COT namespace. Evidence DIRECT_REVIEW_2020_20260923/P_PERFORMANCE_REVIEW.md. No broad suite requested; source/retention composition continues.


## 2026-09-23 20:29 UTC - concrete source blockers

CRO c12fe7099b clarifies retained SmartX data: account PTD decimal evidence1account/4periods; provider-as-of absent, retrieval time only. Do not fill dated-as-of contract with retrieval time. Window-end open roster matching44/44 and42/42 settles only that denominator; whole-window closed-account completeness remains narrower than a general completeness claim. Large-flow association does not establish the precise return formula: carry provider method unknown and preserve provider value. Eastern calendar-date bounds measured; do not silently treat provider midnight epochs as UTC dates. No additional capture requested.

M actual INF positions reader is blocked by NEW legacy source literals. Existing NAMING_LEGACY_READS intentionally cannot admit new sites. G is the bounded naming-owner route for a truthful existing landed-read locator or smallest exact mechanism proposal; CTO will adjudicate it. Do not insert an ineffective waiver, guess a canonical repoint, hide literals or bypass gates. This is a live-thread blocker, not general naming enrichment.


## 2026-09-23 20:35 UTC - INF source locator: reuse the producer's key helper

MSTR99749 confirms G orderly CLOSED. CTO now resolves the fork directly. No new naming seat or gate amendment is needed for the proposed route: data/inf/scripts/silver/_orion_api_silver_lib.py already owns silver_api_dim_s3_key(dim, snapshot_date), and the real write_silver_api_dim_parquet producer calls that same helper (lines350/479). Current source blob6ad80c3b007a3119ac536b94c05b99bffdbba1c9. It formats the actual landed positions_mv key.

M may reuse/import that existing source helper for positions_mv only, as a dependency, rather than adding another literal or a second formatter. Derive the partition-list root from its actual formatted key with an explicit expected partition/file shape check; keep the existing validated cutoff selector and VersionedInputs receipts. The read bucket remains the already-evidenced Inflection source, not an unchecked environment override. Do not invoke producer write functions, copy/extract a new string formatter, repoint data, modify the old01 read context or extend its waiver. This is reuse of an existing producer contract, not a source migration or general read exemption.

Implementation must package/pin the actual helper dependency. Its module constructs an S3 client at import; do not accidentally use that client for the version-bound IRPT read or execute producer side effects. M supplies a focused key-equality/cutoff receipt plus ordinary naming/commit verdict. If that concrete reuse is refused, return the precise gate line; do not silently disguise the literal. Currency remains a separate source fact, with absent data refusing.


## IRPT-RESIDENT-INTEGRATION-20260923 and source review 20:48UTC

CTO direct review accepts bounded Y4ed7ed resident assembly, Mb411 native INF adapter/helper reuse, and closes P external-identity defect at214ddd. Exact limits in RESIDENT_ASSEMBLY_REVIEW.md and M_P_SOURCE_REVIEW.md. CONTRACT amended with existing-lane P exact integration rows; semantic Y ownership and reserved runtime proof remain. CRO8246 corrects INF currency evidence: use retained USD Scope only for exact same-account/date positions bridge, not tenant-wide inference. COT currency confirmation is pending Andrew; preserve unavailable denomination and continue independent composition. No extra vendor call, independent review queue, or broad test rerun.


## Andrew d70decd6b2 Tax source amendment and20:54 control

Read exact CRO~M99756 and verbatim Andrew B. CONTRACT/COO_M now replace prior Tax-in-Client line: canonical workbook Traded membership -> SMAs/ALT Strategies/Tax, exact dated history and net_mv_plus_cash; unresolved claims preserved. Current M49F work integrates this now; other first flows continue. No workbook AUM as custody total. CRO~M traces two absent traded claims from retained sources. Mce2fd bridge comparisons all six mismatch; targeted CRO valuation semantics assigned. Y8d3 capture-source finding holds new bootstrap only; precise secret-read ambiguity repair sent205113. See HOST_CAPTURE_FINDING.md; no broad test/live replay.


## Andrew-direct COT USD 2026-09-23

Exact direct answer retained in ANDREW_COT_USD_20260923.md. COT report amounts are USD; P shared mapping/provenance, M custody consumption. Close denomination blocker and proceed with actual report/custody serving. No vendor-body rewriting, new currency query, or widening to other firms/native security currency. Null/valuation/census proofs remain. First ready Holdings firm/account may proceed; all firms still required.


## INF exact valuation bridge and Tax intake 21:02UTC

CRO99763/10f3cf6f9f measures two accounts on three exact file/valuation pairs:06-11/06-10,06-19/06-18,09-10/09-09; all six value/units match, same-key negatives reproduced. CTO routes precise version/hash-backed provenance to M; no blanket next-business-day roll, request-date rewrite, historical-file inference or tenant-wide USD claim. Source-specific currentValue denomination can bind only the measured observations. COT first flow continues6f45.

Tax99761/907d: research snapshot schema differs from canonical capability, canonicalSilver/member history empty, supplied production store stub. M prepares exact intake recipe; MSTR210127 asked to identify available existing Tax source/release owner/later wrapper. No fake envelope/history or duplicate pipeline. CRO~M current missing-account retained-source search complete; two claims remain unresolved. COT empty-response likely-data diagnosis is an inference, not a new identity rule or vendor-call permission.


## 2026-09-23 21:10 UTC - selected COT source and bounded Tax dependency

7033e23490 selected-account custody source receives bounded CTO PASS: three affected checks and two asymmetric census probes; no live acceptance. M continues actual account mapping/currency/publication. MSTR99766 confirms T wound down and three-COO cap full. No fourth seat requested: existing M prepares the minimum canonical Tax-module dependency recipe, exact paths and runtime effects for CTO adjudication under Andrew Tax B; full historical Tax round remains outside this transfer.


## 2026-09-23 21:16 UTC - Performance source fidelity and policy activation

9e1bc3a751 composition has five focused CTO PASS checks, but P-SOURCE-01 REWORK: parsed JSON retained without original response bytes/digests does not satisfy X10 source family. P supplies exact transport/evidence repair and existing approved reply replay; no new vendor call. Policy activation remains tied to exact enforcement/package/role/destination proof, not a broad state flip from fixtures. Physical disposal stays OPEN under existing X10 and is not a new first-thread prerequisite. P prepares concrete bounded cutover; M retains registry ownership; CTO reviews directly.


## 2026-09-23 21:15 UTC - COT no-position rows and available history

Consumed CRO99769 evidence f307d5841512f8de005b2dd5272350029d1f1b11.
Ruling: for the measured canonical COT Assets_Dim/includeAll export contract,
rows with all four position facts (Market Value, Units, Unaccrued Market Value,
Accrual) absent are dimension-only/no-position-at-as-of rows. Exclude them from
active holdings facts, counts and weights; retain original bytes and excluded row
ordinals/counts in private evidence. Do not convert to zero holdings. Partially
missing facts, held-but-unpriced rows, conflicting duplicates and failed independent
account reconciliation remain failures. Check selected account census against the
independent account valuation before publication. Do not assert every such row
represents a historically closed position: the export also lists later/onboarding
accounts for earlier dates. M implements this narrow producer interpretation.

P: Cottonwood historical availability is account/window-specific. Sparse pre-May2026
coverage does not make every 2025 account invalid, nor does onboarding establish
real inception. Show provider coverage and unavailable periods honestly; never
relabel a partial onboarding window as requested full YTD/since-inception. Current
positive COT account remains the first thread, without another blind vendor retry.

Andrew-direct relayed by CRO at f307d58415, verbatim:
"Cottonwood only has data from maybe a couple months ago, they dont have full data in BD yet as far as I am aware"
"come october we should check again"
"actually, maybe worth just doing a little egress, check right now and see how much cottonwood data there is in 2025"
That per-use CRO check is already executed and does not authorize another use.
October recheck remains parked with CRO, not a blocker to current IRPT completion.


## 2026-09-23 21:19 UTC - M/P mapping seam

M-P-MAP-01 reproduced on614ad2f16b paired9e1bc3a751: M source_revision dict rejected by published P string interface. M keeps source_revision as exact source SHA256 string and carries full receipt under source_provenance. P preserves full mapping evidence. One actual callback-to-consumer request-construction control closes it; no new vendor use. Real selected COT build remains M-reported, not CTO-live acceptance.


## 2026-09-23 21:23 UTC - actual COT source clears first thread input

CTO independently replayed d8173c1b9c on seven exact real S3 versions:57positions/USD19705844.84 exact reconciliation, schema and all receipts match. Three narrow exclusion controls PASS0.64s. M now drives this same P-positive COT account through accepted publication/API/UI, remaining owner of whole Holdings journey; P only owns shared surfaces. Mandate first-account sequence updated. Portal c70855f3 five receipt/render controls PASS526ms; not live reopen/export. No product marked complete or unapproved publication performed.


## 2026-09-23 21:25 UTC - paired source repairs closed

P-SOURCE-01 CLOSED5765ea21a5 with6focused fidelity/composition checks0.74s. M-P-MAP-01 CLOSED9b3fb2a actualS3 callback into latestP5765 request constructor, full receipt retained. Final P package consumes9b3 mapper, not older614 included in5765. Source and adapter readiness clears these defects, not storage policy/live journey. P prepares exact cutover; M retains full Holdings publication/API/UI responsibility under1960 mandate update.


## 2026-09-23 21:28 UTC - bounded Tax store writer and Reporting infrastructure

55145056df recipe accepted for source implementation. Exact Tax membership module and its test narrowed from ANY to M-only in .owned-paths with CONTRACT; no fourthCOO/fullTaxround/scheduler/livecall. One-shot runner reuses whole existing canonical modules, no fabricated capability envelope/history. P canonical reporting bucket NoSuchBucket evidence is accepted as next infrastructure task under existing IRPT core Terraform ownership; prepare minimal exact plan, keep policy pending until cutover adjudication.


## 2026-09-23 21:36 UTC - first native Holdings publication and empty Reporting storage

CTO direct review accepts a86430e39e bounded initial COT publication under exact selected-account/date/source-result checks, absent-index CAS and version readback; M owns execution/API/screen, P exact reader package plan. Source controls5PASS0.62s; live old Lambda/index absence independently confirmed. P f4a1dd60a3 binary storage plan c7639c4c06ba726a8df246c4c5742da6c70e22890940fdbbd38535c8f8329a90 independently reviewed5create0change0destroy; exact safe-apply permitted with readbacks, no automatic policy activation/data-write/runtime deployment. Review: DIRECT_REVIEW_2020_20260923/COT_PUBLICATION_AND_STORAGE_PLAN_REVIEW.md. All products incomplete.


## 2026-09-23 21:42 UTC - Reporting package dependency

P-PACK-01: exact9cc2d2d9 candidate omits org/standards/NAMING_SCHEMA.json; fresh extracted canonical destination probe fails. Adding only pinned schema in scratch makes identical probe pass. P repairs both review/canonical package, returns final manifest/hash and one probe. Source/mapping acceptance and73c40 empty-storage apply remain intact; no vendor call needed. See DIRECT_REVIEW_2020_20260923/P_PACKAGE_NAMING_REVIEW.md.


## 2026-09-23 21:42 UTC - native COT publication independently verified

M5e29e43c2c executed bounded initial publication. CTO independently read4exact output versions, verified lengths/hashes/index acceptance/Gold-JSON nodes and selected1account57positionsUSD19705844.84 at2026-09-22. Accepted revisionfe328763b5da690cc1a48ca4681444f167386578f3f0dfadb45f195459906a4e. Native storage hop PASS, not authenticated API/browser. P exact reader cutover next; M retains complete Holdings ownership. CONTRACT first-thread row aligned with prior1960/73c40 COT ruling; all firms remain required. Evidence DIRECT_REVIEW_2020_20260923/COT_NATIVE_PUBLICATION_CTO_READBACK.json.


## 2026-09-23 21:43 UTC - Analysis runtime recovery

MSTR99771 recovered Y to fresh thread01a0d037 with preserved4ebe source/drive4876 and measured turn/steer injection. CTO rechecked9/9GREEN, new bridge33676/detector34768/heartbeat33548, endpoint58180, stderr0. Agent-side reply/read pending; do not confuse transport recovery with product completion. P continues under Andrew at its current terminal, migration reserved to MSTR on his word.


## 2026-09-23 21:50 UTC - live reporting storage and two narrow repair closures

CTO independently verified new opal-data-irpt versioning/KMS/BPA4/TLS after exact reviewed P apply. Bucket absence CLOSED; policy activation/consumer runtime not implied. P-PACK-01 CLOSED5cdb/v4b9333947 on actual extracted59member artifact/Python-I unchanged destination probe. Y capture secret-read finding CLOSEDbfe6469b1e with10focused adapter-worker cases2.55s; exact3files already P-integrable under existing grant. No vendor calls; no live product completion. See direct review storage JSON/report and appended HOST_CAPTURE_FINDING/P_PACKAGE_NAMING_REVIEW closures. Browser connection absent this turn; authenticated screen proof remains pending.


## IRPT-CROSS-FIRM-PUBLICATION-20260923

CTO directly reviewed 2874e37647: twelve affected offline cases pass. P receives
exact integration ownership of infra/aws/lambda/investor-reporting/ycharts/generate/publisher.py
under IRPT_Y_ACCESS_INTEGRATION_P in the same commit as this contract. The other
three changed files already have that grant. Y remains semantic implementation
owner. Preserve actual current actor, accepted data firm and immutable original
input owner separately. No principal synthesis from queue tenant. P integrates
with bfe6469b1e and supplies the current-authority host/installer boundary; Y owns
the real-login Analysis journey. Source PASS is not live completion or deploy GO.


## IRPT-TAX-DISPOSITION-SOURCE-20260923

CTO direct review d3a8c3e7e3: bounded source PASS; seven isolated persistence cases pass0.12s. TAX_DISPOSITION_STORE_REVIEW.md records exact scope. M continues the granted one-shot runner and returns exact gateway capability/runtime plan. No vendor/cloud activation or historical backdating. Full snapshot failure cannot become partial success.


## IRPT-HOLDINGS-READER-APPLY-20260923

CTO grants P bounded GO for exact saved ca2a907770c081a244cb1eddc854db95cdb80523655989093264c9e20f905301 plan only. HOLDINGS_READER_PLAN_REVIEW.md/JSON carry artifact bcb3fb71, immutable version, exact pre/postapply conditions and independently exercised native read. One create/three updates/no destroy, read permissions only. Deferred artifact lookup requires exact version/hash guard; drift stops closure. M retains real authenticated API/browser proof.


## IRPT-TAX-SILVER-SEAM-20260923

CTO inspected gateway app/taxsma_workbook.py@6abf60e5d5 and the current Silver
consumer: _snapshot emits seven flat business fields alongside row metadata,
while _typed_row requires nested business and refuses that producer shape. The
current synthetic Silver fixtures manufacture the nested object. used_rows in
the canonical producer includes the header, so complete data rows equal used_rows-1.
This is a concrete adapter mismatch on the authorized Tax Holdings thread.

M is sole writer for exactly data/mdpf/scripts/silver/taxsma_workbook.py and
data/mdpf/tests/taxsma/test_taxsma_workbook_silver.py under IRPT_TAX_MEMBERSHIP_M,
recorded in .owned-paths.yaml in this same commit. Consume actual canonical flat
rows, preserve original Bronze bytes/digest and all seven typed business columns,
row metadata and full census. Explicitly refuse incomplete/mixed/contradictory
shapes rather than silently choose one. Any retained nested-fixture compatibility
must be explicit and unambiguous; do not claim that compatibility proves the
production seam. Validate the actual producer output through the Silver boundary
with one focused positive and malformed/partial negative controls. No broad suite.

This adds only the necessary Silver adapter/census and tests to the existing
bounded one-shot runner preparation. Do not change Gateway, manufacture a new
Bronze envelope, backdate observation, schedule the full pipeline or perform a
vendor/cloud write. Return the pinned repair and exact runner/runtime plan.


## IRPT-PERFORMANCE-LINUX-20260923

CTO independently reran exact b933 function /121b8407 native layer /common5 in Lambda Python3.12 Linux with networking disabled: mapping and retained response calculator/schema PASS,1period15points. Combined uncompressed239627841bytes. PERFORMANCE_LINUX_CTO_REVIEW records hashes and limits. Native compatibility closes only for these bytes; deployed factory/role/storage/browser remain open. CONTROL refreshed to measured current state.


## IRPT-HOLDINGS-LIVE-READER-20260923

CTO actual AWS readback: irpt-holdings Active/Successful at22:10:08Z, exact vLP7cZN61JWOOmiCGmCjnOM43296i8qDt1hL1ZE8yUs=, reviewed environment and both reader IAM policies equal saved plan; current artifact version e7XAGneq1_KKe2tnBVK45FsEFNItS2NF matches. HOLDINGS_READER_CTO_LIVE_READBACK.json records evidence. M proceeds authenticated selection/API/screen/drill/reload. Localhost5174 returns200; current computer-use inventory has no connected browsers. This is deployment configuration proof, not a fabricated-auth or browser PASS.


## IRPT-HOLDINGS-ACTUAL-FAIL-20260923

Andrew authenticated Anna Holdings NOT_READY is actual journey FAIL. HOLDINGS_AUTHENTICATED_FAILURE.md records exact evidence and limits. M owns selection/date/coverage trace and supported full COT build; P shared reason contract. No happy-account substitution, identity collapse or fake empty values. Prior code/IAM parity is not withdrawn or inflated to journey PASS.

## IRPT-X10-ACTIVATION-OWNER-20260923

CTO owns enforcement acceptance; M is existing exact registry writer with CRO incumbents preserved. Global irpt-x10-v1 has12families/3firms; enforcement_ref must be full accepted receipt commit, not arbitrary source/bucket-create. P proceeds callable/claim/least-privilege plan and shared enforcement matrix for all36destinations with precise deployed writer coverage. Minimal COT permissions alone do not prove global enforcement. Physical_disposal OPEN remains separate, not a new first-thread gate. No ACTIVE mutation in this ruling.


## 2026-09-23 Holdings deployed shallow-layout crash
CTO independently reproduced bcb3 IndexError at /var/task and passed exact source 3e913e9ce9 in the same Lambda Python 3.12 image. P packages and returns exact one-function plan; M prepares supported COT coverage without replacing the user account. See DIRECT_REVIEW_2020_20260923/HOLDINGS_SHALLOW_RUNTIME_REVIEW.md. Actual user journey remains FAIL.


## 2026-09-23 Holdings exact schema package apply
P GO for saved plan30f1d202bf7a50fa063e7d96eee2e6ae5ed7465c23471cf1d670230f780d5f02 only: one Lambda code update to exact97f190ac artifact, no IAM/config/routes changes. CTO downloaded final33memberS3version and passed actual /var/task runtime import/schema load. See HOLDINGS_SCHEMA_REPLACEMENT_REVIEW.md; independent live readback and actual user journey remain required.


## 2026-09-23 COT supported coverage exact GO
M may publish exact93f930c265ed242d7e38cb48a7ed4baf267025e8c4dfd06ff39739c6a8f55217 per a509946936:19conditionalwrites, oneSept22indexCAS, nootherdatesorversionsremoved. CTO independently reconciled all841accounts/13793positions to retainedsource, everyGoldJSONnode and15partitionhashes; actualreader localbothAnna matrixPASS. Source-refused140accounts andactualauthenticatedproofremainOPEN. See COT_EXPANDED_COVERAGE_REVIEW.md.


## 2026-09-23 23:2x UTC - Claude CTO takeover batch (1.0.0_SA_CTO, runtime successor)

Seat continuity: this session is the Claude successor to the Codex CTO session closed at 22:42Z
(log session_close_IRPT_1859-2242Z.md @e124553a33). Contract v1.4, COO_P/M/Y and every ruling above
stand unchanged. CTO reviews directly; no CVO queue. Evidence for every measurement in this batch:
DIRECT_REVIEW_2020_20260923/CLAUDE_TAKEOVER_LIVE_READBACK_20260923.json. Also repaired in this
commit: this file carried six cp1252 bytes (0x97, em dash) in six ruling headings (IRPT-ANALYSIS-UPLOAD-OWNER,
IRPT-DUAL-OWNER-SOURCE, ...-RESOLUTION-IMPLEMENTATION, IRPT-LOOKUP-CAPTURE, IRPT-SESSION-DELTA,
IRPT-PUSH-HOLD-RELEASE) and was not valid UTF-8; each replaced with ASCII "--". A first read reported
"one byte" because a decode stops at the first error; the count is from the repair loop.

### IRPT-HOLDINGS-SCHEMA-APPLY-VERIFIED-20260923
P executed GO d8e9d68378 exactly (msg 99786): saved plan 30f1d202 unchanged, 0 add / 1 change / 0
destroy at 23:00:52Z. CTO independent readback on a different instrument: the deployed zip
downloaded from the function's own Code.Location hashes to 97f190ac...c35, the approved artifact;
CodeSha256 recomputed from that download equals the live configuration value l/GQrFcE...DDU=;
33 members; snapshot.py carries no fixed-depth parents[4] index; layer irpt-common:5; python3.12.
Ledger closed on P's publish branch @5c8d6f8e34 (LOCAL). Deployment hop PASS. NOT a journey PASS:
no signed-in Holdings response has been exercised against these bytes.

### IRPT-COT-COVERAGE-PUBLICATION-VERIFIED-20260923
M executed GO d940022b06 exactly (msg 99780). CTO independent readback: current index version
grwnbLkeu_OeYL6AcOR33ec9mO51dTBJ (23:00:30Z, ETag 9731cecad3b5..., sha256 5d56285bb8f5...) names
revision 93f930c265...217 for 2026-09-22; prior index version JhtDD... retained; 18 objects under
the revision (gold parquet, header, manifest, 15 parts); header.json 841 accounts / 13,793
positions / USD 548,412,662.59, reconciled to tolerance 0.01, both Anna account ids present.
Publication hop PASS. Open, unchanged: 140 source-refused accounts; the deployed reader matrix
against the repaired Lambda; the authenticated screen.

### IRPT-HOLDINGS-NEXT-PROOF-20260923
Both prerequisites named in IRPT-HOLDINGS-ACTUAL-FAIL are now live. The next proof is Andrew's real
signed-in Cottonwood/Anna selection (0698, d486, combined) on localhost:5174 rendering Holdings, then
reload. M owns the deployed reader matrix (0698 / d486 / combined at default and 2026-09-22 READ_OK,
2026-09-23 refused) against the live Lambda BEFORE asking for the screen, and the journey. P still
owes the defined-code contract for the NOT_READY reason ("code not defined by the v1 contract" is a
render of an undefined code, a separate defect from the crash). No seat synthesizes auth to exercise
the deployed reader: the reader matrix runs through the publisher/reader library against the live
publication, and the HTTP hop is the user's.

### IRPT-ANALYSIS-CURRENT-AUTHORITY-20260923 (adjudicates CRO 99773 / 223752)
CTO read the cited source directly, not the summary: auth-handler/src/auth.ts refresh() :483-555
(getUser by email; new-shape binding or old-shape createdAt-vs-iat guard; status != 'active'
refused; partner re-read; mint), jwt.ts generateAccessToken :162-193 (tier 'internal' iff
firmId == 'opal-capital'; userType from PROFILE), refreshBinding :220 (sha256(PK|createdAt)[:32]),
portal-authorizer/index.mjs computeAllowedFirms :269-297 (userType 'Dev' -> ALL; tier 'internal'
-> ALL; else own firmId plus descendants when role == 'admin', via Scan :223-251; no per-request row
read), and investor-reporting/_scope/canonical_profile_reads.py :19 (_USER_FIELDS lacks createdAt,
role, userType) and :84 (returns fields[2:]). The CRO's account of the source is ACCURATE.

RULING. The CRO recommendation is ACCEPTED with four bounds:
1. Maintained source is the opal-users-v2 PROFILE row read through CanonicalProfileReaders.get_user
   (email-index then consistent GetItem, unchanged). _USER_FIELDS additionally projects and returns
   createdAt, role and userType; read created_at as the fallback name exactly as refresh() does.
2. The worker replays refresh()'s decision server-side at job start and again at final release and
   at any durable dispatch: REFUSE when the user is None, status != 'active', or user.firmId !=
   record.owner.home_firm_id. Locator with no persisted PK: REFUSE when createdAt (or created_at)
   parses and is later than the record's accepted time. A missing or unparseable createdAt does NOT
   refuse on that rule (refresh() :527-529 guards on Number.isFinite the same way) but is recorded
   as createdAt_absent in the decision evidence. ENRICHMENT, not required for the first thread:
   persist the refreshBinding-equivalent sha256(PK|createdAt)[:32] at acceptance so later checks
   compare bindings rather than clocks; owner Y (semantic) with P (shared), un-parks after the
   first live 12.03 journey.
3. Class: OPAL_GLOBAL iff user.firmId == 'opal-capital' OR user.userType == 'Dev' (the authorizer's
   ALL). Otherwise the worker's scope is the user's own firmId only. Admin-descendant scope (the
   Scan) is NOT implemented in the worker now: a non-Opal user's job whose data firm is not the
   user's firmId REFUSES with a defined code, never silently narrows or widens. This is narrower
   than the interactive authorizer only for a firm admin with descendant firms, which is no current
   journey; parked with owner P, un-park condition = a firm-admin cross-firm journey enters scope.
   Advisor/partner fields are not authority inputs; no opal-partner-* read is added.
4. IAM: the executing roles (irpt-ycharts-generate-role, and irpt-ycharts-runner-role as the host's
   instance profile) receive dynamodb:Query on arn:aws:dynamodb:us-east-1:313476888478:table/
   opal-users-v2/index/email-index and dynamodb:GetItem on .../table/opal-users-v2. No Scan, no
   partner tables, no wildcard. P writes the Terraform; CTO reviews the plan before safe-apply.
Never synthesize HTTP claims, trusted headers or OPAL_GLOBAL from retained queue/owner fields:
owner.principal_id and home_firm_id are locators for the lookup, never grants. Revocation latency
is the check interval, no worse than the interactive 15 minutes.
OWNERS: P implements bound 1 (canonical_profile_reads.py is _scope, a shared surface) and bound 4;
Y consumes bounds 2-3 in the resident worker at job start and release and supplies the exact
decision evidence shape. Fast affected checks only: the existing canonical-profile cases plus one
positive (Opal userType Dev), one inactive-status refusal, one firm-mismatch refusal, one
createdAt-after-acceptance refusal and one createdAt-absent pass-with-evidence. No broad suite.
The CRO research is CLOSED as delivered; no further generic authority research.

### IRPT-YCHARTS-HOST-AUTOSHUTDOWN-20260923
Measured, answering CRO 99773's off-scope observation and the contract's "stays running" line:
CloudTrail StartInstances by Andrew_Berman 18:21:11Z; StopInstances by ec2-auto-shutdown-enforcer
21:21:18Z; describe-instances now stopped, "User initiated (2026-09-23 21:21:18 GMT)". The enforcer
(IDLE_CEILING_HOURS 3.0, IDLE_CPU_THRESHOLD 1.0) reaps any running instance idle for 3h; its ONLY
exemption is the instance tag AutoShutdown=disabled (lambda_function.py :18-21, :113-115), and the
host carries no such tag. So the host will be stopped 3h after every start until a consumer runs on
it or the tag exists. No seat stopped it.
DIRECTION: P (shared IaC writer) adds tag AutoShutdown = "disabled" to the irpt-ycharts-runner
instance resource in Terraform, with a comment citing Andrew 6fc3f5f785 (dedicated always-on host)
and this ruling; plan to CTO, then safe-apply. Nobody starts the instance before the tag is applied
and P's resident install is ready to run; a start now is reaped again at +3h. SURFACED TO ANDREW,
not adjudicated: the enforcer's own docstring records his earlier directive that there be ZERO such
tags; his 2026-09-23 ~20:0xZ approval of a dedicated always-on host is read here as the conscious
opt-out for this ONE instance, and he can veto before the tag is applied.

### LD-0609 naming-gate HCL lookup context - ACCEPTED (review_required_by 1.0.0_SA_CTO)
CTO re-ran the arms on its own scratch diffs at HEAD and against the pre-change gate copied from
ddfc91b11f~1: new gate permits lookup(local.X, "cottonwood") and local.X["cottonwood"] where X is
fed from logic/registry/*.json, refuses the same key over a hand-typed map, a non-registry file and
a var; old gate refuses both positives (control) and P's real retained.tf (REFUSE line 37) that the
new gate grades PASS 4. The change mirrors the Python BUILDERS lookup() permission and admits no
new class. P merges CLOUD into its backend branch (never rebase) before committing retained.tf.

### Runtime transition, recorded
M and Y stopped their own dead Codex helpers and drivers before registering as Claude seats (99780,
99790). P's Codex-era driver (PID 3520, 600 s) is MSTR's to retire (99776 item 1). This CTO session
inherits no Codex helper; MSTR owns the runtime transition and every shared push. All three lanes
carry Andrew-directed /goal + /loop 20m (P f7aaa01da1, M 6890584d29, Y fc17929b64), all LOCAL.


## 2026-09-23 23:5x UTC - Claude CTO batch 2: Performance install GO, source reviews, host two-writer correction, Y grant extension

Evidence: DIRECT_REVIEW_2020_20260923/PERFORMANCE_INSTALL_CTO_REVIEW_20260923.json (this commit).

### IRPT-PERFORMANCE-INSTALL-GO-20260923
GO to 2.0.0_SA_COO~P (99804) for the exact saved plan .runtime/performance-install/install.tfplan,
SHA256 f0a189191e4f566f8cd76673ee8fb83f707f78c07e6f75dd7bad1a7d2b247a55, Terraform 1.9.8, 3 create /
1 update / 1 read / 0 destroy, and nothing else. CTO measured on its own instruments: package
s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip version
h.hlJhL3dKXAFT5NsNzceZX6Jls_f39V downloaded and hashed (358117 bytes, 61 members, sha256 b64
JwJEEQGTENJJukTvrNQt3dq6VIAI8xqioIYA1atL+hk=); native layer version tf.fKYdfNRbn9AGt1AEHqn35f6bwGqPb
sha256 121b8407415ce803458f52de03d11d81d26791f94d20f4130658a773cd1f39f6 (the 2fb5422b04 layer);
irpt-common:5 CodeSha ZUcsQUOsc3lT2cKlnur5rCAZc/a0rCkKvU5pjg11U20=. The plan decoded: retained
policy = ListBucket(prefix)+GetObject/GetObjectVersion on the COT mapping partitions only; Get/
GetVersion/Put on opal-data-irpt irpt/cottonwood/state/performance_source_evidence/* and
platinum/performance_reports/* only; irpt-requests Get/Put/Update under LeadingKeys cottonwood; KMS
7f4d3042 via dynamodb (tableName irpt-requests) and via s3 (those two prefixes) only. Selection-read
policy = irpt-requests GetItem under LeadingKeys 49financial/inflection/cottonwood + KMS Decrypt via
dynamodb. Function update: handler runtime.lambda_handler, timeout 120, memory 1536, layers
irpt-common:5 + the new native layer, env 6 keys, IRPT_PERF_TRANSPORT_MODE removed, no approved-plan
env and no secretsmanager grant, so no vendor egress is reachable after this apply.
COLD START PROVEN at the real layout: package + both layers invoked through the Lambda runtime
emulator in public.ecr.aws/lambda/python:3.12 (image 5f188ce6104a), network disabled: INIT success,
invoke 200 returning the guarded CONTRACT_VERSION refusal for an empty event (8.3 s first invoke,
pandas/pyarrow import); control: the deployed v4 package (version 028gVFz77L5vMQGJSIkt0JqSZCk5V4rB,
CodeSha jVktMAiRK+2mYPXEzyst6HjSFFv4xR3Kxm47hAyulyw=) behaves identically. RETRACTED on the way: a
first CTO harness (plain python, /var/task only on sys.path) reported ids.projection_for_firm missing;
that was the harness's path order, not the package, and the emulator run is the instrument of record.
CONDITIONS: P re-reads the S3 version and hash immediately before and after apply (deferred module
data read); ledger opens at apply start and closes on readback (CodeSha == JwJEEQGT..., handler,
two layers, env keys); post-plan -detailed-exitcode 0; exact-function recorder commit; STATUS
overwritten. X10 stays PENDING_ENFORCEMENT (next ruling); until ACTIVE the deployed function refuses
every write and reopen with "registered enforced policy required", which is the truthful state. A
live provider calculation still needs Andrew's per-use word and its own approved-plan change.

### IRPT-PERFORMANCE-SOURCE-REVIEW-20260923 (f04d1e71bd + 068e9ccd85): PASS, bounded
24 affected tests pass in P's own worktree in 1.08 s (the earlier reviewer-export collection failure
was environmental). authorization.py: env-installed approved plan and digest env; scope, expiry,
mapping-revision and request-hash equality before any claim; conditional PutItem claim with no TTL
and no read-retry; the use is consumed even when transport construction fails; the bound transport
refuses any request outside the approved set. runtime.py: lazy assembly, SDK retries 1. retained.py:
reopen-before-compute by immutable pointer; a corrupt pointer or an expired report never falls back
to a vendor call.
FINDING P-REOPEN-01 (design, bounded, NOT a block on the install): the reopen pointer key digests
{owner, request} where owner carries principal_id, account_set_id and directory_revision and request
carries the selection record. The same firm, account set and window reopened after a directory
republish (new sel_ reference, new directory_revision) or by another currently authorized viewer
never hits the pointer, falls through to compute, and the unarmed factory refuses. INVARIANT RULED:
a same-firm, same-sorted-account-set, same-window reopen by any currently authorized viewer finds
the accepted report regardless of directory revision, selection reference or principal;
authorization is re-derived at reopen through the repository (as it already is), never from the
pointer; the pointer's owner and selection remain provenance. P proposes the key shape (for example
digest({firm_id, sorted account_ids, start, end})) and lands it before the reopen/export journey is
graded, not before the install. ADVISORY: only the claim PutItem needs no retry; the S3 client may
keep standard retries so a transient read error on reopen does not surface as a refusal.

### IRPT-X10-SEQUENCING-20260923
Installation is not enforcement. RetentionPolicy._policy (reports/retention.py) requires state ==
ACTIVE, the X10 register commit and a 40-hex enforcement_ref before any reserve, promote or reopen,
so the installed function is inert and truthful while PENDING. ACTIVE flips when the CTO accepts, in
one review: (a) deployed bytes == reviewed bytes (this install's readback); (b) the role policies
applied (this install); (c) the destination verified live (3d9f45175d); (d) P's enforcement matrix
(36 destinations x deployed writer coverage, precise, with the COT two families marked LIVE and the
rest DECLARED); (e) the focused retention arms at the pinned bytes. The EXERCISED arm is the first
live run's reserve -> promote -> reopen receipts, returned before any second use; if they fail, P
reverts the registry row to PENDING and the report is quarantined, never served. M writes the
registry row with enforcement_ref = the accepting CTO commit. Physical disposal stays OPEN and is
not a first-thread gate.

### IRPT-YCHARTS-HOST-TWO-WRITERS-20260923 (CORRECTION of IRPT-YCHARTS-HOST-AUTOSHUTDOWN)
The earlier ruling named ONE writer of a two-writer property. 2.0.0_SA_COO~Y (99801) measured the
second: infra/aws/terraform/investor-reporting/ycharts/instance.tf declares
aws_ec2_instance_state.runner { state = "stopped" } (:131-135, header :9-25), so a tag alone would
leave a plan that reports a running host as drift and converges it to stopped. Both writers move.
GO to 2.0.0_SA_COO~P for the exact saved plan .runtime/ycharts-authority/authority.tfplan, SHA256
1de760399ca1cd7f42e4b570c705f8e464500a1ba31a3da64a6a329d4c35006d, 0 add / 3 change / 0 destroy,
decoded by the CTO: irpt-ycharts-generate-role and irpt-ycharts-runner-role each gain dynamodb:Query
on table/opal-users-v2/index/email-index, dynamodb:GetItem on table/opal-users-v2 and kms:Decrypt on
key 64f25291 conditioned on ViaService dynamodb + EncryptionContext tableName opal-users-v2 (the
users table's own SSE key, read from the table, never typed: ACCEPTED as the necessary companion to
bound 4); aws_instance.runner tags gain AutoShutdown = "disabled" only; aws_ec2_instance_state.runner
stays stopped in this plan. WRITER B flips to "running" in the SAME plan as the resident install
cutover, not before, and the host is started once after that apply. The tag is inert until a start;
Andrew's veto on it stands until then.

### LD-0610 naming-gate packaged-name citation - ACCEPTED (review_required_by 1.0.0_SA_CTO)
CTO arms at HEAD ae754f525f against the pre-change gate copied from ae754f525f~1: positive = P's
committed lambda-source-map.json change (17e94dbdc6) graded from a detached scratch worktree at its
own base 560445f857: old gate REFUSE (lines 3004/3008/3009/... bd_live.py, bd_selected.py,
_vendor/bd49f_reporting_pull.py), new gate PASS 0 graded; negative = a row whose repo_path is
untracked: both gates REFUSE. A first CTO positive arm run against P's current HEAD was INVALID (the
diff no longer applied, so the post-image did not parse and the citation set was empty); the
scratch-worktree arm is the one that counts. P's branch carries ae754f525f (second merge
560445f857) and 17e94dbdc6 committed under the new gate.

### IRPT-Y-CURRENT-AUTHORITY-CONSUMER-20260923 (Y 635af92b76, P 185dfb3e7f)
Y's current_authority.py decide() is ACCEPTED, bounded: it mirrors refresh() and the ruled bounds
2-3 (ACTOR_NOT_FOUND / ACTOR_LOCATOR_MISMATCH / ACTOR_INACTIVE / ACTOR_FIRM_MISMATCH /
ACTOR_CREATED_AFTER_ACCEPTANCE / ACTOR_SCOPE_REFUSED; createdAt_absent recorded; OPAL_GLOBAL iff
opal-capital or Dev; admin descendants parked). Y's reading is CONFIRMED: a same-firm accepted owner
without home_firm_id resolves home == firm_id, the estate's own rule at
_scope/maintained_sources.py:304 (read by the CTO), with the evidence naming home_firm_source. CAVEAT
recorded: for a firm admin whose accepted data firm is a descendant, the fallback makes
ACTOR_FIRM_MISMATCH refuse; that is the parked scope refusing in the safe direction, and if that
journey is ever admitted the entry must persist home_firm_id explicitly. P's 185dfb3e7f (bound 1)
is ACCEPTED: createdAt (created_at fallback), role and userType are returned when present. P
integrates current_authority.py, resident_worker.py and its test at the Y pin below and wires
profile_for = CanonicalProfileReaders(<factory client>).get_user into build_resident_runtime.

### IRPT-Y-INTEGRATION-GRANT-EXTENSION-20260923 (answers Y 99817 and P 99813 item d)
Y's import census (93 reachable files: 78 same, 11 differ, 4 missing at P HEAD) shows six granted
files, resident_session.py among them, cannot import in P's tree because the accepted template-upload
batch lives under intake/ and ops/ outside the 31-path grant. Seven exact rows join
IRPT_Y_ACCESS_INTEGRATION_P in this commit, pinned to Y c4564aad17 in the manifest:
intake/resolution_kimi.py, intake/security_resolution.py, intake/template_reader.py,
intake/tests/test_resolution_kimi.py, intake/tests/test_security_resolution.py,
intake/tests/test_template_reader.py, ycharts/generate/current_authority.py. intake/portfolio.py and
ops/prospect_dates.py ALREADY carry P rows from the 20:47Z grant (measured at .owned-paths.yaml
:1170 and :1191), as do intake/resolution_broker.py, intake/uploads.py and
intake/tests/test_template_uploads.py, so nine paths are pinned in the manifest and seven rows are
new. Seven of the nine are Y-ahead or new and are exact copies. TWO ARE DIVERGED (Y and P commits on both
sides since merge-base 10627906f2): intake/portfolio.py and ops/prospect_dates.py. P produces a
file-level three-way merge for each (git merge-file from the merge-base blob) and Y confirms the
semantic result in ONE exchange before P commits; neither side overwrites the other. Y's
test_canonical_profile_consumption.py now reads _USER_FIELDS (Y's lane). Incumbents retained; no
deploy grant; the temporary P rows come out after the accepted handoff, as before.

### IRPT-HOLDINGS-DEPLOYED-READER-MATRIX-20260923 (M 99810 item 1) - ACCEPTED as the hop-3 library proof
M's receipt COT_DEPLOYED_READER_MATRIX_20260923.json: the reader module hash 2f6e1ba1306c8ed5b282dbcbd18b7f375c1d20b1f0288093c8200fc450bf5c35
equals the snapshot.py bytes inside the deployed irpt-holdings zip (CTO download), loaded against
LIVE S3: 0698 / d486 / combined READ_OK at default and 2026-09-22 (32 / 59 / 91 nodes, USD
26,303,302.17 / 19,705,844.84 / 46,009,147.02, clocks distinct), 2026-09-23 refused x3, excluded
account refused. Limit stands: authorizer, selection and browser hops are not exercised. The next
proof is Andrew's signed-in Anna selection and reload on localhost:5174; nobody synthesizes it.
M's 49F meshed candidate 1d0b700b7d1a and the 7-model snapshot overlay are QUEUED for CTO review;
publication stays refused until Andrew attests 49F currency (M's card at the M terminal), and the
naming RAISE on "smartx/platform/silver/" is PARKED as a registry defect (owner: the
infra/logic/registry lane holder, identified by the CTO next tick; no workaround).

### NOT_READY reason-code vocabulary (P 2cdbe2bd60) - REVIEW PENDING
P's addendum to docs/contracts/investor-reporting/v1/CONTRACT.md (38 added lines, on P's branch) names
the 14 public reason codes in the portal generator's grammar; the CTO reads the ratified text next and,
on acceptance, asks 0.0.0_AB_MSTR to merge that commit into CLOUD so P can regenerate the portal
constant against a clean contract. CONFLICT / SUPERSEDED / UNEXPECTED stay flagged until the portal
rule widens.


## 2026-09-24 00:2x UTC - Claude CTO batch 3: M snapshot-overlay candidates (49F, INF, COT)

### IRPT-HOLDINGS-MESHED-CANDIDATES-20260924 (M 21f696e19a, a700417729, be672a40d8)
CTO read holdings_49f.py (484 lines), holdings_inf.py (382) and holdings_membership.py (158) in full,
the three receipts, and ran the focused arms in M's worktree (test_holdings_49f + test_holdings_inf +
test_holdings_membership: 18 passed in 1.29 s). VERDICT: all three ACCEPTED as SOURCE CANDIDATES,
bounded, unpublished. What is right: custody dollars come only from the custodian (Schwab
net_mv_plus_cash; Orion accounts_v2 current_value; the accepted COT publication); model authority
comes only from the model platform (SmartX open allocations; Eclipse single-account portfolios;
Rebalancer assignment by exact unique roster name); Client is the residual plug and the holdout block
is held (49F 1,607 of 1,607, INF 287 of 287) while the redistributing build fails that check with
zero total drift, which is the right difference control; TARGET model assets sit outside custody
reconciliation; drills that do not tie are WITHHELD with the difference stated; currency refuses
publication without an ANDREW_ATTESTATION record; no vendor call anywhere. The COT overlay is a
projection over the accepted revision with source bytes checked against the receipt hashes, and
single-account custom strategies have their client-derived names withheld.

THREE BOUNDED FINDINGS to land before any of the three is published (M owns; none needs a new GO
to fix):
1. 49F-TAX-CONFLICT-01: holdings_49f.py:280-281 raises for the WHOLE build when one account is both
   SmartX-modeled and Tax-traded. One workbook row would refuse all 7,522 accounts. Carry that account
   in Client with the conflict stated as a fact and count it in refused_accounts; never a whole-build
   refusal for a per-account conflict. (Zero such accounts today, which is why the build ran.)
2. TAXONOMY-PATH-01: MODELS_PATH and TAX_PATH are literals ("Models"; "SMA" > "ALT Strategies" >
   "Tax") while client_path is read from the canonical taxonomy. The contract says consume the MDPF
   taxonomy registry, not a copied enum, and the L0 label the contract and Andrew use is "SMAs". Read
   all three paths from the same registry helper; the label spelling comes from there.
3. INF-CLOCK-01: custody_as_of is the Orion snapshot key (2026-09-23) while 4.0.0_SA_CRO 10f3cf6f9f
   measured 3 of 3 that a daily key holds the PRIOR close. A screen saying "as of 2026-09-23" over
   2026-09-22 values misstates the valuation date. State the valuation date as the prior trading day
   of the snapshot key (lib/trading_calendar.py) with the snapshot key recorded beside it; values do
   not change. The Tax sleeve gets the same treatment: the workbook observed_at (2026-09-23) is the
   overlay clock for that sleeve and is stated on its fact.
Publication of 49F and INF then waits only on Andrew's currency attestations (P writes the two
CurrencyAuthorities.json records on his word) and each gets its own exact-write GO with the same
index-CAS and prior-version-retained shape as d940022b06. The COT tree change M plans (MODEL_LEAF
membership over the accepted custody) is welcome as a candidate: same business date, new revision,
custody totals unchanged, MODEL_LEAF ASSIGNED whole-account at custody value with claim measured,
OBSERVED positions under the leaf, index CAS, prior revision retained, new GO.


## 2026-09-24 00:2x UTC - Claude CTO batch 4: reason-code vocabulary ratified; SmartX prefix RAISE routed

### IRPT-REASON-CODE-VOCABULARY-20260924 (P 2cdbe2bd60) - ACCEPTED as ratified text
CTO read the 38 added lines of docs/contracts/investor-reporting/v1/CONTRACT.md on P's branch: the
fourteen data codes of _authz/errors.py PUBLIC_REASONS named one per row in the portal generator's
grammar ("refused with public_reason_code X" / "returns X"), the two boundary codes unchanged, the
PublicStatusEnvelope pattern unchanged, and the consumer's single-word limit (CONFLICT, SUPERSEDED,
UNEXPECTED stay flagged until the portal widens its rule) disclosed as a portal change under the
same row. NOT_READY is named as a retryable state, which is the truthful render for the Holdings
screen Andrew saw. 0.0.0_AB_MSTR is asked (99837) to bring exactly that docs commit onto local CLOUD
so P's generator, which refuses a dirty contract, can regenerate the portal constant; P then runs
reason-codes.test.ts and owns the single-word widening.

### Performance install VERIFIED LIVE (P 99831) - recorded
CTO readback at 00:1xZ (get-function-configuration, list-role-policies, list-layer-versions):
irpt-performance-adapter CodeSha256 JwJEEQGTENJJukTvrNQt3dq6VIAI8xqioIYA1atL+hk= (== the approved
artifact), LastModified 2026-09-24T00:07:10Z, handler runtime.lambda_handler, 120 s / 1536 MB, layers
irpt-common:5 + irpt-performance-native-layer:1 (created 00:07:00Z), six env keys, State Active;
irpt-performance-retained-policy and irpt-performance-adapter-selection-read-policy present on the
role. Installation hop PASS; X10 PENDING; no journey claimed.

### SmartX prefix naming RAISE - ROUTED, not worked around
M 99810 reported the naming gate grading "smartx/platform/silver/" (holdings_49f.py SMARTX_PREFIX, a
pre-LGIC SmartX silver layout the retained build_49f already read) as RAISE: "'platform' is not a
tier". A RAISE is the gate's own rule/registry defect (its docstring), not a refusal, and the
LEGACY-READ carrier cannot carry it (it authorizes ONE EXISTING literal under a LIVE remediation and
this is a grading defect on a key grammar). Under Rule 30 the SmartX pipeline reaches conformance
through its own migration project, never as a rider. OWNER: the naming-gate mechanism owner
(0.0.0_AB_MSTR, LD-0606/0609/0610 pattern), asked to grade a pre-LGIC key whose tier segment is not
a tier as EXISTING/WARN with the reason printed, or to name the legacy layout in the registry; lands
after the /integrate work unless it starts refusing. Un-park condition: the gate no longer RAISEs on
that literal. M does not type around it.


## 2026-09-24 00:2x UTC - Claude CTO batch 5: the three candidate findings CLOSED (M a0f3f141ed)

### IRPT-HOLDINGS-MESHED-CANDIDATES-20260924, findings CLOSED
CTO read the closing diff and re-ran the arms in M's worktree: the three named arms pass and the four
Holdings test files pass 45 of 45 in 1.83 s.
- 49F-TAX-CONFLICT-01 CLOSED: a SmartX-modeled account that is also a Tax Traded=Yes row is carried
  in Client at full custody value with "MEMBERSHIP CONFLICT" stated, counted in
  census.client_membership_conflict and listed in refused_accounts; the whole-build raise is gone.
- TAXONOMY-PATH-01 CLOSED: holdings_snapshot.taxonomy_path(view_path, member_id) reads the MDPF
  registry's VIEW_TREE and refuses an undeclared node or a member under the wrong node; both builders
  read Models, SMA > ALT Strategies > <registry Tax-Managed SMA display name> and Client through it;
  no literal path remains. LABEL: the registry's own L0 spelling is "SMA", so the candidates carry
  "SMA"; the "SMAs" in the contract text and in this seat's finding was the human spelling, and the
  registry governs by the contract's own rule. If Andrew wants "SMAs" on screen it is a
  NODE_DISPLAY_LABEL row in the registry, never a builder spelling.
- INF-CLOCK-01 CLOSED: custody_as_of and business_date are prev_trading_day(snapshot key) =
  2026-09-22 with custody_snapshot_key 2026-09-23 recorded beside them; the validator still binds
  rows to the key; values unchanged (reconcile 209,358,359.48 both sides). The 49F Tax sleeve states
  the workbook observed_at as its own overlay clock.
REBUILT candidates: 49F a860115ecaf5336ac5db4491d76cf5b60780f8a9c257c579defaf62351ba6a1f and INF
21279569b08d40ce53e163143b2f829f78c7466f6b25c6a024c57e601b4ef441, both business date 2026-09-22, dry,
zero writes. Publication of each now waits only on Andrew's currency attestation (P writes the two
records), then its own exact-write GO in the d940022b06 shape.


## 2026-09-24 00:3x UTC - Claude CTO batch 6: LD-0611 naming-gate RAISE-EXISTING accepted with one finding

### LD-0611 (c49325f3d4) - ACCEPTED, counts-as unchanged, ONE FINDING on the arms
CTO arms at HEAD c49325f3d4 against the pre-change gate copied from c49325f3d4~1, on scratch
new-file diffs: "smartx/platform/silver/" grades RAISE under the old gate and RAISE-EXISTING (reason,
Rule 30 pointer) under the new; WARN 1 graded both. Counts-as is WARN in every branch, so no commit
that passed is blocked and none that was blocked passes; the K3 grammar defect stays printed and
stays LGIC's to close. ACCEPTED.
FINDING LD-0611-ARM-01 (owner 0.0.0_AB_MSTR, bounded, not a block): the NEGATIVE arm is VACUOUS at
HEAD. "smartx/platformx/silver/" graded RAISE-EXISTING under the new gate in the CTO's run, not RAISE
as the ledger records, because the carrier search (git grep -l -F over the whole tracked tree at
HEAD) now finds that literal in ONE file: org/tier0/ledger/LD-0611.md, the ledger naming its own
negative arm. MSTR measured the negative before the ledger carrying it was committed, so its control
was true at measurement and false one commit later. Two consequences: (1) the arm proves nothing
now; (2) the carrier set is the WHOLE tree, so a pre-LGIC key first typed into a ledger, a message
record or a log later grades RAISE-EXISTING in code, which is the prose-carries-the-key shape the
gate's declaration-tree domain (MINUS org/, docs/, run-artifact dirs) already excludes elsewhere.
DIRECTION: scope the carrier search to the gate's own declaration-tree domain and exclude the gate
file and its self-tests; pick a negative literal no file carries and assert it stays RAISE; re-run
the positive. Lands after the /integrate work; nothing is refused meanwhile. No waiver, no registry
row, as before.


## 2026-09-24 00:3x UTC - Claude CTO batch 7: COT membership publication GO (M 26a04257bf)

### IRPT-COT-MEMBERSHIP-PUBLICATION-GO-20260924
GO to 2.0.0_SA_COO~M for exactly the candidate revision
ac3adb97f5e76a5f044d4b0d12ffda3bebccd235915aed661315e98432729d5a (business date 2026-09-22):
18 immutable creates (gold, header, 15 parts, manifest) then ONE index CAS on IfMatch
"9731cecad3b5ff3e7323ff8567260f95" (index version grwnbLkeu_OeYL6AcOR33ec9mO51dTBJ), replacing only
the 2026-09-22 row; prior revision 93f930c265 and the prior index version retained; every returned
version and hash read back before the index; the index read back at its exact version; drift
refuses. No other write, no vendor, no IAM. CTO INDEPENDENT VERIFICATION, its own instrument: the
local candidate body (16,558,818 bytes) hashes to the revision; against the accepted 15 parts fetched
from S3 at revision 93f930c265, the 841 ACCOUNT nodes are identical in id, value and clocks (0
differences), the multiset of 13,793 SECURITY values is identical, the 462 MODEL_LEAF nodes are all
ASSIGNED / claim measured / namespace COT_REBALANCER_MODEL with each leaf equal to its account's
custody value, every SECURITY node is OBSERVED, and both Anna accounts carry a leaf. The live index
ETag re-read at 00:3xZ is still 9731cecad3b5... (no drift since d940022b06). Source: the same seven
retained inputs checked against the native publication receipt; tests 114 of 114 in M's worktree
(membership, snapshot, economic regressions). After the writes: the deployed-reader matrix again
(0698 / d486 / combined at default and 2026-09-22; 2026-09-23 refused) and the receipt to the CTO.
The 379 unassigned accounts remain Client with membership unattributed; the 140 source-refused
accounts remain open. Not a journey PASS; the screen is still Andrew's re-test.


## 2026-09-24 00:3x UTC - Claude CTO batch 8: LD-0612 accepted (LD-0611-ARM-01 closed)

### LD-0612 (1e7121507a) - ACCEPTED; LD-0611-ARM-01 CLOSED
CTO arms at HEAD 67c2844189 (carrying 1e7121507a) against the copy at 1e7121507a~1, on the same
scratch new-file diffs: "smartx/platform/silver/" grades RAISE-EXISTING under both (carried in code
and contracts); "smartx/platformx/silver/" grades RAISE-EXISTING under the pre-change gate (vacuous:
its only carriers are three record-tree files, LD-0611.md, LD-0612.md and this RULINGS.md) and RAISE
under the new gate, which drops record-tree and non-graded-extension carriers from the search.
WARN 1 graded in every arm; counts-as unchanged; the permission only narrows. The negative arm
discriminates again and stays valid however many records quote the literal.


## 2026-09-24 00:4x UTC - Claude CTO batch 9: COT membership publication VERIFIED; the write-count deviation ACCEPTED

### IRPT-COT-MEMBERSHIP-PUBLICATION-VERIFIED-20260924 (M 99860)
M executed the GO at 00:37:03-00:37:11Z. CTO independent readback: the current index is version
XbWnSWxMFRs9jNOUtj6ZOELvpemDQP73 (ETag ab460faa537d..., sha256 983443bbc5b2...), its only date row
2026-09-22 names revision ac3adb97f5e7 with manifest version UCnp0Bq_BRGjdz2RMgfrUCXmNOtAFq4y; three
index versions exist and the prior two (grwnbLkeu, JhtDD) are retained; under ac3adb97 there are 20
objects (gold, header, 17 parts, manifest), under 93f930c265 still 18, under fe328763b5 still 3; 42
keys in the tree. M's reader matrix on the live publication: 0698 / d486 / combined READ_OK at
default and 2026-09-22 with 1 / 1 / 2 MODEL_LEAF nodes and the same USD totals; 2026-09-23 refused.
Publication hop PASS for the membership tree.

THE DEVIATION (20 immutable creates, not the 18 the GO named) is ACCEPTED, no revert. The GO's
blast radius was the set of keys under the new revision's own prefix plus ONE index row, and that is
exactly what was written; the "18" was a count inherited from the prior candidate's 15-part split,
carried by M into its request and by the CTO into the GO without either measuring the new body's
partition plan (the body grew to 16,558,818 bytes and the publisher's deterministic size-bounded
split produced 17 parts). CLAUDE.md's sign-off rule names the ACT'S BLAST RADIUS, never the
producer's decision, and the split is the producer's rule. Both seats own the lesson: an exact-write
GO names the key prefix, the index row and the IfMatch, and the requester prints the publisher's
MEASURED write plan for the named candidate; a count the requester did not measure does not enter
the GO. The 49F and INF requests carry that plan.


## 2026-09-24 00:4x UTC - Claude CTO batch 10: P-REOPEN-01 landed; vocabulary amendment re-accepted; portal regen target; a lane correction

### P-REOPEN-01 CLOSED in source (P 9074dba320) - ACCEPTED, deploys with the next Performance package
The pointer key is digest({firm_id, sorted account_ids, start, end}); the pointer schema
irpt-performance-accepted-v2 carries accepted_key and ref only (no owner, principal or selection);
reopen checks tenant, key, accepted_key and the accepted report's provenance core and still reads
through stores.reports.get with the CURRENT principal, so authorization is re-derived by the
repository and the pointer grants nothing. Three new arms (another authorized viewer after a directory
republish reopens with zero source or vendor reads; the pointer grants nothing to an unauthorized
viewer; a different window misses the pointer). Suite 11 passed. No v1 pointer exists (store empty at
install). It ships in the NEXT package under its own build, plan and GO; the installed function is
unchanged until then.

### IRPT-REASON-CODE-VOCABULARY-20260924, amendment 2a87fa8edf - RE-ACCEPTED
Three rows (CONFLICT, SUPERSEDED, UNEXPECTED) reworded into the "refused with public_reason_code
<CODE>" grammar so the portal's widened reading rule names all 14 data codes; codes and classes
unchanged. 0.0.0_AB_MSTR cherry-picks it onto CLOUD as it did c80b8ccb41. P's portal regeneration
c1ac41ec (branch p-reason-codes-20260924 over c70855f3: 16 named codes, generator and test share the
grammar, 90 code-shaped tokens with 16 admitted and the 74 rejected inspected, bun test and tsc
clean) is ACCEPTED as the render fix for the NOT_READY screen. TARGET: 0.0.0_AB_MSTR merges
c1ac41ec into the local-live portal branch codex/local-live-data-20260923 (the 5174 screen and the
DEV candidate MSTR already named), never a rebase; DEV rides the next portal push on Andrew's word;
PROD is an enrichment item.

### LANE CORRECTION (CTO 99857 was wrong on one file)
ycharts/generate/tests/test_canonical_profile_consumption.py sits under ycharts/** in
IRPT_COMPLETION_Y with no P row; the hook's refusal of P is correct and 99857's "a row you already
hold" was not. Y commits its b35cb286b1 copy and the 7-field stub literal fix for the cross-firm
resident cases on Y's branch; P re-copies both at its next sync. No new P row: the lane stays as
narrow as the integration needs.


## 2026-09-24 00:4x UTC - Claude CTO batch 11: Andrew-direct "all recs approved" (seven open calls) + two Y test rows

### ANDREW-DIRECT 2026-09-24 ~00:4xZ at the 1.0.0_SA_CTO terminal, VERBATIM: "all recs approved"
Record: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_004xZ_ALL_RECS_APPROVED_SEVEN_OPEN_CALLS.md
(the seven cards repeated with their RECs and the ruling each approval creates). Currency record:
IRPT_MVP_COMPLETION_20260922/ANDREW_49F_INF_USD_20260924.md. The rulings, each exactly the card's REC:
1. 49 Financial report amounts are USD (firm-level attestation; same scope and limits as COT).
2. Inflection report amounts are USD (same).
3. ONE live Cottonwood performance calculation, account acc_d486fc9455d6b2aa18e13af1, window
   2026-09-01..2026-09-22, through the installed adapter under a server-installed one-use plan; X10
   ACTIVE first; any other account, window or attempt needs a new word.
4. The AutoShutdown=disabled tag on i-0167fd745ad906a66 stays; the host starts only with the
   resident cutover plan.
5. ONE live Orion Reporting/Scope calculation for a real Inflection client, bound at execution to the
   exact client, window and request P presents.
6. 49F SmartX: ONE bounded live account-level call under yaliu-bundle, bound at execution to the
   exact account, window and request P presents; period-to-date labelled, selected-set limit disclosed.
7. 0.0.0_AB_MSTR pushes workspace CLOUD to origin.
ROUTING: P writes the two ANDREW_ATTESTATION records (49financial, inflection) into
CurrencyAuthorities.json citing ANDREW_49F_INF_USD_20260924.md and prepares the CALL-3 one-use plan
for CTO review; M then requests the 49F and INF exact-write GOs with the measured write plan; MSTR
pushes; CRO informed on 6. Nothing wider is inferred from the word.

### IRPT-Y-INTEGRATION-GRANT-EXTENSION-20260923, two more rows (Y 99870)
ycharts/generate/tests/test_canonical_profile_consumption.py and
ycharts/generate/tests/test_custody_retained.py join IRPT_Y_ACCESS_INTEGRATION_P as exact rows at Y
pin 79c53e1abe (manifest extension 2): both are test files whose semantic writer stays Y; P copies
them at that pin so the eight cross-firm resident cases and the consumption test match the 11-field
reader. Y's reading was right and the CTO's 99868 "no new P row" is superseded by this narrower fact:
P cannot sync a file it holds no row for, and a branch merge would carry more than the grant.


## 2026-09-24 01:3x UTC - Claude CTO batch 12: Anna NOT_READY root cause is the firm-bucket fence, not the reader

### IRPT-HOLDINGS-NOT-READY-ROOT-CAUSE-20260924 (Andrew's 00:5xZ retest via MSTR 99893; M 99900/99904, P 99901/99908)
FINDING (measured, discriminated): opal-data-cottonwood's bucket policy statement
DenyForeignFirmPrincipals denies s3:* to every principal whose ARN is not like role/*-cot-* or one of
the three exempted users (Andrew_Berman, Andrew_Berman_Console, Opal_Terminal). The deployed Holdings
function runs as arn:aws:iam::313476888478:role/irpt-holdings-role, matches neither, and its first read
(begin() on platinum/holdings/current/manifest.json) is refused; publication.py wraps that into
PublicationRefused, snapshot.py into SnapshotUnavailable, entry.py maps it to NOT_READY, served.py
refuses at :938 with the directory business date. That is the exact screen Andrew saw
(Unavailable / No source age yet / NOT_READY).
DISCRIMINATOR: aws iam simulate-principal-policy for irpt-holdings-role WITH --resource-policy = the
live bucket policy -> s3:GetObject and s3:GetObjectVersion on the current index: explicitDeny,
MatchedStatements ResourcePolicy. The same simulation WITHOUT the bucket policy -> allowed (positive
control). Every offline replay (CTO RIE replay: success body, 93 nodes; M's deployed-bytes run
outside the repo: READ_OK x3) ran under the CTO's or M's user credentials, which ARE the exempted
users, so they could not see it. M's item 2 (comp-iam / identity-only simulate: ALLOWED) read the
role's identity policy; the deny lives in the resource policy, which that instrument does not read.
Rule 22: a check scoped to the members cannot see a defect in what the members share; the bucket
fence is the shared dependency. Record with every eliminated cause:
DIRECT_REVIEW_2020_20260923/HOLDINGS_NOT_READY_ROOT_CAUSE_20260924.json.
CONSEQUENCE: the same Deny (wildcard role/*-<firm>-* plus named exemptions) fences
opal-data-49financial and opal-data-inflection, so M's 49F and INF publications would be unreadable
by the function the same way the moment they land. The 49financial fence already names 14 non-firm
roles by exact ARN (registry precedent, LGIC_ENFORCE EN-w-7-r3): a shared reader is admitted by
NAME, never by wildcard.
RULING: within the ratified product (Opal has all functions for any firm; the reader is a registered,
firm-bound, prefix-scoped consumer, contract S7). Surfaced to Andrew as a cross-firm-guard enumeration
edit; the CTO proceeds unless he vetoes. NOT the remedy: renaming the role to match *-cot-* (widens
by pattern), a console edit, moving the publication out of the firm bucket, or any change to the
reader's identity policy (M/P 99904/99908 were right that no IAM change is indicated BY THEIR
finding; the change indicated here is to the bucket's resource policy).
REMEDY, one shape, three buckets, registry-driven (Rule 30: never a hand-typed policy):
1. 4.0.0_SA_CRO (infra/logic/** lane; precedent 845343f925, the six operator rows) adds ONE row per
   firm bucket to infra/logic/registry/exemptions.json under opal-data-cottonwood,
   opal-data-49financial and opal-data-inflection: principal irpt-holdings-role, arn
   arn:aws:iam::313476888478:role/irpt-holdings-role, reason citing this ruling and the discriminator
   above, signoff_ref = the ledger entry P opens for the apply. Validator/generator run; commit LOCAL.
2. 2.0.0_SA_COO~P (IRPT IaC writer; IB-rth-8 precedent on this root) plans
   infra/aws/terraform/shared-infra from that commit: EXPECTED 0 add / 3 change / 0 destroy, the three
   aws_s3_bucket_policy resources only (lgic_firm[cottonwood], lgic_firm[inflection], the 49financial
   policy), each diff adding exactly the one ARN to ArnNotLike and removing nothing. Ledger opened and
   committed before the act; the plan and its decoded diff to the CTO.
3. CTO reviews the decoded plan and signs the CTO never-widen half; the second half is
   4.0.0_SA_CRO's (as IB-rtj-2) or a live COO not holding the act (2.0.0_SA_COO~M) in its stead.
4. P safe-applies; post-apply get-bucket-policy x3 read back; re-plan 0/0/0; ledger closed.
5. CTO re-runs the resource-policy simulation for irpt-holdings-role on all three buckets expecting
   allowed on GetObject (current index) and GetObjectVersion (date=* parts); then Andrew retests Anna
   at localhost:5174. The sink repackage (below) makes the reason readable if anything else remains.
ORDER: the registry edit and the sink repackage run now in parallel; the plan waits on the registry
commit; nothing waits on the sink.

### IRPT-HOLDINGS-SINK-REPACKAGE-GO-20260924 (P 99901/99908)
GO for the CODE-ONLY irpt-holdings repackage carrying served.py at 3ac9cbdc98 (five error sites print
the irpt_internal record and the public line; 80 boundary tests, ruff clean; behaviour unchanged).
Bounds: same layer set (irpt-common:5), same handler, same env, same role; package sha to the CTO
before and after; ledger opened before the act; readback of CodeSha against the built artifact. Not a
fix for NOT_READY; it is the instrument that would have shown the fence refusal in the log.

### IRPT-RESIDENT-CUTOVER-PLAN-RECEIVED-20260924 (P 99911)
Plan 04c77cbe (1 add / 1 change: runner-resident policy + aws_ec2_instance_state stopped -> running)
is in the CTO review queue behind the fence remedy; the X10 ACTIVE review (P 6d3a9215d7) follows it.
Sequencing question answered now so P is not idle: ONE apply (grants + start) is accepted in
principle; the GO itself follows the decoded-plan review.


## 2026-09-24 01:4x UTC - Claude CTO batch 13: fence rows landed, 49F + INF publication GOs, ORIGINAL_HOLDINGS accepted, one Y test row

### FENCE REMEDY STEP 1 DONE (CRO 99926): exemptions.json @8b4c15c6ba on local CLOUD
irpt-holdings-role admitted by exact ARN on opal-data-49financial (17 rows), opal-data-inflection (4)
and opal-data-cottonwood (4); 18 lines added, 0 removed; validator OK at registry@b16e50739ce0ae05.
CTO read the file in the shared tree and accepted. Step 2 (P: shared-infra plan from a tree containing
8b4c15c6ba, expected 0 add / 3 change / 0 destroy, ledger before the act, decoded diff to CTO + CRO) is
in flight (99931). Halves: CTO + 4.0.0_SA_CRO (free, 99926); 2.0.0_SA_COO~M only in the CRO's stead.
CRO's found-not-fixed: modules/opal_name/generated_locals.tf lags scopes.json (stale header mark);
the registry owner's item, untouched here.

### IRPT-49F-HOLDINGS-PUBLICATION-GO-20260924 and IRPT-INF-HOLDINGS-PUBLICATION-GO-20260924 (M 99900)
CTO verification on the prepared bytes in C:/Users/AndrewBerman/Desktop/ajb_irpt_m/.runtime/
holdings-journey-20260923 (own instruments, 01:3x-01:4xZ):
- 49F 7c0e7ce3: platinum 160,561,988 bytes, sha256 == revision; gold sha256 2abf2f8e == summary;
  7,522 accounts / 151,697 nodes; clocks custody 2026-09-22 / overlay 2026-09-23 / business 2026-09-22;
  currency ATTESTED -> ANDREW_49F_INF_USD_20260924.md @69e36619ae; publication._platinum_plan over the
  bytes -> header 284,874 B + 156 parts (max 1,048,515 B) => 159 creates + 1 index = 160 writes.
  Receipts 8 (schwab/08335338 x2 date=2026-09-22, smartx/platform x4 date=2026-09-23, opal-data-bd
  directory 2026-09-17 + latest), each version_id + sha256.
- INF 1ebc7696: platinum 31,180,092 bytes, sha256 == revision; gold 2623f60f == summary; 876 accounts /
  33,328 nodes; same clocks; ATTESTED; _platinum_plan -> header 36,857 B + 31 parts => 34 + 1 = 35.
  Receipts 8 (opal-data-inf accounts_v2 + positions_mv 2026-09-23, eclipse 2026-09-23 x4, directory x2).
- Targets EMPTY (user/Andrew_Berman, 01:3xZ): index head-object 404 on both buckets; 0 keys under
  irpt/49financial/ and irpt/inflection/; positive control cottonwood index 200 (522 B).
- Cross-firm: 49F reads opal-data-assets + opal-data-bd only; INF reads opal-data-inf only.
- Finding (not blocking): each prepared directory also holds the superseded revision (49F 99481820,
  INF 0751e62d); the publish call names the GO'd bytes explicitly and the receipt states path + sha256.
GO A: exactly 160 writes (159 immutable creates under
opal-data-49financial/irpt/49financial/{gold,platinum}/holdings/date=2026-09-22/7c0e7ce3..., then ONE
index create IfNoneMatch *). GO B: exactly 35 writes under opal-data-inflection/irpt/inflection/...,
same shape. Publisher = HoldingsPublication.publish(body, gold, expected=begin(), validate=...,
source_objects=<8 receipts>) as d940022b06; a refusal stops before the index. AFTER EACH: versions +
hashes read back before the index, the index at its exact version, reader matrix stated as
LIBRARY-UNDER-USER plus the one arm naming the role's expected explicitDeny (simulate WITH the bucket
policy) until the fence rows apply. No claim that the function reads either publication before then.

### IRPT-ORIGINAL-HOLDINGS-FAMILY-ACCEPTED-20260924 (M 99924, Y 99916/99929)
Registry row ORIGINAL_HOLDINGS {tier state, table original_holdings, extension csv, unreferenced 30,
ceiling 2555} appended to irpt-private-reporting @58ee5b36dd (M worktree, LOCAL; two files: the row and
M's own family census test 587e782bc6 -> 11 state families). ACCEPTED as committed. The two departures
from the CTO's text are the validator's, printed at HEAD: distinct tables (:1712-1713) so not
prospect_inputs; one extension from {csv,json,pdf} (:1715) so not csv|xlsx. Y measured the retained key
suffix as cosmetic to the template readback (parse keyed by the retained file_type), so widening the
admitted set to xlsx is an ENRICHMENT item after the first trace, not a gate. policy_sha256 of
irpt-x10-v1 moves cb9c4e6e... -> 7a7ed8f6...; P re-pins the X10 matrix on this acceptance (39
destinations); the route-plane grant for the upload function is derived from the registry
(irpt/<firm>/state/original_holdings/*), never typed. Y's hop-1 dependency row closes to "grant
pending at P".

### IRPT-Y-INTEGRATION-GRANT-EXTENSION-20260923, one more row (Y 99923)
ops/tests/test_prospect_dates.py joins IRPT_Y_ACCESS_INTEGRATION_P as an exact row at Y pin 7fec957269
(manifest extension 3), for the same reason as the two ycharts test rows: P's tree runs the affected
three-arm case; semantic writer stays Y; packages exclude tests. P re-copies ops/prospect_dates.py
(existing row) at the same pin.

### Cutover plan 04c77cbe (P 99911, Y 99916): queued behind the fence apply; ONE apply accepted in
principle; Y reviewed the family sets as correct for the resident path. GO follows the decoded-plan read.


## 2026-09-24 01:5x UTC - Claude CTO batch 14: fence plan half signed, baseline captured, sink and cutover applied

### FENCE REMEDY STEP 2-3: plan 1fef40d3 read and the CTO half SIGNED (P 99951; CTO 99959/99960)
Tree C:/Users/AndrewBerman/Desktop/irpt-p-fence-20260924 at CLOUD 1b4b2e61e1 (contains 8b4c15c6ba);
ledger irpt-holdings-fence-20260924 sentinel 49fbc21c0c committed BEFORE the plan act; saved plan
.runtime/holdings-fence/fence.tfplan sha256 1fef40d3e5eb37cc3e49e84819ad67999db8f428fb4bb0fbe4a4dd21379f70cd.
CTO's OWN decode (pinned terraform 1.9.8 `show -json` on the saved plan, not P's decoded_diff.json):
3 of 242 resource changes non-no-op, all update -- aws_s3_bucket_policy.lgic_firm["cottonwood"],
lgic_firm["inflection"], opal_data_49financial; each: 1 statement before / 1 after, Sid
DenyForeignFirmPrincipals, Effect Deny, Action s3:*, ArnNotLike aws:PrincipalArn 4->5 / 4->5 / 17->18,
ADDED exactly arn:aws:iam::313476888478:role/irpt-holdings-role, REMOVED nothing, every other
statement key and Condition key equal. Blast radius: three policies stop denying ONE exact principal;
no Allow added; the role's identity policy stays the only grant; ONE writer of the property (this root
from exemptions.json). Rollback: revert the three registry rows, re-apply (0/3/0 back). CTO half SIGNED
by message 99959 at plan 1fef40d3 / tree 1b4b2e61e1 / sentinel 49fbc21c0c; the second half is
4.0.0_SA_CRO's in its own message; P applies the SAVED plan only after both.
CRO half SIGNED (99962, ~02:0xZ) on its own show -json parse (239 no-op / 3 update, same single ADD,
0 drift), a writer census (2 declared resources in one root: s3-49financial.tf:103 and
s3-lgic-firm-buckets.tf:142; no script writer of put-bucket-policy), and a different-instrument reach
read (comp-iam simulate on the APPLIED identity plane: the holdings index GetObject ALLOWED, three
foreign prefixes DENIED control-proven; PutObject / ListBucket implicitDeny UNPROVEN, no grant exists
to control against). Both halves in; P may apply the saved plan.
BASELINE for the discriminating pair (CTO, 01:5xZ, user/Andrew_Berman credentials, one resource ARN
per call): for each of the three buckets, s3:GetObject on the current index and s3:GetObjectVersion on
a date=2026-09-22 part, simulate-principal-policy for the role WITH the live bucket policy ->
explicitDeny (Resource Policy) 6 of 6; identity-only -> allowed 6 of 6; each live policy names the
role 0 times. After the apply the same script must read allowed 6 of 6 and "names the role" 1 per
bucket; anything else is a STOP before Andrew is told to retest.
APPLIED (P 99963): safe-apply of the saved plan 02:04:06Z, 0/3/0; readback get-bucket-policy x3 live ==
planned (5 / 5 / 18 entries, the role PRESENT, nothing removed); re-plan "No changes"; ledger
irpt-holdings-fence-20260924 CLOSED @7220e4a4f3 (fence branch); receipt HOLDINGS_FENCE_APPLY_20260924.json.
CTO AFTER (02:0xZ, same script): each live policy names the role once; WITH the live bucket policy ->
allowed (IAM Policy) 6 of 6; identity-only -> allowed 6 of 6. DESIRED = APPLIED. EXERCISED is Andrew's
signed-in retest (MSTR 99966 asked for it); the CTO synthesizes no trusted headers. Expected screen:
the 2026-09-22 combined publication (93 nodes, custody USD 46,009,147.02); on a refusal the served
function's irpt_internal line now names the cause.
INSTRUMENT TRAP found while building the baseline: passing TWO --resource-arns values through the
.tools/aws shim collapses EvalResourceName to ${BucketName}/${KeyName} and returns implicitDeny at
rc=0 for BOTH arms; one ARN per call returns the real decision. Recorded in box memory beside the
simulate-principal-policy entry; the script loops one ARN per call.

### IRPT-HOLDINGS-SINK-REPACKAGE AFTER (P 99951 item 2): ACCEPTED
safe-apply of saved plan 06880e79, 0/1/0 at 01:38:06Z; irpt-holdings CodeSha256
xd4mk5fxWRa4Uk9OmYcImm1LEC9FoNIGk6jN7A0vlx0= (== the built artifact), handler / layer irpt-common:5 /
env / timeout 29 / memory 1024 unchanged, State Active, LastUpdateStatus Successful; post-apply plan 0;
ledger irpt-holdings-sink-20260924 CLOSED @10a11bbef3; recorder d24c89a385. Not a READY claim: the
fence still denies the role until the apply above lands; the next refusal prints its irpt_internal line.

### Resident cutover apply (P 99951 item 3): executed 01:53:01Z from saved plan 04c77cbe, 1/1/0,
ledger irpt-resident-cutover-20260924 sentinel 18642607a3; readbacks and the cutover receipt are owed
in their own message before Y's runbook runs from precondition B.


## 2026-09-24 02:2x UTC - Claude CTO batch 15: Anna retest -- the fence fix is EXERCISED; two producer defects ruled

### IRPT-HOLDINGS-SUCCESS-STATUS-20260924 (CRO 99981: Andrew's retest at 02:12Z reads "Uncertain / Business date age: 2d")
EXERCISED: the served function answered Andrew's two signed-in selections with 200 (38,887 and 69,445
bytes; reconcile 26,303,302.17 / 19,705,844.84, matching M's reader matrix). CTO reads: CloudWatch
/aws/lambda/irpt-holdings 02:12:41-02:12:58Z, 4 invocations, 0 irpt_internal lines (the sink prints on
refusals only; its positive arm is not yet exercised); the HAR (Downloads/aaaaaa.har, keys only, read in
place, not copied): 4 holdings entries of 15, top-level keys exactly {contract_version, data, firm_id,
operation, unprojected_grant}, NO status member; data = the HoldingsSnapshot document.
DEFECT: the v1 response schema for holdings-snapshot declares `status` (PublicStatusEnvelope,
status_required false) and says in its own description "PRESENT ON A SUCCESS TOO"; the producer never
emits it (served.py:836-846 carries a status only from a compute's `_status`; holdings/entry.py returns
the bare slice). The portal is correct by FE-s-47 (adapt.ts:169, :246, :300-302): an unstated state is
EXPLICIT_UNKNOWN = UNCERTAIN, never a default READY. RULING: producer fix, P's lane, code-only repackage
under the sink discipline: holdings_snapshot returns {"_data": slice, "_status": PublicStatusEnvelope}
with state READY when every retained account is present and unprojected_grant.count == 0, PARTIAL
otherwise (rule stated in code, citing this ruling); source_dates in the shape the portal's status
reader consumes (P's 2cdbe2bd60 vocabulary); actions []; public_reason_code null on READY; schema-
validated in the boundary tests (READY, PARTIAL, refusal arms). CTO reviews the diff and the rule text
before the build, then GO. Portal unchanged; contract unchanged. Refused alternative: FE defaulting
holdings to READY.
CTO'S OWN MISS: HOLDINGS_NOT_READY_ROOT_CAUSE_20260924.json (01:1xZ) already recorded the portal
rendering a SUCCESS body as UNCERTAIN; the CTO read that only as "not a refusal" and did not flag the
second defect. Rule: a control arm that prints an unexpected value is a finding, not a negative.
ENRICHMENT (parked, not this round): "Business date age: 2d" is calendar age; 2026-09-22 is T-1 for
2026-09-23 ET on the trading calendar. The age label must read lib/trading_calendar.py's frontier or it
reads stale every Monday and holiday. Owner: the IRPT_FNTEND surface.

### IRPT-RESIDENT-SESSION-BUNDLE-CONTRACT-20260924 (P 99984 row IRPT_BCKEND-S119; Y 99993 concurs)
FINDING (static, both sides at b56b99c06f): the JS wrapper's persisted bundle carries none of
schema_version / capture_origin / generation / user_agent / identity.user_id that the Python resident
requires (transport.py:384-388 SESSION_CONTRACT; broker.py:159 NOT_VERSIONED; recipe/validate_identity;
broker.verify enrolled check). EXPOSURE, not incident: the seam never fired (secret versions null; no
runner on the host before this tick). P stopped before D1; correct.
CTO'S OWN PART: GO 99936 bound (a) inherited Y's 99907 sentence that the D1 bundle carries
identity.user_id; no instrument had exercised the wrapper (Rule 24: an inherited universal has no
denominator; ask which instrument produced it).
WORD GIVEN (99997): P changes ycharts_session.js at the CH-AUTHENTICATED success branch to read
window.USER on /dashboard/ in the SAME authenticated context (no second sign-in, no new origin) by the
identity_from_html rule and write Y's key contract (schema_version 1, capture_origin EC2, generation
uuid4 per capture, user_agent = the context's exact UA, identity {user_id int > 0, email}), refusing
explicitly on five checks (USER absent/non-literal, authenticated !== true, userId not int > 0, email
absent, impersonating). JS test: key-set equality with run_session_suite.py:66-83 + one arm per refusal.
Y reviews the diff; no Python moves. Pin re-derived by build_resident_package.py; receipt states both
blobs; wrapper 55ddb8f7 untouched. Then D1 once under the standing host-workflow authorization
(CRO 6fc3f5f785 item 3); enrolled_user_id MEASURED from that bundle; broker.current() versioned and
transport accepting it is the exercised arm; C1; install; --once; runbook. S120 (Playwright under
/root vs ec2-user): host remedy stands for this cutover; the ssm.tf change is P's lane item before the
next host deploy.

### Push state (MSTR 99987): origin/CLOUD f96a0b9dd4; origin carries exactly one workspace branch
(CLOUD); SITEZ deleted (tag archive/SITEZ-20260924). Every CTO commit at or before f96a0b9dd4 is on
origin; batch 14 (c83f5bc036) and this batch ride the next MSTR push.


## 2026-09-24 02:3x UTC - Claude CTO batch 16: Andrew-direct on the ready flag; ruling 99995 amended on the CRO's three corrections

### ANDREW-DIRECT 2026-09-24 ~02:2xZ at the 4.0.0_SA_CRO terminal (CRO 100001), VERBATIM: "fix the ready flag, send the status"
Given after the CRO's HAR diagnosis. Scope: the Holdings success status. Routing under it: 4.0.0_SA_CRO
writes the holdings_snapshot `_status` change in cro-holdings-status-20260924 (cut from P's b56b99c06f)
and sends the CTO the pinned diff + test arms; the CTO reviews and GOes; 2.0.0_SA_COO~P packages and
deploys the GO'd pin code-only under the sink discipline. Nothing wider is inferred from the word.

### IRPT-HOLDINGS-SUCCESS-STATUS-20260924 -- AMENDMENT (CRO 100001; M 100000), the CTO's 99995 text was wrong on three details
VERIFIED by the CTO in the shared tree: PublicStatusEnvelope.schema.json additionalProperties false,
required {operation, state, source_dates, actions, public_reason_code}; public_reason_code string
^[A-Z0-9_]+$ (null fails); source_dates closed over business_date / source_completion_date / as_of (+
prospect keys). portal contracts/public-status.ts:20 closes the key set (internal_correlation_id
rejected), :25 refuses a non-string reason code, :27 refuses custody_as_of / overlay_as_of;
envelope.ts:289-291 turns each into EnvelopeMismatch('status') = the whole response refused, worse than
UNCERTAIN. So: (1) public_reason_code HOLDINGS_READY on READY (PERFORMANCE_READY precedent, P's branch),
OBJECT_NOT_COVERED on PARTIAL; (2) no internal_correlation_id; (3) source_dates = {business_date: slice
clocks.business_date, source_completion_date: the revision's completion_date}; custody/overlay stay in
data.clocks. Unchanged: actions []; the READY/PARTIAL rule (every retained account present AND
unprojected_grant.count == 0); portal untouched; contract untouched.
M's measured trap ACCEPTED: served.py status_envelope() (:209-250) refuses the ruled shape (closed
BOUNDARY_REASONS with no success member; forced actions and source_dates), and no producer has ever
emitted state READY (0 hits); the dict is built directly to the response schema and validated against
it in test_entry_guarded.py (READY, PARTIAL with one selected account dropped, refusal arm), plus one
closed-key arm mirroring requirePublicStatus so the FE-side refusal cannot recur. The census
(unprojected_grant) lives at the boundary (served.py:829-833) while account presence is computable in
the compute: the writer picks the side and states it in the diff; the CTO reviews that choice.
CTO'S THIRD MISS THIS WINDOW, recorded: 99995 named three status members from memory of the internal
StatusEnvelope, not from the PUBLIC schema the portal validates. A ruling that names wire fields cites
the schema line it read, or it names none.
SIDE FINDING routed to P (CRO): performance/entry.py on P's branch puts internal_correlation_id into
its SUCCESS status; by the same closed-key rule a Performance success body would be refused. P verifies
on its branch before the CALL-3 one-use run; if real, it rides the Performance package CALL-3 needs.


## 2026-09-24 02:4x UTC - Claude CTO batch 17: Holdings success-status pin reviewed and GO'd

### IRPT-HOLDINGS-SUCCESS-STATUS-20260924 -- GO on cro-holdings-status-20260924 @01bdf54cfd (CRO 100006; CTO 100008)
Pin: 13012979e1 (holdings/entry.py +54/-1) + 01bdf54cfd (holdings/tests/test_entry_guarded.py +78) on
P's backend head b56b99c06f; lane overrides AUDITED per commit (IRPT_LIVE_SCOPE_P, IRPT_COMPLETION_M)
under Andrew's word + the CTO's routing. LOCAL.
CTO REVIEW, own instruments: diff read (status = a plain dict with the closed key set; READY iff
enforce._unprojected_grant_of(scope).count == 0 else PARTIAL, from the same scope["_census"] served.py:977
reads for the envelope, so status and envelope cannot disagree; the "every retained account present" half
is enforced upstream at snapshot.py:225-226 as a NOT_READY refusal, a stronger guarantee than PARTIAL --
accepted as the side chosen; source_dates {business_date, source_completion_date|null}; actions [];
HOLDINGS_READY / OBJECT_NOT_COVERED (errors.PUBLIC_REASONS:52); no internal_correlation_id; a slice with no
business_date refuses NOT_READY). Tests read: READY arm, PARTIAL arm (one granted id the directory cannot
match), missing-account-still-refused arm; the first two validate the whole response against the v1
response schema with every $id resolved and run the portal's closed-key rule in Python. Own run: 144
passed, no skips. Own discriminator: detached worktree at 01bdf54cfd with entry.py from b56b99c06f -> the
two status arms FAIL (KeyError 'status'), the refusal arm passes; worktree removed.
Note, not blocking: _validate_response uses pytest.importorskip(jsonschema/referencing); on a box without
them the two status arms would report SKIPPED after their closed-key asserts ran. P's package run report
must state "no skips".
Vocabulary: no file carries PERFORMANCE_READY (CRO census of docs/contracts/investor-reporting/v1); the
code lives at performance/entry.py:149 only, so HOLDINGS_READY joins it as a producer-stated code; naming
the data codes in the portal's CONTRACT_NAMED_REASON_CODES stays row IRPT_BCKEND-S52 (READY renders the
table; the code is not printed on the success path).
GO: 2.0.0_SA_COO~P fast-forwards the pin onto irpt-smoke-p-backend-20260923, runs holdings/tests with
the count and "no skips", then the code-only irpt-holdings repackage under the sink discipline (ledger
before the act, saved plan 0/1/0, package sha before/after, safe-apply, CodeSha readback, re-plan 0,
ledger close, AFTER to CTO + CRO with the member census: exactly ONE member differing from xd4mk5fx,
holdings/entry.py). Then Andrew retests; the CRO reads the HAR in place expecting status.state READY,
HOLDINGS_READY, business_date 2026-09-22 and the table rendering.


## 2026-09-24 02:4x UTC - Claude CTO batch 18: session-bundle contract change read; Performance success-status fix accepted

### IRPT-RESIDENT-SESSION-BUNDLE-CONTRACT-20260924 -- P's change @282f7ea427 read by the CTO (P 100011; CTO 100014)
ycharts_session.js +155/-8 on irpt-smoke-p-backend-20260923 (audited lane override on the CTO's word);
new LF blob 34df3e94fc0626757048bfd0ff874083396c196ed92e7c57a18dfc4379bacd91 (was 41ffebbe);
run-ycharts-session.sh unchanged 55ddb8f7. Own read: IDENTITY_PATH /dashboard/; contextGet = the replay
context's requestGet else Playwright ctx.request.get (shares the browser context's cookies): no page
navigation, no second sign-in, no new origin, no credential; readIdentity requires HTTP 200, balanced raw
decode of window.USER, five refusals in order (USER_ABSENT, NOT_AUTHENTICATED, USER_ID_INVALID,
EMAIL_ABSENT, IMPERSONATING), IdentityFailure retried:false; versionedBundle writes exactly the Python
reference keys (schema_version 1, capture_origin EC2, generation randomUUID per capture, fence,
user_agent = the UA newContext was created with, identity {user_id, email}, captured_at, cookies in the
jar shape) plus declared informational keys; the record carries user_id for the D1 pin, email redacted.
Tests @e5fb8ce764: bundle_contract.js 25 arms; replayed /dashboard/ with a modelled window.USER
(trailing script deliberate); offline suite arm (a) asserts the acquired bundle's identity. Own runs on
this box: bundle_contract ok true; offline suite all_pass true. Y's STANDS against transport.py:84-118 /
broker.py:159-200 was the gate (100004 item 2). Y 100018: STANDS -- every line matched against the
Python (identityFromHtml == transport.py:91-96; validateIdentity == :108-117; versionedBundle keys ==
run_session_suite.py:66-83; readIdentity runs in the same context BEFORE ctx.cookies(), so the persisted
jar reflects any Set-Cookie the dashboard read produced); pin 34df3e94 confirmed from the blob; Y's own
run 25/25 + offline all_pass (node v26.9.0). Gate satisfied: P uploads the runner files at 282f7ea427,
re-runs irpt-ycharts-deploy, reads the HostCapture pins back (34df3e94 / 55ddb8f7), builds the package,
then the ONE sign-in; C1 states both library blobs; Y runs --once and the runbook from precondition B.

### IRPT-PERFORMANCE-SUCCESS-STATUS-20260924 -- ACCEPTED @786f767796 (CRO side note 100001; P 100011 item 2)
performance/entry.py:150 put internal_correlation_id into the SUCCESS status; PublicStatusEnvelope is
additionalProperties false without it and public-status.ts:20 closes the same set, so the portal would
have refused every Performance success body as EnvelopeMismatch('status'). Fix: key dropped on success
(refusal path keeps it; served.refuse() strips it); unused uuid import removed; test_entry_selection.py
now validates the wire status against PublicStatusEnvelope (it had validated against the server-internal
StatusEnvelope, which REQUIRES the key -- the test certified the defect) plus a READY/PARTIAL closed-key
arm; 131 passed per P. Rides the next Performance package (CALL-3 needs it); no separate deploy. The
stale "internal_correlation_id" prose in the performance response schema's status description is
contract text, parked for the contract owner. Lesson, recorded: a test that validates against the
INTERNAL schema certifies the internal shape and cannot see the PUBLIC boundary; every wire-status test
validates against the schema the consumer validates against.

### Holdings status repackage: CRO pin merged onto the backend branch at 3d7f66b83b; BEFORE/AFTER awaited.


## 2026-09-24 02:5x UTC - Claude CTO batch 19: Holdings status deployed and verified; legacy probe disable GO; D1 fired

### IRPT-HOLDINGS-SUCCESS-STATUS-20260924 -- DEPLOYED 02:45:27Z (P 100021), CTO-VERIFIED
P: saved plan af3b34e3 applied 0/1/0; member census 33/33 with exactly entry.py differing (== pin
6660c155 / 13012979e1); holdings/tests 144 passed, no skips, at the merge 3d7f66b83b; recorder
c29054e73c; ledger irpt-holdings-status-20260924 CLOSED @bcadb446ba. CTO readback 02:5xZ
(get-function-configuration): CodeSha256 3nc57No0b8rSnz9xbyenToYWgb91aoDT87RHrIJ5vAQ= == the built
artifact; LastModified 02:45:22Z; Active / Successful; handler entry.lambda_handler; layers exactly
irpt-common:5; timeout 29; memory 1024. Andrew's retest requested via MSTR 100024 (expected: the
Holdings TABLE; CRO reads the HAR in place expecting READY / HOLDINGS_READY / 2026-09-22). EXERCISED
reading pending at this write.

### IRPT-RESIDENT-LEGACY-PROBE-DISABLE-20260924 -- GO (P 100027 item 2; CTO 100030)
Found by P while measuring the cutover receipt booleans: EventBridge ycharts-session-probe-schedule
ENABLED cron(0 */6 * * ? *) -> Lambda ycharts-session-probe, which replays the resident's cookies
against the vendor from a different client every six hours -- the race Y's RESIDENT_ASSEMBLY_HANDOFF
item 5 forbids and the receipt's legacy_probe_disabled boolean asserts. CTO own reads: describe-rule
ENABLED, one target; P's saved plan ee5160cf decoded by the CTO's own terraform show -json in the
ycharts-pipeline root: 1 of 26 changes, aws_cloudwatch_event_rule.session_probe update, changed keys
exactly {state ENABLED -> DISABLED, description}; the Lambda stays deployed and on-demand invokable (C2
unchanged). A monitor retired in favour of the owner, not one built; the session-eviction alarm it fed
goes quiet and is stated in the receipt. Sequence: ledger sentinel before the act, safe-apply of the
SAVED plan, describe-rule readback DISABLED, re-plan 0, ledger close, receipt boolean set FROM THE
READBACK; before the rule's next fire at 06:00Z. Lane ycharts-pipeline = CLOUD_OPS_OR_ETL, audited
override on the CTO's word.

### Resident host deps (P 100027 item 3): ACCEPTED
jsonschema 4.23.0 + referencing 0.35.1 (with attrs, jsonschema-specifications, rpds-py) staged under
/opt/investor-reporting-ycharts/pydeps by dnf python3-pip + pip --target on the pip-less host, chowned
ec2-user, import-checked; copied into the package root at install; listed with digests in the receipt
beside SHA256SUMS. Package-mirror egress of the deploy document's own class (npm install / playwright
install); no vendor origin. Lockfile vendoring by the builder = enrichment item (Y's call), reversible.

### Cutover progress (P 100027 item 1)
Host pins read back at 282f7ea427 (library 34df3e94, wrapper 55ddb8f7, package.json 860612d6,
secret-ids.env 88ee08c2); browsers under ec2-user; no units/cron; pre-D1: credentials AWSCURRENT
present, ycharts/session/current VersionIdsToStages null, lease row lease_owner null fence 4, 0 event
source mappings. D1 FIRED ONCE 02:54:32Z (irpt-ycharts-run Task=probe MaxReacquisitions=1, SSM
71d0961f) under the standing host-workflow authorization (CRO 6fc3f5f785 item 3). The exercised arm
of IRPT-RESIDENT-SESSION-BUNDLE-CONTRACT-20260924 = the wrapper receipt + broker.current() grading the
fresh bundle versioned + transport accepting it.

### IRPT-RESIDENT-D1-RERUN-20260924 (P 100033; CTO 100036)
D1 RESULT: exit 1, AUTH_FAILED, 8 x {CH-AUTHENTICATED, via dom}, `filled` false -- ZERO credential
submissions, no POST, no bundle written (secret VersionIdsToStages still null, lease unchanged, fence
4). The GO's ONE sign-in was NOT spent; eight loads of the public /login/ page were. Diagnosis
(static, 282f7ea427): classifyScreen's app-chrome selectors (nav a[href*='/dashboard'], a[href*=
'/model_portfolios']) match the SIGNED-OUT page while no password input matched, so the page classed
CH-AUTHENTICATED via dom; the probe returned NO_IDENTITY_COOKIE without a request; the loop waited.
The README's own "the sign-in DOM and selector list are a MODEL, unmeasured" line came true; the run
carried no page evidence. EXPOSURE (no submission), not an incident.
WORD: (1) commit the fix exactly as bounded -- CH-AUTHENTICATED + NO_IDENTITY_COOKIE + nothing
submitted -> AuthError retried:false at once; screenEvidence(page) = url, selector hit COUNTS per
model group, input census by TYPE, form count, 300-char public text sample, never a credential /
cookie value / field name; attached to that failure and to the MAX_STEPS failure; each step records
the probe reason; sign-in fill, identity read, bundle contract, persist untouched; (2) Y STANDS on the
committed diff (the evidence field lands in a receipt Y's runbook reads); (3) ONE run of
irpt-ycharts-run Task=probe MaxReacquisitions=1 at the fixed pin, AT MOST ONE credential submission:
outcome A signs in -> D1 done; outcome B fails explicitly naming the page -> STOP, the selector model
is edited from the measured evidence, Y reviews, a further run needs a further word. CTO's own read of
P's working-tree diff (47 lines): matches the bounds; node --check ok; bundle_contract failed 0;
offline suite all_pass. Probe-disable GO (100030) does not wait on D1.
AMENDED (CRO 100042, Y 100047; CTO 100049/100052) BEFORE the run fired: the runner's login route is
WRONG -- ycharts_session.js:725 opens /login/ while every measured YCharts login in the estate is
/account/login/ (the CRO's 09-10 live-verified probe probe_split_session.cjs:133/:51, 302 sign-in,
dashboard matched the account email @48db22d1bf; the older capture Lambda index.mjs:101). Y confirmed
from the source three more lines that would WASTE the single submission once the route is right: the
page-wide username pick (:933) lands in the newsletter decoy's input[type=email]; the submit pick
(:940-941) clicks a hidden native submit (30 s timeout) or the decoy's button; no /dashboard/ warm-up
(the aws-waf-token). The committed diff therefore carries (a)-(c) plus (d) default '/account/login/';
(e) form-scoped fill per login_form.cjs:3-8 (password input[type=password]:visible, its form, the
username inside that form incl. [name="auth-username"]); (f) submit = Enter in the password field +
the POST observer so the receipt states "N submissions, fields matched"; (g) /dashboard/ first, then
the login route, bounded wait for a visible password input; (h) auth-username in the selector model.
Y STANDS on that pin, then ONE run, at most one submission; outcome B stops. The CRO's limit: EC2-to-
YCharts portability is unverified until this run.

### Resident host deps, WIDENED (Y 100040; CTO 100044 item 2)
Y's import census over the 82 packaged non-test .py files: third-party = boto3, botocore, jsonschema,
referencing, pdfplumber (ycharts/extract/extract.py, lazy), pdfminer (ycharts/extract/fonts.py, lazy)
-- the certified-report hop 7 imports the PDF libraries through publisher -> publication -> extract,
so a --once poll on an empty queue passes without them and the FIRST real job would park ATTENTION at
hop 7. P re-stages from infra/aws/lambda/layers/irpt-common/requirements.txt (jsonschema 4.26.0,
referencing 0.37.0, attrs 26.1.0, jsonschema-specifications 2025.9.1, rpds-py 2026.6.3,
typing_extensions 4.16.0 -- the deployed Lambdas' and the offline suite's set) plus pdfplumber 0.11.9,
pdfminer.six 20251230, pypdfium2 5.7.1, Pillow 12.1.1 and their resolution; import check names the
lazy modules explicitly; the receipt lists each distribution with version + digest.

### ANDREW-DIRECT 2026-09-24 ~03:0xZ at the CTO terminal -- Anna's table RENDERS; two new findings
Record: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_030xZ_ANNA_TABLE_RENDERS_GLOBAL_VIEW_AND_MODEL_BREAKDOWN_MISSING.md
(verbatim + screenshot transcription). EXERCISED: USD 26,303,302.17, READY, the table renders -- the
fence exemption and the success status are exercised end to end by Andrew's own request. FINDING A:
Anna is absent from the "Global" view and present only under the Cottonwood dropdown; standing
authority: Opal users default to Global and everyone appears there. Routed to P (100044 item 1):
measure resolve-scope / directory-browse / directory-search for an Opal principal at GLOBAL, which
firms' directories the GLOBAL union reads and from which artifacts, whether cottonwood's is in it, and
the request context of Andrew's attempt. FINDING B: acc_0698 renders one "models" node at 100% with
observed-custody basis, "Model coverage 0 of 1 accounts", no model / Opal model / asset-taxonomy
breakdown, Supervision / Advisory "withheld". Routed to M (100043): the accepted COT publication's
content for 0698 / d486 / combined (node kinds, model leaves, holdout status), the coverage field the
portal reads, and whether "withheld" is data, server (P 100044 item 3), or rendering. The CTO rules
each fix on the measured fact; nothing wider inferred from the word.


## 2026-09-24 03:1x UTC - Claude CTO batch 20: Finding B measured; Andrew corrects the COT tree; portal drill items; probe disabled

### IRPT-HOLDINGS-FINDING-B-20260924 -- interim ruling (M 100055/100061; CTO 100057/100066), then CORRECTED by Andrew
M measured the accepted COT publication ac3adb97 under its user: acc_0698 = 33 nodes (ACCOUNT > SLEEVE
"Models" > MODEL_LEAF model_id 6ae9e540 capability_facts model_name "Anna *9238" / is_opal False /
rebalance_model_type Strategy > 30 SECURITY); d486 = 60 (leaf 1ae61190 "Anna *9237"); combined 93; NOT
holdouts (attribution_holdouts.unassigned 0 of 841). Node keys carry NO asset-class member;
HoldingsSnapshot.schema.json has none. "Model coverage 0 of 1" = portal slices.ts modelCoverageOf()
counting a model as a DIRECT child of the account (the leaf is under the sleeve) -> 0 by construction.
"withheld" = DATA: classification.authoritative=false on every node from build_cot (holdings_snapshot.py
:1553-1555, :687-690; no Opal supervision source resolved for COT); the portal renders 'withheld' for
authoritative=false by FE-s-55 and never reads the viewer's authority. Portal side: the adapter carries all
levels (adapt.ts :938-969, no truncation); DrillTree renders ONE level per click; rows are clickable with
no chevron / child count (SliceTable.tsx :120-125); canRenderDrill never refuses on these bodies.
RULED (stand): (1) M's coverage counter counts a model descendant at any depth -- b0e2d9ad on codex/
irpt-m-ui ACCEPTED on CTO read (cycle-guarded parentRef walk; 13 assertions; tsc clean); (2) P's additive
adapter carry of hierarchy_path / capability_facts / modelName is shape-neutral and may land without label
wording; (3) M cuts a VISIBLE drill affordance (chevron + child count per drillable row/slice) and opens a
single-account selection one level deeper than the account; (4) "withheld" un-withholds only with an Opal
fee-taking / advisory source per Cottonwood account asserted authoritative=true (enrichment, data owner);
the asset-taxonomy breakdown is a CONTRACT + PRODUCER enrichment whose SOURCE is a card for Andrew.
WITHDRAWN: the CTO's 100057 statement "Opal model breakdown is empty for Anna by data" -- see below.

### ANDREW-DIRECT 2026-09-24 ~03:1xZ at the CTO terminal -- the COT "Strategy" is the wrapper; the MODELS are its constituents
Record: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_031xZ_COT_MODELS_ARE_CONSTITUENTS_BENEATH_THE_STRATEGY.md
(verbatim). The Rebalancer strategy (e.g. "Anna *9238") holds CONSTITUENT model portfolios ("primary" and
"custom" -- where Opal models live) one drill level beneath it, beside CLIENT (non-model) securities (the
Positioning page's Cottonwood Satellites: models plus a client-held GLD). build_cot collapsed that level
into one MODEL_LEAF carrying the strategy name with the securities directly beneath. CTO's miss: it
restated the producer's field (rebalance_model_type=Strategy) as the product's meaning and told Andrew the
Opal model breakdown was empty "by data" -- a producer's field is not the domain's taxonomy (Rule 24 (iii)).
ACTS (100063/100066/100067): M STOPPED on any COT Holdings rebuild/publication and studies (i) the MDPF COT
constituent decomposition (primary/custom scan; the SmartX silver tables and rosters), (ii) the Satellites
model-vs-client representation, (iii) build_cot's current attribution and what it must read, (iv) the
proposed COT node tree for Anna's accounts; the CTO runs the same study on its own instrument (an Explore
read) and compares before ruling the corrected tree; P's label/facts wording HELD; no wording names the
wrapper a model or asserts no Opal model beneath it; the facts row calls today's leaf "Rebalancer strategy:
<name>" until the re-cut.

### IRPT-COT-HOLDINGS-TREE-20260924 -- RULED (M 100069 + the CTO's own Explore read; CTO 100094)
Two instruments agree: the constituent level exists in silver (fact_model_blend strategy->child edges,
recursive via build_dim_model_portfolio.decompose :219-247; fact_model_definition sleeve_name /
sleeve_depth / symbol / asset_id / allocations); the roster carries STRATEGIES only (65/65); constituents
exist only as blend children, so build_cot's roster default labels every constituent is_opal=False
(wrong; the dimension decides by NAME, rs.is_opal_name :303-309); build_cot expands the blend into
TARGET nodes, parks them privately (:1646-1650) and emits one MODEL_LEAF = the strategy with every
position beneath (cot_actual_security_tree :1305-1387). CTO read denominators: data/**/*.py literal
primary/custom 9 files; fact_model_{blend,roster,assignment} 13 files / 61 hits; MODEL_LEAF 27 files;
rebalance_model_type 22; portal/src "Satellite" 447 hits / 16 files; docs >100 MDPF/cottonwood files;
data READMEs 13. Note: the published tree came from M's branch codex/irpt-m-completion (62 commits
ahead of CLOUD, unmerged); the CLOUD copy of build_cot never fires its expansion on real data (:1019
compares a strategy NAME to GUID keys).
WHERE THE CTO'S READ ADDS: (1) Primary/Custom is the MDPF REGISTRY rule -- mdpf_category_registry.py
:229-235 PRIMARY_MODEL_KEYS (Opal Short-Term, Intermediate-Term, Ultra Short-Term Income, Long-Term
Aggressive, Conservative Growth), qualifier primary|custom (:289), view_path "Models > Primary" /
"Models > Custom" (:292); build_cottonwood_mdpf_slice.py :162-167 CANONICAL_KEY, :318 is_auto_custom
(Opal Fixed Income reclassified Custom :194-201); DIVZ SMA = SMA leaf (mdpf_pair :133); non-Opal
sleeves -> Client residual (:341-359). (2) Model dollars at Cottonwood are ASSIGNED (account value x
blend weight) and CLIENT IS THE PLUG -- recorded constraint (ANDREW_DIRECT_20260923_194xZ_..._CLIENT_
IS_PLUG.md :22-25, :85-87 d; holdings_snapshot.py :1384 "membership is the account's, never inferred
per position"). So M's open rule (split a shared security) is refused as a question, and the CTO's own
draft (per-position attribution by asset_id, proportional split) is WITHDRAWN -- it contradicted a
constraint already in the record (miss recorded). (3) GLD on the Satellites page = "external residual"
(Andrew 2026-09-14): a security the satellite holds that Opal's model books do not; in BD data it sits
inside sleeves. The account analogue = depth-0 components + undefined positions in the Client plug.
THE TREE: L0 ACCOUNT (OBSERVED) > L1 MODEL_WRAPPER = the assigned Rebalancer strategy (ASSIGNED, whole
account; label "Rebalancer strategy: <name>") > L2 MODEL_LEAF per blend child (hierarchy_path per the
registry rule; is_opal by name; qualifier primary|custom; amount = L0 x absolute_allocation, ASSIGNED)
+ L2 SMA leaf where named + L2 CLIENT sleeve (OBSERVED, the plug) > L3 SECURITY (a constituent's
definition components at the constituent's weight, ASSIGNED, with the observed custody position as a
fact; Client's = observed positions not in any constituent + depth-0 components). sum(L2) == L0; a
shared security appears under each constituent that defines it. Producer: M re-cuts build_cot (reads
fact_model_definition; Opal flag by name; retires the private model_target_nodes path); 49F/INF
untouched. GATE: candidate + census for Anna's accounts and the combined selection to the CTO; GO
before any publication (CAS over the current COT index; prior revision retained). Portal: P's carry
shape-neutral; M's render per the ruling; asset-taxonomy = separate enrichment (registry asset_class on
Positioning rows is the source candidate). The 46-model overlay artifact stays withdrawn.

### IRPT-LISTING-SPEED-ASSIGNMENT-20260924 (CRO 100072/100078; CTO 100083/100087)
GAP, the CTO's: Andrew approved the listing-speed brief's levers B1-B8 / F1-F7 at ~20:0xZ ("I like all
your recs, yes go ahead", @6fc3f5f785) and no seat was assigned them for seven hours; the takeover
handoff did not carry them and the CTO did not sweep. Andrew ~03:2xZ at the CRO terminal, VERBATIM:
"It is currently so slow it is embarassing/unusable. I think even though we're only testing, we need to
look into rectifying this issue because it makes every load take 15 seconds too long." Baseline (CRO,
CloudWatch 15:19-03:19Z): irpt-directory-search 264 calls p50 1.33 s / p90 4.91 s / p99 6.95 s;
irpt-holdings p50 1.14 s; one list load = Global resolve (3 firms IN SERIES) + 3 browses + selection +
holdings. ANDREW-DIRECT ~03:2xZ, VERBATIM "I write the backend now (Recommended)": the CRO writes the
backend quick wins, the CTO approves, P deploys; P does the page-side fixes. ASSIGNMENT: CRO B6 (memory
512 -> 1769), B5 (parallel Global resolve, fixed merge order), B1+B2 (one directory + ownership read per
request, one S3 client per container), B4 within-request, B7 keep-warm; one commit each, pin + tests to
the CTO; P deploys code-only. P: F2, F5, F3, F7 and F1 in its lane after D1. RULED: B3 GO with one bound
-- the parsed directory cached per S3 VersionId (HEAD per request, no time TTL; loaders.py:35-37 text
amended to say so); F1 GO -- refresh the auth header, keep the mounted page, never remount. B8 PARKED
(auth-surface change, needs an AE lane; TTL <= 300 s acceptable in principle). Every speed claim is a
before/after on the same instrument. Y holds no listing item (100081).

### IRPT-RESIDENT-D1-RERUN-20260924 -- (d)-(h) LANDED, Y STANDS, the ONE run may fire
P ad8306b769 on 846f7233d2: LOGIN_PATH default /account/login/; /dashboard/ warm-up then a bounded wait
for a visible password input; locateLoginForm = login_form.cjs:3-8 verbatim (form-scoped username incl.
auth-username; refuses with no submission when counts are 0); submit = Enter in the password field +
POST observer (field names vs the secret, booleans only); selector model leads with auth-username;
identity read / bundle / persist / wrapper untouched; library 5a1a8695 (wrapper 55ddb8f7). Y 100092:
STANDS on (a)-(h), pin confirmed from the blob, own run 25/25 + offline all_pass with measured_form. CTO
own run at ad8306b769: node --check ok, bundle_contract failed 0, offline all_pass, login_path
/account/login/, decoy_filled_rows 0. Next: upload at ad8306b769, redeploy, pins read back, ONE
irpt-ycharts-run Task=probe (at most one submission); outcome B stops.

### IRPT-RESIDENT-LEGACY-PROBE-DISABLE-20260924 -- APPLIED
ycharts-session-probe-schedule reads DISABLED (Y's describe-rule 03:1xZ; CTO's own describe-rule 03:1xZ:
DISABLED, cron(0 */6 * * ? *)); P's ledger ycharts-probe-disable-20260924 CLOSED @9b4929fcf4; the receipt's
legacy_probe_disabled boolean has its readback. ycharts/session/current still VersionIdsToStages null.

### IRPT-RESIDENT-D1-RERUN-20260924 -- in progress (Y 100060)
P's 846f7233d2 carries (a)-(c) exactly (explicit failure; redacted screen evidence; identity/bundle/persist
untouched); (d)-(h) (route /account/login/, form-scoped fill incl. auth-username, Enter submit + POST
observer, /dashboard/ warm-up, selector model) are owed in a second commit; Y withholds STANDS until then;
no run before it. Andrew's ~03:0xZ word (Global view, breakdown) and ~03:1xZ correction are recorded;
Finding A (Global-view membership) still awaits P's directory measurement.


## 2026-09-24 03:3x UTC - Claude CTO batch 21: D1 signed in from the host (bundle lost to the probe); Finding A measured server- and portal-side

### IRPT-RESIDENT-D1-RERUN-20260924 -- second amendment (P 100099; Y 100109; CTO 100105/100111)
RESULT (SSM d89690f8, 03:31:19-34Z, pins read back first: library 5a1a8695, wrapper 55ddb8f7): step 0
classified CH-SIGNIN_FORM on /account/login/, fillAndSubmit ran ONCE, Enter submitted, and the vendor
answered with the signed-in dashboard (url /dashboard/#/?dashboardId=1064209; password 0, app_chrome 1,
29 text inputs, 2 forms). The CRO's measured route + form (100042) are LIVE-VERIFIED from the EC2 host;
the sign-in leg's portability is verified. The single submission of 100049 is SPENT. Then seven probes
read NOT_LIVE: probeSession, given a Playwright context with no requestGet, fell through to the bare
Node https port (cookie NAMES + UA; not the browser's stack, jar or WAF token), so the success predicate
never passed, readIdentity never ran, nothing was captured or persisted (ycharts/session/current
unchanged; lease released). P's omission accepted: the MAX_STEPS failure record dropped
login_submission / warmup / password_visible_wait.
WORD (one commit, Y STANDS, ONE run = one further submission under the standing host-workflow
authorization; YCharts' concurrent-sign-in eviction of the first run's server session is designed and
stated): (a) probeSession takes {page, context}; with a page the probe is a fetch() evaluated INSIDE
the page (credentials include, same Accept / X-Requested-With), else ctx.request.get, else the port;
(b) every step records probe_http_status + probe_state; every failure record carries warmup,
password_visible_wait, login_submission; NOT_LIVE names its status; (c) the DISCRIMINATING PAIR in
the receipt, pass or fail: in-page status beside the port status on the same cookies, AND (Y 100109,
adopted) what the port SENT -- cookies with VALUES count, X-AWS-WAF-Token header present, UA -- and
the port reply's Location / x-amzn-waf-action. Reading rule fixed in advance: 302 to /account/login/
with no session cookie value sent = incomplete request (port defect); 202/405 with x-amzn-waf-action
= the WAF/client class (opens item 3 for the Python transport); 200 from the port = the class is fine.
Y's precedent: rest_checkpoint_probe_11.json (09-11) replayed the captured jar browserless from Node
-> template 200, dashboard 200 with the account email, 403 control, waf_action null -- so a non-browser
client is NOT known to be rejected; laptop egress measured, EC2 egress is what this run measures.
(d) nothing else moves; (e) outcome A -> bundle grade, enrolled_user_id pin, C1; outcome B -> STOP with
the pair, a further run needs a further word.
LANDED (P 100117): 160f99b3ea (probe in-page via fetch() evaluated in the page, then the
APIRequestContext, then the replay context, then the port; per-step probe_reason / via / http_status /
state; both AuthError records and the success record carry warmup, login_path, password_visible_wait,
login_submission, probe_pair) + b1f269c6dd (the once-per-run pair control mirrors transport.py
headers_for: FULL jar with values, X-AWS-WAF-Token from the cookie, UA, Accept, X-Requested-With,
Referer; the port returns location / x-amzn-waf-action / content-type; evidence.probe_pair carries both
statuses and what was sent as counts and names, never values). Library c8155201; wrapper 55ddb8f7. CTO
own run at b1f269c6dd: node --check ok, bundle_contract failed 0, offline all_pass, arm (a) probe_via
browser-context / LIVE; the pair fields present in the file. Y STANDS is the gate; then the ONE run.
PYDEPS: the cp312 closure cannot exist for python 3.9, so python3.12 (3.12.14) + pip were installed
and the exact irpt-common pins + pdfplumber set + boto3/botocore staged under pydeps, import-checked as
ec2-user (digest 6a751288f048f127). ABSOLUTE_PYTHON = /usr/bin/python3.12: Y's call (100109), adopted.

### IRPT-HOLDINGS-FINDING-A-20260924 -- Global-view membership, measured (P 100102; CTO's own portal read; CTO 100113)
SERVER (P, own instruments): directory/entry.py global_context() (:321-351) fans ONE resolve per tenant
of IRPT_DIRECTORY_BUCKET_MAP; the deployed env on all four functions = {49financial: opal-data-bd,
cottonwood: opal-data-cot, inflection: opal-data-inf} -- cottonwood is in GLOBAL by construction; a
failed firm is retained as UNAVAILABLE with a reason. The cot directory (opal-data-cot, 2026-09-17, 260
entries, revision irpt-dir/cottonwood/2026-09-17/1.0) carries exactly ONE entry with Anna's two
accounts. Ownership maps: bd 445 KB; cot 107 bytes; inf ABSENT (empty). OPAL_GLOBAL is minted only from
the explicit roster (_scope/resolve.py:47). browse() and search() are SINGLE-FIRM (entry.py:139, :242);
the Global LIST is a portal fan-out. CloudWatch (02:58-03:10Z, 68 events, START/END/REPORT only; the
sink is not yet in irpt-directory-search) cannot show the child states. The 02:12Z HAR holds no
directory calls (CTO read in place: 15 entries, 0 resolve/browse).
PORTAL (CTO's own read, shared tree): index.tsx:57-63 resolves 'global' once; :97-98 contexts = the
scope of every READY firm; an UNAVAILABLE child is shown at :188-191 ("Unavailable firms: <tenant>").
header/ClientSearch.tsx:55-70 fires ONE browseDirectory per context (limit 25) via Promise.allSettled;
a REJECTED browse contributes [] and is only counted; `loaded` stays true unless all fail -- a firm
whose browse rejects VANISHES SILENTLY; :41/:57 also drop a context with no directoryRevision. Row ->
scope matching (:105) by verifiedRequestFirm.firmId === entry.firmId would make a row unselectable, a
different symptom. Candidates ranked: (C) cottonwood's browse under the Global-derived scope rejects
(fingerprint/revision validation, spelling, parse) and is dropped silently -- consistent with no alert
seen; (A) cottonwood's resolve child UNAVAILABLE -- would print the alert; (B) other.
ACTS: P fixes the silent drop (a rejected per-firm browse or a missing revision is surfaced on the alert
line with firm + reason class; never a silent []), commit for CTO review; P drives resolve GLOBAL +
browse per returned firm scope in the directory harness (no live headers) and reports which firm's
browse refuses and why; the HAR of the Global view (resolve firms[].state/reason + the browse calls) is
asked of Andrew and the CRO reads it in place. Withheld columns: none server-side (P; snapshot.project
never reads the viewer's authority); M's producer authoritative=false stands as the whole answer.
