# SELF-DRIVE laptop directives -- ticks 31-32 (2026-09-27 ~03:49Z and ~04:19Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 29-30 log (@`04869f55ca`, ~03:18Z). **State: ARMED.**

## Scope

9 laptop directives of 15 live. IRPT first: IRPT_BCKEND and DSGN_IRPTV1, both active / EXECUTING. Unread at the tick: 0.

## Milestone

**INF's first signed-in Performance journey is DONE** (Andrew's call 2, ~P 101796):
- ONE Orion call;
- RPT-df47a1fc PARTIAL, retained;
- 7.98% for 2026-01-01..09-22 on the face;
- the pre-check was recorded 3/3 before the arm, and the ledger is CLOSED.

## Acts (1.0.0_SA_CTO lane)

1. **Window 7 outcome (~P 101740):**
   - K5 stopped ATTENTION VENDOR_READ_BACK_REFUSED;
   - K10 hit the missing request-list route (DSGN_IRPTV1-S18);
   - K11 was refused unspent (0 Orion calls).
2. **The INF plan end** passed through three rulings in about 6 minutes, each overturned by a better read:
   - 101742 re-cut to the "directory as-of";
   - 101748 (a): the page was thought to show Cottonwood's date;
   - 101756 (b): end = the served INF HOLDINGS as-of.
   ~D's HAR settled it: the page ends on the client's own holdings date, as CTO 101422 ruled. The CRO matched each
   step (addenda 1-3).
3. **R10** (@`54323a0fb5`, CRO card @`d356e26684`):
   - one page date (the holdings business date);
   - an exception label where a section cannot reach it (a round-8 criterion);
   - the 09-22/09-25 gap is holdings staleness, IRPT_BCKEND-S152 (~P @`d19a39fa3a`), fixed by R4.
4. **UIR-29 / UIR-27 (~D 101765/101766):**
   - (a) on both, per Andrew's acceptance lines: "$" page-wide with the client total once; Supervision and Advisory
     one click away;
   - ONE follow-on re-golden cell.
5. **The read-back poll fix (~Y 101762)** was accepted and shipped by ~P (resident `fe64236bbb-rb`, 03:41:53Z). The next
   packet names up to 12 status polls.
6. **Row id collision IRPT_BCKEND-S152** (~P on CLOUD vs ~M's branch): routed to ~M. ~X's four branch rows were
   renumbered S153-S156 @`92244581d2`, and the COT mix_views row is now S155.
7. **Window 8** (~P 101772, blob `e2462004`): CTO half SIGNED @`c42d47163d`.
   - Named: the arm-off pre-check evidence goes in the ledger before the arm.
   - CRO 101777: the pre-check compares account, start and end; a start-only re-cut stands.
8. **W8-2 WAF (~Y 101790):** ruled (c) bounded.
   - A 15 s backed-off poll.
   - A WAF challenge on a READ spends the job's ONE existing session_refresh, then resumes at the checkpoint.
   - A second challenge goes ATTENTION.
   - Offline proof before the next packet.
9. **COT one-use arm + K12** (~P 101796, blob `27434c70`): CTO half SIGNED @`cd91ef7c0e`.
   - I read the 1/1/1 at `retained.tf:152-192`: one exact-ARN COT session grant, and the INF grant destroyed.
   - Named: the end state is `approved_performance_plan = null` (0/1/1). There is no re-apply of the spent INF plan,
     and no live vendor-session grant is left.
10. **Watcher** re-armed on each expiry.

## Open calls in scope

None.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE (no members).

## Waiting on other seats

| seat | owes |
|---|---|
| 4.0.0_SA_CRO | the COT arm's second half |
| ~P / ~D | COT: pre-check, arm (1/1/1), K12 (ONE use), then disarm to null; window 8's close (cap 05:58Z) |
| ~Y | the WAF-recovery branch, proved offline, then the next Analysis packet |
| ~M | Monday 09-28: R1, then the COT cash-line act with S155 alone |
| ~D | the round-8 items (the exception label; the UIR-29/27 re-golden cell); the round 7 push |
| 3.0.0_SA_CVO | round 7 L9 grades; the round-5 slug |

## Compiler Tools

`git hash-object` against `git rev-parse <pin>:<path>` (packets e2462004, 27434c70); `sed -n` at `retained.tf`;
`python` over `irpt-ui-review-findings-20260926.json` (the UIR acceptance lines); `git log -S` for row-id history.

state: ARMED
