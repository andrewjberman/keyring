# AMGT_CORPUS task order -- `CRPS-al-1` -- ROUND 36: the Model slice serves the block's fiscal-year reasons

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_CORPUS/decompositions/AMGT_CORPUS_DECOMP.md</decomp_doc>
<owned_cells>CRPS-al-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_CORPUS~1</issued_to>
<issued_by>2.0.0_SA_COO~X</issued_by>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, task, alarm or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- S3 get/list of the served model blocks only, through scoped_amgt's own reader (the same reads the check makes).
comp-adversary: RUN by the issuer at the cut -- al1_check.py build 0/1 control 1/1. Blind spot: two names (1299 HK, BA), not 96; the issuer's census at the cut read 96 names, 6,796 fiscal-scope entries, 2 distinct reason texts.
EGRESS CLASS, declared: AWS-INTERNAL READ ONLY. NO deploy, NO vendor call, NO S3 write.
</preflight>

**You are `0.9.0_WK_AMGT_CORPUS~1`**, slot `~1` of round 36. This is the FIRST order of your queue; `CRPS-al-2` follows it on the
same slot and consumes the field you add here.

## 1. THE CELL -- `CRPS-al-1`

`lib/research/api/scoped_amgt.py` `read_model(security_key, identity=None, model_block=None)` (at about line 4228) builds the
Model tab's slice. It returns `fiscal_year_figures` and the forecast keys. When there are no forecast figures it serves ONE
forecast reason (`forecast_reason`, about lines 4270-4283). It serves NO fiscal-year reason.

Each served model block carries an `unresolved` list. Entries whose `scope` is `fiscal_year_line_item`
(`lib.research.checkface.scopes.SCOPE_FISCAL_YEAR_LINE_ITEM`) have the shape
`{"scope": "fiscal_year_line_item", "fiscal_year": "2016", "mnemonic": "AVERAGE_DIVIDEND_YIELD", "reason": "not dated at the
fiscal period end (non-December FYE, fye_join)"}`. Measured at the cut over the 96 newest blocks: 6,796 such entries; 1299_HK_Equity
holds 97, BA_US_Equity holds 0.

**Build:**
1. `read_model` returns one more key, `fiscal_unresolved`: a list of `{"mnemonic", "fiscal_year", "reason"}`, one per block
   `unresolved` entry whose scope is `fiscal_year_line_item`, in the block's own order, with the values copied as served (no
   rewording here; the page words them).
2. The key is ALWAYS present, built on the same unconditional return literal as the other keys: `[]` when the block has no such
   entry and when there is no block at all.
3. Nothing else in the returned dict changes: same keys, same values, same order of `fiscal_year_figures`.
4. Write `lib/research/api/tests/test_read_model_fiscal_unresolved.py`. It is offline: pass `model_block=` and `identity=` fixtures
   shaped like the entry above. Cover a block with two fiscal entries plus a header entry and a forecast entry (only the two fiscal
   ones served), a block with none (`[]`), and `model_block=None` with an identity that has no `security_key` (`[]`, no KeyError).

## 2. BOUNDS

1. NO deploy, NO vendor call, NO S3 write. The served move is the issuer's act `CRPS-al-5` after you drain.
2. Only the files in `<paths>` change. Edit only `read_model` in `scoped_amgt.py`; touch no other function.
3. Write code with the Edit/Write tools, never a shell heredoc or `python -c`. ASCII only.
4. Run python from your worktree root as `PYTHONPATH=<worktree root> python ...`.
5. Rows are `AMGT_CORPUS-Z-W1-S<k>` (next free k across every file under `surprise-channel/`), with `disarm_owner
   2.0.0_SA_COO~X`.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_read_model_fiscal_unresolved.py
org/missions/D5/AMGT/AMGT_CORPUS/deliverables/0.9.0_WK_AMGT_CORPUS~1/AMGT_CORPUS.TO-CRPS-al-1.model-slice-serves-fiscal-reasons.proof_of_spec.json
org/missions/D5/AMGT/AMGT_CORPUS/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_CORPUS/task-orders/AMGT_CORPUS.TO-CRPS-al-1.model-slice-serves-fiscal-reasons.md
</paths>

Read-only: the whole repository, in particular `lib/research/checkface/scopes.py`, the existing `lib/research/api/tests/`, and the
issuer's checks under `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round36/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CRPS-al-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python "org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/checks/round36/al1_check.py"</invocation><expect>(?m)^al1 build 1/1 control 1/1$</expect></criterion>
  <criterion id="AC2" cell_refs="CRPS-al-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH=. python -m pytest lib/research/api/tests/test_read_model_fiscal_unresolved.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^[0-9]+ passed(, [0-9]+ warnings?)? in [0-9.]+s$</expect></criterion>
</proof_of_spec>

- AC1 (the real `read_model` on the live newest blocks of 1299 HK and BA): build -- `fiscal_unresolved` equals the block's
  fiscal-scope entries on both names, 1299 HK non-empty; control -- `fiscal_year_figures` length still equals the block's
  fiscal-scope figure count.
- AC2: your offline test passes.

## 5. WHEN YOU ARE DONE

1. Run your test file and `lib/research/api/tests/` files whose name contains `model` with `python -m pytest <files> -q`. Every
   test passes.
2. Write the instance at the proof path, then run `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order
   <this order>` AFTER your final commit. It must return rc 0.
3. Only if every mechanical criterion passes, append a new status tag reading complete at the END of this file, in the SAME
   commit as your proof instance.
4. Report ONCE: the diff summary of `read_model`, every criterion's output line, the pytest summary lines, your commit hashes and
   any row. Then continue with your next order when the issuer hands it to you.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-35 analysis @`02bbbc0208` s.3 ruling 1 + s.4 item 1. Base: al1_check build 0/1 control 1/1. The served
move is CRPS-al-5 (decomposition s.1).
<risk>LOCAL</risk>
<status>pending</status>
<round>36</round>
<slot>~1</slot>
<fabric>site-z</fabric>
