# NFRA_OPALAI task order -- `OA-e-3` -- ROUND 2, E3: switch the Analyst on for opal_asker_query, and its NARROW release

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-e-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~10</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-line seed change and a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the existing host and role (i-07dccb1615503ac99); no IAM surface is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the widening is one named tool whose adversary read was OA-r-1's J1.
EGRESS CLASS, declared: AWS WRITE on Opal's own plane -- one S3 artifact upload and one SSM pull/restart through the existing deploy scripts. Development downloads are covered by Andrew-direct record @f8d1103a38. No vendor call.
</preflight>

## 1. THE CELL -- `OA-e-3` (round 2, decomposition section R2.1)

The Teams-facing Analyst signs in to the gateway as `opalbloomberg@opalinvest.com`. Its server-side allowlist is the
code seed `_SEED` in `infra/aws/ec2/opal-gateway/app/identity_scope.py:51-72`, and that seed does NOT name
`opal_asker_query`. The tool therefore deploys dark for the Analyst (row Z-S6's disarm of Z-S5). OA-e-1 closed the
cited-message bypass and OA-r-1 released it. This cell switches the Analyst on. The switch widens a service identity's
server-side reach, so it rides Andrew's word, G-SCOPE (record @f8d1103a38). This release is FWD-9's first exercise: the
change reaches colleagues only through Andrew's release.

**A. The build (on your slot branch, which carries OA-e-1 and OA-r-1).**
1. `app/identity_scope.py`:
   - add `"opal_asker_query"` to the `opalbloomberg@opalinvest.com` set in `_SEED`, with a one-line comment citing
     G-SCOPE, Andrew-direct record @f8d1103a38, and NFRA_OPALAI OA-e-3;
   - update frame (iv) of the module docstring (`:21-26`). The gateway now registers ONE portal-read tool,
     `opal_asker_query`, scoped to the asker by `app/asker_scope.py`, and this is its reviewed row. Every other frame
     line is byte-unchanged.
   - Add NO other tool, and write no overlay row.
2. `tests/test_identity_scope.py`:
   - add `"opal_asker_query"` to `_CONCIERGE_ALLOWED` (`:33-36`);
   - add the test `test_concierge_seed_admits_asker_query`. It asserts two things:
     - `isc.check("opalbloomberg@opalinvest.com", "opal_asker_query") is None`;
     - the seed set for that identity EQUALS the base's set plus exactly `{"opal_asker_query"}`. Write the base's ten
       names as a literal in the test: whoami, poll_addressed_teams_messages, list_chats, read_chat_messages,
       read_chat_message_images, send_chat_message, list_teams, list_channels, read_channel_messages,
       send_channel_message.
   - Every existing test keeps passing, including `test_scoped_deny_by_default`.

**B. The NARROW release**, with OA-r-1's discipline unchanged. In order:
0. **Resolve the live base BY CONTENT** over SSM (md5 of `/opt/opal-gateway/app/identity_scope.py`, `app/asker_scope.py`,
   `app/tools.py`). The expected base is OA-r-1's release commit on `rel-nfra-opalai-r2-asker-binding-gateway`, but
   prove it by md5, never by the manifest. No commit whose files ALL match: STOP, a BLOCKING row.
   - **TIE-BREAK (AMENDED, row NFRA_OPALAI-Z-S38):** app files cannot tell a release from its ancestor when only the
     deploy template differs. At the round-2 cut the host served `6a98a0553a` (OG-s-1), not its ancestor `fe94911257`,
     whose app files are byte-identical; only `deploy-to-ec2.sh` differs (measured by `2.0.0_SA_COO~O` @e992df46c4). So
     ALSO read the live `/opt/opal-gateway/.env` KEY NAMES (never values) over SSM, and keep only candidates whose
     `deploy-to-ec2.sh` `.env` template writes exactly that key set (e.g. `SPRINT_VIEW_ALLOWED_EMAILS`). If more than one
     candidate survives, the base is the newest, and you name every survivor in your report.
1. **Announce:** write `deliverables/0.9.0_WK_NFRA_OPALAI~10/ANNOUNCE_OA-e-3.md` (branch, base, release commit, ledger
   slug), commit it, STOP and report `ANNOUNCE READY`. The COO relays it through `0.0.0_AB_MSTR~Z` and continues you with
   `GO`.
2. **Release tree:**
   - `git worktree add -b rel-nfra-opalai-r2-asker-switch-on-gateway /c/tmp/oa-10-sw-rel <base>`, then cherry-pick
     `--no-commit` ONLY this cell's commit(s) from A AND OA-f-7's code commit(s) (named in the COO's continuation;
     AMENDMENT 1);
   - restore every file outside `infra/aws/ec2/opal-gateway/` to the base, and commit;
   - census: `diff --stat <base> HEAD -- infra/aws/ec2/opal-gateway` names ONLY `app/identity_scope.py`,
     `tests/test_identity_scope.py`, and OA-f-7's `app/asker_scope.py`, `tests/test_asker_nochannels.py` and the
     asker test files it touched (`tests/test_asker_scope.py`, `tests/test_asker_binding.py`,
     `tests/test_portal_grant.py`). Anything else: STOP;
   - DEPLOY TREE (AMENDMENT 1, the OA-r-1 amendment-5 route): the halt gate admits you only from a tree whose HEAD
     holds your order. So build `rel-nfra-opalai-r2-asker-switch-on-gateway-v2` at `/c/tmp/oa-10-sw-rel2` on CLOUD, with
     ONLY `infra/aws/ec2/opal-gateway` replaced by the release branch's tree. PROVE
     `HEAD:infra/aws/ec2/opal-gateway` equals the release tip's before any act. Build the rollback `-v2` the same way on
     the base's gateway tree. The -v2 branches are deploy-only and never merged;
   - the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPALAI~10` is authorized for exactly the release-branch
     commit(s). Name each use.
3. **Rollback proven before the act:** rebuild `<base>`'s artifact from a clean tree (`/c/tmp/oa-10-sw-rb`) WITHOUT
   uploading, name the redeploy command, and pre-ack the halt gate (`HALT_ACK=1`; rows NFRA_MCPORTAL-Z-S8,
   NFRA_OPALAI-Z-W8-S2). No rollback shown: no deploy.
4. **Guards:**
   - (i) the `.env` `printf` marker render;
   - (ii) on-host `/health` over SSM, 200 within 90 seconds or roll back at once;
   - (iii) the registered MCP tool list before and after must be EQUAL. The seed does not register a tool, so any
     difference means roll back.
5. **NEVER-2 ledger on THIS branch:**
   - open slug `nfra-opalai-r2-asker-switch-on-gateway` (legs: release build + upload, SSM pull + restart, manifest
     record);
   - commit the entry AND the sentinel `org/critical_paths/.open_deploys/nfra-opalai-r2-asker-switch-on-gateway.json`;
   - ACT with `cd /c/tmp/oa-10-sw-rel && bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`;
   - record `EC2_MANIFEST.json` `services.opal-gateway.deployed_commit` plus a `release_note` in words;
   - close every leg and commit the close BEFORE the AC reads.
Act outside US business hours only (row Z-S24).

## 2. BOUNDS

1. No tool other than `opal_asker_query` joins any allowlist. No overlay file edit. The upload stays client-bound
   (`identity_tool_allowlist.txt` is untouched).
2. Terraform, the ALB, the host, its role and its secrets are untouched. The deploy scripts are READ, never edited. No
   HEAD deploy.
3. If a leg fails mid-act: roll back, close the entry as rolled back, and report. Never half-landed.
4. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair, widen or route around a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/app/identity_scope.py
infra/aws/ec2/opal-gateway/tests/test_identity_scope.py
infra/aws/ec2/opal-gateway/app/asker_scope.py
infra/aws/ec2/opal-gateway/tests/test_asker_nochannels.py
infra/aws/ec2/opal-gateway/tests/test_asker_scope.py
infra/aws/ec2/opal-gateway/tests/test_asker_binding.py
infra/aws/ec2/opal-gateway/tests/test_portal_grant.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-opalai-r2-asker-switch-on-gateway.json
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~10/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`,
`infra/aws/ec2/opal-gateway/identity_tool_allowlist.txt`.
Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W10-S<k>`.

## 4. PROOF OF SPEC (literal; run from the WORKSPACE ROOT after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-e-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e3.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-e-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e3.AC2.sh; echo "exit=$?"</invocation><expect>release-branch md5 = live md5 of app/identity_scope.py (ssm status Success); live lines naming opal_asker_query>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-e-3"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/e3.AC3.sh; echo "exit=$?"</invocation><expect>named test passed=1; failed/errored=0 (tests/test_identity_scope.py at the release branch) -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~10/NFRA_OPALAI.TO-OA-e-3.asker-switch-on.proof_of_spec.json`.
Report once:
- the build commit(s);
- the base resolution (the md5 pairs);
- the census;
- the rollback;
- the `.env` render;
- the tool-list counts and their difference;
- the ledger path and commits;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E3 (Z-S6 lifted), a join cell (decomposition R2.2). G-SCOPE is GIVEN, conditioned (Andrew-direct
record @f8d1103a38).

SPAWN ONLY WHEN (continue slot `~10`):
- OA-e-3 spawns only after OA-r-1 has closed with its three negative arms passing AND 3.0.0_SA_CVO~O has graded J1
  PASS.
- OA-e-2 has drained (decomposition R2.2 join: E3 lands only after E1 and E2). MET (e29e0ddd0d).
- AMENDMENT 1: OA-f-7 has drained (the fail-closed channel rule ships in THIS release, CTO ruling msg 26343).
- AMENDMENT 1: 2.0.0_SA_COO~MI's MX-r-4 gateway ledger is CLOSED (it took the slot after OA-r-1); re-resolve the base
  after it. J1 PASS is MET (CVO @c180d84b36, relayed by CTO msg 26343).
- No other gateway deploy entry is OPEN, and the act window is outside US business hours (Z-S24).

Dry-run at base (CLOUD `c8df03c408`, ~20:5xZ):
- e3.AC1 base: FAIL as expected (0 entries).
- e3.AC2 base: FAIL as expected (no release branch; live `identity_scope.py` md5 `442c9755`, 0 live lines naming
  `opal_asker_query`, ssm Success).
- e3.AC3 base: FAIL as expected (release branch absent).

**AMENDMENT (2.0.0_SA_COO~AI, issuer licence, ~22:1xZ):** The served base at the cut is `6a98a0553a`, not `fe94911257`, and the base resolution gains the .env key-set tie-break
(row Z-S38). No criterion's expectation moves. Gate limb: to-pipeline-gate grades a MODIFIED order only on GATE (viii)
placeholders (NONE), so no limb graded this amendment.

**AMENDMENT 1 (2.0.0_SA_COO~AI, issuer licence, ~01:1xZ):** the release also ships OA-f-7 (the CTO's fail-closed ruling on
an asker grant with no portal_channels, msg 26343), so the switch-on never goes live with the open default. The census and
`<paths>` gain those files. The deploy tree follows OA-r-1 amendment 5 (CLOUD-based, gateway-tree-hash proven). The spawn
waits on OA-f-7's drain and ~MI's MX-r-4 close. No criterion moves. Gate limb: none (GATE (viii) placeholders NONE).

<status>complete</status>
<round>2</round>
<slot>~10</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
