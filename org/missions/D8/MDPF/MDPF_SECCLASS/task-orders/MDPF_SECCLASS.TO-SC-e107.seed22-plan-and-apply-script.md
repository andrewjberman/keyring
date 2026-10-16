# TO MDPF_SECCLASS.TO-SC-e107.seed22-plan-and-apply-script -- round 27 SC-e-107: the 22-row canonical seed from the old list: a read-only PLAN, an APPLY that a CloudOps seat runs later under a signed pair, and a selftest (nothing is written)

<to_id>MDPF_SECCLASS.TO-SC-e107</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~97</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>27</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SC-e-107` (`decompositions/MDPF_SECCLASS_DECOMP_R27.md`) |
**outcome_ref:** FWD-1 / FWD-5 (the 22 old-list-only tickers) | **depends_on:** none | **source:** CTO round-26 analysis section 2 and 3 item 1 (msg 6482); row MDPF_SECCLASS-D1-S42

---

## WORKER FACE

### THE CELL

`SC-e-107`. The shared classification list is the DynamoDB table `etf-classifications` (us-east-1, key `ticker`). The OLD list is `bd-securities`. Measured 2026-10-16: **22 tickers ($413,341.59 on the `gold/holdings_lots/2026-10-09.parquet` lots) are in the old list and NOT in `etf-classifications`** (the committed baseline is `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/seed22_candidates_20261016.json`: ticker, market value, old-list class). The CTO ruled (round-26 analysis): the old-list classes are ACCEPTED as source rows, each seeded canonical row carries its provenance (`source_table` = `bd-securities` and `source_last_updated` = that old row's own `last_updated`), and the seed is a served change under a never-widen pair that a CloudOps seat applies. **This cell builds the script and the plan; you write NOTHING to S3 or to any table.** The existing machinery already does the classification: `infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py` has `plan_rows(candidates, vocab=..., existing_tickers=..., bd_securities_lookup=..., updated_by=...)` (about line 492) which takes the old-list row as its first source (tagged legacy-fork) and folds it against the canonical vocabulary, `TableVocabulary.from_live_table`, `existing_tickers`, `default_bd_securities_lookup(table_name)` (about line 595) and `write(plan)` (a conditional put, `attribute_not_exists(ticker)`). E_18 never feeds these 22 to `plan_rows` because it skips every pair whose key is in the old list; the seed is that same call made once for them.

**What you build:**
1. Read the shared module's `plan_rows`, `existing_tickers`, `TableVocabulary`, `default_bd_securities_lookup`, `write` and the tag it sets for a legacy-fork row, and E_18 (`data/black_diamond/scripts/gold/E_18.detect_new_securities.py` lines 189-300) to see how they are called.
2. Write ONE script, `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/seed22.py`, run from the repo root, with three subcommands (import the shared module by adding `infra/aws/lambda/v2_portal/_shared` to `sys.path`; never copy its code):
   a. `plan --out <file>`: READ-ONLY. Candidates = the 22 tickers of the baseline file, each with an `asset_name` read from the 2026-10-09 lots partition (`s3://opal-data-bd/gold/holdings_lots/2026-10-09.parquet`, columns `ticker`, `asset_name`, `market_value`, `is_open`; one name per ticker, the one with the largest open market value). Call `plan_rows` with `bd_securities_lookup=default_bd_securities_lookup('bd-securities')`. Write the plan file `{"firm": "49financial", "read_at": "<UTC>", "candidates": [<22 tickers>], "planned": [{"ticker", "market_value", "row": {...the row plan_rows built, plus source_table, source_last_updated...}}], "unresolved": [{"ticker", "reason", "market_value"}], "seed_pending": [{"ticker", "reason", "market_value"}], "mv_by_class": {<asset_class>: dollars of the planned tickers}}`. Every one of the 22 is in exactly one of `planned`, `unresolved`, `seed_pending`; the market values are the baseline file's. `source_last_updated` is copied from the old-list row's `last_updated` (read the old row with a `get_item`). The old list's `needs_review` sub-class (PCEF is such a row) is NOT a canonical sub-class: if `plan_rows` leaves it in `unresolved`, report it there with its reason, never fold it yourself.
   b. `apply --plan <file> --pair <path>`: writes each `planned` row by the shared module's `write` (or, if `write` drops the two provenance attributes, by a conditional `put_item` with `ConditionExpression='attribute_not_exists(ticker)'` that you write in this script, and say which in the report). It REFUSES (exit 2, nothing written) when `--pair` does not name an existing file, when the plan file's `firm` is not `49financial`, or when any planned ticker already has a canonical row; it prints `SEED22-APPLY written=<n> refused=<m>` and each refused ticker. **You never run `apply` against AWS.**
   c. `selftest`: NO AWS call. With stub tables, show: (i) `plan` on a three-ticker fixture (one resolvable old-list row, one with a `needs_review` sub-class, one already in the canonical stub) puts the first in `planned` with `source_table` and `source_last_updated`, the second in `unresolved`, and refuses the third; (ii) `apply` on the stub writes the planned row INCLUDING both provenance attributes and issues a conditional put; (iii) the DIFFERENCE CONTROL: `apply` with a missing `--pair` file writes nothing and exits 2; (iv) `apply` on a planned ticker already in the stub canonical writes nothing for it. Prints `SEED22-SELFTEST ok=True` only if all hold.
