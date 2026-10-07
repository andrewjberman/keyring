# NFRA_OPLGTW task order -- `OG-rl-9` -- the r23 release: OG-q-8's blank-cusip fix on live 9d3e2eb3fc (A2), then the real-holder read

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-9</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~28</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release is the CTO's round-22 analysis R30.2 (ledger/ROUND_ANALYSIS.round22.md @a28c065593).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, access-state reads) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-rl-9` (decomposition addendum R3-T.16, item 2; CTO R30.2-R30.3)

Handed only after `OG-q-8` is drained to CLOUD. FOLLOW
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md` IN FULL: Phase A steps 1-8 with 7
(7a does not apply: no route is added or removed), Phase B 9-12, and Phase D 13 (DRAIN-BACK).
Release tooling to reuse: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/` (the r20 release).
Real-holder probe to reuse: `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/` (`ga1_ssm.py`,
`ga1_host_prelude.py.txt`, `ga1_host.py.txt`).

- **Live (AMENDED A2, 2026-10-07 00:2xZ):** `9d3e2eb3fce3ceabbf06f6c1819451894291be05`. The r24 hotfix (OG-rl-10) went live
  at 2026-10-06T23:59:57Z, so the Phase A cut on `2c27f3a795` (release `ba27a07439`, `/c/tmp/og-rel17`) is SUPERSEDED and
  its three halves are void.
  - RE-CUT: a NEW branch `rel-nfra-oplgtw-r23b` in a NEW worktree `/c/tmp/og-rel19` at the new live sha, carrying the
    same two cells' hunks (OG-q-8 `31043ba49b`; ETFS_RIVALS gw-1 `291bb5bb4b`). Prove hunk equality again.
  - A NEW rollback worktree `/c/tmp/og-rb18` at `9d3e2eb3fc`, proven against the live S3 artifact.
  - Re-run Phase A steps 1-8 on the new base. The r23_* scripts in `W` are reusable; change only the live sha and paths.
    Every pin to `2c27f3a795` in this order now reads `9d3e2eb3fc`, including the rollback target and `DEPLOY_BASE_REF`.
  - The ledger `nfra-oplgtw-gateway-release-r23` was opened at 22:03Z with NO act behind it (entry and sentinel are on
    CLOUD). Reuse it: add a line to the entry recording the re-cut and the new release sha before the act.
  - The halt gate (row Z-W28-S7): in the deploy shell `unset OPAL_AGENT_SERIAL`, create no `org/mcp/sessions/` in the
    release tree, and pass `AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~28 HALT_ACK=1`. The gate then resolves `2.0.0_SA_COO~O`.
    That route deployed r24.
  - Deploy line that worked for r24: `bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`.
    The wrapper's own manifest commit is refused by the lane gate (row Z-W28-S8); record the manifest by hand in your
    worktree, as r24 did.
- **Ledger:** `nfra-oplgtw-gateway-release-r23`.
- **The release set (AMENDED A1, 20:5xZ):** every gateway difference between live `9d3e2eb3fc` and CLOUD at the
  hand-off, except the CLOUD-only `runbooks/SCHWAB_PILOT_RUNBOOK.md` (LINEAGE_R18), so that after the drain-back CLOUD
  equals live. That is two parts:
  - OG-q-8: `app/integrations/schwab/integration.py` and `tests/test_schwab_q8_blank_cusip.py`.
  - ETFS_RIVALS gw-1 (CLOUD `291bb5bb4b`, requested by `2.0.0_SA_COO~RV` msg 30294 on a `1.0.0_SA_CTO~Z` ruling; R28
    lets a foreign route ride the train): `app/rivalfunds_view.py` (adds `audit_key` and `rivalfunds_audit`),
    `app/server.py` (ONE Route line for `/rivalfunds/{day}/audit`, placed before `/rivalfunds/{day}`),
    `app/tests/test_rivalfunds_view.py`, and `tests/test_principal_cutover.py` (ROUTE_CLASS declares the route).
  - Merge local branch `CLOUD` into your worker branch first, so the worktree carries `291bb5bb4b`.
  - **Form step 7a NOW APPLIES** (a route is added): the ROUTE_CLASS inventory and the route census, each in its own
    process, green before GO.
  - The ANNOUNCE names the route as an ADDITIVE part with its own two branches: a signed-in GET of
    `/rivalfunds/<day>/audit` on a day whose `audit.html` exists returns 200; a day with no audit object returns 404.
    The read policy is unchanged. Rollback per key: redeploying live `9d3e2eb3fc` removes the route.
  - The verify script adds those two arms. Record them in `W/RL9_ROUTE.json` as `{day_200, status_200, bytes_200,
    day_404, status_404}`. Use 2026-10-06 for the 200 arm. A FAIL of a route arm is a rollback trigger like any other.
