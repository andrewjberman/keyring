# NFRA_OPALAI task order -- `OA-r-1` -- ROUND 2, E1's release: the NARROW gateway release of the asker-scoping repair

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_OPALAI/decompositions/NFRA_OPALAI_DECOMP.md</decomp_doc>
<owned_cells>OA-r-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPALAI~10</issued_to>
<issued_by>2.0.0_SA_COO~AI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the existing host and role (i-07dccb1615503ac99); no IAM surface is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release ships OA-e-1's negative arms; rule J's judgment J1 is the adversary read.
EGRESS CLASS, declared: AWS WRITE on Opal's own plane -- one S3 artifact upload and one SSM pull/restart through the existing deploy scripts. Development downloads are covered by Andrew-direct record @f8d1103a38. No vendor call.
</preflight>

## 1. THE CELL -- `OA-r-1` (round 2, decomposition section R2.1)

You built OA-e-1 on this slot's branch: `app/asker_scope.py`, `app/tools.py`, `tests/test_asker_scope.py` and
`tests/test_asker_binding.py` under `infra/aws/ec2/opal-gateway/`. Those commits are named in your OA-e-1 report and in
the COO's continuation. Ship them, and ONLY them, to the gateway host `i-07dccb1615503ac99`. One gateway deployer at a
time (CTO ruling @75117e60d6). Act outside US business hours only (row Z-S24).

In order:
0. **Resolve the live base BY CONTENT at your own cut** (never by the manifest or a branch name):
   - read the md5 of `/opt/opal-gateway/app/asker_scope.py`, `app/tools.py`, `app/identity_scope.py` and
     `app/data_entitlement.py` over SSM;
   - compare each with `git show <candidate>:infra/aws/ec2/opal-gateway/app/<file> | md5sum`, for `6a98a0553a` (served
     at the round-2 cut) and any later commit on `origin/rel-*` or local `rel-*` branches;
   - **TIE-BREAK (AMENDED, row NFRA_OPALAI-Z-S38):** app files cannot tell a release from its ancestor when only the
     deploy template differs. At the round-2 cut the host served `6a98a0553a` (OG-s-1), not its ancestor `fe94911257`,
     whose app files are byte-identical; only `deploy-to-ec2.sh` differs (measured by `2.0.0_SA_COO~O` @e992df46c4). So
     ALSO read the live `/opt/opal-gateway/.env` KEY NAMES (never values) over SSM, and keep only candidates whose
     `deploy-to-ec2.sh` `.env` template writes exactly that key set (e.g. `SPRINT_VIEW_ALLOWED_EMAILS`). If more than one
     candidate survives, the base is the newest, and you name every survivor in your report.
   - the base is the commit whose files ALL match. If none matches, STOP and file a BLOCKING row.
1. **The announcement, BEFORE touching the instance.**
   - You cannot send, so write the announcement to
     `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~10/ANNOUNCE_OA-r-1.md`: branch, base commit,
     release commit, ledger slug.
   - Commit it, then STOP and report `ANNOUNCE READY` as your final message. The COO relays it through
     `0.0.0_AB_MSTR~Z` and continues you with `GO`.
   - Do no step below the release tree's census (step 2) before `GO`.
2. **The release tree.**
   - `git worktree add -b rel-nfra-opalai-r2-asker-binding-gateway /c/tmp/oa-10-rel <base>`, then
     `git -C /c/tmp/oa-10-rel cherry-pick --no-commit` OA-e-1's commits. Restore every file outside
     `infra/aws/ec2/opal-gateway/` to the base, and commit under your serial.
   - Census: `git -C /c/tmp/oa-10-rel diff --stat <base> HEAD -- infra/aws/ec2/opal-gateway` names ONLY
     `app/asker_scope.py`, `app/tools.py`, `tests/test_asker_scope.py` and `tests/test_asker_binding.py`. Any other
     file: STOP, a BLOCKING row.
   - **The issuer authorizes the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPALAI~10` for exactly the
     release-branch commit(s).** Name each use in your report.
   - Inside the release tree, from `infra/aws/ec2/opal-gateway`, run
     `python -m pytest tests/test_asker_binding.py tests/test_asker_scope.py tests/test_identity_scope.py -rA -q` and
     save the FULL output to `deliverables/0.9.0_WK_NFRA_OPALAI~10/OA-r-1_NEGATIVE_ARMS.txt`. It must show
     `test_old_message_from_wider_person_refused`, `test_reply_to_other_chat_refused`,
     `test_group_chat_unprofiled_member_refused` and `test_same_chat_recent_message_served` PASSED. That file is the
     transcript J1 is graded on. Any failure: STOP, no deploy.
3. **Rollback proven before the act:**
   - rebuild `<base>`'s gateway artifact from a clean `<base>` tree (`/c/tmp/oa-10-rb`, branch
     `rb-nfra-opalai-r2-asker-binding-base`) WITHOUT uploading, and name the redeploy command;
   - pre-acknowledge the rollback's halt gate now: `HALT_ACK=1` when the halt gate reads 0 STOP (rows
     `NFRA_MCPORTAL-Z-S8` and `NFRA_OPALAI-Z-W8-S2`: the gate takes up to ~24 minutes, and the issuer accepts that);
   - if the rollback cannot be shown, STOP: no deploy, a BLOCKING row.
4. **Guards (from the 2026-09-25 outage, row `NFRA_MCPORTAL-Z-W2-S7`):**
   - (i) render the release tree's `.env` `printf` line locally with a distinct marker per `%s`, and show every marker
     on its own key (markers only, no secrets). Any misalignment: STOP.
   - (ii) immediately after the restart, poll `/health` ON THE HOST over SSM:
     `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:<port>/health`. The public URL sits behind the load
     balancer's Entra sign-in and always returns 302 (row NFRA_OPALAI-Z-W8-S3). If it is not 200 within 90 seconds,
     run the rollback at once, close the entry as rolled back, and stop.
   - (iii) list the registered MCP tool names on the host before and after, on-box, with the service's own venv and
     `.env`. OA-e-1 adds no tool, so the difference must be empty; a non-empty difference means roll back.
5. **NEVER-2 ledger, on THIS worktree's branch, in this order:**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-opalai-r2-asker-binding-gateway`. Legs: release build +
     upload, SSM pull + restart, manifest record. Plus the base resolution, the census, the rollback, and this order's
     path;
   - commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-opalai-r2-asker-binding-gateway.json`;
   - ACT from the release worktree with ITS scripts:
     `cd /c/tmp/oa-10-rel && bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
     If the manifest auto-commit fails (jq.exe writes CRLF), record by hand on an LF copy;
   - **record the release on THIS branch:** `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway` gets the release
     commit as `deployed_commit`, and a `release_note` naming in words the base and what CLOUD holds unreleased;
   - close every leg with its proof, and commit the close BEFORE the AC reads.

