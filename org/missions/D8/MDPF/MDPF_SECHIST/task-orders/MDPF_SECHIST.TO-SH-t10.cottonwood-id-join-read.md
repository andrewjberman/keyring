# TO MDPF_SECHIST.TO-SH-t10 -- round 3 SH-t-10: cottonwood id join read

<to_id>MDPF_SECHIST.TO-SH-t10</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~9</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-10` (`decompositions/MDPF_SECHIST_DECOMP_R3.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`SH-t-10` (FWD-2). READ ONLY. Map the 4,545 `security_id` values of
`org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv` to `etf-classifications` keys
(DynamoDB, full paginated scan; key forms `CUSIP:<id>`, bare ticker, `BBG:`, `NAME::`). Try `CUSIP:<id>` first, then any other key form
that carries the same CUSIP; never guess a neighbour. Write ONE evidence file with one summary line exactly
`matched=<m>/4545 unmapped=<u>` (m + u = 4545), the per-key-form match counts, and the unmapped ids with their source (YAHOO or
BLOOMBERG_SITE_Z). The CRO measured 234 `CUSIP:` matches on 2026-10-09; report what you measure.

### ACCEPTANCE

<criterion id="SH3-t10-AC1" cell_refs="SH-t-10"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_evidence_line.py COTJOIN "org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~9/cot_id_join.txt" "matched=(?P<m>\d+)/4545 unmapped=(?P<u>\d+)" m=234</invocation><expect>COTJOIN-EVIDENCE-OK</expect></criterion>

<expected_criteria>SH3-t10-AC1</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~13:3xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the
check under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. Read only: no S3 or DynamoDB write, no Bloomberg call.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row to the project's channel and keep working.

<paths>
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~9/cot_id_join.txt
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~9/MDPF_SECHIST.TO-SH-t10.cottonwood-id-join-read.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R3.md</decomp_doc> (round 3), cell `SH-t-10`.
<owned_cells>SH-t-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH3-t10-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~9/MDPF_SECHIST.TO-SH-t10.cottonwood-id-join-read.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH3-t10-AC1`
BEFORE the flip.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE reads an existing scheduled output.
comp-iam: DECLARED-NOT-APPLICABLE dell1 read grants used in rounds 1-2 (opal-data-etfs, opal-data-portal-v2, etf-classifications read); no new grant.
comp-adversary: RUN -- 9 of 9 round-3 criteria dry-run at the base 2026-10-09 ~13:3xZ, 9 FAIL (decomposition Battery); BLIND: live S3 and DynamoDB contents after that read, and the worker's code before it exists.
risk: LOCAL.
direct_act: true -- a read.
</preflight>

Source: CTO round-2 analysis @d0230a0dac section 2 (+ ADDENDUM 1 @678d85e071 for item 6); PRD v0.2 + ADDENDUM v0.3.
