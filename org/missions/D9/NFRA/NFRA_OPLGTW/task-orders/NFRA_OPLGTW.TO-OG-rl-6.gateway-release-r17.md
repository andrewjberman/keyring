# NFRA_OPLGTW task order -- `OG-rl-6` -- the gateway release carrying OG-q-7 on live 4b6b823fae

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release is the CTO's round-16 analysis item 2.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, Secrets Manager reads) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-rl-6` (decomposition addendum R3-T.10, item 2)

Handed only after `OG-q-7` is drained to CLOUD. Pattern: `ANNOUNCE_OG-rl-5.md` and the r16 tooling in
`deliverables/0.9.0_WK_NFRA_OPLGTW~15/` (`rl5_ssm.py`, `rl5_host_prelude.py.txt`, `rl5_verify.sh`/`.py`). Reuse them;
do not rebuild them. STANDING RULE (row Z-S32): never source `/opt/opal-gateway/.env`.

### PHASE A (pre-GO): read-only on the host; no upload

1. **Live ref.** Confirm `4b6b823faec5288c714b70117fcd691239a2633f` by host md5. A mismatch STOPS.
   - Release tree: a fresh worktree on branch `rel-nfra-oplgtw-r17` at `4b6b823fae`.
   - Take OG-q-7's `integration.py` hunks and its two test files (`test_schwab_q7_asset_download.py` new,
     `test_schwab_rl5_asset_query.py` restated) from the drained CLOUD head.
   - Prove the release's `git diff 4b6b823fae -- integration.py` equals q-7's own diff of that file.
   - **Release-branch commit, R13 (a):** commit it under the audited `GIT_COMMIT_AUTHOR_OVERRIDE`. The file list must be
     within this order's release set, and you cite the audit-log line in the ANNOUNCE.
2. **Tests** on the release tree: `test_schwab_q7_asset_download.py` (4 named), `test_schwab_rl5_asset_query.py`,
   `test_schwab_query.py`, `test_schwab_grain_r9.py`, and `test_entitlement_admin.py::test_ogz2_ac08`.
3. **Rollback:** a worktree at `4b6b823fae`, equal file by file to the live S3 artifact `opal-gateway-4b6b823fae.tar.gz`.
4. **BEFORE run.** On the host, through the installed engine and venv, with a SYNTHETIC principal and an in-memory
   grant (never a real identity, never a state-store write), record:
   - a `dim_asset` `prepare_download` on one qualified snapshot (expected: REFUSED `asset_policy_selection_unavailable`);
   - the `dim_asset` query on the same snapshot (expected: OK, held-only).
   Remove every host scratch copy.
5. **Verify script** extended from `rl5_verify.sh`:
   - host `/health` 200; shipped md5 = release bytes; tool list unchanged (65); `.env` 50 key names unchanged;
   - the AFTER run:
     - the download is OK;
     - the held check is `{returned, unheld_returned, held_cusips_in_dim_position, asset_universe_cusips}`, graded only
       when held < universe;
     - an empty-holdings synthetic grant's download is REFUSED `asset_read_denied_unqualified`;
     - the query is OK, with the download's held set equal to the query's;
   - then `rl4.AC1.sh` and `ht.AC2.sh`.
6. `ANNOUNCE_OG-rl-6.md` with the blast radius, written for the three halves; commit; report. Do NOT upload.

### PHASE B (GO): only after the issuer says GO (CTO + COO + CVO halves SIGNED: dim_asset downloads open under C3)

7. Re-read live; if it moved, re-cut. Open NEVER-2 ledger `nfra-oplgtw-gateway-release-r17` (legs: upload,
   install + verify, manifest, rollback-proven), with entry AND sentinel committed before the act.
8. Deploy from the release tree with
   `DEPLOY_BASE_REF=4b6b823faec5288c714b70117fcd691239a2633f HALT_ACK=1 AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~15` through
   `infra/aws/ec2/safe-ec2-deploy.sh`.
9. Run the verify script IMMEDIATELY. Write `RL6_DOWNLOAD.json` with:
   - `served_release`;
   - `before {dim_asset_download}`;
   - `after {dim_asset_download, empty_holdings_download, dim_asset_query}`;
   - `held_check {returned, unheld_returned, held_cusips_in_dim_position, asset_universe_cusips}`;
   - `query_held_equal_download_held`;
   - `synthetic_principal: true`, `grants_written: 0`, `state_store_written: false`.

   Any failure, or ANY unheld CUSIP: roll back, re-verify, and close ROLLED BACK.
10. Record `EC2_MANIFEST.json` by hand. Close every leg with proof. Run section 4. Write the proof. Edit this order's ONE
    `<status>` tag IN PLACE to `complete`. Commit.

