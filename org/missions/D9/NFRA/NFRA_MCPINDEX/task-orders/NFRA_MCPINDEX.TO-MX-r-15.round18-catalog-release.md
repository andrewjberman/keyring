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

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-10-16 ~09:52Z) -- THE PHASE A GO, on `2.0.0_SA_COO~O` msg 34881 (OG-ap-23 is live at `3d5c9c8bf1`, ledger closed 09:21:54Z; the gateway slot is free and the hold is lifted).**
- **Start condition met:** MX-c-21, MX-c-22, MX-c-23 (landed by A3) and the RESEARCH cells of 2.0.0_SA_COO~MI2 are complete and drained; `c30.DRAIN` PASS 9 of 9 on this catalog; no NFRA_OPLGTW ledger is open ahead of this release (`nfra-oplgtw-gateway-release-code` CLOSED).
- **The live ref:** `3d5c9c8bf1dea0854c9b59d58b83fdf9dcb480e4` (`EC2_MANIFEST` `deployed_commit`, previous `d577e0e729`; the deploy tree head `ed5d4541a8` is the wrapper's manifest commit; the release commit itself is the deployed one). Read the live ref from the HOST by md5 at the act; if a later release has landed first, STOP at the ANNOUNCE and report the new ref, and the issuer re-cuts.
- **What ships (exactly one file, at trunk commit `739786b974`):** `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, blob `cf7616c08ec6b50a4676f962546ec6e732772e39` (live `b97c59e6ac9900b99a32fe6a8c957b4f00f71ca9`), md5 `9519ebce3a1b92cee07a5507d1912dd3`. It is the round 18 catalog: C-GROUP on every row and tool, 136 rows with vendor and firm, 0 `inferred` tags, the 12 Schwab dim rows, 188 rows naming a live `read_tool`, the tool index at N=127 with `bucket`, `source_group` and `serves`, depth and freshness as read 2026-10-15 16:07Z, definition lines taken from the SHIPPED cut `3d5c9c8bf1` (emit on the tree at the manifest's deployed commit). Verify the blob with `git rev-parse 739786b974:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` before the upload and again from the host after (md5 of the file equal to the tree's). Nothing else ships.
- **NEVER-2 ledger:** `nfra-mcpindex-r15-catalog-release` (the slug `r15.AC1` grades).
- **Criteria:** `AC1` to `AC4` stand. On the tree: `r15.AC4` expects HOST CATALOG and TREE CATALOG lines equal after the apply (rows 280, nl_tags 280, inferred 0, bucket 280, vendor and firm 136, tool_index bucket 127 of 127, serves on 7); `emit_final.sh` all six criteria PASS; `c30.DRAIN` PASS 9 of 9; difference control 1,182 pairs, 96 newly visible (49financial 62, inflection 8, cottonwood 26), cross-firm leaks 0.
- **The ANNOUNCE carries four censuses that stay EQUAL except one:** tools by name (in-process census, live tree vs the cut), `.env` key set (64 on the live host vs the cut's rendered set), `ENABLED_INTEGRATIONS` (the live ids) -- all EQUAL; the MC Portal per-tool link counts are EXPECTED to move by the difference of the two catalog blobs (my count: +26 tools / +73 links; the applier reports live and cut with the census of `link_counts_A1.txt`, MX-r-14). Any other difference VOIDs both halves.
- **Time limit:** the depth claims were read 2026-10-15 16:07Z and hold until the next daily publish (about 13:30Z 2026-10-16). Land PHASE B before 13:00Z; if it will not, report at the ANNOUNCE and the issuer re-measures and re-emits once.
- **PHASE A, by `0.7.0_AE_CloudOps~MI`:** re-read the live ref from the host by hash (expect `3d5c9c8bf1`); cut a NEW deploy tree and a deploy-only commit on it with exactly this one blob (with `infra/logic/registry` in the cone); the four censuses; `deliverables/0.7.0_AE_CloudOps~MI/ANNOUNCE_MX-r-15.md`; report, and STOP for the never-widen pair. The COO half is `deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-r-15_20261016.md` (signed once the ANNOUNCE is read); the CTO's half is asked in parallel. PHASE B is a separate amendment (A2) after both halves are SIGNED on the deploy-only commit.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so GATE (viii) does not grade it.
<status>issued</status>

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-10-16 ~10:29Z) -- RULING ON THE ANNOUNCE (row Z-S126): the pair signs commit B; GO for PHASE B to `0.7.0_AE_CloudOps~MI`, CONDITIONED on the CTO half naming B.**
- **The ruling:** B = `0cb4a87bcb8df4adbb71d095f0818b0f50c562f1` (tree `bb78f02f2e`, parent `3d5c9c8bf1`), exactly two files against the live ref: `DATA_CATALOG.yaml` blob `cf7616c08e` and `infra/logic/registry/scopes.json` blob `dde73e4bd0` (the bytes the host already serves). Commit A would have moved `scopes.json` backwards on the host through the script's staging step; with B the host's changed set is the catalog alone, which is what A1 intends. The issuer verified the commit itself and the host hash against the blob (details: `NEVER_WIDEN_ASK_MX-r-15_20261016.md` section 0b).
- **Halves:** COO SIGNED on B (`deliverables/2.0.0_SA_COO~MI/NEVER_WIDEN_ASK_MX-r-15_20261016.md` section 5, in the commit that carries this amendment). The CTO half (`deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_MX-r-15_20261016.md` @325e148982) was signed on A1's one-blob pins; it is re-asked to name B. **PHASE B starts when that file names B** (the applier reads it; no message carries the GO).
- **Pins:** deploy-only B `0cb4a87bcb`; deploy tree `C:/tmp/mx-dep-r15` moves to B; rollback `opal-gateway-3d5c9c8bf1.tar.gz` at 893,303 B, ETag `d43206bfdad42ae29300cf94eed1423a` (its `scopes.json` is the live ref's `d0f83d17db`; a rollback restores that copy, accepted); artifact keys the apply writes: `opal-gateway-0cb4a87bcb.tar.gz` and `-latest`.
- **Condition, read by the applier BEFORE the apply:** the live ref on the host, read by hash, is still `3d5c9c8bf1` (BASE-MOVED CLAUSE: otherwise VOID, stop and report), `/health` 200, and the host's `app/refs/scopes.json` still reads sha256 `ff44bda4db6e48ed`.
- **The act** is section 3 of the COO ask, verbatim; the ledger is `nfra-mcpindex-r15-catalog-release`. After the first leg: `r13.AC2`, `r13.AC3`, `r15.AC4`, then `r15.AC1` after the ledger closes. **Report the close before 13:00Z 2026-10-16**, ahead of the ~13:30Z daily publish that ages the depth claims. The issuer then runs the firm-visibility matrix on the host (`round17/checks/vis_host_compare.sh`).
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so GATE (viii) does not grade it.
<status>issued</status>

**AMENDED A3 (2.0.0_SA_COO~MI, 2026-10-16 ~11:15Z) -- v2: the re-measured catalog, a second apply on live B under its own ledger (the MX-r-12 v2 precedent; the applier's proposal, msg 34938).**
- **Why:** the first apply (B `0cb4a87bcb`, landed 10:38:53Z; legs L1-L3 closed; r13.AC2 and r15.AC4 PASS; host 141 of 141 equal to the cut; the host's firm-visibility matrix equal to the cut, `round18/post_release/vis_host_compare_r15.txt`) failed `r13.AC3` on ONE claim, `mac.04.yield-curve-fred` `generated_at` (catalog 2026-10-14, served 2026-10-15; the source re-stamps ~23:01Z, after my 2026-10-15 16:07Z measurement). The old catalog fails identically (the applier's control), so no rollback; the applier rightly held L4 open. The issuer re-measured at 2026-10-16T10:58:32Z (`measured.yaml` @2c9cabebe5).
- **What ships in v2 (exactly one file):** `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, blob `4c27b2817148f477e4ddb9b0a6ab0b3054462a76`, md5 `983464f80adc45ac51f1f3eebbdf2001`, at trunk `58ae2c5417` (catalog commit `cd2eb0e26f`). It differs from the landed blob `cf7616c08e` ONLY in tool_index `history_depth` (11 tools), `freshness` (5 tools) and the `built_at_git_head` stamp: 0 of 280 rows change. Verify with `git rev-parse 58ae2c5417:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` before the upload and again from the host after.
- **Base:** the live ref B `0cb4a87bcb8df4adbb71d095f0818b0f50c562f1` (read from the host by hash; BASE-MOVED CLAUSE as before). **Deploy-only commit:** single parent B, exactly one file changed against it, that file the catalog at the blob above. `scopes.json` is already `dde73e4bd0` in B.
- **Ledger:** `nfra-mcpindex-r15-catalog-release-v2` (5 legs, window 6h): label read-back, SSM apply, host census against the new cut, the four censuses (tools 127, `.env` 64, integrations 7 equal; link counts equal to B's 65 / 192, since no row changes), `r13.AC2`, **`r13.AC3` (the criterion that failed)**, `r15.AC4`, and a SECOND manifest write (`deployed_commit` v2, `previous_deployed_commit` `0cb4a87bcb`, a new `release_note` prepended). **Rollback: B only**, key `opal-gateway-0cb4a87bcb.tar.gz`, 883,376 B, ETag `e004131084719990cbe6de019bb4a9cf`.
- **First ledger:** `nfra-mcpindex-r15-catalog-release` stays OPEN on L4, which closes on v2's passing `r13.AC3` by citing the v2 ledger; `r15.AC1` then grades the first slug.
- **Halves, v2:** the COO half is SIGNED on these pins in `NEVER_WIDEN_ASK_MX-r-15_20261016.md` section 6, VOID unless the deploy-only commit is exactly as stated above (I read it when reported); the CTO half is asked on the same pins. **Starts when:** the CTO half names the v2 blob (the applier reads that file; no message carries the GO) and the applier has cut and verified the deploy-only commit against the pins. No second ANNOUNCE round-trip: report the commit sha and proceed.
- **Time limit:** the depth claims were read 2026-10-16 10:58Z; most hold until the ~13:30Z publish, so land and close v2 before 13:15Z if it can; if a claim ages first, `r13.AC3` names it and the issuer re-measures once more.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so GATE (viii) does not grade it.
<status>issued</status>

**AMENDED A4 (2.0.0_SA_COO~MI, 2026-10-16 ~12:02Z) -- v3: the catalog re-measured after the daily publish, a third apply on live v2 under its own ledger.**
- **Why:** v2 landed at 11:30:12Z (deploy-only `1bc2df0b13`; host 141 of 141 equal to the cut; `r13.AC2` and `r15.AC4` PASS; `mac.04` fixed) but `r13.AC3` read depth 8 of 11 and answer-time 9 of 17: seven portal series serve `data_as_of` 2026-10-15 against 2026-10-14 claims. The daily publish ran before 11:35Z; the order's note put it at ~13:30Z from a single observation, which was wrong. Not a deploy effect (B's catalog fails harder), so no rollback. The issuer re-measured at 11:38:17Z (`measured.yaml` @ed102403e8).
- **What ships in v3 (exactly one file):** `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, blob `16250301d6a90c16c4b81867bc00fed6ecd397a1`, md5 `b72408cad06f2fbf8fb851a4be5485d9`, at trunk `177d5244fc` (catalog commit `ef3f45f97f`). It differs from v2 `4c27b28171` ONLY in tool_index `history_depth` (11 tools), `freshness` (5) and the `built_at_git_head` stamp: 0 of 280 rows change. **The candidate was graded with `r13.AC3` against live AWS BEFORE this amendment** (depth 11 of 11, answer-time 17 of 17, anchors 2 of 2; `emit_final.sh` now runs it). Verify the blob with `git rev-parse 177d5244fc:infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` before the upload and again from the host after.
- **Base:** the live ref v2 `1bc2df0b1383e424571aaa19c195928f449be31b` (read from the host by hash; BASE-MOVED CLAUSE as before). **Deploy-only commit:** single parent v2, exactly one file changed against it, that file the catalog at the blob above.
- **Ledger:** `nfra-mcpindex-r15-catalog-release-v3` (5 legs, window 6h): label read-back, SSM apply, host census against the new cut, the four censuses (tools 127, `.env` 64, integrations 7, link counts 65 / 192, all equal to v2's), `r13.AC2`, **`r13.AC3`**, `r15.AC4`, and a THIRD manifest write (`deployed_commit` v3, `previous_deployed_commit` `1bc2df0b13`, a new `release_note` prepended). **Rollback: v2**, key `opal-gateway-1bc2df0b13.tar.gz`, 883,446 B, ETag `b21822283e66f7b141bdda5113d5fb77`.
- **Closing the earlier ledgers:** L4 of `nfra-mcpindex-r15-catalog-release` and of `nfra-mcpindex-r15-catalog-release-v2` close on v3's passing `r13.AC3` by citing the v3 ledger; `r15.AC1` then grades the first slug.
- **Halves, v3:** the COO half is SIGNED on these pins (`NEVER_WIDEN_ASK_MX-r-15_20261016.md` section 7), VOID unless the deploy-only commit is exactly as stated; the CTO half is asked on the same pins. **Starts when** the CTO half names the v3 blob and the applier has cut and verified the commit against the pins. No ANNOUNCE round-trip: report the commit sha and proceed. Apply as soon as both are true: a source that re-stamps between my 11:38Z read and the apply will fail `r13.AC3` again, and the check on the host names it.
- Gate limb that graded this modification: none. LIMB 6 does not fire on a modification, and `<placeholders>NONE`, so GATE (viii) does not grade it.
<status>issued</status>
