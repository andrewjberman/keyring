# NFRA_OPLGTW task order -- `OG-rl-4` -- the next opal-gateway release on live 4231bd2ddc: audit fields, symmetric shared-value refusal, .env shape, roster count, Tax identity host-side, contract pinned

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change: the host role already reads gateway/principals/rosters (gateway-read-secrets.tf, OG-pr-1; 4 ARNs since OG-rl-3).
comp-adversary: DECLARED-NOT-APPLICABLE -- the payload is the CTO's enrichment list (analysis round 12 s.5 item 2, amended by analysis round 13 s.4 item 2 @fea5fbcdbf and addendum @b100b15b2e).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, Secrets Manager) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-rl-4` (decomposition addendum R3-T.7, item 2)

Handed only after BOTH `OG-au-1` (audit fields) and `OG-sr-1` (symmetric shared-value refusal) are drained to CLOUD.
Pattern: your OG-tr-1 and OG-rl-3 records (`ANNOUNCE_OG-tr-1.md`, `ANNOUNCE_OG-rl-3.md`) for every step. STANDING RULE
(row Z-S32): nobody sources `/opt/opal-gateway/.env` in a shell; key names only, or the base64-shipped parsers under
`deliverables/2.0.0_SA_COO~O/{trnspt,r14,hxteams}/checks/`, never a value echoed. Every worktree you cut is a SPARSE cone.

### PHASE A (pre-GO): read-only on the host; no upload, no secret written

1. **Live ref.** The manifest at HEAD names `4231bd2ddc6fd975304ed5a2c097473bdd5b41a5`; confirm by host md5 of every
   shipped file. A mismatch STOPS. Release tree `/c/tmp/og-rel9`, branch `rel-nfra-oplgtw-r14`, at that commit
   (`4231bd2ddc` is not an ancestor of CLOUD: never cut from CLOUD; a cut on `3a7d6a7dc8` would unmount `/hx/teams`).
   Audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPLGTW~15` for release-branch commits only.
2. **Audit (row Z-W15-S23).** Merge ONLY `OG-au-1`'s lines (its commits by `0.9.0_WK_NFRA_OPLGTW~19` on CLOUD) onto the
   live `app/audit.py` and `app/tools.py`, plus `tests/test_audit_bytes_principal.py`.
3. **Symmetric shared-value refusal (the CVO's post-hoc finding on OG-rl-3, analysis addendum @b100b15b2e).** Take
   `app/mail_route.py`, `app/transcript_route.py`, `tests/test_mail_route.py` and `tests/test_transcript_route.py` from
   `OG-sr-1`'s drained head on CLOUD. The live and CLOUD copies of those four files were byte-equal at the cut, so the
   result's `git diff 4231bd2ddc -- <file>` must equal `OG-sr-1`'s own diff for each file, line for line.
4. **`.env` shape (row Z-S32).** In the live `deploy-to-ec2.sh` `.env` render (one `printf`), render every value that
   can hold whitespace double-quoted, so a systemd `EnvironmentFile` and a bash parse read the SAME value. Today there
   are 4 such values: `OTP_BEARER`, `OTP_BEARER_LABELS`, `ENABLED_INTEGRATIONS`, `FIRM_ROLE_ARNS` (re-read 00:0xZ: 50 keys,
   4 whitespace values, 4 disagreeing). Key names stay unchanged at 50, including `TEAMS_BEARER` and
   `TEAMS_BEARER_LABELS`. Prove it on a rendered sample with masked values: `_env_shape_host.py`'s parse must read
   `disagreeing 0`.
5. **Roster log count (row Z-S34).** The template counts `printf '%s' ... | wc -l` (pairs minus 1) and hard-codes
   `master_admin 1 pair`. Compute both counts from the parsed roster JSON instead.
6. **Tax identity host-side.** Replace the deploying-shell input `OG_TAXSMA_WORKBOOK_IDENTITY` with a host-side read of a
   NEW key `taxsma_workbook_identity` in the existing secret `gateway/principals/rosters`. It holds one `<tid>/<oid>`
   pair, matched by the pair regex the template already has. The role already reads that secret. Extend its validator to
   admit the one new key and to refuse a malformed value with rc 3, before any `.env` write. After this, the shell
   variable is not read at all.
7. **Contract single source (row NFRA_MCPINDEX-Z-W19-S13).** The shipped `deploy/NFRA_OPLGTW_CONTRACT.json` must equal
   `org/standards/NFRA_OPLGTW_CONTRACT.json` at CLOUD HEAD. Extend `tests/test_schwab_host_inputs.py` so the release
   suite ALSO fails when the grant-writer's `build_package.py` stages the contract from any other source. Prove both with
   a planted-mutant control.
8. **Tests** on the release tree, with `AUDIT_PATH` isolated: `test_audit_bytes_principal.py`, `test_mail_route.py`,
   `test_transcript_route.py`, `test_teams_route.py`, `test_schwab_host_inputs.py`, `test_taxsma_workbook.py`,
   `test_mail_listing.py` and `test_entitlement_admin.py::test_ogz2_ac08` (LIVE + OWN = LIVE + 0).
9. **Rollback** `/c/tmp/og-rb9` at `4231bd2ddc`, built WITHOUT uploading, equal file by file to the live S3 artifact.
   Its template still reads the identity from the shell. Export it as `ANNOUNCE_OG-rl-3.md` step 6 did: from
   `%LOCALAPPDATA%/opal/og-principals/part_d_20260930.json`, via a python eval, never printed, MATCH-checked against the
   host by hash.
10. **Verify script** (row W15-S18), written now:
    - host `/health` 200; shipped md5 equal to the release bytes; tool list unchanged; `.env` key names equal to
      `r14/RL4_ENV_KEYS_BEFORE.txt` (50);
    - ONE authorized read each on `/hx/mail`, `/hx/transcripts` and `/hx/teams` with its OWN bearer (from Secrets
      Manager, in memory, never printed) returning 200: the new refusal must not fire on the distinct live values;
    - then `rl4.AC1.sh`, `trnspt/checks/tr.AC1.sh` and `hxteams/checks/ht.AC2.sh`.
11. Write `ANNOUNCE_OG-rl-4.md` with the numbers from steps 1-10 (no value, no identifier). Commit and report. Do NOT
    upload.

### PHASE B (GO): only after the issuer says GO

GO conditions: the CTO, COO AND CVO never-widen halves are SIGNED (analysis round 13, ruling 4); `OG-r-4` is complete
(its bench must not overlap the deploy); the gateway queue has been told.

12. Re-read live. If it moved, re-cut and re-run steps 1-11. Open NEVER-2 ledger `nfra-oplgtw-gateway-release-r14` with
    legs: secret key, upload, install + verify, manifest, rollback-proven. Commit the entry AND the sentinel BEFORE the
    act.
13. **Secret key.**
    - Read `gateway/principals/rosters` IN MEMORY.
    - Add `taxsma_workbook_identity` with the value whose sha256 equals the host's current `TAXSMA_WORKBOOK_IDENTITY`.
      Read the hash host-side; the value is the step-9 export.
    - `put-secret-value`, then prove every pre-existing key's value hash is unchanged.
    - Never print a value.
14. Act from `/c/tmp/og-rel9` with `OG_TAXSMA_WORKBOOK_IDENTITY` UNSET and `DEPLOY_BASE_REF=<live full sha> HALT_ACK=1
    AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~15`, through `infra/aws/ec2/safe-ec2-deploy.sh`. Capture its result lines literally.
15. Run the verify script immediately. On any failure: roll back, re-verify, close ROLLED BACK. Otherwise STOP and
    report: the issuer makes one live transcript read so `rl4.AC2` has a record to grade, and continues you after it.
16. Record `EC2_MANIFEST.json` `services.opal-gateway` by hand on the CLOUD base. Close every leg with proof, then commit.

## 2. BOUNDS

- **Untouched:** Terraform, IAM, the ALB, the instance, the identity allowlist, `app/taxsma_workbook.py` and
  `app/teams_route.py`.
- **Read only:** `safe-ec2-deploy.sh`.
- **Secrets:** none written except step 13's one key. No transcript text.
- **Never:** push, `git stash`, rebase, `checkout --` or `clean`; override a gate; call a vendor.
- REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r14.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The gateway files of steps 2-8 live on the release branch only; this cell never merges them to CLOUD. Rows: id
`NFRA_OPLGTW-Z-W15-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/rl4.AC1.sh; echo "exit=$?"</invocation><expect>(?s)RELEASE READ-BACK ARMS 4 of 4.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/rl4.AC2.sh; echo "exit=$?"</invocation><expect>(?s)bytes integer \S+ 0 True; principal is a \S+ pair True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-rl-4"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r14/checks/rl4.AC3.sh; echo "exit=$?"</invocation><expect>(?s)sentinel at HEAD=no;.*descends from 4231bd2ddc=yes;.*outside the release set 0; ms_ingest.py shipped 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: on the served host:
  - the `.env` key names are unchanged (50);
  - every value parses the same under systemd and bash;
  - the contract copy equals `org/standards`;
  - the Tax keys are non-empty.
