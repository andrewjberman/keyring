# TO ADVI_COTBKF.TO-CB-ce-3.ticker-asset-name-key -- round 83 CB-ce-3: the four readers that key the price store by ticker alone key it by (ticker, asset_name), so SCCO's bond row and APH's two classes never merge

<to_id>ADVI_COTBKF.TO-CB-ce-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~166</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>83</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-ce-3` (`decompositions/ADVI_COTBKF_DECOMP.round83.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a LOCAL code change with tests, in four census and provenance scripts that read the price store; none of them produces served output. You change the four scripts and the tests named in `<paths>`. Nothing is applied, minted, served or uploaded; no S3 write; no vendor call. If you find that one of the four writes a served object, STOP on it and file a row (the change is then under a never-widen pair and not this cell's).**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_83_20261013.md` section 2 item 3, word for word: "W158-S2, the keyed fix: the four ticker-only readers key the price store by (ticker, asset_name), so SCCO's bond row and APH's two classes never merge. It goes under the same pair as item 2 if the served figures move, otherwise LOCAL."
Then the round-82 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~163/TICKER_KEY_READ.json` (the four readers with file and line; what each does with two rows for one ticker and date; the keyed fix's footprint; the six `asset_name`-keyed gold readers for the pattern) and the rows `ADVI_COTBKF-D2-W158-S2`, `-D2-W159-S1` and `-D2-W163-S1` in the channel.
The store: `s3://opal-data-cot/silver/prices/canonical_prices.parquet`, columns `date, asset_name, ticker, price, source`. It holds two `asset_name` values under one ticker on some days: SCCO on 1,027 dates (the equity's price on a row named for a 3.875% 04/23/2025 bond) and APH on 70 dates (CL A and NEW CL A, equal on 69 and different on 2026-04-14). Pattern: "one store, one Opal key": the gold readers `B_00.canonical_holdings.py:445,:710`, `A_03.positions_cube.py:677,:681` key by `asset_name`.

**The four readers (re-find each line yourself; the numbers are round 82's):** `data/assets/scripts/analysis/commonwealth_price_census.py:57` (presence only), `data/assets/scripts/silver/commonwealth_price_basis_census.py:364` (a ticker-day median), `data/assets/scripts/silver/commonwealth_bond_custodian_price.py:125` (selects ticker values equal to bond CUSIPs), `data/assets/scripts/silver/commonwealth_bd_txn_provenance.py:38` and `:117-121` (a source-label test plus a ticker-in-CUSIP test).

**AMENDMENT 1 (issuer `2.0.0_SA_COO~C2`, 2026-10-13T23:1xZ), on your row `ADVI_COTBKF-D2-W166-S1`:** the AC1 invocation as first written could not collect (two `tests` packages, one under `silver/` and one under `analysis/`; the same error at HEAD before any edit). The invocation now carries `--import-mode=importlib`, which you measured: 28 passed. Re-run AC1 as it now reads, record the result in the proof instance, and flip the order in the commit that carries it. Nothing else in the order changes.

**Your item.**

1. **The key each reader needs.** For each of the four, say what `asset_name` it can supply on the reader's side (a held security's name from the transactions or holdings table it already reads, a CUSIP-to-name bridge it already loads) and where it comes from. A reader that has NO `asset_name` on its side gets the narrowest safe change: it keys the STORE by `(ticker, asset_name)` and, when its own side has no name, keeps the rows apart (never merges two names under one ticker) and reports the ambiguous tickers as a count. Describe each in the record before you edit it.
2. **The change, minimal, per reader.** Group, join or select the store by `(ticker, asset_name)`; where one ticker-day then has two rows, the reader no longer takes a median, mean or first of them: it keeps both and picks by name, or reports the day as `ambiguous_name` with a count. Do not change a reader's output columns except to ADD one (the `asset_name` it used, or an ambiguity count) at the end. Do not change any value of an existing column on a day that has one name under the ticker (a byte-equality test over a one-name fixture).
3. **Tests (one new file `test_commonwealth_ticker_asset_key.py` plus additions to `test_commonwealth_price_basis.py` and `test_commonwealth_price_census.py`):** a fixture with the SCCO shape (an equity row and a bond row under one ticker and day, different prices) and the APH shape (two classes under one ticker, equal on most days, different on one): each reader returns the price of the intended name and does not average or merge; a one-name fixture returns exactly what the old code returned. Run:
   `python -m pytest --import-mode=importlib data/assets/scripts/silver/tests/test_commonwealth_ticker_asset_key.py data/assets/scripts/silver/tests/test_commonwealth_price_basis.py data/assets/scripts/analysis/tests/test_commonwealth_price_census.py -q` and report passed/failed. A test you cannot make pass is reported, never skipped or weakened.
4. **Before and after on the real store, counts only.** With the store object read once (`get-object` of that key at version `76.rgWIXYdLNsXSwrXvyuEmaEtfr9y98`, 97,443,387 bytes, byte length checked, into your `.scratch/`) and each reader run in its read-only mode over local inputs, per reader: the number of ticker-days that carry two names (it should be 1,027 for SCCO and 70 for APH plus any other), the number of output rows that change and the number of existing values that change, with the old code (`git stash` is hook-blocked: use a second worktree copy or `git show <base>:<file>` into `.scratch/`) and the new code. If a reader needs inputs you do not have on this box, say which and mark that reader's count `not_established`; do not fetch.
5. **Does any served figure move?** For each reader: does its output feed a served object (the minted tables, the ARD output, the portal)? Answer from the round-82 consumer record `deliverables/0.9.0_WK_ADVI_COTBKF~158/CONSUMER_READ.json` and the code: `no` (say why), `yes` (stop on that reader, file the row), or `not_established`.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~166/TICKER_ASSET_KEY_RECORD.json` and a short `.md`. Top-level keys, exactly: `readers` (a list of 4: `{"path", "line_before", "line_after", "asset_name_source", "change", "feeds_served"}`), `tests` (`{"passed", "failed", "files"}`), `store` (`{"key", "version", "bytes", "bytes_match"}`), `two_name_ticker_days` (`{"SCCO", "APH", "others"}`), `before_after` (a list of 4: `{"reader", "rows_changed", "existing_values_changed", "state"}`), `served_figures_move` (true, false or `not_established`), `row_w158_s2_disarms` (true, false or `not_established`, with the reason), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB83ce3-AC1" cell_refs="CB-ce-3"><invocation>python -m pytest --import-mode=importlib data/assets/scripts/silver/tests/test_commonwealth_ticker_asset_key.py data/assets/scripts/silver/tests/test_commonwealth_price_basis.py data/assets/scripts/analysis/tests/test_commonwealth_price_census.py -q</invocation><expect>passed</expect></criterion>
`CB83ce3-AC1` -- the new test file and the two existing test files pass with no failure and no skipped test.

<criterion id="CB83ce3-AC2" cell_refs="CB-ce-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~166/TICKER_ASSET_KEY_RECORD.json',encoding='utf-8'));ba=d['before_after'];print('TICKER-ASSET-KEY readers=%d tests_passed=%s tests_failed=%s bytes_match=%s before_after=%d existing_values_changed=%s served_figures_move=%s disarms=%s'%(len(d['readers']),d['tests']['passed'],d['tests']['failed'],d['store']['bytes_match'],len(ba),[x['existing_values_changed'] for x in ba],d['served_figures_move'],d['row_w158_s2_disarms']))"</invocation><expect>TICKER-ASSET-KEY readers=4</expect></criterion>
`CB83ce3-AC2` -- all four readers are changed and recorded with their before and after counts; the served-figures answer and the row answer are in the record.

<criterion id="CB83ce3-AC3" cell_refs="CB-ce-3" judgment="true"/>
`CB83ce3-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each reader keys by `(ticker, asset_name)` and no longer merges two names under one ticker; a day with one name returns exactly the old values; the SCCO and APH fixtures show the intended name's price; the served-figures answer follows from the consumer record and the code; the row `D2-W158-S2` is called disarmable only if all four are keyed and tested; nothing was applied, minted, served or uploaded.

<expected_criteria>CB83ce3-AC1,CB83ce3-AC2,CB83ce3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the file of this order.
- **Code edits are limited to the four scripts and the tests in `<paths>`.** No other code, test, config, manifest, registry or infrastructure; not the price-store writer `build_canonical_prices_v2.py`; not the six gold readers; not the scan test.
- **Commit every `.py` through `.tools/safe-commit.sh`;** the commit gate (py_compile, ds-precommit, ruff) must pass and you quote its lines.
- **AWS: READ-ONLY, through the `.tools/aws` shim:** one `get-object` of the store object above (that key and version, byte length checked) into your `.scratch/`. No listing, write, delete or serve. Do not run `aws sts get-caller-identity`.
- **Another firm's data is never opened.** No account id and no account's value: counts, tickers, CUSIPs (only in a `cusip` column), dates, prices and ratios only. Do not list or open `C:/dev/_cotbkf_private_evidence_20261009/`.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`. **No vendor call and no fetch.**
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- Searches go through the estate's tools; a recursive shell search of the repository is denied by a hook and is not retried another way.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W166-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`),
  APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
