# TO IRPT_BCKEND.TO-IB-pr-530 -- BUILD the directory exemption repair: the publish gate's all-UNKNOWN test reads source-marked statuses only and ignores the entries the directory builder carries forward (CTO ruling 7489 and round-190 analysis item 2 @6e527b13c6; rows D2-S158, D2-S160)

<to_id>IRPT_BCKEND.TO-IB-pr-530</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~377</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>190</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-190 analysis (item 2: "the all-UNKNOWN test reads source-marked statuses only. A test re-plays Cottonwood's 2026-10-12 directory, with its 2 carried TERMINATED entries, and the candidate passes the gate with one listed lost account") | **Decomp cell:** `IB-pr-530` (decomposition section 182) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-377` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~377 <0.9.0_WK_IRPT_BCKEND~377@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push, deploy, invoke a Lambda or call AWS (everything is offline). Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Cell `IB-pr-530` (inlined).** The holdings publish gate (`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, `evaluate_publish_gate` about line 3020) refuses a candidate on `account_lost` unless the account is recorded closed by the firm's source, or `marks_no_closures()` is true, in which case the lost account is LISTED (`account_lost_not_refused`) and the candidate publishes (PRD v0.33). `directory_marks_no_closures(s3, bucket, firm_id)` (about line 3010) returns true only when the landed directory has entries and EVERY entry's `termination.indicator` is UNKNOWN: Cottonwood's source has no status column, so it marks every entry UNKNOWN. But the directory builder (`directory_runner.py`) CARRIES FORWARD entries for clients removed from the source as `TERMINATED` with `termination.effective_date` and a `cohort.capability_facts` string beginning `source_removed_on=` (the constant `SOURCE_REMOVED_FACT_PREFIX` and the helper `_source_removed_on_of`, `directory_runner.py` about lines 900-920). Those marks are this pipeline's own, not the source's; Cottonwood's 2026-10-09 and 2026-10-12 directories carry 10 and 2 of them, which makes "every entry UNKNOWN" false and has made the gate refuse Cottonwood since 2026-10-13T14:17Z. **The repair: the all-UNKNOWN test reads source-marked statuses only.**

