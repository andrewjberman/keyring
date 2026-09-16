# /self-drive MDPF_TAXSMA,NFRA_OPLGTW,LGIC_NAMING,LGIC_ENFORCE,LGIC_CANON -- ticks 6-7 (2026-09-15 ~22:1xZ to ~22:2xZ)

state: ARMED | cadence 30m (CronCreate e5ff987a) | carrier org/XXX.md @6cfec7a785 | adjudicator: 1.0.0_SA_CTO.

Tick 6 was quiet: no call; disk held at 21G after 2.0.0_SA_COO~G removed the 10 approved worktrees (97253); all five
projects are EXECUTING and ADMITTED; CAPACITY is 3 of 3.

## Open calls in scope: 1 ADJUDICATED (MDPF_TAXSMA, 2.0.0_SA_COO~T 97254); 0 RESERVED

**CALL 7 -- TX-p-1: TXP1-AC7's host census (ssm send-command) contradicts TXP1-AC10 (read verbs only).**
- Row MDPF_TAXSMA-W6-S1 records it. The worker refused to reword either criterion and left the order pending; 9 of 10
  criteria pass.
- REC (2.0.0_SA_COO~T): (A), amend AC10 by name.
- RULING: (A). AC10 becomes "a read verb, or AC7's ONE ssm send-command" under four conditions:
  1. one AWS-RunShellScript command, on the Gateway host only;
  2. a read-only script, recorded with its sha256;
  3. the command id and final status logged;
  4. SSM's own bookkeeping recorded, and no app path changed.
- Every other call keeps AC10's full check, and AC10 is re-run alone with no new AWS act.
- (B) is refused because it is a round-closing defect; (C) is refused because it is unmeetable.
- Guidance, not a ruling: TX-r-1's release builds from each Lambda's deployed pin plus MDPF_TAXSMA's own commits, so
  another project's unreleased Gold changes (TXP1-AC2) never ride along. If they must, the ledger entry and the
  never-widen sign-off name them.
- Sent to 2.0.0_SA_COO~T this tick.

COMPLETION TEST: NOT DONE -- 0 of 5 projects read `status: complete`.
