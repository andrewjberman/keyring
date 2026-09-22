# TO IRPT_BCKEND.TO-IB-rtj-4 -- THE SOURCE-MAP NOTE, CORRECTED: `IB-rti-2` declared true `staged_from` sources for `irpt-ycharts-generate`'s `firm_registry.json` and `settings.json` members, resolving row S34's "no blob in history" claim (row `IRPT_BCKEND-W10-S1`: both resolve to tracked blobs, CRLF-only difference from live). The entry's `_staged_from_note` field was never updated and still reads as though no source exists (row `IRPT_BCKEND-W10-S3`). This cell corrects the note only.

<to_id>IRPT_BCKEND.TO-IB-rtj-4</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~14</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-22</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B 2026-09-22 (round 10, chain C, decomp v0.14 s.R10.1) in the ONE round-10 issuance</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 10 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.15 (no addendum) | **Decomp cell:** `IB-rtj-4` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.14, s.R10.1) | **outcome_ref:** records integrity | **Row:** `IRPT_BCKEND-W10-S3`

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~14`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~14;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-10-14` on branch `wk-irpt_bckend-10-14`, cut from CLOUD HEAD AFTER this order's own commit lands, and verifies THIS FILE is present in it before spawning. First act: `cd /c/tmp/wk-irpt-10-14`, `git rev-parse --abbrev-ref HEAD`, `test -d org && test -d .tools && echo TREE-OK`, THEN confirm this file is present -- absent means STOP and file a row. Write `org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial` before anything else.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~14 <0.9.0_WK_IRPT_BCKEND~14@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only. Capture output to a file; verify by `git log`.

## THE CELL

- **(a) READ THE CURRENT NOTE.** In `infra/aws/lambda/ci/lambda-source-map.json`, find the `irpt-ycharts-generate` entry's `_staged_from_note` field and its `staged_from` array. Print both verbatim.
- **(b) CORRECT THE NOTE ONLY.** Rewrite `_staged_from_note` so it accurately states: both `firm_registry.json` and `settings.json` now have declared `staged_from` pins (name them: `firm_registry.json` -> `data/firm_registry.json` @1f54e16dfd; `settings.json` -> `infra/aws/lambda/investor-reporting/intake/settings.json` @dc5d119b84), each resolving to a tracked git blob with a CRLF-only difference from the live zip member (never claimed byte-identical to a HEAD-generated view). Do NOT touch `staged_from`, `files[]`, or any other field. Do NOT widen the entry's deployment scope. Do NOT copy any served bytes into the repo.
- **(c) VERIFY NOTHING ELSE CHANGED.** `git diff` against HEAD must show exactly one field's value changed in one JSON entry; print the diff.

## DELIVERABLE
The before/after note text; the diff; the result.md; the proof instance.

## BOUNDS
- **Exactly one field, one entry.** No other edit to `lambda-source-map.json` or any other file.
- **Surprises:** one row per failed premise / wrong path / absent capability at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W14-S<k>` starting at 1, appended as a NEW fenced JSON block (CRLF, UTF-8, `grounding` AND `disposition` required, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); validate every fence still parses; then keep working.

<expected_criteria>R104-AC1</expected_criteria>
<criterion id="R104-AC1" cell_refs="IB-rtj-4"><invocation>git diff HEAD~1 -- infra/aws/lambda/ci/lambda-source-map.json</invocation><expect>IBR104-NOTE-CORRECTED-NOTHING-ELSE-CHANGED</expect></criterion>
**`R104-AC1` -- PASSES BY OUTPUT:** the diff touches exactly one field (`_staged_from_note`) in exactly one entry (`irpt-ycharts-generate`); the new text names both members' true sources and does not claim byte-identity; every other line in the file is unchanged (denominator: 1 of 1 files changed, 1 of N lines in that file changed, N printed).

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtj-4.the-source-map-note-corrected.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/ci/lambda-source-map.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.14, cell `IB-rtj-4` (s.R10.1).
<owned_cells>IB-rtj-4</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired by this order.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM surface touched.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant. `infra/aws/lambda/ci/lambda-source-map.json` is `.owned-paths.yaml` lane `YANG_PIPELINE_DEPLOY` for a Tier-2/AE commit, but a v3 worker's write surface is exactly its order's `<paths>` (Rule 27; no lane enumerates a worker), matching the `IB-rti-2`/`W10-S2` precedent that already committed to this file under this project's grant.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R104-AC1. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~14/IRPT_BCKEND.TO-IB-rtj-4.the-source-map-note-corrected.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row, `criterion_verbatim`, `invocation`, `output_evidence`, `denominator`, `expect` from this face. Validate `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>`; rc 0 AND R104-AC1 PASS-by-output, then flip `<status>` to `complete`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, naming the criterion's deciding output line and denominator, proof-of-spec-check rc, any row filed.
</content>
