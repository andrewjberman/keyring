# AMGT_HARVST task order -- `HVST-cd-2` -- ROUND 89, workstream S29-SERVE-2: THE OPAL GATEWAY STOPS SERVING DOSSIER FIELDS BUILT FROM A MISFILED REPORT AND KMB IS READ ON THE SERVED TOOL WITH A CONTROL NAME (STAGED behind `HVST-cd-1` and a signed never-widen pair)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cd-2.the-gateway-stops-serving-dossier-fields-built-from-a-misfiled-report</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cd-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order.
comp-iam: RUN at L5 -- the deploy path is `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` (S3 tarball, then an SSM pull on the instance); no grant is created or widened. The BLAST RADIUS is the whole `opal-gateway` service (every MCP tool it serves restarts), which the never-widen pair below names with its rollback.
comp-adversary: RUN at L5 -- the adversary is a deploy of a tree that is not the merged one (a stale base, or other seats' unreleased gateway changes at HEAD), a served read that passes because the tool answered from a cache, a control name that is not a control (a security that has no listed report and no dossier), a half-landed deploy (NEVER-2), and a fix declared served on the deployer's own read without the surfacing seat's.
</preflight>

## 0. THE CELL

`HVST-cd-1` changes `infra/aws/ec2/opal-gateway/app/harvest_research.py` (and adds `infra/aws/ec2/opal-gateway/tests/test_cd1_dossier_misfiled.py`): `harvest_get_research` drops from `dossier_fields` and `continuation_fields` any field whose entry cites a report listed in `MISFILED_REPORTS` for that same security, and names it in the response key `misfiled_fields_excluded`. The close condition of `D1-S29` (REMEDIATION_v19) is that the surfacing seat reads the defect on the SERVED data; on 2026-10-17 the CVO read KMB on the live gateway (`319c9413a2`) and `fund_of_record` and `last_stated_position` still cite `fbd50086c4065785`. This cell deploys the gateway from the merged tree and reads KMB and a control name on the served tool.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-cd-1` is `<status>complete</status>` and merged on `box/dell1` (the issuer sends GO with the merge commit).
- (b) The never-widen pair for the gateway deploy is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round89/NEVER_WIDEN_HALF_COO_CD2_GATEWAY_DOSSIER.md` (sha256 `8b5102de2a56e0c4c0874a76ec8a457c0b3de6e81dde2517e4e890b5b833a9d8`) and CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CD2_GATEWAY_DOSSIER_CTO_HALF.md`. Read both halves before you start; their conditions C-1 to C-7 bind you, including C-6 (the MCP tool-name count and `/health` read BEFORE and AFTER, equal) and the restart window stated in the ledger entry.
- (c) A deploy ledger entry is open at the start and closed at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cd2-gateway-dossier-20261017.json`). The entry holds the restart window and the before and after tool-name counts.

## 2. THE ACT (dell1)

Read `docs/deployment/` and `infra/aws/ec2/opal-gateway/deploy/` first. **THE RELEASE IS CUT ON THE LIVE BASE, NEVER ON HEAD** (other seats' unreleased gateway changes sit at HEAD, and the live gateway moved twice during round 88; `HVST-cc-7`'s record `deliverables/0.7.0_AE_CloudOps~SC1/round88/cc7_before.out` shows the cut you repeat).

