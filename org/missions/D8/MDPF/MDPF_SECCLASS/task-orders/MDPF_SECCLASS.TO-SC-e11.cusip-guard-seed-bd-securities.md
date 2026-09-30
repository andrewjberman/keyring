# TO MDPF_SECCLASS.TO-SC-e11 -- round 5 SC-e-11: the CUSIP guard on the bd-securities seeder, dry-run delta 0, and the CUSIP_ROWS half's guard section

<to_id>MDPF_SECCLASS.TO-SC-e11</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~9</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-30</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-e-11` (`decompositions/MDPF_SECCLASS_DECOMP_R5.md`) |
**outcome_ref:** FWD-4, FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-11`. Round 3's SC-e-9 planned 349 CUSIP-keyed rows for `etf-classifications` (key `CUSIP:<9>`, census
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CUSIP_CENSUS_20260930.json`). Its reader census found the
one genuine reader risk: `data/black_diamond/scripts/classification/seed_bd_securities.py` copies EVERY
`etf-classifications` row into the retiring per-firm table `bd-securities`, unconditionally. If the CUSIP rows land
first, the fork gains 349 rows it never had. The CTO (`ROUND2_3_ANALYSIS_MDPF_SECCLASS_20260930.md` @0a8deabc8e, section
2, last paragraph) signs the CUSIP_ROWS half only on a packet whose dry-run prints the bd-securities delta from CUSIP
keys as 0 new rows. This cell builds that guard and that packet.

**Build (LOCAL build + record: no table write, no deploy):**
1. **The guard.** In `seed_bd_securities.py`, every row whose hash key starts with `CUSIP:` is skipped before any
   write path, and the skip is counted and printed (`skipped_cusip=<n>`). Nothing else in the copy logic changes.
   Read the file first; keep its CLI, its dry-run flag and its output lines as they are.
2. **The test** in `data/black_diamond/scripts/classification/tests/test_seed_bd_securities_cusip_guard.py` (create the
   directory if absent; stub DynamoDB): a `CUSIP:037833100` row is skipped and counted; a `TICKER`-keyed row is copied
   as today; the count equals the number of `CUSIP:` rows offered.
3. **The dry-run against the LIVE tables** (read only). Write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R5_CHECKS/r5_cusip_guard_dryrun.py`. It reads the live
   `etf-classifications` (denominator = rows read) and the live `bd-securities` (rows read), applies the seeder's
   guard, and prints ONE line: `CUSIP-GUARD etf_rows=<n> cusip_rows=<n> bd_rows=<n> bd_delta_from_cusip=<n>`. It also
   runs the planned 349 rows of `R2_CUSIP_CENSUS_20260930.json` through the same guard and prints
   `CUSIP-GUARD-PLANNED planned=<n> would_copy_to_bd=<n>`. Both `bd_delta_from_cusip` and `would_copy_to_bd` must read
   0; a nonzero is a refusal, not a rounding.
4. **The half's guard section.** Append `## Guard (SC-e-11)` to
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CUSIP_ROWS_20260930.md`:
   the two lines from step 3 verbatim, the guard's file and line, the test's path, and the sentence that the
   CUSIP_ROWS act is REFUSED unless a fresh dry-run immediately before it prints both counts as 0. Do not edit any
   other section of the half.

### ACCEPTANCE

<criterion id="SC5-e11-AC1" cell_refs="SC-e-11"><invocation>python -m pytest data/black_diamond/scripts/classification/tests/test_seed_bd_securities_cusip_guard.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC5-e11-AC1` -- the guard's test passes: CUSIP rows skipped and counted, ticker rows copied.

<criterion id="SC5-e11-AC2" cell_refs="SC-e-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R5_CHECKS/r5_cusip_guard_dryrun.py</invocation><expect>CUSIP-GUARD</expect></criterion>
`SC5-e11-AC2` -- the live dry-run prints both lines with `bd_delta_from_cusip=0` and `would_copy_to_bd=0`.

<criterion id="SC5-e11-AC3" cell_refs="SC-e-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CUSIP_ROWS_20260930.md</invocation><expect>HALF-READY</expect></criterion>
`SC5-e11-AC3` -- the CUSIP_ROWS half still reads HALF-READY with its new guard section.

<expected_criteria>SC5-e11-AC1,SC5-e11-AC2,SC5-e11-AC3</expected_criteria>

Dry-run at the base 2026-09-30 14:2xZ: AC1 no such test file (FAIL as expected); AC2 no such check (FAIL as expected);
AC3 HALF-READY already (the half exists from SC-e-9; the criterion binds the file AFTER step 4, and the section's
presence is read by the issuer at the drain).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Build scaffolding goes under
  `.scratch/`, uncommitted.
- **LOCAL build + record.** No table write, no upload, no deploy. The live tables are READ only (Scan is permitted for
  the denominator). `bd-securities` is never written by this cell.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W9-S<k>`), and do not weaken the test to pass.

<paths>
data/black_diamond/scripts/classification/seed_bd_securities.py
data/black_diamond/scripts/classification/tests/test_seed_bd_securities_cusip_guard.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R5_CHECKS/r5_cusip_guard_dryrun.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CUSIP_ROWS_20260930.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R5.md</decomp_doc> (round 5), cell `SC-e-11`.
<owned_cells>SC-e-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC5-e11-AC1, SC5-e11-AC2, SC5-e11-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~9/MDPF_SECCLASS.TO-SC-e11.cusip-guard-seed-bd-securities.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC5-e11-AC1,SC5-e11-AC2,SC5-e11-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the guard's diff (file and lines), the test line, both dry-run lines verbatim with their denominators, the
half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change; the seeder is a manual script and this cell adds a guard to it.
comp-iam: RUN -- 1 file read (seed_bd_securities.py reads etf-classifications and writes bd-securities under the laptop principal's own credentials; no role change); BLIND: whether the laptop principal may Scan both tables is unmeasured (a refusal is a surprise row, not a grant).
comp-adversary: RUN -- 1 census read (R2_CUSIP_CENSUS_20260930.json: readers=18, would_write=349), 1 ruling read (ROUND2_3_ANALYSIS section 2, the CVO's adopted question), 1 code read (seed_bd_securities.py copies every row); BLIND: the live bd-securities row count at the cut is unmeasured (step 3 measures it).
lane: the <paths> block IS the grant.
</preflight>

Source: 1.0.0_SA_CTO rounds 2-3 analysis @0a8deabc8e (section 2, the CUSIP_ROWS signing precondition; section 4 item 1).
