# TO IRPT_BCKEND.TO-IB-rto-1 -- C-S174 METADATA, PROPERLY CORRECTED: RECOMPUTE, NEVER COPY: `1.0.0_SA_CTO`'s round-14 analysis found (row `C-S196`) that this chain's own earlier `C-S174` fix (round 13's arm (f), round 14's arm (g)) itself carries two further faults: a TRANSPOSED CRLF hash value (`...03fbb20...` recorded where the true value is `...03bfb20...`) and a MISATTRIBUTED LF hash (the proof text attributes the LF/git-object value to "the worktree diagnostic", which is backwards -- a worktree read on this box's CRLF checkout produces the CRLF value, never the LF value). The capture-tool CODE line is DONE (R114-AC3 PASSED, the ask released to Andrew) -- this is a pure metadata/record-integrity correction, no code change, no publish, no S3 act.

<to_id>IRPT_BCKEND.TO-IB-rto-1</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~13</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B 2026-09-22 (round 15, chain A, decomp v0.19 s.R15.1) in the ONE round-15 issuance</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 15 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.15 (no addendum) | **Decomp cell:** `IB-rto-1` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.19, s.R15.1) | **outcome_ref:** records integrity (no FWD directly) | **Rows:** `IRPT_BCKEND-C-S196` (the CTO's own finding, this cell's source) | **Ruling:** the CTO's round-14 analysis @0782226170, section "Round 15" | **Reference (READ-ONLY, never edited by this cell):** row `IRPT_BCKEND-W13-S3` in `../surprise-channel/investigations/INVESTIGATION_v1.md` (the original CRLF-vs-LF grain finding and its hash-derivation discipline)

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~13` (TENTH invocation, same serial as every prior capture-tool-chain pass -- continuity of the `deliverables/<SERIAL>/**` ownership). Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~13;`.
- **Worktree:** the issuer creates a fresh worktree on a new branch, cut from CLOUD HEAD AFTER this order's own commit lands, and verifies THIS FILE is present in it before spawning. First act: `cd` into the worktree, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN `test -f org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rto-1.the-c-s174-metadata-recomputed-not-copied.md` -- absent means STOP and file a row, never proceed on content read from outside the worktree. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else. Repo root = the worktree; make every path below absolute by prefixing the worktree's own absolute path.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~13 <0.9.0_WK_IRPT_BCKEND~13@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only; never push/merge/rebase/`checkout --`/`clean`. Capture `safe-commit.sh` output to a file, never `| tail`, never with `$( )`; if it fails, ask `git log` whether it committed -- never read its prose. **Commit your progress FREQUENTLY, in small increments.**
- **Report discipline:** your FINAL MESSAGE is the WORKER REPORT the order asks for, sent exactly once when your task is genuinely done or genuinely STOPPED. Do not report intermediate progress as if it were final. **Before you stop, confirm your work is genuinely complete or genuinely blocked -- a commit landing is not the same as your turn ending, and the issuer will not remove your worktree until your actual task-notification arrives (row `IRPT_BCKEND-S117`'s lesson).**
- Python `py -3.12`; Node via the host's `node`; AWS via `.tools/aws`. A recursive grep/find in Bash is rail-DENIED and a denial aborts the WHOLE call: use the Read/Grep/Glob tools and keep a gated read in its own call.

## THE CELL

- **(a) RECOMPUTE, NEVER COPY.** Derive both hash values FRESH, from the actual bytes, using the same instruments row `W13-S3` established: the CRLF/checkout-grain value from a RAW working-tree read of `infra/aws/ec2/investor-reporting-export/capture-session.cjs` on THIS box (e.g. `sha256sum infra/aws/ec2/investor-reporting-export/capture-session.cjs` against the actual checked-out file -- at whatever commit the original `IB-rtk-1` fourth-pass repair introduced the value this metadata describes; read the existing `C-S174` text first to identify WHICH commit/blob the citation is about, then recompute against that exact commit, not against HEAD); the LF/git-object value via `git cat-file -p <blob> | sha256sum`, CROSS-CHECKED with `git show <commit>:<path> | sha256sum`, both must agree. **Do not copy either value from this order's own citations above, from any prior commit message, or from any existing row text, even where it looks correct -- recompute from scratch and let the recomputed value be the one you write.** Print both freshly-derived values in your own commit message and result.md, with the exact commands you ran.
- **(b) CORRECT THE TRANSPOSED CRLF VALUE.** First locate every place this chain's own `C-S174` fix wrote the CRLF value (start with the `IB-rtm-1` proof instance's `controls.mutant.observed` field or equivalent, `battery_ib_rtm_1.py`'s source, and any result.md prose from commits `1914e80595`, `f9c83f851f`, and `188a483e37`; use the Grep tool, never raw grep in Bash, to find every occurrence of any substring of the WRONG value `03fbb20` across the worker's own deliverables directory). Wherever the transposed `...03fbb20...` form appears, replace it with your freshly-recomputed correct form from arm (a). **A partial fix that corrects one location and misses a sibling copy is not acceptable** -- enumerate every hit before editing, then verify zero hits for the wrong substring remain afterward.
- **(c) CORRECT THE MISATTRIBUTED LF HASH.** Wherever the proof or its prose attributes the LF/git-object hash value to "the worktree diagnostic" or any language implying a raw/checkout-grain read produced it, correct the attribution: the LF/git-object value is what `git cat-file -p`/`git show` produce, NEVER a raw working-tree read on this box (which produces the CRLF value instead, per row `W13-S3`'s own finding -- restate that finding correctly here, do not repeat the inversion).
- **(d) ADD A RUN-TIME RECOMPUTATION CONTROL.** Extend `battery_ib_rtm_1.py`'s `--arm metadata` check (or add a new check within that same arm) so it FAILS if either the stored CRLF value or the stored LF/git-object value differs from a FRESH recomputation performed AT BATTERY RUN TIME (not read from a constant the battery script itself hardcodes as a comparison target copied from the proof -- the control must independently regenerate both values from the actual bytes each time it runs). This makes a future silent copy-paste drift into this exact class of error a battery FAILURE, not something only caught by a later manual review.
- **(e) VERIFICATION.** Run the widened `battery_ib_rtm_1.py --arm metadata` and confirm it PASSES with the corrected values AND that the new recomputation control genuinely exercised (print evidence the control actually ran a fresh computation and compared it -- not merely that the stored values happen to look right). Re-run `proof-of-spec-check.py` on every proof instance this cell touches (at minimum the `IB-rtm-1` instance); VALID rc=0 required on each.
- **(f) NO PUBLISH REPLAY, NO CODE CHANGE, NO PACKET, NO SIGN-OFF.** This cell touches ONLY metadata/documentation/proof text and `battery_ib_rtm_1.py`'s own check logic. `capture-session.cjs`, `capture-session.sh`, and `README.md` are NOT touched. No new never-widen packet. No S3 act. If you find yourself wanting to touch any of those files, STOP and file a row -- that would mean the fix requires more than metadata, which contradicts this cell's own scope and needs issuer re-scoping, not silent widening.

## DELIVERABLE
Both freshly-recomputed hash values, printed with the exact derivation commands; the corrected `IB-rtm-1` proof instance (or wherever `C-S174`'s text lives); the widened `battery_ib_rtm_1.py` with the new run-time recomputation control; the battery's own passing output showing the control genuinely ran; `proof-of-spec-check` VALID rc=0 on every touched instance; the result.md; the proof instance for THIS order.

## BOUNDS
- **NO host start or stop, NO live login, NO credential, NO MFA automation, NO network call to the portal.**
- **NO code change to `capture-session.cjs`/`.sh`, NO README change, NO new packet, NO S3 act, NO never-widen sign-off.** This cell is metadata-only. Any temptation to touch those files is a signal to STOP and file a row, not to proceed.
- **Hash instrument discipline:** every blob hash you cite is derived from the git OBJECT (`git cat-file -p` or `git show <ref>:<path>`); every CRLF/checkout value is derived from an ACTUAL raw working-tree read on THIS box, never assumed or copied (row `W13-S3`).
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W13-S<k>` continuing above the highest at your HEAD, appended as a NEW fenced JSON block (CRLF, UTF-8, `project`, `fabric`, `surfaced_at`, `one_line`, `grounding` AND `disposition` required, full ISO `surfaced_at`); validate every fence still parses; then keep working. **Do NOT self-graduate your own filed row to a closed/GRADUATED disposition.** Never edit this face, never widen the order.

<expected_criteria>R115-AC1, R115-AC2</expected_criteria>
<criterion id="R115-AC1" cell_refs="IB-rto-1"><invocation>timeout 300 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/battery_ib_rtm_1.py --arm metadata</invocation><expect>IBR115-C174-RECOMPUTED-NO-TRANSPOSITION-NO-MISATTRIBUTION</expect></criterion>
**`R115-AC1` -- PASSES BY OUTPUT:** the widened metadata arm prints both freshly-recomputed values, confirms zero remaining occurrences of the wrong transposed substring `03fbb20` anywhere in the worker's own deliverables, confirms the LF/git-object attribution now correctly names `git cat-file -p`/`git show` (never "the worktree diagnostic") as the value's source, and demonstrates the new run-time recomputation control genuinely re-derives both values at run time and compares them (not a hardcoded constant comparison).

<criterion id="R115-AC2" cell_refs="IB-rto-1"><invocation>timeout 120 py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rtm-1.the-capture-tool-typed-error-classification-and-truthful-cleanup-report.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtm-1.the-capture-tool-typed-error-classification-and-truthful-cleanup-report.md</invocation><expect>VALID (rc=0)</expect></criterion>
**`R115-AC2` -- PASSES BY OUTPUT:** the `IB-rtm-1` proof instance, after this cell's metadata corrections, re-validates VALID rc=0 -- the correction did not break the instance's own structural/alignment checks, and no criterion verdict changed (this cell corrects HOW a fact was described, never WHAT was found).

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rto-1.the-c-s174-metadata-recomputed-not-copied.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.19, cell `IB-rto-1` (s.R15.1).
<owned_cells>IB-rto-1</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM grant is read or exercised by this cell.
comp-adversary: DECLARED-NOT-APPLICABLE -- metadata-only, no code or infra change.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override -- and per this order's own BOUNDS, needing `infra/aws/ec2/investor-reporting-export/` at all is itself a signal to STOP, not to request it.
</preflight>

<proof_of_spec>
Criterion ids minted at cut: R115-AC1, R115-AC2 (both mechanical, no judgment row -- this cell is metadata-only and needs no CVO grade). Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~13/IRPT_BCKEND.TO-IB-rto-1.the-c-s174-metadata-recomputed-not-copied.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hashes PINNED TO THE COMMIT THAT CARRIED EACH ARTIFACT (git-object-derived, never a raw working-tree read, EXCEPT where this order's own arm (a) explicitly calls for a raw working-tree read as the CRLF-grain instrument itself -- that one exception is the cell's own subject matter, not a violation of R-40's general discipline). Validate with `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>` BEFORE any `complete` flip; rc 0 AND both criteria PASS-by-output, then flip `<status>` to `complete` and commit instance and flip together.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
</content>