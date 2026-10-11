# MDPF_CANON task order -- `CN-d-1` -- THE SERVED GLOBAL TOTAL'S IDENTITY IS STATED AND ASSERTED, AND THE GLOBAL ACCOUNT-DISTRIBUTION NAMES THE COTTONWOOD LEG'S VINTAGE (W8-S3, W8-S4; FWD-3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-d-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~10</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the new function is a refusal inside the existing consolidator run, not a monitor.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call is added to any script; the criteria read one served object with a read-only get.
comp-adversary: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1 at box/dell1 -- r4_cn_d_1.py 0 of 5 arms and r4_cn_d_1_vintage.py 0 of 3 arms at base; a reference tree reads 5 of 5 and 3 of 3 (the arms can pass); the served 2026-10-08 global object holds the identity on 484 non-null dates, so the new refusal does not brick today's run.
EGRESS CLASS, declared: NONE (the worker writes no AWS).
</preflight>

## 1. THE CELL -- `CN-d-1` (round 4, decomposition v4)

Two facts about the global object, both already true in the producers and neither stated where a reader looks. Make each one a statement
plus a guard. No served value moves.

**Fact 1 -- the served total.** The global `opal_aggregate_aua` is built in two stages. `build_global_artifact`
(`data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py`, about :2245) builds the BASE total, and its docstring says
`opal_aggregate_aua[i] == model_aua[i] + non_model_aua[i] at EVERY date`. After that, `data/mdpf/scripts/gold/mdpf_gold_consolidator.py`
folds Tax (`apply_taxsma_overlay`, about :1720) and then the additive SMA sleeves (`apply_sma_sleeve_overlay`, about :1836) onto it, so the
SERVED identity is:

```
opal_aggregate_aua[i] == model_aua[i] + non_model_aua[i] + tax_additive_aua[i] + sma_additive_aua[i]
                         (a None additive term = nothing counted that date, i.e. 0.0; a None opal_aggregate_aua date is skipped)
```

Nothing asserts that on the final object, and the base docstring reads as if the 2-term form were served (the CVO measured the
2-term form failing on 24 of 484 non-null dates, each equal to the two additive terms). Build the guard and fix the statement:

1. In `mdpf_gold_consolidator.py`, add a module-level function `assert_global_served_identity(arts: dict) -> None`, placed directly after
   `apply_sma_sleeve_overlay` (after the end of that function, before the next top-level definition). Behaviour, exactly:
   - `g = arts.get("global")`; return when it is None or carries no `dates`.
   - For each index `i` of `g["dates"]`: read `o = opal_aggregate_aua[i]`, and skip the date when `o` is None. Read `m = model_aua[i]`,
     `nm = non_model_aua[i]`, `t = tax_additive_aua[i]`, `s = sma_additive_aua[i]`; a list that is shorter than `dates` or a key that is
     absent reads as None at that index. `t` and `s` None count as 0.0.
   - A date VIOLATES when `m` is None or `nm` is None, or `abs(o - round(m + nm + t + s, 2)) > 0.011`.
   - On any violation raise `SystemExit` whose message begins `GLOBAL SERVED IDENTITY REFUSED:`, gives the violation count, and lists up
     to the first five as `(date, difference to the cent)`. Never print a level or a total. The function never mutates `arts`.
2. In `build_all` (same file, about :2640) call it on the line directly after `arts = apply_sma_sleeve_overlay(arts)`, with one comment line
   naming it.
3. In `dim_mdpf_aggregate_aua_timeseries.py`, change two docstrings and nothing else in that file:
   - `build_global_artifact`: keep the HEADLINE IDENTITY paragraph and say it is the BASE identity (before the additive folds); add the
     served identity above, naming `base_excluding_tax_aua`, `tax_additive_aua` and `sma_additive_aua`, and say it is asserted by
     `assert_global_served_identity` in `mdpf_gold_consolidator.py`.
   - `_assert_global_composition`: add one sentence to its docstring saying the same two-stage fact and pointing at that function.
   No executable line of that file changes, and the base assertion's logic stays as it is.

**Fact 2 -- the Cottonwood leg's vintage.** `build_firm_distribution("global", ...)` in
`data/mdpf/scripts/gold/dim_mdpf_account_distribution.py` (about :423) folds Cottonwood's units from a sidecar whose `value_date` can lag the
global key date by up to the declared window (`_cottonwood_sidecar`, about :335-420; ruled, and its window rule stands -- do NOT edit that
function). The fold marks itself under `meta["cottonwood_fold"]` (about :481-488) but not the leg's date.

