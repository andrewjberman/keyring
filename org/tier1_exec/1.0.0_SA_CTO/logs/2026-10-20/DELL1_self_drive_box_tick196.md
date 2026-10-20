# DELL1 self-drive box -- tick 196, 2026-10-20 ~16:48Z (delta: password confirmed, device-trust cause, headful Chrome ruling, HARVST r99)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 16:48Z. Acked since tick 195: 8698, 8702, 8706, 8710, 8712.
- open_calls.json: 160 rows, 2 OPEN, both acts only Andrew can do.

## Acts and rulings
- **655e CLOSED.** Andrew confirmed by hand that the stored password works (CRO record @006a61e350).
- **The device-trust cause** (CRO HAR 5, @5610d79894):
  - The password 403 is device trust. ATT is earned by the cfa.fidelity fingerprint beacons, and a headless browser on a datacenter
    IP is scored untrusted.
  - The factor step is "Text me the code", sent to the ...3066 Quo line.
- **Andrew-direct ~16:30Z, the headful Chrome amendment** (CRO @ed4f2ad8b0): the agent goes first; real Google Chrome, headful; the
  Claude-in-Chrome plugin; the agent-driven login proven as the fallback.
  - Ruled @c618ca8c8c (`deliverables/CTO_RULING_NFRA_FIDUPL_HEADFUL_CHROME_20261020.md`).
  - Track A: Playwright with channel chrome, headful under Xvfb, with a persistent profile. One attempt.
  - Track B: plugin feasibility on the box, then one agent-driven sign-in, issued now through P1 to CloudOps~NFRA1.
  - A non-datacenter egress would be new spend, so it is Andrew's act, and it comes up only if both tracks are untrusted. Answered P1
    8712 (msgs 8713, 8714).
- **AMGT_HARVST round 99** (CVO slug 8706, ADJUDICATION_v94 @deb6bc6492, MAY-CLOSE):
  - The analysis @f6e9ee7ec4: the standing dossier refresh is MET on the live first fire (92 written, 3 guard stops, errors 0). The
    one-row guard STOP stays.
  - Round 100: name the BZLFY and TSM drops; a scheduled gold chatter rebuild (S67); drive the two unfired branches; a gateway
    test-list read before Wed 06:00Z.
  - Sent to W1. The four ARMED instrument rows went to MSTR.

## Scope state
- **NFRA_FIDUPL:**
  - FU-s-2 REPAIR 7 (real Chrome) and FU-s-10 delivery are pending; FU-x-1 is pending.
  - 0 objects under `fidelity/`. The 3 fetch rules are DISABLED.
- **AMGT_HARVST:** round 100 is at W1.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).

## Compiler Tools
- `open-calls.py close`.
- `describe-instances`.
- `list-objects-v2`.
- `events list-rules`.
