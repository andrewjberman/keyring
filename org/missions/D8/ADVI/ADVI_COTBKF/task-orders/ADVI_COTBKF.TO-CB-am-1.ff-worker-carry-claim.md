# TO ADVI_COTBKF.TO-CB-am-1.ff-worker-carry-claim -- round 39 CB-am-1: the cot gold carry-forward stamps its claim and never carries a foreign price

<to_id>ADVI_COTBKF.TO-CB-am-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~67</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>39</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-am-1` (`decompositions/ADVI_COTBKF_DECOMP.round39.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

Cottonwood's gold holdings builder `data/cot/scripts/gold/B_00.canonical_holdings.py` fills non-Schwab dates from the prior holdings
file in `_ff_worker` (line 1339).

For each asset, it uses today's `canonical_prices` row if one exists. Otherwise it reuses the prior file's `price` for that
`asset_name` (`fallback`, or the whole `prior_price_lookup` when the day has no prices), then calls `price_holdings(ph, hybrid_prices)`.
A carried price is indistinguishable from a fresh one in the output: no column says it was carried, or from which date. The CTO calls
this an UNFLAGGED stale-price carry-forward.

It matters because Cottonwood's price store just had 49 Financial's rows removed (three bonds; source label spelled `bd` + `_txn_price`).
A carry-forward could put such a price back with no claim field. The path is unreachable for cot today, because its input prefix is
empty. The fix is made now so it is right when that prefix fills.

**Your item (CTO, CB-aj-2 CTO half AMENDMENT 1 @fa3cabc1ea).** Change ONLY `_ff_worker` and what it passes to `price_holdings`, so
that both hold:
1. **Every row whose price was carried** (not from today's `canonical_prices`) carries `price_basis = "carried_forward"` and
   `price_source_date = <the prior file's date>`. Every fresh row carries `price_basis = "same_day"` and `price_source_date = <date>`.
   The two new columns are added to the output and nothing else changes.
2. **No price is carried whose prior row's `source` is another firm's label.** The label set is derived from the repo's firm map
   (`lib/opal_naming` lookup, as `data/assets/scripts/silver/commonwealth_bd_txn_writer_trace.py` does), not hand-typed.
   - Such an asset's carried price is null, with `price_basis = "not_carried_foreign_source"`. It is never zero.

Write the test `data/cot/scripts/gold/tests/test_b00_ff_carry_claim.py`. On a small synthetic prior file plus a sparse prices day, it
asserts:
- (a) a fresh asset reads `same_day`;
- (b) a missing asset reads `carried_forward` with the prior date;
- (c) a foreign-labelled prior price is not carried and reads `not_carried_foreign_source` with a null price;
- (d) every other existing column is unchanged versus the current code on the same input.

The commit that adds the test and the change must be preceded by a commit of the test ALONE, which fails at the base.

Do NOT deploy. Shipping the gold script to the cot code mirror is a later SERVED cell under its own pair.

### ACCEPTANCE

<criterion id="CB39am1-AC1" cell_refs="CB-am-1"><invocation>python -m pytest data/cot/scripts/gold/tests/test_b00_ff_carry_claim.py -q</invocation><expect>passed</expect></criterion>
`CB39am1-AC1` -- the four assertions pass on the changed code. The test alone was committed first and failed at the base.

<criterion id="CB39am1-AC2" cell_refs="CB-am-1" judgment="true"/>
`CB39am1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- the change is confined to `_ff_worker` and what it passes;
- the firm label set is derived, not typed;
- no carried price escapes the claim.

<expected_criteria>CB39am1-AC1,CB39am1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Code and test only.** No S3 write and no deploy. The existing tests in `data/cot/scripts/gold/tests/` stay green.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W67-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/cot/scripts/gold/B_00.canonical_holdings.py
data/cot/scripts/gold/tests/test_b00_ff_carry_claim.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round39.md</decomp_doc> (round 39), cell `CB-am-1`.
<owned_cells>CB-am-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB39am1-AC1, CB39am1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~67/ADVI_COTBKF.TO-CB-am-1.ff-worker-carry-claim.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB39am1-AC1,CB39am1-AC2` BEFORE the flip. Mechanical: CB39am1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the pytest line; the diff summary (lines changed in `_ff_worker`); the derived label set; commits, with the test-alone
commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change, not deployed (the path is unreachable for cot today: schwab/silver/rps/ empty, CTO-measured).
comp-iam: DECLARED-NOT-APPLICABLE no AWS act.
comp-adversary: RUN -- the test alone first (fails at base); the change confined to _ff_worker; firm labels derived, not typed; null never zero; BLIND: other carry paths in B_00 outside _ff_worker (named in the report if seen).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` CB-aj-2 CTO half AMENDMENT 1 @fa3cabc1ea (msg 3385).
