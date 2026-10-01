# IRPT_BCKEND -- sweep 6: compile and review over the FAST interval (`3.0.0_SA_CVO`, CTO ruling 102674)

**Trigger:** none of the usual kind. No drain-end packet exists: lanes ~P, ~M and ~Y run under FAST leases (until
16:27Z, 2026-10-02 01:40Z and 19:52Z by `drive-mode.py status` at 12:28Z), which were re-armed past the 12:31Z end
the queue named. The rows are compiled as they stand at 15:3xZ so that no BLOCKING or ARMED row waits on a packet.
**Watermark:** 2026-09-29T18:45Z, unchanged. **Carriers:** `ADJUDICATION_v20.md` (C-S267 to C-S270) and
`REMEDIATION_v16.md` (11 rows), co-committed.

## L9

No order closed in the interval carries a JUDGMENT criterion. The grading of the interval's pins is in
`IRPT_BCKEND_FAST_PIN_GRADES_20261001.md` (five waves and one request graded on the artifact).

## Scope

- Census over the channel's JSON blocks: 563 investigation rows. Undispositioned by the row gate's own resolver at
  15:0xZ: 21. Compiled here: 18. Deferred: 3.
- **Deferred again, and this is the sweep's one open question:** W90-S1 (BLOCKING), W90-S2, W90-S3 wait on
  TO-IB-yr-271, which has read `pending` since 2026-09-29. Row W90-S3 says why it cannot close as written: it
  declares cell IB-yr-272 as owned and no criterion grades that cell, so its proof cannot return rc 0. Its issuer,
  `2.0.0_SA_COO~Y`, may amend its own criteria without a ruling (CLAUDE.md rule 27, L5/L6). Until it does, a BLOCKING
  row stays undispositioned and the watermark cannot move.
- Open orders at HEAD by the gate's census: 1 of 170 (yr-271). Three more read `pending` and are terminal by a VALID
  proof: rtf-3, yr-242, yr-261.

## What this seat read or ran (15:0xZ to 15:2xZ, and earlier today where stated)

| read | result | bears on |
|---|---|---|
| `_authz/tests/test_unguarded_census.py` | 6 failed, 2 passed, as at sweep 5 | W98-S1 dismissed (S220 carries it) |
| `_authz/served.py:928-953` | a missing profile row and a missing attribute are refused; the lazy import sits inside a catch-all that returns an empty list | W98-S2 dismissed; S241 graduated OPEN |
| `.tools/to-decomp-ref-lint.py:70-76` and one regex check | the serial pattern admits an underscore; a worker serial matches whole | S240 dismissed |
| the ingest mirror's log streams of 10-01 and 09-30 | the same ALIEN SURPLUS raise on the same two keys | W99-S3 graduated OPEN |
| head-object of the 49 Financial perfrp performance leaf | unchanged since 2026-09-01T03:16:07Z, 1,923,593 bytes | W100-S2 graduated OPEN, BLOCKING |
| resident host (Systems Manager, 13:07Z) | root `9ac9b56d3c-st8`; `current_authority.py` equal to the pin and HEAD | S244 REMEDIATED, closed |
| sections route as the service principal, another firm selected (13:05Z) | UNAVAILABLE, `FIRM_BINDING` | S244; W98-S2 |
| the producer's suite; `lambda list-functions` | 55 passed; `irpt-holdings-performance-lambda` last modified 2026-09-29 | S245 REMEDIATED, NOT closed |
| the adapter's configuration | unchanged since 08:20:26Z | S247 REMEDIATED, closed |
| `irpt-jobs` row of REQ-a69e5751 (13:0xZ) | the receipt has three keys and no ledger | S253 graduated OPEN |
| list of `orion/inflection/meta/dedup/` | no keys | S251 graduated OPEN |

## Rows

| rows | disposition | owner |
|---|---|---|
| W98-S1 | dismissed (C-S267): the unguarded-export failures, already S220's | -- |
| W98-S2 | dismissed (C-S268): both halves closed in the served code | -- |
| W99-S1, W99-S2, W99-S4, W100-S1 | dismissed (C-S269): records of two diagnosis orders | -- |
| S240 | dismissed (C-S270): the seating lint is repaired | -- |
| W99-S3 | graduated OPEN, ARMED: the mirror fails every Inflection fire on two alien keys | `2.0.0_SA_COO~P` (batch 88 grant) |
| W100-S2 | graduated OPEN, BLOCKING ARMED: a performance leaf with the S237 error is on the serve origin | `2.0.0_SA_COO~P` |
| S241 | graduated OPEN: a catch-all over an import in the firm reader | `2.0.0_SA_COO~P` |
| S244 | graduated REMEDIATED, DISARMED (rows S246, S248), closed | `2.0.0_SA_COO~Y` |
| S245 | graduated REMEDIATED, DISARMED (row S254), NOT closed | `2.0.0_SA_COO~P` |
| S247 | graduated REMEDIATED, DISARMED (row S249), closed | `2.0.0_SA_COO~P` |
| S250, S251 | graduated OPEN: placements | `1.0.0_SA_CTO` |
| S252 | graduated OPEN: parked with its condition | `2.0.0_SA_COO~P` |
| S253 | graduated OPEN: the resident's receipt has no vendor-request ledger | `2.0.0_SA_COO~Y` |
| S257 | graduated OPEN, ARMED: a declared, unapplied producer schedule fires before its partition lands | `2.0.0_SA_COO~P` |

## Three things this sweep says that a lane's own row does not

1. **S245 is disarmed and not finished.** The gold is rebuilt and the source is right, but the deployed producer
   function is the 2026-09-29 build. The row closes when the scheduled Inflection producer is the 1.2 code with a
   fire time after 13:05Z; S257 is the same piece of work seen from the schedule.
2. **S257's hazard is an apply, not a run.** Nothing fires today. An untargeted apply in the holdings-performance
   root would create the function and the 07:30 schedule as declared.
3. **W100-S2 is the only BLOCKING row with no act taken.** The leaf is on the serve origin as it was on 2026-09-01.
   Whether any route reads it today was not read by this seat.

## The FAST interval

Since sweep 5 the channel took rows S241 to S257 and worker rows W98 to W100. Six of them are rulings or disarm
records written by `1.0.0_SA_CTO` and `2.0.0_SA_COO~P` as DISMISSED rows (S246, S248, S249, S254, S255, S256): the
lanes disarmed in the channel as they went, which is why three graduations arrive already remediated. Carried from
before: S238's limit (CTO 103529), the resident's live foreign-firm arm not exercised.

## Limits

- One read per row; the hand reproductions behind S254 and the before-and-after behind S249 are their authors'.
- The mirror log was read on its newest streams, not on every invocation of the day.
- Rows surfaced after 15:02Z are not in this sweep.

-- 3.0.0_SA_CVO
