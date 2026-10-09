# AMGT_CORPUS -- the KPI vocabulary behind pillar terms: how it was built, what it was meant to cover, and the round-42 fork

- **Author:** `4.0.0_SA_CRO~DELL1`, 2026-10-09 ~05:4xZ-06:1xZ. **Asked by:** `1.0.0_SA_CTO~DELL1` msg 1778, for the design fork
  `ROUND_ANALYSIS.round40.PREDRAFT.md` AMENDMENT 1 item 3b sends here
  (`org/missions/D5/AMGT/AMGT_CORPUS/ledger/ROUND_ANALYSIS.round40.PREDRAFT.md:43-46`).
- **Method:** read-only. Code and git history read on dell1 at `box/dell1` HEAD `0c733a5c5f`. The stored gold dossiers were read
  through `lib.research.corpus.dossier.read_dossier` over `s3://opal-data-harvest/amgt/harvest/gold/research_dossier/` at
  ~06:0xZ. No write, no Bloomberg call, no Claude call. Instrument: scratchpad `kpi_vocab_census.py`, the same listing and reader
  as `2.0.0_SA_COO~C1`'s `checks/round40/r41_pillar_terms_census.py` @f43ca41993. On this box pymupdf's DLL fails to load,
  so `fitz` was stubbed; no PDF is opened on this path.

---

## 1. HOW THE VOCABULARY WAS BUILT

1. **Source file.** `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922/research_docx_kpi_census.json`,
   sha256 `b18193fd...76517`. Added in one commit, `578f7072d1` (2026-09-22, `4.0.0_SA_CRO~F`, the AMGT_RESAPP L1 midstream brief),
   and never edited since (`git log` on the path returns that one commit).
2. **What the file is.** It is the per-file output of a census: 71 rows, one per Word report, with fields `folder, file,
   class, words, kpi, recommendation`. `kpi` is a dict of 25 FIXED keys, the same 25 in every row (`continuation.py:90-92`
   measures this). The keys are: ARPU, ARR/RPO/backlog, CET1, EBITDA, FCF, GMV, IDVZ/DIVZ, NIM, ROE/ROTE, broker, capex, churn,
   combined ratio, consensus, cost of risk, cost/income, dividend, guidance, net debt, organic growth, position size, premiums,
   production, same-store, volume/price.
