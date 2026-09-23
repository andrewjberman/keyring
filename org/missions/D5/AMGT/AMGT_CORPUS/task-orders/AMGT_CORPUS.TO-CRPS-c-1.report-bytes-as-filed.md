# AMGT_CORPUS task order -- `CRPS-c-1` -- ROUND 1: every report in a resolved folder landed in bronze EXACTLY AS FILED through the ONE bronze writer, then re-opened from the store and matched byte for byte against the file on the drive, objects == files, both counted

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-c-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=7 C3=12 C4=21 C5=334), 0 on any harvest, research or corpus surface; this cell opens no deploy.
comp-iam: RUN at L5 -- 214 roles on the DESIRED plane, none the credential this box writes with; BLIND to this box's own credential, which this cell's first conditional PUT measures.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, continued from `CRPS-c-4` with its context. Work ONLY in your worktree.
- **First act:** print `git rev-parse --abbrev-ref HEAD`, and test that `lib/research/corpus/library.py`,
  `lib/research/corpus/backlog.py`, `lib/research/corpus/tests/conftest.py` and `lib/research/harvest/store.py` exist. If
  any is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~1;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API.**
- **THE LIBRARY IS READ-ONLY.** This is the first cell that OPENS a library file, and it opens every one with mode `"rb"`
  and NO other mode. No write, move, rename or delete under the library root.

## 1. THE CELL, inlined in full -- `CRPS-c-1` (manifest row R1, outcome FWD-1)

**FWD-1, verbatim:** *"Every report the team has written can be re-opened from our store exactly as it was filed. DONE
WHEN EXERCISED -- for every file the library's own folder list resolves to, the stored object is re-opened and matches
the file on the synced drive byte for byte, and the count of objects equals the count of files scanned, both printed."*

**`C-CORPUS-AS-RECEIVED`, verbatim:** *"Each stored report is the file's bytes as filed, with its own `sha256`, its
source path relative to the library root, its file modification time as the library reports it, and the scan vintage.
Extraction (text, headings, tables) is a SEPARATE object that names the bytes object it was derived from. Bronze is never
re-written: a changed file lands as a NEW object, and the prior one stays."*

