# /self-drive NFRA four -- ticks 10-11 + REACHABLE classification (1.0.0_SA_CTO~O, site Z, 2026-09-29 23:20Z-23:5xZ)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4

## Measured

- **Inbox:** 0 unread at both ticks. No scope commits by any other seat since 22:50Z.
- **Open TOs:** 12 of 180 (last-tag read). OG 4, OA 4, MP 2, MX 2.
- **Site Z push:** 41ba3f747f is still not on origin. The CLOUD push is held on 5 merge conflicts at Andrew.

## Completion test, with the section-4 classification

**NOT DONE: 0 of 4 complete. 1 REACHABLE, 3 UNREACHABLE.**

Correction: ticks 1-9 printed "4 REACHABLE" without classifying. This is the first per-member read against the blocking
records.

| project | class | why (from the project's blocking field) | the act that makes it reachable |
|---|---|---|---|
| NFRA_MCPINDEX | REACHABLE | MX-s-14 advances with no Andrew act: its L5/L9 legs are proven at the scheduled fires (2026-09-30 21:46/21:53Z; 2026-10-05 for the weekly legs, row Z-S61). MX-t-10 waits on the push. | n/a |
| NFRA_OPLGTW | UNREACHABLE | OG-g-1 waits on the G-C user (Opal IT); OG-v-7 on G-C + G-D (Andrew's controlled walkthrough); OG-t-2 on the switchover sitting's Part D record (Andrew, then 2.0.0_SA_COO~O); OG-v-8 on G-E + G-F. | Opal IT creates the unprivileged M365 user (Andrew is talking to IT); Andrew's G-D walkthrough and Part D sitting |
| NFRA_OPALAI | UNREACHABLE | all 4 open orders (OA-t-1, OA-t-3, OA-e-6, then OA-e-8) wait on G-ACCT step 5. | Andrew stores the Claude setup-token on Opal_Agent (his login) |
| NFRA_MCPORTAL | UNREACHABLE | MP-v-1 waits on G-2ND; MP-c-1 waits on G-CLOSE. | Andrew's sign-in as Opal Bloomberg (G-2ND); his grant narrow-and-widen with a named colleague (G-CLOSE) |

- **HELD-AT-STOP is not reached**, because the one REACHABLE member is not complete.
- It is reached if MCPINDEX's reachable work closes while its remainder waits only on the push, or when all three
  UNREACHABLE members stay put and MCPINDEX completes.
- The member set is not edited; the denominator stays 4.

## Calls

No open calls in scope (ticks 10-11).

## Acts only Andrew can do (each cited)

- The 5 CLOUD merge conflicts behind the site Z push (his shared-branch push hold).
- G-ACCT step 5 (his login). MCPORTAL G-2ND (his sign-in) and G-CLOSE (his grant change). OPLGTW G-D walkthrough and
  the Part D sitting. MX-t-11: his widening word for platinum/advi.
- G-C is external: Opal IT.

## Compiler Tools

- None beyond git reads, the task-order last-tag census and the project-JSON blocking reads.
