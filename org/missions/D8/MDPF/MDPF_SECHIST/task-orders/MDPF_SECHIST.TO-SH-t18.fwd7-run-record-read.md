# TO MDPF_SECHIST.TO-SH-t18 -- round 4 SH-t-18: fwd7 run record read

<to_id>MDPF_SECHIST.TO-SH-t18</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~17</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-18` (`decompositions/MDPF_SECHIST_DECOMP_R4.md`) | **outcome_ref:** FWD-7 |
**depends_on:** EVENT: the 2026-10-12 07:00 ET scheduled pull and its manifest

---

## WORKER FACE

### THE CELL

`SH-t-18` (FWD-7). READ ONLY, event-gated; replaces the carried TO-SH-t12. After the 2026-10-12 07:00 ET (11:00Z) scheduled pull writes
its manifest (as-of 2026-10-09), run the check once: `history_backfill_budget` carries SH-t-4's `spent_after` and `remainder`, non-null with
`remainder == max(limit - spent_after, 0)` when a backfill drew rows. This is leg L3 of ledger `mdpf-sechist-sh-t4-sitez-run-record-20261009`;
the ledger close is the issuer's.

### ACCEPTANCE

<criterion id="SH4-t18-AC1" cell_refs="SH-t-18"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_fwd7_read.py</invocation><expect>FWD7-READ-OK</expect></criterion>

<expected_criteria>SH4-t18-AC1</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~15:4xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the
check under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. Read only: no S3 or DynamoDB write, no Bloomberg call.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row (dell1 id form `<CODE>-D1-W<n>-S<k>`) and keep working.

<paths>
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~17/MDPF_SECHIST.TO-SH-t18.fwd7-run-record-read.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R4.md</decomp_doc> (round 4), cell `SH-t-18`.
<owned_cells>SH-t-18</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH4-t18-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~17/MDPF_SECHIST.TO-SH-t18.fwd7-run-record-read.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH4-t18-AC1`
BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE reads an existing scheduled output.
comp-iam: DECLARED-NOT-APPLICABLE dell1 read grants used in rounds 1-3 (opal-data-etfs read).
comp-adversary: RUN -- 5 of 5 round-4 criteria dry-run at the base 2026-10-09 ~15:4xZ, 5 FAIL (decomposition Battery); BLIND: live S3 contents after that read, and the worker's code before it exists.
risk: SERVED.
direct_act: true -- a read.
</preflight>

Source: CTO round-3 analysis (msg 2675) section 3; PRD v0.2 + ADDENDUM v0.3.
