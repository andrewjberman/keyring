# SELF-DRIVE laptop directives -- ticks 25-26 (2026-09-27 ~00:49Z and ~01:22Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since tick 24 (@`4e0668af34`, ~00:28Z). **State: ARMED.**

## Scope

9 laptop directives of 15 live. IRPT first: IRPT_BCKEND and DSGN_IRPTV1, both active / EXECUTING. Unread at the tick: 0.

## Acts (1.0.0_SA_CTO lane)

1. **FAST leases** IRPT_BCKEND~M, ~P and ~Y re-armed for 12h, until 2026-09-27T12:49Z. The surfaces are unchanged.
2. **Window 6 ruling on 2.0.0_SA_COO~Y 101672** (@`a7692416e0`, in `deliverables/SIGNOFF_UI_WALK_W6_20260926.md`):
   - verified at `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py:274-281`:
     `principal("start")` re-grades the submitter's CURRENT profile before claim;
   - branch (e) is struck, so a UI-walk window keeps its principal until every job it started is terminal;
   - job `REQ-3a1b73a8`'s residue goes to ~P at DLQ time (a packet amendment if the row stays non-terminal).
   - Messages sent: to ~P at 00:53:01Z, to ~Y at 00:53:16Z. ~P recorded S150 as DISARMED @`51d0f0fdee`.
3. **Watcher:** the inbox watcher re-armed twice on expiry.
4. **/overview DSGN_IRPTV1 for Andrew:**
   - The UI review brief `fd463341e3` (UIR-01..49, plus UIR-50) reached ~D, and the coverage check reads 50 of 50.
   - Round 7 was issued @`f56587bf9e`: 7 of 9 orders complete. IV-e-43 (colours) and IV-e-45 (face batch) are
     pending, last on their chain by design.
   - Direct acts IV-e-46, 49 and 50 are pending.
   - 34 portal DEV commits are local only (origin DEV `c3dd9ca9`).

## Open calls in scope

One at Andrew (RESERVED, vendor egress beyond his stated word):
- **The call:** the receive-1 diagnostic wrapper run, a live YCharts headless session capture (S151, ARMED, owner ~Y).
- **Citation:** the arm covers "egress is permitted for API calls". A browser-driven vendor sign-in is not plainly an
  API call.
- **What it gates:** the next Analysis window (~P STATUS @`b561fb334f`).
- **REC:** yes to one wrapper run under the arm's ledger, no vendor write.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE (no members).

## Waiting on other seats

| seat | owes |
|---|---|
| ~P | job REQ-3a1b73a8's row read at DLQ time (due ~01:12Z, not yet reported) |
| ~D | IV-e-43, 45, 46, 49 and 50; the push of round 7 to origin DEV |
| 3.0.0_SA_CVO | round 7 L9 grades after the drain; the round-5 slug |
| ~M | Monday 09-28 runs; the R4 enable half |

## Compiler Tools

`drive-mode.py arm/status`; `sed -n` at the cited `resident_worker.py` lines; `irpt-ui-review-coverage-check.py`;
`git rev-list --count origin/DEV..DEV` (portal).

state: ARMED
