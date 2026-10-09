# TO ADVI_COTBKF.TO-CB-an-1.source-firm-field -- round 40 CB-an-1: every cot price row carries source_firm, set from its input's address

<to_id>ADVI_COTBKF.TO-CB-an-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~68</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-an-1` (`decompositions/ADVI_COTBKF_DECOMP.round40.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

Cottonwood's price writer `data/cot/scripts/gold/build_canonical_prices_v2.py` builds
`canonical[['date', 'asset_name', 'ticker', 'price', 'source']]` (line 565) and writes `silver/prices/canonical_prices.parquet` (line
~624). Its `source` column is a provenance LABEL (`yahoo_finance`, `linear_interpolation`, `transaction_observed`, ...), not a firm.

The label `bd_txn_price` once carried 49 Financial's data into this store. But `bd_` can mean either the Black Diamond PLATFORM (which
serves Cottonwood's own accounts) or the separate bd FIRM, so a token cannot decide whether a row is another firm's.

**CTO ruling (ADDENDUM 12 @7d33a8581d).** Every price row carries `source_firm`: the firm whose data or configuration produced it, set
by the writer from its INPUT's address (the bucket and key prefix it read), never from a name or ticker token. The cross-firm check reads
`source_firm != cottonwood` as the breach. A missing `source_firm` is `absent`, which grades NOT-CLEAN.

**Your item.** Code and tests only, no deploy, no S3 write.

1. **In `build_canonical_prices_v2.py`:**
   - Give every input source the writer reads (each S3 read and each repo file it loads) a firm.
   - Resolve that firm from the input's bucket and key prefix through `lib/opal_naming` (`lookup()` / the registry). Never hand-type it.
   - Stamp `source_firm` on every output row from the input that produced it. An interpolated row takes the firm of the points it
     interpolates between; if those disagree, it reads `mixed`.
   - Add the column after `source`. No other column changes.
   - An input whose firm cannot be resolved stamps `absent`. Print the count.
2. **In `data/assets/scripts/silver/commonwealth_cot_price_rewrite.py`:** the census reads `source_firm` when present.
   - Per key, report rows with `source_firm == cottonwood`, `!= cottonwood` (BREACH) and `absent` (NOT-CLEAN).
   - Today's 38 keys have no such column, so they all read `absent`. That is expected and is printed.
3. **Tests:**
   - `data/cot/scripts/gold/tests/test_canonical_prices_source_firm.py`, on synthetic inputs at a cottonwood address and at a foreign
     address, asserts: (a) the column exists after `source`; (b) a row from the cottonwood input reads `cottonwood`; (c) a row from the
     foreign-address input reads that firm; (d) an unresolvable input reads `absent`; (e) the other columns are unchanged versus the
     current code.
   - Commit the test ALONE first; it must fail at the base.

### ACCEPTANCE

<criterion id="CB40an1-AC1" cell_refs="CB-an-1"><invocation>python -m pytest data/cot/scripts/gold/tests/test_canonical_prices_source_firm.py -q</invocation><expect>passed</expect></criterion>
`CB40an1-AC1` -- the five assertions pass on the changed writer. The test alone was committed first and failed at the base.

<criterion id="CB40an1-AC2" cell_refs="CB-an-1" judgment="true"/>
`CB40an1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded:
- `source_firm` comes from the input's address via the registry, never from a token;
- absent is never defaulted to cottonwood;
- the census reports absent as NOT-CLEAN.

<expected_criteria>CB40an1-AC1,CB40an1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Code and tests only.** No S3 write and no deploy. The existing tests in `data/cot/scripts/gold/tests/` and
  `data/assets/scripts/silver/tests/` stay green.
- **Disjoint from round 39.** Round 39 (~67) is editing `B_00.canonical_holdings.py`, a different file. Do not touch it.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W68-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/cot/scripts/gold/build_canonical_prices_v2.py
data/cot/scripts/gold/tests/test_canonical_prices_source_firm.py
data/assets/scripts/silver/commonwealth_cot_price_rewrite.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round40.md</decomp_doc> (round 40), cell `CB-an-1`.
<owned_cells>CB-an-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB40an1-AC1, CB40an1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~68/ADVI_COTBKF.TO-CB-an-1.source-firm-field.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB40an1-AC1,CB40an1-AC2` BEFORE the flip. Mechanical: CB40an1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the pytest lines (the new test and both suites); the per-input firm table, with how each resolved; the census output on
today's 38 keys; commits, with the test-alone commit first.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a code change, not deployed; the field lands with the next manual silver-prep under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE no AWS act.
comp-adversary: RUN -- the test alone first; the firm comes from the address via the registry, never a token; absent is never defaulted; BLIND: an input path resolved only at runtime (named; absent).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 12 @7d33a8581d (msg 3390); row D2-S62.
