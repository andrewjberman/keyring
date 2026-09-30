# AMGT_HARVST task order -- `HVST-q-2` -- ROUND 27 chain 2: bbg's AS-RECEIVED ARTICLES PARSE INTO SILVER (row `Z-S44`; FWD-2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-q-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~71</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no scheduled writer (the collector task is Disabled). This cell changes the silver builder only; it writes no silver.
comp-iam: RUN at L5 -- S3 GET/LIST on the bbg bronze article objects (read-only). NO PUT, NO DELETE, NO vendor call, NO deploy.
comp-adversary: RUN at L5 -- the adversary is a parser that "passes" on a synthetic fixture shaped like the other publishers but still returns an empty row for bbg's real received bytes. AC2 parses the 11 REAL held bbg bronze objects read-only and requires each non-empty.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE, NO VENDOR CALL, NO COLLECTION, NO DEPLOY.** The served silver rebuild from bronze is a later paired act
   (round 28).
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~71/scripts/`; outputs named `q2_*`.
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~71/AMGT_HARVST.TO-HVST-q-2.bbg-as-received-parses-into-silver.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-q-2.bbg-as-received-parses-into-silver`.

<paths>
lib/opal_data_harvest/silver_from_bronze.py
lib/opal_data_harvest/test_q2_bbg_as_received.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~71/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE DEFECT (row `AMGT_HARVST-Z-S44`; `ROUND_ANALYSIS.round26.md` @`ff4405d3d5` ruling 4)

**Measured:**
- `store.silver_latest("bloomberg","article")` holds 11 rows fetched 2026-09-30 (HVST-o-5's upload). All 11 have title `''`
  and 0 `text_blocks`, so they yield no mention pair.
- The upload built each row with `silver_from_bronze.article_rows("bbg", <the as-received bytes>, "as_received", ...)`
  (`lib/opal_data_harvest/uploads.py` `HarvestUploader._run_articles`).
- The same builder parses wsj's and sa's as-received bytes.

**The change:**
- `article_rows` parses bbg's AS-RECEIVED response shape into the silver fields: title, text blocks, published date, and
  the rest its other forms already carry.
- Read the real bytes first. Name, by file:line, why the base returns empty.
- The normalised-record form and every other publisher stay byte-identical.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-q-2"><invocation>python -m pytest lib/opal_data_harvest/test_q2_bbg_as_received.py -rA --tb=line</invocation><expect>passed</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-q-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~71/scripts/q2_ac2_real_bbg_objects.py</invocation><expect>REAL BBG OBJECTS PARSED NON-EMPTY: 11 of 11</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-q-2"><invocation>python -m pytest lib/opal_data_harvest/ lib/research/harvest/tests/ -rA --tb=line</invocation><expect>0 failed</expect></criterion>
</proof_of_spec>

**What each criterion must print or prove:**
- **AC1:** a test built from one real bbg as-received body (a copied fixture) parses to a non-empty title and text. A
  mutant restoring the base parse FAILS it. An other-publisher fixture is byte-identical before and after.
- **AC2:** read-only GET of the 11 bbg bronze objects that the 2026-09-30 silver rows name (via each row's `bronze_key`).
  Print, per object, the title and the text-block count under the base and the new builder, with the count line exactly as
  in the expect. A shortfall prints its object and reason.
- **AC3:** the base is commit `ff4405d3d5`, pinned at cut. It prints the base and after pass counts, and the line
  `0 failed`.

## 3. MERGE ORDER

This cell merges only after `HVST-q-1` drains (ruling 6). The issuer holds the merge.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- `ROUND_ANALYSIS.round26.md` s.4 item 2.
- The served bbg silver rebuild is round 28, one rebuild covering this and `q-1`'s new bronze.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>27</round>
<slot>~71</slot>
<fabric>site-z</fabric>
