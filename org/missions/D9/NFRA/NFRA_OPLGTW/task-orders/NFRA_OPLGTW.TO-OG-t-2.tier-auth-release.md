# NFRA_OPLGTW task order -- `OG-t-2` -- ROUND 2 (E7 SERVED step, with E9): the NARROW gateway release of the principal-keyed tier and the auth hardening, under never-widen halves

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-t-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~12</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the host, its role and Terraform are untouched.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release shape is ruled (R-3 (e): narrow, never-widen halves).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM).
</preflight>

## 1. THE CELL -- `OG-t-2` (decomposition addendum R2-E, items E7 and E9, served half)

The build cells `OG-t-1`, `OG-u-1` and `OG-u-2` (your own earlier queue positions, author `0.9.0_WK_NFRA_OPLGTW~12`)
are complete on CLOUD and NOT deployed. This cell ships them NARROW: the live commit plus those cells' own gateway
commits, and nothing else CLOUD holds. It also ADDS the two principal rosters to the host `.env`.

**Values the issuer hands you at hand-off, never typed by you:** `ADMIN_PRINCIPAL` (the operator's `<tid>/<oid>`, from
the switchover sitting's Part D record) and `WRITE_CAPABLE_PRINCIPALS` (the two write-capable persons' `<tid>/<oid>`
pairs). They arrive in the hand-off message that continues you on this order, each with the record path it came from.
If either is missing or is not a `<tid>/<oid>` pair, STOP: a BLOCKING row.

Two phases. PHASE A runs when the issuer hands you this order. PHASE B runs only when the issuer says GO.

### PHASE A (pre-GO) -- no upload, and no contact with the instance beyond read-only SSM
1. **The live commit, and the release order.**
   - Read `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway.deployed_commit`. Addendum R2-E serialises the two
     round-2 releases: `OG-x-3` (the streaming export) ships FIRST, so the live commit must be `OG-x-3`'s release
     commit or descend from it. If `OG-x-3` has not shipped, STOP: a BLOCKING row (never release under it).
   - Confirm it BY CONTENT over read-only SSM on `i-07dccb1615503ac99`: the md5 of the host's
     `/opt/opal-gateway/app/{tier,guard,tools,token_broker,server,ratelimit,oauth_as,config}.py`,
     `app/integrations/base.py` and `app/integrations/schwab/{engine,integration,export,envelope}.py` equals that
     commit's bytes, 13 of 13. Any mismatch: STOP, a BLOCKING row.
2. **Release tree.**
   - `git worktree add -b rel-nfra-oplgtw-tier-auth /c/tmp/og-rel2 <live>`, then cherry-pick the build cells' gateway
     commits (author `0.9.0_WK_NFRA_OPLGTW~12 <`) with `--no-commit`, oldest first.
   - Pin every NON-gateway path back to `<live>`.
   - Commit under your serial. The issuer authorizes the audited `GIT_COMMIT_AUTHOR_OVERRIDE=0.9.0_WK_NFRA_OPLGTW~12`
     for exactly the release-branch commit(s). Name each use.
   - Census: `git -C /c/tmp/og-rel2 diff --stat <live> HEAD -- infra/aws/ec2/opal-gateway` names ONLY files the build
     cells changed, plus `deploy-to-ec2.sh` for step 6.
3. **Tests on the release tree** (`AUDIT_PATH=$(mktemp)`), from `infra/aws/ec2/opal-gateway`:
   `python -m pytest tests/test_tier_principal.py tests/test_auth_hardening.py tests/test_dcr_idle_lifetime.py tests/test_min_tier_gate.py tests/test_attachment_tools.py tests/test_owner_gate.py tests/test_email_deny.py tests/test_sprint_view.py -q -p no:cacheprovider`,
   then `tests/test_ratelimit.py` in its own process. Record both results. Restore `GW/audit.jsonl` if dirtied.
