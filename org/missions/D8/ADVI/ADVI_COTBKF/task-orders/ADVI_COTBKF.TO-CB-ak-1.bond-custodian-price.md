# TO ADVI_COTBKF.TO-CB-ak-1.bond-custodian-price -- round 37 CB-ak-1: does Cottonwood's own data price the three bonds

<to_id>ADVI_COTBKF.TO-CB-ak-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~65</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>37</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ak-1` (`decompositions/ADVI_COTBKF_DECOMP.round37.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

Three corporate bonds held by Cottonwood accounts have NO usable price today:

| CUSIP | issuer |
|---|---|
| 05613L3H2 | BNP Paribas |
| 95000U2D4 | Wells Fargo 4.15% 01/24/2029 |
| 651639AX4 | Newmont 2.8% 10/01/2029 |

- Their old prices were 49 Financial's constants and are being removed (round 36).
- Yahoo has no bond-specific series (`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~64/cot_price_rewrite.md`).
- FWD-3 holds them blank (988 account-days).

The CTO's ruling sets the source order: (1) Cottonwood's OWN custodian-reported price for the bond, from the cot tree, carrying the
basis `custodian_reported`; otherwise (2) UNPRICED, reason `NO_FIRM_OWNED_SOURCE`. Never another firm's price, never a proxy.

**Your item.** READ-ONLY. Write `data/assets/scripts/silver/commonwealth_bond_custodian_price.py --out <dir>`. It does the following.

1. **Search Cottonwood's OWN data for the three CUSIPs.**
   - Read the Commonwealth delivery as this project's chain reads it (`data/assets/scripts/silver/commonwealth_transactions.py`,
     `commonwealth_daily_holdings.py`, `commonwealth_portfolio_files.py`, and the cache those use).
   - Read the cot silver and gold holdings / positions in `opal-data-cot`, using keys the cot code names, and paginate with a printed
     denominator.
   - For each CUSIP, list every field that can yield a per-unit price on a date: a price column, market value / quantity, or a trade
     price on buy/sell rows. Print its source, dates covered and row count.
2. **Classify each bond by a rule committed in its OWN commit before the first run:**
   - `custodian_reported:<source>`: a per-unit price on at least one date from Cottonwood's own custodian data, with its date coverage
     printed;
   - `trade_only:<source>`: only transaction prices, on trade dates;
   - `none`: no per-unit price anywhere checked.
   - A value derived from another firm, or from an equity ticker, never counts.
3. **Print each bond's price series coverage** against its held days (988 account-days in total across the three).

Write `bond_custodian_price.md`. LAST line exactly:
`BOND-CUSTODIAN-PRICE bonds=3 custodian_reported=<a> trade_only=<b> none=<c>`.

### ACCEPTANCE

<criterion id="CB37ak1-AC1" cell_refs="CB-ak-1"><invocation>python data/assets/scripts/silver/commonwealth_bond_custodian_price.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~65</invocation><expect>BOND-CUSTODIAN-PRICE bonds=3</expect></criterion>
`CB37ak1-AC1` -- each bond is classed from its printed sources and coverage.

<criterion id="CB37ak1-AC2" cell_refs="CB-ak-1" judgment="true"/>
`CB37ak1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: each class follows from the printed rows by the rule
committed first, and no other firm's source is counted.

<expected_criteria>CB37ak1-AC1,CB37ak1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Read-only, no S3 write.** Reads are limited to Cottonwood's own data: `opal-data-cot`, and the Commonwealth delivery this chain
  already reads. NEVER read or list `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or
  `opal-data-demo`. No Yahoo, no Bloomberg.
- **Naming gate.** If it refuses typed firm tokens, derive them from `lib/opal_naming` as `commonwealth_bd_txn_writer_trace.py` does.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W65-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_bond_custodian_price.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round37.md</decomp_doc> (round 37), cell `CB-ak-1`.
<owned_cells>CB-ak-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB37ak1-AC1, CB37ak1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~65/ADVI_COTBKF.TO-CB-ak-1.bond-custodian-price.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB37ak1-AC1,CB37ak1-AC2` BEFORE the flip. Mechanical: CB37ak1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the BOND-CUSTODIAN-PRICE line; per bond the sources checked, coverage and class; commits (rule commit first).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only measurement.
comp-iam: DECLARED-NOT-APPLICABLE reads of Cottonwood's own data under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the class rule is committed before the run; only Cottonwood's own sources count; the denominator of keys and rows scanned is printed; BLIND: a custodian file the cot code does not name (named as unread).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ruling on W64-S1, CB-aj-2 CTO half @a614350d84 (msg 3346).
