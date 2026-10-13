# TO IRPT_ANLREQ.TO-AR-y-247.swap-suggestions-wired-and-called -- the server asks the swap advisory when its capability is verified, verifies each candidate, and attaches them as suggestions -- default off

<to_id>IRPT_ANLREQ.TO-AR-y-247</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~80</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-247` (`decompositions/IRPT_ANLREQ_DECOMP_R22B_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~80`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-80` (branch `wk-IRPT_ANLREQ-80`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~80 <0.9.0_WK_IRPT_ANLREQ~80@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W80-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-247`, inlined) -- GATES (2) AND (3) OF RULING B, SERVER SIDE: THE WIRING AND THE CALLER. Code and tests only; the capability stays absent, so nothing changes until the receipt exists.

*Ruling B (CTO msg 7112): `search_capability` is wired where the resident builds `KimiAdvisory`, and the composer's upload path is the caller. Today the typo `check` is the only source (`intake/upload_suggestions.py` `suggest_for`, called at `ycharts/generate/resident_worker.py` :760-765) and a finding carries at most one `suggestion` {symbol, source, provider_receipt_sha256}. `intake/security_resolution.py` :242-250 `verified_suggestions(candidates, resolver)` already keeps only exact provider FOUND rows, at most 3, and has no caller outside tests. A suggestion NEVER fills the box or the request on its own (ruling).*

1. **Read first:** `intake/resolution_kimi.py` (the gate and the `swap` parse), `intake/security_resolution.py` :242-250, `intake/upload_suggestions.py`, `ycharts/generate/resident_worker.py` :740-790, `ycharts/generate/resident_session.py` (where `KimiAdvisory` is built and its arguments), `ycharts/generate/kimi_port.py`, and the existing tests `ycharts/generate/tests/test_y4_check_gate.py`, `intake/tests/test_resolution_kimi.py`. Record `where_wired` (file:lines) and `how_the_capability_would_arrive` (a config/parameter/file the resident reads at start; propose ONE, from what the resident already reads; do not add a secret or an environment variable of your own invention: name the existing mechanism or say there is none).
2. **The wiring (gate 2).** The resident builds `KimiAdvisory` with `search_capability` read from that ONE existing mechanism; absent or invalid means `None` (so `swap` returns `KIMI_WEB_SEARCH_UNVERIFIED` exactly as today). No default capability is shipped in the code.
3. **The caller (gate 3).** In `suggest_for` (or a sibling function next to it in the same file; the file is `intake/upload_suggestions.py`): for each `TICKER_NOT_FOUND` row that the typo `check` left WITHOUT a verified suggestion, and only when the advisory's `search_capability` verifies, ask `advisory("swap", symbol, context_symbols=..., deadline=...)`, pass its `candidates` (at most 3) through the provider verification the file already uses (`verify` port; use `verified_suggestions` if it fits the port, else the same exact-match test as the check lane: FOUND, EXACT_PROVIDER_MATCH, no `features_needed`, a provider receipt) and attach the kept ones to the finding as a NEW member `suggestions`: a list of `{symbol, source: "KIMI_SWAP_PROVIDER_VERIFIED", provider_receipt_sha256, reason}` where `reason` is the candidate's own reason string (bounded to 200 characters, treated as text). The existing `suggestion` member and the action `ACCEPT_SUGGESTION` stay exactly as they are for the typo lane; the swap lane adds NO action and NEVER writes a proxy or a substitution. The total Kimi time per upload stays inside `TOTAL_SUGGEST_SECONDS` (240) shared with the check lane; rows the budget does not reach stay as the freeze wrote them. A swap failure, an empty candidate list, an unverified candidate or any refusal leaves the finding as it was.
4. **The tests, before and after.** New file `ycharts/generate/tests/test_swap_suggestions.py` (at least 6 tests; fake ports): (a) capability absent: a TICKER_NOT_FOUND row gets no `suggestions` and `swap` is never sent (TIMXX's case: still no match); (b) capability verified and the provider verifies two of three candidates: the finding carries exactly those two, each with source and receipt; (c) a candidate the provider does not FIND exactly is dropped; (d) four candidates are refused (`SUGGESTIONS_INVALID`) and the finding is untouched; (e) the per-upload budget is shared with the check lane (a spent budget leaves the rest unasked); (f) the finding's `actions` and `suggestion` members are byte-equal to today's for every case. `before_arm`: run (b) against HEAD without your change: it FAILS. Then: `intake/tests` passes (365 floor; if you touch `upload_suggestions.py` the existing `test_y4_check_gate.py` stays green) and the neighbours that collect in `ycharts/generate/tests` (fitz-missing collection errors are a known limit: name them and show they are the same at HEAD).
5. **Write `r22/SWAP_SUGGESTIONS.json`:** `where_wired`, `how_the_capability_would_arrive`, `behaviour` (with a capability, without, with failures; file:lines), `wire_shape` (the exact `suggestions` member with a constructed example), `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `files_changed`, `claim`, `not_read`.
6. **In your report:** the wire shape in one line, the mechanism the capability would arrive by, the counts, and anything that would make the release larger than one member in a leg.

### ACCEPTANCE

<criterion id="AR247-y-AC1" cell_refs="AR-y-247"><invocation>python C:/dev/wk-irpt-anlreq-80/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y247-swap --root C:/dev/wk-irpt-anlreq-80</invocation><expect>Y247-SWAP-OK</expect></criterion>
`AR247-y-AC1`: the record names the wiring and the capability mechanism, the exact wire shape of `suggestions`, a new test file with at least 6 passing tests whose case (b) fails at HEAD, and the intake folder passes at 365 or more.

<criterion id="AR247-y-AC2J" cell_refs="AR-y-247" judgment="true"/>
`AR247-y-AC2J` (judgment, graded at L9, never by you): with no capability the behaviour is byte-identical to today (TIMXX still shows no match), a suggestion is never an action or a substitution, every candidate is provider-verified exactly, the Kimi time stays inside the one per-upload budget, and no secret or default capability was added.

<expected_criteria>AR247-y-AC1 AR247-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~80/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22B_Y.md</decomp_doc>
<owned_cells>AR-y-247</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~80/IRPT_ANLREQ.TO-AR-y-247.swap-suggestions-wired-and-called.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-247`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR247-y-AC1,AR247-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source and test edits in a worktree; nothing is released, deployed or called; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling B (msg 7112) and the read record `0.9.0_WK_IRPT_ANLREQ~76/r22/PROXY_SUGGESTION_READ.json` against the cell; the lens: a suggestion that fills a box or a request on its own, a candidate shown without its provider verification, a gate that is skipped because the next one is built. The order requires the user to pick, the gates in their order, and the no-suggestion case to show nothing. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling B (msg 7112: the Kimi swap advisory, behind its own three gates; a suggestion never fills the box) as workstream `YR` round 20. Base: `AR247-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
