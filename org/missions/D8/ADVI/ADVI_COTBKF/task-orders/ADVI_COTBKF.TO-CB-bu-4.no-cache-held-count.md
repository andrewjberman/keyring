# TO ADVI_COTBKF.TO-CB-bu-4.no-cache-held-count -- round 73 CB-bu-4: counts only: of the 121 fund series with no cached unadjusted close, how many are held on a served account-day

<to_id>ADVI_COTBKF.TO-CB-bu-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~126</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>73</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bu-4` (`decompositions/ADVI_COTBKF_DECOMP.round73.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a COUNT. You change no code. NO FETCH IS MADE: you ask no vendor and no gateway for anything.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_73_20261011.md` section 3 item 4 ("Counts only: of the 121 fund series with no cached unadjusted close, how many are held on
any served account-day. That number is what a fetch would be for; no fetch is made in this round."); the round-72 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~120/UNADJUSTED_SOURCE_READ.json`,
key `coverage_of_the_197` (76 with an unadjusted close in the cache, 121 without: 120 with no cache file and 1 with a marker and no
bars) and its `.md` for how the 197 were built (fund kinds in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet` whose close the
as-traded basis did not change against `.../r34/before/`).

**Your item.**

1. Rebuild the 197 and the 121 and print both with their denominators (270 fund series; 73 substituted; 197 left; 76 with; 121
   without). If you do not get 121, that is the refusal clause: say what you get and why.
2. For the 121: how many are HELD on any served account-day, that is, have at least one row with a value in
   `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet`; how many are not. For the held ones: priced holding account-days, distinct
   accounts as a COUNT, the first and last held date, and MEASURED account-days (an account-day with a return in
   `C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/daily_returns.parquet` on which the account holds the fund). Counts only.
3. Split the held ones by what is known of them: which price store their close comes from (the `store` column), whether they have any
   reinvestment row, and their round-72 reading (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~119/REINVESTMENT_PRICE_CHECK.csv`).
   And how many of the 121 have a ticker at all (a fetch needs one).
4. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~126/NO_CACHE_HELD_COUNT.json`, a `.csv` of the 121 (columns: cusip, ticker, held, priced_holding_account_days, measured_account_days,
   store, reinvestment_rows, round_72_reading; CUSIPs only in the column named exactly `cusip`) and a short `.md`. Top-level keys,
   exactly: `fund_series` (270), `left_on_store` (197), `no_cached_close` (121), `held` , `not_held`, `with_a_ticker`,
   `priced_holding_account_days`, `measured_account_days`, `by_store`, `by_round_72_reading`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB73bu4-AC1" cell_refs="CB-bu-4"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~126/NO_CACHE_HELD_COUNT.json',encoding='utf-8'));print('NO-CACHE-HELD-COUNT no_cached_close=%d held=%d not_held=%d sum=%d with_a_ticker=%d priced_holding_account_days=%d measured_account_days=%d left_on_store=%d fund_series=%d'%(d['no_cached_close'],d['held'],d['not_held'],d['held']+d['not_held'],d['with_a_ticker'],d['priced_holding_account_days'],d['measured_account_days'],d['left_on_store'],d['fund_series']))"</invocation><expect>NO-CACHE-HELD-COUNT no_cached_close=121</expect></criterion>
`CB73bu4-AC1` -- the 121 are rebuilt, every one is held or not held (`sum` equals 121), and the held ones are counted in priced and
measured account-days.

<expected_criteria>CB73bu4-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local; no network call of any kind.
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
  `ADVI_COTBKF-D2-W126-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round73.md</decomp_doc> (round 73), cell `CB-bu-4`.
<owned_cells>CB-bu-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB73bu4-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~126/ADVI_COTBKF.TO-CB-bu-4.no-cache-held-count.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB73bu4-AC1` BEFORE the flip. Mechanical. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the 270 / 73 / 197 / 76 / 121 as rebuilt; held and not held; the held ones in priced and measured account-days, by store and by round-72 reading; how many have a ticker; the headline; the `NO-CACHE-HELD-COUNT` line; a statement that nothing was fetched; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a count over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the 121 must be rebuilt to round 72's number before anything is counted; held and not held must sum to 121; no fetch is made and the cell says so; BLIND: a holding outside the served account-day table.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-73 analysis @35cf1a97dd (msg 5633), section 3 item 4; `3.0.0_SA_CVO` REMEDIATION_v43 @bf44c1d294.
