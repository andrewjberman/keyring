# /self-drive NFRA four -- ticks 4-5 + events (1.0.0_SA_CTO~O, site Z, 2026-09-29 19:49Z-20:3xZ)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4

## Measured

- **Tick 4 (19:49Z), tick 5 (20:20Z):** inbox 0 unread at each; open TOs 13 of 180 (OG 5, OA 4, MP 2, MX 2); 0 calls;
  0 verdicts; completion 0 of 4, 4 REACHABLE.
- **Paired halves, all running (broker, 20:2xZ):**
  - 2.0.0_SA_COO~O was executing OG-n-1.
  - 2.0.0_SA_COO~MI is on a no-op until the 21:38-22:00Z fires; t-10 is blocked on Z-W15-S5, the site Z push.
  - 2.0.0_SA_COO~AI (cron b1182d84) is BLOCKED-SOVEREIGN on G-ACCT step 5.
- Andrew's removal word b004af859a ("go ahead and remove the 13 worktrees") was given at 1.0.0_SA_CTO~Z for its 13.
  It is not read as covering this scope.

## Events

1. **19:28Z, 2.0.0_SA_COO~O msg 26674:** mp3-1 held the only copy of the grant-writer layer zip that OG-n-1 needed
   (measured: 1 of 49 worktrees). It was moved to KEEP @219a681671.
2. **20:23Z, 2.0.0_SA_COO~O msg 26693:** OG-n-1 is COMPLETE, drained @c72df75fce, with ledger nfra-oplgtw-gateway-eip
   CLOSED @473217c119. **This seat read it live:** `describe-addresses` shows 3.214.118.242 on i-07dccb1615503ac99
   (eipalloc-093d97376b28d2388), and `describe-instances` shows the same public IP, running.
   - **S45 disarmed:** row NFRA_OPLGTW-Z-S19 disarms NFRA_OPLGTW-S45 (no EIP, so every stop/start moved the egress
     identity), whose disarm_owner was 1.0.0_SA_CTO. REMEDIATION_v1's S45 row is the CVO's to move at L8.
   - **Worktrees:** mp3-1 returns to DISPOSE, and wk-oplgtw-14 joins OPLGTW's set. The removal set is 34.
- Open TOs after OG-n-1: 12 of 180 (OG 4).

## Calls

No open calls in scope (ticks 4-5). The S45 disarm is this seat's own act as disarm owner, not a call.

## Acts only Andrew can do (each cited)

- Yes to the 34 checkout removals (recursive deletion; CLAUDE.md Agent Autonomy).
- G-C: one new unprivileged M365 user (tenant admin). G-ACCT step 5: the setup-token on Opal_Agent (his login).
- MCPORTAL G-2ND (his sign-in) and G-CLOSE (his grant narrowing and widening). OPLGTW G-D: his walkthrough.
- Release the site Z push (his shared-branch push hold; MX-t-10 waits on it). MX-t-11: his widening word for platinum/advi.

## Compiler Tools

- `.tools/aws` ec2 describe-addresses and describe-instances, the live read behind Z-S19. Git plumbing for
  worktree-content checks (the zip census across 49 worktrees).
