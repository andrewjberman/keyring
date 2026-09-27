# SELF-DRIVE laptop directives -- ticks 27-28 (2026-09-27 ~01:48Z and ~02:18Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 25-26 log (@`6e795f1658`, ~01:22Z). **State: ARMED.**

## Scope

9 laptop directives of 15 live. IRPT first: IRPT_BCKEND and DSGN_IRPTV1, both active / EXECUTING. Unread at the tick: 0.

## Andrew-direct

- **~02:0xZ, verbatim: "yes on the YCharts wrapper run, one run".** Record @`60ffa353f1`; relayed to ~Y and ~P.
  - ~Y ran it at 02:02:13-25Z (SSM 29cacb70, rc 0): authenticated, a fresh session at fence 13, no retry, no vendor
    write.
  - The ledger was opened @`b778f918a2` and closed @`a679a32e4b`.
  - S151 DISARMED: receive 1's failure was transient and unmeasured. The retained-reason patch names any recurrence.

## Acts (1.0.0_SA_CTO lane)

1. **Window 6 amendment 2** (~P 101677, blob `e78f5c58`) SIGNED @`c8ac86dff0`: job REQ-3a1b73a8's row is left alone.
   Named item: the release test-data item names that row by key.
2. **IV-e-49 commodities colour** (~D 101679) RULED (b): a chromatic PALETTE token, not gray900 (the text ink, UIR-37).
   ~D cut TO-IV-e-51 @`8f12e8662f`; complete @`1e639572dd`; drained @`d6b66c7899`.
3. **COT cash line / S152** (~M 101683): the fix rides Monday's act after R1, on five terms (addendum 4 @`17da02639a`).
   - CRO 101687 asked that it ride ALONE. The CTO concurred.
   - ~M re-cut it @`ff63895521` (the list, its test and the gate-forced future import). Addendum 5 @`7eb19f44e3`: the
     re-cut stands without a re-open.
   - Read-back tolerance: at most $0.02 (0.01 per added class), with the total exact.
   - The CRO signed the re-cut @`267b5d8db3`.
4. **Cross-viewer title binding** (~P 101690, blob `474495c0`): CTO half SIGNED @`e0423ca880`.
   - Named: the resident moves FIRST, then generate, on a 0/0 queue; roll back in reverse.
   - The CRO half SIGNED @`0cc18ec6e3` and added a refusal arm plus a paired rollback.
   - ~P opened the ledger @`457bb18c5b`.
5. **Watcher** re-armed on each expiry.

## Open calls in scope

None. S151 was the only card at Andrew, and it is closed on his word.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete (IRPT_BCKEND, DSGN_IRPTV1 active / EXECUTING). D10 is UNMEASURABLE (no
members).

## Waiting on other seats

| seat | owes |
|---|---|
| ~P | the cross-viewer swap (resident then generate) and its served-after proof; the next Analysis window, now unblocked |
| ~M | Monday 09-28: R1, then the COT cash-line act with S152 riding alone |
| ~D | IV-e-43, IV-e-45 (amended @`baf7a216bc`), IV-e-46, IV-e-50; the push of round 7 to origin DEV |
| 3.0.0_SA_CVO | round 7 L9 grades after the drain; the round-5 slug |

## Compiler Tools

`git hash-object` against `git rev-parse <pin>:<path>` (packet blobs); `git diff CLOUD...<recut> --stat`; `git show` at
the cited lines; `drive-mode.py status`.

state: ARMED
