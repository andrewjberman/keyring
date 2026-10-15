# TO ADVI_COTBKF.TO-CB-ch-2.active-bloomberg-need -- round 86 CB-ch-2: the active Cottonwood set's full Bloomberg need in cells, its day rate and finish date, ordered by value held and cut into one-day request slices

<to_id>ADVI_COTBKF.TO-CB-ch-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~170</issued_to>
<issued_by>2.0.0_SA_COO~C1</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>86</round>
<workstream>~C1</workstream>

**Directive:** D8 | **Fabric:** dell1 (placement DELL1) | **Decomp cell:** `CB-ch-2` (`decompositions/ADVI_COTBKF_DECOMP.round86.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**Why.** Andrew, 2026-10-15: "Active accounts should get BBG pricing exclusively." The active Cottonwood set has 3,368 securities. Two Bloomberg requests already exist for part of it (B1, 613 CUSIPs, 34,437 cells; the Yahoo-failed-14, 14 CUSIPs, 7,685 cells). Nobody has yet priced the REST in cells, said when it would finish at the daily rate, or put it in the order the largest positions price first. You do that, from the committed active set, and you leave request files ready to queue. You make NO vendor call and draw nothing.

**Read first (under `C:/dev/ajb_workspace`):**
1. `data/mdpf/scripts/demque/b1_request.py` (read the whole module docstring: the option C depth, the money market skip, the active-window clip, `held_back`, `emptied`, the `--names PATH --request-id ID --out PATH` mode and the ONE JSON line it prints) and `data/mdpf/scripts/demque/active_set.py` (reads the committed V2 file by sha256).
2. `data/mdpf/scripts/demque/bbg_quote.py` (the cell rules by channel and `quote(...)`) and `data/mdpf/scripts/demque/bbg_allowance.json` (the history channel's `ceiling`, the cells per day, with its `claim` and `basis`).
3. The two existing requests and their quotes, to learn the request and quote file form and to subtract their names: `org/missions/D8/MDPF/MDPF_DEMQUE/requests/MDPF_SECHIST-CARD-A-B1-OPTION-C.json` (+ `.quote.json`), `org/missions/D8/MDPF/MDPF_DEMQUE/requests/MDPF_SECHIST-CARD-A-B1-YAHOO-FAILED-14.json` (+ `.quote.json`).
4. The committed active set: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ACTIVE_COTTONWOOD_SET_V2.csv` (sha256 `5cef7ab0c9e10fe299cb757d4dba31792d069bad35f7250defa76e18773046ae`; columns `account_key,source_side,cusip,ticker,held_from,held_to,window_basis`; it carries raw account numbers: they never leave it).

**Your items.**

1. **The names.** From the V2 file take the distinct non-blank CUSIPs that are not cash (`CASH`, and the cash tickers the file marks, such as `FCASH`; state your exact rule and count what it removes). That is the active need (the research note reads 3,367 non-cash CUSIPs; print yours). Subtract the CUSIPs already carried by the B1 request's `securities` and by the failed-14 request's `securities`. The remainder is the NEW set; print the partition: need = in B1 + in failed-14 + NEW.
2. **The build.** Write the NEW CUSIPs to a names file under `.scratch/` in the form `b1_request.py --names` reads, and run `python data/mdpf/scripts/demque/b1_request.py --names <file> --request-id ADVI_COTBKF-ACTIVE-BBG-ALL --out <scratch path>` (S3 read only; it makes no vendor call). Record its ONE JSON line verbatim in your record: securities, cells, days_to_finish, finish_date, clipped, emptied, held_back (a count and the reasons by count), skipped one-dollar. Names the builder cannot price (no transaction in the Commonwealth silver table, so no window for it; names held only at Black Diamond) are counted separately and named by CUSIP in the record, with the rule you used to window them if you windowed them, else `not_priced_by_this_builder`.
3. **The day rate.** From `bbg_allowance.json` read the history channel's `ceiling` (cells per day), its `claim` and its `basis`, and state the figure you used. The research note names about 23,432 cells a day; you state which figure the committed file gives and why they may differ, and you quote at the file's figure. Compute the finish date for NEW alone, and for NEW plus B1 plus failed-14 together (their cells are in their quote files), starting the first draw day after 2026-10-17, using `lib/trading_calendar.py` for trading days.
4. **The order by value held.** Value held per CUSIP = the sum over active accounts of the market value in the latest Black Diamond snapshot (2026-10-12). Find the value column in `s3://opal-data-cot/silver/holdings/` or `s3://opal-data-cot/gold/canonical/holdings/` (read-only; state which table and column carry it; if neither carries a market value, order by number of active accounts holding the CUSIP on the latest snapshot and say so; a CUSIP no active account holds on the latest snapshot, held only in history, ranks last, ordered by cells). Write the dollars, if any, ONLY to `C:/dev/_cotbkf_bbg_need_20261015/VALUE_HELD.csv` (outside the repository: columns `cusip,value_held,accounts_holding`). In the repository, write the ranking only: `ACTIVE_BBG_ORDER.csv` with columns `cusip,rank,slice,cells,held_open` and no dollar value.
5. **The slices.** Cut the NEW request into SLICES in rank order, each slice at most one day's cells (the ceiling you used in item 3), a CUSIP's cells never split across two slices. Write each slice as a request file in the same form as the existing B1 file: `ACTIVE_BBG_SLICE_01.json`, `_02.json`, ... under `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~170/slices/`, with request ids `ADVI_COTBKF-ACTIVE-BBG-01`, `-02`, ..., and beside each a `.quote.json` made by `bbg_quote.quote` the way the existing quote files were made (read `MDPF_SECHIST-CARD-A-B1-OPTION-C.quote.json` for the form). The tier, `need_class` and `window_start` of each slice are the builder's own output; do not hand-edit a field. Do NOT place any file in `org/missions/D8/MDPF/MDPF_DEMQUE/`.
6. **Baseline for the pace record.** Count the active non-cash CUSIPs that already have a Bloomberg-sourced price series in any Opal store (search `s3://opal-data-assets/bloomberg/` and the MDPF_SECHIST `security_series/` prefix by listing; state each prefix listed, its object count and what a hit means); print 0 of N if none. This is the first of the three pace counts (the Yahoo count is `MDPF_DEMQUE` cell `DQ-t-64`'s; the third is the issuer's at the round close).
7. **The script and the record.** The code that does items 1 and 3 to 5 is one committed file `data/assets/scripts/silver/cotbkf_active_bbg_need.py` (it shells out to `b1_request.py` and imports `bbg_quote`; it changes neither), with a test `data/assets/scripts/silver/tests/test_cotbkf_active_bbg_need.py` on stubs (made-up CUSIPs `T00000001`...) proving three things, one test each: the partition sums; slices never exceed the day's cells and never split a CUSIP; rank order is non-increasing in value then ties by cells. The script carries no account number, name or dollar. Write `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~170/ACTIVE_BBG_NEED_RECORD.json` with exactly these top-level keys: `v2_sha256`, `need_cusips`, `cash_rule`, `in_b1`, `in_failed14`, `new_cusips`, `builder_line` (the verbatim one-line JSON of item 2), `not_priced_by_this_builder`, `day_rate` (`{"cells_per_day", "claim", "basis"}`), `cells_new`, `days_new`, `finish_new`, `cells_all`, `days_all`, `finish_all`, `value_source`, `slices` (`{"count", "max_cells", "sum_cells", "files"}`), `baseline_bbg_series` (`{"active_cusips", "with_bloomberg_series", "stores_listed"}`), `not_established`; and a short `.md` beside it with the same figures in a table. No account number, name or dollar appears in either.

### ACCEPTANCE

<criterion id="CB86ch2-AC1" cell_refs="CB-ch-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~170/ACTIVE_BBG_NEED_RECORD.json',encoding='utf-8'));ok=d['in_b1']+d['in_failed14']+d['new_cusips']==d['need_cusips'];print('ACTIVE-BBG-NEED need=%d new=%d cells_new=%d cells_per_day=%d days_new=%d finish_new=%s partition_sums=%s'%(d['need_cusips'],d['new_cusips'],d['cells_new'],d['day_rate']['cells_per_day'],d['days_new'],d['finish_new'],ok))"</invocation><expect>partition_sums=True</expect></criterion>
`CB86ch2-AC1` -- the need, its partition against the two existing requests, its cells, its day rate and its finish date are printed from the record, and the partition sums.

<criterion id="CB86ch2-AC2" cell_refs="CB-ch-2"><invocation>python -c "import json,glob,csv;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~170/ACTIVE_BBG_NEED_RECORD.json',encoding='utf-8'));base='org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~170/';rows=list(csv.DictReader(open(base+'ACTIVE_BBG_ORDER.csv',encoding='utf-8')));s=d['slices'];fs=sorted(glob.glob(base+'slices/ACTIVE_BBG_SLICE_*.json'));cusips=sum(len(json.load(open(f,encoding='utf-8'))['securities']) for f in fs);print('ACTIVE-BBG-SLICES files=%d count=%d max_cells=%d day=%d sum_cells=%d order_rows=%d slice_cusips=%d within_day=%s no_dollar_column=%s'%(len(fs),s['count'],s['max_cells'],d['day_rate']['cells_per_day'],s['sum_cells'],len(rows),cusips,s['max_cells']<=d['day_rate']['cells_per_day'],'value_held' not in rows[0]))"</invocation><expect>within_day=True no_dollar_column=True</expect></criterion>
`CB86ch2-AC2` -- the slice files exist and match the record's count, no slice exceeds a day's cells, and the committed order file carries no dollar column.

<criterion id="CB86ch2-AC3" cell_refs="CB-ch-2"><invocation>python -m pytest data/assets/scripts/silver/tests/test_cotbkf_active_bbg_need.py -q</invocation><expect>3 passed</expect></criterion>
`CB86ch2-AC3` -- the partition, slice and ordering rules hold on stubs.

<expected_criteria>CB86ch2-AC1,CB86ch2-AC2,CB86ch2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and the folder `C:/dev/_cotbkf_bbg_need_20261015/` (the one outside file `VALUE_HELD.csv`). You change no other file. You do not edit `b1_request.py`, `bbg_quote.py`, `bbg_allowance.json`, `active_set.py`, any file under `data/mdpf/`, the two existing requests, the V2 file, or anything under `org/missions/D8/MDPF/`.
- **AWS: READ-ONLY, through the `.tools/aws` shim,** of `s3://opal-data-cot/silver/holdings/`, `s3://opal-data-cot/gold/canonical/holdings/`, the Commonwealth silver transactions and crosswalk the B1 builder itself reads, and the listings in item 6. State each listing's denominator. No write, delete or serve; no other bucket; not the restricted CRM prefix. Do not run `aws sts get-caller-identity`.
- **NO vendor call of any kind, no Bloomberg sign-in, no queue draw, no change to `draw_hold`, no file placed in the DEMQUE tree.** Filing the slices is the issuer's act.
- **Account numbers and dollar values never appear in the repository, a report or a message.** Counts, dates, ranks and CUSIPs only. The dollars live in the one outside file.
- After your last commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s` and give its DENOMINATOR line.
- **NEVER** `--apply`, an S3 write or delete, `--refresh`. No push. No gate override and no `--force`. Do not weaken, delete, xfail or skip any test. Scratch under the worktree `.scratch/`, never committed.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id `ADVI_COTBKF-D1-W170-S<k>` (k from 1), `"fabric": "dell1"`, `surfaced_at` read from the clock (`date -u +%FT%TZ`), APPENDED to the channel file with `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with an editing tool.

<paths>
data/assets/scripts/silver/cotbkf_active_bbg_need.py
data/assets/scripts/silver/tests/test_cotbkf_active_bbg_need.py
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant for the repository. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round86.md</decomp_doc> (round 86), cell `CB-ch-2`.
<owned_cells>CB-ch-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB86ch2-AC1, CB86ch2-AC2, CB86ch2-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~170/ADVI_COTBKF.TO-CB-ch-2.active-bloomberg-need.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB86ch2-AC1,CB86ch2-AC2,CB86ch2-AC3` BEFORE the flip. All three criteria are mechanical. An artifact already committed and not changed in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`. **YOU flip your own order `<status>` to `complete` in the commit that carries the proof instance, and only when every criterion PASSES** (the flip is inside your grant: the order's own face is lane ANY).
</proof_of_spec>

**REPORT:** FIRST the ONE line the builder printed and the three numbers the issuer needs: NEW cells, the day rate with its claim, the finish date for NEW and for all three requests together. Then: the partition; the value source (table and column, or the fallback you used); the slice count and the largest slice; the not-priced names by count; the baseline count (0 of N or the figure) with each prefix listed; every S3 read with its denominator; the three criterion lines; the account-id scan's DENOMINATOR line; commits; every gate refusal and hook denial, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE reads of tables and request files; nothing is scheduled or drawn.
comp-iam: DECLARED-NOT-APPLICABLE read-only calls on Opal data under the existing role; no write, delete or serve, and no new permission.
comp-adversary: RUN -- the cell prices a request and draws nothing; the day rate is read from the allowance file with its claim and may differ from the research note's 23,432 (the order makes the worker say which and why); the dollars stay outside the repository; BLIND: names held only at Black Diamond since 2026-04-22 (no Commonwealth transaction), which the B1 builder windows from transactions and may not reach; the order counts them and does not price them.
lane: the <paths> block IS the grant (worker RULING 1). Nothing is written under `data/mdpf/` or the DEMQUE tree.
</preflight>

Source: `1.0.0_SA_CTO~DELL1` ruling @f984c02191 items 2 and 6; `4.0.0_SA_CRO~DELL2` research note `RESEARCH_20261015_COTTONWOOD_BACKFILL_STATE.md` @03d1a87a9c (the 3,367 and the 23,432 are its figures, unverified here).
