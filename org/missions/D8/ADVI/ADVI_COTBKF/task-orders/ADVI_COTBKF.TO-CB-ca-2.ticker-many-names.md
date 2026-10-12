# TO ADVI_COTBKF.TO-CB-ca-2.ticker-many-names -- round 79 CB-ca-2: of the securities this firm held, how many have a ticker carrying more than one asset name, and whether each is priced from its own rows

<to_id>ADVI_COTBKF.TO-CB-ca-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~152</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
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

### AMENDMENT 1 (issuer `2.0.0_SA_COO~C2`, 2026-10-12T01:54Z) -- a second item in this cell, on a CTO ruling

**Why.** `1.0.0_SA_CTO~DELL2` msg 6286, with PRD v0.9 SIGNED: "One read added, the reviewer's note and my own doubt. v0.9 says
`as_traded_close` means the traded price only after the split scaling, and that a point not yet scaled is not written with that
value. The build's own comment (commonwealth_daily_valuation.py:196) says the scaling 'then applies on top', after the
substitution that writes the value. So read, from code: where the basis value is written against where the split scaling runs, for
every security type, and whether a point can leave the build marked `as_traded_close` and unscaled. Until that is shown the
meaning holds for funds only, and I amend the sentence on your answer."

**The added item. A CODE READ of this project's own valuation build; it is done FIRST, because the CTO amends a signed sentence on
it. No data is needed to answer it; one check on the build's own output is allowed and named below.**

A1. **Where the basis value is written:** in `data/assets/scripts/silver/commonwealth_daily_valuation.py`, every line that assigns
    the per-point column `basis` (the constants `BASIS_AS_TRADED_CLOSE` and `BASIS_STORE_POINT`; the signed text cites `:186-199`,
    `:211`, `:246-258`): the function, the condition under which each value is written, and for which security types and series
    classes. Quote the lines.
A2. **Where the split scaling runs:** the function that applies the split store's factors (`load_store_splits` and whatever
    consumes it), the order of the calls in the build's main path (file and line of each call, in order), which points it scales
    (every point? only points with a given `basis`? only securities with a split in the store?), and what it does to the `basis`
    column of a point it scales or leaves alone.
A3. **The order, as a statement:** is the value `as_traded_close` written BEFORE the scaling runs; and after the scaling, does
    anything record that a given point HAS been scaled, or that it needed none?
A4. **Can a point leave the build marked `as_traded_close` and unscaled?** Enumerate the paths by which it could, each with file and
    line: a security with a split the split store does not hold; a split dated outside what the store covers; the pinned
    split-store instant (`--split-store-as-of`) leaving out a later-recorded split; a security type the scaling skips; a point
    after its last split (which needs no scaling: say that this is "unscaled and right"). For each path: reachable, not
    reachable, or `not_established`, with the reason from the code.
A5. **For every security type the build values** (the kinds the build's own code distinguishes): does the substitution that writes
    `as_traded_close` apply to it, and does the scaling apply to it? A small table from the code.
A6. **One check on the build's own output, allowed and local:** in the served build's price input or price table on disk
    (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/`), if a `basis` column or a price-basis file is present: the count of
    points by `basis`, and how many securities marked `as_traded_close` have a split in the pinned split store inside their held
    range. Counts only. If the column is not in the files on disk, say so and make no other read.
A7. Write a SECOND record, `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~152/BASIS_VALUE_AGAINST_SPLIT_SCALING.json`, beside the first. Top-level keys, exactly: `basis_written_at` (a list of `{"file_line",
    "value", "condition"}`), `split_scaling_at` (a list of `{"file_line", "what_it_scales"}`), `order` (`value_before_scaling`,
    `scaling_before_value` or `not_established`), `scaling_is_recorded_per_point` (true or false), `paths_marked_and_unscaled` (a
    list of `{"path", "file_line", "reachable"}`), `can_leave_marked_and_unscaled` (true, false or `not_established`),
    `by_security_type` (a list), `output_check`, `the_sentence_holds_for` (a short string: every type, funds only, or none, as the
    code shows), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB79ca2-AC1" cell_refs="CB-ca-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~152/TICKER_MANY_NAMES.json',encoding='utf-8'));c=d['classes'];n=d['not_own_rows'];print('TICKER-MANY-NAMES control=%d/%d test_written=%s held_securities=%d priced_by_ticker=%d ticker_many_names=%d classed=%d not_own_rows=%d measured_account_days=%d the_15_listed=%d classes=%s'%(d['control']['with_more_than_one_name'],d['control']['tickers'],bool(d['test']['written_at']),d['held_securities'],d['priced_from_the_store_by_ticker'],d['ticker_with_more_than_one_name'],sum(c.values()),n['securities'],n['measured_account_days'],len(d['the_15']),json.dumps(c,sort_keys=True)))"</invocation><expect>TICKER-MANY-NAMES control=308/4000 test_written=True</expect></criterion>
`CB79ca2-AC1` -- the store-wide control reproduces; the test was written first; every held security whose ticker carries more than
one name is classed (`classed` equals `ticker_many_names`); the issuer reads how many are not priced from their own rows.

<criterion id="CB79ca2-AC2" cell_refs="CB-ca-2" judgment="true"/>
`CB79ca2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the denominators run from every held security down;
the rule for a security's own name and for "its own rows" was written before any was classed; names that carry the same series
are said to be indistinguishable and not counted as wrong; a security whose own name cannot be identified is that class and not
`own_rows`; no account id or amount appears. AMENDMENT 1 adds to this judgment: the order of the basis value and the split scaling is
read from the calls in the build's main path, with file and line, not from a comment; "can a point leave marked and unscaled" is
answered path by path, with `not_established` where the code does not settle it; a point after its last split is said to be
unscaled and right.

<criterion id="CB79ca2-AC3" cell_refs="CB-ca-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~152/BASIS_VALUE_AGAINST_SPLIT_SCALING.json',encoding='utf-8'));p=d['paths_marked_and_unscaled'];print('BASIS-VS-SCALING basis_written_at=%d split_scaling_at=%d order=%s scaling_is_recorded_per_point=%s paths=%d reachable=%d not_established=%d can_leave_marked_and_unscaled=%s security_types=%d the_sentence_holds_for=%s'%(len(d['basis_written_at']),len(d['split_scaling_at']),d['order'],d['scaling_is_recorded_per_point'],len(p),sum(1 for x in p if x['reachable'] is True),sum(1 for x in p if x['reachable'] not in (True,False)),d['can_leave_marked_and_unscaled'],len(d['by_security_type']),str(d['the_sentence_holds_for'])[:60]))"</invocation><expect>BASIS-VS-SCALING basis_written_at=</expect></criterion>
`CB79ca2-AC3` (AMENDMENT 1) -- where the basis value is written and where the split scaling runs are read with file and line; the
order is stated; every path by which a point could leave marked and unscaled carries a reading. The issuer reads the answer the
CTO amends its sentence on.

<expected_criteria>CB79ca2-AC1,CB79ca2-AC2,CB79ca2-AC3</expected_criteria>

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
Criterion ids: CB79ca2-AC1, CB79ca2-AC2, CB79ca2-AC3 (AMENDMENT 1: validate with all three). Instance at
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
