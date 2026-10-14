# NFRA_MCPINDEX task order -- `MX-r-12` -- release MX-c-9's catalog, discover and breakdown-reader change onto the opal-gateway host on the live ref, then read FWD-20 (index + depth) and FWD-21 live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-12</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-r-12</to_id>
<issued_to>0.7.0_AE_CloudOps~MI</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule. The gateway host takes one release at a time; this release queues behind any gateway ledger then open (NFRA_OPLGTW.TO-OG-ap-14 at issuance).
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-r-11 release pattern; never-widen halves (CTO + COO) before PHASE B.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM, S3 reads).
</preflight>

## 1. THE CELL -- `MX-r-12` (round 11; PRD v0.10 @301af339c7; decomposition section ROUND 11)

**Start only when MX-c-9 is complete and drained, AND every other gateway ledger reads CLOSED.** The issuer continues
you with this order, naming the live ref to read.

**Follow MX-r-11's order exactly, as amended A1-A6**
(`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-11.catalog-tool-index-release.md`):
- the live ref is read from the HOST by md5;
- the deploy tree's HEAD IS the deploy-only commit, cut on the live ref;
- the label is read back before the first leg closes;
- the manifest's `previous_deployed_commit` is the live ref you cut on.

These are the differences:
1. **What ships, by CONTENT.** The live tree, plus MX-c-9's three gateway files and nothing else:
   - `app/refs/DATA_CATALOG.yaml`;
   - `app/integrations/opal_discover/integration.py`;
   - `app/admin_gateway_breakdown.py`.
   Take EXACTLY their drained blobs. Trunk carries other projects' gateway changes, so never ship a whole trunk tree
   (the MX-r-11 v2 lesson).
2. **The deploy cone carries `infra/logic/registry`** (round-10 analysis ruling 3, row Z-S92; now a cut-template rule).
3. **No widening.** These stay equal, before and after:
   - `ENABLED_INTEGRATIONS`;
   - the `.env` KEY set;
   - the tool census by name.
   A difference in any of them is a BLOCKING row.
4. **NEVER-2 ledger** `nfra-mcpindex-r11-catalog-release`. Legs: upload/ship, `/health` 200, then r12.AC2 and r12.AC3
   read back. On a failed read-back, roll back to the live ref you cut on, never further.
5. **The phases.**
   - PHASE A is yours: the deploy-only commit and `ANNOUNCE_MX-r-12.md`. Report, and stop.
   - PHASE B is re-addressed by amendment to `0.7.0_AE_CloudOps~MI` on both never-widen halves.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-14 ~01:1xZ) -- the MC Portal FWD-20 sitting (`2.0.0_SA_COO~MP`, msg 33866).**
- This release must not land between Andrew's FWD-20 read of the MC Portal breakdown page and NFRA_MCPORTAL.TO-MP-z-6's
  run, unless the page's per-tool index link counts stay EQUAL.
- PHASE A's ANNOUNCE therefore prints `admin_gateway_breakdown._catalog_read_tool_rows()` per-tool link counts on the
  live tree and on the cut. A difference makes the slot conditional on MP-z-6 being closed or not yet started, and the
  issuer reads that before the GO.
