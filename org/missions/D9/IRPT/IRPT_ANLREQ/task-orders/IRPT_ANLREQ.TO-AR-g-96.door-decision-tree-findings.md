# TO-AR-g-96 -- the upload door's findings follow the unmatched-ticker decision tree: Replace and No beside the typo prompt, a ticker that exists but cannot be priced files UNRESOLVED with the staff words, NAME_PROXY retired

<to_id>IRPT_ANLREQ.TO-AR-g-96</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~198</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>22</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-96` (`decompositions/IRPT_ANLREQ_DECOMP_R22_G.md`) |
**outcome_ref:** FWD-2 (C-FILING-HINT, C-SWAP step 2; PRD v0.17, v0.18, v0.19) | **depends_on:** `AR-g-68` (the keep pair, merged `4c82e94402`) and `AR-g-95` (merged `26d720a980`). Order: CTO msgs 8687 and 8704 (PRD v0.19 @ the CTO's commit, Andrew-direct ~21:5xZ: "If yes, we accept the swap, if replace we try it with the replaced ticker(s) and rerun the process for those, if no, then we say that Opal Staff will manage the replacement").

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~198`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-198` (branch `wk-IRPT_ANLREQ-198`), provisioned by the issuer with the whole of `infra/`, `docs/`, `data/` and `org/missions/D9/IRPT` on disk. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~198 <0.9.0_WK_IRPT_ANLREQ~198@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W198-S<k>` (take the next free `<k>`; check the channel file for `W198` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

### Read first (under `C:/dev/wk-irpt-anlreq-198/infra/aws/lambda/investor-reporting/`)

- `intake/portfolio.py`: `CORRECTABLE_FINDINGS` (line 364), `template_corrections` (389) and the finding chain in `freeze_template_portfolio` (lines 509-538: `NOT_FOUND`, `YFINANCE_CHECK_FAILED`, `YFINANCE_NOT_CHECKED`, `PROVIDER_ENTITLEMENT_UNVERIFIED`, the rest) and the UNRESOLVED row built near line 582.
- `intake/uploads.py`: `CORRECTION_WORDS` (line 58), `PROXY_CODES` (154), `SYMBOL_WORDS_CODES` (164), `_words_for` and `_with_correction_words`; `ops/status.py`: its own `CORRECTION_WORDS` (line 86), which `intake/tests/test_correction_words.py` locks equal to the uploads copy.
- `intake/upload_suggestions.py` (it puts `ACCEPT_SUGGESTION` FIRST on a TICKER_NOT_FOUND finding and keeps the other actions; NOT edited).
- `intake/tests/test_kept_holding.py` (its helpers `freeze`, `resolve`, `codes`, `finding`, `FakeChecker` are what your new tests import).

### THE CELL (`AR-g-96`, inlined)

PRD v0.19 (C-FILING-HINT): the filer's choices for a holding the door cannot match form a tree. A ticker that does NOT exist (`TICKER_NOT_FOUND`) is a possible typo: the form shows "Did you mean X?" with **Yes** (accept the suggestion), **Replace** (type the right ticker(s), re-post, the door checks them again) and **No** (file it UNRESOLVED: "Opal Staff will manage the replacement."). A ticker that EXISTS but cannot be priced (`TICKER_DATA_NOT_ENTITLED`) is not a typo and the filer chooses nothing: it files UNRESOLVED with those words. The filer is never asked to name a proxy: `NAME_PROXY` is retired from every finding the door emits. The backend's C-SWAP replaces every UNRESOLVED holding later (not this cell).

**`intake/portfolio.py`, exactly this:**
1. `CORRECTABLE_FINDINGS`: remove `"TICKER_DATA_NOT_ENTITLED"` (a correction naming a stand-in for a not-covered ticker is refused as `CORRECTIONS_INVALID`, including an equal pair). The other five codes stay. `template_corrections` is otherwise unchanged (the equal pair on `TICKER_NOT_FOUND` stays the No branch; a pair that differs stays the Replace branch).
2. The `state == "NOT_FOUND"` finding (the one that is not a kept pair): `actions=["REPLACE_FILE", "REPLACE_TICKER", "FILE_UNRESOLVED"]`, value as before. A two-line comment cites the v0.19 tree (Yes is added by the suggestion gate, which prepends `ACCEPT_SUGGESTION`, unchanged).
3. `TICKER_CHECK_FAILED`: `actions=["REPLACE_FILE"]` and its description becomes `"%s could not be checked just now (%s); upload again in a few minutes."` (same two arguments). `TICKER_NOT_CHECKED`: `actions=["REPLACE_FILE"]` and its description ends `"upload again."` instead of `"name a proxy."` (the rest of the sentence unchanged).
4. The `reason == "PROVIDER_ENTITLEMENT_UNVERIFIED"` branch becomes: `emit("TICKER_DATA_NOT_ENTITLED", coordinate, "A", actions=["REVIEW"], value=named, severity="NOTICE", description="Row %s: %s is not covered by our price data. Opal Staff will manage the replacement." % (coordinate, named))` and then `unresolved = True` (so the row is built below exactly as a kept `TICKER_NOT_FOUND` row is: parsed, priced as every other row's amount, UNRESOLVED, outside `totals` and the holdings block, counted in the rounding residual). The old comment lines there are replaced by two lines citing PRD v0.17 and v0.19.
5. In the UNRESOLVED row dict, `"method"` becomes `"KEPT_AS_TYPED" if state == "NOT_FOUND" else "NOT_COVERED"` (a kept typed symbol keeps its method; a not-covered one reads `NOT_COVERED`). Nothing else in the row changes.
6. Nothing else in `portfolio.py` changes: `AMBIGUOUS` and `CHECK_UNAVAILABLE` keep their findings; the KEPT_BY_HISTORY path is untouched.

**`intake/uploads.py` and `ops/status.py`, the SAME edits in both word tables (the lock test compares them), exactly these sentences:**
- `TICKER_DATA_NOT_ENTITLED`: `"This holding is not covered by our price data. Opal Staff will manage the replacement."`
- `TICKER_NOT_FOUND`: `"Our data provider does not recognize this ticker, so it may be a typo. Accept the suggestion, type the correct ticker, or leave it for Opal Staff, who will manage the replacement."`
- `TICKER_NOT_CHECKED`: `"This ticker was not checked in this upload, because only a limited number of unknown tickers are checked at once. Submit the request again."`
- `CORRECTION_UNMATCHED`: `"A ticker you replaced is not in this file any more, so that choice was not used. Check the tickers in the file, and replace it again if it is still needed."`
- `TICKER_AMBIGUOUS`: `"This ticker could mean more than one security at our data provider. Replace it with a ticker that names one security, and submit the request again."`
- `TICKER_CHECK_FAILED`: `"We could not check this ticker with our price history service just now. Submit the request again in a few minutes."`
- In `uploads.py` only: delete the `PROXY_CODES` constant and its comment; add `"TICKER_DATA_NOT_ENTITLED"` to `SYMBOL_WORDS_CODES` (the finding's own description, with the row and symbol in it, is the sentence the filer reads; the table word is the fallback). The long comment above `CORRECTION_WORDS` and the rest of both tables stay.
The words may be wrapped across source lines as the file's style does; the strings must equal the above.

**Ten existing tests fail on the product edits above. Eight are edited as follows, and two more pass again once the constant in `test_y5_proxy_corrections.py` changes (`test_a_replacement_the_provider_does_not_know_names_that_row_again` and `test_no_corrections_keeps_every_existing_revision_hash_and_the_csv_lane_refuses_them`). A test's intent is kept; none is deleted; nothing else in those files changes:**
- `intake/tests/test_kept_holding.py`: `test_not_kept_is_ticker_not_found_exactly_as_today` expects `["REPLACE_FILE", "REPLACE_TICKER", "FILE_UNRESOLVED"]`; `test_check_failed_reads_its_reason_in_words_and_keeps_the_proxy_prompt` is renamed `test_check_failed_reads_its_reason_in_words_and_asks_for_a_retry` and expects the new description and `["REPLACE_FILE"]`; `test_twelve_holdings_ten_kept_and_two_read_not_checked_in_words` expects the two descriptions to end `upload again.`.
- `intake/tests/test_correction_words.py`: `test_an_unknown_ticker_reads_plain_words_and_keeps_its_proxy_action` is renamed `test_an_unknown_ticker_reads_plain_words_and_offers_replace_and_no`, expects the three actions, and `"proxy" not in item["description"].lower()`.
- `ycharts/generate/tests/test_y5_proxy_corrections.py`: the constant `SGOV_FOR_TIMXX` uses `"finding_code": "TICKER_NOT_FOUND"`; `test_a_gated_fund_row_is_named_with_plain_words_and_name_proxy` is renamed `test_a_gated_fund_row_files_unresolved_with_the_staff_words` and expects state `NORMALIZED`, exactly one finding in `answer["portfolio"]["findings"]` (code `TICKER_DATA_NOT_ENTITLED`, row 3, column `A`, actions `["REVIEW"]`, severity `NOTICE`, value `TIMXX`, description `"Row 3: TIMXX is not covered by our price data. Opal Staff will manage the replacement."`, no "proxy" in it) and the holdings rows `["AAPL"]`; in `test_a_named_proxy_opens_the_next_revision_and_normalizes_with_the_correction_disclosed` the first `resolve(...)` reads only AAPL (TIMXX absent, so it is NOT_FOUND). Its module docstring's first sentence is adjusted to say a not-found ticker is named with plain words and the three actions.
- `ycharts/generate/tests/test_y4_check_gate.py`: `test_without_an_advisory_the_resolve_is_exactly_as_before` expects `["REPLACE_FILE", "REPLACE_TICKER", "FILE_UNRESOLVED"]` at its line 241 (the synthetic findings elsewhere in that file keep `NAME_PROXY`: they are fixtures, not door output; leave them).
- `ycharts/generate/tests/test_resolve_upload.py`: `test_s284_an_entitlement_gated_fund_row_is_counted_gated_and_its_feature_named` expects `answer["state"] == "NORMALIZED"` and `[(f["code"], f["row"], f["actions"]) for f in answer["portfolio"]["findings"]] == [("TICKER_DATA_NOT_ENTITLED", 3, ["REVIEW"])]`, with the comment citing PRD v0.17 and v0.19.
If after your product edits a DIFFERENT existing test fails, change only what its failing assertion shows, name it in your report, and file a row.

**Tests.** A NEW file `intake/tests/test_decision_tree_findings.py`, offline, with these exact test function names (the checker looks for each by name); import the helpers `FakeChecker`, `codes`, `finding`, `freeze`, `resolve` from `test_kept_holding` (add `intake/`, `intake/tests/` and `ops/` to `sys.path` from `__file__`):
`test_not_found_offers_replace_and_no_and_never_names_a_proxy`, `test_a_ticker_that_exists_but_cannot_be_priced_files_unresolved_with_the_staff_words` (a hand-made check `{"symbol": "TIMXX", "state": "UNAVAILABLE", "reason": "PROVIDER_ENTITLEMENT_UNVERIFIED", "provider_receipt": None}`; the row is UNRESOLVED with method `NOT_COVERED`, price `None`, outside the holdings), `test_a_proxy_naming_correction_for_a_not_covered_ticker_is_refused_but_replace_and_no_are_accepted`, `test_no_files_unresolved_and_replace_is_checked_again_naming_the_files_own_row`, `test_a_retry_class_asks_for_a_retry_and_the_suggestion_gate_still_adds_yes_first` (`upload_suggestions.suggest_for` with a fake advisory and verify), `test_no_word_in_either_table_and_no_finding_the_door_emits_says_proxy_or_stand_in` (both tables equal; no "proxy", "stand in" or "stand-in" in any word).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR96-g-AC1" cell_refs="AR-g-96"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g96_checks.py g96</invocation><expect>^AR-G96-OK</expect></criterion>

<criterion id="AR96-g-AC2" cell_refs="AR-g-96"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g96_checks.py regress</invocation><expect>^AR-G96-REGRESS-OK</expect></criterion>

<expected_criteria>AR96-g-AC1,AR96-g-AC2</expected_criteria>

- AC1 asks the freeze, the corrections, the word tables and the suggestion gate 23 things on fakes (the tree on a missing ticker, no proxy action anywhere, a not-covered ticker filed NORMALIZED with one NOTICE of the exact words, its row UNRESOLVED / NOT_COVERED / unpriced and outside the totals, the weight-file residual counting its dollars, a bad amount still an error, no proxy correction for a not-covered ticker, Replace and No accepted, a failing Replace naming the file's row with the tree, the retry classes' words, the two tables equal and free of proxy talk, the door's words passing through, Yes first, determinism), then checks your six named tests exist and pass. At base it FAILs.
- AC2 runs fifteen test files one at a time (225 tests: the upload service and its refusal class and on-behalf tests, the owner lookup, the unresolved-keep, the template reader, the kept-holding, correction-words, price-date tests, the proxy corrections, the check gate, the resolve upload, the normalized-input unresolved and the prospect dates) and needs all of them to pass: the guard that your test edits are exactly those. At base it PASSes. Run it under `timeout 590`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/intake/portfolio.py
infra/aws/lambda/investor-reporting/intake/uploads.py
infra/aws/lambda/investor-reporting/ops/status.py
infra/aws/lambda/investor-reporting/intake/tests/test_decision_tree_findings.py
infra/aws/lambda/investor-reporting/intake/tests/test_kept_holding.py
infra/aws/lambda/investor-reporting/intake/tests/test_correction_words.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_y5_proxy_corrections.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_y4_check_gate.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resolve_upload.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~198/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-96.door-decision-tree-findings.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22_G.md</decomp_doc> round 22, workstream ~G, cell `AR-g-96`.
<owned_cells>AR-g-96</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR96-g-AC1, AR96-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~198/IRPT_ANLREQ.TO-AR-g-96.door-decision-tree-findings.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-96`.
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder (use `kind` `test` for a test file): commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR96-g-AC1,AR96-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed with line numbers;
- the names of any existing test you changed beyond the ten listed;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the findings and words are made by `freeze_template_portfolio` (called by the resident's resolve and the generate Lambda's normalization) and shaped by `uploads._with_correction_words`; `intake/portfolio.py` and `intake/uploads.py` are members of the `irpt-ycharts-generate` package and of the resident package (r32 carries both at the earlier bytes); `ops/status.py` is a member of the `irpt-status` package, whose envelope words are the same table. NOTHING is deployed by this cell: the words and actions reach the filer when r33 ships the Lambda leg (and the irpt-status words with it, which the r33 pair must name). A frozen document whose NOT_COVERED row has `method` NOT_COVERED has the same `resolution` UNRESOLVED as a kept one; the downstream readers (`runner.read_holdings`, `normalized_input`) test `resolution`, not `method` (read at HEAD). A re-post of an upload whose first normalization asked for a proxy computes a new revision (the findings differ); stated, not mitigated.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against PRD v0.17, v0.18, v0.19 and the ten tests. Traps: a NAME_PROXY left on one finding (the checker dumps every finding to JSON); a word table edited in one file only (the lock test and D8); a not-covered row counted into the holdings totals or priced; the residual losing the unresolved dollars; a proxy correction for a not-covered ticker still accepted; the notice's description replaced by the table sentence (the row and symbol lost); `ACCEPT_SUGGESTION` no longer first. The checker feeds a green arm (a reference build passes the 23 cases, the six named tests and the 225 regress tests) and nine mutant arms (a gated row left an error: the cases cannot run; NAME_PROXY kept on not-found: 5 cases; a proxy correction accepted: 2; one table still naming a proxy: 3; the wrong method: 1; the row prefix lost: 1; the table word in place of the notice: 1; check-failed keeping NAME_PROXY: 1; the tables differing: 1). NOT claimed: that the suggestion is computed for the REPLACEMENT typed in the Replace branch (the gate asks about the file's own symbol); that a SHARES file with a not-covered ticker files (its price lookup still refuses it as SHARES_PRICE_UNAVAILABLE, as a kept one does today).
</preflight>

- Cut on CTO msgs 8687 and 8704 and the issuer's reference build in a scratch tree (the ten tests fail on it and are edited as listed; the reference passes AC1 and AC2). Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR96-g-AC1` FAILs and `AR96-g-AC2` PASSes (225), as expected.
- The action names `ACCEPT_SUGGESTION` (Yes), `REPLACE_TICKER` (Replace: re-post with a correction `{finding_code: TICKER_NOT_FOUND, from_value: <the file's symbol>, to_value: <the typed one>}`) and `FILE_UNRESOLVED` (No: re-post with the equal pair `{TICKER_NOT_FOUND, X, X}`) are the issuer's choice inside this decomposition; `~Y2`'s form is told them by message. A NORMALIZED answer carries its NOTICE findings in `answer["portfolio"]["findings"]` (not in a top-level `findings`).
- The swap pass itself (the backend replacement) is `AR-g-98` and later, in the same round; the Lambda and irpt-status ship under r33's pair.
