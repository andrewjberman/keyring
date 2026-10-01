# AMGT_HARVST task order -- `HVST-ai-4` -- ROUND 36 REPAIR (CTO msg 28084): A bbg HTML BRANCH IN silver_from_bronze SO THE 772 STRANDED bbg ARTICLES DRAIN TO SILVER/GOLD (row Z-S57)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ai-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~91</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code + plants; the drain is the live bbg driver's own upload step after the issuer merges; no Secrets write; no gold write.
comp-adversary: RUN at L5 -- the adversary is a branch that "parses" a bbg page into an empty or wrong row (title or date missing), or that changes the JSON path for another publisher. Plants use a REAL stored bbg HTML body and a JSON-publisher control.
</preflight>

## 0. THE CELL (CTO ruling msg 28084; row Z-S57)

The bbg backfill runs in-tab through the monthly sitemaps. It stores each accepted bbg article body as the full HTML
page (`ext` "html"). `lib/opal_data_harvest/uploads.py` `HarvestUploader` (lines ~186-235) builds the silver row from
those bytes through `lib/opal_data_harvest/silver_from_bronze.py` `article_rows` -> `_extract`, and `_extract` parses
bbg as JSON. Every bbg row therefore fails with `JSONDecodeError`: 772 of 779 rows are pending in the live bbg
outbox and 0 are uploaded.

The bbg ACCEPTANCE already parses the same HTML: `lib/opal_data_harvest/publishers.py`, bbg article parse (read it).
The new branch must reproduce that parse, not invent one. Real stored bodies are in the main tree:
`C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest-bbg/progress.sqlite3`, table
`harvest_raw_outbox`, column `path`. Read-only.

## 1. THE BUILD (LOCAL), bounded by the ruling

1. In `_extract` / `article_rows`, add a bbg HTML branch, taken only when the bbg body is HTML (it starts with
   `<!DOCTYPE` or `<html`, after whitespace). It yields the same fields the JSON path yields: title, article id,
   published, text blocks and vendor fields. The bbg JSON path and every other publisher's path are unchanged.
2. Plants in `lib/opal_data_harvest/test_ai4_bbg_html_silver.py`:
   - (i) one REAL stored bbg HTML body, copied as a fixture into `lib/opal_data_harvest/fixtures/silver/bbg_article.html`,
     parses to a row with a non-empty title, the article id, a published date in 2026 and non-empty text blocks;
   - (ii) a JSON-publisher control (the existing sa or bbg-JSON fixture the suite already carries) still parses
     byte-identically to before;
   - (iii) a mutant that removes the branch fails (i).
3. The collector suite (`python -m pytest lib/opal_data_harvest/ -q`, base 523 passed, 3 skipped) stays green.
4. Do NOT drain: the issuer merges, then the live bbg driver's next upload drains the outbox. The issuer prints the
   pending count before and after, which is AC2.

<paths>
lib/opal_data_harvest/silver_from_bronze.py
lib/opal_data_harvest/test_ai4_bbg_html_silver.py
lib/opal_data_harvest/fixtures/silver/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ai-4"><invocation>python -m pytest lib/opal_data_harvest/test_ai4_bbg_html_silver.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ai-4"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round36/checks/ai-4.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 is graded by the ISSUER after the merge and the drain (the live outbox is in the main tree). Write the proof
  instance with AC1 and AC2 marked "issuer-graded after drain", and leave `<status>` open.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~91/AMGT_HARVST.TO-HVST-ai-4.bbg-html-silver-repair.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ai-4.bbg-html-silver-repair`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 28084 (YES, bounded). Carried as workstream `bbgsilver` of round 36 (its own scope: the silver parser; disjoint from ai-1..ai-3), so ONE ISSUER PER ROUND holds per workstream. Gold #4 runs only after this cell drains and its census shows 0 rows
gone and 0 changed outside the new bbg rows; if it is not drained by 10:00Z, #4 runs without it, before 13:00Z.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>open</status>
<round>36</round>
<workstream>bbgsilver</workstream>
<slot>~91</slot>
<fabric>site-z</fabric>
