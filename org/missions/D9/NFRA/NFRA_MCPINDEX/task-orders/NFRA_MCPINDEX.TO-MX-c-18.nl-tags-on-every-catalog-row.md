# NFRA_MCPINDEX task order -- `MX-c-18` -- every catalog row carries `nl_tags`: the emitter derives tags for the 44 rows whose source gives none, from the row's own text, and marks them `inferred`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-18</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-18</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~42</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- the emitter, one new module and tests only; no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs plus eleven planted arms are the control (decomposition R17.4).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-18` (round 17; PRD v0.16 FWD-22, closes row Z-C-S57's first half)

Work in your own worktree (cut from `box/sitez`; its portal folder is provisioned because the emitter reads it). Every path below is relative to its root. The one catalog writer is `workflows/atom_decomposition/emit_catalog_v02.py`; it writes `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, which you REGENERATE in YOUR worktree to grade the checks and do NOT commit (the issuer regenerates and lands it at the drain).

**Why.** The catalog has 304 rows in three sections (`silver_datasets`, `portal_datasets`, `harvest_datasets`). 260 carry `nl_tags`; 44 carry none or an empty list: 32 harvest rows (bronze and state layers), 2 draft silver table rows (the smartx allocation and valuation drafts) and 10 older hand-kept rows (`blackdiamond_fees`, four `schwab_dim_*`, five `portal_*`; their source schema has no `nl_tags` field). `opal_discover` matches a plain-words question against a row's own text plus its `nl_tags`, so a row with none is found only by its entity name. Those 44 rows get tags derived from their own `business_meaning` and `example_questions`, marked as derived.

**What to build.**

1. A new module `workflows/atom_decomposition/derive_nl_tags.py` with one public function `derive_tags(entity, business_meaning, example_questions)` returning a list of strings. It is pure and deterministic (no clock, no randomness, no I/O, no set iteration order). The algorithm, exactly:
   - `words(text)` = `re.findall(r"[a-z0-9]+", str(text).lower())`; a word in `STOP` is dropped (`STOP` is a module constant: `a an the of in for to and or is are was were on at by with from as it its this that these those be been what which who how where when why table data row rows one per each all any not no your you we our can will may must so than then into out up down over under`).
   - candidates, in this order: (i) the entity's non-stop words, first 4, if there are at least 2; (ii) for each of the first TWO example questions, its non-stop words, first 4, if at least 2; (iii) the meaning's non-stop words, first 12, cut into chunks of 3 consecutive words starting at index 0, 3, 6, 9 (each chunk joined by one space, kept if it has at least 2 words).
   - join each candidate's words with one space; drop a duplicate (keep the first); keep a tag only if it has 2 to 5 words; take the first 5.
   - if fewer than 3 remain, add 2-word windows of the meaning's non-stop words (index 0, 1, 2, ...) not already present until there are 3 or the words run out. Never invent a word: every word of every tag comes from the row's own entity, meaning or questions.
2. In `emit_catalog_v02.py`, one helper (for example `infer_nl_tags(row)`) called at the THREE row writer sites, on the finished row dict just before it is dumped: the silver rows (`silver_catalog_row`, after `unquote_carrier_spans`), the portal rows loop, and the harvest rows loop. If the row's `nl_tags` is absent, or an empty list, or holds only blank strings, set `row["nl_tags"]` to `derive_tags(row["entity"], row.get("business_meaning") or "", row.get("example_questions") or [])` and set `row["nl_tags_basis"] = "inferred"` (placed right after `nl_tags` where that key exists, otherwise at the end). If the derivation returns fewer than 3 tags, leave the row alone and print `WARN: nl_tags not derived for <entity>`. A row that already has non-empty `nl_tags` is NOT touched and gets NO `nl_tags_basis` key (the field exists only on derived rows, so a reader can tell a contract-given tag from an inferred one). The source files under `catalog_entries/` are not edited.
3. Tests, in a NEW file `workflows/atom_decomposition/tests/test_derive_nl_tags.py` with at least 8 tests: deterministic; 3 to 6 tags; each tag 2 to 5 lowercase ASCII words; no duplicate; every word drawn from the inputs; the 2-word fallback; the emitter helper fills an empty list and marks it inferred; it fills an absent key; it leaves a tagged row byte-equal with no basis key. Fix any EXISTING test under `tests/` that pinned the old emitted field set.

### Steps

1. Write the module, the helper and the tests. Run `python -m pytest -q -p no:cacheprovider workflows/atom_decomposition/tests` (all must pass).
2. Regenerate the catalog in your worktree: `python workflows/atom_decomposition/emit_catalog_v02.py` (it must end with HARVEST ROWS, SILVER and TOOL INDEX lines and no EMIT REFUSED line). Do NOT commit `DATA_CATALOG.yaml`.
3. Run the three criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. No `catalog_entries/` row, no registry file, no `DATA_CATALOG.yaml` commit, no gateway app or test file, no portal file, no tool, grant, route, role, `.env` or AWS change. No deploy. No push.
2. No firm or product name is typed as a whole-string literal in code (the naming gate refuses a NEW hand-kept firm or product token); `STOP` words and the field name are fine.
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
4. The checks are `deliverables/2.0.0_SA_COO~MI/round17/checks/t1.AC1.sh`, `t1.AC2.sh`, `t1.AC3.sh` (python `t1_check.py`). Read `t1_check.py` for exactly what is graded. Do not edit them. Another worker (`~43`) edits `emit_catalog_v02.py` in other functions at the same time; keep your change to the helper, its three call sites and the constants you add, so the merge is hunk-disjoint.
5. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/derive_nl_tags.py
workflows/atom_decomposition/tests/
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~42/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W42-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-18" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/checks/t1.AC1.sh; echo "exit=$?"</invocation><expect>DENOMINATOR rows 304; with a non-empty nl_tags 304 of 304 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-18" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/checks/t1.AC2.sh; echo "exit=$?"</invocation><expect>DENOMINATOR base rows 304, new rows 304; empty in the base 44; marked inferred now 44; the inferred set is exactly the 44; every row that had tags keeps them byte-equal with no basis mark -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-18" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/checks/t1.AC3.sh; echo "exit=$?"</invocation><expect>DENOMINATOR inferred rows 44; bad 0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~42/NFRA_MCPINDEX.TO-MX-c-18.nl-tags-on-every-catalog-row.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance.
2. APPEND `<status>complete</status>` only if all three criteria PASS (if the commit gate refuses the flip, leave it and say so).
3. Commit your files together through `.tools/safe-commit.sh` (never `DATA_CATALOG.yaml`).
4. Report once, with:
   - the module and the helper by function, and the three call sites;
   - three of the derived tag lists (one harvest row, one table row, one older row), no more than 12 lines;
   - the AC1 and AC2 DENOMINATOR lines, the unit-test count and your commit sha.

The issuer then merges, regenerates the catalog, runs the gateway suite by failing-ID delta and lands the catalog through the lane that owns the gateway folder.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 17, worker ~42, parallel to `MX-c-19` (the same emitter file, other functions; each adds its own test file). Source: `ledger/ROUND_ANALYSIS.round12-16.md` ruling 1 (CTO msg 34404) and the CVO's Z-C-S57. The 44-row set was measured on the deployed catalog blob `e5096b5d6c` (`1b18b94979`): 32 harvest, 2 silver table, 10 older. Base dry-runs 2026-10-15: `t1.AC1` FAIL (260 of 304), `t1.AC2` FAIL, `t1.AC3` FAIL (module absent), as expected. Planted arms: `plant_t1.py` 11 of 11 (a reference derive module and a good catalog pass all three; an untouched base, one empty row left, an altered contract-tagged row, a tag word outside the row's text, a missing basis mark and a non-deterministic module each fail the criterion that grades them). The two plain-words discover reads (one G2 client table, one G6 news table) are the issuer's, after `MX-r-14`.

<status>issued</status>
<round>17</round>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
