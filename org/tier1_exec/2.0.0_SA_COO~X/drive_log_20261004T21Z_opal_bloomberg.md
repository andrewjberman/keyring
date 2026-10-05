# /canonical-drive -- 2.0.0_SA_COO~X -- 2026-10-04 20Z-21Z (site Z, opal_bloomberg)

Loop: `/canonical-drive AMGT_CORPUS` 30m, re-armed after the 18:58Z site-Z crash on Andrew's "2.) Yes" (msg 29201, record
@3166fec43e; LIVE_ARMS row AMGT_FRIDAY).

| tick (Z) | project | limb | round | TOs | cells | act |
|---|---|---|---|---|---|---|
| 19:43-20:21 (relaunch work) | AMGT_CORPUS | L7 -> L8 | 35 | 3/3 + ak-4 | 4/4 | ak-4 SERVED act run whole after the crash (ledger `amgt-corpus-r35-ak4` CLOSED @66a15668e1); packet @f699518c86 to CVO~Z |
| 20:22 | AMGT_CORPUS | L8 | 35 | 3/3 | 4/4 | NO-OP: packet READ by CVO~Z 20:22:07Z |
| 20:48 | AMGT_CORPUS | L10 | 35 | 3/3 | 4/4 | NO-OP: CVO~Z slug @04ff86b965 to the CTO |
| 21:0x-21:5x | AMGT_CORPUS | L10 -> L6 | 36 | 0/3 | 0/5 | DRIVE FORWARD: round-35 analysis @02bbbc0208 (msg 29236) -> round 36 ISSUED @80717c897c the same tick; workers ~1 and ~2 spawned |

**Decisions closed this hour:**
- Round 35 closed: FWD-22 REALIZED (CTO analysis @02bbbc0208).
- Round 36's rectangle, issuer ruling: FWD-20's "reason where none is measured" needs an API field. `read_model` serves only the
  forecast reason. So item 1 became al-1 (API), then al-2 (page), then al-5 (WORLD redeploy, a pair).
- al-5's pair is HELD until al-1 drains. A code-only redeploy ships every change between the deployed pin and the new pin (round
  66 ap-4's CTO half, condition 1), so its blast radius is measured on the drain commit, never before. A redeploy AMGT_RESAPP
  round 67 may also owe is the one to ride, if one is owed.
