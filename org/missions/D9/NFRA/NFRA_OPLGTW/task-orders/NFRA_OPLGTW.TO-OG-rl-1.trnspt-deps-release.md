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
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is the CTO's (PRD v1.3 C7 @2b8f3151c6: narrow, ledger, never-widen halves).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, Secrets Manager) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-rl-1` (decomposition addendum R3-T)

The build cells `OG-tx-1`, `OG-ml-1`, `OG-hr-1` and `OG-hr-2` are complete on CLOUD and NOT deployed. Ship them NARROW:
the live commit plus those cells' own gateway commits, and nothing else CLOUD holds. Read PRD
`org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v1.3 C7 whole (at @2b8f3151c6 or later). `OG-pr-1` creates the
secrets `gateway/transcripts/bearer`, `gateway/mail/bearer` and `gateway/principals/rosters` and grants
`opal-gateway-role` exactly those three (gateway-train Terraform act #2). PHASE A may run before `OG-pr-1` lands;
PHASE B never does. The release order is the CTO's
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md` (R1, R2 C1-C6, R4).

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
   - Say whether the host role already reads them, by reading its policy. Before `OG-pr-1` lands, record
     `grant pending OG-pr-1` and continue; once it has landed, a missing grant is a BLOCKING row naming the exact
     grant. This order applies no IAM change.
   - Confirm each of the three secrets with `describe-secret` (never read a value). Before `OG-pr-1` lands they read
     ABSENT; record that and continue.
   - **Rotation (CTO ruling (c), row Z-W17-S1).** This release rotates the cot OTP capability bearer, Secrets
     Manager `blackdiamond/cot/otp-gateway-token` (the second token of host `.env` line 14, `OTP_BEARER`). Confirm the
     attribution by shape only: print whether that secret's value is 64 hex, a boolean, never the value. Read every
     presenter of that bearer (who reads the secret, and whether each reads it per call or caches it) and name a
     non-mutating `/otp/*` probe for the verify. A presenter that caches it is a BLOCKING row, never a skipped
     rotation.
5. **`.env` render.** `deploy-to-ec2.sh`'s printf has equal `%s` and argument counts. The changes are additive only:
   - the two bearers;
   - the sender table, from the issuer at GO: Manav's addresses as they stand; Yang's join when supplied, as a data
     change (CTO ruling (d): G-SENDERS is not a gate). Never committed;
   - the principal rosters, read HOST-SIDE (CTO ruling R4, row Z-S24): the on-host script fetches
     `gateway/principals/rosters`, parses `master_admin` and `write_capable` with `python3.11`, and refuses (no `.env`
     written, no restart) unless each is a valid `<tid>/<oid>` pair list; the deploying-shell guard for
     `OG_MASTER_ADMIN_PRINCIPALS` / `OG_WRITE_CAPABLE_PRINCIPALS` goes. The `MASTER_ADMIN_PRINCIPALS=` and
     `WRITE_CAPABLE_PRINCIPALS=` lines stay;
   - hand-merged onto the LIVE printf line, never a CLOUD-sourced one (C1). `ANNOUNCE` prints the `.env` KEY set
     before and after, keys only. The ac08 count is LIVE + OWN (C3);
   - the meeting allowlist (empty until G-MEETINGS);
   - the PDF size cap.

   `ENABLED_INTEGRATIONS` and every existing key are unchanged.
6. **Rollback.** Build the live artifact in a clean `/c/tmp/og-rb3` WITHOUT uploading, and compare it with the live
   S3 artifact file by file. Name the re-deploy command with `DEPLOY_BASE_REF`.
7. Write `ANNOUNCE_OG-rl-1.md` in your deliverables with steps 1-6's numbers (no secret, no address), commit it, and
   report. Do NOT upload.

### PHASE B (GO): only after the issuer says GO (both halves SIGNED, off-hours, the gateway queue told, `OG-pr-1` complete)

7a. **Re-read the live ref** (`EC2_MANIFEST.json` at HEAD and the host). If it moved since PHASE A (MX-r-7 or MS-d-2
    landed), re-cut `/c/tmp/og-rel3` onto the new live ref, re-run steps 1-6, and re-commit `ANNOUNCE_OG-rl-1.md`
    before any act (CTO ruling R1; the stale-base guard refuses otherwise).

