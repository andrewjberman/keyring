# TO IRPT_DASHBD.TO-DB-b-303 -- ONE MEANING of history_scope across firms (CTO msg 9480): the Cottonwood adapter calls an account PARTIAL_HISTORY when it has a ROW on the source floor day, whatever the row's value, as the 49 Financial producer does; the contract sentence says so (round 149, 31 of 867 floor-day accounts split the two rules)

<to_id>IRPT_DASHBD.TO-DB-b-303</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~242</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>COTFIRSTROW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** COTFIRSTROW, round 149 | **Ordered by:** the CTO's ruling msg 9480 (history_scope has ONE meaning across firms; PARTIAL when the account's first row is on or before the source floor) on the issuer's offline count `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/RD_COT_REWRITE_OFFLINE_DIFF_20261016.json` | **Decomp cell:** `DB-b-303` (decomposition section 163).

**Risk class WORLD** is the floor of the paths below (`org/standards/` contracts and a gold adapter that a deploy pair later carries): code and contract text in a branch; no Terraform command, no AWS call, no push. The re-pin of the source-map entry and the deploy pair are separate cells.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-242` (branch `wk-IRPT_DASHBD-242`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~242/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report. **Before every commit, scan what you stage for a client figure and for long identifier runs; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends.**

**Why.** `derive_rows` in the Cottonwood adapter reads the floor day's `{account: value}` and calls an account PARTIAL_HISTORY only when its floor-day value is POSITIVE; an account with a zero, negative or unreadable row on the floor day reads FULL. The 49 Financial producer (`account_return_daily.py`, `_history_scope`) calls an account PARTIAL when its FIRST ROW is on or before the source floor, whatever the value. The CTO ruled one meaning (the conservative one: an account that existed at the floor may have history the source never held). On the 867 Cottonwood accounts that have a row on the floor day 2026-07-10, 31 (25 negative, 6 zero) are the split.

**The cell (`DB-b-303`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p171_cot_first_row.py` (your three criteria; `check_diff`, `check_behaviour` and `check_tests` are the exact spec); the adapter `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py` (`derive_rows`, `derive`, `day_values`, `accounts_in_partition`); the tests `data/assets/scripts/gold/irpt_reporting/tests/test_history_scope_derivation.py`, `test_cottonwood_rewrite.py`, `test_cottonwood_bd_account_return_daily.py`; the two contracts named below.
2. **The adapter (ONE file, only inside `derive_rows` and `derive`; every other byte of the file stays).** (a) `derive_rows(account_id, values, flows, unreconciled, days, floor_accounts=None)`: the parameter `floor_values` becomes `floor_accounts`, a set of account keys that have a row on the floor day. With `floor_accounts` None the rows are the legacy PARTIAL_HISTORY with no claim (unchanged). With a set (even an EMPTY set) each row carries the claim `inferred` and `history_scope` = PARTIAL_HISTORY when `account_id in floor_accounts`, else FULL. (b) `derive(...)`: with `floor_day` given AND listed, read that partition and build `floor_accounts` as the set of `_key(a)` of EVERY value of its `AccountID` column that is also in `accounts` (any row counts: a zero, negative or null value is still a row); pass it to `derive_rows`. Nothing named `floor_values` remains in the file (update the docstrings of the two functions with the new words). Write the file as bytes with LF line endings.
3. **The tests.** In `test_history_scope_derivation.py` replace the `floor_values` use with `floor_accounts` (the parametrised test becomes sets: `{ACCT}` reads PARTIAL_HISTORY, `{"OTHER"}` and `set()` read FULL) and ADD at least THREE tests whose names contain `first_row`: an account with a zero floor row is PARTIAL; an account with a negative or unreadable (null) floor row is PARTIAL; an account absent from the floor partition is FULL. No other test file may mention `floor_values` (the other two files must pass unchanged or with the rename only).
4. **The contracts (text only, three fields, ONE sentence each).** Append EXACTLY this sentence (a leading space, then the text) to the END of each of: in `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` the field `series.fields.history_scope.sentence`; in `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` the fields `conditional_columns[1].rule` and `rule24_record.v046`: ` A 'value day' is a day on which the source holds a row for the account, whatever the row's value: a zero, negative or unreadable balance row counts, so an account with a row on the source floor is PARTIAL_HISTORY.` Change NO other byte of either file: no version, hash, supersedes entry or other field (the checker compares the parsed documents and the line count). Keep each file's line endings and formatting (edit the text of the existing lines in place; do not re-serialise the file).
5. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p171_cot_first_row.py" . DB171-1-AC1`, then AC2, then AC3.
6. **Record** `RD_COT_FIRST_ROW_FACTS_R149.json` in your folder with EXACTLY these fields: `adapter_changed_functions` (["derive_rows", "derive"]); `parameter_old` ("floor_values"); `parameter_new` ("floor_accounts"); `contract_fields_changed` (the three field paths as written above); `new_first_row_tests` (the names of the new tests); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: no landed day was rewritten, nothing was deployed, the 31 accounts are the issuer's offline count and the rewrite waits for a re-pinned, re-signed packet).

