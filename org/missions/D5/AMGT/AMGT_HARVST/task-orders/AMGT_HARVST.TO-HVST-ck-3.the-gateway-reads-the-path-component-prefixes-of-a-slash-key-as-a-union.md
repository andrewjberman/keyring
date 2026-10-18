# AMGT_HARVST task order -- `HVST-ck-3` -- ROUND 96, workstream PATHKEY-RELEASE: THE `opal-gateway` READS THE PATH-COMPONENT PREFIXES OF A SLASH KEY AS THE UNION OF THE CANONICAL AND THE LEGACY RAW PREFIX (ONE RELEASE CARRYING `HVST-ck-2`, CUT ON THE LIVE COMMIT PLUS SIX FILES; STAGED behind a signed never-widen pair and the host owner's notice) (CTO round-95 analysis section 3 item 2, enrichment items 2 and 4, msg 8025)

<!-- ===================== SEAT FACE -- read by the CloudOps seat that receives it ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ck-3.the-gateway-reads-the-path-component-prefixes-of-a-slash-key-as-a-union</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ck-3</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no scheduled task of the harvest runner is touched by this order; the seat reads the scheduled-task list (step 0) for any task that deploys or restarts the gateway in its window.
comp-iam: RUN at L5 -- the deploy uses the principal the seat's existing deploy tooling already holds (`infra/aws/ec2/safe-ec2-deploy.sh`); no grant is created or widened; the only write is the deploy of one service (`opal-gateway`) and its manifest entry. The BLAST RADIUS is the gateway service for every principal on every box (a restart of about a minute), named in the never-widen pair with its rollback.
comp-adversary: RUN at L5 -- the adversary is a release cut from the CLOUD tip or from `HEAD` (other workstreams' gateway files), a carried file outside the six, a modified file whose md5 at the live commit differs from the pair's (the live file changed, for example by site Z's round 43), a deploy without `DEPLOY_BASE_REF` equal to the live commit, a deploy before the host owner's answer, a path-component read that returns FEWER objects than before, a control key whose served bytes move or gain a `stored_spelling` field, an `etfs_compare_peers` call, and a half-landed deploy (NEVER-2).
</preflight>

## 0. THE CELL

`HVST-ck-2` (merged `5e026fa7f4`) made the gateway's path-component tools resolve a slash key (`BP/_LN_Equity`, `NG/_LN_Equity`) to its canonical spelling and read the UNION of the canonical prefix and the legacy raw prefix by name, the canonical object winning a same-name collision, each served object saying which spelling it came from; offline tests and a read-only replay against the stored objects are green and were re-run by the issuer. Nothing of this is live yet. **This cell is the ONE release.** The CTO's rule (cj-3 shape): cut on the live base plus exactly the six files; `DEPLOY_BASE_REF` the live commit; the pair lists the six with the md5 proof for the five modified files; site Z told first; the release ref pushed to the shared lineage. **State plainly in `ck3_before.out`:** for a key with no slash nothing served changes; for the two slash keys a request in either spelling now reaches the whole canonical set (and the newer canonical object where four same-name pairs differ).

## 1. START CONDITIONS (any false: DO NOT START, file one row, and the issuer reads it)

- (a) `HVST-ck-2` is `<status>complete</status>` and merged (`5e026fa7f4`).
- (b) The never-widen pair is SIGNED at the current bytes: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round96/NEVER_WIDEN_HALF_COO_CK3_GATEWAY_UNION_READ_RELEASE.md` (the issuer prints its sha256 in the GO) and the CTO half in `org/missions/D5/AMGT/AMGT_HARVST/ledger/` named in the GO. Read both; their conditions bind you. The order is STAGED until the issuer sends GO.
- (c) No other order of yours is mid-write against the harvest bucket (the control reads must not move under you); the issuer says so in the GO.
- (c2) No release of site Z is in flight on the host (its round 43 lands `6575999df5` and its own batch); the issuer says so in the GO from site Z's answer.
- (d) A deploy ledger entry is open at the start and CLOSED and COMMITTED at the end (NEVER-2; `org/critical_paths/change_management/` and the sentinel `org/critical_paths/.open_deploys/harvst-ck3-gateway-union-read-release.json`), with the window and the rollback.

## 2. THE ACT (dell1)

Read the COO half first: it is the specification of this act, with the md5 table. Read `docs/deployment/` and `infra/aws/ec2/opal-gateway/deploy/`. **THE RELEASE IS CUT ON THE LIVE COMMIT, NEVER ON `HEAD` AND NEVER ON THE CLOUD TIP.**
0. **Before-state, read only (`ck3_before.out`):** `services.opal-gateway.deployed_commit` and `previous_deployed_commit` in `infra/aws/ec2/EC2_MANIFEST.json`, the commit the instance runs and `/opt/opal-gateway/.deployed_commit` (all three must read the SAME commit, and it must be `6575999df5d22c0123abfc0c88cd1c6f1efe8c96`; any other commit: STOP, do not cut, file a row, and the issuer writes a re-base addendum; fetch the commit from `origin/rel-amgt-harvst-cj3` if it is not in the store); the MCP tool-name count and `/health`; the previous tarball key; the scheduled-task list with its control (none deploys or restarts the gateway in the window); `test_og_gt8` once (expected to fail: print the result as a no-change control). Then the BEFORE reads through the gateway: (i) `harvest_get_research` for `UNH_US_Equity`, `CPA_US_Equity`, `KMB_US_Equity` and `MNST_US_Equity` with `fields` `["fund_of_record","last_stated_position"]`, printing every returned field entry, `content_sha256`, `as_of`, `dossier_key`, `continuation_key` and `source_keys`; (ii) `harvest_get_fundamentals` for `UNH_US_Equity`, each kind of consensus, reference, valuation_history, segments and price; (iii) for `UNH_US_Equity`: `harvest_get_peers_and_scores`, `harvest_get_filing_analysis` and `harvest_security_coverage`, in full; (iv) for `BP/_LN_Equity`, `BP-SLASH-_LN_Equity`, `NG/_LN_Equity` and `NG-SLASH-_LN_Equity`: `harvest_get_peers_and_scores` (print `peers_key`, `member_count`, `object_key` of peers, scores and posture), `harvest_security_coverage` (print each dataset's `objects` and `newest`) and `harvest_get_research` (print which of `dossier_key`, `continuation_key`, `ai_fill_key`, `research_reports[]` and `management_roster.bloomberg_exec_officers` are present). DO NOT call `etfs_compare_peers`.
1. **Cut** `rel-amgt-harvst-ck3` from the live commit in a worktree of your own. For each of `app/harvest_research.py`, `app/harvest_figures.py`, `app/harvest_identity.py`, `app/harvest_keys.py` and `tests/test_cj6_slash_key_other_tools.py` print the md5 of `git show <live>:infra/aws/ec2/opal-gateway/<path>`: they must equal `bae82b93332988673a8f2eeaa0d62ab9`, `ff7ec861c59320c64ba3eac21898d452`, `bca2e8d8ee91d5ea862522b8eef3f0fd`, `9c9e46822d213fb10517eeb12132c7a4` and `ac6c6d1a90ff02c8a2daf98fded45a00`; a difference means the live file changed: STOP, carry nothing, tell the issuer. Carry ONLY the six paths of the COO half's table, by `git checkout 5e026fa7f4 -- <path>` for each (all under `infra/aws/ec2/opal-gateway/`), and print the md5 of each carried file against the table. `git diff --name-status <live> rel-amgt-harvst-ck3` lists exactly those six paths (5 `M`, 1 `A`; print it). Run on the release branch: `tests/test_ce3_parts_absent_wording.py`, `tests/test_cd1_dossier_misfiled.py`, `tests/test_cc1_model_basis.py`, `tests/test_cc2_research_misfiled.py`, `tests/test_cc3_ticker_shaped_never_exact_on_name.py`, `tests/test_og_gt1.py`, `tests/test_og_gt3.py`, `tests/test_og_gt4.py`, `tests/test_cg4_report_fund_relation.py`, `tests/test_cj2_slash_key_one_form.py`, `tests/test_cj6_slash_key_other_tools.py` and `tests/test_ck2_path_component_union_read.py` (82 tests expected: 75 + 7).
1b. **The host owner is told first.** After step 1 and BEFORE the deploy write `ck3_hostowner_note.out` (release commit, the six paths, the intended window start and end UTC, the rollback tarball) and tell the issuer. The issuer sends it to site Z through `0.0.0_AB_MSTR~DELL1` and sends GO. Do not deploy before that GO; an in-flight release on the host in your window is a STOP.
2. **Cache and deploy:** run `ops/bun_cache_precheck.py` once before the build and print it (any count other than complete: STOP, no package is fetched). Deploy with `infra/aws/ec2/safe-ec2-deploy.sh opal-gateway ...` from the RELEASE BRANCH with `AGENT_NAME` set to your serial and `DEPLOY_BASE_REF=<the live commit>`, never a bare `aws` update. Wait for the service health check; record it and the tool-name count in `ck3_after.out`; they equal the before values.
3. **The reads after (`ck3_served.out`):** the same reads of step 0 (i) to (iv), verbatim. Every returned entry, key, `content_sha256`, `as_of` and `source_keys` of step 0 (i) to (iii) equals the before read and carries no `stored_spelling`. For (iv): the raw and the encoded request of each key return the SAME peers `object_key` and `member_count` and the SAME `objects` per coverage dataset; the research record is still whole (all five present); each slash-key response carries `stored_spelling`.
4. Write `ck3_served.out` ending with exactly these lines: `RELEASE_SIX_PATHS_AND_EQUALITY=PASS|FAIL`, `CONTROL_READS_UNCHANGED=PASS|FAIL`, `TOOLS_AND_HEALTH_EQUAL=PASS|FAIL`, `UNION_READS_EQUAL_BOTH_SPELLINGS=PASS|FAIL`. A FAIL is rolled back to the previous tarball at once if the cause is the deploy itself, and the cell stays `pending`.
5. Right after the deploy tell the issuer the release branch name and commit; the issuer asks `0.0.0_AB_MSTR~DELL1` to push the ref and tells site Z. Record it in `ck3_after.out`.
6. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working. Tell the issuer when the cut is done (before the deploy), when the deploy has landed and when `ck3_served.out` is written.

## 3. STOPS AND EXPECTED QUESTIONS (the CTO's S51 rule: they live here, before the run; do not ask me for an answer inside the window)

- **STOP, deploy nothing, file one row and tell me:** the live commit is not `6575999df5` on all three readings; a modified file's md5 at live differs from the pair's; the diff lists a path outside the six or a carried md5 differs; a test fails (other than `test_og_gt8`, which is expected to fail and is not a gate); the bun cache precheck is not complete; an in-flight release on the host; a control read (step 0 (i) to (iii)) differs between before and after; a path-component read of a slash key returns FEWER objects than before; `/health` fails or the tool-name count differs.
- **After the deploy, a difference not named here:** write it plainly (what differs, how, the read that shows it), do NOT self-grade the criterion; roll back at once if the cause is the deploy; finish the read-only steps; tell me; I rule.
- **Expected and NOT a failure:** for the two slash keys the peers, model-block and coverage reads reach MORE objects in the raw spelling after than before (the raw spelling holds a subset of the canonical set); four same-name pairs now serve the canonical (newer) object in both spellings; each slash-key response gains a `stored_spelling` map; `harvest_get_research`'s record of the two keys stays whole; `test_og_gt8` red before and after.
- **Window:** from my GO, the seat states its own window (start and end UTC) in the ledger; the gateway restarts for about a minute.

Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round96/`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round96/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-ck3-gateway-union-read-release.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1, from the repo root)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ck-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round96/ck3_served.out</invocation><expect>(?m)^RELEASE_SIX_PATHS_AND_EQUALITY=PASS$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ck-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round96/ck3_served.out</invocation><expect>(?m)^CONTROL_READS_UNCHANGED=PASS$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ck-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round96/ck3_served.out</invocation><expect>(?m)^TOOLS_AND_HEALTH_EQUAL=PASS$</expect></criterion>
  <criterion id="AC4" cell_refs="HVST-ck-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round96/ck3_served.out</invocation><expect>(?m)^UNION_READS_EQUAL_BOTH_SPELLINGS=PASS$</expect></criterion>
</proof_of_spec>

- A fourth criterion, with its reason: AC4 is the CTO's named grade for item 2 ("each tool returns the same objects for both spellings of `BP/` and `NG/`") and item 4 (coverage equal for both spellings), read through the live gateway; AC1 to AC3 are the release's own controls, as `HVST-cj-3` had them (AC2 is the proof that nothing moves for a key without a slash).
- The checker reads `<expect>` as a regular expression. At the base the file does not exist (all FAIL as expected).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-ck-3.the-gateway-reads-the-path-component-prefixes-of-a-slash-key-as-a-union.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-ck-3.the-gateway-reads-the-path-component-prefixes-of-a-slash-key-as-a-union` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ck-3.the-gateway-reads-the-path-component-prefixes-of-a-slash-key-as-a-union.md`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` and report its last line.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads N insertions and 0 deletions.
- **Long runs and detached processes (CTO round-90 item 3, row `D1-S44`):** nothing in this order is a long write run; if you start any process that outlives a tool call, start it unbuffered with its stdout and exit status logged to a file, and read that file; never rely on a buffer.
- Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- **STAGED, not sent.** It waits on: the CTO half of the pair (I send the COO half and ask for it), site Z's answer and its round-43 timing (MSTR carries it), SC1 being free, and my GO. Receiving seat: `0.7.0_AE_CloudOps~SC1` (CLAUDE.md rule 34).
- Authority: the CTO's round-95 analysis (msg 8025) section 3 item 2 and enrichment items 2 and 4. The release is cut on the live commit `6575999df5` (my own `HVST-cj-3` release, a ref only on origin until site Z lands it); if site Z's round 43 deploys first the live commit moves and I write a re-base addendum as for ap-40.
- **The ARMED rows this release disarms:** `D1-W171-S6` (coverage differs between spellings): closed by the coverage equality read of AC4; `D1-W171-S4` (the path-component tools read the caller's spelling): closed by the ruling's reader change; the census rows `D1-W172-S2` to `-S5` (four same-name pairs): disarmed by my served read showing the canonical object for each pair; `-S3` (the app's copy of the rule) stays with the cross-adjudication.
- Dry run at the base: all four criteria FAIL as expected (the file does not exist).
- **COMPLETE (issuer, 2026-10-18 ~14:2xZ):** seat `0.7.0_AE_CloudOps~SC1`; site Z CLEAR 13:58Z to 15:00Z (its CTO msg 35710, COO~O msg 35711); GO msg 8072 (needed a typed nudge at 14:02:44Z, the idle-seat case); cut on the live commit `6575999df5` (all three planes), md5 guard 5 of 5 equal, exactly six paths (5 M, 1 A; 573+/30-), carried md5 6 of 6 equal, 82 tests passed (`test_cc1`, `test_cc2` and `test_cc3` absent at the live base, copied in from `5e026fa7f4` for the run only, as at `cg-3` and `cj-3`), bun precheck 77 of 77, `test_og_gt8` red as the control; release `rel-amgt-harvst-ck3` = `922ee425fea4b2cbce2beb8ca7930f3a474d877a`, parent `6575999df5`; DEPLOYED 14:07:06Z (rc 0, `DEPLOY_BASE_REF=6575999df5`); ledger `harvst-ck3-gateway-union-read-release` CLOSED 14:17:24Z, COMMITTED (`334444eea6`); manifest record `52b93de111`; deliverables `ff8f8a3830`; pair: COO half `c00567ca...`, CTO half `379693fc5b`; `origin/rel-amgt-harvst-ck3` = `922ee425fe` (MSTR's 13:56:30Z push, read by `ls-remote` at 14:18Z). READ BY ME (not SC1's word): the proof instance VALID rc 0 (re-run), `ck3_served.out` ends with four PASS lines; the live gateway after the deploy, BP/_LN_Equity against BP-SLASH-_LN_Equity: the SAME peers object (`peers/v1/BP-SLASH-_LN_Equity/2026-10-11T1125Z.json`, 12 members; the raw spelling reached 7 legacy objects with newest 09-24 before), the same scores and posture, the same coverage objects per dataset (peers 10, model block 25, ledger 17, scores 2, posture 1, filings 1; gold 39, bronze 73, derived 25, state 19), `stored_spelling` canonical in each, the filings tool the same absent record. NOT read by me: NG (SC1's read), the UNH controls (SC1's before and after, by reading, not machine-diffed), the research record for the four spellings (SC1's), the `harvest_get_fundamentals` model kind. SC1's plain limits: the release tree's naming limb cannot load so the commit used the trunk's `safe-commit` run from the release tree (gate ran, no override); the BEFORE five-present research print was not repeated. Rows disarmed by me in `D1-S61`: `D1-W171-S4`, `-S6` and `D1-W172-S2` to `-S5`; the two peers pairs are not served by name by any tool (the newest object wins) and rest on the offline arm of `ck-2`, stated in the row. `D1-S58` and `D1-S60` (the four pairs) stand INERT. Not covered, named: the raw-spelling writer (the `pull_enqueue` Lambda; round-97 Terraform cell), any migration of the legacy raw objects, the publication-links and seekingalpha prefixes (derived from a key component), the stale comments in `test_cj6` arm 3 (`D1-W172-S8`), the app's copy of the slash-key rule (`D1-W171-S3`, call `48ae`).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>complete</status>
<round>96</round>
<workstream>PATHKEY-RELEASE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
