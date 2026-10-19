# TO IRPT_ANLREQ.TO-AR-y-415.o1-staff-owner-fallback-in-create-owner-and-advisor-owner -- O1 backend: an Opal staff filer with no advisor, or with an advisor who has no profile at the firm, is never refused; the owner falls back to the signed-in principal (served.py _create_owner and _advisor_owner only)

<to_id>IRPT_ANLREQ.TO-AR-y-415.o1-staff-owner-fallback-in-create-owner-and-advisor-owner</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~309</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ75</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-415` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (a staff user files for any firm without being refused), C-FIRM | **depends_on:** PRD IRPT_ANLREQ v0.24 (both halves signed @7b55cfefe1), CTO msg 10978, ~P2 review msg 10992 (typed exception), AR-y-416 (the portal half ships in the SAME release)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~309`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-309` (branch `wk-IRPT_ANLREQ-309`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~309 <0.9.0_WK_IRPT_ANLREQ~309@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W309-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-415`, inlined)

*Context.* Owner resolution in `infra/aws/lambda/investor-reporting/_authz/served.py`: `_create_owner(self, access, actor, event, tenant, reads)` (def at about line 1073) and `_advisor_owner(self, advisor_email, tenant, reads)` (def at about line 1095, to the end of `resolve_prospect_owner(claims, tenant)`), with `ON_BEHALF_ADVISOR_PARAM = "advisor_email"` (about line 633). TODAY: no `advisor_email` key and `tenant in actor["allowedFirmIds"]` raises `ProspectOwnershipRefused("an on-behalf upload must name the firm advisor")`; an advisor named whose partner profile at the firm is absent raises `ProspectOwnershipRefused("advisor has no partner profile at the named firm")` (a typed email that matches nothing refuses an Opal staff filer: measured 2026-10-19 16:38:54Z and 16:39:17Z, NOT_AUTHORIZED). The PRD (v0.23/v0.24, C-FIRM): Opal staff choose any firm and own the request through `access.prospect_owner()`; the typed advisor email is ATTRIBUTION ONLY. The CTO's placement (msg 10955): this ONE function family is absorbed into IRPT_ANLREQ; the rest of `served.py` stays IRPT_BCKEND's, and `2.0.0_SA_COO~P2` reviews the hunk. The reviewed design is in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/O1_OWNER_RESOLUTION_HUNK_FOR_P2_REVIEW_20261019.md` (read it first).

*The change (cite by function name).*
1. Add ONE class beside `ProspectOwnershipRefused`'s use in `served.py` (a module-level `class AdvisorUnprovisioned(ProspectOwnershipRefused)` with a one-line docstring; import `ProspectOwnershipRefused` at module level only if the file does not already import it in a way that makes the subclass definable, otherwise define it where `from prospect import ProspectOwnershipRefused` is lazy by importing it inside a small factory: read the file and choose the smallest change; it is the only line outside the two function bodies).
2. `_create_owner`: read `named = query.get(ON_BEHALF_ADVISOR_PARAM)` (keep the `queryStringParameters` not-a-dict refusal as today). If `named` is not a non-blank string: `return access.prospect_owner()` whatever `allowedFirmIds` lists (delete the `allowedFirmIds` clause). Otherwise `try: return self._advisor_owner(named, tenant, reads)` and `except AdvisorUnprovisioned: return access.prospect_owner()`.
3. `_advisor_owner`: raise `AdvisorUnprovisioned` (instead of `ProspectOwnershipRefused`) for exactly two cases: the partner profile at the named firm is absent ("advisor has no partner profile at the named firm") and the user row is absent, not active, or of another firm ("advisor profile absent, disabled or of another firm"). EVERY other raise stays a plain `ProspectOwnershipRefused`: a blank email, the firm not in `firm_ids()`, the profile reads raising, AND a partner email or firm MISMATCH (`raw.get("email") != email` or a different `firmId`: data damage, not "unprovisioned"; read the existing condition and split it so only the ABSENT-profile case raises the subclass). A provisioned advisor still builds the owner through `resolve_prospect_owner(claims, tenant)` unchanged.
4. Nothing else in the file moves: every other function, class and constant is byte-identical (the bound check enforces it). The typed email is NOT recorded anywhere as attribution (state this in your report); the portal stops sending it (AR-y-416).

*The tests (NEW file `infra/aws/lambda/investor-reporting/_authz/tests/test_create_owner_on_behalf.py`, nine test functions named exactly `test_t1_...` to `test_t9_...`).* No test in the repo pins the on-behalf branch today (read `infra/aws/lambda/investor-reporting/_authz/tests/` for the stub style of the other served tests; the guard class is the one that defines `_create_owner`; call the two methods directly on an instance or an unbound call with a small stub `self` that exposes `_advisor_owner`, with a fake `access` whose `prospect_owner()` returns a sentinel dict, a fake `actor` dict, a fake `reads` with `partner(email, tenant)` and `user(email)`, `ids.firm_ids` monkeypatched to hold the tenant, and `prospect.resolve_prospect_owner` monkeypatched to return a marker dict): T1 staff, no advisor key, tenant in `allowedFirmIds` -> the `prospect_owner()` sentinel; T2 staff, blank advisor value -> sentinel; T3 advisor named, partner profile and active user row present -> the advisor's owner (the resolver marker, and the sentinel NOT returned); T4 advisor named, no partner profile -> sentinel; T5 advisor named, user row disabled -> sentinel; T6 partner email or firm mismatch -> raises plain `ProspectOwnershipRefused` and NOT `AdvisorUnprovisioned`; T7 tenant not in `firm_ids()` -> raises `ProspectOwnershipRefused`; T8 `queryStringParameters` not a dict -> raises `ProspectOwnershipRefused`; T9 `access.prospect_owner()` raising `ProspectOwnershipRefused` (an unresolvable subject) propagates and returns nothing.

*What to do.* (1) Read `served.py` around the two functions and the tests folder; run the baseline first and print it: `cd infra/aws/lambda/investor-reporting/ && python -m pytest _authz -q --color=no -p no:cacheprovider` (ReadMe of ~P2: 365 passed at HEAD) and the six owner-composition tests it names if you can find them. (2) Write the tests, run them against the UNCHANGED `served.py` and record which fail (T1, T2, T4, T5 must fail: that is the difference control). (3) Make the change. (4) Run the nine tests and the whole `_authz` folder; print both lines (the folder must read the baseline plus 9 passed, no failure). (5) Write `check_o1_bound.py` (below) and run it; commit with the proof instance; `controls.mutant` = the nine tests run against a copy of `served.py` WITHOUT your change (at least 4 FAIL).

You also write `check_o1_bound.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~309/` (ruff clean, stdlib only): it takes the branch point `git merge-base HEAD box/dell2`, lists `git diff --name-only <that> HEAD` and keeps the paths NOT under `org/`; it prints `O1-BOUND-OK functions=2 classes=1 files=2` only when that kept list is exactly `served.py` and the new test file AND, comparing `ast.dump` of every top-level definition and every method of the guard class in `served.py` at the branch point and at HEAD, exactly `_create_owner` and `_advisor_owner` differ and exactly one class (`AdvisorUnprovisioned`) was added; otherwise `O1-BOUND-BAD <what>` and a non-zero exit. Run it before your first edit (BAD or an error) and after.

---

## ACCEPTANCE

<criterion id="AR415-y-AC1" cell_refs="AR-y-415"><invocation>cd infra/aws/lambda/investor-reporting/ && python -m pytest _authz/tests/test_create_owner_on_behalf.py -q --color=no -p no:cacheprovider</invocation><expect>9 passed</expect></criterion>
<criterion id="AR415-y-AC2" cell_refs="AR-y-415"><invocation>cd infra/aws/lambda/investor-reporting/ && python -m pytest _authz -q --color=no -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
<criterion id="AR415-y-AC3" cell_refs="AR-y-415"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~309/check_o1_bound.py</invocation><expect>O1-BOUND-OK functions=2 classes=1 files=2</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~309/IRPT_ANLREQ.TO-AR-y-415.o1-staff-owner-fallback-in-create-owner-and-advisor-owner.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-415.o1-staff-owner-fallback-in-create-owner-and-advisor-owner`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR415-y-AC1,AR415-y-AC2,AR415-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-415</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/_authz/served.py
infra/aws/lambda/investor-reporting/_authz/tests/test_create_owner_on_behalf.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~309/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-415.o1-staff-owner-fallback-in-create-owner-and-advisor-owner.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one function family of one module and one new test file; nothing is deployed; the release (an IB2 apply with its own signed pair) is a separate act.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading `served.py` `_create_owner` and `_advisor_owner` and the ~P2 review (msg 10992) against this cell; the lens: a fallback that also swallows the mismatch refusal (T6 pins it), a fallback that lets a NON-staff filer through (the function is reached only for an internal subject; T7-T9 pin the closed refusals), an owner taken from a request value (never: the owner is `prospect_owner()` or the resolver over verified claims), a typed email recorded as authority (it is dropped), a second function edited (the bound check). NOT seen (blind): the deployed Lambda and the live directory rows; AC2 is a control that PASSES at the base (365 passed); denominator: three criteria.
</preflight>
