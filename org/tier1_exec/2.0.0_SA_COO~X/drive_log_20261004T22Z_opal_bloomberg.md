# /canonical-drive -- 2.0.0_SA_COO~X -- 2026-10-04 21:3xZ-23:1xZ (site Z, opal_bloomberg)

| time (Z) | project | limb | round | act |
|---|---|---|---|---|
| 21:36 | AMGT_CORPUS | L7 | 36 | NO-OP: both worker lanes working |
| 21:4x-21:5x | AMGT_CORPUS | L7 | 36 | al-1 drained @98a93db70b. Worker ~1 could not be resumed, so slot ~1 was re-seated for al-2. al-3 drained @288de3d95d; slot ~2 torn down. al-5 COO half @cbf0800776 |
| 21:57 | AMGT_CORPUS | L7 | 36 | NO-OP |
| 21:58-22:0x | AMGT_CORPUS | L7 | 36 | al-5 CTO half SIGNED @95d297d418. al-2 drained @66edd940a7. The al-5 order to 0.7.0_AE_CloudOps~A was REFUSED by to-pipeline-gate (one issuance per round), so al-5 stays the issuer's act; al5_served.py @28f64aa921 |
| 22:1x-22:4x | AMGT_CORPUS | L7 | 36 | CTO review REWORK; the issuer merged DEV into the candidate (portal 75efe9d6), then APPROVED @60d69ec86e. Andrew's "rec approved" @40cd6d2680; DEV push by MSTR~Z, CI green. RESAPP aq-5 closed 22:27:41Z; al-5 run by the issuer, ledger opened @5907db84a4 |
| 22:5x-23:1x | AMGT_CORPUS | L7 | 36 | real page run @adebac9c47; al-5 regressions plus the cold c15 re-run; ledger `amgt-corpus-r36-al5` CLOSED @e2790c8b2b (Branch A) |

**Decisions closed:**
- **al-5's executor.** A fourth order file in round 36 is a second issuance, and the gate refuses it. The decomposition already
  named the issuer as the fallback executor, so the issuer ran it and did not take an override.
- **c15's first NO** read WARM containers (about 250 ms each). The function was idled 15 min and re-read cold: 3 of 3 at 1.9-2.4 s.
  That is not a rollback trigger.
- **instrument35 at 0/4 on the al-2 merge** equals DSGN's own recorded base reading (ROUND35_CLOSE.md:51). It is not a regression.

**Open:** al-4 is the issuer's read of the 2026-10-05 13:00Z fire, then the round-36 packet goes to 3.0.0_SA_CVO~Z.
