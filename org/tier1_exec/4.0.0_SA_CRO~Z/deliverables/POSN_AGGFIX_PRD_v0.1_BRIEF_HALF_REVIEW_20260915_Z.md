# L4-R REVIEW -- POSN_AGGFIX PRD v0.1 @d6bee5693c, BRIEF HALF -- REFUSE (one defect, by pinned line)

**Reviewer:** 4.0.0_SA_CRO~Z (brief half; `TREE_PRD_SIGNOFF`; the seated CRO lane for POSN_AGGFIX per `project.json`
`seats.cro`, and the L1 author of the brief this PRD cites)
**Delivered by:** `1.0.0_SA_CTO~Z` msg 23189, 2026-09-15T17:43:30Z. `prd-signoff.py status` routes this half to `~W`;
POSN is `~Z`'s, so the delivery is correct.
**Reviewed:** 2026-09-15 ~17:45-17:55Z, first review of this PRD
**Half reviewed:** brief, `half_hash` `f044e8d31df23efefab8c489507638f9329227ad201bc8e00974abef3f632490`, computed with
`prd_signoff_lib.half_hashes` on `git show d6bee5693c:<prd>` (34,442 bytes) and equal on the working copy

## CONTROLS RUN BEFORE THE VERDICT

| control | read | result |
|---|---|---|
| last touch of the PRD == the review pin | `git log -1 -- prd/` gives `d6bee5693c` (1.0.0_SA_CTO~Z, 2026-09-15T13:42:21-04:00); `git diff --stat d6bee5693c HEAD -- prd/` shows only the CVO's sign-off file added | MATCH |
| brief-half bytes unchanged since the pin | `half_hashes` at the pin and on the working copy, brief `f044e8d31d...` both | EQUAL |
| s.8 denominator | heading lines of the brief @1e268c164e outside fences, counted by a python pass: 31, title at `:1` | 31 less the title = 30; every s.8 line reference (`:14` ... `:403`) matches the census |
| S6 / S7 / S8 producer lines | native search of `lambda_function.py` at SITEZ HEAD: `load_aum_data` `:1421`, name map `:1437-1451`, legacy read `:1461`, `calculate_aggregated_holdings` `:1525`, AGG write `:1811`, `OUTPUT_KEY` `:2529`, `put_object` `:2618-2636` | MATCH |
| S9 grant | `infra/aws/terraform/yang-pipeline/iam.tf` printed `:30-50`: `S3ReadWrite` Get/Put/List/Copy on `opal-data-portal-v2` and `/*` | MATCH; a new key in that bucket needs no IAM edit |
| S10 module | `infra/aws/terraform/yang-pipeline/lambdas.tf` printed `:160-174`: `module "generate_positioning"`, artifact `yang-pipeline/yang-generate-positioning.zip` | MATCH |
| standards file keys | `data/mdpf/scripts/gold/dim_mdpf_aum_metrics.py` printed `:82-92`: `SERVED_MODEL_NAME` holds the seven canonical keys and served names the file restates | MATCH; `measured_against` restates brief F4 exactly (7 rows, 5 primary, 2 blend, 0 outside) |
| S4 scope, on a DIFFERENT instrument from the CTO's `comp-find` | native ripgrep `-i "x-user-tier\|userTier\|user_tier"` over `infra/aws`: 15 files; `auth-validator-edge/index.mjs` and `shared-advisor-router/index.mjs` present, `public-data-router` ABSENT | consistent with S4's "not found in the two functions the trace names"; the one edge function with tier references besides the injector is `shared-advisor-router`, a candidate for S4 to read first |
| **five-book byte identity vs the re-point (the defect below)** | producer `:1796-1798` at SITEZ `ec29ae6fae`; served `positioning_data.json` VersionId `aJ7nhwRKko3H_AMRzsNvvwkf1NiO9aou` walked in full for every value equal to a legacy AUM row; `git -C portal grep` over `src/pages/Positioning` at origin/PROD `edf85ce503` for book-level `aum` readers | see REFUSAL |

## REFUSAL -- ONE DEFECT: C-FIVE-BOOKS-UNCHANGED cannot hold under C-CURRENT-SOURCE as written

**The mechanism, measured.** The producer builds every model book as

```
lambda_function.py:1796-1798 @ec29ae6fae
        current_holdings[model_code] = {
            'holdings': holdings_list,
            'aum': aum_data.get(model_code, 0)
```

so each book's `aum` comes from the SAME `aum_data` dict that `load_aum_data` (`:1421`) fills from
`json/portfolios/aum-metrics.json` (`:1461`, `:1470`). The served file confirms it. A full walk of the served
`positioning_data.json` finds **exactly 6 values equal to a legacy AUM figure**: `/current_holdings/{UST,ST,INT,LT,ULT}/aum`
(52,360,822.93 / 129,227,888.01 / 444,315,640.92 / 804,605,507.26 / 206,634,320.89) and
`/current_holdings/AGG/total_aum` (1,637,144,180.01). 5 of those 6 sit INSIDE the five model books.

**Why the two properties collide.** C-CURRENT-SOURCE (PRD `:154-157`) says the producer takes its weights from the
current file and "stops reading `json/portfolios/aum-metrics.json`". Once `aum_data` is re-pointed, the five
book-level `aum` values stop being the July figures. They become the current figures (UST 65,550,660.50 on the
2026-09-14 file, brief F4), or zero, or absent, depending on the port. **Every branch changes bytes inside the five
books.** That contradicts, by pinned line:

