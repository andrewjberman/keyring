# AMGT_CORPUS task order -- `CRPS-y-3` -- ROUND 23: a same-currency anchor for an ADR (TSM) -- a stored line or a stored rate, never an invented one

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-y-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~3</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 raw reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~3`**, slot `~3` of round 23. Serves **a unit on an ADR whose fundamentals report in another
currency (row `Z-W2-S16`)**.

## 1. THE CELL -- `CRPS-y-3`

**Where this came from.** `integrations/bloomberg/research/build_unit_map.py` `discriminate_facts` resolves a unit by a
cross-field ratio against `CUR_MKT_CAP`. It refuses a name whose listing currency (`CRNCY`) differs from its reporting currency
(`EQY_FUND_CRNCY`). TSM US Equity reads `CRNCY USD`, `EQY_FUND_CRNCY TWD`, so its `CURR_ENTP_VAL` stays UNRESOLVED. The CTO
ruled that the discriminator gains a same-currency anchor, in this order:
1. the TWD-listed line's market cap, where the store holds that line;
2. otherwise, a STORED, measured FX rate with its date.

**An FX rate is never invented or defaulted.** Measured at the cut, the store holds neither for TSM: `2330_TT_Equity` has 0 raw
objects, and the bronze families (article, bestdata, exec_officers, histdata, histdata_daily_px, identity, news_listing,
refdata) carry no FX field.

**RULED -- what you build:**
1. `integrations/bloomberg/research/unit_anchor.py` (new): `same_currency_anchor(s3, security, header) -> dict` returning
   `{"anchor": {"field", "value", "currency", "source_key", "as_of"} | None, "searched": [<each anchor tried, with where>],
   "reason": <str, why none, when None>}`.
   - When `CRNCY` equals `EQY_FUND_CRNCY`, the anchor is the name's own `CUR_MKT_CAP` (`source_key` = its refdata object).
   - When they differ: first a same-currency line in the store, found by a rule you state (e.g. the crosswalk's other listing for
     the same issuer), carrying its `CUR_MKT_CAP` and `source_key`; then a stored FX field or object with its date. Otherwise
     None.
   - Reads only the model_block_pull bucket's bronze and the served crosswalk. Imports what it needs from `model_block_pull` by
     path, as `build_unit_map` does.
2. It never returns an anchor without a `source_key` it read, and never computes a rate it did not read.
3. `integrations/bloomberg/research/tests/test_unit_anchor.py` (new), with a stub S3:
   - a same-currency name returns its own cap;
   - a planted TWD line resolves the ADR;
   - a planted stored FX rate with its date resolves it;
   - nothing stored returns None, with every searched anchor named.
4. Do NOT edit `build_unit_map.py` (another cell owns it). The issuer wires `discriminate_facts` to your function at the merge:
   name the exact hookup lines in your report.

## 3. SURFACES

<paths>
integrations/bloomberg/research/unit_anchor.py
integrations/bloomberg/research/tests/test_unit_anchor.py
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-y-3.same-currency-anchor.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/y3/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`). Never disable the sparse checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO FX value typed into code.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W3-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-y-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round23/y3_AC1.sh</invocation><expect>(?m)^y3 tsm anchor none searched [1-9]\d* reason_set True fx_invented False control_sap anchor CUR_MKT_CAP$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-y-3"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round23/y3_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: on the real raw today, TSM finds no anchor, with each searched anchor named and a reason, and nothing invented. The
  same-currency control (SAP GY, EUR both sides) returns its own `CUR_MKT_CAP`.
- AC2: your tests (the planted line and the planted stored rate resolve).

## 6. WHEN YOU ARE DONE
1. Write the instance at `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~3/AMGT_CORPUS.TO-CRPS-y-3.same-currency-anchor.proof_of_spec.json`.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE: each AC line, the search rule for a same-currency line, and the exact `discriminate_facts` hookup.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-22 analysis ruling 4 @`a940eb6813`. Dry-run at base CLOUD `afad83a02f`:
- y3_AC1 FAIL as expected (FileNotFoundError: no `unit_anchor.py`).
- y3_AC2 FAIL as expected (no tests ran).
<risk>LOCAL</risk>
<status>pending</status>
<round>23</round>
<slot>~3</slot>
<fabric>site-z</fabric>

<status>complete</status>
