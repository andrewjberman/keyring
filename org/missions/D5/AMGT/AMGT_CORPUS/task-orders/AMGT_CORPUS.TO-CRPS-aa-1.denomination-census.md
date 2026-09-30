# AMGT_CORPUS task order -- `CRPS-aa-1` -- ROUND 25: the measured denomination of the header money figures on the mixed-currency names, and the label rule the derive reads

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-aa-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or deploy surface (the re-derive is a later issuer act under a pair).
comp-iam: DECLARED-NOT-APPLICABLE -- S3 reads only.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 25. Serves **every served figure's currency label**.

## 1. THE CELL -- `CRPS-aa-1`

**Where this came from (row `AMGT_CORPUS-Z-S69`, ruled a SERVED WRONG FACT).** The derive labels each figure's currency in
`integrations/bloomberg/research/model_block_pull.py`, in `_figure_currency(mnemonic, quote_ccy, reporting_ccy)` (about `:809`):
- every `_CURRENCY_SENSITIVE_FIELDS` member (about `:764`, including `CUR_MKT_CAP`, `NET_DEBT` and `CURR_ENTP_VAL`) is labelled
  with the REPORTING currency (`EQY_FUND_CRNCY`, basis `reporting (EQY_FUND_CRNCY)`);
- `PX_LAST` is labelled with the QUOTE currency (`CRNCY`);
- everything else is `invariant`.

No value is ever converted; this is a LABEL. On a name that lists in one currency and reports in another, a MARKET figure is
denominated in the quote currency. For example, `TSM_US_Equity`'s `CUR_MKT_CAP` is served as 2,339,877,750,964.95 labelled TWD,
while the ADR trades in USD and the value is USD. A label that names a currency the value is not in is a wrong fact to a reader.

**The population, measured by the issuer's checker** (the newest served block of every key except `BP/_LN_Equity` and
`NG/_LN_Equity`, which are EXCLUDED under `Z-S64`, where `currencies.mixed` is true and a `scope: header` figure carries basis
`reporting (EQY_FUND_CRNCY)`): **73 figures on 25 securities** (`CUR_MKT_CAP` 25, `NET_DEBT` 25, `CURR_ENTP_VAL` 23). The
figure 79 on 27 in the round-24 row counted BP and NG.

**RULED -- what you build:**
1. **The census, BY MEASUREMENT:** `deliverables/0.9.0_WK_AMGT_CORPUS~1/DENOMINATION_CENSUS_ROUND25.json` (+ `.md`), with one
   entry per population figure.
   - Its shape: `{"population": 73, "securities": 25, "excluded": [{"key": "BP/_LN_Equity", "row": "Z-S64"}, {"key":
     "NG/_LN_Equity", "row": "Z-S64"}], "figures": [{"security_key", "mnemonic", "value", "quote_ccy", "reporting_ccy", "class":
     "quote"|"reporting"|"UNRESOLVED", "measurement"}]}`.
   - `security_key` is the underscore form of the model-block key (for example `TSM_US_Equity`).
   - `measurement` states the read that decided the class: the figure's value against a same-block quantity in a KNOWN currency
     (for example `PX_LAST` in `CRNCY` times a share count, stating which share count and any ADR ratio you measured), or the
     internal consistency `CURR_ENTP_VAL ~ CUR_MKT_CAP + NET_DEBT` with the tolerance you applied.
   - A class you cannot decide by a stated read is `UNRESOLVED`, with the reason in `measurement`. NEVER assume a class from the
     field's name alone, and never invent an FX rate.
2. **The label rule the derive reads**, in `_figure_currency`, which gains an optional keyword `security=None`. The existing
   three-argument calls must keep working.
   - A `quote` class returns (`quote_ccy`, `"quote (CRNCY)"`).
   - A `reporting` class returns (`reporting_ccy`, `"reporting (EQY_FUND_CRNCY)"`).
   - A figure the census leaves `UNRESOLVED` returns (`None`, a basis beginning `"UNMEASURED:"` that names why). It must not print
     a currency it has not measured.
   - Where one class holds for a mnemonic on every name the census decided, state it as a mnemonic-level class (a named constant
     set, with its measured ground in a code comment).
   - Where names differ, carry a per-security exception table in `model_block_pull.py`, keyed by the Bloomberg-form security
     (for example `"TSM US Equity"`).
   - Statement figures outside the census population (for example `SALES_REV_TURN`) keep the reporting rule unchanged.
3. **Tests:** `integrations/bloomberg/research/tests/test_figure_currency_round25.py` (new):
   - TSM `CUR_MKT_CAP` reads USD;
   - a reporting-class statement figure on TSM stays TWD;
   - an UNRESOLVED census figure returns `None` with an `UNMEASURED:` basis;
   - a same-currency name is unchanged in currency;
   - no network.

   `test_currency_labels.py` pins the superseded rule for `CUR_MKT_CAP` / `NET_DEBT` on a mixed fixture (about `:225-227`).
   Change ONLY the assertions your measured rule supersedes, each with a comment citing this order. Keep its other arms.
