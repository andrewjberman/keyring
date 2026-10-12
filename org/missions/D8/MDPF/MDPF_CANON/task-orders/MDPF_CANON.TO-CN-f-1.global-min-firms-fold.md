# MDPF_CANON task order -- `CN-f-1` -- THE GLOBAL MIN-FIRMS FOLD: A GLOBAL PER-MODEL LINE IS SHOWN ON A DATE ONLY WHERE AT LEAST TWO FIRMS HOLD IT (fe9b, RULED A; FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-f-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~16</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the fold is a step inside the existing consolidator run and a refusal inside it, not a monitor.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is added to any script; the criteria read served objects with read-only get/list.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r6_cn_f_1.py contract 0 of 10, seams 0 of 6 and r6_cn_f_1_comparator.py 1 of 11 at base (arm K0 is a control); a reference tree reads 10 of 10, 6 of 6 and 11 of 11 (the arms can pass); three planted defects (the fold line never suppressed; pooled dollars dropped with the cell's own refusal disabled; a removed model's name left in free text) turn the comparator red on K6, K4+K5 and K7.
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-f-1` (round 6, decomposition v6)

**AMENDMENT 1 (2.0.0_SA_COO~D1, 2026-10-12 ~18:5xZ, the CTO's ADDENDUM 6, msg 4534):** one new behaviour, step 6a below. A day whose as-of
pool is held by fewer than two firms refuses Global whole instead of publishing a short Models node. AC1 now reads 13 arms (C11-C13 are new;
C6 plants a different two-firm world). Everything already built stays; add the refusal and its tests and re-run the three criteria.

**The rule (the cluster lead's ruling (A) and the CTO's ADDENDA 1-4, which you do not need to read).** The combined Global view lists per-model
lines. A line that only one firm holds is that firm's own book under a Global label. So Global shows a model-class line on a date ONLY where at
least TWO firms hold that model on that date; every model-class line held by fewer folds, on that date, into ONE line `other_models`, and that
line is itself shown on a date only where at least two firms hold it. What is not shown is not zero: it is absent (`None`), and the dollars that
left `by_model` are suppressed, not redistributed. Headline totals and every served JSON key stay as they are.

**Where it runs.** `data/mdpf/scripts/gold/mdpf_gold_consolidator.py`. `build_all` already runs
`arts = guard_global_served_identity(arts, _isolated)` (about :2701); read `assert_global_served_identity` and `guard_global_served_identity`
(about :2000-2057) first, they are the idiom. `arts` is a dict by scope: `arts["global"]` and `arts["49financial"]`, `arts["inflection"]`,
`arts["cottonwood"]`, each an aggregate-aua-timeseries document with `dates`, `by_model`, `model_aua` and the other headline arrays.
A `by_model` entry is `{"display_name", "cohort_class", "model_value": [..per date..], "account_count": [..per date..]}`
(an SMA entry may add `count_as_of`, `source_basis`). `cohort_class` is `"model"` for a model-class line, `"sma"` for an SMA line and for `tax`.

### Step 1 -- `apply_global_min_firms_fold` (a new module-level function, placed directly after `guard_global_served_identity`)

```
GLOBAL_FOLD_KEY = "other_models"
def apply_global_min_firms_fold(arts: dict, firm_scopes=FIRM_SCOPES, min_firms: int = 2) -> tuple   # (arts_out, report)
```

Behaviour, exactly:

1. `g = arts.get("global")`. When it is None or carries no `dates`, return `(arts, {"applied": False})` and touch nothing.
2. **Validate, fail closed.** Every `by_model` entry has `cohort_class` equal to `"model"` or `"sma"`, and `model_value` and `account_count`
   are lists of exactly `len(dates)`. Any violation raises `SystemExit` whose message STARTS `GLOBAL MIN-FIRMS FOLD REFUSED:` and names the
   line key and the fact, never a level or a total.
3. **Held.** A firm `f` in `firm_scopes` HOLDS a model-class key `k` on date index `i` of `g["dates"]` when `arts[f]["by_model"][k]["model_value"]`,
   read at the firm's OWN position of the same date string (the firm's `dates` axis can be shorter), is not None and is greater than 0. A firm
   scope that is None, a key the firm does not carry, and a date the firm does not have are not holdings. Nothing is a static list: the firm
   count is computed from these objects on every run.
4. **The as-of fold set.** `fold_keys` = the model-class keys held by fewer than `min_firms` firms on the LAST date of `g["dates"]` (a key with no
   value there, held by none, is in it). Sorted. A key not in `fold_keys` is KEPT as its own line.
5. **Per date `i`:** a model-class line is emitted individually on `i` only if it is KEPT and held by at least `min_firms` firms on `i`. Every
   other model-class line's value and count on `i` goes into the POOL for `i` (a key in `fold_keys` is pooled on every date it has a value, kept or
   not). `pool_value[i]` = the sum of the pooled non-None values, None when every pooled value is None; `pool_count[i]` likewise for counts;
   `pool_firms[i]` = the union of the firms holding any pooled line that has a value on `i`.
6. **The fold line.** On `i` the pool is EMITTED when `len(pool_firms[i]) >= min_firms`, as `by_model["other_models"] =
   {"display_name": "Other Models", "cohort_class": "model", "model_value": [...], "account_count": [...]}` with the pooled value (rounded to 2)
   and count on `i`. When it is not emitted both arrays hold None on `i` and the pooled dollars are the SUPPRESSED amount of `i`. Include the key
   only if it is emitted on at least one date. No `count_as_of`, no `source_basis`.
   **6a. A one-firm as-of refuses Global WHOLE (AMENDMENT 1, the CTO's ADDENDUM 6).** If on the LAST date the pool has a value
   (`pool_value[last]` is not None) and is NOT emitted because `len(pool_firms[last]) < min_firms`, `apply_global_min_firms_fold` raises
   `SystemExit` whose message STARTS `GLOBAL MIN-FIRMS FOLD REFUSED:` and names the as-of date and the number of firms holding the pool, never a
   dollar level. Do this check BEFORE building any output. `guard_global_min_firms_fold` (Step 2) isolates it: Global is refused whole, so
   its category views, aum-metrics and account distribution are not built or written for that run (never partially), the three firm scopes
   build as before, and the prior Global object stays served with its own as_of. A pool with NO value on the last date is not a refusal
   (there are no dollars to withhold). Dates before the last are never a refusal: they are suppressed as in step 6.
7. **Output.** A shallow copy `out` of `arts` whose `"global"` is a copy of `g` with `by_model` and `meta` replaced; every other scope is the
   SAME object. Nothing of `arts` is mutated. Keep the dict's key order rule (the keys are in sorted order today; keep it sorted).
   - `by_model`: the non-model-class entries (SMA lines, `tax`) are carried unchanged and are never folded; kept lines carry their arrays with the
     not-emitted dates set to None; `fold_keys` entries are removed; `other_models` as step 6.
   - `meta["by_model_channels"]`: drop the removed keys; add `other_models` = the sorted union of the removed keys' original channel lists.
   - `meta["by_model_fold"]` (a NEW key inside the existing `meta`; there is NO new top-level key): `{"min_firms": 2,
     "per_model_detail_begins": "<the first date any kept line is emitted, ISO>", "statement": "<plain English: per-model lines are shown on a
     date only where at least 2 firms hold the model; per-model detail begins <that date>, the first date Global combined 2 firms; lines held by
     fewer are folded into one Other Models line, itself shown only where at least 2 firms hold it>"}`. The statement names NO removed model.
   - Every other field of `g` (`model_aua`, `non_model_aua`, `tax_additive_aua`, `sma_additive_aua`, `opal_aggregate_aua`,
     `account_count_total`, `account_count_total_raw`, `count_as_of`, `count_basis`, `point_class`, `dates`, all of `meta` except the two keys
     above) is byte-equal to the input.
8. **The differential identity, fail closed.** For every date where `model_aua` is not None: `before = sum of the INPUT model-class lines' values`
   (None counts as nothing), `after = sum of the OUTPUT model-class lines' values (other_models included)`. Require
   `round(before - after, 2) == round(suppressed[i], 2)` where `suppressed[i]` is the pool's dollars on a date it was NOT emitted and 0.0 where it
   was. A pre-existing difference between `model_aua` and the sum of the lines (a rounding cent or two, measured on 208 of 485 dates) is carried
   by `before` and never trips the check: the test is the DIFFERENCE the fold made, not the absolute gap. On any violation raise `SystemExit`
   `GLOBAL MIN-FIRMS FOLD REFUSED:` with the count and up to five `(date, difference to the cent)`; no level.
9. **The report** (a dict, returned as the second value; the build logs it with dates and differences, never an account id):
   `applied` (True), `as_of`, `fold_keys`, `null_lines` = `{key: {"last_value": <last non-None value>, "last_value_date": <ISO date>}}` for every
   `fold_keys` entry with no value on the last date (a null line is printed WITH its dollars), `suppressed_dates` (the dates the pool had a value
   and was not emitted), `other_models_emitted_dates` (an int), `other_models_emitted_as_of` (bool), `identity_dates_checked` (the count of dates
   step 8 ran on), `identity_gap_dates` (0 on return), `first_per_model_date`, `flip_dates` (informational: for each kept key, the number of
   earlier dates held by fewer than `min_firms` while the last date is held by at least that; NOT a refusal, the per-date rule makes those dates
   the folded dates).

### Step 2 -- `guard_global_min_firms_fold` and the call in `build_all`

```
def guard_global_min_firms_fold(arts: dict, isolated) -> tuple      # (arts_out, report_or_None)
```
Return `(arts, None)` when `arts.get("global")` is None. Otherwise run `apply_global_min_firms_fold(arts)` through `isolated("global", ...)`
(the same idiom as `guard_global_served_identity`; it never catches an exception itself). When the isolation swallowed a refusal, return a
shallow copy of `arts` with `"global"` set to None and `None` as the report. In `build_all`, directly AFTER the
`guard_global_served_identity` line, add `arts, fold_report = guard_global_min_firms_fold(arts, _isolated)` with a one-line comment. Read every
statement from there to the point where `arts["global"]["by_model"]` is last used (the aum-metrics build, the shaping, the category views, the gold
parquet) and file a BLOCKING row, with the line, if any of them re-sums `by_model` or compares it with a headline total.

### Step 3 -- the other two global artifacts follow the same rule

3a. `data/mdpf/scripts/gold/dim_mdpf_account_distribution.py`: `build_firm_distribution(firm_id, firm_name)` gains two keyword parameters
`fold_keys=None, fold_emit=True`; every other caller is unchanged and `None` means no fold. For `firm_id == "global"` with `fold_keys` given,
remove those model keys from `by_model` and, when `fold_emit` is True, add ONE `other_models` entry built by CONCATENATING the folded keys'
per-account value vectors BEFORE the distribution statistics are computed (min, max, mean, median, percentiles and standard deviation cannot be
summed from per-model statistics; the histogram bin edges are the same for every model, so counts add). `account_count`,
`active_accounts_count` and `excluded_unfunded_count` equal the sums of the removed entries. `meta.account_count_by_model_key` and
`meta.cottonwood_fold.by_model_folded` drop the folded keys and gain `other_models`. `total` is unchanged. In `build_all` the global call
becomes `acct_dist.build_firm_distribution("global", "Global", fold_keys=tuple((fold_report or {}).get("fold_keys") or ()),
fold_emit=bool((fold_report or {}).get("other_models_emitted_as_of")))`. The staged object the aggregate builder reads for its FRONTIER counts
(`load_account_dist_frontier_counts`) must stay UNFOLDED: do not change what is staged; read how `gold/mdpf_revamp/global/account_distribution.json`
is written first and, if the fold would reach it, file a BLOCKING row.
3b. `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py`: add `"other_models"` to `MODEL_ORDER` (last) and `"other_models": "Other Models"` to
`SERVED_MODEL_NAME`. The row is built by the existing code from the folded series; its q0-q3 cells follow the existing honest-None law (a quarter
end the line is not shown on is an all-None triple, absent not zero). Do not edit `calc_metric` or `quarter_ends`.

### Step 4 -- register the fold line (the crosswalk, BOTH homes, one commit)

The category registry derives its model members from the crosswalk and refuses at import any model-class member the crosswalk does not hold
(`_check_crosswalk_keyspace`). So the fold line is a crosswalk row, in the shape of the nine Cottonwood custom models already there:
in `data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py` AND its second home
`infra/aws/lambda/opal-assets/opal-assets-daily-emitter/mdpf_revamp_model_crosswalk.py` (byte-equal files today; keep them byte-equal):
- append `ModelEntry("other_models", None, "Other Models", "model", False),` as the last row of `CANONICAL_MODELS`;
- append `"other_models": "Other Models",` to `GLOBAL_ACCOUNT_DIST_DISPLAY`.
It joins no `SERVED_MODEL_KEYS`, `CORE_MODEL_KEYS` or `BLEND_MODEL_KEYS` (no model id, no eclipse id, not served) and it is NOT added to
`GLOBAL_MODEL_KEYS` in `dim_mdpf_aggregate_aua_timeseries.py` (that tuple names leg-composed keys; the fold line has no leg). Do not edit
`mdpf_category_registry.py`. After the edit run `python data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py` (its self-test) and import
`mdpf_category_registry` and `dim_mdpf_aggregate_aua_timeseries` once each; report the result lines (not a criterion).

### Step 5 -- tests (new file, synthetic data, no network; idiom of `data/mdpf/tests/canon/test_global_served_identity.py`)

`data/mdpf/tests/canon/test_global_min_firms_fold.py`, at least SIX tests: (a) the fold set is computed from the objects (a key a second firm
also holds is kept); (b) `other_models` equals the sum of the pooled values and an all-None pool stays None, never 0.0; (c) the fold line is
suppressed on a date its pooled lines are held by one firm, in both arrays, and a kept line held by one firm on a date is None there;
(d) the differential identity tolerates a pre-existing 0.01 gap and refuses a planted loss; (e) a malformed array or an unclassified line is
refused with the prefix; (f) the guard returns `global` None with the three firm scopes the SAME objects and records the refusal; (g) a day whose
as-of pool is held by one firm is refused by the function and the guard (the message names the as-of date and carries no level), a two-firm
day builds and emits `other_models`, and a day whose pool has no value at the as-of builds; and the SMA
line and `tax` are carried byte-equal. Name the documents in the test with the real model keys of the world described in the issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round6/checks/r6_cn_f_1.py` (`_synthetic`; read it, never edit it).

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`/`rm`, no `safe-deploy`. Read-only `get`/`list`/`describe` is
   allowed (criterion AC2 reads four served objects). No install, no push. REFUSE, do not rescue. The deploy of this code is CloudOps's, in its
   own window, after a never-widen pair; none of it is yours.
2. Only the files in section 3 change (plus your deliverables and the surprise channel). `apply_taxsma_overlay`, `apply_sma_sleeve_overlay`,
   `assert_global_served_identity`, `_cottonwood_sidecar`, `build_global_artifact`, the category registry and every existing test are read-only.
3. **Never** loosen, wrap or skip an existing assertion to make a criterion pass, and never print a client level: the refusal and the report carry
   dates, counts and differences, and the null lines' last values the report names (that is the one place a dollar is printed, by ruling).
4. **Never** make the SMA lines or `tax` part of the fold (they are outside `model_aua`; a `by_model` entry carries one `source_basis`); the three
   SMA-class lines `opal_div_sma`, `opal_growth_sma` and `pfde` stay exactly as they are.
5. **No new top-level key** in any served object, and no new key of any kind outside `meta.by_model_fold`, the `other_models` line itself and
   the `other_models` entries of the two maps named in Step 3a.
6. **CLIENT DATA:** never print an account id. No non-ASCII. Keep each file's line endings as you find them (read them first). Use the Edit tool.
7. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
data/mdpf/scripts/gold/mdpf_gold_consolidator.py
data/mdpf/scripts/gold/dim_mdpf_account_distribution.py
data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py
data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py
infra/aws/lambda/opal-assets/opal-assets-daily-emitter/mdpf_revamp_model_crosswalk.py
data/mdpf/tests/canon/test_global_min_firms_fold.py
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-f-1.global-min-firms-fold.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~16/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `data/mdpf/scripts/gold/mdpf_category_registry.py`,
`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` (the ts builder; `build_global_artifact` and `GLOBAL_MODEL_KEYS`),
`data/mdpf/tests/canon/test_global_served_identity.py` (the idiom) and the issuer's checks under
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round6/checks/` (`r6_cn_f_1.py`, `r6_cn_f_1_comparator.py`; never edit them,
read what each arm asserts).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-f-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round6/checks/r6_cn_f_1.py" contract; echo "exit=$?"</invocation><expect>ROUND 6 CONTRACT: 13 of 13 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-f-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round6/checks/r6_cn_f_1_comparator.py"; echo "exit=$?"</invocation><expect>ROUND 6 COMPARATOR: 11 of 11 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-f-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round6/checks/r6_cn_f_1.py" seams; echo "exit=$?"</invocation><expect>ROUND 6 SEAMS: 6 of 6 arms -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="CN-f-1" judgment="true"/>
</proof_of_spec>

AC4 is JUDGMENT, graded at the round-6 close (never self-graded): `/seams` on the fold-to-served seam, grounded on the objects after the first
scheduled run that carries the code -- MECHANICAL (the four global objects read back hold no model line held by fewer than two firms on any date
they carry), DECLARATIVE (the in-band statement says why per-model detail begins when it does, and names no model), SEMANTIC (the only
client-visible deltas are the ones the never-widen pair names: the two inflection blends leaving the Model Portfolios roll-up and the Total
Holdings count, and per-model history starting where Global first combined two firms).

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~16/MDPF_CANON.TO-CN-f-1.global-min-firms-fold.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for), with AC4 UNVERIFIABLE-BY-INSTRUMENT and status_reason
"graded at the round-6 close". **Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the order file is in your
paths), and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W16-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the diff (one line per file), the output line of every criterion, the crosswalk self-test line, the lines you read for the Step 2
consumers check, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 6, issuer 2.0.0_SA_COO~D1, on the CTO's round-5 analysis `ledger/ROUND_ANALYSIS.round5.md` @7cbc4492c0 section 3 item 1 and the
record `org/tier1_exec/1.0.0_SA_CTO/deliverables/RECORD_FE9B_RULED_BY_CLUSTER_LEAD_20261012.md` ADDENDA 1-5 (@25f1d760e5 for ADDENDUM 5, msg 4439).
Design: `deliverables/2.0.0_SA_COO~D1/round6/FOLD_DESIGN.md` @2f702bb7ff with its CORRECTION notes, `FOLD_ADDENDUM2_READ.md` @01b9e95401. Input: row
D1-W8-S5 (disarms on this cell's read-back); open call dell1-20261011T053810Z-fe9b, ruled (A) by the cluster lead.
- **Corrections to the design the face carries, both measured:** (1) the fold line is a crosswalk row in BOTH homes (the registry raises at import on
  a model-class member the crosswalk lacks, `mdpf_category_registry.py:773-804`); (2) the pre-fold `model_aua - sum(lines)` residual is a cent or two
  on 208 of 485 valued dates, so the identity is asserted as the DIFFERENCE the fold makes (ADDENDUM 5 item 1, which also requires the build to print
  the pre-existing residual with its denominator, 208 of 485: the cell's report carries `identity_dates_checked` and the issuer's comparator prints it).
- **Rulings the face implements:** ADDENDUM 5 item 2 (flips are reported, never refused on; refusal is on the differential and the per-date 2-firm
  assertion), item 3 (the 10 absent core quarter cells are accepted into the pair), item 4 (WORLD class, the emitter package named in the deploy order).
- **The pair (CTO + COO, written at the drain by the issuer, never by the worker)** names: blast radius = the four global aggregate objects and the
  global gold parquet partitions FROM THE FIRST NEW-DATE FIRE ONWARD (no firm scope, no staged object, no dated key already served; no retro-fold, the
  reader read found no served reader of a pre-fold dated object); N = 8 writers across 7 leaf classes; the three branches (pass publishes; refusal
  leaves the prior Global object served and the firm scopes publish; a fault is the same); the per-key rollback (the prior object's version id); the
  accepted client-visible deltas (Total Holdings -185, archetype cards -$43.16M, per-model trend and the core quarter cells beginning 2026-05-15) and,
  per the CTO's C-S65 ruling, every routine STATE write of an on-demand gold run with its prior VersionId as rollback, naming
  `mdpf/global/state/taxsma_control/current.json` first. The pair is the first to carry that clause and closes C-S65 on it.
- **Deploy order (CloudOps ~DELL1, a WORLD order the issuer cuts after the drain; never a worker):** the code lands by the CN-d-1 order's shape (named
  files through `safe-deploy.sh`, the gold package through `build_package.py --pin <the merge commit>` and a targeted `safe-apply` on
  `mdpf-gold-lambda`), in its OWN window, clear of FIRMBKTS's window acts and touching none of the router, guard, CloudFront behaviours,
  `bronze_homes.json`, `firm-config.mjs` or the WAF rider before FIRMBKTS's flip receipt (PRD v2.11 R2). Its plan also sets the function's
  `MDPF_GOLD_COMMIT` environment value from the pin actually built (row D1-S18, CTO round-5 item 3), and the order names whether the emitter lambda
  package is re-packaged for the second crosswalk home or the home lands as repo parity only. The on-demand run, if one is taken, is graded on the
  run manifest (AMENDMENT 3 of `ADHOC.canon-r4-code-deploy`: the A4 writer is write-once per dated key); the served-key read is the first scheduled
  fire that mints a new date.
- **Open, not decided:** a pool of per-date-folded core dollars plus a trace of a second firm's custom line satisfies the union predicate; on the real
  history that never occurs (0 dates). The rule as worded would emit it.
- **Not provable offline, graded after deploy (AC4 and the pair's read-back):** the pooled account-distribution statistics (they need the
  account-level vectors from silver), the category-views Custom node, the gold parquet column set, and the Model Portfolios page on a missing key.
  The comparator's real-object arm covers the aggregate-aua-timeseries type only.
- **Risk and class:** WORLD (the cell changes served bytes once deployed; `<paths>` include an `infra/` file). `worker`, not light: about 200
  product lines, one behaviour, one cross-file contract (`fold_keys`).
- **Fanout:** one cell, one chain, slot ~16. Base box/dell1.
- **Checks at base (dry-run from `round6/checks/` before the cut):** `r6_cn_f_1.py contract` 0 of 10, `seams` 0 of 6, `r6_cn_f_1_comparator.py`
  1 of 11 (K0 is a control). A reference tree reads 10 of 10, 6 of 6 and 11 of 11; three planted defects turn it red.

<status>pending</status>
<round>6</round>
<to_id>MDPF_CANON.TO-CN-f-1</to_id>
<slot>~16</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
