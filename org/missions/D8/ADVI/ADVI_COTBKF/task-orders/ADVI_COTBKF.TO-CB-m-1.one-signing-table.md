# TO ADVI_COTBKF.TO-CB-m-1 -- round 13 CB-m-1: every transaction type signed in ONE table, then daily holdings rebuilt

<to_id>ADVI_COTBKF.TO-CB-m-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~29</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-m-1` (`decompositions/ADVI_COTBKF_DECOMP.round13.md`) |
**outcome_ref:** FWD-3 (CB12l1-AC3) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`CB-m-1`, FWD-3: the daily-holdings rebuild (`data/assets/scripts/silver/commonwealth_daily_holdings.py`, round 12) signs each
transaction's quantity with `commonwealth_crosswalk.SIGN` (`commonwealth_crosswalk.py` lines 80-82). That table has no entry for `leu`
(cash in lieu: a fraction of a share sold for cash), so those fractions are never subtracted -- 13 of 13 snapshot differences equal their
pair's `leu` quantity; 515 `leu` rows across 69 accounts carry the defect.

Worse, there are TWO signing tables. `commonwealth_account_links.py` lines 83-87 has its own `HOLDING_SIGN`, which disagrees with `SIGN`:
it signs `leu` -1 and also `trci`, `trco`, `ss`, `si`, `cs`, `so`, `LOX`, `LISU`, `LICASU`, `TRCISU`, `BYX`, `LIX`, `pyd`, which `SIGN`
omits; `SIGN` signs `ci` and `12b1`, which `HOLDING_SIGN` omits. One property, two rules.

**Do, in order:**
1. **The census first.** Build `data/assets/scripts/analysis/commonwealth_tx_types.py`, read-only, over the applied silver transactions
   (`opal_naming.address("commonwealth", <cottonwood scope via opal_naming.lookup>, "silver", "transactions", "date=2026-06-23")`): for
   EVERY `Transaction_Type`, print its row count, how many rows carry a non-zero `Quantity` on a non-cash CUSIP, a sample
   `Transaction_Description`, and its sign in the ONE table (below) or `UNSIGNED`. Last line exactly:
   `TX-TYPES types=<n> signed=<s> unsigned=<u> unsigned_with_quantity=<q> unsigned_with_quantity_named=<k>`.
2. **ONE table.** Create `data/assets/scripts/silver/commonwealth_signs.py` holding the single signing table and a short docstring per
   type group. Decide each type from the census and the two old tables: where the two agree, keep it; where they disagree or one omits it,
   decide from the type's description and its quantity-bearing rows, and write the reason beside it. `leu` is -1. `ileu` is decided from
   its one quantity-bearing row, with that row's reasoning written beside it. A type that moves no shares may stay unsigned ONLY if the
   module names it in an explicit `NO_SHARE_MOVEMENT` set with a one-line reason -- that is how `unsigned_with_quantity_named` counts.
   Make `commonwealth_crosswalk.SIGN`, `commonwealth_account_links.HOLDING_SIGN` and the daily holdings all come from this module
   (import it; keep the old names as aliases so nothing else breaks). Change nothing else in those scripts.
3. **The rebuild.** Re-run the daily holdings. Its last line gains two fields after the existing ones:
   `fractional_residuals=<f> fractional_accounts=<a>` -- over ALL 1,533 accounts, the account-security pairs left holding a non-zero
   quantity under one share after their LAST transaction; write each to `fractional_residuals.csv` with its type history (the ordered
   types of that pair's rows).

**Tests:** in `data/assets/scripts/silver/tests/` -- a stub with a buy of 10.4 and a `leu` of 0.4 holds 10.0 (the leu arm); a stub of the
crosswalk and the account links each resolve `leu` to -1 through the one module (the single-rule arm); every existing test of the three
scripts keeps passing.

### ACCEPTANCE

<criterion id="CB13m1-AC1" cell_refs="CB-m-1"><invocation>python data/assets/scripts/analysis/commonwealth_tx_types.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~29</invocation><expect>unsigned_with_quantity=0</expect></criterion>
`CB13m1-AC1` -- every type that moves a quantity is signed (or named in `NO_SHARE_MOVEMENT` with its reason, which then counts as signed).

<criterion id="CB13m1-AC2" cell_refs="CB-m-1"><invocation>python data/assets/scripts/silver/commonwealth_daily_holdings.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~29</invocation><expect>snapshot_diffs=0</expect></criterion>
`CB13m1-AC2` -- the rebuild on the one table: the snapshot pairs all equal; `fractional_residuals` and `fractional_accounts` on the same
line are recorded, not presumed, and listed in the CSV.

<criterion id="CB13m1-AC3" cell_refs="CB-m-1" judgment="true"/>
`CB13m1-AC3` -- JUDGMENT, graded by `3.0.0_SA_CVO` at L9: account acct#0e4ff3a3 read again across its span, with 0 cash-in-lieu residuals.

<expected_criteria>CB13m1-AC1,CB13m1-AC2,CB13m1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scratch under `.scratch/`, uncommitted.
- **Read-only on S3.** No apply of any table; no vendor call; no download; never bun.
- **In the three existing scripts change only the source of the signing table** (import it); every other behaviour stays.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `ADVI_COTBKF-D2-W29-S<k>`, `"fabric": "dell2"`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_signs.py
data/assets/scripts/analysis/commonwealth_tx_types.py
data/assets/scripts/silver/commonwealth_crosswalk.py
data/assets/scripts/silver/commonwealth_account_links.py
data/assets/scripts/silver/commonwealth_daily_holdings.py
data/assets/scripts/silver/tests/test_commonwealth_signs.py
data/assets/scripts/silver/tests/test_commonwealth_daily_holdings.py
data/assets/scripts/silver/tests/test_commonwealth_crosswalk.py
data/assets/scripts/silver/tests/test_commonwealth_account_links.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round13.md</decomp_doc> (round 13), cell `CB-m-1`.
<owned_cells>CB-m-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB13m1-AC1, CB13m1-AC2, CB13m1-AC3 (judgment: UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming 3.0.0_SA_CVO; never
PASS or FAIL). Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~29/ADVI_COTBKF.TO-CB-m-1.one-signing-table.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB13m1-AC1,CB13m1-AC2,CB13m1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the TX-TYPES and DAILY-HOLDINGS lines, every type whose sign you decided (with the reason), the fractional residuals summarized,
commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE code and a local rebuild.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity on opal-data-assets; denominator 1 bucket; BLIND: none needed.
comp-adversary: RUN -- one rule for one property (two divergent tables found by the issuer); every type censused before any sign is set; the check spans all accounts, not the one-day snapshot's pairs; BLIND: transaction types whose description misleads.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-12 analysis @9a9384d247, E1; CVO grade CB12l1-AC3 NOT MET (row D2-S24).
