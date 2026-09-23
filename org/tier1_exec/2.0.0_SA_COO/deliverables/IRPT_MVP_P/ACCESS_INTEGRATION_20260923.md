# IRPT actual-viewer integration and dual-owner handoff

Seat: 2.0.0_SA_COO~P. Source evidence only, not new deployment or full-access completion.

## Candidate and measured tests

P source 37526d36aeb9a1299d0046355aa3c1e96e852b4f contains the closed dual-owner RequestComposition schema, shared validate_bindings, 50 passing composition contract tests, and repository.head compatibility for existing two-argument get callbacks on same-firm reads. P Entry remains4ec461a2e9; trusted viewer9a3ec2a11f; storage base dd6edfc3aa.

Exact Y deltas85af5eb95d72051c363727229981c4dc1a35cad9,4ea95d1117cb2dd48c4d3b95fb980704c4cec87f,104d9472f11a45e072b5feb5fce0e5ae0aa016e6 are locally applied in this tree. They are NOT committed here: safe-commit rejected P on13 Y-owned paths. The gate was not bypassed. CTO was given the exact blocker for a narrow integration grant or owner-preserving procedure. Their unchanged source commits remain the provenance pins.

Separate process runs before the shared schema change: ops179 PASS; intake94 PASS+18subtests; generation212 PASS+32subtests. Zero skips. Total485 tests+50subtests. Paired tests load immutable actual P viewer9a3/storage dd6/Entry4ec fixtures from.runtime/directory-review/paired-*; other tests load the current combined tree. Current P storage/Entry focused59 PASS. Do not confuse pinned fixture bytes with later repository.head compatibility bytes.

After37526d36ae: test_request_composition.py50 PASS in1.87s; standalone generation suite212 PASS+32subtests in26.37s, zero skips. A wider contracts+generation run returned322 PASS+32subtests and30 FAIL, all listed under_contracts/tests/test_seam_paired.py (legacy fixture denominator11 versus current12, old operation-name paths versus canonical paths, and current response envelope requirements including unprojected_grant). A contracts-only repeat confirmed first two failures independent of generation module collection. These failures are retained findings, not a green whole-tree assertion; no test was disabled or loosened to suppress them.

## Exact ownership contract

resolved.owner is the submitting actor with concrete input storage firm; resolved.input_owner, when present, is the original normalized input owner. Missing input_owner retains legacy owner semantics. Prospect base input owners may omit repository-added account_ids/prospect_input_id; when present those must equal empty accounts and the original upload ID. The normalized document owner, retained bytes, artifact hash/reference and upload ID remain unchanged. Cross-storage-firm composition is refused in this tranche.

M descriptors bind input_owner; the exact recipe_source_id/settings_source_id descriptors bind the actual request owner. Prepared-by/organization source scope and projections remain attributable to the actual Opal actor/home. The closed Opal prospect schema forbids invented advisor/custody fields and browser ownership injection. This validator establishes shape/equality, NOT current permission: Y admission/service/worker must verify input retention owner and current actor access to both records before acceptance and final dispatch. Y/M received the pin for paired integration. No deployed ZIP contains these new changes.

## Live result and recorder

Andrew directly confirmed Global/Select Firm and investor list appear on the existing authenticated localhost5174 live-data surface. This closes only the scope/list symptom. No claim is made for pagination, account selection, persistence, submission, generation or full Opal access.

Directory deployment remains the exact previously approved one-function apply undere186d7ea22. Canonical ledger4917bed568 remains OPEN: V1 recorder and B1 remaining journey proof. Under CTO containment5cc9fa65e4, the sole accidental irpt-ycharts-generate artifact_sha256 local edit was restored byte-exact to its pre-recorder value; no cloud change. RECORDER_CONTAINMENT_20260923.json carries hashes. Partial directory record, bad broadened CHANGELOG and reconcile audit remain preserved, uncommitted, pending canonical recorder repair. No manual replacement record, whole-file reset, CLOUD push or new deployment.