### PHASE C -- AMENDMENT A1 (CTO R14 @b478972fec, msg 29402): the r17b release carrying /yearinreview on live e91819e281

Phases A and B are DONE: r17 `e91819e281` is LIVE, and AC1 and AC2 were graded at that deploy (proof @2994d320b4). They
are not re-run after Phase C, because AC2's shipped set is anchored to its own release. The kit is Andrew's
`/yearinreview` page. It sits on origin CLOUD (laptop push 9c4eb4a7d5) at
`org/tier1_exec/4.0.0_SA_CRO/deliverables/BRIEF1_YEAR_ONE_20261004/gateway_candidate/`; read it with
`MSYS_NO_PATHCONV=1 git show origin/CLOUD:<path>`. Its README lists 4 files plus `apply_hookup.py`, and its 3 anchored
`server.py` edits reproduce how `/sprint` and `/rivalfunds` are hooked up.

**PHASE C-A (pre-GO; read-only on the host; no upload):**

11. **Live ref.** Confirm `e91819e2819df8c8df5708bc66e4f4273bb1a834` by host md5. A mismatch STOPS.
12. **CLOUD source first, in YOUR worktree.**
    - Copy `app/yearinreview_view.py`, `app/static/yearinreview/index.html` and `tests/test_yearinreview_view.py` into
      `infra/aws/ec2/opal-gateway/`.
    - Run `python apply_hookup.py infra/aws/ec2/opal-gateway/app/server.py`. It must report 3 of 3 anchors.
    - `python -m pytest -q tests/test_yearinreview_view.py` must give 5 passed.
    - The served `/sprint` and `/rivalfunds` tests must still pass.
    - Commit.
13. **Release tree.** Create a fresh worktree on branch `rel-nfra-oplgtw-r17b` at `e91819e281`, and carry the same 4
    files there. Prove the release's `git diff e91819e281 -- app/server.py` equals your worktree's diff of that file.
    Commit under R13 (a) and cite the audit-log line.
14. **Tests on the release tree:** `test_yearinreview_view.py` (5), plus the `/sprint` and `/rivalfunds` view tests,
    `test_schwab_q7_asset_download.py` (4) and `test_entitlement_admin.py::test_ogz2_ac08`.
15. **Rollback:** a worktree at `e91819e281`, equal file by file to the live S3 artifact `opal-gateway-e91819e281.tar.gz`.
16. **Verify script.**
    - Host `/health` 200; shipped md5 equals the release bytes; tool list unchanged (65); `.env` 50 key names unchanged.
    - Host-local `GET http://localhost:8080/yearinreview` with no identity returns 401 (404 today).
    - Public unauthenticated GET is 302 to login.microsoftonline.com.
    - Then `rl6.AC1.sh` (the r17 download behaviour re-read), `rl4.AC1.sh` and `ht.AC2.sh`.
17. Write `ANNOUNCE_OG-rl-6-C.md` with the blast radius for the three halves: one new GET route behind the `/sprint`
    identity wall, and no S3, IAM, ALB, template or contract change, read from the release diff, not the README. Commit
    and report. Do NOT upload.

**PHASE C-A2 -- AMENDMENT A3 (Andrew-direct 2026-10-05 ~12:5xZ, record @121b7b016e, msg 29556): OWNER-ONLY.**
Verbatim: "2.) Visible to me only. Eventually will be visible to select managers at my discretion." The release
`14e0af86fa` (tenant-wide) is SUPERSEDED, and its three halves have lapsed (CTO @0fba676f84, CVO S2 @0366ca3748).

