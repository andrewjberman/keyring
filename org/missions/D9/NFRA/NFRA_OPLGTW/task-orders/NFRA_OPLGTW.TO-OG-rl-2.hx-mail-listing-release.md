# NFRA_OPLGTW task order -- `OG-rl-2` -- the NARROW gateway release of the /hx/mail listing route (train slot 5), under never-widen halves

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the bearer secret and the host role's grant exist (OG-pr-1).
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is the CTO's (PRD v1.4 C7 addendum "Release" @dabb8e1e9f).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, Secrets Manager reads) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-rl-2` (decomposition addendum R3-T.3)

`OG-hl-1` (the listing route and `deploy/mail_sender_table.txt`) is complete on CLOUD and NOT deployed. Ship it NARROW:
the live commit plus `OG-hl-1`'s own gateway commits (their messages name `OG-hl-1`), and nothing else CLOUD holds.
Read PRD `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` C7 and the v1.4 addendum whole. The release order is
the CTO's `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md` (R1, R2 C1-C6):
this is train slot 5, after NFRA_MCPINDEX MX-r-8. Your OG-rl-1 record
(`deliverables/0.9.0_WK_NFRA_OPLGTW~15/ANNOUNCE_OG-rl-1.md`) is the pattern for every step.

**Grade by CONTENT, never ancestry.** STANDING RULE (row Z-S32): nobody sources `/opt/opal-gateway/.env` in a shell; key
names only (`grep -o '^[A-Z0-9_]*='`) or `/proc/<service pid>/environ` for one named key, never echoed.

### PHASE A (pre-GO): no upload, no secret written, read-only SSM only

1. **Live commit** from the manifest at HEAD, confirmed by host md5 of every file the release ships. A mismatch STOPS.
2. **Release tree** `/c/tmp/og-rel5`, branch `rel-nfra-oplgtw-hx-mail-listing`, at the live commit: apply `OG-hl-1`'s
   gateway commits three-way onto the live bytes; pin every non-gateway path to live. Audited
   `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPLGTW~15` for release-branch commits only; name each use. Census against
   live: gateway files only, `OG-hl-1`'s files plus `deploy-to-ec2.sh`.
3. **Tests** on the release tree, `AUDIT_PATH` isolated: `tests/test_mail_listing.py`, `tests/test_mail_route.py`,
   `tests/test_transcript_route.py`, `tests/test_entitlement_admin.py::test_ogz2_ac08` (count LIVE + OWN = LIVE + 0).