**THE POPULATION (the decomposition's ruling 4):** the files of RESOLVED folders only, which is the DONE WHEN's own
phrase. A file in an UNRESOLVED or AMBIGUOUS folder is NOT stored under any guessed key. It is printed with its folder and
the backlog's reason. Take resolution from `CRPS-c-4`'s `backlog.build()` (a fresh read), never from a list you type.

**THE PLACEHOLDERS.** 103 of 351 files measured as OneDrive cloud placeholders at L5. Opening one hydrates it through
OneDrive (the firm's own Microsoft 365 tenant, not a vendor API). Record each file's placeholder state BEFORE its read,
using `library.census`. A read that fails to hydrate is printed with its error and counted in `read_failed`. It is never
skipped silently.

**RULED -- what you build:**
1. **`lib/research/corpus/ingest.py`:**
   - `ingest(root, backlog, client=None)`: for every file of every RESOLVED folder, read the bytes with
     `open(path, "rb")`, compute sha256, and land them with `lib/research/harvest/store.py`
     `bronze_put("amgt", "research-report", store.entity_partition("security_key", <key>), <object>, body,
     content_type=<by extension>, metadata=...)`.
   - **Object name:** `store.form_b_object(<report_id>, <safe file name>)`, where `report_id` is the first 16 hex of the
     sha256 (so a changed file is a NEW key and the prior object stays). The safe file name is the file's own name when
     it is ASCII and has no `/`; otherwise it is `<report_id><ext>`. The builder refuses non-ASCII objects, so never
     pass one.
   - **Metadata** (keys must match store's `^[a-z0-9][a-z0-9-]*$`; values ASCII): `source-relpath` (percent-encoded
     with `urllib.parse.quote`), `source-mtime` (ISO UTC), `scan-vintage`, `placeholder-at-read` (`true`/`false`),
     `security-key`.
   - `python -m lib.research.corpus.ingest --write` runs it. Print per file
     `<state> <security_key> <relpath> <put_performed|existed> <uri>`, then totals:
     `resolved_folders <n> files_in_resolved <n> stored <n> (put_performed <a> existed <b>) read_failed <n>`,
     `placeholders_before <p> hydrated_ok <h>`, `unresolved_files <n> in <m> folders` followed by one line per such file,
     and a run record written to your deliverables dir as `ingest_run.json`.
   - `python -m lib.research.corpus.ingest --verify` RE-OPENS every stored object (list the `research-report` prefix
     for each resolved partition, then GET each) and re-reads the matching file with `"rb"`. It compares bytes, prints
     each mismatch, then prints `objects <n> files <n> match <n> mismatch <n>` and `elapsed_s <t>`. **Use a thread pool
     (16 workers)**, because the population is about 300 MB and the criterion runs under a 120 s bound.
2. **`lib/research/corpus/tests/test_ingest.py`**, offline under the package poison, with a stub S3 client:
   - **SAME BYTES TWICE:** the second ingest is existed True, put_performed False.
   - **CHANGED BYTES:** a new report_id and a new key, with the prior object still present.
   - **NON-ASCII NAME:** a file named with a non-ASCII character is stored as `<report_id><ext>`, and its metadata
     carries the percent-encoded relpath.
   - **UNRESOLVED IS NOT STORED:** a file in an UNRESOLVED folder produces no put and is printed.
   - **READ MODE:** with `builtins.open` wrapped to record modes, every open of a library path is `"rb"`.
   - **VERIFY CAN FAIL:** `--verify`'s comparison over a stub where one stored object differs by one byte reports
     `mismatch 1`. A verifier that cannot report a mismatch proves nothing.

**What this cell does NOT do:** no extraction (that is `CRPS-c-2`), no write under the library root, no store for
unresolved folders, and no change to `lib/research/harvest/store.py` or to `CRPS-c-4`'s modules.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @3c09ae6ce8, chain A, cell 2 of 7 on this slot, after `CRPS-c-4` drained VALID.

## 3. SURFACES

<paths>
lib/research/corpus/ingest.py
lib/research/corpus/tests/test_ingest.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-1.report-bytes-as-filed.md
</paths>

**READ-ONLY:** `lib/research/corpus/library.py`, `backlog.py`, `gold.py`, `tests/conftest.py` (`CRPS-c-4`'s; never change
them), `lib/research/harvest/store.py`, `lib/research/identity/crosswalk.py`, `lib/opal_naming.py`, the library (`"rb"`
only). Scratch in `.scratch/c1/`, never committed. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **Pure ASCII, LF, Python 3.9-compatible.**
- **S3:** writes ONLY through `store.bronze_put`, which is never-overwrite by construction. A REFUSED first put
  (AccessDenied or anything else) is a BLOCKING row with the error verbatim. A `BronzeImmutableError` is a row too:
  it means a key already holds DIFFERENT bytes, which the content-hash key should make impossible.
- **Run `--write` as a BUILD STEP before the criteria** (it hydrates placeholders and may take minutes). The criteria are
  the fast read-backs.
- **Surprise rows:** `AMGT_CORPUS-Z-W1-S<k>`, next unused `k`, `disarm_owner` `2.0.0_SA_COO~X`.
- **REFUSE a criterion you cannot satisfy as written**, and report it with your measurement. Never repair or widen it.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 120`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-c-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_ingest.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-c-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.ingest --verify 2>&1 | tail -4</invocation><expect>objects (\d+) files \1 match \1 mismatch 0\b</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-c-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -c "import json,glob; p=glob.glob('org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/ingest_run.json')[0]; d=json.load(open(p)); print('files_in_resolved', d['files_in_resolved'], 'stored', d['stored'], 'read_failed', d['read_failed'], 'unresolved_files', d['unresolved_files'])"</invocation><expect>files_in_resolved (\d+) stored \1 read_failed 0 unresolved_files \d+</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-c-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC5" cell_refs="CRPS-c-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/c1/hyg.py</invocation><expect>(?s)outside_allowed \[\].*changed_files \d+.*bad 0</expect></criterion>
</proof_of_spec>

- `ingest_run.json` must carry the integer keys `files_in_resolved`, `stored`, `read_failed` and `unresolved_files`.
- `.scratch/c1/hyg.py`: the same shape as `CRPS-c-4`'s hygiene script, over THIS order's `<paths>` (diff against
  `git merge-base HEAD SITEZ`; print `outside_allowed [...]`, `changed_files <n>`, per-file `compiles/crlf/non_ascii`,
  `bad <n>`). Only this order's changes count, so diff from this order's starting commit if that is cleaner, and say
  which base you used.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-c-1.report-bytes-as-filed.proof_of_spec.json`, each row carrying its `expect`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5 --governing-order <this order>` returns rc 0.
3. Flip `<status>` to `complete` only if every criterion passes. Commit with `--only`, including `ingest_run.json`.
4. Report ONCE: the `objects/files/match/mismatch` line, the stored and put_performed counts, placeholders hydrated, and
   the unresolved-file count with its folder count.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the content-hash key is what makes "a changed file lands as a NEW object" true by construction and
not by care. The backreference in AC2's pattern (`objects (\d+) files \1 match \1`) is the equality FWD-1 names,
graded by the checker rather than read by eye.

<status>complete</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