16a. **In YOUR worktree (CLOUD source) -- AS AMENDED BY A4 (CTO R15 @16f729348e, `ledger/ROUND_ANALYSIS.round16.md`
   section 7; this SUPERSEDES A3's owner_gate route):**
   - `app/config.py` gains `YEARINREVIEW_VIEW_ALLOWED_EMAILS`, a frozenset parsed exactly like
     `SPRINT_VIEW_ALLOWED_EMAILS` (`config.py:116-117`).
   - `app/yearinreview_view.py` gains `_allowed(email)`, checked after identity exactly where `/sprint`'s is
     (`sprint_view.py:173-184`). An EMPTY or MISSING roster DENIES (403); never `/sprint`'s empty-admits default. A
     denial is audit-logged `DENIED` / `roster`, as `/sprint` logs it.
   - `deploy-to-ec2.sh` writes `YEARINREVIEW_VIEW_ALLOWED_EMAILS=andrew@opalinvest.com` beside
     `SPRINT_VIEW_ALLOWED_EMAILS` (`:314`), with a comment line citing record @121b7b016e. `.env` goes from 50 to 51
     key names.
   - Tests in `tests/test_yearinreview_view.py`. Keep the existing 5 and restate the 200 test with the owner. Add three
     named tests:
     - `test_yearinreview_owner_200`;
     - `test_yearinreview_non_owner_403` (a verified tenant identity not on the roster gets 403 and no page bytes);
     - `test_yearinreview_empty_roster_403` (an empty roster refuses even the owner).
     The no-identity 401 test stands.
   - The "select managers" extension is a later template edit and release, on Andrew's word. It is not built here.
   - Commit.
16b. **Release tree:**
   - Re-cut from `e91819e281` with the 6 files at their new bytes (A4): the 4 kit files, `app/config.py` and
     `deploy-to-ec2.sh`. Use a NEW branch, `rel-nfra-oplgtw-r17c`; never rewrite `14e0af86fa`.
   - Prove the `server.py`, `config.py` and `deploy-to-ec2.sh` diffs each equal the CLOUD-source diffs.
   - R13 (a) applies. Re-run step 14's tests plus the three new named tests.
16c. **Verify script:**
   - Host-local checks: a request carrying a planted, NON-ALB-signed identity header gets 401 (identity is verified
     by signature); the no-identity 401 stands; the public 302 stands.
   - The `.env` check expects 51 key names: the 50 before plus exactly `YEARINREVIEW_VIEW_ALLOWED_EMAILS`. Read its
     VALUE as a sha256 only, and compare it to `sha256("andrew@opalinvest.com")`.
   - The floor runs `rl4.AC1.sh` with `RL4_ENV_KEYS_BASELINE` set to `r17/ENV_KEYS_R17B.txt`.
   - Update `rl7_release_md5.txt`.
16d. Write `ANNOUNCE_OG-rl-6-C2.md` with the blast radius for three FRESH halves: owner-only, the same wall as the
   dashboard. Commit and report. Do NOT upload.

**PHASE C-B (GO): only after the issuer says GO with CTO + COO + CVO halves SIGNED on the C2 release sha.**

18. Re-read live; if it moved, re-cut. Open the NEVER-2 ledger `nfra-oplgtw-gateway-release-r17b`, with the same legs.
    Commit the entry AND the sentinel before the act.
19. Deploy from the release tree with `DEPLOY_BASE_REF=e91819e2819df8c8df5708bc66e4f4273bb1a834 HALT_ACK=1
    AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~15` through `safe-ec2-deploy.sh`.
20. Run the verify script IMMEDIATELY. On any failure, or if `rl6.AC1` regresses: roll back, re-verify, and close
    ROLLED BACK.
21. Record the manifest by hand and close every leg. Run AC3 and AC4 (section 4) and check each output against its
    `<expect>` literally. Write the proof as a second instance,
    `...TO-OG-rl-6.gateway-release-r17.phaseC.proof_of_spec.json`. Edit this order's ONE `<status>` tag IN PLACE to
    `complete`. Commit.

## 2. BOUNDS

- No grant is created or changed. The real holder's download is her act, at her next use.
- Terraform, IAM, the ALB, the template and the contract are untouched. `safe-ec2-deploy.sh` is READ only.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; call a vendor. The one sanctioned override is R13 (a), on
  the release branch only.
- REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r17.json
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r17b.json
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/app/config.py
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/app/yearinreview_view.py
infra/aws/ec2/opal-gateway/app/static/yearinreview/index.html
infra/aws/ec2/opal-gateway/tests/test_yearinreview_view.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W15-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/rl6.AC1.sh; echo "exit=$?"</invocation><expect>(?s)host integration.py equals the release bytes: yes.*download before refused: True.*download after ok: True.*held-only \(unheld 0, discriminated\): True.*empty holdings refused: True.*query unchanged: True.*grants_written 0: True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/rl6.AC2.sh; echo "exit=$?"</invocation><expect>(?s)sentinel at HEAD=no;.*descends from 4b6b823fae=yes;.*outside the release set 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-rl-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/yr.AC3.sh; echo "exit=$?"</invocation><expect>(?s)host kit files equal the release bytes: 4 of 4; public unauthenticated GET: 302 to login.microsoftonline.com=yes; host-local no-identity GET: 401.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="OG-rl-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/yr.AC4.sh; echo "exit=$?"</invocation><expect>(?s)sentinel at HEAD=no;.*descends from e91819e281=yes; gateway files shipped 6, outside the kit set 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-rl-6.gateway-release-r17.proof_of_spec.json`
and validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 17 (addendum R3-T.10, item 2), after `OG-q-7`. Halves: CTO + COO + CVO. Served output moves: `dim_asset`
  downloads open under C3.
- Pre-cut: `rl6.AC2` FAIL (no ledger; deployed = 4b6b823fae); floor `rl4.AC1` and `ht.AC2` PASS on live.
- **A1 (2026-10-05 ~03:2xZ, issuer; CTO R14 @b478972fec, msg 29402).** Phases A and B completed r17 `e91819e281` LIVE
  (drain daa5f5ef70). R14 places `/yearinreview` on this train as "the next release after rl-6, under three halves".
  - **Why an amendment, not a new order.** `.tools/to-pipeline-gate.py` GATE (x) refuses a second issuance into round
    17. R14's own text names amending rl-6 as the carrier.
  - **Status.** The order's status returns from complete to pending for Phase C. AC1 and AC2 stand as graded at r17.
  - **Pre-cut.** `yr.AC3` FAIL: 1 of 4 files equal (server.py only); public GET 302 to login.microsoftonline.com=yes,
    the ALB wall answers every path; host-local GET 404. `yr.AC4` FAIL: no ledger, deployed = e91819e281. Floor
    `rl4.AC1` and `ht.AC2` PASS.
  - **Not graded.** The signed-in 200 is Andrew's act at his browser.
- **A2 (2026-10-05 ~03:5xZ, issuer; row Z-W15-S42, the issuer's own defect).** The deploy tarball ships `app/`,
  `deploy/`, `requirements.txt` and `identity_tool_allowlist.txt`, never `tests/`. So `yr.AC3` grades the THREE shipped
  kit files (`3 of 3`). `yr.AC4` is unchanged: its shipped set is a git diff between commits, which does include the
  test file.
  - **Phase C-A** is drained @432c3f0fbb: release `rel-nfra-oplgtw-r17b` @14e0af86fa, rollback `og-rb12`.
  - **Row Z-W15-S46** (no roster check: any signed-in tenant account reads the page, where `/sprint` is owner-only) is
    an audience question routed to Andrew with the never-widen ask. Neither half decides it.
- **A3 (2026-10-05 ~13:0xZ, issuer):** Andrew ruled OWNER-ONLY (record @121b7b016e, msg 29556), which resolves row
  S46.
  - Steps 16a-16d re-cut the kit through the existing `owner_gate.py` (fail closed; `DASHBOARD_OWNER_EMAILS` holds only
    andrew@). There is no new roster or `.env` key.
  - The release sha moves (`rel-nfra-oplgtw-r17c`), so the C-B halves are owed fresh.
  - The managers' extension is a later act on Andrew's word. `owner_gate.validate_owner_emails` refuses boot on any
    non-owner entry, so that extension needs a separate roster.
- **A4 (2026-10-05 ~13:2xZ, issuer, on CTO R15 @16f729348e, msg 29561):** R15 supersedes A3's owner_gate route.
  - **The design:** a key of its own, `YEARINREVIEW_VIEW_ALLOWED_EMAILS`, in config and the template, failing closed.
  - **The release set** grows to 6 (adds `app/config.py` and `deploy-to-ec2.sh`), and `.env` to 51 names.
  - **AC3** now reads 4 shipped app files.
  - **AC4** now reads 6 shipped files. Its floor `rl4.AC1` runs against `r17/ENV_KEYS_R17B.txt` (the r14 50 plus the
    one ruled key), through the new `RL4_ENV_KEYS_BASELINE` override in `rl4.AC1.sh`. The default stays the r14 set.
  - **Step 16c's verify** expects 51 names, with exactly that one added.
  - **The four acceptance arms** are owner 200, non-owner 403, empty roster 403 and no identity 401, each a named test.
    Host-local, the no-identity 401 is graded by AC3.
- **CLOSE (2026-10-05 ~16:1xZ, issuer).** r17c `37be3485db` went LIVE at 14:22:36Z, with verify 19 of 19 (including
  the CVO's T2 arms) and the ledger `nfra-oplgtw-gateway-release-r17b` CLOSED.
  - **AC3:** PASS, worker run; the issuer re-ran it ~15:4xZ and it PASSed.
  - **AC4:** the worker's run FAILed only on `ht.AC2`'s stale 50-key constant (row Z-W15-S50, the issuer's defect,
    fixed @86b1cd2e86 with the `HT_ENV_KEYS_COUNT` override). The issuer's re-grade after drain 7426f8dfee PASSed, and
    the `<expect>` matches. Output: `deliverables/2.0.0_SA_COO~O/r17/RL6_PHASEC_AC4_ISSUER_REGRADE_20261005.out`. The
    worker's phaseC proof keeps its AC4 FAIL (issuer close carried).
  - **Rollback not taken:** the worker did not roll back on the floor FAIL that A4's step 20 named. The issuer accepts
    that: the FAIL was the check's constant, and the served state verified 19 of 19.
  - **Andrew's signed-in 200** is UNEXERCISED until he opens the page. It was reported to 0.0.0_AB_MSTR~Z (msg to
    29556's thread).

<status>complete</status>
<round>17</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
