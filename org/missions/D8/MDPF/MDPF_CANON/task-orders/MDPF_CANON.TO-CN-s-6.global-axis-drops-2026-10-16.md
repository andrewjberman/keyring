# MDPF_CANON task order -- `CN-s-6` -- GLOBAL'S AXIS DROPS THE ENUMERATED DATE 2026-10-16, SO GATE (v) NEVER SEES IT (PRODUCER; FWD-9 head g, the Global fire)


<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-s-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~33</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the cell adds one enumerated constant and one subtraction in code the scheduled run already executes.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read, no new key prefix, no IAM change; the code reads the same legs it reads today.
comp-adversary: RUN by the issuer on DELL1 at the base (the deployed pin d2f734fbac, worktree C:/dev/wk-canon-s6-33) -- `r11_cn_s_6.py real` 2 of 5 (S3 and S4 are controls the base already meets; S0, S1 and S2 are red: the base REFUSES Global on gate (v), "5 across 1 date(s)"); a scratch reference with the two-line change reads 5 of 5 (the arms can pass); planted mutants each turn their named arms red: the date added to the exempt list instead (S0, S1 and S2 red: gate (v) passes and the composition gate then refuses, "1 band/total violation(s)"), a general rule that drops any date only the Cottonwood leg holds (S4 red), the date in both the exempt list and the drop set (S0 red).
EGRESS CLASS, declared: NONE (the worker writes no AWS and reads three files already on disk).
</preflight>

## 1. THE CELL -- `CN-s-6` (round 11, amendment 2)

**The cell, verbatim from the decomposition:** Global's axis drops the enumerated date 2026-10-16: a new `GLOBAL_AXIS_DROP_DATES = frozenset({"2026-10-16"})` beside `GLOBAL_CROSS_AXIS_EXEMPT_DATES`, subtracted from the union of the three legs' dates in `build_global_artifact`, so Global's series, its `as_of_last` and its coherence gates never see 2026-10-16; Cottonwood's own axis keeps the date.

