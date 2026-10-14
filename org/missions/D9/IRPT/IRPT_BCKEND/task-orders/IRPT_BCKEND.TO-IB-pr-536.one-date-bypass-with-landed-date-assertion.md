# TO IRPT_BCKEND.TO-IB-pr-536 -- BUILD the one-firm, one-date operator bypass of the publish gate's `source_frontier_older` condition, with the landed-date-equals-`as_of` assertion on that path and a mutant that fails, OFFLINE (CTO round-193 analysis item 2 and ruling "The 2026-10-08 replay route" @e9dabffe7b; rows D2-W381-S2, D2-W381-S3)

<to_id>IRPT_BCKEND.TO-IB-pr-536</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~382</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>193</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-193 analysis (ruling: "The operator bypass for ONE firm (49financial) and ONE date (2026-10-08). No gap-fill exemption in `evaluate_publish_gate`... Before the bypass, a LOCAL build cell makes the bypass path assert that the landed date equals `as_of`, and refuse otherwise, with a mutant that fails.") | **Decomp cell:** `IB-pr-536` (decomposition section 185) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree (the only place you write):** `C:/dev/wk-IRPT_BCKEND-382` on a branch cut from the current branch. Commit there with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~382 <0.9.0_WK_IRPT_BCKEND~382@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). The `portal` gitlink shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected, not a finding. **Paths you post are `file:///` absolute URIs or markdown links to them.**

**Client data rule:** no account id, client id, position value, quantity or holding name in any tracked file; the tests use synthetic fixtures only.

