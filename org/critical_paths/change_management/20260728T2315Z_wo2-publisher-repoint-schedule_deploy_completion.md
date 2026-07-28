# Deploy: wo2-publisher-repoint-schedule

**Opened:** 2026-07-28T23:15Z by 0.7.0_AE_CloudOps · **Authority:** MDPF_RESET WO-2 (Andrew ~2157Z
element 2/3; CTO 230156Z ladder item 6; COO co-sign 221211Z scoped `platinum/mdpf/*` ONLY).

Re-point both publisher legs (derived gold read → live platinum serve write), egress role swap
(old fenced role attached to nothing), co-sign var flip, own 16:15Z daily schedule (reasoned in
TF), PIN-4 event log + R7 `_provenance` stamp from birth. Legs L1–L4 in the ledger JSON.

**The open item no clean run closes (COO, binding):** "on schedule" closes only on the first
unattended 16:15Z fire, expected 2026-07-29. A publisher only ever run by hand is never
reported as scheduled.

## Completion

**CLOSED 2026-07-28T23:22Z.** L1 `94952ba865`+`5579fc381c`. L2 apply 4add/1change, 0-diff, live
role/env/schedule verified, tag `opal-assets-v0.35.0`. L3 battery: live-serve reaches exactly
`platinum/mdpf/*`; isolated sims allowed/implicitDeny/allowed; D-controls unmoved + behaviorally
exercised. L4 invoked once 23:20Z: 11/11, **written set ≡ pinned set `d6c9562318` both
directions**, provenance stamped, legacy keys untouched.

**OPEN (by design, no clean run closes it):** "on schedule" closes only on the first
UNATTENDED `cron(15 16)` fire, expected 2026-07-29 ~16:15Z — self-evidencing via the PIN-4
event log (`source=aws.events` + rule ARN in the payload).
