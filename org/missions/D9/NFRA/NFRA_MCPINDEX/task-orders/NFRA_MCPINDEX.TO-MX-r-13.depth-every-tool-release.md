# NFRA_MCPINDEX task order -- `MX-r-13` -- release MX-c-10's catalog and discover change onto the opal-gateway host on the live ref, behind NFRA_OPLGTW's queued releases, then read FWD-20 depth on every indexed tool live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-13</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-r-13</to_id>
<issued_to>0.7.0_AE_CloudOps~MI</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule. The gateway host takes one release at a time; this release queues behind NFRA_OPLGTW r30, its tier fix and OG-mg-1 (ROUND_ANALYSIS.round11.md section 3).
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-r-12 release pattern; never-widen halves (CTO + COO) before PHASE B.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM, S3 reads).
</preflight>

## 1. THE CELL -- `MX-r-13` (round 12; decomposition section ROUND 12)

**Start only when MX-c-10 is complete and drained, AND every NFRA_OPLGTW gateway ledger named in the queue reads
CLOSED.** The issuer continues you, naming the live ref and the blobs.

**Follow MX-r-12's order** (`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-12.depth-v4-release.md`,
A1-A7):
- the live ref is read from the HOST by md5;
- the deploy tree's HEAD IS the deploy-only commit, in a NEW deploy tree, with `infra/logic/registry` in the cone;
- the ANNOUNCE carries four censuses that stay EQUAL: tools, `.env` keys, `ENABLED_INTEGRATIONS`, and MC Portal per-tool
  link counts;
- a fresh never-widen pair is signed on the pins;
- the label is read back before the first leg closes;
- the manifest gets `previous_deployed_commit` = the live ref and a `release_note` naming THIS release;
- the rollback is to the live ref only.

These are the differences:
1. **What ships:** MX-c-10's `app/refs/DATA_CATALOG.yaml` and `app/integrations/opal_discover/integration.py`, at their
   drained blobs, and nothing else.
2. **NEVER-2 ledger:** `nfra-mcpindex-r12-catalog-release`.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-14 ~06:1xZ) -- the slot, as `2.0.0_SA_COO~O` corrected it (msg 33999).**
- MX-c-10 drained @8c74d1d902. The issuer's re-run: c10.AC1 11 of 11 valid, c10.AC2 7 of 7 with anchors 2 of 2, and
  c10.AC3 18 of 18 measured rows answered, anchors 2 of 2.
- The ships-blobs are named in the PHASE A GO.
- **Gateway order:** OG-ap-14 (r30; B2 at 11:00Z or later), then OG-ap-17 (the tier fix), then THIS release, then
  NFRA_OPLGTW OG-hv-2, which cuts on the ref this release leaves.
- OG-mg-1 writes grant records and deploys nothing, so it does not hold this slot. `2.0.0_SA_COO~O` sends the live
  deployed_commit when OG-ap-17's ledger closes, and PHASE A starts on that ref.
- At this release's close, the issuer tells `2.0.0_SA_COO~O` the deployed_commit for OG-hv-2.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

## 2. BOUNDS

1. No change to any source file.
2. Never bare `terraform apply`; never `update-function-code`. No push.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r12-catalog-release.json
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
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; on the host the PARTITION sums N of N, every member valid (index rc=0), and discover reads good 3 of 3 (discover rc=0) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-r-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC3.sh; echo "exit=$?"</invocation><expect>DEPTH valid N of N; ANSWER-TIME answered measured and equal m of m, anchors 2 of 2; catalog rc=0; answer-time rc=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/NFRA_MCPINDEX.TO-MX-r-13.depth-every-tool-release.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report, and stop. After PHASE B, write the proof instance and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 12, chain tail. Battery at the base:
- r13.AC1 FAIL (no entry; 18 of 18 sentinels);
- r13.AC2 a live regression guard, PASS on the host now;
- r13.AC3 FAIL (catalog rc=1; anchors 0 of 2).

<status>issued</status>
<round>12</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
