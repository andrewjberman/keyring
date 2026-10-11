# /canonical-drive -- 2.0.0_SA_COO~M1 on dell1 -- 2026-10-08 01Z (through 02:0xZ)

Scope: MDPF_SECCLASS (DIRECTED, 10m). Lease FULL. RELEASE MODE.

| tick (UTC) | limb | outcome |
|---|---|---|
| ~01:0xZ | release | e65 + e66 ledgers CLOSED by ~S; e65b gate met for ~SD. CTO: e65 safe but UNEXERCISED (grade the cash outcome from e32's 316 rows) |
| ~01:1xZ | release | ~SD STOP on e57e61: stale staged_from pins would ship rivalfunds pre-port. Amendment 1 @5e6133f92b re-pins ONE member (CTO confirmed = its signed port) |
| ~01:1xZ | release | ai_leg_verify reads the NEWEST listing @0d91b0fa96 (~SC's midnight false-FAIL warning) |
| ~01:3xZ | release | e65b attempt 1 failed closed (aws.cmd found no CLI, 0 PUTs); MSTR fixed aws.cmd (62d57c9f73). TO-AI-e32 amendment 4 @81e14f21bb: rollback input = ~SC's preserved copy (sha256 5fd655e06f0b4a0e) |
| ~01:5xZ | release | e65b retry HALF-LANDED (bd only; cot explicit deny), ROLLED BACK by ~SD in 115 s; row S68 @5681b29ee0; e65b HELD until Andrew item 2. CTO ADDENDUM 1 @0d520d9d70 -> seat-gate precondition in all 4 ~SD orders @32187cd38d |

Decisions closed this hour:
- A build that stages from pins proves the pinned bytes, not the worktree's. A re-pin moves only the signed member, and the built zip's
  members are checked before the upload.
- A multi-target deploy proves write access on every target, and honours a gate's STOP whatever the gate's mode, before its first write.
- A rollback's input is the one snapshot taken before the act's first write. It is never regenerated on another device.

Owed:
- ~SD: e57e61 apply, verified at the 14:00Z run;
- e65b once item 2 lifts the cot deny;
- e32 run 2 and e49 once the kimi grant lands;
- e42 L2 at 12:45Z (~S);
- round 12 (S60 first).
