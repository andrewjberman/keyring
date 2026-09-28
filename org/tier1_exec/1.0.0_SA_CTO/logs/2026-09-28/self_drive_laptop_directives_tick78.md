# SELF-DRIVE laptop directives -- ticks 74-78 (2026-09-28 ~00:18Z to ~13:28Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 72-73 log (@`28f2bb280a`). **State: ARMED.**

**Gap:** this seat stalled on a usage limit from ~01:10Z to 12:35Z (Andrew, 12:35Z). The CRO and MSTR stalled over
the same span.

## Andrew-direct (this terminal, ~12:4xZ)

"The only classification table that matters is whatever ETFClassifier is connected to, the DDB table and associated infra
that feeds into the "Positioning" POSN page." / "THat is the canonical table." Record @`871b7458ec`.
- The canonical table is DynamoDB `etf-classifications`: 285 tickers, no firm-tagged attribute, owned by D4 POSN.
- **S173** (COT gold served equity 85.8% vs 52.5%):
  - the `bd-securities` grant is WITHDRAWN, and the CVO fork is moot. The CRO found 222 `firm_origin=inflection` rows,
    and the CVO filed S174;
  - ~M's coverage census: COT 179/847 tickers (39.7% of served $), BD 228/1,449 (68.1%);
  - the Holdings producer also reads `bd-securities`;
  - **ruled (a):** R4 goes today, because its classification source is unchanged. The re-point of all three producers
    to `etf-classifications` is ONE act with halves, AFTER the POSN owner fills the gap (668 COT + 1,221 BD tickers),
    relayed cross-fabric via MSTR;
  - ~M's COT cash-line act and Part 2 stay held.

## Rulings and halves

1. **irpt-status rebuild 2** (`5fSyChId`, served 00:02:49Z) failed live at window 20's K10. Two causes: no read on
   `original_holdings`, and a pin-skewed `errors.py` that turned owner-read refusals into 500s.
   - **Ruled: roll back.** It rolled back to `bMMJ` at 00:36:25Z (read back by this seat); the refusals are named,
     with 0 TypeError.
   - **Rebuild 3 ruled MINIMAL** (102285 (a)): bMMJ plus two files plus the original_holdings grant; my 102269
     shared-module list is withdrawn.
   - **CTO half @`472a6d0d94`, CONDITIONAL** on ~Y's gates 3 (role sim) and 4 (REQ-67 READY on the built zip) before
     apply. The CRO signed the same condition.
2. **Export receipt RUNNING per R11:** CTO @`072b8d8e86`, CRO @`4a28382f7a`. Apply after the freeze, with a LIVE
   before-read.
3. **Comparison GRANT release** (generate AdE17rT6, resident st2): CTO @`2ad6fdb05d`, CRO @`e60a5043e8`. Named: no
   false foreign-firm refusal of a firm's own name.
4. **Window 20** (K10 only): CTO @`519ab8bb5c`, CRO @`802c8fb54d`. Run: K10 got 500 on 5fSyChId, which the rollback
   above answers.
5. **The cited-hash scare** (CRO "O1Vu8CyD" vs packet "BORQ2shb") was the S3 version of the same artifact. No
   discrepancy.

## The S19 purge

It did NOT run at 03:00Z (MSTR stalled). It is running now on Andrew-direct "Purge now, then push":
- the freeze began 12:50Z;
- it narrowed at 13:27Z (MSTR 102330): local commits are legal, pushes are frozen until CLOSE.

## State

- C: has 25 GB free, so round 9 has worker room again. The Downloads card is retired.
- Local CLOUD is ahead 631 / behind 419 of origin: unpushed laptop work. MSTR integrates after the purge.

## Open calls at Andrew

1. CARRIED: Schwab's registration-code list (UIC-16).

## Completion test

NOT DONE: 0 of 2 IRPT projects are complete (both `active`). D10 is UNMEASURABLE (no members).

state: ARMED
