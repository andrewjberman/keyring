# TO-AR-g-68 -- the upload door: a kept TICKER_NOT_FOUND symbol (the exact equal pair) files as an UNRESOLVED row for C-SWAP; the vendor path refuses such a row; the research read carries or refuses it

<to_id>IRPT_ANLREQ.TO-AR-g-68</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~178</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-68` (`decompositions/IRPT_ANLREQ_DECOMP_R10_G.md`) |
**outcome_ref:** FWD-7 (C-SWAP) and FWD-1 | **depends_on:** `AR-g-55` (merged `e9c9bdf1f0`, the read this cell implements).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~178`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-178` (branch `wk-IRPT_ANLREQ-178`), provisioned by the issuer. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~178 <0.9.0_WK_IRPT_ANLREQ~178@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W178-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you edit or add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.

### Read first (under `C:/dev/wk-irpt-anlreq-178/`)

- The read this cell implements: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~174/r8/DOOR_UNRESOLVED_READ.json` (q2, q3, q4 and the recommendation).
- Under `infra/aws/lambda/investor-reporting/`: `intake/portfolio.py` lines 336-348 (`verify_frozen_portfolio`), 376-406 (`_kept_by_history`, `template_corrections`), 440-450 (corrections applied in the freeze), 486-575 (the row loop: the `NOT_FOUND` branch at about line 500, the `KEPT` row built at 562-574) and 576-600;
  `ycharts/generate/normalized_input.py` lines 40-70 (`prepare_normalized_upload`, template branch); `ycharts/research/runner.py` lines 422-476 (`HoldingsUnreadable`, `read_holdings`).
- Tests to copy the fixtures from: `intake/tests/test_kept_holding.py` (a frozen template with a KEPT check), `ycharts/generate/tests/test_y5_proxy_corrections.py` (the correction tests and the case-only pin), `ycharts/generate/tests/test_normalized_input.py`, `ycharts/research/tests/test_runner.py`.

### THE CELL (`AR-g-68`, inlined)

Andrew, 2026-10-15: "swaps are not up to the filer." The filing form offers the door's own suggestion for an unknown ticker and the filer may KEEP the ticker as typed (Keep re-posts the same file with a
correction whose `from_value` and `to_value` are the same symbol). Today the door refuses that pair and an unknown ticker stops the upload at `NEEDS_CORRECTION`. The CTO ruled (PRD v0.15) that a kept
`TICKER_NOT_FOUND` holding files as `UNRESOLVED` so the backend replacement rule (C-SWAP) can deal with it later. This cell changes the door, closes one defect the read found on the vendor path, and
lets the research read carry the marker. Three files change; nothing is deployed.

**A. `intake/portfolio.py`, `template_corrections`.** Accept a correction whose `from_value` EQUALS its `to_value` EXACTLY (the same characters, not just the same letters ignoring case) ONLY when its
`finding_code` is `"TICKER_NOT_FOUND"`. Every other equal pair stays refused `PortfolioRefused("CORRECTIONS_INVALID")`: an equal pair on any other code, and a pair equal only ignoring case (`TIMXX` and `timxx`, pinned by
`test_y5_proxy_corrections.py`). All other rules stay: three keys exactly, symbol pattern, at most 20, no repeated `from_value`. The returned items keep exactly three keys (the stored list is replayed through this same
function by `verify_frozen_portfolio`, so what it returns must be accepted by it again).

