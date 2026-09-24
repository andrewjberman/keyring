# AMGT_CORPUS task order -- `CRPS-d-1` -- ROUND 2, FIRST CELL ON THIS SLOT: extraction method 2 -- the inline-lead section rule and the PFOE name set; v2 objects land BESIDE v1, never over it; the docx path is the control

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-d-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=5 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 (round-1 read, 214 roles on the DESIRED plane, not re-run this cut); BLIND to this box's credential; this cell's first v2 bronze put measures the extract prefix.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 2. Work ONLY in your worktree (its absolute path is in your prompt).
- **First act:** print `git rev-parse --abbrev-ref HEAD`, and test that `lib/research/corpus/extract.py`,
  `lib/research/corpus/tests/test_extract.py` and `lib/research/harvest/store.py` exist. If any is absent, STOP with a
  BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~1;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. NEVER TOUCH THE LIBRARY** (every input is a stored bronze
  object read back through `store`; nothing here opens a path under the OneDrive research library).

## 1. THE CELL, inlined in full -- `CRPS-d-1` (manifest row R2 enriched: method 2; serves FWD-16 and is upstream of FWD-10..13)

**FWD-16, verbatim:** *"A PDF-only pack gets the same fold, or the tab states which shape the PDF could not be read to and
why. DONE WHEN EXERCISED -- a PDF-only name renders pillars, management and cases from the PDF pack; and the docx path is
KEPT AS THE CONTROL and still recovers what it recovered before. SOURCE brief O7 :91 AT ITS AMENDED BYTES. Extractability
is MEASURED (99 of 99 on the control) -- this is a READER change and NO CELL RE-MEASURES IT."*

**THE MEASURED CAUSE (4.0.0_SA_CRO~Y, `org/tier1_exec/4.0.0_SA_CRO~Y/deliverables/PDF_EXTRACTABILITY_20260924/SUMMARY.md`
@`d64d83a5d2`, read-only):** `extract.py`'s K3 heuristic sees a heading only as a STANDALONE large/bold short line
(`_extract_pdf`, word count <= 8, size > 1.15 x median or bold). The PFOE author's packs label sections with INLINE BOLD
LEADS on body lines -- `RECOMMENDATION: <text>`, `COMPANY DESCRIPTION: <text>`, `INVESTMENT THESIS: <one-sentence summary>`,
`RISKS AND CONSIDERATIONS:` (the team also spells it `RISKS AND CONSDIERATIONS:`), `Ownership:`, `Management and capital
allocation:`, `Special items:`, and in updates `Headline results`, `Positives`, `Negatives`, `Segment highlights`,
`Headwinds and risks`, `Guidance`, `Changes in analyst sentiment`, `Why we own`. K3 saw none of them, which is why the
scan counted 33 of 52 and called the PFOE packs "PDF-only unknowns". Three rules, each measured against a control of 56
same-stem docx+pdf pairs (17 FULL of 19, 99 of 99 pillars recovered):
1. **A section opens on a standalone heading OR on a line whose LEADING BOLD SPANS, colon-trimmed and upper-cased, are a
   known section name.**
