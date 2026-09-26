# AMGT_CORPUS task order -- `CRPS-i-1` -- ROUND 7: the continuation readers serve the CURRENT method version among input-matching objects, so a method bump is served on every name, not by hash order

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-i-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface; the served rewrite is the issuer's drain act.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 7. Serves **FWD-18** (its served half) through row `Z-S45`.

## 1. THE CELL -- `CRPS-i-1`

**Where this came from.** `lib/research/corpus/continuation.py` names each stored continuation
`<sha16 of {method_version, inputs}>.json` (`write_one`, `_inputs_sha16`), and `METHOD_VERSION` is now
`"amgt-corpus-continuation/2"`. Two readers pick "the" continuation for a name, and both take the FIRST key in sorted order
whose document `inputs` equal the current inputs: `continuation.read_latest` and `substrate._pick_stored` (the latter serves
the dossier, for four tables: continuation, sector template, fund form, typecast). `inputs` does not carry the method version,
so when a /1 and a /2 object share inputs, hash order decides. Measured by the issuer, read-only: a /2 rewrite would be served
on 49 of 95 names and the /1 object kept on 46.

**RULED -- what you build:**
- Both readers, among stored objects whose `inputs` equal the wanted inputs, prefer the one whose `method_version` equals the
  producer's CURRENT method version; among several of those, the one written last (S3 `LastModified` from the same listing);
  the key name breaks an exact tie only. If none carries the current method version, the existing behaviour stands (the
  input-matching object is still served, `current=True`) -- a table is never left unserved by this change.
- `substrate._pick_stored` learns each table's current method version from that table's own producer module constant (the
  module that writes it), never a string typed into `substrate.py`.
- Nothing else changes: no producer's write path, no object name, no `inputs` shape.
- `lib/research/corpus/tests/test_continuation_reader_method.py` (new), stub client: a /1 and a /2 object with identical
  inputs where the /1 key sorts FIRST -> both readers return the /2; two current-method objects -> the later write; no
  current-method object -> the input-matching /1 is still returned; one test per substrate table proving the table's own
  constant is what is compared.

## 3. SURFACES

<paths>
lib/research/corpus/continuation.py
lib/research/corpus/substrate.py
lib/research/corpus/tests/test_continuation_reader_method.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-i-1.continuation-readers-select-method-version.md
</paths>

READ-ONLY: every other module. Scratch `.scratch/i1/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO S3 write: never run `continuation --write` or `dossier --write`.
- The existing substrate and continuation tests keep passing unmodified; if one pins the old first-match order, REFUSE with
  its name rather than editing it.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-i-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i1_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-i-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i1_AC2.sh</invocation><expect>continuation_pick names ([1-9]\d*) current_method_available \d+ stale_pick 0\b</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-i-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round7/i1_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the bound on the live table: no reader serves a stale method while a current one matches (a
  read-only census); AC3 the bound: the corpus suite still passes.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-i-1.continuation-readers-select-method-version.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-6 analysis s.6 item 1 @`1e53f322f3`; rows Z-S45 / Z-S46 @`070cf35da9`. AC2 is a bound before the
drain (no /2 object exists, so `current_method_available 0`); the discrimination is AC1, and the drain's rewrite is what makes
AC2 read `current_method_available 95 stale_pick 0`. Checks dry-run at the base: AC1 FAIL (no such file), AC2 bound, AC3 bound.

<risk>SERVED</risk>
<status>pending</status>
<round>7</round>
<slot>~1</slot>
<fabric>site-z</fabric>

**WORKER CLOSE (`0.9.0_WK_AMGT_CORPUS~1`):** AC1 PASS -- 8 passed in test_continuation_reader_method.py (new); AC2 PASS -- `continuation_pick names 95 current_method_available 0 stale_pick 0` (no /2 object exists yet in the live table, so this is the pre-drain bound the record face names, matched exactly); AC3 PASS -- 347 passed in the whole corpus suite (up from 339, this cell's 8 new tests included), every pre-existing test unmodified.

<status>complete</status>
