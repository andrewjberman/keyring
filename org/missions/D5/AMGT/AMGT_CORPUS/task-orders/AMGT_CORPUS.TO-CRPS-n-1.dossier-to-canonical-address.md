# AMGT_CORPUS task order -- `CRPS-n-1` -- ROUND 12: the dossier store reads and writes at the naming builder's canonical prefix (`research_dossier`), with no hyphen literal left in its code

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-n-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface; the served rewrite is the issuer's drain act.
comp-iam: DECLARED-NOT-APPLICABLE -- no cloud act in this cell (the new prefix is in the same bucket the store already writes).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 12. Serves **FWD-12**: AMGT_RESAPP's reader can serve the team's cases
only from a conformant address.

## 1. THE CELL -- `CRPS-n-1`

**Where this came from.** `lib/research/corpus/dossier.py` stores each dossier with `TABLE = "research-dossier"`;
`lib/research/corpus/gold.py` `table_prefix(table)` derives the key prefix from the naming builder
(`naming.key(SOURCE, SCOPE, TIER, table, ...)`), so only the table NAME is a literal. The naming gate refuses the hyphen literal
`research-dossier` (AMGT_RESAPP's `vv-4` grant was rolled back for carrying it). The builder's own output for this store is
`lib/opal_naming.py address("amgt", <harvest scope>, "gold", "research_dossier", "security_key=X")` ->
`s3://opal-data-harvest/amgt/harvest/gold/research_dossier/security_key=X`. The CTO's ruling: the dossier store writes to that
canonical prefix, `read_dossier` reads it there, the old objects stay undeleted, and the served move is the issuer's act under a
pair. The literal is carried today by `dossier.py` (5 occurrences) and `lib/research/corpus/tests/test_backlog.py` (5).

**RULED -- what you build:**
1. `dossier.TABLE` becomes `"research_dossier"`; every read and write of the store (`write_one`, `read_dossier`, the listing
   helpers, every census and CLI mode) goes through `TABLE` / `gold.table_prefix(TABLE)`, never a typed prefix.
2. **No hyphen literal left in `dossier.py`** -- code, docstrings and comments -- and none in `test_backlog.py`. Where a docstring
   describes the store, name it by its builder address or by `TABLE`.
3. **No fallback to the legacy prefix.** `read_dossier` raises `LookupError` for a name with no object at the new prefix, exactly as
   today for an empty partition; the issuer's rewrite fills the new prefix in the same window as the merge.
4. Grep `lib/` for any other reader that builds the dossier prefix by the literal; if one exists outside your `<paths>`, file a
   row naming it and STOP on that criterion.
5. `lib/research/corpus/tests/test_dossier_canonical_address.py` (new), offline stub: `write_one` puts under
   `amgt/harvest/gold/research_dossier/`; `read_dossier` reads that prefix and does NOT read an object planted under the legacy
   prefix; `gold.table_prefix(dossier.TABLE)` equals the builder address's prefix.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_canonical_address.py
lib/research/corpus/tests/test_backlog.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-n-1.dossier-to-canonical-address.md
</paths>

READ-ONLY: every other file (`gold.py`, `lib/opal_naming.py` included), every S3 object. Scratch `.scratch/n1/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO S3 write: never run `dossier --write`. Do not change `METHOD_VERSION` (nothing is
  stored at the new prefix, so the rewrite writes without a bump). Importing `dossier` must still load no PDF library.
- The whole `lib/research/corpus/tests` suite must pass.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-n-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round12/n1_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-n-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round12/n1_AC2.sh</invocation><expect>n1 table research_dossier prefix amgt/harvest/gold/research_dossier/ equals_builder True hyphen_literal 0</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-n-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round12/n1_AC3.sh</invocation><expect>l1 dossier_import pdf_libs_loaded none read_dossier_callable True</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the store's prefix equals the builder's and the literal is gone; AC3 the bound: the import stays
  PDF-free.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-n-1.dossier-to-canonical-address.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: each AC line, the corpus suite count, and every other `lib/` carrier of the literal you found (or none).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** `1.0.0_SA_CTO~Z` msg 26555, verdict @`e1e4ae43d4`. Checks dry-run at the base: AC1 FAIL (no tests ran); AC2 FAIL
('n1 table research-dossier prefix amgt/harvest/gold/research-dossier/ equals_builder False hyphen_literal 5'); AC3 PASS. The merge
is HELD until the pair is signed and runs in one window with the rewrite (decomposition v12.0 s.1a).

<risk>SERVED</risk>
<status>complete</status>
<round>12</round>
<slot>~1</slot>
<fabric>site-z</fabric>