<criterion id="DB171-1-AC1" cell_refs="DB-b-303"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p171_cot_first_row.py" . DB171-1-AC1</invocation><expect>DB171-1-AC1 PASS</expect></criterion>
`DB171-1-AC1` -- the adapter differs from the base only inside `derive_rows` and `derive`, with `floor_values` gone; the three contract fields gain exactly the one sentence and nothing else of either contract moves (same line count, one changed line per field). Base: FAIL.
<criterion id="DB171-1-AC2" cell_refs="DB-b-303"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p171_cot_first_row.py" . DB171-1-AC2</invocation><expect>DB171-1-AC2 PASS</expect></criterion>
`DB171-1-AC2` -- behaviour: with `floor_accounts` an account in the set reads PARTIAL_HISTORY with the claim whatever its floor-day value, an account outside the set (even an empty set) reads FULL with the claim, None keeps the legacy rows without a claim; `derive` over a fake reader reads zero, negative and unreadable floor rows as PARTIAL and an account absent from the floor partition as FULL; no floor day, or one absent from the listing, writes no claim. Base: FAIL.
<criterion id="DB171-1-AC3" cell_refs="DB-b-303"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p171_cot_first_row.py" . DB171-1-AC3</invocation><expect>DB171-1-AC3 PASS</expect></criterion>
`DB171-1-AC3` -- `floor_values` is gone from the adapter and its three test files, the history-scope test file holds at least three new `first_row` tests, and the three Cottonwood test files pass under pytest. Base: FAIL.

<expected_criteria>DB171-1-AC1,DB171-1-AC2,DB171-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no Terraform command, no push. Writes: the one adapter, the one test file, the two contract files and your private folder.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W242-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them, and READ the whole gate output: a refused commit leaves your edit uncommitted and blocks every other seat's merge. ASCII only in anything you write.

<paths>
data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_history_scope_derivation.py
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_rewrite.py
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_bd_account_return_daily.py
org/standards/IRPT_DASHBD_SERIES_CONTRACT.json
org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~242/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-303.cottonwood-history-scope-first-row.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 163 (round 149, workstream COTFIRSTROW), cell `DB-b-303`.
<owned_cells>DB-b-303</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB171-1-AC1, DB171-1-AC2, DB171-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~242/IRPT_DASHBD.TO-DB-b-303.cottonwood-history-scope-first-row.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB171-1-AC1,DB171-1-AC2,DB171-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the signature change in one line; the three contract fields; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: code and contract text in a branch; no plan, no apply, nothing deployed; the later deploy pair carries its own blast radius.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and were run by the issuer on a reference tree (green) and on four single-fault mutants of the adapter and one diff mutant (all red).
lane: the <paths> block IS the grant.
</preflight>
