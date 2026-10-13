# TO ADVI_COTBKF.TO-CB-ce-2.porting-verdict-into-the-figures -- round 83 CB-ce-2: every COTBKF figure built on a Yahoo price whose porting_verdict is not PASS carries the label UNVERIFIED, in a field a reader can reject on: built and counted LOCALLY, nothing applied or served

<to_id>ADVI_COTBKF.TO-CB-ce-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~165</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>83</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-ce-2` (`decompositions/ADVI_COTBKF_DECOMP.round83.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a LOCAL code change with tests and a counted dry run. You change the three scripts and three tests named in `<paths>` and add one test file. Nothing is applied, minted, re-minted, served or uploaded; no S3 write of any kind; no vendor call. The minted tables are served objects, so moving them is a later act under a CTO+COO never-widen pair, which you DRAFT (the COO half only) and do not sign or apply.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_83_20261013.md` section 2 item 2, word for word: "UNVERIFIED Yahoo prices (Andrew-direct 10-13): every COTBKF figure built on a Yahoo price whose `porting_verdict` is not passed carries claim UNVERIFIED, in a field a reader can reject on. It goes under a never-widen pair, with the count of figures that change."
Then dell1's CTO half, which defines the column (read it from the ref: `git show origin/box/dell1:org/missions/D8/MDPF/MDPF_DEMQUE/ledger/NEVER_WIDEN_R9_YAHOO_B_CTO_HALF.md`; if the ref does not resolve in your tree, say so, and use only the facts below): the Yahoo store's index (`index/index.parquet` and `index/index.csv` at the address `data/mdpf/scripts/demque/price_store.py` `s3_root()` returns) gains ONE column `porting_verdict`
with the values UNVERIFIED (default) | PASS | FAIL | UNTESTABLE; **the label is NOT put in `claim`** (that would mint a value-enum member without its TAXONOMY LAW record), so your field is a separate field with those four values and the same default. Three branches dell1 signed, and you build all three: no verdicts file (every row reads UNVERIFIED); a verdicts file (each name reads its verdict, a missing row reads UNVERIFIED);
unreadable or malformed (every row reads UNVERIFIED and says why; it fails closed, so a PASS is never produced on a read that did not complete). **The column is not on the live index yet** (dell1 has not applied pair B): an index with no `porting_verdict` column is the "no verdicts" branch and reads UNVERIFIED everywhere. The gap, in dell1's words: "`commonwealth_price_need.py` carries `demque_claim` and ignores the new column; `land_cot.py` does not read the index at all. So a Cottonwood valuation built from a Yahoo price does not yet say UNVERIFIED." `land_cot.py` is dell1's lander and you do NOT edit it; the consumer side is yours.

**The rule for "Yahoo-sourced" (ruled by the issuer for this cell):** a price whose store `source` value is `yahoo_finance` or `linear_interpolation` (derived from Yahoo prices) is Yahoo-sourced; `transaction_observed`, `transaction_observed_capped`, `scoped_override` and `bd_txn_price` are not. The price store's `source` column is in `s3://opal-data-cot/silver/prices/canonical_prices.parquet`; the build's per-day prices are `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet` (cusip, date, price, store) and the minted tables are the local copy
`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/` (read only; round 82 verified the served objects equal it row for row). Count under this rule AND under the narrower rule (`yahoo_finance` only) and report both.

**AMENDMENT 1 (issuer `2.0.0_SA_COO~C2`, 2026-10-13T23:2xZ), on your row `ADVI_COTBKF-D2-W165-S2`:** the AWS bound gains ONE read-only grant so that `month_grades` can be measured like the other two tables: the Commonwealth reported-performance prefix that `commonwealth_monthly_grade.py` names as `performance_prefix` (around line 45; the address comes from that code, you type none), read at its `date=2026-06-23/` partition: `list-objects-v2 --max-items 5` once, then `get-object` of the objects it lists (state their count and sizes), into your `.scratch/`; no other listing, no write, no delete. With it, re-derive `month_grades` with the changed code and compare its EXISTING columns with the served `month_grades` object you already read (82,593 rows), under both rules, and replace `NOT_MEASURED` in the record with the measured count of existing values that change (it must be 0; if it is not 0, say which columns and how many rows, and stop on that). Then update the record, re-run the criteria, update the proof instance and flip the order in the commit that carries them. Nothing else in the order changes.

**Your item.**

