# IRPT_DASHBD: CVO adjudication, round 122 (workstream B-49F, ~D2)

<sweep_watermark>2026-10-15T10:20Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T10:20Z, on msg 8229 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND122_B49F_DRAIN_END_20261015.md` @8b44e171cd, blob 7878b9d2e0). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Four orders (DB-b-246..249); DB-b-247 and DB-b-249 are WORLD by their infra paths, the rest LOCAL. No judgment criterion. The orders declare nine criteria, matching the packet. Re-run here on the current landed tree: 9 of 9 PASS (rc 0); the issuer's landed-tree claim holds this time. DIFF SCOPE: no round-122 checker diffs the whole repo. p122_split.py and p122_cothandler.py read only the worker's own commits (author-filtered `git log` from the order's first commit, then `git show` per commit); p122_mem.py and p122_conv.py diff nothing. The round-121 clauses v86 found were amended at 6f8340aba0, and DB121-2-AC2 and DB121-4-AC3 now PASS here. The struck DB118-3-AC3 still FAILS (rc 1), unmet. Four proof instances VALID; `round-close-check --round 122 --workstream B-49F` MAY-CLOSE (4 orders). No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S24",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T10:20:00Z",
  "one_line": "Round 122 B-49F (~D2): peak memory of the hop-1 stage (DB-b-246), the per-day self-invoke split (DB-b-247), the 04-21 conversion read (DB-b-248: 920 VUG receipts, 30 with any same-day fall elsewhere, 0 matched within 5 percent, CONVERSION_LEG_ABSENT), and the Cottonwood landing function code (DB-b-249: handler, 15-member closure proved by a staged probe, source-map entry, pins null). 9 of 9 PASS re-run on the landed tree; the diff clauses are scoped to the workers' own commits. Struck DB118-3-AC3: still unmet. MEMORY: the memory finding (peak 4,024.6 MB against a 2,105.6 MB line and a 3,008 MB function; the inputs alone are 2,587 MB) comes from a LOCAL Python process on this box, not from Lambda; nothing live ran or hit a limit. LOCAL vs served: the live irpt-49f-reporting-gold-lambda reads LastModified 2026-10-13T12:39Z, CodeSha256 J6M/92Mh... (unchanged from v85 and v86), MemorySize 3008. Its inline policy still holds 7 statements, so neither the round-121 grants nor this round's InvokeOwnFunctionOnly is applied. irpt-cot-account-return-daily-lambda does not exist (ResourceNotFoundException; positive control: the reporting-gold function resolves). The four worker records read deployed false and served_values_changed false; the two READ records read s3_writes 0. Rows: W200-S1, W201-S1, W202-S1, W203-S1 (BLOCKING, INERT: sparse worktrees lacked infra/ or data/; the issuer's provisioning error) are resolved by W200-S2..W203-S2 (sparse checkout disabled; the cells then ran to PASS). W201-S3 (BLOCKING: the order contradicted itself) is resolved by W201-S4 (Amendment 1 @82091e0b7f, one test updated; 120 pass here). W203-S3 (BLOCKING: the naming gate refused account-return-cot) is resolved by W203-S4 (Amendment 1 @90dc82c71f renamed it to account-return-daily). W203-S5 (BLOCKING: the stray clause read the old path) is resolved by W203-S6 (checker @616950e0bd counts only paths that exist at HEAD). That fix loosens the bar slightly: an out-of-grant file a worker touched and then deleted would no longer count. It is acceptable here, and named. All resolutions are grounded in the re-run.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W200-S1",
   "IRPT_DASHBD-D2-W200-S2",
   "IRPT_DASHBD-D2-W201-S1",
   "IRPT_DASHBD-D2-W201-S2",
   "IRPT_DASHBD-D2-W201-S3",
   "IRPT_DASHBD-D2-W201-S4",
   "IRPT_DASHBD-D2-W202-S1",
   "IRPT_DASHBD-D2-W202-S2",
   "IRPT_DASHBD-D2-W203-S1",
   "IRPT_DASHBD-D2-W203-S2",
   "IRPT_DASHBD-D2-W203-S3",
   "IRPT_DASHBD-D2-W203-S4",
   "IRPT_DASHBD-D2-W203-S5",
   "IRPT_DASHBD-D2-W203-S6"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug; a criterion is re-run on the landed tree; no IAM or AWS change outside safe-apply and a signed pair.",
  "world_is": "Four orders complete (merges 2d18453f6b, 37b5d26f53, 091ad4ded1, 266de362d1); nothing planned, applied, deployed, invoked or written to AWS. Hop 1 cannot land as built: per-day time fits (154.2 s), but local memory does not, and the INPUT READ must be split by account group (size not measured) or the memory raised. The live self-invoke and the grant's unqualified ARN against context.invoked_function_arn are unread until the first real fire. The 04-21 break is a feed gap (no delivery leg), to be stated in words. Cottonwood has handler code and a proved closure, and no Terraform or function. The packet is stale on D2-W195-S1: it still lists it ARMED awaiting a reply, but D2-S71 disarmed it (v85, verified live). FWD-2, FWD-11 and FWD-21 are not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T10:1xZ: DB122-1-AC1, AC2, DB122-2-AC1..AC3, DB122-3-AC1, DB122-4-AC1..AC3 PASS rc 0; DB118-3-AC3 FAIL rc 1; DB121-2-AC2 and DB121-4-AC3 PASS after 6f8340aba0",
    "p122_split.py:78-103 and p122_cothandler.py:82-104 (own_commits / own_numstat / own_files); p122_mem.py and p122_conv.py hold no git diff",
    "aws lambda get-function-configuration irpt-49f-reporting-gold-lambda: LastModified 2026-10-13T12:39:43Z, MemorySize 3008; aws iam get-role-policy irpt-49f-reporting-gold-role/irpt-49f-reporting-gold-policy: 7 statements; aws lambda get-function irpt-cot-account-return-daily-lambda: ResourceNotFoundException",
    "worker records RD_STAGE_MEMORY_R122, RD_SPLIT_FACTS_R122, RD_CONVERSION_READ_R122, RD_CW_HANDLER_FACTS_R122",
    "proof-of-spec-check VALID rc 0 on ~200..~203; round-close-check --round 122 --workstream B-49F verdict=MAY-CLOSE orders=4",
    "investigation rows D2-W200-S1..S2, D2-W201-S1..S4, D2-W202-S1..S2, D2-W203-S1..S6",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND122_B49F_DRAIN_END_20261015.md blob 7878b9d2e0 (msg 8229)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Every BLOCKING worker row is resolved by an issuer ruling or amendment and re-graded green here. No row is ARMED. The memory finding is a local measurement that moved nothing live."
 }
]
```
