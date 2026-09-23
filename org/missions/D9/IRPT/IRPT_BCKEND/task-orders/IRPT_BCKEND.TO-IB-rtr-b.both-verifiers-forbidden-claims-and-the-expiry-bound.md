# TO IRPT_BCKEND.TO-IB-rtr-2 -- BOTH VERIFIERS, THE FORBIDDEN CLAIMS + THE EXPIRY BOUND: the real V2 `authorizeRenderToken` accepts a render token carrying `role admin`/`firmRole admin`/`tier internal`/`userType Dev` -- exactly the four claims the whole separate-key design exists to make structurally impossible, and V3 already refuses. CVO round-17 findings `C-S201`, `C-S210` -- `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md` (co-committed with `REMEDIATION_v8.md` @7595037af9).

<to_id>IRPT_BCKEND.TO-IB-rtr-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~18</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 18 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.17 @`4f942b7657` | **Decomp cell:** `IB-rtr-2` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.22, s.R18.1) | **outcome_ref:** FWD-2 (own) | **Rows:** `IRPT_BCKEND-C-S201`, `IRPT_BCKEND-C-S210` | **Ruling:** CTO's round-17 analysis, msg 99542, ruling R18-b | **Reference (READ-ONLY, never edited by this cell):** `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_PROBE.mjs` (the CVO's own probe -- it minted a render token carrying each forbidden claim against the real V2 handler and got `isAuthorized: true` four times; your fix must flip that to `false` four times)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~18` (first invocation). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~18;`.
- **Worktree:** the issuer creates a fresh worktree on a new branch, cut from CLOUD HEAD AFTER this order's own commit lands, and verifies THIS FILE is present in it before spawning. First act: `cd` into the worktree, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtr-2.both-verifiers-forbidden-claims-and-the-expiry-bound.md` -- absent means STOP and file a row. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing the worktree's own absolute path.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~18 <0.9.0_WK_IRPT_BCKEND~18@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`.
- **Report discipline:** your FINAL MESSAGE is the WORKER REPORT the order asks for, sent exactly once when genuinely done or genuinely STOPPED. A commit landing is not the same as your turn ending; the issuer will not remove your worktree until your actual task-notification arrives (row `IRPT_BCKEND-S117`'s lesson).
- Node via the host's `node`. A recursive grep/find in Bash is rail-DENIED and a denial aborts the WHOLE call: use the Read/Grep/Glob tools and keep a gated read in its own call.

## THE CELL

- **(a) V2: REJECT THE FOUR FORBIDDEN CLAIMS.** `infra/aws/users/lambda/portal-authorizer/index.mjs`'s `authorizeRenderToken` (currently reads the verified JWT payload and checks route/path-id only) must ALSO refuse if the payload carries `role: "admin"`, `firmRole: "admin"`, `tier: "internal"`, or `userType: "Dev"` -- checked on the VERIFIED payload (post `jwt.verify`), matching how V3's `hasForbiddenRenderClaims` already does it (read `render_auth.mjs` for the exact shape, mirror it, do not diverge). Test: each of the four claims, individually, against an otherwise-valid render token on an otherwise-admissible route, refused; a clean render token (none of the four) on the same route, admitted (the positive control).
- **(b) BOTH VERIFIERS: THE EXPIRY BOUND, STATED AND TESTED.** `exp` must be REQUIRED at both V2 and V3 (a token with no `exp` claim is refused, never treated as non-expiring) and bounded at 5 minutes or less from `iat` (an oversized `exp`, e.g. 1 hour out, is refused even though it has not yet expired -- the minter never produces one, but a verifier must not trust an unbounded value blindly). Skew leeway stays 60s or less at both (do not widen it). Controls, each beside a valid positive: missing `exp` entirely; an oversized `exp` (further than 5 minutes from `iat`); just inside the 60s skew edge (accepted); just outside it (refused) -- run all four against BOTH V2 and V3, eight arms total, not four.
- **(c) LOGGING.** V2's accept and refusal logs for the render path currently carry route/claimName (accept) or route/claimName/pathIdPresent (refusal) only -- no render identity. Add `jti` and render id (identical values, per the minter's own `sub`/`jti` grammar) to BOTH the accept and refusal log lines at V2. Check V3's own logging for the same gap and fix it there too if present (read `render_auth.mjs`/`index.mjs`'s current logging first; do not assume). **NEVER log the token itself or any key material** -- test that your new log lines do not contain the raw JWT string or PEM content (a simple substring-absence assertion on the captured log output is sufficient).
- **(d) THE HUMAN PATH IS UNTOUCHED.** The existing human `aud`/`iss` policy (a separately-known, separately-scoped gap, per the CTO's own explicit carve-out) is NOT this cell's to fix -- do not add any check to the human-token verification path. Confirm via a regression test that human-token behavior on every route is byte-identical to before this cell.

## DELIVERABLE
V2's four-forbidden-claims refusal with its five controls (four negative, one positive); the expiry bound at both V2 and V3 with all eight controls; the jti/render-id logging fix at both verifiers with its no-secret-leak test; the human-path regression confirmation; the proof instance for THIS order.

## BOUNDS
- **NO Secrets Manager entry, NO SSM parameter, NO AWS API call, NO Lambda deploy, NO CloudFront/API-Gateway change.** Code + tests only.
- **NO edit to the human `aud`/`iss` verification path** -- that gap is a separate, already-known change under its own halves, not this cell's.
- **NO edit to any EXISTING test's expected value** in either verifier's pre-existing suite -- only NEW test functions are added.
- **NO edit to `_scope/resolve.py`, `_authz/enforce.py`, or the asset-allowlist/origin-marker logic in `render_auth.mjs`** -- those are `IB-rtr-3`'s and `IB-rtr-1`'s surfaces; this cell's V3 edits are confined to the forbidden-claims check, the expiry bound, and logging.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W18-S<k>` continuing above the highest at your HEAD, appended as a NEW fenced JSON block (CRLF, UTF-8, `project`, `fabric`, `surfaced_at`, `one_line`, `grounding` AND `disposition` required, full ISO `surfaced_at`); validate every fence still parses; then keep working. Do NOT self-graduate your own filed row. Never edit this face, never widen the order.

