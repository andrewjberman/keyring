# TO MDPF_SECHIST.TO-SH-t22 -- round 5 SH-t-22: fwd9 filled read

<to_id>MDPF_SECHIST.TO-SH-t22</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~21</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-22` (`decompositions/MDPF_SECHIST_DECOMP_R5.md`) | **outcome_ref:** FWD-9 |
**depends_on:** EVENT: SH-t-21 read OK, then the next scheduled run (as-of 2026-10-13) and its publish

---

## WORKER FACE

### THE CELL

`SH-t-22` (FWD-9). READ ONLY, event-gated. After the scheduled run for as-of 2026-10-13 and its publish, run the check once: the gap re-request
put a non-null 2026-10-12 daily return into that run's history for each fund that was null, and the page (data_as_of 2026-10-13) serves that
fund's WTD non-null -- the same day served FILLED (the CVO's condition at PRD v0.3, CTO msg 2791).

### ACCEPTANCE

<criterion id="SH5-t22-AC1" cell_refs="SH-t-22"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R5_CHECKS/r5_fwd9_read.py filled 2026-10-12</invocation><expect>FWD9-FILLED-OK</expect></criterion>

<expected_criteria>SH5-t22-AC1</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~16:4xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the checks under
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/` or `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R5_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. Read only: no S3 or DynamoDB write, no Bloomberg call.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row (dell1 id form `<CODE>-D1-W<n>-S<k>`) and keep working.
- Client-data bounds (0.0.0_AB_MSTR~DELL1, standing): never read, search, copy or `git show` any `org/**/W73_S*_EVIDENCE.json`, commits
  1ba8eafcda / f5645bb6e9, the ADVI_COTBKF ~74 / ~66 / ~70 cottonwood manifests, the IRPT_DASHBD tie-out files, or anything under
  `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~76/`. Search only inside the paths named here.

<paths>
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~21/MDPF_SECHIST.TO-SH-t22.fwd9-filled-read.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R5.md</decomp_doc> (round 5), cell `SH-t-22`.
<owned_cells>SH-t-22</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH5-t22-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~21/MDPF_SECHIST.TO-SH-t22.fwd9-filled-read.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH5-t22-AC1`
BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE reads an existing scheduled output.
comp-iam: DECLARED-NOT-APPLICABLE dell1 read grants used in rounds 1-4 (opal-data-etfs, opal-data-portal-v2 read).
comp-adversary: RUN -- 7 of 7 round-5 criteria dry-run at the base 2026-10-09 ~16:4xZ, 7 FAIL (decomposition Battery); BLIND: live S3 contents after that read, and the worker's code before it exists.
risk: SERVED.
direct_act: true -- a read.
</preflight>

Source: CTO round-4 analysis `ledger/ROUND_ANALYSIS.round4.md` (msg 2828) section 3; PRD v0.3 (CVO sign @cc57bafcdb).
