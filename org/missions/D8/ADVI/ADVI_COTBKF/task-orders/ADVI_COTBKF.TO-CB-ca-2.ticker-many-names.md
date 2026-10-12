# TO ADVI_COTBKF.TO-CB-ca-2.ticker-many-names -- round 79 CB-ca-2: of the securities this firm held, how many have a ticker carrying more than one asset name, and whether each is priced from its own rows

<to_id>ADVI_COTBKF.TO-CB-ca-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~152</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>79</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-ca-2` (`decompositions/ADVI_COTBKF_DECOMP.round79.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a COUNT on local copies. You change no code. Nothing is fetched and no bucket is read.**

**Read first:** `org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md`, the two sections headed `## ADDENDUM v0.8` (near line 292: it is also the round-79 analysis and holds the ENRICHMENT LIST) and `## ADDENDUM v0.9` (near line 343, the SIGNED text: it REPLACES item 2 of C-BASIS; v0.8's two tokens AS_TRADED and ADJUSTED are WITHDRAWN and are not used anywhere), the paragraph on rows D2-W149-S1 and D2-W149-S2 ("S2 widens the question past the 15 funds: 308 of 4,000
tickers carry more than one asset name and the build reads by ticker. Item 2 of the list below sizes it for what this firm held.")
and ENRICHMENT LIST item 2, word for word: "Of the securities this firm held, how many have a ticker carrying more than one asset
name, and for each whether its held days are priced from its own rows. Counts only." Then row ADVI_COTBKF-D2-W149-S2 in the
channel and the round-78 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~149/STORE_UNADJUSTED_FIELD.json` (the store's schema: `date`, `asset_name`, `ticker`, `price`, `source`; 11,289,398
rows; 5,748,151 with no ticker; 308 of 4,000 tickers with more than one asset name; VGHAX carries three). How the build reads the
store: `data/assets/scripts/analysis/commonwealth_price_census.py` (which key it reads the store by, and what it does when a key
returns rows of more than one asset name) and `data/assets/scripts/silver/commonwealth_daily_valuation.py` (how a held security
is joined to a price: by ticker, by CUSIP, by name).

**The store, on disk:** the object the round-78 worker downloaded is at `C:/dev/wk-cotbkf-84/.scratch/w149/store/` (this firm's; read it there; do not download it
again). **The build's prices:** `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet` (cusip, date, price, store). **What the firm held:**
`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet` (the securities with a held day; counts only).

**Your item.**

1. **The denominators first:** securities this firm held (distinct, in the build's table); of them, those the build prices from
   the silver price store by ticker; of those, the ones whose ticker carries MORE THAN ONE asset name in the store. Reproduce the
   store-wide 308 of 4,000 first, as the control.
2. **THE TEST FIRST.** Before any security is classed, write to a file in your scratch (with a clock timestamp) and copy into the
   record what "priced from its own rows" means and how it is decided: for a held security whose ticker carries several names,
   (a) how its OWN name is identified (the custodian's description for its CUSIP against the store's `asset_name`: the matching
   rule, stated); (b) the names under that ticker carry the SAME price series or DIFFERENT ones (equal on every common date within
   a stated tolerance, or not); (c) which rows the build's price for that security equals, day by day: its own name's, another
   name's, a mixture; the classes: `own_rows`, `another_names_rows`, `mixed`, `names_identical_so_indistinguishable`,
   `own_name_not_identified`; (d) the thresholds. Then keep it.
3. **Each such held security classed,** counts per class, with the held days and (as COUNTS) the priced holding account-days and
   measured account-days on the days that are NOT from its own rows. By kind of security. The 15 failing funds reported apart
   (which of them carry more than one name, and their class).
4. **The other half of the row:** half the store's rows have no ticker. Of the securities this firm held, how many have NO ticker
   in the custodian's rows or none in the store, and how the build prices them then (from which store, by which key), as counts.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~152/TICKER_MANY_NAMES.json`, a `.csv` (columns: cusip, ticker, names_under_ticker, class, held_days, days_not_own_rows, kind;
   CUSIPs only in the column named exactly `cusip`) and a short `.md`. Top-level keys, exactly: `control` (`{"tickers",
   "with_more_than_one_name"}`), `test` (`{"text", "written_at"}`), `held_securities`, `priced_from_the_store_by_ticker`,
   `ticker_with_more_than_one_name`, `classes` (an object: class to count), `not_own_rows` (`{"securities", "held_days",
   "priced_holding_account_days", "measured_account_days"}`), `the_15` (a list), `no_ticker` (`{"held_securities", "how_priced"}`),
   `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB79ca2-AC1" cell_refs="CB-ca-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~152/TICKER_MANY_NAMES.json',encoding='utf-8'));c=d['classes'];n=d['not_own_rows'];print('TICKER-MANY-NAMES control=%d/%d test_written=%s held_securities=%d priced_by_ticker=%d ticker_many_names=%d classed=%d not_own_rows=%d measured_account_days=%d the_15_listed=%d classes=%s'%(d['control']['with_more_than_one_name'],d['control']['tickers'],bool(d['test']['written_at']),d['held_securities'],d['priced_from_the_store_by_ticker'],d['ticker_with_more_than_one_name'],sum(c.values()),n['securities'],n['measured_account_days'],len(d['the_15']),json.dumps(c,sort_keys=True)))"</invocation><expect>TICKER-MANY-NAMES control=308/4000 test_written=True</expect></criterion>
`CB79ca2-AC1` -- the store-wide control reproduces; the test was written first; every held security whose ticker carries more than
one name is classed (`classed` equals `ticker_many_names`); the issuer reads how many are not priced from their own rows.

<criterion id="CB79ca2-AC2" cell_refs="CB-ca-2" judgment="true"/>
`CB79ca2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the denominators run from every held security down;
the rule for a security's own name and for "its own rows" was written before any was classed; names that carry the same series
are said to be indistinguishable and not counted as wrong; a security whose own name cannot be identified is that class and not
`own_rows`; no account id or amount appears.

<expected_criteria>CB79ca2-AC1,CB79ca2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local: no S3 read, no network call. The store object is
  read where the round-78 worker left it; it is not downloaded again.
- No account id and no account's value: counts only.
- After your commit run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`;
  keep CUSIPs in CSV columns named exactly `cusip` and tickers elsewhere; report its DENOMINATOR line.
- **NEVER `--apply`, `--remint`, `--overwrite`, a serve, or any S3 write or delete against a real bucket.** No push. No `--refresh`.
  **No vendor call and no fetch** (no Yahoo, no Bloomberg, no gateway series pull): what is on disk is read, never refreshed.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity, share balance or return. Counts, dates, CUSIPs, tickers, a
  security's price or per-share distribution, ratios and reason codes only.
- **No gate override** of any kind and no `--force`. Do not weaken, delete, xfail or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W152-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round79.md</decomp_doc> (round 79), cell `CB-ca-2`.
<owned_cells>CB-ca-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB79ca2-AC1, CB79ca2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~152/ADVI_COTBKF.TO-CB-ca-2.ticker-many-names.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB79ca2-AC1,CB79ca2-AC2` BEFORE the flip. Mechanical: CB79ca2-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the control (308 of 4,000) as reproduced; the test as written before any security was classed, with its timestamp; the denominators from every held security down; the classes with their counts; the securities not priced from their own rows, with held days and the account-day counts; the 15 failing funds apart; the no-ticker half and how the build prices it; how the build joins a held security to a price, with file and line; the `TICKER-MANY-NAMES` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a count over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the store-wide count of round 78 is the positive control; the rule for a security's own name and its own rows is written before any is classed; names carrying one series are indistinguishable and are not counted as wrong; a name that cannot be identified is its own class; BLIND: a security the custodian describes differently from the store, matched to no name.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` PRD ADDENDUM v0.8 @fab39b5beb, which is also the round-79 analysis (msg 6275), its ENRICHMENT LIST item 2, with ADDENDUM v0.9 @95da777fbf (msg 6282), the SIGNED text; `3.0.0_SA_CVO` REMEDIATION_v47 @77527824fd.
