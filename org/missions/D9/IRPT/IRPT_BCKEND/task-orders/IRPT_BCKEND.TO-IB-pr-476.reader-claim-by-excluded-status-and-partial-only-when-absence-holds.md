# TO IRPT_BCKEND.TO-IB-pr-476 -- BUILD ONLY: the performance reader's claim follows the excluded day's STATUS (C-CHAINCLAIM), and PARTIAL is sent only when an absence holds

<to_id>IRPT_BCKEND.TO-IB-pr-476</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~331</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>166</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6503 (CTO ROUND-166 ANALYSIS section 3 items 1 and 2; PRD ADDENDUM v0.48 contract C-CHAINCLAIM as amended by v0.49 section 1; row D2-W321-S2) | **Decomp cell:** `IB-pr-476` (decomposition section 158) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-331/` (bash `/c/dev/wk-irpt-bckend-331`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it).

**HARD BOUNDS.** BUILD ONLY. No Lambda invoked, no route called, nobody signs in, no vendor call, nothing deployed or uploaded, no AWS write. The ONLY AWS calls allowed are S3 `list` and `get` of the addresses the reader's own
composition builds over the SERVED holdings gold (as `deliverables/0.9.0_WK_IRPT_BCKEND~325/ib164_measure.py` does), up to the cap day 2026-10-08. NO account id in any form and NO account value in any file you write: counts, status tokens and hashes only.

**Read first (the contract).** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`: `## ADDENDUM v0.48` (contract C-CHAINCLAIM, about 45 lines, line 1211) and `## ADDENDUM v0.49` section 1 (line 1256: item 2 is amended). In short:
- the reader (`infra/aws/lambda/investor-reporting/performance/holdings_gold.py`, about lines 246, 254 and 286-292) drops every day whose status is not `OK`, chains the rest and says `measured`; its claim turns `inferred` only for a MISSING partition;
- ONE rule by the excluded day's STATUS, wherever the day sits in the window (first, interior, last, after the last OK day): `NO-PRIOR-HOLDINGS`, and `NON-POSITIVE-BASE` on a day whose PRIOR-DAY holdings carry NO position row, keep `measured`; a `NON-POSITIVE-BASE` day whose prior-day holdings carry at least one position row, `ALL-HOLDINGS-EXCLUDED`, `IMPLAUSIBLE-RETURN`, `FOLLOWS-DISCONTINUITY` and ANY status the rule does not name (seen or not) make the figure `inferred`;
- the answer carries, beside `days_linked`, two integers for the window: the days with no base and the days with a return left out (choose the member names; state them in the record).
The gold's own columns say what the account held the prior day: read `deliverables/0.9.0_WK_IRPT_BCKEND~325/IB164-1_STATUS_SET_AND_BASE_READ.md` (the `held_count`, `included_count`, `negative_count`, `cash_value` columns and the producer lines that define them) and reuse its classification of a NON-POSITIVE-BASE day by what the account held the prior day.