4. **The template edit (row Z-S36's durable fix, CTO msg 27843).** Hand-merged onto the LIVE `deploy-to-ec2.sh`:
   - the on-host script reads `MAIL_SENDER_TABLE` from the shipped `${REMOTE_DIR}/deploy/mail_sender_table.txt` (one
     address per line, joined with commas), checks the template's address character set, and REFUSES with a message
     containing `REFUSED`, `MAIL_SENDER_TABLE` and `empty` (non-zero, before any `.env` write or restart) when the file
     is MISSING or holds no address (CTO 27852);
   - the deploying-shell `OG_MAIL_SENDER_TABLE` input goes (no longer read);
   - `%s` and argument counts stay equal; the `.env` key set is unchanged (46 -> 46); `ENABLED_INTEGRATIONS` unchanged.
   Early read: `python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/_rl2.py <release template>`
   must PASS, and FAIL on the live template.
5. **Rollback.** Build the live artifact in a clean `/c/tmp/og-rb5` WITHOUT uploading; compare with the live S3 artifact
   file by file; name the re-deploy command with `DEPLOY_BASE_REF`. If the live template still takes
   `OG_MAIL_SENDER_TABLE` from the shell, the rollback exports it from `criterion.py` (A4 of OG-rl-1).
6. Write `ANNOUNCE_OG-rl-2.md` in your deliverables with steps 1-5's numbers (no secret, no address) and the standing
   rule line; commit it and report. Do NOT upload.

### PHASE B (GO): only after the issuer says GO (both halves SIGNED, off-hours or Andrew's word, the gateway queue told)

7. Re-read the live ref; if it moved, re-cut onto it and re-run steps 1-6 before any act.
8. BEFORE reads (tool list, `ENABLED_INTEGRATIONS`, `.env` key names). NEVER-2 ledger, slug
   `nfra-oplgtw-hx-mail-listing-release` (legs: upload, install + verify, manifest, rollback-proven), entry AND sentinel
   committed BEFORE the act.
9. Act from the release tree with `DEPLOY_BASE_REF=<live full sha>`, `HALT_ACK=1`,
   `AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~15`, through `infra/aws/ec2/safe-ec2-deploy.sh`.
10. VERIFY from the host within 90 s: `/health` 200; shipped md5 = release bytes; tool list AFTER = BEFORE;
    `ENABLED_INTEGRATIONS` and the `.env` key set unchanged; `MAIL_SENDER_TABLE` holds exactly as many entries as
    `criterion.py` `DEFAULT_AUTHORS` at the cut (count only; CTO 27852); `/ms/*` and the existing `/hx/*` routes answer as before. Then `rl2.AC1.sh`. Any failure: roll back,
    re-verify, close ROLLED BACK.
11. Record `EC2_MANIFEST.json` `services.opal-gateway`; close every leg with its proof and commit.

## 2. BOUNDS

1. Terraform, IAM, the ALB, the instance and the identity allowlist untouched; `safe-ec2-deploy.sh` READ only; no secret
   is written.
2. Your worktree is named in your identity line; the release tree is `/c/tmp/og-rel5`. Never push, never `git stash`; no
   vendor call; every pytest run isolates `AUDIT_PATH`. REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-hx-mail-listing-release.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Release-branch only, never merged to CLOUD by this cell: `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`. Rows: id
`NFRA_OPLGTW-Z-W15-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/rl2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)LIST ARMS 9 of 9.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/rl2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)sentinel at HEAD=no;.*outside OG-hl-1's set 0; ms_ingest.py shipped 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-rl-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/rl2.AC3.sh; echo "exit=$?"</invocation><expect>(?s)reads deploy/mail_sender_table.txt host-side: True.*from the deploying shell: False.*empty-table refusal lines naming MAIL_SENDER_TABLE: [1-9].*bash -n rc=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the v1.4 acceptance on the SERVED route: the laptop's four checks and the issuer's two token arms, 9 conditions.
- `AC2`: NEVER-2 is closed, and the release is narrow (only `OG-hl-1`'s files plus the template; `/ms/*` unshipped).
- `AC3`: the SHIPPED template reads the sender table host-side and refuses an empty one (row Z-S36 disarmed).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-rl-2.hx-mail-listing-release.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 11, ONE issuance with `OG-hl-1`. PHASE A is handed when `OG-hl-1` is drained; PHASE B GO after MX-r-8
  lands (train slot 5) and both halves (CTO, CVO) sign against an issuer ask naming: the new public listing surface
  (the per-prefix bearer stays the only edge gate), the sender-table read moving host-side, and the rollback.
- Pre-cut controls: `rl2.AC1.sh` reads `LIST ARMS 0 of 9` (all 404, route absent); `rl2.AC3.sh` FAILs on the live
  template (no file read, shell input present, no empty-table refusal).
- `<risk>` WORLD: a deploy that adds a served surface.


## AMENDMENT A1 (issuer `2.0.0_SA_COO~O`, 2026-10-01 ~13:2xZ; `1.0.0_SA_CTO~O` msg 27852)

Graded by: no gate limb (a modification; GATE (viii) reads `<placeholders>NONE</placeholders>`). The CTO accepted the
artifact-shipped sender table over a Secrets Manager copy, on two read-back conditions now in steps 4 and 10: a MISSING
or empty file refuses before any `.env` write, and the deployed table's item count equals `criterion.py`'s at the cut.
Criteria unchanged.
<status>staged</status>
<round>11</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
