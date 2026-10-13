# TO ADVI_COTBKF.TO-CB-cd-3.ticker-key-read-and-header -- round 82 CB-cd-3: who reads the price store keyed by ticker alone (row D2-W158-S2), and the one false sentence in the adapter's module docstring corrected (row D2-W158-S5)

<to_id>ADVI_COTBKF.TO-CB-cd-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~163</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>82</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-cd-3` (`decompositions/ADVI_COTBKF_DECOMP.round82.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ of code and configuration in the tree plus ONE docstring correction in ONE script. Nothing else is edited. Nothing is built, served, corrected or fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_82_20261013.md` whole, section 2 rulings 2 and 3 and section 3 item 3, word for word: "W158-S2 disarms on a read that names 0 ticker-only readers (the builder `build_canonical_prices_v2.py` and the two minted-table
readers first), or, if any exists, on a keyed fix to the (ticker, asset_name) pair. The keyed fix is in pattern: one store, one Opal key." and "The adapter header's 'no S3 write' is corrected in the same cell (W158-S5). The file carries a guarded `--apply` mint."
Then the channel rows `ADVI_COTBKF-D2-W159-S1` (the store holds two `asset_name` values under one ticker: SCCO, a 3.875% 04/23/2025 bond row at the equity's price, on 1,027 dates; APH `CL A` and `NEW CL A` on 70 dates, equal on 69 and different on 2026-04-14), `ADVI_COTBKF-D2-W158-S2` and `-S5`, the stage record
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~159/STAGE_READ.json` and the consumer record `deliverables/0.9.0_WK_ADVI_COTBKF~158/CONSUMER_READ.json`.

**The store:** `s3://opal-data-cot/silver/prices/canonical_prices.parquet`, columns `date, asset_name, ticker, price, source`. You do NOT download it again in this cell; the counts above are the record's. If you need a count the record lacks, say so as `not_established` unless one read-only `get-object` of that one key at version `76.rgWIXYdLNsXSwrXvyuEmaEtfr9y98` (97,443,387 bytes) into your worktree's `.scratch/` is
the only way: that single read is granted, with the byte length checked.

**Your item.**

1. **Every reader of the store, found through the graph first and then each file's own code.** The graph first (`org/modules/graph/graph-call-manifest.yaml`, QUERY never rebuild, its age printed), then `comp-find` and `comp-estate` for the key `silver/prices/canonical_prices`, the table name the registry gives it (`infra/logic/registry/legacy_addresses.json:11-13` names the key), and the readers named by round 81 and round 79
   (`data/cot/scripts/gold/build_canonical_prices_v2.py`, `data/assets/scripts/silver/commonwealth_account_return_daily.py:221-226`, `commonwealth_price_basis_census.py:292-295`, `data/assets/scripts/analysis/commonwealth_price_census.py:57-58`, and every other hit). The denominator of every search (files scanned) is printed beside its hits; `0 hit(s) across 0 file(s)` is out-of-corpus, not absence.
