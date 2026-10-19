# MDPF_CANON task order -- `CN-s-7` -- GLOBAL'S AXIS KEEPS 2026-10-16: THE DROP SET IS EMPTIED (PRODUCER; FWD-9 head g, the Global fire)


<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-s-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~34</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the cell changes one constant in code the scheduled run already executes.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read, no new key prefix, no IAM change; the code reads the same legs it reads today.
comp-adversary: RUN by the issuer on DELL1 at the base (the deployed pin 128fce3524, a scratch worktree) -- `r11_cn_s_7.py real` 2 of 5 (S2 and S3 are controls the base already meets; S0, S1 and S4 are red: the base still drops the date, so Global ends 2026-10-15 over the live legs and the old legs EMIT instead of being refused); a scratch reference with the constant emptied reads 5 of 5 (the arms can pass); planted mutants each turn their named arms red: a wrong date in the set (S0), the set emptied but the date added to the exempt list (S0 and S4: the composition gate refuses the old legs), a computed drop of any date only the Cottonwood leg holds (S4).
EGRESS CLASS, declared: NONE (the worker writes no AWS and reads six files already on disk).
</preflight>

## 1. THE CELL -- `CN-s-7` (round 11, amendment 3)

**The cell, verbatim from the decomposition:** Global's axis keeps 2026-10-16: `GLOBAL_AXIS_DROP_DATES` becomes an empty frozenset (the mechanism and the constant stay; the date is no longer dropped), so Global's series, its `as_of_last` and its gates see 2026-10-16 again; the CN-s-6 test is replaced by one that asserts the date stays on the axis when all three legs carry it.

**Why (CTO ruling @176378e74d, row MDPF_CANON-D1-S36):** `CN-s-6` took 2026-10-16 off Global's axis because Cottonwood alone carried it and no catch-up was expected to fill it. The feeder has since written it: 49 Financial, Inflection and Cottonwood all end 2026-10-16 with values. The drop now holds Global at as_of 2026-10-15, one trading day behind its legs, and would leave 2026-10-16 as a hole in Global's series. The ruled fix is to stop dropping it.

**The edit, in `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` (an LF file; keep LF):**
1. Change the constant `GLOBAL_AXIS_DROP_DATES = frozenset({"2026-10-16"})` (about L1744) to `GLOBAL_AXIS_DROP_DATES = frozenset()` and rewrite the comment above it (about L1737-1743, ASCII only) to say: the set is EMPTY since the CTO ruling on row D1-S36 (2026-10-19); it was {2026-10-16} for CN-s-6 (CTO msgs 7594 and 7600) and was emptied because the feeder wrote 2026-10-16 for 49 Financial and Inflection; it stays as an ENUMERATED set, never a rule, and a date is never both in it and in `GLOBAL_CROSS_AXIS_EXEMPT_DATES`.
2. Leave the axis line in `build_global_artifact` (the `dates = sorted((set(a49["dates"]) | ...) - GLOBAL_AXIS_DROP_DATES)` of about L2377) exactly as it is.
3. Do NOT add 2026-10-16 to `GLOBAL_CROSS_AXIS_EXEMPT_DATES`. Do NOT write any "drop a date a leg lacks" rule in any form: a computed drop is a later round's question. Do NOT touch `_assert_cross_axis_coherence`, `_assert_global_composition`, the Cottonwood leg or any per-firm artifact.

**The test, in `data/mdpf/scripts/gold/tests/test_global_fold_flag2.py` (an LF file; it holds 16 passing tests plus the 3 failing ones that are not yours, row D1-S1, and the one CN-s-6 test):** REPLACE the test `test_s6_axis_drops_only_the_enumerated_date` (it asserts the drop and now contradicts the code) with `test_s7_axis_keeps_2026_10_16`, in the file's style (the helpers `_stub`, `_leg` and `_empty_cot`; `CORE` is the model key the nearby tests use): `D2 = ["2026-10-15", "2026-10-16"]`; `a49 = _leg(D2, [100.0, 101.0], [50.0, 51.0], [160.0, 161.0], {CORE: {"display_name": "I", "cohort_class": "model", "model_value": [100.0, 101.0], "account_count": [10, 10]}})`; `ainf` the same shape with smaller synthetic numbers (`[20.0, 21.0]`, `[5.0, 6.0]`, `[30.0, 31.0]`, counts `[2, 2]`); the Cottonwood leg `_empty_cot(D2)`; after `_stub([CORE])` call `spine.build_global_artifact(a49, ainf, cot)` and assert `g["dates"] == D2`, `g["as_of_last"] == "2026-10-16"` and `spine.GLOBAL_AXIS_DROP_DATES == frozenset()`. If building with two dates needs a different shape, copy the shape of `test_flag2_b_non_enumerated_none_still_poisons` and `test_m8_exempt_date_total_is_none_never_partial`, which already build two dates. Synthetic numbers only.

## 2. BOUNDS

