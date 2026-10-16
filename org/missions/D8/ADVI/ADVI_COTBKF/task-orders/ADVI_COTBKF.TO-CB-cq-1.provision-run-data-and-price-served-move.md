# TO ADVI_COTBKF.TO-CB-cq-1.provision-run-data-and-price-served-move -- round 95 CB-cq-1: rebuild the served-returns run data on dell1 from S3 (read-only), prove the build equals the SERVED tables on every pre-existing column, and count what the two added columns would say; counts only

<to_id>ADVI_COTBKF.TO-CB-cq-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~185</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>95</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-cq-1` (`decompositions/ADVI_COTBKF_DECOMP.round95.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** The three served FWD-3 tables (`daily_returns`, `account_day_value`, `month_grades`) are to gain labelled columns under Andrew's call `3adb` (a): served Yahoo-priced days stay and are labelled. The CTO's rule (msg 6455): under (a) every pre-existing value's DELTA is 0, only columns are added, and any value that moves is a finding and a stop. That is only provable with the builder's run data, which is absent on this box (`NO_DATA_DIR`, round 89). You rebuild it from S3 and prove the delta. **This cell writes nothing to S3, serves nothing, changes no code and no committed file except your own record.**

**Read first.**
1. `data/assets/scripts/silver/commonwealth_fwd3_serve.py` (its module docstring: modes, the `--build` inputs, the `--hold-cusips` and `--yahoo-active-policy` options; `target_addresses()` gives the three served addresses; `_read_served(uri)` reads one).
2. The recipe records, to learn the SETTINGS the served build used, not to copy values blindly: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~97/CONTROL_RECORD.json`, `.../0.9.0_WK_ADVI_COTBKF~104/R28_VS_R29_AT_PIN.json`, `.../0.9.0_WK_ADVI_COTBKF~106/PRICE_CACHE_PIN.json`, `.../0.9.0_WK_ADVI_COTBKF~99/SPLIT_STORE_PIN.json`, `.../0.9.0_WK_ADVI_COTBKF~100/ADDED_SPLITS.json`, and `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R34_FWD3_ASTRADED_REMINT_COO_HALF.md` section 3.
3. Round 83's counts for the SERVED content: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~165/NEVER_WIDEN_R83_PORTING_VERDICT_COO_HALF.md` section 1 and 3 (served rows: `daily_returns` 1,691,729; `account_day_value` 21,102,041; `month_grades` 82,593; run_commit of the served build `728d223ddca5472884c464b0482f814bfc706f41`).

**The served build's settings, as the records give them (verify against the records before you run; any difference you find is a finding, not a free choice):** cash leg `method_r28`, price basis `as_traded`, list `v1`, hold list `05613L3H2,95000U2D4,651639AX4` (`--hold-cusips`), the pinned price cache and split store of the two PIN records. Round 69's drain-end read: "with the served hold list the rebuild is exact apart from `run_commit`."

**Your items.**