0. **Before-state, read only (`cd2_before.out`):** `services.opal-gateway.deployed_commit` and `previous_deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json` and the commit the instance really runs (if they differ, STOP and file a row); the MCP tool-name count and `/health`; the previous tarball key. Then the CONTROL READ BEFORE: `harvest_get_research(security_key="UNH_US_Equity")` through the gateway as an Opal principal: print the counts of `dossier_fields` and `continuation_fields` and the `as_of` and `source_keys` (the control name is a security with no listed report; if `UNH_US_Equity` has no dossier, pick another large name and say which, with its counts).
1. **Cut** `rel-amgt-harvst-cd2` from the live deployed commit in a worktree of your own. Print `git show <HVST-cd-1 merge>^1:infra/aws/ec2/opal-gateway/app/harvest_research.py` against `git show <live>:infra/aws/ec2/opal-gateway/app/harvest_research.py`: they must be IDENTICAL (the live file is exactly the file `HVST-cd-1` started from); a difference means the live gateway changed this file, so STOP, carry nothing, tell the issuer. Carry onto the release branch ONLY the two files of `HVST-cd-1` taken from its merge (`harvest_research.py`, `tests/test_cd1_dossier_misfiled.py`); `git diff <live> rel-amgt-harvst-cd2 --name-only -- infra/aws/ec2/opal-gateway` must list exactly those two paths (print it in `cd2_before.out`; ANY other path means STOP). The release branch passes `tests/test_cd1_dossier_misfiled.py`, `tests/test_cc1_model_basis.py`, `tests/test_cc2_research_misfiled.py`, `tests/test_cc3_ticker_shaped_never_exact_on_name.py`, `tests/test_og_gt1.py`, `tests/test_og_gt3.py` and `tests/test_og_gt4.py` (a test file the live base lacks is carried whole).
2. **Cache and deploy:** run `ops/bun_cache_precheck.py` once before the build and print it (it read 77 of 77 on 2026-10-17; any other count: STOP and tell the issuer, no package is fetched). Deploy with `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` from the RELEASE BRANCH with `AGENT_NAME` set to your serial and `DEPLOY_BASE_REF` as that script requires, never a bare `aws` update. Wait for the service health check; record it and the tool-name count in `cd2_after.out`; they equal the before values (C-6).
3. **The served reads**, each through the gateway tool as an Opal principal, verbatim in `cd2_served.out` with each response's `as_of` and `source_keys`:
   - KMB: `harvest_get_research(security_key="KMB_US_Equity")` -> neither `dossier_fields` nor `continuation_fields` holds an item named `fund_of_record` or `last_stated_position`; no string anywhere in either list contains `fbd50086c4065785` or `1a3b56044db679a5`; `misfiled_fields_excluded` names the dropped fields with their `part` and `report_id`; `misfiled_reports_excluded` still names the two reports;
   - CONTROL: the same call for the control name of step 0 -> `misfiled_fields_excluded` is `[]` and the counts of `dossier_fields` and `continuation_fields` equal the step-0 counts (C-7).
4. Write `cd2_served.out` ending with exactly these three lines: `SERVED_KMB_DOSSIER=PASS|FAIL`, `SERVED_CONTROL=PASS|FAIL`, `TOOLS_AND_HEALTH_EQUAL=PASS|FAIL`. A FAIL is rolled back to the previous tarball at once if the cause is the deploy itself, and the cell stays `pending`; otherwise it is reported.
5. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Tell the issuer when the deploy has landed and again when `cd2_served.out` is written.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round89/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round89/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cd2-gateway-dossier-20261017.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cd-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round89/cd2_served.out</invocation><expect>(?m)^SERVED_KMB_DOSSIER=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cd-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round89/cd2_served.out</invocation><expect>(?m)^SERVED_CONTROL=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cd-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round89/cd2_served.out</invocation><expect>(?m)^TOOLS_AND_HEALTH_EQUAL=PASS$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cd-2.the-gateway-stops-serving-dossier-fields-built-from-a-misfiled-report.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cd-2.the-gateway-stops-serving-dossier-fields-built-from-a-misfiled-report` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cd-2.the-gateway-stops-serving-dossier-fields-built-from-a-misfiled-report.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Do not edit this order file: the issuer flips its status.
- `HVST-cc-5`'s hourly `sa` reads (Branch F stands) continue beside this order until the issuer says stop.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on `HVST-cd-1`'s merge and on the CTO half of the never-widen pair (start condition b). The receiving seat is `0.7.0_AE_CloudOps~SC1`, the AMGT CloudOps lane on dell1 (CLAUDE.md rule 34).
- Authority: CTO round-88 analysis (msg 7491) item 1 ("the proof is a live gateway read with a control name, under its own release pair"); the CVO's grade that `D1-S29` (b) is NOT fixed (`ADJUDICATION_v82.md`). After `AC1` to `AC3` the issuer asks `4.0.0_SA_CRO~DELL1` (the surfacing seat) to read KMB itself.
- **Not covered, named:** a silver or gold REBUILD that re-derives the KMB dossier without the misfiled reports (the true remedy, a later cell; this one hides the served field); `harvest_resolve_security("PG")` still has no `not_held` sign (`D1-S39`, a candidate beyond the CTO's three items); adding `KIMBERA MM` to the universe.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>staged</status>
<round>89</round>
<workstream>S29-SERVE-2</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
