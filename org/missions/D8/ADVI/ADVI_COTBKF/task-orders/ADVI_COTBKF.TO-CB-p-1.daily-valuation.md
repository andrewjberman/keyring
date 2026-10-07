# TO ADVI_COTBKF.TO-CB-p-1.daily-valuation -- round 16 CB-p-1: daily valuation from the price stores Opal holds

<to_id>ADVI_COTBKF.TO-CB-p-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~32</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-p-1` (`decompositions/ADVI_COTBKF_DECOMP.round16.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none (built against the interfaces fixed in the decomposition)

---

## WORKER FACE

### THE CELL

FWD-3: an analyst reads each Cottonwood account's return day by day, after fees, from 2013 to June 2026; strung together over a
month, the days give Commonwealth's reported monthly return, or the difference is shown with its reason; a day that cannot be worked
out says so and is never filled in. Step 1 (daily holdings) is done. This round builds steps 2-4 against STUB prices, so that when
the price history lands the whole chain is one run. The three steps are built in parallel by three workers against fixed files:

| file | columns |
|---|---|
| `account_day_value.parquet` (step 2 writes) | `account` str, `date` date, `value` float (null unless complete), `holdings` int, `priced_holdings` int, `complete` bool |
| `daily_returns.parquet` (step 3 writes) | `account` str, `date` date, `value` float, `flow` float, `ret` float (decimal; null when blank), `blank_reason` str |
| `monthly_grade.csv` (step 4 writes) | `account, month (YYYY-MM), computed_pct, reported_pct, diff_pct, grade (MATCH/DIFF/UNGRADABLE), reason` |

**Your step: 2, daily valuation.** Build `data/assets/scripts/silver/commonwealth_daily_valuation.py`, read-only:
1. holdings: `commonwealth_daily_holdings.load_tx_pos()` then `daily_holdings_table(tx)` (import; never copy) -> `account, date, cusip, quantity`;
2. prices: the six stores in `data/assets/scripts/analysis/commonwealth_price_census.py` -- import `STORES`, `read_store` (or
   `load_store_cached`), `symbol_claims`, `match_security`; a security matches by CUSIP first, then by a ticker no other CUSIP
   claims; plus, when `--sechist <s3 prefix>` is given, that series (a clearly named function that raises if the prefix holds
   nothing readable). Cash securities (CUSIP starting `FDIC`, or `CFNCASH`) are priced at 1.0;
3. value each holding at that day's close (no carry-forward from another day, ever); an account-day is `complete` only when every
   holding has a price, and only then has a `value`;
4. write `account_day_value.parquet` to `--data-dir` (default `<repo>/.scratch/advi_cotbkf/fwd3/`) and `daily_valuation.md` to `--out`
   (counts, coverage by year, top unpriced securities by holding-days), and print as its LAST line exactly:
   `DAILY-VALUATION accounts=<a> account_days=<d> complete=<c> holding_days=<h> priced=<p> blank=<b> sources=<comma-separated store ids that priced at least one holding>`.

**Tests** `data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py` (stubs, no AWS): two securities on one day, one
priced and one not, give `complete=False` and `value` null; with both priced, `value` equals the hand sum; a control: removing one
price row turns a complete day blank; a cash CUSIP is valued at 1.0 with no store row.

### ACCEPTANCE

<criterion id="CB16p1-AC1" cell_refs="CB-p-1"><invocation>python -m pytest -q data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py</invocation><expect>passed</expect></criterion>
`CB16p1-AC1` -- the valuation rules and the blank-not-filled control on stubs.

<criterion id="CB16p1-AC2" cell_refs="CB-p-1"><invocation>python data/assets/scripts/silver/commonwealth_daily_valuation.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~32</invocation><expect>DAILY-VALUATION accounts=1533</expect></criterion>
`CB16p1-AC2` -- today's coverage from the stores Opal holds, recorded, not presumed (most account-days are expected blank until the price load).

<expected_criteria>CB16p1-AC1,CB16p1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Large parquet output under `.scratch/`, uncommitted.
- **Read-only.** No apply, no S3 write, no vendor call, no download of any kind, never bun. Read only the buckets named here; never
  `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`. Do not edit any existing script.
- **Unpriced is blank.** A value, return or month that cannot be worked out is null with its reason, never estimated or filled.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W32-S<k>`, `"fabric": "dell2"`, `surfaced_at` the actual UTC time you file it), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_daily_valuation.py
data/assets/scripts/silver/tests/test_commonwealth_daily_valuation.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round16.md</decomp_doc> (round 16), cell `CB-p-1`.
<owned_cells>CB-p-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB16p1-AC1, CB16p1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~32/ADVI_COTBKF.TO-CB-p-1.daily-valuation.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB16p1-AC1,CB16p1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the DAILY-VALUATION line, the coverage by year, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a local derivation run by hand; no schedule until FWD-3 is served.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- a value only from a same-day close; a blank holding blanks the account-day; the control removes a price and the day goes blank; BLIND: prices for securities no store holds (the SECHIST load).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 999 (yes to round 16); draft @661c50a7ac; decomposition round 16.
