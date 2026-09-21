# TO IRPT_BCKEND.TO-IB-rth-3 -- THE SEVEN TERMINAL-BY-PROOF ORDERS' STATUS WORDS FLIPPED: the round-7 close measured 7 orders terminal by a VALID proof instance at HEAD whose `<status>` WORD is not terminal, so every seat that censuses by status word gets a wrong number (the class the CTO hit in his own round-7 denominator, three projects over). BOOKKEEPING, not re-work.

<to_id>IRPT_BCKEND.TO-IB-rth-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>pending -- HANDED by 2.0.0_SA_COO~B 2026-09-21 (round 8, recut on the CTO's round-7 analysis @0d400d5c07). Records-only: no source, no build, no deploy, no served change.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 8 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` | **Round-7 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND7_ANALYSIS.md` @0d400d5c07 (s.4, s.8) | **Decomp cell:** `IB-rth-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.8, s.R8.1) | **outcome_ref:** records integrity

---

## IDENTITY AND WORKTREE
- **Serial:** `0.9.0_WK_IRPT_BCKEND~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-8-3` on `wk-irpt_bckend-8-3` from CLOUD HEAD; absolute path at spawn. First act: `cd`, `git rev-parse --abbrev-ref HEAD`, `test -d org && echo TREE-OK`. Repo root = the worktree.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only. Capture output to a file; never `| tail`; never `$( )`. Verify by `git log`.
- Python `py -3.12`; recursive grep/find rail-DENIED -- use Read/Grep.

## THE CELL
- **(a) MEASURE, printed with the denominator:** run the gate's OWN proof-based resolver (`.tools/surprise-row-gate.py::_open_tos_for_project('.','IRPT_BCKEND')`, or the tool that wraps it) at HEAD -- it globs BOTH roots (legacy `task_orders/` underscore + tree `task-orders/` hyphen) and applies `_proof_terminal`. Confirm the SEVEN orders it names as terminal-by-proof with a non-terminal `<status>` word: `IB-rt-6`, `rtf-3`, `rtf-4`, `rtf-7`, `rtf-10`, `rtf-12`, `rtf-14`. For EACH, read its proof instance and confirm it is VALID at HEAD (`proof-of-spec-check`) BEFORE touching the face -- a face whose proof is NOT valid is NOT flipped, it is a BLOCKING row.
- **(b) FLIP, changing NOTHING but the `<status>` word:** for each of the seven whose proof is VALID, edit ONLY its `<status>` field's leading word to a terminal value, appending a one-line note `terminal-by-proof at HEAD, proof <path> VALID rc=0, status-word flipped by IB-rth-3 (bookkeeping, round 8)`. Do NOT change any other field, criterion, or byte. If a face carries an ISSUER-CORRECTION status (a deliberate `pending` with a reason, as rtg-3's first pass did), that is NOT a stale word -- it is a live correction; leave it and row it.
- **(c) VERIFY:** re-run the proof-based resolver AND a status-word census; ACCEPTANCE R78-AC1: the two counts AGREE for IRPT_BCKEND (0 terminal-by-proof-but-status-non-terminal remain, or the residual is exactly the ISSUER-CORRECTION faces, named).

## DELIVERABLE
the seven `<status>` flips (each its own or one commit); `battery_ib_rth_3.py` (the before/after count check) + output; the result.md naming the seven + any left un-flipped with reason; the proof instance.

## BOUNDS
- Records-only: NO source, build, deploy, apply, or served change. ONLY the `<status>` word of the named seven (and only those VALID at HEAD). A face not in the seven is not touched.
- S56 vintage pins; R-40 (the resolver run's output pinned to its commit).
- **Surprises:** one row per failed premise / wrong path at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W3-S<k>` continuing above the highest at your HEAD (append INSIDE the first fence, PREVAILING EOL, UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); then keep working. Never widen; never fix a neighbour.

<expected_criteria>R78-AC1</expected_criteria>
<criterion id="R78-AC1" cell_refs="IB-rth-3"><invocation>timeout 600 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_rth_3.py</invocation><expect>IBR78-STATUS-WORD-AND-PROOF-RESOLVER-AGREE</expect></criterion>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.8, cell `IB-rth-3` (s.R8.1).
<owned_cells>IB-rth-3</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- records-only, no AWS.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). The seven faces live under `task-orders/`, which is granted. A path not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R78-AC1 (the status-word census and the proof-based resolver agree for IRPT_BCKEND, or the residual is exactly the named ISSUER-CORRECTION faces). Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-rth-3.the-seven-terminal-by-proof-orders-status-words-flipped.proof_of_spec.json` per `org/standards/PROOF_OF_SPEC.schema.json`: `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hash of the resolver run pinned to its commit. Validate `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>`; rc 0 AND R78-AC1 PASS-by-output, then flip `<status>` complete. A FAIL row leaves it open.
</proof_of_spec>
