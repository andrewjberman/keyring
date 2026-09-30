# AMGT_HARVST task order -- `HVST-i-2` -- ROUND 19 chain 1 of 1, cell 2 of 4: A PARTIAL DAY NAMES ITS PUBLISHER -- the rule keeps the covering publisher codes, and both timeline routes carry them; proved in memory

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-i-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~46</issued_to>
<issued_by>2.0.0_SA_COO~H</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- 2 armed gates fabric-wide, none on publication_gold.py, timeline_api.py or the harvest gold prefixes.
comp-iam: RUN at L5 -- `comp-iam service opal-amgt-scoped-api` reads 4 DynamoDB calls UNRESOLVED/UNGRANTED in lib/research/api/scoped_amgt.py (pre-existing RESAPP reads, untouched here); this cell adds NO boto3 call. S3 GET/LIST only; NO PUT.
comp-adversary: RUN at L5 -- the adversary is a schema change that moves an existing served cell, or a served route that errors on an OLDER daily part without the new column (the deployed API reads whatever part is newest). AC1 names a tolerance test; AC2 requires every pre-existing column unmoved on every row.
</preflight>

## 0. BEGIN ONLY WHEN

`HVST-i-1` is complete and merged on CLOUD. You are the same slot; the issuer continues you with its merge named. Use
`i-1`'s securities file for every build in this cell:
`org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/securities.universe.json`.

## 1. THE STANDING CLAUSES

1. **NO S3 WRITE OR DELETE, NO VENDOR CALL, NO DEPLOY.** The served rebuild is `HVST-i-3` under its own never-widen
   pair; the deploy of the API is `HVST-i-4`, a CloudOps seat's order.
2. **Scripts in** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/scripts/`; outputs named
   `i2_*` -- **never `.scratch/`.**
3. INSTANCE NAMED EXACTLY
   `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/AMGT_HARVST.TO-HVST-i-2.a-partial-day-names-its-publisher.proof_of_spec.json`
   **with `to_id`** `AMGT_HARVST.TO-HVST-i-2.a-partial-day-names-its-publisher`.

<paths>
lib/research/harvest/publication_gold.py
lib/research/harvest/timeline_api.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/
</paths>

## 2. THE CELL (`ledger/ROUND_ANALYSIS.round18.md` @`d11fd4d089`, s.2 ruling 1 and s.4 item 1)

**The defect:** a served PARTIAL day cannot say WHO covered it.
- The daily rule computes the covering publishers
  (`covered = [pub for pub in ENABLED_PUBLISHERS if _covers(publisher_spans.get(pub), day)]`,
  `publication_gold.py` ~:647).
- It keeps only `len(covered)` as `publishers_covered` (~:675).
- The served `/timeline` series entry (`timeline_api.py`, the entry builder ~:200-222, and `SERIES_STORED_FIELDS`
  ~:109) passes `data_status` and omits both the count and the codes.
- `timeline_day` (~:328-336) passes `data_status` only.

**The change, and only this:**
1. `chatter_daily` gains ONE column, `publishers_covered_codes`: a list of strings, the covering publisher codes in
   `ENABLED_PUBLISHERS` order. Its length equals `publishers_covered` on every row. The parquet schema declares it. No
   existing column's name, type or value changes.
2. The `/timeline` series entry and the `timeline_day` body each carry BOTH `publishers_covered` (int) and
   `publishers_covered_codes` (list). Update the field-list constants the check scripts diff against.
3. **Tolerance:** a daily row read from an OLDER part without the column serves `publishers_covered_codes: null`, with
   `publishers_covered` as stored, and never raises.
4. The page's wording of the publisher is DSGN_AMGTV1's. Serve the codes, not display names.

## 3. PROOF OF SPEC (each invocation LITERAL; timeout 900). TWO mechanical

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-i-2"><invocation>python -m pytest lib/research/harvest/tests/ -rA --tb=line</invocation><expect>the harvest suite passes with new tests NAMED in the -rA output: a daily row carries publishers_covered_codes equal to the covering publishers in ENABLED_PUBLISHERS order and len == publishers_covered (a PARTIAL day names its code, a DENIED day names none, a COMPLETE day names all); the /timeline series entry carries publishers_covered and publishers_covered_codes; the timeline_day body carries both; a daily row WITHOUT the column serves publishers_covered_codes null and does not raise; the pass count BEFORE and AFTER printed (base: the i-1 drain's count) and the collected count not falling</expect></criterion>

  <criterion id="AC2" cell_refs="HVST-i-2"><invocation>python org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~46/scripts/i2_ac2_codes_in_memory.py</invocation><expect>THE REBUILD, IN MEMORY, OVER TODAY'S INPUTS with i-1's securities file, set beside the SERVED newest chatter_daily part: (a) every PRE-EXISTING column equal on every row, denominator printed (51,952 at the cut), any difference printed in full and attributed DRIFT, with 0 non-DRIFT differences; (b) the new column: row counts per data_status class; every PARTIAL row names >= 1 code, every DENIED row names 0, len(codes) == publishers_covered on EVERY row; every security with a PARTIAL day listed with its day count and its codes (ASML_NA_Equity and ASML_US_Equity 74 days each naming sa at the cut); (c) the /timeline and timeline_day bodies built by timeline_api over these in-memory rows (loaders stubbed to them) for ASML_NA_Equity and FDX_US_Equity, printing one PARTIAL and one DENIED entry each where they exist. PASS only if (a)-(c) print and (a) holds</expect></criterion>
</proof_of_spec>

## 4. WHAT THIS CELL DOES NOT DO

No gold write, no deploy, no change to `data_status` or any other existing column's rule, no mention or event change,
no portal work, no vendor call.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6):**

1. **Measured at the cut:**
   - Deployed `/timeline` for ASML_NA_Equity: 272 series days (PARTIAL 74, DENIED 198). Every entry lacks both fields,
     and `timeline_day` 2026-07-15 returns keys `articles`, `data_status`, `date` and `security_key`
     (`round19/checks/i-4.AC1.base.txt`).
   - The rule already computes `covered` (`publication_gold.py:647`).
2. **Why the rule is its own LOCAL cell ahead of the served rebuild:** NEVER-1 reads the expected outcome from the
   producer's own rule at signing. That rule does not exist until this cell merges (the `g-1` -> `g-2` pattern).
3. **`timeline_api.py` is packaged into `opal-amgt-scoped-api`,** so its change reaches users only through `HVST-i-4`
   (the WORLD deploy seat). Until then the deployed API ignores the new column, so the tolerance runs both ways.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>19</round>
<slot>~46</slot>
<fabric>site-z</fabric>
