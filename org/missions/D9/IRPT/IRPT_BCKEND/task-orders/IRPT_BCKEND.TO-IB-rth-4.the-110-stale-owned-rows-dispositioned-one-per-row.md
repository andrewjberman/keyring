# TO IRPT_BCKEND.TO-IB-rth-4 -- THE 110 STALE OWNED ROWS, DISPOSITIONED ONE PER ROW: the round-7 gate disclosed nine times (NOT as a refusal) that 110 OPEN, owned remediation rows under IRPT_BCKEND have not moved for 2+ rounds and named the remedy itself -- "clearing them needs its own cell with an owner." A disclosure with no owner is how 110 becomes 130. The CTO's L10 rules this a round-8 cell owned by 2.0.0_SA_COO~B as issuer, output a DISPOSITION-PER-ROW.

<to_id>IRPT_BCKEND.TO-IB-rth-4</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~4</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-21</issued_date>
<status>complete -- 0.9.0_WK_IRPT_BCKEND~4, 2026-09-21. R79-AC1 PASS-by-output (battery_ib_rth_4.py, token IBR79-EVERY-ROW-DISPOSITIONED-COUNTS-SUM-TO-DENOMINATOR): the gate's own resolver (srg._stale_open_row, current_round=8) RE-MEASURED the denominator at 150 (not the inherited, already-stale 110 -- confirmed the same instrument reproduces 110 exactly at current_round=7). All 150 dispositioned CARRIED (0 DISARMED, 0 STAYS-ARMED), owner extracted per-row from each row's own disarm.owner/remediation.owner schema field (113 -> 2.0.0_SA_COO~B, 37 -> 1.0.0_SA_CTO), never a bulk or age-based close. Proof instance VALID rc=0 both unbound and --governing-order-bound. Commit: b30017444a (build/battery/record/result) and this instance+flip.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 8 | **PRD:** `../prd/IRPT_BCKEND_PRD.md` | **Round-7 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND7_ANALYSIS.md` @0d400d5c07 (s.6) | **Decomp cell:** `IB-rth-4` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.8, s.R8.1) | **outcome_ref:** channel hygiene

---

## IDENTITY AND WORKTREE
- **Serial:** `0.9.0_WK_IRPT_BCKEND~4`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~4;`.
- **Worktree:** the issuer creates `/c/tmp/wk-irpt-8-4` on `wk-irpt_bckend-8-4` from CLOUD HEAD; absolute path at spawn. First act: `cd`, `git rev-parse --abbrev-ref HEAD`, `test -d org && echo TREE-OK`. Repo root = the worktree.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~4 <0.9.0_WK_IRPT_BCKEND~4@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` by the Write tool. Branch only. Capture output to a file; never `| tail`; never `$( )`. Verify by `git log`. ⛔ The channel file is APPEND-ONLY and shared; edit IN the worktree where you commit, union any drain conflict.
- Python `py -3.12`; recursive grep/find rail-DENIED -- use `comp-surprise` and Read/Grep.

## THE CELL
- **(a) ENUMERATE, printed with the denominator:** `comp-surprise --project IRPT_BCKEND --json` (both roots) -> the OPEN, owned remediation rows that have not moved for 2+ rounds. PRINT the count (the gate said 110; RE-MEASURE it -- do not inherit 110; a handed count is perishable) and the exact id set. This id set is the cell's denominator and every later count is `N of <denominator>`.
- **(b) DISPOSITION EACH ROW ON ITS OWN EVIDENCE -- one at a time, never a sweep:** for each id, read the row and the artifact it names, and decide ONE of:
  - **DISARM** -- only with EVIDENCE the hazard is resolved (a later row, a commit, a live measurement that the row's own signature no longer fires); cite the evidence `path:line @ <commit-ish>` or the live read. Write the disarm as a LATER remediation row under the row's `disarm_owner` discipline, never an in-place mutation.
  - **STAYS ARMED** -- if the hazard is still live or the evidence is absent; say WHY in one line. A still-live row STAYS live; this cell does not make it disappear.
  - ⛔ **NO ROW IS CLOSED BY AGE.** "Has not moved for 2 rounds" is a STALENESS signal about the PROCESS, never evidence about the HAZARD (the label-vs-evidence inversion). A row disarmed must carry hazard evidence, not a date.
  - ⛔ **A row whose disposition needs another seat's authority** (a REMEDIATION only the CVO can write, an act only the CTO can rule) is NOT forced -- it is recorded as CARRY with the owner named.
- **(c) REPORT, printed:** the DENOMINATOR, and the per-disposition counts -- DISARMED `x of N` (each with its evidence), STAYS-ARMED `y of N` (each with its reason), CARRIED `z of N` (each with its owner), `x+y+z == N`. ACCEPTANCE R79-AC1: every row in the denominator has exactly one disposition with its own evidence/reason/owner, and the printed counts sum to the denominator.

## DELIVERABLE
`battery_ib_rth_4.py` (or a disposition script) + its output; the disposition RECORD (denominator, the per-row table, per-disposition counts) in `deliverables/0.9.0_WK_IRPT_BCKEND~4/`; the disarm rows written to the channel where evidence supports; the result.md; the proof instance.

## BOUNDS
- Records-only: NO source, build, deploy, or served change. NO bulk close; NO age-close; each row on its OWN evidence. A row needing another seat's authority is CARRIED with the owner, not forced.
- S56 vintage pins on every cited disarm evidence; R-40 (the enumeration run pinned to its commit); the disarm-row schema (CLOSED; `disarm_owner` a seat serial; full ISO `surfaced_at`; no `HH:0xZ`).
- **Surprises (the cell's OWN off-task finds, distinct from the rows it dispositions):** one row at `../surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W4-S<k>` continuing above the highest at your HEAD (append INSIDE the first fence, PREVAILING EOL, UTF-8 explicit, full ISO `surfaced_at`, `disarm_owner` a SEAT SERIAL when ARMED); then keep working. Never widen; never fix a neighbour.

<expected_criteria>R79-AC1</expected_criteria>
<criterion id="R79-AC1" cell_refs="IB-rth-4"><invocation>timeout 1800 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/battery_ib_rth_4.py</invocation><expect>IBR79-EVERY-ROW-DISPOSITIONED-COUNTS-SUM-TO-DENOMINATOR</expect></criterion>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rth-4.the-110-stale-owned-rows-dispositioned-one-per-row.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/remediations/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.8, cell `IB-rth-4` (s.R8.1).
<owned_cells>IB-rth-4</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- records-only, no AWS.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut.
lane: the `<paths>` block above IS the grant plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). The remediation dir is granted so the cell can write disarm rows; the investigations file for the cell's own surprises. A path not listed is a BLOCKING row, never an override.
</preflight>

<proof_of_spec>
Criterion id minted at cut: R79-AC1 (every row in the re-measured denominator carries exactly one disposition -- DISARMED with evidence / STAYS-ARMED with reason / CARRIED with owner -- and the per-disposition counts sum to the denominator). Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~4/IRPT_BCKEND.TO-IB-rth-4.the-110-stale-owned-rows-dispositioned-one-per-row.proof_of_spec.json` per `org/standards/PROOF_OF_SPEC.schema.json`: `criterion_verbatim`, `invocation`, `output_evidence`, `denominator` beside every count, `expect` from this face, R-40 content hash of the enumeration run pinned to its commit. Validate `py -3.12 .tools/proof-of-spec-check.py <instance> --governing-order <this face path>`; rc 0 AND R79-AC1 PASS-by-output, then flip `<status>` complete. A FAIL/incomplete row leaves it open.
</proof_of_spec>
