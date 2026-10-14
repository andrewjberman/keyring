# TO IRPT_BCKEND.TO-IB-pr-527 -- BUILD the IR holdings class rule from ONE shared definition: on the canonical-row branch of `classify_security`, a row whose `sub_asset_class` is cash serves the cash class (CTO round-189 analysis item 2 @318056547a; count IB-pr-526; row D2-S156; D2's read IR_HOLDINGS_CLASS_SOURCE.json)

<to_id>IRPT_BCKEND.TO-IB-pr-527</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~374</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>189</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-189 analysis (item 2: "One shared rule: a holding whose sub-class is cash-type serves the cash class") and ruling call 3's note (FDRXX on Inflection resolves on the canonical branch, so the rule is canonical-only) | **Decomp cell:** `IB-pr-527` (decomposition section 181) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-374` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~374 <0.9.0_WK_IRPT_BCKEND~374@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push, deploy, invoke a Lambda or call AWS (everything is offline). Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Cell `IB-pr-527` (inlined).** Andrew's point: the Investor Reporting Holdings page shows FDRXX (a money-market fund) as Fixed Income; it should be Cash. In `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, `classify_security` (about lines 952-994) serves a canonical `etf-classifications` row's `asset_class` exactly as stored (CTO ruling 103169) and carries its `sub_asset_class` beside it. The canonical row for FDRXX reads asset_class `fixed_income` with sub_asset_class `Cash`. **The rule to build: on the canonical-row branch, when the row's `sub_asset_class`, trimmed and lower-cased, equals `cash`, the served `asset_class` is `cash`, whatever the row stores. Nothing else changes.**

**The design (build exactly this, no more):**
1. **One new top-level function** named `apply_cash_rule(result)`, placed immediately BEFORE `classify_security` (after `cusip_key`). It takes the result dict the canonical branch builds, and when `result.get("sub_asset_class")` is a string that, trimmed and lower-cased, equals `cash`, sets `result["asset_class"] = "cash"`; it returns `result`. Any other value (`None`, `Money Market`, `T-Bill`, `Short Duration`) is left alone. Put a short docstring naming the rule and row D2-S156.
2. **One call, on the canonical branch only:** the single `return {...}` that ends the canonical-row branch of `classify_security` (the one with `class_source` `CANONICAL_CLASS_SOURCE`) becomes `return apply_cash_rule({...})`. The CUSIP-key hit uses the same return, so it is covered by the same one call. **The fallback return (the bd-securities layer) and the Black Diamond CASH-line early return stay exactly as they are**: the CTO ruled the rule canonical-only because FDRXX on Inflection resolves on the canonical branch; the fallback layer's cash-sub-class holdings stay as served and are counted in the packet of the sister order.
3. **Confinement (the check enforces it):** change ONLY `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (hunks only at the new function, `classify_security`, and the line between them) and ADD ONLY `data/assets/scripts/gold/investor_reporting/tests/test_holdings_cash_rule.py`. Do not change `ASSET_CLASS_VALUES`, `bd_securities_fallback.py`, any other test, the source map or any `.tf`.

**Tests (`tests/test_holdings_cash_rule.py`, at least FIVE test functions named `test_...`):** copy the in-memory fixture style of `tests/test_holdings_narrowed.py` and `tests/test_holdings_classification.py` (a stand-in classifier whose `canonical_lookup` answers from a dict, over the real fallback class with an in-memory table; no network, no DynamoDB). Prove: a canonical `fixed_income` row with sub `Cash` serves `cash` with its sub, basis `TABLE` and the canonical `class_source`; the lower-case and padded sub `cash` serve cash; a CUSIP-key canonical hit with sub `Cash` serves cash; an `equity` row, an already-`cash` row and a `Money Market` row are not changed; a fallback-table row whose sub is `Cash` is NOT changed (stays `fixed_income`, fallback `class_source`). Run from `data/assets/scripts/gold/investor_reporting`: `python -m pytest -q -p no:cacheprovider tests/test_holdings_classification.py tests/test_holdings_cusip_fallback.py tests/test_holdings_narrowed.py tests/test_holdings_unclassified.py tests/test_holdings_snapshot.py tests/test_holdings_publish_gate.py tests/test_holdings_multi_asset_v1_enum.py tests/test_holdings_display.py tests/test_holdings_cash_rule.py`: the 101 at base and yours must all pass (at least 106 passed). (Do not run `test_holdings_rearm_trigger.py`: it reads live AWS state and fails at base for a reason that is not yours.)

