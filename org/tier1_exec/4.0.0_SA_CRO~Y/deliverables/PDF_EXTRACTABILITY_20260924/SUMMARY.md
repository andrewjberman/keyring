# PDF extractability of the research-corpus skeleton -- MEASURED 2026-09-24 03:1xZ-03:3xZ, site Z

**Seat:** `4.0.0_SA_CRO~Y`. **Andrew-direct:** *"Begin with PDF Extractibility"* (~03:07Z, record
`../ANDREW_DIRECT_20260924_030xZ_BEGIN_WITH_PDF_EXTRACTABILITY.md`). **Answers:** dossier brief O7 / Part VIII-5
(`docs/briefs/amgt-corpus-dossier-fold-brief-20260924.md` @`5ef3e9a89b`). **Instrument:** `measure_pdf_extractability.py`
(this folder), read-only over the OneDrive-synced library; per-file results in `per_file.json`, aggregates in
`summary.json`. Reuses the estate's own rules: `lib/research/corpus/extract.py`'s PyMuPDF line/heading heuristic and
`continuation.py`'s RULED docx pillar rule as the positive control's expected value.

## THE ANSWER IN ONE LINE

**Yes. The PDF packs are extractable to the same skeleton, and the "30 PDF-only folders" problem is smaller than the
brief said: 26 of 30 carry a full research pack, 29 of 30 carry pillars or a "Why we own", and the one folder with
nothing (QXO) holds only an investor Q&A. The cost was three rule changes, each measured against a control.**

## POPULATION (denominators)

| what | count |
|---|---|
| folders | 93 (46 docx+pdf, 30 PDF-only prose, 6 docx-only, 10 workbook-only, 1 empty) |
| PDFs at folder top level, READ | **157** (0 read failures, 0 zero-text, 0 placeholders hydrated by this run) |
| PDFs in ONE subfolder, NOT read | 28 (`Copa CPA/CAP earnings press releases/`, company press releases 2005-2026) |
| docx files, READ (control side) | 71 (22 carry docx-rule pillars) |
| the 2026-09-22 scan's "184 PDF" | = 157 top-level + 28 subfolder, minus 1 added since; reconciled |

## THE POSITIVE CONTROL -- docx+pdf pairs of the same stem

| | |
|---|---|
| pairs | 56 |
| pairs whose docx has no INVESTMENT THESIS block (earnings updates; expected) | 37 |
| pairs with docx pillars | 19 |
| **FULL** (every docx pillar recovered from the PDF, no extra) | **17** |
| PARTIAL | 1 (Alibaba: all 6 docx pillars recovered, PDF finds a 7th -- a bold lead the docx rule's one-paragraph shape misses) |
| NONE | 1 (Michelin: the docx is a blank Research Pack TEMPLATE with 0 pillars; the PDF carries 1) |
| **docx pillars recovered from PDF** | **99 of 99** |

So on the Word-author (IDVZ) packs the PDF path reads the pillars the ruled docx path reads, lead for lead.

## THE PDF-ONLY FOLDERS -- what each field reads (30 folders)

| field, from the folder's PDFs | folders with it (of 30) |
|---|---|
| a Class A research pack (INVESTMENT THESIS present) | 26 |
| thesis pillars (>= 1) | 26 |
| thesis one-sentence summary (PFOE inline shape) | 24 |
| RECOMMENDATION line | 27 |
| RISKS block | 27 |
| MANAGEMENT block | 26 |
| Upside / Base / Downside cases (all three) | 26 |
| COMPANY DESCRIPTION | 24 |
| "Why we own" (earnings-update section) | 15 |
| **pillars OR "Why we own"** | **29** |
| nothing at all | 1 (QXO: `QXO-May-2026-Investor-Q-A-Final.pdf` only) |

The three folders with "Why we own" but no pillars hold only an earnings update (Alphabet, Eli Lilly, UnitedHealth);
their thesis is the update's "Why we own" paragraph, which the dossier can carry as the thesis summary until a pack is
filed.

## ACROSS ALL 157 PDFs

class A (pack) 56 · class B (update) 67 · class D (stock move) 1 · OTHER 33 (company source documents: 10-Ks, RNS,
results releases, investor presentations -- bronze, not team reports). Pillars in 52 files (204 pillars); management
in 50; recommendation line in 99; all three cases in 50; PFOE inline thesis summary in 30; company description in 46;
growth algorithm in 28; ownership in 34; "Why we own" in 17.

## THE THREE FINDINGS THAT CHANGE THE CUT (each found by the control, not by reading)

1. **The PFOE author's packs have a RICHER fixed skeleton than the Word packs, and its labels are INLINE BOLD LEADS,
   not headings.** `RECOMMENDATION:` · `COMPANY DESCRIPTION:` · `Long-term growth algorithm and expected return:` ·
   `INVESTMENT THESIS: <one-sentence summary>` · pillars (2 per pack, bold lead + paragraph) · `RISKS AND
   CONSIDERATIONS:` with `Pre-mortem:` first · `Ownership:` · `Management and capital allocation:` · `Special items:`;
   the updates add `Headline results`, `Positives`, `Negatives`, `Segment highlights`, `Headwinds and risks`,
   `Guidance`, `Changes in analyst sentiment`, `Why we own`. The extraction cell's K3 heuristic (standalone heading =
   large or all-bold short line) sees none of these, which is why K3 read "33 of 52 surfaced a skeleton heading" and
   why this brief first counted 3 packs among the PDF-only folders instead of 26. **Rule: a section opens on a
   standalone heading OR on a line whose leading bold spans are a known section name.**
