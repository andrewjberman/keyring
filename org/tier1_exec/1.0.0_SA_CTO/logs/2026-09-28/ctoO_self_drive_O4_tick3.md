# /self-drive ticks 2-3 -- ~O fabric, four projects (1.0.0_SA_CTO~O)

**archetype:** COORDINATE

- Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md`
  @7612f001c4. Cron `0eef1ea2`.
- Ticks covered: 2 (22:45Z, quiet line in the runtime file) and 3 (23:13Z). **state: ARMED**

## Scope at tick 3

| project | status | dep_stage | open TOs (t1 -> t3) |
|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 14/50 -> 14/50 |
| NFRA_OPALAI | active | EXECUTING | 15/30 -> 11/31 |
| NFRA_MCPORTAL | active | EXECUTING | 3/18 -> 3/18 |
| NFRA_MCPINDEX | active | EXECUTING | 4/64 -> 3/64 |

Open orders fell from 36 of 162 to 31 of 163. Inbox: 0 unread at each tick start. Sequence: no flags on any in-scope
project, after `1.0.0_SA_CTO~Z` fixed the fabric drift @2bed2ad08b.

## Calls closed on this seat's REC (call routing; none was a design or governance fork)

| call | ruling | record |
|---|---|---|
| G-ACCT step 3: enable WinRM, or probe another way | Probe as Opal_Agent via Start-Process -Credential (OA-f-4). No WinRM: it adds a standing listener. A launch failure reads ERROR. | @21f17e26e3 |
| Andrew speed test: option (a), his own portal-only grant | WITHDRAWN. COO~AI measured that a profile strips his non-Schwab tools and that revoking it leaves a tombstone. Option (b) applied instead. | @1d0ca61992 |
| NFRA_MCPORTAL closer candidate (obligation 8) | DECLINED on COO~MP's REC. Every hop is built, and the rest is G-SUB and G-CLOSE, both Andrew's acts. | msg to ~MP 23:07Z |

## Acts in this seat's own lane

- **G-A** (s.8.1 G1-G8) SIGNED for opal_discover and portal_index at pin 2dedae93df, @0d9f28d8f9. The G5-G7 live
  cert is the CVO's, after the enable.
- **MX-r-4 never-widen, CTO half** SIGNED @e3fd90cb63. The second half is SIGNED by `3.0.0_SA_CVO~O` @a491adda5e,
  adding GO guard N1: the mcportal re-ship is DELTA=0 only at a3bff71.
- **Shared-tree drain merges:** two conflicted merges from 2.0.0_SA_COO~AI's drain loop blocked every commit for
  about 30 minutes. It was nudged twice; it aborted the leftover and now pre-merges in the worker worktrees (26272).

## Verdicts from CVO~O

0 pitched and 0 received. No governance fork was open.

## At Andrew

- The switchover acts: the Analyst sign-in at setup-token, and one MFA. MSTR~Z runs the rest, and step 3 waits on
  OA-f-4.
- His `sub` value (Part D step 7), which is G-SUB for MCPORTAL MP-a-2.
- Alyssa posting Q1-Q3 for his speed test (card option b).

## Completion test

NOT DONE: 0 of 4 complete. REACHABLE 4, UNREACHABLE 0.

## Compiler Tools

- `sequence-check.py --project` x4: flags none.
- A Python census of the order files' last `<status>` tag: 31 of 163 open.
- The pin census at signing: `git -C /c/tmp/mx-rel3 diff --stat 6a98a0553a HEAD` shows 5 files, +113/-10, and the
  catalog diff adds 0 `s3_key` lines.
- A forked sub-run ran the G-A arch-gate: `validate_integration_spec` in-process, `register_enabled(mcp, [])`, and a
  live `aws iam get-role-policy`. It worked.
- The gap: `safe-commit` has no wait-for-merge mode, so commits during a peer's drain loop needed a hand retry loop.
