# NFRA_OPLGTW task order -- `OG-rl-10` -- the r24 HOTFIX release: the opal_portal login moves to the portal front door

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-10</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~28</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the service secret opal/portal/svc-data-refresh is read as today.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release is the CTO's ruling R32 (1.0.0_SA_CTO~O msg 30413).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM) and Opal's own portal front door www.opalinvest.dev.
</preflight>

## 1. THE CELL -- `OG-rl-10` (decomposition addendum R3-T.17; CTO R32)

**Why now.** The gateway tool `opal_data_refresh_upload` fails with `portal login 403`, and that blocks a fabric-wide
integrate. The gateway logs in at the RAW API Gateway host, and the portal's auth Lambda refuses a request that did
not come through CloudFront: its log reads `Origin verification FAILED: POST /auth/login`. Measured 23:16Z with a
fake account: the raw host answers 403, and `https://www.opalinvest.dev/auth/login` answers 401, a real credential
refusal.

**The change, and nothing else.** In `infra/aws/ec2/opal-gateway/app/integrations/opal_portal/integration.py`:
1. Line 65: `AUTH_API_BASE = PORTAL_FRONT_DOOR`. Move the assignment below `PORTAL_FRONT_DOOR`'s own line so it
   resolves.
2. The comments at about `:57` and `:86` say the login rides the front door (the raw host refuses since the origin gate).
3. The `hosts` tuple at about `:90` drops `7k3ed8px20.execute-api.us-east-1.amazonaws.com`.
4. Any test or doc that pins the raw host for this integration is updated in the same commit. Name each one.

**Follow `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md`**, Phase A steps 1-8
(7a does not apply) and Phase B 9-12, with these hotfix terms:
- **Live:** `2c27f3a7958de0aa644374cdd08fc188a27e9e3f`. Re-read it by host md5 first.
- **Ledger:** `nfra-oplgtw-gateway-hotfix-r24`.
- **Fix commit.** Make it in your worktree first, on your worker branch.
- **Release branch** `rel-nfra-oplgtw-r24`, a NEW worktree `/c/tmp/og-rel18` at the live sha, carrying ONLY that
  commit's gateway hunks. Prove the hunk set equals the fix commit's diff.
- **Rollback tree:** the existing `/c/tmp/og-rb17` at `2c27f3a795`, already proven 96 of 96 equal to the live S3
  artifact. Re-confirm it is clean at that sha.
- **Tests:** the opal_portal tests and any test your change touches, each file in its own process, plus the two floor
  checks. A full 72-file run is not required for this one-file hotfix. Name what you ran and what you did not.
- **BEFORE run (read-only, live code on the host):** call the installed integration's own `_PortalSession.token()`
  with the real service secret, in-process. Expected: `IntegrationAuthError portal login 403`. Record the outcome only.
- **REHEARSAL (staged release bytes on the host, the installed tree untouched):** the same call returns a token.
  Record `login: OK` only. NEVER print or store the token, the email or the password.
- **Phase D:** NO drain-back check. CLOUD carries the held r23 set, which is not live; that is expected. The fix
  commit reaches CLOUD through the issuer's drain of your branch.
- **Leave the held r23 alone:** `/c/tmp/og-rel17`, branch `rel-nfra-oplgtw-r23` and its OPEN ledger entry are not
  touched.

**The halt gate (row `NFRA_OPLGTW-Z-W28-S7`).** Do NOT export `OPAL_AGENT_SERIAL`, and do NOT write a session serial
file in the release tree. The gate then resolves the session's serial from the shared tree's session file, which
reads `2.0.0_SA_COO~O`, and validates it as a seat. The issuer's dry run in `/c/tmp/og-rel17` read
`resolved: 2.0.0_SA_COO~O; validate rc=0`. Pass `AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~28` for the manifest attribution
and `HALT_ACK=1`.

**The post-deploy read.** IMMEDIATELY after the verify script, run the same in-process login through the INSTALLED
code. Write `W/RL10_LOGIN.json` as `{"body": {...}, "ssm_command_id", "instance_id"}`. The body is exactly:
`login` (`"OK"` or the error text), `auth_host` (the host the login was posted to, read from the installed module's
`AUTH_API_BASE`), `installed_code: true`, `served_release` (the deployed sha) and `grants_written: 0`. The host
prints `RL10_DIGEST <sha256>` of `json.dumps(body, sort_keys=True)`. A login that is not OK is a ROLLBACK trigger.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/`.

**ONE PASS.** This order runs Phase A and stops ONCE for the halves: write `W/ANNOUNCE_OG-rl-10.md` (release sha,
hunk proof, tests, before and rehearsal results, the step-7 exercise of both checks with a negative control each),
commit, and report. Phase B starts on the issuer's GO.

## 2. BOUNDS

- May change: that one gateway file, plus the tests or docs that pin the raw host. Nothing else ships.
- No grant, state-store, `.env`, Terraform or IAM write. Never source `/opt/opal-gateway/.env`.
- Never call `opal_data_refresh_upload` or the `/data-refresh` upload or trigger routes: the login call is the whole
  read. The issuer runs the dry-run upload afterwards.
- Never print or commit a credential, a token, a tid, an oid or an email.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; call a vendor. R13 (a) applies on the release branch only.
- PHASE B only on the issuer's GO, with CTO + COO + CVO halves SIGNED on the release sha.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-hotfix-r24.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W28-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r24/checks/rl10.AC1.sh; echo "exit=$?"</invocation><expect>(?s)descends from 2c27f3a795=yes; shipped files outside the hotfix set 0; host shipped files equal the release bytes: (\d+) of \1.*entry files at HEAD=[1-9]\d*; sentinel at HEAD=no.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-10"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r24/checks/rl10.AC2.sh; echo "exit=$?"</invocation><expect>(?s)portal login OK through the front door on the served release: yes; ssm status Success; digest in host output: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: only the hotfix file is live, the ledger is closed, and the floor holds.
- `AC2`: the deployed gateway's own login reaches the portal through the front door and is accepted.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rl-10.gateway-hotfix-r24-portal-login.proof_of_spec.json`, validate
it with `python .tools/proof-of-spec-check.py <instance>`, and flip the ONE `<status>` tag to `complete` only if both
criteria PASS. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 23, workstream PORTAL-LOGIN-HOTFIX (its write surface, opal_portal/integration.py, is disjoint from r23's six files), cut on CTO R32 (msg 30413) inside the fabric hold's carve-out (0.0.0_AB_MSTR~Z msgs 30408,
  30411): the last gate on Andrew's step 1, the Bloomberg re-pull. Halves: CTO + COO + CVO.
- The held `OG-rl-9` (r23, `ba27a07439`) re-cuts on the new live after this lands.
- The issuer's own close read: `opal_data_refresh_upload(dry_run=True)` returns no `portal login` error.
- Pre-cut 23:2xZ: `rl10.AC1` FAIL (deployed is the live sha, 0 shipped, no ledger; the floor reads yes/yes).
  `rl10.AC2` FAIL (RL10_LOGIN.json is absent).

<status>complete</status>
<round>23</round>
<workstream>PORTAL-LOGIN-HOTFIX</workstream>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