2. **The team's PDF headings carry a trailing colon** (`RISKS AND CONSDIERATIONS:` -- the typo is theirs and is in the
   name set). A block-boundary rule that treats "bold line ending in ':'" as a pillar lead lets the whole RISKS list
   bleed into the pillars: the first run's control read 16 PARTIAL of 19 with every "extra" being a risk item.
   **Rule: a known section name closes the block whatever punctuation follows it; `Valuation` is a PILLAR lead
   (BB Seguridade, Petrobras), never a section name.**
3. **A PFOE pillar lead can sit alone on its line with the colon in a NON-bold span** (Cadence's second pillar), so
   "all-bold line ending in ':'" misses it. **Rule: a line ending in ':' whose text equals its bold prefix is a lead
   with its body below.** The 80-character lead cap of the docx regex changed nothing here (measured: a 140-char
   variant gives identical counts), so the cap is not the limit; the colon-span shape was.

## WHAT THIS DOES NOT CLAIM

- Recall is proven on the 19 Word-author pairs; the PFOE packs have no docx twin, so their pillar counts (2 per pack,
  consistent across 24 packs) are a self-consistent measurement, not a controlled one. A human read of two PFOE packs
  against `per_file.json`'s leads is the cheap check (`3.0.0_SA_CVO~Z`'s to grade, never this seat's).
- The 28 Copa subfolder PDFs were not read (company press releases; bronze at most, never team reports).
- Management, risks and cases are measured as BLOCK PRESENCE (heading found, block non-empty), not as typed fields;
  typing them is the cell's work. The recommendation line is captured as text (<= 160 chars) but not parsed into
  fund / size.
- Nothing was written under the library root; PyMuPDF opened bytes read with `open(path, 'rb')`.

## WHAT THE CUT SHOULD TAKE FROM THIS

- `lib/research/corpus/extract.py` gains the inline-lead section rule and the PFOE section-name set (finding 1); the
  extraction object records `section_leads` beside `headings`.
- `continuation.py`'s pillar rule gains a PDF branch with the three rules above, keeping the docx branch as the
  positive control (17 FULL of 19, 99 of 99).
- The dossier gains the fields the PFOE skeleton makes free: `thesis_summary`, `company_description`,
  `growth_algorithm`, `ownership`, `special_items`, `why_we_own`, `positives` / `negatives` -- each cited or absent.
- The scan's "class A = INVESTMENT THESIS heading" test becomes "INVESTMENT THESIS heading OR inline lead"; 30 more
  PDFs are packs than the scan counted.