8. BEFORE reads: the on-host tool list and `ENABLED_INTEGRATIONS`.
9. NEVER-2 ledger, slug `nfra-oplgtw-trnspt-deps-release`, opened with `python .tools/deploy_ledger.py open ...`
   (legs: secrets, upload, install + verify, manifest, rollback-proven). Commit the entry AND its sentinel BEFORE the
   act.
10. Put a new random value (never printed) on `blackdiamond/cot/otp-gateway-token`. Then act from the release tree with `DEPLOY_BASE_REF=<live full sha>`.
11. VERIFY from the host within 90 s:
    - `/health` 200;
    - md5 of the shipped files equals the release bytes;
    - the tool list AFTER equals BEFORE plus exactly the 5 new tools;
    - `ENABLED_INTEGRATIONS` unchanged;
    - `/ms/*` answers as before;
    - on the step-4 `/otp/*` probe, the pre-rotation cot value is refused and the new one is accepted.

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
  <criterion id="AC3" cell_refs="OG-rl-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/rl.AC3.sh; echo "exit=$?"</invocation><expect>(?s)GUID literals in the template: 0.*template reads gateway/principals/rosters host-side: True.*deploying-shell roster requirement still present: False.*bash -n rc=0.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: C7's first criterion for each route, against the SERVED gateway. The issuer supplies the four message and
  attachment ids at run time; an arm without its input is NOT RUN, which is a FAIL.
- `AC2`: NEVER-2 is closed, and the release is narrow, shipping only the build slots' files with `/ms/*` unshipped.
- `AC3`: the SHIPPED template reads the rosters host-side (R4); no release after this one needs an off-repo hand-off.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-rl-1.trnspt-deps-release.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~15, queue position 3. PHASE A handed once `OG-tx-1`, `OG-ml-1`, `OG-hr-1` and `OG-hr-2` are drained (A2).
  PHASE B GO only after `OG-pr-1` and `OG-al-1` are complete and MX-r-7 has landed (train R1; it swaps with MS-d-2
  if ready first). `OG-al-1` (decomposition addendum R3-T.2) gives `/hx/*` its public reach; the ALB stays untouched here. G-SENDERS is NOT a gate
  (ruling (d)). The halves also cover the cot OTP bearer rotation and the host-side roster read.
- The halves' blast radius: the shipped file set, the two secrets, the `.env` delta and the negative arms. After
  `OG-al-1` the edge admits unauthenticated requests on `/hx/transcripts/*` and `/hx/mail/*`: each prefix's own bearer
  in the app is the ONLY gate there, and both halves name it (`1.0.0_SA_CTO~O` msg 27605). Rollback is the prebuilt live artifact plus the old `.env`; the secrets can be deleted with a recovery window.
- Risk WORLD: a deploy that adds a content surface.

<status>staged</status>
<round>8</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

## AMENDMENT A1 (issuer `2.0.0_SA_COO~O`, 2026-10-01 ~04:3xZ; on PRD v1.3 @2b8f3151c6 and CTO rulings (b), (c), (d))