4. Do NOT derive. In `model_block_pull.py`, touch only `_figure_currency`, its constants and its CALL SITES (AMENDMENT 1).

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_figure_currency_round25.py
integrations/bloomberg/research/tests/test_currency_labels.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/DENOMINATION_CENSUS_ROUND25.json
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/DENOMINATION_CENSUS_ROUND25.md
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-aa-1.denomination-census.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-aa-1.denomination-census.md
</paths>

READ-ONLY: every other file, every S3 object. Scratch `.scratch/aa1/`.

Your worktree is a SPARSE cone (`lib integrations .tools .claude org docs rcg infra/logic`). Never disable the sparse checkout.

## 4. BOUNDS
- Pure ASCII, LF, Python 3.9-compatible.
- NO vendor call, NO S3 write, NO derive, NO write to `field_map.json`.
- Any long-running script you write runs from a NAMED file with `python -u` (never a heredoc).
- REFUSE a criterion you cannot satisfy as written, with your measurement. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k), with
  `disarm_owner 2.0.0_SA_COO~X`.

## 5. PROOF OF SPEC (each invocation LITERAL, under `timeout 900`; the check files are the issuer's, read-only to you)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-aa-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round25/aa1_AC1.sh</invocation><expect>(?m)^aa1 population 73 securities 25 census_covered 73 classes_valid True reader_matches 73 tsm_mkt_cap USD control_reporting TWD unmeasured_labelled 0 callers [1-9]\d* unwired 0$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-aa-1"><invocation>cd "$(git rev-parse --show-toplevel)" && bash org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round25/aa1_AC2.sh</invocation><expect>(?m)^\d+ passed(, \d+ \w+)* in </expect></criterion>
</proof_of_spec>

- AC1:
  - the checker measures the population itself (73 on 25);
  - your census must cover every figure, each with a valid class and a non-empty measurement;
  - `_figure_currency(..., security=<Bloomberg form>)` must return exactly the currency your class implies, for every figure;
  - TSM `CUR_MKT_CAP` must read USD, and TSM `SALES_REV_TURN` TWD;
  - no UNRESOLVED figure may carry a currency.

  How many figures you decide is reported, not demanded.
- AC2: your tests with the existing currency-label suite.

## 6. WHEN YOU ARE DONE
1. Write the instance at the proof path in section 3.
2. `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>` returns rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file. Commit the files you changed
   plus the instance.
4. Report ONCE with:
   - each AC line;
   - the census by class (per mnemonic: quote, reporting, UNRESOLVED counts);
   - the measurement that decided each mnemonic;
   - every assertion you changed in `test_currency_labels.py`.

## 7. AMENDMENT 1 (issuer, 2026-09-30 ~15:5xZ) -- rows `Z-W1-S21` and `Z-W1-S22`, both the issuer's defects

1. **`Z-W1-S22` (the rule did not reach the derive).** Item 4 as first issued forbade every function but `_figure_currency`. The
   derive's own call sites therefore pass no `security`, and a served block would still print TSM `CUR_MKT_CAP` in TWD.
   **GRANTED:** every call of `_figure_currency` in `model_block_pull.py` passes `security=<the block's Bloomberg-form security>`.
   That is the only change allowed at those call sites.
   - `test_currency_labels.py`: change the arm-1 pins the wired rule now supersedes (the `992 HK Equity` fixture's
     `CUR_MKT_CAP` / `NET_DEBT`), each with a comment citing this amendment. Keep every other arm.
   - AC1 now also reads, by AST, every `_figure_currency` call in `model_block_pull.py`: `callers N unwired 0`.
2. **`Z-W1-S21` (the checker's EXCLUDED set).** RESAPP round-53 ac-3 has copied the slash keys to their encoded form
   (`BP-SLASH-_LN_Equity`, `NG-SLASH-_LN_Equity`). The checker now excludes both forms, and the population reads 73 on 25 again.
   Your census is unchanged.
3. Your commits `e0ab961ad8` and `da883ed031` stand. Continue from them; do not redo the census.

Gate limb that graded this modification: to-pipeline-gate grades a modified order's `<placeholders>` only (NONE); no limb graded
the criteria change.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-24 analysis ruling 1 and enrichment item 1 @`0cdf1b748d` (msg 27200). Dry-run at base CLOUD `98781013e0`
(worktree `C:/tmp/coox-crps25-issue`):
- aa1_AC1 FAIL as expected: `aa1 population 73 securities 25 census_covered 0 classes_valid False reader_matches 0 tsm_mkt_cap TWD
  control_reporting TWD unmeasured_labelled 0`. It reproduces the defect: TSM reads TWD.
- aa1_AC2 FAIL as expected (no tests ran).

`test_currency_labels.py` is granted because it pins the superseded rule (the round-23 `Z-W2-S17` lesson: grant at the cut).
<risk>LOCAL</risk>
<status>pending</status>
<round>25</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
