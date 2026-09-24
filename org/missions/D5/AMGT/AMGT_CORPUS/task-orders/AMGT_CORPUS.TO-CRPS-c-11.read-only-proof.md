# AMGT_CORPUS task order -- `CRPS-c-11` -- ROUND 1, LAST CELL: the read-only proof -- the ingestion run against a WRITE-DENIED copy of the library completes, and an AST census of every line of this project's code prints zero write, move, delete or open-for-write calls reaching the library root, with its denominator and a planted positive control

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-c-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=7 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: DECLARED-NOT-APPLICABLE -- the negative control's re-ingest meets bronze objects that already exist, and the never-overwrite writer makes zero puts; no grant is exercised beyond CRPS-c-1's.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, continued from `CRPS-c-10`. Work ONLY in your worktree.
- **First act:** print `git rev-parse --abbrev-ref HEAD`, `ls lib/research/corpus/`, and test that `ingest.py` and
  `library.py` exist there. If either is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~1;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. THE REAL LIBRARY IS READ-ONLY**, and this cell reads it
  only to COPY it. **NEVER DELETE ANYTHING, anywhere, recursively or otherwise, and that includes the copy you make.**
  Recursive deletion is an operator act on this estate.

## 1. THE CELL, inlined in full -- `CRPS-c-11` (manifest row R11, outcome FWD-9)

**FWD-9, verbatim:** *"Nothing this project runs can write to, move or delete anything in the team's library. DONE WHEN
EXERCISED -- a deliberate negative control runs the ingestion against a read-only copy of the library and completes; and
a census of the project's own code prints zero write, move, delete or open-for-write calls against any path under the
library root, with the denominator of files scanned. ACCEPT: Adam's team's folder is exactly as they left it, and we can
prove it rather than assert it."*

**`C-CORPUS-READ-ONLY`:** *"The library is read-only to this estate. Every read opens the file for reading only; no code
in this project may write, move, rename or delete under the library root, and no run may depend on the library being
writable. The library path is resolved, never hardcoded."*

**RULED -- what you build:**
1. **`lib/research/corpus/readonly_proof.py`:**
   - **`--negative-control`:**
     (a) copy the library (`library.library_root()`) with `shutil.copytree` to a NEW directory OUTSIDE the repository,
         `<tempfile.gettempdir()>/amgt_corpus_ro_copy_<UTC stamp>`. Copying reads the source; it writes only the
         destination.
     (b) DENY WRITES on the copy for the current user: `icacls <copy> /deny "<USERDOMAIN>\<USERNAME>:(OI)(CI)(W,D,DC,WD,AD,WEA,WA)" /T`,
         run from Python with an argument LIST (never through the Git-Bash shell, which rewrites `/deny`-style
         arguments into paths). Print the rc.
     (c) POSITIVE CONTROL that the denial is real: try to create a file in the copy's root, and try to open one copied
         file for append. Print `write_denied_probe <ExceptionClass> <ExceptionClass>`. Both must raise.
     (d) run `CRPS-c-1`'s ingestion (`ingest.ingest`) with `OPAL_RESEARCH_LIBRARY_ROOT` set to the copy, in-process, and
         print `ingest_rc <0|1> stored <n> put_performed <a> existed <b> read_failed <r>`. Every object already exists,
         so `put_performed` is expected 0 and nothing is written anywhere.
     (e) REMOVE the deny entries (`icacls <copy> /remove:d "<USERDOMAIN>\<USERNAME>" /T`) so an operator can clean the
         copy up later. Print `copy_root <path> left_for_operator_cleanup True` and its size in MB. **Do not delete it.**
   - **`--code-census`:** parse EVERY `.py` under `lib/research/corpus/` (tests included) with `ast`, and flag each call
     that WRITES, MOVES or DELETES a filesystem path:
     - `open`/`io.open`/`Path.open` with a mode containing `w`, `a`, `x` or `+`;
     - `Path.write_text/write_bytes/unlink/rename/replace/rmdir/mkdir/touch/chmod`;
     - `os.remove/unlink/rename/replace/rmdir/removedirs/makedirs/mkdir/chmod`;
     - `shutil.move/copy/copy2/copyfile/copytree/rmtree`.
     A flagged call COUNTS against the library when its target expression references `library_root`, `LIBRARY`, the
     root variable, or a value derived from them in the same function (a simple def-use walk is enough), OR when it sits
     in a non-test module and its target cannot be shown to be something else. `readonly_proof.py`'s own
     `copytree`/`icacls` DESTINATION is the copy; its SOURCE is only ever read, and the census says so line by line.
     Print `files_scanned <n>`, `write_like_calls <n>`, one line per flagged call (`<file>:<line> <call> <target>
     reaches_library <bool>`), `library_write_calls <k>`, and the POSITIVE CONTROL:
     `positive_control flagged <1|0>`, obtained by census of a planted temp file (outside the repo) containing
     `open(library_root() / "x", "w")`. **A census that cannot flag the plant proves nothing.**
