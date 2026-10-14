# NFRA_OPLGTW task order -- `OG-ap-14` -- APPLY: the r30 gateway release, OG-pf-1 + OG-tg-1 + OG-bd-2 + OG-sh-1, re-cut on the live ref behind NFRA_MCPORTAL MP-z-5 (round-37 R1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-14</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-14</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut, amended A1 -- the gateway queue is NFRA_MCPORTAL MP-z-5 (LIVE @64b3e54658, ledger closed 21:44:07Z), then NFRA_MCPINDEX MX-r-11 (2 files, no tool), then THIS release; MCPORTAL MP-n-4 follows. Phase B1 starts only after MP-z-5's ledger is CLOSED and its sentinel gone. B2 window 11:00Z-23:00Z. No cron, alarm or monitor is created.
comp-iam: RUN-BY-ISSUER -- every API call the four cells' code makes, read at the cut: pf-1 and bd-2 are in-process decisions (no AWS or Graph call); bd-2's tier read is app/tier.py resolve_tier over the deploy-time rosters (no call); tg-1 reads the sender's UPN and tenant from the Graph message payload the Teams routes already fetch (no new Graph scope, no AWS call); sh-1 calls Graph GET /shares/{id}/driveItem and /children under the signed-in user's own delegated token (Files.ReadWrite.All already consented, app/config.py:64). The release changes no role, policy or Graph consent.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's ruling org/missions/D9/NFRA/NFRA_OPLGTW/ledger/CTO_RULING_R37_ONE_RELEASE_PF1_TG1_BD2_SH1_20261013.md @8f236865cc and round-36 analysis R1 @713305ee56 (row Z-S101).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (SSM reads of the gateway host).
</preflight>

## 1. THE CELL -- `OG-ap-14` (decomposition addendum R3-T.49, R1)

Ship four built and drained cells to the opal-gateway host in ONE release. Nothing else rides.

