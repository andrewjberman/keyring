# TO ADVI_COTBKF.TO-CB-bt-1.reinvestment-price-check -- round 72 CB-bt-1: every fund series: the build's close beside the custodian's reinvestment price; three counts; the reach re-derived

<to_id>ADVI_COTBKF.TO-CB-bt-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~119</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>72</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bt-1` (`decompositions/ADVI_COTBKF_DECOMP.round72.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT. You change no code. No vendor data is used at all: that is the point of the instrument.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_72_20261011.md` sections 1, 2 (items 1, 2 and 4) and 4 item 1; the reviewer's grade it rests on (the file
`org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/remediations/REMEDIATION_v42.md` names it: read the passage on the nine funds, 87
of 92 dates, lowest ratio 0.47, and reproduce that instrument exactly before you widen it); the round-71 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~116/DIVIDEND_ADJUSTED_SERIES.json`, its
`.md` and `_DETAIL.json` (the vendor-against-itself test this replaces: 270 fund series; 73 substituted; 197 left on the store; 73 of
those tested, 72 reading adjusted; 124 untested; reach 3,187 measured account-days), and row ADVI_COTBKF-D2-W116-S1.

**The instrument (the reviewer's).** A reinvested distribution row in the custodian's own transactions carries an amount and the
shares it bought, so amount over shares is the price the fund traded at on that date, in the custodian's hand. Set the BUILD's close
for that fund on that date beside it. A fund's close equal to its reinvestment price is as-traded; a close below it by a factor that
shrinks toward the present is a dividend-adjusted series.

**Your item.**

1. **Reproduce the reviewer's nine first:** 92 reinvestment dates, the build's close below the reinvestment price on 87, in 9 of 9
   funds, the lowest ratio 0.47. If you cannot, that is the refusal clause: say what you get and why it differs.
2. **Every fund series.** For EVERY fund security in the build's price table (Mutual Fund and Mutual Fund (Closed End); the table is
   `C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet`): its reinvestment rows in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/` (type `dvr`, and any other type you
   can show is a reinvestment at the day's price; shares at least 0.05, because quantities are rounded to three decimals), pooled
   across accounts to one price per (fund, date) with the spread across accounts reported; the build's close on that date (same date
   only; say separately how many more pair within one trading day); the ratio close over reinvestment price.
3. **Three counts, as the CTO words them, over all fund series:** `confirmed_adjusted`, `confirmed_not`, `nothing_to_test_on` (no
   reinvestment row on a date the table has a close). State your rule for "confirmed" BEFORE you run it over the table and keep it:
   the count of dates, the share of them below 1 by more than 2 percent, and the trend (the ratio rises toward the present). A fund
   with too few dates to say is `nothing_to_test_on`, with the count of dates it has, never `confirmed_not`.
4. **Against round 71, series by series:** the 72 that read adjusted there, the 1 that did not, the 124 untested and the 73
   substituted: where does each land under this instrument. Every disagreement listed by ticker with both readings.
5. **ETF and Equity** separately, same three counts (they pay distributions and are reinvested too).
6. **The reach re-derived** on the `confirmed_adjusted` set: priced holding account-days, and MEASURED account-days
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet`, `daily_returns.parquet`) that rest on a close dated before the fund's last
   reinvestment date at which the ratio is still below 0.98. Beside round 71's 287,912 and 3,187. And how wrong: the distribution of
   the ratio over those account-days (share below 0.9, below 0.75, below 0.5), counts only.
7. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~119/REINVESTMENT_PRICE_CHECK.json`, a `.csv` of every fund series with its three-way reading (columns: cusip, ticker, kind, substituted,
   reinvestment_dates, dates_below_0_98, min_ratio, median_ratio, reading, round_71_reading, measured_account_days; CUSIPs only in the
   column named exactly `cusip`) and a short `.md`. Top-level keys, exactly: `reproduced_nine` (`{"funds", "dates", "dates_below",
   "min_ratio"}`), `rule` (the confirmed rule, as stated before the run), `fund_series`, `confirmed_adjusted`, `confirmed_not`,
   `nothing_to_test_on`, `against_round_71` (a table of counts and a list of disagreements), `other_kinds`, `reach`
   (`{"priced_holding_account_days", "measured_account_days", "ratio_bands"}`), `headline` (one sentence with all three counts),
   `not_established`.

### ACCEPTANCE

<criterion id="CB72bt1-AC1" cell_refs="CB-bt-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~119/REINVESTMENT_PRICE_CHECK.json',encoding='utf-8'));n=d['reproduced_nine'];print('REINVESTMENT-PRICE-CHECK nine_funds=%d nine_dates=%d nine_below=%d fund_series=%d confirmed_adjusted=%d confirmed_not=%d nothing_to_test_on=%d three_sum=%d disagreements_with_round_71=%d measured_account_days=%d'%(n['funds'],n['dates'],n['dates_below'],d['fund_series'],d['confirmed_adjusted'],d['confirmed_not'],d['nothing_to_test_on'],d['confirmed_adjusted']+d['confirmed_not']+d['nothing_to_test_on'],len(d['against_round_71']['disagreements']),d['reach']['measured_account_days']))"</invocation><expect>REINVESTMENT-PRICE-CHECK nine_funds=9</expect></criterion>
`CB72bt1-AC1` -- the reviewer's nine are reproduced and every fund series carries one of three readings (`three_sum` equals
`fund_series`), with the reach re-derived.

<criterion id="CB72bt1-AC2" cell_refs="CB-bt-1" judgment="true"/>
`CB72bt1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: no vendor series enters the reading; the rule for
"confirmed" was stated before the run and kept; too few dates reads `nothing_to_test_on`, never `confirmed_not`; every disagreement
with round 71 is listed; the reach is counted on the confirmed set only.

<expected_criteria>CB72bt1-AC1,CB72bt1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local; no network call.
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
  `ADVI_COTBKF-D2-W119-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round72.md</decomp_doc> (round 72), cell `CB-bt-1`.
<owned_cells>CB-bt-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB72bt1-AC1, CB72bt1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~119/ADVI_COTBKF.TO-CB-bt-1.reinvestment-price-check.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB72bt1-AC1,CB72bt1-AC2` BEFORE the flip. Mechanical: CB72bt1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the reproduced nine (funds, dates, dates below, lowest ratio); the rule for "confirmed", as stated before the run; the three counts over all fund series; each round-71 group's fate and every disagreement by ticker; ETF and Equity separately; the reach beside round 71's and the ratio bands; the headline; the `REINVESTMENT-PRICE-CHECK` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- the reviewer's own result on the nine is the positive control and must be reproduced first; no vendor series enters the reading; the rule is fixed before the run; too few dates is nothing-to-test-on, never confirmed-not; every disagreement with the vendor-based round-71 reading is listed; BLIND: a fund no account ever reinvested in has no yardstick under this instrument.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-72 analysis @19911afdeb (msg 5561), section 4 item 1; `3.0.0_SA_CVO` REMEDIATION_v42 @fd300b1f97.
