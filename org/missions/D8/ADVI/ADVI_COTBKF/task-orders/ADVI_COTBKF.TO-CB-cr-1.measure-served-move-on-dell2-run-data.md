# TO ADVI_COTBKF.TO-CB-cr-1.measure-served-move-on-dell2-run-data -- round 96 CB-cr-1: from the run data received from dell2, rebuild the three FWD-3 tables at the served settings, prove the build equals the SERVED tables on every pre-existing column, and count what the two added columns would say; counts only

<to_id>ADVI_COTBKF.TO-CB-cr-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~186</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>96</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cr-1` (`decompositions/ADVI_COTBKF_DECOMP.round96.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** The three served FWD-3 tables (`daily_returns`, `account_day_value`, `month_grades`) are to gain two labelled columns (`use_class`, `porting_verdict`) under Andrew's call `3adb` (a): served Yahoo-priced days stay and are labelled. The CTO's rule (msg 6455): under (a) every pre-existing value's DELTA is 0, only columns are added, and any value that moves is a finding and a stop. Round 95 could not prove it because the run data lived on dell2. That data now sits on this box, copied over the tailnet on the CTO's route B (off git, gitignored). You rebuild the tables from it and prove the delta. **This cell writes nothing to S3, serves nothing, changes no code and no committed file except your own record.**