<expected_criteria>R118-AC2</expected_criteria>
<criterion id="R118-AC2" cell_refs="IB-rtr-2"><invocation>cd deliverables/0.9.0_WK_IRPT_BCKEND~18 &amp;&amp; node --test test_v2_v3_forbidden_claims_and_expiry.mjs</invocation><expect>all tests PASS rc=0: 4 forbidden-claim refusals + 1 positive at V2, 8 expiry/skew arms across both verifiers, the no-secret-leak log assertion, and the human-path regression control</expect></criterion>
**`R118-AC2` -- PASSES BY OUTPUT:** V2 refuses all four forbidden claims, both verifiers enforce the same stated expiry/skew bound with all eight controls passing, logging carries render identity without leaking secrets, and the human path is confirmed unchanged. The result.md prints the full test output.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtr-2.both-verifiers-forbidden-claims-and-the-expiry-bound.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~18/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/mcp/sessions/
infra/aws/users/lambda/portal-authorizer/
infra/aws/lambda-edge/auth-validator-edge/render_auth.mjs
infra/aws/lambda-edge/auth-validator-edge/index.mjs
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.22, cell `IB-rtr-2` (s.R18.1).
<owned_cells>IB-rtr-2</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS credential or IAM grant is read or exercised this round; offline only.
comp-adversary: DECLARED-NOT-APPLICABLE at this offline-build stage -- the adversarial read is the CVO's cross-cell L9 once IB-rtr-5's chain lands.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override. Note: `infra/aws/lambda-edge/auth-validator-edge/render_auth.mjs` and `index.mjs` are granted READ+EDIT here ONLY for the forbidden-claims check, expiry bound and logging on the RENDER branch -- IB-rtr-1 owns the origin-marker/asset-allowlist logic in the SAME files; if your edit and IB-rtr-1's overlap on the same lines at merge time, that is a drain-time conflict the issuer resolves, never a reason to widen this cell's own scope.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R118-AC2 (mechanical -- test-suite pass across both verifiers). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~18/IRPT_BCKEND.TO-IB-rtr-2.both-verifiers-forbidden-claims-and-the-expiry-bound.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row for the id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND the criterion PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, the criterion's deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
</content>