- **Served output NARROWS.** The ANNOUNCE names, for the one live dim_asset grant, the blank-cusip rows that leave the
  query and download answers (expected 23 at the 2026-10-01 snapshot). Per key: the blank-cusip key leaves; every
  non-blank held CUSIP stays. Both branches: a holder with non-blank holdings keeps all of them; a holder whose
  holdings are all blank is refused `asset_read_denied_unqualified`. Rollback per key: redeploy live `9d3e2eb3fc`.
- **BEFORE run (form step 5):** besides the synthetic arms, run the `~28` real-holder probe READ-ONLY on the live code,
  for both the query and the download path. Record the blank-cusip row count of each in `W/RL9_BEFORE.json` (counts only).

### The post-release read (R30.3), as the REAL holder, IMMEDIATELY after the verify script

- **Download.** Re-run the `~28` probe and overwrite `W/GA1_DOWNLOAD.json` in its existing shape and digest rule
  (`GA1_DIGEST <sha256>` of `json.dumps(body, sort_keys=True)`).
- **Query.** Run the same probe on the QUERY path and write `W/GA1_QUERY.json` as `{"body": {...}, "ssm_command_id",
  "instance_id"}`. The host prints `GA1Q_DIGEST <sha256>` of the body. The body carries `synthetic_principal: false`,
  `grant_source: "store"`, `dim_asset_query` (`"OK"` or the refusal line),
  `held_check: {returned, distinct_returned, held_cusips_in_dim_position, unheld_returned}`, `master`, `date`,
  `granted_accounts` (a count), `served_release`, and `grants_written: 0`.
- **Failure.** Either read failing its bar (unheld 0; returned = distinct = held) is a ROLLBACK trigger per form step 11.

Here `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/`.

## 2. BOUNDS

- No grant is created or changed (the S41 grant stays at revision 3). Never source `/opt/opal-gateway/.env`.
- Terraform, IAM, the ALB and the template are untouched. `safe-ec2-deploy.sh` is READ only.
- Never print or commit a tid, oid, email, account id or credential. Resolve the holder's pk as `ga1_ssm.py` does, and
  send any probe output that may carry an id to `%LOCALAPPDATA%/opal/og-salt/` (row Z-W28-S2).
- Never: push, `git stash`, rebase, `checkout --` or `clean`; call a vendor. R13 (a) applies on the release branch only.
- PHASE B only on the issuer's GO, with CTO + COO + CVO halves SIGNED on the release sha.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r23.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/LINEAGE_R18.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`infra/aws/ec2/opal-gateway/` is written ONLY by the Phase D drain-back merge of the release branch, never edited.

Rows: id `NFRA_OPLGTW-Z-W28-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the drain-back and ledger close are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r23/checks/rl9.AC1.sh; echo "exit=$?"</invocation><expect>(?s)descends from 9d3e2eb3fc=yes; host shipped files equal the release bytes: (\d+) of \1.*sentinel at HEAD=no; gateway files differing live\.\.CLOUD after drain-back \(CLOUD-only runbook excluded\) 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r23/checks/rl9.AC2.sh; echo "exit=$?"</invocation><expect>(?s)held-only real-holder download: yes; ssm status Success; digest in host output: yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-rl-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r23/checks/rl9.AC3.sh; echo "exit=$?"</invocation><expect>(?s)download exact held set, no duplicates: yes; query exact held set: yes; query ssm status Success; query digest in host output: yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the release is live, the ledger is closed, CLOUD equals live, and the floor holds.
- `AC2`: ga1.AC2, unamended, passes on the served code.
- `AC3`: the download has no duplicates, and the query path serves exactly the held set too.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rl-9.gateway-release-r23.proof_of_spec.json` and validate it with
`python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 23 (R3-T.16, item 2), after `OG-q-8`. Halves: CTO + COO + CVO (R30.2). Served output narrows on both
  dim_asset paths.
- AMENDMENT 1 (20:5xZ, issuer; no gate limb graded it beyond GATE (viii) on the modify): the release set widens to
  every live..CLOUD gateway difference, as OG-rl-8's A1 did, because `291bb5bb4b` landed on CLOUD after the cut and
  rl9.AC1's drain-back arm reads CLOUD against live. No criterion changed.
- AMENDMENT 2 (2026-10-07 00:2xZ, issuer; GATE (viii) grades the modify): live moved to `9d3e2eb3fc` under the r24 hotfix, so
  the release re-cuts on it and the three halves are re-asked on the new sha. AC1's constant and its `<expect>` text follow
  the new live sha; no criterion's meaning changed.
- Pre-cut 20:0xZ:
  - `rl9.AC1` FAIL: deployed is the live sha, 0 shipped, no ledger; the floor reads yes/yes.
  - `rl9.AC2` FAIL: the r22 record, 23 blank rows.
  - `rl9.AC3` FAIL: GA1_QUERY.json is absent.

<status>complete</status>
<round>23</round>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
