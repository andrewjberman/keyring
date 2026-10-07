# TO MDPF_SECCLASS.TO-SC-e48 -- round 9 SC-e-48: FWD-14 -- the clean-name row set regenerated with the repaired function, held unnamed rows named from the custody feed: row set, dry-run writer, half request

<to_id>MDPF_SECCLASS.TO-SC-e48</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~35</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-48` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-14 | **depends_on:** MDPF_SECCLASS.TO-SC-e47 (the repaired `clean_name()`). Slot `~35`, second in its queue; the
issuer hands it once `TO-SC-e47` has drained.

---

## WORKER FACE

### THE CELL

`SC-e-48`: "The clean-name row set regenerated with the repaired function, plus held unnamed rows named from the custody feed's
security name (2.2); dry-run writer; half request" (DECOMP_R9).

FWD-14 (PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` v0.13): "An advisor reads a properly written security name
wherever holdings are listed." Analysis ruling 2.2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md`):
"The source for a held row with no name is the custody feed's security name for that position, passed through `clean_name` once
W28-S5 is repaired. An AI-made row keeps FWD-11's clean name. Unheld unnamed rows are not graded by FWD-14." The contract's
precedence (C-WRITER): a `seed` row is corrected in the seed source, never in the table -- list it as SEED-SOURCE.

**Round 8's set** (`M/CLEAN_NAME_ROW_SET_20261007.tsv`, TO-SC-e34; `M/` = `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/`)
covered the 883 named rows only (write 495, seed-source 33, unchanged 355) with the unrepaired function; 2,624 of 3,507 rows carry no
name, the 13 AI-made rows among them. This cell rebuilds it with the repaired function and adds the held unnamed rows.

**Held set: `inferred`.** dell1's principal is denied the three firm buckets (row W25-S1; ruling 2.9). Build each firm's held set the
way TO-SC-e26 and TO-SC-e33 did: the Holdings producer `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` run per
firm WITHOUT `--upload` (nothing published), reusing `M/R10_CHECKS/old_list_census.py` `build_firm()` (as-of 2026-10-05); the
custody feed's security name for a position is the SECURITY node's name field the producer carries (read the producer to name the
field). A grade that needs the served bytes is a laptop seat's read, filed as a row, not done here.

**Build (NO table write):**
1. `M/R11_CHECKS/clean_name_row_set_v2.py`: one consistent scan of `etf-classifications`, plus the per-firm held sets; writes
   `M/CLEAN_NAME_ROW_SET_V2_20261007.tsv`, tab-separated, header
   `key	classified_by	current_name	source_name	clean_name	action	source`:
   - one line per row with a non-blank live `name`: `source` = `table`, `source_name` empty, `clean_name = clean_name(current_name)`,
     `action` UNCHANGED (equal) / SEED-SOURCE (a `seed` row) / WRITE;
   - one line per HELD key with no live `name` whose custody name is non-blank: `source` = `custody:<firm>` (the first firm in the
     order 49financial, cottonwood, inflection that holds it), `current_name` empty, `source_name` = the custody name,
     `clean_name = clean_name(source_name)`, `action` WRITE (or SEED-SOURCE for a seed row). An AI-made row (`classified_by` model)
     is never in the custody group: FWD-11 names it.
2. `M/R11_CHECKS/clean_name_write_v2.py`: the writer. Default is a dry run. `--write` requires `--half <path>` (refuses unless both
   halves read SIGNED) and `--snapshot <path>` (the pre-state of every WRITE key, consistent reads). Each WRITE is a conditional
   update `SET name = :clean, updated_by = :by` with condition `name = :current` for a `table` row and `attribute_not_exists(name)`
   for a `custody` row. The dry run prints `CLEAN-NAME-V2-DRY-RUN write=<n> custody=<n> seed_source=<n> unchanged=<n> refused_stale=<n> puts=0`
   and asserts `puts=0` (a counter on the table handle). Rollback per key: back to the snapshot (a custody row: `REMOVE name`).
3. `M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CLEAN_NAMES_V2_20261007.md`: COO and CTO halves UNSIGNED; sections `## The act`,
   `## Blast radius` (one table, `name` and `updated_by` on the WRITE keys, counts and list, the local candidate diff), the readers
   that print the name (those you can name from the repo, and those you cannot), `Rollback per key`, the dry-run line; it SUPERSEDES
   round 8's clean-name half (say so).
4. ASCII only.

### ACCEPTANCE

<criterion id="SC9-e48-AC1" cell_refs="SC-e-48"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_set_v2_check.py</invocation><expect>CLEAN-NAME-SET-V2 ok=True</expect></criterion>
`SC9-e48-AC1` -- every named row once with the repaired function's name, every custody row a held unnamed key, the right actions.

<criterion id="SC9-e48-AC2" cell_refs="SC-e-48"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_write_v2.py</invocation><expect>puts=0</expect></criterion>
`SC9-e48-AC2` -- the writer dry-runs over the set with no write.

<expected_criteria>SC9-e48-AC1,SC9-e48-AC2</expected_criteria>

Dry-run at the base 5d70aab6c9: AC1 FAIL as expected (`missing=CLEAN_NAME_ROW_SET_V2_*.tsv`); AC2 FAIL as expected (no writer).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- **No table write and no `--write` run.** The write is the issuer's act under the signed half. No upload of any producer build.
- Do not edit `security_name.py`, the seed module, the producer or any reader; the R11 issuer check is READ-ONLY to you.
- **No package install and no download of any kind** (row S49). No model call.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W35-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_row_set_v2.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_write_v2.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_V2_20261007.tsv
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_CLEAN_NAMES_V2_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-48`.
<owned_cells>SC-e-48</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e48-AC1, SC9-e48-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~35/MDPF_SECCLASS.TO-SC-e48.clean-name-row-set-v2.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e48-AC1,SC9-e48-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the counts per action and per source, the custody field used per firm, the held-set as-of and claim, the dry-run line,
the half path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the cell schedules nothing; the write is an issuer act with its own pair and ledger entry.
comp-iam: RUN -- round 8 (W25-S1, W23-S4): dell1's principal is denied the three firm buckets by DenyForeignFirmPrincipals; held sets are local producer builds, inferred. No role is declared by this cell.
comp-adversary: RUN -- the round-8 set's counts (883 named, 2,624 unnamed incl. 13 model rows); ruling 2.2's source; the precedence rule (seed corrected in the seed source). BLIND: the custody name field per firm (the worker names it); every reader that prints the name.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.13 FWD-14 @90f99888cd; analysis ruling 2.2 @1ca9e97fc9; DECOMP_R9 @5d70aab6c9; TO-SC-e34 (round 8).
