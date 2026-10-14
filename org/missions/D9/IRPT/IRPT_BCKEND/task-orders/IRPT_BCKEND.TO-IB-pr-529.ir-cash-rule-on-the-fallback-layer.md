# TO IRPT_BCKEND.TO-IB-pr-529 -- BUILD the IR cash rule on the bd-securities FALLBACK layer too: the one `apply_cash_rule` is also called at the fallback return of `classify_security` (CTO round-190 analysis item 1 @6e527b13c6; the CVO's cross-page call v90 ruled; rows D2-S156, D2-S162)

<to_id>IRPT_BCKEND.TO-IB-pr-529</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~376</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>190</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-190 analysis (item 1: "The same `apply_cash_rule` is called at the bd-securities fallback return as well: one definition, two call sites") | **Decomp cell:** `IB-pr-529` (decomposition section 182) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-376` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~376 <0.9.0_WK_IRPT_BCKEND~376@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push, deploy, invoke a Lambda or call AWS (everything is offline). Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Cell `IB-pr-529` (inlined).** Round 189 built the IR cash rule in `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`: `apply_cash_rule(result)` (about line 952) sets `asset_class` to `cash` when the result's `sub_asset_class`, trimmed and lower-cased, equals `cash`; `classify_security` (about lines 962-1004) calls it ONCE, at the canonical-row return. The CTO ruled that a cash fund must read Cash on every page, whichever layer answers for it, so **the same function is also called at the bd-securities fallback return** (the last `return` of `classify_security`, the one with `class_source` `FALLBACK_CLASS_SOURCE`): one definition, two call sites. Cottonwood's 215 and Inflection's 67 fallback cash-sub holdings are the expected movers.

**The design (build exactly this, no more):**
1. The fallback return becomes `return apply_cash_rule({...})`, wrapping the dict it builds today. The canonical-branch call stays. The Black Diamond CASH-line early return (a node whose ticker and description are both CASH) stays untouched, before both layers.
2. Update the docstring of `apply_cash_rule` so it says the rule acts on the canonical-row and the fallback returns (a hunk inside that function's docstring is allowed). Change nothing else: not `ASSET_CLASS_VALUES`, not `bd_securities_fallback.py`, not any function other than `classify_security` and the docstring above.
3. **Tests, in the existing `tests/test_holdings_cash_rule.py` (the only test file you touch):** the test `test_a_fallback_table_row_with_cash_sub_is_not_changed_by_the_rule` asserts the OLD design and must be REWRITTEN to the new one (a fallback table row with sub Cash serves `cash`, with its sub, basis `TABLE` and the fallback `class_source`). ADD at least THREE tests: a fallback NAME_ALIAS row with sub Cash serves cash (basis `NAME_ALIAS`); a fallback row with sub `Money Market` and one with a null sub stay as the fallback answers; an equity fallback row is unchanged. Keep the in-memory fixture style of the existing file (no network). Add no other test file.

Run from `data/assets/scripts/gold/investor_reporting`: `python -m pytest -q -p no:cacheprovider tests/test_holdings_classification.py tests/test_holdings_cusip_fallback.py tests/test_holdings_narrowed.py tests/test_holdings_unclassified.py tests/test_holdings_snapshot.py tests/test_holdings_publish_gate.py tests/test_holdings_multi_asset_v1_enum.py tests/test_holdings_display.py tests/test_holdings_cash_rule.py`: all must pass (the 107 at base, one of them rewritten, plus yours: at least 109 passed). Do not run `test_holdings_rearm_trigger.py` (it reads live AWS state).

**Do, in this order:** (1) `git rev-parse HEAD` before your first commit is `base_commit` (state it); (2) read `holdings_snapshot.py` lines 940-1010 and `tests/test_holdings_cash_rule.py`; (3) make the change and the tests; (4) run the nine test files; (5) run the three criteria below from your worktree root, record each output and exit code verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~376/IB190-1_criteria_output.txt`; (6) write the proof instance named under `<proof_of_spec>`, validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the code, the tests and the criteria output FIRST, then the instance last), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR change (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 200` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB190-1-AC1" cell_refs="IB-pr-529"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r190/p190_cells.py" . IB190-1-AC1</invocation><expect>IB190-1-AC1 PASS</expect></criterion>
<criterion id="IB190-1-AC2" cell_refs="IB-pr-529"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r190/p190_cells.py" . IB190-1-AC2</invocation><expect>IB190-1-AC2 PASS</expect></criterion>
<criterion id="IB190-1-AC3" cell_refs="IB-pr-529"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r190/p190_cells.py" . IB190-1-AC3</invocation><expect>IB190-1-AC3 PASS</expect></criterion>

<expected_criteria>IB190-1-AC1, IB190-1-AC2, IB190-1-AC3</expected_criteria>

What the checks grade: AC1 the nine-file set passes (at least 109), `tests/` holds exactly the 33 files it holds at base (no new file), and `holdings_snapshot.py` differs from its base blob only inside `classify_security`, the `apply_cash_rule` docstring and `cusip_key`'s neighbour; AC2 the behaviour on the check's own stub classifier (a fallback table row and a name-alias row with a Cash sub, and a padded lower-case one, serve cash with their sub, basis and the fallback `class_source`; Money Market, equity and null-sub fallback rows are unchanged; a canonical Cash row still serves cash; the canonical equity and Money Market rows are unchanged; the CASH-line rule is unchanged); AC3 exactly one function named like `cash_rule`, called exactly twice inside `classify_security` (one before the fallback `answer` line, one after it) and nowhere else, and `ASSET_CLASS_VALUES` unchanged. Do not edit the checks.

## BOUNDS

- **Write surface:** exactly the `<paths>` below. **BUILD ONLY and offline:** nothing is deployed, uploaded, applied or invoked; no AWS call; the served holdings do not change until a later, separately signed release.
- **Refusal clause:** STOP, file a row and report if: any baseline test fails at base before your change (say which; do not edit it other than the one rewritten); the rule cannot be built without touching another function or file; a fallback fixture in the existing tests has a non-string `sub_asset_class` (say what it is). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W376-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with the usual fields, including `grounding`) and keep working.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_cash_rule.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~376/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 182 (round 190, workstream ~P), cell `IB-pr-529`.
<owned_cells>IB-pr-529</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB190-1-AC1, IB190-1-AC2, IB190-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~376/IRPT_BCKEND.TO-IB-pr-529.ir-cash-rule-on-the-fallback-layer.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served holdings are NOT changed by this order (build only, offline); the code path changed is the fallback return of `classify_security`, the single producer-side classifier (one call site, `holdings_snapshot.py` about line 1040); the movers it adds are the fallback layer's cash-sub holdings (Cottonwood 215 and Inflection 67 by the round-188 count and the round-189 split), which the round-190 packet re-reads; the release, its pair and the publish-gate interplay are later cells.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p190_cells.py IB190-1 dry-run at base on dell2 2026-10-14 ~04:1xZ: AC1 FAIL (the set holds 107 tests, 109 required), AC2 FAIL (a fallback Cash row stays fixed_income), AC3 FAIL (one call, two required). Positive control in a throwaway git worktree at HEAD (created and removed by the run; my own hand edit of the fallback return, the rewritten test removed and three added): all three PASS; negatives, each failing its own arm: the fallback call absent (AC2 and AC3), a third call, Money Market also moving, the class enum changed, a hunk in another function, too few new tests, an extra test file.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~376` (worktree `C:/dev/wk-IRPT_BCKEND-376`). Class LOCAL (offline code and tests; no served byte; a data/assets path, not infrastructure). The premises (the two layers, the single function) are the round-189 build I merged and read.
</preflight>