2. **`lib/research/corpus/tests/test_readonly_proof.py`**, offline, under the package poison:
   - the census flags the planted write, and does NOT flag an `open(p, "rb")`;
   - the census flags `shutil.move(src_under_root, x)` as reaching the library;
   - a write to `tmp_path` in a test module is counted in `write_like_calls` and NOT in `library_write_calls`.

**What this cell does NOT do:** no write, move or delete under the real library, no deletion of the copy, no S3 write
beyond what `ingest` would do (and it does nothing, because every object exists).

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @3c09ae6ce8, chain A, the LAST cell on this slot, because its census must see the whole
package.

## 3. SURFACES

<paths>
lib/research/corpus/readonly_proof.py
lib/research/corpus/tests/test_readonly_proof.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-11.read-only-proof.md
</paths>

**READ-ONLY:** every other `lib/research/corpus/` file, `lib/research/harvest/store.py`, and the real library (`"rb"` and
the copy's read only). Scratch in `.scratch/c11/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **Pure ASCII source, LF, Python 3.9-compatible.**
- **Run `--negative-control` as a BUILD STEP** (copying about 300 MB may take minutes), saving its output to
  `negative_control.log` in your deliverables dir. AC2 reads that log AND re-checks the copy's denial live.
- **If the icacls denial cannot be applied, or the probe does NOT raise,** that is a BLOCKING row. Never proceed to (d)
  on an unproven denial.
- **Surprise rows:** `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`. **REFUSE a criterion you cannot satisfy as
  written**, and report it with your measurement.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 120`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-c-11"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_readonly_proof.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-c-11"><invocation>cd "$(git rev-parse --show-toplevel)" && tail -8 org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/evidence/negative_control_root_bound.log</invocation><expect>(?s)write_denied_probe \w*(Permission|Access)\w* \w*(Permission|Access)\w*.*ingest_rc 0 stored \d+ put_performed 0 existed \d+ read_failed 0.*copy_root \S.* left_for_operator_cleanup True</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-c-11"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.readonly_proof --code-census 2>&1 | tail -40</invocation><expect>(?s)files_scanned [1-9]\d*.*library_write_calls 0\b.*positive_control flagged 1\b</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-c-11"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC5" cell_refs="CRPS-c-11" judgment="true"/>
  <criterion id="AC6" cell_refs="CRPS-c-11"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/c11/hyg.py</invocation><expect>(?s)outside_allowed \[\].*changed_files \d+.*bad 0</expect></criterion>
</proof_of_spec>

- **AC5 (JUDGMENT, the CVO's):** AC3's full flagged-call list with each `reaches_library` decision. Is every write-like
  call in the package correctly judged, and does the census cover every file `lib/research/corpus/` holds at HEAD?
  Record the list and the `ls` of the package, with NO verdict.
- `.scratch/c11/hyg.py`: the same shape as before, over this order's `<paths>`.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/AMGT_CORPUS.TO-CRPS-c-11.read-only-proof.proof_of_spec.json` (ISSUER AMENDMENT below: the executor's own deliverables home).
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6 --governing-order <this order>` returns rc 0.
3. Flip to `complete` only if every mechanical criterion passes. Commit with `--only`, including `negative_control.log`.
4. Report ONCE: the probe line, the ingest line, the census totals, and the copy's path and size, so the issuer can
   hand its cleanup to the operator.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER AMENDMENT 2026-09-24 ~05:0xZ (2.0.0_SA_COO~X, executing this cell personally per G00 @8d33ad1cc5; the worker
slot was never spawned):** AC3's invocation window widened `tail -30` -> `tail -40`; the `<expect>` is unchanged. The code
census prints 32 lines at HEAD (the package grew after this order was cut at 40107c6f48), so the literal `tail -30` dropped
`files_scanned` and the regex, anchored on it, could not match while every graded value passed. Row AMGT_CORPUS-Z-S10
carries the measurement. AC2's path amended from `deliverables/0.9.0_WK_AMGT_CORPUS~1/negative_control.log` to
`deliverables/2.0.0_SA_COO~X/evidence/negative_control_root_bound.log` (tracked @d382f2a30e, sha256 7e39e925439b..., the run C01
graded PASS, CTO msg 24841) and the section-6 instance home to `deliverables/2.0.0_SA_COO~X/`: the owned-paths hook refuses this
seat a write under the never-spawned worker's folder (TREE_DELIVERABLES, owner in the path), and the complete-flip gate searches
every `deliverables/*/` folder for the instance. Both `<expect>` regexes are unchanged.

**ISSUER NOTES:** the copy is left in place deliberately, because recursive deletion is an operator act under the
Agent Autonomy clause. The issuer names its path to the operator at the drain. The icacls argument list goes through
Python because Git Bash's MSYS layer rewrites slash-arguments into paths, which would make the denial a silent no-op.

<status>complete</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