**Do, in this order:** (1) `git rev-parse HEAD` before your first commit is `base_commit` (state it); (2) read `holdings_snapshot.py` lines 927-994, `tests/test_holdings_narrowed.py` and `tests/test_holdings_classification.py`; (3) make the change and write the tests; (4) run the nine test files; (5) run the three criteria below from your worktree root, record each output and exit code verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~374/IB189-1_criteria_output.txt`; (6) write the proof instance named under `<proof_of_spec>`, validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the code, the tests and the criteria output FIRST, then the instance last), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR change (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 200` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB189-1-AC1" cell_refs="IB-pr-527"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r189/p189_cells.py" . IB189-1-AC1</invocation><expect>IB189-1-AC1 PASS</expect></criterion>
<criterion id="IB189-1-AC2" cell_refs="IB-pr-527"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r189/p189_cells.py" . IB189-1-AC2</invocation><expect>IB189-1-AC2 PASS</expect></criterion>
<criterion id="IB189-1-AC3" cell_refs="IB-pr-527"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r189/p189_cells.py" . IB189-1-AC3</invocation><expect>IB189-1-AC3 PASS</expect></criterion>

<expected_criteria>IB189-1-AC1, IB189-1-AC2, IB189-1-AC3</expected_criteria>

What the checks grade: AC1 the nine-file classification set passes (at least 106 passed), `tests/` holds exactly the 32 baseline files plus `test_holdings_cash_rule.py`, and `holdings_snapshot.py` differs from its base blob only at `cusip_key` (the new function's neighbour), `classify_security` and module level; AC2 the behaviour above on the check's own stub classifier (a Cash sub serves cash on the canonical branch including the lower-case, padded and CUSIP-key forms; an equity row, an already-cash row, a Money Market row and a null sub are unchanged; a fallback-table row with sub Cash is unchanged; the Pathward CASH-line rule is unchanged); AC3 exactly one top-level function named like `cash_rule`, called exactly once, inside `classify_security` and before the fallback answer line, called nowhere else, and `ASSET_CLASS_VALUES` unchanged. Do not edit the checks.

## BOUNDS

- **Write surface:** exactly the `<paths>` below. **BUILD ONLY and offline:** nothing is deployed, uploaded, applied or invoked; no AWS call; the served holdings do not change until a later, separately signed apply moves the producer.
- **Refusal clause:** STOP, file a row and report if: any of the 101 baseline tests fails at base before your change (say which; do not edit them); the rule cannot be built without touching a function other than `classify_security` and the new one, or a file outside the two named; a canonical row's `sub_asset_class` is not a string in some existing fixture (say what it is; do not work around it). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W374-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with the usual fields, including `grounding`) and keep working.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_cash_rule.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~374/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 181 (round 189, workstream ~P), cell `IB-pr-527`.
<owned_cells>IB-pr-527</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB189-1-AC1, IB189-1-AC2, IB189-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~374/IRPT_BCKEND.TO-IB-pr-527.ir-holdings-class-rule-build.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served holdings are NOT changed by this order (build only, offline); the code path changed is the canonical-row branch of `classify_security`, the single producer-side classifier call (one call site, `holdings_snapshot.py` about line 1032); the count of nodes it will move per firm is IB-pr-526's (upper bounds 32, 253, 841) and the sister order IB-pr-528's split by layer; the release, its pair and the publish-gate interplay (Cottonwood's candidates are refused by the gate today) are later cells.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p189_cells.py IB189-1 dry-run at base on dell2 2026-10-14 ~03:0xZ: AC1 FAIL (no new test file), AC2 FAIL (FDRXX stays fixed_income), AC3 FAIL (no rule function). Positive control in a throwaway git worktree at HEAD (created and removed by the run; my own hand implementation of the design plus a five-test file): all three PASS (106 or more tests); negatives, each failing its own arm: the rule also on the fallback layer, a strict-case match only, Money Market also moving, a second call, the class enum changed, a hunk in another function, an extra test file, too few tests.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~374` (worktree `C:/dev/wk-IRPT_BCKEND-374`). Class LOCAL (offline build; no served byte, no AWS call; the producer lives under `data/assets/scripts`, not an infrastructure path). The premises (the rule, the single call site, the canonical row for FDRXX reading fixed_income with sub Cash) are D2's read and my own read of the live canonical table at ~02:5xZ.
</preflight>
