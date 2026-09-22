# TO IRPT_BCKEND.TO-IB-rtr-5 -- THE ONE OFFLINE ACTUAL-MODULE CHAIN, THE ONLY PROOF OF THE RENDER CONTRACT: every prior round proved its own component against its own fixtures; this cell wires the ACTUAL minter, the ACTUAL V3 branch, the ACTUAL V2 branch, the ACTUAL resolver and the ACTUAL enforcer together, with no claim-shaped stand-in for any of them, and proves the full contract end to end. PRD v0.17 CONTRACTS item 7's full (a)-(k) table except (g). CTO's round-17 analysis, msg 99542, ruling R18-e: "This cell is the only proof of the render contract."

<to_id>IRPT_BCKEND.TO-IB-rtr-5</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~21</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete -- 0.9.0_WK_IRPT_BCKEND~21: the wired offline chain test (mint.py -> V3 -> V2 -> resolve.py -> enforce.py -> served.py) passes rc=0, 3 positive fixture objects resolved (non-overlapping), 6 negative arms refused/UNKNOWN, 3 additional item-7 checks. Mechanical bar PASS; R118-AC5's wider coverage judgment is 3.0.0_SA_CVO's own L9 read, per result.md's explicit arm-by-arm mapping.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 18 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.17 @`4f942b7657` | **Decomp cell:** `IB-rtr-5` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.22, s.R18.1) | **outcome_ref:** FWD-2, FWD-3, FWD-4, FWD-8, FWD-11 (the round's own proof) | **Rows:** none yet -- this cell is the integration proof, not a defect fix | **Ruling:** CTO's round-17 analysis, msg 99542, ruling R18-e | **Reference (READ-ONLY, never edited by this cell):** `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_PROBE.py` / `.mjs` (the CVO's own cross-module probe shape -- your chain test should be the SAME kind of instrument, extended to cover every arm, never a narrower re-check), `IRPT_BCKEND_R17_REVIEW_20260922.md`, PRD `:230-241` (item 7's acceptance-arm table)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~21` (first invocation). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~21;`.
- **Worktree:** the issuer creates this worker's worktree FRESH, from CLOUD HEAD AFTER `IB-rtr-1`/`IB-rtr-2`/`IB-rtr-3` have all merged (never from the round-18 issuance commit alone -- this cell needs their landed fixes, not just their task orders). Verify THIS FILE is present, and verify all three siblings' fixes are actually present in your own worktree before starting (e.g. grep for the real operation names in `enforce.py`, the origin-marker injection in `render_auth.mjs`, the forbidden-claims check in `portal-authorizer/index.mjs` -- if any is missing, STOP and file a row, do not proceed on a partial base). Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing the worktree's own absolute path.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~21 <0.9.0_WK_IRPT_BCKEND~21@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`.
- **Report discipline:** your FINAL MESSAGE is the WORKER REPORT the order asks for, sent exactly once when genuinely done or genuinely STOPPED. A commit landing is not the same as your turn ending; the issuer will not remove your worktree until your actual task-notification arrives (row `IRPT_BCKEND-S117`'s lesson).
- Python `py -3.12` and Node via the host's `node` -- this chain crosses both languages (the minter and resolver/enforcer are Python; V2/V3 are `.mjs`). Bridge them with a small harness that shells out or uses a subprocess boundary as needed; do not fake either side. A recursive grep/find in Bash is rail-DENIED and a denial aborts the WHOLE call: use the Read/Grep/Glob tools and keep a gated read in its own call.

## THE CELL

Build ONE offline test (or a small, clearly-linked suite) that wires the REAL modules together, across THREE distinct bundle/account fixture objects (never one -- a single-object coincidence must not be able to pass silently):

- **(a) THE CHAIN.** `_render_identity/mint.py`'s `mint_render_token()` mints a real token from a fixture `ExportBundle`-shaped mapping -> the real `evaluateRenderBranch` (`render_auth.mjs`/`index.mjs`, post `IB-rtr-1`/`IB-rtr-2`) verifies it, checks the origin marker, admits it, injects real headers -> the real `authorizeRenderToken` (`portal-authorizer/index.mjs`, post `IB-rtr-2`) verifies it independently, checks the four forbidden claims, admits it -> the real `_scope.resolve`/`classify_principal`/`trusted_only` (`resolve.py`, post `IB-rtr-4`'s citation fixes) classifies the resulting header set as `RENDER_DELEGATE` -> the real `Enforcer.resolve_now`/`_resolve_render_delegate` (`enforce.py`, post `IB-rtr-3`) resolves the delegate's scope against the real operation-name vocabulary -> the real `served.py` operation-key boundary (`key_operation`) accepts the resolved operation without a `KEY_REFUSED`. Every step uses the ACTUAL function from the ACTUAL file -- no hand-rolled restatement of what a function "would do," no copied parameters standing in for a real call.
- **(b) THREE OBJECTS.** Run the full positive chain against three DIFFERENT fixture bundle/account combinations (different tenants or different account sets), confirming each produces its own correct, non-overlapping result -- proves the chain is genuinely parameterized by its real inputs, not coincidentally correct for one hardcoded case.
- **(c) THE NEGATIVES, EACH THROUGH THE SAME REAL CHAIN.** (1) a forbidden claim (pick one of the four; the others are already covered by `IB-rtr-2`'s own unit tests, this is about proving the CHAIN itself refuses, not re-proving each claim) is refused somewhere in the chain, never silently admitted; (2) an expired token is refused; (3) a swapped path id (matching `IB-rtq-2`'s/`IB-rtr-1`'s existing arm shape) is refused; (4) a wrong bundle id (per `IB-rtr-3`'s new check) is refused; (5) a fourth, unlisted operation is refused; (6) a missing render marker (the token is real and valid, but the edge-injected marker headers are absent -- simulating a request that never actually passed through the real edge) resolves `UNKNOWN`, never `RENDER_DELEGATE`.
- **(d) ITEM 7'S TABLE, (a)-(k) EXCEPT (g).** Cross-check your suite against PRD `:230-241`'s literal list; every arm except (g) (the applied-IAM-policy read, deploy-time only per the CTO's ruling 4) must be traceable to a specific test in your suite -- name which test proves which arm in your result.md, explicitly, arm by arm. Arms already covered by a sibling cell's own unit tests (e.g. the individual forbidden-claim refusals) do not need re-proving in isolation here, but the CHAIN-LEVEL version (does the fully-wired system still refuse) does.
- **(e) THIS CRITERION IS JUDGMENT-GRADED.** Your own proof instance states PASS-by-output on your test suite passing; whether the suite's COVERAGE genuinely satisfies "the full item-7 table" is the CVO's own L9 read, never self-graded here. Be exhaustive and explicit in your result.md's arm-by-arm mapping so that read is easy to check, not because your own say-so decides it.

## DELIVERABLE
The wired offline chain test, all three fixture objects, all six negative arms, an explicit result.md mapping every item-7 arm (except g) to the specific test that proves it; the proof instance for THIS order.

## BOUNDS
- **NO Secrets Manager entry, NO SSM parameter, NO AWS API call, NO Lambda deploy, NO Terraform/CloudFront change, NO key provisioning.** This is still an offline chain, wired at the function-call level, never against live infrastructure.
- **NO edit to any of the five real modules' own logic** -- this cell is a TEST that calls them, never a further fix. If you find a NEW defect while wiring the chain, do not fix it here -- file a row and keep working (the chain test should demonstrate the defect if it's real, which is itself useful L9 evidence).
- **NO edit to any sibling cell's own test file.**
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W21-S<k>` continuing above the highest at your HEAD, appended as a NEW fenced JSON block (CRLF, UTF-8, `project`, `fabric`, `surfaced_at`, `one_line`, `grounding` AND `disposition` required, full ISO `surfaced_at`); validate every fence still parses; then keep working. Do NOT self-graduate your own filed row. Never edit this face, never widen the order.

<expected_criteria>R118-AC5</expected_criteria>
<criterion id="R118-AC5" cell_refs="IB-rtr-5"><invocation>cd deliverables/0.9.0_WK_IRPT_BCKEND~21 &amp;&amp; py -3.12 test_actual_module_chain.py</invocation><expect>the full chain test PASSES: 3 positive fixture objects all correctly resolved, all 6 negative arms correctly refused/UNKNOWN, rc=0, with an explicit arm-by-arm item-7 mapping printed</expect></criterion>
**`R118-AC5` -- JUDGMENT, GRADED BY THE CVO AT L9, NEVER SELF-GRADED:** the mechanical bar (the chain test passes) is necessary but not sufficient -- whether the suite's coverage genuinely satisfies PRD item 7's full (a)-(k) table (except g) is the CVO's own read. The result.md's explicit arm-by-arm mapping is the evidence that read is built on.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtr-5.the-one-offline-actual-module-chain.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~21/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/mcp/sessions/
infra/aws/lambda/investor-reporting/_render_identity/
infra/aws/lambda/investor-reporting/_scope/
infra/aws/lambda/investor-reporting/_authz/
infra/aws/lambda-edge/auth-validator-edge/
infra/aws/users/lambda/portal-authorizer/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.22, cell `IB-rtr-5` (s.R18.1).
<owned_cells>IB-rtr-5</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS credential or IAM grant is read or exercised this round; offline only.
comp-adversary: DECLARED-NOT-APPLICABLE at this offline-build stage -- this cell IS the adversarial cross-module read, at the offline layer; a live adversarial read is deploy-time (arm g), out of scope.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face) -- listing all five real modules' directories as READ (to call their functions) though this cell's own WRITES land only in its own `deliverables/` and the surprise channel. A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R118-AC5 (JUDGMENT -- graded by 3.0.0_SA_CVO at L9, never self-graded; the mechanical test-pass bar is necessary but not the full grade). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~21/IRPT_BCKEND.TO-IB-rtr-5.the-one-offline-actual-module-chain.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row for the id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND the criterion PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, the criterion's deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why, and the explicit arm-by-arm item-7 mapping for the CVO's L9 read).
</content>
