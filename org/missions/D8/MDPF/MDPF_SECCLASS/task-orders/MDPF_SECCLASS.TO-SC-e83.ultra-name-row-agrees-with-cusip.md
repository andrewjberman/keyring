# TO MDPF_SECCLASS.TO-SC-e83 -- round 16 SC-e-83: AMERICAN CENTURY ULTRA INV's NAME:: row agrees with its CUSIP: row (one REMAP line + the half)

<to_id>MDPF_SECCLASS.TO-SC-e83</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~73</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-83` (`decompositions/MDPF_SECCLASS_DECOMP_R16.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SC-e-83`, row MDPF_SECCLASS-D1-W66-S1. One security has two canonical rows in `etf-classifications` that disagree. A full scan (11,361
rows) at the cut found exactly two rows carrying the name "American Century Ultra Inv":
- `CUSIP:025083882`: asset_class `equity`, sub_asset_class `US Large Cap`, classified_by scheduled, updated_by mdpf-secclass-s62-ascii-names;
- `NAME::AMERICAN CENTURY ULTRA INV`: asset_class `fixed_income`, sub_asset_class `Ultra Short Duration`, classified_by scheduled,
  updated_by mdpf-secclass-old-list-reclassify.
American Century Ultra Fund, Investor class (TWCUX), is a US large-cap growth equity fund. "Ultra" is the fund's name, not an ultra-short
duration bond. The `NAME::` row is the wrong one, and this cell sets it to the `CUSIP:` row's class.

**Build:**
1. Re-read both rows with a consistent get_item and confirm the values above. If either moved, stop and report.
2. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_ULTRA_ROW_SET_20261009.tsv` with the header
   `key	name	action	asset_class	sub_asset_class	current_class	rule	evidence` and ONE line: key
   `NAME::AMERICAN CENTURY ULTRA INV`, name `AMERICAN CENTURY ULTRA INV`, action `REMAP`, asset_class `equity`, sub_asset_class
   `US Large Cap`, current_class `fixed_income`, a short rule ("agree with CUSIP:025083882"), and short evidence. Tab-separated.
3. Write `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ULTRA_NAME_ROW_20261009.md`, shaped
   like the other half requests in that folder (`## The act`, `## Blast radius`, `Rollback per key`). It must name:
   - the act: `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/s11_rows_write.py --set <the TSV> --write
     --half <this file> --snapshot <a new snapshot path>`, run by the issuer after both halves sign;
   - the blast radius: one row's asset_class and sub_asset_class. Count the BD and COT served positions that carry this name (read-only,
     from the newest `gold/canonical/holdings/` partition in each firm bucket) and their dollars, because those positions' class moves
     at the next gold run;
   - the rollback per key: the snapshot the writer takes first, restored with `s11_rows_write.py --rollback <snapshot> --write`.
   Leave both halves unsigned.

### ACCEPTANCE

<criterion id="SC16-e83-AC1" cell_refs="SC-e-83"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/s11_rows_write.py --set org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_ULTRA_ROW_SET_20261009.tsv</invocation><expect>S11-ROWS-DRY-RUN new=0 remap=1 refused_present=0 refused_stale=0 puts=0</expect></criterion>
`SC16-e83-AC1` -- the writer's DRY RUN (no flag writes nothing; its client counts every mutating call and asserts 0) plans exactly one REMAP
and refuses nothing.
<criterion id="SC16-e83-AC2" cell_refs="SC-e-83"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ULTRA_NAME_ROW_20261009.md</invocation><expect>HALF-READY</expect></criterion>
`SC16-e83-AC2` -- the half request carries the act, the blast radius and the rollback per key.

<expected_criteria>SC16-e83-AC1,SC16-e83-AC2</expected_criteria>

Dry-run at the base (dell1 box/dell1, 2026-10-09 ~09:0xZ):
- SC16-e83-AC1: FAIL, as expected (the set file is absent). A scratch one-line set of this exact shape read
  `S11-ROWS-DRY-RUN new=0 remap=1 refused_present=0 refused_stale=0 puts=0`, so the criterion is satisfiable.
- SC16-e83-AC2: FAIL, as expected (the half is absent).

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment).
- **AWS is READ-ONLY.** NEVER pass `--write` to `s11_rows_write.py`; the write is the issuer's act under the pair. No deploy, no invoke.
  Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id
  `MDPF_SECCLASS-D1-W73-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_ULTRA_ROW_SET_20261009.tsv
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_ULTRA_NAME_ROW_20261009.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R16.md</decomp_doc> (round 16), cell `SC-e-83`.
<owned_cells>SC-e-83</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC16-e83-AC1, SC16-e83-AC2. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~73/MDPF_SECCLASS.TO-SC-e83.ultra-name-row-agrees-with-cusip.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC16-e83-AC1,SC16-e83-AC2`.
</proof_of_spec>

**REPORT:** the two rows as re-read, the set line, the blast-radius counts, each criterion's output, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the one-row write is the issuer's act, outside a gold run.
comp-iam: DECLARED-NOT-APPLICABLE read-only for the worker; the issuer's principal wrote etf-classifications rows tonight (e77, e71).
comp-adversary: RUN -- a moved row (step 1 stops); the wrong row corrected (evidence names TWCUX); a stale condition (AC1 refused_stale=0); a write by the worker (bounds forbid --write)
lane: the <paths> block IS the grant.
</preflight>

Source: CTO rounds 13-15 analysis section 3 item 5 (msg 2139); row D1-W66-S1; DECOMP_R16.
