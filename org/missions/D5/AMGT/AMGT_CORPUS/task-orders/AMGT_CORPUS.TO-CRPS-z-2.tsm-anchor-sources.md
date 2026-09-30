# AMGT_CORPUS task order -- `CRPS-z-2` -- ROUND 24: TSM's same-currency anchor -- every stored source searched, or the limit stated on the figure

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-z-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~2</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~2`**, slot `~2` of round 24. Serves **TSM's unit (row `Z-W2-S16`)**.

## 1. THE CELL -- `CRPS-z-2`

**Where this came from.** `TSM US Equity` lists in USD (`CRNCY`) and reports in TWD (`EQY_FUND_CRNCY`). So its `CURR_ENTP_VAL` has
no same-currency cross-field anchor, and stays UNRESOLVED.

Round 23 landed `integrations/bloomberg/research/unit_anchor.py` `same_currency_anchor(s3, security, header)`, which searches a
same-LEI line in the reporting currency, then a stored FX object with its date. `build_unit_map.discriminate_facts` calls it when
the two currencies differ, and appends its `reason`. Today it finds nothing: no `2330_TT_Equity` raw, and no FX field.

The CTO ruled (round-23 analysis, ruling 5): round 24 reads whether ANY stored source carries a same-currency figure for TSM. If none
does, the served reason states the limit in these words: "no same-currency anchor stored". No FX is invented.

**RULED -- what you build:**
1. **The census:** `deliverables/0.9.0_WK_AMGT_CORPUS~2/TSM_ANCHOR_SOURCES_ROUND24.json` (+ `.md`).
   - It covers every stored source that could carry a TWD figure or a TWD/USD rate for TSM: every bronze family under the
     producer's bucket, the served crosswalk records for TSM's issuer, and the model-block and gold stores you can list.
   - Its shape: `{"sources": [{"source", "where", "searched_count", "found": bool, "detail"}], "anchor": null | {"source",
     "source_key", "value", "currency", "as_of"}}`.
2. **If a source carries a usable same-currency figure:** extend `same_currency_anchor` to read it, with its `source_key` and date.
3. **If none does:** `same_currency_anchor`'s `reason` for a no-anchor result BEGINS "no same-currency anchor stored:" and then
   names what was searched. The served discriminator reason then carries the ruled words.
4. `integrations/bloomberg/research/tests/test_unit_anchor.py`: add a test that a no-anchor result's reason begins with the ruled
   words. Keep the existing 4 green.
5. Do NOT edit `build_unit_map.py` (another cell owns it) or `field_map.json`, and do NOT derive.

## 3. SURFACES

<paths>
integrations/bloomberg/research/unit_anchor.py
integrations/bloomberg/research/tests/test_unit_anchor.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/TSM_ANCHOR_SOURCES_ROUND24.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/TSM_ANCHOR_SOURCES_ROUND24.md
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-z-2.tsm-anchor-sources.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/z2/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`). Never disable the sparse checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO FX value typed into code.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W2-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-z-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round24/z2_AC1.sh</invocation><expect>(?m)^z2 sources_searched [1-9]\d* anchor \S+ reason_states_limit True fx_invented False census_file True$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-z-2"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round24/z2_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: your census lists the sources searched. Then, live, either TSM resolves on a stored anchor with its `source_key`, or its
  served reason states "no same-currency anchor stored". Never an invented rate.
- AC2: the anchor tests, yours included.

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~2/AMGT_CORPUS.TO-CRPS-z-2.tsm-anchor-sources.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE: each AC line, the sources searched with counts, and the anchor or the limit.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-23 analysis ruling 5 @`4cbd61daf8`. Dry-run at base CLOUD `da4fb630b5`:
- z2_AC1 FAIL as expected: `z2 sources_searched 0 anchor none reason_states_limit False fx_invented False census_file False`.
- z2_AC2 PASS as expected (bound: the 4 existing anchor tests stay green).
<risk>LOCAL</risk>
<status>pending</status>
<round>24</round>
<slot>~2</slot>
<fabric>site-z</fabric>
<status>complete</status>
