# NFRA_MCPINDEX task order -- `MX-c-15` -- the catalog's one writer loads the CLEAN silver table row (no firm token in it), joins the fork registry file back to the full row, and writes the joined row

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-15</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-15</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~39</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the emitter, its validator and their tests only; no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-run plus planted PASS and FAIL arms are the control (decomposition R14.7).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-15` (round 15; CTO ruling msg 34160: firm values live in a registry file, rows hold none)

Work in your own worktree, cut from `box/sitez`. Every path below is relative to its root. The one catalog writer is
`workflows/atom_decomposition/emit_catalog_v02.py`. It already loads, validates and writes silver TABLE rows (MX-c-13: `is_table_entry`,
`validate_entry`, `_validate_table_fields`, `load_catalog_entries`, `silver_catalog_row`). You do NOT write any `catalog_entries/` row, any registry
file or `DATA_CATALOG.yaml`: `MX-c-14` writes the 174 rows and the registry files in parallel; `2.0.0_SA_COO~MI` regenerates the catalog at the drain.
Do not run the emitter's `main`.

**Why.** The commit-time naming gate refuses a firm or product token in any whitespace-free string of a catalog row (a hand-kept carrier). The rows ARE the firm
fork, so the tokens move out of the rows and into `infra/logic/registry/catalog_fork_keys.json`, where tokens are permitted. A row keeps the fork's SHAPE only; the
loader JOINS the registry entry back, so the catalog the gateway loads still holds the full values.

**The clean row (what `MX-c-14` writes).** The table row you already accept, with these differences:
- `prefix` is a non-empty string OR null (null when the prefix is absent or carries a token); `table` is a non-empty string OR null;
- `contract` has exactly the keys `id label size freshness partition producer`: `id` a hashed id such as `c-068b87add1de` (non-empty string), `label` a non-empty string, the other four mappings (their string leaves may be null where a token was removed);
- `fork_keys` is a mapping whose keys are a SUBSET of `firm account platform`, each a mapping or null (a token key or value was dropped from it); an empty mapping is valid;
- `nl_tags`, `open_items` and `example_questions` are lists of strings (a token item was dropped);
- everything else as today.

### Part 1 -- the join in `load_catalog_entries`

The registry file is `catalog_fork_keys.json` in the registry directory: read it from `lib/opal_naming.py`'s `REGISTRY_DIR` attribute AT CALL TIME (a check points that
attribute at a planted copy). Its shape: `{"_about": "...", "rows": {"<hashed id>": {"key_template": "<full s3_prefix>", "restore": {"<top-level field>": <the full original value>, ...}}}}`.
A missing file or a missing row means no join. For a TABLE row that passes validation, look up `rows[row["contract"]["id"]]`; when it exists, return a COPY of the row in which each
`restore` field replaces the row's field, and `key_template` is set to the entry's `key_template`. The row is validated CLEAN (before the join). Rows without a `contract` (the old rows) are unchanged.

### Part 2 -- the writer

`silver_catalog_row(name, data)` writes, for a table row, the fields it writes today and then `key_template` when `data` carries it (after `retired_reason`). Nothing else changes: the emitted catalog holds the joined values.

### Part 3 -- relax the validator to the clean row

Change `_validate_table_fields` and its constants (`SILVER_TABLE_CONTRACT_FIELDS` gains `label`, `FORK_KEY_FIELDS` becomes a subset test, `prefix` and `table` may be null) so the 174 clean rows load.
Also write your own tests in `workflows/atom_decomposition/tests/test_silver_table_grain.py` (extend the file MX-c-13 left) for the join and the relaxed shape, and fix any test of the earlier shape that now fails.

## 2. BOUNDS

1. You change only the files in `<paths>`. No `catalog_entries/` row, no registry file, no `DATA_CATALOG.yaml`, no tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. Grade the gateway suite by failing-ID DELTA (`suite_delta.py`) against your base. The known failures (rows Z-S97, Z-S107) are listed, never fixed here.
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8). The gate refuses a firm or product token in a whitespace-free string of a NEW line: write none in code or tests (build a fixture identifier from a hashed id; the tests under `tests/` are exempt).
4. The checks build their own 174 clean rows, their own planted registry copy and their own one-defect rows. Read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c15_check.py` and `plant_impl_c15.py` for the exact interface. Do not edit them.
5. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/validate_catalog_v02.py
workflows/atom_decomposition/tests/test_silver_table_grain.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~39/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W39-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-15" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c15.AC1.sh; echo "exit=$?"</invocation><expect>ACCEPT: 174 of 174 clean table rows load; 174 of 174 JOINED to their full expected row; existing rows still load 10 of 10; REFUSE: 10 of 10 one-defect rows refused -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-15" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round14/checks/c15.AC2.sh; echo "exit=$?"</invocation><expect>CHECKS pass 6 of 6 (the joined row is written with key_template; an un-joined row and an old row are unchanged) -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~39/NFRA_MCPINDEX.TO-MX-c-15.silver-table-loader-fork-registry-join.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance.
2. APPEND `<status>complete</status>` only if both criteria PASS (if the commit gate refuses the flip, leave it and say so).
3. Commit everything together through `.tools/safe-commit.sh`.
4. Report once, with:
   - the validator change by constant and function;
   - one joined row before and after the join (print a short excerpt, no more than 12 lines);
   - the suite delta and your commit sha.

The issuer then merges this with `MX-c-14`, regenerates the catalog and runs the drain checks.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 15 (a one-cell round: the gate allows ONE issuance per round, and round 14 is issued), worker ~39 (a fresh slot, cut from the merged HEAD that carries MX-c-13), parallel to `MX-c-14` (no shared file). Source: CTO msg 34160 (rule 30's own remedy,
no gate edit): ids hashed, firm values in `catalog_fork_keys.json`, the loader joins. This order SUPERSEDES the row shape `c13.AC1-AC3` graded: those checks fail on the new loader by design (the contract gained `label`).
Battery and planted arms: decomposition R14.7.

<status>issued</status>
<round>15</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
