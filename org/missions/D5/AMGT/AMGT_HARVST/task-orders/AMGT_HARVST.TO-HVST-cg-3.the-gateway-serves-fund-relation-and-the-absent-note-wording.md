# AMGT_HARVST task order -- `HVST-cg-3` -- ROUND 92, workstream FUNDREL-RELEASE: THE OPAL GATEWAY SERVES `fund_relation` IN `research_reports[]` AND THE ABSENT-NOTE WORDING UNDER A FIELD FILTER (STAGED behind the silver rewrite, a signed never-widen pair and the host owner's notice) (row D1-S46; CTO msg 7775)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cg-3.the-gateway-serves-fund-relation-and-the-absent-note-wording</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cg-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order.
comp-iam: RUN at L5 -- the deploy path is `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` (S3 tarball, then an SSM pull on the instance); no grant is created or widened. The BLAST RADIUS is the whole `opal-gateway` service (every MCP tool it serves restarts), which the never-widen pair names with its rollback.
comp-adversary: RUN at L5 -- the adversary is a deploy of a tree that is not the live commit plus the three files (a stale base, or other seats' unreleased gateway changes at HEAD), a release BEFORE the silver rewrite lands (the field would be served as None on every row), a served read answered from a cache, a call of `etfs_compare_peers` (site Z row `Z-S375`: it can OOM the 1.8 GB host), and a half-landed deploy (NEVER-2).
</preflight>

## 0. THE CELL

Two changes to `infra/aws/ec2/opal-gateway/app/harvest_research.py` are merged on `box/dell1` and not served: `HVST-ce-3` (merged `b77e08e198`; with a non-empty `fields` argument, when every requested dossier field cites a misfiled report, `parts_absent.dossier` names only the requested fields it excluded) and `HVST-cg-4` (`REPORT_FIELDS` gains `fund_relation`, so each `research_reports[]` entry carries the silver row's `fund_relation`; the merge commit is named in the issuer's GO). This cell releases both in ONE gateway release. **State plainly in `cg3_before.out`:** after `HVST-ce-4`/`cf-4` no live read triggers the ce-3 sentence, so its proof is the offline test; the live proof of this release is that `research_reports[].fund_relation` is served and nothing else changed.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-ce-3` is merged (`b77e08e198`) and `HVST-cg-4` is `<status>complete</status>` and merged (the issuer names the commit in the GO).
- (b) **The silver rewrite has landed:** `HVST-cg-2` is `<status>complete</status>`, and you read ONE newest silver part (a `part-*.parquet` the cg-2 manifest names) and print that its rows carry the column `fund_relation` with at least one non-null value. A release before this serves `None` on every row.
- (c) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round92/NEVER_WIDEN_HALF_COO_CG3_GATEWAY_FUND_RELATION.md` and CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CG3_GATEWAY_FUND_RELATION_CTO_HALF.md` (both written by the issuer and the CTO before the GO; their conditions bind you). The order is STAGED until the issuer sends GO.
- (d) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cg3-gateway-fundrel-release.json`), with the restart window and the before and after tool-name counts.

## 2. THE ACT (dell1)