1. **Provision the run data.** Under your worktree `.scratch/advi_cotbkf/` (gitignored; never committed), run the default re-grade `data/assets/scripts/silver/commonwealth_sweep_regrade.py` with the flags the records give for the served build (`--data-dir`, `--out` under the same scratch tree, `--price-input-out` when the records name it), reading S3 read-only. If a step needs a file only dell2 holds, STOP at that step: write the record with `measured: false` and `reason` naming the missing input, file one row, and report. Do not guess a substitute.
2. **Build locally, both policies' common case.** `commonwealth_fwd3_serve.py --build ... --yahoo-active-policy interim` with the served settings, into `.scratch/advi_cotbkf/fwd3_serve_cq` (no `--apply`, no `--blank` build here).
3. **The control.** Read the three SERVED tables from their builder addresses (S3 read-only, one get each). For each table compare every column that exists in the served table with the same column in your build, row-aligned on the table's key (`daily_returns`: account, date; `account_day_value`: account, date, cusip; `month_grades`: account, month). `run_commit` is excluded from the comparison and counted separately. Float columns compare with exact equality first; report the largest absolute difference. Record per table: served rows, built rows, columns compared, rows whose compared columns differ, and `pre_existing_equal` (true only when rows are equal and zero rows differ). A `False` is the cell's most important line: report it, do not repair it.
4. **The added columns.** In your build, count rows per value of `use_class` and of `porting_verdict`, per table, and for `account_day_value` the number of distinct accounts with at least one `NOT_FOR_ACTIVE` row. Also name which columns your build has that the served table lacks (expected: `use_class`, `porting_verdict`; any other is a finding).
5. **The record** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~185/SERVED_MOVE_PRICED_RECORD.json` with exactly these top-level keys: `measured`, `reason` (when not measured), `basis` (`{"built_run_commit", "served_run_commit", "price_basis", "cash_leg", "hold_cusips_count", "policy", "inputs_pinned_as_recorded"}`), `control` (per table: `{"served_rows", "built_rows", "columns_compared", "rows_differing", "max_abs_diff", "pre_existing_equal"}`), `added_columns` (per table: `{"columns_added": [...], "use_class": {value: rows}, "porting_verdict": {value: rows}}`, plus `account_day_value_accounts_not_for_active`), `not_established`; and a short `.md` beside it. No account number, name or dollar value in either: counts only.

### ACCEPTANCE

<criterion id="CB95cq1-AC1" cell_refs="CB-cq-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~185/SERVED_MOVE_PRICED_RECORD.json',encoding='utf-8'));m=d['measured'];print('SERVED-MOVE measured=%s' % m + ((' equal_tables=%d of 3 added_columns=%s' % (sum(1 for t in d['control'].values() if t['pre_existing_equal']), ','.join(sorted(set(c for t in d['added_columns'].values() if isinstance(t,dict) for c in t.get('columns_added',[])))))) if m else ' reason=%s' % d['reason']))"</invocation><expect>^SERVED-MOVE measured=(True equal_tables=[0-3] of 3 added_columns=[a-z_,]*|False reason=.+)$</expect></criterion>
`CB95cq1-AC1` -- the record states the control result and the added columns, or states plainly why nothing could be measured.

<criterion id="CB95cq1-AC2" cell_refs="CB-cq-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~185/SERVED_MOVE_PRICED_RECORD.json',encoding='utf-8'));ok=(not d['measured']) or all(sum(t['use_class'].values())==d['control'][k]['built_rows'] and sum(t['porting_verdict'].values())==d['control'][k]['built_rows'] for k,t in d['added_columns'].items() if isinstance(t,dict));print('SERVED-MOVE-SUMS consistent=%s' % ok)"</invocation><expect>SERVED-MOVE-SUMS consistent=True</expect></criterion>
`CB95cq1-AC2` -- every label count adds up to the built row count of its table.

<expected_criteria>CB95cq1-AC1,CB95cq1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below only: your deliverables folder and your own NEW channel row. You change no code, test or committed file; scratch outputs stay under the worktree `.scratch/` (never committed) and are deleted when you finish, since they hold per-account values.
- **AWS: READ-ONLY** (`get` / `head` / `list` of the objects the builder and re-grade already read, plus one get of each of the three served keys); no write, no `--apply`, no vendor call, no Bloomberg.
- **No account number, name or dollar value** in the record, the report or any message: counts only.
- **NEVER** serve, apply, overwrite, push, override a gate or `--force`; never edit `commonwealth_fwd3_serve.py` or any module.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W185-S<k>` (`date -u +%FT%TZ` for `surfaced_at`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. A control that reads `pre_existing_equal: false` is recorded and reported, and still PASSES AC1 and AC2: the cell asks for the measurement.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round95.md</decomp_doc> (round 95), cell `CB-cq-1`.
<owned_cells>CB-cq-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB95cq1-AC1, CB95cq1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~185/ADVI_COTBKF.TO-CB-cq-1.provision-run-data-and-price-served-move.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB95cq1-AC1,CB95cq1-AC2` BEFORE the flip. Both criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when both criteria PASS** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the `SERVED-MOVE` line. Then: the settings you used and where each came from; per table the served rows, built rows, rows differing and `max_abs_diff`; the added columns and their label counts; any step you could not run and why; the two criterion lines; commits; every gate refusal and hook denial, verbatim. No account number or value in the report.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read and a count; nothing is scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE read-only gets under the existing role on objects the builder and re-grade already read; no new permission.
comp-adversary: RUN -- the control (the build equals the SERVED tables on every pre-existing column) is the check on both the provisioning and on `CB-ck-1`; BLIND: the served objects are read at their current version, not at a pinned VersionId, so a write by another seat between the served build and this read would show as a difference (the record states each key's VersionId and LastModified); the run data may not reproduce if a pinned input has been overwritten since round 82.
lane: the <paths> block IS the grant (worker RULING 1). A read and a count: nothing outside the deliverables folder and one channel row is written.
</preflight>

**ISSUER NOTES:** Source: `1.0.0_SA_CTO~DELL1` msg 6455 (cut served round 95; delta 0 or stop). The signed pair (the COO half is this seat's, the CTO's half is his) and the served write by the box applier are round 96, after this record is read. Round 83's `porting_verdict` was built locally and never applied, so the served move adds TWO columns; the pair names both. Mechanical checks dry-run at the base (the record file is absent): AC1 and AC2 FAIL there as expected.
