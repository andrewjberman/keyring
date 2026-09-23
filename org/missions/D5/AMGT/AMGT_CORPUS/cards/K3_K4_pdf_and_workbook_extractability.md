# K3 / K4 -- PDF and workbook extractability (CRPS-c-2)

**Seat:** `0.9.0_WK_AMGT_CORPUS~1`. **Cell:** `CRPS-c-2` (manifest row R2). **Built:**
`lib/research/corpus/extract.py`. **Measured against:** the 123 bronze `research-report`
objects landed by `CRPS-c-1` (the 33 RESOLVED-folder subset of the library, NOT the full
351-file / 93-folder scan denominator -- see "scope" below).

## The PRD's questions, verbatim

**K3:** *"the PDF-only reports -- 184 PDFs against 71 Word files: whether the PDF text is
extractable to the same skeleton, since the scan's term census read the Word files only"*

**K4:** *"the workbooks -- whether the model sheets read without Excel on this box, and
whether the 23 FactSet-coded variants type onto the same mnemonics"*. This cell answers the
FIRST half of K4 only (read without Excel; FactSet codes found). Typing the found mnemonics
onto standard mnemonics is `CRPS-c-9`'s.

## Scope of this measurement

The bronze store this cell reads from carries only the 33 RESOLVED-folder files `CRPS-c-1`
ingested (123 objects: 52 PDF, 43 XLSX, 25 DOCX, 3 PNG), not the CRO scan's full 351-file
corpus (184 PDF / 78 XLSX / 71 DOCX / 17 PNG / 1 HTML across 93 folders). Every count below
is over THIS 123-object population, printed as its own denominator.

## Commands and their printed output (this run)

```
$ python -m lib.research.corpus.extract --write
...
objects 123 extracted 120 not_extracted 3 crash 0 stored 123

$ python -m lib.research.corpus.extract --census
bronze_objects 123 extractions 123 missing 0
k3 pdf 52 text_extractable 52 zero_text 0 median_chars 15642 skeleton_heading_hits 33 of 52
k4 xlsx 43 opened 43 failed 0 with_mnemonics 37 factset_coded 0
k4_calls BDH,BDP,FDS,FF_ENTRPR_VAL_DAILY,FREF_MARKET_VALUE_COMPANY,FREF_SHARES_COMPANY
```

(120 of 123 objects are extractable: 52 PDF + 43 XLSX + 25 DOCX; the other 3 are PNG,
`not-extracted: png` by design -- images are out of scope for text/heading extraction.)

## K3 -- yes, the PDF-only reports are extractable to the same skeleton

All 52 of 52 PDF-only bronze objects in this population produced non-empty extractable text
(`text_extractable 52`, `zero_text 0`) via PyMuPDF -- none of the 52 are scanned-image-only
with no text layer. Median document length is 15,642 characters. 33 of 52 (63%) surfaced at
least one heading (by the size/bold heuristic: a short line whose span font size exceeds
1.15x the page's median body size, or which is bold) matching one of the scan's own section
names case-insensitively (RECOMMENDATION, INVESTMENT THESIS, RISKS, Headline results,
Guidance, Segment highlights, Geographic highlights) -- i.e. nearly two-thirds of the
PDF-only reports carry a heading the extraction can align to the same skeleton the Word
files were scanned for.

**What this could NOT measure:** why the other 19 of 52 did not surface a skeleton-name
heading. Candidates not distinguished here: a different section-name phrasing (e.g. a
company-specific variant), a section heading not visually distinguished by font size/bold
in that particular PDF (so the heuristic misses it even though the text is present), or a
report whose skeleton genuinely omits that section. `find_tables()` was deliberately never
used for heading detection (measured on this box to misreport a wrapped Word heading as a
2x2 table -- BOUNDS, this order). No OCR was run; every PDF here already has a text layer
(`zero_text 0`), so OCR absence does not explain the 19.

## K4 (first half) -- yes, the model sheets read without Excel; FactSet codes ARE present
in the corpus, but this cell's ruled extraction method under-reads them (see the surprise row)

43 of 43 XLSX bronze objects opened cleanly with openpyxl `read_only=True` (both a
`data_only=True` pass for values and a `data_only=False` pass for formulas) -- `opened 43
failed 0`. No Excel install is used or needed on this box.

37 of 43 (86%) carry at least one quoted upper-case token found inside an actual formula
call (`with_mnemonics 37`) -- the corpus genuinely uses BDP/BDH/FDS-style vendor calls with
literal quoted arguments (`k4_calls` names the call identifiers this run actually measured:
`BDH, BDP, FDS`, plus three false-positive "call names" from the token-scan's non-nested-
paren limitation on FDS's string-concatenation array formulas -- see the surprise row).

`factset_coded 0` of 43, however, **understates** the corpus: the FactSet-coded variant's
primary mnemonic argument (`FF_SALES`, `FE_ESTIMATE`, `FG_FACTSET_SECTOR`, etc. -- the
scan's own 23-workbook FactSet-coded set) is a CELL REFERENCE to a label cell holding the
bare mnemonic text, not a literal quoted string inside the call itself (measured directly:
`Model NEW VERSION!A79` in a FactSet-coded workbook holds the plain string `FF_SALES`,
referenced by `Model NEW VERSION!D79`'s array formula `=_xll.FDS($D$2,$A79&"(ANN_R,"&D$75&
")")` -- 81 such label-cell mnemonics counted in that one workbook's `Model NEW VERSION`
sheet alone). The ruled extraction method (RULED, this order: "quoted upper-case tokens ...
inside formula calls") is implemented and run exactly as specified and its output is
accurate FOR WHAT IT MEASURES (real quoted tokens inside real calls -- mostly BDH/BDS
override-parameter names like `EQY_CONSOLIDATED`, `ACCOUNTING_STANDARD_OVERRIDE`, `PER`,
never an `F[FGE]_`-prefixed instrument mnemonic because those are never literal in this
corpus's formulas). Filed as `AMGT_CORPUS-Z-W1-S1`: the corpus's own shape means "FactSet
codes found" by literal quoted-token scanning reads structurally low, and resolving a
cell-referenced mnemonic to its label text is a strictly different (and larger) extraction
task than the one this cell was ruled to build -- left for whoever takes up the handoff (not
`CRPS-c-9`, which is scoped to typing already-found mnemonics onto standard ones, not to
finding more of them).

**What this could NOT measure:** the 23-workbook FactSet-coded count itself (that is the
scan's own count over the full 78-workbook corpus, not this cell's 43-object population);
whether resolving cell-referenced mnemonics would raise `with_mnemonics`/`factset_coded`
materially -- not attempted here, out of this cell's ruled scope.
