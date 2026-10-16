# TO-AR-g-133 -- the upload door asks yfinance FIRST, YCharts second (PRD v0.22 item 1): SecurityResolver.check sends every uncached symbol to the checker in one batch and only the symbols it does not keep to the provider

<to_id>IRPT_ANLREQ.TO-AR-g-133</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~265</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>44</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-133` (`decompositions/IRPT_ANLREQ_DECOMP_R44_G.md`) |
**outcome_ref:** FWD-1 run 3, FWD-7 | **depends_on:** none (the checker `intake/yfinance_check.py` is merged at `5e7fe11fc8`). Order: CTO msg 9522 and PRD v0.22 item 1 (Andrew-direct: yfinance first, YCharts second).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~265`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-265` (branch `wk-IRPT_ANLREQ-265`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~265 <0.9.0_WK_IRPT_ANLREQ~265@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W265-S<k>` (take the next free `<k>`; check the channel file for `W265` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only in the product file. Do not touch anything outside the `<paths>` block.

### THE CELL (`AR-g-133`, inlined)

File: `infra/aws/lambda/investor-reporting/intake/security_resolution.py` (stdlib only). Today `SecurityResolver.check(symbols)` reads the cache, sends the uncached symbols (`pending`) to the provider port (`provider_check`, YCharts), classifies the receipt, and THEN, for every symbol still NOT_FOUND, asks the checker (`self.checker`, yfinance) once in `_check_unknown`. Andrew's rule is yfinance first, YCharts second. Change `check` so that, when `self.checker` is present:

1. After the cache loop, build `to_check` = the symbols in `unique` (their order) that are in `pending` OR whose cached result is a provider NOT_FOUND (today's "cached NOT_FOUND is not the last word" case). Ask the checker ONCE: `self.checker.check(list(to_check))`. If it raises, every symbol in `to_check` reads CHECK_FAILED with reason `EXCEPTION`. Read each entry with the existing `_checker_verdict(entry)` -> (state, reason).
2. A symbol whose verdict is KEPT is final: it gets exactly the KEPT row `_check_unknown` builds today (`dict(base, state="KEPT", reason="YFINANCE_HISTORY", candidates=[], provider_receipt=None, resolution_action="NONE", price_source="yfinance", checker={"rows": ..., "last_close": float(...)})`, where `base` for a fresh symbol is `{"symbol": s, "state": "UNAVAILABLE", "reason": "PROVIDER_READ_UNAVAILABLE", "candidates": [], "provider_receipt": None, "reference": copy.deepcopy(REFERENCE_NOT_CONSULTED), "cache_hit": False}`), is written to the cache with `KEPT_TTL` as today, and is REMOVED from `pending`: the provider is never asked about it.
3. The remaining `pending` symbols go to `provider_check` in ONE call, exactly as today (receipt, `classify_batch`, `_reference`, registry, cache put). If nothing is left pending the provider is not called and `provider_requested_count` is 0. A provider FOUND beats a NOT_KEPT.
4. After the provider step, a symbol that is still NOT_FOUND and whose first-pass verdict was NOT_KEPT stays NOT_FOUND, and the checker is NOT asked again. A symbol still NOT_FOUND whose verdict was CHECK_FAILED or NOT_CHECKED becomes what `_check_unknown` makes it today: `UNAVAILABLE` with `reason="YFINANCE_CHECK_FAILED"` and `check_failed=<reason>` (CHECK_FAILED), or `reason="YFINANCE_NOT_CHECKED"` and `not_checked="UPLOAD_LIMIT"` (NOT_CHECKED), both with `resolution_action="CHECK_THEN_SWAP"`. `_check_unknown` is replaced by this logic (keep its docstring's meaning in the new helper's docstring).
5. A cached KEPT answer (the existing cache branch) and a cached FOUND are still served with no call at all. With NO checker the resolver answers exactly as before (one provider call with every pending symbol, no checker step).
6. `verified_suggestions` displays a candidate whose check state is `FOUND` or `KEPT` (it filters on `FOUND` only today, which would hide a suggestion Yahoo keeps).

Design hint (use it or write your own; the checks only read behaviour): add `_judge(self, symbols)` -> `{symbol: (state, reason, entry)}`, `_keep(self, results, symbol, entry, now)` and `_apply_failure(self, results, symbol, verdict)` next to `_check_unknown`'s old place; keep `last_unverified` and `last_funds` set as today.

Tests: existing tests that encode the old order (provider first, checker second) are REWRITTEN to the new order, never deleted without a replacement and never weakened. The files you may edit are `intake/tests/test_security_resolution.py`, `intake/tests/test_kept_holding.py`, `intake/tests/test_registry_known.py`; add `intake/tests/test_door_yfinance_first.py` with one test per numbered behaviour above (a failing and a passing arm for 2, 3 and 4). Read the issuer's check `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g133_checks.py` for the exact fakes and the exact expectations; do not edit it.

1. Run the three criteria. Commit the code and tests, then the proof and the status flip, as separate commits (code first).
2. **Report** the commit hashes, the three criterion outputs and the list of existing tests you rewrote (file and test name).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR133-g-AC1" cell_refs="AR-g-133"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g133_checks.py build</invocation><expect>^AR-G133-OK</expect></criterion>

<criterion id="AR133-g-AC2" cell_refs="AR-g-133"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g133_checks.py guard</invocation><expect>^AR-G133-OK</expect></criterion>

<criterion id="AR133-g-AC3" cell_refs="AR-g-133"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g133_checks.py regress</invocation><expect>^AR-G133-REGRESS-OK</expect></criterion>

<expected_criteria>AR133-g-AC1,AR133-g-AC2,AR133-g-AC3</expected_criteria>

- AC1 runs the real `SecurityResolver` with fake provider, identity, cache and checker ports: one checker call with every uncached symbol, the provider asked only about symbols not kept (none when all kept), KEPT rows identical to today's, a provider FOUND beating a NOT_KEPT with no second checker call, CHECK_FAILED / NOT_CHECKED reason words, a checker that raises, a provider outage leaving a kept symbol KEPT, and `verified_suggestions` showing KEPT and FOUND candidates. At base it FAILs.
- AC2 holds what must not move: no checker is the resolver of today, a cached FOUND and a cached KEPT are served with no call, an outage leaves a non-kept symbol UNAVAILABLE and never NOT_FOUND, a duplicated symbol is one checker entry. At base it PASSes.
- AC3 runs each existing resolver test file on its own (`test_security_resolution.py`, `test_kept_holding.py`, `test_registry_known.py`, `test_yfinance_check.py`, `ycharts/session/tests/test_resolution_broker.py`) and then that the branch changed only your files, your folder, the order and the channel file (against the merge-base with `box/dell2`). At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. The checker, the provider port, the cache keys, `KEPT_TTL`, the checker's cap and pacing, and every file not listed are not yours.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/intake/security_resolution.py
infra/aws/lambda/investor-reporting/intake/tests/test_security_resolution.py
infra/aws/lambda/investor-reporting/intake/tests/test_kept_holding.py
infra/aws/lambda/investor-reporting/intake/tests/test_registry_known.py
infra/aws/lambda/investor-reporting/intake/tests/test_door_yfinance_first.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~265/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-133.door-asks-yfinance-first.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R44_G.md</decomp_doc> round 44, workstream ~G, cell `AR-g-133`.
<owned_cells>AR-g-133</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR133-g-AC1, AR133-g-AC2, AR133-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~265/IRPT_ANLREQ.TO-AR-g-133.door-asks-yfinance-first.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-133`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR133-g-AC1,AR133-g-AC2,AR133-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 2.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one stdlib module and its tests; no deploy, no AWS call, no network. Callers of `SecurityResolver` (read at HEAD): `ycharts/session/resident_session.py:149` (passes the real checker), tests `test_security_resolution.py`, `test_kept_holding.py`, `test_registry_known.py`, `ycharts/generate/tests/test_registry_identity_port.py`, `ycharts/session/tests/test_resolution_broker.py`. The change reaches production only through the r34g resident release, under its own never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: RUN (by reading) -- cache keys and TTLs unchanged (FOUND 86400, NOT_FOUND 900, KEPT 900). 
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; the resolver runs inside the existing resident.
comp-adversary: RUN -- the issuer's check `ar_g133_checks.py` was dry-run against a scratch copy with the reference fix (build OK, guard OK) and four mutants (KEPT still sent to the provider; a second checker call after the provider; verified_suggestions unchanged; CHECK_FAILED symbols dropped from the provider call): each mutant fails build or guard. Traps: a KEPT symbol that still reaches the provider; two checker calls per check; the cached NOT_FOUND symbols left out of the first checker batch; a suggestion hidden because it is KEPT; a NOT_FOUND misread when the provider is down (must be UNAVAILABLE). NOT seen (blind): the live checker's Yahoo behaviour at a larger first batch (its cap of 10 and 1 s pacing are unchanged) and the resident's wall time; denominator: 6 behaviours in AC1, 4 in AC2.
</preflight>

- Cut on the CTO's rule (msg 9522, PRD v0.22) by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path (the module lives under infra/); the cell itself moves nothing deployed. Base: AR133-g-AC1 FAILs, AR133-g-AC2 PASSes, AR133-g-AC3 PASSes (in the worker's worktree).