- `AC2`: a post-release transcript read's audit record carries `bytes` and `principal`.
- `AC3`: NEVER-2 is closed; the release ships only the named files, and neither `taxsma_workbook.py` nor
  `ms_ingest.py`.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-rl-4.gateway-release-r14.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round label 14 (addendum R3-T.7, item 2): the unissued round-13 draft `OG-rl-3`, renamed, because `OG-rl-3` is now
  the `/hx/teams` release. Chained after `OG-au-1` and `OG-sr-1`; PHASE B also waits on `OG-r-4`. `OG-o-4` follows this
  cell, because its runbook names the live release.
- Halves: CTO + COO + CVO (a capability change: the symmetric refusal changes who `/hx/mail` and `/hx/transcripts`
  admit). The never-widen ask is written at PHASE A.
- Guard N1 (the CVO's half on OG-rl-3) binds every bearer rotation until this release ships the symmetric refusal; it
  lapses at this cell's close.
- Z-S41 is out of the payload: it shipped in `4231bd2ddc`.
- `.env` before-set: `deliverables/2.0.0_SA_COO~O/r14/RL4_ENV_KEYS_BEFORE.txt` (50 names, SSM b596b265, 00:0xZ).
- Pre-cut 00:2xZ: `rl4.AC1` 3 of 4 (4 values disagree under systemd vs bash); `rl4.AC3` FAIL (no ledger; live = `4231bd2ddc`);
  `rl4.AC2` FAIL on the round-13 read (no transcript read since carries either field).

<status>pending</status>
<status>complete</status>
<round>14</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