4. Add two keys to that dict: `"value_date": str(sc.get("value_date"))[:10]` and `"age_trading_days": _trading_day_age(<that date>,
   dt.date.today().isoformat())`. `_trading_day_age` is already imported at the top of the file (the same math `_cottonwood_sidecar` uses at
   about :405). No other line of that file changes; `total` and `by_model` stay byte-identical.

Tests (new files; follow the idiom of `data/mdpf/tests/stratid/test_stratid_global_fold.py`, synthetic data, no network):

5. `data/mdpf/tests/canon/test_global_served_identity.py`: a conforming global is accepted; a global broken by 1.00 on one date raises
   `SystemExit` naming that date; a None additive term is read as nothing counted; a date with `opal_aggregate_aua` None is skipped; a date
   with `opal_aggregate_aua` set and `model_aua` None is refused.
6. `data/mdpf/tests/canon/test_cottonwood_fold_vintage.py`: with `_FIRM_UNITS["global"]` and `_cottonwood_sidecar` replaced by synthetic ones
   (as the issuer's check `r4_cn_d_1_vintage.py` does), `meta.cottonwood_fold` carries `value_date` and an int `age_trading_days`, and
   `total`/`by_model` do not change between two sidecar dates.

## 2. BOUNDS

1. **No AWS write of any kind**: no apply, no deploy, no invoke, no `s3 cp`/`put`/`rm`. Read-only `get`/`describe`/`head`/`list` is allowed
   (criterion AC1 arm A4 reads one served object). No install, no push. REFUSE, do not rescue.
2. Only the files in section 3 change (plus your deliverables and the surprise channel). `apply_taxsma_overlay`, `apply_sma_sleeve_overlay`,
   `_cottonwood_sidecar`, `_assert_global_composition`'s logic and every existing test are read-only.
3. **Never** loosen, wrap or skip an existing assertion to make a criterion pass. If the served 2026-10-08 object fails the new function, that
   is a finding: file a BLOCKING row with the dates and differences (no levels) and stop on that criterion.
4. **CLIENT DATA:** never print a client figure or account id; the refusal message prints dates and a difference only.
5. Keep each file's line endings as you find them (read them first). No non-ASCII. Use the Edit tool.
6. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
data/mdpf/scripts/gold/mdpf_gold_consolidator.py
data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
data/mdpf/scripts/gold/dim_mdpf_account_distribution.py
data/mdpf/tests/canon/test_global_served_identity.py
data/mdpf/tests/canon/test_cottonwood_fold_vintage.py
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~10/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `data/mdpf/tests/stratid/test_stratid_global_fold.py` (the idiom) and the issuer's checks
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_1.py` and `r4_cn_d_1_vintage.py` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 300)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-d-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_1.py"; echo "exit=$?"</invocation><expect>ROUND 4 IDENTITY: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-d-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round4/checks/r4_cn_d_1_vintage.py"; echo "exit=$?"</invocation><expect>ROUND 4 VINTAGE: 3 of 3 arms -- and exit=0</expect></criterion>
</proof_of_spec>

No judgment criterion: both facts are checked on the object and the code.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~10/MDPF_CANON.TO-CN-d-1.proof_of_spec.json`. **Flip this
order's `<status>` to `complete` in the SAME commit as your proof instance**, and only when every mechanical criterion passes.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W10-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 4 = `org/missions/D8/MDPF/MDPF_CANON/ledger/ROUND_ANALYSIS.round3.md` @ae094ea51d section 3 item 2 as re-cut by
ADDENDUM 1 @187b53dbe6 (AC2 stands; AC1 became the basis cell `CN-d-2`; AC3 became step 4 here; the "align or refuse" ruling is withdrawn).
Evidence for the re-cut: `deliverables/2.0.0_SA_COO~D1/round4/FOLD_AC1_AC3_CONFLICT.md`. Slot ~10, its own chain. The deploy is CloudOps's under
`CN-d-5`, sequenced behind the pending `MDPF_STRATID.TO-APPLY-R2.global-fold-deploy` so neither overwrites the other's bytes; the added `meta`
keys change the served account-distribution bytes, so the deploy carries a never-widen pair (CTO + COO) naming that blast radius and its
rollback. Base box/dell1. LF only.

<status>staged</status>
<round>4</round>
<to_id>MDPF_CANON.TO-CN-d-1</to_id>
<slot>~10</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
