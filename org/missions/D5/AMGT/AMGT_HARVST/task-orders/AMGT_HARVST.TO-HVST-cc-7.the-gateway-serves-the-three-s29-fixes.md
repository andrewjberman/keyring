# AMGT_HARVST task order -- `HVST-cc-7` -- ROUND 88, workstream S29-SERVE: THE OPAL GATEWAY SERVES THE D1-S29 FIXES AND EACH IS READ ON THE SERVED TOOL (STAGED behind `HVST-cc-1`, `HVST-cc-2` and `HVST-cc-3`)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cc-7.the-gateway-serves-the-three-s29-fixes</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cc-7</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order.
comp-iam: RUN at L5 -- the deploy path is `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` (S3 tarball, then an SSM pull on the instance); no grant is created or widened. The BLAST RADIUS is the whole `opal-gateway` service (every MCP tool it serves restarts), which the never-widen pair below must name with its rollback.
comp-adversary: RUN at L5 -- the adversary is a deploy of a tree that is not the merged one (a stale base), a served read that passes because the tool answered from a cache, a half-landed deploy (NEVER-2), and a fix declared served on the CRO's names without the CRO's own read.
</preflight>

## 0. THE CELL

`HVST-cc-1` (model figures carry `basis` and `figure_claim`), `HVST-cc-2` (a misfiled research report is excluded and named) and `HVST-cc-3` (a ticker-shaped query that matches no ticker slot never answers `exact` on a name) change `infra/aws/ec2/opal-gateway/app/` (`harvest_figures.py`, `harvest_research.py`, `harvest_identity.py`) and, for cc-2, `lib/research/corpus/typed.py`. The close condition of `D1-S29` (REMEDIATION_v19) is that the surfacing seat reads each defect on the SERVED data. This cell deploys the gateway from the merged tree and reads the three names on the served tools.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-cc-1`, `HVST-cc-2` and `HVST-cc-3` are `<status>complete</status>` and merged on `box/dell1` (`006828d8d5`, `44a1048df9`, `0ce056da15`); the release branch of step 0 carries their six files onto the live base.
- (b) The never-widen pair for the gateway deploy is SIGNED at the current bytes: COO half `deliverables/2.0.0_SA_COO_W1/round88/NEVER_WIDEN_HALF_COO_CC7_GATEWAY_S29.md` (sha256 `b5c79b76ca3bc1a1e913601b9ea4f924cff2999e509957ec490dd762cffde710`) and CTO half `ledger/NEVER_WIDEN_CC7_GATEWAY_S29_CTO_HALF.md` (msg 6895), with the CTO's added condition **C-6**: read the MCP tool-name count and `/health` BEFORE and AFTER, on BOTH branches; they must be equal (127 at the last release record); a different count after the deploy means a path outside the six shipped: Branch F, roll back. The gateway serves every box, so STATE THE RESTART WINDOW (start and end, UTC) in the deploy ledger entry. Read both halves before you start.
- (c) A deploy ledger entry is open at the start and closed at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cc7-gateway-s29-20261016.json`). The entry also holds the restart window and the before and after tool-name counts (C-6).

## 2. THE ACT (dell1)

