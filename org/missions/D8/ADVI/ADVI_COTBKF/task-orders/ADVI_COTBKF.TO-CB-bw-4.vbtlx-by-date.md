# TO ADVI_COTBKF.TO-CB-bw-4.vbtlx-by-date -- round 75 CB-bw-4: one fetched fund at a ratio of 0.18, read date by date until the cause has a name or is stated as not named

<to_id>ADVI_COTBKF.TO-CB-bw-4</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~135</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>75</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bw-4` (`decompositions/ADVI_COTBKF_DECOMP.round75.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ of one security, date by date. You change no code. Nothing is fetched: the round-74 fetch is read as it sits.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_75_20261011.md` section 2 item 6 and section 3 item 4 ("VBTLX at a ratio of 0.18 (row D2-S126) is not a dividend adjustment.
It is read date by date until the cause has a name: a share-class change, a wrong symbol behind the security, a unit. It is excluded
from every count until then."); row ADVI_COTBKF-D2-S126 in the channel; the round-74 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~130/FETCH_HELD_27.json` and its `.csv` (VBTLX: 1,482
shared dates, lowest ratio 0.1823, 7.83 percent of dates below 0.98; read `looks unadjusted` by a rule that needs half the dates
below 0.98).

**Your item.**

1. **The ratio, date by date:** the BUILD's close for the security (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/r34/after/security_day_price.parquet`, with its `store`
   column) over the fetched unadjusted close (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census_fetch_r74/`), on every shared date. The stretches where the ratio
   is off by more than 2 percent: first and last date of each, days, the ratio's level inside it (a constant? a ramp?), and the ratio
   on the days either side. Is the level a recognisable number (a tenth, a share-class price, another fund's price)?
2. **Which side is wrong on those dates,** from evidence that is neither: the custodian's own rows for this CUSIP
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/`): trade prices (amount over shares on purchases and sales) and any reinvestment price on or near the off
   dates, beside both closes. And the BUILD's close on those dates by `store`: does one store carry the off stretch?
3. **What is behind the security,** from the custodian rows: every distinct symbol and description the CUSIP carries and when; every
   distinct CUSIP that carries this ticker and when (a share-class conversion shows as two CUSIPs or two symbols with a hand-over
   date); the local price-store caches (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3/price_cache/`): rows for this CUSIP and for this ticker, by store and source,
   on the off dates: is a different key (a ticker more than one CUSIP claims) supplying the price?
4. **Name the cause, or do not.** One of: `share_class_change`, `wrong_symbol_behind_the_security`, `unit`, `other` (say what), or
   `not_named`, with the evidence for it and what would have to be read to settle it. A cause is named only if the custodian's own
   prices or the key evidence show it; a level that merely looks like one is `not_named`.
5. **What rests on the off dates:** priced holding account-days and MEASURED account-days
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet`, `daily_returns.parquet`) holding the security on those dates. Counts only.
   And whether the round-70 scan (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~113/CLOSE_VS_TRADE_SCAN_WIDE.json`
   and its detail file) already classed this series, and how.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~135/VBTLX_BY_DATE.json`, a `.csv` of the off stretches (columns: first_date, last_date, days, ratio_level, store,
   custodian_prices_in_stretch, nearer_to) and a short `.md`. Top-level keys, exactly: `shared_dates`, `off_dates`, `stretches` (a
   list), `which_side` (`build`, `fetched`, `both` or `not_established`), `behind_the_security` (`{"symbols", "cusips_for_the_ticker",
   "stores_on_off_dates"}`), `cause`, `cause_evidence`, `priced_holding_account_days_on_off_dates`,
   `measured_account_days_on_off_dates`, `round_70_class`, `excluded_from_counts` (true), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB75bw4-AC1" cell_refs="CB-bw-4"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~135/VBTLX_BY_DATE.json',encoding='utf-8'));print('VBTLX-BY-DATE shared_dates=%d off_dates=%d stretches=%d which_side=%s cause=%s priced_on_off=%d measured_on_off=%d round_70_class=%s excluded_from_counts=%s'%(d['shared_dates'],d['off_dates'],len(d['stretches']),d['which_side'],d['cause'],d['priced_holding_account_days_on_off_dates'],d['measured_account_days_on_off_dates'],d['round_70_class'],d['excluded_from_counts']))"</invocation><expect>VBTLX-BY-DATE shared_dates=1482</expect></criterion>
`CB75bw4-AC1` -- the security is read on its 1,482 shared dates, its off stretches are listed, and a cause is named or stated as
not named. The issuer reads the cause and what rests on the off dates.

<criterion id="CB75bw4-AC2" cell_refs="CB-bw-4" judgment="true"/>
`CB75bw4-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: which side is wrong rests on the custodian's own
prices or on the key evidence, not on the look of a ratio; a cause is named only where that evidence shows it, and `not_named` is
used otherwise with what would settle it; nothing was fetched; no account id or account value appears.

<expected_criteria>CB75bw4-AC1,CB75bw4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local; no network call and no new fetch.
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
  `ADVI_COTBKF-D2-W135-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round75.md</decomp_doc> (round 75), cell `CB-bw-4`.
<owned_cells>CB-bw-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB75bw4-AC1, CB75bw4-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~135/ADVI_COTBKF.TO-CB-bw-4.vbtlx-by-date.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB75bw4-AC1,CB75bw4-AC2` BEFORE the flip. Mechanical: CB75bw4-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the shared dates and the off stretches with their levels; which side is wrong and on what evidence; the symbols and CUSIPs behind the security and the stores on the off dates; the cause, or `not_named` with what would settle it; what rests on the off dates; the round-70 class; the headline; the `VBTLX-BY-DATE` line; the account-id scan's DENOMINATOR line; a statement that nothing was fetched; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- which side is wrong is decided by the custodian's own trade prices or by key evidence, never by the look of a ratio; not-named is a legal cause and says what would settle it; the security stays excluded from every count; BLIND: a stretch on which the account made no trade, where the custodian gives no price.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-75 analysis @cd481e59d2 (msg 5920), section 3 item 4; `3.0.0_SA_CVO` REMEDIATION_v45 @7dbb71c512.
