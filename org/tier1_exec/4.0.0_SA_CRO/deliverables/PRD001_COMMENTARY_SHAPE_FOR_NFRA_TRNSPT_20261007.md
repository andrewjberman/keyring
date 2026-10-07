# PRD-001 Commentary (Alyssa): the shape, for NFRA_TRNSPT's second commentary source

**For:** `1.0.0_SA_CTO~DELL2`, answering msg 751 (the asks in order).
**From:** `4.0.0_SA_CRO~D2`, 2026-10-07 ~15:25Z.
**Record:** `ANDREW_DIRECT_20261007_151xZ_PRODUCT_ALYSSA_RECON_CIO_HUNT_COMMENTARY_SUBSTRATE_TOP3_AUTOMATION.md`.

**Instrument.** The opalgateway MCP, with `list_site_files` and `read_site_file`, over SharePoint site `Shared`, path
`Shared Documents/Product-Alyssa/PRD-001_commentary/`. Nothing was downloaded; file text was read into the session
only.

**Claim key.** Every value carries a claim tag:
- **measured**: read from the bytes this session;
- **held**: Alyssa's own written statement, not re-run by me;
- **absent**: not present on the drive.

## 0. The headline: no database exists yet

- **[measured]** No `commentary.jsonl` or other store sits anywhere in `PRD-001_commentary/`.
- **[held]** The PRD (v1.1, draft, 2026-09-23) lists the field extractor as "not built", and its contract is "not yet"
  frozen.

What does exist, by kind:
- **a finder:** `src/classify.py` plus its scorer `src/evaluate.py`;
- **a schema:** `assets/SCHEMA_v2.md` plus the PRD's section 8;
- **one hand-made mock record:** `assets/mock/commentary_record.json`;
- **a labelled email corpus:** on Alyssa's laptop only.

So the "second source" is a design plus a labelled corpus, not a populated store.

## 1. Record count

| Population | Count | Claim | Where |
|---|---|---|---|
| Records in a built database | 0 | measured (absent) | n/a |
| Emails pulled for labelling | 183 unique, Mar to Sep 2026 | held (`assets/FINDER_REPORT_2026-09-23.md`) | Alyssa's laptop |
| Labelled real commentary after her review | 70 (113 look-alikes) | held (same report) | same |
| Labelled real commentary before her review | 78 | held (same report) | same; `fixtures/labels_v1_before_review.csv` |
| Mock records on the drive | 1 | measured | `assets/mock/commentary_record.json` |

## 2. Fields

PRD-001 section 8, `commentary`, has one row per email: 10 fields plus an id. **[measured]**

| # | Field | Type | Rule (held, from SCHEMA_v2 and the PRD) | In NFRA_TRNSPT gold? (measured against `org/standards/NFRA_TRNSPT_COMMENTARY_GOLD_CONTRACT.json`) |
|---|---|---|---|---|
| - | `record_id` | text | hash of the Graph message id | yes |
| 1 | `sent_at` | ISO datetime UTC | email header | yes |
| 2 | `body_text` | text | HTML to text; cut at the reply header and at "Best,"; subject client tokens become `[CLIENT]`; account-number patterns stripped | yes |
| 3 | `yc_variant` | 1/2/3 | computed from field 4: 0 models = 1, 1 = 2, 2+ = 3 | yes |
| 4 | `models_referenced` | list of model codes | fixed Opal model-name dictionary over the body and PDF names | yes |
| 5 | `account_type` | text | keyword match: ira / roth / 401(k) / brokerage / trust, else household | yes |
| 6 | `holdings` | list of tickers | the YCharts PDF holdings table in the thread; fallback is the request sheet | yes, but as nullable `string`, not a list |
| 7 | `mention_rate` | number 0-1 | holdings named in body / count of holdings | **no** |
| 8 | `themes` | ordered list of {theme, client, model} | bold headings in order, plus the first "X% versus Y%" in each paragraph | yes, as {theme, client_figure, model_figure} |
| 9 | `approved` | bool | a later Manav reply starting "Looks good" / "Good to go" / "Approved" | **no** |
| 10 | `model_as_of` | date | the email date, joined to the Bloomberg `model_weights` on (model, as_of) | **no** |

Five fields are in TRNSPT gold only:
- `recipient_firm`
- `paragraph_hashes`, `body_hash`
- `pdf_sha256`, `has_pdf`
- `request_text`

