# TO ADVI_COTBKF.TO-CB-br-3.scan-wide -- round 70 CB-br-3: the close-against-trade scan widened: what is left of the 346, the 50 and the 1,700

<to_id>ADVI_COTBKF.TO-CB-br-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~113</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>70</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** dell2 (placement DELL2) | **Decomp cell:** `CB-br-3` (`decompositions/ADVI_COTBKF_DECOMP.round70.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

**This is a MEASUREMENT. You change no code.**

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_70_20261011.md` section 2 item 4 and section 3 item 3; row ADVI_COTBKF-D2-W108-S1 in the channel; the round-69 scan, all
five files under `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~108/` (its class rules, its denominator and its
`not_established` list). Its scripts may still be in this worktree's scratch (`.scratch/w108/`); they are this worktree's own.

**Why.** Seven mis-scaled close series is a FLOOR: 346 of the 720 compared securities had too few pairs to class, 50 of those carry a
pair more than 10 percent off, and 1,700 traded share-priced securities have no close in the build's table at all. The CTO: "The scan
is widened once, and the count of seven is never shown without those three numbers beside it."

**Your item: shrink each of the three unknowns, and say exactly what is left.**

1. **Reproduce the round-69 denominator first** (720 securities, 7,979 pairs; classes 315 / 5 / 2 / 15 / 37 / 346 for AGREES /
   CONSTANT_SCALE / STEP / ISOLATED / NOISY / TOO_FEW). If you cannot, that is the refusal clause.
2. **The 346 too-few (and the 50 beyond 10 percent).** Widen the pairing, each widening reported SEPARATELY so its effect is visible:
   (a) a trade date with no close that day pairs with the nearest close within 3 trading days either side (report the day gap);
   (b) other custodian rows that carry a price at a market level: reinvested distributions (`dvr`: amount over quantity is the
   reinvestment price) and any other type you can show is a market-price print; say which types and why, and keep each type's pairs
   labelled; (c) the same security under another CUSIP or ticker in the table (a ticker more than one CUSIP claims): report, do not
   merge. After each widening: how many of the 346 leave TOO_FEW and into which class; how many of the 50 are now classed and as what.
3. **The 1,700 with no close.** They cannot be compared, so characterise them: by kind; how many are HELD on any date in the served
   holdings table (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3_serve_r34/account_day_value.parquet`) and so sit unpriced there; how many holding account-days
   and how many NOT_MEASURABLE account-days rest on them; and how many have a close in ANY of the six local store caches
   (`C:/dev/ajb_workspace/.scratch/advi_cotbkf/fwd3/price_cache/`) under a key the build does not match. The point: is "no close" an absence in the stores, or a
   join the build does not make?
4. **Fixed income** was left out for want of a unit. Establish the unit from the data (a bond's close near 100 against amount over
   quantity near 1.00 or near 100; accrued interest in the amount) on the 180 fixed-income securities that are in the table, or say
   precisely why it cannot be established. Do not class them unless the unit is shown.
5. **The final table.** Every class count after widening, next to its round-69 count. The CONSTANT_SCALE and STEP securities (all of
   them, with factor, span, pairs and reach as in round 69), marking which are NEW. And the statement the CTO requires, as one
   sentence in the record: the count of mis-scaled series WITH the three numbers beside it, each at its post-widening value.
6. Write the record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~113/CLOSE_VS_TRADE_SCAN_WIDE.json`, a `.csv` of the CONSTANT_SCALE and STEP securities (columns as round 69's, plus `new_in_round_70`;
   CUSIPs in a column named exactly `cusip`), and a short `.md`. Top-level keys, exactly: `round_69` (the reproduced counts),
   `widenings` (a list of `{"name", "pairs_added", "left_too_few", "newly_classed"}`), `classes` (the six names, post-widening),
   `mis_scaled` (count), `too_few_left`, `thin_beyond_10pct_left`, `no_close` (`{"securities", "held", "holding_account_days",
   "not_measurable_account_days", "found_in_a_store_under_another_key"}`), `fixed_income` (`{"unit_established", "why", "classed"}`),
   `headline` (the one sentence), `measured_account_days_affected`, `not_established`.

### ACCEPTANCE

<criterion id="CB70br3-AC1" cell_refs="CB-br-3"><invocation>python -c "import json;d=json.load(open('org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~113/CLOSE_VS_TRADE_SCAN_WIDE.json',encoding='utf-8'));r=d['round_69'];c=d['classes'];n=d['no_close'];print('SCAN-WIDE-RECORD r69_securities=%d r69_pairs=%d widenings=%d class_sum=%d mis_scaled=%d too_few_left=%d thin_beyond_10pct_left=%d no_close=%d no_close_held=%d fixed_income_unit=%s measured_account_days_affected=%d'%(r['securities_compared'],r['pairs_compared'],len(d['widenings']),sum(c.values()),d['mis_scaled'],d['too_few_left'],d['thin_beyond_10pct_left'],n['securities'],n['held'],d['fixed_income']['unit_established'],d['measured_account_days_affected']))"</invocation><expect>SCAN-WIDE-RECORD r69_securities=720 r69_pairs=7979</expect></criterion>
`CB70br3-AC1` -- the round-69 denominator is reproduced and the widened scan prints the mis-scaled count beside what is left of each
of the three unknowns.

<criterion id="CB70br3-AC2" cell_refs="CB-br-3" judgment="true"/>
`CB70br3-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each widening is reported separately and a wider
pairing is not allowed to manufacture a class (a pair across a day gap or from a reinvestment row is labelled as such); the 1,700 are
characterised, not waved away; the headline sentence carries all the numbers; fixed income is classed only if its unit is shown.

<expected_criteria>CB70br3-AC1,CB70br3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below (your deliverables folder and your own NEW channel row) and the file of this order.
- **You change no code, test, config, manifest or registry.** Everything is local; no network call.
- Before committing run `env -u COTBKF_SWEEPS_CONFIG python -m pytest data/assets/scripts/silver/tests/test_cotbkf_no_account_ids.py -q -s`
  and keep CUSIPs in CSV columns named `cusip` so the project's own scan passes; report its DENOMINATOR line.
- **NEVER `--apply`, `--overwrite`, a serve, or any S3 write or delete.** No push. No `--refresh`. No vendor call.
- A commonwealth script you run carries `COTBKF_SWEEPS_CONFIG=C:/dev/_cotbkf_private_evidence_20261009/config/commonwealth_sweeps.json` in its command line. Do not open or print anything else under that folder.
- Run outputs go under your own worktree `.scratch/` (never committed); nothing under `C:/dev/ajb_workspace/.scratch/advi_cotbkf` is modified.
- **Never print** an account id or an account's value, flow, quantity or return. Counts, dates, CUSIPs, tickers, a security's price,
  ratios, version ids and reason codes only. A build log line carrying `read_account=` is never echoed.
- **No gate override** of any kind and no `--force`. Do not weaken, delete or skip a test.
- **Refusal clause.** If a criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row with id
  `ADVI_COTBKF-D2-W113-S<k>` (k from 1), `"fabric": "dell2"`, `surfaced_at` read from the clock, APPENDED to the channel file with
  `open(path, 'a', encoding='utf-8', newline='\n')`; `git diff --numstat` must show added lines only. Never open the channel file with
  an editing tool.

<paths>
org/missions/D8/ADVI/ADVI_COTBKF/deliverables/
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit. The one channel write allowed is your own NEW row.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round70.md</decomp_doc> (round 70), cell `CB-br-3`.
<owned_cells>CB-br-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB70br3-AC1, CB70br3-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~113/ADVI_COTBKF.TO-CB-br-3.scan-wide.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB70br3-AC1,CB70br3-AC2` BEFORE the flip. Mechanical: CB70br3-AC1. A judgment criterion is recorded as PENDING-ADJUDICATION, never PASS. An artifact already committed and not changed
in the flip commit is pinned to the commit that carried it, never left `PENDING-THIS-COMMIT`.
</proof_of_spec>

**REPORT:** the reproduced round-69 counts; each widening with the pairs it adds and where the too-few securities go; the 50 thin securities' fate; the 1,700 by kind, held or not, and whether a store holds a close under another key; fixed income's unit; the post-widening class counts beside round 69's; every CONSTANT_SCALE and STEP security, new ones marked; the headline sentence; the `SCAN-WIDE-RECORD` line; the account-id scan's DENOMINATOR line; what is not established; commits; every gate refusal, verbatim.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement over local copies.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: RUN -- round 69's denominator is reproduced first; each widening is reported separately and its pairs labelled, so a looser pairing cannot manufacture a class unseen; the headline must carry the three unknowns; BLIND: a security no account ever traded has no traded price under any widening.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-70 analysis @991f749df1 (msg 5340), section 3 item 3; PRD ADDENDUM v0.7 @72d624cd26; `3.0.0_SA_CVO` REMEDIATION_v40 @90e1a7cbda.
