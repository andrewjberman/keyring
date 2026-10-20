# TO-AR-g-177 -- the Opal thread integration test stops asserting the NOT_IN_THIS_VERSION sections that AR-y-408 removed from the document

<to_id>IRPT_ANLREQ.TO-AR-g-177</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~333</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-177` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** none. Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~333`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-333` (branch `wk-IRPT_ANLREQ-333`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~333 <0.9.0_WK_IRPT_ANLREQ~333@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W333-S<k>` (check the channel file for `W333` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `-m pytest --color=no -q -p no:cacheprovider` (read it if it is a file; you cannot edit it). It computes every expected value itself, independent of your work: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-177`, inlined)

**What this cell is.** One stale assertion in one test file. AR-y-408 made the Opal producer drop every NOT_IN_THIS_VERSION entry from the report document, so the served report (the sections the reader returns) carries no section with that reason. The integration test still asserts the old behaviour and FAILS on trunk.

In `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_opal_thread_integration.py`, function `test_opal_thread_ready_end_to_end`, replace the ONE line

    assert {s["reason"] for s in answer["sections"] if s["status"] == "NOT_AVAILABLE"} >= {"NOT_IN_THIS_VERSION"}

by exactly these three lines (same indentation):

    # AR-y-408: a NOT_IN_THIS_VERSION entry has no report section; every NOT_AVAILABLE section left states a different reason
    reasons = {s["reason"] for s in answer["sections"] if s["status"] == "NOT_AVAILABLE"}
    assert reasons and "NOT_IN_THIS_VERSION" not in reasons

Change nothing else in the file and touch no other test. Run from `infra/aws/lambda/investor-reporting`: `python -m pytest --color=no -q -p no:cacheprovider ycharts/generate/tests/test_opal_thread_integration.py` (3 passed) and `python -m ruff check ycharts/generate/tests/test_opal_thread_integration.py`. Do not fix any other failing test you see; the issuer has the baseline.

Steps: 1. Edit and run. 2. Commit that file alone. 3. Run the two criteria below. 4. Write the proof instance (shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json`), validate with `python .tools/proof-of-spec-check.py <instance> AR177-g-AC1,AR177-g-AC2`, commit it, and flip the order's `<status>` to `complete` (commit alone) only on VALID and both PASS.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR177-g-AC1" cell_refs="AR-g-177"><invocation>python -m pytest --color=no -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_opal_thread_integration.py</invocation><expect>3 passed</expect></criterion>

<criterion id="AR177-g-AC2" cell_refs="AR-g-177"><invocation>python -m pytest --color=no -q -p no:cacheprovider infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_producer_not_in_this_version.py</invocation><expect>passed</expect></criterion>

<expected_criteria>AR177-g-AC1,AR177-g-AC2</expected_criteria>

- AC1: the Opal thread integration file passes. At base it FAILs (1 failed, 2 passed).
- AC2: AR-y-408's own test of the document still passes. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_opal_thread_integration.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~333/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-177.stale-thread-test-assertion-after-ar-y-408.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-177`.
<owned_cells>AR-g-177</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR177-g-AC1,AR177-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~333/IRPT_ANLREQ.TO-AR-g-177.stale-thread-test-assertion-after-ar-y-408.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-177`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR177-g-AC1,AR177-g-AC2` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- a test file only; no product code, no resident package member.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: AC1 FAIL at base (1 failed, 2 passed), AC2 PASS at base. Trap: weakening the assertion until it passes for any input; the new lines still require NOT_AVAILABLE sections to exist and to carry reasons.
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1 FAILs, AC2 PASSes.
