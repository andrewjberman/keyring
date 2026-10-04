# AMGT_HARVST task order -- `HVST-ar-1` -- ROUND 45 CHAIN A (FWD-2; round-44 analysis ruling 1, enrichment item 1): EVERY FIELD THE PUBLISHER SENT IS TYPED IN SILVER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ar-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~93</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code, plants and READ-ONLY S3 (list/get on the harvest bronze and silver prefixes). No S3 write, no upload, no outbox change, no vendor call. The served re-derivation is the issuer's act after the merge, under a never-widen pair.
comp-adversary: RUN at L5 -- the adversary is a typing that changes a pre-existing silver column's value (a never-widen breach), a value stringified or reshaped instead of kept verbatim, a "typed" field that is only re-serialised into page_config_json, site chrome typed as an article field, or a census whose in-memory rows come from different code or different originals than the served path would use.
</preflight>

## 0. THE CELL

**FWD-2 DONE WHEN:** "every field present in the received article (including language, paywall flags, the publisher's own ticker
tags, sentiment, themes and summary where sent) appears typed in the queryable table, rebuilt from the stored original, and a query
by company and date returns it".

Round 44's field census (`org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round44/aq-1.field_census.py`; its result
`aq-1.field_census.json`; its reading `aq-1.READ.md` in the same folder) sampled <= 50 stored originals per publisher and checked each
leaf against the silver row rebuilt from that original. sa PASSES. barrons, bbg, ft and wsj LOSE fields:
- **barrons:** ticker tags (`articleMeta.properties[].symbol`, `.properties.ticker`, `.properties.internalSymbol`, `tickers[]...`,
  `snippet[].content[].ticker` and kin), paywall flags (`isFreeArticle`, `isBICPaywall`, `isServerUnlockedArticle`, `paywallIndex`),
  themes (`djmlKeyword`, `subjectName`, `articleMeta...topicId`, `endpoints.barronsTopics`, `snippet[].data.section`), summary
  (`articleToolsProps.summary`, `dek`, `snippet[].data.description`).
- **bbg:** `html_lang`, `__NEXT_DATA__.query.lang`, `ld[other].isAccessibleForFree`, and the page meta keywords / parsely-section /
  lotame category and topic.
- **ft:** `html_lang`, and the article JSON-LD `publisher` block (`ld[article].publisher.@type`, `.legalName`, `.url`, `.logo.*`,
  `.sameAs[]`).
- **wsj:** `html_lang`, `__NEXT_DATA__.locale`, `ld[other].inLanguage`, `ld[other].isAccessibleForFree`,
  `ld[other].hasPart.isAccessibleForFree`, meta `keywords` / `news_keywords` / `page.section` / `cXenseParse:*` / `article:section`,
  `ld[other].articleSection`, `ld[other].keywords[]`, `ld[other].description`, `ld[other].author[].description`. Also: 3 of 50 sampled
  wsj originals have NO silver row (`wsj/harvest/bronze/article/article_hash=b27bbdc2.../20261002T064907Z.html`,
  `cc8d1d4d.../20261002T062437Z.html`, `f721b35d.../20261002T064733Z.html`; full keys in the census JSON under
  `publishers.wsj.no_silver_row_for_sampled_bronze`).

**The exact target list is the grader's output.** Print it at any time:
`python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round45/checks/ar1_grade.py org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round44/aq-1.field_census.json BASE`
(today: lost per publisher barrons 39, bbg 10, ft 9, sa 0, wsj 20). The grader's CHROME rule (navigation menus, translation strings,
ad config, the reader's session state, follow-button config, author-byline props, live market quotes) is fixed; do not edit it and do
not type chrome.

`lib/opal_data_harvest/silver_from_bronze.py` builds silver rows from bronze bytes (pure functions; `article_rows(...)`), with one
extractor per publisher (`_extract_barrons`, `_extract_bbg`, `_extract_bbg_html`, `_extract_ft`, `_extract_wsj`). Its contract: every
vendor field present in bronze is kept, a nested dict stays a struct, a list stays a list, nothing is filtered or summarised; a string
is retyped only for a field named in `TIMESTAMP_FIELDS`. The field helpers `json_fields`, `typed_blocks`, `typed_text` live in
`lib/opal_data_harvest/publishers.py`.

## 1. THE BUILD (LOCAL; read-only S3; no write anywhere outside this worktree)

