# AMGT_CORPUS task order -- `CRPS-c-4` -- ROUND 1, FIRST CELL: the backlog -- a fresh folder census of the Research library, each folder resolved through the identity layer, three counts that sum to the folder count, one gold object per scan vintage; plus the package, the library-root module, the gold writer and the test poison every later cell uses

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-c-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=7 C3=12 C4=21 C5=334), 0 on any harvest, research or corpus surface; this cell opens no deploy.
comp-iam: RUN at L5 -- 214 roles on the DESIRED plane, none of them the credential this box writes with; BLIND to this box's own credential, so AC2's first conditional PUT measures it.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. This is the
FIRST order in your queue. After it drains you will be CONTINUED with the next order, so what you learn here carries.
- **Your first act** prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`,
  `.tools/`, `lib/research/identity/crosswalk.py`, `lib/research/harvest/store.py` and `lib/opal_naming.py` exist. If any
  is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~1;`.
- **NEVER RUN AN INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API.** S3 reads and writes to `opal-data-harvest` are the
  firm's own infrastructure and are allowed exactly as section 4 bounds them.
- **THE LIBRARY IS READ-ONLY TO YOU.** This cell LISTS it and never opens a file in it. No write, move, rename or delete
  under the library root, ever.

## 1. THE CELL, inlined in full -- `CRPS-c-4` (manifest row R4, outcome FWD-3)

**FWD-3, the outcome this cell serves, verbatim:** *"The backlog universe IS the library's folder list, resolved to
securities, with every unresolved folder shown. DONE WHEN EXERCISED -- the folder list is read fresh from the library
(never a transcribed list), each folder is resolved through the identity layer to a security key, and the output
carries three counts that sum to the folder count: resolved, unresolved-with-reason, and ambiguous-with-candidates."*

**THE LIBRARY.** The team's research library is the firm's SharePoint `Shared/Asset Management/Research/` library,
synced to this desktop by OneDrive. On this device it measured, at L5:
`C:\Users\Opal Bloomberg\OneDrive - Opal Capital\Shared - Documents\Asset Management\Research`, 93 name folders, 351
files (184 .pdf, 78 .xlsx, 71 .docx, 17 .png, 1 .html; 305.7 MB). **103 of the 351 are OneDrive cloud placeholders**
(`st_file_attributes & 0x400000`, RECALL_ON_DATA_ACCESS), which means that OPENING one downloads it. **This cell must
not open any file**, so it hydrates nothing: `os.stat` and `os.scandir` do not hydrate.

**THE IDENTITY LAYER, measured at L5** (read it; do not change it):
- `lib/research/identity/crosswalk.py` `harvester_key(folder, pilots)` gives the key the harvester persists for a
  source folder, and `load_pilots()` supplies `pilots`. `resolve(any_form)` returns the canonical identity for any known
  form. It returns `security_key` `None` on a miss, and a `reason` beginning `AMBIGUOUS:` naming the candidates on a
  collision.
- `crosswalk.resolve(<raw folder name>)` resolved **2 of 93**. `crosswalk.resolve(crosswalk.harvester_key(folder,
  pilots)[0])` gave **33 of 93** with `security_key` set (resolution `MEASURED`), **60** hits on records whose
  `security_key` is `None` (the universe carries them UNRESOLVED; the hit dict has NO `reason` key), and **0** ambiguous.
- **Use the layer's functions and nothing else** (`C-IDENTITY-VIA-THE-LAYER`: *"A folder resolves to a security
  through `AMGT_RESAPP`'s identity layer and its crosswalk, never by a local string match in this project. An ambiguous
  resolution returns its candidate list and is graded unresolved. This project adds no second identity mechanism."*).
  For an unresolved folder, the REASON is the layer's own `reason` when present. Otherwise it is the record's
  `source_row.bloomberg_ticker.status` and `evidence`, read with `crosswalk.record_for` or the resolve hit. Never write
  your own sentence in place of the layer's.

