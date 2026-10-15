# MDPF_SECHIST task order -- `A2-cap-62` -- DIRECT ACT: A2 BACKFILL_CAP 50 to 62 (Andrew-direct da0c): one line in etf_daily_pull.py

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP.md</decomp_doc>
<owned_cells>A2-cap-62</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_SECHIST~25</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the schedule is unchanged; the daily 07:00 ET pull reads the constant, and the act adds no schedule, trigger or rule
comp-iam: DECLARED-NOT-APPLICABLE no new boto3 call, no new grant; the run block already reads and writes the keys it writes today
comp-adversary: RUN -- (the three checks dry-run at the base 2026-10-15 ~23:5xZ: r7a2_diff_check FAIL, r7a2_default_cap FAIL (BACKFILL_CAP=50 planned=50), r7a2_pull_tests PASS (13); the diff check's GREEN arm exercised in a throwaway repo (OK on a one-line commit, BAD with an extra file); BLIND: the live run on site Z, the ledger's spend on the day, any reader of the constant outside first-party source)
</preflight>

## 1. THE SIGNED SECTION -- inlined verbatim from both halves of the never-widen pair

### COO HALF
## integrations/bloomberg/pipeline/etf_daily_pull.py -- line 62, BACKFILL_CAP 50 to 62

**The act.** ONE line: `BACKFILL_CAP = 50` becomes `BACKFILL_CAP = 62` (+24%, inside the CTO's one step of at most +25%). No other byte of any file moves (the commit's diff is 1 insertion, 1 deletion, one path). A worker makes the commit on `box/dell1`; box-sync carries it to `CLOUD` and to site Z's working tree, where the daily 07:00 ET pull reads it.

**What reads the constant (counted from the code, `comp-find` denominator 18 hits / 100,234 files; first-party source hits 2):**
- `history_backfill_plan(..., cap=BACKFILL_CAP)`, the default bound at definition: called at L513 (the read-only `HISTORY-PLAN` entry, writes nothing) and at L713 (the run, no `cap` argument). N = 1 rule; plan order is sorted ticker, and the overflow is returned as `capped` for the next run.
- `data/mdpf/scripts/demque/reserve_estimate.py` L256 reads the literal from source into a note string only (a reader, no write).
- Tests: `test_etf_daily_pull_history_plan.py` passes `cap=50` explicitly, so none moves.


### CTO HALF
# NEVER-WIDEN -- CTO half: `integrations/bloomberg/pipeline/etf_daily_pull.py` BACKFILL_CAP 50 -> 62 (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~23:4xZ)

**Signs:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/NEVER_WIDEN_HALF_COO_SECHIST_A2_BACKFILL_CAP_62_20261015.md` @62b505c131,
sha256 `f04b805e597a8cf424cb2b1ba1e4cfb5c4748e92add671cfcd97f42b6650f372`. Authority: Andrew, "Positioning ETF pull can have slight increase"
(`ANDREW_DIRECT_20261015_233xZ_DA0C_POSITIONING_PULL_SLIGHT_INCREASE.md` @3353228c01). Read at HEAD: `etf_daily_pull.py:62` `BACKFILL_CAP = 50`.

**GIVEN.**
- Only that constant moves, 50 -> 62.
- No field, security, schedule, code path or shared budget file (`bbg_budget.json`) changes; the 9-30 hold stands for everything else.
- The first run on it reads the budget ledger.
- Rollback: the constant back to 50.

-- 1.0.0_SA_CTO~DELL1

## 2. WHERE THIS CAME FROM

Minted by `python .tools/direct-act-order.py mint` from the signed never-widen pair bounding this DIRECT act; round 6.

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/pipeline/etf_daily_pull.py
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~25/
org/missions/D8/MDPF/MDPF_SECHIST/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/MDPF/MDPF_SECHIST/task-orders/MDPF_SECHIST.TO-A2-cap-62.a2-backfill-cap-50-to.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
</paths>

## 4. BOUNDS

Bounded to the paths the signed pair names -- the pair bounds, the order grants. No path outside the <paths> block above is a write surface.

## 5. PROOF OF SPEC

<criterion id="A2-AC1" cell_refs="A2-cap-62"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R7A2_CHECKS/r7a2_diff_check.py</invocation><expect>A2-DIFF-OK</expect></criterion>
<criterion id="A2-AC2" cell_refs="A2-cap-62"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R7A2_CHECKS/r7a2_default_cap.py</invocation><expect>A2-CAP-OK planned=62 capped=8</expect></criterion>
<criterion id="A2-AC3" cell_refs="A2-cap-62"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R7A2_CHECKS/r7a2_pull_tests.py</invocation><expect>A2-TESTS-OK passed=13</expect></criterion>

<proof_of_spec>
Criterion ids: A2-AC1, A2-AC2, A2-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~25/MDPF_SECHIST.TO-A2-cap-62.a2-backfill-cap-50-to.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~25/MDPF_SECHIST.TO-A2-cap-62.a2-backfill-cap-50-to.proof_of_spec.json A2-AC1 A2-AC2 A2-AC3` BEFORE the flip. Your whole act: change line 62 of integrations/bloomberg/pipeline/etf_daily_pull.py from `BACKFILL_CAP = 50` to `BACKFILL_CAP = 62` and nothing else, make ONE commit with safe-commit under your granted paths (the file, your proof_of_spec instance and this order's status flip), then run the three invocations above.
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the proof_of_spec instance, flip <status> to complete, commit under the granted <paths> only.

<!-- ===================== RECORD FACE -- never travels to a worker ===================== -->

<status>pending</status>
<risk>WORLD</risk>
<direct_act>true</direct_act>
<slot>~25</slot>
<fabric>dell1</fabric>