Read `docs/deployment/` and `infra/aws/ec2/opal-gateway/deploy/` first. **THE RELEASE IS CUT ON THE LIVE COMMIT, NEVER ON HEAD.**
0. **Before-state, read only (`cg3_before.out`):** `services.opal-gateway.deployed_commit` and `previous_deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json`, the commit the instance runs and `/opt/opal-gateway/.deployed_commit` (if they differ, STOP and file a row; the last report is `efcc8ae19f`, fetch it from `origin/rel-nfra-og-live-efcc8ae19f` if it is not in the store); the MCP tool-name count and `/health`; the previous tarball key. Then the BEFORE reads: `harvest_get_research` for `KMB_US_Equity`, `CPA_US_Equity` and `UNH_US_Equity` with `fields` `["fund_of_record","last_stated_position"]`, printing every returned field entry, `content_sha256`, `as_of` and `source_keys`, and for each the `research_reports` entries (`fund`, `fund_evidence`, and the absence of `fund_relation`). DO NOT call `etfs_compare_peers`.
1. **Cut** `rel-amgt-harvst-cg3` from the live commit in a worktree of your own. Print `git show b77e08e198^1:infra/aws/ec2/opal-gateway/app/harvest_research.py` against `git show <live>:infra/aws/ec2/opal-gateway/app/harvest_research.py`: they must be IDENTICAL (md5 `6d9e0dd38166b82943d6834a0ce482b5` read by the issuer at `efcc8ae19f`); a difference means the live file changed: STOP, carry nothing, tell the issuer. Carry ONLY these three paths, from the merge commits (cherry-pick `b77e08e198`, then the `cg-4` merge the GO names, and print the result): `infra/aws/ec2/opal-gateway/app/harvest_research.py`, `infra/aws/ec2/opal-gateway/tests/test_ce3_parts_absent_wording.py`, `infra/aws/ec2/opal-gateway/tests/test_cg4_report_fund_relation.py`. `git diff --name-status <live> rel-amgt-harvst-cg3` lists exactly those three paths (print it), and `git diff <live> rel-amgt-harvst-cg3 -- infra/aws/ec2/opal-gateway/app/harvest_research.py` shows exactly the ce-3 hunk and the one-token `REPORT_FIELDS` hunk (print it). Run `tests/test_ce3_parts_absent_wording.py`, `tests/test_cg4_report_fund_relation.py`, `tests/test_cd1_dossier_misfiled.py`, `tests/test_cc1_model_basis.py`, `tests/test_cc2_research_misfiled.py`, `tests/test_cc3_ticker_shaped_never_exact_on_name.py`, `tests/test_og_gt1.py`, `tests/test_og_gt3.py` and `tests/test_og_gt4.py` on the release branch.
1b. **The host owner is told first.** After step 1 and BEFORE the deploy write `cg3_hostowner_note.out` (release commit, the three paths, the intended window start and end UTC, the rollback tarball) and tell the issuer. The issuer sends it to site Z through `0.0.0_AB_MSTR~DELL1` and sends GO. Do not deploy before that GO; an in-flight release on the host in your window is a STOP.
2. **Cache and deploy:** run `ops/bun_cache_precheck.py` once before the build and print it (any count other than complete: STOP, no package is fetched). Deploy with `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` from the RELEASE BRANCH with `AGENT_NAME` set to your serial and `DEPLOY_BASE_REF=<the live commit>`, never a bare `aws` update. Wait for the service health check; record it and the tool-name count in `cg3_after.out`; they equal the before values.
3. **The reads after (`cg3_served.out`):** the same reads of step 0, verbatim, then the new proof: `harvest_get_research` with `fields` `["fund_of_record","last_stated_position"]` for `ADBE_US_Equity`, `SNPS_US_Equity`, `MNST_US_Equity`, `ML_FP_Equity`, `CLX_US_Equity` and the control `UNH_US_Equity`, printing for each the `fund_relation` of every `research_reports[]` entry that has a `fund`. Every gold field entry and key of KMB, CPA and UNH equals the before read (`content_sha256`, `source_keys` equal); the proof names read `candidate` (ADBE, SNPS, MNST, CLX), `template` (ML_FP) and UNH `holding`.
4. Write `cg3_served.out` ending with exactly these lines: `RELEASE_THREE_PATHS_AND_EQUALITY=PASS|FAIL`, `SERVED_GOLD_READS_UNCHANGED=PASS|FAIL`, `TOOLS_AND_HEALTH_EQUAL=PASS|FAIL`, `FUND_RELATION_SERVED=PASS|FAIL`. A FAIL is rolled back to the previous tarball at once if the cause is the deploy itself, and the cell stays `pending`.
5. Right after the deploy tell the issuer the release branch name and commit; the issuer asks `0.0.0_AB_MSTR~DELL1` to push the ref and tells site Z. Record it in `cg3_after.out`.
6. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Tell the issuer when the deploy has landed and when `cg3_served.out` is written.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cg3-gateway-fundrel-release.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cg-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/cg3_served.out</invocation><expect>(?m)^RELEASE_THREE_PATHS_AND_EQUALITY=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cg-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/cg3_served.out</invocation><expect>(?m)^SERVED_GOLD_READS_UNCHANGED=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cg-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/cg3_served.out</invocation><expect>(?m)^TOOLS_AND_HEALTH_EQUAL=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-cg-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round92/cg3_served.out</invocation><expect>(?m)^FUND_RELATION_SERVED=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the CTO's named proof for the ruling (msg 7775, item 4: the proof read through the gateway on ADBE, SNPS, MNST, ML_FP and CLX, UNH as control); AC1 to AC3 are the release's own controls, as `HVST-ce-5` had them.
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cg-3.the-gateway-serves-fund-relation-and-the-absent-note-wording.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cg-3.the-gateway-serves-fund-relation-and-the-absent-note-wording` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cg-3.the-gateway-serves-fund-relation-and-the-absent-note-wording.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- **Long runs and detached processes (CTO round-90 item 3, row `D1-S44`):** nothing in this order is a long write run; if you start any process that outlives a tool call, start it unbuffered with its stdout and exit status logged to a file, and read that file; never rely on a buffer.
- Do not edit this order file: the issuer flips its status.
- The hourly `sa` reads (Branch F stands) continue beside this order until the issuer says stop.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** `HVST-cg-4` is merged at `290f2e9e6d` (the commit the GO names). It waits on `HVST-cg-2` complete (the silver rewrite), and the pair (COO half to be written after the cg-2 dry run is read; CTO half to be signed). Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's cut (msg 7775): `REPORT_FIELDS` gains `fund_relation`, the two `ce-3` files ride the release, one release under its own pair, site Z told first, the stale-base guard on the live commit, released after the silver lands so the field is never served empty. It replaces the superseded `HVST-ce-5` (carried file `ledger/ROUND91_CARRIED_FOR_NEXT_GATEWAY_RELEASE.md`); its controls are copied here unchanged.
- **The live commit moved (site Z CTO, msg 35578 via MSTR msg 7795, 2026-10-18 00:12Z):** ledger `nfra-oplgtw-gateway-release-batch7` CLOSED 00:02:10Z; live is `d077cef04333500595a7a531ebddc2f43e5f8789` on base `efcc8ae19f`; site Z says `harvest_research.py` is unchanged (so the `b77e08e198^1` equality, md5 `6d9e0dd38166b82943d6834a0ce482b5`, must still hold: the seat measures it and STOPS on a difference) and the unit now has `MemoryMax 1400M`; scratch ref `origin/rel-nfra-og-live-d077cef043`. The order reads the live commit from the manifest, the instance and `/opt/opal-gateway/.deployed_commit` as written; expect `d077cef043`, not `efcc8ae19f`. Read at the issuer's side, not yet at the seat's.
- **AMENDMENT 1 (issuer, 2026-10-18 01:3xZ; CTO half SIGNED @48d6e4e72b, msg 7813, binding the COO half at sha256 `29d9e1b9ad11a73c08f8ac8225e06d958cd51e7c8a51453a95753314c5dd87c4` @17ede77bad unchanged):** the CTO half is `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CG3_GATEWAY_FUND_RELATION_CTO_HALF.md`; C-1 to C-10 of the COO half bind you. **START CONDITIONS (a) to (d) status:** (a) `cg-4` merged `290f2e9e6d`, `ce-3` merged `b77e08e198`: met; (b) `cg-2` complete, ledger CLOSED and COMMITTED (`8225380445`), the issuer read the bucket: 353 of 353 reports from the new parts carry `fund_relation`; you still print ONE newest part's column in `cg3_before.out`; (c) the pair is signed: met; (d) your own ledger entry: yours to open. **You may do step 0, the cut (step 1: the live-commit read, the three-path and two-hunk diffs, the equality and md5 controls, the tests) and write `cg3_hostowner_note.out` now; you deploy NOTHING until the issuer sends GO with site Z's answer (C-9).** Expected live commit `d077cef043` (site Z msg 35578); the md5 of the release `harvest_research.py` (`git show 290f2e9e6d:` that path) is `596c299597067fe5a8afb8e3493a0ed9`, the equality guard md5 is `6d9e0dd38166b82943d6834a0ce482b5`.
- **Own workstream** `FUNDREL-RELEASE`: each issuance of this round holds its own workstream (the gate refuses a second order into a workstream that already has an issuance at HEAD).
- **Not covered, named:** any other gateway change; the `fund_form` rebuild (`HVST-cf-3`, `-5`).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>92</round>
<workstream>FUNDREL-RELEASE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