- The reader's line is `:108` at HEAD.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-10-14 ~02:1xZ) -- MX-c-9 drained; the slot is OURS now on live b0c75d24f1; PHASE A
and PHASE B both re-addressed to 0.7.0_AE_CloudOps~MI; close by 10:00Z.**
- MX-c-9 drained @435958cd7c and is complete @9e0f8ae6ad (A2: six research rows HELD on the R20 call
  `sitez-20261014T015958Z-a63a`; they ship in a LATER release on that call's YES, not in this one).
- **The live ref is `b0c75d24f1`** (NFRA_MCPORTAL MP-n-4, 01:31Z; `EC2_MANIFEST.json` at HEAD), not `7eff14b2e6`.
  - The issuer's census of `b0c75d24f1` with c-9's three files laid over it: N=67, partition a=11 b=44 c=12 valid,
    definitions 67 of 67, identity 0. MP-n-4 changed only `app/admin_fabric_gitstate.py`.
- **The slot** (`2.0.0_SA_COO~O` msg 33905): MX-r-12 goes NOW. The ledger must read CLOSED by 10:00Z; otherwise
  NFRA_OPLGTW r30 (OG-ap-14) deploys at 11:00Z and MX-r-12 follows it. At the close, the issuer tells `2.0.0_SA_COO~O`
  the deployed_commit; r30 re-cuts on it.
- **`<issued_to>` is now `0.7.0_AE_CloudOps~MI` for both phases.** No worker is spawned, to meet the window. PHASE A:
  1. read the live ref from the host by md5;
  2. cut the deploy-only commit on it in a NEW deploy tree, carrying exactly the three drained blobs at @435958cd7c,
     with `infra/logic/registry` in the cone;
  3. write `ANNOUNCE_MX-r-12.md` in `deliverables/0.7.0_AE_CloudOps~MI/`, with the three censuses and A1's MC Portal
     per-tool link counts (live vs cut);
  4. report, and stop for the never-widen pair.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

**AMENDED A3 (2.0.0_SA_COO~MI, 2026-10-14 ~02:2xZ) -- PHASE A waits for MX-c-9 A3.**
- Call a63a is ruled (@d5e0b1a0b6): the six held harvest rows land through `legacy_addresses.json` in MX-c-9 A3, so this
  release carries all seven research tables.
- PHASE A starts only when MX-c-9 A3 drains. The issuer then names the three blobs at the new drain commit. A cut made
  before that would ship the six-row-short catalog and need a v2.
- The 10:00Z close stands (`2.0.0_SA_COO~O` msg 33905).
- The shipped set stays exactly the three gateway files. The registry rows are repo-side and do not ship to the host.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

**AMENDED A4 (2.0.0_SA_COO~MI, 2026-10-14 ~02:4xZ) -- PHASE A starts NOW on MX-c-9's COMMITTED bytes @435958cd7c; the
six research rows follow in a later release.**
- MX-c-9 A3's six rows cannot be committed yet. `.tools/naming-gate.py` does not read `legacy_addresses.json`, so their
  emitted `prefix:` values grade NEW OUT-OF-PATTERN (row Z-W34-S7). The gate is LGIC_ENFORCE's; the ask is with
  `1.0.0_SA_CTO~Z`.
- So that the 10:00Z slot is not lost on a gate fix with no owner yet, this release ships the three blobs AS COMMITTED
  at @435958cd7c (equal at HEAD):
  - `app/refs/DATA_CATALOG.yaml` `f15b348263`: 33 harvest rows, `tool_index` 67 with `index` keys, AUA depth measured;
  - `app/integrations/opal_discover/integration.py` `cdf178e17f`: answer-time depth;
  - `app/admin_gateway_breakdown.py` `b10782ca26`: reads `index`.
- That delivers FWD-20 depth and the durable key, and FWD-21 at 24 of 24 top-level prefixes with 1 of 7 research tables.
- r12.AC2 and r12.AC3 grade FWD-20 and discover and do not count research tables, so they stand as written.
- If the gate fix lands and MX-c-9 A3 commits BEFORE the never-widen pair is signed, PHASE A is re-cut once on the new
  catalog blob. After the pair, the six rows ride the next gateway release.
- The 10:00Z close stands.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

**AMENDED A5 (2.0.0_SA_COO~MI, 2026-10-14 ~03:0xZ) -- GO for PHASE B to 0.7.0_AE_CloudOps~MI, CONDITIONED on the
ANNOUNCE.**
- Both never-widen halves are SIGNED on deploy-only `027fedfda4` (live `b0c75d24f1`):
  - COO `deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-r-12_20261014.md` @bcc2a3e6a8;
  - CTO `deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_MX-r-12_20261014.md` @0312862e0f (msg 33952).
- **Condition, read by the applier BEFORE the apply:** `ANNOUNCE_MX-r-12.md` is committed with:
  - the host census (107 files identical to `b0c75d24f1`);
  - `.env` keys equal;
  - `ENABLED_INTEGRATIONS` 7 = 7;
  - tools 67 = 67;
  - MC Portal's per-tool link counts equal live vs cut (A1).
  Any difference makes BOTH halves VOID. Stop, and report.
- The act is section 1 of the ask, verbatim. The rollback is `b0c75d24f1` only. The close is due by 10:00Z.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

**AMENDED A6 (2.0.0_SA_COO~MI, 2026-10-14 ~03:3xZ) -- v1 CLOSED; RE-OPENED for a catalog-only v2 carrying the six
legacy-addressed research rows.**
- **v1 is complete.** deployed_commit `027fedfda4` (previous `b0c75d24f1`), ledger `nfra-mcpindex-r11-catalog-release`
  CLOSED on 5 legs (msg 33964, @0dc0ddac4c). MC Portal link counts held equal (11 tools, 14 links). The issuer's
  re-run: r12.AC1, AC2 and AC3 PASS.
- **v2** ships MX-c-9 A3+A4's regenerated `app/refs/DATA_CATALOG.yaml` ALONE, at its drained blob (named in the GO).
  It carries 39 harvest rows: the six research tables through `legacy_addresses.json`, with research rowed 7 of 7.
  - It is cut on the LIVE `027fedfda4`, with `infra/logic/registry` in the cone.
  - The slot is `2.0.0_SA_COO~O` msg 33967: v2 goes BEFORE r30's re-cut. The close is due by 10:00Z; otherwise v2
    follows r30, OG-ap-17 and OG-hv-2.
- **A new NEVER-2 ledger** `nfra-mcpindex-r11-catalog-release-v2`. AC1's invocation is re-pointed to
  `round11/checks/r12v2.AC1.sh` (the same check on the v2 slug); AC2 and AC3 are unchanged and re-run on v2.
- **The rollback for v2 is v1's artifact** `opal-gateway-027fedfda4.tar.gz`, never further.
- PHASE A and PHASE B both belong to `0.7.0_AE_CloudOps~MI`, with a fresh never-widen pair on the v2 pins.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

**AMENDED A7 (2.0.0_SA_COO~MI, 2026-10-14 ~04:0xZ) -- GO for v2 to 0.7.0_AE_CloudOps~MI.**
- v2 is deploy-only `43088464f5` on live `027fedfda4`: 1 file, catalog blob `d180a6d86b`, four censuses equal
  (ANNOUNCE @88a6679a81).
- Both halves are SIGNED:
  - COO `deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-r-12_v2_20261014.md` @5c6ea45c75;
  - CTO `deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_MX-r-12_v2_20261014.md` @f0a6f0a8aa (msg 33977).
- The act is section 1 of the v2 ask, verbatim. The rollback is v1 `027fedfda4` only. The close is due by 10:00Z; at the
  close the issuer tells `2.0.0_SA_COO~O` (r30 re-cuts on the new ref).
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so
  GATE (viii) does not grade it.

## 2. BOUNDS

1. No change to any source file. This order ships what MX-c-9 committed, and nothing else.
2. Never bare `terraform apply`; never `update-function-code`. No push.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r11-catalog-release.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~34/**
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/ec2/EC2_MANIFEST.json
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W34-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-12" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round11/checks/r12v2.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-12" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round11/checks/r12.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; on the host the PARTITION sums N of N with every member valid through MC Portal's reader and no row identity in tool_index (index rc=0), and discover reads good 3 of 3 (discover rc=0) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-r-12" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round11/checks/r12.AC3.sh; echo "exit=$?"</invocation><expect>PART1 measured depths verified m of m by the aws CLI, mdpf_get_aggregate_aua measured; PART2 the AUA answer's answer-time depth is measured and equal -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/NFRA_MCPINDEX.TO-MX-r-12.depth-v4-release.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report, and stop. After PHASE B, the applier writes the proof instance at the
`<instance_path>`, and then reports once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 11, chain tail. Battery dry-run at the issuance base:
- r12.AC1 FAIL (no entry; 19 of 19 sentinels);
- r12.AC2 FAIL live (ssm 0838b977: index rc=1, links 0; discover 3 of 3);
- r12.AC3 FAIL (= c9.AC3).

<status>issued</status>
<status>pending</status>
<status>complete</status>
<status>issued</status>
<round>11</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
