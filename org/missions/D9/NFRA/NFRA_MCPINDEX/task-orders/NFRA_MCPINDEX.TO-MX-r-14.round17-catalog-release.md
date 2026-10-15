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

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-15 ~18:3xZ) -- THE PHASE A GO, on `2.0.0_SA_COO~O` msgs 34427 and 34514 (OG-ap-20 is live; this release holds the next gateway slot; `OG-ap-21` waits behind it until 21:00Z).**
- **Start condition met:** MX-c-18, MX-c-19 and MX-c-20 are complete and drained; the NFRA_OPLGTW ledger `nfra-oplgtw-gateway-release-g5a` is the only one ahead and `2.0.0_SA_COO~O` reads it as a leg left to close, not a block.
- **The live ref:** `06cfb6db6471972c7304cd3d7a5b93e6f521ad72` (`EC2_MANIFEST` `deployed_commit`, previous `1b18b94979`; the release commit itself is the deployed one, there is no separate deploy-only commit). Read the live ref from the HOST by md5 at the act, as MX-r-12 A1 says; if a later release has landed first, STOP at the ANNOUNCE and report the new ref, and the issuer re-cuts.
- **What ships (exactly two files, at trunk commit `7cfd0b09ec`):**
  - `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, blob `b97c59e6ac9900b99a32fe6a8c957b4f00f71ca9` (live `e5096b5d6c`). It is the round 17 catalog: 44 rows with derived `nl_tags` marked `inferred`, 24 table rows with a `firm` field, 7 table rows naming a live `read_tool`, the tool index at N=99, depth and freshness re-read 2026-10-15 16:07Z, definition lines taken from the SHIPPED cut (live ref plus the discover module below).
  - `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`, blob `92ca8b57f727bc75a304edfb86b0bbb74960c4b3` (live `f3cf344cc3`): `_silver_answer` shows a firm-scoped row to its own firm's principals only, and a string `never_sum_rules` gives at most one caveat line (row Z-S120).
  Verify each blob with `git rev-parse 7cfd0b09ec:<path>` before the upload and again from the host after (md5 of the file equal to the tree's). Nothing else ships.
- **NEVER-2 ledger:** `nfra-mcpindex-r14-catalog-release` (the slug `r14.AC1` grades).
- **Criteria:** `AC1` to `AC4` stand. Base dry-runs 2026-10-15: AC1 FAIL (no entry), AC4 FAIL (host nl_tags 260, inferred 0, firm 0); AC2 and AC3 are graded after the first leg. On the tree: `r13.AC3` PASS (depth 11 of 11, answer-time 17 of 17, anchors 2 of 2); `c11_index` on the SHIPPED cut: PARTITION a=11 b=76 c=12, sum 99 of N=99, definitions located 99 of 99; `c10_discover` good 3 of 3; `r1.AC1` to `AC3` PASS; `f1.AC1` to `AC3` PASS (1,326 pairs, 24 newly visible, cross-firm leaks 0).
- **The ANNOUNCE carries four censuses that stay EQUAL except one:** tools 99 = 99, `.env` keys 57 = 57, `ENABLED_INTEGRATIONS` 7 = 7 (all equal to the live ref); the MC Portal per-tool link counts are EXPECTED to go **33 tools / 112 links (live) to 39 tools / 119 links (cut)** (measured on the extract of the shipped cut). Any other link count VOIDs both halves.
- **Time limit:** the depth claims were read 2026-10-15 16:07Z and hold until the next daily publish (about 13:30Z 2026-10-16). Land PHASE B before 13:00Z; if it will not, report at the ANNOUNCE and the issuer re-measures. `NFRA_OPLGTW`'s `OG-ap-21` is released on the live ref if this release is not live by 21:00Z tonight; then this release re-cuts on its ref and the catalog is re-emitted once.
- **PHASE A, by `0.7.0_AE_CloudOps~MI`:** re-read the live ref from the host by hash (expect `06cfb6db64`); cut a NEW deploy tree and a deploy-only commit on it with exactly these two blobs (with `infra/logic/registry` in the cone); the four censuses; `deliverables/0.7.0_AE_CloudOps~MI/ANNOUNCE_MX-r-14.md`; report, and STOP for the never-widen pair. The COO half is `deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-r-14_20261015.md` (signed once the ANNOUNCE is read); the CTO's half is asked in parallel. PHASE B is a separate amendment (A2) after both halves are SIGNED on the deploy-only commit.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so GATE (viii) does not grade it.
<status>issued</status>