1. **Where each figure gets its price, one table.** From the code (file and line, read not run): the path from the store's `source` to the build's per-day price (`commonwealth_daily_valuation.py`), to the minted tables (`commonwealth_fwd3_serve.py`), and to the price-need list (`commonwealth_price_need.py`). Name every column that today carries a price's origin (`store`, `basis`, `demque_claim`, `source`) and every figure table (`daily_returns`, `account_day_value`, `month_grades`) with its columns. Which figure rows are built on a price at all (count, under the rule)?
2. **The change, minimal and local.** Add a field `porting_verdict` (values as above, default UNVERIFIED) that (a) `commonwealth_price_need.py` reads from the index when the column is present and otherwise sets UNVERIFIED, written beside `demque_claim` in its rows; (b) `commonwealth_daily_valuation.py` carries per price point and per account-day row built on a Yahoo-sourced price; (c) `commonwealth_fwd3_serve.py` writes into the minted tables' schema as an added column (NULL-free: non-Yahoo rows read `NOT_YAHOO`).
   Existing columns, their order and dtypes do not change; the new column is appended last; no existing value changes. If a consumer reads these tables positionally or by a fixed schema (the ARD adapter `commonwealth_account_return_daily.py:221-226` and the census `commonwealth_price_basis_census.py:292-295` read them), show by a test that an appended column does not break them, or stop and file a row.
