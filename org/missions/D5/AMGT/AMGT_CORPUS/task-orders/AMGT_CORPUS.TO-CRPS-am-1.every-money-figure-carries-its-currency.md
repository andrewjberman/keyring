# AMGT_CORPUS task order -- `CRPS-am-1` -- ROUND 37: every money figure the producer derives carries its currency

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-am-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task, alarm or cadence; the daily task's re-pin is the issuer's act CRPS-am-2.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 get/list of landed raw and served blocks only; the check captures every put and sends none.
comp-adversary: RUN by the issuer at the cut -- am1_check.py build 0/1 (913 unlabelled money figures on 4 names, unchanged by a re-derive) control 2/2. Blind spot: 4 names, not 96; the issuer's census over 96 served blocks is the served act's control (am-2).
EGRESS CLASS, declared: AWS-INTERNAL READ ONLY. NO Bloomberg call, NO vendor call, NO S3 write, NO re-derive that lands.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 37.

## 1. THE CELL -- `CRPS-am-1`

A model block's money figures carry a `currency` and a `currency_basis`, set by `_figure_currency(mnemonic, quote_ccy,
reporting_ccy, security=None)` in `integrations/bloomberg/research/model_block_pull.py` (about lines 1135-1167). The call sites are
`stage_derive` and its helpers (about lines 1357, 1438, 1604 and 1649). The two currencies come from `_header_currencies` (about line
1019): `quote_ccy` is CRNCY and `reporting_ccy` is EQY_FUND_CRNCY.

Today `_figure_currency` labels:
- the REPORTING currency for `_CURRENCY_SENSITIVE_FIELDS` and `_DENOMINATION_REPORTING_MNEMONICS` members;
- the QUOTE currency for `PX_LAST` and for the round-25 census's `_DENOMINATION_QUOTE` names;
- a reasoned null `UNMEASURED: ...` for the census's held-out figures (`_DENOMINATION_UNRESOLVED`);
- **everything else `None` with basis `"invariant"`.**

So most money fields carry no currency. Measured at the cut over the 96 served blocks: 32,176 money figures (unit beginning
`MILLIONS` but not `MILLIONS (share count)`, `ABSOLUTE`, or `PER SHARE`), of which 8,578 are labelled, 42 are reasoned nulls, and
**23,556 are null with basis "invariant"**. On TSM_US_Equity (quote USD, reporting TWD) that includes NET_INCOME,
BS_TOTAL_LIABILITIES, the BEST_* money forecasts and the round-34 money fields. On 1299_HK_Equity the quote is HKD and the reporting
currency is USD.

**Build, in `model_block_pull.py` only (the currency classification and nothing else):**
1. Every MONEY figure (by the unit rule above) gets a currency:
   - the REPORTING currency for a reported value (statement lines, per-share statement values, the BEST_* consensus of a reported
     line);
   - the QUOTE currency for a market value (price-based values such as a market capitalisation or a traded value).
   Decide each money field's side from Bloomberg's definition (the producer's own `FIELD_BASIS` text) and check it against the
   landed values where a sibling makes it decidable. For example, a market cap is price x shares in the quote currency, and a
   statement total reconciles with its reporting-currency siblings.
2. Never assume a currency that is not stated. A needed header currency that is absent keeps the existing reasoned null
   (`UNSTATED: ...`). The round-25 census's held-out figures keep their `UNMEASURED: ...` null, and its quote/reporting overrides
   stay as they are.
3. Non-money figures (ratios, percents, share counts, text, dates, years) stay `invariant`.
4. A figure that already carries a currency keeps exactly that currency.
5. Write `integrations/bloomberg/research/tests/test_figure_currency_round37.py`. It is offline and calls `_figure_currency`
   directly. Cover: a reported money field -> reporting; a market-value money field -> quote; a mixed block (USD quote, TWD
   reporting); an absent reporting currency -> the UNSTATED null; a census held-out figure -> its UNMEASURED null unchanged; a ratio
   -> invariant.

## 2. BOUNDS

1. NO Bloomberg call, NO vendor call, NO S3 write. Never let a re-derive land: the served move is the issuer's paired act
   `CRPS-am-2`. The check re-derives in memory and captures every put.
2. Only the files in `<paths>` change. Never edit a value, a unit, a field list or a fetch path.
   - Three existing tests pin the OLD rule and are granted to you for that alone: `tests/test_currency_labels.py` (its arm at
     about lines 220-253 asserts every figure outside the sensitive set and PX_LAST is `invariant`),
     `tests/test_figure_currency_round25.py` and `tests/test_figure_currency_round26.py`.
   - You may change an assertion ONLY where it pins `None` / `"invariant"` on a MONEY figure, and you record each change with an
     `AMENDMENT (CRPS-am-1, round 37):` comment, as the file's own AMENDMENT 1 of CRPS-aa-1 does.
   - Every other assertion stays as it is: the ratio, text and PX_LAST arms, the census arms, and the non-vacuity counts.
3. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
4. Run python from your worktree root as `PYTHONPATH=<worktree root> python ...`.
5. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_figure_currency_round37.py
integrations/bloomberg/research/tests/test_currency_labels.py
integrations/bloomberg/research/tests/test_figure_currency_round25.py
integrations/bloomberg/research/tests/test_figure_currency_round26.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-am-1.every-money-figure-carries-its-currency.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-am-1.every-money-figure-carries-its-currency.md
</paths>

Read-only: the whole repository, in particular `build_unit_map.py`, `field_map.json`, the existing
`integrations/bloomberg/research/tests/` (the currency tests among them), and the issuer's checks under
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round37/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-am-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round37/am1_check.py"</invocation><expect>(?m)^am1 build 1/1 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-am-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python -m pytest integrations/bloomberg/research/tests/test_figure_currency_round37.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^[0-9]+ passed(, [0-9]+ warnings?)? in [0-9.]+s$</expect></criterion>
  <criterion id="AC3" cell_refs="CRPS-am-1" judgment="true"/>
</proof_of_spec>

- AC1 (the REAL `stage_derive`, in memory, on TSM, 1299 HK, SAP and BA, on each served block's own raw stamp; puts captured, never
  sent): build -- 0 money figures null without a reason; control -- 0 values moved and 0 already-labelled currencies changed.
- AC2: your offline test passes.
- AC3 (JUDGMENT, graded by the CVO at L9): each money field's side (reporting or quote) is right by Bloomberg's definition. Record
  it as `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO~Z`; no verdict.

## 5. WHEN YOU ARE DONE

1. Run your test file and every `integrations/bloomberg/research/tests/` file whose name contains `currency` or `model_block` with
   `python -m pytest <files> -q`. Every test passes.
2. Write the instance at the proof path, with its mutant control from the start. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2,AC3 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME
   commit as your proof instance.
4. Report ONCE:
   - the side you gave each money field that was "invariant" at the base (reporting / quote), with the reason for each market-value
     one;
   - every criterion's output line, the pytest summary lines, your commit hashes and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-36 analysis @`4c3e3755a7` s.3 ruling 1 + s.4 item 1. Base: am1_check build 0/1 control 2/2; census 96 names
money 32,176 / labelled 8,578 / null_reasoned 42 / null_unlabelled 23,556. The served move is CRPS-am-2.
<risk>LOCAL</risk>
<status>pending</status>
<round>37</round>
<slot>~1</slot>
<fabric>site-z</fabric>
