# TO IRPT_BCKEND.TO-IB-rth-3 -- THE SEVEN TERMINAL-BY-PROOF ORDERS' STATUS WORDS FLIPPED: the round-7 close measured 7 orders terminal by a VALID proof instance at HEAD whose `<status>` WORD is not terminal, so every seat that censuses by status word gets a wrong number (the class the CTO hit in his own round-7 denominator, three projects over). BOOKKEEPING, not re-work.

<to_id>IRPT_BCKEND.TO-IB-rth-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete -- 0.9.0_WK_IRPT_BCKEND~3, 2026-09-21. R78-AC1 PASS-by-output (battery_ib_rth_3.py, token IBR78-STATUS-WORD-AND-PROOF-RESOLVER-AGREE): the resolver's proven-set for IRPT_BCKEND is exactly the same seven cells (IB-rt-6, rtf-3, rtf-4, rtf-7, rtf-10, rtf-12, rtf-14) this worker left LEFT NON-TERMINAL per the honest-word rule (CTO ruling 98990/98993) -- none flipped to `complete` (no order's own bound admits completion with a disclosed FAIL) and none to `superseded` (no later round's decomp cell names any of the seven; filed as surprise row IRPT_BCKEND-W3-S51 against the order's own contrary premise). Proof instance VALID rc=0 both unbound and --governing-order-bound. Commits: 023b4697df (the seven annotations), 7a74155d0e (the surprise row), 973e82c883 (battery+output+result), and this instance+flip.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 8 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` | **Round-7 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND7_ANALYSIS.md` @0d400d5c07 (s.4, s.8) | **Decomp cell:** `IB-rth-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.8, s.R8.1) | **outcome_ref:** records integrity

---

## IDENTITY AND WORKTREE
- **Serial:** `0.9.0_WK_IRPT_BCKEND~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-8-3` on `wk-irpt_bckend-8-3` from CLOUD HEAD; absolute path at spawn. First act: `cd`, `git rev-parse --abbrev-ref HEAD`, `test -d org && echo TREE-OK`. Repo root = the worktree.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only. Capture output to a file; never `| tail`; never `$( )`. Verify by `git log`.
- Python `py -3.12`; recursive grep/find rail-DENIED -- use Read/Grep.

## THE CELL
- **(a) MEASURE, printed with the denominator:** run the gate's OWN proof-based resolver (`.tools/surprise-row-gate.py::_open_tos_for_project('.','IRPT_BCKEND')`, or the tool that wraps it) at HEAD -- it globs BOTH roots (legacy `task_orders/` underscore + tree `task-orders/` hyphen) and applies `_proof_terminal`. Confirm the SEVEN orders it names as terminal-by-proof with a non-terminal `<status>` word: `IB-rt-6`, `rtf-3`, `rtf-4`, `rtf-7`, `rtf-10`, `rtf-12`, `rtf-14`. For EACH, read its proof instance and confirm it is VALID at HEAD (`proof-of-spec-check`) BEFORE touching the face -- a face whose proof is NOT valid is NOT flipped, it is a BLOCKING row.
- **(b) SET THE HONEST WORD PER-ORDER, ON THAT ORDER'S OWN BOUND + DISPOSITION -- NO UNIFORM WORD** (CTO ruling 98990, the NFRA_MCPINDEX W1-S1 distinction @f1c469829c; a FAIL that MEASURED differs from a FAIL that refused to run). ⛔ **ALL SEVEN carry a FAILING acceptance criterion** (rt-6 RT6-AC1 FAIL, rtf-3 R60-AC1 FAIL, rtf-4 R61-AC1 FAIL, rtf-7 R64-AC1 FAIL, rtf-10 R67-AC1 FAIL, rtf-12 R69-AC1 FAIL, rtf-14 R71-AC1 FAIL): their criteria RAN and the world FAILED them, so they are genuinely TERMINAL-by-proof but **NOT SUCCESSFUL**. TERMINAL != SUCCESSFUL, and the status enum (complete/superseded/cancelled/withdrawn) only offers words that assert one or the other. For EACH order, determine the honest word from ITS OWN bound + disposition, record the reason, change NOTHING but the `<status>` word (git diff: exactly one line per face):
  - ⛔ **`complete` is written ONLY where that order's OWN bound EXPRESSLY permits completion with a disclosed FAIL** (the OG-r-1 / R-58 shape: a deliberate flip with declared, adjudicated exclusions). ABSENT such a bound, `complete` IS REFUSED -- writing it on a failing proof launders a success that did not happen.
  - **`superseded` is written ONLY where a LATER round actually RE-CUT that cell** -- a FACT to READ (`supersedes` in the decomp, or a later order naming it), never assumed. True for some of the seven, false for others.
  - ⭐ **WHERE NEITHER IS HONEST, LEAVE THE WORD NON-TERMINAL AND RECORD THE REASON** (one line). This costs nothing: `_proof_terminal` already makes terminality correct at every gate/compile/L9, so a wrong word only buys a wrong status-word census -- and a FALSE `complete` is far worse than a stale `pending`.
  - An ISSUER-CORRECTION `pending`-with-a-reason (as rtg-3's first pass carried) is a LIVE correction, not a stale word: leave it, name it.
- **(c) VERIFY:** re-run the proof-based resolver AND a status-word census; ACCEPTANCE R78-AC1: the two counts AGREE for IRPT_BCKEND, OR the residual is EXACTLY the faces (b) left NON-TERMINAL by the honest-word rule, each NAMED with its reason. ⭐ **The cell PASSES by NAMING the residual, NEVER by flipping a failing order to `complete`.** A face flipped to `complete` on a failing proof is a FAIL of this cell, not a pass.

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