1. **Type every lost path** on the target list as a silver column carrying the vendor's value VERBATIM (a dict stays a struct, a list
   a list, a scalar its type). Page-level descriptors (`<html lang>`, `<meta>` keywords and sections, JSON-LD `inLanguage`,
   `isAccessibleForFree`, `description`, `keywords`, `articleSection`, the ft JSON-LD `publisher` block) become columns of the article
   row they came with. Name each new column so the census's leaf matcher finds it (same final key and value; see `index()` and
   `last_key()` in the census). Barrons first.
2. **Never widen:** every column a silver row carries TODAY keeps its exact value for every stored original. Only columns are added.
3. **The 3 wsj originals with no silver row:** find the cause from the stored bytes and the builder. If the builder drops or fails
   them, fix it so each yields its row. If the cause is outside the builder (for example never uploaded), say exactly where, with
   evidence, in your report.
4. **The census, in-memory mode:** copy `round44/aq-1.field_census.py` to
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~93/ar-1.field_census.py` and add two flags:
   - `--out <path>` (the JSON record path; default unchanged);
   - `--in-memory`: for each sampled original, the compared silver row is built by THIS checkout's `silver_from_bronze.article_rows`
     from the stored bytes (the same arguments the upload path passes), instead of read from served silver. Same deterministic sample,
     same leaf classification, same JSON shape. Without `--in-memory` it reads served silver exactly as aq-1 did.
5. **The re-derivation manifest (dry run, read-only):** a script
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~93/ar-1.rederive_manifest.py` that, for EVERY stored original
   of barrons, bbg, ft and wsj, builds the new row in memory and compares it with the served silver row of the same `bronze_key`
   (latest `run_stamp`). Write `ar-1.rederive_manifest.json` beside it and print per publisher: originals, rows that gain columns,
   columns added (names), rows whose PRE-EXISTING columns change (must be 0; list any), originals with no served row, and build errors.
   This is what the issuer's never-widen half signs, so it must be exact.
6. **Plants** in `lib/opal_data_harvest/test_ar1_silver_fields.py`, no network: for each of barrons, bbg, ft and wsj, one REAL stored
   original copied as a fixture under `lib/opal_data_harvest/fixtures/silver/` gives a row carrying the new columns with the vendor's
   values; a row's pre-existing columns are unchanged by the typing; a mutant without the typing fails. Read originals read-only from S3
   (bucket and prefixes via `lib/research/harvest/store.py`: `HARVEST_BUCKET`, `table_prefix(src, "bronze", "article")`).
7. Readers stay green on mixed parts: `python -m pytest lib/opal_data_harvest -q` and `python -m pytest lib/research/harvest -q`.
   Report both counts. If a silver or gold reader cannot read old and new parts together, that is a BLOCKING row, not a workaround.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r45-93`, branch `wk-AMGT_HARVST-93-r45a`, cut from CLOUD at the issuance commit
(sparse cone, decomposition section 50). Do not touch any `.runtime` directory. Every invocation below may take minutes (S3 reads);
it terminates.

<paths>
lib/opal_data_harvest/silver_from_bronze.py
lib/opal_data_harvest/publishers.py
lib/opal_data_harvest/test_ar1_silver_fields.py
lib/opal_data_harvest/test_silver_from_bronze.py
lib/opal_data_harvest/fixtures/silver/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~93/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ar-1"><invocation>python -m pytest lib/opal_data_harvest/test_ar1_silver_fields.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ar-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round45/checks/ar-1.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ar-1"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round45/checks/ar-1.AC3.py</invocation><expect>AC3 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 runs your census with `--in-memory` and grades it. AC3 is graded by the ISSUER after the merge and the served re-derivation;
  record it as "issuer-graded after re-derivation" and do not run it.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~93/AMGT_HARVST.TO-HVST-ar-1.silver-field-typing.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ar-1.silver-field-typing`.
- Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-44 analysis @ed9efe80ea ruling 1 and enrichment item 1. Decomposition section 58. AC3 is graded after the
issuer re-derives served silver from the stored originals under a never-widen pair (COO half from the manifest; CTO half owed), by the
round-37 aj-8 path (re-pend the outbox rows of exactly the manifest's originals, then `upload-harvest`). The fourth-criterion slot is
unused.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>issued</status>
<round>45</round>
<slot>~93</slot>
<fabric>site-z</fabric>
