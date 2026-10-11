# TO ADVI_COTBKF.TO-CB-bm-2.price-requests -- round 65 CB-bm-2: the two price requests, written and sized, and NOT sent

<to_id>ADVI_COTBKF.TO-CB-bm-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~95</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>65</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bm-2` (`decompositions/ADVI_COTBKF_DECOMP.round65.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**RULE: counts, shares, security identifiers (CUSIP, symbol), asset kinds, dates, transaction types, file-and-line citations and reason codes only** in your record, report, commit messages and rows. Never an account id, never an account's position size, value, flow or return tied to an account. A RATIO of two of an account's numbers may be reported to two decimal places. Aggregate before you print.

**This is a MEASUREMENT that ends in two written requests. NOTHING IS SENT, PULLED OR FETCHED: no Yahoo call, no Bloomberg call, no
network.**

**Read first, in this order:**
1. `integrations/bloomberg/READ_HERE.md`, IN FULL. The Bloomberg request must be one a seat that has read that file would write: it
   names the surface, respects the budget and the queue, and asks for nothing the file says cannot be asked. Quote, with line numbers,
   each rule of that file your request relies on.
2. `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_65_20261011.md` sections 1, 3 item 2 and 4 item 2.
3. `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md` lines 205 to 225 (Andrew's word on the two sources; where prices land).
4. The round-64 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~90/PRICE_COVERAGE_BY_KIND.json` and its `.md`.
5. `data/assets/scripts/analysis/commonwealth_price_need.py` and `commonwealth_price_need_file.py`: the build already has a
   price-need computation and a kind-to-source grouping (lines 10 to 11 of the second). USE them; do not write a second grouping.

**Why.** The returns table is about 94 percent blank because 15,993,996 of 21,102,041 position rows carry no value, and no data
already held prices them. Andrew's word names two sources. The CTO wants the two requests WRITTEN, each sized, before either is sent.

**Your item, over the WHOLE table (2013-04-03 to 2026-06-22), not one date.**

1. From `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet` (columns account, date, cusip, value, price_source) and the silver
   transactions cache `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/trade_year=*/*.parquet` (Cusip, Asset_Type, Symbol): the unpriced position rows. They must
   total 15,993,996 of 21,102,041. If not, that is the refusal clause.
2. Assign every unpriced SECURITY to a leg by the build's own grouping: `YAHOO` (equity, ETF and fund kinds), `BLOOMBERG` (fixed income
   and other). Report separately the securities in a Yahoo kind that carry NO symbol: a symbol request cannot name them, so say how
   many there are and what identifier the delivery does carry for them.
3. For each leg: the securities; for each security its identifier (symbol where there is one, else CUSIP), its kind, and the first and
   last date on which it is held unpriced; the SECURITY-DAY count (distinct security x date held unpriced); the unpriced position rows.
4. What each leg would unblank. An account-day is blank for price when at least one of its holdings rows is unpriced. Count the
   account-days where EVERY unpriced row belongs to (a) the Yahoo leg alone, (b) the Bloomberg leg alone, (c) both legs together (that
   is all of them), and give each as a share of the blank-for-price account-days. Say plainly that these are UPPER BOUNDS: a source may
   not price every security it is asked for, and a return also needs the prior day's value.
5. Write TWO request documents in your deliverables folder, each a `.md` a person can read plus a `.csv` of its securities
   (identifier, kind, first_date, last_date, security_days):
   - `PRICE_REQUEST_YAHOO.md` / `.csv`
   - `PRICE_REQUEST_BLOOMBERG.md` / `.csv`
   Each `.md` states: what is asked, for which securities and dates, the size, where the prices land (MDPF_SECHIST's securities
   history, which this project does not own), what it would unblank (upper bound), what is not established, and at its top the line
   `STATUS: WRITTEN, NOT SENT`. The Bloomberg one also states the budget and queue rules it relies on, with their line numbers.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~95/PRICE_REQUESTS.json`. Top-level keys, exactly: `position_rows`, `unpriced_position_rows`, `unpriced_securities`,
   `blank_for_price_account_days`, `legs` (a list of `{"leg", "securities", "securities_without_symbol", "security_days",
   "unpriced_position_rows", "account_days_unblanked_alone", "first_date", "last_date", "by_kind"}`), `both_legs_account_days`,
   `bloomberg_rules_relied_on` (a list of `{"line", "text"}`), `evidence`, `not_established`.

### ACCEPTANCE

<criterion id="CB65bm2-AC1" cell_refs="CB-bm-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~95/PRICE_REQUESTS.json',encoding='utf-8'));L=d['legs'];print('PRICE-REQUESTS-RECORD position_rows=%d unpriced_position_rows=%d legs=%d leg_rows_sum=%d unpriced_securities=%d leg_securities_sum=%d bloomberg_rules=%d'%(d['position_rows'],d['unpriced_position_rows'],len(L),sum(x['unpriced_position_rows'] for x in L),d['unpriced_securities'],sum(x['securities'] for x in L),len(d['bloomberg_rules_relied_on'])))"</invocation><expect>PRICE-REQUESTS-RECORD position_rows=21102041 unpriced_position_rows=15993996 legs=2 leg_rows_sum=15993996</expect></criterion>
`CB65bm2-AC1` -- the totals are the measured ones and the two legs cover every unpriced row exactly once.

<criterion id="CB65bm2-AC2" cell_refs="CB-bm-2"><invocation>python -c "import io;D='DIorg/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~95/PRICE_REQUESTS.json';y=io.open(D+'PRICE_REQUEST_YAHOO.md',encoding='utf-8').read();b=io.open(D+'PRICE_REQUEST_BLOOMBERG.md',encoding='utf-8').read();print('PRICE-REQUESTS-STATUS yahoo_not_sent=%s bloomberg_not_sent=%s yahoo_csv_rows=%d bloomberg_csv_rows=%d'%('STATUS: WRITTEN, NOT SENT' in y,'STATUS: WRITTEN, NOT SENT' in b,len(io.open(D+'PRICE_REQUEST_YAHOO.csv',encoding='utf-8').read().splitlines())-1,len(io.open(D+'PRICE_REQUEST_BLOOMBERG.csv',encoding='utf-8').read().splitlines())-1))"</invocation><expect>PRICE-REQUESTS-STATUS yahoo_not_sent=True bloomberg_not_sent=True</expect></criterion>
`CB65bm2-AC2` -- both request documents exist, each marked written and not sent, each with its security list.

<criterion id="CB65bm2-AC3" cell_refs="CB-bm-2" judgment="true"/>
`CB65bm2-AC3` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the Bloomberg request is one a seat that read
`integrations/bloomberg/READ_HERE.md` would write; the unblank counts are stated as upper bounds with their denominator; the legs
follow the build's own grouping and Andrew's word; nothing was sent.

<expected_criteria>CB65bm2-AC1,CB65bm2-AC2,CB65bm2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** You READ local data under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` (the base checkout; never write
  there) and write scratch under your own worktree `.scratch/` only (never committed).
- **No network call of any kind**: no AWS, no Yahoo, no Bloomberg, no HTTP. Everything you need is local.
- **No gate override** of any kind and no `--force`. If a gate refuses a commit, stop and report its exact refusal line.
- **Do not open or print** anything under `C:/dev/_cotbkf_private_evidence_20261009/`. A commonwealth script you run carries
  `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row: the next
  free `ADVI_COTBKF-D2-S<k>` id read from the channel at write time, `"fabric": "dell2"`, `surfaced_at` read from the clock.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round65.md</decomp_doc> (round 65), cell `CB-bm-2`.
<owned_cells>CB-bm-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB65bm2-AC1, CB65bm2-AC2, CB65bm2-AC3. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~95/ADVI_COTBKF.TO-CB-bm-2.price-requests.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB65bm2-AC1,CB65bm2-AC2,CB65bm2-AC3` BEFORE the flip. Mechanical: CB65bm2-AC1 and CB65bm2-AC2. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the `PRICE-REQUESTS-RECORD` and `PRICE-REQUESTS-STATUS` lines; per leg: securities, securities without a symbol, security-days, unpriced rows, date span, account-days unblanked alone; both legs together; the Bloomberg rules relied on with line numbers; what is not established; a statement that nothing was sent; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement and two documents.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network call.
comp-adversary: RUN -- totals are pinned so a wrong join stops the cell; the two legs must sum to every unpriced row; both documents must carry the not-sent line; the grouping is the build's own; BLIND: whether either source in fact prices a named security, which only a pull shows.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-65 analysis @1e9128413f (msg 4715), section 4 item 2; `3.0.0_SA_CVO` REMEDIATION_v37 @054e94e8fc.