1. **C-FIVE-BOOKS-UNCHANGED (PRD `:176-177`):** "The five model books in the shared served file are byte-identical
   before and after every producer change."
2. **S6 bound (PRD `:248`, last column):** "the five model books' inputs untouched". `aum_data` IS a five-book input.
3. **S8 bound (PRD `:250`, last column):** "the five books byte-identical in the shared file before and after".

A worker bound by these rows either fails its own before/after compare at S8 or S10, or keeps a legacy read for the
book-level `aum` and so fails C-CURRENT-SOURCE. No cell can satisfy both as written. That is why this refuses rather
than signs with a note: the decomposition would inherit an unsatisfiable pair.

**What it does NOT reach, measured at text grain.** The ratified FWD-8 ("the same holdings and weights") is probably
unaffected. `git -C portal grep` over `src/pages/Positioning` at origin/PROD `edf85ce503` finds `aum` readers only at
holding level (`HoldingsTab.tsx:966`, `:1582`, per-ETF AUM in millions) and on the ETF-mode adapter
(`etfAdapter.ts:157`, `book.aum` of the ETF payload). No Models-mode reader of `current_holdings.<code>.aum` shows
up. A positive control on the same ref (`Holdings Breakdown` in `HoldingsTab.tsx`) hit 2. **Not measured:** a
destructured or spread read on that page, and any consumer of `positioning_data.json` outside the Positioning
directory.

**So the fix is inside the brief half, and the CVO's ratified-text signature survives it** (the half hashes bind
separately; this review does not touch the ENDPOINT). The shape of the fix is 1.0.0_SA_CTO~Z's call. Two candidates,
recommendation first:

- **(recommended)** Scope C-FIVE-BOOKS-UNCHANGED, S6's bound and S8's bound to "holdings and weights, and every field
  except the five book-level `aum` values". Name those five values in C-NEVER-WIDEN's blast radius as moving from
  the July figures to the current ones. State whether each book's `aum` is the primary model's own row or includes
  its share of the blends, since C-MEMBERS makes both readable. Add the consumer census of
  `current_holdings.<code>.aum` to S2 beside the writer census.
- Or keep byte identity and carve a named exception into C-CURRENT-SOURCE for the book-level `aum`. That leaves the
  project still reading the legacy file and so contradicts ruling 5's premise (F9). Not recommended.

**The same root reaches C-NO-SILENT-EMPTY (PRD `:158-160`)**, which says "the five model books keep their current
behaviour". Today a failed weight read makes every book's `aum` 0 (`:1798`, `.get(model_code, 0)`), so "current
behaviour" includes a silent zero inside the books. v0.2 should say whether that survives.

## CONTENT CHECK -- s.8, each row CONTENT not pointer

| rows | verdict |
|---|---|
| 1-2 (why, map) | content present; the three findings each carried to the right consumer (FWD-2/FWD-7 advisor arms, C-GAP-EXPLAINED with S1, the Phase-1-alone branch moot on D1) |
| 3-10 (Part I, O1-O7) | content present; O4's date clause correctly RETIRED with FWD-5 on Andrew e); O7 correctly unconditional now that D3 is settled |
| 11-15 (Part II) | content present; row 15 adds the per-firm aggregate from Andrew b), which is right |
| 16 (Part III) | content present; each bar mapped. **Note:** "nothing else moves" maps to C-FIVE-BOOKS-UNCHANGED, the property refused above, and inherits the fix |
| 17-26 (Part IV, F1-F9) | content present with VersionIds and figures restated, not pointed at |
| 27 (Part V) | content present; item 3's "explained, the bar Andrew confirmed" is fair: the FWD-6 line he answered carries "explained". Item 6 maps to the refused property and inherits the fix |
| 28 (Part VI) | correctly CONTEXT, not a requirement |
| 29 (Part VII) | content present; item 11 RESOLVED is correct (LOCAL on CLOUD @`bd2fa195c0`, recorded on SITEZ) |
| 30 (Refs) | content present |

## NON-BLOCKING NOTES, by pinned line

1. **S4 (PRD `:246`).** `shared-advisor-router/index.mjs` carries tier references (the native search above) and is
   the obvious first read for "where, if anywhere, a tier refusal runs". Naming it in S4's MEASURED-BY would save
   the verify cell a search. It does not change the row's claim.
2. **C-ONE-BOOK (PRD `:148-149`)** reads Andrew b) "we just need it at global level" as "no aggregate per partner
   firm is built". The page also has an internal viewer's FIRM context (the "THE INTERNAL VIEWER'S FIRM" block in
   `Positioning.tsx` beside `:267` at origin/PROD). Whether the global aggregate shows while an internal viewer has
   a firm selected is not stated. S13 or S14 should settle it by reading the page; it is not a new decision.

## VERDICT

**REFUSE**, on the one defect above: C-FIVE-BOOKS-UNCHANGED (`:176-177`) with S6's bound (`:248`) and S8's bound
(`:250`), versus C-CURRENT-SOURCE (`:154-157`), through `lambda_function.py:1796-1798`. The stamp binds to the brief
half's bytes as reviewed (`--expect-half-hash f044e8d31d...`). Every other brief-half row reviewed here would sign as
written.
