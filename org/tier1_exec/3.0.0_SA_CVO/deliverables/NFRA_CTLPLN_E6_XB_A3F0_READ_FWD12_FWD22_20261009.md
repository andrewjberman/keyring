# NFRA_CTLPLN E6 -- XB-20261008T203134Z-a3f0 read against FWD-12 and FWD-22 (round analysis ROUND_ANALYSIS.20261009.md, row E6)

**archetype:** VALIDATE

## Reading: XB-a3f0 does not evidence FWD-12 or FWD-22; it evidences FWD-3's cross-box mechanics only

The timeline, from the records at box/laptop HEAD:

| UTC 2026-10-08 | Act | Record |
|---|---|---|
| 19:41 | Andrew answers "Yes do it" at the laptop, for the laptop's own leg 2 of `IRPT_BCKEND.TO-APPLY-E6` (one S3 delete) | 39ab7ddd70 (2.0.0_SA_COO~C amendment; CTO msg 107163) |
| 19:42:21 | dell2 opens open-call row `dell2-20261008T194221Z-2cf8` | `org/devices/state/dell2/open_calls.json`: asked_by 0.7.0_AE_CloudOps (the laptop's applier), source the laptop task order, subject "... laptop leg 2" |
| 20:31-21:00 | dell2 opens XB dell2 -> laptop "ANSWERED by Andrew"; the laptop ACKs by bus id; both sides close | d5e4a6654b, cac6808afe, 45399791dd, 0724357fd9, 1c4acb766b |

- **FWD-12 is not shown.** Its DONE WHEN is "a decision raised on another box answered by Andrew from the laptop", and its ACCEPT
  says "his answer there reaches the box that asked". Here the decision was the laptop's own act. The laptop's seat asked it and
  the laptop's applier ran it. Andrew answered it before dell2's row existed. The cross-box message then ran dell2 -> laptop as a
  closure notice, so no answer travelled from the laptop to an asking box. And as the analysis says, the laptop's one list
  (`open-calls.py list --all --cloud`) is not shown being read.
- **FWD-22 is not shown, on either arm.**
  - Arm one, a decision settled by one box's CTO and never shown to Andrew: this decision was Andrew's (an S3 delete).
  - Arm two, a two-box decision agreed between the managers and read from both sides: nothing was settled between the boxes. The
    record closes a row both sides already knew the answer to.
- **What it does show:** FWD-3's mechanics, which the analysis already credits (row FWD-3). A cross-box record has a bus send, an
  agent-side ACK by bus id, and CLOSED-BOTH, and each side's commits read the same state.

## The deliberate exercise that would grade them (recommendation, not a cut)

- **FWD-12:** dell1 or dell2 raises a decision that only Andrew can make, about an act on that box. It appears in
  `open-calls.py list --all --cloud` on the laptop, where Andrew reads and answers it. The asking box's row then reads the answer
  through the bus before the box acts, and nobody relays it by hand. The negative arm: the same box's lane does not sit waiting at
  its own terminal.
- **FWD-22:**
  - Arm one: one decision that touches only dell2 is settled by `1.0.0_SA_CTO~DELL2` and does not appear on Andrew's list.
  - Arm two: one decision that touches dell2 and the laptop (for example a shared Terraform root both deploy to) goes MSTR to MSTR
    as a file with an ACK, and is read afterwards from both boxes.

-- 3.0.0_SA_CVO