2. **For each reader, one of:** `keyed_ticker_only` (it selects, joins or groups by `ticker` without `asset_name`), `keyed_pair` (by `(ticker, asset_name)` or by a CUSIP-derived key), `keyed_other` (say what), `writer_only`, or `not_established`. Cite file and line. Where a reader is `keyed_ticker_only`, say what it does with two rows for one ticker and date (takes the first, last, mean, or fails), and for SCCO and APH which of the two rows it would take.
3. **The count and the verdict:** `ticker_only_readers` (an integer), and `verdict_fact` one of `zero_ticker_only_readers` (this needs a positive control: the same search finds a reader known to be keyed by ticker, e.g. the builder's own join), `ticker_only_readers_found`, or `not_established`.
4. **The keyed fix, described and NOT made:** if any reader is ticker-only, list the files and lines a `(ticker, asset_name)` key would touch. This is a description for the next cut.
5. **The header correction (row D2-W158-S5), the ONE edit of this cell.** In `data/assets/scripts/silver/commonwealth_account_return_daily.py` the module docstring (lines 1-12) says "NO S3 WRITE anywhere in this file; the mint is CB-al-2's, on the applier, through emit_day(upload=True)." The file carries a guarded `--apply` mint (the argparse help at `:1556`, the guard at `:460` and `:856-867`, the `--apply` text at `:80` and `:89`).
   Replace that one sentence so it is true: the default build writes locally only and uploads nothing; `--apply` is a guarded mint of the local days through the producer's `emit_day(upload=True)` (name the guard that refuses it, from the lines above, with their line numbers as the file now stands). Change nothing else: not the other two places that say "no S3 write" (`:702` is inside a generated string, `:1553` is the argparse description; both are
   read-only findings you REPORT with their lines and do not edit). Docstring text only, ASCII only. After the edit: `python -m py_compile data/assets/scripts/silver/commonwealth_account_return_daily.py`; `git diff --numstat` for that file shows changed lines inside lines 1-14 only (state the numbers); commit through `.tools/safe-commit.sh` with the file named; the commit gate (py_compile, ds-precommit, ruff) passes and you quote its lines.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~163/TICKER_KEY_READ.json` and a short `.md`. Top-level keys, exactly: `graph` (`{"provenance", "age", "calls": [{"call", "output_rows"}]}`), `readers` (a list: `{"path", "line", "kind", "what_it_does_with_two_rows", "scco_takes", "aph_takes"}`), `searches` (a list: `{"term", "scope", "files_scanned", "hits"}`), `positive_control` (`{"reader", "found"}`),
   `ticker_only_readers` (an integer), `verdict_fact`, `keyed_fix_would_touch` (a list), `header` (`{"file", "old_sentence", "new_sentence", "lines_changed", "other_no_s3_write_lines": [{"line", "kind"}]}`), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB82cd3-AC1" cell_refs="CB-cd-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~163/TICKER_KEY_READ.json',encoding='utf-8'));r=d['readers'];print('TICKER-KEY-READ readers=%d ticker_only=%d verdict=%s searches=%d graph_calls=%d control_found=%s'%(len(r),d['ticker_only_readers'],d['verdict_fact'],len(d['searches']),len(d['graph']['calls']),d['positive_control']['found']))"</invocation><expect>TICKER-KEY-READ readers=</expect></criterion>
`CB82cd3-AC1` -- every reader found is listed with its key kind; the count, the verdict and the positive control are in the record; every search carries its denominator. The issuer reads whether row D2-W158-S2 disarms.

<criterion id="CB82cd3-AC2" cell_refs="CB-cd-3"><invocation>python -c "import py_compile,ast;p='data/assets/scripts/silver/commonwealth_account_return_daily.py';py_compile.compile(p,doraise=True);t=open(p,encoding='utf-8').read();doc=ast.get_docstring(ast.parse(t)) or '';print('HEADER-FIX py_compile=OK old_sentence_gone=%s mentions_apply=%s ascii_only=%s'%('NO S3 WRITE anywhere in this file' not in doc,'--apply' in doc,all(ord(c)<128 for c in doc)))"</invocation><expect>HEADER-FIX py_compile=OK old_sentence_gone=True mentions_apply=True ascii_only=True</expect></criterion>
`CB82cd3-AC2` -- the module docstring no longer carries the false sentence, now names `--apply`, is ASCII, and the file compiles.

<criterion id="CB82cd3-AC3" cell_refs="CB-cd-3" judgment="true"/>
`CB82cd3-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the graph was queried first and its age printed; `zero_ticker_only_readers` is claimed only with a positive control and every search's denominator; a reader that selects by ticker is not called keyed_pair; the header diff touches the docstring lines only and the new sentence is true of the file as it stands (the guard lines it cites are the real ones); the two other "no S3 write" lines are reported and left alone.

<expected_criteria>CB82cd3-AC1,CB82cd3-AC2,CB82cd3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder, the ONE script named in it and your own NEW channel row) and the file of this order.
- **You change nothing but the docstring sentence of the one script in `<paths>`.** No other code, test, config, manifest, registry, graph or infrastructure. QUERY the graph; never rebuild it.
- **AWS: none, except the single optional `get-object` described above** (that key and version, into your `.scratch/`, byte length checked). No listing, write, delete or serve.
- **Another firm's data is never opened.** No account id and no account's value: counts, tickers, dates, prices and line numbers only.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`; keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket; do not run the adapter at all.** No push. No `--refresh`. **No vendor call and no fetch.**
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- Searches go through the estate's tools (`comp-find`, `comp-estate`, the native Grep on a named path); a recursive shell search of the repository is denied by a hook and is not retried another way.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D2-W163-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`),
  APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
data/assets/scripts/silver/commonwealth_account_return_daily.py
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row; the one script edit is the docstring sentence of item 5.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round82.md</decomp_doc> (round 82), cell `CB-cd-3`.
<owned_cells>CB-cd-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB82cd3-AC1, CB82cd3-AC2, CB82cd3-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~163/ADVI_COTBKF.TO-CB-cd-3.ticker-key-read-and-header.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB82cd3-AC1,CB82cd3-AC2,CB82cd3-AC3` BEFORE the flip. Mechanical: CB82cd3-AC1, CB82cd3-AC2. A judgment criterion is recorded with status `UNVERIFIABLE-BY-INSTRUMENT` and a `status_reason` that begins `PENDING-ADJUDICATION`, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. You flip your own order `<status>` to `complete` in the commit that carries the proof instance, as the earlier rounds' workers did.
</proof_of_spec>

**REPORT:** every reader with its file, line and key kind; the count and the verdict with the positive control; what a ticker-only reader does with two rows for SCCO and APH; every search with its denominator; the graph's provenance and age; the keyed fix's footprint; the header's old and new sentence, the lines changed and the commit gate's lines; the two other "no S3 write" lines; the `TICKER-KEY-READ` and `HEADER-FIX` lines; every remote read made (or none); the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of code plus one docstring sentence; nothing is scheduled or served.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call beyond the one optional read of an Opal object under the existing role; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the graph is queried first; a zero needs a positive control; a ticker-selecting reader is not called keyed_pair; the header diff is docstring lines only; BLIND: a reader outside the tree, a reader that keys by a lower-cased or stripped ticker, and a consumer of a local copy of the store.
lane: the <paths> block IS the grant (worker RULING 1); the one script in it is edited for its docstring sentence only.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-82 analysis @ea59dfcdec (msg 7196), section 2 rulings 2 and 3, section 3 item 3; `3.0.0_SA_CVO` REMEDIATION_v50 @43b340c673.
