# AMGT_CORPUS task order -- `CRPS-d-2` -- ROUND 2: the continuation artifact's PDF pillar branch over extraction v2, the docx branch KEPT AS THE CONTROL, `thesis_summary` as a cited field, v2 keys in the inputs hash

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-d-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- 2 armed gates of the census (C1=23 C2=5 C3=12 C4=21 C5=334), 0 on these surfaces; no deploy.
comp-iam: RUN at L5 (round-1 read, 214 roles on the DESIRED plane, not re-run this cut); BLIND to this box's credential; this cell's first gold put of a rebuilt continuation measures the prefix.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, continued from `CRPS-d-1`. Work ONLY in your worktree.
- **First act:** print `git rev-parse --abbrev-ref HEAD`, and test that `lib/research/corpus/extract.py` defines
  `METHOD_VERSION_2` and that `lib/research/corpus/continuation.py` exists. If either is absent, STOP with a BLOCKING row.
- Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_CORPUS~1;`.
- **NEVER INSTALL. NEVER CALL A VENDOR API OR THE CLAUDE API. NEVER TOUCH THE LIBRARY.** Every input is a stored object.

## 1. THE CELL, inlined in full -- `CRPS-d-2` (manifest row R6 enriched: the PDF branch; serves FWD-16 and FWD-10's store half)

**FWD-10, verbatim:** *"An analyst opens a covered name and reads the TEAM'S OWN investment-thesis pillars on the Thesis
tab. DONE WHEN EXERCISED -- IMB_LN_Equity renders the pack's pillars as bold lead plus paragraph, each openable to the
report and the passage it came from, and each marked as the team's rather than generated."* The RENDER is
`AMGT_RESAPP`'s; this cell makes the pillars exist for PDF-only names too, cited, so the render has something to show.

**`C-CITED-OR-ABSENT`** and **`C-INPUT-HASHED`** bind exactly as in round 1: every field cites the report and passage
(`report_key`, `locator`, `passage`); a field the reports do not state is `null` with an `absent` reason; the artifact
carries `{key, sha256}` for every input and its own `content_sha256`; a rebuild whose inputs changed is a NEW gold object
beside the old one, through `gold.gold_put`, never overwriting.

**RULED -- what you build in `lib/research/corpus/continuation.py`:**
- **Extraction resolution:** `_read_reports_with_bytes` reads, for each typed row, the v2 object
  (`<report_id>/extract.v2.json`, beside the row's `extract_key`) WHEN IT EXISTS, else v1 -- typed silver rows are NOT
  rewritten. The key actually read (v2 or v1) enters `inputs` with its sha256, so `current_inputs` and `inputs_sha16` move
  exactly when the read object changes (FWD-8 / FWD-17's own discriminator).
- **The PDF pillar branch** (the RULED docx rule stays byte-unchanged and is the CONTROL): over a v2 PDF document's
  `lines`, the INVESTMENT THESIS block is the lines after the `INVESTMENT THESIS` section lead (standalone or inline) up
  to the next section lead (any name in `extract.py`'s section-name set, whatever punctuation follows) or an unnamed
  large/bold heading that is not a lead-only line. Inside it, a pillar starts at (a) a line whose LEADING bold spans end
  at a colon -- `<Lead>: <body>` with the lead matching `^([A-Z][^:]{2,140}?):\s*(.+)$` and the lead text starting with
  the bold prefix; or (b) an all-bold line ending in ':'; or (c) a line ending in ':' whose text equals its bold prefix
  (the PFOE shape); a lead whose normalised text is a section name is NEVER a pillar. The body is the non-bold remainder
  plus the following non-lead, non-heading lines. Each pillar: `{pillar, text, citation}` with the citation's locator the
  PAGE index and the passage the pillar's first 300 chars.
- **`thesis_summary`**, a new cited field: the inline remainder after an `INVESTMENT THESIS:` lead plus up to five
  following non-lead lines (PFOE shape), or `''` with reason `standalone heading, no inline summary` for the Word shape.
- **Which document supplies the pillars:** the most recent class A report; if it is a docx, the docx branch; if a PDF,
  the PDF branch. A name whose most recent class A is a PDF with no INVESTMENT THESIS lead reads ABSENT with the reason
  `pdf pack carries no INVESTMENT THESIS section lead`.
- **`--show-first-pdf-only`:** the FIRST resolved security key (sorted) whose most recent class A report is a PDF: print
  `security_key`, `source_type pdf`, the pillars (`pillars N`, one line each with `report_key` and page), and
  `thesis_summary`. **`--verify-citations`** re-resolves every citation of every stored continuation object against the
  extraction text it names (v1 or v2 as recorded) and prints `citations_checked N resolved N unresolved 0`.
- **`--write`** (a BUILD STEP): rebuild every resolved name; a name whose inputs are unchanged is `existed`; print
  `names N rebuilt R existed E with_pillars P with_pdf_pillars Q` first and last.

**What this cell does NOT do:** no change to `typed.py`, `extract.py`, silver or any other gold table; no docx-rule change.

## 2. WHERE THIS CAME FROM
Round 2, decomposition v2.0, chain A, cell 2 of 4 on this slot, after `CRPS-d-1` drained VALID. `CRPS-d-3` reads the
rebuilt continuation.

## 3. SURFACES

<paths>
lib/research/corpus/continuation.py
lib/research/corpus/tests/test_continuation.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-d-2.continuation-pdf-pillar-branch.md
</paths>

**READ-ONLY:** every other `lib/research/corpus/` module (import `extract`'s section-name set; do not copy it),
`lib/research/harvest/store.py`, `lib/opal_naming.py`, `PDF_EXTRACTABILITY_20260924/per_file.json` (the CRO's per-file
leads, for fixtures). Scratch in `.scratch/d2/`. Commit with
`bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_CORPUS~1 <0.9.0_WK_AMGT_CORPUS~1@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS
- **NO S3 DELETE OF ANY KIND**; a superseded artifact is a new object beside the old one.
- **Pure ASCII source, LF, Python 3.9-compatible.** Passages stored with `ensure_ascii=True`.
- **S3:** writes ONLY through `gold_put`, never overwriting. **Run `--write` as a BUILD STEP.**
- **Tests:** offline under the poison; v2 PDF documents are built as dicts in the test from the shapes above (a PFOE pack
  with an inline `INVESTMENT THESIS:` summary, two pillars one of which is the lead-alone shape, a `RISKS AND
  CONSDIERATIONS:` line that must close the block, and a `Valuation:` line that is a pillar); a docx document as before,
  proving the docx branch's output is unchanged (the CONTROL).
