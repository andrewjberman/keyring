# AMGT_HARVST task order -- `HVST-n-2` -- ROUND 24 chain 2 of 5: SA'S MISSING FIELDS AND ROWS IN SILVER, AND "QUERY BY COMPANY" OVER THE MENTION JOIN (FWD-2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-n-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~57</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on lib/opal_data_harvest/ or the harvest prefixes; this cell writes nothing to S3.
comp-iam: RUN at L5 -- S3 GET/LIST only on s3://opal-data-harvest/ (bronze, silver, the newest mention part). NO PUT, NO vendor call.
comp-adversary: RUN at L5 -- the adversary is a silver fix proved on fixtures that never meets the real 5 + 6 sa objects, or a "query by company" that still keys on discovered_for (which means "found while searching for"). AC2 rebuilds the REAL objects in memory; AC3 prints both keyings side by side.
</preflight>

## 0. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL, NO DEPLOY.** This cell changes the silver builder and proves it IN MEMORY
   over the real bronze objects. If the change would move served silver rows, the served silver rebuild is a SEPARATE
   order under a never-widen pair, cut by the issuer after this cell drains. It is not this cell.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~57/scripts/`; outputs named `n2_*`
   -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~57/AMGT_HARVST.TO-HVST-n-2.sa-fields-and-rows-and-the-mention-query.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-n-2.sa-fields-and-rows-and-the-mention-query`.

<paths>
lib/opal_data_harvest/silver_from_bronze.py
lib/opal_data_harvest/test_silver_from_bronze.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~57/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 1. THE RULINGS (`ledger/ROUND_ANALYSIS.round23.md` @`d1ec6f4118`, s.2 rulings 2 and 6)

**Measured last round:**
- sa loses fields in silver on 5 of 46 articles (`links`, `type`, `meta.path`, `meta.page`, `meta.redirectPath`,
  `meta.proStatus`, all on the 5 `as_received` articles).
- 6 sa bronze objects (unlabelled) have no silver row.
- sa silver rows tagged `discovered_for` `992_HK_Equity` include titles not about Lenovo (AES, Barrick; row `Z-W53-S4`).

**The change:**
1. `silver_from_bronze.py` keeps every field sa sends, including those 6, typed.
2. `silver_from_bronze.py` builds a silver row for each of the 6 unlabelled sa bronze objects that is an article. Any
   that is not an article is named with the reason it gets no row.
3. **"Query by company" is a query over the MENTION JOIN** (gold `article_security_mention`'s alias-matched mentions,
   joined to silver on the article key), not over silver's `discovered_for`. `discovered_for` stays as FWD-3's
   provenance carrier, meaning "found while searching for". Define the query as a function or script; it is not a new
   table.

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900). THREE mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-n-2"><invocation>python -m pytest lib/opal_data_harvest/test_silver_from_bronze.py -rA --tb=line</invocation><expect>the suite passes with new tests NAMED in the -rA output: an sa as_received article keeps links, type, meta.path, meta.page, meta.redirectPath and meta.proStatus typed in silver; an unlabelled sa bronze article object yields a silver row; the pass count BEFORE and AFTER printed and the collected count not falling</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-n-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~57/scripts/n2_ac2_real_objects_in_memory.py</invocation><expect>OVER THE REAL SERVED sa BRONZE OBJECTS (S3 GET/LIST only), silver rebuilt IN MEMORY by the new builder: the 5 articles now carry every bronze field (missing count 5 -> 0, fields named), the 6 unlabelled objects each yield a row or are named with the reason they do not; and, beside the SERVED silver, every other row unchanged, with a count of served silver rows that WOULD move (denominator printed)</expect></criterion>

  <criterion id="AC3" cell_refs="HVST-n-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~57/scripts/n2_ac3_query_by_company.py</invocation><expect>For 992_HK_Equity on 2026-09-23 (and the whole-series count), rows returned by the MENTION JOIN against rows returned by discovered_for, side by side, with every row that differs listed by title: the AES and Barrick rows appear under discovered_for and not under the mention join; denominators printed</expect></criterion>
</proof_of_spec>

## 3. WHAT THIS CELL DOES NOT DO

No served silver rebuild, no gold rebuild, no vendor call, no S3 write, no change to `discovered_for`'s meaning.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **From `ROUND_ANALYSIS.round23.md` @`d1ec6f4118` s.3 item 2:** "LOCAL, then a silver rebuild under a pair if it moves
   served rows".
2. **AC2's would-move count decides whether the issuer cuts that paired rebuild.** The issuer cuts it after this cell
   drains, reading the expected diff from the merged builder at signing.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>24</round>
<slot>~57</slot>
<fabric>site-z</fabric>
