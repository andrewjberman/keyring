# Delta re-cert: PROMOTE.P1 absorptions @ `a9589dc5a` — **PASS** (P3 rewire unblocked) · FEDOBS(b) live limb — **VERIFIED on the served artifact** (cert upgraded) · one new P2 surfaced

**archetype:** VALIDATE
**Verifier:** 3.0.0_SA_CVO~Z · 2026-07-14 ~084x-090xZ
**Commissions:** CTO~Z ruling `cb6a86177` term "DELTA RE-CERT before any wiring" (requested by 0.8.0~Z 084300Z) + my standing FEDOBS(b) UNVERIFIED-PENDING-APPLY limb (0.7.0~Z apply ping 085903Z).
**Routing:** ~Z group only (partition @ `76fad8514`).

---

## Part 1 — Delta re-cert of the three DS~B absorptions (`a9589dc5a`, one file, production manifest untouched)

**Self-test: 29/29 live** (was 22/22; the six absorb tests + fixture-support test all pass under my run).

**Limb (a) — DROPPED both ways, re-taken through the API on synthetic records (temp trail, never the production manifest):**
- MEASURED→DROPPED without `drop.coverage_ref` → REFUSED ("never drop-unlooked-at") — PASS
- legal drop (reason + coverage_ref) → DROPPED — PASS
- closed table: DROPPED→MATERIALIZED → REFUSED — PASS
- DROPPED→CANDIDATE without `new_evidence.ref` → REFUSED; with it → CANDIDATE, `recandidacies[]` stamped (1) — PASS
- **Bonus strictness my probe tripped:** `drop.reason` is ALSO required (a drop must state why, not just what was looked at) — stricter than the delivery prose documented, in the right direction.

**Limb (b) — the measurement floor, re-taken with MY OWN planted values (not the fixture's):**
- focused 0.07 (raw 0.44 alongside) at PROPOSED → **REFUSED on the invariant-2 MEASUREMENT FLOOR arm**, refusal text carries the floor (0.12) AND the raw (`raw=0.440, transparency`) — PASS
- above-floor control (focused 0.13): the floor arm does NOT fire (refusals present were the other PROPOSED requirements my synthetic evidence lacked — correct discrimination) — PASS
- all three fallback arms exercised: focused → raw-only (`coupling_ratio=0.05` refused) → legacy `co_sessions` (1 refused / 3 passes vs floor 2) — PASS
- **Probe note (naming):** the raw's field is `coupling_ratio`; my first probe wrote `raw_coupling_ratio` and silently lost only the transparency rider (the GATE still fired — fail-closed held). An integrator making the same slip loses transparency, not safety. One docstring line naming the exact keys would close it.

**Limb (c) — floor-import identity:**
- `FEDOBS_RATIO_FLOOR` homed in `comp_promote_lifecycle.py` = **0.12**, env-overridable (exercised: `FEDOBS_RATIO_FLOOR=0.5` env → module reads 0.5); `MEANINGFUL_CO_OCCURRENCE_FLOOR` = 2 — PASS
- **The 0.15-vs-0.12 question GROUNDED** (the ruling message said DS~B's 0.15; the code ships 0.12): 0.12 is the CTO re-calibration my own office certed on 07-08 — signal-cert `c5fd9d85f` + the gate-flip exercise-cert (`logs/2026-07-08/cvo_FINALIZE-item3_gate-flip_...md`), incl. the CEIL-sensitivity sweep showing 0.12 is mid-gap of the natural split 0.094→0.151 and not knife-edge. The in-code lineage comment (`:96-100`) states exactly this. 0.12 is the correct current value; 0.15 was the pre-flip constant.

**Verdict Part 1: DELTA RE-CERT PASS.** The machine is re-certed ON THE DELTA; per `cb6a86177` the P3 rewire + retire-with-provenance + same-name-trail archive may proceed as ONE change (I take that change when it lands — the rewire moves a live consumer).

## Part 2 — FEDOBS(b) live limb: VERIFIED (upgrading cert `454394604` off UNVERIFIED-PENDING-APPLY)

Re-taken from the SERVED artifact myself (`s3://opal-313476888478-globgrph/warehouse/fedobs_signals/observations/fedobs_observations.json`), not from the ping:
- `marker_pin.pinned = True`, `marker_pin.verified_stable = True`, bracket heads EQUAL (`c155b488…` both ends), `pinned_snapshot_id = 7392125655251158233` (top-level, as flagged)
- three signals present (the CI-asserted three), `source_table = iceberg.globgrph.cse`, `cse_log_total = 342`, and an internal consistency the ping didn't mention: **provenance_instrument rows = 342 == cse_log_total** — the decompression instrument covers the full census
- vintage UNFROZEN: computed_at 1784019051 (07-14 08:51Z run on the rebuilt image) vs the frozen 07-08 stamp — the served-observations freeze that NERVES diagnosed is over
- apply scope as certed: module 7/1/0, TARGETED applied 6/0/0; **negative control run by me: the excluded email subscription did NOT land** (no email endpoint on the topic).

**The FEDOBS(b) cert's MECHANICAL limb is now fully PASS. SOUND-AS-SCOPED upgrades to SOUND.**

## New P2 (surfaced, not adjudicated — pre-existing, NOT caused by this apply)

My SNS negative control enumerated the topic's ACTUAL subscriptions: `opal-critical-surface-alerts` carries a live **SQS** sub (`…-coo` queue) and a live **SMS** sub (`+1786…`, landed June @ `ade04b01a`, NFRA_INFRPT era — later noted "sandbox-blocked" @ `446f00eca`). Andrew's LATER posture (07-13, `cfb741306`, verbatim): *"we're not doing sms so you can forget that."* Latest + most-restrictive puts the SMS subscription in conflict with the standing ruling — possibly inert (SMS sandbox), but **an inert subscription on a device number is drift wearing a dead switch, and nobody has ruled it retired.** Resource is base-group-owned (cross-partition): routed to CTO~Z for disposition routing (retire via the owner's lane, or an explicit Andrew keep-ruling). The SQS sub (a queue, not a device) reads consistent with the posture; noted for completeness.

## Verdict

**Delta re-cert PASS — P3 rewire unblocked. FEDOBS(b) SOUND (live limb verified on served rows). One P2 surfaced (SMS sub vs the 07-13 no-sms verbatim).** The learning plane is now live end-to-end up to its ratify gates: scheduled producer live + pinned, machine canonical with absorbed floors, 7 candidates awaiting their first genuine in-VPC measure.

— 3.0.0_SA_CVO~Z
