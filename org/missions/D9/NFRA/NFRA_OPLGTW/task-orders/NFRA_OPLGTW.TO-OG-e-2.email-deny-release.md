# NFRA_OPLGTW task order -- `OG-e-2` -- R2-k's SERVED step (a supplementary direct act; round 2's issuance is OG-e-1): the NARROW gateway release of OG-e-1's email-keyed deny guard

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-e-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~8</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the host, its role and Terraform are untouched; the runtime role's GetItem on the access-state table is unconditioned (terraform/opal-gateway/schwab_access_state.tf:99).
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is ruled (R-8 narrow; R2-k call 4: live base only).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM).
</preflight>

## 1. THE CELL -- `OG-e-2`

OG-e-1 (complete, drained @2d0f2dda83) built the email-keyed deny guard. It is not deployed. This cell ships it NARROW:
the live commit plus OG-e-1's own gateway commits, and nothing else CLOUD holds.

Two phases. PHASE A runs now. PHASE B runs only when the issuer says GO.

### PHASE A (pre-GO) -- no upload, no contact with the instance beyond read-only SSM
1. **The live commit.** Read `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway.deployed_commit` (it reads
   110d93fb73). Confirm it BY CONTENT over read-only SSM on instance `i-07dccb1615503ac99`: the md5 of the host's
   `/opt/opal-gateway/app/{access_state,data_entitlement,server,token_broker}.py` equals that commit's bytes, 4 of 4.
   Any mismatch: STOP, a BLOCKING row.
2. **This cell's commits.** These are the CLOUD commits touching `infra/aws/ec2/opal-gateway` whose author is exactly
   `0.9.0_WK_NFRA_OPLGTW~7` (anchor on `"0.9.0_WK_NFRA_OPLGTW~7 <"`). Expect `06eff3b73f` and `744e4468e1`. List them
   oldest first.
3. **The release tree.**
   - `git worktree add -b rel-nfra-oplgtw-email-deny /c/tmp/og-rel <live commit>`;
   - cherry-pick those commits with `--no-commit`, in order;
   - pin every NON-gateway path back to the live commit (the commits also carry a surprise-channel row);
   - commit under your serial. The issuer authorizes the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPLGTW~8` for
     exactly the release-branch commit(s). Name each use.
   - Census: `git -C /c/tmp/og-rel diff --stat <live> HEAD -- infra/aws/ec2/opal-gateway` names ONLY files those commits
     changed. Anything else: STOP, a BLOCKING row.
4. **Tests on the release tree.** Set `AUDIT_PATH=$(mktemp)` first, then run `python -m pytest tests/test_email_deny.py
   tests/test_owner_gate.py tests/test_portal_grant.py tests/test_sprint_view.py tests/test_asker_scope.py -q -p no:cacheprovider`
   in `/c/tmp/og-rel/infra/aws/ec2/opal-gateway`. Record the result. moto is not installed; do not run moto modules.
5. **mcportal pin.** `deploy-to-ec2.sh` builds the dashboard bundle from a nested `mcportal/` checkout. Clone mcportal
   into `/c/tmp/og-rel/mcportal` at the manifest's `mcportal_commit` (a3bff71ffa...). Copy `node_modules` from an
   existing clone if one exists (`/c/tmp/mx-rel/mcportal`), so `bun install` fetches nothing. Record its HEAD.
6. **Rollback proven.** In a clean tree `/c/tmp/og-rb` at the live commit, with mcportal at the same pin, build the live
   artifact WITHOUT uploading. Compare its file set with the live S3 artifact
   `s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-<live short>.tar.gz`; expect all files identical.
   Name the re-deploy command: `cd /c/tmp/og-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~8 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
7. **.env render.** `deploy-to-ec2.sh` rewrites the host `.env` from one printf near :196. Show its `%s` count equals its
   argument count. Show the rendered `ENABLED_INTEGRATIONS` literal is `ycharts opal_portal globgrph`.
8. Write `ANNOUNCE_OG-e-2.md` in your deliverables dir with steps 1-7's numbers. Commit it on your branch
   `wk-NFRA_OPLGTW-8-e2` (worktree `/c/tmp/og-e2`), and report. Do NOT upload.