**Why (CTO rulings msgs 7594 and 7600, PRD v2.29):** the 2026-10-17 13:30Z scheduled fire REFUSED to build Global. Global's axis is the union of the three legs' dates; Cottonwood now carries 2026-10-16 (it has account counts for five models on that date) while 49 Financial and Inflection end at 2026-10-15, so on that date five Global model legs have `account_count` and no `model_value`, and cross-axis gate (v) refuses ("5 across 1 date(s)"). No catch-up will ever fill 2026-10-16, so Global would be refused on every fire. Adding the date to the exempt list is NOT the fix (the composition gate then refuses on a band/total violation, and Global's newest row would carry a None headline). The ruled fix is to take the date off Global's axis, as an ENUMERATED set, never as a rule.

**The edit, in `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` (LF file; keep LF):**
1. Define `GLOBAL_AXIS_DROP_DATES = frozenset({"2026-10-16"})` directly after `GLOBAL_CROSS_AXIS_EXEMPT_DATES` (the frozenset ends near L1736) with a short ASCII comment: it names the CTO ruling (msgs 7594 and 7600), says it is an enumerated set and never a rule, and says the date is NOT in the exempt list.
2. In `build_global_artifact` (L2297) change the one line `dates = sorted(set(a49["dates"]) | set(ainf["dates"]) | set(acot["dates"]))` (L2368) so it subtracts the set: `dates = sorted((set(a49["dates"]) | set(ainf["dates"]) | set(acot["dates"])) - GLOBAL_AXIS_DROP_DATES)`, wrapped over two lines as the file's line length wants.
3. Do NOT add the date to `GLOBAL_CROSS_AXIS_EXEMPT_DATES`. Do NOT write "any date a leg lacks" in any form: the set is the only rule. Do NOT touch `_assert_cross_axis_coherence`, `_assert_global_composition`, the Cottonwood leg or any per-firm artifact.

**The test, in `data/mdpf/scripts/gold/tests/test_global_fold_flag2.py` (LF file; the file already holds 16 passing tests and 3 failing ones that are not yours: row D1-S1, keep them untouched):** ADD one test, named `test_s6_axis_drops_only_the_enumerated_date`, in the file's style (the `_stub`, `_leg` and `_empty_cot` helpers): legs `a49` and `ainf` on `["2026-10-15"]` and a Cottonwood leg built with `_empty_cot(["2026-10-15", "2026-10-16"])`; assert the built Global's `dates` is `["2026-10-15"]` and its `as_of_last` is `"2026-10-15"`. In the same test run the control: the same legs with the Cottonwood date `"2026-10-19"` instead; assert `"2026-10-19"` IS in Global's `dates` (the set is enumerated, not a rule). Synthetic numbers only.

## 2. BOUNDS

1. **No AWS contact of any kind** (no read, write, invoke, deploy, install, push). The check reads three files already on disk, `C:/dev/_deploy_artifacts/canon_s6/leg_{49financial,inflection,cottonwood}.json`, outside the repo and client-scale: read them only through the check; never print a figure, an account id or a firm level from them.
2. Only the two files named in section 3 change (plus your deliverables and the surprise channel). Everything else is read-only; in particular the checks under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/`, which are the issuer's.
3. No non-ASCII character in any line you add (the dim file already holds 21 non-ASCII bytes in older lines: leave them). Use the Edit tool; keep LF.
4. Your worktree is already on the deployed pin `d2f734fbac`; the earlier history stays as it is. The change must be ONE commit on top of it so the deploy can be built from that commit alone. If a step cannot be done as written, file a row naming the step and stop on that step.

## 3. SURFACES

<paths>
data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
data/mdpf/scripts/gold/tests/test_global_fold_flag2.py
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-s-6.global-axis-drops-2026-10-16.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~33/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, and the three leg files named in bound 1.

## 4. PROOF OF SPEC (literal; timeout 300 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-s-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 300 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_6.py" real 2&gt;&amp;1 | grep -E "^  S|REAL"; echo "exit=${PIPESTATUS[0]}"</invocation><expect>five lines S0 to S4 each reading PASS, then ROUND 11 CN-S-6 REAL: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-s-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 300 python -m pytest data/mdpf/scripts/gold/tests/test_global_fold_flag2.py -q --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_within_window_carries_and_labels --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_beyond_window_absent_for_real --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_source_is_measured_never_interpolated; echo "exit=$?"</invocation><expect>no failure, at least 17 passed (16 pass at the base with the three pre-existing failures deselected; your added test makes 17) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 runs the tree's real `build_global_artifact` over the three staged legs of the 2026-10-17 13:30Z fire (the same inputs that were refused) and reads the emitted Global's axis, `as_of_last`, headline and core-model cells. AC2 is the regression guard plus your added test. They cannot prove what the deployed function builds in the cloud or what the served objects read after the next fire: that is the issuer's and CloudOps's read after the deploy (a never-widen pair first, a no-write dry run before the fire). There is no judgment criterion.

## 5. WHEN YOU ARE DONE

1. Commit the two code files through `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_CANON~33 <0.9.0_WK_MDPF_CANON~33@opal.agent>" -F <msgfile> -- data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py data/mdpf/scripts/gold/tests/test_global_fold_flag2.py` as ONE commit, the message file written with the Write tool; the commit gate (py_compile, ds-precommit, ruff py39) must pass. Print `git rev-parse HEAD` as the CODE COMMIT.
2. Write the proof instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~33/MDPF_CANON.TO-CN-s-6.global-axis-drops-2026-10-16.proof_of_spec.json` (beside the order's own file stem, which is the name the pipeline gate searches for). **Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, and only when both criteria pass. Commit through `.tools/safe-commit.sh` with a message file written by the Write tool, paths = the instance and this order file. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W33-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the code commit, the diff (one line per file), the output lines of both criteria, the instance commit, the verdict line and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11, amendment 2, issuer 2.0.0_SA_COO~D1, on the fire read `round11/real_run/FIRE_READ_20261017.md` @882da2f5f8 (row `MDPF_CANON-D1-S33`), the CTO's rulings msgs 7594 and 7600 and PRD v2.29 @11ea6ef573 (a change-log bump). The gate code was read at the pin: `dim_mdpf_aggregate_aua_timeseries.py` L1791-1815 (clause (v) loops every date), L2368 (the axis is the union), L2860 (`as_of_last = dates[-1]`), L2712 (the call). The offline reproduction ran `build_global_artifact` over the fire's three staged legs at the pin: it refuses with the fire's exact message; the reference change emits 498 dates, `as_of_last` 2026-10-15, the headline present, the five core models non-None from 2026-07-21, and `model_aua` +X where X is the Muni account's value on 2026-10-15 (63,473,980.96) with `non_model_aua` equal; its `opal_aggregate_aua` is +34.21M because the offline build has no tax/SMA additive overlay (the consolidator adds it): the deployed function's D4 dry run, not this offline build, is the arbiter of the headline.
- **Build base:** the deployed pin `d2f734fbac` (CTO msg 7600), NOT box/dell1 HEAD. The slot ~33 branch is `wk-MDPF_CANON-33`; the order file is placed on it as the grant.
- **Deploy:** the 2026-10-18 13:30Z fire's ONE gold change (CTO msgs 7594, 7600), by a CloudOps ADHOC order after a never-widen pair (COO half, CTO half); D4 dry run (no write) must show Global `as_of` = the frontier, a non-None headline and no None `model_value` inside the covered range, else the change does not ride the fire.
- **Not in this cell:** the deploy, the pair, any change to Cottonwood, 49 Financial or Inflection, to either gate, or to the exempt list.

**Fanout:** 1 of 1 chain (this amendment's), cap 8. Slot ~33. Base: the deployed pin, not the issuance commit.

<status>staged</status>
<round>11</round>
<workstream>GLOBAXIS</workstream>
<to_id>MDPF_CANON.TO-CN-s-6</to_id>
<slot>~33</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