4. **The blast-radius pre-read (R-3 (e); ruling Q1), the input to the halves.**
   - For EVERY distinct identity in the access-state table's principal partitions AND in the last 14 days of the host's
     audit log, machine and server-held callers included (the MS-ingest identity among them), compute the OLD tier (the
     live rules and `.env`) and the NEW tier (the release's rules, with the principal rosters from the hand-off).
   - Print the denominator and every delta. The ONLY allowed delta is the synthetic test fixture. Machine callers must
     show 0 deltas (Q1).
   - Also count the `oauth_client` records that would read EXPIRED under `OG-u-2`'s idle lifetime at release time, and
     say whether the operator's upload client (`identity_tool_allowlist.txt:19`) is among them.
   - Any other delta, or the operator's client expiring: STOP, a BLOCKING row. The CTO rules it; never widen a roster
     to make it pass.
5. **mcportal pin and rollback proven**, as `OG-e-2` steps 5-6:
   - clone mcportal at the manifest's `mcportal_commit` (`a3bff71ffa` at the issuance base) into
     `/c/tmp/og-rel2/mcportal`, copying `node_modules` from an existing clone so `bun install` fetches nothing;
   - build the live artifact in a clean `/c/tmp/og-rb2` WITHOUT uploading, and compare it with the live S3 artifact;
   - name the re-deploy command.
6. **`.env` render.**
   - `deploy-to-ec2.sh` rewrites the host `.env` from one printf. Show that its `%s` count equals its argument count.
   - The ONE change this release makes to it: ADD `MASTER_ADMIN_PRINCIPALS=<the hand-off ADMIN_PRINCIPAL>` and
     `WRITE_CAPABLE_PRINCIPALS=<the hand-off WRITE_CAPABLE_PRINCIPALS>`. The email rosters STAY: after `OG-t-1` they are
     read only by the machine-identity rule for server-held identities (Q1).
   - This template edit is the release branch's, cherry-picked nowhere else, and it is never merged to CLOUD by you.
   - `ENABLED_INTEGRATIONS` must render `ycharts opal_portal globgrph`.
7. Write `ANNOUNCE_OG-t-2.md` in your deliverables dir with steps 1-6's numbers (never a tid/oid value: cite the record
   path), commit it on your branch, and report. Do NOT upload.

### PHASE B (GO) -- only after the issuer says GO (both never-widen halves SIGNED, off-hours, "deploying" announced)
8. Take the BEFORE reads over SSM: the on-host tool-name list, and `ENABLED_INTEGRATIONS` only. Print no other `.env` line.
9. NEVER-2 ledger, slug `nfra-oplgtw-tier-auth-release`. Open it with `python .tools/deploy_ledger.py open ...` (legs:
   upload, install + verify, manifest, rollback-proven), and commit the entry AND its sentinel BEFORE the act.
