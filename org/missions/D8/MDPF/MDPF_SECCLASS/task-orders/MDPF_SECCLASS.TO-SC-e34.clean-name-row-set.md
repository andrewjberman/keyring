# TO MDPF_SECCLASS.TO-SC-e34 -- round 8 SC-e-34: FWD-14 -- the clean names for the rows the table already holds: row set, dry-run writer, half request

<to_id>MDPF_SECCLASS.TO-SC-e34</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~28</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>8</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-34` (`decompositions/MDPF_SECCLASS_DECOMP_R8.md`) |
**outcome_ref:** FWD-14 | **depends_on:** MDPF_SECCLASS.TO-SC-e30 (imports
`infra/aws/lambda/v2_portal/_shared/security_name.py` `clean_name()`). Slot `~28`, second in its queue; the issuer hands it to
the slot only when `TO-SC-e30` has drained.

---

## WORKER FACE

### THE CELL

`SC-e-34`. "The clean names for the rows the table already holds: the row set (current name, clean name) from `SC-e-30`'s
function, a dry-run writer and the half request" (R8).

FWD-14 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.12): "An advisor reads a properly written security
name wherever holdings are listed." ACCEPT: "the name beside each holding is the shared list's clean, properly capitalized name,
not the custody feed's capital-letter string." Addendum v0.7: the clean-name rule "applies to every row, not only model rows".
The contract's precedence (addendum v0.4 C-WRITER): "a seed row always wins, and a correction is made in the seed source" --
so a `seed` row whose name would change is NOT written to the table; it is listed for the seed source.

**Measured by the issuer 2026-10-07 (read-only scan of DynamoDB `etf-classifications`, 3,507 rows):**
| name shape | legacy | scheduled | seed | model |
|---|---|---|---|---|
| all capitals | 3 | 492 | 33 | 0 |
| already mixed case | 176 | 15 | 164 | 0 |
| no name | 59 | 2,552 | 0 | 13 |

So 883 rows carry a name and 2,624 carry none. A row with no name has no source name in the table and is OUTSIDE this cell
(count it in the report; sourcing a name is a later decision, not a casing act).

**Build (NO table write):**
1. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/clean_name_row_set.py`: one consistent scan, then
   writes `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_20261007.tsv`, tab-separated, header
   `key	classified_by	current_name	clean_name	action`, one line per row with a non-blank name:
   `clean_name = clean_name(current_name)`; `action` is `UNCHANGED` when equal, else `SEED-SOURCE` for a `seed` row, else `WRITE`.
2. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/clean_name_write.py`: the writer. Default is a dry run.
   `--write` requires `--half <path>` (refuses unless both halves read SIGNED in that file) and `--snapshot <path>` (the
   pre-state of every WRITE key, consistent reads). Each WRITE is a conditional update: `SET name = :clean, updated_by =
   :by` with condition `name = :current` (a row that moved since the set was built is refused, never overwritten). The dry run
   prints `CLEAN-NAME-DRY-RUN write=<n> seed_source=<n> unchanged=<n> refused_stale=<n> puts=0` and asserts `puts=0` (wrap the
   table with a counter). Rollback per key: a conditional update back to the snapshot name where `updated_by` is the run's.
3. `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CLEAN_NAMES_20261007.md`: the
   half request, COO and CTO halves UNSIGNED: blast radius (one table, the `name` and `updated_by` attributes of the WRITE
   keys, count and list), the SEED-SOURCE list handed to the seed source's owner (cell `SC-e-21` owns
   `infra/aws/lambda/v2_portal/_shared/etf_classification.py` this round; you do not edit it), the readers that print the
   name (state which you can name from the repo, and which you cannot), the rollback per key, and the dry-run line.

### ACCEPTANCE

<criterion id="SC8-e34-AC1" cell_refs="SC-e-34"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/sc_e34_row_set_check.py</invocation><expect>CLEAN-NAME-SET ok=True</expect></criterion>
`SC8-e34-AC1` -- every named row appears once, matches the live name, carries the function's clean name and the right action.

<criterion id="SC8-e34-AC2" cell_refs="SC-e-34"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/clean_name_write.py</invocation><expect>puts=0</expect></criterion>
`SC8-e34-AC2` -- the writer dry-runs over the set with no write.

<expected_criteria>SC8-e34-AC1,SC8-e34-AC2</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`CLEAN-NAME-SET ok=False missing=CLEAN_NAME_ROW_SET_20261007.tsv`);
AC2 FAIL as expected (no writer).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No table write and no `--write` run.** The scan is read-only. The write is the issuer's act under the signed half.
- Do not edit `security_name.py` (a case you believe it gets wrong is a surprise row), the seed module or any reader.
- **Refusal clause.** If a criterion cannot be met as written, stop on it, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W28-S<k>`), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/clean_name_row_set.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/clean_name_write.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_20261007.tsv
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CLEAN_NAMES_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R8.md</decomp_doc> (round 8), cell `SC-e-34`.
<owned_cells>SC-e-34</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC8-e34-AC1, SC8-e34-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~28/MDPF_SECCLASS.TO-SC-e34.clean-name-row-set.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC8-e34-AC1,SC8-e34-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the counts per action, the unnamed-row count, the SEED-SOURCE list size, the dry-run line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- R8 battery (2026-10-07 ~07:3xZ): 8 gates name the lane, all open deploy-ledger entries; none names a name write. The write is an issuer act with its own pair and ledger entry.
comp-iam: RUN (R8 battery, DESIRED plane): 0 gap lines on etf-classifications. No role is declared by this cell.
comp-adversary: RUN -- R8 compose. Cell read by the issuer 2026-10-07: the name-shape by classified_by partition above (3,507 rows; 883 named; 2,624 unnamed incl. all 13 model rows). BLIND: every reader that prints the name (the half names those it can).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.12 FWD-14, addenda v0.4 and v0.7 @87ad6d2e4c; R8 @495efa3c32.
