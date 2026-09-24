# AMGT_CORPUS task order -- `CRPS-d-4` -- ROUND 2, LAST CELL ON THIS SLOT: the coverage census -- every folder in the Research list dispositioned, the three counts summing to the folder count, the eleven that can never carry prose NAMED, and any folder answerable by name

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-d-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=5 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 (round-1 read, 214 roles on the DESIRED plane, not re-run this cut); BLIND to this box's credential; this cell's put of a new backlog scan vintage measures the prefix it already wrote in round 1.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, continued from `CRPS-d-3`. Work ONLY in your worktree. **Your issuer has, before
continuing you, merged the drained `CRPS-d-5` branch into yours and run the scripted production sequence for the newly
inducted names** (the record is in your worktree's git log; read it). Work from the store as it is NOW.
- **First act:** print `git rev-parse --abbrev-ref HEAD`, and test that `lib/research/corpus/dossier.py` defines
  `read_dossier` and that `lib/research/corpus/backlog.py` exists. If either is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~1;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. THE LIBRARY IS LISTED ONLY** (`library.list_folders`,
  `library.census`); nothing under it is opened for writing, moved or deleted.

## 1. THE CELL, inlined in full -- `CRPS-d-4` (manifest row R14, NEW; serves FWD-14 and FWD-19's census)

**FWD-19, verbatim:** *"EVERY SECURITY IN THE ASSET MANAGEMENT RESEARCH FOLDER -- all 93 -- is dispositioned through the
opal-data-harvest channels. DONE WHEN EXERCISED -- a census prints, for all 93, dossier-served / resolved-but-no-prose /
unresolved-with-reason, and THE THREE SUM TO 93; ... and the 11 that can never carry prose (10 workbook-only, 1 empty) are
NAMED with their reason rather than dropped from the denominator. ACCEPT Andrew names any of the 93 and gets its corpus
layers or the reason it has none. 93 of 93 DISPOSITIONED -- never 93 of 93 populated."*
**FWD-14, verbatim:** *"Any folder in the Research list returns its dossier or the printed reason there is none. DONE WHEN
EXERCISED -- for a named folder the read returns a dossier or a reason; and the three counts (resolved / ambiguous /
empty-or-workbook-only) SUM TO THE FOLDER COUNT every time."*
**`C-BACKFILL-DENOMINATOR-IS-THE-RESEARCH-FOLDER`, verbatim:** *"EVERY FWD-19 POPULATION CLAIM IS A SUBTRACTION FROM A FRESH
READ OF THE ASSET MANAGEMENT RESEARCH FOLDER, WITH THE DENOMINATOR PRINTED."* **`C-FOLDER-LIST-IS-THE-DENOMINATOR`** and
**`C-CORPUS-READ-ONLY`** bind.

**RULED -- what you build in `lib/research/corpus/backlog.py`:**
- **`--coverage`:** the folder list read FRESH from the library (`library.list_folders(root)`, never a transcribed list),
  the crosswalk resolution per folder exactly as `build()` does it, and for EVERY folder exactly ONE disposition:
  - `dossier-served` -- the folder resolves to a security key AND `dossier.read_dossier(key)` returns an object (record
    its URI and `content_sha256`);
  - `resolved-but-no-prose` -- resolves, but no dossier can exist, with the reason MEASURED from the folder's own files
    (`workbook-only` = every file is xlsx; `empty` = zero files; `pdf-unreadable-to-skeleton` = prose files exist but the
    v2 extraction of the most recent class A carries no INVESTMENT THESIS lead; `no-class-a-or-b-report` = prose exists but
    is neither class); a resolved folder with a readable pack and NO dossier object is `resolved-but-no-prose` with reason
    `dossier not yet built` -- printed, never hidden;
  - `unresolved-with-reason` -- the crosswalk's own state and reason (`ambiguous` naming the candidates, e.g. America Movil
    AXMB/AMXB; `no-evidence`; `refused`).
  Print, FIRST and LAST: `folders_read F dossier_served S resolved_no_prose P unresolved_with_reason U sum F` (the
  arithmetic is asserted in code and the run FAILS if it does not hold), then `never_prose_named K` followed by one line
  per never-prose folder: `<folder> <reason>`. Write the census as a NEW scan vintage at `research-backlog` through
  `gold.gold_put` (object name the scan vintage stamp, as `write()` does), carrying `records[]` with the per-folder
  disposition beside round 1's fields.
