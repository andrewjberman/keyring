# TO-AR-g-52 -- C-SWAP step 2, the replacement rule: one pure module that picks the class-matched, Yahoo-priced security with the longest history, deterministically, and records what it did

<to_id>IRPT_ANLREQ.TO-AR-g-52</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~171</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-52` (`decompositions/IRPT_ANLREQ_DECOMP_R7_G.md`) |
**outcome_ref:** FWD-7 (C-SWAP) | **depends_on:** none.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~171`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-171` (branch `wk-IRPT_ANLREQ-171`), provisioned by the issuer. Work only there.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~171 <0.9.0_WK_IRPT_ANLREQ~171@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W171-S<k>` (take the next free `<k>`); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no model call, no install. Scratch outside the product tree.

### Read first (under `C:/dev/wk-irpt-anlreq-171/infra/aws/lambda/investor-reporting/ycharts/research/`)

- `held_data.py` (the module style: pure functions, readers passed in, no connection opened) and `tests/test_held_data.py` (the test style and fakes).

### THE CELL (`AR-g-52`, inlined)

When a security cannot be priced by any tier, Andrew wants a replacement found, not a hole in the report (CTO price ruling ADDENDUM 2 and 3,
PRD v0.14 C-SWAP). The rule, as the CTO ruled it on Andrew's word ("longest-history is fine as an additional qualification"): the
candidate pool is the securities of the SAME asset class and sub asset class in `etf-classifications`, plus the model's proposals
admitted ONLY if they pass that same class match; every candidate must be priced by Yahoo; the pick is the LONGEST Yahoo history, ties
broken by ticker in alphabetical order. The same input always gives the same pick: the model can widen the pool, it never decides the pick.
The report names the substitution. This cell builds that rule as one pure module. It reads no table and calls no model or vendor: the
pool, the proposals, the class lookup and the history length are passed in. The adapters are a later cell.

**Build a NEW file `infra/aws/lambda/investor-reporting/ycharts/research/swap_replacement.py`** with exactly this contract.

1. `METHOD = "CLASS_LONGEST_YAHOO_HISTORY"`.
2. `choose_replacement(missing, classification, pool_rows, model_proposals, history_days, classify=None)`:
   - `missing`: the ticker that could not be priced (stripped, upper-cased).
   - `classification`: `{"asset_class": str, "sub_asset_class": str}` of the missing security, or `None`. If it is not a dict, or either
     value is not a non-blank `str`, there is no class: the answer is `NO_REPLACEMENT` with `why` `"NO_CLASS"`.
   - `pool_rows`: an iterable of `{"ticker", "asset_class", "sub_asset_class"}` (the `etf-classifications` rows). Tickers are stripped and upper-cased.
   - `model_proposals`: an iterable of tickers the model proposed. Its own claims about class are not an input: a proposal is class-checked
     from `pool_rows` (the row for that ticker), else from `classify(ticker)` if given (a callable returning
     `{"asset_class", "sub_asset_class"}` or `None`), else it is dropped.
   - `history_days`: a callable `(ticker) -> int | None`, the length of the ticker's Yahoo history in days.
3. **Class match** compares `asset_class` AND `sub_asset_class`, each stripped and `casefold()`-ed, for equality. The missing ticker itself
   is never a candidate.
4. **The pool.** Candidates from `pool_rows` that match the class have origin `"CLASSIFICATIONS"`. A proposal (stripped, upper-cased;
   blanks and non-strings and the missing ticker skipped; duplicates once) is checked: no class found -> dropped `"NOT_CLASSIFIED"`; class
   differs -> dropped `"CLASS_MISMATCH"`; class matches -> a candidate with origin `"MODEL"`, or `"BOTH"` if it is already a
   `"CLASSIFICATIONS"` candidate (listed once).
5. **Priced by Yahoo.** For each candidate call `history_days(ticker)` once. An exception -> dropped `"HISTORY_ERROR"` (the message is NEVER
   put in the result); `None`, a `bool`, a non-`int`, or `<= 0` -> dropped `"NOT_PRICED_BY_YAHOO"`. The rest keep `history_days`.
6. **The pick** is the candidate with the greatest `history_days`; a tie goes to the alphabetically first ticker (plain string order). The
   result does not depend on the order of `pool_rows` or `model_proposals`.
