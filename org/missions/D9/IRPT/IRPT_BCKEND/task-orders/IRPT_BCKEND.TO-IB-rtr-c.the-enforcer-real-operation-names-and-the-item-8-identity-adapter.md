# TO IRPT_BCKEND.TO-IB-rtr-3 -- THE ENFORCER, REAL OPERATION NAMES + THE ITEM-8 IDENTITY ADAPTER: `RENDER_DELEGATE_OPERATIONS` names operations that do not exist in the real served vocabulary, so every real request would be refused `OBJECT_NOT_COVERED`; the delegator-identity adapter assumes subject equals advisor id and never verifies the bundle id, producing wrong grants and colliding cache keys. CVO round-17 findings `W15-S5`, the served half of `C-S203` -- `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md` (co-committed with `REMEDIATION_v8.md` @7595037af9).

<to_id>IRPT_BCKEND.TO-IB-rtr-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~19</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 18 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.17 @`4f942b7657` | **Decomp cell:** `IB-rtr-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.22, s.R18.1) | **outcome_ref:** FWD-2 (own) | **Rows:** `IRPT_BCKEND-W15-S5`, `IRPT_BCKEND-C-S203` (served half) | **Ruling:** CTO's round-17 analysis, msg 99542, ruling R18-c | **Reference (READ-ONLY, never edited by this cell):** `docs/contracts/investor-reporting/v1/routes.json` (the real published operation ids: `performance-report`, `analysis-report`, `narrative-packet` -- confirm these yourself, do not trust this citation blindly, it drifts), `infra/aws/lambda/investor-reporting/_authz/served.py` (`key_operation()`, the hyphen-to-underscore transform), `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_PROBE.py` (the CVO's own probe demonstrating both defects against the real enforcer)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~19` (first invocation). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~19;`.
- **Worktree:** the issuer creates a fresh worktree on a new branch, cut from CLOUD HEAD AFTER this order's own commit lands, and verifies THIS FILE is present in it before spawning. First act: `cd` into the worktree, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtr-3.the-enforcer-real-operation-names-and-the-item-8-identity-adapter.md` -- absent means STOP and file a row. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing the worktree's own absolute path.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~19 <0.9.0_WK_IRPT_BCKEND~19@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`.
- **Report discipline:** your FINAL MESSAGE is the WORKER REPORT the order asks for, sent exactly once when genuinely done or genuinely STOPPED. A commit landing is not the same as your turn ending; the issuer will not remove your worktree until your actual task-notification arrives (row `IRPT_BCKEND-S117`'s lesson).
- Python `py -3.12`. A recursive grep/find in Bash is rail-DENIED and a denial aborts the WHOLE call: use the Read/Grep/Glob tools and keep a gated read in its own call.

## THE CELL

- **(a) THE REAL OPERATION NAMES.** `infra/aws/lambda/investor-reporting/_authz/enforce.py`'s `RENDER_DELEGATE_OPERATIONS` (currently `("performance", "analysis_sections", "narrative")`, near line 247 -- confirm the live line yourself) must become the REAL `key_operation`-transformed served vocabulary. Read `docs/contracts/investor-reporting/v1/routes.json` yourself and confirm the three published operation ids for the three render-scoped GET routes (do not copy this order's own citation blindly -- the contract can move); run each through `served.py`'s own `key_operation()` function (import and call it, do not hand-transform) to get the exact allowed strings. Update the tuple. Test: each of the three REAL transformed operation names, run through the actual `_resolve_render_delegate` path (not a renamed fixture), is admitted when otherwise valid; a fourth, unrelated operation name is refused `OBJECT_NOT_COVERED`.
- **(b) THE DELEGATOR IDENTITY, WITHOUT THE SUBJECT-EQUALS-ADVISOR-ID ASSUMPTION.** `_resolve_render_delegate` (`enforce.py:364-447` at this order's cut -- confirm current lines) currently does `delegator_headers["x-advisor-id"] = delegator` where `delegator` is the RAW `X-Render-Delegator` subject (typically an email) -- i.e. it assumes the delegator's advisor id IS their email subject. Read how `_scope.resolve`'s own identity resolution normally maps a subject to an advisor id for an ordinary (non-render) request, and reuse THAT resolution path rather than a bare substitution -- the goal is: a delegator whose real advisor id differs from their email subject must still resolve to their REAL current grant, not an empty one. Test with a fixture human whose advisor id is genuinely different from their email address, confirming a non-empty, CORRECT intersection results (matching what that human would get resolving their own identity directly).
- **(c) THE BUNDLE ID, ACTUALLY VERIFIED.** `load_render_bundle` is currently called with only `(tenant, revision)` -- `X-Render-Bundle` is read into `trusted` (via `_scope.trusted_only`) but never passed to the loader or checked against the loader's own return. Fix: pass the bundle id to the loader call (or, if the loader's own signature is fixed at `(tenant, revision)` by a sibling's design, verify the LOADED bundle's own returned identity field matches the claimed `X-Render-Bundle` value before using its `account_ids`) -- refuse on a mismatch, the same `EMPTY_GRANT`-shaped refusal the intersection-empty case already uses. Test: a request whose claimed bundle id does NOT match the tenant+revision's real bundle is refused, never silently served against the wrong bundle's accounts.
- **(d) THE CACHE KEY, CLASS AND REVISION INCLUDED.** The fingerprint call (`_scope.fingerprint(intersection, entitlement_revision, policy, self.binding.tenant)`, `enforce.py:443` at this order's cut) must also fold in the RENDER_DELEGATE class marker and the bundle revision, so two requests with the SAME intersection but DIFFERENT revisions never produce the same cache key. Test: two render-delegate requests differing only in `X-Render-Revision`, both otherwise producing the same account intersection, must NOT collide on the resulting fingerprint/cache key.
- **(e) DO NOT REGRESS THE ALREADY-PASSING ARM.** The revocation control (a delegator whose entitlement is revoked between mint and read produces a narrower/empty intersection) already passes at `IB-rtq-2`'s cut -- confirm it still passes after your changes, unmodified in expectation.

## DELIVERABLE
The corrected `RENDER_DELEGATE_OPERATIONS` tuple with its three-name-plus-fourth-refused test; the delegator-identity fix with its differing-subject-and-advisor-id test; the bundle-id verification with its mismatch-refused test; the cache-key fix with its revision-separation test; confirmation the revocation control still passes; the proof instance for THIS order.

## BOUNDS
- **NO Secrets Manager entry, NO SSM parameter, NO AWS API call, NO Lambda deploy, NO Terraform change.** Code + tests only.
- **NO edit to any EXISTING test's expected value** in this file's own pre-existing suite (`IB-rtq-2`'s three-arm scope-algebra test, the revocation control) -- only NEW test functions are added, and the revocation control's own expected value is UNCHANGED.
- **NO edit to `_scope/resolve.py`, `render_auth.mjs`, `index.mjs`, or `portal-authorizer/index.mjs`** -- those are `IB-rtr-1`'s, `IB-rtr-2`'s and `IB-rtr-4`'s surfaces.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W19-S<k>` continuing above the highest at your HEAD, appended as a NEW fenced JSON block (CRLF, UTF-8, `project`, `fabric`, `surfaced_at`, `one_line`, `grounding` AND `disposition` required, full ISO `surfaced_at`); validate every fence still parses; then keep working. Do NOT self-graduate your own filed row. Never edit this face, never widen the order.

<expected_criteria>R118-AC3</expected_criteria>
<criterion id="R118-AC3" cell_refs="IB-rtr-3"><invocation>cd deliverables/0.9.0_WK_IRPT_BCKEND~19 &amp;&amp; py -3.12 -m pytest test_enforcer_real_operations_and_identity_adapter.py -v</invocation><expect>all tests PASS rc=0: real-operation-name admission (3) + fourth-operation refusal (1), differing-subject-advisor-id resolution (1), bundle-mismatch refusal (1), cache-key revision-separation (1), and the unmodified revocation control still passing</expect></criterion>
**`R118-AC3` -- PASSES BY OUTPUT:** the enforcer's operation allowlist matches the real served vocabulary, the delegator identity resolves correctly without the subject-equals-advisor-id shortcut, the bundle id is genuinely verified, cache keys separate by revision, and the pre-existing revocation control is unregressed. The result.md prints the full test output.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtr-3.the-enforcer-real-operation-names-and-the-item-8-identity-adapter.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~19/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/mcp/sessions/
infra/aws/lambda/investor-reporting/_authz/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.22, cell `IB-rtr-3` (s.R18.1).
<owned_cells>IB-rtr-3</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS credential or IAM grant is read or exercised this round; offline only.
comp-adversary: DECLARED-NOT-APPLICABLE at this offline-build stage -- the adversarial read is the CVO's cross-cell L9 once IB-rtr-5's chain lands.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override. `_authz/served.py` is READ-ONLY reference (you call `key_operation()`, never edit it) -- if it needs to change, that is a BLOCKING row, not an override.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R118-AC3 (mechanical -- test-suite pass on the enforcer's own surface). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~19/IRPT_BCKEND.TO-IB-rtr-3.the-enforcer-real-operation-names-and-the-item-8-identity-adapter.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row for the id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND the criterion PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, the criterion's deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
</content>
