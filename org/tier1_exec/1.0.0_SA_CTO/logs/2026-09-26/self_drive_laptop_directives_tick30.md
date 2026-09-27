# SELF-DRIVE laptop directives -- ticks 29-30 (2026-09-27 ~02:47Z and ~03:18Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 27-28 log (@`bdb5715ea7`, ~02:18Z). **State: ARMED.**

## Scope

9 laptop directives of 15 live. IRPT first: IRPT_BCKEND and DSGN_IRPTV1, both active / EXECUTING. Unread at the tick: 0.

## Andrew-direct (at 2.0.0_SA_COO~P, relayed as ~P 101717)

**~02:5xZ, verbatim: "yes to all three"** (record @`6039c2f680`):
1. the window-7 go;
2. ONE new INF Orion one-use Performance call;
3. ONE COT one-use re-arm, after INF.

## Acts (1.0.0_SA_CTO lane)

1. **Window 7** (~P 101707, blob `3ab51a52`): CTO half SIGNED @`c226ade7a3`.
   - Named: at create, before K1, re-read both served pins.
   - CRO half @`d9b4142aa6`, with the condition that K1-CRED lives only as long as a login needs it.
   - Ledger opened @`1de955abf2`.
2. **INF one-use arm + window-7 amendment 3 (K11)** (~P 101726, blob `3a68bb2d`): CTO half SIGNED @`1b9060e893`.
   - Named: safe-apply re-plans 0/1/0 with exactly the two env keys.
   - Named: an unspent arm is disarmed the same tick window 7's principal is deleted.
   - Named: INF before COT.
   - CRO half @`9567a7c0fd`: grade by the adapter log's Orion-call count (exactly 1); a preset miss is refused unspent.
   - ~P ARMED f0de098f at 03:07:25Z, env only, re-plan 0/1/0 (@`d8939a74ba`).
3. **/open-calls** at Andrew's request: none open at this lane (window 7 go given at ~P).
4. **Watcher** re-armed on each expiry.

## Open calls in scope

None.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE (no members).

## Waiting on other seats

| seat | owes |
|---|---|
| ~P / ~Y / ~D | window 7: K4 then K5 to READY, K10, K11 (the INF read); the principal is deleted only when every job is terminal (cap 120 min) |
| ~P | the COT one-use re-arm packet, after INF is spent or disarmed |
| ~M | Monday 09-28: R1, then the COT cash-line act with S152 alone |
| ~D | IV-e-45 (the batch cell); the push of round 7 to origin DEV |
| 3.0.0_SA_CVO | round 7 L9 grades; the round-5 slug |

## Compiler Tools

`git hash-object` against `git rev-parse <pin>:<path>`; `diff` of the window 6 and window 7 packets; `git log` of the
ledger entries.

state: ARMED
