# NFRA_OPLGTW task order -- `OG-s-1` -- /sprint for the owner only: the .env roster set in deploy-to-ec2.sh, shipped as a NARROW gateway release (row W3-S22)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-s-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~9</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot config change and deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the host, its role and Terraform are untouched.
comp-adversary: DECLARED-NOT-APPLICABLE -- Andrew's word, verbatim; the release shape is R-8 narrow.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM).
</preflight>

## 1. THE CELL -- `OG-s-1`

**The word (Andrew-direct 2026-09-27 ~19:5xZ).** The record is
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260927_195xZ_CTO_O_SPRINT_OWNER_ONLY_AND_BD_MFA_USE_THE_TRUST_TOKEN_ROUTE.md`
@785fc4d71f. The ask: `/sprint` for Andrew only.

**The gap.**
- The gateway's `/sprint` roster (`SPRINT_VIEW_ALLOWED_EMAILS`) is EMPTY on the host. `app/sprint_view.py:172-174` admits every signed-in tenant account when it is empty.
- `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` rewrites the host `.env` from ONE `printf` literal near :196, on every deploy, and that literal carries no such key.
- The literal already carries staff addresses the same way: `MASTER_ADMIN_EMAILS`, `WRITE_CAPABLE_EMAILS`, `DASHBOARD_OWNER_EMAILS`.

### PHASE A (pre-GO) -- no upload
1. **The edit.** In your worktree `/c/tmp/og-s1` (branch `wk-NFRA_OPLGTW-9-s1`, at CLOUD):
   - add `\nSPRINT_VIEW_ALLOWED_EMAILS=andrew@opalinvest.com` to that `printf` literal, immediately after the `DASHBOARD_OWNER_EMAILS=...` segment;
   - add NO new `%s` and change nothing else;
   - add one comment line above it citing the record path above.
   Commit it. The issuer authorizes `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPLGTW~9` for this one commit if lane-refused; name the use.
2. **The live commit, by content.** The manifest reads `deployed_commit` fe94911257. Over read-only SSM on `i-07dccb1615503ac99`, the md5 of `/opt/opal-gateway/app/{access_state,data_entitlement,server,token_broker}.py` must equal fe94911257's bytes, 4 of 4. Any mismatch: STOP, a BLOCKING row.
3. **The release tree.**
   - `git worktree add -b rel-nfra-oplgtw-sprint-owner /c/tmp/og-s1-rel fe94911257`;
   - `git checkout <your step-1 commit> -- infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`;
   - commit (the same override is authorized for this one commit).
   - Census: `git diff --stat fe94911257 HEAD -- infra/aws/ec2/opal-gateway` names exactly ONE file, `deploy-to-ec2.sh`, with 1-2 lines added.
4. **Render check.** Show:
   - the `%s` count equals the printf argument count, unchanged from fe94911257's;
   - the rendered `.env` carries `SPRINT_VIEW_ALLOWED_EMAILS=` exactly once;
   - `ENABLED_INTEGRATIONS=ycharts opal_portal globgrph` is unchanged.
   Print counts, not the address.
5. **mcportal pin.** Copy `/c/tmp/og-rel/mcportal` (at a3bff71ffa, with node_modules) to `/c/tmp/og-s1-rel/mcportal`. Record its HEAD.
6. **Rollback proven.** In `/c/tmp/og-s1-rb` at fe94911257, with mcportal at the same pin, build the live artifact WITHOUT uploading. Compare its file set with the live S3 artifact `opal-gateway-fe94911257.tar.gz`. Name the redeploy command (the OG-e-2 pattern).
7. Write `ANNOUNCE_OG-s-1.md` in your deliverables dir with steps 1-6's numbers, commit it, and report. Do NOT upload.

### PHASE B (GO) -- only after the issuer says GO
8. BEFORE reads over SSM:
   - the on-host tool-name list (expect 46);
   - `ENABLED_INTEGRATIONS` (value only; must be the literal, else STOP);
   - the process env's `SPRINT_VIEW_ALLOWED_EMAILS` count (expect 0).
   Print no other `.env` line.
9. NEVER-2 ledger, slug `nfra-oplgtw-sprint-owner-release`, on `/c/tmp/og-s1`. Open it and commit the entry + sentinel BEFORE the act.
10. ACT from `/c/tmp/og-s1-rel`: `HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~9 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
11. VERIFY on the host:
    - `/health` 200;
    - the process env carries `SPRINT_VIEW_ALLOWED_EMAILS` once with 1 entry;
    - tool list AFTER = 46, sorted diff EMPTY;
    - `ENABLED_INTEGRATIONS` unchanged;
    - app md5 4 of 4 = fe94911257 (this release changes no app file).
    Any failure: roll back, re-verify, close ROLLED BACK. Never half-landed.
12. Record `infra/aws/ec2/EC2_MANIFEST.json` on `/c/tmp/og-s1` (LF copy):
    - deployed_commit = the release commit;
    - previous = fe94911257;
    - deployed_at and deployed_by;
    - mcportal unchanged;
    - release_note.
    Close every leg; commit the close; run the criteria.

## 2. BOUNDS

1. Exactly one file changes: `deploy-to-ec2.sh`'s `.env` literal gains one key. No app code, Terraform, host role or secret. `ENABLED_INTEGRATIONS` is never changed.
2. No address appears in any committed evidence, row or log line except the one literal Andrew named, inside the script.
3. Standing: no push, no vendor call, never `git stash`. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-sprint-owner-release.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~9/**
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/**
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id `NFRA_OPLGTW-Z-W9-S<k>`,
fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-s-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/sp.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-s-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/sp.AC2.sh; echo "exit=$?"</invocation><expect>descends=yes; gateway files shipped 1, only deploy-to-ec2.sh=yes; template key occurrences=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-s-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/sp.AC3.sh; echo "exit=$?"</invocation><expect>status=Success; /health=200; sprint roster keys=1 entries=1; ENABLED_INTEGRATIONS unchanged=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~9/NFRA_OPLGTW.TO-OG-s-1.sprint-owner-only.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

# pipeline-override: Andrew-direct 2026-09-27 ~19:5xZ ("/sprint for Andrew only", record @785fc4d71f), cut by the issuer on 1.0.0_SA_CTO~O msg 20260927T200552Z; supersedes the OA-g-3 deny backfill; W3-S22 disarms on this landing.

**ISSUER NOTES:** Dry-run at base (CLOUD after @65ba2ef981):
- sp.AC1 FAIL (entry 0; SCAN DENOMINATOR 11 of 11);
- sp.AC2 FAIL (the manifest records OG-e-2's 8-file release; template key occurrences 0);
- sp.AC3 FAIL (roster keys 0, entries 0; health 200 and ENABLED_INTEGRATIONS unchanged=yes, the in-check control).

Blast radius for the never-widen halves:
- /sprint narrows from every signed-in tenant account to the one owner, by Andrew's word;
- every other route and the tool list are unchanged (46 = 46);
- rollback is the prebuilt fe94911257 artifact.

GO: both halves SIGNED; guards read from the signed half FILES, not the messages; off-hours; the issuer's announcement via `0.0.0_AB_MSTR~Z` + agentbus.

<status>pending</status>
<direct_act>true</direct_act>
<slot>~9</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