- **Surprise rows:** `AMGT_CORPUS-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~X`. **REFUSE a criterion you cannot satisfy as
  written**, and report it with your measurement -- a PDF-only resolved name whose pack genuinely carries no pillars is a
  finding, not a failure of this cell.

## 5. PROOF OF SPEC (each invocation LITERAL; each runs under your `timeout 600`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-d-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/corpus/tests/test_continuation.py -q --color=no -p no:cacheprovider 2>&1 | tail -3</invocation><expect>(?m)^\d+ passed in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-d-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.continuation --verify-citations 2>&1 | tail -3</invocation><expect>citations_checked (\d+) resolved \1 unresolved 0\b</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-d-2"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m lib.research.corpus.continuation --show-first-pdf-only 2>&1 | tail -40</invocation><expect>(?s)security_key \S+.*source_type pdf.*pillars [1-9]\d*.*report_key .*thesis_summary </expect></criterion>
  <criterion id="AC4" cell_refs="CRPS-d-2" judgment="true"/>
</proof_of_spec>

- AC1 the built behaviour; AC2 the seam probe against the store (every stored citation, v1 and v2, resolves); AC3 the one
  further criterion (reason: FWD-16 is only true if a REAL PDF-only name yields pillars, which fixtures cannot show).
- **AC4 (JUDGMENT, the CVO's):** AC3's printed pillars for the PDF-only name beside the pack's own text at the cited pages.
  Are the leads the team's leads, and is the split between pillar and section correct? Record AC3's output and the
  artifact's S3 URI, with NO verdict.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-d-2.continuation-pdf-pillar-branch.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3,AC4 --governing-order <this order>` returns rc 0.
3. Flip `<status>` to `complete` only if every mechanical criterion passes. Commit via safe-commit with the pathspec of
   exactly the files you changed plus the instance.
4. Report ONCE: the `--write` totals line, the citation line, and the PDF-only name AC3 picked with its pillar count.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the docx branch is the control by the CRO's measurement (17 FULL of 19 pairs, 99 of 99 pillars); this
cell must not "improve" it. The v2-preferred read is what makes every continuation rebuild into a new object (FWD-17's
store half) without any silver rewrite.

<status>complete</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
