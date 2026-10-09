# TO MDPF_STRATID.TO-W2-2 -- workstream 2 ST-w-2: one shared strategy matcher reading the ETF list and the name rules as data
<to_id>MDPF_STRATID.TO-W2-2</to_id>
<project>MDPF_STRATID</project>
<issued_to>0.9.0_WK_MDPF_STRATID~5</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>2</workstream>
**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `ST-w-2` (`decompositions/MDPF_STRATID_DECOMP_W2.md`) | **outcome_ref:** FWD-5, FWD-4 |
**depends_on:** none (builds against the list contract below)

---

## WORKER FACE

### THE CELL

`ST-w-2`. Today the decision "which Opal strategy is this sleeve?" is code: `OPAL_SMA_NAME_RULES` and `opal_sma_member_of` in
`data/assets/scripts/silver/rebalancer_schemas.py:205-233` (read it), called by `build_cottonwood_mdpf_slice.py:651,726,760`,
`build_cottonwood_mdpf_pair.py:148` and `build_dim_model_portfolio.py:324` (all under `data/assets/scripts/gold/`). Other hard-coded
copies of the Opal ETF tickers exist (e.g. `data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py:62`,
`data/mdpf/scripts/gold/mdpf_aggregate_aua.py:83`). You build ONE matcher that reads the list and rules as DATA, make
`opal_sma_member_of` delegate to it with exactly today's answers, and write down every hard-coded copy.

**The list (the contract; another worker is adding these keys to `infra/aws/etfs/config/etf_universe.json` in parallel):**
```
{"tickers": ["DIVZ","IDVZ","PFDE","PFOE"],
 "full_names": {"PFDE": {"name": "<full fund name>", "source": ".."}, ...},
 "sma_name_rules": [{"member": "pfde", "pattern": "Pathfinder\\s+Disciplined", "source": ".."},
                    {"member": "pfoe", "pattern": "Pathfinder\\s+Focused\\s+Opportunit", "source": ".."},
                    {"member": null, "pattern": "<matches Opal_Muni_Income>", "source": ".."}]}
```
Put a copy with these keys in your worktree's `infra/aws/etfs/config/etf_universe.json` only if you need it to run the seam locally,
and do NOT commit that file (it is not in your grant); your tests build their own dict.

**Build `data/assets/scripts/silver/opal_strategy_matcher.py`:**
- `StrategyMatcher(cfg: dict)`. Rules, all case-insensitive: each ticker in `cfg["tickers"]` as a WHOLE WORD (boundary = not a letter
  or digit; so `IDVZ` never hits `DIVZ`) -> member = the ticker lower-cased; each `full_names[T]["name"]` (whitespace-flexible) ->
  `T.lower()`; each `sma_name_rules` row -> its `member` (may be `None`).