10. ACT from the release tree:
    `cd /c/tmp/og-rel2 && HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~12 bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
11. VERIFY from the host within 90 s:
    - `/health` 200;
    - md5 of the shipped app files equals the release commit's bytes;
    - tool list AFTER equals BEFORE, sorted diff EMPTY;
    - `ENABLED_INTEGRATIONS` unchanged;
    - one `/mcp` call as the admin principal resolves MASTER_ADMIN in the audit tier field.
    Any failure: roll back, re-verify, close the ledger ROLLED BACK. Never half-landed.
12. Record `EC2_MANIFEST.json` `services.opal-gateway` as `OG-e-2` step 13 did (`deployed_commit`,
    `previous_deployed_commit`, `deployed_at`, `deployed_by`, `mcportal_commit` unchanged, a `release_note`). Close every
    leg with its proof, commit, then run the criteria.

## 2. BOUNDS

1. Terraform, the ALB, the host, its role and its secrets are untouched. `safe-ec2-deploy.sh` is READ, never edited. The
   only `.env` change is step 6's two added lines.
2. You work in the worktree named in your identity line; the release tree is `/c/tmp/og-rel2`. Standing: no push, no
   vendor call, never `git stash`. Every pytest run isolates `AUDIT_PATH`. REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-tier-auth-release.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~12/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Release-branch only (never merged to CLOUD by this cell): `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` (the two added
lines of the `.env` printf).

Rows go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W12-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-t-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/tr.AC1.sh; echo "exit=$?"</invocation><expect>sentinel at HEAD=no; listed OPEN/HELD=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-t-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/tr.AC2.sh; echo "exit=$?"</invocation><expect>descends=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-t-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/tr.AC3.sh; echo "exit=$?"</invocation><expect>/health=200; email roster reads on host 0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

- `AC1` -- NEVER-2: the entry is committed at HEAD, the sentinel gone, the OPEN/HELD scan clean with its denominator.
- `AC2` -- the narrow release from the committed record: the deployed commit descends from the previous one, ships only
  files the build slot's commits changed, and its `app/tier.py` reads no email roster.
- `AC3` -- the served host over SSM: `/health` 200, host `tier.py` reads no email roster, the browser callback is in
  `AUTH_PATHS`, and `ENABLED_INTEGRATIONS` is unchanged.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~12/NFRA_OPLGTW.TO-OG-t-2.tier-auth-release.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~12, queue position 4. HANDED only when: `OG-t-1`, `OG-u-1`, `OG-u-2` are drained; `OG-x-3` has shipped (release
  serialisation, addendum R2-E); and the switchover sitting's Part D record gives `ADMIN_PRINCIPAL`. The two principal
  values ride the hand-off message, never this file (a tid/oid pair is a personal identifier and stays out of the repo).
- Q1 folded: machine callers are in the pre-read denominator and must show 0 deltas; the email rosters stay in `.env`
  for the machine-identity rule only.
- The halves' blast radius: step 4's delta table and the expiring-client count are the whole content. Rollback is the
  prebuilt live artifact plus the old `.env`.
- The declared class is WORLD: a deploy (the gateway release) and GATE (xii)'s floor (`infra/` path).

<status>staged</status>
<round>3</round>
<slot>~12</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

## AMENDMENT A1 (issuer `2.0.0_SA_COO~O`, 2026-09-30 ~21:2xZ; row `NFRA_OPLGTW-Z-S21`)

Graded by: no gate limb (LIMB 6 fires on a newly-added order only; GATE (viii) reads `<placeholders>NONE</placeholders>`).
Released by: Part D, `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/PART_D_RECORD_20260930.md` @205c2e7f6c.

1. **Ancestry is not evidence on this gateway; content is.** Deploy-only refs carry history without bytes. Measured by
   the issuer: live `42c52ed4d9` has `b5a585cf2f`, `344cca64a1`, `c4d2274c6d` and `0906bf01e5` in its history, yet its
   `app/tier.py` reads `MASTER_ADMIN_PRINCIPALS` 0 times (CLOUD HEAD and `b5a585cf2f`: 2). So:
   - Step 1's release-order check passes BY CONTENT. OG-x-2's gateway lines (`0c3d545002`) are present in live
     460 of 490. The 27 absent `engine.py` lines are OG-x-4's rewrite (`d1ba79742c`, `132a07ee11`); the 3 absent
     `tests/test_schwab_export_stream.py` lines were not attributed. Re-read both numbers yourself; a different
     number is a BLOCKING row.
   - Step 1's live commit is `42c52ed4d9e834b0f1cf4f96eb83f9b0f7a183df` (MX-r-6 v3, live 18:33:41Z; CLOUD's
     `EC2_MANIFEST.json` may still read `4ce7946426`, because that ledger closed on a worker branch). The 13-file md5
     read on the host is the authority.
   - Step 2 cherry-picks the four build commits by diff even though git calls them ancestors. Never skip one on
     `--is-ancestor`, and never let `git cherry-pick` report "empty" without checking the file bytes.
2. **Values.** The hand-off carries `ADMIN_PRINCIPAL` and the two `WRITE_CAPABLE_PRINCIPALS` pairs, citing the Part D
   record above. `.env` gets exactly the pairs as handed. Never print or commit a value.
3. **PHASE B step 10.** If the release tree's `safe-ec2-deploy.sh` honours `DEPLOY_BASE_REF`, set it to the live full
   sha read at act time, for the act and for any rollback. If it does not, repeat step 1's 13-file content read
   immediately before the upload and STOP on any drift.

<status>pending</status>

## AMENDMENT A2 (issuer `2.0.0_SA_COO~O`, 2026-09-30 ~23:xxZ; rules ARMED rows Z-W12-S4 and Z-W12-S5, disarm row Z-S22)

Graded by: no gate limb (LIMB 6 fires on a newly-added order only; GATE (viii) reads `<placeholders>NONE</placeholders>`).
PHASE A drained @0a5cc3c093 (ANNOUNCE_OG-t-2.md: 13 of 13 by content, 9 identities 0 deltas, rollback 87 of 87).

1. **Step 6's `ENABLED_INTEGRATIONS` literal is stale (S4).** It MUST render the live value unchanged, which at
   `42c52ed4d9` is `ycharts opal_portal globgrph opal_discover portal_index schwab`. Step 8's BEFORE read is the
   authority. `tr.AC3.sh` now compares against that value, or against `OG_T2_ENABLED_BEFORE` when step 8 reads a
   different one.
2. **AC2's allowed set omitted a file this order ships (S5).** `tr.AC2.sh` now allows
   `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` (step 6).
3. **PHASE B principals.** The release branch renders the pairs from `OG_MASTER_ADMIN_PRINCIPALS` and
   `OG_WRITE_CAPABLE_PRINCIPALS` in the deploying shell (row Z-W12-S6). The issuer supplies both at the GO. The same
   no-print rule applies.

<status>complete</status>
