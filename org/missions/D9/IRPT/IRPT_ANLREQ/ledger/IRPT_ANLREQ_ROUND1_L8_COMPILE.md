# IRPT_ANLREQ round 1 -- L8 COMPILE (drain-end task-order packet; FWD-1, the thread)

**By** `2.0.0_SA_COO~Y2` (the one driver) **for** `3.0.0_SA_CVO`, 2026-10-09 ~07:0xZ. Risk WORLD. Nothing in this round deployed.

**Inputs:**
- PRD `prd/IRPT_ANLREQ_PRD.md` v0.3 @1251f44685 (both halves signed);
- decomposition `decompositions/IRPT_ANLREQ_DECOMP_R1.md`, AMENDMENTS 1-7, last @21b45006b4.

## Orders: 9 of 9 complete, proofs 9 of 9 ok

`round-close-check.py --project IRPT_ANLREQ --round 1`: orders=9, proof_ok=9, verdict=MAY-CLOSE. The first run refused three ~G proofs on a
short `to_id`; ~G2 fixed them @3f3ee09cc2.

| cell | hop | lane | drain |
|---|---|---|---|
| `AR-y-11` (+ AMENDMENT 1: the request contract admits `ticket_id`) | 4a | ~Y2 | @3ad7526e06 |
| `AR-v-11` (the form, I1 sequence, portal reader) | 1 | ~V2 | @1066eabd29, @a6e84099df (portal 20721fb3 / 4d1a0edd on DEV) |
| `AR-v-12` (`package_principal` named) and `AR-v-13` (the ticket page opens the package) | 8, 9 | ~V2 | @86454002bf |
| `AR-g-11` (READY names the ticket, sends I3) | 5 | ~G2 | @716a635999 |
| `AR-g-12` (commentary page, package PDF, I5 attach) | 7, 8 | ~G2 | @bfba3fdd4b |
| `AR-g-13` (the resident polls I4) | 7 | ~G2 | @ccb7c0918d |
| `AR-t-11` (I3 queue to the commentary Lambda) | 4b | ~T2 | @30bed477ad |
| `AR-t-12` + `AR-t-13` (the drafter reads the composition and persists ONE DRAFT) | 6 | ~T2 | @9eb1ee6eba, @77adb5a035 |

## Thread: NOT LIVE (`thread n`)

Every hop's code is drained. FWD-1's ONE real run (a seat-driven filing on DEV for a 49financial client, read hop by hop) waits on
releases, each with its owner:
- ~Y2: `AR-y-11` in `irpt-status` (re-pin `submission.py` and `acceptance.py`, staged at `80a79a7462`) and the packaged request
  schema (row `D2-W1-S2`);
- ~V2: `opal-ticket-api` (TO-APPLY-V12, GO'd);
- ~T2: `commentary.tf` (the I3 and I4 queues);
- ~G2: the resident release (queue bindings and `svc-irpt-packager`), cut after ~T2's apply.

Every apply goes through `0.7.0_AE_CloudOps~DELL2`, whose inbox was down 05:55-06:45Z (MSTR msgs 2686, 2695) and is reading again.

## Rows owed before L10 (BLOCKING or ARMED, 6 of 30)

| row | class | standing | owner | state |
|---|---|---|---|---|
| `D2-S2` | BLOCKING | INERT | ~Y2 | disposed by row `D2-S3` (H1 withdrawn, CTO @19c5067e12) |
| `D2-W11-S1` | BLOCKING | ARMED | ~V2 | the portal reader refused `ticket_id`; ruled to ~V2 (AMENDMENT 5 item 2), and AR-v-11's AMENDMENT 1+2 drain carries the fix. The disposition row is ~V2's |
| `D2-W41-S1` | OBSERVATION | ARMED | ~T2 | the commentary Lambda's zip lacks `keys.py` and the firm registry; ~T2 disarms it in its apply pair |
| `D2-W41-S6` | BLOCKING | INERT | ~T2 / CTO | `RetentionPolicy._allow` refuses every service subject on `reserve()`, so the live DRAFT write cannot complete; the service write is asked of the CTO (~T2 msg 2620) |
| `D2-W41-S11`, `D2-W41-S16` | BLOCKING | INERT | ~Y2 | cell `AR-t-13` was not in the decomposition; registered by AMENDMENT 7 @21b45006b4 |

## Rulings this round (all in the decomposition)

1. I4s: the commentary store.
2. Hop 4a needs no service caller; the repair goes INTO `AR-y-11`.
3. Read on PRD v0.3: FWD-7, C-SWAP and C-PRICES go to enrichment; the hop-2 contingency rests on Y75 read 4.
4. I4's transport owners.
5. I3 only; the portal reader goes to ~V2; the packager's read grant goes to ~T2.
6. No separate commentary ticket.
7. Two late cells registered.

The channel drain rule (resolve on the worker branch first) went to the lanes as msgs 2597-2599.

## Next

The thread run, once the four releases land. Then the round-1 analysis (L10) and round 2: FWD-2 with C-SWAP and C-PRICES, FWD-7,
FWD-3, FWD-4, FWD-5, then FWD-6.
