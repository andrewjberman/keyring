# NFRA_OPLGTW task order -- `OG-x-3` -- ROUND 2 (E5 SERVED step): the NARROW gateway release of OG-x-2's streaming export

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-x-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~11</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the host, its role and Terraform are untouched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is ruled (narrow, live base only), as for OG-e-2.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM).
</preflight>

## 1. THE CELL -- `OG-x-3` (decomposition addendum R2-E, item E5, served half)

`OG-x-2` (your queue position 1, author `0.9.0_WK_NFRA_OPLGTW~11`) builds the streaming export. It is not deployed. This
cell ships it NARROW: the live commit plus OG-x-2's own gateway commits, and nothing else CLOUD holds. Addendum R2-E
serialises the round's two releases: this one ships FIRST; `OG-t-2` (slot ~12) builds on top of it.

Two phases. PHASE A runs when the issuer hands you this order (after OG-x-2 is drained). PHASE B runs only when the
issuer says GO.

### PHASE A (pre-GO) -- no upload, no contact with the instance beyond read-only SSM
1. **The live commit.** Read `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway.deployed_commit` (it read
   `6a98a0553a` at the issuance base). Confirm it BY CONTENT over read-only SSM on instance `i-07dccb1615503ac99`: the
   md5 of the host's `/opt/opal-gateway/app/integrations/schwab/{engine,integration,export,envelope}.py` and
   `/opt/opal-gateway/app/download_routes.py` equals that commit's bytes, 5 of 5. These files cannot tell `6a98a0553a`
   from `fe94911257`; the discriminator is the host `.env` KEY `SPRINT_VIEW_ALLOWED_EMAILS` (count it, print no value),
   which only `6a98a0553a`'s template writes. Any mismatch: STOP, a BLOCKING row.
2. **This cell's commits.** The CLOUD commits touching `infra/aws/ec2/opal-gateway` whose author is exactly
   `0.9.0_WK_NFRA_OPLGTW~11 <` (anchor on that string), oldest first, restricted to OG-x-2's drain.