7. **Result.** A `dict` with these keys, always:
   - `"status"`: `"REPLACED"` or `"NO_REPLACEMENT"`; `"proxy_for"`: the missing ticker; `"replacement"`: the pick or `None`;
     `"method"`: `METHOD`; `"candidates"`: the priced candidates as `{"ticker", "history_days", "origin"}`, sorted by history descending then ticker;
     `"dropped"`: `{"ticker", "reason"}` rows sorted by ticker then reason.
   - `"confidence"`: `"CLASS_MATCH_PRICED"` when the pick's origin is `CLASSIFICATIONS` or `BOTH`; `"CLASS_MATCH_PRICED_MODEL_PROPOSED"` when it
     is `MODEL`; `None` when there is no replacement.
   - `"named"`: one ASCII sentence for the report. Replaced: `"<MISSING> is replaced by <PICK> (same asset class and sub asset class; longest Yahoo history, <N> days)."`
     No replacement: `"<MISSING> has no replacement (<WHY>); the report is generated without it."`
   - On `NO_REPLACEMENT` also `"why"`: `"NO_CLASS"` (no class), `"NO_CANDIDATE"` (no candidate matched, before pricing) or `"NONE_PRICED"` (candidates
     existed and none was priced). On `REPLACED` there is no `why` key.
8. **The module is pure and stdlib-only:** it imports nothing but `re`, `collections`, `typing` (and `__future__`); it opens no file, makes no
   connection, reads no environment variable, and has no `print`.

**Tests.** A NEW file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_swap_replacement.py` with at least 8 tests, offline: the
longest history wins; a tie goes to the alphabetically first; the answer is the same for every permutation of the pool; unpriced candidates are
dropped with their typed reasons and an error message never appears in the result; the missing ticker and other classes are excluded; a model
proposal that passes the class match through `classify` widens the pool and can win; a proposal in the wrong class or unknown to the classifier is
dropped and never decides; no class, no candidate and none priced each give `NO_REPLACEMENT` with the right `why` and a `named` sentence that
says the report runs without the security; and the class match ignores case and blanks.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR52-g-AC1" cell_refs="AR-g-52"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g52_checks.py g52</invocation><expect>^AR-G52-OK</expect></criterion>

<criterion id="AR52-g-AC2" cell_refs="AR-g-52"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g52_checks.py hygiene</invocation><expect>^AR-G52-HYGIENE-OK</expect></criterion>

<expected_criteria>AR52-g-AC1,AR52-g-AC2</expected_criteria>

- AC1 imports `swap_replacement`, asks `choose_replacement` fourteen cases (the contract above, item by item, including every permutation of a pool), then runs your test file (0 failed, at least 8 passed). At base it FAILs (no module).
- AC2 reads the module's bytes: ASCII only, only the allowed imports, no `open`, `print`, `exec`, `eval`. At base it FAILs (no module).

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no model call, no installs. Nothing outside the two new files, your deliverable folder, this order's status flip and the channel file is edited.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/swap_replacement.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_swap_replacement.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~171/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-52.swap-replacement-rule-core.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R7_G.md</decomp_doc> round 7, workstream ~G, cell `AR-g-52`.
<owned_cells>AR-g-52</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR52-g-AC1, AR52-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~171/IRPT_ANLREQ.TO-AR-g-52.swap-replacement-rule-core.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-52`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR52-g-AC1,AR52-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the module's function names with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the module is NEW and imported by nothing; the later compose cell is the first importer. Nothing deployed, so no edge is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change; the pool, the proposals and the history are passed in.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read the cell against the CTO's replacement ruling (ADDENDUM 3) and the CRO's provider QA finding that the replacement must be deterministic. Traps: the model deciding the pick; a proposal admitted on the model's own stated class; a tie broken by input order; the missing security replacing itself; an unpriced candidate picked; an exception message with a credential in the result; a hole in the report with no sentence naming it. The checker feeds a green arm (a reference build passes all fourteen cases) and a mutant arm (the history sort reversed fails four cases). NOT seen (blind): the real classifications table and Yahoo, which the adapter cell reads.
</preflight>

- Cut on CTO msg 8377 (ENGINE lane, `2.0.0_SA_COO~G2`), PRD v0.14 C-SWAP and the CTO price ruling ADDENDUM 3. Risk WORLD: the class the infrastructure path in `<paths>` implies (the gate floor); new source and tests only, nothing deployed or called.
- Base: `AR52-g-AC1` and `AC2` FAIL as expected (no module). The checker's green arm and mutant arm were run by the issuer before the cut.
- Ships to the host only in the single resident release (a later cell of this workstream); `swap_replacement.py` must be added to the resident package's member list in that cell.
