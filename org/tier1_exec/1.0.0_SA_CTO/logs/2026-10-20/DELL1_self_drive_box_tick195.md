# DELL1 self-drive box -- tick 195, 2026-10-20 ~16:18Z (delta: secret rewritten, username passes, password 403)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 16:18Z. Acked since tick 194: 8687, 8690, 8693, 8695.
- open_calls.json: 160 rows, 3 OPEN, all acts only Andrew can do.

## Acts and rulings
- **7708 CLOSED.** Andrew rewrote `fidelity/alongside/wealthscape-credentials` at 16:04:39Z (CRO 8687); 2 versions exist. P1 was
  told to rerun.
- **Attempt 6** (P1 8690):
  - The username step passes (redirect-info 200).
  - The password POST answers 403 "Not Authorized". One attempt was made and none repeated, because of the lockout risk.
  - Act row 655e: Andrew confirms the stored password by a sign-in by hand, and whether the account shows a lock or a new-device prompt.
- **CRO 8693** (`RESEARCH_20261020_NFRA_FIDUPL_PASSWORD_403.md` @46e04d7f64): the box call is structurally complete, so the
  credential is most likely.
  - Ruled: P1 builds a pre-flow fix on fakes. One live attempt runs only after Andrew confirms.
  - P1 8695 corrected the premise: the pre-flow DID run in attempt 6. P1 now builds an ATT cookie-name probe, plus an ATT-conditional
    pre-flow. Accepted.
- **Round 2 code:** all 6 FR orders are complete; FR-s-6 repair 2 (the accountList shape) merged at 16:00Z. The FU-s-10 fifth delivery
  closed with 13 files matching.

## Scope state
- **NFRA_FIDUPL:** FU-x-1 is blocked on 655e. 0 objects under `fidelity/`. The 3 fetch rules are DISABLED. The box is running.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **655e:** confirm the stored Wealthscape password by a sign-in by hand (his login).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).

## Compiler Tools
- `open-calls.py add` and `close`.
- `describe-secret` (dates only).
