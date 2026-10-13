# NFRA_MCPINDEX task order -- `MX-r-11` -- release MX-c-8's catalog and discover change onto the opal-gateway host, behind MC Portal's MP-z-5, then read FWD-20's partition, FWD-21's three discover reads and one tool's depth and freshness live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-11</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-r-11</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~33</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule. The gateway host takes one release at a time; this release queues BEHIND NFRA_MCPORTAL.TO-MP-z-5 (direction Z1, first on site Z).
comp-iam: DECLARED-NOT-APPLICABLE -- no role or policy change. The harvest rows ship with read_tool null; no tool reads opal-data-harvest after this release either.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-r-10 release pattern; never-widen halves (CTO + COO) before PHASE B.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM, S3 reads).
</preflight>

## 1. THE CELL -- `MX-r-11` (round 10; PRD v0.9 @e581c26ab4 FWD-20, FWD-21; decomposition section ROUND 10)

**Start only when MX-c-8 is complete and drained.** The issuer continues you with this order.

**Follow MX-r-10's order exactly, as amended A1-A3**
(`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-10.ops-readers-release.md`):
- read the live ref from the HOST by md5, never from the `-latest` label;
- the deploy tree's HEAD IS the deploy-only commit, cut on the live ref;
- after the upload, read back `opal-gateway-<deploy sha>.tar.gz` present and `-latest`'s `git-ref` equal to the deploy
  sha, BEFORE the ledger's first leg closes.

These are the differences:
1. **What ships, by CONTENT.** The live tree, plus MX-c-8's regenerated `app/refs/DATA_CATALOG.yaml` and its
   `app/integrations/opal_discover/integration.py`. Nothing else ships. Print the cut's file list in the ANNOUNCE.
2. **No widening.** These stay equal, before and after:
   - `ENABLED_INTEGRATIONS` (7 = 7 at issuance);
   - the `.env` KEY set (keys only, never values);
   - the tool census (67 = 67 at issuance).
   A difference in any of them is a BLOCKING row, not a release.
3. **The slot.** This release goes AFTER MC Portal's gateway release: `NFRA_MCPORTAL.TO-MP-z-5`'s NEVER-2 ledger must
   read CLOSED. That release MOVES the live ref, so cut your deploy-only commit on the ref the host serves AFTER it.
   A pin read before then is void.
4. **NEVER-2 ledger** `nfra-mcpindex-r10-catalog-release`, opened at PHASE B start. Legs: upload/ship, `/health` 200,
   then r11.AC2 and r11.AC3 read back. Roll back to the live ref on any failed leg.
5. **The phases.**
   - PHASE A is yours: the deploy-only commit and `ANNOUNCE_MX-r-11.md` in your deliverables. Report, and stop.
   - PHASE B is re-addressed by amendment to `0.7.0_AE_CloudOps~MI` once both never-widen halves (CTO + COO) are
     signed on your pins. It starts on the issuer's GO, which comes by message citing that amendment.
6. **Also the manifest.** After the apply, record the new `deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json`
   (plane 2), as MX-r-10 did. AC2's census and the (a)/(b)/(c) partition are then read against the commit the host serves.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-13 ~21:4xZ, at the MX-c-8 drain @212f2370a3) -- AC3 re-cut to what MX-c-8
measured; PHASE A starts at MP-z-5's ledger close.**
- **AC3, the issuer's defect.** As cut, `c10_second.py` picked an (a) entry whose `history_depth` AND `freshness` both read
  `measured` on one prefix basis. MX-c-8 measured `history_depth` as `absent` on all 11 (a) tools, because each served
  object is one overwritten file whose key carries no date (row Z-W33-S1). A measured `freshness` names its object
  through the catalog `row`, with the bucket root as its basis (the naming gate, row Z-W33-S5). So the pick read
  `none` in every world, and AC3 could never pass.
  - Now the pick resolves the served KEY through `freshness.row`.
  - FRESHNESS must be on or before the listed object's date.
  - A depth `absent` is CONFIRMED only when exactly one object sits at a dateless key, so no history is listable.
  - Planted arms: freshness after the object's date gives DISAGREE (FAIL); a second object at the key gives REFUTED
    (FAIL).
  - Issuer's run at 212f2370a3: `etfs_get_positioning`, `platinum/etfs/positioning_data.json`, latest 2026-10-13 =
    catalog 2026-10-13 AGREE; depth absent CONFIRMED (1 object). RESULT: PASS.
  - AC3 is the FWD-20 PROOF's second-instrument read. It does not depend on the release, so it is graded again after
    PHASE B against the deployed catalog's bytes.
  - Gate limb that graded this modification: none. `.tools/to-pipeline-gate.py` LIMB 6 does not fire on a
    modification, and this order declares `<placeholders>NONE`, so GATE (viii) does not grade it.