**Cell `IB-pr-536` (inlined).** 49financial's served series has no row for 2026-10-08. The producer's own publish gate refuses a replay of that date (`evaluate_publish_gate`, condition `source_frontier_older`: the candidate's source date is older than the served frontier, 2026-10-12). The CTO ruled that the replay goes by an **operator bypass for ONE firm and ONE date, never a gate exemption**: the gate stays as it is for every scheduled fire and every other run. Also, `run_firm` does not assert that the date it lands equals the date the operator asked for (`as_of` is a source-selection CUTOFF; the landed date is `snapshot.clocks.business_date`; with a missing partition the builder would select an OLDER date whose row exists and a bypass would REPLACE that row). **This order builds the bypass, with the assertion, offline. It uploads, applies and runs nothing against AWS.** All edits are in `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` plus ONE new test file.

**Build, exactly this and no more** (read `run_firm`, `main`, `evaluate_publish_gate`, `land` and `tests/test_holdings_publish_gate.py` first; the existing test file's offline versioned in-memory S3 under a REAL `HoldingsPublication` is your fixture base, imported and not edited):
1. **A new CLI flag** `--allow-older-date YYYY-MM-DD` on `main`. `ap.error` (before any firm runs) unless ALL hold: `--upload` is given; `--firms` is exactly `49financial`; `--as-of` is given and EQUALS the flag's value; no `--qa`; no `--dry-run`; no `--account-id`; the value is a well-formed date.
2. **`run_firm` gains a keyword `allow_older_date: "str | None" = None`** (default None; `main` passes it only from the flag; the scheduled invocation, which passes no `--as-of`, is untouched and its behaviour byte-identical).
3. **The assertion**, wrapped in the marker lines `# BEGIN ONE-DATE-ASSERT` and `# END ONE-DATE-ASSERT` (exactly one such block in the file; the check removes it to run the mutant), placed right after `publication_date` is computed and BEFORE the gate and any write: if `allow_older_date is not None and publication_date != allow_older_date`, raise `RuntimeError("REFUSED: the landed date %s is not the requested date %s ..." )` naming both dates. Nothing is written before it (the publisher's `begin()` read is the only call that precedes it).
4. **The waiver**, only when `allow_older_date is not None`, after `evaluate_publish_gate` returns: remove from `gate["conditions"]` ONLY the conditions whose `condition == "source_frontier_older"` and whose `candidate_frontier == allow_older_date`; if NO condition remains the outcome is `PUBLISHED` and `gate["bypass"] = {"waived": ["source_frontier_older"], "date": allow_older_date}`; any other condition left (an `account_lost`, a `reconcile_difference`, anything) keeps the outcome `REFUSED` and the refusal record path as today. No other gate behaviour changes, for any firm.
5. **New tests** in `data/assets/scripts/gold/investor_reporting/tests/test_holdings_bypass_one_date.py` (at least EIGHT `def test_` functions; offline; named after what they prove): the flag refuses without `--upload`, with another firm, without `--as-of`, with an `--as-of` different from the flag, and with `--qa`; a requested date whose source partition is absent (the builder returns an older date) raises the assertion refusal and writes NOTHING (the fixture bucket's object and version counts are equal before and after); a good replay of an older date lands that date, adds exactly ONE index row, leaves `latest_date` and every other row's bytes unchanged, and the gate record shows the waiver; a candidate that is older AND loses an account stays `REFUSED` under the flag; the scheduled path (no flag) still REFUSES an older candidate exactly as before.

**Do, in this order:**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit` (state it). Read the code named above.
2. Build 1 to 4, write 5, run `python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_holdings_bypass_one_date.py data/assets/scripts/gold/investor_reporting/tests/test_holdings_publish_gate.py -q` until everything passes.
3. Run the mutant yourself: copy the investor_reporting package to scratch OUTSIDE the worktree (`C:/dev/_scratch382/`), delete the BEGIN/END block from the copy, and run the new tests there: at least one MUST fail. Record how many failed. Delete the scratch at the end with a short bounded script.
4. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~382/IB193-2_record.json`: `{"base_commit":"<40hex>","changed_paths":["data/assets/scripts/gold/investor_reporting/holdings_snapshot.py","data/assets/scripts/gold/investor_reporting/tests/test_holdings_bypass_one_date.py"],"tests_total":<n>,"tests_passed":<n>,"mutant_tests_failed":<n>,"default_path_unchanged":true,"refusals_tested":["no_upload","wrong_firm","no_as_of","as_of_differs_from_allowed_date","landed_date_differs","qa"],"notes":["what each fact rests on and what was not run"]}`. `changed_paths` lists the PRODUCT paths only (the deliverables folder and the investigation file are not listed).
5. **Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB193-2_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>` (every `artifacts_produced` row pinned to the commit that carried the artifact: commit the code, the tests, the record and the criteria output FIRST, then the instance last), and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR code or tests (never the check). Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB193-2-AC1" cell_refs="IB-pr-536"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r193/p193_cells.py" . IB193-2-AC1</invocation><expect>IB193-2-AC1 PASS</expect></criterion>
<criterion id="IB193-2-AC2" cell_refs="IB-pr-536"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r193/p193_cells.py" . IB193-2-AC2</invocation><expect>IB193-2-AC2 PASS</expect></criterion>
<criterion id="IB193-2-AC3" cell_refs="IB-pr-536"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r193/p193_cells.py" . IB193-2-AC3</invocation><expect>IB193-2-AC3 PASS</expect></criterion>

<expected_criteria>IB193-2-AC1, IB193-2-AC2, IB193-2-AC3</expected_criteria>

What the checks grade: AC1 the new test file and the existing gate test file both pass (at least eight new tests); AC2 exactly one BEGIN/END ONE-DATE-ASSERT block, and the new tests FAIL on a copy of the package with that block removed; AC3 the record, `changed_paths` equal to the git diff since `base_commit` (the deliverables folder and the investigation file aside), nothing outside the producer file and the new test, `default_path_unchanged` true, all tests passed, at least one mutant failure, the six refusals tested named, a note, and no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block and the scratch directory. OFFLINE BUILD. **Nothing is invoked, written to AWS, uploaded, applied, deployed or sent;** the tests use the in-memory fixture. The bundles are NOT re-minted by this order (a later release under its own pair).
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a change to any other function's behaviour; a file outside `<paths>`; a client identifier in a tracked file; a need to touch `evaluate_publish_gate` beyond the waiver in step 4 (the CTO ruled no gate exemption: the waiver sits in `run_firm`, scoped by the flag). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W382-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with the usual fields, including `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_bypass_one_date.py
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~382/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 185 (round 193, workstream ~P), cell `IB-pr-536`.
<owned_cells>IB-pr-536</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB193-2-AC1, IB193-2-AC2, IB193-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~382/IRPT_BCKEND.TO-IB-pr-536.one-date-bypass-with-landed-date-assertion.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order edits one producer file (`holdings_snapshot.py`, used by the scheduled holdings fires and the three standalone bundles) and adds one offline test; the new behaviour is reachable only through a flag no scheduled fire passes and the bundles are not re-minted here, so no served byte moves; the release that would carry it is a later round under its own signed pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p193_cells.py IB193-2 dry-run at base on dell2 2026-10-14 ~12:5xZ: AC1, AC2, AC3 FAIL (no new test, no marker block, no record). Positive control in a temp git repo the run created itself (a stub producer with the marker block, a stub test file, a record; removed): all three PASS; negatives, each failing its own arm: no marker block, tests that still pass with the block removed, a path outside the grant, changed_paths that differ from the diff.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~382` (worktree `C:/dev/wk-IRPT_BCKEND-382`). Class LOCAL (offline code and tests; no served byte; a data/assets path). The premises are the CTO's ruling and the round-192 rows D2-W381-S2 and D2-W381-S3 (the gate refuses an older date; `publish()` does not assert the landed date equals `as_of`), and my own read of `run_firm` at HEAD.
</preflight>
