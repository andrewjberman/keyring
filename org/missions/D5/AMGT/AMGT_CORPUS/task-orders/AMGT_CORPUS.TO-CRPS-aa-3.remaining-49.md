# AMGT_CORPUS task order -- `CRPS-aa-3` -- ROUND 25: the 49 still-UNRESOLVED served units by class, 6861_JP first

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-aa-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (a map commit and re-derive are a later issuer act under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 25. Serves **every served figure's unit**.

## 1. THE CELL -- `CRPS-aa-3`

**Where this came from.** After round 24, the newest served model block of 98 keys carries **49 figures whose unit reads
`UNRESOLVED-ON-<security>: <reason>`**. That count excludes `BP/_LN_Equity` and `NG/_LN_Equity`, which are EXCLUDED under
`Z-S64` and must be named as EXCLUDED in your table.

The round-24 census (`deliverables/0.9.0_WK_AMGT_CORPUS~1/UNRESOLVED_CLASSES_ROUND24.json`, read-only to you) names them:
- `6861_JP_Equity`, 26 figures (BOOK_VAL_PER_SH 11, REVENUE_PER_SH 11, BEST_EPS 3, CURR_ENTP_VAL 1): `EQY_FUND_CRNCY` is not
  stated, so no same-currency read ran;
- `939_HK_Equity` `BS_TOTAL_LIABILITIES`, 10 figures: HKD listing against CNY reporting, with no stored anchor;
- `BBSE3_BZ_Equity` `CAPITAL_EXPEND`, 10 figures: a tiny value (0.058) in no plausible band;
- `BA_US_Equity` `BEST_PE_RATIO`, 2 figures: the 1FY consensus is absent;
- `TSM_US_Equity` `CURR_ENTP_VAL`, 1 figure: USD listing against TWD reporting, with no anchor.

The unit comes from `integrations/bloomberg/research/field_map.json`, built by `integrations/bloomberg/research/build_unit_map.py`
(`classify_unit`, `unit_from_basis_zero`, the same-currency bands against `PX_LAST` / `CUR_MKT_CAP`, the round-21 discriminator
inside `build_entries`). It is read per figure through `model_block_pull._resolved_unit`.

**RULED -- what you build (6861_JP FIRST, being more than half):**
1. **The class table, BY CENSUS:** `deliverables/0.9.0_WK_AMGT_CORPUS~3/UNRESOLVED_CLASSES_ROUND25.json` (+ `.md`), covering every
   UNRESOLVED figure of the newest served block of each non-slash key.
   - Its shape: `{"denominator_keys": 98, "excluded": [{"key": "BP/_LN_Equity", "row": "Z-S64"}, {"key": "NG/_LN_Equity", "row":
     "Z-S64"}], "before_total": 49, "classes": [{"mnemonic", "reason_class", "securities": [...], "count", "disposition":
     "family"|"stays_unresolved", "reason"}], "remaining_after": <int>}`.
   - The class counts sum to `before_total`.
2. **6861_JP:** establish its reporting currency by a STATED read before any family applies. Examples: a stored raw field that
   names it, or the name's own statement figures against a same-block quantity in a known currency. If none is stored, the limit
   is stated in the class `reason`; never assume JPY because the listing is JPY.
3. **The families that close a class.** Only where the census names a real, stated rule: a field-basis definition, or a
   cross-field read in the same currency. NEVER a default scale, magnitude alone, or an invented FX rate. Each change goes into
   `build_unit_map.py`'s classifier, with its ground in a code comment.
   - A class you cannot close stays UNRESOLVED, with its `reason` in the table.
4. `remaining_after` is the UNRESOLVED count your builder leaves. The issuer's checker recomputes it independently: it rebuilds a
   temp copy of the committed map over the crosswalk population and resolves every figure through the reader. The two must agree.
5. `integrations/bloomberg/research/tests/test_build_unit_map_families_round25.py` (new):
   - one test per family added;
   - one test that an unclosable class stays UNRESOLVED;
   - no network.
   Keep the builder's suites green.
6. Do NOT write the committed `field_map.json`, do NOT touch `model_block_pull.py` or `unit_anchor.py`, and do NOT derive.

## 3. SURFACES

<paths>
integrations/bloomberg/research/build_unit_map.py
integrations/bloomberg/research/tests/test_build_unit_map_families_round25.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/UNRESOLVED_CLASSES_ROUND25.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/UNRESOLVED_CLASSES_ROUND25.md
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-aa-3.remaining-49.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-aa-3.remaining-49.md
</paths>

READ-ONLY: every other file (`field_map.json` NEVER written), every S3 object. Scratch `.scratch/aa3/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`). Never disable the sparse checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO write to `field_map.json`, NO derive.
- Any long-running script you write runs from a NAMED file with `python -u` (never a heredoc).
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W3-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-aa-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round25/aa3_AC1.sh</invocation><expect>(?m)^aa3 keys 98 excluded 2 measured_before 49 table_total 49 classes [1-9]\d* dispositions_complete True projected_after \d+ table_remaining \d+ consistent True$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-aa-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round25/aa3_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: your table must sum to the checker's own served count (49 over 98 keys, 2 EXCLUDED), and every class must carry a
  disposition and a reason. Your `remaining_after` must equal the checker's independent projection of your builder. How many you
  close is reported, not demanded.
- AC2: your family tests with the builder's suites, including round 24's.

## 6. WHEN YOU ARE DONE
1. Write the instance at the proof path in section 3.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE with:
   - each AC line;
   - 6861_JP's reporting-currency read and its outcome;
   - each family added, with its ground;
   - what stays UNRESOLVED and why.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-24 analysis ruling 3 and enrichment item 3 @`0cdf1b748d` (msg 27200). Dry-run at base CLOUD `98781013e0`
(worktree `C:/tmp/coox-crps25-issue`):
- aa3_AC1 FAIL as expected: `aa3 keys 98 excluded 2 measured_before 49 table_total 0 classes 0 dispositions_complete False
  projected_after 49 table_remaining -1 consistent False`. The served count and the builder projection agree at 49.
- aa3_AC2 FAIL as expected (no tests ran).

Write set disjoint from aa-1: aa-1 owns `model_block_pull.py`; aa-3 owns `build_unit_map.py`.
<risk>LOCAL</risk>
<status>pending</status>
<round>25</round>
<slot>~3</slot>
<fabric>site-z</fabric>