3. **Tests (one new file `test_commonwealth_porting_verdict.py` plus additions to the three named test files):** the three branches (no column; a verdicts frame; malformed); a PASS is never produced on a failed read (a negative control: a read that raises yields UNVERIFIED for every row); the appended column leaves every existing column's values byte-equal (a regression test over a small fixture); and a Yahoo-sourced row reads UNVERIFIED while a `transaction_observed` row reads `NOT_YAHOO`. Run: `python -m pytest data/assets/scripts/silver/tests/test_commonwealth_porting_verdict.py data/assets/scripts/silver/tests/test_commonwealth_price_need.py data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve.py -q` and report the counts passed/failed. A test you cannot make pass is reported, never skipped or weakened.
4. **The dry-run count, with no write.** Over the local copies named above, with the changed code and the live index (read the index object by `get-object` into your `.scratch/`; no column, so all UNVERIFIED): the number of figure rows (account-days in `account_day_value`, rows in `daily_returns`, rows in `month_grades`) that WOULD read UNVERIFIED, that would read NOT_YAHOO, and the number whose existing values change (this must be 0). Under both source rules. Counts only.
5. **The COO half DRAFT** in your folder, `NEVER_WIDEN_R83_PORTING_VERDICT_COO_HALF.md`, marked DRAFT and unsigned, in the form of the earlier halves in `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_R27_FWD3_SERVE_COO_HALF.md` (read it): the act (re-mint of the three minted objects with one appended column, by the builder's guarded apply, under a CloudOps seat), the blast radius per key (the three keys, N writers read, N printed), the expected outcome in BOTH branches of the producer's rule (index with the column; without it), the rollback per key (the object versions before the act), and the counts of item 4. State that no consumer is attached to the tables (round 82's read found two CODE readers and no page) and that the route to a page is not live.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~165/PORTING_VERDICT_RECORD.json` and a short `.md`. Top-level keys, exactly: `price_path` (a list: `{"hop", "file_line", "columns"}`), `figure_tables` (a list of 3: `{"table", "rows", "rows_on_a_price"}`), `rule` (`{"wide", "narrow"}`), `tests` (`{"passed", "failed", "files"}`), `dry_run` (`{"wide": {"unverified", "not_yahoo", "existing_values_changed"}, "narrow": {...}}`), `consumers_checked` (a list: `{"consumer", "appended_column_breaks_it"}`), `pair_half` (`{"file", "state"}`), `index_column_present`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB83ce2-AC1" cell_refs="CB-ce-2"><invocation>python -m pytest data/assets/scripts/silver/tests/test_commonwealth_porting_verdict.py data/assets/scripts/silver/tests/test_commonwealth_price_need.py data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve.py -q</invocation><expect>passed</expect></criterion>
`CB83ce2-AC1` -- the new test file and the three existing test files pass with no failure and no skipped test.

<criterion id="CB83ce2-AC2" cell_refs="CB-ce-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~165/PORTING_VERDICT_RECORD.json',encoding='utf-8'));w=d['dry_run']['wide'];n=d['dry_run']['narrow'];print('PORTING-VERDICT tables=%d tests_passed=%s tests_failed=%s wide_unverified=%s wide_not_yahoo=%s wide_changed=%s narrow_unverified=%s narrow_changed=%s consumers=%d pair_state=%s'%(len(d['figure_tables']),d['tests']['passed'],d['tests']['failed'],w['unverified'],w['not_yahoo'],w['existing_values_changed'],n['unverified'],n['existing_values_changed'],len(d['consumers_checked']),d['pair_half']['state']))"</invocation><expect>PORTING-VERDICT tables=3</expect></criterion>
`CB83ce2-AC2` -- the three figure tables are counted under both rules, no existing value changes, the consumers are checked, and the pair half is a DRAFT.

<criterion id="CB83ce2-AC3" cell_refs="CB-ce-2" judgment="true"/>
`CB83ce2-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the label is a field a reader can reject on and is NOT a new member of `claim`; an absent or unreadable index reads UNVERIFIED and a PASS cannot be produced by a failed read; no existing column or value moves; the count is under both source rules; the COO half names the three keys, N writers, both branches and the rollback and is unsigned; nothing was applied, minted, served or uploaded.

<expected_criteria>CB83ce2-AC1,CB83ce2-AC2,CB83ce2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the file of this order.
- **Code edits are limited to the three scripts and three test files in `<paths>`, plus the one new test file.** No other code, test, config, manifest, registry or infrastructure; not `land_cot.py` or any file under `data/mdpf/` (dell1's); not the scan test. Commit every `.py` through `.tools/safe-commit.sh`; the commit gate (py_compile, ds-precommit, ruff) must pass and you quote its lines.
- **AWS: READ-ONLY, through the `.tools/aws` shim (AMENDMENT 1 adds the reported-performance partition above):** one `get-object` of the Yahoo store's index (address from `price_store.s3_root()` in code; nothing typed) and, only if you need a count the local copies lack, one `get-object` of `s3://opal-data-cot/silver/prices/canonical_prices.parquet` at version `76.rgWIXYdLNsXSwrXvyuEmaEtfr9y98` (97,443,387 bytes, byte length checked) into your `.scratch/`. No listing, write, delete or serve. Do not run `aws sts get-caller-identity`.
- **Another firm's data is never opened.** No account id and no account's value: counts, tickers, CUSIPs (only in a `cusip` column), dates, prices and ratios only. Do not list or open `C:/dev/_cotbkf_private_evidence_20261009/`.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket; do not run the serve builder with any flag that uploads.** No push. No `--refresh`. **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull).
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- Searches go through the estate's tools; a recursive shell search of the repository is denied by a hook and is not retried another way.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W165-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`),
  APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
data/assets/scripts/silver/commonwealth_price_need.py
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/commonwealth_fwd3_serve.py
data/assets/scripts/silver/tests/test_commonwealth_price_need.py
data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py
data/assets/scripts/silver/tests/test_commonwealth_fwd3_serve.py
data/assets/scripts/silver/tests/test_commonwealth_porting_verdict.py
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round83.md</decomp_doc> (round 83), cell `CB-ce-2`.
<owned_cells>CB-ce-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB83ce2-AC1, CB83ce2-AC2, CB83ce2-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~165/ADVI_COTBKF.TO-CB-ce-2.porting-verdict-into-the-figures.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB83ce2-AC1,CB83ce2-AC2,CB83ce2-AC3` BEFORE the flip. Mechanical: CB83ce2-AC1, CB83ce2-AC2. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. You flip your own order `<status>` to `complete` in the commit that carries the proof instance.
</proof_of_spec>

**REPORT:** FIRST, if a consumer breaks on the appended column: which, and the test. Then: the price path table; the change in each of the three scripts (file, lines); the test counts; the dry-run counts under both rules; the consumers checked; the COO half draft's path and the blast radius it states; whether the live index carries the column; every remote read made; the `PORTING-VERDICT` line; the account-id scan's DENOMINATOR line; the commit gate's lines; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local code change and a counted dry run; nothing is scheduled, minted or served here.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: one or two read-only calls on Opal data under the existing role; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the label is a field, not a new `claim` member; a failed read yields UNVERIFIED, never PASS; no existing value moves (a byte-equality test); the count is under both source rules; BLIND: a consumer that reads the tables by position, and dell1's verdicts file (not written yet) whose real shape may differ from the three branches built here.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-83 analysis @01ed464473 (msg 7298), section 2 item 2; Andrew-direct 2026-10-13 via `1.0.0_SA_CTO~DELL1` (relayed by `0.0.0_AB_MSTR~DELL2` msg 7294); dell1 pair B CTO half @261ab7bbf2 on origin/box/dell1.
