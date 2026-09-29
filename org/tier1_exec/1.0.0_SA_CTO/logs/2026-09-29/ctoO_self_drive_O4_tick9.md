# /self-drive tick 9 -- ~O fabric, four projects (1.0.0_SA_CTO~O)

**archetype:** COORDINATE

- Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md`
  @7612f001c4. Cron `0eef1ea2`.
- Tick covered: 9 (02:15Z). **state: ARMED**

## Scope

| project | status | dep_stage | open TOs | reachability |
|---|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 7 / 51 | REACHABLE |
| NFRA_OPALAI | active | EXECUTING | 6 / 34 | REACHABLE (steps 1-4 of G-ACCT done; steps 5-6 are Andrew's) |
| NFRA_MCPORTAL | active | EXECUTING | 3 / 18 | **UNREACHABLE (Andrew's acts only)** |
| NFRA_MCPINDEX | active | EXECUTING | 1 / 64 | REACHABLE (the MX-r-4 GO is ready) |

17 of 167 open. Inbox: 0 unread. Sequence flags: none.

**NFRA_MCPORTAL is classed UNREACHABLE** (COO~MP msg 26380). Its three open orders wait only on Andrew:
- MP-a-2 waits on G-SUB (his `sub` value);
- MP-v-1 waits on G-2ND (a sign-in as Opal Bloomberg);
- MP-c-1 waits on G-CLOSE (his sitting).
The card was surfaced to him once, in this seat's terminal report at ~02:1xZ. HELD-AT-STOP does not fire, because 3
REACHABLE members are not complete.

## Acts in this seat's lane since tick 8

1. **naming-gate `tf_local` read_context kind LANDED** @7610be987f. Laptop `1.0.0_SA_CTO` ruled it (102531) and read
   and APPROVED the patch (102538, sha256 757b22255336). Controls: 16/16 PASS.
2. **The authority record** for OPLGTW-LEGACY-READ-01 @a5aa8e92c8.
3. **The entry** OPLGTW-LEGACY-READ-01 in `org/standards/NAMING_LEGACY_READS.json` @e4ec197609: tf_local
   `advi_49f_chain_log_prefix`, occurrences 1, reference_count 3, cutoff 2026-10-06. Verified: `waivers_for()` on the
   frozen OG-m-2b candidate returns the waiver ("referenced 3 time(s) as reviewed"). The 2b re-ask went to COO~O.
4. **MX-r-4 re-ack** for deploy-only commit 0bce8d322a @6545af38ce. Its gateway tree object equals the pin's
   (09ccfc39ad). The CVO re-acked @f7d22e3e9e.

## Standing

- G-ACCT (from COO~AI's artifact read, 26383): the OA-f-6 ACLs are in force, and all 4 boundary arms read DENIED-OK
  on the real account. Step 4 is done, but its `claude mcp list` was EMPTY; it is re-checked before step 5.

## Verdicts from CVO~O

0 pitched. The CVO acts this span are signatures and re-acks.

## At Andrew

- G-ACCT steps 5-6: the Analyst setup-token sign-in and one MFA.
- G-SUB, G-2ND and G-CLOSE for MCPORTAL.
- Alyssa's Q1-Q3 post.

## Completion test

NOT DONE: 0 of 4 complete. REACHABLE 3, UNREACHABLE 1 (NFRA_MCPORTAL, Andrew's acts).

## Compiler Tools

- `sequence-check.py --project` x4: flags none.
- The order-file census: 17 of 167 open.
- `naming-gate.py` `waivers_for()` against the HEAD carrier on a detached worktree at 8340c65376 plus the frozen
  patch: WAIVED as reviewed.
- `git rev-parse <commit>:infra/aws/ec2/opal-gateway` on two commits: tree-object equality.
- The gap: a full worktree checkout took longer than 120 s. The next such check should use a sparse cone.
