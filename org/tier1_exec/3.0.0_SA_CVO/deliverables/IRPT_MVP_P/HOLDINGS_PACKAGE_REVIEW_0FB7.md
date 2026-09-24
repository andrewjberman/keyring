# Holdings declared-package review: bounded PASS

Reviewer: `3.0.0_SA_CVO~P`, 2026-09-22.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Candidate: `0fb7e56629c5262a4074543d2f67ef58c529fda3`.
Comparison/source pin: `5a85252603e80515d2e7f1875ce5debdb7cdbd91`.

The declared holdings package reconstructs and its guarded reader controls pass at these pins. No new packaging defect was reproduced. IAM source permissions correspond to the observed reader call shapes within the boundaries below; effective deployed IAM remains untested. This result is not full product, package-deployment, layer or live readiness.

## Declaration and byte denominator

The exact source maps contain 216 function objects. Only `irpt-holdings` changes; all 215 other function objects and all top-level metadata compare equal. Within holdings, only `files`, `staged_from`, `_staged_from_note` and `_build_note` change. Deployment metadata is unchanged.

All 31 unique declared members were independently reconstructed from Git blobs. All 28 staged source pins/hashes matched; the 3 direct members (`stage.py`, `STAGE_MANIFEST.json`, `BUILD_MANIFEST.json`) matched the candidate and comparison pin. All 31 resulting hashes also match the producer's committed evidence. Historical manifest files are compared as package members, not accepted as proof that a deployment occurred.

The canonical nested `lib/opal_naming.py`, registry/schema tree and flat forwarding module import from the reconstructed package. The forwarder's `address` is the canonical implementation's same function object. Missing `scopes.json` refuses in a fresh isolated process. The canonical import-closure checker passes for 17 packaged Python files; its documented exemption for nested lazy imports remains. Real reader controls import no `pyarrow`.

## Executed checks

The supplied guarded-entry controls were rerun against the independently reconstructed package: selected-account read, unversioned current-index read followed by exact-version manifest/snapshot reads, corrupt-byte refusal, post-read grant revocation refusal, canonical locations for all three firms, and missing-registry refusal all pass.

Seven additional reviewer controls pass:

1. Injected `snapshot_fixture` refuses before product storage reads.
2. Injected `resolved_scope` refuses before product storage reads.
3. Injected `object_id` refuses before product storage reads.
4. Missing retained selection refuses before product storage reads.
5. Actual `SelectionStore.load` emits `GetItem` with the configured table, exact tenant/`SELECTION#<reference>` key and `ConsistentRead=True`.
6. Actual directory and ownership loaders emit the expected unversioned S3 calls for all three enabled identity firms.
7. Actual canonical product locations match the source resource patterns for all three firms; current-index, Gold and QA paths do not match the dated Platinum pattern.

These additional controls reuse the pinned producer's synthetic guarded-entry setup, then execute reviewer-written assertions. The spy clients exercise real packaged methods but are not AWS or an IAM simulator. The setup's selected guarded read uses one firm's synthetic accepted publication; location/loader enumeration for three firms is not three-firm live product proof.

## IAM source correspondence

| Read | Source grant and observed shape |
| --- | --- |
| Current publication index | `s3:GetObject` on each canonical firm's exact `irpt/<firm>/platinum/holdings/current/manifest.json`; no VersionId request parameter |
| Accepted manifest and snapshot | `s3:GetObjectVersion` under canonical `irpt/<firm>/platinum/holdings/date=*/*`; reader sends VersionId |
| Current directory | `s3:GetObject` under the separately registered identity bucket's `investor-reporting/directory/*`; pointer and pointed artifact are read |
| Ownership | `s3:GetObject` on identity bucket `platinum/<firm>/ownership_map.json` |
| Retained selection | `dynamodb:GetItem` on the requests table; LeadingKeys is the enabled identity-firm set |
| Requests-table KMS | `kms:Decrypt` on the core key with DynamoDB ViaService and requests-table encryption-context conditions |

Canonical product buckets are `opal-data-49financial`, `opal-data-inflection`, and `opal-data-cottonwood`. Scope dependencies still use `opal-data-bd`, `opal-data-inf`, and `opal-data-cot` respectively. This deliberate separation was observed in the actual loaders and naming module, not inferred from abbreviated names.

The source dated-object wildcard allows versions in that dated subtree; it does not itself enforce a particular accepted version. The reader enforces the accepted receipt's location/version/hash. Likewise the LeadingKeys set is a service-level firm boundary, not a per-viewer authorization policy; the guard owns current viewer authorization. The source includes no S3 writes/listing, Dynamo writes or vendor action in these policies. Own-log writes remain present. No permissions from external attachments, key policies, bucket policies, SCPs, remote state or deployed resources were evaluated.

The absolute-module-path correction is present. Terraform validate PASS remains producer-reported; this review did not rerun init/validate or read remote state. The package uses installed local third-party modules; the deployed shared layer remains unqualified. No builder upload, deployment, provisioning, authenticated HTTP, server-clock, queue, custody census or Gold writer proof was performed. Holdings publication semantics remain CVO~M's separate review scope, including its timeout/versioning limitations. Full P1-P8/S1-S7 gates remain NOT_EVALUATED. Upload R-P09 is separate and remains open pending a pinned retest.

## Reproduction artifacts

- `holdings_package_probe_0fb7.py`: exact-pin reconstruction, complete map comparisons, supplied controls and source hashes.
- `holdings_package_cases.py`: seven additional controls. SHA-256 `2a40547dac4d873a11c6fc2351b44752e9234b113737872b6f4a93f00952c7d6`.
- `holdings_package_probe_0fb7.json`: complete member hashes, subprocess outputs, observed calls and Terraform source hashes.

All three subprocess runs exit 0. Ruff passes for both reviewer files. An initial lint run identified implicit shared setup names in the reviewer case fragment; explicit imports and setup bindings corrected that harness issue, then all controls were rerun. No candidate source changed.
