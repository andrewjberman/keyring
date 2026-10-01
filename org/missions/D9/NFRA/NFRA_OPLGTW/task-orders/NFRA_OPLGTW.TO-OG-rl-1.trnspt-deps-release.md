# NFRA_OPLGTW task order -- `OG-rl-1` -- workstream TRNSPT-DEPS: the NARROW gateway release of O1, O2, O4 and O5, under never-widen halves

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no IAM change. The two new secrets use the host's existing bearer mechanism; if PHASE A step 4 finds the host role cannot read them, that is a BLOCKING row back to the issuer (an IAM change is its own cut), never a grant here.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is the CTO's (PRD v1.2 C7: narrow, ledger, never-widen halves).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, Secrets Manager) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-rl-1` (decomposition addendum R3-T)

The build cells `OG-tx-1`, `OG-ml-1`, `OG-hr-1` and `OG-hr-2` are complete on CLOUD and NOT deployed. Ship them NARROW:
the live commit plus those cells' own gateway commits, and nothing else CLOUD holds. Read PRD
`org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.2 C7 whole.

**Grade by CONTENT, never ancestry** (row `NFRA_OPLGTW-Z-S21`). Deploy-only refs carry history without bytes.

### PHASE A (pre-GO): no upload, no secret created, read-only SSM only

1. **Live commit.** Read `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway.deployed_commit` and confirm it by
   host md5 over read-only SSM for every app file the release touches. Any mismatch STOPS with a BLOCKING row.
2. **Release tree.** `git worktree add -b rel-nfra-oplgtw-trnspt-deps /c/tmp/og-rel3 <live>`.
   - Apply the four build cells' gateway commits (authors `0.9.0_WK_NFRA_OPLGTW~15 <` and `~16 <`) by diff, oldest
     first.
   - Pin every non-gateway path to `<live>`.
   - The issuer authorizes the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPLGTW~15` for the release-branch
     commits only; name each use.
   - Census: `git diff --stat <live> HEAD -- infra/aws/ec2/opal-gateway`. It must name ONLY files the build cells
     changed, plus `deploy-to-ec2.sh`.
3. **Tests on the release tree**, with `AUDIT_PATH` isolated:
   - the build cells' 4 new test files plus the 3 adopted ones;
   - `tests/test_entitlement_admin.py::test_ogz2_ac08`;
   - `tests/test_ratelimit.py` in its own process.
4. **Secrets and host access.**
   - Read how the host gets its existing static bearers today (`OTP_BEARER`, `MS_INGEST_BEARER` in
     `deploy-to-ec2.sh`'s render), and use that same mechanism for the two new bearers.
   - Names come from `deliverables/0.9.0_WK_NFRA_OPLGTW~16/ROUTE_NAMES.json`.
   - Say whether the host role already reads them, by reading its policy. If it does not, STOP with a BLOCKING row
     that names the exact grant. This order applies no IAM change.
   - Plan the creation of both secrets (random 32 bytes, never printed). Create nothing.
5. **`.env` render.** `deploy-to-ec2.sh`'s printf has equal `%s` and argument counts. The changes are additive only:
   - the two bearers;
   - the sender table, from the issuer at GO (gate G-SENDERS: Manav's and Yang's addresses, never committed);
   - the meeting allowlist (empty until G-MEETINGS);
   - the PDF size cap.

   `ENABLED_INTEGRATIONS` and every existing key are unchanged.
6. **Rollback.** Build the live artifact in a clean `/c/tmp/og-rb3` WITHOUT uploading, and compare it with the live
   S3 artifact file by file. Name the re-deploy command with `DEPLOY_BASE_REF`.
7. Write `ANNOUNCE_OG-rl-1.md` in your deliverables with steps 1-6's numbers (no secret, no address), commit it, and
   report. Do NOT upload.

### PHASE B (GO): only after the issuer says GO (both halves SIGNED, off-hours, the gateway queue told)

8. BEFORE reads: the on-host tool list and `ENABLED_INTEGRATIONS`.
9. NEVER-2 ledger, slug `nfra-oplgtw-trnspt-deps-release`, opened with `python .tools/deploy_ledger.py open ...`
   (legs: secrets, upload, install + verify, manifest, rollback-proven). Commit the entry AND its sentinel BEFORE the
   act.
10. Create the two secrets as planned. Then act from the release tree with `DEPLOY_BASE_REF=<live full sha>`.
11. VERIFY from the host within 90 s:
    - `/health` 200;
    - md5 of the shipped files equals the release bytes;
    - the tool list AFTER equals BEFORE plus exactly the 5 new tools;
    - `ENABLED_INTEGRATIONS` unchanged;
    - `/ms/*` answers as before.

    Then run `rl.AC1.sh` (the negative arms). Any failure: roll back, re-verify, close the ledger ROLLED BACK.
12. Record `EC2_MANIFEST.json` `services.opal-gateway` (`deployed_commit`, `previous_deployed_commit`, `deployed_at`,
    `deployed_by`, `release_note`). Close every leg with its proof and commit.

## 2. BOUNDS

1. Terraform, IAM, the ALB, the instance and the identity allowlist are untouched. `safe-ec2-deploy.sh` is READ,
   never edited.
2. Your worktree is named in your identity line; the release tree is `/c/tmp/og-rel3`. Never push, never `git stash`;
   no vendor call. Every pytest run isolates `AUDIT_PATH`. REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-trnspt-deps-release.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Release-branch only, never merged to CLOUD by this cell: `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` (the additive
render lines). Rows: id `NFRA_OPLGTW-Z-W15-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/rl.AC1.sh; echo "exit=$?"</invocation><expect>(?s)ARMS 6 of 6 refused-or-metadata.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/rl.AC2.sh; echo "exit=$?"</invocation><expect>(?s)sentinel at HEAD=no;.*outside the build slots' set 0; ms_ingest.py shipped 0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: C7's first criterion for each route, against the SERVED gateway. The issuer supplies the four message and
  attachment ids at run time; an arm without its input is NOT RUN, which is a FAIL.
- `AC2`: NEVER-2 is closed, and the release is narrow, shipping only the build slots' files with `/ms/*` unshipped.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-rl-1.trnspt-deps-release.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~15, queue position 3. HANDED only when `OG-tx-1`, `OG-ml-1`, `OG-hr-1` and `OG-hr-2` are drained, and OG-t-2
  and NFRA_MCPINDEX MX-r-7 have landed (release serialisation). PHASE B also needs G-SENDERS (Yang's addresses, N1).
- The halves' blast radius: the shipped file set, the two secrets, the `.env` delta and the negative arms. Rollback is the prebuilt live artifact plus the old `.env`; the secrets can be deleted with a recovery window.
- Risk WORLD: a deploy that adds a content surface.

<status>staged</status>
<round>8</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
