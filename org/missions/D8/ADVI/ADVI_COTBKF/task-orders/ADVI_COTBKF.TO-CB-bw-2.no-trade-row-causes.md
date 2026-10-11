# TO ADVI_COTBKF.TO-CB-bw-2.no-trade-row-causes -- round 75 CB-bw-2: the 74 large changes with no trade row: each given a cause from a closed list written first, or left as none found

<to_id>ADVI_COTBKF.TO-CB-bw-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~133</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>75</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bw-2` (`decompositions/ADVI_COTBKF_DECOMP.round75.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT on copies. You change no code. Nothing is served or fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_75_20261011.md` section 2 item 2 and section 3 item 2; row ADVI_COTBKF-D2-S127 in the channel (of 96 changes over 10 basis
points, 22 fall on a day the account has a share-moving row in one of the five exposed funds; "74 have no such row and are not
explained"); the round-74 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.json`.

**The two builds of round 74 are your input, READ ONLY:** `C:/dev/wk-cotbkf-83/.scratch/w129/fwd3_baseline/` and `C:/dev/wk-cotbkf-83/.scratch/w129/fwd3_variant/` (each:
`daily_returns.parquet` with account, date, value, flow, return, blank_reason; `account_day_value.parquet`), and
`C:/dev/wk-cotbkf-83/.scratch/w129/baseline_out/` and `C:/dev/wk-cotbkf-83/.scratch/w129/variant_out/` (the valuation's own tables, the security-day prices among them). The baseline
equals the served table; the variant differs in the price of 19 validated funds alone (record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.json`). You modify nothing in that
folder and build nothing new: no S3 read, no fetch.

**Your item.**

1. **Reproduce the 74 first:** the 96 changes over 10 basis points; the 22 with a share-moving row that day in one of the five funds
   with measured exposure; the 74 without.
2. **THE CLOSED LIST FIRST.** Before any of the 74 is looked at, write to a file in your scratch (with a clock timestamp) and copy
   into the record the closed list of causes AND the test for each, in the order they are tried (a day takes the FIRST that fits):
   `reinvestment` (a reinvestment row within a stated number of days, in which fund); `transfer` (shares or cash moved in or out of
   the account that day, any security); `distribution_date` (a cash distribution of an exposed fund posted that day or the day
   before); `price_step` (the variant-over-baseline price ratio of a held exposed fund changes between the previous day and this day
   by more than a stated amount: the adjustment factor stepping); `trade_in_another_security` (a purchase or sale that day outside
   the exposed funds, which changes the weight of the fund in the account); `small_base` (the account's previous-day value under a
   stated share of its median, so a small price difference is a large return); `none_found`. You may add causes to the list ONLY
   before you start, with their tests. Then keep it.
3. **Each of the 74 given its cause,** counts per cause, with the sign and the median size of the change per cause. For `price_step`
   say how many are steps UP of the ratio and how many down, and whether the step date is a distribution date of the fund.
4. **The same list over the 22,** as a check on the list: a purchase day should not also read `price_step`; say how many of the 22
   would have taken each cause had the trade row been ignored.
5. **Does one cause carry most of it?** The share of the 74, and of their total absolute change, under each cause; and `none_found`
   stated plainly with its count, its largest change, and what was looked at.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~133/NO_TRADE_ROW_CAUSES.json` and a short `.md`. Top-level keys, exactly: `reproduced` (`{"over_10bp", "with_a_row", "without"}`),
   `closed_list` (`{"text", "written_at", "causes": [...]}`), `causes` (an object: cause to `{"days", "higher", "lower",
   "median_bp"}`), `none_found`, `price_step_detail`, `check_on_the_22`, `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB75bw2-AC1" cell_refs="CB-bw-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~133/NO_TRADE_ROW_CAUSES.json',encoding='utf-8'));r=d['reproduced'];c=d['causes'];print('NO-TRADE-ROW list_written=%s reproduced=%d/%d/%d causes_in_list=%d days_given=%d none_found=%d by_cause=%s'%(bool(d['closed_list']['written_at']),r['over_10bp'],r['with_a_row'],r['without'],len(d['closed_list']['causes']),sum(v['days'] for v in c.values()),c.get('none_found',{}).get('days',0),json.dumps({k:v['days'] for k,v in c.items()},sort_keys=True)))"</invocation><expect>NO-TRADE-ROW list_written=True</expect></criterion>
`CB75bw2-AC1` -- the closed list was written first; the 74 are reproduced; every one carries a cause from the list or `none_found`
(`days_given` equals the count without a row).

<criterion id="CB75bw2-AC2" cell_refs="CB-bw-2" judgment="true"/>
`CB75bw2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the list and its tests precede the look at the 74
and were not widened after; a day takes the first cause that fits and `none_found` is used where none does; the check over the 22
is reported as it came out; no account id or account value appears.

<expected_criteria>CB75bw2-AC1,CB75bw2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local: no S3 read, no network call, no new build.
- **Accounts.** Inside your own scratch you work with account ids as the tables hold them. NOTHING you commit, print in your report
  or write to the channel carries an account id, or an account's value, flow, quantity, balance or return. Where accounts must be
  told apart, label them `A1` to `A9` by a rule you state, and keep the mapping in your scratch only.
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
  `ADVI_COTBKF-D2-W133-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round75.md</decomp_doc> (round 75), cell `CB-bw-2`.
<owned_cells>CB-bw-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB75bw2-AC1, CB75bw2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~133/ADVI_COTBKF.TO-CB-bw-2.no-trade-row-causes.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB75bw2-AC1,CB75bw2-AC2` BEFORE the flip. Mechanical: CB75bw2-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the 96 / 22 / 74 as reproduced; the closed list and its tests as written before the look, with its timestamp; the 74 by cause with sign and median size; the price steps up and down and whether on a distribution date; `none_found` with its count, largest change and what was looked at; the check over the 22; the headline; the `NO-TRADE-ROW` line; the account-id scan's DENOMINATOR line; a statement that no account id or value left the scratch; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the closed list and each cause's test are written before any of the 74 is looked at, and the list is not widened after; a day takes the first cause that fits; none-found is a legal answer and is counted; the list is run over the 22 trade days as a check on itself; BLIND: a cause that leaves no row in the transactions or the price tables.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-75 analysis @cd481e59d2 (msg 5920), section 3 item 2; `3.0.0_SA_CVO` REMEDIATION_v45 @7dbb71c512.