**J1 (rule J, graded by `3.0.0_SA_CVO~O` at L9, never by you).** The CVO reads `OA-r-1_NEGATIVE_ARMS.txt` and the
group-chat case in `tests/test_asker_binding.py`, and judges whether each answer's scope is the asker's own, not merely
whether the tool returned without error. Record J1 in your instance as `UNVERIFIABLE-BY-INSTRUMENT` with a
`status_reason` naming `3.0.0_SA_CVO~O`. Never write PASS or FAIL on it.

## 2. BOUNDS

1. Terraform, the ALB, the host, its role and its secrets are untouched. `safe-ec2-deploy.sh` and `deploy-to-ec2.sh`
   are READ, never edited. No HEAD deploy: only the release branch ships.
2. If a leg fails mid-act: roll back, close the entry as rolled back, and report. Never half-landed.
3. Standing rule: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with
   its measurement. Never repair, widen or route around a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/app/asker_scope.py
infra/aws/ec2/opal-gateway/app/tools.py
infra/aws/ec2/opal-gateway/tests/test_asker_scope.py
infra/aws/ec2/opal-gateway/tests/test_asker_binding.py
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-opalai-r2-asker-binding-gateway.json
org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~10/**
org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/**
</paths>

Read (never write): `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
Rows: `org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_OPALAI-Z-W10-S<k>`.

## 4. PROOF OF SPEC (literal; run from the WORKSPACE ROOT after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OA-r-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/r1.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OA-r-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/r1.AC2.sh; echo "exit=$?"</invocation><expect>release-branch md5 = live md5 of app/asker_scope.py (ssm status Success) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OA-r-1"><invocation>bash org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~AI/round2/checks/r1.AC3.sh; echo "exit=$?"</invocation><expect>release-branch md5 = live md5 of app/tools.py (ssm status Success) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="OA-r-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance to
`org/missions/D6/NFRA/NFRA_OPALAI/deliverables/0.9.0_WK_NFRA_OPALAI~10/NFRA_OPALAI.TO-OA-r-1.asker-binding-release.proof_of_spec.json`.
Report once, with:
- the base resolution (the md5 pairs);
- the census;
- the negative-arms transcript path;
- the rollback;
- the `.env` render;
- the tool-list counts and their difference;
- the ledger path and commits;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E1's release. Rule J's judgment criterion J1 sits HERE (decomposition R2.4). The COO is the single
opal-gateway deployer (@75117e60d6) and relays the announcement through MSTR. OA-g-2's discipline is carried
unchanged.

SPAWN ONLY WHEN (continue slot `~10`):
- OA-e-1 has drained to CLOUD with AC1-AC3 PASS;
- no other gateway deploy entry is OPEN (`python .tools/deploy_ledger.py list`);
- the act window is outside US business hours (Z-S24).

Dry-run at base (CLOUD `c8df03c408`, ~20:5xZ):
- r1.AC1 base: FAIL as expected (0 entries; SCAN DENOMINATOR 18 of 18).
- r1.AC2 base: FAIL as expected (no release branch; live `asker_scope.py` md5 `f21b8614`, ssm Success).
- r1.AC3 base: FAIL as expected (no release branch).

**AMENDMENT (2.0.0_SA_COO~AI, issuer licence, ~22:1xZ):** The served base at the cut is `6a98a0553a`, not `fe94911257`, and the base resolution gains the .env key-set tie-break
(row Z-S38). No criterion's expectation moves. Gate limb: to-pipeline-gate grades a MODIFIED order only on GATE (viii)
placeholders (NONE), so no limb graded this amendment.

<status>pending</status>
<round>2</round>
<slot>~10</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