**Naming drift inside Alyssa's own folder [measured]:**
- `SCHEMA_v2.md` calls field 3 `model_variant`; the PRD calls it `yc_variant`.
- SCHEMA_v2 has 9 fields plus an id; `model_as_of` was added on 9/23. Its join table there is named `model_snapshots`,
  holding derived stats; the PRD instead joins raw `model_weights` and computes at read time. The PRD is the later
  text.

## 3. Labelled by report or by variant?

- **By variant, yes [measured].** `yc_variant` is 1 = Overview (no model), 2 = one-model Comparison, 3 = Multi-Comp.
  It is derived from `models_referenced`, so the two cannot disagree.
- **By report, no [measured].**
  - No YCharts report id or PDF hash field exists.
  - Linkage to the report is only the classifier gate `ycharts_linked()`: the thread mentions YCharts, a stress test
    or a multi-comp, or carries a PDF.
  - TRNSPT gold's `pdf_sha256` is the closer report key.
- **Quality label:** `approved`, Manav's no-edit reply. It marks gold-standard examples. Not in TRNSPT gold.

## 4. Date span

- **[held]** The labelled pull covers March to September 2026. The PRD backfill is defined from 2026-03-01 to date.
  The mock record is dated 2026-09-15.
- **[held]** About 3 new commentaries a week.

## 5. Where the source bytes live, and who wrote them

| Bytes | Location | Authored by | Claim |
|---|---|---|---|
| The source emails | M365 mail. The mailbox scope is open (PRD Q1: Alyssa only, Manav, or a 49F shared box) | Opal staff | held |
| 183 labelled raw Graph messages + `labels.csv` | `C:\Users\AlyssaKeith\Claude Files\YCharts Commentary DB\fixtures\`, "deliberately not on the shared drive" (it holds client PII) | Pulled by Alyssa's Claude agent; labels made by Claude, ambiguous ones reviewed by Alyssa 9/23, some left as Claude labelled them | held |
| Finder code `classify.py`, `features.py`, `evaluate.py` | SharePoint `PRD-001_commentary/src/` | Alyssa's agent | measured |
| Schema, finder report, mock, PRD | SharePoint `PRD-001_commentary/` | Alyssa's agent, from the 9/23 Andrew<>Alyssa Teams thread | measured |

**Finder accuracy [held, an upper bound by its own caveat; scored on the same 183 it was built from]:**
- 170 of 183 correct (92.9%); precision 90.1%; recall 91.4%.
- 0 real write-ups in `skip`.
- The held-out test is PRD Q5, still open.

## 6. Client names in it: counted, not printed

The denominator is the 11 text files read under `PRD-001_commentary/`:
- PRD.md, CHANGELOG.md
- assets/: FINDER_REPORT, SCHEMA_v2, mock record, README
- intake/: 2 dated notes
- alyssas-notes/NOTES.md
- src/: classify.py, evaluate.py

**Not read:** `versions/PRD_v1.0.md`, `src/features.py`, and the remaining README stubs. The counts below do not cover them.

| File | Client-like personal surnames | Partner or advisor names | Account-number-like token |
|---|---|---|---|
| `assets/FINDER_REPORT_2026-09-23.md` | 10 distinct | 2 | 1 |
| `PRD.md` (section 13 decisions log) | 3 distinct (a subset of the 10 above) | 1 | 0 |
| every other file read | 0 | 0 | 0 |

- The mock record carries tickers and percentages only: 0 names **[measured]**.
- The fixtures on Alyssa's laptop hold client PII by her statement, uncounted **[held]**.
- Classification is my reading of context: "written from a statement", "advisor model, not a client". It is
  **[inferred]**, not checked against a client roster.

## 7. What a TRNSPT addendum would actually gain

1. **The labelled corpus and its finder rules.** 70 positive and 113 negative examples, plus a deterministic
   classifier with a measured miss rate of 0 on its build set. This is ground truth for TRNSPT's ingest criterion.
   The bytes are on Alyssa's laptop and leave only by her act.
2. **Three fields TRNSPT gold lacks:**
   - `approved`: the quality label for few-shot selection;
   - `mention_rate`: the macro story vs a fund-by-fund cleanup;
   - `model_as_of` with the weights join.
3. **One rule for the drafter (intake, not yet folded into the PRD):** the commentary is held back from the advisor.
   The PDF goes out immediately; the commentary follows only after Alyssa's sign-off. Any drafter output is internal
   only.

-- 4.0.0_SA_CRO~D2
