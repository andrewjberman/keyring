# NFRA_MCPINDEX task order -- `MX-s-19` -- retire the realized and transactions documents' merge step: one writer on all four Black Diamond silver tables

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-s-19</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~NFRA1</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at PHASE A by the worker -- bd-realized-pipeline-trigger 21:45Z, bd-transaction-pipeline-trigger 21:53Z (weekdays); bd-silver-merge on bronze/<date>/_BRONZE_COMPLETE.json (~00:10Z); no act inside 21:30-22:15Z or 23:45-00:45Z.
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change; two trigger rules and two document versions.
comp-adversary: DECLARED-NOT-APPLICABLE -- a writer retirement under never-widen halves (CTO + COO), sequenced after MX-s-18's sentinel fix is live.
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `MX-s-19` (round 7; `ROUND_ANALYSIS.round6.md` @361b186c92 section 3b rows Z-W24-S3 and Z-W24-S8, section 5 item 1(c) and criteria (iv)-(v))

**The CTO's ruling:** retire both documents' merge step with the sentinel fix, so a writer census reads 1 writer per BD
silver table, 4 of 4. Z-W24-S8's hold (the freshness-gate premise) is replaced: transactions retires on the sentinel
fix. Acceptance is the next scheduled `bd-silver-merge` run after a Mon/Tue empty window, reading failures=0 with the
partition landing the same evening.

**Precondition (do not start PHASE B without it):** MX-s-18 is applied and its ledger closed. You will hold that
order's report; quote its ledger close line in the ANNOUNCE.

**How round 6 retired the other two tables (MX-s-16, the pattern to follow):** a no-op document version (the merge
step removed, the download already gone) published with `aws ssm update-document`, set DEFAULT and read back; the
trigger rule disabled through Terraform (`infra/aws/terraform/bd-pipeline/`) with a saved targeted plan and
`safe-apply`. Nothing is deleted; documents and functions stay for rollback.

**Measured at the round-7 base:**
- Sentinel-less run dates in 09-03..10-02: 9, every Monday and Tuesday (09-07, 08, 09, 14, 15, 21, 22, 28, 29).
- On a normal day, `bd-silver-merge` logs `Incremental Merge [transactions]` then
  `SUMMARY: ... | failures=0 | ...` and writes `silver/transactions/*.parquet` between 00:00 and 03:00Z (10-01: 5 files;
  10-02: 2 files).
- The writer census (`s16.AC1.sh`, round 6) reads 2 of 4 tables with 1 writer (transactions, realized: 2 each).

### PHASE A -- no publish, no apply
1. Write both no-op document versions and cut the saved targeted plan disabling `bd-realized-pipeline-trigger` and
   `bd-transaction-pipeline-trigger` (any destroy is a BLOCKING row).
2. Write `ANNOUNCE_MX-s-19.md`: the plan, the expected served DELTA (0 on a normal day; on a Mon/Tue the partitions now
   land from `bd-silver-merge` at ~00:10Z instead of the document at ~21:50Z), and the rollback per table (re-set the
   prior document version DEFAULT and re-enable its rule; version numbers read). Report and STOP.

### PHASE B -- only on the issuer's GO
3. Open the NEVER-2 ledger `nfra-mcpindex-r7-bd-doc-retire`, naming BOTH the entry under
   `org/critical_paths/change_management/` AND `org/critical_paths/.open_deploys/nfra-mcpindex-r7-bd-doc-retire.json`.
4. Publish, apply, read back, run s19.AC1. Leave the ledger OPEN until the acceptance: s19.AC2 reads the scheduled runs
   of 2026-10-12 and 2026-10-13. On 2 of 2 close it; on a failure roll back that table per the ANNOUNCE and report.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-06 ~18:3xZ) -- acceptance re-dated.** The seat was down from 2026-10-02 04:26Z
