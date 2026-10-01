# Drive log -- 2.0.0_SA_COO~RV -- 2026-10-01 09Z-10Z (opal_bloomberg)

**archetype:** COORDINATE

Scope: ETFS_RIVALS, round 3. The lease read FULL on every tick.

| tick | time | TOs t/T | outcome |
|---|---|---|---|
| 32 | 09:45Z | 4/6 | NO-OP. Slot ~1's served_delta_after: BASG 0/0 |
| 33 | 09:5x-10:1xZ | 5/6 | DRIVE FORWARD. The RIV-i-1 reopen drained (CLOUD 66b1800541); the d-4 COO half SIGNED @7a17b348a9; CTO~Z asked |
| 34 | 10:06Z | 5/6 | NUDGE. Ask 27732 read OFFER-EXHAUSTED (invisible to the recipient's probes) and was re-sent once |
| 35 | 10:1xZ | 5/6 | DRIVE FORWARD. The CTO half landed @44eb66268e; d-4 amendment 1 @e7b94e2fe8; d-4 SPAWNED on ~4 |
| 36-38 | 10:15-10:35Z | 5/6 | NO-OP. d-4 running gate 1 (the served-delta re-run) before any apply |

## Closed decisions

- **RIV-i-1 complete after the reopen.** G5 matches on a window-stable raw key, and AC1 and AC2 PASS.
  - The full served delta reads BASG 527/527 (0/0), with 7 funds at 0/0. Row Z-S8 is disarmed.
  - The residuals are ruled expected:
    - BIDD -2/+1, newest-capture (the supersede rule);
    - TSEL +6 and WCMG +1, own-prior-date (C-TRADE-SCHEDULE). The served daily stage's pairing goes to the round analysis (row
      W1-S27).
- **The d-4 pair.** The COO half was SIGNED with the served delta measured per fund. The CTO half SIGNED keys 1, 2, 3 and 5-8 and
  REFUSED key 4.
  - Key 4's floor of 1.00 was measured over 5 issuer funds, while `identity_coverage` grades every fund.
  - The home funds read 0.0, BASG 0.924 and SCHY 0.982, so the floor would have marked 4 funds not-updated and broken FWD-1.
  - The CTO also withheld the GQGU BQL request, which needs Andrew's vendor word.
- **d-4 amendment 1.**
  - Key 4 is not acted; the floor stays PROVISIONAL at 0.0, and the per-fund fractions are recorded for the analysis.
  - GQGU is withdrawn.
  - Gate 1 is inlined.
  - AC3 is amended: non-home funds at >= 0.90, home funds reported only.

## Self-disclosure

- I took the identity floor from the instrument the cell produced (`i1_identity.json`, 5 issuer funds), not from the population
  the guardrail grades (every fund). The CTO's refusal caught it. A floor has to be measured over the same population as its
  gate.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| `get_delivery_state` | read of the d-4 ask | OFFER-EXHAUSTED, so re-sent; the reply came 2 min later |
| `.tools/safe-merge.sh` + `rv_union.py` | the i-1 reopen drain | PASS |
| `round3/checks/d-4.AC3.py` | amended and re-dry-run | FAIL at base (no act record), as expected |