3. Run `plan` once for real (read-only AWS) to produce `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~97/SEED22_PLAN.json`; it reads a 50 MB partition and two tables, so run it with `run_in_background` if it nears the 120 s bound, and read its output when it ends.
4. Nothing else. Do not edit the shared module, E_18, any gold script or any check script.
**Report (not a criterion):** counts of planned / unresolved / seed_pending, the dollars by class, which of `write` or your own put `apply` uses and why, the legacy-fork tag value, and each unresolved ticker with its reason.

### AMENDMENT 1 (issuer, 2026-10-16 ~04:5xZ, the CTO's fold ruling): the plan seeds 13 and holds out 9

You are a RE-SEATED worker. Inherited state (already merged, in your tree): `seed22.py` with `plan`, `apply`, `selftest` (commit f0df5c57a9, merged @283e087af6) and `SEED22_PLAN.json` as the first run produced it (4 planned, 18 unresolved). Read both first. The CTO ruled (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_MDPF_SECCLASS_SEED22_FOLDS_20261016.md`): the 18 unresolved are not folded by `plan_rows`; 9 are SEEDED with a ruled class and 9 are HELD OUT as Unclassified. The ruling is committed as a MAP you read and never edit: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/seed22_fold_map_20261016.json` (`seed`: ticker -> rule, asset_class, sub_asset_class (null = no sub-class), note; `held_out`: ticker -> rule, reason).

**What you add:**
1. `plan --out <file> [--fold-map <file>]`. With `--fold-map`, the tickers that `plan_rows` cannot plan are resolved by the map: a ticker in `seed` becomes a `planned` entry whose `row` has the same field set the module's rows have (read how `plan_rows` builds a row and which fields `apply` writes), with `asset_class` and `sub_asset_class` from the MAP (a null sub-class means the attribute is OMITTED from the row; first read, read-only, how an existing canonical row with no sub-class is stored, for example one found by a scan with `FilterExpression=attribute_not_exists(sub_asset_class)` and `Limit` of a page, and do the same), `input` = `fold-map`, the two provenance attributes `source_table` = `bd-securities` and `source_last_updated` = the old row's `last_updated` (as before), plus `fold_rule` (the map's rule), `fold_note` (the map's note) and the old row's own `source_asset_class` and `source_sub_asset_class` for audit. A ticker in `held_out` goes to `seed_pending` with the map's reason and its baseline dollars and is NEVER planned. The four equity tickers that `plan_rows` already plans stay as they are. Result for the real plan: planned 13 (the 4 equity + the 9 `seed`), seed_pending 9, unresolved 0. A ticker that is in neither `plan_rows`' output nor the map stays `unresolved` (it must not occur; the check refuses it).
2. `apply` writes the new attributes (`fold_rule`, `fold_note`, `source_asset_class`, `source_sub_asset_class`) with the others, still by your own conditional put, and never writes a `seed_pending` entry.
3. Extend `selftest` (it must still print `SEED22-SELFTEST ok=True`) with: (vi) a map fixture: a seeded ticker gets the MAP's classes, the provenance and the `fold_*` attributes; a null sub-class omits the attribute; a held-out ticker lands in `seed_pending` and `apply` writes nothing for it; (vii) the OVERRIDE case: a seeded entry whose note starts with `OVERRIDE` keeps that text in `fold_note` of the planned row.
4. Re-run `plan --fold-map` once for real (read-only AWS) and overwrite `SEED22_PLAN.json`.
5. Update the proof-of-spec instance to carry `SC27-e107-AC1`, `SC27-e107-AC2` and `SC27-e107-AC3`, and re-validate it with all three.

### AMENDMENT 2 (issuer, 2026-10-16 ~05:1xZ): the check defect is fixed; close the order

Your predecessor's last run read AC2 FAIL because `check_seed22_plan.py` demanded a non-empty `sub_asset_class` on every planned row, which the fold ruling forbids for HPI, LCFYX, PFF, VRP and CPXIX (the issuer's defect, row D1-W97-S2). The check is amended at HEAD (it still requires an `asset_class` and the provenance on each planned row). **What you do, and nothing else:** (1) run the three acceptance invocations once under `timeout 120` and record each output verbatim; (2) in the proof-of-spec instance set the `SC27-e107-AC2` row's `status` to PASS with the new output in `output_evidence` (keep the old FAIL text in the evidence as history, say that the issuer amended the check), and replace every `PENDING-THIS-COMMIT` in `artifacts_produced` by the real hash of the commit that landed that file (`7db826a659` for `seed22.py`, `SEED22_PLAN.json` and the investigation file); (3) re-validate with `python .tools/proof-of-spec-check.py <instance> SC27-e107-AC1,SC27-e107-AC2,SC27-e107-AC3` (rc 0); (4) set this order's `<status>` to `complete` (every mechanical criterion PASSES) and commit the instance and the order file together. Change no script, plan, check, map or baseline.