Read `docs/deployment/` and `infra/aws/ec2/opal-gateway/deploy/` first. **THE RELEASE IS CUT ON THE LIVE BASE, NEVER ON HEAD** (other seats' unreleased gateway changes sit at HEAD; earlier gateway releases were cut on the live base, for example `rel-nfra-mcportal-pf`). Step 0: read `services.opal-gateway.deployed_commit` and `previous_deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json` and the commit the instance really runs, and record both in `cc7_before.out` (if they differ, STOP and file a row); cut a release branch from that live commit in a worktree of your own and carry onto it ONLY the three cells' file changes, taken from the merges `006828d8d5` (`harvest_figures.py` and `tests/test_cc1_model_basis.py`), `0ce056da15` (`harvest_identity.py` and `tests/test_cc3_ticker_shaped_never_exact_on_name.py`) and `44a1048df9` (`harvest_research.py` and `tests/test_cc2_research_misfiled.py`); `git diff <live commit>..<release branch> -- infra/aws/ec2/opal-gateway` must list exactly those six paths and no other (print it in `cc7_before.out`; ANY other path means STOP), and the release branch passes `tests/test_cc1_model_basis.py`, `tests/test_cc2_research_misfiled.py`, `tests/test_cc3_ticker_shaped_never_exact_on_name.py`, `tests/test_og_gt1.py`, `tests/test_og_gt3.py` and `tests/test_og_gt4.py` (a file the live base lacks, such as a test module, is carried whole). Then: (1) record the previous tarball key in `cc7_before.out` too; (2) deploy with `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` from the RELEASE BRANCH with `AGENT_NAME` set to your serial and `DEPLOY_BASE_REF` as that script requires, never a bare `aws` update; (3) wait for the service health check and record it in `cc7_after.out`; (4) the three SERVED reads, each through the gateway tool as an Opal principal, recorded verbatim in `cc7_served.out`:
   - `harvest_resolve_security("PG")` -> status `candidates` (not `exact`); `harvest_resolve_security("PCG")` -> `exact` `PCG_US_Equity`;
   - `harvest_get_fundamentals(security_key="UNH_US_Equity", kind="model", mnemonics=["IS_DIL_EPS_CONT_OPS","IS_EPS"])` -> every `IS_DIL_EPS_CONT_OPS` figure carries a `figure_claim` containing `NOT the reported`, and every figure carries the key `basis`;
   - `harvest_get_research(security_key="KMB_US_Equity")` -> `fbd50086c4065785` is absent from `research_reports` and the response names the exclusion (identity mismatch).
(5) Write `cc7_served.out` ending with exactly these three lines: `SERVED_RESOLVE_PG=PASS|FAIL`, `SERVED_EPS_CLAIM=PASS|FAIL`, `SERVED_KMB_RESEARCH=PASS|FAIL`. A FAIL is rolled back to the previous tarball at once if the cause is the deploy itself, and the cell stays `pending`; otherwise it is reported.

**AMENDMENT 1 (issuer, 17:4xZ; CTO ruling msg 6934): THE DASHBOARD DIST COMES FROM THE LIVE ARTIFACT; NO REBUILD, NO PACKAGE FETCH.** The deploy was refused at `ops/bun_cache_precheck.py` (dell1's bun cache holds 27 of 77 packages; row `D1-S36`). The laptop package ask is CANCELLED. The release becomes EXACTLY the live artifact plus the six Python files:
- (A) FEASIBILITY FIRST, READ ONLY (`cc7_dist_method.out`): read `deploy-to-ec2.sh` (the dashboard section, about lines 235-294) and any wrapper under `infra/aws/ec2/opal-gateway/ops/`, and write the EXACT method by which the tarball it uploads can carry the live artifact's `dashboard` dist instead of a fresh build, WITHOUT editing any gate or script (`bun_cache_precheck.py`, `deploy-to-ec2.sh`, `safe-ec2-deploy.sh`, the halt gate): an existing switch or env var, or a named wrapper. If the only way is to edit a gate or to skip the precheck by editing it, STOP and write `DIST_METHOD=needs_gate_edit`; the CTO then waits on the laptop intake. Otherwise write `DIST_METHOD=<the method in one line>`. NO world act in (A): no upload, no SSM.
- (B) THE SIGNED CONDITIONS FOR THE NEW COO HALF (the issuer writes it after (A); do NOT deploy before the new halves are signed at their bytes): (1) the `dashboard` dist's per-file sha256 in the new tarball equals the live artifact's, printed in `cc7_before.out` (download the live `opal-gateway-latest.tar.gz`, hash every file under the dist dir, hash the same files in the new tarball); (2) `tar` listing diff of the new tarball against the live artifact lists ONLY the six paths; (3) the method of (A) edits no gate; (4) C-6 and the rollback stand (tool-name count and `/health` equal before and after, restart window in the ledger, `previous_deployed_commit` as the rollback).
**AMENDMENT 1 IS WITHDRAWN (issuer, 19:2xZ):** step (A) found `DIST_METHOD=needs_gate_edit` (`cc7_dist_method.out`), so the CTO's stated fallback applies (msg 6934): wait on the laptop intake. The signed halves (COO `a84dbdc1e7`, CTO msg 6895 with C-6) stand UNCHANGED: the release is the kept branch `rel-amgt-harvst-cc7` @`b5aa696c90` on `d14445961d`, built by the standard script once the bun cache holds 77 of 77.
**AMENDMENT 2 (issuer, 19:2xZ; CTO msg 6992): THE STEP BEFORE THE DEPLOY IS THE CACHE INSTALL.** The laptop intake (CTO ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_INTAKE_NPM_TARBALL_LIMB_FOR_DELL1_BUN_20261016.md`) will deliver the verified `.tgz` pack of the 50 packages; the issuer sends GO WITH THE PACK DIRECTORY when it lands (do not look for it before). Then, in this order:
- (i) re-check each package's sha512 against `mcportal@c66ca82952`'s `bun.lock` (the 50 names and versions are in `cc7_bun_miss.txt`); print the 50 results in `cc7_cache_receipt.out`; ANY mismatch: STOP, install nothing, tell the issuer;
- (ii) run `intake_receive.py install --ecosystem npm --pack <dir> --target C:/Users/Test/.bun/install/cache` (locate the script with `comp-find`; print its exact output); the pack stays OFF git;
- (iii) run `ops/bun_cache_precheck.py` against `bun.lock` and print it: it must read 77 of 77. Write `BUN_CACHE=77_of_77` as the last line of `cc7_cache_receipt.out`; that receipt is YOUR word to redeploy. Any other count: STOP and tell the issuer;
- (iv) THEN the deploy as signed: a fresh ledger entry, the standard script from the kept release, C-6 counts and `/health` before and after, the restart window in the ledger, the three served reads. Nothing in the signed halves changes.
**AMENDMENT 3 (issuer, 22:3xZ; SC1 msg 7052, row D1-S37): THE LIVE BASE MOVED TO `4be300110e` (NFRA1, 22:01:25Z); THE SIGNED PAIR STANDS, THE CUT IS RE-DONE ON THE NEW BASE.** Both halves bind the cut to "THE LIVE DEPLOYED COMMIT read from `EC2_MANIFEST.json` and the instance" and name no hash; the six-path diff and C-6 (tool-name count and `/health` equal BEFORE and AFTER) are base-independent, and the "127" in C-6 is a record of the last release, not the control. No re-sign. Release `rel-amgt-harvst-cc7` @`b5aa696c90` (on `d14445961d`) is RETIRED; deploy nothing from it.
- (a) WAIT for the commit: `4be300110e` and its rollback target `bf9d23b518` are not on dell1; the issuer has asked `0.0.0_AB_MSTR~DELL1` to relay a push of a ref holding both. The issuer sends GO with the ref name. Do not look for it before.
- (b) On GO: re-read `EC2_MANIFEST.json` and the instance. If the live commit is still `4be300110e`, cut `rel-amgt-harvst-cc7b` from it; if it moved again, cut from whatever the manifest and instance agree on and say so. Print `git diff d14445961d <live> -- <the six paths>`: it must be EMPTY. A non-empty diff means the live gateway changed a file this order carries, so STOP, carry nothing, tell the issuer.
- (c) Carry the six files, prove `git diff <live> rel-amgt-harvst-cc7b --name-only` lists exactly those six, run the gateway tests, read the tool-name count and `/health` and print them in `cc7_before.out` (the count there is the baseline, ~103 per NFRA1's note); the bun cache is already 77 of 77 (`cc7_cache_receipt.out`; re-run the precheck once before the build).
- (d) Then the deploy as signed: a FRESH ledger entry naming `previous_deployed_commit` as the rollback, the standard script, C-6 counts and `/health` after, the three served reads in `cc7_served.out`. Branch F rolls back to the manifest's `previous_deployed_commit` read at the start.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round88/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round88/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cc7-gateway-s29-20261016.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cc-7"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round88/cc7_served.out</invocation><expect>(?m)^SERVED_RESOLVE_PG=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cc-7"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round88/cc7_served.out</invocation><expect>(?m)^SERVED_EPS_CLAIM=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cc-7"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round88/cc7_served.out</invocation><expect>(?m)^SERVED_KMB_RESEARCH=PASS$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cc-7.the-gateway-serves-the-three-s29-fixes.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cc-7.the-gateway-serves-the-three-s29-fixes` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cc-7.the-gateway-serves-the-three-s29-fixes.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on the three build cells' merges and on the never-widen pair (start condition b). The receiving seat is `0.7.0_AE_CloudOps~SC1`, the AMGT CloudOps lane on dell1 (CLAUDE.md rule 34, Andrew-direct 2026-10-16 ~15:4xZ: one CloudOps lane per macro per box). The runner hold of `HVST-cc-5` is `0.7.0_AE_CloudOps~HV1`'s, so this order does not wait on it.
- Authority: CTO round-87 analysis (msg 6766) rulings for `D1-S29` and ERRATUM 1 (msg 6780); close condition of REMEDIATION_v19 (the surfacing seat reads each on the served data). After `AC1` to `AC3` the issuer asks `4.0.0_SA_CRO~DELL1` (the surfacing seat) to read the three names itself.
- **Not covered, named:** a silver REBUILD for KMB's misfiled report (the cc-2 on-the-fly check serves without it when the stored row carries the header; otherwise a rebuild is owed and is a later cell); adding Procter & Gamble or `KIMBERA MM` to the universe; the `modelSheet.ts` label.
- **SENT 2026-10-16 ~16:5xZ** after both halves were signed (COO `a84dbdc1e7`; CTO msg 6895 with C-6). Sequence at the seat: `HVST-cc-5` runner steps first (done), then this order, `HVST-cc-4`'s Arm A' last.

COMPLETE (issuer, 2026-10-17 ~00:2xZ): deployed 00:10:31Z by 0.7.0_AE_CloudOps~SC1 from rel-amgt-harvst-cc7b @319c9413a2 on live base 4be300110e (amendment 3; the signed pair stood, no hash bound). Read by the issuer from the record: manifest deployed_commit 319c9413a2, previous 4be300110e; C-6 equal before and after (/health 200, 127 tools, names md5 9a593c84); six-path live diff empty before the cut; served reads SERVED_RESOLVE_PG, SERVED_EPS_CLAIM, SERVED_KMB_RESEARCH = PASS (cc7_served.out); checker VALID rc=0 (409995bde8). LIMITS: (1) the same KMB response still cites the excluded Mexico report in its gold-dossier fields (fund_of_record, last_stated_position), row D1-S38, outside this order's three criteria; (2) the CRO's read of the three names on the served tools is not yet made; (3) the served reads are the deployer's MCP session, one principal. Push state LOCAL.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>complete</status>
<round>88</round>
<workstream>S29-SERVE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
