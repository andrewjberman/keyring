# TO ADVI_COTBKF.TO-CB-bw-1.purchase-day -- round 75 CB-bw-1: the purchase-day reading, rule first: on every changed account-day with a trade row in a validated fund, the return recomputed with the day's flow and the day's unadjusted close

<to_id>ADVI_COTBKF.TO-CB-bw-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~132</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>75</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bw-1` (`decompositions/ADVI_COTBKF_DECOMP.round75.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT on copies. You change no code. Nothing is served or fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_75_20261011.md` sections 1, 2 (items 2 and 3), 3 item 1 and 4; row ADVI_COTBKF-D2-S127 in the channel (the reviewer's: 1,577
changed at a floor of 1e-12, the worker's 1,575 at 1e-9; of 96 changes over 10 basis points, 22 fall on a day the account has a
share-moving row in one of the five exposed funds: 12 purchases all higher, 2 sales both lower, 8 reinvestments 7 lower; 74 have no
such row; "No return was recomputed by this seat"); the round-74 record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.json`; how the build computes a day's return and its
flow: `data/assets/scripts/silver/commonwealth_flows.py`, `commonwealth_sweeps.py` and the return step of
`commonwealth_fwd3_serve.py` (READ ONLY: the formula, what counts as an external flow, and how a purchase inside the account is
treated: it is NOT an external flow, so a purchase moves cash to shares and the day's value is shares times the day's close).

