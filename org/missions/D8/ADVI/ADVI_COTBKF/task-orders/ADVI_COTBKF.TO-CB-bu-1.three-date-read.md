# TO ADVI_COTBKF.TO-CB-bu-1.three-date-read -- round 73 CB-bu-1: every fund with a reinvestment row and a cached unadjusted close: the row's price beside the close on three dates, rule first; the defect sized on them

<to_id>ADVI_COTBKF.TO-CB-bu-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~123</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>73</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bu-1` (`decompositions/ADVI_COTBKF_DECOMP.round73.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT. You change no code. Nothing is fetched: the vendor cache is read as it sits on disk.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_73_20261011.md` sections 1, 2 (items 1, 2 and 4) and 3 item 1; row ADVI_COTBKF-D2-W120-S1 in the channel; the round-72 records
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~120/UNADJUSTED_SOURCE_READ.json` (for nine funds the cached unadjusted close equals the custodian's reinvestment price on 45 of 93 dates on the row's own
date, on 88 of 93 one trading day earlier, on 32 one day later; that previous-day reading "was not the stated comparison") and
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~119/REINVESTMENT_PRICE_CHECK.json` (the build's close beside the custodian's price: 19 confirmed adjusted, 15 confirmed not, 236 nothing to test on, because
the build's table holds a close on few reinvestment dates).

**The ruling you serve.** "The date convention is decided on evidence, not adopted from one fit on nine funds: one cell reads, for every
fund with a reinvestment row AND a cached unadjusted close (the 76 the packet counts, plus the nine), the row's price beside the close
on the row's own date, the trading day before and the day after. The rule is written to a file before the run: which of the three
wins, per fund and over all. The same pass sizes the defect on those 76 against a custodian price, which no read has done."

**Your item.**

1. **The population, printed with its denominator:** every fund series in the build's table (270) that has BOTH at least one
   reinvestment row (`dvr`, shares at least 0.05) in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/` AND an unadjusted `Close` in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/`. Say how
   many of the 197 left on the store, how many of the 73 substituted, and how many of the nine are in it, and how many funds have one
   and not the other.
2. **THE RULE FIRST.** Before any comparison over the population, write to a file in your scratch (with a clock timestamp) and copy
   into the record: (a) what "equal" means (within 0.5 percent); (b) how a fund's winning date is decided among `same`, `before`,
   `after` (a minimum count of dates; the margin by which one must beat the others; else `undecided`); (c) how the overall convention
   is decided from the funds (and what share of funds may disagree before it is `no single convention`); (d) for the sizing in step 4,
   what makes the cached close a VALIDATED yardstick for a fund (how many custodian dates it must match on the winning date) and what
   reads `adjusted`, `not adjusted`, `undecided`. Then keep it. If the result under the rule looks wrong to you, report the result
   under the rule and say separately what another rule would give.
3. **The three-date read:** per (fund, reinvestment date): the custodian's price (amount over shares, pooled) beside the cached
   unadjusted close on the row's own date, the previous trading day and the next trading day (trading days from the fund's own cache
   rows). Per fund: dates compared and dates equal under each; its winner. Over all: the counts, the funds by winner, and the
   convention under your rule. Report the nine separately from the rest, so the reader sees whether the rest behave as the nine did.
4. **The sizing against a custodian price.** For each fund whose cached close is VALIDATED by step 3 under your rule: set the BUILD's
   close (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet`) beside the cached unadjusted close over every date they share (aligned by
   the same date: both are closes of the fund). A fund whose build close sits below the cached close by a ratio that rises toward the
   present reads `adjusted`; one that sits at 1 reads `not adjusted`. Counts: validated funds, adjusted, not adjusted, undecided; and
   the funds NOT validated (too few custodian dates, or the cache does not match the custodian on any of the three dates), which stay
   unsized. Beside round 72's 19 / 15 / 236 and round 71's 72, by series: every series whose reading differs is listed by ticker.
