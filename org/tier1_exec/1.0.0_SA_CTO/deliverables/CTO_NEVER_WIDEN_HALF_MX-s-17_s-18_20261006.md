# CTO never-widen half -- NFRA_MCPINDEX MX-s-17 + MX-s-18 PHASE B -- SIGNED 2026-10-06 ~21:2xZ (was HELD)

- **Seat:** 1.0.0_SA_CTO~O, 2026-10-06 ~19:0xZ.
- **Ask:** `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-s-17_s-18_20261006.md`
  @27501e83dd (msg 30199). The COO half is SIGNED there.
- **State: SIGNED** (section "SIGNED" at the end). Earlier state, kept for the record: HELD, not SIGNED and not REFUSED. The technical review below is clean. One scope question goes to Andrew
  first, because this seat does not adjudicate the scope of his word.

## Why HELD

Andrew-direct 2026-10-03 ~17:3xZ, at the 2.0.0_SA_COO~H terminal, verbatim: "We have permissions in place, it is
inappropriate for agents to adjust our data engineering operations without my explicit directive."
Record: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261003_17xxZ_RELEASE_ALL_QUARANTINE_NO_DATA_OPS_CHANGES_WITHOUT_DIRECTIVE.md`.

- The word was given in AMGT_HARVST's context, but its sentence names data-engineering operations generally. A
  reading that covers other projects is plausible: the laptop CTO treated it as a named hold on the
  mdpf-daily-runner restart (`ANDREW_DIRECT_20261005_030xZ_ALL_RECS_APPROVED_SELF_DRIVE_SEAT_ADJUDICATES_OPEN_CALLS.md`,
  card 2).
- These acts change BD production data operations: two SSM documents repointed, the bd-49f-runner's completeness
  logic, and one IAM statement.
- Their authority predates the word: round-6 analysis @361b186c92 (2026-10-02 01:02Z) and the round-7 issuance
  @9108f11494 (2026-10-02 02:40Z). Andrew's 2026-10-01 ~17:4xZ priority ("MCPINDEX ... first", msg 28000) names a
  priority, not these acts.
- CLAUDE.md section 2(b): when a wider scope is plausible, ASK. The question is put to Andrew as one card.

## Technical review (would SIGN on his yes, at these pins)

1. **Documents (s-17):** the diff at `wk-nfra_mcpindex-r7-24` (vs @9108f11494) changes exactly three lines,
   `scripts/` -> `code/silver/`. Re-read 2026-10-06 ~18:5xZ:
   - the served `code/silver/merge-daily-incremental.py` md5 is `91eaf2486fc56ece76db2f0d862096f7`, equal to pin 0;
   - the script imports no `lib` module;
   - `code/silver/lib/config.py` and `scripts/lib/config.py` resolve the same `S3_BUCKET`.
   So the lib repoint is inert.
2. **Writers:** 2 per property (`silver/transactions/`, `silver/realized/`): the documents and `bd-silver-merge`.
   - After s-17, both writers run one script, so s-17 must land before s-18. The ask orders it so.
   - Gap days: the write moves to ~00:1xZ, with identical bytes; the 21:5xZ document run then ETag-skips.
   - The one behavioural difference is the ETag re-process of a same-name re-land, and the ask names it.
3. **Runner (s-18):** `_emit_sentinel` fails closed. A missing, -1 or inferred sidecar, or any non-transactions
   table at 0 rows, withholds the sentinel. A failed read-back raises. The shared `data/cot/` module is unchanged.
4. **IAM:** the statement is NOT yet authored on the branch. This half would admit exactly one statement:
   - Effect Allow, Action `s3:GetObject`, Resource `arn:aws:s3:::opal-data-bd/bronze/*/_BRONZE_COMPLETE.json`;
   - nothing else changes in `bd-49f-runner-policy`;
   - the printed plan diff shows that statement and reads 0/2/0.
   The runner already holds PutObject on that key, so no firm boundary moves.
5. **Failure branch:** a runner deployed without the grant raises nightly, and Lambda's 2 async retries re-pull from
   Black Diamond. The ask's same-session rollback (code first, then policy) bounds this.

## Andrew's answer (2026-10-06 ~19:4xZ, at the 2.0.0_SA_COO~MI terminal; msg 30258)

Record: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261006_194xZ_BD_CONSOLIDATE_WRITERS_INVESTIGATE_SHAPE_FIRST_SEAT_AE_MI.md`
@89ef943035. Verbatim, in part: "Yes we can consolidate writers. I need you to investigate first. ... we need to
confirm the shape first before making that move."

- **This half stays HELD.** His order of acts:
  1. the shape investigation, read-only (order NFRA_MCPINDEX.TO-MX-a-1, seat 0.7.0_AE_CloudOps~MI);
  2. the evening run's decommission, if the investigation finds it extraneous;
  3. the round-7 BD chain.
- The pins above are NOT signed now. If the evening documents are decommissioned, MX-s-17's repoint is moot and
  the ask changes.
- This seat signs a fresh or re-pinned ask after the verdict, at the bytes of that day. The technical review above
  carries only as far as its pins still hold.

-- 1.0.0_SA_CTO~O

## SIGNED -- 1.0.0_SA_CTO~O, 2026-10-06 ~21:2xZ (ask msg 30316)

**Why it can be signed now.** Andrew's order of acts put the investigation first. It is done:
`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/BD_RUN_SHAPE_COMPARISON.md` @b4e1284fad.
- The evening run fetches nothing from Black Diamond.
- It emits no field the morning path lacks, and its transactions output lacks `cusip`.
- It is still the only same-day merger on sentinel-withheld days.

So his "Yes we can consolidate writers" applies. MX-s-18 is what makes the evening run extraneous as a scheduler,
and MX-s-17 puts both writers on one script for the interim. The decommission (MX-s-19) is NOT in this half.

**Pins, re-read by this seat at 2026-10-06T21:19:43Z (4 of 4 equal to the ask's section 0):**
- both SSM documents Default 3 = Latest 3, Active;
- `bd-49f-runner` CodeSha256 `q37ovM/F07p39ObyY6bML9tmIEXDN1S/OhyJv1oDH00=`;
- `code/silver/merge-daily-incremental.py` ETag `91eaf2486fc56ece76db2f0d862096f7`, 59,820 B.

**Signed for:** the acts of the ask's section 1, in that order (s-17 first), and the blast radius and rollbacks of
its section 2. The executor is `0.7.0_AE_CloudOps~MI` (A2 @2c8d840b67, A3 @5017a9cc7f), on branch
`wk-nfra_mcpindex-r7-24` @3709ae40d6.

**Conditions (each voids this half if unmet):**
1. The ask's BASE-MOVED CLAUSE: PHASE B re-reads every pin at its first act.
2. The IAM change is exactly one added statement, and the printed plan diff shows only it:
   - Effect Allow, Action `s3:GetObject`, Resource `arn:aws:s3:::opal-data-bd/bronze/*/_BRONZE_COMPLETE.json`;
   - the plan reads `0 to add, 2 to change, 0 to destroy`.
3. Both branches as the ask states them. In particular: a read-back simulate that is not `allowed` after the apply
   rolls back BOTH keys in the same session, code first.
4. No rule is disabled, and no document or Lambda is retired, under this half.

GO to the executor is the issuer's.

-- 1.0.0_SA_CTO~O
