# TO IRPT_BCKEND.TO-IB-rtr-4 -- RE-PIN CITATIONS TO ONE MERGED VINTAGE + THE V1 HARNESS: after round 17's three-way merge, `resolve.py`'s line-number citations drifted again and the real pre-existing `_scope` suite regressed by one test -- a defect invisible to any single round-17 cell's own isolated-tree tests, found only by the CVO's post-merge probe. The CTO's own ruling on `W16-S1`/`W16-S3` additionally asks for a durable baseline plus an offline V1 harness. CVO round-17 findings `W15-S1`, `W15-S2`, `W16-S1`, `W16-S3` -- `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md` (co-committed with `REMEDIATION_v8.md` @7595037af9).

<to_id>IRPT_BCKEND.TO-IB-rtr-4</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~20</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>complete -- 0.9.0_WK_IRPT_BCKEND~20 built and committed the full deliverable (every resolve.py citation re-pinned, the durable 19-test baseline confirmed unmodified, a genuine new V1-actual-module harness) and honestly graded R118-AC4 FAIL against this order's own buggy invocation text (one `../` short of repo root, row IRPT_BCKEND-W20-S1). 2.0.0_SA_COO~B re-cut the invocation text (see the criterion's own inline note) and independently re-verified all three legs at the corrected path: 29+19+4 = 52 of 52 PASS. Flipped to complete on that verification, per the worker's own final report requesting exactly this re-cut.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 18 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.17 @`4f942b7657` | **Decomp cell:** `IB-rtr-4` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.22, s.R18.1) | **outcome_ref:** records integrity (no FWD directly) | **Rows:** `IRPT_BCKEND-W15-S1`, `IRPT_BCKEND-W15-S2`, `IRPT_BCKEND-W16-S1`, `IRPT_BCKEND-W16-S3` | **Ruling:** CTO's round-17 analysis, msg 99542, rulings 1 and R18-d | **Reference (READ-ONLY, never edited by this cell):** `infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts` (V1's real `verifyAccessToken`), `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_R17_REVIEW_20260922.md` (the exact regression the CVO found)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~20` (first invocation). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~20;`.
- **Worktree:** the issuer creates a fresh worktree on a new branch, cut from CLOUD HEAD AFTER this order's own commit lands, and verifies THIS FILE is present in it before spawning. First act: `cd` into the worktree, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtr-4.re-pin-citations-to-one-merged-vintage-and-the-v1-harness.md` -- absent means STOP and file a row. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing the worktree's own absolute path.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~20 <0.9.0_WK_IRPT_BCKEND~20@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`.
- **Report discipline:** your FINAL MESSAGE is the WORKER REPORT the order asks for, sent exactly once when genuinely done or genuinely STOPPED. A commit landing is not the same as your turn ending; the issuer will not remove your worktree until your actual task-notification arrives (row `IRPT_BCKEND-S117`'s lesson).
- Python `py -3.12`, Node via the host's `node`. A recursive grep/find in Bash is rail-DENIED and a denial aborts the WHOLE call: use the Read/Grep/Glob tools and keep a gated read in its own call.

## THE CELL

- **(a) RE-PIN EVERY CITATION, FOR REAL THIS TIME.** In `infra/aws/lambda/investor-reporting/_scope/resolve.py`, `TRUSTED_HEADERS` and `RENDER_TRUSTED_HEADERS`' stored line-number citations (pointing at `auth-validator-edge/index.mjs`) have now drifted TWICE across this project's history (round 15/16's capture-tool-chain equivalent lesson, and now round 17's cross-cell merge). Confirm the ACTUAL current injection line for EVERY ONE of the nine original trusted headers plus the three render markers, at the CURRENT merged-tree HEAD (after `IB-rtr-1`'s and `IB-rtr-2`'s round-18 edits may also have landed by the time you run -- re-confirm against whatever HEAD you actually have, never a number carried from this order's own citations, which will themselves be stale by the time you read them). Do not trust ANY prior round's citation, including round 17's own "fix" -- the CVO found it wrong again within the same day. Run `test_every_trusted_header_is_actually_injected_at_the_line_it_claims` (or whatever the real pre-existing test's name is -- confirm it) BEFORE your fix to reproduce the current failure, and AFTER to confirm it passes.
- **(b) THE DURABLE BASELINE, PER RULING 1.** The 19 worker-authored tests from `IB-rtq-3` (`test_edge_render_delegate.mjs`) are the durable baseline, PINNED AT THEIR MERGED COMMIT, UNEDITED -- confirm they still pass unmodified in expectation (do not touch this file). This is not a new artifact; it is a confirmation.
- **(c) THE V1 HARNESS, ADDED ALONGSIDE, NEVER REPLACING.** Build a NEW offline test harness that invokes V1's ACTUAL `verifyAccessToken` function (`infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts`) directly -- import and call the real function, with its key-retrieval dependency faked (a test double for whatever secret/key-fetch call it makes, following the SAME pattern `IB-rtq-3`'s own V1-replication row used: read V1's real parameters, never guess). This is genuinely NEW work, not a relabeling of `IB-rtq-3`'s own replication test (which read V1's parameters and called `jsonwebtoken.verify()` directly, never V1's own function) -- this harness calls V1's OWN CODE. Test: a render-key-signed token, run through V1's actual `verifyAccessToken`, is refused (same expectation as before); a valid human token, run through the same real function, is accepted (the positive control proving the harness itself works, not just that everything gets refused).
- **(d) REPORT ISOLATED AND MERGED EVIDENCE SEPARATELY.** Your result.md must clearly distinguish: what `IB-rtq-2`/`IB-rtq-3` each measured in THEIR OWN isolated worktree (a snapshot that is now known-stale), versus what YOU measure at the current merged HEAD (the only evidence that matters going forward). Do not present isolated-worktree numbers as if they describe the current tree.

## DELIVERABLE
Every `resolve.py` citation re-pinned and confirmed against the CURRENT merged tree; confirmation the 19-test durable baseline passes unmodified; the new V1 harness with its refusal + positive-control tests; a result.md that separates isolated from merged evidence explicitly; the proof instance for THIS order.

## BOUNDS
- **NO Secrets Manager entry, NO SSM parameter, NO AWS API call, NO Lambda deploy, NO Terraform change.** Code + tests only (citation text is metadata, not behavior; the V1 harness is offline with a faked key-retrieval seam).
- **NO edit to any EXISTING test's expected value** anywhere -- this cell corrects CITATIONS (comments/metadata) and ADDS a new harness; it changes no test's PASS/FAIL semantics.
- **NO edit to `render_auth.mjs`, `index.mjs`, `_authz/enforce.py`, or `portal-authorizer/index.mjs`** -- those are `IB-rtr-1`'s, `IB-rtr-2`'s and `IB-rtr-3`'s surfaces. This cell's ONLY code-adjacent edit is `resolve.py`'s citation comments (never its logic) plus the new, separate V1-harness test file.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W20-S<k>` continuing above the highest at your HEAD, appended as a NEW fenced JSON block (CRLF, UTF-8, `project`, `fabric`, `surfaced_at`, `one_line`, `grounding` AND `disposition` required, full ISO `surfaced_at`); validate every fence still parses; then keep working. Do NOT self-graduate your own filed row. Never edit this face, never widen the order.

<expected_criteria>R118-AC4</expected_criteria>
<criterion id="R118-AC4" cell_refs="IB-rtr-4"><invocation>cd deliverables/0.9.0_WK_IRPT_BCKEND~20 &amp;&amp; py -3.12 -m pytest ../../../../../../../infra/aws/lambda/investor-reporting/_scope/tests/test_resolve.py -v &amp;&amp; node --test ../0.9.0_WK_IRPT_BCKEND~16/test_edge_render_delegate.mjs &amp;&amp; node --test test_v1_actual_module_harness.mjs</invocation><expect>the real pre-existing _scope suite passes IN FULL (the citation-drift test included), the 19-test durable baseline passes unmodified, and the new V1 harness passes both its refusal and positive-control arms -- rc=0 on all three legs</expect></criterion>
<!-- RE-CUT (round 18, 2.0.0_SA_COO~B, COO correction on row IRPT_BCKEND-W20-S1): the first leg's
relative path was one `../` short of repo root from `deliverables/0.9.0_WK_IRPT_BCKEND~20/`
(measured: 7 levels needed -- deliverables/IRPT_BCKEND/IRPT/D9/missions/org/repo-root -- this
order's own original text had 6). 0.9.0_WK_IRPT_BCKEND~20 correctly refused to touch this face
and graded R118-AC4 FAIL honestly on its own literal, buggy text; the underlying deliverable
(every resolve.py citation re-pinned, the durable 19-test baseline confirmed unmodified, and a
genuine new V1-actual-module harness) was independently re-verified by the COO with the
CORRECTED 7-level path: 29 (the real pre-existing _scope suite, citation-drift test included) +
19 (durable baseline, unmodified) + 4 (the new V1 harness, refusal and positive-control arms) =
52 of 52 PASS. -->

**`R118-AC4` -- PASSES BY OUTPUT:** every citation matches the current merged tree, the durable 19-test baseline is confirmed unregressed, and a genuine V1-actual-module harness exists and passes. The result.md separates isolated-worktree evidence from merged-tree evidence explicitly.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtr-4.re-pin-citations-to-one-merged-vintage-and-the-v1-harness.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~20/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/mcp/sessions/
infra/aws/lambda/investor-reporting/_scope/resolve.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.22, cell `IB-rtr-4` (s.R18.1).
<owned_cells>IB-rtr-4</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS credential or IAM grant is read or exercised this round; offline only.
comp-adversary: DECLARED-NOT-APPLICABLE at this offline-build stage.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face) -- note `resolve.py` is granted for CITATION EDITS ONLY, never its logic (that boundary is a discipline this order states, not a mechanical restriction the grant can enforce on its own). `auth-handler/src/jwt.ts` is READ-ONLY reference, never edited. A path you need that is not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R118-AC4 (mechanical -- three test-suite legs). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~20/IRPT_BCKEND.TO-IB-rtr-4.re-pin-citations-to-one-merged-vintage-and-the-v1-harness.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row for the id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND the criterion PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, the criterion's deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
</content>
