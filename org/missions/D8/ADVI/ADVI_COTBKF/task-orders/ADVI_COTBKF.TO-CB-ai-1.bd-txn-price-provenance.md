# TO ADVI_COTBKF.TO-CB-ai-1.bd-txn-price-provenance -- round 35 CB-ai-1: how 49 Financial's three bond prices entered opal-data-cot

<to_id>ADVI_COTBKF.TO-CB-ai-1</to_id>
<project>ADVI_COTBKF</project>
<issued_to>0.9.0_WK_ADVI_COTBKF~63</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>35</round>
<workstream>~C2</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL2) | **Decomp cell:** `CB-ai-1` (`decompositions/ADVI_COTBKF_DECOMP.round35.md`) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

Cottonwood's price store `s3://opal-data-cot/silver/prices/canonical_prices.parquet` carries 1,623 rows whose `source` is the 49 Financial
label (spelled `bd` + `_txn_price`). They cover three bond CUSIPs:

| CUSIP | price | dates |
|---|---|---|
| 05613L3H2 | 1.0188 | 2024-10-15 to 2026-06-09 |
| 95000U2D4 | 0.9804 | 2024-01-24 to 2026-06-09 |
| 651639AX4 | 0.9037 | 2024-04-01 to 2026-06-09 |

These are exactly the constants in 49 Financial's `data/black_diamond/scripts/silver/scoped_price_exceptions.json`. The only writer of the
label is 49 Financial's `data/black_diamond/scripts/silver/inject_scoped_overrides.py:136`. Cottonwood's
`data/cot/scripts/gold/build_canonical_prices_v2.py:22-24` states that cot does not run that inject. The repo guard
`.tools/ds-precommit-check.py` `_CROSS_FIRM_FOREIGN_BUCKETS` (generated from `infra/logic/registry/scopes.json`) already bars `data/cot/`
from `opal-data-bd`.

The CTO reads this as CONTAMINATED DATA that reached the cot store by another route. Evidence is in
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~61/bd_txn_writer_trace.md`.

The store object has ONE version (LastModified 2026-06-09T20:42:16Z), so there is no version history to bisect.

**Your item (CTO ADDENDUM 9.1, msg 3188).** READ-ONLY. Write
`data/assets/scripts/silver/commonwealth_bd_txn_provenance.py --out <dir>`. It names the route by which the label entered
`opal-data-cot`.

1. **The store object.** Print its `head-object` metadata (all `x-amz-meta-*`, ContentType, ETag, VersionId, LastModified) and its
   parquet file metadata (schema metadata, created_by, any writer or run tag).
2. **Every other key in `opal-data-cot` that carries the label or the three CUSIPs.**
   - Enumerate the cot price lineage prefixes the cot writers name (read them from the cot code, e.g. `silver/prices/`, gold price
     inputs, backups, seeds).
   - Paginate fully and print the denominator of keys scanned.
   - For each parquet key, read only the `source` / `cusip` / `ticker` columns.
   - Print each hit's key, version, LastModified and row count.
   - Put the earliest hit first.
3. **The cot writers' history.** For every repo script that writes `silver/prices/canonical_prices.parquet` under `opal-data-cot`
   (`data/cot/...`, plus any shared builder run with `BD_S3_BUCKET=opal-data-cot`), print the `git log` of that file and its run config
   (`infra/aws/terraform/cot-pipeline/ssm.tf`, `data/cot/scripts/gold/gold_dispatch.sh`) around the earliest hit's time. Name any
   step that copies, seeds or reads another firm's prices.
4. **Class by a rule committed in its OWN commit BEFORE the first run:**
   - `seeded_copy`: an earlier cot key holds the rows, written by a copy or seed whose source was 49F's store or file;
   - `shared_builder_run`: a shared builder ran with cot's bucket and 49F's exceptions;
   - `live_cot_path:<file:line>`: a current cot code path the generated guard misses;
   - `untraced:<what was checked>`.

   A `live_cot_path` class is a BLOCKING row in the same commit.
5. **The delete list for Andrew.** List every cot key and version carrying the rows, with sizes. List them only; delete nothing.

Write `bd_txn_provenance.md`. LAST line exactly: `BD-TXN-PROVENANCE keys_scanned=<n> keys_with_rows=<k> earliest=<key@time> class=<class>`.

### ACCEPTANCE

<criterion id="CB35ai1-AC1" cell_refs="CB-ai-1"><invocation>python data/assets/scripts/silver/commonwealth_bd_txn_provenance.py --out org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~63</invocation><expect>BD-TXN-PROVENANCE keys_scanned=</expect></criterion>
`CB35ai1-AC1` -- the cot keys carrying the rows are found with a printed denominator, the earliest is named, and the class is printed.

<criterion id="CB35ai1-AC2" cell_refs="CB-ai-1" judgment="true"/>
`CB35ai1-AC2` -- JUDGMENT, graded by 3.0.0_SA_CVO at L9 and never self-graded: the class follows from the printed keys, metadata and
history by the pre-written rule, and the delete list is complete for what was scanned.

<expected_criteria>CB35ai1-AC1,CB35ai1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Read-only. NO S3 write, and NO delete:** removal is Andrew's act.
- Reads are limited to `opal-data-cot`. NEVER read or list `opal-data-bd`, `opal-data-49financial`, `opal-data-inf`,
  `opal-data-inflection` or `opal-data-demo`. The route is named from cot's side and the repo.
- **Rule first.** Commit the script with its class rule in its OWN commit before the first run. If the naming gate refuses typed firm
  tokens, derive them from `lib/opal_naming` as ~61 did.
- **Refusal clause.** If the criterion cannot be met as written, stop. Write the reason in your report and a NEW surprise row (id
  `ADVI_COTBKF-D2-W63-S<k>`, `"fabric": "dell2"`). Do not weaken the test.

<paths>
data/assets/scripts/silver/commonwealth_bd_txn_provenance.py
org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_COTBKF/decompositions/ADVI_COTBKF_DECOMP.round35.md</decomp_doc> (round 35), cell `CB-ai-1`.
<owned_cells>CB-ai-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CB35ai1-AC1, CB35ai1-AC2. Instance at
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~63/ADVI_COTBKF.TO-CB-ai-1.bd-txn-price-provenance.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CB35ai1-AC1,CB35ai1-AC2` BEFORE the flip. Mechanical: CB35ai1-AC1. A
judgment criterion is recorded as PENDING-ADJUDICATION, never PASS.
</proof_of_spec>

**REPORT:** the BD-TXN-PROVENANCE line; the keys with rows (version, time, rows); the store's metadata; the writers' history around the
first write; the class; the delete list; commits (rule commit first).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only trace.
comp-iam: DECLARED-NOT-APPLICABLE reads of opal-data-cot under the dell2 identity; BLIND: none needed.
comp-adversary: RUN -- the class rule is committed before the run; the denominator of keys scanned is printed; no other firm's bucket is read; nothing is deleted; BLIND: a route that left no key or metadata in cot (named untraced).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: `1.0.0_SA_CTO~DELL2` ADDENDUM 9.1 @3093730512 (msg 3188); row D2-W61-S1.
