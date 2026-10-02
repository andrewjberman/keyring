# NFRA_OPLGTW task order -- `OG-rl-3` -- the /hx/teams gateway release on live 3a7d6a7dc8: IAM + ALB, then the narrow app release

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot release; no cron, alarm, monitor or cadence.
comp-iam: RUN -- `comp-iam role opal-gateway-role` lists secretsmanager:GetSecretValue grants; live `iam simulate-principal-policy` (ht.AC1 pre-cut, 17:5xZ): gateway/teams/bearer implicitDeny, synthetic gateway/teams/ sibling implicitDeny; gateway-read-secrets-policy holds 3 ARNs, no wildcard.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is the CTO's ruling (CTO_RULING_20261002_NFRA_OPLGTW_HX_TEAMS_RELEASE.md, msg 28599) on Andrew's word.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (Terraform, S3 upload, SSM, Secrets Manager reads) and the public gateway URL (whose /hx/teams routes call Microsoft Graph as the server-held identity; that is the product's own path).
</preflight>

## 1. THE CELL -- `OG-rl-3` (decomposition addendum R3-T.6)

Andrew-direct today: "release the gateway /hx/teams route TODAY. Andrew's first live End of Day post, 4:30-5:30 PM ET
(20:30-21:30Z), depends on it." **Live and read back before 20:30Z.** Read whole, in this order:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261002_NFRA_OPLGTW_HX_TEAMS_RELEASE.md` (the spec; M1-M6),
`org/tier1_exec/4.0.0_SA_CRO/deliverables/SITEZ_GATEWAY_RELEASE_REQUEST_HX_TEAMS_20261002.md` (the bytes, sha256 table).
Your own records are the pattern for every step: `deliverables/0.9.0_WK_NFRA_OPLGTW~15/ANNOUNCE_OG-tr-1.md` (release
tree, rollback tree, render test, verify script, deploy) and `deliverables/0.9.0_WK_NFRA_OPLGTW~18/ANNOUNCE_OG-al-1.md` (rule 35 itself) +
ledger `org/critical_paths/change_management/20261001T1752Z_nfra-oplgtw-taxsma-alb-rule_deploy_completion.md` (targeted
plan from a fresh worktree, `safe-apply` of the saved plan). STANDING RULE (row Z-S32): nobody sources
`/opt/opal-gateway/.env` in a shell; key names only, or the base64-shipped parsers under
`deliverables/2.0.0_SA_COO~O/{trnspt,r13,hxteams}/checks/`; never a value echoed. Disk is tight: every worktree you cut
is a SPARSE cone.

### PHASE A (pre-GO): no apply, no upload, no secret written

1. **Live ref.** The manifest at HEAD names `3a7d6a7dc85fe3c54a4b63b27b59055abc9adca7`; confirm by host md5 of every
   shipped file. A mismatch STOPS. It is NOT an ancestor of CLOUD HEAD (M2): never cut the release from CLOUD.
2. **Release tree** `/c/tmp/og-rel8`, branch `rel-nfra-oplgtw-hx-teams`, at `3a7d6a7dc8`. Take
   `app/teams_route.py` and `tests/test_teams_route.py` whole from `db92656c72`, and apply ONLY `db92656c72`'s own hunks
   (`git show db92656c72 -- <file>`) to the LIVE `app/config.py`, `app/server.py`, `app/taxsma_workbook.py`. Prove each
   result's sha256: the two new files equal the request's table (`f4705400...`, `d7632f56...`); for the other three,
   `git diff 3a7d6a7dc8 -- <file>` equals `db92656c72`'s hunk for that file line for line. Census against live: exactly
   these five files plus `deploy-to-ec2.sh`. Audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPLGTW~15` for
   release-branch commits only.
3. **The template edit** hand-merged onto the LIVE `deploy-to-ec2.sh`, following its `MAIL_BEARER` block: on the host,
   `TEAMS_BEARER` from `aws secretsmanager get-secret-value --secret-id gateway/teams/bearer`; REFUSE (non-zero, before
   any `.env` write or restart) when the read fails or is empty. The `.env` printf gains `TEAMS_BEARER=%s` and
   `TEAMS_BEARER_LABELS=teamsassist`; `%s` and argument counts equal; 48 -> 50 keys, every existing key unchanged.
   Synthetic render test: failed read, empty and `None` each refused before any write; a value renders both lines.
4. **Tests** on the release tree, `AUDIT_PATH` isolated: `tests/test_teams_route.py` (14), `tests/test_taxsma_workbook.py`,
   `tests/test_mail_route.py`, `tests/test_mail_listing.py`, `tests/test_entitlement_admin.py::test_ogz2_ac08` (LIVE +
   OWN = LIVE + 0: the routes are not MCP tools).
5. **Terraform** on your worktree (the CLOUD base): `infra/aws/terraform/opal-gateway/gateway-read-secrets.tf` gains a
   fourth `data "aws_secretsmanager_secret"` for `gateway/teams/bearer` and its ARN in the SAME statement (same action,
   no wildcard; the header comment says four). `hx-capability.tf` already carries `/hx/teams/*` (8e6872f265). From a
   FRESH sparse worktree of your commit, a plan `-target=aws_iam_role_policy.gw_gateway_read_secrets
   -target=aws_lb_listener_rule.hx_capability`, saved: exactly `0 to add, 2 to change, 0 to destroy`, both in place.
   Also record the untargeted plan's summary line; any other diff there is NOT applied: file a row for it.
6. **The identity the live template needs.** The live `deploy-to-ec2.sh` refuses with no `OG_TAXSMA_WORKBOOK_IDENTITY`
   in the deploying shell. Its value is `values.tenant_id + "/" + values["opalbloomberg@opalinvest.com"]` from
   `%LOCALAPPDATA%/opal/og-principals/part_d_20260930.json`, exported via a python eval, NEVER printed. Prove its sha256
   equals the sha256 of the host's current `TAXSMA_WORKBOOK_IDENTITY` (hash computed host-side; print MATCH/DIFFER only).
   DIFFER STOPS with a BLOCKING row.
7. **Rollback** `/c/tmp/og-rb8` at `3a7d6a7dc8`, built WITHOUT uploading, equal file by file to the live S3 artifact;
   the re-deploy command with `DEPLOY_BASE_REF` and the step-6 export.
8. **Verify script** written now (row W15-S18): host `/health` 200 (on the host), shipped md5 = release bytes, tool list
   unchanged, `.env` key names 48 -> 50 (the other 48 unchanged), then `ht.AC2.sh`, `ht.AC3.sh`, `ht.AC4.sh` arms 1-2.
9. Write `ANNOUNCE_OG-rl-3.md` (steps 1-8 numbers; no value, no full identifier); commit and report. Do NOT apply or
   upload.

### PHASE B (GO): only after the issuer says GO (CTO + COO halves SIGNED; the gateway queue told)

10. Re-read the live ref; if it moved, re-cut and re-run 1-9 before any act. NEVER-2 ledger `nfra-oplgtw-hx-teams-infra`
    (legs: iam, alb), entry AND sentinel committed BEFORE the apply. `safe-apply` the saved targeted plan; read
    `ht.AC1.sh` -> PASS, then close the ledger. Any other result: revert per key (fourth ARN out; rule 35 back to 2 values).
11. NEVER-2 ledger `nfra-oplgtw-hx-teams-release` (legs: upload, install + verify, manifest, rollback-proven), entry AND
    sentinel committed BEFORE the act. Act from `/c/tmp/og-rel8` with the step-6 export, `DEPLOY_BASE_REF=<live full
    sha> HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~15` through `infra/aws/ec2/safe-ec2-deploy.sh`. Capture its result
    lines literally.
12. Run the verify script immediately after the deploy returns. Any failure except AC3's GRAPH-SCOPE-MISSING: roll back,
    re-verify, close ROLLED BACK. GRAPH-SCOPE-MISSING (502, `graph_status` 403): do NOT roll back; file a BLOCKING row
    (disarm_owner `2.0.0_SA_COO~O`) and report at once.
13. Record `EC2_MANIFEST.json` `services.opal-gateway` (deployed_commit = the release head, previous `3a7d6a7dc8`) by
    hand on the CLOUD base; close every leg with proof; commit; run section 4.

## 2. BOUNDS

May touch ONLY: the opal-gateway host code and `.env`; `gateway-read-secrets-policy` (one ARN added); ALB rule 35 (one
path added). Every other route's behaviour, every other IAM statement, every other listener rule, the instance and the
identity allowlist untouched. `safe-ec2-deploy.sh` READ only. No secret written. Neither POST verb is exercised (no
Teams message is sent). Never push, `git stash`, rebase, `checkout --` or `clean`; never override a gate; no vendor call.
REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/gateway-read-secrets.tf
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-hx-teams-infra.json
org/critical_paths/.open_deploys/nfra-oplgtw-hx-teams-release.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Release-branch only, never merged to CLOUD by this cell: `deploy-to-ec2.sh` and the release tree's merged
`config.py` / `server.py` / `taxsma_workbook.py`. Rows: id `NFRA_OPLGTW-Z-W15-S<k>`, fabric `site-z`, disarm_owner
`2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after both ledger closes are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/hxteams/checks/ht.AC1.sh; echo "exit=$?"</invocation><expect>(?s)INFRA ARMS 4 of 4.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/hxteams/checks/ht.AC2.sh; echo "exit=$?"</invocation><expect>(?s)SERVED ARMS 4 of 4.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-rl-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/hxteams/checks/ht.AC3.sh; echo "exit=$?"</invocation><expect>(?s)BEARER ARMS 2 of 2.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="OG-rl-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/hxteams/checks/ht.AC4.sh; echo "exit=$?"</invocation><expect>(?s)FLOOR ARMS 4 of 4.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: IAM allowed on `gateway/teams/bearer`, implicitDeny on a synthetic `gateway/teams/` sibling, the policy exactly
  four named ARNs, rule 35 three path values.
- `AC2`: the host serves db92656c72's module, `.env` 50 keys with the Teams pair, `/hx/teams/x` refused by the app, `/`
  still 302.
- `AC3`: with the bearer, `/hx/teams/me` and `/hx/teams/chats` return 200.
- `AC4`: the regression floor (other `/hx` routes as on live, the Tax route and Z-S41 bytes), NEVER-2 closed, narrow.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-rl-3.hx-teams-release.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 13 (addendum R3-T.6), one cell. Halves: CTO (the ruling's blast-radius section, msg 28599) + COO
  (`NEVER_WIDEN_ASK_OG-rl-3_20261002.md`, signed after PHASE A).
- Pre-cut controls 17:5xZ: `ht.AC1` 1 of 4, `ht.AC2` 1 of 4 (`/hx/teams/x` 302, `.env` 48), `ht.AC3` 0 of 2 (302),
  `ht.AC4` 0 of 4.
- The ruling's AC4 "401" for `/hx/mail/x` was re-measured: live answers 404 ("Not Found", app-originated) for both
  `/hx/mail/x` and `/hx/transcripts/x`; AC4 grades "unchanged from live".

<status>pending</status>
<round>13</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
