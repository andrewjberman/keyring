# AMGT_CORPUS task order -- `CRPS-c-2` -- ROUND 1: one extraction object per bronze report (text, headings, tables, sheet labels), read from the STORE, naming its bronze parent; answers K3 (are the PDF-only reports extractable to the same skeleton) and K4 (do the workbooks read without Excel)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-c-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=7 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 -- 214 roles on the DESIRED plane; BLIND to this box's credential, which CRPS-c-1's puts measured before this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, continued from `CRPS-c-1`. Work ONLY in your worktree.
- **First act:** print `git rev-parse --abbrev-ref HEAD`, and test that `lib/research/corpus/ingest.py` and
  `lib/research/harvest/store.py` exist. If either is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~1;`.
- **NEVER INSTALL.** python-docx, pdfplumber and xlrd are NOT installed, and you do not install them. Installed and
  measured at L5: openpyxl 3.1.5, PyMuPDF (`fitz`) 1.28.2, pypdf 6.16.2, lxml 6.1.1, pyarrow, boto3.
- **NEVER CALL A VENDOR API OR THE CLAUDE API. THIS CELL NEVER TOUCHES THE LIBRARY:** it reads bronze from the store.

## 1. THE CELL, inlined in full -- `CRPS-c-2` (manifest row R2; serves FWD-1, FWD-5, FWD-6, FWD-7)

**Manifest R2:** *"per-report extraction (text, headings, tables, sheet labels) | harvest / bronze /
research-report-extract, same partition."* **`C-CORPUS-AS-RECEIVED`:** *"Extraction (text, headings, tables) is a
SEPARATE object that names the bytes object it was derived from."*

**THE CORPUS, from the brief's scan** (`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922/RESEARCH_CORPUS_SCAN_20260922.md`,
read-only). Four report classes share one stable skeleton: research pack, earnings update, word-capped short form, and
stock-move update. The Word files carry headings. The PDF-only reports were read only to page 6 for headings, and their
text is NOT in the scan's term census. The workbooks carry sheets `Overview`, `CSC`, `Model`, `Model NEW VERSION` and
`Charts`, plus vendor cache sheets `_CIQHiddenCacheSheet` and `__FDSCACHE__`, which are NOT opened.

**K3 and K4, the PRD's questions, verbatim:** K3 *"the PDF-only reports -- 184 PDFs against 71 Word files: whether the
PDF text is extractable to the same skeleton, since the scan's term census read the Word files only"*. K4 *"the
workbooks -- whether the model sheets read without Excel on this box, and whether the 23 FactSet-coded variants type
onto the same mnemonics"*. This cell answers the first half of K4 (read without Excel; FactSet codes found). The typing
onto mnemonics is `CRPS-c-9`'s.

**RULED -- what you build:**
1. **`lib/research/corpus/extract.py`:**
   - `extract(bronze_uri, body, ext)` returns one JSON-serialisable document: `bronze_key`, `bronze_sha256`,
     `method_version`, `type`, `extractable` (bool), `reason` when not, and per type:
     - **DOCX:** `zipfile` + `lxml` over `word/document.xml`. Emit `paragraphs` (text, style name resolved through
       `word/styles.xml`, bold flag) and `headings`: a paragraph whose style is `Heading*` or `Title`, or a short
       (8 words or fewer) paragraph whose runs are all bold. Emit `tables` as rows of cell text.
     - **PDF:** PyMuPDF. Emit `pages` (text per page) and `headings`: short lines (8 words or fewer) whose span font size
       exceeds 1.15 x the page's median body size, or which are bold. **Do NOT use `find_tables()` for headings:** it is
       measured on this box to report a wrapped Word heading as a 2x2 table. `text_chars` is the total.
     - **XLSX:** openpyxl on the bytes (`io.BytesIO`). Load TWICE, once with `read_only=True, data_only=True` for
       values and once with `read_only=True, data_only=False` for formula strings. Emit `sheets` (names). Per sheet
       NOT named `_CIQHiddenCacheSheet` or `__FDSCACHE__`, emit `labels` (string cells, capped at 2000 per sheet with
       the cap printed) and `mnemonics`: quoted upper-case tokens `[A-Z][A-Z0-9_]{2,}` inside formula calls
       (`BDP`, `BDH`, `BDS`, `FDS`, `FDSC`, `FQL`, and any other call you MEASURE in the corpus, named in the output).
       Emit `factset_codes`: the subset matching `^F[FGE]_`.
     - **PNG, HTML, anything else:** `extractable` false, `reason` `not-extracted: <type>`.
   - `python -m lib.research.corpus.extract --write` lists every `research-report` object (per resolved partition),
     reads each from the store, extracts it, and lands the document through `store.bronze_put("amgt",
     "research-report-extract", <same partition>, "<report_id>/extract.json", <json bytes>,
     content_type="application/json")`. It prints per object `<type> <extractable> <uri>` and a totals line.
   - `python -m lib.research.corpus.extract --census` LISTS BOTH prefixes (no extraction, no GET beyond what the
     count needs) and prints `bronze_objects <n> extractions <n> missing <n>`. Then the K3 line, from the stored
     extractions: `k3 pdf <n> text_extractable <t> zero_text <z> median_chars <c> skeleton_heading_hits <h> of <n>`,
     where a skeleton hit is a PDF whose headings include at least one of the scan's section names
     (RECOMMENDATION, INVESTMENT THESIS, RISKS, Headline results, Guidance, Segment highlights, Geographic highlights;
     case-insensitive). Then the K4 line: `k4 xlsx <n> opened <o> failed <f> with_mnemonics <m> factset_coded <fc>`.
2. **`lib/research/corpus/tests/test_extract.py`**, offline, under the poison. Build tiny fixtures in code: a DOCX
   written with `zipfile` carrying one Heading1 and one bold short paragraph; a one-page PDF made with PyMuPDF, with one
   large-font line; an XLSX made with openpyxl, with a `BDP("X","PX_LAST")` formula and an `FF_SALES` label. Arms:
   - DOCX headings found, both routes (style and bold);
   - PDF heading found by size, and a body line NOT reported as a heading (the negative arm);
   - XLSX mnemonic `PX_LAST` found, `FF_SALES` in `factset_codes`, and a sheet named `__FDSCACHE__` NOT opened
     (its cells absent from the output);
   - PNG gives `extractable` false with its reason.

**What this cell does NOT do:** no typing, classing or period work (that is `CRPS-c-3`), no OCR, no library read, no
Claude call.

## 2. WHERE THIS CAME FROM
Round 1, decomposition v1.0 @3c09ae6ce8, chain A, cell 3 of 7 on this slot, after `CRPS-c-1` drained VALID. Its
extractions feed `CRPS-c-3`, `CRPS-c-6`, `CRPS-c-7`, `CRPS-c-8` and `CRPS-c-9`, so the document shape you choose is
their input. Write it down at the top of `extract.py`.

## 3. SURFACES

<paths>
lib/research/corpus/extract.py
lib/research/corpus/tests/test_extract.py
org/missions/D5/AMGT/AMGT_CORPUS/cards/K3_K4_pdf_and_workbook_extractability.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-c-2.per-report-extraction.md
</paths>

**READ-ONLY:** every earlier `lib/research/corpus/` module and `tests/conftest.py`, `lib/research/harvest/store.py`,
`lib/opal_naming.py`, and the scan file above. Scratch in `.scratch/c2/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **Pure ASCII source, LF, Python 3.9-compatible.** Extracted TEXT may be any Unicode: store it in the JSON with
  `ensure_ascii=True`.