3. **The release tree.**
   - `git worktree add -b rel-nfra-oplgtw-stream-export /c/tmp/og-x3-rel <live commit>`;
   - cherry-pick those commits with `--no-commit`, in order;
   - pin every NON-gateway path back to the live commit (the commits also carry a surprise-channel row);
   - commit under your serial. The issuer authorizes the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPLGTW~11`
     for exactly the release-branch commit(s). Name each use.
   - Census: `git -C /c/tmp/og-x3-rel diff --stat <live> HEAD -- infra/aws/ec2/opal-gateway` names ONLY files those
     commits changed. Anything else: STOP, a BLOCKING row.
4. **Tests on the release tree.** Set `AUDIT_PATH=$(mktemp)` first, then in `/c/tmp/og-x3-rel/infra/aws/ec2/opal-gateway`
   run, with your `.venv-og` interpreter, `-m pytest tests/test_schwab_export_stream.py tests/test_schwab_export.py
   tests/test_schwab_engine.py tests/test_schwab_query.py -q -p no:cacheprovider`. Record the result.
5. **mcportal pin.** `deploy-to-ec2.sh` builds the dashboard bundle from a nested `mcportal/` checkout. Clone mcportal
   into `/c/tmp/og-x3-rel/mcportal` at the manifest's `mcportal_commit` (`a3bff71ffa` at the issuance base). Copy
   `node_modules` from an existing clone if one exists, so `bun install` fetches nothing. Record its HEAD.
6. **Rollback proven.** In a clean tree `/c/tmp/og-x3-rb` at the live commit, with mcportal at the same pin, build the
   live artifact WITHOUT uploading. Compare its file set with the live S3 artifact
   `s3://opal-313476888478-lambda-artifacts/ec2/opal-gateway/opal-gateway-<live short>.tar.gz`; expect all files
   identical. Name the re-deploy command: `cd /c/tmp/og-x3-rb && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~11 bash
   infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
7. **The blast radius, measured.** Over read-only SSM: the host `.env` `ENABLED_INTEGRATIONS` value only (print no
   other line), and the on-host tool-name list with its count. State whether `schwab` is in `ENABLED_INTEGRATIONS`. If
   it is NOT, no caller can mint a download ticket, so no served answer changes (DELTA=0). If it IS, STOP: a BLOCKING
   row, because the never-widen halves were written for a dark integration.
8. Write `ANNOUNCE_OG-x-3.md` in your deliverables dir with steps 1-7's numbers. Commit it on your branch and report.
   Do NOT upload.

### PHASE B (GO) -- only after the issuer says GO
9. Take the BEFORE reads over SSM: the on-host tool-name list and count, and the `.env` `ENABLED_INTEGRATIONS` value
   only. If either differs from step 7, STOP.
10. NEVER-2 ledger, slug `nfra-oplgtw-stream-export-release`, on your worktree. Open it with
    `python .tools/deploy_ledger.py open ...` (legs: upload, install + verify, manifest, rollback-proven). Commit the
    entry AND its sentinel BEFORE the act.
11. ACT from the release tree: `cd /c/tmp/og-x3-rel && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~11 bash
    infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`. The wrapper's manifest
    auto-commit may fail on this device; leave it unlanded and record by hand in step 13. `/c/tmp/og-x3-rel/mcportal`
    HEAD must still be the pin before the upload.
12. VERIFY, from the host, within 90 s of the restart:
    - `/health` 200 ON THE HOST;
    - md5 of the 5 files in step 1 equals the release commit's bytes;
    - tool list AFTER equals BEFORE (count and sorted diff EMPTY);
    - `ENABLED_INTEGRATIONS` unchanged.
    Any failure: run the rollback, re-verify health and md5 = the live commit, close the ledger ROLLED BACK. Never
    half-landed.
13. On your worktree, on an LF copy, record `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway`:
    `deployed_commit` = the release commit (full); `previous_deployed_commit` = the live commit (full); `deployed_at`
    and `deployed_by`; `mcportal_commit` unchanged; a `release_note` naming CLOUD's still-unreleased gateway commits.
    Commit it. Close every leg with its proof, commit the close, then run the criteria.

## 2. BOUNDS

1. Terraform, the ALB, the host, its role and its secrets are untouched. `safe-ec2-deploy.sh` and `deploy-to-ec2.sh`
   are READ, never edited. The `.env` `ENABLED_INTEGRATIONS` is never changed; this cell does not enable Schwab.
2. You work in the worktree named in your identity line (the same one as OG-x-2); the release tree is `/c/tmp/og-x3-rel`.
   Standing: no push, no vendor call, never `git stash`. Every pytest run isolates `AUDIT_PATH`. REFUSE a criterion you
   cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-stream-export-release.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W11-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-x-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/xr.AC1.sh; echo "exit=$?"</invocation><expect>sentinel at HEAD=no; listed OPEN/HELD=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-x-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/xr.AC2.sh; echo "exit=$?"</invocation><expect>descends=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-x-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/xr.AC3.sh; echo "exit=$?"</invocation><expect>/health=200; streaming export on host 1; schwab files equal deployed_commit 4 of 4; ENABLED_INTEGRATIONS unchanged=yes -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

- `AC1` -- NEVER-2: the entry is committed at HEAD, the sentinel gone, the OPEN/HELD scan clean with its denominator.
- `AC2` -- the narrow release from the committed record: the deployed commit descends from the previous one, ships only
  files OG-x-2's commits changed, and carries OG-x-2's `tests/test_schwab_export_stream.py`.
- `AC3` -- the served host over SSM: `/health` 200, the streaming export shipped, the four Schwab engine files equal the
  deployed commit's bytes, and `ENABLED_INTEGRATIONS` unchanged (Schwab stays dark).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~11/NFRA_OPLGTW.TO-OG-x-3.streaming-export-release.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~11, queue position 2 (after `OG-x-2`, before `OG-r-3`). Ships BEFORE `OG-t-2` (release serialisation).
- Blast radius for the never-widen halves (CTO + COO): the live `ENABLED_INTEGRATIONS` read `ycharts opal_portal
  globgrph` (SSM 3f1bce17 on 2026-09-28 read the 6a98a0553a template). Schwab is dark, so no caller can reach the
  export and every served answer is unchanged (DELTA=0). Step 7 re-measures this, and PHASE B refuses if it moved.
  Rollback: the prebuilt live artifact.
- GO: both halves SIGNED, off-hours, and "deploying" announced by the issuer.
- The declared class is WORLD: a deploy and GATE (xii)'s floor (`infra/` path).

<status>staged</status>
<round>3</round>
<slot>~11</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
