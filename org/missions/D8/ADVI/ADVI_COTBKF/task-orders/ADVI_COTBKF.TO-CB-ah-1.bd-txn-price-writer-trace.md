# TO ADVI_COTBKF.TO-CB-ah-1.bd-txn-price-writer-trace -- round 34 CB-ah-1: which inputs write `bd_txn_price` into the cottonwood price store

<to_id>ADVI_COTBKF.TO-CB-ah-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~61</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>34</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ah-1` (`decompositions/ADVI_COTBKF_DECOMP.round34.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

Cottonwood's price store `s3://opal-data-cot/silver/prices/canonical_prices.parquet` carries 1,623 rows labelled `bd_txn_price`. They
cover three bond CUSIPs: 05613L3H2, 651639AX4 and 95000U2D4 (row ADVI_COTBKF-D2-W60-S1;
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~60/price_basis_census.md`).

The only writer in the repo is `data/black_diamond/scripts/silver/inject_scoped_overrides.py:136`, with values from
`data/black_diamond/scripts/silver/scoped_price_exceptions.json`. Cottonwood ("cot") and BD / 49 Financial are SEPARATE FIRMS, never
mirrored.

**Your item (CTO ADDENDUM 9, msg 3180).** A READ-ONLY CODE trace. Read repo files only. Do NOT read any S3 object of any bucket
other than `opal-data-cot`, and do not even list one: the law forbids reading another firm's data. Write
`data/assets/scripts/silver/commonwealth_bd_txn_writer_trace.py --out <dir>`. Statically, from the repo, it prints the following.

1. **The writer.** Every file and line that writes the `bd_txn_price` label or calls the writer: `inject_scoped_overrides.py`, its
   callers, any scheduler, Makefile or Terraform that runs it, and the function that writes the cottonwood store.
2. **Every input it reads,** as bucket and key prefix, resolved from the code (constants, config, `opal_naming` calls, CLI defaults),
   by file and line. It also prints which firm each bucket or prefix belongs to, by the repo's own firm map
   (`.tools/ds-precommit-check.py` `_CROSS_FIRM_FOREIGN_BUCKETS` / `_CROSS_FIRM_FOREIGN_KEY_PREFIXES`, and the bucket naming).
3. **Every output it writes** (bucket and key prefix), and specifically whether it writes `opal-data-cot`.
4. **The account ids its exceptions cover,** from `scoped_price_exceptions.json` (repo file), each with the firm the id belongs to
   where the repo says so.
5. **Class by the CTO's rule, written in the script BEFORE the run:**
   - `own_firm`: every input is Cottonwood's own data, and it writes only `opal-data-cot`.
   - `cross_firm`: any input is another firm's data. Print which input.
   - `unresolved:<what>`: an input's bucket or prefix cannot be resolved statically. Name it.

Write `bd_txn_writer_trace.md`. LAST line exactly: `BD-TXN-TRACE writer=<file:line> inputs=<n> outputs=<n> class=<own_firm|cross_firm|unresolved>`.

### ACCEPTANCE

<criterion id="CB34ah1-AC1" cell_refs="CB-ah-1"><invocation>python data/assets/scripts/silver/commonwealth_bd_txn_writer_trace.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~61</invocation><expect>BD-TXN-TRACE writer=</expect></criterion>
`CB34ah1-AC1` -- the writer, its inputs and its outputs are named by file and line, and the class is printed.

<criterion id="CB34ah1-AC2" cell_refs="CB-ah-1" judgment="true"/>
`CB34ah1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the class follows from the printed inputs by the CTO's
stated rule, and no input is left unexamined.

<expected_criteria>CB34ah1-AC1,CB34ah1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Read-only, code only.** No S3 read of any bucket except `opal-data-cot`, and none is needed. Never read or list `opal-data-bd`,
  `opal-data-49financial`, `opal-data-inf`, `opal-data-inflection` or `opal-data-demo`.
- **Rule first.** Commit the script with its class rule in its OWN commit before the first run.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W61-S<k>`, `"fabric": "dell2"`). Do not weaken the test. A `cross_firm` class is a BLOCKING row in the same commit.

<paths>
data/assets/scripts/silver/commonwealth_bd_txn_writer_trace.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round34.md</decomp_doc> (round 34), cell `CB-ah-1`.
<owned_cells>CB-ah-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB34ah1-AC1, CB34ah1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~61/ADVI_COTBKF.TO-CB-ah-1.bd-txn-price-writer-trace.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB34ah1-AC1,CB34ah1-AC2` BEFORE the flip. Mechanical: CB34ah1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the BD-TXN-TRACE line; the writer, its inputs and outputs with file:line and firm; the account ids and their firm; the
class; commits (rule commit first).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a static code trace.
comp-iam: DECLARED-NOT-APPLICABLE no S3 read needed.
comp-adversary: RUN -- the class rule is the CTO's, written before the read; no other firm's bucket is read to answer a cross-firm question; BLIND: an input resolved only at runtime (named unresolved).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 9 @cf58046f35 (msg 3180); rows D2-S48, D2-W60-S1.