### ACCEPTANCE

<criterion id="SC27-e107-AC1" cell_refs="SC-e-107"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/seed22.py selftest</invocation><expect>SEED22-SELFTEST ok=True</expect></criterion>
`SC27-e107-AC1` -- the stub run shows the plan, the provenance attributes, the conditional put and the refusals, including the difference control (iii).

<criterion id="SC27-e107-AC2" cell_refs="SC-e-107"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/check_seed22_plan.py org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~97/SEED22_PLAN.json</invocation><expect>SEED22-PLAN ok=True</expect></criterion>
`SC27-e107-AC2` -- the real plan covers exactly the 22 baseline tickers once each, every planned row carries provenance equal to the live old row, none is in the canonical table now, and the dollars equal the baseline total within $1.

<criterion id="SC27-e107-AC3" cell_refs="SC-e-107"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/check_seed22_fold.py org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~97/SEED22_PLAN.json</invocation><expect>SEED22-FOLD ok=True</expect></criterion>
`SC27-e107-AC3` -- (amendment 1) the plan seeds exactly the 4 equity tickers and the map's 9, holds out exactly the map's 9, leaves nothing unresolved, takes each seeded class from the map, records the HODL override, and carries the dollars of the baseline.

<expected_criteria>SC27-e107-AC1, SC27-e107-AC2, SC27-e107-AC3</expected_criteria>

Dry-run at the base (dell1 box/dell1 HEAD, 2026-10-16 ~04:5xZ): AC1 FAILS as expected (the script is absent); AC2 FAILS as expected (`SEED22-PLAN ok=False file=ABSENT`, rc 3). AMENDMENT 1 base: AC3 FAILS as expected on the merged first plan (`SEED22-FOLD ok=False planned=4 seed_pending=0 unresolved=18`); the check's green arm (a plan built from the map, 13 planned, 9 pending) read `ok=True`, its negative arm (the HODL override note removed) read `ok=False ... HODL override not recorded`. The check's own green arm (a plan generated from the live old-list rows, 22 planned) read `ok=True dollars=413341.59`; its negative arm (one row without `source_table`) read `ok=False ... KAMIX provenance`.

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch). pandas, pyarrow and boto3 are already installed.
- **AWS is READ-ONLY** (get, list, head, query, scan, list_object_versions): no write to any bucket or table, no deploy, no invoke. Never push.
- **`apply` is built and selftested, never run against AWS by you.** A write to `etf-classifications` is a served change that only a CloudOps seat makes, after a signed pair.
- **Never edit** anything outside the `<paths>` block; the check scripts under `R27_CHECKS/` are READ-ONLY to you. Never push.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and file a surprise row (id `MDPF_SECCLASS-D1-W97-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing). Do not weaken a check, and do not edit a check to make it pass.
- Run every invocation under `timeout 120`; the checks end well inside it.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/seed22.py
org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~97/SEED22_PLAN.json
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R27.md</decomp_doc> (round 27), cell `SC-e-107`.
<owned_cells>SC-e-107</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC27-e107-AC1, SC27-e107-AC2, SC27-e107-AC3. Write the instance at
`org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~97/MDPF_SECCLASS.TO-SC-e107.seed22-plan-and-apply-script.proof_of_spec.json`.
Validate it BEFORE the flip with `python .tools/proof-of-spec-check.py <instance> SC27-e107-AC1,SC27-e107-AC2,SC27-e107-AC3`.
</proof_of_spec>

**REPORT:** the counts, the dollars by class, `write` or own put and why, the legacy-fork tag value, each unresolved ticker with its reason, each criterion's output verbatim, commits, rows.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing is scheduled; nothing ships.
comp-iam: DECLARED-NOT-APPLICABLE only the reads the seat's role already makes.
comp-adversary: RUN -- a plan whose provenance is typed rather than copied from the old row (the check compares it with a live read); an `apply` that overwrites a canonical row (selftest (iv), and the conditional put); a fold of the `needs_review` sub-class by guess (forbidden: it stays unresolved); BLIND: a canonical vocabulary change between the plan and the apply (the apply refuses a ticker that now has a row, and the pair's GO re-reads the plan).
lane: the <paths> block IS the grant.
</preflight>

Source: CTO round-26 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_26_20261016.md`, msg 6482); DECOMP_R27.
