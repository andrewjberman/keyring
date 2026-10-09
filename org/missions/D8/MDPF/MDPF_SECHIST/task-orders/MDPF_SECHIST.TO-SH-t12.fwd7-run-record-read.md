# TO MDPF_SECHIST.TO-SH-t12 -- round 3 SH-t-12: fwd7 run record read

<to_id>MDPF_SECHIST.TO-SH-t12</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~11</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>carried</status>
<direct_act>true</direct_act>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-12` (`decompositions/MDPF_SECHIST_DECOMP_R3.md`) | **outcome_ref:** FWD-7 |
**depends_on:** EVENT: the 2026-10-12 07:00 ET scheduled pull (the first with SH-t-4 at site Z) and its manifest

---

## WORKER FACE

### THE CELL

`SH-t-12` (FWD-7). READ ONLY, event-gated. After the 2026-10-12 07:00 ET (11:00Z) scheduled pull writes its manifest (as-of 2026-10-09),
run the check once. It requires `history_backfill_budget` to carry SH-t-4's `spent_after` and `remainder` keys, non-null with
`remainder == max(limit - spent_after, 0)` when a backfill drew rows. This is leg L3 of ledger
`mdpf-sechist-sh-t4-sitez-run-record-20261009`; the ledger close is the issuer's. A `no-scheduled-manifest-since` result before the
fire is expected; the issuer spawns this worker after the fire.

### ACCEPTANCE

<criterion id="SH3-t12-AC1" cell_refs="SH-t-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_fwd7_read.py</invocation><expect>FWD7-READ-OK</expect></criterion>

<expected_criteria>SH3-t12-AC1</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~13:3xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the
check under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. Read only: no S3 or DynamoDB write, no Bloomberg call.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row to the project's channel and keep working.

<paths>
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~11/MDPF_SECHIST.TO-SH-t12.fwd7-run-record-read.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R3.md</decomp_doc> (round 3), cell `SH-t-12`.
<owned_cells>SH-t-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH3-t12-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~11/MDPF_SECHIST.TO-SH-t12.fwd7-run-record-read.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH3-t12-AC1`
BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE reads an existing scheduled output.
comp-iam: DECLARED-NOT-APPLICABLE dell1 read grants used in rounds 1-2 (opal-data-etfs, opal-data-portal-v2, etf-classifications read); no new grant.
comp-adversary: RUN -- 9 of 9 round-3 criteria dry-run at the base 2026-10-09 ~13:3xZ, 9 FAIL (decomposition Battery); BLIND: live S3 and DynamoDB contents after that read, and the worker's code before it exists.
risk: SERVED -- graded on the served artifact.
direct_act: true -- a read.
</preflight>

Source: CTO round-2 analysis @d0230a0dac section 2 (+ ADDENDUM 1 @678d85e071 for item 6); PRD v0.2 + ADDENDUM v0.3.

<carried>
Carried to round 4 by the issuer (2.0.0_SA_COO~H1, 2026-10-09 ~15:3xZ) on the CTO fold of UB-20261009T151512Z-64ce
(org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_UNBLOCK_SECHIST_64CE_CLOSE_ROUND3_NOW_20261009.md, msg 2665). Replacement: round 4's
dated read of the 2026-10-12 07:00 ET (11:00Z) scheduled pull for FWD-7 (spent_after / remainder), same check
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_fwd7_read.py. No worker was spawned on this order.
</carried>