**The design (build exactly this, no more):**
1. In `directory_marks_no_closures`: ignore every entry that is a carried-forward entry (its `cohort.capability_facts` holds a string starting `source_removed_on=`). Over the remaining (source-marked) entries: if there are none, return False (fail closed: an absent, empty or all-carried directory marks nothing); otherwise return true exactly when every remaining entry's indicator (a missing one counting as UNKNOWN, as today) is UNKNOWN. A source-marked TERMINATED or ACTIVE entry keeps the result False, as today. You may add one small private helper function immediately before `directory_marks_no_closures` (for example `_carried_forward(entry)`); do not import from `directory_runner.py` (this file ships in a bundle without it): re-state the prefix as a module constant next to the helper, with a comment naming `directory_runner.SOURCE_REMOVED_FACT_PREFIX`.
2. `closed_account_ids` (the closed-account exemption, which reads TERMINATED entries) is NOT changed. `evaluate_publish_gate` is NOT changed.
3. **Confinement (the check enforces it):** change ONLY `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (hunks only at `_directory_entries`'s neighbour, `closed_account_ids`'s neighbour and `directory_marks_no_closures`) and ADD ONLY `data/assets/scripts/gold/investor_reporting/tests/test_directory_exemption_source_marks.py`.

**Tests (`tests/test_directory_exemption_source_marks.py`, at least FOUR test functions named `test_...`; no network):** stub `holdings_snapshot._directory_entries` (monkeypatch) to prove: all UNKNOWN is true; UNKNOWN plus carried TERMINATED entries is true; UNKNOWN plus a source-marked TERMINATED entry (no marker) is false; an ACTIVE entry is false; no directory and an empty directory are false; only carried entries is false. ADD a REPLAY test through the real gate, in the style of `tests/test_holdings_publish_gate.py` (read its `seeded`, `make_snapshot`, `fire` and `_directory` helpers; you may import that module from your test): a directory of many UNKNOWN entries plus two carried TERMINATED entries (each with `termination.effective_date` and the `source_removed_on=` fact) and a candidate that lost one account PUBLISHES, listing that account under `account_lost_not_refused`, as Cottonwood's 2026-10-12 directory would. Run from `data/assets/scripts/gold/investor_reporting`: `python -m pytest -q -p no:cacheprovider tests/test_holdings_classification.py tests/test_holdings_cusip_fallback.py tests/test_holdings_narrowed.py tests/test_holdings_unclassified.py tests/test_holdings_snapshot.py tests/test_holdings_publish_gate.py tests/test_holdings_multi_asset_v1_enum.py tests/test_holdings_display.py tests/test_holdings_cash_rule.py tests/test_directory_exemption_source_marks.py`: the 107 at base and yours must all pass (at least 111 passed). Do not run `test_holdings_rearm_trigger.py` (it reads live AWS state).

**Do, in this order:** (1) `git rev-parse HEAD` before your first commit is `base_commit` (state it); (2) read `holdings_snapshot.py` lines 2980-3075, `directory_runner.py` lines 890-940 and `tests/test_holdings_publish_gate.py`; (3) make the change and write the tests; (4) run the ten test files; (5) run the three criteria below from your worktree root, record each output and exit code verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~377/IB190-2_criteria_output.txt`; (6) write the proof instance named under `<proof_of_spec>`, validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the code, the tests and the criteria output FIRST, then the instance last), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR change (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 200` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB190-2-AC1" cell_refs="IB-pr-530"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r190/p190_cells.py" . IB190-2-AC1</invocation><expect>IB190-2-AC1 PASS</expect></criterion>
<criterion id="IB190-2-AC2" cell_refs="IB-pr-530"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r190/p190_cells.py" . IB190-2-AC2</invocation><expect>IB190-2-AC2 PASS</expect></criterion>
<criterion id="IB190-2-AC3" cell_refs="IB-pr-530"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r190/p190_cells.py" . IB190-2-AC3</invocation><expect>IB190-2-AC3 PASS</expect></criterion>

<expected_criteria>IB190-2-AC1, IB190-2-AC2, IB190-2-AC3</expected_criteria>

What the checks grade: AC1 the ten-file set passes (at least 111), `tests/` holds exactly the 33 baseline files plus the new one, and `holdings_snapshot.py` differs from its base blob only in the directory-reading functions; AC2 `directory_marks_no_closures` on the check's own entries (all UNKNOWN true; plus carried TERMINATED true; plus a source-marked TERMINATED false; plus an ACTIVE false; none, empty and only-carried false); AC3 the check's OWN replay through the real gate with the existing publish-gate helpers (a directory of UNKNOWN plus two carried TERMINATED entries lets a candidate with one lost account PUBLISH, listing it; the same directory with an older source frontier is still refused; a directory that marks a closure at the source still refuses the lost unmarked account). Do not edit the checks.

## BOUNDS

- **Write surface:** exactly the `<paths>` below. **BUILD ONLY and offline:** nothing is deployed, uploaded, applied or invoked; no AWS call; the gate on the served Cottonwood does not change until a later, separately signed release.
- **Refusal clause:** STOP, file a row and report if: any baseline test fails at base before your change (say which; do not edit it); the repair cannot be built without touching another function or file; the carried-forward marker in the directory builder is not what this order states (say what it is; do not guess). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W377-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with the usual fields, including `grounding`) and keep working.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_directory_exemption_source_marks.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~377/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 182 (round 190, workstream ~P), cell `IB-pr-530`.
<owned_cells>IB-pr-530</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB190-2-AC1, IB190-2-AC2, IB190-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~377/IRPT_BCKEND.TO-IB-pr-530.directory-exemption-reads-source-marks-only.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the served holdings are NOT changed by this order (build only, offline); the code path changed is `directory_marks_no_closures`, read by the gate at one call site (`run_firm`, about line 3170); the firms it changes anything for are those whose directory carries TERMINATED entries the builder carried forward (Cottonwood today; the directory builder's header says 49financial marks closures from `dim_account`, and Inflection's directory shape is NOT read here: the round-191 packet counts, per firm, which refused candidates would then publish); which refused candidates would then publish is counted in the round-191 packet; the release, its pair and the publish-gate interplay are later cells.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p190_cells.py IB190-2 dry-run at base on dell2 2026-10-14 ~04:1xZ: AC1 FAIL (no new test file), AC2 FAIL (UNKNOWN plus a carried TERMINATED entry reads false), AC3 FAIL (the replay candidate is REFUSED). Positive control in a throwaway git worktree at HEAD (created and removed by the run; my own hand edit of the function and a four-test file): all three PASS; negatives, each failing its own arm: the function unchanged (AC2 and AC3), an only-carried directory reading true, a rule that ignores every source mark, a hunk in another function, too few tests, no new test file.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~377` (worktree `C:/dev/wk-IRPT_BCKEND-377`). Class LOCAL (offline code and tests; no served byte; a data/assets path). The premises are the CTO's ruling 7489 and my own read of the 2026-10-12 directory (271 entries, 2 carried TERMINATED, row D2-S160) and of the code.
</preflight>
