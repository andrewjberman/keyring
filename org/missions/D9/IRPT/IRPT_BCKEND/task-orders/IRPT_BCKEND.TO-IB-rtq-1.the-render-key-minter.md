# TO IRPT_BCKEND.TO-IB-rtq-1 -- THE RENDER-KEY MINTER: B14's export job mints one short-lived, narrowly-scoped JWT per render, signed with a SEPARATE key never used for any human token, from the frozen `ExportBundle` only. CONTRACTS "THE RENDER IDENTITY" items 1, 2, 3, 6, 8 (minter half) -- PRD v0.17, `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md:177-262`. Andrew-direct 2026-09-22 ~12:2xZ chose this mechanism (Option 2) over a human-captured session, whose refresh token lives only 7 days.

<to_id>IRPT_BCKEND.TO-IB-rtq-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~14</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 17 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.17 @`4f942b7657` | **Decomp cell:** `IB-rtq-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.21, s.R17.1) | **outcome_ref:** FWD-8, FWD-3, FWD-4 (contrib, B14 row) | **Rows:** none yet -- this cell opens the render-identity build line | **Ruling:** CTO msg 99478, "round 17 ... rests on CONTRACTS THE RENDER IDENTITY, items 1-8" | **Reference (READ-ONLY, never edited by this cell):** `infra/aws/lambda/shared/opal_auth/__init__.py` (the existing verifier pattern this minter's signing side mirrors -- python-jose, RS256, boto3 `secretsmanager`, container-cached key)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~14` (first invocation). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~14;`.
- **Worktree:** the issuer creates a fresh worktree on a new branch, cut from CLOUD HEAD AFTER this order's own commit lands, and verifies THIS FILE is present in it before spawning. First act: `cd` into the worktree, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtq-1.the-render-key-minter.md` -- absent means STOP and file a row, never proceed on content read from outside the worktree. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing the worktree's own absolute path.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~14 <0.9.0_WK_IRPT_BCKEND~14@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`.
- **Report discipline:** your FINAL MESSAGE is the WORKER REPORT the order asks for, sent exactly once when your task is genuinely done or genuinely STOPPED. A commit landing is not the same as your turn ending; the issuer will not remove your worktree until your actual task-notification arrives (row `IRPT_BCKEND-S117`'s lesson).
- Python `py -3.12` (python-jose and cryptography are already estate dependencies -- confirm, do not add a new dependency without filing a row first). A recursive grep/find in Bash is rail-DENIED and a denial aborts the WHOLE call: use the Read/Grep/Glob tools and keep a gated read in its own call.

## THE CELL

- **(a) THE SEPARATE KEY, OFFLINE ONLY THIS ROUND.** Generate ONE throwaway RSA keypair (2048+ bit) inside your own `deliverables/0.9.0_WK_IRPT_BCKEND~14/fixtures/` directory -- this is a TEST fixture standing in for the real `opal/auth/irpt-render-jwt-{private,public}-key` Secrets Manager entries, which are NOT created this round (BOUNDS below). Write the minter module so it loads the private key material from an injectable source (an env var or an explicit parameter the caller supplies), never hardcoded and never reading `opal/auth/jwt-private-key` under any code path -- that exclusion is structural, not a comment: grep your own new module for the string `jwt-private-key` and confirm the ONLY match is the render key's own name.
- **(b) THE MINTER.** A new module under `infra/aws/lambda/investor-reporting/` (your own naming choice, following the estate's `_authz`/`_scope`/`_keys` underscore-module convention; never an edit to `infra/aws/lambda/shared/opal_auth/`, which is the SHARED human-token verifier and out of this cell's scope). One function that takes a frozen `ExportBundle`-shaped object (tenant/firm id, bundle id, revision, the three path ids `accountSetId`/`jobId`/`reportId`, and the delegator subject stamped into the bundle at freeze) and returns a signed JWT string with EXACTLY these claims: `iss` = `opal-irpt-render`; `aud` = `irpt-render`; `exp` <= 5 minutes after `iat`; `nbf`/`iat` with at most 60s skew leeway; `jti` = a fresh unique render id; `role` = `renderer`; `tier` = `render`; `firmId` = the bundle's tenant firm id; `bundle`, `revision`, `accountSetId`, `jobId`, `reportId`; `sub` = `render:<the same render id as jti>`; `delegator` = the bundle's stamped freeze-time subject. Sign RS256 with the fixture private key from (a).
- **(c) STRUCTURAL REFUSAL OF ADMIN-BYPASS CLAIMS.** The minter's claim-construction code path must make it IMPOSSIBLE to emit `role admin`, `firmRole admin`, `tier internal`, or `userType Dev` -- not "the caller happens not to pass them", but the function's own claim dict never has a code path that can set any of those four values, and a unit test asserts this by attempting to pass them in and confirming they are absent or the call is refused (your choice which, but pick one and prove it).
- **(d) MINTED ONLY FROM THE FROZEN BUNDLE, LOGGED.** The minter takes no live request context (no headers, no caller-supplied claim) -- every claim value traces to the bundle object or is freshly generated (jti, iat, exp, nbf) inside the function. Log the mint (a structured log line or return value carrying `jti` and the render id is sufficient at this offline stage) so a future caller can wire it to the estate's logging without a redesign.
- **(e) VERIFICATION.** Write a test that: mints a token from a synthetic bundle fixture; decodes it with the fixture PUBLIC key using `jose.jwt.decode` with `issuer='opal-irpt-render'`, `audience='irpt-render'`, `algorithms=['RS256']`; asserts every claim above is present with the correct value and shape (`exp - iat <= 300`, `jti` unique across two successive mints from the same bundle, `sub == 'render:' + jti`); asserts decoding with the WRONG key fails (proves the key really is separate -- decode should raise, never silently pass); asserts a token minted past its `exp` fails `jwt.decode` (uses `jose`'s own expiry check, do not hand-roll). This is JUDGMENT-adjacent evidence the CVO will read at L9 alongside `rtq-2`/`rtq-3` for the compound arms (item 7 (c), (g)); your own criterion below is mechanical (does the test suite pass), not a self-grade of the compound arm.

## DELIVERABLE
The minter module; its unit test suite, passing; the throwaway keypair fixture (never committed as anything but a TEST fixture, clearly named as such); the proof instance for THIS order.

## BOUNDS
- **NO Secrets Manager entry, NO SSM parameter, NO AWS API call of any kind, NO Lambda deploy, NO Terraform change.** This cell is code + an offline test only.
- **NO edit to `infra/aws/lambda/shared/opal_auth/`** -- that module is shared and this is a project-private minter.
- **NO edit to `_scope/resolve.py`, `_authz/enforce.py`, `portal-authorizer/index.mjs`, or `auth-validator-edge/index.mjs`** -- those are `IB-rtq-2`/`IB-rtq-3`'s surfaces, not this cell's.
- **NO wiring into the real B14 export job's call graph this round** -- write the minter as a standalone, tested module; the call-site wiring is a future cell once this and its siblings are adjudicated (avoids a half-wired call into a job this round does not touch end-to-end).
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W14-S<k>` continuing above the highest at your HEAD, appended as a NEW fenced JSON block (CRLF, UTF-8, `project`, `fabric`, `surfaced_at`, `one_line`, `grounding` AND `disposition` required, full ISO `surfaced_at`); validate every fence still parses; then keep working. Do NOT self-graduate your own filed row. Never edit this face, never widen the order.

<expected_criteria>R117-AC1</expected_criteria>
<criterion id="R117-AC1" cell_refs="IB-rtq-1"><invocation>cd deliverables/0.9.0_WK_IRPT_BCKEND~14 &amp;&amp; py -3.12 -m pytest test_render_mint.py -v</invocation><expect>all tests PASS, rc=0, output shows the claim-shape assertions, the wrong-key-fails assertion, the expiry assertion, and the admin-bypass-claim-refusal assertion each explicitly by name</expect></criterion>
**`R117-AC1` -- PASSES BY OUTPUT:** the minter's own test suite passes in full, covering claim shape (item 2), key separation (item 1), bundle-only minting (item 3), and structural admin-bypass refusal (item 2's negative clause). The result.md prints the full test output and the minted-token claim set from one concrete run for direct inspection.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtq-1.the-render-key-minter.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~14/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.21, cell `IB-rtq-1` (s.R17.1).
<owned_cells>IB-rtq-1</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS credential or IAM grant is read or exercised this round; offline only.
comp-adversary: DECLARED-NOT-APPLICABLE at this offline-build stage -- the adversarial read is the CVO's cross-cell L9, once B3/B15 also land.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R117-AC1 (mechanical -- test-suite pass; the compound acceptance arms are CVO-graded across all three round-17 cells, never self-graded here). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~14/IRPT_BCKEND.TO-IB-rtq-1.the-render-key-minter.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row for the id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND the criterion PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, the criterion's deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
</content>