2. **A known section name closes a block whatever punctuation follows it** (the trailing colon is the team's); **`Valuation`
   is a PILLAR lead, never a section name.**
3. **A line ending in ':' whose text equals its bold prefix is a lead with its body below** (the PFOE pillar shape, CDNS's
   second pillar); the docx regex's 80-char lead cap is NOT a limit (a 140-char variant gave identical counts).

**RULED -- what you build in `lib/research/corpus/extract.py`:**
- `METHOD_VERSION_2 = "amgt-corpus-extract/2"`. `extract_v2(bronze_uri, body, ext)` returns v1's document shape PLUS, for PDF:
  `lines` -- every line across pages as `{text, page, size, bold_all, bold_first, lead_prefix, n_spans}` (`lead_prefix` =
  the concatenated LEADING bold spans' text, stripped; spans with only whitespace are transparent), and `section_leads` --
  `[{name, page, line_index, inline_remainder}]`, one per line that OPENS a section under rules 1-2. For DOCX: v2's
  `paragraphs`, `headings`, `tables` are BYTE-EQUAL to v1's (THE CONTROL), plus `section_leads` = each paragraph whose
  colon-trimmed upper-cased text is a section name (`{name, paragraph_index, inline_remainder}`). XLSX: unchanged shape.
- **THE SECTION NAME SET, in the module as data** (a frozenset of upper-cased names): the scan's names --
  `INVESTMENT THESIS`, `RISKS AND CONSIDERATIONS`, `RISKS AND CONSDIERATIONS`, `RISKS`, `KEY RISKS AND CONSIDERATIONS`,
  `KEY RISKS AND CONSDIERATIONS`, `KEY RISKS`, `HEADWINDS AND RISKS`, `MANAGEMENT/BOARD`, `MANAGEMENT / BOARD`,
  `MANAGEMENT`, `MANAGEMENT-BOARD`, `MANAGEMENT AND CAPITAL ALLOCATION`, `RECOMMENDATION`, `UPSIDE CASE`, `BASE CASE`,
  `DOWNSIDE CASE`, `COMMON STOCK COMPARISON`, `FINANCIAL SUMMARY`, `HEADLINE RESULTS`, `HEADLINE NUMBERS`, `GUIDANCE`,
  `SEGMENT HIGHLIGHTS`, `GEOGRAPHIC HIGHLIGHTS`, `PERFORMANCE VS FUND` -- plus the PFOE set: `COMPANY DESCRIPTION`,
  `LONG-TERM GROWTH ALGORITHM AND EXPECTED RETURN`, `LONG-TERM GROWTH ALGORITHM`, `OWNERSHIP`, `SPECIAL ITEMS`,
  `WHY WE OWN`, `POSITIVES`, `NEGATIVES`, `OTHER POSITIVES`, `OTHER NEGATIVES`, `CHANGES IN ANALYST SENTIMENT`,
  `INVESTMENT CONSIDERATIONS`, `OPPOSING VIEW`, `COMPANY OVERVIEW`, `SEGMENTS`, `BROKER COMMENTARY`, `TRADING HISTORY`,
  `EARNINGS ESTIMATE PROGRESSION`, `HISTORICAL VALUATION`, `PRICE CHART`. `VALUATION` is NOT in the set.
  Normalisation for the match: collapse whitespace, strip, strip a trailing ':', upper-case; a name followed by a
  number (`INVESTMENT THESIS 250`) matches on its alphabetic prefix.
- **`--run-v2`:** for EVERY bronze `research-report` object in the store (list, then read back through `store` -- the same
  walk `--run` does), compute v2 and land it BESIDE v1 through the ONE bronze writer at object name
  `<report_id>/extract.v2.json` in the SAME `research-report-extract` partition (conditional put; the same bytes on a
  second run are `existed`, a different byte at an existing v2 key RAISES -- bump `METHOD_VERSION_2` and the object name
  together if that ever happens; never delete). Print, at the START and at the END: `bronze_reports N v2_stored S
  put_performed P existed E read_failed R`, `docx_control identical D of D` (D = every docx report; identical = v2's
  `paragraphs`/`headings`/`tables` equal v1's stored document's), and `section_leads_pdf_files_with_any M of T` (T = every
  PDF report). A read failure is printed with its key, never skipped silently.
- **`--census-leads`:** read-only over the stored v2 objects: per PDF report the count of section leads and the names
  found; totals `pdf_files T with_inline_leads M with_standalone_only S with_none Z` (M + S + Z = T), printed first and last.
- Port the CRO's rules from its instrument (`measure_pdf_extractability.py` @`6ae4cb0c93`, `pdf_lines`, `section_name_of`,
  `is_section_heading`) by REWRITING them in this module; do not import a deliverables script.

**What this cell does NOT do:** it does not rewrite or delete any v1 object; it does not touch silver (R3) or any gold
table; it does not change `typed.py`, `continuation.py` or any reader -- `CRPS-d-2` resolves v2 by key substitution.

## 2. WHERE THIS CAME FROM
Round 2, decomposition v2.0 (`AMGT_CORPUS_DECOMP.md`, the L5 commit), chain A, cell 1 of 4 on this slot. `CRPS-d-2`
(continuation's PDF branch) and `CRPS-d-3` (the dossier) read what this cell writes.

## 3. SURFACES

<paths>
lib/research/corpus/extract.py
lib/research/corpus/tests/test_extract.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-d-1.extraction-method-2-inline-leads.md
</paths>

**READ-ONLY:** every other `lib/research/corpus/` module, `lib/research/harvest/store.py`, `lib/opal_naming.py`, and
`org/tier1_exec/4.0.0_SA_CRO~Y/deliverables/PDF_EXTRACTABILITY_20260924/` (SUMMARY.md, per_file.json, the instrument).
Scratch in `.scratch/d1/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **NO S3 DELETE OF ANY KIND** (row `AMGT_CORPUS-Z-S4`): a wrong object is superseded by a NEW key, never deleted.
- **Pure ASCII source, LF, Python 3.9-compatible.** `ensure_ascii=True` on every stored document.
- **S3:** writes ONLY through `store.bronze_put`, ONLY at the builder's address, NEVER overwriting. **Run `--run-v2` as a
  BUILD STEP** (123 reports at the cut; minutes). A refused PUT is a BLOCKING row, never a hand-typed key.
- **Tests:** offline under `tests/conftest.py`'s poison; PDF fixtures are BUILT in the test (PyMuPDF can write a small PDF
  with bold spans) -- never a library file, never a bronze read.
- **Surprise rows:** `AMGT_CORPUS-Z-W1-S<k>` (continue the numbering after the highest existing W1 row), `disarm_owner`
  `2.0.0_SA_COO~X`. **REFUSE a criterion you cannot satisfy as written**, and report it with your measurement.
- Every census prints its totals FIRST and LAST, so a `tail` window never drops them.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 600`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-d-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_extract.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-d-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.extract --run-v2 2>&1 | tail -6</invocation><expect>(?s)bronze_reports [1-9]\d* v2_stored \d+ put_performed \d+ existed \d+ read_failed 0.*docx_control identical (\d+) of \1\b.*section_leads_pdf_files_with_any [1-9]\d* of [1-9]\d*</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-d-1"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.extract --census-leads 2>&1 | tail -3</invocation><expect>pdf_files [1-9]\d* with_inline_leads [1-9]\d* with_standalone_only \d+ with_none \d+</expect></criterion>
</proof_of_spec>

- AC1 is the built behaviour (rules 1-3 on built fixtures: an inline `RECOMMENDATION: text` line opens a section; a
  `RISKS AND CONSDIERATIONS:` line closes the thesis block; `Valuation:` does not; a docx document's v2 paragraphs equal v1's).
- AC2 is the seam probe against the REAL neighbour, the store: every retained report re-read, v2 landed beside v1, the docx
  control identical for every docx, and at least one PDF carrying an inline lead.
- AC3 (the one further criterion; reason: FWD-16's cause IS the inline lead, and a census reading zero would mean the rule
  is blind on the real corpus even if the fixtures pass).

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-d-1.extraction-method-2-inline-leads.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` returns rc 0.
3. Flip `<status>` to `complete` only if every criterion passes. Commit via safe-commit with the pathspec of exactly the
   files you changed plus the instance.
4. Report ONCE: the AC2 totals line, the docx_control line, the AC3 line, and the count of v2 objects written vs existed.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** v2 lands beside v1 because `store.bronze_put` refuses a changed byte at an existing key and R3's silver
rows point at v1 keys; d-2 resolves v2 by key substitution, so no silver rewrite. The section-name set is authored once
here and restated verbatim in d-3, which reads it from this module rather than re-listing it.

<status>complete</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