to 10-06 18:1xZ, so MX-s-17/s-18 did not apply before 10-05 and the original dates (10-05, 10-06) ran with the old
writers: both read sentinel ABSENT (measured 18:29Z). The acceptance is now the first Mon/Tue pair after this order's
apply: 2026-10-12 and 2026-10-13. `s19.AC2.sh` carries the same dates. If the apply lands after 2026-10-12T00:00Z, the
issuer re-dates to the next Mon/Tue pair before the halves. Graded by: no gate limb graded this modification.

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-10-06 ~20:5xZ) -- re-addressed; re-sequenced behind a proven Monday and Tuesday.**
- **Re-addressed** from `0.9.0_WK_NFRA_MCPINDEX~24` to `0.7.0_AE_CloudOps~MI` on Andrew-direct 2026-10-06 ~19:4xZ
  ("bringing on a 0.7.0_AE_CloudOps~MI ... to handle these operations"; record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261006_194xZ_BD_CONSOLIDATE_WRITERS_INVESTIGATE_SHAPE_FIRST_SEAT_AE_MI.md`).
  The PHASE A work stands as built on branch `wk-nfra_mcpindex-r7-24` @3709ae40d6 (worktree
  `C:/Users/Opal Bloomberg/Desktop/wk-mcpindex-r7-24`); work there and commit there. Your write surface adds
  `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/**`; the proof instance goes there under the
  same file name.
- Basis: the MX-a-1 verdict (`org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/BD_RUN_SHAPE_COMPARISON.md`): the evening documents fetch nothing from BD and emit
  no field the morning path lacks; they remain the only same-day merger on sentinel-withheld days.
- **Precondition, replacing A1's dates:** PHASE B starts only after MX-s-18's Monday 2026-10-12 AND Tuesday
  2026-10-13 reads both pass with the evening rules still enabled. Andrew: "we need to confirm the shape first
  before making that move."
- **PHASE B is the rule disable only:** `bd-transaction-pipeline-trigger` and `bd-realized-pipeline-trigger`
  ENABLED -> DISABLED through a saved targeted plan and `safe-apply`. No document version is published, nothing is
  deleted, no instance is stopped or terminated. `opal-bd-asset-dim-download` and its rule and instance are not
  touched. Retiring the documents, trigger Lambdas and instances is a later order after one observed week.
- **Acceptance (s19.AC2):** the first Monday and Tuesday after the disable, 2026-10-19 and 2026-10-20; `s19.AC2.sh`
  carries those dates. If the disable lands later, the issuer re-dates.
- **Row ids (A3, 2026-10-06 ~21:2xZ):** a Tier-2 seat mints `NFRA_MCPINDEX-Z-S<k>` (next free k at commit time). The
  `W24-` form below is a worker-slot form and `Z-AEMI-` is refused by `surprise-row-gate.py` and
  `proof-of-spec-check.py` (seat report msg 30308).
- Graded by: no gate limb graded this modification.

**AMENDED A4 (2.0.0_SA_COO~MI, 2026-10-08 ~22:5xZ) -- re-addressed to the site Z applier.** From `0.7.0_AE_CloudOps~MI`
(dark since the site Z reboot) to `0.7.0_AE_CloudOps~Z`, on Andrew-direct 2026-10-08 ~22:0xZ ("spawn 0.7.0_AE_CloudOps on
their own box to handle deploys"; record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_220xZ_ONE_LAPTOP_APPLIER_EXCEPTION_YES.md`;
relayed by 0.0.0_AB_MSTR~Z msg 32063: "Site Z apply orders now address 0.7.0_AE_CloudOps~Z"). The A2 precondition is
unchanged: PHASE B starts only after MX-s-18's Monday 2026-10-12 and Tuesday 2026-10-13 reads pass; the issuer reads
them and sends the GO. MX-s-18 is complete @a74b50e525 (branch `wk-nfra_mcpindex-r7-24`), its ledger CLOSED @f2422adb7f.
Write surface adds `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~Z/**`; the proof instance goes
there under the same file name.
- Graded by: no gate limb graded this modification.

**AMENDED A5 (2.0.0_SA_COO~MI, 2026-10-09 ~01:5xZ) -- the A2 precondition becomes one read.** "MX-s-18's Monday and
Tuesday reads both pass" is graded by `bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/s19.PRE.sh`
(default dates 2026-10-12 2026-10-13), expecting `precondition dates passing 2 of 2 -- RESULT: PASS`. Per date it reads:
the runner's `OK: bronze sentinel emitted` line AND the sentinel object by head-object; the scheduled bd-silver-merge
transactions and realized SUMMARY lines with failures=0; and an object under silver/transactions/ and silver/realized/
written 00:00-03:00Z. The last two limbs are the Z-W24-S8 discriminator. Before the disable they show that the Lambda,
not the 21:54Z document, refreshes what the gold dispatch's freshness gate reads.
- Why: the A2 wording was prose, and a log line alone is not sound. On 2026-10-05 the pre-MX-s-18 code printed `OK:
  bronze sentinel emitted` while the shared module WARNed NOT emitted and the object reads 404.
- Controls run at amendment: positive 2026-10-08 2026-10-09 -> 2 of 2 PASS. Negative 2026-10-05 -> 0 of 1 FAIL
  (object 404, no merge SUMMARY, 0 silver objects).
- The issuer runs it on 2026-10-13 after 03:00Z. On PASS, the issuer sends the PHASE B GO to `0.7.0_AE_CloudOps~Z`.
  On FAIL, PHASE B does not start and the failing limb is filed as a row.
- Graded by: no gate limb graded this modification (to-pipeline-gate LIMB 6 does not fire on a modify).

**AMENDED A6 (2.0.0_SA_COO~MI, 2026-10-09 ~04:0xZ) -- the assignee is ruled, and its re-point is deferred.** 1.0.0_SA_CTO~Z
ruled in msg 32344 (relayed in 32345) that `0.7.0_AE_CloudOps~Z` keeps NFRA_OPLGTW (Rule 27). This order does not go to
that seat, and A4's re-address stands only until then. When s19.PRE.sh passes after 03:00Z on 2026-10-13, the issuer
amends `<issued_to>` to a FRESH site-Z CloudOps lane and tells 1.0.0_SA_CTO~Z, which seats it on demand. No GO goes to
`0.7.0_AE_CloudOps~Z`. `<issued_to>` is left as is now, per the ruling ("amend issued_to then, not now").
- Graded by: no gate limb graded this modification.

**AMENDED A7 (2.0.0_SA_COO~MI, 2026-10-13 ~03:2xZ) -- the precondition PASSED; re-addressed to `0.7.0_AE_CloudOps~MI`;
start at PHASE A.**
- s19.PRE.sh ran at 2026-10-13T03:06Z: `precondition dates passing 2 of 2 -- RESULT: PASS`. 2026-10-12: sentinel object
  00:11:10Z, transactions and realized SUMMARY failures=0, silver objects 5 + 1. 2026-10-13: sentinel object 00:11:32Z,
  both SUMMARY failures=0, silver objects 4 + 1.
- `<issued_to>` moves from `0.7.0_AE_CloudOps~Z` to `0.7.0_AE_CloudOps~MI` (A6). That lane holds orders on this project
  only: MX-a-1, MX-s-17 and MX-s-18, all complete. Its deliverables folder is already in `<paths>`. The issuer seats
  it.
- **PHASE A under A2 was never built.** No `ANNOUNCE_MX-s-19.md` and no saved plan exist at HEAD or on
  `wk-nfra_mcpindex-r7-24`. Start at PHASE A as A2 scopes it:
  - cut ONE saved targeted plan in `infra/aws/terraform/bd-pipeline/` that moves `bd-transaction-pipeline-trigger` and
    `bd-realized-pipeline-trigger` from ENABLED to DISABLED and nothing else (any destroy or any other change is a
    BLOCKING row);
  - write `deliverables/0.7.0_AE_CloudOps~MI/ANNOUNCE_MX-s-19.md`: the plan, the expected served DELTA, and the
    rollback (re-enable each rule through the same targeted path);
  - report, and STOP.
  The issuer then writes the never-widen ask, the COO and CTO halves are signed on the plan's pin, and the GO follows.
- Work in a fresh worktree cut from `box/sitez` HEAD. Do not use `C:/Users/Opal Bloomberg/Desktop/wk-mcpindex-r7-24`:
  it is held by worktree GC with 34 uncommitted paths, and its branch is already merged.
- The proof instance goes to `deliverables/0.7.0_AE_CloudOps~MI/` under the file name `<instance_path>` gives.
- Windows unchanged: no act inside 21:30-22:15Z or 23:45-00:45Z.
- s19.AC2's dates stand at 2026-10-19 and 2026-10-20 if the disable lands before 2026-10-19T00:00Z; otherwise the
  issuer re-dates them.
- Graded by: no gate limb graded this modification (to-pipeline-gate LIMB 6 does not fire on a modify; `<placeholders>`
  reads NONE, so GATE (viii) does not grade it).

**AMENDED A8 (2.0.0_SA_COO~MI, 2026-10-13 ~05:4xZ) -- PHASE A accepted; s19.AC1 re-cut to the SCHEDULED plane (row
Z-S101, option (b)); Z-S102 dismissed.**
- PHASE A is accepted as reported: `ANNOUNCE_MX-s-19.md` and `mx-s-19.plan.txt` @8b47c81ae2 (render sha256
  `bd04f330...`, binary sha256 `f69eae52...`), `.tf` edit on `wk-mcpindex-r7-s19-mi` @6df81ececb, plan 0/2/0.
- **s19.AC1** now counts an SSM document as a writer only while an ENABLED EventBridge rule targets its trigger Lambda.
  It reads `list-rule-names-by-target` and `describe-rule`; a document with no mapped trigger is counted fail-closed.
  It grades the SCHEDULED plane, never reachability: an ad-hoc `send-command` can still run a document. The invocation
  and `<expect>` are unchanged. Dry-run before the GO:
  - live, rules ENABLED: 2 of 4, FAIL;
  - planted, both DISABLED: 4 of 4, PASS;
  - planted, realized ENABLED: 3 of 4, FAIL.
  Row Z-S103 disarms Z-S101.
- **Z-S102 is dismissed (row Z-S104):** all 84,533 rows of the prior 2026-10-10 version are in the 2026-10-08 partition
  (69 of 69 value-stable columns match). The shrink removed a duplicate copy.
- **The unmeasured log-key consumer (ANNOUNCE section 3):** the only hits for `(realized|transaction)-download-` in
  `infra/`, `data/black_diamond/` and `lib/` are the three SSM documents that write the logs. No reader was found in
  that scope, and the rest of the repo was not searched.
- The GO follows the two never-widen halves: `deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-s-19_20261013.md`.
- Graded by: no gate limb graded this modification (LIMB 6 does not fire on a modify; `<placeholders>` NONE).

## 2. BOUNDS

1. One producer per table: no second schedule, no parallel path, no comparator. Served silver must not lose a
   partition it has today.
2. Nothing under `data/cot/`. No push. Never bare `terraform apply`; never `update-function-code`.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ssm/opal-bd-transaction-download.json
infra/aws/ssm/opal-bd-realized-download.json
infra/aws/terraform/bd-pipeline/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r7-bd-doc-retire.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~24/**
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/**
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~Z/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W24-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-s-19" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/s19.AC1.sh; echo "exit=$?"</invocation><expect>WRITER CENSUS: 4 of 4 BD silver tables have exactly 1 writer -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-s-19" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/s19.AC2.sh; echo "exit=$?"</invocation><expect>2026-10-19 and 2026-10-20 each: sentinel present, transactions SUMMARY failures=0, partitions written 00:00-03:00Z >=1; empty-window acceptance dates passing 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-s-19" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round7/checks/s19.AC3.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~24/NFRA_MCPINDEX.TO-MX-s-19.bd-doc-merge-retire.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report and stop. After PHASE B's apply, report; the issuer re-grades AC2 on the
acceptance dates. Write the proof instance when AC2 has read.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round-7 item 1(c), criteria (iv) and (v). AC2 is the CTO's named acceptance: the
first empty-window run dates after the retirement are 2026-10-05 and 2026-10-06; the scheduled run is the
discriminator (an ad-hoc runner invocation pulls from Black Diamond, a vendor call). Battery dry-run at base: s19.AC1
FAIL as expected (2 of 4); s19.AC2 FAIL as expected (dates not yet run; the instrument's positive control on
2026-10-01 + 10-02 reads 2 of 2 PASS, and the gap day 2026-09-29 reads sentinel ABSENT); s19.AC3 FAIL as expected.

<status>pending</status>
<round>7</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

**ISSUER NOTE (2.0.0_SA_COO~MI, 2026-10-15 ~23:5xZ), a correction.** An earlier note of 23:48Z in message 34615 said the PHASE B GO had never been sent. It was wrong: the GO is @4c154baf3b and PHASE B was applied on 2026-10-13 at 06:06Z (safe-apply of mx-s-19.tfplan, ledger nfra-mcpindex-r7-bd-doc-retire L1-L4 CLOSED, commit a2d33efb8e). Re-measured 23:53Z by 0.7.0_AE_CloudOps~MI: both rules DISABLED, schedules unchanged, s19.AC1 4 of 4 PASS. The order is correctly `pending`: only L5 is open, s19.AC2 on 2026-10-19 and 2026-10-20 (a date-gated wait; the owner is the schedule, not a seat). Nothing was re-applied. Gate limb that graded this note: none (LIMB 6 does not fire on a modification).

**AMENDED A9 (2.0.0_SA_COO~MI, 2026-10-16 ~16:4xZ) -- `<issued_to>` moves to `0.7.0_AE_CloudOps~NFRA1`; the order is live work and is not cancelled.** CLAUDE.md rule 34 (Andrew-direct ~15:4xZ 2026-10-16, relayed by MSTR~Z msg 35103) seats CloudOps one lane per macro per box; `1.0.0_SA_CTO~Z` (msgs 35107, 35111, 35125) names `~NFRA1` as the surviving NFRA lane and told this order to move there, not to be cancelled: s19.AC2 is dated 2026-10-19 and 2026-10-20 and the CVO's ADJUDICATION_v13 holds rows to it. `0.7.0_AE_CloudOps~MI` holds nothing and retires. What remains of this order is the acceptance only: PHASE B was applied 2026-10-13T06:06Z (ledger `nfra-mcpindex-r7-bd-doc-retire` legs L1 to L4 closed with proof) and the issuer re-grades `s19.AC2.sh` on 2026-10-19 and 2026-10-20; the applier's one act is to close ledger leg L5 on a PASS. **The ledger was measured, not closed:** the world shows the disable DONE (both rules `State DISABLED`, re-plan 0-diff) but the order's acceptance leg is a future, dated event, so the entry stays OPEN with its owner (`~NFRA1`, seated on demand by MSTR~Z) and its un-parking condition (s19.AC2 PASS on both dates), and is NOT closed SUPERSEDED. MSTR~Z is told by one line at this cut (CTO msg 35115). Gate limb that graded this amendment: none (a modification).
