# TO IRPT_BCKEND.TO-IB-m20-204 -- R4: read back the first scheduled Holdings fire per firm (2026-09-29)

<to_id>IRPT_BCKEND.TO-IB-m20-204</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~43</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-204`
(`decompositions/IRPT_BCKEND_DECOMP_R20_M.md`) | **outcome_ref:** FWD-5, goal criterion 3 | **depends_on:** IB-mr-201,
and the 14:15Z fire having ended

---

## WORKER FACE

### THE CELL

`IB-mr-204` -- the CTO and CRO signed the R4 enable on one condition: the FIRST SCHEDULED fire (Tue 2026-09-29 10:15
America/New_York = 14:15Z) is the per-firm proof, never a hand-run, and a firm that fails reads unchanged. You read
that fire back. You are spawned only after it has run; if no scheduled command dated 2026-09-29 exists on runner
`i-02448edb624a7a7cf`, STOP with a row -- never invoke the dispatch yourself.

### BUILD

1. The scheduled fire sends one SSM command per firm commented `irpt holdings refresh <firm> 2026-09-29` (no `qa`).
   Find the three (boto3 `ssm.list_commands(InstanceId=...)`, paginated), wait for each to be terminal (poll at most every
   60 s, at most 60 min), and read `get_command_invocation`: status, rc, the as_of it built, the revision it published.
2. Per firm, read the SERVED Holdings manifest VersionId (the key comes from `holdings_snapshot.py`'s publisher
   `location("platinum", "current", "manifest.json")` in the firm's bucket) and its version immediately before the fire.
   Use `s3.list_object_versions` on that key to name the version current just before the command's start time.
3. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_R4_FIRST_FIRE_20260929.json` as
   `{"firms": [{"firm", "command_id", "status", "rc", "as_of", "revision", "served_version_before",
   "served_version_after", "reconcile"}]}` -- `reconcile` is the command output's own reconciliation line (the
   difference control and custody total). A Success firm's served VersionId must have MOVED; a failed firm's must be
   UNCHANGED. If either rule breaks, STOP with a row: that is the halves' condition failing.
4. Also record the 2026-09-29 business date the fire built against (the halves' holiday condition: a non-trading day
   publishes no new business date; 09-29 is a trading day, so a new business date is expected).
5. Close ledger `irpt-holdings-schedule-enable-m-20260929` leg V2 with a one-line per-firm proof, then `close` the
   ledger. Commit.

### ACCEPTANCE

<criterion id="IBM20-204-AC1" cell_refs="IB-mr-204"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_m204_first_fire.py</invocation><expect>READ-BACK followed by 49financial, inflection and cottonwood each with its SSM status</expect></criterion>
`IBM20-204-AC1` -- the first scheduled fire is read back per firm, served VersionIds move exactly where the fire
succeeded, and the enable ledger is CLOSED.

<expected_criteria>IBM20-204-AC1</expected_criteria>

Dry-run at the base 2026-09-29 01:0xZ: NOT-READ: the read-back JSON absent (FAIL as expected).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **Read-only on AWS** except the ledger files: no dispatch invoke, no schedule change, no package mint, no served
  write, no runner start/stop.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W43-S<k>`), and do not weaken the test to pass.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_R4_FIRST_FIRE_20260929.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-holdings-schedule-enable-m-20260929.json
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R20_M.md</decomp_doc> (round 20, workstream ~M), cell `IB-mr-204`.
<owned_cells>IB-mr-204</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM20-204-AC1. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~43/IRPT_BCKEND.TO-IB-m20-204.r4-first-scheduled-fire-read-back.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM20-204-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** per firm command id, status, rc, as_of, revision, served VersionId before -> after,
reconcile line; the ledger close; commit hashes.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- first fire after the IB-mr-201 flip: Tue 2026-09-29 14:15Z (trading day); the runner's up window is 12:52Z-16:41Z.
comp-iam: DECLARED-NOT-APPLICABLE -- read-only.
comp-adversary: RUN -- 1 dispatch source read (refresh_dispatch.py:99-137: one SSM command per firm, comment "irpt holdings refresh[ qa] <firm> <date>"); BLIND: the served manifest key path was not read at the cut (the cell derives it from the publisher); the check re-reads each SSM command comment to refuse a qa command or a hand-run passed off as the scheduled fire.
lane: the <paths> block IS the grant.
</preflight>

Source: `STATUS~M.md` @dc913869d8 next-list item 1 (proof leg); CTO 102501 and CRO 102507 conditions; CTO ruling 102516.
