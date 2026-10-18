# AMGT_HARVST task order -- `HVST-cj-3` -- ROUND 95, workstream SLASH-RELEASE: THE `opal-gateway` READS A SLASH KEY FROM ITS ONE STORED FORM (ONE RELEASE CARRYING `HVST-cj-2` AND `HVST-cj-6`, CUT ON THE LIVE COMMIT `aa2efa2cf3` PLUS SEVEN FILES; STAGED behind a signed never-widen pair and the host owner's notice) (CTO round-94 analysis item 1, msg 7946; his rule, msg 7978)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cj-3.the-gateway-reads-a-slash-key-from-its-one-stored-form</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cj-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order; the seat reads the scheduled-task list (step 0) for any task that deploys or restarts the gateway in its window.
comp-iam: RUN at L5 -- the deploy uses the principal the seat's existing deploy tooling already holds (`infra/aws/ec2/safe-ec2-deploy.sh`); no grant is created or widened; the only write is the deploy of one service (`opal-gateway`) and its manifest entry. The BLAST RADIUS is the gateway service for every principal on every box (a restart of about a minute), named in the never-widen pair with its rollback.
comp-adversary: RUN at L5 -- the adversary is a release cut from the CLOUD tip or from `HEAD` (35 gateway files differ from the live commit, 28 of them other workstreams'), a carried file outside the seven, a modified file whose md5 at the live commit differs from the pair's (the live file changed), a deploy without `DEPLOY_BASE_REF` equal to the live commit, a deploy before the host owner's answer, a slash-key read that returns less than before, a control key whose served bytes move, an `etfs_compare_peers` call, and a half-landed deploy (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-cj-2` (merged `c692c5dfbb`) and `HVST-cj-6` (merged `34fb405b29`) made the gateway's harvest tools read a slash key (`BP/_LN_Equity`, `NG/_LN_Equity`) from its one stored form (the partition `security_key=BP-SLASH-_LN_Equity/`), in either spelling, with the canonical raw key for the silver column; offline tests and read-only replays against the stored objects are green and were re-run by the issuer. Nothing of this is live yet: the CTO measured through the live gateway that the raw spelling returns the reports and nothing else and the encoded spelling everything but the reports. **This cell is the ONE release.** The CTO's rule (msg 7978): cut on the live base plus exactly the seven files; `DEPLOY_BASE_REF=aa2efa2cf3`; the pair lists the seven with the md5 proof for the three modified files; site Z told first; the release ref pushed to the shared lineage. **State plainly in `cj3_before.out`:** for a key with no slash nothing served changes; for the two slash keys the served record becomes whole.

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-cj-2` and `HVST-cj-6` are `<status>complete</status>` and merged (`34fb405b29`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round95/NEVER_WIDEN_HALF_COO_CJ3_GATEWAY_SLASH_RELEASE.md` (the issuer prints its sha256 in the GO) and the CTO half in `org/missions/D5/AMGT/AMGT_HARVST/ledger/` named in the GO. Read both; their conditions bind you. The order is STAGED until the issuer sends GO.
- (c) Your ledger `harvst-cj4-dossiers-nonslash` is CLOSED and COMMITTED (the dossier writes are finished: the control reads below must not move under you).
- (c2) Site Z's ap-40 release is deployed and its ledger CLOSED (the issuer says so in the GO; site Z's own sequencing, msg 35664); the CTO has confirmed the COO addendum.
- (d) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-cj3-gateway-slash-release.json`), with the window and the rollback.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act, with the md5 table. Read `docs/deployment/` and `infra/aws/ec2/opal-gateway/deploy/`. **THE RELEASE IS CUT ON THE LIVE COMMIT, NEVER ON `HEAD` AND NEVER ON THE CLOUD TIP.**
0. **Before-state, read only (`cj3_before.out`):** `services.opal-gateway.deployed_commit` and `previous_deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json`, the commit the instance runs and `/opt/opal-gateway/.deployed_commit` (all three must read the SAME commit, and it must be `3b94a83e0572f9a14851c2f229ca4aba64c7e670`, site Z's ap-40 release, once ap-40 is deployed and its ledger CLOSED, which the issuer confirms in the GO (the COO addendum `NEVER_WIDEN_ADDENDUM_COO_CJ3_REBASE_ON_AP40.md`); `aa2efa2cf3` means ap-40 has not deployed: STOP, do not cut; any other commit: STOP and file a row; fetch the commit from `origin/rel-nfra-og-ap-40-cand` or `origin/rel-nfra-og-live-aa2efa2cf3` if it is not in the store); the MCP tool-name count and `/health`; the previous tarball key; the scheduled-task list with its control (none deploys or restarts the gateway in the window); `test_og_gt8` once (expected to fail: print the result as a no-change control). Then the BEFORE reads through the gateway: (i) `harvest_get_research` for `UNH_US_Equity`, `CPA_US_Equity`, `KMB_US_Equity` and `MNST_US_Equity` with `fields` `["fund_of_record","last_stated_position"]`, printing every returned field entry, `content_sha256`, `as_of`, `dossier_key`, `continuation_key` and `source_keys`; (ii) `harvest_get_fundamentals` for `UNH_US_Equity`, each kind of consensus, reference, valuation_history, segments and price; (iii) `harvest_get_research` for `BP/_LN_Equity`, `BP-SLASH-_LN_Equity`, `NG/_LN_Equity` and `NG-SLASH-_LN_Equity` (the same `fields`), printing for each which of `dossier_key`, `continuation_key`, `ai_fill_key`, `research_reports[]` and `management_roster.bloomberg_exec_officers` are present; and `harvest_get_fundamentals` kind consensus for `BP/_LN_Equity` and `BP-SLASH-_LN_Equity`. DO NOT call `etfs_compare_peers`.
1. **Cut** `rel-amgt-harvst-cj3` from the live commit in a worktree of your own. For each of `app/harvest_research.py`, `app/harvest_figures.py` and `app/harvest_identity.py` print the md5 of `git show <live>:infra/aws/ec2/opal-gateway/<path>`: they must equal `596c299597067fe5a8afb8e3493a0ed9`, `610eb6862918d2c6695c10d2de58734f` and `9c8d1fd69ffe0594968b4acd2751fba9`; a difference means the live file changed: STOP, carry nothing, tell the issuer. Carry ONLY the seven paths of the COO half's table, by `git checkout 34fb405b29 -- <path>` for each (all under `infra/aws/ec2/opal-gateway/`), and print the md5 of each carried file against the table. `git diff --name-status <live> rel-amgt-harvst-cj3` lists exactly those seven paths (3 `M`, 4 `A`; print it). Run on the release branch: `tests/test_ce3_parts_absent_wording.py`, `tests/test_cd1_dossier_misfiled.py`, `tests/test_cc1_model_basis.py`, `tests/test_cc2_research_misfiled.py`, `tests/test_cc3_ticker_shaped_never_exact_on_name.py`, `tests/test_og_gt1.py`, `tests/test_og_gt3.py`, `tests/test_og_gt4.py`, `tests/test_cg4_report_fund_relation.py`, `tests/test_cj2_slash_key_one_form.py` and `tests/test_cj6_slash_key_other_tools.py` (75 tests expected).
1b. **The host owner is told first.** After step 1 and BEFORE the deploy write `cj3_hostowner_note.out` (release commit, the seven paths, the intended window start and end UTC, the rollback tarball) and tell the issuer. The issuer sends it to site Z through `0.0.0_AB_MSTR~DELL1` and sends GO. Do not deploy before that GO; an in-flight release on the host in your window is a STOP.
2. **Cache and deploy:** run `ops/bun_cache_precheck.py` once before the build and print it (any count other than complete: STOP, no package is fetched). Deploy with `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` from the RELEASE BRANCH with `AGENT_NAME` set to your serial and `DEPLOY_BASE_REF=<the live commit>`, never a bare `aws` update. Wait for the service health check; record it and the tool-name count in `cj3_after.out`; they equal the before values.
3. **The reads after (`cj3_served.out`):** the same reads of step 0 (i) to (iii), verbatim. Every returned entry, key, `content_sha256`, `as_of` and `source_keys` of step 0 (i) and (ii) equals the before read. The four slash-key reads of (iii) each return a `dossier_key`, a `continuation_key`, an `ai_fill_key`, at least one `research_reports[]` entry and the exec-officer roster; the consensus read for `BP/_LN_Equity` returns the same object as for `BP-SLASH-_LN_Equity`.
4. Write `cj3_served.out` ending with exactly these lines: `RELEASE_SEVEN_PATHS_AND_EQUALITY=PASS|FAIL`, `CONTROL_READS_UNCHANGED=PASS|FAIL`, `TOOLS_AND_HEALTH_EQUAL=PASS|FAIL`, `SLASH_KEYS_SERVE_WHOLE=PASS|FAIL`. A FAIL is rolled back to the previous tarball at once if the cause is the deploy itself, and the cell stays `pending`.
5. Right after the deploy tell the issuer the release branch name and commit; the issuer asks `0.0.0_AB_MSTR~DELL1` to push the ref and tells site Z. Record it in `cj3_after.out`.
6. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Tell the issuer when the cut is done (before the deploy), when the deploy has landed and when `cj3_served.out` is written.

## 3. STOPS AND EXPECTED QUESTIONS (the CTO's S51 rule: they live here, before the run; do not ask me for an answer inside the window)

- **STOP, deploy nothing, file one row and tell me:** the live commit is not `3b94a83e05` on all three readings (see step 0), or ap-40's ledger is not confirmed CLOSED in the GO; a modified file's md5 at live differs from the pair's; the diff lists a path outside the seven or a carried md5 differs; a test fails (other than `test_og_gt8`, which is expected to fail and is not a gate); the bun cache precheck is not complete; an in-flight release on the host; a control read (step 0 (i), (ii)) differs between before and after; a slash-key read returns less than before; `/health` fails or the tool-name count differs.
- **After the deploy, a difference not named here:** write it plainly (what differs, how, the read that shows it), do NOT self-grade the criterion; roll back at once if the cause is the deploy; finish the read-only steps; tell me; I rule.
- **Expected and NOT a failure:** for the two slash keys the `dossier_key`, `continuation_key`, `ai_fill_key`, exec-officer roster (raw spelling) and the reports (encoded spelling) are present after and were absent before; the printed key of a slash-key response is the raw `BP/_LN_Equity` whichever spelling was requested; `harvest_get_peers_and_scores`, filings and coverage path reads of the two keys behave as before (path components keep the caller's spelling, by design); `test_og_gt8` red before and after.
- **Window:** from my GO, the seat states its own window (start and end UTC) in the ledger; the gateway restarts for about a minute.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cj3-gateway-slash-release.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cj-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj3_served.out</invocation><expect>(?m)^RELEASE_SEVEN_PATHS_AND_EQUALITY=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cj-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj3_served.out</invocation><expect>(?m)^CONTROL_READS_UNCHANGED=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cj-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj3_served.out</invocation><expect>(?m)^TOOLS_AND_HEALTH_EQUAL=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-cj-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round95/cj3_served.out</invocation><expect>(?m)^SLASH_KEYS_SERVE_WHOLE=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the CTO's named grade for item 1 (`BP/ LN` and `NG/ LN` return the full record whichever form is requested), read through the live gateway; AC1 to AC3 are the release's own controls, as `HVST-cg-3` had them (AC2 is the proof that nothing moves for a key without a slash).
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cj-3.the-gateway-reads-a-slash-key-from-its-one-stored-form.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cj-3.the-gateway-reads-a-slash-key-from-its-one-stored-form` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cj-3.the-gateway-reads-a-slash-key-from-its-one-stored-form.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
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
- **STAGED, not sent.** It waits on the CTO half of the pair, SC1 being free (`HVST-cj-4` runs to about 11:35Z; SC1 serves a second order only between its foreground runs and I do not hand this one before `cj-4`'s ledger closes), site Z's answer and my GO. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's round-94 analysis item 1; his rule msg 7978 (cut on `aa2efa2cf3` plus exactly the seven files). The earlier rule (msg 7975, cut from the CLOUD tip) is withdrawn for this release.
- **The ARMED rows this release disarms:** `D1-W171-S1` and `-S5` (the gateway's raw-key prefixes reach nothing; the figures and identity tools): I disarm them with MY OWN served reads of the four slash-key spellings through the live gateway after `cj3_served.out`, each returning the whole record; `-S3` (the app's copy of the rule), `-S4` and `-S6` (the path-component spelling) stay ARMED for the CTO's decisions.
- **The CTO's S51 rules are applied:** every stop and expected question is section 3; I check SC1's READ ack within 10 minutes of the handing and type a nudge if there is none.
- **AMENDMENT 1 (issuer, 2026-10-18 ~09:3xZ; site Z CTO msg 35664 via MSTR msg 7990: NOT YET, its release OG-ap-40 deploys first):** the release is RE-BASED on the live commit after ap-40: `3b94a83e0572f9a14851c2f229ca4aba64c7e670` (candidate on `aa2efa2cf3`; its diff against `aa2efa2cf3` is exactly `probe_listener.py` A, `server.py` M and `tests/test_og_pr1.py` A, none of the seven). **I measured the md5 guard at `3b94a83e05`: the three modified files equal the pair's table and `harvest_keys.py` is absent** (the redo the CTO's condition asks for), written in the COO addendum `deliverables/2.0.0_SA_COO_W1/round95/NEVER_WIDEN_ADDENDUM_COO_CJ3_REBASE_ON_AP40.md`, which does not edit the COO half; I ask the CTO to confirm it. Step 0 and the STOP list now name `3b94a83e05` and the ap-40 CLOSED confirmation; `DEPLOY_BASE_REF` is the live commit read at the cut; `previous_deployed_commit` after ap-40 is `3b94a83e05`. **Nothing is handed to SC1 until ap-40's CLOSED time reaches me through MSTR.** No criterion text changed. The gate limb that graded this amendment, if any, is read from this commit's output and stated in the next note.


