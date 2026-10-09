# TO MDPF_SECHIST.TO-SH-t11 -- round 3 SH-t-11: name key census read

<to_id>MDPF_SECHIST.TO-SH-t11</to_id>
<project>MDPF_SECHIST</project>
<issued_to>0.9.0_WK_MDPF_SECHIST~10</issued_to>
<issued_by>2.0.0_SA_COO~H1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>issued</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `SH-t-11` (`decompositions/MDPF_SECHIST_DECOMP_R3.md`) | **outcome_ref:** FWD-6 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`SH-t-11` (FWD-6). READ ONLY. The `NAME::` key census (C-IDENTITY, PRD `:98`; CRO note section 3: 5,673 of 11,361 rows on 2026-10-09).
(1) Which code writes `NAME::<label>` keys into `etf-classifications` (search the repo; candidates under
`data/black_diamond/scripts/classification/` and `infra/aws/lambda/v2_portal/_shared/`), with file:line for each writer.
(2) The live row count per writer (DynamoDB full paginated scan; attribute each `NAME::` row to a writer by the evidence you can read; an
unattributable row is counted as such, never guessed). (3) Whether any hop carries a `NAME::` key to the pull label or to gold's join
(`_strip_bbg_security`, `etf_positioning_gold.py:668-672`). Write ONE evidence file with one summary line exactly
`NAME:: rows=<r> writers=<w>`. This cell rules nothing: the key ruling is MDPF_SECCLASS's / the CTO's on this census.

### ACCEPTANCE

<criterion id="SH3-t11-AC1" cell_refs="SH-t-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/r3_evidence_line.py NAMECENSUS "org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~10/name_key_census.txt" "NAME:: rows=(?P<r>\d+) writers=(?P<w>\d+)" r=1 w=1</invocation><expect>NAMECENSUS-EVIDENCE-OK</expect></criterion>

<expected_criteria>SH3-t11-AC1</expected_criteria>

Each criterion FAILS at the base (2026-10-09 ~13:3xZ, decomposition Battery). Run each invocation from the worktree root; do not edit the
check under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/R3_CHECKS/`.

## BOUNDS

- Write only the files in `<paths>`. Read only: no S3 or DynamoDB write, no Bloomberg call.
- A new S3 address or resource name is `lib/opal_naming.py` output only; a builder refusal is a missing registry row to report, never a
  hand-typed workaround (naming-place enforcement is live on dell1).
- Anything odd outside this cell: append ONE surprise row to the project's channel and keep working.

<paths>
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~10/name_key_census.txt
org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~10/MDPF_SECHIST.TO-SH-t11.name-key-census-read.proof_of_spec.json
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECHIST/decompositions/MDPF_SECHIST_DECOMP_R3.md</decomp_doc> (round 3), cell `SH-t-11`.
<owned_cells>SH-t-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SH3-t11-AC1. Instance at `org/missions/D8/MDPF/MDPF_SECHIST/deliverables/0.9.0_WK_MDPF_SECHIST~10/MDPF_SECHIST.TO-SH-t11.name-key-census-read.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> SH3-t11-AC1`
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
