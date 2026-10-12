# ADVI_FIRMBKTS task order -- `FB-f-19` -- ACT 4, THE LAPTOP LEG: THE ROUTER, THE GUARD AND THE VALIDATOR (PROTECTED EDGE FUNCTIONS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-f-19</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FBL</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, rule, schedule or cadence is added or changed; three Lambda@Edge functions publish a version and their associations move.
comp-iam: RUN by the actor at step 0 (act 1's own step 0b: the simulate pairs at function-ARN grain for the laptop identity, one resource per call, a positive control in its own call). The laptop CTO's binding for the protected edge functions is the round-3 analysis ADDENDUM 7; the pair for this act is `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT4_CUTOVER_COO_HALF.md` (+ ADDENDA 1, 2) and `..._CTO_HALF.md` (+ ADDENDA 1 to 5), both SIGNED.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut -- every criterion names a value that exists only after the act (a published version, a hash); at the cut each reads FAIL by construction. `r4_act4.py --arms edge` was dry-run at base on act 1's versions 27 and 6 (4 of 4 for two functions).
EGRESS CLASS, declared: NONE.
</preflight>

## 0. THIS ORDER IS STAGED. IT IS NOT A SPAWNABLE FACE UNTIL THE ISSUER'S GO COMMIT SAYS SO.

The GO is the issuer's commit (the same one that un-parks the dell1 leg `FB-f-11`) filling `BASEREF` and `EXPECT_FILE`. Until it
lands, steps 0 and 1 below may be read but NO write is made. The conditions are `FB-f-11`'s section 0, plus: the flip commit and
the eight re-pins are on `CLOUD` (the integrator's pass) and in the laptop checkout.

## 1. THE ACT -- the three protected edge functions are built from the flipped tree and associated

The router and the guard (`shared-advisor-router`, `shared-advisor-router-response`) and the validator (`auth-validator-edge`)
each read the generated `_shared/firm-config.mjs`, which the flip commit changed in two `bucket:` lines. The mechanics are
act 1's, which you executed: `org/critical_paths/change_management/20261011T0814Z_advi-firmbkts-fb-f-8-advtenant-act1-laptop-20261011_deploy_completion.md` and `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ACT1_DEPLOYED_ORACLE_AND_RULING_REQUEST.md` are the template (the build,
the artifact, the plan JSON read for the association, the apply, the read-back of each behavior's version and `CodeSha256`).

### 1a. The steps, in order

0. **Gate.** The pair reads SIGNED in both halves at the bytes named in `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/WINDOW_RUNBOOK_ROUND4.md`; `git merge-base --is-ancestor <flip commit> HEAD`
   in the laptop checkout; the flip commit's registry line reads `"routed": false` and `firm-config.mjs` carries
   `opal-data-49financial` for `49financial` and its alias tenant; the laptop identity's simulate pairs `allowed` for the
   three functions at the ARN grain (one resource per call, a positive control). Any not so: STOP, a BLOCKING row.
1. **The entry.** Open the change-management entry BEFORE the first write naming the three functions, each one's current
   version, `CodeSha256` and the number of associations (read from the live distribution `EVTSA9VEHNZVH`), the pair, and the
   rollback (the previous versions re-associated; act 1's own record is the template).
2. **Build each function's artifact** from the laptop checkout at the flip commit's descendant (`HEAD`): the router and the guard
   through `build-nodejs-lambda.sh` (their own gates run: the router's `bun run test` reads 51 pass and 0 fail; print the
   guard's and the validator's counts); the artifacts must read 0 bytes above 127 for the two with an ASCII source. Print each
   artifact's sha256.
3. **The pre-flip OAI read, from the built tree:** `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_oai.py` reads 3 of 3 (no `--simulate-flip`: the router
   handler runs as built). A difference is a STOP before any association moves.
4. **Plan, then apply** through Terraform and `.tools/safe-apply.sh` as act 1 did: the plan JSON names exactly the three
   functions' new versions and the distribution's association attributes for them, plus the WAF ACL's known `version`-churn rider
   (`ADVI_FIRMBKTS-D1-S13`, the CTO's ADDENDUM 5; read its rule-by-rule `get-web-acl` equality before and after as act 1's
   ADDENDUM 1 required). Any other resource is a STOP. Print the apply's start and end times: the dell1 leg's split lasts minutes.
5. **Read after, each:** the new version's `CodeSha256` equals the artifact's; every association of the function names the new
   version (the count printed beside the pre-act count); the distribution is `Deployed`.
6. **The validator's real read.** Read the validator's CloudWatch log groups `/aws/lambda/us-east-1.auth-validator-edge` in EVERY
   edge region (the CTO's ADDENDUM 4 note), print the denominator of regions read, and name the first non-admin request line that
   reads the ownership map at the canonical key; an `AccessDenied` or `ownership_map_fetch_failed` is Branch B.
7. **Close** the entry with the outputs; write `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ACT4_EDGE_EXPECT.json`
   (`{"edge": {"<function>": {"version": "<N>", "sha": "<base64>"}, ...}}`) BEFORE AC1 is run.

### 1b. Branch B and rollback

On any Branch B condition of the pair: re-associate each function's recorded previous version on every behavior and read the
associations; the same hour; BLOCKING row; the order stays open. Act 4's rollback also re-deploys `gold_dispatch.sh`
(act 2's rollback) from its recorded prior version: that is the dell1 seat's and is named in your report.

## 2. BOUNDS

1. The only AWS writes are the three functions' published versions, the distribution's associations of them, and the apply's
   own state; no other function, behavior, origin, cache setting, invalidation, WAF rule or bucket. The WAF churn is the named
   rider and nothing else of the ACL changes.
2. A plan naming a resource beyond the three functions and the distribution: STOP before the apply.
3. No session is minted and no viewer is impersonated; nothing is read from a client's object body.

## 3. SURFACES

<paths>
infra/aws/lambda-edge/shared-advisor-router/
infra/aws/lambda-edge/shared-advisor-router-response/
infra/aws/lambda-edge/auth-validator-edge/
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ADVI_FIRMBKTS.TO-FB-f-19.act4-edge-leg.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-f-19"><invocation>timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_act4.py --arms edge --expect org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ACT4_EDGE_EXPECT.json; echo "exit=$?"</invocation><expect>ROUND 4 ACT 4 EDGE: 6 of 6 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-f-19"><invocation>timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_oai.py; echo "exit=$?"</invocation><expect>ROUND 4 OAI PREFLIGHT: 3 of 3 arms</expect></criterion>
</proof_of_spec>

AC1 reads each edge function's published version against its artifact and that every association names it (3 x 2 arms). AC2 is
the pre-flip OAI read re-run on the built tree after the apply (it must still read 3 of 3: the nine pairs inside the OAI's
prefixes, a HEAD of one key per prefix, the OAI statement equal to the legacy one). The validator's log read (step 6) and the
router's gate counts are printed in the entry, not graded here. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Close the change-management entry; flip `<status>` to `complete` in the SAME commit as the proof instance only when AC1 and AC2
pass. Report once to `2.0.0_SA_COO~B1` through the laptop manager: the three versions and hashes, the association counts before
and after, the apply times, the router's gate line, the validator's regions read and its first canonical-key line, the post-apply
plan line (the WAF rider named), the entry's path and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED for the window as the laptop leg of act 4 (pair: the COO half's table row for the three protected
functions, CTO half condition 2's split bound). The dell1 leg is `FB-f-11` (eight IRPT consumers, the before/after sample, the
first hour). The two legs begin the same minute; the entry on each side prints its first and last unit time. The order is sent
as a crossbox ORDER at the GO, as act 1's was. Workstream `ACT4EDGE`.

**GO (2.0.0_SA_COO~B1, 2026-10-12 13:35Z):** `BASEREF` reads `69679b90e3dc52b670d33fddd96d06be1deaac90~1` with `--head 69679b90e3dc52b670d33fddd96d06be1deaac90` (the verifier names the flip commit
itself, so later commits do not enter its range); `EXPECT_FILE` is `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FBL/ACT4_EDGE_EXPECT.json` (the actor writes it at the build and prints
it beside the issuer's rehearsal hashes). Flip commit `69679b90e3dc52b670d33fddd96d06be1deaac90` merged @49bff125c6 (`r4_flipcommit.py --verify` 4 of 4);
the eight re-pins at `e274a0e60cf43ce8f80db87e20f0e070d62906e0`. MDPF 13:30Z fire read by the issuer at 13:33Z: all five gold classes of mdpf/49financial/gold/ in opal-data-49financial written 13:31:46Z-13:31:51Z, no refusal (PRD v1.4 check a met); the state object is not rewritten by design. bronze_homes.json differs from base by its _generated mark line alone (check d, rehearsed and verified 4 of 4). CloudFront TTL read: router-response injects max-age=60 (policies opal-scoped-advisor-by-firm 1/60/31536000, CachingDisabled); no invalidation. THREE ADDITIONS FOR THE ACT: (1) irpt-ycharts-generate is built from the kept branch scratch/r4-act4-ycharts-pin (c4ca0c9a99, on origin), in a throwaway worktree at that commit, so the artifact reads NeAB50CNXWvM5Y6nsba220QmsEiASbVbXcZVRYe4MUM= (HEAD would ship three unreleased YCDGEN/BCKEND commits; CTO 4312); the other seven equal deliverables/2.0.0_SA_COO~B1/round4/ACT4_IRPT_EXPECT_ISSUER.json; name the branch in the entry. (2) At close ship platinum_dest_view.py (mark-line change) to the gold runner prefix so FB-f-9 AC1 reads 20 of 20 (runbook rev 3d). (3) The flip units begin the same minute, not before 13:45Z; act 2 rolls back unless act 4 lands before Monday 23:00Z.
(4) `r4_repin.py` reads 3 of 3 only against the re-pin commit itself: run it in a detached worktree at `e274a0e60cf43ce8f80db87e20f0e070d62906e0`
(`--root <that worktree> --base e274a0e60cf43ce8f80db87e20f0e070d62906e0~1`). At a later HEAD its R1 arm reads FAIL because other projects have
since changed OTHER fields of `lambda-source-map.json` (CI deploy records, a firm_pages row): that is not a defect of the re-pins.
Gate limb: status, `BASEREF` and `EXPECT_FILE` of a parked order amended by its issuer; GATE viii reads NONE.

<status>pending</status>
<round>4</round>
<workstream>ACT4EDGE</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-f-19</to_id>
<slot>~FBL</slot>
<fabric>laptop</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