- **`--folder "<name>"`** and **`--folder-by-index N`** (the N-th folder of the fresh sorted list): print `folder <name>`,
  `disposition <one of the three>`, then `dossier_uri <s3 uri> content_sha256 <hex>` or `reason <text>`. Never a silence;
  an unknown folder name prints `folder <name> disposition unknown reason not in the Research folder list (F folders)`.

**What this cell does NOT do:** no induction, no ingestion, no dossier build (those ran before you were continued); no
edit to `dossier.py`, `library.py` or the crosswalk; no library write.

## 2. WHERE THIS CAME FROM
Round 2, decomposition v2.0, chain A cell 4 of 4 and chain B's sink, after `CRPS-d-3` AND `CRPS-d-5` drained VALID and
the issuer's drain sequence ran.

## 3. SURFACES

<paths>
lib/research/corpus/backlog.py
lib/research/corpus/tests/test_backlog.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-d-4.coverage-census-93-of-93.md
</paths>

**READ-ONLY:** every other `lib/research/corpus/` module, `lib/research/identity/crosswalk.py`,
`lib/research/harvest/store.py`. Scratch in `.scratch/d4/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **NO S3 DELETE OF ANY KIND.** **Pure ASCII source, LF, Python 3.9-compatible.**
- **S3:** the one write is the new scan vintage through `gold_put`, never overwriting.
- **Tests:** offline under the poison, with a fake library root built in `tmp_path` (folders of each shape: workbook-only,
  empty, prose with a dossier stub, prose without one, an unresolved name) and `dossier.read_dossier` faked; assert the
  sum, the eleven-style naming, and the by-name and unknown-name answers.
- **Surprise rows:** `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`. **REFUSE a criterion you cannot satisfy as
  written**, and report it with your measurement -- a sum that does not close is a finding about the crosswalk, and it is
  printed, not forced.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 600`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-d-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_backlog.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-d-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.backlog --coverage 2>&1 | tail -30</invocation><expect>(?s)folders_read ([1-9]\d*) dossier_served \d+ resolved_no_prose \d+ unresolved_with_reason \d+ sum \1\b.*never_prose_named [1-9]\d*</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-d-4"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.backlog --folder-by-index 0 2>&1 | tail -4</invocation><expect>(?s)folder \S.*disposition (dossier-served|resolved-but-no-prose|unresolved-with-reason).*(dossier_uri s3://opal-data-harvest/amgt/harvest/gold/research-dossier/|reason \S)</expect></criterion>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe against the real library list and the real store, with the sum asserted
  (FWD-19's own denominator); AC3 FWD-14's by-name answer on a deterministic pick (reason: the outcome is "never a silence",
  which only a real folder shows).

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-d-4.coverage-census-93-of-93.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` returns rc 0.
3. Flip `<status>` to `complete` only if every criterion passes. Commit via safe-commit with the pathspec of exactly the
   files you changed plus the instance.
4. Report ONCE: the AC2 totals line, the never-prose list, the scan vintage's S3 URI, and AC3's folder and disposition.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** this cell is continued only AFTER the fire, the re-ingest and the production sequence (decomposition
s.5, drain duties 1-2), because a census before them would report the run order as a fact about the world. The grade is
DISPOSITIONED, never populated; the never-prose list is the part a naive "N of 93" would hide.

<status>complete</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
