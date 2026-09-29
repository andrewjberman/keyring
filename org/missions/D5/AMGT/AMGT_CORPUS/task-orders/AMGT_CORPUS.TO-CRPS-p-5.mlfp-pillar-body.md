# AMGT_CORPUS task order -- `CRPS-p-5` -- ROUND 14: `Z-W1-S16` -- ML_FP's one pillar: read the source, then recover its body or serve the pillar ABSENT with a reason

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-p-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~5</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only; the served move is the issuer's drain act under a pair.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~5`**, slot `~5` of round 14. Serves **FWD-10 (a served pillar is lead + paragraph + citation), row `Z-W1-S16`**.

## 1. THE CELL -- `CRPS-p-5`

**Where this came from.** Row `AMGT_CORPUS-Z-W1-S16`: 158 of 159 served thesis pillars carry lead, paragraph, citation
and terms; ML_FP_Equity's one pillar `Nearing turn in cycle` has text `''`, and its citation passage begins mid-sentence and runs
into the next `RISKS AND CONSDIERATIONS` heading (source: `Michelin Research Pack Template 2026 05 28_v1.pdf`, a PDF report). Pillars
are built in `lib/research/corpus/continuation.py`: PDF reports through `_pdf_pillars_raw` / `_resolve_thesis_pillars_pdf`, docx
through `_thesis_pillar_paragraphs` / `_resolve_thesis_pillars_docx`, joined in `_resolve_thesis_pillars`; `continuation.build(key)`
builds the document WITHOUT writing. The CTO ruled (round-13 analysis): *"read the source first. If the source paragraph has text,
the reader drops it, and the reader is repaired. If the source is empty, the pillar is served ABSENT with that reason, never as an
empty string."*

**RULED -- what you build:**
1. Read ML_FP's source: the extracted PDF text the reader consumes (the continuation reads the stored extraction; print the
   lines around `Nearing turn in cycle` through the next heading). Write what you found into your report, verbatim lines.
2. If the source carries the paragraph: repair the PDF pillar reader so it keeps the body and the citation stops at the next
   heading. If the source is empty: the pillar is served ABSENT with that reason (the field's own ABSENT shape
   `{"value": null, "absent": <reason>}` when no pillar has text; an empty `text` is never served). Either branch applies to every
   name through the same rule; IMB_LN_Equity (docx, 6 pillars) and ADBE_US_Equity (PDF, 2 pillars) must read unchanged.
3. Bump `continuation.METHOD_VERSION` to `amgt-corpus-continuation/3` and update the tests that pin it
   (`test_continuation_terms.py` asserts the string; the standing ruling grants them to this order).
4. `lib/research/corpus/tests/test_continuation_pillar_body.py` (new): the ML_FP shape (a lead whose body sits on the lines after it, then the next heading)
   yields the branch you built; a lead with a body keeps it; the citation never crosses the next heading.
5. **Do NOT change how continuation objects are keyed** (`<inputs_sha16>.json`, which excludes `METHOD_VERSION`) and write nothing
   to S3: the served move and its keying are the issuer's drain act under a pair. Report whether a rebuilt ML_FP document would
   collide with its stored key (read its stored object's key; do not write).

## 3. SURFACES

<paths>
lib/research/corpus/continuation.py
lib/research/corpus/tests/test_continuation_pillar_body.py
lib/research/corpus/tests/test_continuation.py
lib/research/corpus/tests/test_continuation_terms.py
lib/research/corpus/tests/test_continuation_reader_method.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-p-5.mlfp-pillar-body.md
</paths>

READ-ONLY: every other file in the repository, every S3 object, the research library on the synced drive. Scratch `.scratch/p5/`.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible. NO vendor call. NO S3 write (never run `continuation --write` or `dossier --write`). Importing continuation must stay free of new heavy imports.
- REFUSE a criterion you cannot satisfy as written, with your measurement; rows `AMGT_CORPUS-Z-W5-S<k>`, `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-p-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p5_AC1.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-p-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p5_AC2.sh</invocation><expect>(?m)^p5 ML_FP_Equity pillars 5 empty_text 0 \| IMB_LN_Equity pillars 6 empty_text 0 \| ADBE_US_Equity pillars 2 empty_text 0$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-p-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round14/p5_AC3.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1 the continuation tests with the new one; AC2 the live build (no write): ML_FP carries no empty pillar, the two controls unchanged; AC3 the whole corpus suite.

## 6. WHEN YOU ARE DONE
1. Instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/AMGT_CORPUS.TO-CRPS-p-5.mlfp-pillar-body.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2,AC3 --governing-order <this order>` rc 0.
3. Flip `<status>` to `complete` only if every criterion passes; commit the files you changed plus the instance.
4. Report ONCE: each AC line, the source lines you read, which branch you built, and whether a rebuilt ML_FP document collides with its stored key.

## 7. AMENDMENT 1 (issuer, 2026-09-29 ~19:2xZ, on row `AMGT_CORPUS-Z-W5-S5`) -- this supersedes RULED item 2's branch choice

Your first pass (708242756c) read the source correctly: `Nearing turn in cycle:` (line 689) has no body. But the same
INVESTMENT THESIS block (lines 675-688 of extract `362ec404b3d2eba8`) carries FIVE pillars with body text whose leads are
bold_first and end in a PERIOD (`Irreplaceable brand and pricing power.`, `Mix shift to premium.`, `FCF Generation.`,
`Beyond tires.`, `EV-agnostic positioning.`). The CTO's ruling was "if the source paragraph has text, the reader drops it,
and the reader is repaired", so the branch is the REPAIR, not ABSENT:
1. The PDF thesis-pillar reader accepts, inside the thesis block bounds only, a line with `bold_first` True whose
   `lead_prefix` ends in `.` as a pillar lead, exactly as it accepts one ending in `:`. The body runs to the next lead or
   the block end; the citation stops at the block's closing heading (keep your clip).
2. Keep your empty-text drop: `Nearing turn in cycle` has no body and is not served. ABSENT is served only when no pillar
   in the block has text.
3. AC2's expectation is now `ML_FP_Equity pillars 5 empty_text 0`, the two controls unchanged. Your new test file gains the
   period-led shape (five period leads with bodies then an empty colon lead then the heading yields five pillars).
4. REPORT (not a criterion): the pillar count per PDF-sourced name BEFORE (CLOUD HEAD code) and AFTER (your code), read-only
   over every name `continuation` builds, with the denominator, and every name whose count changed.
5. Keying: your row Z-W5-S4 stands -- the METHOD_VERSION bump moves every name's key; the order's "excludes METHOD_VERSION"
   was wrong. Keep the keying as it is; the served move is the issuer's drain act under a pair.
Merge CLOUD into your branch first (`git merge CLOUD`, no rebase); this file's last status tag reads pending until you
append a new status tag reading complete at the end of the file. Re-run AC1-AC3 and proof-of-spec-check, re-write the instance, commit.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-13 analysis s.4 item 5 @`f1c482d24f` (msg 26603). Checks dry-run at the base `dbafd14c52`: p5_AC1 FAIL (no tests ran); p5_AC2 FAIL ('ML_FP_Equity pillars 1 empty_text 1 | IMB_LN_Equity pillars 6 empty_text 0 | ADBE_US_Equity pillars 2 empty_text 0'); p5_AC3 PASS (444 passed).
Merge HELD until the pair is signed; the continuation keying (inputs-only key; GoldImmutableError on a new body) is ruled at the pair with the CTO.
<risk>SERVED</risk>
<status>pending</status>
<round>14</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<status>pending</status>
<status>complete</status>
