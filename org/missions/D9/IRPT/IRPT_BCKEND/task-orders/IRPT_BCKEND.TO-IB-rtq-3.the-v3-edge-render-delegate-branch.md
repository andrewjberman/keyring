# TO IRPT_BCKEND.TO-IB-rtq-3 -- V3, THE EDGE: a render-key branch in `auth-validator-edge/index.mjs` that runs BEFORE the admin-bypass evaluation, admits the render token only for the print page/SPA-assets/three API paths, and injects the verified render-delegate marker headers. CONTRACTS "THE RENDER IDENTITY" item 4 (V3 half) and item 8 (edge half) -- PRD v0.17, `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md:177-262`.

<to_id>IRPT_BCKEND.TO-IB-rtq-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~16</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 17 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.17 @`4f942b7657` | **Decomp cell:** `IB-rtq-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.21, s.R17.1) | **outcome_ref:** FWD-2 (own, B15 row), FWD-11 (contrib) | **Rows:** none yet | **Ruling:** CTO msg 99478 | **Reference (READ-ONLY, never edited by this cell):** `auth-validator-edge/index.mjs:255-261` (the admin-bypass evaluation this branch must run BEFORE), `:404` (the existing `X-Firm-Id` injection shape this branch's own header injection mirrors)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~16` (first invocation). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~16;`.
- **Worktree:** the issuer creates a fresh worktree on a new branch, cut from CLOUD HEAD AFTER this order's own commit lands, and verifies THIS FILE is present in it before spawning. First act: `cd` into the worktree, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtq-3.the-v3-edge-render-delegate-branch.md` -- absent means STOP and file a row. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing the worktree's own absolute path.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~16 <0.9.0_WK_IRPT_BCKEND~16@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`.
- **Report discipline:** your FINAL MESSAGE is the WORKER REPORT the order asks for, sent exactly once when genuinely done or genuinely STOPPED. A commit landing is not the same as your turn ending; the issuer will not remove your worktree until your actual task-notification arrives (row `IRPT_BCKEND-S117`'s lesson).
- Node via the host's `node`, this repo's existing `.mjs` Lambda test pattern (find and reuse it -- do not invent a new test runner). A recursive grep/find in Bash is rail-DENIED and a denial aborts the WHOLE call: use the Read/Grep/Glob tools and keep a gated read in its own call.

## THE CELL

- **(a) THE BRANCH, BEFORE ADMIN-BYPASS.** In `infra/aws/lambda-edge/auth-validator-edge/index.mjs`, add a new render-key verification branch that executes BEFORE the admin-bypass evaluation (currently `:255-261` -- `payload.role === "admin" || payload.firmRole === "admin" || payload.tier === "internal" || payload.userType === "Dev"`). Confirm the exact current line numbers yourself before citing them in your own commit/result -- they drift. The render branch: verifies the token against the render PUBLIC key (a fixture key you generate for this cell's own test -- do not depend on `IB-rtq-1`'s actual module; generate your own throwaway keypair so this cell is independently testable) and `aud === "irpt-render"`; admits ONLY when the request URI is `/investor-reporting/print`, one of the SPA's static asset paths, or one of the three API paths (`GET /api/scoped/investor-reporting/performance/{accountSetId}`, `.../analysis/{jobId}/sections`, `.../narrative/{reportId}`) -- ANY OTHER URI IS REFUSED, and the refusal happens in this branch, never by falling through to the human-token path.
- **(b) THE INJECTION, MIRRORING THE EXISTING SHAPE.** On accept, inject headers in the SAME shape the existing code already uses for `X-Firm-Id` (currently `:404`, `request.headers["x-firm-id"] = [{ key: "X-Firm-Id", value: ... }]`): `X-User-Email` = `render:<render_id>` (from the verified `jti`/`sub` claim); `X-User-Role` = `renderer`; `X-Firm-Id` = the VERIFIED `firmId` claim (never trust a client-supplied value for this); and the render marker -- `X-Render-Delegator`, `X-Render-Bundle`, `X-Render-Revision` -- from the verified `delegator`/`bundle`/`revision` claims. This OVERWRITES any client-supplied header of those exact names, exactly as the existing trusted-header injection already does for the human path -- write a test proving a client-supplied `X-Firm-Id`/`X-User-Role`/etc. on the request is IGNORED and the verified claim value wins. The branch NEVER injects `X-Advisor-Id`, `X-Advisor-Role`, or `X-User-Type` under any condition -- a test asserts these three headers are absent from the outgoing request on every render-token path, including one where the caller supplied fake values for them.
- **(c) REFUSAL ARMS.** Test: (d) a render-key-signed token carrying `tier internal` or `role admin` is refused BY THIS BRANCH (not merely unused downstream -- the branch itself must check and refuse, since a later handler reading the injected headers has no way to know the claim was poisoned); (c) a token past its `exp` is refused (use the JWT library's own expiry check, do not hand-roll clock comparison); a token for the wrong `aud` (e.g. a human portal token, `aud` != `irpt-render`) falls through to the EXISTING human-path evaluation completely unchanged -- write this as a regression test proving your new branch does not alter behavior for any non-render token (arm (f), the negative-widening control): run the existing edge-auth test file (find it, confirm its current pass state before your change, confirm it still passes unmodified in expectation after).
- **(d) V1 UNCHANGED.** Arm (e) -- a render token presented to V1 (`/auth/...`) is refused there -- needs NO code change in this cell (V1 is out of scope; a render-key token fails V1's existing key/aud check structurally). Write ONE test confirming this by constructing a render-key token and running it through V1's existing verification path (read-only use of V1's code, no edit), confirming it is refused for the expected reason (wrong key or wrong aud, whichever V1 actually checks first -- read the code, do not guess).

## DELIVERABLE
The render-key branch in `auth-validator-edge/index.mjs`, its header-injection logic, and its refusal arms; the regression test proving the existing human-path edge-auth suite is unaffected; the V1-refusal confirmation test; the proof instance for THIS order.

## BOUNDS
- **NO Secrets Manager entry, NO SSM parameter, NO AWS API call, NO Lambda deploy, NO CloudFront distribution change.** Code + tests only, against a fixture keypair and synthetic requests.
- **NO edit to V1, V4, V5, V6, or V7** -- item 4's closing line ("every other verifier refuses it unchanged") means those five need NO code change; if you find yourself wanting to touch one, STOP and file a row -- that means the design assumption is wrong, not that this cell's scope should grow.
- **NO edit to any EXISTING test's expected value** in the edge-auth test suite -- only NEW test functions are added; every pre-existing assertion must still pass unmodified.
- **NO edit to `_scope/resolve.py`, `_authz/enforce.py`, `portal-authorizer/index.mjs`, or the render-key minter module** -- those are `IB-rtq-2`'s and `IB-rtq-1`'s surfaces.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W16-S<k>` continuing above the highest at your HEAD, appended as a NEW fenced JSON block (CRLF, UTF-8, `project`, `fabric`, `surfaced_at`, `one_line`, `grounding` AND `disposition` required, full ISO `surfaced_at`); validate every fence still parses; then keep working. Do NOT self-graduate your own filed row. Never edit this face, never widen the order.

<expected_criteria>R117-AC3</expected_criteria>
<criterion id="R117-AC3" cell_refs="IB-rtq-3"><invocation>cd deliverables/0.9.0_WK_IRPT_BCKEND~16 &amp;&amp; node --test test_edge_render_delegate.mjs</invocation><expect>all tests PASS, including: the three-path admission, the header-injection-overwrites-client-supplied-values arm, the X-Advisor-* absence arm, the tier-internal/role-admin refusal arm (d), the V1 refusal confirmation (e), and the full pre-existing edge-auth suite passing unmodified in expectation (arm (f), negative-widening)</expect></criterion>
**`R117-AC3` -- PASSES BY OUTPUT:** the new render branch passes every arm it owns, and the pre-existing human-path edge-auth suite passes unchanged, proving no regression. The result.md prints the full test output and quotes the exact branch placement (line numbers, confirmed at your own HEAD) relative to the admin-bypass evaluation.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtq-3.the-v3-edge-render-delegate-branch.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~16/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda-edge/auth-validator-edge/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.21, cell `IB-rtq-3` (s.R17.1).
<owned_cells>IB-rtq-3</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS credential or IAM grant is read or exercised this round; offline only.
comp-adversary: DECLARED-NOT-APPLICABLE at this offline-build stage -- the adversarial read is the CVO's cross-cell L9, once B14/B3 also land.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R117-AC3 (mechanical -- test-suite pass on the edge branch and the unmodified pre-existing suite; the compound acceptance arms are CVO-graded across all three round-17 cells, never self-graded here). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~16/IRPT_BCKEND.TO-IB-rtq-3.the-v3-edge-render-delegate-branch.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row for the id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND the criterion PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, the criterion's deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
</content>