**The received run data (READ-ONLY for you; absolute paths).** `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/` (the shared checkout's gitignored scratch; your worktree has no `.scratch`). Inside it, as the records name them:
- the re-grade run of the served build: data dir `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/r34` (holds `after/`, `before/`; `after/price_basis.json` reads `as_traded`), grades `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/r34_out/month_grades_after.parquet` and `month_grades_before.parquet`;
- the transactions cache `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/cache` (the builder's `--cache`; its default points under the repo root of the checkout the script sits in, which for you is your worktree, so PASS IT EXPLICITLY);
- the previous held build, for reference only: `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34_hold/` (served `run_commit` `6f70d5cc01bb2e196266799a657be6d0b2dc8a16`).
You do NOT run the re-grade (`commonwealth_sweep_regrade.py`) and make no vendor call: the re-grade output is already in `r34`. If any of these paths is absent or unreadable, STOP at that step, write the record with `measured: false` and `reason`, file one row, and report.

**Read first.**
1. `data/assets/scripts/silver/commonwealth_fwd3_serve.py` in your worktree (module docstring: modes, `--build` inputs, `--hold-cusips`, `--yahoo-active-policy`, `--cash-leg`, `--price-basis`; `target_addresses()` gives the three served addresses; `_read_served(uri)` reads one).
2. The recipe, to learn the SETTINGS the served build used and to confirm each against the records: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R34_FWD3_ASTRADED_REMINT_COO_HALF.md` section 3, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~106/PRICE_CACHE_PIN.json` and `.../0.9.0_WK_ADVI_COTBKF~97/CONTROL_RECORD.json`.
3. Round 83's counts for the SERVED content (rows: `daily_returns` 1,691,729; `account_day_value` 21,102,041; `month_grades` 82,593): `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~165/NEVER_WIDEN_R83_PORTING_VERDICT_COO_HALF.md` sections 1 and 3.

**The served build's settings, as the records give them (verify each against the records before you run; any difference you find is a finding, not a free choice):** cash leg `method_r28`, price basis `as_traded`, list `v1`, hold list `05613L3H2,95000U2D4,651639AX4` (`--hold-cusips`), policy `interim`. The R34 recipe's command, which you reproduce with absolute paths and the added policy flag: `commonwealth_fwd3_serve.py --build --data-dir <r34> --out <out> --hold-cusips 05613L3H2,95000U2D4,651639AX4`.

**Your items.**

1. **The receipt check (the CTO's condition on the copy).** Count the files and sum the bytes under `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/`. Record both in `received`. Expected from the dell2 manager's report: 20,563 files, 4,478,568,892 bytes. Any difference is a finding: record it, and still continue only if the difference is in files the build does not read; otherwise stop.
2. **Build locally.** Run the builder with `--build --data-dir C:/Dev/ajb_workspace/.scratch/advi_cotbkf/r34 --grades C:/Dev/ajb_workspace/.scratch/advi_cotbkf/r34_out/month_grades_after.parquet --cache C:/Dev/ajb_workspace/.scratch/advi_cotbkf/cache --cash-leg method_r28 --price-basis as_traded --hold-cusips 05613L3H2,95000U2D4,651639AX4 --yahoo-active-policy interim --out C:/Dev/ajb_workspace/.scratch/cotbkf_r96_build` (a NEW directory beside the received tree, never inside it). No `--apply`, no `blank` policy. If the builder refuses ("nothing is taken on trust"), the refusal text is the finding: record it verbatim, `measured: false`.
3. **The control.** Read the three SERVED tables from their builder addresses (S3 read-only, one get each; record each key's VersionId and LastModified). For each table compare every column that exists in the served table with the same column in your build, row-aligned on the table's key (`daily_returns`: account, date; `account_day_value`: account, date, cusip; `month_grades`: account, month). `run_commit` is excluded from the comparison and counted separately (served value vs built value, and the number of rows each carries). Floats compare with exact equality first; report the largest absolute difference. Record per table: served rows, built rows, columns compared, rows whose compared columns differ, `max_abs_diff`, and `pre_existing_equal` (true only when the row counts are equal and zero rows differ). A `False` is the cell's most important line: report it, do not repair it.
4. **The added columns.** In your build, count rows per value of `use_class` and of `porting_verdict`, per table, and for `account_day_value` the number of distinct accounts with at least one `NOT_FOR_ACTIVE` row. Name which columns your build has that the served table lacks (expected: `use_class`, `porting_verdict`; any other is a finding).
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~186/SERVED_MOVE_MEASURED_RECORD.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `received` (`{"files", "bytes"}`), `basis` (`{"built_run_commit", "served_run_commit", "price_basis", "cash_leg", "hold_cusips_count", "policy", "inputs_pinned_as_recorded", "served_versions": {table: {"VersionId", "LastModified"}}}`), `control` (per table: `{"served_rows", "built_rows", "columns_compared", "rows_differing", "max_abs_diff", "pre_existing_equal"}`), `added_columns` (per table: `{"columns_added": [...], "use_class": {value: rows}, "porting_verdict": {value: rows}}`, plus `account_day_value_accounts_not_for_active`), `not_established`; and a short `.md` beside it. No account number, name or dollar value in either: counts only. **The build you made (`.scratch/cotbkf_r96_build`) holds per-account values: leave it where it is (the issuer needs the build to apply) and never copy it into the worktree.**

### ACCEPTANCE

<criterion id="CB96cr1-AC1" cell_refs="CB-cr-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~186/SERVED_MOVE_MEASURED_RECORD.json',encoding='utf-8'));m=d['measured'];print('SERVED-MOVE measured=%s' % m + ((' equal_tables=%d of 3 added_columns=%s' % (sum(1 for t in d['control'].values() if t['pre_existing_equal']), ','.join(sorted(set(c for t in d['added_columns'].values() if isinstance(t,dict) for c in t.get('columns_added',[])))))) if m else ' reason=%s' % d['reason']))"</invocation><expect>^SERVED-MOVE measured=(True equal_tables=[0-3] of 3 added_columns=[a-z_,]*|False reason=.+)$</expect></criterion>
`CB96cr1-AC1` -- the record states the control result and the added columns, or states plainly why nothing could be measured.

<criterion id="CB96cr1-AC2" cell_refs="CB-cr-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~186/SERVED_MOVE_MEASURED_RECORD.json',encoding='utf-8'));ok=(not d['measured']) or all(sum(t['use_class'].values())==d['control'][k]['built_rows'] and sum(t['porting_verdict'].values())==d['control'][k]['built_rows'] for k,t in d['added_columns'].items() if isinstance(t,dict));print('SERVED-MOVE-SUMS consistent=%s' % ok)"</invocation><expect>^SERVED-MOVE-SUMS consistent=True$</expect></criterion>
`CB96cr1-AC2` -- every label count adds up to the built row count of its table.

<criterion id="CB96cr1-AC3" cell_refs="CB-cr-1"><invocation>python -c "import os;n=0;b=0;r='C:/Dev/ajb_workspace/.scratch/advi_cotbkf'
for p,ds,fs in os.walk(r):
    for f in fs:
        n+=1;b+=os.path.getsize(os.path.join(p,f))
print('RECEIVED files=%d bytes=%d' % (n,b))"</invocation><expect>^RECEIVED files=20563 bytes=4478568892$</expect></criterion>
`CB96cr1-AC3` -- the received folder still holds the 20,563 files and 4,478,568,892 bytes the manager sent (read directly, not from your record). The builder writes to `.scratch/cotbkf_r96_build`, outside the received tree, so this reading does not change when you build; run it BEFORE item 2 anyway and keep that line as the evidence.

<expected_criteria>CB96cr1-AC1,CB96cr1-AC2,CB96cr1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder and your own NEW channel row. You change no code, test or committed file; scratch outputs stay under `C:/Dev/ajb_workspace/.scratch/` (gitignored, never committed): the build goes to `cotbkf_r96_build` and stays there.
- **AWS: READ-ONLY** (`get` / `head` of the three served keys and the objects the builder already reads, such as the Yahoo store index); no write, no `--apply`, no vendor call, no Bloomberg.
- **No account number, name or dollar value** in the record, the report or any message: counts only. The received run data and every file in it are off git: do not list, quote or describe its contents beyond counts.
- **NEVER** serve, apply, overwrite, push, override a gate or `--force`; never edit `commonwealth_fwd3_serve.py` or any module; never write anything into the received tree `C:/Dev/ajb_workspace/.scratch/advi_cotbkf/`.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W186-S<k>` (`date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. A control that reads `pre_existing_equal: false` is recorded and reported, and still PASSES AC1 and AC2: the cell asks for the measurement.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round96.md</decomp_doc> (round 96), cell `CB-cr-1`.
<owned_cells>CB-cr-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB96cr1-AC1, CB96cr1-AC2, CB96cr1-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~186/ADVI_COTBKF.TO-CB-cr-1.measure-served-move-on-dell2-run-data.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB96cr1-AC1,CB96cr1-AC2,CB96cr1-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when all three PASS** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the `SERVED-MOVE` line. Then: the receipt counts (before the build); the settings you used and where each came from; per table the served rows, built rows, rows differing and `max_abs_diff`; the `run_commit` served vs built; the added columns and their label counts; any step you could not run and why; the three criterion lines; commits; every gate refusal and hook denial, verbatim. No account number or value in the report.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read and a count; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE read-only gets under the existing role on objects the builder already reads; no new permission.
comp-adversary: RUN -- the control (the build equals the SERVED tables on every pre-existing column) is the check on the received copy as well as on CB-ck-1; BLIND: the served objects are read at their current version, not at a pinned VersionId, so a write by another seat between the served build and this read would show as a difference (the record states each key's VersionId and LastModified); and the received folder is checked here by count and total bytes against the manager's report and the CTO confirmation ("20,563 files, 4.3 GB"), not by a per-file hash, so a same-size corrupted file is caught only if it changes the build.
lane: the <paths> block IS the grant (worker RULING 1). A read and a count: nothing outside the deliverables folder and one channel row is written to the repo.
</preflight>

**ISSUER NOTES:** Source: `1.0.0_SA_CTO~DELL1` msg 6455 (cut served round 95; delta 0 or stop) and msg 6467 (route B). Round 95's `CB-cq-1` (worker ~185, @c2f2aff341) stopped at provisioning (`W185-S1`). The signed pair (the COO half is this seat's; the draft is `ledger/NEVER_WIDEN_R96_FWD3_LABELS_COO_HALF_DRAFT.md`) and the served write by a CloudOps seat are after this record is read. Mechanical checks dry-run at the base (the record file is absent): AC1 and AC2 FAIL there as expected; AC3 reads the received folder directly and PASSES at the base once the issuer has confirmed the figures.
