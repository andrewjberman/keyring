# NFRA_MCPINDEX task order -- `MX-r-15` -- release the round 18 catalog (C-GROUP on every row and tool, the 12 Schwab dim rows, the vendor and firm labels, curated tags) onto the opal-gateway host on the live ref, then read it live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-15</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-r-15</to_id>
<issued_to>0.7.0_AE_CloudOps~MI</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule. The gateway host takes one release at a time; this release queues behind whatever NFRA_OPLGTW has staged (the issuer names the live ref at the PHASE A GO).
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-r-14 pattern; never-widen halves (CTO + COO) before PHASE B, and the pair names the rows that become visible to their own firm.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM, S3 reads).
</preflight>

## 1. THE CELL -- `MX-r-15` (round 18, release workstream; decomposition section ROUND 18)

**Start only when the issuer's amendment A1 reaches you.** A1 names the live ref, the catalog blob, the never-widen pins and the expected censuses. The catalog is emitted by the issuer after BOTH workstreams' cells (`MX-c-21` to `MX-c-23` and `2.0.0_SA_COO~MI2`'s RESEARCH cells) are drained, against the live ref's tool definitions, with depth and freshness re-read the same day.

**Follow MX-r-14's order** (`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-14.round17-catalog-release.md`, section 1 with its amendments A1 and A2, which are the pattern as it ran):
- the live ref is read from the HOST by md5, and a moved base voids the halves (BASE-MOVED);
- a deploy-only commit on the live ref in a NEW deploy tree, with `infra/logic/registry` in the cone, carrying exactly the files A1 names (the catalog alone, unless A1 says otherwise);
- the ANNOUNCE carries four censuses that stay EQUAL unless A1 names an expected difference: tools, `.env` keys, `ENABLED_INTEGRATIONS`, and the MC Portal per-tool link counts;
- PHASE A ends at the ANNOUNCE (report and stop); PHASE B is a separate amendment (A2) after both never-widen halves are signed on the deploy-only commit;
- the label is read back before the first leg closes; the manifest gets `previous_deployed_commit` = the live ref and a `release_note` naming THIS release; the rollback is to the live ref only.

These are the differences:
1. **What ships:** `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` at the blob A1 names, and nothing else.
2. **NEVER-2 ledger:** `nfra-mcpindex-r15-catalog-release`.
3. **The never-widen pair covers a catalog-row visibility change.** Before this release a principal of firm X sees the firm-scoped catalog rows whose `firm` is X (23 + 1 rows today); after it, the rows the C-GROUP labels name (about 96 more). Seeing a row reads no data; client data still needs the firm's data grant. The issuer writes the COO half and asks the CTO half; A1 names both.
4. **Criteria:** `AC1` to `AC4` in section 4 (`AC2` and `AC3` are the MX-r-13 reads, run after the first leg; `AC4` is the round 18 catalog on the host, compared with the tree's by the same script). The firm-visibility matrix on the host (`deliverables/2.0.0_SA_COO~MI/round17/checks/vis_host_compare.sh`) is the issuer's own run after the apply; you do not run it.
5. **Deadline:** the depth claims are re-read at the cut and hold until the next daily publish (about 13:30Z). Land PHASE B before the deadline A1 names.

## 2. BOUNDS

1. No change to any source file.
2. Never bare `terraform apply`; never `update-function-code`. No push.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r15-catalog-release.json
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
  <criterion id="AC1" cell_refs="MX-r-15" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/r15.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-15" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; on the host the PARTITION sums N of N, every member valid (index rc=0), and discover reads good 3 of 3 (discover rc=0) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-r-15" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC3.sh; echo "exit=$?"</invocation><expect>DEPTH valid N of N; ANSWER-TIME answered measured and equal m of m, anchors 2 of 2; catalog rc=0; answer-time rc=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="MX-r-15" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/checks/r15.AC4.sh; echo "exit=$?"</invocation><expect>HOST CATALOG and TREE CATALOG lines equal (rows, nl_tags, inferred=0, bucket on every row, vendor, firm, tool_index bucket and serves); the host md5 equals the tree md5; read_tool names unserved by the deployed commit: none -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/NFRA_MCPINDEX.TO-MX-r-15.round18-catalog-release.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report, and stop. After PHASE B, write the proof instance and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 18, the release tail, the MX-r-14 pattern; held by design until the issuer's A1. Source: PRD v0.17 (done-by 2026-10-16 ~22:00Z), the CTO's ruling on label visibility (msg 34562: each release adding known-firm values carries its own pair at 0 leaks, the CTO signs on receipt). Battery at the base (2026-10-16): `r15.AC1` FAIL (no ledger entry), `r15.AC4` FAIL (the host equals the tree, but 44 rows are still inferred and 294 of 304 rows have a bucket); `r13.AC2` and `r13.AC3` are graded on the host after the release. Planted arms for AC4: `plant_r15.py` 4 of 4. The trial catalog (all five maps, 173 of 173 applied): 314 rows, nl_tags 314, inferred 0, bucket 314, vendor 136, firm 136, tool_index bucket 99 of 99, serves on 2 tools (it grows as the OG-cl tools land); the difference control (c23.AC3, 1,386 pairs): 96 rows newly visible (49financial 62, inflection 8, cottonwood 26), cross-firm leaks 0.

<status>issued</status>
<round>18</round>
<workstream>RELEASE</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