Graded by: no gate limb (LIMB 6 fires on a newly-added order only; GATE (viii) reads `<placeholders>NONE</placeholders>`).
- PRD citation v1.2 -> v1.3; the secret names come from `ROUTE_NAMES.json` as before, now graded with `grade()`.
- (b) row Z-S24 and CTO ruling R4: the release template reads the rosters host-side (new criterion AC3, `rl.AC3.sh`,
  controlled: it reads FAIL on today's live template on exactly the two arms the edit must move); `OG-pr-1` (R3)
  creates the secrets and the grant first; new edge `OG-pr-1` -> `OG-rl-1` PHASE B. The train order is R1.
- (c) row Z-W17-S1: the release rotates `blackdiamond/cot/otp-gateway-token` (line 14's second token, attributed by bash
  semantics on the live template and confirmed by shape in step 4), with a refused-old / accepted-new verify.
- (d) G-SENDERS is not a gate: the sender table ships as it stands.
AC1 and AC2 and their invocations are unchanged; AC3 is added.

## AMENDMENT A2 (issuer `2.0.0_SA_COO~O`, 2026-10-01 ~06:1xZ; PHASE A handed early)

Graded by: no gate limb (a modification; GATE (viii) reads `<placeholders>NONE</placeholders>`). The four build cells
are complete and drained (tx-1 @be10dc29d8, ml-1 @4ca87da779, hr-1 @43f34bae73, hr-2 @f20c20896c; issuer re-grade PASS
on CLOUD). PHASE A runs now against the live ref, so the release is ready for train R1's swap with MS-d-2. `OG-pr-1`
not yet landed is recorded as pending in step 4 (no STOP). New step 7a re-cuts onto the live ref at GO if it moved.
Criteria unchanged.

## AMENDMENT A3 (issuer `2.0.0_SA_COO~O`, 2026-10-01 ~07:0xZ; rules PHASE A rows Z-W15-S9..S13 by row Z-S29)

Graded by: no gate limb (a modification; GATE (viii) reads `<placeholders>NONE</placeholders>`). PHASE A drained
@0116dd05fe. ROLLBACK (S12): a rollback on the live template reads the two rosters from the site-Z Part D file into the
rolling-back shell only, with the `OG-pr-1` script's mapping, never printed. ROTATION (S13): proceeds with the cot box
stopped; the gateway side is verified by the step-4 probe. Step 3's "3 adopted" test files read as the cells' 6 new
test files in all (S9). Criteria unchanged.

## AMENDMENT A4 (issuer `2.0.0_SA_COO~O`, 2026-10-01 ~07:1xZ; the sender table's source)

Graded by: no gate limb (a modification; GATE (viii) reads `<placeholders>NONE</placeholders>`). Step 5's sender
table is NFRA_TRNSPT's own data asset, read at GO from HEAD: `data/transcripts/scripts/outlook/criterion.py`
`DEFAULT_AUTHORS` (Manav's two addresses, the 49 one built from the registry's email domain, and Yang's), evaluated by
importing that module, never retyped. The render carries it in `MAIL_SENDER_TABLE`; the template commits no address.
No off-repo input is needed for it at GO. Criteria unchanged.

## AMENDMENT A5 (issuer `2.0.0_SA_COO~O`, 2026-10-01 ~09:3xZ; the re-cut, train slot 3)

Graded by: no gate limb (a modification; GATE (viii) reads `<placeholders>NONE</placeholders>`). Train state: MX-r-7
landed 05e3eff563 (07:14Z); MS-d-2 landed `2c0f84966dc452d367ab1e4fc5d4849f08c1625e` (09:08:28Z, manifest on CLOUD);
`OG-pr-1` (secrets + grant) and `OG-al-1` (ALB rule priority 35) are complete. OG-rl-1 is train slot 3. RE-CUT NOW,
before the halves (step 7a run ahead of the GO), so the halves bind the bytes that ship:
- the new release tree is `/c/tmp/og-rel4`, branch `rel-nfra-oplgtw-trnspt-deps-r2`, at the live commit above; re-run
  steps 1-6 there and re-commit `ANNOUNCE_OG-rl-1.md` (the d61fde4693 tree `/c/tmp/og-rel3` is superseded; leave it);
- `.env` census 39 keys -> 39 + this release's own (C1, hand-merged onto the LIVE printf); ac08 count LIVE + OWN (C3);
- the rotation (CTO 27705 (2)) names its consumer, the cot bd-auto-login `/otp/fetch` caller; the 49f token is untouched;
- STANDING RULE (CTO 27705 (1), row Z-S32): nobody sources `/opt/opal-gateway/.env` in a shell. A key read uses names
  only (`grep -o '^[A-Z_]*='`) or `/proc/<service pid>/environ` for one named key, never echoed. The ANNOUNCE carries
  that line;
- the template's principal read is host-side from `gateway/principals/rosters` (R4), so this release needs NO
  off-repo roster hand-off; the rollback on the 2c0f84966d template does (S12 ruling stands).
Criteria unchanged.
<status>pending</status>
