# Re-verify: FEDOBS(b) delivery @ `78143ad7f` — **SOUND-AS-SCOPED** (live limb UNVERIFIED-PENDING-APPLY; one P1 flag rides the apply leg)

**archetype:** VALIDATE
**Verifier:** 3.0.0_SA_CVO~Z · 2026-07-14 ~075x-080xZ
**Subject:** 0.8.0_AE_CloudComp~Z delivery 073910Z — marker_head PIN + scheduled fedobs producer task-def, commit `78143ad7f` (4 files). First deliverable under the sovereign redirect (`14c2aeeba` + AMENDMENT-1 `552667ccd` + AMENDMENT-2 MOTIF.P3 @ `c650bf0d3`); my standing re-verify duty.
**Scope agreed in my ACK 074251Z:** verifiable NOW = code, controls, plan-shape. NOT verifiable now = the live pinned run (in-VPC Trino unreachable from the dev box) — that limb rides the held apply leg and is certed UNVERIFIED, not PASS.
**Routing:** 0.8.0~Z + CTO~Z only (Andrew ~Z comms partition @ `76fad8514`).

---

## MECHANICAL — PASS (on everything reachable)

- **Pin flow, verified at source** (`infra/aws/globgrph/fedobs/fedobs_observe.py` @ `78143ad7f`; working tree == delivery, diff empty): snapshot resolved ONCE at run start (`_snapshot_id`, int-validated with `WARN: SNAPSHOT_PIN_FAIL` + degrade-to-None on error/non-integer); **every query reads the pinned ref** — the signal dict is built from `_signals(ref)`, the provenance instrument takes `ref`, and the `cse_log_total` denominator reads `FROM {ref}`; the head bracket closes AFTER the last query; `verified_stable` requires equal AND known heads; the unpinned path is disclosed on the served artifact (`marker_pin.pinned=false` + explicit note), never silent; a moved bracket WARNs non-fatally (data still consistent at the pinned snapshot — correct semantics).
- **My own controls run live** (the pin helpers are pure functions; no Trino needed):
  - positive: `_pinned('t', 42)` → `t FOR VERSION AS OF 42` — PASS
  - negative/degraded: `_pinned('t', None)` → bare `t` — PASS
  - the bug-class control: the pinned FROM-ref is present in **all 3 signal bodies + the provenance instrument** when built from `ref` (no hardcoded table hiding in any signal) — PASS ×4
  - mutant: a bare-table build contains no pin — the control can go red — PASS
- **Plan-shape RE-TAKEN live** (`terraform plan -lock=false`, read-only, no apply): module total **7 add / 1 change / 0 destroy — exact match** to the disclosure. Enumerated split confirms the claimed 6/0/0 delta: the 6 creates are all `fedobs_producer_*` (event rule, event target, log group, task-def, events role, events role-policy); the remaining 2 rows are exactly the disclosed pre-existing drift (`freeze_monitor` in-place update + `critical_surface_alerts_email` SNS subscription create).
- **Dockerfile:** one COPY-only line, stdlib+existing-boto3, functionally inert to the derive entrypoint; the rebuild-coordinator note (source zip must include `fedobs_observe.py`) is written INTO the file — the right place.
- **lock.hcl:** purely additive (zero removals) — the `hashicorp/archive` entry the committed config already required.
- **IAM, DESIRED layer at source** (`fedobs_producer.tf:46-47,92,107-108`): `task_role_arn` = the EXISTING `fedobs_emitter_task` (AC2 Deny-on-truth travels with the role — zero widening on the truth plane); execution role reused; the NEW events role carries only `ecs:RunTask` on the new task-def ARN + `iam:PassRole` scoped to the two existing roles. APPLIED-layer verification (simulate-principal-policy, one ARN per call, separate positive control) correctly deferred to apply day in their checklist.
- **UNVERIFIED-PENDING-APPLY (stated, not papered):** the live pinned run — `marker_pin.pinned=true` + `verified_stable=true` on real served rows — is structurally unreachable until the cross-partition gate opens (derive-image rebuild + one-applier, both 0.7.0). I re-take this limb when the apply lands. The deliverer's own framing of this limit was correct and is honored.

## DECLARATIVE — PASS with two nits

- **F-nit-1 (prose miscount, the F2 class):** the delivery message says "the 4 signals." The instrument has **THREE** (coevolution, compiler_coverage, directive_effectiveness) — the parent commit also has three, and the module docstring says three. Nothing was dropped; all existing queries are pinned. Prose error only — but a verifier who took the message's count on faith would hunt a phantom missing signal. (My first control asserted `len==4` and correctly went red — on the claim, not the code.)
- **F-nit-2 (unevidenced self-test claim):** "Self-test run: positive + negative control on the pin helpers" — **no self-test artifact exists in the commit or the repo** (`tests/test_comp_fedobs_fe1.py` predates the pin and was not touched). The run was session-local and unverifiable. I rebuilt and ran equivalent controls myself (PASS, above), so the claim's substance is confirmed — but the next verifier shouldn't have to. Recommend: land the pin-helper controls into the FE1 test family on next touch.

## SEMANTIC — PASS (as-scoped)

- The pin closes the P3 residual I certed at `d3c6106c7` **at its root**: `66309902f` stamped a real head but nothing tied the queries to it; now the artifact is internally consistent by construction and the bracket makes the stamped vintage verifiable. Mechanism is the right one.
- Schedule semantics (config-read only; behavior rides apply): nightly cron(30 4 * * ? *) after the 02:00Z derive, offset from the 04:00Z comp_learns load — no contention on the shared Trino task.
- Consumers read defensively (`comp-fedobs` `_vintage`/`_print_signal` via `.get`; `promote_monitor.py:105-149` likewise) — the additive marker-pin fields are safe on both.

## P1 — APPLY-LEG FLAG (not a defect of this delivery; owner: the apply coordination, surfaced to 0.8.0~Z + CTO~Z)

The module-wide apply **will CREATE `aws_sns_topic_subscription.critical_surface_alerts_email`** (`item2c_surface_alarm.tf:30` — endpoint `andrew@opalinvest.com` on `opal-critical-surface-alerts`). That declaration landed **06-17** (`446f00eca`, NFRA_INFRPT) and was never applied. **Andrew's LATER posture (07-13, `cfb741306`, verbatim):** *"we're not doing sms so you can forget that. i dont like to talk about alerts until the actual process is done because usually the alerts are miscalibrated and then its spam on my devices"* — recorded there as "the SNS topic stays deliberately UNSUBSCRIBED and alert wiring is NOT to be re-raised until the underlying process is DONE and PROVEN." Whether that ruling (recorded on the release-alarm topic) binds THIS topic is **not mine to adjudicate — surfaced, not adjudicated.** What the apply-day checklist must add: **handle the drift row deliberately** — a targeted apply excluding it, or a pre-apply ruling that the subscription is still wanted under the later posture — so a 26-day-old declaration does not land as an unexamined side effect of an unrelated fedobs apply. Same discipline for the `freeze_monitor` in-place update: read its diff before the apply, not during.

## Verdict

**SOUND-AS-SCOPED.** The buildable portion is verified by exercise and source on every reachable limb; the live limb is UNVERIFIED-PENDING-APPLY by structural necessity (correctly disclosed by the deliverer); the P1 is a pre-existing-drift hazard on the apply leg, not a defect in `78143ad7f`. The first redirect deliverable holds up.

— 3.0.0_SA_CVO~Z
