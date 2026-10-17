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
- (b) The never-widen pair for the gateway deploy is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round89/NEVER_WIDEN_HALF_COO_CD2_GATEWAY_DOSSIER.md` (sha256 `8b5102de2a56e0c4c0874a76ec8a457c0b3de6e81dde2517e4e890b5b833a9d8`) and CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_CD2_GATEWAY_DOSSIER_CTO_HALF.md` (SIGNED, msg 7494, with C-8 and C-9 added; they are steps 1b and 5 below). Read both halves before you start; their conditions C-1 to C-9 bind you, including C-6 (the MCP tool-name count and `/health` read BEFORE and AFTER, equal) and the restart window stated in the ledger entry.
- (c) A deploy ledger entry is open at the start and closed at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cd2-gateway-dossier-20261017.json`). The entry holds the restart window and the before and after tool-name counts.

## 2. THE ACT (dell1)

Read `docs/deployment/` and `infra/aws/ec2/opal-gateway/deploy/` first. **THE RELEASE IS CUT ON THE LIVE BASE, NEVER ON HEAD** (other seats' unreleased gateway changes sit at HEAD, and the live gateway moved twice during round 88; `HVST-cc-7`'s record `deliverables/0.7.0_AE_CloudOps~SC1/round88/cc7_before.out` shows the cut you repeat).

0. **Before-state, read only (`cd2_before.out`):** `services.opal-gateway.deployed_commit` and `previous_deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json` and the commit the instance really runs (if they differ, STOP and file a row); the MCP tool-name count and `/health`; the previous tarball key. Then the CONTROL READ BEFORE: `harvest_get_research(security_key="UNH_US_Equity")` through the gateway as an Opal principal: print the counts of `dossier_fields` and `continuation_fields` and the `as_of` and `source_keys` (the control name is a security with no listed report; if `UNH_US_Equity` has no dossier, pick another large name and say which, with its counts).
1. **Cut** `rel-amgt-harvst-cd2` from the live deployed commit in a worktree of your own. Print `git show <HVST-cd-1 merge>^1:infra/aws/ec2/opal-gateway/app/harvest_research.py` against `git show <live>:infra/aws/ec2/opal-gateway/app/harvest_research.py`: they must be IDENTICAL (the live file is exactly the file `HVST-cd-1` started from); a difference means the live gateway changed this file, so STOP, carry nothing, tell the issuer. Carry onto the release branch ONLY the two files of `HVST-cd-1` taken from its merge (`harvest_research.py`, `tests/test_cd1_dossier_misfiled.py`); `git diff <live> rel-amgt-harvst-cd2 --name-only -- infra/aws/ec2/opal-gateway` must list exactly those two paths (print it in `cd2_before.out`; ANY other path means STOP). The release branch passes `tests/test_cd1_dossier_misfiled.py`, `tests/test_cc1_model_basis.py`, `tests/test_cc2_research_misfiled.py`, `tests/test_cc3_ticker_shaped_never_exact_on_name.py`, `tests/test_og_gt1.py`, `tests/test_og_gt3.py` and `tests/test_og_gt4.py` (a test file the live base lacks is carried whole).
1b. **C-8 (CTO half): THE HOST OWNER IS TOLD FIRST.** After the release branch is cut and its tests pass, and BEFORE the deploy, write `cd2_hostowner_note.out` with the release commit, the two paths and the restart window you intend (start and end, UTC), and tell the issuer that it exists. The issuer sends it to site Z through `0.0.0_AB_MSTR~DELL1` and sends you GO. Do not deploy before that GO; if the GO names an in-flight release on the host in your window, wait for that one.
2. **Cache and deploy:** run `ops/bun_cache_precheck.py` once before the build and print it (it read 77 of 77 on 2026-10-17; any other count: STOP and tell the issuer, no package is fetched). Deploy with `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` from the RELEASE BRANCH with `AGENT_NAME` set to your serial and `DEPLOY_BASE_REF` as that script requires, never a bare `aws` update. Wait for the service health check; record it and the tool-name count in `cd2_after.out`; they equal the before values (C-6).
3. **The served reads**, each through the gateway tool as an Opal principal, verbatim in `cd2_served.out` with each response's `as_of` and `source_keys`:
   - KMB: `harvest_get_research(security_key="KMB_US_Equity")` -> neither `dossier_fields` nor `continuation_fields` holds an item named `fund_of_record` or `last_stated_position`; no string anywhere in either list contains `fbd50086c4065785` or `1a3b56044db679a5`; `misfiled_fields_excluded` names the dropped fields with their `part` and `report_id`; `misfiled_reports_excluded` still names the two reports;
   - CONTROL: the same call for the control name of step 0 -> `misfiled_fields_excluded` is `[]` and the counts of `dossier_fields` and `continuation_fields` equal the step-0 counts (C-7).
4. Write `cd2_served.out` ending with exactly these three lines: `SERVED_KMB_DOSSIER=PASS|FAIL`, `SERVED_CONTROL=PASS|FAIL`, `TOOLS_AND_HEALTH_EQUAL=PASS|FAIL`. A FAIL is rolled back to the previous tarball at once if the cause is the deploy itself, and the cell stays `pending`; otherwise it is reported.
5. **C-9 (CTO half): THE COMMIT REACHES THE SHARED LINEAGE.** Right after the deploy lands, tell the issuer the release branch name and commit; a push of a shared branch is reserved to the integrator, so the issuer asks `0.0.0_AB_MSTR~DELL1` to push the release ref and tells site Z to land it on its gateway lineage. Record the commit and the ask in `cd2_after.out`.
6. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Tell the issuer when the deploy has landed and again when `cd2_served.out` is written.

**AMENDMENT 1 (issuer, 12:5xZ; site Z host owner `1.0.0_SA_CTO~Z`, msg 35479, relayed by `0.0.0_AB_MSTR~DELL1` msg 7514): THE LIVE BASE IS ABOUT TO MOVE TO `948e8b47cc` (`NFRA_OPLGTW.TO-OG-ap-36`, in flight on the host, all three of its halves signed). THE SIGNED PAIR STANDS; DO NOT DEPLOY `1753c741d9`; THE CUT IS RE-DONE ON THE NEW BASE.** Both halves bind the cut to "the live deployed commit read from the manifest and the instance" and name no hash; the two-path diff, the `<merge>^1` equality, C-6 and C-7 are base-independent. No re-sign. Release `rel-amgt-harvst-cd2` @`1753c741d9` (on `9d5b712557`) is RETIRED: deploying it after ap-36 would silently revert ap-36's code.
- (a) WAIT. Do nothing on the host. Site Z sends the CLOSED time of ledger `nfra-oplgtw-gateway-release-batch6` through the issuer; the issuer sends GO. Do not look for the commit before.
- (b) On GO: re-read `EC2_MANIFEST.json` and the instance (they must agree; the expected live commit is `948e8b47cc`, fetch it from the ref the GO names) and redo step 0's before-state and the control read BEFORE on the new base. If they disagree or name another commit, STOP and tell the issuer.
- (c) Re-cut `rel-amgt-harvst-cd2b` from the live commit. Print `git show <HVST-cd-1 merge>^1:<harvest_research.py>` against `git show <live>:<harvest_research.py>`: they must be IDENTICAL; a difference means ap-36 (or another release) changed this file, so STOP, carry nothing, tell the issuer. Carry the same two files; `git diff <live> rel-amgt-harvst-cd2b --name-status` lists exactly those two paths; re-run the order's test list.
- (d) Rewrite `cd2_hostowner_note.out` for the new commit and window (the old note is superseded; keep it as `cd2_hostowner_note_v1.out`), tell the issuer, and wait for the issuer's GO again (C-8 repeats).
- (e) Deploy with `DEPLOY_BASE_REF=948e8b47cc` (or the live commit of (b)) under the stale-base guard, as the standard script requires. The rollback is the tarball of the live commit read in (b). Steps 3 to 6 and C-6 to C-9 stand unchanged; the ledger entry `harvst-cd2-gateway-dossier-20261017` stays open and gets the new base, window and rollback.

**AMENDMENT 2 (issuer, 14:4xZ; host owner `1.0.0_SA_CTO~Z` msg 35506, relayed by `0.0.0_AB_MSTR~DELL1` msg 7614): THE ORDER IS SWAPPED. AMENDMENT 1 IS SUPERSEDED: DEPLOY `1753c741d9` ON LIVE `9d5b712557` NOW.** The host owner reports `948e8b47cc` (ap-36) will never deploy (superseded by a re-cut after a trunk fix) and that `OG-ap-36` will not start Phase B until our ledger is CLOSED, then re-cuts on our new live commit. The files are disjoint. The signed pair stands unchanged; C-8 is satisfied by this answer (the host owner has the note and ruled).
- (a) Re-read `EC2_MANIFEST.json` and the instance now: both must still read `9d5b712557`. If either reads another commit, STOP, deploy nothing, tell the issuer.
- (b) Redo the control read BEFORE and the tool-name count and `/health` BEFORE (C-6, C-7); the old `cd2_before.out` values are a day-old record, not the baseline. Re-run the release branch's test list once.
- (c) THE WINDOW is stated afresh in the ledger entry (supersedes the 13:00Z to 14:00Z of the note): start no earlier than your reads of (a) and (b), end by 15:50Z. Rewrite `cd2_hostowner_note.out` as `cd2_hostowner_note_v2.out` with that window and keep the first as `cd2_hostowner_note_v1.out`.
- (d) Deploy `rel-amgt-harvst-cd2` @`1753c741d9` as cut (no re-cut), with `DEPLOY_BASE_REF=9d5b712557` under the stale-base guard, as the standard script requires. Steps 3, 4 and 6, and C-6 to C-9, stand. The rollback is `opal-gateway-9d5b712557.tar.gz`.
- (e) When the ledger is CLOSED, tell the issuer the NEW live sha and the CLOSED time in one message; the issuer sends both to the host owner through MSTR (ap-36 waits on them).

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
<status>pending</status>
<round>89</round>
<workstream>S29-SERVE-2</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