| cell | what it changes | its commits (gateway paths only) |
|---|---|---|
| OG-pf-1 | `decide()`: a restricted profile confines only the data-grant family (`DATA_GRANT_TOOLS`: the five schwab_* tools + `blackdiamond_list_fees`) | `b47fc56a98`, `27e1969db3` |
| OG-tg-1 | sender identity (UPN, tenant) on Teams reads for every caller; the Opal-users-only gate on the Bloomberg concierge; the concierge unscoped | `5c5549b8bd`, `9abb699720` (A1 test re-pins) |
| OG-bd-2 | `blackdiamond_list_fees` denied to an unprofiled principal unless its tier is `master_admin` | `c37fdf95a5` |
| OG-sh-1 | the READ tool `list_shared_folder(url)` (tools 62 -> 63 on trunk's count) | `47cee985ee` |

box/sitez also carries other gateway work that is NOT live and is NOT in this release, for example OG-lk-1 (`c379d059eb`,
`app/audit.py`) and NFRA_MCPORTAL's later cells. Take only the six commits' hunks. Never take a whole file from trunk.

### PHASE B1 -- re-cut, prove, ask. NO deploy

1. **Precondition (A1).** NFRA_MCPORTAL's MP-z-5 ledger `nfra-mcportal-gw-release` AND NFRA_MCPINDEX's MX-r-11 release
   ledger are both CLOSED at HEAD, and their sentinels are gone (MX-r-11 takes the slot before this release). Read
   `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway.deployed_commit` at HEAD: that is the LIVE ref. Confirm it
   with ONE SSM md5 read of the host against that commit, walking `app/`, `deploy/` and `dashboard/`. A mismatch is a STOP.
   Confirm ONE gateway release in flight across all worktrees (`git worktree list --porcelain`, then each tree's
   `org/critical_paths/.open_deploys/`), with the per-tree denominator printed.
2. **Re-cut** in a worktree `C:/tmp/og-rel-r30` on a new branch `rel-nfra-oplgtw-r30`, at the live ref. Cherry-pick the
   six commits in order: `5c5549b8bd`, `9abb699720`, `b47fc56a98`, `27e1969db3`, `c37fdf95a5`, `47cee985ee`.
   - Keep ONLY paths under `infra/aws/ec2/opal-gateway/`; restore every other path a pick brings.
   - Resolve a conflict so that the cells' hunks land and nothing else changes; report every conflict and its
     resolution in the ask.
   - Commit with the audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL`, on the release branch's commits ONLY.
   - Write `W/ap14_release.json` = `{"base_sha", "release_sha", "conflicts": [..]}`.
3. **Suites** in the release tree: `tests/test_data_entitlement_family.py`, `tests/test_data_entitlement_guard.py`,
   `tests/test_opal_users_gate.py`, `tests/test_identity_scope.py`, `tests/test_og_bd2.py`, `tests/test_og_sh1.py`,
   `tests/test_entitlement_admin.py`. Record pass/fail counts and each failing id in the ask; a failing id that also
   fails at the live ref is named as pre-existing. Then run AC1.
4. **The ask**, `W/NEVER_WIDEN_ASK_OG-ap-14.md`, for `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~O`. It carries:
   - the diff by file, and the six commits each hunk came from;
   - **who gains and who loses**, per cell:
     - pf-1 WIDENS a profiled principal's reach to every non-data tool;
     - bd-2 NARROWS the unprofiled non-admin caller;
     - tg-1 NARROWS the concierge to Opal senders and unscopes the concierge;
     - sh-1 ADDS one READ tool;
   - the live principals each change touches, named from the grant store with the denominator printed (ids only, no
     names or emails);
   - every other unreleased `app/` diff (live -> HEAD), listed as EXCLUDED;
   - the triggers relative to the live base: tools +1 by name (`list_shared_folder`) only; `.env` names unchanged;
     md5 = release;
   - rollback: redeploy the live base.

   Commit, REPORT, STOP.

### PHASE B2 -- only on the issuer's GO, which names both halves signed at `release_sha`

5. Ledger `nfra-oplgtw-gateway-release-r30`: entry AND sentinel first. Deploy from `C:/tmp/og-rel-r30` through
   `infra/aws/ec2/safe-ec2-deploy.sh`, with `DEPLOY_BASE_REF=<base_sha>`. The release cone carries `lib/`, `.tools/`,
   `org/modules/graph/`, `data/transcripts/scripts/teams/` AND your agent home `org/tier2_senior/0.7.0_AE_CloudOps~Z/`.
   No `HALT_OVERRIDE`.
6. **Read back immediately** against the triggers. On any trigger, redeploy the base and file an ARMED row naming
   `2.0.0_SA_COO~O`.
7. **The served read.** One SSM read through the INSTALLED code, in-process, with synthetic principals: no Graph call,
   no grant or profile written. Write `W/AP14_SERVED.json` = `{"body": {...}, "ssm_command_id", "instance_id"}`.
   The body holds exactly these fields:

   | field | value |
   |---|---|
   | `installed_code` | `true` |
   | `data_grant_family_size` | `len(DATA_GRANT_TOOLS)` |
   | `bd_unprofiled_standard_denied` | `decide()` on `blackdiamond_list_fees`, no profile, tier `standard`, returns a denial |
   | `bd_unprofiled_master_admin_admitted` | the same with tier `master_admin` returns None |
   | `list_shared_folder_listed` | the tool is listed |
   | `list_shared_folder_safe` | `destructive_ops.classify` returns SAFE |
   | `opal_users_gate_refuses_non_opal` | the gate function tg-1 added, given a non-Opal tenant, refuses |
   | `objects_written` | `0` |
   | `bbg_identity_admitted_8` | (A2) how many of the 8 tools the installed identity-scope check admits for the principal `opalbloomberg@opalinvest.com` (by its oid from the grant store, never typed): `opal_discover`, `mdpf_get_aum_metrics`, `mdpf_get_aggregate_aua`, `mdpf_get_account_distribution`, `mdpf_get_model_benchmarks`, `etfs_get_positioning`, `gateway_query_catalog`, `ycharts_freshness`. Want 8. |
8. **Standing release clauses.**
   - Runbook 7.2 (`infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md`) names the new live release; `rb.AC2`
     reads FAIL at the cut because 7.2 does not name today's live ref, so this release brings it current.
   - EC2_MANIFEST `deployed_commit` and `file_checksums` come from the release blobs.
   - Close the ledger, commit, run AC2, and report once to `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- The six commits' gateway hunks only. No grant, profile, policy or Terraform act: the two grant writes (Andrew's
  profile; the Bloomberg mirror) are a separate act. No real Teams send, Graph call or object written by you.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; merge box/sitez into the release branch; bare `terraform`;
  print an `.env` value, a name or an email; override a gate other than the one audited lane escape in step 2.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r30.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root; AC1 after B1, AC2 after B2's ledger is closed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-14"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap14.AC1.sh; echo "exit=$?"</invocation><expect>(?s)is the live ref: yes.*outside the four cells' files 0 \(want 0\).*diff lines outside the four cells' hunks 0 \(want 0\); cell markers present 4 of 4.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-14"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ap14.AC2.sh; echo "exit=$?"</invocation><expect>(?s)entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*equal=yes; rb\.AC2 PASS; served r30 fields: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-ap-14" judgment="true"/>
