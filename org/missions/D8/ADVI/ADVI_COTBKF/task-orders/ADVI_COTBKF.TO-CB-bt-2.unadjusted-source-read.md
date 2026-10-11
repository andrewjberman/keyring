# TO ADVI_COTBKF.TO-CB-bt-2.unadjusted-source-read -- round 72 CB-bt-2: for the nine funds: does a source already on disk return the unadjusted value the custodian reinvested at

<to_id>ADVI_COTBKF.TO-CB-bt-2</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~120</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>72</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bt-2` (`decompositions/ADVI_COTBKF_DECOMP.round72.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a READ, not a fetch order. You pull nothing from any vendor. You change no code.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_72_20261011.md` section 2 item 1 (the ruling: "The basis for a fund series is the unadjusted value the fund traded at on the
day") and section 4 item 2; the round-71 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~116/DIVIDEND_ADJUSTED_SERIES.json` and its `_DETAIL.json` (the nine funds AMCPX, AMRMX, CWGIX, WGIFX, CPXIX,
FINFX, NEWFX, AWSHX, WMFFX; the basis census classed each `other: matches_neither`; the Yahoo cache holds Close and Adj Close);
`data/assets/scripts/silver/commonwealth_daily_valuation.py` (`as_traded_store`, `read_yahoo_close`) and
`data/assets/scripts/silver/commonwealth_price_basis_census.py` (how it classes a ticker and why a ticker lands in `other`);
`data/assets/scripts/analysis/commonwealth_price_census.py` lines 50 to 80 (the six stores the build reads).

**The question.** For the nine funds, does a source THE ESTATE ALREADY RUNS return an unadjusted value that equals the custodian's
reinvestment price on the reinvestment's own date? If yes, a corrected series is a read of data already held. If no, it is a new
source, which is a different decision and not this cell's.

**Your item.**

1. **The yardstick:** for each of the nine, the custodian's reinvestment price per date (type `dvr` rows in `C:/dev/ajb_workspace/.scratch/advi_cotbkf/tx_cache/`:
   amount over shares, shares at least 0.05, pooled across accounts; a fund's price is not client data). Expect about 92 dates over
   the nine.
2. **Each candidate source, on disk, compared on those dates** (equal means within 0.5 percent; report also within 2 percent, the
   median ratio and the worst):
   (a) the Yahoo cache's unadjusted `Close` (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/yahoo_census/`);
   (b) the Yahoo cache's `Adj Close`;
   (c) each of the six price-store caches (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3/price_cache/`), by its own `source` label where it has one;
   (d) the build's present close for the fund (the thing being corrected), as the baseline.
   For each fund and source: dates compared, dates equal, and the date range the source covers for that fund.
3. **Why the build did not use it.** If (a) reproduces the reinvestment price, say exactly why the as-traded basis left these funds on
   the store: read the census's rule and print, for each of the nine, the two fit numbers the census computed (against Close and
   against Adj Close) and the threshold it missed. One paragraph: what rule change would have substituted them, and how many OTHER
   tickers the same change would also substitute (count from the census file; do not make the change).
4. **Coverage beyond the nine, counts only:** of the fund series round 71 left on the store (197), how many have an unadjusted `Close`
   in the Yahoo cache at all, and for how many of their held dates. So the CTO can see whether a read of held data covers the defect or
   only the nine.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~120/UNADJUSTED_SOURCE_READ.json` and a short `.md`. Top-level keys, exactly: `yardstick` (`{"funds", "dates"}`), `sources` (a list of
   `{"source", "funds_covered", "dates_compared", "dates_equal_half_percent", "dates_within_two_percent", "median_ratio",
   "worst_ratio"}`), `per_fund` (a list), `reproduces` (the name of the source that reproduces the reinvestment price on the nine, or
   `NONE`), `why_not_used` (the census numbers per fund and the paragraph), `others_the_same_change_would_move`, `coverage_of_the_197`
   (`{"with_unadjusted_close", "without"}`), `not_established`.

### ACCEPTANCE

<criterion id="CB72bt2-AC1" cell_refs="CB-bt-2"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~120/UNADJUSTED_SOURCE_READ.json',encoding='utf-8'));s=d['sources'];c=d['coverage_of_the_197'];print('UNADJUSTED-SOURCE-READ funds=%d dates=%d sources=%d reproduces=%s best=%s coverage_with=%d coverage_without=%d'%(d['yardstick']['funds'],d['yardstick']['dates'],len(s),d['reproduces'],max(s,key=lambda x:x['dates_equal_half_percent'])['source'],c['with_unadjusted_close'],c['without']))"</invocation><expect>UNADJUSTED-SOURCE-READ funds=9</expect></criterion>
`CB72bt2-AC1` -- every candidate source on disk is compared with the custodian's reinvestment price on the nine, the one that
reproduces it is named or `NONE`, and the coverage beyond the nine is counted.

<criterion id="CB72bt2-AC2" cell_refs="CB-bt-2" judgment="true"/>
`CB72bt2-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: nothing was fetched; the yardstick is the custodian's
own rows; "reproduces" rests on the counts shown; the reason the build did not use the source is read from the census's own numbers;
no rule is changed.

<expected_criteria>CB72bt2-AC1,CB72bt2-AC2</expected_criteria>

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
  `ADVI_COTBKF-D2-W120-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round72.md</decomp_doc> (round 72), cell `CB-bt-2`.
<owned_cells>CB-bt-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB72bt2-AC1, CB72bt2-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~120/ADVI_COTBKF.TO-CB-bt-2.unadjusted-source-read.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB72bt2-AC1,CB72bt2-AC2` BEFORE the flip. Mechanical: CB72bt2-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the yardstick (funds, dates); each candidate source with its coverage and its counts; the source that reproduces the custodian's price, or NONE; per fund, the census's two fit numbers and the threshold missed; how many other tickers the same rule change would move; the coverage of the 197; the `UNADJUSTED-SOURCE-READ` line; a statement that nothing was fetched; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read of files on disk.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the yardstick is the custodian's own reinvestment price, not a vendor series; every source on disk is compared, including the adjusted one and the build's present close as baselines; NONE is a legal answer; the census rule is read, not changed, and the reach of a change is counted; BLIND: a source the estate runs that keeps no copy on this box is not read.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-72 analysis @19911afdeb (msg 5561), section 4 item 2; `3.0.0_SA_CVO` REMEDIATION_v42 @fd300b1f97.