1. **No AWS contact of any kind** (no read, write, invoke, deploy, install, push). The check reads six files already on disk, `C:/dev/_deploy_artifacts/canon_s6/fire_20261019/leg_{49financial,inflection,cottonwood}.json` and `C:/dev/_deploy_artifacts/canon_s6/leg_{49financial,inflection,cottonwood}.json`, outside the repo and client-scale: read them only through the check; never print a figure, an account id or a firm level from them.
2. Only the two code files in section 3 change (plus your deliverables and the surprise channel). Everything else is read-only; in particular the issuer's checks under `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/`.
3. No non-ASCII character in any line you add (the dim file already holds 21 non-ASCII bytes in older lines: leave them). Use the Edit tool; keep LF.
4. Your worktree is already on the deployed pin `128fce3524`; the earlier history stays. The change must be ONE commit on top of it, so the deploy can be built from that commit alone. If a step cannot be done as written, file a row naming the step and stop on that step.
5. Start EVERY shell call with `cd "C:/dev/wk-canon-s7-34"`: the proofs below resolve the repo root from the shell's current directory, and a reset cwd lands in the primary checkout, which reads the base (row D1-W33-S1).

## 3. SURFACES

<paths>
data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py
data/mdpf/scripts/gold/tests/test_global_fold_flag2.py
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-s-7.global-axis-keeps-2026-10-16.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~34/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, and the six leg files named in bound 1.

## 4. PROOF OF SPEC (literal; timeout 300 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-s-7"><invocation>cd "C:/dev/wk-canon-s7-34" &amp;&amp; timeout 300 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round11/checks/r11_cn_s_7.py" real 2&gt;&amp;1 | grep -E "^  S|REAL"; echo "exit=${PIPESTATUS[0]}"</invocation><expect>five lines S0 to S4 each reading PASS, then ROUND 11 CN-S-7 REAL: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-s-7"><invocation>cd "C:/dev/wk-canon-s7-34" &amp;&amp; timeout 300 python -m pytest data/mdpf/scripts/gold/tests/test_global_fold_flag2.py -q --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_within_window_carries_and_labels --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_beyond_window_absent_for_real --deselect data/mdpf/scripts/gold/tests/test_global_fold_flag2.py::test_carry_source_is_measured_never_interpolated; echo "exit=$?"</invocation><expect>no failure, at least 17 passed (16 pass at the base and the CN-s-6 test is replaced by the CN-s-7 test, so 17) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 runs the tree's real `build_global_artifact` over the live legs of the 2026-10-19 fire and over the 2026-10-17 legs (the control) and reads the emitted Global's axis, `as_of_last`, headline and core-model cells. AC2 is the regression guard plus your replaced test. They cannot prove what the deployed function builds in the cloud or what the served objects read after the next fire: that is the issuer's and CloudOps's read after the deploy (a never-widen pair first, a no-write dry run before the fire). There is no judgment criterion.

## 5. WHEN YOU ARE DONE

1. Commit the two code files through `.tools/safe-commit.sh --author "0.9.0_WK_MDPF_CANON~34 <0.9.0_WK_MDPF_CANON~34@opal.agent>" -F <msgfile> -- data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py data/mdpf/scripts/gold/tests/test_global_fold_flag2.py` as ONE commit, the message file written with the Write tool (a short ASCII subject starting `feat(MDPF_CANON CN-s-7, 0.9.0_WK_MDPF_CANON~34):`, a short body, then the line `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`); the commit gate (py_compile, ds-precommit, ruff py39) must pass. Print `git rev-parse HEAD` as the CODE COMMIT.
2. Write the proof instance at `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~34/MDPF_CANON.TO-CN-s-7.global-axis-keeps-2026-10-16.proof_of_spec.json`, copying the shape of the committed instance `org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~33/MDPF_CANON.TO-CN-s-6.global-axis-drops-2026-10-16.proof_of_spec.json` (read it first), with this order's criterion ids AC1 and AC2, the literal invocations above and the real outputs. **Flip this order's `<status>` to `complete` in the SAME commit as the instance**, and only when both criteria pass. Commit through `.tools/safe-commit.sh` with a message file written by the Write tool, paths = the instance and this order file. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.

A row id carries the dell1 infix: `MDPF_CANON-D1-W34-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the code commit, the diff (one line per file), the output lines of both criteria, the instance commit, the verdict line and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 11, amendment 3, issuer 2.0.0_SA_COO~D1, on the fire read `round11/real_run/FIRE_READ_20261019.md` @4d30e30e8a (row `MDPF_CANON-D1-S36`) and the CTO's ruling `ledger/CTO_RULING_S36_EMPTY_GLOBAL_AXIS_DROP_20261019.md` @176378e74d. The offline reproduction and the check are described in the decomposition amendment 3. The code was read at the pin: `dim_mdpf_aggregate_aua_timeseries.py` L1744 (the constant), L2377 (the axis subtraction), L1791-1815 (gate (v) over every date), L2860 (`as_of_last = dates[-1]`).
- **Both branches (for the pair):** all three legs carry 2026-10-16 at the fire: Global emits with `as_of_last` 2026-10-16 and its dated keys are NEW (no conflict); a leg loses the date before the fire: the date is on the axis through the other legs, gate (v) refuses Global, `errors` {global}, 12 of 16 built, exactly as on 2026-10-17 (the old-legs control arm S4).
- **Build base:** the deployed pin `128fce3524`; slot ~34 branch `wk-MDPF_CANON-34`; the order file on the worker's branch is the grant.
- **Not in this cell:** the deploy, the pair, any change to the gates or the exempt list, and the round-12 question (a drop computed at build time): row D1-S37.

**Fanout:** 1 of 1 chain, cap 8. Slot ~34. Base: the deployed pin, not the issuance commit.

<status>staged</status>
<round>11</round>
<workstream>GLOBAXIS2</workstream>
<to_id>MDPF_CANON.TO-CN-s-7</to_id>
<slot>~34</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