- **S3:** writes ONLY through `store.bronze_put`, never overwriting. A failure to extract one object is recorded in its
  document (`extractable` false, `reason` the exception class and message) and counted. It never aborts the run.
- **Run `--write` as a BUILD STEP before the criteria.**
- **The K3/K4 card** answers both questions in plain words with your printed lines as evidence, and names what it could
  NOT measure.
- **Surprise rows:** `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`. **REFUSE a criterion you cannot satisfy as
  written**, and report it with your measurement.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 120`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-c-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_extract.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-c-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.extract --census 2>&1 | tail -4</invocation><expect>(?s)bronze_objects (\d+) extractions \1 missing 0\b.*k3 pdf \d+ text_extractable \d+ zero_text \d+ median_chars \d+ skeleton_heading_hits \d+ of \d+.*k4 xlsx \d+ opened \d+ failed \d+ with_mnemonics \d+ factset_coded \d+</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-c-2" judgment="true"/>
  <criterion id="AC4" cell_refs="CRPS-c-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC5" cell_refs="CRPS-c-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/c2/hyg.py</invocation><expect>(?s)outside_allowed \[\].*changed_files \d+.*bad 0</expect></criterion>
</proof_of_spec>

- **AC3 (JUDGMENT, the CVO's):** the K3/K4 card answers both PRD questions from your printed lines. Record its path and
  text, with NO verdict.
- `.scratch/c2/hyg.py`: the same shape as before, over this order's `<paths>`.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-c-2.per-report-extraction.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4,AC5 --governing-order <this order>` returns rc 0.
3. Flip to `complete` only if every mechanical criterion passes. Commit with `--only`.
4. Report ONCE: the census line, the K3 and K4 lines quoted, and the document shape you chose (its top-level keys).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** reading from the STORE rather than the library is what keeps the library touched exactly once per
ingest, and it makes every downstream derivation reproducible from `{key, sha256}` inputs (`C-INPUT-HASHED`). The
`find_tables` prohibition is an estate lesson (PyMuPDF reports a wrapped Word heading as a 2x2 table), inlined because a
worker has no memory to read it from.

<status>pending</status>
<round>1</round>
<slot>~1</slot>
<fabric>site-z</fabric>
