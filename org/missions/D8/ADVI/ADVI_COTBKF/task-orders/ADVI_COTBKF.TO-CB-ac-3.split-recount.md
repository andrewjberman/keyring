# TO ADVI_COTBKF.TO-CB-ac-3.split-recount -- round 29 CB-ac-3: re-count the 28 unconfirmed splits against the price fill

<to_id>ADVI_COTBKF.TO-CB-ac-3</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~56</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ac-3` (`decompositions/ADVI_COTBKF_DECOMP.round29.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

FWD-3's chain (`data/assets/scripts/silver/`, default `method_r28`) scales closes before a CONFIRMED split to as-traded. A split is
confirmed from the account's own rows (a quantity ratio within 0.5% of an integer k in 2..50, or 1/k, on the split day) or from dell1's
store `s3://opal-data-assets/yahoo/global/silver/price_history/cusip=<CUSIP>/splits.parquet`, and in both cases only where the stored
close is continuous across the day. Round 28 detected 61 splits: 33 applied, **28 unconfirmed and left as they are** (row D2-W53-S4,
named in `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~53/`). dell1's MDPF_DEMQUE is filling the store from this
project's ranked need list (`deliverables/PRICE_NEED/COTTONWOOD_PRICE_NEED_RANKED.csv`); its index is
`s3://opal-data-assets/yahoo/global/silver/price_history/index/index.parquet`.

**Your item (CTO ADDENDUM 4, msg 2789: "the W53-S4 re-count after the price fill. Unconfirmed splits stay unapplied").** READ-ONLY. A
script `data/assets/scripts/silver/commonwealth_split_recount.py --out <dir>` that reads the store's index AS IT STANDS (print its row
count and newest `as_of`), and for each of the 28 unconfirmed splits prints: the CUSIP, the day, whether the store now holds the CUSIP,
whether its `splits.parquet` names a split on or near that day, and whether the continuity condition would now hold -- i.e. whether the
split is NOW confirmable. Apply nothing. Write `split_recount.md`. LAST line exactly:
`SPLIT-RECOUNT unconfirmed=28 now_confirmable=<n> store_rows=<r> store_as_of=<date>`.

### ACCEPTANCE

<criterion id="CB29ac3-AC1" cell_refs="CB-ac-3"><invocation>python data/assets/scripts/silver/commonwealth_split_recount.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~56</invocation><expect>SPLIT-RECOUNT unconfirmed=28</expect></criterion>
`CB29ac3-AC1` -- the 28 re-counted against the store as it stands, with the store's size and date printed.

<expected_criteria>CB29ac3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **Read-only.** Nothing applied; no S3 write. Reads of dell1's store and this project's deliverables only.
- **Refusal clause.** If the criterion cannot be met as written, stop, write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W56-S<k>`, `"fabric": "dell2"`), and do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_split_recount.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round29.md</decomp_doc> (round 29), cell `CB-ac-3`.
<owned_cells>CB-ac-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB29ac3-AC1. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~56/ADVI_COTBKF.TO-CB-ac-3.split-recount.proof_of_spec.json`, validated
with `python .tools/proof-of-spec-check.py <instance> CB29ac3-AC1` BEFORE the flip. Mechanical.
</proof_of_spec>

**REPORT:** the SPLIT-RECOUNT line, the now-confirmable list, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only re-count.
comp-iam: DECLARED-NOT-APPLICABLE reads under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- read-only; the store read as it stands with its date printed; BLIND: a fill that lands after the read (the next re-count).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 4 (msg 2789); row D2-W53-S4.
