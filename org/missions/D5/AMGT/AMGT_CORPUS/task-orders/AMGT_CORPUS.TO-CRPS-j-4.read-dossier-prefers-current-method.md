# AMGT_CORPUS task order -- `CRPS-j-4` -- ROUND 8: `read_dossier` serves the object carrying the producer's CURRENT method version, so a method bump is served by rule, not by write order

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-j-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface; S3 reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only in this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 8. This is the FIRST of your two orders (the second, `CRPS-j-1`,
edits the same file and follows when this one is complete). Serves **FWD-17 (b)** and the served pick behind **FWD-12**.

## 1. THE CELL -- `CRPS-j-4`

**Where this came from.** `lib/research/corpus/dossier.py` stores each dossier at
`.../research-dossier/security_key=<key>/as_of=<YYYY-MM-DD>.<sha16 of {method_version, inputs}>.json` and never overwrites.
`read_dossier(security_key)` picks the newest `as_of` DATE, then the greatest S3 `LastModified` among that date's objects
(the key name breaks an exact tie, or decides when any object in the group lacks `LastModified`, as an offline stub does). It
never reads `method_version`. `METHOD_VERSION` is `"amgt-corpus-dossier/1"` today; your next order bumps it to `/2` and the
issuer then rewrites all 95 names. Last-write-wins would serve those `/2` objects, but any later `/1` write (a rollback, a
stale writer) would be served over them. Round 7 fixed exactly this class on the continuation table (`continuation.py`
`_select_stored`: current method first, else the old behaviour).

**RULED -- what you build:**
- `read_dossier` reads each stored object's `method_version`. If ANY stored object for the name carries the module's current
  `METHOD_VERSION`, the pick is made among those objects only, by the existing rule (newest `as_of` date, then greatest
  `LastModified`, then key). If NONE does, the existing rule over all objects stands unchanged -- a name is never left
  unserved. Return shape unchanged: `{"uri", "content_sha256", "document"}`; `LookupError` unchanged.
- One listing per call, as today; each object is fetched at most once per call.
- A read-only CLI mode `python -m lib.research.corpus.dossier --pick-census` (add it to the existing mutually exclusive
  group): over `_resolved_security_keys()`, for each name, whether a stored object carries the current method version, and
  whether `read_dossier` returns one. Final line EXACTLY:
  `dossier_pick names <N> current_method_available <A> stale_pick <S>` where a stale pick is a name whose pick is NOT
  current-method while a current-method object exists. Print `stale_pick <key> <picked method_version>` per stale name. It
  may run names concurrently (a thread pool is fine: the work is S3 reads). It writes nothing.
- `lib/research/corpus/tests/test_dossier_reader_method.py` (new), stub client: a `/1` object written AFTER a `/2` on the
  same date -> `/2` returned; a `/2` on an OLDER date than a `/1` -> `/2` returned; two `/2` objects -> the later write; no
  current-method object -> exactly the pre-existing pick; the census's stale count on a planted stale case.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_reader_method.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-j-4.read-dossier-prefers-current-method.md
</paths>

READ-ONLY: every other module (`lib/research/corpus/continuation.py`'s `_select_stored` is the pattern to read). Scratch
`.scratch/j4/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO S3 write: never run `dossier --write`. Do not change `METHOD_VERSION` in this
  order (that is `CRPS-j-1`).
- The existing tests (`test_dossier.py`, `test_dossier_newest.py`, `test_dossier_model_rows.py`) keep passing unmodified; if
  one pins behaviour this rule must change, REFUSE with its name rather than editing it.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`,
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-j-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round8/j4_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-j-4"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round8/j4_AC2.sh</invocation><expect>dossier_pick names ([1-9]\d*) current_method_available \d+ stale_pick 0\b</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe on the live table: no name's pick is stale while a current-method object exists.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-j-4.read-dossier-prefers-current-method.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's line; then the issuer continues you on `CRPS-j-1`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-7 analysis s.5 item 4 @`03327ebbf9` (named by the round-7 CTO half @`54731994ee`). Checks dry-run at
the base @`e3fd90cb63`: AC1 FAIL (no test file), AC2 FAIL (argparse refuses `--pick-census`). Before the drain every stored
object is `/1` = current, so AC2 reads `current_method_available 95 stale_pick 0` after the build; the discrimination is AC1.

<risk>LOCAL</risk>
<status>complete</status>
<round>8</round>
<slot>~1</slot>
<fabric>site-z</fabric>