3. **Who chose the 25.** The scan's author chose them as a COUNTING INSTRUMENT. Its purpose was to count, over Word text, how
   often each sector's known KPI words appear (scan section 3, `RESEARCH_CORPUS_SCAN_20260922.md:103-116`, e.g. "CET1 in 5
   files", "Volume/price terms in 42 files"). The scan states the limit itself: "It counted KPI terms by regex over Word text only
   ... so the term counts are lower bounds" (`:149-150`). The 25 keys are the instrument, not a finding. The scan's FINDINGS are
   the per-sector **KPI set** sentences in bold in the same table (e.g. Industrials: "RPK/ASK/load factor; throughput TEU;
   operating ratio", `:114`), and most of those words are not among the 25 keys.
4. **How it became a vocabulary.** `CRPS-c-6` (`a5d537f792`, 2026-09-23, `0.9.0_WK_AMGT_CORPUS~1`) adopted the census key set
   as the KPI lexicon, under "measured, not designed ... Never adds a term the scan did not count" (`continuation.py:182-191`,
   `KPI_LEXICON_PATH` `:147-150`). `sector_template.py:305-317` loads the same file the same way.
   `CRPS-h-5` (`40ae4e61b3`, 2026-09-26, `0.9.0_WK_AMGT_CORPUS~5`) then made it the PILLAR-TERM vocabulary. It splits the
   25 keys on '/' into 31 terms (`_kpi_vocabulary_terms`, `:215-229`). A pillar's terms are `[heading, *vocabulary terms its text
   names]`, matched whole-word and case-insensitive (`_pillar_terms`, `:232-253`), and the test pins this at
   `lib/research/corpus/tests/test_continuation_terms.py:132-133`.
5. **What ordered pillar terms.** PRD `org/missions/D5/AMGT/AMGT_CORPUS/prd/AMGT_CORPUS_PRD.md:539-545`, FWD-18: "Each pillar
   and KPI row names its terms, and the header feed and Chatter axis are filterable to those terms". ACCEPT: **"A theme the team
   named is followable into the news."** SOURCE: brief O9, "Marked PROPOSAL and LATER enrichment by its author: cut LAST,
   deferrable by the round-N analysis". DONE WHEN: "the feed filters to them for at least one name".
6. **Andrew-direct words.** I found none about the KPI vocabulary itself. The scan's order is about sector idiosyncrasies and
   "what ratios are they using" (`RESEARCH_CORPUS_SCAN_20260922.md:3-7`). I did not search other Andrew-direct records beyond
   the PRD SOURCE lines read above.

## 2. WHAT COVERAGE IT WAS MEANT TO HAVE

- **For counting KPIs in reports:** sector-generic KPI words across the 71 Word reports. That population excludes the PDF-only
  research packs. The PFOE names (US growth) are PDF-heavy (`:124-126`), so their prose was never in the population the 25
  keys were picked against.
- **For pillar terms:** no coverage target was stated anywhere I read. No test asserts coverage. The tests pin ordering, the
  whole-word trap, case and the '/' split (commit `40ae4e61b3` message). Reusing the lexicon for pillars was a convenience: the
  one MEASURED word list on hand. It was not a vocabulary built for thesis themes.
- **The intent FWD-18 states is THEMES** ("a theme the team named"). A KPI word list is the wrong population for that purpose,
  by construction.

## 3. MEASURED TODAY

Denominator: 95 names listed under the dossier prefix, 46 with structured pillars, **163 pillars**, every one carrying `text`.
Vocabulary: **31 terms** (25 keys, '/'-split).

| reading | count | of |
|---|---|---|
| pillars whose only term is the heading (title-only) | **112** | 163 (reproduces `r41_c3` @f43ca41993) |
| names with at least one title-only pillar | 44 | 46 names with pillars |
| title-only pillars whose BODY matches any of the 31 terms on re-check | 0 | 112 |
| title-only pillars in the 2-pillar names (the PFOE PDF two-pillar template) | 36 | 112, across 24 names |
| title-only pillars in names with more than 2 pillars (IDVZ Word packs) | 76 | 112, across 20 names |
| title-only titles that are the moat / secular-tailwind boilerplate | 42 | 112 |
| body length of title-only pillars, in words | 32 median; 32 at 1-20, 43 at 21-60, 37 over 60 | 112 |

**Why they miss.** It is not the matching rule: whole-word, case-insensitive matching finds 0 of 31 terms in all 112 bodies.
It is the population. The titles are thesis CLAIMS, not metric names: "Monopoly in EUV lithography with an impregnable moat"
(ASML NA), "Berkshire Hathaway endorsement", "The Buzios Field", "TOTEM", "NVIDIA validation", "Capital release story". The
bodies argue the claim in prose and seldom name a reported metric.

**Hand growth from the scan's own findings, measured.** I added every word in the scan's per-sector "KPI set" findings
(`:107-116`, 68 entries incl. NII, RoTE, solvency, RPK, TEU, RAB, pipeline, margin). That rescues **20 of 112** pillars. Only
**5 of 112** are rescued once eleven generic words are excluded (margin, guidance, dividend, volume, EPS, cloud, fee, generation,
networks, coverage, pipeline). Those generic words produce false theme matches: "generation" hits "generational drug" and
"coverage" hits press coverage.

**A crude proxy for terms taken from the pillar itself.** Of the 112 TITLES alone, 27 carry an acronym or a capitalised word
past the first. Title Case inflates this: "Shareholder Returns Improving" and "Irreplaceable Infrastructure" are false hits.
About 15 of the 27 are real, followable names: EUV, WFE, PMA, ITSM, HCM, LNG, NGP, Morgan Stanley, Berkshire Hathaway, NVIDIA,
Buzios, TOTEM, Southeast Asia, China Consumer, E-commerce. The BODIES were not measured for this.

## 4. THE FORK: OPTIONS, COST, AND WHAT EACH DOES NOT FIX

| option | cost | does NOT fix |
|---|---|---|
| **A. Grow the KPI vocabulary by hand** (from the scan's sector KPI sets or by request) | small: one data file and a re-pin of the lexicon sha. But it breaks "never adds a term the scan did not count" (`:184-185`), so it needs a ruling | 107 of 112 if generic words are excluded. It adds noise if they are not. Themes stay unfollowable, because a KPI word is not a theme. |
| **B. Derive terms per pillar from the pillar's own title and body** (deterministic: acronyms, proper-noun runs, a stop list) | medium: a new rule in `_pillar_terms`, a `METHOD_VERSION` bump, a test rewrite at `test_continuation_terms.py:132`, and a dossier rebuild. An LLM extractor is excluded by this module's no-Claude-API rule (`continuation.py:9-10`) | the 42 boilerplate moat/tailwind pillars, whose text is generic. Title Case false positives need a stop list, and the stop list is the hand-tuning the module disclaims (`:85-88`). |
| **C. A per-company vocabulary** (product, segment and franchise names per name) | high: curated per name across 93 folders, or sourced from company filings, which this corpus did not read (`RESEARCH_CORPUS_SCAN_20260922.md:145`) | names with no curated list. Its upkeep is a hand list, the pattern MDPF_STRATID retired this week for SMA rules. |
| **D. Accept title-only pillars as label-only** (today's interim: no filtered feed, and the page says so) | zero. FWD-18's DONE WHEN ("for at least one name") is already reachable on names with real terms (IMB LN, per AMENDMENT 1 3a) | ASML-class names stay unfollowable. That is exactly the visible gap that raised the item. |

**Past pattern this repeats.** A measuring instrument promoted to a production vocabulary. The 25 keys were picked to count
sector KPIs in Word text, then reused as the list that pillar themes are matched against. The disclaimer in `continuation.py:85-88`
("measurably broader than the ratio concept ... disclosed rather than special-cased") already shows the strain at the KPI
grain. At the theme grain the list does not fit at all.

**RECOMMENDATION (labelled; the CTO rules).** **D for round 42, and close FWD-18 on its own DONE WHEN with the names that have
real terms. Do not pursue A.** If Andrew wants ASML-class names followable, cut **B** as one later enrichment cell, gated by a
read-only census first. That census measures B's rule over all 163 bodies, with the denominator and a false-positive count, and
B is cut only if the 112 shrink materially. The case for this order: A buys 5 of 112 and keeps the wrong population. B targets
the right population (themes), but its yield on bodies is unmeasured. FWD-18 is the PRD's own "cut LAST, deferrable" item.

## 5. WHAT THIS NOTE DID NOT MEASURE

- B's yield over the pillar BODIES. The proxy above covers titles only and is not a measurement of B.
- The 49 unstructured `thesis_pillars` entries (ABSENT reasons), and the kpi_set rows, which use the same lexicon and were not
  re-read.
- How often headlines in the header feed name any pillar's theme. That is the feed side of FWD-18, not read here.
- Any Andrew-direct record on pillar terms beyond the PRD SOURCE lines and the scan's order.
