# AMGT_CORPUS task order -- `CRPS-an-1` -- ROUND 38: count and ratio fields carry no currency (row Z-W1-S35)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-an-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<direct_act>true</direct_act>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task, alarm or cadence; the re-pin is the issuer's CRPS-an-2.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 get/list only; the check captures every put and sends none.
comp-adversary: RUN by the issuer at the cut -- count_ratio_currency.py --derive (BA, SAP, BABA, TSM) build 0/1 (31 IS_SH_FOR_DILUTED_EPS figures with a currency) control 2/2.
EGRESS CLASS, declared: AWS-INTERNAL READ ONLY. NO Bloomberg call, NO vendor call, NO S3 write.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 38.

## 1. THE CELL -- `CRPS-an-1`

`_figure_currency(mnemonic, quote_ccy, reporting_ccy, security=None)` in `integrations/bloomberg/research/model_block_pull.py`
gives every `_CURRENCY_SENSITIVE_FIELDS` member the REPORTING currency. That set (about line 230) includes
`IS_SH_FOR_DILUTED_EPS`, a SHARE COUNT ("Weighted-average diluted shares used for EPS, millions of shares", unit
`MILLIONS (share count)`). So all 932 of its served figures carry a currency, which is a false claim (CVO, round 37: row
`AMGT_CORPUS-Z-W1-S35`). Measured at the cut over the 96 served blocks: 34,894 count-or-ratio figures (unit containing
"(share count)", or beginning RATIO or PERCENT), of which 932 carry a currency, all `IS_SH_FOR_DILUTED_EPS`. Money figures are
already right: 31,985, with 0 unlabelled.

**Build, in `model_block_pull.py` only (the currency classification and nothing else):**
1. A count field (shares, volume) and a ratio or percent field gets NO currency: `currency` None with basis `invariant`. Decide this
   by the field's unit family, never by the block's reporting currency. `IS_SH_FOR_DILUTED_EPS` is the measured case; apply the
   rule to any other count, ratio or percent member of `_CURRENCY_SENSITIVE_FIELDS` / `_DENOMINATION_REPORTING_MNEMONICS`.
2. Every money figure keeps exactly the currency round 37 gave it. PX_LAST (a price) keeps its quote currency. Round 25's
   UNMEASURED / UNSTATED reasoned nulls stay.
3. Write `integrations/bloomberg/research/tests/test_figure_currency_round38.py`. It is offline and calls `_figure_currency`
   directly: `IS_SH_FOR_DILUTED_EPS` -> (None, "invariant") on a mixed block; a reported money field still -> reporting; PX_LAST
   still -> quote; a ratio -> invariant.

## 2. BOUNDS

1. NO Bloomberg call, NO vendor call, NO S3 write. The served move is the issuer's paired act `CRPS-an-2`.
2. Only the files in `<paths>` change. Never edit a value, a unit, a field list (other than the currency classification's own
   membership) or a fetch path. The three granted currency tests may change ONLY where an assertion pins a currency on a count or
   ratio field. Record each change with an `AMENDMENT (CRPS-an-1, round 38):` comment, as the files' earlier AMENDMENT comments do.
3. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only. Run python from your worktree root as
   `PYTHONPATH=<worktree root> python ...`.
4. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_figure_currency_round38.py
integrations/bloomberg/research/tests/test_figure_currency_round37.py
integrations/bloomberg/research/tests/test_currency_labels.py
integrations/bloomberg/research/tests/test_figure_currency_round25.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-an-1.counts-and-ratios-carry-no-currency.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-an-1.counts-and-ratios-carry-no-currency.md
</paths>

Read-only: the whole repository, in particular `build_unit_map.py` (the unit families) and the issuer's check under
`org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round38/` (never edit it).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-an-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round38/count_ratio_currency.py" --derive BA_US_Equity,SAP_GY_Equity,BABA_US_Equity,TSM_US_Equity</invocation><expect>(?m)^crc derive build 1/1 control 2/2$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-an-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python -m pytest integrations/bloomberg/research/tests/test_figure_currency_round38.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^[0-9]+ passed(, [0-9]+ warnings?)? in [0-9.]+s$</expect></criterion>
</proof_of_spec>

- AC1 (the REAL `stage_derive`, in memory, puts captured): build -- 0 count/ratio figures with a currency on the 4 names; control
  -- money unlabelled 0, values moved 0, money labels changed 0.
- AC2: your offline test passes.

## 5. WHEN YOU ARE DONE

1. Run your test file and every `integrations/bloomberg/research/tests/` file whose name contains `currency` or `model_block`. Every
   test passes.
2. Write the instance at the proof path, with its mutant control from the start. Then run `python .tools/proof-of-spec-check.py
   <instance> AC1,AC2 --governing-order <this order>` AFTER your final commit. It must return rc 0.
3. Only if every criterion passes, append a new status tag reading complete at the END of this file, in the SAME commit as your
   instance.
4. Report ONCE: the fields whose currency you removed, every criterion's output line, the pytest summary lines, your commit hashes
   and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-37 analysis @`b12904724c` ruling 1 + s.4 item 1. Base: crc derive build 0/1 control 2/2; crc served build
0/1 control 1/1 (932 IS_SH with a currency).
<risk>LOCAL</risk>
<status>pending</status>
<round>38</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<status>complete</status>
