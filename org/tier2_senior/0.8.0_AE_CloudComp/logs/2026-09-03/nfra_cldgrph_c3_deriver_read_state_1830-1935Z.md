# NFRA_CLDGRPH C-3 deriver read-state build — 0.8.0_AE_CloudComp~O

**archetype:** IMPLEMENT
**Date:** 2026-09-03
**Task Order:** NFRA_CLDGRPH.TO-CG-C-3
**Status:** COMPLETE LOCALLY — proof validated before task-face flip; no push or deploy

---

## Objective

Make the canonical graph deriver report failed S3 notification reads as `UNREADABLE`, derive S3-to-Lambda `TRIGGERS` edges from both live AWS and Terraform declarations with visible provenance/disagreement, print a read/unreadable bucket denominator on every full build, and exercise the repaired engine read-only against the live account plus a denial seam.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "<inspection question>"` before searches/inspections | PASS | Routing was measured; low-confidence/no-curated results were not treated as decisions. |
| comp-to | `bash .tools/comp-to NFRA_CLDGRPH.TO-CG-C-3.deriver-read-state` | PASS | Set the race-free seat/session TO context through the repository-local entry point. |
| comp-read | `python .tools/comp-read org/modules/graph/comp_aws_cli.py --for ...`; `python .tools/comp-read ... --enumerate 'except:\s*$|except Exception|pass$'` | PASS | Read the notification sites and measured the current exception census. Bare user-bin shim was ACL-denied; COO ruling 93884 authorized the local Python entry point and forbade ACL changes. |
| comp-find | `python .tools/comp-find --corpus aws 'TRIGGERS'`; runtime caller/COPY search | PASS | Pre-write graph reported 0 textual TRIGGERS hits across 2,132 AWS nodes at DB vintage 2026-09-03T18:23:39Z; runtime search resolved the canonical runner/image path. |
| commit-gate | `bash .tools/commit-gate.sh org/modules/graph/comp_aws_cli.py org/modules/graph/tests/test_comp_aws_s3_notification_state.py` | PASS | Clean for 2 of 2 touched Python files, both at commit and post-commit. |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <C-3 proof> C3-AC1,C3-AC2,C3-AC3,C3-AC4,C3-AC5,C3-AC6` | PASS | VALID before the task-face complete flip. |

Results: PASS=accurate+useful | PARTIAL=present but noisy | FAIL=wrong/crash/silent | SKIPPED=explain why | WARN=empty+correct WARN message

## Work Completed

1. Replaced three notification-specific failure swallows with a single cached `READ`/`UNREADABLE` result carrier; unknown node counts remain `None` and retain the error.
2. Added Terraform-state discovery for resolved `aws_s3_bucket_notification` Lambda targets and merged it with live reads into `TRIGGERS` edges carrying `live`, `declared`, or `both` provenance plus explicit source disagreement.
3. Added a per-build summary in graph metadata and stdout: `buckets read / buckets unreadable` plus unreadable names.
4. Added four focused tests for the denial state/denominator, legacy-zero mutant, three-way provenance merge, and resolved Terraform provenance.
5. Exercised the full canonical deriver against real AWS read-only: exit 0, 3,934 edges, 188 `TRIGGERS`, 34 read / 0 unreadable, `NOT PERSISTED`.
6. Quoted the three `opal-data-bd` Lambda targets; all three reconcile as provenance `both`, live state `READ`, disagreement `NONE`.
7. Filed and committed S26 (shim ACL), S27 (cot EventBridge-only), and S28 (shared-image rebuild route), each through the one-new-row gate; preserved inherited S20.
8. Received and ACKed the CG-s-2 read-dependency release: revision-3 task advanced the existing projection path to the 19:02 vintage after exact verification; C-3 claims no CG-s-2 surface.

## Evidence

- Engine/tests commit: `b5bc1c8b27e89a477e17a5d9b789fdc010173af5`.
- Notification swallow sites: 3 before, 0 after. Whole-file executable census: bare `except` 0→0; `except Exception` handlers 81→79; `pass` statements 25→24.
- Test battery: 27/27 passed in 1.47 seconds; Python compilation passed.
- Real build denominator: `s3 notifications buckets read=34 / buckets unreadable=0; unreadable=none`.
- Denial plant: legacy returned zero; repaired helper returned `UNREADABLE`, `configuration=None`, and denominator 1 read / 1 unreadable with `denied` named.
- Push measurement: `origin/CLOUD=351f309e0a6ded1a5a5bdf3aacec18a5f9f8dbee`; implementation ancestry rc 1, therefore LOCAL; no push.

## Decisions and Bounds

| Decision | Rationale |
|----------|-----------|
| Cache one honest notification result per bucket per build | Node properties and all notification edge classes consume the same state and cannot disagree through separate reads. |
| Preserve declared edges when live is unreadable | The declared plane remains evidence; `UNKNOWN_LIVE_UNREADABLE` makes the unresolved comparison visible. |
| Do not invent a cot Lambda edge | The complete cot notification resource and resolved state are EventBridge-only; S27 records the spec/world divergence. |
| Route, do not deploy, the shared image | Docker COPY proves a rebuild is required and the image serves five task definitions; deployment is outside C-3. S28 assigns routing to the issuer. |
| Do not alter compiler shim ACLs | COO ruling 93884 requires repository-local entry points and preserves launcher ownership. |

## Files

| File | Change | State |
|------|--------|-------|
| `org/modules/graph/comp_aws_cli.py` | Honest read-state carrier, declared-source merge, provenance/disagreement, denominator | LOCAL commit `b5bc1c8b27` |
| `org/modules/graph/tests/test_comp_aws_s3_notification_state.py` | Four focused controls including legacy mutant and denial seam | LOCAL commit `b5bc1c8b27` |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` | S26-S28 observations and measured denominator | LOCAL commits `99ee4a5968`, `57500ca0fb`, `6e5af8cdc7` |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.8.0_AE_CloudComp~O/CG-s-14.deriver-read-state.result.md` | Required one-block result and comp-trigger handoff | This completion commit |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.8.0_AE_CloudComp~O/NFRA_CLDGRPH.TO-CG-C-3.deriver-read-state.proof_of_spec.json` | Six-criterion proof instance | This completion commit |

## Current State

All six C-3 criteria are proven locally. The implementation, tests, result, proof, and task status are on `CLOUD` without a push. The only external follow-on is the separately routed shared-image rebuild recorded in S28; it is not a blocker to the bounded local task and was not performed.
