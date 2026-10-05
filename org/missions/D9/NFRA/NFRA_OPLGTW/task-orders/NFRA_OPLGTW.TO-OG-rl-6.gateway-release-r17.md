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
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W15-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/rl6.AC1.sh; echo "exit=$?"</invocation><expect>(?s)host integration.py equals the release bytes: yes.*download before refused: True.*download after ok: True.*held-only \(unheld 0, discriminated\): True.*empty holdings refused: True.*query unchanged: True.*grants_written 0: True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-6"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r17/checks/rl6.AC2.sh; echo "exit=$?"</invocation><expect>(?s)sentinel at HEAD=no;.*descends from 4b6b823fae=yes;.*outside the release set 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-rl-6.gateway-release-r17.proof_of_spec.json`
and validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 17 (addendum R3-T.10, item 2), after `OG-q-7`. Halves: CTO + COO + CVO. Served output moves: `dim_asset`
  downloads open under C3.
- Pre-cut: `rl6.AC2` FAIL (no ledger; deployed = 4b6b823fae); floor `rl4.AC1` and `ht.AC2` PASS on live.

<status>pending</status>
<round>17</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