</proof_of_spec>

- `AC1`: the re-cut carries exactly the four cells' hunks on the live ref. `AC2`: landed, closed, recorded, and each
  cell is served.
- `AC3` (judgment, `3.0.0_SA_CVO~Z`; A2, CTO ruling msg 33850): after this release AND the Bloomberg mirror grant write
  (NFRA_OPLGTW.TO-OG-mg-1), `0.0.3_BG_BBGTerminal` re-runs its own exercise of the 8 tools, read the same way it read
  them on 10-13. 8 of 8 ALLOWED is the arm; any tool still denied after both is a BLOCKING row, not a pass. The exercise
  is that seat's act, owed; record it UNVERIFIABLE-BY-INSTRUMENT naming the CVO and the owed act.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-14.r30-gateway-release.proof_of_spec.json`. Validate it after your last
commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip the ONE
`<status>` tag to `complete` only if both PASS. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, R1 (`ledger/ROUND_ANALYSIS.round36.md` @713305ee56; ruling @8f236865cc; row Z-S101). Measured at the cut:
  - bd-2's diff fails to apply flat on the live ref 185dc04888 (`data_entitlement.py:144`), because it rides on pf-1;
    `DATA_GRANT_TOOLS` reads 0 there.
  - live -> HEAD over `app/`, `deploy-to-ec2.sh` and `dashboard/` is 9 files, +789/-66. That set includes MP-z-5's
    `admin_gateway_breakdown.py`, which will be live by B1.
