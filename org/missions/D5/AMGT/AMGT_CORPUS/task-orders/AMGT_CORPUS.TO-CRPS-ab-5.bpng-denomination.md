# AMGT_CORPUS task order -- `CRPS-ab-5` -- ROUND 26: the header-currency census extended to BP/ LN and NG/ LN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-ab-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~5</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (the re-derive is a later issuer act under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~5`**, slot `~5` of round 26. Serves **every served figure's currency label**.

## 1. THE CELL -- `CRPS-ab-5`

**Where this came from (row `Z-S69`'s class; round-25 analysis enrichment item 5).** Round 25 (`CRPS-aa-1`) measured the currency of
every header money figure on the mixed-currency names and wired the result into
`integrations/bloomberg/research/model_block_pull.py`:
- `_figure_currency(mnemonic, quote_ccy, reporting_ccy, security=None)`;
- its tables `_DENOMINATION_REPORTING_MNEMONICS`, `_DENOMINATION_QUOTE`, `_DENOMINATION_UNRESOLVED` and `_DENOMINATION_REASONS`.

That census EXCLUDED `BP/ LN Equity` (quote GBp, reporting USD) and `NG/ LN Equity` (quote GBp, reporting GBP). Their header money
figures still print the reporting currency unmeasured.

The census method of round 25, read-only to you, is in
`deliverables/0.9.0_WK_AMGT_CORPUS~1/DENOMINATION_CENSUS_ROUND25.{json,md}`: the value against `PX_LAST` x shares in the same block, and
`CURR_ENTP_VAL` ~ `CUR_MKT_CAP` + `NET_DEBT`, with GBp handled as GBP / 100. No FX rate is invented anywhere.

**The population, measured by the issuer's checker:** the newest block at `BP-SLASH-_LN_Equity` and `NG-SLASH-_LN_Equity` (the encoded
keys) whose `currencies.mixed` is true, and on it every `scope: header` figure with basis `reporting (EQY_FUND_CRNCY)`. That is **6
figures on 2 securities**.

**RULED -- what you build:**
1. **The census:** `deliverables/0.9.0_WK_AMGT_CORPUS~5/DENOMINATION_CENSUS_ROUND26.json` (+ `.md`), with round 25's shape.
   - `security_key` is the ENCODED key (`BP-SLASH-_LN_Equity`).
   - Each figure gets `class` quote / reporting / UNRESOLVED, with the `measurement` that decided it.
   - A class you cannot decide by a stated read is UNRESOLVED.
   - Where the value is in a currency neither label states (for example GBP on a GBp-quoted, USD-reporting name), the class is
     UNRESOLVED, as round 25 ruled.
2. **The label rule:** add BP/NG to the per-security denomination tables, keyed by the Bloomberg-form security `"BP/ LN Equity"` /
   `"NG/ LN Equity"`, with each ground in a code comment. Change no other entry and no other function.
3. **Tests:** `integrations/bloomberg/research/tests/test_figure_currency_round26.py` (new): each BP/NG class returns its currency, and
   an UNRESOLVED one returns `None` with a basis beginning `UNMEASURED:`. Keep round 25's label suites green.
4. Do NOT derive.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_figure_currency_round26.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/DENOMINATION_CENSUS_ROUND26.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/DENOMINATION_CENSUS_ROUND26.md
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~5/AMGT_CORPUS.TO-CRPS-ab-5.bpng-denomination.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-ab-5.bpng-denomination.md
</paths>

READ-ONLY: every other file, every S3 object. In `model_block_pull.py`, only the denomination tables (and their comments). Scratch
`.scratch/ab5/`. Your worktree is a SPARSE checkout; never disable it.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO derive, never an invented FX rate.
- Any long-running script runs from a NAMED file with `python -u`.
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W5-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-ab-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round26/ab5_AC1.sh</invocation><expect>(?m)^ab5 population 6 securities 2 census_covered 6 classes_valid True reader_matches 6 unmeasured_labelled 0$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-ab-5"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round26/ab5_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1: the checker measures the population itself. Your census must cover all 6 with valid classes and measurements, and
  `_figure_currency(..., security=)` must return exactly the currency each class implies. No UNRESOLVED figure may carry a currency.
  How many you decide is reported, not demanded.
- AC2: your tests with round 25's label suites.

## 6. WHEN YOU ARE DONE
1. Write the instance at the proof path in section 3.
2. Run `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit, and pin each
   artifact row to the commit whose BYTES you graded (verify with `git show <pin>:<path>`). It must return rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file, and commit.
4. Report ONCE: each AC line, the census by class with the measurement that decided each figure, and the table entries you added.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-25 analysis enrichment item 5 @`19207dfb83`. Dry-run at base CLOUD `ae1c849af1`: ab5_AC1 FAIL as designed
(`ab5 population 6 securities 2 census_covered 0 classes_valid False reader_matches 0 unmeasured_labelled 0`); ab5_AC2 FAIL.

The write sets are disjoint from ab-1 (`dossier.py`), ab-2 (`build_unit_map.py`) and ab-3 (`case_rule.py`).
<risk>LOCAL</risk>
<status>pending</status>
<round>26</round>
<slot>~5</slot>
<fabric>site-z</fabric>
