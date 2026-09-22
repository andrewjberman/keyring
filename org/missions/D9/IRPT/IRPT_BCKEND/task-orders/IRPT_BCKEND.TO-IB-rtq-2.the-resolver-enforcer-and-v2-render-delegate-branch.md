# TO IRPT_BCKEND.TO-IB-rtq-2 -- THE RESOLVER, THE ENFORCER, AND V2: the `RENDER_DELEGATE` principal class in `_scope/resolve.py`, its scope algebra in `_authz/enforce.py`'s `Enforcer.resolve_now`, and the scoped render-token branch in the `portal-authorizer` Lambda (V2). CONTRACTS "THE RENDER IDENTITY" item 8 (resolver/enforcer half) and item 4 (V2 half) -- PRD v0.17, `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md:177-262`. `3.0.0_SA_CVO~B`'s L4-R review found the v0.16 contract FALSE here (an offline reproducer showed the renderer's own header set classifies UNKNOWN and resolves NO_PRINCIPAL against the CURRENT code) -- this cell is the fix the v0.17 correction authorizes.

<to_id>IRPT_BCKEND.TO-IB-rtq-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~15</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 17 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.17 @`4f942b7657` | **Decomp cell:** `IB-rtq-2` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.21, s.R17.1) | **outcome_ref:** FWD-2 (own, B3 row) | **Rows:** none yet | **Ruling:** CTO msg 99478; CVO's `IRPT_BCKEND_PRD_v017_L4R_REVIEW_20260922.md` reproduced-implementation-boundary section (@e963205de6 / half_hash `4d95de5f4f98...`) | **Reference (READ-ONLY, never edited by this cell):** `IRPT_BCKEND_PRD_v016_RENDER_PRINCIPAL_PROBE.py` (the CVO's own offline reproducer -- your test suite should EXTEND its shape, not diverge from it, so the CVO can re-run a comparable check at L9)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~15` (first invocation). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~15;`.
- **Worktree:** the issuer creates a fresh worktree on a new branch, cut from CLOUD HEAD AFTER this order's own commit lands, and verifies THIS FILE is present in it before spawning. First act: `cd` into the worktree, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtq-2.the-resolver-enforcer-and-v2-render-delegate-branch.md` -- absent means STOP and file a row. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing the worktree's own absolute path.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~15 <0.9.0_WK_IRPT_BCKEND~15@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`.
- **Report discipline:** your FINAL MESSAGE is the WORKER REPORT the order asks for, sent exactly once when genuinely done or genuinely STOPPED. A commit landing is not the same as your turn ending; the issuer will not remove your worktree until your actual task-notification arrives (row `IRPT_BCKEND-S117`'s lesson).
- Python `py -3.12`. Node is read-only reference here (`portal-authorizer/index.mjs` is edited, but this cell's own proof runs in Python/pytest against the Python surfaces; the `.mjs` edit is proved by a Node-side test per (c) below). A recursive grep/find in Bash is rail-DENIED and a denial aborts the WHOLE call: use the Read/Grep/Glob tools and keep a gated read in its own call.

## THE CELL

- **(a) TRUSTED HEADERS.** In `infra/aws/lambda/investor-reporting/_scope/resolve.py`, `TRUSTED_HEADERS` (currently `:88-98`, confirm the live line numbers yourself -- they drift): add THREE new entries, `x-render-delegator`, `x-render-bundle`, `x-render-revision`, each citing its source as the edge's verified render-marker injection (parallel format to the existing nine entries, which cite `auth-validator-edge/index.mjs` line numbers -- cite the render branch `IB-rtq-3` is building at its own file, since that is where these three will actually be injected; if `IB-rtq-3` has not landed a branch to cite yet, cite the PRD contract paragraph itself, CONTRACTS item 8, and file a row noting the citation will need updating once `IB-rtq-3`'s line numbers exist). Confirm via a unit test that `trusted_only()` no longer drops these three names -- reproduce the CVO's own probe finding (v0.16 code drops them) and confirm your fix flips it.
- **(b) THE RENDER_DELEGATE BRANCH.** In `classify_principal` (currently `:154-196`), add ONE new branch placed AFTER the existing origin/subject checks (currently `:176-180`, "no verified edge marker, or no subject -> UNKNOWN") and BEFORE the OPAL_GLOBAL roster check (currently `:181-183`): if `trusted.get("x-user-role") == "renderer"` AND the render marker (`x-render-delegator`/`x-render-bundle`/`x-render-revision`, or whichever subset you and `IB-rtq-3` settle marks "the marker present" -- state your exact test explicitly in the code's own docstring) is present, return `RENDER_DELEGATE`; if `x-user-role == "renderer"` WITHOUT the marker, return `UNKNOWN` with a reason naming the missing marker (arm (j)). No existing branch's condition or return value changes -- write a test that runs the FULL existing test suite in `_scope/tests/test_resolve.py` unmodified-in-assertion (you may add new test functions, never change an existing one's expected value) and confirms every pre-existing case still classifies exactly as before. Add `RENDER_DELEGATE` to `PRINCIPAL_CLASSES` (currently `:106`).
- **(c) THE ENFORCER'S SCOPE ALGEBRA.** In `infra/aws/lambda/investor-reporting/_authz/enforce.py`'s `Enforcer.resolve_now` (currently `:256`): when `principal_class == "RENDER_DELEGATE"`, compute the scope as the INTERSECTION of (i) the delegator's scope resolved NOW by calling the EXISTING resolution path with the delegator's own identity (read from the `delegator` claim/header the minter/edge carries) -- so a delegator whose entitlement is revoked between mint and read produces a NARROWER or EMPTY intersection on the next resolve (arm (i)) -- and (ii) the bundle's pinned scope at the `X-Render-Revision` claim (the three read operations, for only the bundle-pinned object ids). An empty intersection returns a REFUSAL (the existing refusal shape/codes), never an empty-but-successful answer. Requesting an operation outside the three, or an object outside the pinned ids, is refused the same way (arm (k)). Write a test with THREE arms: (1) delegator currently entitled + object inside the pinned/bundle scope -> the three reads succeed; (2) delegator's entitlement revoked (simulate by having the "resolved now" call return an empty/narrower scope) -> refused; (3) an object outside the bundle's pinned scope, or an operation outside the three -> refused.
- **(d) V2 -- `portal-authorizer/index.mjs`.** Currently default-allow. Add a render-key branch: load the render public key (a fixture key for this cell's own test, following `IB-rtq-1`'s fixture pattern -- do not depend on `IB-rtq-1`'s actual module, generate your own throwaway keypair so this cell is independently testable); admit `aud irpt-render` ONLY when the request's `routeKey` is one of the three named GETs (`GET /api/scoped/investor-reporting/performance/{accountSetId}`, `.../analysis/{jobId}/sections`, `.../narrative/{reportId}`) AND the path id in the route equals the corresponding claim; every other route or a mismatched id is an EXPLICIT deny, never a fallthrough to the default-allow. Confirm the authorizer's cached-result TTL stays 0 (it is shared across 14+ scoped routes; do not introduce a cache keyed only on `Authorization`). Write a Node-side test (this repo's existing test runner for `.mjs` Lambdas -- find and reuse its pattern, do not invent a new one) covering: the three routes with matching ids pass; a fourth route is denied (arm (b) route half); the same route with a swapped path id is denied (arm (b) id half); a human portal token's existing default-allow behavior on non-render routes is UNCHANGED (arm (f)).
- **(e) NO SIBLING-BLOCKING.** If `IB-rtq-1`'s minter module or `IB-rtq-3`'s edge branch have not landed when you start, do NOT wait -- build and prove (a)-(d) against your OWN fixtures (a throwaway keypair you generate, synthetic header sets you construct by hand matching the PRD's exact claim names). The PRD contract text is the shared dependency, not another cell's code.

## DELIVERABLE
The `TRUSTED_HEADERS`/`classify_principal`/`PRINCIPAL_CLASSES` edits with passing tests (old + new); the `Enforcer.resolve_now` `RENDER_DELEGATE` branch with its three-arm test; the `portal-authorizer/index.mjs` render branch with its Node test; the proof instance for THIS order.

## BOUNDS
- **NO Secrets Manager entry, NO SSM parameter, NO AWS API call, NO Lambda deploy, NO Terraform change, NO CloudFront/API-Gateway change.** Code + tests only, against fixture keys and synthetic requests.
- **NO edit to any EXISTING test's expected value** in `_scope/tests/test_resolve.py` or elsewhere -- every pre-existing assertion must still pass unmodified; only NEW test functions are added.
- **NO edit to `_keys/keys.py`, `auth-validator-edge/index.mjs`, or the render-key minter module** -- those are `IB-rtq-3`'s and `IB-rtq-1`'s surfaces.
- **NO wiring of the authorizer's render branch into the live API Gateway** -- code + test only, this round.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W15-S<k>` continuing above the highest at your HEAD, appended as a NEW fenced JSON block (CRLF, UTF-8, `project`, `fabric`, `surfaced_at`, `one_line`, `grounding` AND `disposition` required, full ISO `surfaced_at`); validate every fence still parses; then keep working. Do NOT self-graduate your own filed row. Never edit this face, never widen the order.