- Pre-cut dry runs:
  - ap14.AC1 base FAIL as expected (record absent).
  - ap14.AC1 arms on synthetic records: one cell commit as the release gives 0 stray lines and markers 3 of 4; the live
    ref -> trunk HEAD gives 1495 stray lines. Both read FAIL, which shows the check discriminates.
  - ap14.AC2 base FAIL as expected (records absent; rb.AC2 FAIL because runbook 7.2 does not name today's live ref).

- A1 (issuer, 2026-10-13 ~21:4xZ): the gateway slot after MP-z-5 goes to NFRA_MCPINDEX MX-r-11 (2.0.0_SA_COO~MI msg
  33805; reply 20261013T214631Z): two files, no tool, already drained, ready now, while this release has not yet built.
  Phase B1's precondition now names MX-r-11's ledger as well; the live ref is read at the act, so the base moves with it.
  Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A2 (issuer, 2026-10-14 ~00:4xZ, CTO ruling msg 33850): r30 gains a POSITIVE arm. The Bloomberg principal is denied
  8 of 8 gateway data tools today (`identity_scope_denied`, log
  `org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-10-13/capability_exercise_8of8_gateway_denied_serving_path_live_and_a_vintage_hazard.md`).
  OG-tg-1 unscopes that identity (PRD v2.3 item 2; Andrew "exact copy of opal-gateway for now").
  - The served read gains `bbg_identity_admitted_8` (ap14.AC2 extended: want 8).
  - New AC3 (judgment) is the seat's own re-exercise after r30 plus the mirror grant write (OG-mg-1, cut separately).
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A3 (issuer, 2026-10-14 ~01:3xZ): **PHASE B2 GO, effective at or after 11:00Z 2026-10-14** (the window).
  - Both halves are SIGNED at `release_sha` `db3d1972bc`: COO `deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-ap-14_20261014.md`
    @d8119a4d7a, CTO `deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_OG-ap-14_20261014.md` @2dacbf0fce (msg 33889).
  - Their conditions bind:
    - C1: correct the ask's section 2 to name OG-tg-1's unscoping of the Bloomberg principal as a widening, before B2;
    - C2: `bbg_identity_admitted_8` reads 8 through the installed code, or STOP and redeploy the base;
    - C3: the GO holds ONLY while live is still `7eff14b2e6` at the act. If NFRA_MCPORTAL MP-n-4 has moved it, the GO
      lapses: re-cut B1, re-run AC1, and both halves re-sign.
  - Before step 5, confirm ONE gateway release in flight across all worktrees, with the per-tree denominator printed.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A4 (issuer, 2026-10-14 ~02:0xZ): **PHASE B2 GO re-issued at `92698aea8c`, effective at or after 11:00Z 2026-10-14.**
  - A3's GO lapsed under C3 when NFRA_MCPORTAL MP-n-4 went live at `b0c75d24f1` (01:31Z). The re-cut `92698aea8c` (on
    `rel-nfra-oplgtw-r30b`) carries the identical change: patch-id `eac7550c45` for v1 and v2, issuer-measured.
  - Both halves are RE-SIGNED there: COO ADDENDUM 1 @f58d3d1652, CTO ADDENDUM 1 @1003665c3d (msg 33902).
  - C1 is discharged. C2 binds. C3 binds on live still `b0c75d24f1` at the act, else the GO lapses again.
  - The rollback target is `b0c75d24f1`.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A5 (issuer, 2026-10-14 ~04:3xZ): **PHASE B2 GO re-issued at `90967e39ba`, effective at or after 11:00Z 2026-10-14.**
  - A4's GO lapsed under C3 when NFRA_MCPINDEX MX-r-12 moved live, first to 027fedfda4, then (catalog-only v2) to
    `43088464f5`. The one re-cut waited for v2.
  - The re-cut `90967e39ba` (on `rel-nfra-oplgtw-r30c`) carries the identical change: patch-id `eac7550c45`, measured
    by the issuer.
  - Both halves are RE-SIGNED: COO ADDENDUM 2 @ab3eda5984, CTO ADDENDUM 2 @0314607f88 (msg 33985).
  - C2 binds. C3 binds on live still `43088464f5` at the act.
  - The rollback target is `43088464f5`.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).

- A6 (issuer, 2026-10-14 ~05:0xZ, row Z-S105, ARMED): **step 5's deploy source is RE-PINNED.**
  - Step 5 named `C:/tmp/og-rel-r30`, the v1 worktree (HEAD db3d1972bc on base 7eff14b2e6). It was never re-pinned when
    C3 fired twice. Deploying it would ship the release AND MP-n-4's and MX-r-12's files at their PRE-release blobs
    (8 files differ v1 vs v3), a silent regression of two live releases that every patch-id check passes. This is an
    issuer defect.
  - Deploy from **`C:/tmp/og-rel-r30c`** (branch `rel-nfra-oplgtw-r30c`), with
    **`DEPLOY_BASE_REF=43088464f51c81e9fe3528b080c6ca8ce5fa90fe`**. Measured by the issuer at A6: that worktree's HEAD
    is `90967e39ba4bdca17c6f84d9806c29cc67f8482e`, and its parent is `43088464f5...`.
  - **New guard, before step 5's first deploy command:** the deploy tree's `git rev-parse HEAD` must equal the signed
    `release_sha` in full, and its parent must equal live `deployed_commit`. Any mismatch is a STOP. Print both.
  - Carried to the cut template: a release order names its deploy source by `release_sha`, never by a worktree path.
  - Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
