# AMGT_CORPUS task order -- `CRPS-h-1` -- ROUND 6: `read_dossier` serves the dossier WRITTEN LAST on the newest date, so a rebuild on unchanged inputs writes nothing

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-h-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 1 drift candidate, on data/black_diamond; 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell reads S3 listings only; the one-name --write exercise is the issuer's drain act.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 6. Serves **FWD-17 (b)**: "a rebuild with UNCHANGED inputs writes
NOTHING".

## 1. THE CELL -- `CRPS-h-1`

**Where this came from.** `lib/research/corpus/dossier.py` stores each dossier as
`research-dossier/security_key=<k>/as_of=<YYYY-MM-DD>.<inputs_sha16>.json`. `read_dossier` returns `sorted(keys)[-1]`. On a
date holding several objects that is the one with the GREATEST INPUTS HASH, not the last one written; its docstring claims a
later hash sorts after an earlier one, which a sha256 prefix does not do. `write_one` compares fresh inputs against
`read_dossier`'s pick, so when the pick is stale it writes again on inputs already stored. Measured by the issuer: 37 of 95
names carry a rewrite on unchanged inputs, and 58 names were served a stale dossier for 3.4 to 19.3 hours.

**RULED -- what you build:**
- `read_dossier` returns, among the objects on the NEWEST `as_of` date in the key name, the one with the greatest S3
  `LastModified` (gold never overwrites, so `LastModified` is the write time); the key name breaks a tie only. Across dates the
  date decides, as today. Take `LastModified` from the same `list_objects_v2` listing (no extra call per object).
- Correct the docstring to say what it now does.
- `write_one` is NOT changed: its comparison is right once the pick is.
- `lib/research/corpus/tests/test_dossier_newest.py` (new), with a stub client: two objects on one date whose hash order is the
  REVERSE of their write order -> the later write is returned; a later date beats an earlier date regardless of time; an exact
  `LastModified` tie falls back to the key name; and `write_one` over a stub whose last write's inputs equal the fresh inputs
  prints `unchanged` and puts nothing, while the greater-hash older object's inputs differ.

## 3. SURFACES

<paths>
lib/research/corpus/dossier.py
lib/research/corpus/tests/test_dossier_newest.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-h-1.dossier-newest-is-last-write.md
</paths>

READ-ONLY: every other `lib/research/corpus/` module. Scratch `.scratch/h1/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO S3 write: never run `dossier --write` or `write_one` against the real store.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 600`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h1_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h1_AC2.sh</invocation><expect>read_dossier serves the last write (\d+) of \1\b</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-h-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round6/h1_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ subtests passed)? in </expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the bound on the live table: the changed `read_dossier` still serves the last write for every
  partition (a read-only census); AC3 the bound: the corpus suite still passes.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-h-1.dossier-newest-is-last-write.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: AC2's line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-5 analysis s.5 item 1 @`37217d8053`; rows Z-S41 (ARMED) / Z-S42 (hold) @`ac7fc54651`. Checks dry-run at
the base: AC1 FAIL (no such file), AC2 bound (95 of 95 today; the defect is in history and in the next same-day rebuild, which
AC1 exercises), AC3 bound. The drain's exercised arm (IMB `--write` twice, `wrote 0` both) is the issuer's.

<risk>SERVED</risk>
<status>pending</status>
<round>6</round>
<slot>~1</slot>
<fabric>site-z</fabric>

**WORKER CLOSE (`0.9.0_WK_AMGT_CORPUS~1`):** AC1 PASS (4 passed in test_dossier_newest.py); AC2 PASS (read_dossier serves the last write 95 of 95); AC3 PASS (312 passed in lib/research/corpus/tests).

<status>complete</status>
