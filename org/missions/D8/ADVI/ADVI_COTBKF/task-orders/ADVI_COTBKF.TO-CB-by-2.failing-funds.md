# TO ADVI_COTBKF.TO-CB-by-2.failing-funds -- round 77 CB-by-2: the 15 failing funds listed: trades read, median ratio, whether an unadjusted close is already held and whether it reproduces the price paid

<to_id>ADVI_COTBKF.TO-CB-by-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~144</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>77</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-by-2` (`decompositions/ADVI_COTBKF_DECOMP.round77.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a LISTING from records and local files. You change no code. Nothing is fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_77_20261011.md` section 3 item 2 ("The 15 failing funds listed with, for each, its trade count read, its median ratio, and
whether an unadjusted close is already held (the 27 fetched in round 74, the cache)."); the round-76 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~140/FUNDS_BY_TRADES.json`, its `.csv`
and `.md` (the 15, key `named`); the round-74 fetch record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~130/FETCH_HELD_27.json` and its `.csv` (27 asked, 25 returned, into
`C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census_fetch_r74/`); the cache `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/` (per ticker: Close, Adj Close).

**Your item.**

1. **Reproduce the 15** from the round-76 record, by ticker, with the trade units read, the failing units and the median ratio as
   that record holds them (printed from it, not recomputed).
2. **For each: is an unadjusted close already held, and where:** in the cache; in the round-74 fetch folder; in neither. For a
   fund with one: the first and last date it covers; whether `Close` and `Adj Close` differ anywhere (a series that never differs
   cannot be told from an adjusted one); the share of the fund's HELD days in the build
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet`) that the unadjusted series covers; and the earliest held day it does NOT cover.
3. **For each fund with an unadjusted close held: does that close reproduce the price paid?** The same instrument as round 76, with
   the unadjusted close in place of the served one: over the fund's trade units, the share within 1 percent. So the reader sees,
   fund by fund, whether a held series would pass where the served close fails. A fund with no unadjusted close held is
   `none_held`; a held series that also fails is listed as that, by ticker.
4. **And whether it is validated by the custodian's reinvestment price** (the round-74 record
   `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~128/VALIDATED_UNADJUSTED.csv`: `validated` or `unreadable`).
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~144/FAILING_FUNDS.json`, a `.csv` (columns: cusip, ticker, trade_units, failing_units, median_ratio, unadjusted_close_held,
   where_held, covers_from, covers_to, share_of_held_days_covered, held_series_within_1pct, validated_by_reinvestment; CUSIPs only
   in the column named exactly `cusip`) and a short `.md`. Top-level keys, exactly: `funds` (15), `held_in_cache`,
   `held_in_fetch_folder`, `none_held`, `held_series_passes`, `held_series_fails`, `held_series_too_few_trades`, `by_fund` (a list
   of 15), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB77by2-AC1" cell_refs="CB-by-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~144/FAILING_FUNDS.json',encoding='utf-8'));print('FAILING-FUNDS funds=%d listed=%d held_in_cache=%d held_in_fetch_folder=%d none_held=%d held_sum=%d held_series_passes=%d held_series_fails=%d held_series_too_few_trades=%d'%(d['funds'],len(d['by_fund']),d['held_in_cache'],d['held_in_fetch_folder'],d['none_held'],d['held_in_cache']+d['held_in_fetch_folder']+d['none_held'],d['held_series_passes'],d['held_series_fails'],d['held_series_too_few_trades']))"</invocation><expect>FAILING-FUNDS funds=15 listed=15</expect></criterion>
`CB77by2-AC1` -- the 15 are listed; each is held in the cache, in the fetch folder or in neither (`held_sum` equals 15); each held
series is read against the price paid.

<expected_criteria>CB77by2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local: no S3 read, no network call.
- No account id or amount is written. Counts, ratios, tickers and dates only.
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
  `ADVI_COTBKF-D2-W144-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round77.md</decomp_doc> (round 77), cell `CB-by-2`.
<owned_cells>CB-by-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB77by2-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~144/ADVI_COTBKF.TO-CB-by-2.failing-funds.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB77by2-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the 15 as reproduced from the round-76 record; for each, where an unadjusted close is held, what it covers and whether the two columns ever differ; for each held series, the share of trade units within 1 percent of the price paid; any held series that also fails, by ticker; the validated flag; the headline; the `FAILING-FUNDS` line; the account-id scan's DENOMINATOR line; a statement that nothing was fetched; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a listing from records and local files.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the 15 are printed from the round-76 record, not recomputed; a held series is read against the price paid, so held is not taken to mean right; a series whose two columns never differ is said to be indistinguishable; nothing is fetched for a fund with none held; BLIND: a held day the series does not cover.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-77 analysis @1101e06fcd (msg 6154), section 3 item 2; `3.0.0_SA_CVO` round-76 grade file @d299fd357a.
