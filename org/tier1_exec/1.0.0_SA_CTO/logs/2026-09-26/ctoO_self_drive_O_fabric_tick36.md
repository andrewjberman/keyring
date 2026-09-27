# /self-drive ~O fabric -- ticks 33-36 (2026-09-26 20:35Z - 22:18Z)

- Driver `1.0.0_SA_CTO~O`; arming record `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d; cron 8abcafba.
- state: ARMED.

## Calls
- In scope, adjudicable here: none.
- At Andrew (carded in /open-calls at ~21:1xZ):
  1. BLOCKING: re-seat NFRA_OPLGTW's CTO and CVO legs to ~O on his word (the laptop release asked at 04:58Z is
     unanswered). Gates MCPORTAL C6 and OPLGTW's v1.2 ratification. REC yes.
  2. CARRIED: whether D9 as a whole moves to site Z. REC (a) no; the per-project fields carry the placement.

## OA-g-2 (the portal-grant gateway release)
- Tick 35 reported "GO did not fire". **WRONG**, corrected by COO~O's file 220015Z. The GO fired: gates re-measured
  21:12-21:15Z; "deploying" posted 21:25Z (MSTR file 212516Z, agentbus 0485c480); worker spawned ~21:26Z. Its first act
  is merging CLOUD into wk-NFRA_OPALAI-9. The ledger opens after that merge.
- Why the read missed it: it looked at `ls-tree HEAD` of the worktrees and the release-branch tip. An act still inside
  an uncommitted merge is invisible to both.
- At 22:18Z the merge in `C:/tmp/oa-9` is still open. The shared-tree corpus is clean (`surprise-corpus-validate.py`:
  123 documents, 5090 rows, 0 new failures), so the hold is specific to that merge's index. COO~O is retrying; nothing
  on the instance has been touched.

## Other fabric movement
- `0.7.0_AE_CloudOps~I`: MX-s-4 step 2 fixed @4b3a757410; row NFRA_MCPINDEX-Z-S15 @b629459239 (MX-s-4 step 3's premise
  was wrong); the step-4 spec @7f2e82d758 says DO NOT BUILD YET; Andrew-direct "rec a approved" recorded @4d2fb2996f
  (one ad-hoc fire of the existing Black Diamond producer).
- `2.0.0_SA_COO~O`: MX-s-6 issued and MX-s-4 amended on Z-S15 @3e972dac5d.

## Completion test
NOT DONE: 0 of 4 `complete`. Reachable 4 of 4.

## Compiler Tools
`python .tools/surprise-corpus-validate.py` (OK, 0 new).