5. **The reach on the `adjusted` set:** priced holding account-days and MEASURED account-days
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet`, `daily_returns.parquet`) on dates where the ratio is below 0.98, with the
   bands (below 0.9, 0.75, 0.5). Counts only. State it as a FLOOR AND WHAT IS UNSIZED: the funds with no cached close (121) and the
   funds not validated are not in it.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~123/THREE_DATE_READ.json`, a `.csv` of every fund in the population (columns: cusip, ticker, in_group, reinvestment_dates,
   equal_same, equal_before, equal_after, winner, validated, sizing_reading, min_ratio, measured_account_days; CUSIPs only in the column
   named exactly `cusip`) and a short `.md`. Top-level keys, exactly: `population` (`{"funds", "of_the_197", "of_the_73", "of_the_nine",
   "reinvestment_only", "cache_only"}`), `rule` (`{"text", "written_at"}`), `three_date` (`{"cells", "equal_same", "equal_before",
   "equal_after", "funds_by_winner", "convention", "the_nine", "the_rest"}`), `sizing` (`{"validated", "adjusted", "not_adjusted",
   "undecided", "not_validated"}`), `against_earlier` (`{"differs": [...]}`), `reach` (`{"priced_holding_account_days",
   "measured_account_days", "ratio_bands"}`), `unsized` (`{"no_cached_close", "not_validated"}`), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB73bu1-AC1" cell_refs="CB-bu-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~123/THREE_DATE_READ.json',encoding='utf-8'));p=d['population'];t=d['three_date'];s=d['sizing'];print('THREE-DATE-READ rule_written=%s funds=%d of_the_197=%d of_the_nine=%d cells=%d equal_same=%d equal_before=%d equal_after=%d convention=%s validated=%d adjusted=%d not_adjusted=%d undecided=%d not_validated=%d sizing_sum=%d measured_account_days=%d differs=%d'%(bool(d['rule']['written_at']),p['funds'],p['of_the_197'],p['of_the_nine'],t['cells'],t['equal_same'],t['equal_before'],t['equal_after'],t['convention'],s['validated'],s['adjusted'],s['not_adjusted'],s['undecided'],s['not_validated'],s['adjusted']+s['not_adjusted']+s['undecided']+s['not_validated'],d['reach']['measured_account_days'],len(d['against_earlier']['differs'])))"</invocation><expect>THREE-DATE-READ rule_written=True</expect></criterion>
`CB73bu1-AC1` -- the rule was written first; every fund of the population is read on three dates and carries one sizing reading
(`sizing_sum` equals `funds`); the issuer reads the convention and the counts.

<criterion id="CB73bu1-AC2" cell_refs="CB-bu-1" judgment="true"/>
`CB73bu1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the rule precedes the run and was kept; the convention
rests on the funds beyond the nine and is `no single convention` if they disagree; a cached close sizes a fund only where the
custodian's price validates it; the reach is stated as a floor with what is unsized beside it; nothing was fetched.

<expected_criteria>CB73bu1-AC1,CB73bu1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local; no network call; you do NOT run the price-basis
  census script (it fetches).
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
  `ADVI_COTBKF-D2-W123-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round73.md</decomp_doc> (round 73), cell `CB-bu-1`.
<owned_cells>CB-bu-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB73bu1-AC1, CB73bu1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~123/ADVI_COTBKF.TO-CB-bu-1.three-date-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB73bu1-AC1,CB73bu1-AC2` BEFORE the flip. Mechanical: CB73bu1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the population with its denominators; the rule as written before the run, with its timestamp; the three-date counts over all, the funds by winner, the convention, the nine beside the rest; the sizing counts and every series whose reading differs from rounds 71 and 72, by ticker; the reach as a floor and what is unsized; the headline; the `THREE-DATE-READ` line; the account-id scan's DENOMINATOR line; a statement that nothing was fetched; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the rule is written to a file before the run and kept; the nine are reported apart from the rest so one fit on nine cannot carry the convention; `no single convention` and `undecided` are legal answers; a cached close sizes a fund only where the custodian's price validates it; the reach is a floor with the unsized funds counted beside it; BLIND: a fund with no reinvestment row or no cached close is outside this instrument.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-73 analysis @35cf1a97dd (msg 5633), section 3 item 1; `3.0.0_SA_CVO` REMEDIATION_v43 @bf44c1d294.
