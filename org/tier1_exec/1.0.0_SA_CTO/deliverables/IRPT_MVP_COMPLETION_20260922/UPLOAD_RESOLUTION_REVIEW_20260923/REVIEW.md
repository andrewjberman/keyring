# Direct CTO review: upload resolution source

Reviewer: 1.0.0_SA_CTO. Date: 2026-09-23.
Source: 6cfe01c3e238e9a90e88d3a501b25ac0eaf41540. Handoff: 8228a253e2.
Verdict: PARTIAL SOURCE REVIEW; TOTAL-DEADLINE DEFECT OPEN. No feature or runtime acceptance.

Fresh git archive replay: intake164 tests+18subtests; generation236+32; session35. Total435 tests+50subtests, no skips. Exact outputs retained alongside this record. Paired dependencies were copied from the prior isolated CTO dual-owner review archive, retaining its fixture-enforced pins: P37526 schema/storage; M485b maintained source; P9a3 access; P4ec Entry; dd6 storage and8845 accepted-reader controls. See ../DUAL_OWNER_CTO_REVIEW_20260923.json for full dependency evidence. CRO lookup fixture files02/03/04 came from d7d044ba7a. Synthetic50-symbol harness is not live lookup evidence. CRO replay reports five requested, three FOUND, two NOT_FOUND; it establishes only those recorded responses. No network, credentials or cloud actions were used.

Reviewed source includes dedicated CSV/XLSX template parsing, immutable v2 freezer, normalized recipe bridge, deterministic provider resolution/cache, K3 advisory, account-level operation lease and pure D2 controller. Existing test passes establish bounded offline mechanics only. Legacy broker regression was reported by Y, not replayed by CTO; its known status-only eviction fallback remains W1 work.

## CTO-Y-KIMI-DEADLINE-01

Reproduced with ctoreview_deadline_probe.py against the archived source: first check attempt spends119s and raises HTTP503; second spends119s and returns valid JSON. call returns success after238s with timeout arguments[120,120]. The handoff promises a120s total check budget including both attempts. This implementation resets the budget each attempt.

Required repair: one monotonic absolute deadline across telemetry, attempts and response validation; recompute remaining time immediately before each send; no send after exhaustion, no accepted late result; transport must enforce remaining wall time. Meaningful regression controls cover both call kinds, transient retry, telemetry delay and exhausted budget. Local patch assigned to Y by receipt20260923T191250Z. No live provider exercise required to fix this defect.

The saved probe takes its archived source root from IRPT_CTO_REVIEW_SOURCE_ROOT, falling back to its own directory. It deliberately exits successfully when the original defect is reproduced; it is evidence, not the eventual acceptance test.

## Remaining integration boundaries

P: closed v1/v2 admission and retention schema; actual CAS/outbox and fenced lease lifecycle; all account consumers sharing the lease; transport-enforced hard deadline; D2 persisted continuation and host ownership; scoped routes/queue/polling and exact package/cold-import evidence. Y: UploadService/Entry v2, durable resolution workflow and W1 conservative failed-pull wiring, explicit user approval/new revision/three-round lineage, UI and disclosure. M: installed canonical identity and dated USD/share-class price facade remains absent; Shares must remain explicitly unavailable rather than fabricate prices.

Kimi web-search capability, installed runtime ports, shared-account serialization, session recovery, browser continuity and report/PDF end-to-end behavior remain unproved. Concrete deployment/login/vendor authority remains governed by existing rulings, not this offline review.