**Build (two things, one reader surface).**
1. **The claim by status.** Implement the rule above in the reader. The figures themselves do NOT move: only the claim and the two new integers. Where a window is missing a partition, today's `inferred` stays.
2. **PARTIAL only when an absence holds** (row IRPT_BCKEND-D2-W321-S2; search it by id in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`). By the code every holdings-basis answer is state PARTIAL because three absences are appended on every call
   (`holdings_gold.py` about lines 308-317: `accrual_basis`, `fees_and_income`, `money_weighted_return`; `entry.py` about lines 279-288: `partial = bool(outcome.get('absences') or outcome.get('refusals'))`). The CTO's ruling: an absence is added only when it holds. For EACH of the three, read the code and decide
   `ALWAYS_HOLDS` (the absence is a true statement about every holdings-basis answer, so PARTIAL on every answer is correct and the code stays) or `CONDITIONAL` (it holds only under a condition you name and cite; then gate it on that condition). Do not invent a condition: if the code gives none, the verdict is `ALWAYS_HOLDS`. Whatever you decide, state in the record each absence's verdict with its cite and in words.
   If every verdict is `ALWAYS_HOLDS`, the code for this part stays and the tests below prove the CURRENT rule (an answer with no excluded day and every absence holding reads PARTIAL; an `excluded_rows` absence appears only when a day is excluded).

**Tests (the build's own):**
- `infra/aws/lambda/investor-reporting/performance/tests/test_chain_claim.py`, at least FOUR tests over synthetic gold frames: (1) an account whose excluded days are only no-base days (`NO-PRIOR-HOLDINGS`; `NON-POSITIVE-BASE` with no prior-day position row) reads `measured` and carries its counts; (2) an account with one `ALL-HOLDINGS-EXCLUDED` day reads `inferred`; (3) a `NON-POSITIVE-BASE` day with a prior-day position row reads `inferred`; (4) a status the rule does not name reads `inferred`. A fifth is welcome: the same excluded day as the last row, the first row and after the last OK day reads the same.
- `infra/aws/lambda/investor-reporting/performance/tests/test_partial_only_when_absence_holds.py`, at least THREE tests, as your verdicts define.
- `performance/tests` reads `251 passed, 1 failed` at base (the failure is `test_the_fallback_calendar_is_graded_in_its_own_years_and_clipped_outside_them`, not yours; do not touch it). After: no new failure and at least 258 passed.

**Offline proof over the served gold, and the counts.** With the reader's NEW rule over the served gold at the cap day 2026-10-08 (both entries, windows SI, YTD, QTD, 1Y; reuse the cache step, window rule and reader call of `ib164_measure.py`), count the ACCOUNTS whose claim moves from `measured` to `inferred`. The CTO's v0.49 counts, which your run must reproduce, are:
`49F`: SI 23, YTD 19, QTD 2, 1Y 20; `orion`: SI 894, YTD 200, QTD 7, 1Y 240. Also hash, per (entry, window), the list of figures the reader returns before your change (at `base_commit`) and after, and show the lists equal: the figures do not move (`figures_compared` is the number of figures hashed). Cache partitions in `C:/dev/_scratch331/` (outside the worktree; bound every step with its own timeout; print the denominator of partitions read; never truncate silently); remove the scratch at the very end with a short bounded python script; if the cleanup hangs, stop cleaning and say so.
If a count differs from the CTO's, STOP on it: file a row naming the cell and both numbers, and report; do not edit a threshold.

**Consumers.** `consumers_of_claim_and_state`: every place in `infra/aws/lambda/investor-reporting/` (the service, `entry.py`, `normalize`, adapters, narrative, the contracts and the tests) that reads the claim, `days_linked`, the new integers or the PARTIAL state, each `{cite, reads}`, with one read through each (use the native Grep tool; print the denominator). The portal is NOT read here.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~331/IB166-1_reader_record.json`: `{base_commit, latest_landed_day: "2026-10-08", files_changed, new_member_names:{...}, claim_move_counts:{"49F":{"SI":..,"YTD":..,"QTD":..,"1Y":..},"orion":{...}},
absences:[{name, verdict, cite, in_words}], consumers_of_claim_and_state:[{cite, reads}], figures_unchanged:true, figures_compared:<int>, hash_pins:[every place in the repo that pins a hash of a file you changed, with what you did],
host_reach (which Lambda package carries each changed file: read lambda-source-map.json; nothing is built here), not_established:[...], functions_invoked:0, sign_ins_made:0, aws_writes_made:0, accounts_written:0, figures_written:0, vendor_requests_sent:0}`.

<criterion id="IB166-1-AC1" cell_refs="IB-pr-476"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-1-AC1</invocation><expect>IB166-1-AC1 PASS</expect></criterion>
<criterion id="IB166-1-AC2" cell_refs="IB-pr-476"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-1-AC2</invocation><expect>IB166-1-AC2 PASS</expect></criterion>
<criterion id="IB166-1-AC3" cell_refs="IB-pr-476"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-1-AC3</invocation><expect>IB166-1-AC3 PASS</expect></criterion>

<expected_criteria>IB166-1-AC1, IB166-1-AC2, IB166-1-AC3</expected_criteria>

What the checks grade: AC1 your claim test file exists and at least 4 tests pass; AC2 your PARTIAL test file exists and at least 3 tests pass; AC3 the record: the eight claim-move counts equal the CTO's, `latest_landed_day` reads 2026-10-08, at least one resolving consumer cite, at least 3 absences judged with resolving cites, `figures_unchanged` true over
at least one figure, the six bound counters 0, and nothing outside `performance/`, your deliverables, your rows and your order changed. Every count in your record is yours; the issuer re-reads the suite at the drain.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No change to the producer (`data/assets/scripts/gold/irpt_holdings_performance/`), to the schemas, to the adapters other than where a test needs a read, or to any other Lambda.
- **Refusal clause:** a status the rule cannot place, a count that differs, an S3 read refused: file a row and report. Never weaken a check or a test; do not edit `p166_cells.py`. The check script in your worktree is the one the order names; if it counts a file of the issuer's folder as yours, say so in a row.
- **Hash pins:** list every test, manifest or SHA256SUMS that pins the bytes of a file you change; regenerate one only if it is inside your `<paths>` and is a generated record of those bytes.
- **Row ids** are `IRPT_BCKEND-D2-W331-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~331" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~331@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~331 <0.9.0_WK_IRPT_BCKEND~331@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/lambda/investor-reporting/performance/holdings_gold.py
infra/aws/lambda/investor-reporting/performance/entry.py
infra/aws/lambda/investor-reporting/performance/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~331/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-476.reader-claim-by-excluded-status-and-partial-only-when-absence-holds.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 158 (round 166, workstream ~P), cell `IB-pr-476`.
<owned_cells>IB-pr-476</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB166-1-AC1, IB166-1-AC2, IB166-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~331/IRPT_BCKEND.TO-IB-pr-476.reader-claim-by-excluded-status-and-partial-only-when-absence-holds.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the rule as built in a sentence; each of the three absences' verdict and cite; the new member names; the four-plus arms; the eight claim-move counts against the CTO's; the figures hashed and that the lists are equal; the consumers found and the denominator; the performance suite's last line before and after;
the hash pins found and what you did; whether the scratch was cleaned; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell changes the reader and its tests in the repo; nothing is deployed, uploaded or invoked, and the served claim moves only when a later release lands the build under its own never-widen pair (CTO ROUND-166 ANALYSIS item 2).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; S3 list and get of the served gold, the reads earlier cells (IB-pr-467, IB-pr-470) already made.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; no route is called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p166_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~19:3xZ: IB166-1 AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. Measured by the issuer at base: pytest performance/tests reads 251 passed, 1 failed (the calendar-fallback test). The three absences' verdicts and the new member names are the worker's; the issuer expects but does not know whether any absence is conditional.
lane: the <paths> block IS the grant. Class WORLD by the L6 floor (an infra path); nothing is deployed.
</preflight>
