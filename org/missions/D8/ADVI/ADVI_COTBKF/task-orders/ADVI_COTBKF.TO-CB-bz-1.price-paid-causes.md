# TO ADVI_COTBKF.TO-CB-bz-1.price-paid-causes -- round 78 CB-bz-1: the causes of the trades that do not reproduce the price paid, to completion: the flat-charge reading stated first and tested on held-out units

<to_id>ADVI_COTBKF.TO-CB-bz-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~148</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>78</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-bz-1` (`decompositions/ADVI_COTBKF_DECOMP.round78.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT on local copies. You change no code. Nothing is fetched and no bucket is read.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_78_20261012.md` section 3 item 1 ("The causes of the trades that do not reproduce the price paid, to completion ...: the last
input the fund-basis addendum waits on.") and the sentence it serves, from the round-76 analysis: "It is not written before the 26
percent has causes: a rule that a quarter of the rows contradict is not a rule yet." Then the round-76 records: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~138/PURCHASE_ROWS_OFF.json` and its
`.md` (246 of 936 purchase rows of the 19 funds miss the UNADJUSTED close by more than 1 percent; a closed list written first left
124 `none_found`; the rate-based fee test fits at chance; and a POST HOC reading, in no count: the amount less shares times close
lands within 15 cents of 0, 3, 10, 15, 19, 30 or 34 dollars on all 936 rows, the sale rows mirrored -- "read off the rows after the
look; not a test they passed"); `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~139/PRICE_PAID.json` (the price-paid instrument over every fund: 14,250 units; the 73 substituted funds, whose
served close IS the unadjusted vendor close: 10,636 units, 225 of them outside 1 percent, unexplained); `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~144/FAILING_FUNDS.json` (the 15 failing
funds' held unadjusted series: 14 pass, five of them only through allowances); `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~140/FUNDS_BY_TRADES.json` (the classing rule that used the same
constants only to excuse units).

**The gap this cell closes.** The flat-charge reading explains almost everything and has never been tested: its constants were read
off the same rows it explains. A reading becomes a cause when it is stated first and then holds on rows that did not suggest it.

**Your item.**

1. **THE TEST FIRST.** Before any row is looked at this round, write to a file in your scratch (with a clock timestamp) and copy
   into the record:
   (a) the hypothesis, with its constants FIXED as round 76's record states them (the seven dollar figures, the 15-cent window, the
   sign: a purchase's amount above shares times close, a sale's below) -- you may not change them after;
   (b) the HELD-OUT populations it is tested on, none of which was used to read the constants: the trade units of the 73 substituted
   funds (purchases and sales), and the purchase and sale units of the 15 failing funds against their held unadjusted close for any
   fund outside round 76's 19;
   (c) the CHANCE control: the same test with the seven figures each shifted by a stated amount in each direction, and against a
   uniform expectation given the window's width, so the fit can be read against what a wrong set of constants would score;
   (d) what counts as the hypothesis HOLDING (the share of held-out units it must fit, and the margin over chance), FAILING, or
   being `not_established`;
   (e) the closed list of causes for every unit still off after it, with the ORDER and one ALTERNATIVE order: the flat charge (now
   a stated cause), a neighbouring day's close, a reinvestment or exchange recorded as a purchase, an adjusted close, another
   share class, a small quantity, `none_found`.
   Then keep it.
2. **Run the test** on the held-out populations and on round 76's own 936 rows (reported apart: in-sample). Per population: units,
   units fitting each constant, units fitting none, the chance figures, and the verdict under (d).
3. **Whatever the charge is, describe it from the rows without naming it from memory:** per constant, the funds and the YEARS it
   appears in (as counts), whether it depends on the fund, the kind of row (purchase or sale) or the size of the trade, and whether
   one account-day carries the same figure on every fund traded that day. Is anything on disk that names it (a note or a type on the
   row; a fee row dated the same day in the same account, as a COUNT)? You do not say what the charge IS unless a row says so.
4. **To completion:** every unit of every population that is still more than 1 percent off after the charge is set aside, given a
   cause from the closed list under both orders: counts per cause, how many change with the order, and `none_found` listed by fund
   and year with what was looked at. One fund carried 243 of round 76's 246: say what is particular to it.
