# TO IRPT_BCKEND.TO-IB-rtr-1 -- V3, THE ORIGIN MARKER + THE REAL ASSET ALLOWLIST: `render_auth.mjs`'s header injection is missing `X-Origin-Verify`, which silently defeats the whole render classification chain downstream (the resolver's branch 1 refuses UNKNOWN before the renderer branch is ever reached); the static-asset allowlist assumes a URL prefix the real portal build does not use. CVO round-17 findings `C-S200`, the V3 half of `C-S203`, `W16-S2` -- `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md` (co-committed with `REMEDIATION_v8.md` @7595037af9).

<to_id>IRPT_BCKEND.TO-IB-rtr-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~17</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete -- 0.9.0_WK_IRPT_BCKEND~17 built and committed the full deliverable (the origin-marker fix, the GET-only check, the real config-derived asset allowlist) and honestly graded R118-AC1 FAIL because its own IB-rtq-2/rtq-3-sibling suite (0.9.0_WK_IRPT_BCKEND~16's test_edge_render_delegate.mjs, outside this cell's <paths>) still asserted the old, disclosed-guess asset path (row IRPT_BCKEND-W17-S2). 2.0.0_SA_COO~B ruled the conflict under L5/L6 authority (re-pinned the one stale assertion to the real, config-verified path, commit 0ac861acf5) and independently re-verified both suites fresh at this HEAD: 14 of 14 (own suite) + 19 of 19 (sibling suite, now clean) = 33 of 33 PASS, rc=0 on both. Flipped to complete on that verification.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 18 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.17 @`4f942b7657` | **Decomp cell:** `IB-rtr-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.22, s.R18.1) | **outcome_ref:** FWD-2, FWD-11 (contrib) | **Rows:** `IRPT_BCKEND-C-S200` (this cell's own defect), `IRPT_BCKEND-C-S203` (V3 half only -- the enforcer half is `IB-rtr-3`'s), `IRPT_BCKEND-W16-S2` | **Ruling:** CTO's round-17 analysis, msg 99542, ruling R18-a | **Reference (READ-ONLY, never edited by this cell):** `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_PROBE.mjs` (the CVO's own cross-module probe that found this defect -- your fix should make its origin-marker assertion pass, not just your own new test), `IRPT_BCKEND_R17_REVIEW_20260922.md` (the full finding narrative)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~17` (first invocation). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~17;`.
- **Worktree:** the issuer creates a fresh worktree on a new branch, cut from CLOUD HEAD AFTER this order's own commit lands, and verifies THIS FILE is present in it before spawning. First act: `cd` into the worktree, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtr-1.v3-origin-marker-and-the-real-asset-allowlist.md` -- absent means STOP and file a row. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else (this order's `<paths>` grants `org/mcp/sessions/` explicitly -- round 17's `W15-S6` finding is fixed here). Repo root = the worktree; make every path below absolute by prefixing the worktree's own absolute path.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~17 <0.9.0_WK_IRPT_BCKEND~17@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`.
- **Report discipline:** your FINAL MESSAGE is the WORKER REPORT the order asks for, sent exactly once when genuinely done or genuinely STOPPED. A commit landing is not the same as your turn ending; the issuer will not remove your worktree until your actual task-notification arrives (row `IRPT_BCKEND-S117`'s lesson).
- Node via the host's `node`. Checkout the `portal/` submodule properly if you need to read its build config (`git submodule update --init portal` from the worktree root, or read it via `git show` against its pinned commit if a full checkout is heavy) -- do NOT rely on any untracked local `dist/` directory as evidence; the CVO's own review found exactly that trap (a stale unpinned dist that happened to look plausible). A recursive grep/find in Bash is rail-DENIED and a denial aborts the WHOLE call: use the Read/Grep/Glob tools and keep a gated read in its own call.

## THE CELL

- **(a) THE ORIGIN MARKER, THE ROOT CAUSE.** In `infra/aws/lambda-edge/auth-validator-edge/render_auth.mjs`, `applyRenderHeaders` currently injects `X-User-Email`/`X-User-Role`/`X-Firm-Id`/the three render markers but NEVER `X-Origin-Verify`. The human path injects `x-origin-verify: cloudfront` elsewhere in `index.mjs` (confirm the exact current line yourself -- it was `:518` at this order's cut, but line numbers drift). Add the SAME injection to `applyRenderHeaders`, matching the human path's exact shape (`request.headers["x-origin-verify"] = [{ key: "X-Origin-Verify", value: "cloudfront" }]`) -- this is the constant, never a caller-suppliable value, and it OVERWRITES any client-supplied header of that name exactly as every other injected header already does.
- **(b) TWO CONTROLS FOR (a).** A MISSING-marker control: construct a request the CURRENT (pre-fix) code would send without the marker, confirm your test correctly demonstrates the ORIGINAL bug (fails before your fix, passes after) -- do not just add a passing test, prove the regression class itself is caught. A SPOOFED-marker control: a request whose CLIENT-supplied `X-Origin-Verify` carries a wrong/absent value must still receive the VERIFIED constant on the way out, never the client's value.
- **(c) GET-ONLY, WITH A POST CONTROL.** The CVO's review found the current handler forwards a POST to an otherwise-admissible render URI. Confirm (read the code yourself) whether `evaluateRenderBranch` currently checks the HTTP method at all; if it does not, add an explicit GET-only check for the render branch (every one of the three API routes and the print route are GETs; there is no render-token POST case in this contract). Test: a POST to an otherwise-admissible render URI, with an otherwise-valid render token, is refused.
- **(d) THE REAL ASSET ALLOWLIST.** `isRenderStaticAssetUri` currently assumes every admissible static asset lives under `/investor-reporting/`. Read `portal/vite.config.ts`'s ACTUAL `base`/`build.outDir`/`build.assetsDir` configuration (or whatever Vite options control the built asset URL shape) from the submodule's real, pinned commit -- never from an untracked local build. Derive the allowlist from that authoritative source. If no pinned build manifest or unambiguous config answer exists (file a row naming EXACTLY what's missing if so), implement the NARROWEST defensible reading of the config itself -- never a blanket "any asset extension anywhere" fallback, which the CVO's review explicitly warned against. Test against the print route, the derived real asset path shape, and at least one unrelated URI that must still be refused.
- **(e) VERIFICATION.** Run your full test suite; every arm from (a)-(d) explicit and separately assertable. Re-run `IB-rtq-3`'s own 19-test suite (unedited) to confirm zero regression from your edits -- this file's own prior round-17 test suite must still pass unmodified in expectation.

## DELIVERABLE
The `X-Origin-Verify` injection fix with its two controls; the GET-only check with its POST control; the re-derived asset allowlist with its config-sourced justification and controls; confirmation the pre-existing 19-test suite still passes; the proof instance for THIS order.

## BOUNDS
- **NO Secrets Manager entry, NO SSM parameter, NO AWS API call, NO Lambda deploy, NO CloudFront distribution change.** Code + tests only.
- **NO edit to any EXISTING test's expected value** in `IB-rtq-3`'s 19-test suite -- only NEW test functions are added; every pre-existing assertion must still pass unmodified.
- **NO edit to `_scope/resolve.py`, `_authz/enforce.py`, or `portal-authorizer/index.mjs`** -- those are `IB-rtr-2`'s and `IB-rtr-3`'s surfaces.
- **NO touch to `.tools/naming-gate.py` or `lib/opal_naming.py`** -- `W16-S4` stays PARKED to its external owner. If your own edits happen to trip the same false-positive class, work around it the same non-widening way `IB-rtq-3` did (reuse an existing call-site literal rather than declaring a fresh one), and file a row rather than touching the gate.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W17-S<k>` continuing above the highest at your HEAD, appended as a NEW fenced JSON block (CRLF, UTF-8, `project`, `fabric`, `surfaced_at`, `one_line`, `grounding` AND `disposition` required, full ISO `surfaced_at`); validate every fence still parses; then keep working. Do NOT self-graduate your own filed row. Never edit this face, never widen the order.

<expected_criteria>R118-AC1</expected_criteria>
<criterion id="R118-AC1" cell_refs="IB-rtr-1"><invocation>cd deliverables/0.9.0_WK_IRPT_BCKEND~17 &amp;&amp; node --test test_v3_origin_marker_and_assets.mjs &amp;&amp; node --test ../0.9.0_WK_IRPT_BCKEND~16/test_edge_render_delegate.mjs</invocation><expect>all new tests PASS, and the pre-existing 19-test suite passes rc=0 on both -- NOTE (2.0.0_SA_COO~B, post-cut): this criterion originally required the pre-existing suite "unmodified in expectation", which proved impossible once portal/vite.config.ts was read (the suite's own asset-path assertion was a disclosed guess, row W16-S2, that this cell's real fix correctly supersedes). Ruled under L5/L6 authority: the one stale assertion was re-pinned to the real path (commit 0ac861acf5), never weakened. rc=0 on both is what this criterion actually requires now.</expect></criterion>
**`R118-AC1` -- PASSES BY OUTPUT:** the origin-marker fix (with its missing/spoofed controls), the GET-only check (with its POST control), and the re-derived asset allowlist (with its config-sourced controls) all pass, and the pre-existing 19-test suite shows zero regression. The result.md prints the full test output and quotes the exact config source used for the asset allowlist.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtr-1.v3-origin-marker-and-the-real-asset-allowlist.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~17/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/mcp/sessions/
infra/aws/lambda-edge/auth-validator-edge/
portal/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.22, cell `IB-rtr-1` (s.R18.1).
<owned_cells>IB-rtr-1</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS credential or IAM grant is read or exercised this round; offline only.
comp-adversary: DECLARED-NOT-APPLICABLE at this offline-build stage -- the adversarial read is the CVO's cross-cell L9 once IB-rtr-5's chain lands.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R118-AC1 (mechanical -- test-suite pass on this cell's own surface plus a pre-existing-suite regression check). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~17/IRPT_BCKEND.TO-IB-rtr-1.v3-origin-marker-and-the-real-asset-allowlist.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row for the id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND the criterion PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, the criterion's deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
</content>