**B. `intake/portfolio.py`, `freeze_template_portfolio`.** Let `kept` be the set of `from_value`s of the accepted equal pairs. In the row loop, when a row's symbol is in `kept` AND its check is the `NOT_FOUND` case
(the branch that today emits `TICKER_NOT_FOUND` and `continue`s), do NOT emit and do NOT skip: build the row as a KEPT row is built, with these differences. The row's `security_id` is the typed symbol; `analysis_dollars` is
computed exactly as for every other row (so a SHARES-basis upload still refuses `SHARES_PRICE_UNAVAILABLE`, and weight bases still need their notional); `price` is `None`; `provider_receipt_sha256` is `None`;
`method` is `"KEPT_AS_TYPED"`; `resolution` is `"UNRESOLVED"`; `price_source` is `None`. Emit NO new finding code. The row is appended to `rows` (so the row count still equals the template's) but is NOT added to
`totals`, so the document's `holdings` block (the vendor identity block) does not contain it. An equal pair that names a symbol whose check is FOUND or KEPT changes nothing for that row; one that names a
symbol absent from the file still yields `CORRECTION_UNMATCHED`. A frozen document with UNRESOLVED rows must pass `verify_frozen_portfolio` (the replay rebuilds it from the stored options).

**C. `ycharts/generate/normalized_input.py`, `prepare_normalized_upload` (template branch).** If any row of the document's `rows` carries `resolution == "UNRESOLVED"`, raise `RecipeRefused` BEFORE anything is
built for the vendor (the vendor path prices only provider-receipted holdings, and `holdings["rows"]` no longer lists the unresolved row, so without this refusal the upload would silently go without it). The message names
no ticker and no amount. Also replace the bare `["provider_receipt"]["sha256"]` subscript in the identity bindings by a guard that raises `RecipeRefused` (a row with no receipt must never raise a `TypeError`; this
closes row `IRPT_ANLREQ-D2-W174-S3`).

**D. `ycharts/research/runner.py`, `read_holdings`.** Add the keyword parameter `allow_unresolved=False` at the END of the signature (existing callers unchanged). A document row with `resolution == "UNRESOLVED"`:
with the default it raises `HoldingsUnreadable("UNRESOLVED_ROW")` before the rows list is built; with `allow_unresolved=True` it is returned as `{"ticker": ..., "amount": ..., "resolution": "UNRESOLVED"}`.
Rows without the marker are returned exactly as today (no new key).

**E. Tests.** Three NEW test files, with EXACTLY these test function names (the checker looks for each name), each test offline:

- `infra/aws/lambda/investor-reporting/intake/tests/test_unresolved_keep.py`:
  `test_keep_pair_files_the_row_as_unresolved`, `test_unresolved_row_has_no_receipt_and_stays_out_of_the_vendor_holdings`, `test_keep_pair_on_a_found_symbol_files_nothing_extra`,
  `test_frozen_unresolved_document_replays_and_verifies`, `test_shares_basis_still_refuses_an_unresolved_row`.
- `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_normalized_input_unresolved.py`: `test_vendor_path_refuses_an_unresolved_row_with_recipe_refused`.
- `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_runner_unresolved.py`: `test_read_holdings_refuses_unresolved_by_default`, `test_read_holdings_with_allow_unresolved_returns_the_marker`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR68-g-AC1" cell_refs="AR-g-68"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g68_checks.py g68</invocation><expect>^AR-G68-OK</expect></criterion>

<criterion id="AR68-g-AC2" cell_refs="AR-g-68"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g68_checks.py regress</invocation><expect>^AR-G68-REGRESS-OK</expect></criterion>

<expected_criteria>AR68-g-AC1,AR68-g-AC2</expected_criteria>

- AC1 asks `template_corrections` six direct cases (the exact equal pair accepted for `TICKER_NOT_FOUND`; refused for another code; the case-only pair still refused; an ordinary pair unchanged; the accepted output replays; a repeated `from_value` refused),
  then checks the eight named tests exist in your three new files and runs them (0 failed, all eight passed). At base it FAILs.
- AC2 runs the four existing test files (`test_kept_holding.py`, `test_y5_proxy_corrections.py`, `test_normalized_input.py`, `test_runner.py`; 108 tests today) and requires 0 failed and at least 108 passed. At base it PASSes (it guards that nothing existing breaks).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. Do not edit `intake/uploads.py`, `ops/status.py`, `opal_producer.py`, the portal or any other file.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/intake/portfolio.py
infra/aws/lambda/investor-reporting/ycharts/generate/normalized_input.py
infra/aws/lambda/investor-reporting/ycharts/research/runner.py
infra/aws/lambda/investor-reporting/intake/tests/test_unresolved_keep.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_normalized_input_unresolved.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_runner_unresolved.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~178/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-68.door-keep-as-typed-files-unresolved.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R10_G.md</decomp_doc> round 10, workstream ~G, cell `AR-g-68`.
<owned_cells>AR-g-68</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR68-g-AC1, AR68-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~178/IRPT_ANLREQ.TO-AR-g-68.door-keep-as-typed-files-unresolved.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-68`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR68-g-AC1,AR68-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- for A to D, the function and lines changed;
- the one thing in the retained row you were unsure of, if any;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `portfolio.py` is read by the upload door, `verify_frozen_portfolio` (every replay of a stored template document), `composition_admission` and the research read; the change adds an accepted pair and a new row kind, both reachable only through the new equal pair, so every stored document and every existing upload replays unchanged. NOT seen: the deployed `irpt-ycharts-generate` and `irpt-status` packages, which this cell does not touch; it ships only in the next release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change, no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or wire change (the equal pair uses the existing correction item). comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read against the AR-g-55 record's risk note. Traps: an unpriced row reaching a report as if priced (D refuses by default); the vendor path uploading without the unresolved holding (C refuses); an equal pair on a FOUND symbol creating a second unpriced row beside a priced one (B changes nothing for it); the case-only pair becoming acceptable (A keeps the pin); a replay that no longer reproduces the stored document (B and the stored three-key list); a new finding code needing a words table (none added). The checker feeds a green arm (a patched copy of the tree passes the six direct cases and the eight named tests) and a base arm (the unpatched tree fails both).
</preflight>

- Cut on the AR-g-55 record and PRD v0.15 item 3 (CTO msg 8417). Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR68-g-AC1` FAILs as expected; `AR68-g-AC2` PASSes as expected (108 tests).
- Disarms row `IRPT_ANLREQ-D2-W174-S3` (a receipt-less row raises a TypeError on the vendor path) when merged. `2.0.0_SA_COO~Y2` posts the Keep only after this merges.