**RULED -- what you build (every file new; the package `lib/research/corpus/` does not exist at HEAD):**
1. **`lib/research/corpus/__init__.py`** -- a one-line docstring naming the package and the project.
2. **`lib/research/corpus/library.py`** -- the library root and a LISTING-ONLY census:
   - `library_root()` derives the root in this order, printing which source won: env `OPAL_RESEARCH_LIBRARY_ROOT`;
     then env `OneDriveCommercial` joined with `Shared - Documents/Asset Management/Research`; then `Path.home()` joined
     with `OneDrive - Opal Capital/Shared - Documents/Asset Management/Research`. **If the chosen path is not a
     directory, raise `LibraryAbsentError` whose message names EVERY path it looked for** (`C-LOCAL-AND-DEVICE-DERIVED`:
     *"a run on a device without the library refuses loudly with the path it looked for, and does not report an empty
     corpus"*). No path string is typed anywhere else.
   - `census(root)` returns one entry per file (folder, path relative to the root, extension, size, mtime UTC,
     `placeholder` bool from the attribute bit) using `os.scandir` and `os.stat` ONLY. Loose files at the root, if any,
     are reported as their own class, never dropped.
   - `python -m lib.research.corpus.library --census` prints `root <path>`, `root_source <which>`,
     `folders <n> files <n>`, one `ext <.x> <n>` line per extension, `placeholders <p> of <n>`, `loose_root_files <n>`,
     and a `partial_sync_signal <text>` line: what, if anything, this device exposes that separates a PARTIAL sync from a
     SMALL library. Measure it (for example, OneDrive's own sync-state attributes). If nothing on the listing plane
     separates them, say exactly that, and say what WOULD (a prior vintage's census from the store). That is the K1
     question the PRD owes an answer to.
3. **`lib/research/corpus/gold.py`** -- the ONE gold writer for this package (gold has no shared writer in the estate).
   `gold_put(table, partition, object_name, body_bytes, client=None)` addresses with `lib/opal_naming.py address("amgt",
   "harvest", "gold", table, partition, object=object_name)` and REFUSES unless the printed bucket is `opal-data-harvest`.
   It puts with `IfNoneMatch='*'` and metadata `document-sha256`. On a PreconditionFailed it HEADs the existing object:
   the same sha256 is a no-op (`existed=True, put_performed=False`), and a different sha256 raises `GoldImmutableError`.
   It never overwrites. Model it on `lib/research/harvest/store.py` `bronze_put` (read it) and return the same shaped
   result. `gold_get(uri)` reads one back.
4. **`lib/research/corpus/backlog.py`** -- the backlog:
   - `build(root, client=None)` lists folders FRESH (`library.census`), resolves each through the layer as above, and
     returns one record per folder: `folder`, `harvester_key`, `state` in `RESOLVED | UNRESOLVED | AMBIGUOUS`,
     `security_key` (or null), `reason` (for UNRESOLVED and AMBIGUOUS), `candidates` (for AMBIGUOUS), `files`, and
     `placeholders`. Plus totals, `crosswalk_loaded_from` (`crosswalk.loaded_from()`), `method_version`, and
     `scan_vintage` (UTC).
   - `python -m lib.research.corpus.backlog --write` builds it and prints ONE line per folder
     (`folder <name> | <state> | <security_key or -> | <reason or candidates>`), then
     `folders_read <N> = resolved <r> + unresolved <u> + ambiguous <a>`, then `sum_check OK` ONLY if r+u+a == N (else
     `sum_check FAIL` and rc 1). It writes the document with `gold_put("research-backlog", "date=<scan date UTC>",
     "<YYYYMMDDTHHMMSSZ>.json", ...)` (the object name from `lib/research/harvest/store.py` `form_a_object`: one object
     per scan vintage, never overwritten) and prints `written <s3 uri> put_performed <bool>`.
   - `python -m lib.research.corpus.backlog --read-latest` lists the partition's objects, reads the newest, and prints
     the same totals line and `sum_check` from the STORED document (the read-back).
5. **`lib/research/corpus/tests/__init__.py`** (empty) and **`lib/research/corpus/tests/conftest.py` -- THE POISON.** An
   `autouse` fixture that monkeypatches `boto3.client`, `boto3.resource`, `boto3.session.Session.client`,
   `subprocess.run`, `subprocess.Popen` and `socket.create_connection` to RAISE `RuntimeError("POISON: <site>")`.
   **Every later cell's tests run under it**, which is why it exists: *"a no-network PASS with no poison proven is an
   ABSENCE"* (the CVO's standard, adopted estate-wide). Tests pass stub clients explicitly.
6. **`lib/research/corpus/tests/test_library.py`** and **`lib/research/corpus/tests/test_backlog.py`**, offline, with
   these arms at least:
   - **POISON POSITIVE CONTROL:** each of the six poisoned sites RAISES when called inside a test. Assert the message.
   - **LIBRARY ABSENT:** with `OPAL_RESEARCH_LIBRARY_ROOT` pointing at a missing dir, `library_root()` raises
     `LibraryAbsentError` naming that path.
   - **LISTING DOES NOT OPEN:** census over a `tmp_path` tree with `builtins.open` monkeypatched to raise. The census
     completes.
   - **THREE STATES:** backlog over a stub crosswalk (monkeypatch `crosswalk.resolve`, `harvester_key`,
     `load_pilots`) producing one RESOLVED, one UNRESOLVED and one AMBIGUOUS folder gives counts 1/1/1 and
     `sum_check OK`. The AMBIGUOUS record carries its candidates.
   - **GOLD NEVER OVERWRITES:** `gold_put` over a stub client: the first put is performed; the same bytes again give
     existed True / put_performed False; different bytes raise `GoldImmutableError`.

**What this cell does NOT do:** it opens no library file, hydrates nothing, writes nothing under the library root, calls
no vendor, changes nothing under `lib/research/identity/` or `lib/research/harvest/`, and inducts nothing (that is
`CRPS-c-5`'s request and `AMGT_RESAPP`'s act).

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @3c09ae6ce8, chain A, cell 1 of 7 on this slot. Every later cell reads the modules you build
here and does not change them, so build them as the package's foundation, not as scratch.

## 3. SURFACES -- what you may read and write

<paths>
lib/research/corpus/__init__.py
lib/research/corpus/library.py
lib/research/corpus/gold.py
lib/research/corpus/backlog.py
lib/research/corpus/tests/__init__.py
lib/research/corpus/tests/conftest.py
lib/research/corpus/tests/test_library.py
lib/research/corpus/tests/test_backlog.py
org/missions/D5/AMGT/AMGT_CORPUS/cards/K1_library_on_this_device.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-4.backlog-folder-census-and-resolution.md
</paths>

**READ-ONLY references (read; never change):** `lib/research/identity/crosswalk.py`, `lib/research/harvest/store.py`,
`lib/opal_naming.py`, `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md`, and the library itself (listing only).
- Scratch goes in `<your worktree>/.scratch/c4/`. Never commit it.
- **Committing:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`,
  with the message file written by the Write tool, never a heredoc.

## 4. BOUNDS
- **Pure ASCII, LF line endings, Python 3.9-compatible** (the commit gate runs ruff at py39).
- **S3:** writes ONLY `opal-data-harvest` at `address()` output, ONLY through `gold_put`, NEVER overwriting. If the first
  real PUT is REFUSED (AccessDenied or anything else), that is a BLOCKING row with the error verbatim. Never retry under
  another key or another credential.
- **The K1 card** (`cards/K1_library_on_this_device.md`) answers the PRD's K1 row in plain words: the derived root and
  how it was derived; the folder and file counts at cell time against the scan's 93 and 351; the placeholder count; and
  what separates a partial sync from a small library, measured, or a statement that nothing on this plane does. Quote
  your own printed output as the evidence.
- **Surprise rows:** `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`. The file already holds seat rows
  `Z-S1..Z-S3`; append, never edit.
- **REFUSE a criterion you cannot satisfy as written**, and report the refusal with your measurement. Never repair,
  widen or re-route a criterion so that your own proof validates.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 120`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-c-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_library.py lib/research/corpus/tests/test_backlog.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-c-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.backlog --write 2>&1 | tail -6</invocation><expect>(?s)folders_read \d+ = resolved \d+ \+ unresolved \d+ \+ ambiguous \d+.*sum_check OK.*written s3://opal-data-harvest/amgt/harvest/gold/research-backlog/date=</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-c-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.backlog --read-latest 2>&1 | tail -4</invocation><expect>(?s)folders_read \d+ = resolved \d+ \+ unresolved \d+ \+ ambiguous \d+.*sum_check OK</expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-c-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.library --census 2>&1 | tail -14</invocation><expect>(?s)root_source \S+.*folders \d+ files \d+.*placeholders \d+ of \d+.*partial_sync_signal \S</expect></criterion>
  <criterion id="AC5" cell_refs="CRPS-c-4" judgment="true"/>
  <criterion id="AC6" cell_refs="CRPS-c-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/c4/hyg.py</invocation><expect>(?s)outside_allowed \[\].*changed_files \d+.*bad 0</expect></criterion>
</proof_of_spec>

- **AC5 (JUDGMENT, graded by the CVO, never by you):** the K1 card answers the PRD's K1 row: root, counts against the
  scan, placeholders, and the partial-sync question, each quoting a line of your own output. Record the card's path and
  its text as the output, with NO verdict.
- **`.scratch/c4/hyg.py`** (write it): diff the worktree against `git merge-base HEAD SITEZ` over `lib` and `org`; print
  `outside_allowed [...]` (every changed path NOT in section 3's `<paths>`), `changed_files <n>`, then for each changed
  `.py`: `compiles <bool> crlf <n> non_ascii <n>`, and finally `bad <n>` (the count of changed files failing compile,
  CRLF or ASCII).

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.**

## 6. WHEN YOU ARE DONE
1. Write the instance to
   `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-c-4.backlog-folder-census-and-resolution.proof_of_spec.json`.
   Each mechanical row carries `expect` copied from the criterion above. The judgment row is
   `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`.
2. Grade it with `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5,AC6 --governing-order <this order>`,
   which must return rc 0.
3. Flip `<status>` to `complete` ONLY if every mechanical criterion passes.
4. Commit with `--only` over your `<paths>` and the instance.
5. Report ONCE: the three counts and the `sum_check` line quoted, the gold URI, `put_performed`, the placeholder count,
   and your `partial_sync_signal` line.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**
1. **The 33 / 60 / 0 split is the L5 read, and the K2 ruling rests on it** (decomposition s.1a): FWD-3 is a printed
   denominator this round, with no human pass. The worker re-measures it; a different split is a finding, not an error.
2. **The listing-only rule is load-bearing twice.** It keeps FWD-9's library untouched, AND it keeps 103 placeholders
   from hydrating in a cell that has no use for their bytes. `CRPS-c-1` is the first cell allowed to open a file.
3. **`gold.py` and `conftest.py` are foundations.** Every gold cell writes through the former and every test runs
   under the latter. A defect in either is inherited by six cells, which is why each carries its own negative arm here.

<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
