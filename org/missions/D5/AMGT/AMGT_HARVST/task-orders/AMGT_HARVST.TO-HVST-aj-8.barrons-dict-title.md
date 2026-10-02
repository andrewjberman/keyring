# AMGT_HARVST task order -- `HVST-aj-8` -- ROUND 37 CELL 8 (CTO 28525; row Z-W90-S17): BARRONS SILVER TITLES ARE DICTS -- UNWRAP THEM AS WSJ DOES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-aj-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~90</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code + plants; no S3 write (the issuer re-derives the 149 silver rows after the merge); reading one real barrons bronze body from the main-tree runtime is read-only.
comp-adversary: RUN at L5 -- the adversary is an unwrap that changes a title that was already a string (the 15 good rows, every wsj row), or one that turns a dict into its repr ("{'text': ...}") instead of its text, or one that drops a title the dict carried in a different key. Plants pin a string passing unchanged, a dict unwrapping to its text, and a real stored barrons body.
</preflight>

## 0. THE CELL

`lib/opal_data_harvest/silver_from_bronze.py`:
- `_extract_barrons` (around line 170) sets `title = article.get("headline")` raw.
- `_extract_wsj` (around line 201) does `title = props.get("headline") or typed_text(article.get("headline"))`, then
  `if isinstance(title, dict): title = typed_text(title)`.

Today's barrons pages (07:06Z onward) carry `headline` as `{"text": "..."}`. 149 of the 164 barrons silver rows
therefore hold a dict title, and the gold builder's `_match_counts` raises TypeError on them.

## 1. THE BUILD (LOCAL)

1. In `_extract_barrons`, unwrap a dict headline through `typed_text`, exactly as `_extract_wsj` does. A string
   headline passes unchanged.
2. Plants in `lib/opal_data_harvest/test_aj8_barrons_dict_title.py` (no network):
   - (i) a payload whose `articleData.headline` is `{"text": "X"}` gives row title "X" (a str);
   - (ii) a payload whose headline is the string "Y" gives "Y" unchanged;
   - (iii) one REAL stored barrons bronze body with a dict headline, copied as a fixture under
     `lib/opal_data_harvest/fixtures/silver/`. The bodies are under
     `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest/harvest_raw/`; the outbox path column
     names them, so read it read-only. That body gives a str title;
   - (iv) `publication_gold._match_counts(<that title>, ["X"], set())` does not raise;
   - (v) a mutant without the unwrap fails (i) and (iii).
3. The collector suite stays green: `python -m pytest lib/opal_data_harvest/ -q`.

Worktree: `C:/Users/Opal Bloomberg/Desktop/wk-hvst-r36-90`, branch `wk-AMGT_HARVST-90-r37f`.

<paths>
lib/opal_data_harvest/silver_from_bronze.py
lib/opal_data_harvest/test_aj8_barrons_dict_title.py
lib/opal_data_harvest/fixtures/silver/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 2. PROOF OF SPEC (each invocation LITERAL; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-aj-8"><invocation>python -m pytest lib/opal_data_harvest/test_aj8_barrons_dict_title.py -rA --tb=line</invocation><expect>passed</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-aj-8"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round37/checks/aj-8.AC2.py</invocation><expect>AC2 RESULT: PASS</expect></criterion>
</proof_of_spec>

- AC2 is graded by the ISSUER after the merge and the re-derivation. Mark it "issuer-graded after re-derivation".
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~90/AMGT_HARVST.TO-HVST-aj-8.barrons-dict-title.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-aj-8.barrons-dict-title`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO 28525 (YES, conditions 1-3). The issuer re-derives exactly the 149 rows (manifest), then grades
AC2, then re-runs aj-7 AC2, then prepares rebuild #5's never-widen pair. The CTO half is owed.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>37</round>
<workstream>barronstitle</workstream>
<slot>~90</slot>
<fabric>site-z</fabric>
