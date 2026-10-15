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

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-10-14 ~14:0xZ) -- the slot moved again, and the release carries round 13's catalog too.**
- **Gateway order, from `2.0.0_SA_COO~O` (msgs 34047 and 34079):** OG-hv-2, then OG-ap-18 (the G1 typed harvest tools), then OG-ap-17, then THIS release.
  Supersedes A1's order. `2.0.0_SA_COO~O` sends the live deployed_commit at each close; PHASE A starts on the ref OG-ap-17 leaves.
- **What ships (replaces difference 1):** `app/refs/DATA_CATALOG.yaml` and `app/integrations/opal_discover/integration.py` at the blobs the PHASE A GO names. They carry MX-c-10 (round 12) AND
  MX-c-11 / MX-c-12 (round 13: one catalog row per harvest dataset, 78, at v0.5). The issuer regenerates the catalog against the LIVE ref's tool census before it names the blobs, so no row names a
  tool the host does not serve (PRD v0.11 item 3).
- **Start condition:** MX-c-10, MX-c-11 and MX-c-12 are drained AND every NFRA_OPLGTW ledger above reads CLOSED.
- **Criteria:** r13.AC1 to AC3 stand. A fourth, `r13.AC4` (the round-13 catalog live: 78 harvest rows, v0.5, every named read_tool served), is added at the PHASE A GO, once its check exists and has been
  dry-run at the base. Round 12 closes with round 13 because this order is the tail of both.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so GATE (viii) does not grade it.

**AMENDED A3 (2.0.0_SA_COO~MI, 2026-10-15 ~06:0xZ) -- THE PHASE A GO, on `2.0.0_SA_COO~O` msg 34339 (the OPLGTW queue ahead of this release is empty).**
- **Start condition met:** MX-c-10, MX-c-11 and MX-c-12 are drained (and MX-c-13 to MX-c-17 with them); the NFRA_OPLGTW ledgers ahead (OG-yr-1, OG-ap-18, OG-ap-19) read CLOSED.
- **The live ref:** `ee23dd004c` as `2.0.0_SA_COO~O` states it (and `infra/aws/ec2/EC2_MANIFEST.json` at the GO). Read the live ref from the HOST by md5 at the act, as MX-r-12 A1 says; if a later release has landed first, STOP at the ANNOUNCE and report the new ref, and the issuer re-cuts.
- **What ships (names the blobs; replaces differences 1 and A2's list):** exactly two files, at trunk commit `789ffd57b0`:
  - `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, blob `11620b3c520175260a4662b803c1f6344b7a8eec` (catalog v0.5: 78 harvest rows, 216 table rows with key templates, the 78 + 19 rows naming the live tools, the aum-metrics row denied, the legacy mdpf row dropped, history depth re-read on 2026-10-15);
  - `infra/aws/ec2/opal-gateway/app/integrations/opal_discover/integration.py`, blob `f3cf344cc315420f1e7d833657b07b504a246b1a` (a table row that names no tool is a gap and sorts last).
  Verify each blob with `git rev-parse 789ffd57b0:<path>` before the upload and again from the host after (md5 of the file equal to the tree's). Nothing else ships.
- **Criteria:** `r13.AC1` to `r13.AC3` stand; **`r13.AC4` is added** (the round 13, 14 and 16 catalog live on the host: version 0.5, 78 harvest rows, 216 table rows with a key_template, 5 retired, md5 equal to the tree's catalog, every named read_tool served by the deployed commit). Base dry-runs 2026-10-15: AC1 FAIL (no entry), AC2 live guard PASS, AC3 PASS on this tree, AC4 FAIL (host version 0.4, 39 harvest rows, 0 table rows). Planted arms for AC4: 5 of 5.
- **Time limit:** the depth claims were read today and equal the live objects until the next daily publish (about 13:30Z). Land PHASE B before then; if it will not, report at the ANNOUNCE and the issuer re-measures.
- **At close:** the issuer tells `2.0.0_SA_COO~O` the deployed commit (it takes the next gateway slot for OG-ap-20, which reads its keys from this catalog).
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so GATE (viii) does not grade it.

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
  <expected_criteria>AC1,AC2,AC3,AC4</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; on the host the PARTITION sums N of N, every member valid (index rc=0), and discover reads good 3 of 3 (discover rc=0) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-r-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC3.sh; echo "exit=$?"</invocation><expect>DEPTH valid N of N; ANSWER-TIME answered measured and equal m of m, anchors 2 of 2; catalog rc=0; answer-time rc=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="MX-r-13" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round12/checks/r13.AC4.sh; echo "exit=$?"</invocation><expect>HOST CATALOG version=0.5 harvest=78 table=216 key_template=216 retired=5; the host md5 equals the tree md5; read_tool names unserved by the deployed commit: none -- RESULT: PASS -- exit=0</expect></criterion>
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
