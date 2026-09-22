# TO IRPT_BCKEND.TO-IB-rtp-1 -- C-S174 EXCLUSION WORDING, SCOPED CORRECTLY: `3.0.0_SA_CVO~B`'s round-15 review found one residual wording fault in the `IB-rtk-1` proof instance that its own hash-repair verification (round 15) did not touch: line `:23` correctly records the S3 publish pass's PUBLISHED state, but lines `:269-270` still carry an unqualified exclusion claiming "any real host/SSM/S3 action" was excluded under stubs/static reads -- true of the historical diagnostic pass, FALSE of the publish pass, which DID act on real S3 bytes with a verified readback. The CTO's round-15 analysis confirms this and authorizes exactly this narrow wording fix. No hashes are touched (already correct as of `IB-rto-1`), no code, no publish, no sign-off.

<to_id>IRPT_BCKEND.TO-IB-rtp-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~13</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B 2026-09-22 (round 16, chain A, decomp v0.20 s.R16.1) in the ONE round-16 issuance</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 16 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.15 (no addendum) | **Decomp cell:** `IB-rtp-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.20, s.R16.1) | **outcome_ref:** records integrity (no FWD directly) | **Rows:** `IRPT_BCKEND-C-S174` (the residual wording, this cell's source), `C-S197` (the CVO's own verification row, read-only context) | **Ruling:** the CTO's round-15 analysis @81338c807a, section "Round 16" | **Reference (READ-ONLY, never edited by this cell):** the `IB-rtk-1` proof instance's own line `:23` (the correct publish-state record this cell must NOT contradict, only align the exclusion text with)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~13` (ELEVENTH invocation, same serial as every prior capture-tool-chain pass -- continuity of the `deliverables/<SERIAL>/**` ownership). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~13;`.
- **Worktree:** the issuer creates a fresh worktree on a new branch, cut from CLOUD HEAD AFTER this order's own commit lands, and verifies THIS FILE is present in it before spawning. First act: `cd` into the worktree, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtp-1.the-c-s174-exclusion-wording-scoped-correctly.md` -- absent means STOP and file a row, never proceed on content read from outside the worktree. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing the worktree's own absolute path.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~13 <0.9.0_WK_IRPT_BCKEND~13@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`.
- **Report discipline:** your FINAL MESSAGE is the WORKER REPORT the order asks for, sent exactly once when your task is genuinely done or genuinely STOPPED. **Before you stop, confirm your work is genuinely complete -- a commit landing is not the same as your turn ending, and the issuer will not remove your worktree until your actual task-notification arrives (row `IRPT_BCKEND-S117`'s lesson).**
- Python `py -3.12`; Node via the host's `node`; AWS via `.tools/aws`. A recursive grep/find in Bash is rail-DENIED and a denial aborts the WHOLE call: use the Read/Grep/Glob tools and keep a gated read in its own call.

## THE CELL

- **(a) SCOPE THE EXCLUSION TO WHAT IT IS ACTUALLY TRUE OF.** In the `IB-rtk-1` proof instance (blob `f8253e60` @`6b8139682d` -- find the current file at HEAD via its committed path, do not assume the file has not moved since), read lines `:269-270` (or wherever this text now lives -- confirm the exact location yourself, line numbers can drift) carrying the unqualified exclusion "any real host/SSM/S3 action... everything under stubs/static reads". This is scoped correctly ONLY for the historical diagnostic pass and for whichever limbs remain genuinely never exercised (host start, SSM calls). It is WRONG for the S3 publish limb, which DID act on real S3 bytes with a verified readback -- read line `:23` of the same proof instance (or wherever that record now lives) to find the exact evidence citation already present there, and reuse it. Rewrite the exclusion so it names each limb's TRUE state precisely: keep the historical-diagnostic-pass exclusion for what remains genuinely unexercised (host, SSM), and explicitly state that the publish pass DID publish to S3 and DID read back, citing the existing evidence.
- **(b) DO NOT RECUT THE FIXED HASHES.** The CRLF and LF/git-object values are already correct as of `IB-rto-1`'s own fix (round 15) -- do not touch them, do not re-derive them, do not second-guess them. This cell's ENTIRE scope is the exclusion sentence's wording.
- **(c) DO NOT REPLAY THE PUBLISH.** No S3 act, no ledger entry, no new packet, no sign-off. The published bytes and their readback already happened and are already correctly recorded elsewhere in the same proof instance; this cell only corrects how the EXCLUSION text describes what was and wasn't exercised.
- **(d) DO NOT TOUCH ANY CODE.** `capture-session.cjs`, `capture-session.sh`, and `README.md` are NOT touched under any circumstance. If you find yourself wanting to, STOP and file a row instead of proceeding -- that would mean the fix needs more than wording, contradicting this cell's own scope.
- **(e) VERIFICATION.** Re-run `proof-of-spec-check.py` on the `IB-rtk-1` instance after the wording fix; VALID rc=0 required, and confirm no criterion verdict changed (this cell corrects text describing a fact, never the fact or the grade itself). Print the corrected exclusion text IN FULL in your own result.md so the CVO/CTO can verify the actual wording directly rather than trusting a paraphrase.

## DELIVERABLE
The corrected `IB-rtk-1` proof instance with the exclusion text properly scoped; `proof-of-spec-check` VALID rc=0 confirming no verdict changed; the result.md printing the full corrected text; the proof instance for THIS order.

## BOUNDS
- **NO host start or stop, NO live login, NO credential, NO MFA automation, NO network call to the portal.**
- **NO hash recomputation** (already correct), **NO code change, NO README change, NO new packet, NO S3 act, NO never-widen sign-off.** This cell is wording-only. Any temptation to touch those surfaces is a signal to STOP and file a row.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W13-S<k>` continuing above the highest at your HEAD, appended as a NEW fenced JSON block (CRLF, UTF-8, `project`, `fabric`, `surfaced_at`, `one_line`, `grounding` AND `disposition` required, full ISO `surfaced_at`); validate every fence still parses; then keep working. **Do NOT self-graduate your own filed row to a closed/GRADUATED disposition.** Never edit this face, never widen the order.

<expected_criteria>R116-AC1</expected_criteria>
<criterion id="R116-AC1" cell_refs="IB-rtp-1"><invocation>timeout 120 py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtk-1.the-capture-tool-complete-lifecycle-observer-and-sticky-refusal.md</invocation><expect>VALID (rc=0)</expect></criterion>
**`R116-AC1` -- PASSES BY OUTPUT:** the `IB-rtk-1` proof instance re-validates VALID rc=0 after the exclusion-wording correction, with no criterion verdict changed. The result.md prints the exact corrected exclusion text in full for direct verification.

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtp-1.the-c-s174-exclusion-wording-scoped-correctly.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.20, cell `IB-rtp-1` (s.R16.1).
<owned_cells>IB-rtp-1</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM grant is read or exercised by this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- wording-only, no code or infra change.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override -- and per this order's own BOUNDS, needing anything outside `deliverables/0.9.0_WK_IRPT_BCKEND~13/` is itself a signal to STOP, not to request it.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R116-AC1 (mechanical, no judgment row -- this cell is wording-only and needs no CVO grade). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtp-1.the-c-s174-exclusion-wording-scoped-correctly.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row for the id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT. Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND the criterion PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, the criterion's deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
</content>