- `.member_of(name) -> str | None`: non-str -> None; two DIFFERENT non-null members hit -> `raise ValueError` (today's behaviour); a
  null-member rule hit alone -> None.
- `.hit(name) -> dict | None`: `{"member": <str|None>, "rule": "<which rule>"}` so a caller can tell "matched a not-counted rule"
  from "matched nothing".
- `load_strategy_config(s3=None)`: reads `s3://opal-data-etfs/config/etf_universe.json`; unreadable -> RAISE (fail closed, never fall
  back to code constants).
- In `rebalancer_schemas.py`, replace the regex block so `opal_sma_member_of(name)` keeps its signature and returns exactly today's
  answers through a `StrategyMatcher`. The config it uses is passed in by the caller or set once at module level; wiring the S3 read
  into the running pipeline is NOT this cell (the issuer does it later). Keep the comment's Andrew-direct provenance.

**Census** `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~5/IDENTITY_COPY_CENSUS.md`: search the repo for every
hard-coded copy of the Opal ETF tickers or strategy-name rules (`comp-find` with the ticker names and `OPAL_`), then a line
`DENOMINATOR: <n>` and a table `| path:line | what it decides | REPLACED or KEPT | reason |`, one row per copy. KEPT is right for a copy
that decides something other than STRATEGY identity (e.g. a direct ETF holding flag, an ownership producer's universe); say which.

**Tests** `data/assets/scripts/silver/tests/test_opal_strategy_matcher.py` with exactly these test names:
`test_today_rules_unchanged` (PFDE, IDVZ-not-DIVZ, "Pathfinder Disciplined ..." -> pfde, "Pathfinder Focused Opportunity" -> pfoe, a
plain name -> None), `test_two_hits_raise`, `test_new_ticker_in_list_found_without_code_edit` (add e.g. `ZZZQ` to a dict copy ->
`zzzq`), `test_full_name_matches`, `test_data_rule_row_found_without_code_edit`, `test_null_member_rule_is_flagged_not_counted`,
`test_rebalancer_schemas_delegates_to_the_matcher`.

### ACCEPTANCE

<criterion id="W2-2-AC1" cell_refs="ST-w-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_2_tests.py</invocation><expect>W22-OK</expect></criterion>
`W2-2-AC1` -- the seven named tests pass. At the base: `W22-BAD no file ...`.

<criterion id="W2-2-AC2" cell_refs="ST-w-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_2_seam.py</invocation><expect>W22-SEAM-OK</expect></criterion>
`W2-2-AC2` -- SEAM on real data: over the 362 distinct names in Cottonwood's Rebalancer silver (latest date), the matcher gives the
same member as today's rules; any GAINED member is printed (allowed only for a full-name or rule hit); any CHANGED member fails. It
builds the matcher from `infra/aws/etfs/config/etf_universe.json` in your worktree (the contract's keys). At the base:
`W22-SEAM-BAD matcher not importable`. Read-only S3.

<criterion id="W2-2-AC3" cell_refs="ST-w-2"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_2_census.py</invocation><expect>W22-CENSUS-OK</expect></criterion>
`W2-2-AC3` -- the census exists, its DENOMINATOR equals its REPLACED/KEPT rows. At the base: `W22-CENSUS-BAD no file ...`.

<expected_criteria>W2-2-AC1 W2-2-AC2 W2-2-AC3 W2-5-AC1 W2-6-AC1 W2-6-AC2</expected_criteria>

Run each invocation from your worktree root.

### AMENDMENT A5 (issuer, 2026-10-09 ~05:3xZ) -- cell `ST-w-5`, continued by this slot on its branch

Your first pass is complete and stands. This amendment adds cell `ST-w-5` (decomposition amendment A5). Re-flip `<status>` to
`complete` only when every criterion in `<expected_criteria>` passes.

`ST-w-5`. Your row `MDPF_STRATID-D1-W5-S1` is right: `rebalancer_schemas.py` now imports `opal_strategy_matcher.py`, and six carriers
ship the first without the second. Make each carrier ship the matcher too, beside `rebalancer_schemas.py`, in that carrier's own
form (a tuple row in a build script, a manifest entry with the same fields its neighbour carries, a list entry). Deploy nothing,
build nothing, upload nothing.

The six carriers:
1. `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py` (line ~169, the `("rebalancer_schemas.py", ...)` row)
2. `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/mdpf-gold-lambda.BUILD_MANIFEST.json` (line ~178; if the manifest carries a content
   hash for each file, compute the matcher's the same way the neighbour's was computed and say how in your report)
3. `infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/BUILD_MANIFEST.json` (line ~10)
4. `infra/aws/lambda/investor-reporting/performance/build_tools/build_candidate.py` (line ~57)
5. `infra/aws/lambda/investor-reporting/PATH_MANIFEST.json` (line ~148)
6. `.tools/safe_deploy_core.py` (line ~500, the silver script list)

Read each file around the line first; match its exact pattern. If a carrier turns out not to ship `rebalancer_schemas.py` as code
(only documents it), leave it, and say so in the report. Then, as the disarm proof, run the gold lambda's build in a DRY form if
`build_package.py` has one (`--help` first); if it has none, skip that and say so.

The check lives in the shared tree: run it with this absolute path from your worktree root (it reads your worktree's files).

<criterion id="W2-5-AC1" cell_refs="ST-w-5"><invocation>python C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_5_ship.py</invocation><expect>W25-SHIP-OK</expect></criterion>
`W2-5-AC1` -- every carrier that ships `rebalancer_schemas.py` ships the matcher. On your branch now: `W25-SHIP-BAD 6 of 6 ...`.

### AMENDMENT A9 (issuer, 2026-10-09 ~14:4xZ, drain step 4) -- cell `ST-w-6`: the running path reads the S3 list

The shared list is live at `s3://opal-data-etfs/config/etf_universe.json` (byte-identical to commit 7a8a5e39ab; ledger
`mdpf-stratid-w2a-etf-universe-s3-dell1-20261009`), and the MDPF runner and gold-lambda roles are being granted `s3:GetObject` on that
key. Today `rebalancer_schemas.opal_sma_member_of` uses `OPAL_STRATEGY_CONFIG_SEED` unless a caller runs `set_strategy_config`.
Change `data/assets/scripts/silver/rebalancer_schemas.py` so that, when no caller has set a config, the FIRST call loads the config
with `opal_strategy_matcher.load_strategy_config()` (once per process, cached) and builds the matcher from it; an unreadable config
RAISES (fail closed, no fallback to the seed). Set a module attribute `STRATEGY_CONFIG_SOURCE` to
`"s3://opal-data-etfs/config/etf_universe.json"` when the S3 config is loaded (and to `"set_strategy_config"` when a caller sets
one). `set_strategy_config(cfg)` and the `cfg=` argument keep winning. The seed may stay only as test data, never as a runtime
fallback. Do not edit the five callers.

**Tests** `data/assets/scripts/silver/tests/test_opal_strategy_wiring.py` with exactly: `test_default_reads_s3_config_on_first_use`,
`test_s3_config_loaded_once_per_process`, `test_unreadable_config_raises`, `test_set_strategy_config_overrides_the_s3_default`,
`test_cfg_argument_still_wins` (stub S3; no network in tests).

<criterion id="W2-6-AC1" cell_refs="ST-w-6"><invocation>python C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_6_tests.py</invocation><expect>W26-OK</expect></criterion>
`W2-6-AC1` -- the five named tests pass. At the base: `W26-BAD no file ...`.

<criterion id="W2-6-AC2" cell_refs="ST-w-6"><invocation>python C:/Dev/ajb_workspace/org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_STRATID_S1/W2_CHECKS/w2_6_live.py</invocation><expect>W26-LIVE-OK</expect></criterion>
`W2-6-AC2` -- SEAM on real S3 (read-only, under your own credentials): with no config set, the module reads the S3 list, and over
the 361 real Cottonwood names its answers equal the matcher built from the repo file. At the base:
`W26-LIVE-BAD STRATEGY_CONFIG_SOURCE=None`.

Re-run the four earlier criteria too. Re-flip `<status>` to `complete` only when all six pass. **No deploy:** the issuer opens a
change-management entry before merging this branch, because a `box/dell1` push uploads silver scripts the runner syncs.

## BOUNDS

- **GUARD 1:** no deploy of `mdpf-gold-lambda` or any script, and no write to the ETF universe config, before the 2026-10-09 13:30Z
  read. You write nothing in AWS; read-only S3 is allowed.
- Do not edit the five callers of `opal_sma_member_of`; they keep working through the unchanged signature.
- **Grant.** The `<paths>` block plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_STRATID-W2-W5-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below. Rows are APPEND-ONLY.

<paths>
data/assets/scripts/silver/opal_strategy_matcher.py
data/assets/scripts/silver/rebalancer_schemas.py
data/assets/scripts/silver/tests/test_opal_strategy_matcher.py
data/assets/scripts/silver/tests/test_opal_strategy_wiring.py
org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~5/IDENTITY_COPY_CENSUS.md
org/missions/D8/MDPF/MDPF_STRATID/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py
infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/mdpf-gold-lambda.BUILD_MANIFEST.json
infra/aws/lambda/opal-assets/opal-assets-silver-blackdiamond/BUILD_MANIFEST.json
infra/aws/lambda/investor-reporting/performance/build_tools/build_candidate.py
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
.tools/safe_deploy_core.py
</paths>

The block is your WRITE grant (paths relative to your worktree root are the same files). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_STRATID/decompositions/MDPF_STRATID_DECOMP_W2.md</decomp_doc> (workstream 2), cell `ST-w-2`.
<owned_cells>ST-w-2 ST-w-5 ST-w-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: W2-2-AC1, W2-2-AC2, W2-2-AC3. Instance at `org/missions/D8/MDPF/MDPF_STRATID/deliverables/0.9.0_WK_MDPF_STRATID~5/MDPF_STRATID.TO-W2-2.shared-strategy-matcher.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> W2-2-AC1 W2-2-AC2 W2-2-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the matcher's API as built, the seam's DENOMINATOR/same/gained/changed line, the census DENOMINATOR and REPLACED/KEPT
counts, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE nothing wired into a running path in this cell (ruling W5).
comp-iam: DECLARED-NOT-APPLICABLE read-only S3 under the worker's credentials; the runner role's config read is a drain act.
comp-adversary: DECLARED-NOT-APPLICABLE hazard recorded in the decomposition battery (fail closed on an unreadable config).
risk: WORLD (gate floor once amendment A5 added infra/ and .tools/ ship lists) -- code, tests and ship lists on a branch; nothing merges before the 13:30Z read (ruling W1).
direct_act: false -- workstream issuance with shared contracts.
</preflight>

Source: PRD ADDENDUM v0.4 @c690447ee7 (S01; GUARD 1, GUARD 2); C-SLEEVE, C-ONE-LIST, C-SMA-RULES; decomposition rulings W1-W5.
