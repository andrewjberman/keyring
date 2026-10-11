# TO ADVI_COTBKF.TO-CB-bx-3.funds-by-trades -- round 76 CB-bx-3: which funds: every fund series classed by its trade rows under a rule written first, set beside the reinvestment classes; the failing funds named

<to_id>ADVI_COTBKF.TO-CB-bx-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~140</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>76</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bx-3` (`decompositions/ADVI_COTBKF_DECOMP.round76.md`) |
**outcome_ref:** FWD-3 | **depends_on:** CB-bx-1, CB-bx-2

---

## WORKER FACE

### THE CELL

**This is a CLASSING of funds from two records already in the tree. You change no code. Nothing is fetched.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_76_20261011.md` section 3 item 3 ("Which funds, not which family: the funds whose served close fails cell 2 on more than a
stated share of their trade rows, listed with their counts, set beside the 19, the 33 validated and the 237 unreadable. A fund that
was unreadable by reinvestment and is readable by trades changes class here.") and section 4 ("the test that a series IS unadjusted
is that it reproduces the custodian's price paid on that fund's trade rows; a series that fails is a named correction, never a
class rule"); this round's two records, both in the tree when you start (if either is absent, that is the refusal clause):
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~139/PRICE_PAID.json` with its per-fund `.csv`, and
`.../0.9.0_WK_ADVI_COTBKF~138/PURCHASE_ROWS_OFF.json` (the causes of rows that are off for a reason that is NOT a wrong close: a fee
inside the amount, a neighbouring day's close, a different instrument).

**Your item.**

1. **THE RULE FIRST.** Before any fund is classed, write to a file in your scratch (with a clock timestamp) and copy into the record:
   the minimum number of trade rows a fund needs to be read; which band counts as a row the served close FAILS, given what cell 1
   found about fees (a front load puts a PURCHASE a few percent off with a right close, so say how purchases in the fee band are
   treated, and that sales are not excused by it); the share of failing rows above which a fund `fails`, at or below which it
   `passes`, and what is `mixed` or `too_few`. State why each number, without reference to how many funds each choice fails.
2. **Every fund series classed** (270): `fails`, `passes`, `mixed`, `too_few`, `no_trade_row`. The counts sum to 270.
3. **Set beside the earlier classes,** as a table of counts: the 19 moved; the 33 validated by reinvestment; the 237 unreadable by
   reinvestment; the 73 substituted and the 197 left on the store. **The funds that change class:** unreadable by reinvestment and
   now `fails` or `passes` by trades, listed by ticker with their counts. And any conflict, by ticker: a fund validated by
   reinvestment whose trades say `fails`, or one that read adjusted and whose trades say `passes`.
4. **The named list:** every fund that `fails`, by ticker, with its trade rows, its failing rows, its median ratio and the dates of
   its first and last failing row. This is the list a named correction would start from; you propose no correction.
5. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~140/FUNDS_BY_TRADES.json`, a `.csv` of all 270 (columns: cusip, ticker, class_by_trades, trade_rows, failing_rows, median_ratio,
   class_by_reinvestment, substituted, moved_in_round_74; CUSIPs only in the column named exactly `cusip`) and a short `.md`.
   Top-level keys, exactly: `rule` (`{"text", "written_at", "minimum_rows", "failing_band", "share_fails"}`), `fund_series` (270),
   `fails`, `passes`, `mixed`, `too_few`, `no_trade_row`, `against_earlier` (a table of counts), `changes_class` (a list),
   `conflicts` (a list), `named` (a list), `headline`, `not_established`.

### ACCEPTANCE

<criterion id="CB76bx3-AC1" cell_refs="CB-bx-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~140/FUNDS_BY_TRADES.json',encoding='utf-8'));print('FUNDS-BY-TRADES rule_written=%s minimum_rows=%s share_fails=%s fund_series=%d fails=%d passes=%d mixed=%d too_few=%d no_trade_row=%d sum=%d named=%d changes_class=%d conflicts=%d'%(bool(d['rule']['written_at']),d['rule']['minimum_rows'],d['rule']['share_fails'],d['fund_series'],d['fails'],d['passes'],d['mixed'],d['too_few'],d['no_trade_row'],d['fails']+d['passes']+d['mixed']+d['too_few']+d['no_trade_row'],len(d['named']),len(d['changes_class']),len(d['conflicts'])))"</invocation><expect>FUNDS-BY-TRADES rule_written=True</expect></criterion>
`CB76bx3-AC1` -- the rule was written first; every fund series carries one class (`sum` equals 270); the failing funds are named
(`named` equals `fails`); the issuer reads the changes of class and the conflicts.

<criterion id="CB76bx3-AC2" cell_refs="CB-bx-3" judgment="true"/>
`CB76bx3-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the rule's numbers precede the classing and are not
chosen by their yield; a purchase in the fee band is treated as the rule says and a sale is not excused by a fee; `too_few` and
`mixed` are used where they apply; every conflict with the reinvestment reading is listed; no correction is proposed.

<expected_criteria>CB76bx3-AC1,CB76bx3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local: no S3 read, no network call.
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
  `ADVI_COTBKF-D2-W140-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round76.md</decomp_doc> (round 76), cell `CB-bx-3`.
<owned_cells>CB-bx-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB76bx3-AC1, CB76bx3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~140/ADVI_COTBKF.TO-CB-bx-3.funds-by-trades.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB76bx3-AC1,CB76bx3-AC2` BEFORE the flip. Mechanical: CB76bx3-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the rule as written before the classing, with its timestamp and its numbers and why each; the five classes over 270; the table against the 19, the 33, the 237, the 73 and the 197; the funds that change class, by ticker; every conflict with the reinvestment reading, by ticker; the named failing funds as a count and where the list is; the headline; the `FUNDS-BY-TRADES` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- held until cells 1 and 2 drain, since the fee finding decides what a failing row is; the rule's numbers are written before any fund is classed and not chosen by their yield; a sale is never excused by a fee; too-few and mixed are legal classes; every conflict with the reinvestment reading is listed; no correction is proposed; BLIND: a fund with no trade row.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-76 analysis @8ae9f87cf2 (msg 5996), section 3 item 3; `3.0.0_SA_CVO` round-75 grade file @0e95fc9cca.