5. **What the rule may then say.** With a flat charge set aside (ONLY if the hypothesis HOLDS), the share of purchase units and of
   sale units on which the unadjusted close reproduces the price per unit, for: the 19 funds; the 15 failing funds' held series; the
   73 substituted funds. If the hypothesis does not hold, give the plain shares and say the rule still has that share against it.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~148/PRICE_PAID_CAUSES.json` and a short `.md`. Top-level keys, exactly: `test` (`{"text", "written_at", "constants", "window"}`),
   `held_out` (`{"units", "fits", "fits_none", "chance", "verdict"}`), `in_sample` (the same keys), `by_population` (a list),
   `the_charge` (`{"by_constant", "named_on_disk"}`), `still_off` (`{"units", "causes", "alternative", "change_with_the_order",
   "none_found"}`), `fit_once_set_aside` (`{"purchases", "sales"}`), `reading` (`holds`, `fails` or `not_established`), `headline`,
   `not_established`.

### ACCEPTANCE

<criterion id="CB78bz1-AC1" cell_refs="CB-bz-1"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~148/PRICE_PAID_CAUSES.json',encoding='utf-8'));h=d['held_out'];i=d['in_sample'];s=d['still_off'];c=s['causes'];print('PRICE-PAID-CAUSES test_written=%s constants=%d held_out_units=%d held_out_fits=%d held_out_fits_none=%d held_out_chance=%s in_sample_units=%d in_sample_fits=%d reading=%s still_off=%d given=%d none_found=%d change_with_the_order=%d'%(bool(d['test']['written_at']),len(d['test']['constants']),h['units'],h['fits'],h['fits_none'],h['chance'],i['units'],i['fits'],d['reading'],s['units'],sum(v['units'] for v in c.values()),c.get('none_found',{}).get('units',0),s['change_with_the_order']))"</invocation><expect>PRICE-PAID-CAUSES test_written=True constants=7</expect></criterion>
`CB78bz1-AC1` -- the test was written first with the seven constants of round 76; it is run on held-out units and in sample, with a
chance figure; every unit still off carries a cause (`given` equals `still_off`). The issuer reads the reading.

<criterion id="CB78bz1-AC2" cell_refs="CB-bz-1" judgment="true"/>
`CB78bz1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the constants are round 76's and were not changed; the
held-out units were not used to read them; the fit is read against a chance figure and `fails` or `not_established` is used where
it applies; the charge is described from the rows and not named from memory; `none_found` is used where no test fits; no account
id or amount appears.

<expected_criteria>CB78bz1-AC1,CB78bz1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local: no S3 read, no network call.
- **Accounts.** Inside your own scratch you work with account ids as the tables hold them. NOTHING you commit, print in your report
  or write to the channel carries an account id, or an account's value, flow, quantity, balance, amount or return. Counts, ratios,
  dollar figures of a CHARGE as a class (never of an account), tickers and dates only.
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
  `ADVI_COTBKF-D2-W148-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round78.md</decomp_doc> (round 78), cell `CB-bz-1`.
<owned_cells>CB-bz-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB78bz1-AC1, CB78bz1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~148/ADVI_COTBKF.TO-CB-bz-1.price-paid-causes.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB78bz1-AC1,CB78bz1-AC2` BEFORE the flip. Mechanical: CB78bz1-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the test as written before any row was looked at, with its timestamp: the constants, the held-out populations, the chance control, what counts as holding; the fit on each held-out population and in sample, beside chance; the reading; the charge described from the rows, by constant, and whether anything on disk names it; every unit still off, by cause under both orders, with how many change and `none_found` by fund and year; what is particular to the one fund that carried 243; the fit once the charge is set aside, or the plain shares; the `PRICE-PAID-CAUSES` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no vendor call.
comp-adversary: RUN -- the constants are round 76's and are fixed in a file before any row is looked at; the units they are tested on were not used to read them; the fit is read against shifted constants and a uniform expectation, so a wrong set of constants has a score to beat; fails and not-established are legal readings; the charge is described from the rows and never named from memory; BLIND: a fee schedule is not on disk, and a charge that is a percentage on some trades and flat on others.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-78 analysis @e5d2fc8e59 (msg 6229), section 3 item 1; `3.0.0_SA_CVO` REMEDIATION_v46 @d389aa8f85.
