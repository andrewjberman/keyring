# NFRA_MCPINDEX task order -- `MX-r-14` -- release MX-c-18's tags and MX-c-19's firm field (the regenerated catalog and the discover change) onto the opal-gateway host on the live ref, behind NFRA_OPLGTW's queue, then read the catalog live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-14</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-r-14</to_id>
<issued_to>0.7.0_AE_CloudOps~MI</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule. The gateway host takes one release at a time; this release queues behind whatever NFRA_OPLGTW has staged (the issuer names the live ref at the PHASE A GO).
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-r-13 pattern; never-widen halves (CTO + COO) before PHASE B, and the F1 half names the per-firm catalog visibility change.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM, S3 reads).
</preflight>

## 1. THE CELL -- `MX-r-14` (round 17; decomposition section ROUND 17)

**Start only when MX-c-18 and MX-c-19 are complete and drained AND the issuer has landed the regenerated catalog AND every NFRA_OPLGTW gateway ledger ahead in the queue reads CLOSED.** The issuer continues you with an AMENDMENT (A1) that names the live ref, the blobs and the never-widen pins; until it arrives, do nothing.

**Follow MX-r-13's order** (`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-13.depth-every-tool-release.md`, section 1 with its amendments A3 to A6, which are the pattern as it actually ran, including the re-cut):
- the live ref is read from the HOST by md5;
- the deploy tree's HEAD IS the deploy-only commit, in a NEW deploy tree, with `infra/logic/registry` in the cone;
- the ANNOUNCE carries four censuses that stay EQUAL: tools, `.env` keys, `ENABLED_INTEGRATIONS`, and MC Portal per-tool link counts (the expected link counts are named in A1);
- a fresh never-widen pair is signed on the pins;
- the label is read back before the first leg closes;
- the manifest gets `previous_deployed_commit` = the live ref and a `release_note` naming THIS release;
- the rollback is to the live ref only.

These are the differences:
1. **What ships:** exactly two files, named with their blobs in A1: `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (the 44 derived `nl_tags` marked `inferred`, and the `firm` field on 24 firm-scoped table rows) and `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py` (`_silver_answer` shows a firm-scoped row to its own firm's principals only). Nothing else.
2. **NEVER-2 ledger:** `nfra-mcpindex-r14-catalog-release`.
3. **The never-widen pair covers a catalog-row visibility change.** Before this release a firm principal sees no firm-scoped catalog row; after it, a principal of firm X sees the 24 rows whose `firm` is X and no other firm's. No data object is read by seeing a row; client data still needs the firm's data grant. The pair is the issuer's COO half and the CTO's half; the issuer names both in A1.
4. **Criteria:** `AC1` to `AC4` in section 4 (`AC2` and `AC3` are the MX-r-13 reads, run after the first leg; `AC4` is the round 17 catalog on the host).

## 2. BOUNDS

1. No change to any source file.
2. Never bare `terraform apply`; never `update-function-code`. No push.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r14-catalog-release.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/ec2/EC2_MANIFEST.json
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W35-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3,AC4</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/checks/r14.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; on the host the PARTITION sums N of N, every member valid (index rc=0), and discover reads good 3 of 3 (discover rc=0) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-r-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC3.sh; echo "exit=$?"</invocation><expect>DEPTH valid N of N; ANSWER-TIME answered measured and equal m of m, anchors 2 of 2; catalog rc=0; answer-time rc=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="MX-r-14" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round17/checks/r14.AC4.sh; echo "exit=$?"</invocation><expect>HOST CATALOG version=0.5 harvest=78 table=216 key_template=216 retired=5 rows=304 nl_tags=304 inferred=44 firm=24; the host md5 equals the tree md5; read_tool names unserved by the deployed commit: none -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/NFRA_MCPINDEX.TO-MX-r-14.round17-catalog-release.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report, and stop. After PHASE B, write the proof instance and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 17, chain tail, the MX-r-13 pattern. Held by design until `MX-c-18` and `MX-c-19` drain: the catalog is regenerated by the issuer on the merged tree with `--overlay-ref <the shipped cut>` (the Z-S118 lesson: definition lines come from the shipped source) and landed by a worker amendment (the gateway folder is lane-refused to the issuer); the depth claims are re-measured at the cut and the release must land before the daily ~13:30Z publish. Battery at the base (2026-10-15): `r14.AC1` FAIL (no entry; 18 of 18 sentinels), `r14.AC4` FAIL (host: nl_tags 260, inferred 0, firm 0, version 0.5, harvest 78, table 216); `r13.AC2` and `r13.AC3` are graded on the host AFTER the release only. Planted arms for `AC4`: `plant_r14_ac4.py` 7 of 7. R1 (the `read_tool` updates for tools OPLGTW deploys later) is HELD for an enrichment recut and a later release; it is not in this order.

<status>issued</status>
<round>17</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