- **PHASE A starts only when `NFRA_MCPORTAL.TO-MP-z-5`'s NEVER-2 ledger reads CLOSED.** MP-z-5 went pending at
  ~19:38Z (81e079ba4b), so its release is in flight, and a deploy-only commit cut before it lands would be void at the
  slot (the MX-r-10 A1 v1 -> v2 lesson). The issuer continues you with this order at that close, naming the live ref
  to read.
- AC3's expectation now reads: `PICK one (a) tool; listing rc=0; GRADE ... AGREE; depth ... CONFIRMED (or AGREE when
  measured) -- RESULT: PASS -- exit=0`.

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-10-13 ~21:5xZ) -- the slot is ours; PHASE A starts now on live ref 64b3e54658.**
- MP-z-5's ledger `nfra-mcportal-gw-release` reads CLOSED at 21:44:07Z: all 5 legs proven, on 0.7.0_AE_CloudOps~MQ's
  tree `C:/tmp/mp-z5-rel`. The host serves 64b3e54658 with 67 tools (z5.AC2).
- `2.0.0_SA_COO~O` (msg 33806) gives MX-r-11 the next gateway slot. NFRA_OPLGTW.TO-OG-ap-14 (the r30 release carrying
  OG-bd-2) cuts on OUR live ref only after this order's ledger reads CLOSED at HEAD. At the close, the issuer tells
  `2.0.0_SA_COO~O` the new `deployed_commit`.
- **PHASE A, in order:**
  1. Merge `box/sitez` into your branch. It carries A1 and the amended `round10/checks/`.
  2. Read the live ref FROM THE HOST by md5. Expect 64b3e54658; if the host serves anything else, file a BLOCKING row
     and stop.
  3. Cut the deploy-only commit on that ref, carrying exactly MX-c-8's two blobs (`app/refs/DATA_CATALOG.yaml` and
     `app/integrations/opal_discover/integration.py`, read at @212f2370a3).
  4. Write `ANNOUNCE_MX-r-11.md` with the cut's file list, the rollback key (`opal-gateway-64b3e54658.tar.gz`), and the
     three equal censuses: tools 67 = 67, `.env` keys, `ENABLED_INTEGRATIONS` 7 = 7.
  5. Report, and stop.
- PHASE B is then re-addressed to `0.7.0_AE_CloudOps~MI` on both never-widen halves.

## 2. BOUNDS

1. No change to any source file. This order ships what MX-c-8 committed, and nothing else.
2. Never bare `terraform apply`; never `update-function-code`. No push.
3. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r10-catalog-release.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~33/**
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/ec2/EC2_MANIFEST.json
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W33-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp, never a placeholder.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-11" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round10/checks/r11.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-11" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round10/checks/r11.AC2.sh; echo "exit=$?"</invocation><expect>/health=200; on the host the PARTITION sums N of N with every member valid (index rc=0) and discover reads good 3 of 3 (discover rc=0) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-r-11" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round10/checks/r11.AC3.sh; echo "exit=$?"</invocation><expect>PICK one (a) tool; listing rc=0; GRADE ... AGREE; depth ... CONFIRMED (or AGREE when measured) -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.7.0_AE_CloudOps~MI/NFRA_MCPINDEX.TO-MX-r-11.catalog-tool-index-release.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

PHASE A ends at the ANNOUNCE: report, and stop. After PHASE B, the applier writes the proof instance at the
`<instance_path>`, and then reports once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 10, chain tail after MX-c-8. Battery dry-run at base 08b77fd98d
(`round10/checks/`):
- r11.AC1 FAIL as expected: no entry at HEAD (12 of 12 sentinels scanned).
- r11.AC2 FAIL as expected, live (ssm 6f80490b): `/health` 200; host census 67; partition absent; discover 1 of 3.
- r11.AC3 FAIL as expected: no (a) entry with a measured s3 basis. Its grader was exercised on a planted listing:
  AGREE (PASS), and depth one day early: DISAGREE (FAIL).

<status>issued</status>
<round>10</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