**The two builds of round 74 are your input, READ ONLY:** `C:/dev/wk-cotbkf-83/.scratch/w129/fwd3_baseline/` and `C:/dev/wk-cotbkf-83/.scratch/w129/fwd3_variant/` (each:
`daily_returns.parquet` with account, date, value, flow, return, blank_reason; `account_day_value.parquet`), and
`C:/dev/wk-cotbkf-83/.scratch/w129/baseline_out/` and `C:/dev/wk-cotbkf-83/.scratch/w129/variant_out/` (the valuation's own tables, the security-day prices among them). The baseline
equals the served table; the variant differs in the price of 19 validated funds alone (record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~129/RETURN_CHANGE.json`). You modify nothing in that
folder and build nothing new: no S3 read, no fetch.

**The reading to test.** "on the day shares are bought, the build values the new shares at a close that is too low against the cash
that paid for them, and the difference lands in that day's return. That is a different mechanism from a holding carried at an
adjusted close, and a larger one. It is a lead on 14 of 14 trade days and it is treated as a lead."

**Your item.**

1. **The set, with its denominators.** The changed account-days at both floors (1,575 and 1,577), and of them every account-day on
   which the account has a share-moving row (a purchase, a sale, a reinvestment, a transfer of shares in or out: name the custodian
   types you count under each) in one of the VALIDATED funds whose price moved. Reproduce the reviewer's 22 of 96 (12 / 2 / 8) first.
2. **THE RULE FIRST.** Before any recomputation, write to a file in your scratch (with a clock timestamp) and copy into the record:
   (a) the return formula as the build has it, in symbols; (b) the PREDICTION of the purchase-day reading: for a purchase of q shares
   paid with cash c, valued at the baseline close p0 and the variant close p1, the change in the day's return the mechanism predicts
   (state it from the formula, including the previous day's holding of the same fund, which moves with the price too); (c) a trade
   day is `confirmed` when the observed change in return (variant minus baseline) equals the predicted one within a stated tolerance,
   `refuted` when it does not and the day's inputs are complete, `undecided` otherwise with a reason code; (d) what would show the
   reading WRONG overall (for instance: the predicted and observed changes agreeing no better on purchase days than on days with no
   trade). Then keep it.
3. **The recomputation.** For each account-day of the set: the day's return recomputed BY YOU from the day's value, the previous
   day's value and the day's flow under the formula, once with the baseline close and once with the unadjusted close, set beside the
   served return and the round-74 variant return. First show your recomputation reproduces the two builds' own returns on these days
   (count equal within 1e-9); a day you cannot reproduce is `undecided: not reproduced` and is counted.
4. **The result,** by kind of row (purchase, sale, reinvestment, transfer) and by size of change (under 1, 1 to 10, over 10 basis
   points): confirmed, refuted, undecided; the sign of the change; the share of the total absolute change in return, over all 1,577,
   that sits on these trade days. And the plain sentence the CTO needs for its addendum: on a purchase day, which of the two closes
   makes the shares bought worth the cash paid (the ratio of q times close to c, for each close, as a distribution: median and the
   share within 1 percent of 1). Basis points and counts only.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~132/PURCHASE_DAY.json` and a short `.md`. Top-level keys, exactly: `set` (`{"changed_floor_1e9", "changed_floor_1e12",
   "trade_days", "by_kind"}`), `reproduced_reviewer` (`{"over_10bp", "with_a_row", "purchases", "sales", "reinvestments"}`), `rule`
   (`{"text", "written_at"}`), `recomputation` (`{"days", "reproduced", "not_reproduced"}`), `confirmed`, `refuted`, `undecided`,
   `by_kind_and_band`, `share_of_total_change_on_trade_days`, `cash_against_shares` (`{"baseline_close", "unadjusted_close"}`),
   `reading` (`confirmed`, `refuted` or `not_established`, under your rule (d)), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB75bw1-AC1" cell_refs="CB-bw-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~132/PURCHASE_DAY.json',encoding='utf-8'));s=d['set'];r=d['reproduced_reviewer'];c=d['recomputation'];print('PURCHASE-DAY rule_written=%s reviewer=%d/%d(%d+%d+%d) changed=%d/%d trade_days=%d reproduced=%d not_reproduced=%d confirmed=%d refuted=%d undecided=%d sum=%d reading=%s'%(bool(d['rule']['written_at']),r['with_a_row'],r['over_10bp'],r['purchases'],r['sales'],r['reinvestments'],s['changed_floor_1e9'],s['changed_floor_1e12'],s['trade_days'],c['reproduced'],c['not_reproduced'],d['confirmed'],d['refuted'],d['undecided'],d['confirmed']+d['refuted']+d['undecided'],d['reading']))"</invocation><expect>PURCHASE-DAY rule_written=True</expect></criterion>
`CB75bw1-AC1` -- the rule was written first; the reviewer's count is reproduced; every trade day carries one of three readings
(`sum` equals `trade_days`); the issuer reads the reading and how many days the recomputation reproduced.

<criterion id="CB75bw1-AC2" cell_refs="CB-bw-1" judgment="true"/>
`CB75bw1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the prediction was written from the build's own
formula before any return was recomputed; the recomputation reproduces the builds' returns before it is used; `refuted` and
`undecided` are used where they apply; the reading is `confirmed` only under the rule's own test of what would show it wrong; no
account id or account value appears.

<expected_criteria>CB75bw1-AC1,CB75bw1-AC2</expected_criteria>

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
  `ADVI_COTBKF-D2-W132-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round75.md</decomp_doc> (round 75), cell `CB-bw-1`.
<owned_cells>CB-bw-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB75bw1-AC1, CB75bw1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~132/ADVI_COTBKF.TO-CB-bw-1.purchase-day.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB75bw1-AC1,CB75bw1-AC2` BEFORE the flip. Mechanical: CB75bw1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the set with its denominators at both floors and the reviewer's 22 of 96 as reproduced; the rule as written before the recomputation, with its timestamp: the formula, the prediction, the tolerance, and what would show the reading wrong; how many days the recomputation reproduced; confirmed, refuted and undecided by kind of row and by band; the sign; the share of the total change on trade days; which close makes the shares bought worth the cash paid; the reading; the `PURCHASE-DAY` line; the account-id scan's DENOMINATOR line; a statement that no account id or value left the scratch; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the prediction is written from the build's own formula before any return is recomputed; the recomputation must reproduce the builds' returns before it is used; refuted and undecided are legal readings, and the rule states beforehand what would show the reading wrong; the reviewer's count is the positive control; BLIND: a trade row dated a day off its settlement, and an account whose prior-day value is blank.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-75 analysis @cd481e59d2 (msg 5920), section 3 item 1; `3.0.0_SA_CVO` REMEDIATION_v45 @7dbb71c512.