<expected_criteria>R117-AC2</expected_criteria>
<criterion id="R117-AC2" cell_refs="IB-rtq-2"><invocation>cd deliverables/0.9.0_WK_IRPT_BCKEND~15 &amp;&amp; py -3.12 -m pytest test_render_delegate_resolver_enforcer.py -v &amp;&amp; py -3.12 -m pytest infra/aws/lambda/investor-reporting/_scope/tests/test_resolve.py -v</invocation><expect>all tests PASS rc=0, including every pre-existing test in test_resolve.py unmodified in expectation, plus the new RENDER_DELEGATE classification arms and the three enforcer scope-algebra arms; a separate Node invocation for the V2 authorizer test also PASSES, printed in the same result.md</expect></criterion>
**`R117-AC2` -- PASSES BY OUTPUT:** every pre-existing `_scope`/`_authz` test still passes unchanged, the new `RENDER_DELEGATE` branch and enforcer intersection algebra pass their own arms, and the V2 authorizer's render branch passes its Node test including the negative-widening arm (f). The result.md prints the full test output for all three suites.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtq-2.the-resolver-enforcer-and-v2-render-delegate-branch.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~15/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/_scope/
infra/aws/lambda/investor-reporting/_authz/
infra/aws/users/lambda/portal-authorizer/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.21, cell `IB-rtq-2` (s.R17.1).
<owned_cells>IB-rtq-2</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS credential or IAM grant is read or exercised this round; offline only.
comp-adversary: DECLARED-NOT-APPLICABLE at this offline-build stage -- the adversarial read is the CVO's cross-cell L9, once B14/B15 also land.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R117-AC2 (mechanical -- test-suite pass across the three edited surfaces; the compound acceptance arms are CVO-graded across all three round-17 cells, never self-graded here). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~15/IRPT_BCKEND.TO-IB-rtq-2.the-resolver-enforcer-and-v2-render-delegate-branch.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row for the id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND the criterion PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, the criterion's deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
</content>
