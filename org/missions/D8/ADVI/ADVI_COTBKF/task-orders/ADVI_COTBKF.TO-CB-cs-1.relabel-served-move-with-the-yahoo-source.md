# TO ADVI_COTBKF.TO-CB-cs-1.relabel-served-move-with-the-yahoo-source -- round 97 CB-cs-1: re-run the as-traded regrade at the served settings with the current code, rebuild the three FWD-3 tables, prove every pre-existing column equals the SERVED one, and count the use_class and porting_verdict labels against the Yahoo-sourced prices; counts only

<to_id>ADVI_COTBKF.TO-CB-cs-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~187</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>97</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cs-1` (`decompositions/ADVI_COTBKF_DECOMP.round97.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** The three served FWD-3 tables (`daily_returns`, `account_day_value`, `month_grades`) are to gain two labelled columns, `use_class` and `porting_verdict`, so that a day priced from Yahoo is labelled as such (Andrew's call `3adb`: Yahoo-priced days stay, labelled interim). Round 96 rebuilt the tables from the run data and found every label reading `NOT_YAHOO`, because the served run (`r34`) was made before the regrade wrote a per-point `source` column into `security_day_price.parquet`; the builder reads Yahoo-ness from that column. The current code writes it, and the as-traded substitution keeps each point's own `yahoo_finance` / `linear_interpolation` label. So you re-run the regrade with the current code, rebuild from the new run, and show (a) the pre-existing columns still equal the SERVED tables (delta 0) and (b) the labels now mark the Yahoo-sourced prices. **This cell writes nothing to S3, serves nothing, changes no code and no committed file except your own record.**

**Inputs (READ-ONLY; absolute paths).**
- Received run data (off git, gitignored): `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/`. You use `cache` (the transactions cache, the builder's and regrade's `--cache`) and `yahoo_census` (the pinned Yahoo close cache: 3,580 files, sha256 over the sorted (name, file sha256) pairs `5b4bb7db3acde4b18f15b22bde58e3d4a27c1e690c5c601f7684bcf62e0cf3cb`, per `deliverables/0.9.0_WK_ADVI_COTBKF~106/PRICE_CACHE_PIN.json`). Your worktree has no `.scratch`, so pass every path explicitly.
- The private sweeps config: `C:/Users/Test/.opal/commonwealth_sweeps.json` (outside the checkout; it arrived over the box-to-box route and its sha256 was read equal by the issuer). Set the environment variable `COTBKF_SWEEPS_CONFIG` to it for the regrade (the loader refuses a file whose sha256 is not `b1d93408f64a996b2a9659bbed9ca0863fbf0d0db348e1397e1a7e184910a89d`). Never copy, print, quote or commit its contents.
- The served regrade's split store instant: `2026-10-09T11:52:52Z` (`deliverables/0.9.0_WK_ADVI_COTBKF~99/SPLIT_STORE_PIN.json`, `served_as_of`).

**Read first.**
1. `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.md` section 2: the recorded regrade command; its BASELINE leg reproduced the served returns (0 rows differing). You reproduce that leg with the paths below. The default price-basis census (`BASIS_CENSUS`, `0.9.0_WK_ADVI_COTBKF~60/price_basis_census.csv`) is the baseline's own census, so you need no wrapper.
2. `data/assets/scripts/silver/commonwealth_fwd3_serve.py` in your worktree (module docstring: `--build`, `--hold-cusips`, `--yahoo-active-policy`, `--cash-leg`, `--price-basis`; `target_addresses()`; `_read_served(uri)`) and `data/assets/scripts/silver/commonwealth_daily_valuation.py` (`write_prices`, `as_traded_store`, `YAHOO_SOURCES`).
3. Round 96's record, for the control you repeat: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~186/SERVED_MOVE_MEASURED_RECORD.json` and its `.md` (served rows 1,691,729 / 21,102,041 / 82,593; served `run_commit` `6f70d5cc01bb2e196266799a657be6d0b2dc8a16`; served VersionIds recorded there).

**The served settings (verify each against the records; a difference is a finding, not a free choice):** before arm `--before-list v1 --before-cash-leg method_r28 --before-price-basis store`; after arm `--after-list v1 --after-cash-leg method_r28 --after-price-basis as_traded`; hold list `05613L3H2,95000U2D4,651639AX4`; policy `interim`.

**Your items.**

1. **Receipt check.** Run `CB97cs1-AC3`'s invocation first (below) and keep its line. It reads the received folder's count and bytes (20,563 files, 4,478,568,892 bytes); the build output of this cell goes to a sibling directory, not into it.
2. **Regrade.** From your worktree root, with `COTBKF_SWEEPS_CONFIG` set, run (about 10 minutes; run it in the background under `timeout 2400` and wait for it, since a foreground call is limited):
   `python data/assets/scripts/silver/commonwealth_sweep_regrade.py --before-list v1 --after-list v1 --before-cash-leg method_r28 --after-cash-leg method_r28 --before-price-basis store --after-price-basis as_traded --data-dir C:/Dev/ajb_workspace/.scratch/cotbkf_r97/regrade --out C:/Dev/ajb_workspace/.scratch/cotbkf_r97/regrade_out --cache C:/Dev/ajb_workspace/.scratch/advi_cotbkf/cache --price-cache C:/Dev/ajb_workspace/.scratch/cotbkf_r97/price_cache --price-input-out C:/Dev/ajb_workspace/.scratch/cotbkf_r97/price_input.parquet --split-store-as-of 2026-10-09T11:52:52Z --yahoo-cache C:/Dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census`
   Record its printed pins (split store `as_of listed held sha256`; Yahoo cache files and sha256; price input rows and sha256) and `PRICE-BASIS` line. The new `after/security_day_price.parquet` must carry a `source` column. If the regrade refuses or fails, the refusal text verbatim is the finding: record `measured: false`, file one row, stop.
3. **Build.** `python data/assets/scripts/silver/commonwealth_fwd3_serve.py --build --data-dir C:/Dev/ajb_workspace/.scratch/cotbkf_r97/regrade --grades C:/Dev/ajb_workspace/.scratch/cotbkf_r97/regrade_out/month_grades_after.parquet --grades-before C:/Dev/ajb_workspace/.scratch/cotbkf_r97/regrade_out/month_grades_before.parquet --cache C:/Dev/ajb_workspace/.scratch/advi_cotbkf/cache --cash-leg method_r28 --price-basis as_traded --hold-cusips 05613L3H2,95000U2D4,651639AX4 --yahoo-active-policy interim --out C:/Dev/ajb_workspace/.scratch/cotbkf_r97/build` (about 9 minutes; background under `timeout 2400`). No `--apply`, no `blank` policy. A builder refusal is the finding, verbatim.
4. **The control.** As round 96 did: read the three SERVED tables from their builder addresses (S3 read-only, one get each; record each key's VersionId and LastModified and check they equal round 96's), compare every column the served table has with your build, row-aligned on the key (`daily_returns`: account, date; `account_day_value`: account, date, cusip; `month_grades`: account, month). `run_commit` is excluded and counted separately. Floats compare exactly first; report the largest absolute difference. Per table: served rows, built rows, columns compared, rows differing, `max_abs_diff`, `pre_existing_equal`. A `False` is the most important line: report it, do not repair it.
5. **The labels.** In your build, per table, count rows per value of `use_class` and of `porting_verdict`; for `account_day_value` also the distinct accounts with a `NOT_FOR_ACTIVE` row; for `account_day_value` the rows whose `price_source` names a Yahoo source (a `|`-split part equal to `yahoo_finance` or `linear_interpolation`), and the rows whose `use_class` is not `NOT_YAHOO`. In the new `after/security_day_price.parquet`: the distinct (cusip, date) pairs whose `source` names `yahoo_finance`, and those naming `linear_interpolation`. In the price input `price_input.parquet`: the rows with `source = yahoo_finance` and `basis = as_traded_close` (the replaced points; round 96's sidecar read 1,049,193) and the rows with `basis = as_traded_close` and `source = linear_interpolation` (the re-derived days; sidecar 477,980). Name which columns your build has that the served table lacks (expected: `use_class`, `porting_verdict`; any other is a finding). Say plainly where two of these counts differ and by how much; do not force them equal.
6. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~187/SERVED_MOVE_RELABEL_RECORD.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `received` (`{"files","bytes"}`), `regrade` (`{"price_basis_line","split_store_as_of","split_store_listed","split_store_sha256","yahoo_cache_files","yahoo_cache_sha256","price_input_rows","price_input_sha256","source_column_present"}`), `basis` (`{"built_run_commit","served_run_commit","price_basis","cash_leg","hold_cusips_count","policy","served_versions":{table:{"VersionId","LastModified"}}}`), `control` (per table: `{"served_rows","built_rows","columns_compared","rows_differing","max_abs_diff","pre_existing_equal"}`), `added_columns` (per table: `{"columns_added":[...],"use_class":{value:rows},"porting_verdict":{value:rows}}`, plus `account_day_value_accounts_not_for_active`), `yahoo_points` (`{"price_input_replaced","price_input_rederived","price_file_cusip_days_yahoo_finance","price_file_cusip_days_linear_interpolation","adv_rows_yahoo_source","adv_rows_labelled_not_yahoo_false"}`), `not_established`; and a short `.md` beside it. No account number, name or dollar value in either: counts only. **Your regrade and build directories under `C:/Dev/ajb_workspace/.scratch/cotbkf_r97/` hold per-account values: leave them there (the issuer applies from the build) and never copy them into the worktree.**

### ACCEPTANCE

<criterion id="CB97cs1-AC1" cell_refs="CB-cs-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~187/SERVED_MOVE_RELABEL_RECORD.json',encoding='utf-8'));m=d['measured'];print('RELABEL measured=%s' % m + ((' equal_tables=%d of 3 added_columns=%s' % (sum(1 for t in d['control'].values() if t['pre_existing_equal']), ','.join(sorted(set(c for t in d['added_columns'].values() if isinstance(t,dict) for c in t.get('columns_added',[])))))) if m else ' reason=%s' % d['reason']))"</invocation><expect>^RELABEL measured=(True equal_tables=[0-3] of 3 added_columns=[a-z_,]*|False reason=.+)$</expect></criterion>
`CB97cs1-AC1` -- the record states the control result and the added columns, or states plainly why nothing could be measured.

<criterion id="CB97cs1-AC2" cell_refs="CB-cs-1"><invocation>python -I org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cs1_ac2_label_check.py</invocation><expect>^LABELS adv_rows=\d+ yahoo_point_rows=[1-9]\d* labelled_rows=\d+ equal=(True|False)$</expect></criterion>
`CB97cs1-AC2` -- (AMENDMENT 1, 2026-10-16: the first text counted rows whose built `price_source` names Yahoo, but that column carries the store name, never the per-point source; the worker found it and was right.) The issuer's script (in your worktree; read it, do not edit it) joins the built `account_day_value.parquet` at `C:/Dev/ajb_workspace/.scratch/cotbkf_r97/build/` to the regrade's `after/security_day_price.parquet` at `C:/Dev/ajb_workspace/.scratch/cotbkf_r97/regrade/after/` (its per-point `source` column) and prints the count of priced, non-cash rows whose (cusip, date) point names a Yahoo source, the count of rows whose `use_class` is not `NOT_YAHOO`, and whether they are equal. The criterion requires at least one Yahoo-sourced point row (zero means the regrade did not carry the source, which fails this cell). `equal=True` is the expected result; `equal=False` is a finding to report, not to repair, and still passes.

<criterion id="CB97cs1-AC3" cell_refs="CB-cs-1"><invocation>python -c "import os;n=0;b=0;r='C:/Dev/ajb_workspace/.scratch/advi_cotbkf'
for p,ds,fs in os.walk(r):
    for f in fs:
        n+=1;b+=os.path.getsize(os.path.join(p,f))
print('RECEIVED files=%d bytes=%d' % (n,b))"</invocation><expect>^RECEIVED files=20563 bytes=4478568892$</expect></criterion>
`CB97cs1-AC3` -- the received folder still holds exactly the 20,563 files and 4,478,568,892 bytes (read directly). Your regrade and build write to `.scratch/cotbkf_r97/`, outside it, so the reading does not change as you work.

<expected_criteria>CB97cs1-AC1,CB97cs1-AC2,CB97cs1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder and your own NEW channel row. You change no code, test or committed file. Scratch outputs stay under `C:/Dev/ajb_workspace/.scratch/cotbkf_r97/` (gitignored, never committed). You may create that directory in it.
- **AWS: READ-ONLY** (`get` / `head` / `list` of the objects the regrade, the builder and the split-store pin already read, and the three served keys); no write, no `--apply`, no vendor call, no Bloomberg. The Yahoo close cache is read from the local pinned directory; the regrade must not call Yahoo.
- **No account number, name or dollar value** in the record, the report or any message: counts only. The received run data, the private config and every file in them are off git: do not list, quote or describe their contents beyond counts.
- **NEVER** serve, apply, overwrite, push, override a gate or `--force`; never edit any module; never write into the received tree `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/`.
- **Timing.** The regrade and the build each outlast the worker bar's 120 s: run each in the background under `timeout 2400` and read its log when it ends. Round 96's build took about 19 minutes in all.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W187-S<k>` (`date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. A control that reads `pre_existing_equal: false`, or `equal=False` in AC2, is recorded and reported, and still PASSES: the cell asks for the measurement.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round97.md</decomp_doc> (round 97), cell `CB-cs-1`.
<owned_cells>CB-cs-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB97cs1-AC1, CB97cs1-AC2, CB97cs1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~187/ADVI_COTBKF.TO-CB-cs-1.relabel-served-move-with-the-yahoo-source.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB97cs1-AC1,CB97cs1-AC2,CB97cs1-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when all three PASS** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the `RELABEL` line. Then: the receipt line; the regrade's pins and `PRICE-BASIS` line; the settings you used and where each came from; per table the served rows, built rows, rows differing and `max_abs_diff`; the `run_commit` served vs built; the label counts and the `yahoo_points` figures with every difference named; any step you could not run and why; the three criterion lines; commits; every gate refusal and hook denial, verbatim. No account number or value in the report.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a regrade and a build run once, locally, and counted; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE read-only gets and lists under the roles the regrade and builder already use on objects they already read; no new permission.
comp-adversary: RUN -- the control (the build equals the SERVED tables on every pre-existing column) is the check on both the regrade re-run and the relabel; BLIND: the regrade re-reads the S3 price stores today (round 129 measured the gold holdings store at 579,580 rows against 564,563 in the served cache and it did not reach a return) and the split store at the served instant, so a store change since the served build would show as a difference; the received folder is checked by count and total bytes, not per file; the private config is checked by its pinned sha256 inside the loader only.
lane: the <paths> block IS the grant (worker RULING 1). A regrade, a build and a count: nothing outside the deliverables folder and one channel row is written to the repo.
</preflight>

**ISSUER NOTES:** Source: `1.0.0_SA_CTO~DELL1` msg 6530. Round 96's `CB-cr-1` (worker ~186, @26f2781a61) found every label `NOT_YAHOO`; rows `D1-W186-S1`, `D1-S12`. The COO half (`ledger/NEVER_WIDEN_R96_FWD3_LABELS_COO_HALF_DRAFT.md`) stays unsigned until this record is read. The private config reached dell1 by the box-to-box file route (MSTR~DELL2 to MSTR~DELL1), off git. Mechanical checks dry-run at the base: AC1 FAILS (record absent); AC2 FAILS (the build is absent); AC3 PASSES. AC2's script was run on round 96's build as a negative control: `yahoo_source_rows=0`, which the `[1-9]` floor refuses.
