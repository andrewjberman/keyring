# AMGT_CORPUS task order -- `CRPS-p-1` -- ROUND 14: FWD-9 inside its bound -- both arms of `readonly_proof` write only under ONE `mkdtemp` directory that is gone at exit

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-p-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only (the arm's client is RetainedOnlyClient: 0 actual puts).
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 14. Serves **FWD-9 (the ingestion cannot write to the library)**.

## 1. THE CELL -- `CRPS-p-1`

**Where this came from.** FWD-9's fence (PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md`): *"a deliberate negative control runs the
ingestion against a read-only copy of the library and completes; and a census of the project's own code prints zero write, move,
delete or open-for-write calls against any path under the library root, with the denominator of files scanned"*. The census arm
reads clear. The negative-control arm is `lib/research/corpus/readonly_proof.py` `negative_control()`: it copies the whole library
(~308 MB) to `Path(tempfile.gettempdir()) / ("amgt_corpus_ro_copy_" + stamp)`, denies writes on the copy with `icacls`, runs
`ingest.ingest` against it through `RetainedOnlyClient` (0 actual S3 puts), restores the ACL, and LEAVES the copy
(`left_for_operator_cleanup True`). `main()`'s `--code-census` arm makes `tempfile.mkdtemp(prefix="amgt_corpus_census_")`, plants
two positive-control files there, and LEAVES them too. The CTO ruled (round-13 analysis): *"The no-write bound admits one scratch
directory. The check creates it with tempfile.mkdtemp(), every write of the negative-control arm goes under it, and the check
asserts the directory is gone at exit. A write anywhere else still fails the bound."*

**RULED -- what you build:**
1. `negative_control()` makes ONE `tempfile.mkdtemp(prefix="amgt_corpus_")` directory; the library copy and every probe file go
   under it; in `finally`, after the ACL is restored, the directory is removed and the arm ASSERTS it is gone (prints
   `scratch_removed True`; a directory that survives is an error, never a `left_for_operator_cleanup` line). The copy-location
   guard (outside the library and the repository) stays.
2. The `--code-census` arm's planted directory is removed at exit the same way, after its positive controls are read.
3. `lib/research/corpus/tests/test_readonly_proof_bound.py` (new, offline, Windows): each arm, run against a small temp library (set
   `library.ENV_LIBRARY_ROOT`; stub the S3 client), leaves NO new `amgt_corpus*` entry in `tempfile.gettempdir()`, and a scratch
   directory that cannot be removed fails the arm. Keep `test_readonly_proof.py` / `test_readonly_proof_tristate.py` green (edit
   `test_readonly_proof.py` only where it pins the old leave-behind behaviour).
4. Run AC2 yourself: it drives the REAL negative-control arm over the whole library (~308 MB copy, a few minutes).

## 3. SURFACES

<paths>
lib/research/corpus/readonly_proof.py
lib/research/corpus/tests/test_readonly_proof_bound.py
lib/research/corpus/tests/test_readonly_proof.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-p-1.fwd9-inside-its-bound.md
</paths>

READ-ONLY: every other file in the repository, every S3 object, the research library on the synced drive. Scratch `.scratch/p1/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO vendor call. NO S3 write (the arm's client already refuses). NO write to the library. Temp writes only under the arm's own mkdtemp directory.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-p-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p1_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-p-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p1_AC2.sh</invocation><expect>p1 negative_control rc 0 ingest_rc 0 put_performed 0 temp_new_entries 0</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-p-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p1_AC3.sh</invocation><expect>p1 code_census rc 0 library_write_calls 0 temp_new_entries 0</expect></criterion>
</proof_of_spec>

- AC1 the built bound, offline; AC2 the real negative-control arm on the whole library inside the bound; AC3 the census arm inside the bound.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-p-1.fwd9-inside-its-bound.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: each AC line, the negative arm's printed `stored` / `existed` counts, and the suite count.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-13 analysis s.4 item 1 @`f1c482d24f` (msg 26603). Checks dry-run at the base `dbafd14c52`: p1_AC1 FAIL (no tests ran); p1_AC2 FAIL (bound_absent, not run); p1_AC3 FAIL (temp_new_entries 1).
The check refuses to run the 308 MB arm until negative_control() carries mkdtemp.
<risk>LOCAL</risk>
<status>complete</status>
<round>14</round>
<slot>~1</slot>
<fabric>site-z</fabric>