data/assets/scripts/analysis/commonwealth_price_census.py
data/assets/scripts/silver/commonwealth_price_basis_census.py
data/assets/scripts/silver/commonwealth_bond_custodian_price.py
data/assets/scripts/silver/commonwealth_bd_txn_provenance.py
data/assets/scripts/analysis/tests/test_commonwealth_price_census.py
data/assets/scripts/silver/tests/test_commonwealth_price_basis.py
data/assets/scripts/silver/tests/test_commonwealth_ticker_asset_key.py
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round83.md</decomp_doc> (round 83), cell `CB-ce-3`.
<owned_cells>CB-ce-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB83ce3-AC1, CB83ce3-AC2, CB83ce3-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~166/ADVI_COTBKF.TO-CB-ce-3.ticker-asset-name-key.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB83ce3-AC1,CB83ce3-AC2,CB83ce3-AC3` BEFORE the flip. Mechanical: CB83ce3-AC1, CB83ce3-AC2. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. You flip your own order `<status>` to `complete` in the commit that carries the proof instance.
</proof_of_spec>

**REPORT:** FIRST, if one of the four feeds a served object: which and how. Then: per reader the key source, the change (file, lines) and the before/after counts; the test counts; the two-name ticker-days (SCCO, APH, others); whether served figures move; whether `D2-W158-S2` disarms and why; every remote read made; the `TICKER-ASSET-KEY` line; the account-id scan's DENOMINATOR line; the commit gate's lines; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local code change in census tools; nothing is scheduled, minted or served here.
comp-iam: DECLARED-NOT-APPLICABLE no lens was run: one read-only call on an Opal object under the existing role; no write, delete or serve, and no new permission.
comp-adversary: RUN -- each reader keys by name and no longer merges; a one-name day returns exactly the old values; the SCCO and APH fixtures pick the intended name; BLIND: a reader whose own side has no name, a ticker that is lower-cased or stripped on one side, and an output that a served object reads.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-83 analysis @01ed464473 (msg 7298), section 2 item 3; `3.0.0_SA_CVO` REMEDIATION_v50 @43b340c673 (row D2-W158-S2).