### PHASE B (GO) -- only after the issuer says GO
9. Take the BEFORE reads over SSM: the on-host tool-name list (expect 46), and the `.env` `ENABLED_INTEGRATIONS` value only.
   If that value is not exactly `ycharts opal_portal globgrph`, STOP. Print no other `.env` line.
10. NEVER-2 ledger, slug `nfra-oplgtw-email-deny-release`, on `/c/tmp/og-e2`. Open it with `python .tools/deploy_ledger.py open ...`
    (legs: upload, install + verify, manifest, rollback-proven). Commit the entry AND its sentinel BEFORE the act.
11. ACT from the release tree:
    `cd /c/tmp/og-rel && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~8 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
    The wrapper's manifest auto-commit may fail on this device. Leave it unlanded and record by hand in step 13.
    `/c/tmp/og-rel/mcportal` HEAD must still be the pin before the upload.
12. VERIFY, from the host, within 90 s of the restart:
    - `/health` 200 ON THE HOST;
    - md5 of the 4 app files equals the release commit's bytes;
    - tool list AFTER = 46, sorted diff vs BEFORE EMPTY;
    - `ENABLED_INTEGRATIONS` unchanged.
    Any failure: run the rollback, re-verify health and md5 = the live commit, close the ledger ROLLED BACK. Never
    half-landed.
13. On `/c/tmp/og-e2`, on an LF copy, record `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway`:
    - `deployed_commit` = the release commit (full);
    - `previous_deployed_commit` = the live commit (full);
    - `deployed_at` and `deployed_by`;
    - `mcportal_commit` unchanged;
    - a `release_note` naming CLOUD's still-unreleased gateway commits.
    Commit it. Close every leg with its proof, commit the close, then run the criteria.

## 2. BOUNDS

1. Terraform, the ALB, the host, its role and its secrets are untouched. `safe-ec2-deploy.sh` and `deploy-to-ec2.sh` are
   READ, never edited. The `.env` `ENABLED_INTEGRATIONS` is never changed. No deny record is written by this cell (the
   backfill waits on Andrew).
2. Standing: no push, no vendor call, never `git stash`. Every pytest run isolates `AUDIT_PATH`. REFUSE a criterion you
   cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-email-deny-release.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~8/**
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id `NFRA_OPLGTW-Z-W8-S<k>`,
fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-e-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/rl.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-e-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/rl.AC2.sh; echo "exit=$?"</invocation><expect>descends=yes; gateway files shipped>=1, outside OG-e-1's set 0; email_denial carried>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-e-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/rl.AC3.sh; echo "exit=$?"</invocation><expect>status=Success; /health=200; email_denial on host>=1; ENABLED_INTEGRATIONS unchanged=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~8/NFRA_OPLGTW.TO-OG-e-2.email-deny-release.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: the SERVED step of the R2-k cell (CTO ruling @2ae58221ab, call 4: build from the live base only); OG-e-1 built the guard, this ships it narrow.

**ISSUER NOTES:** Dry-run at base (CLOUD after @ed13cfee26):
- rl.AC1 FAIL (entry 0; SCAN DENOMINATOR 11 of 11);
- rl.AC2 FAIL (the manifest still records the MX-r-3 release: 18 of 19 shipped files are outside OG-e-1's set; email_denial carried 0);
- rl.AC3 FAIL (health 200, email_denial on host 0, ENABLED_INTEGRATIONS unchanged=yes).
The host's `data_entitlement.py` md5 equals 110d93fb73's (4a248147..., read 16:4xZ).

Blast radius for the never-widen halves:
- No deny record exists until the Andrew-held backfill, so every current caller's answer is unchanged (DELTA=0) and the tool list stays 46 = 46.
- The only live change is one strongly-consistent DynamoDB GetItem per request on the 5 routes and the legacy /callback, failing closed (503) on a table outage, as ruled (call 2).
- Rollback: the prebuilt live artifact.

GO: both halves SIGNED, off-hours, and "deploying" announced by the issuer via `0.0.0_AB_MSTR~Z` + agentbus.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~8</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