**COMPLETE 2026-10-18T11:0xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** seat `0.7.0_AE_CloudOps~SC1`, GO 10:38:54Z (site Z's GO: batch9 CLOSED 10:31:55Z, live `3b94a83e05`, dell1 CLEAR NOW, its CTO msg 35670 via MSTR msg 7999); cut on the live commit read three ways by the seat (`3b94a83e05`), md5 guard equal, exactly seven paths (3 `M`, 4 `A`) with carried md5 7 of 7 equal, 75 tests passed, bun precheck 77 of 77, `test_og_gt8` red as the no-change control; release `rel-amgt-harvst-cj3` = `6575999df5d22c0123abfc0c88cd1c6f1efe8c96`, parent `3b94a83e05`; **deployed 10:52:49Z** (restart 10:52:42Z, window 10:51:38Z to 10:53:20Z, one attempt rc 0) by `safe-ec2-deploy.sh opal-gateway` with `DEPLOY_BASE_REF=3b94a83e05`; ledger `harvst-cj3-gateway-slash-release` CLOSED 11:00:55Z, COMMITTED (`d3bad434c9`); deliverables `c511631840`; EC2 manifest record `5b6ed29110`. Pair: COO half `bac6670b...`, addendum `5daec4cb...`, CTO half `e8864023c3` and his addendum `6fbe19a62c`. MSTR pushed the release ref early (10:53:34Z, `origin/rel-amgt-harvst-cj3` = `6575999df5`, a ref only; site Z could not verify the commit before) and relayed my notice and the result to site Z. SC1 had not read the GO until my typed nudge (row `D1-S57`).
- **Read by me (not SC1's word):** the proof instance VALID rc 0 (re-run here); **the four slash-key spellings through the live gateway, each whole**: `BP/_LN_Equity` (dossier `as_of=2026-10-12.7daf292c4fb81806.json`, continuation `4ecc7216257f7d08`, ai_fill, 7 reports, roster), `BP-SLASH-_LN_Equity` (the same record, `content_sha256` `539d27d5...` equal), `NG/_LN_Equity` and `NG-SLASH-_LN_Equity` (the same record, `43c14ec1...` equal); BEFORE, my own reads reproduced the CTO's two halves (raw: 7 reports and nothing else; encoded: everything but the reports); `harvest_get_fundamentals` consensus for `BP/_LN_Equity` returns the bestdata object (SC1 read it refused by an argument guard before). SC1's controls (UNH, CPA, KMB, MNST research; UNH fundamentals x5) read equal before and after, `/health` 200, tool-name count 127 md5 equal: SC1's word, not re-read by me. Rows `D1-W171-S1` and `-S5` disarmed (`D1-S56`).
- **A correction of my own pair text:** the COO half said the key a tool prints is the canonical raw key; `harvest_get_research` has no top-level key field, so the printed key is not visible in its response (SC1 stated it plainly as not a failure); the canonical raw key reaches the silver compare and the body of the tools that print one. **What this does NOT prove:** the path-component tools (peers, posture, scores, filings, drafting, management, model block, publication links), which keep the caller's spelling (the CTO's rows `D1-W171-S4` and `-S6`); the other fundamentals kinds, bestdata and coverage by me; that site Z's lineage and `CLOUD` will carry `6575999df5` (not yet on either); the app's copy of the rule (`D1-W171-S3`, an open call).
- **Own workstream** `SLASH-RELEASE`.
- **Not covered, named:** the path-component tools; the standing red `test_og_gt8`; the two slash-key dossiers (`HVST-cj-5`, after this release is read).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>complete</status>
<round>95</round>
<workstream>SLASH-RELEASE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
