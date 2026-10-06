# NFRA_OPLGTW task order -- `OG-rl-9` -- the r23 release: OG-q-8's blank-cusip fix on live 2c27f3a795, then the real-holder read

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

- **Live:** `2c27f3a7958de0aa644374cdd08fc188a27e9e3f`.
- **Ledger:** `nfra-oplgtw-gateway-release-r23`.
- **The release set:** `app/integrations/schwab/integration.py` (OG-q-8's one-line change) and
  `tests/test_schwab_q8_blank_cusip.py`. The only other live..CLOUD gateway difference,
  `runbooks/SCHWAB_PILOT_RUNBOOK.md`, is CLOUD-only (LINEAGE_R18) and does not ship.
- **Served output NARROWS.** The ANNOUNCE names, for the one live dim_asset grant, the blank-cusip rows that leave the
  query and download answers (expected 23 at the 2026-10-01 snapshot). Per key: the blank-cusip key leaves; every
  non-blank held CUSIP stays. Both branches: a holder with non-blank holdings keeps all of them; a holder whose
  holdings are all blank is refused `asset_read_denied_unqualified`. Rollback per key: redeploy live `2c27f3a795`.
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
  <criterion id="AC1" cell_refs="OG-rl-9"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r23/checks/rl9.AC1.sh; echo "exit=$?"</invocation><expect>(?s)descends from 2c27f3a795=yes; host shipped files equal the release bytes: (\d+) of \1.*sentinel at HEAD=no; gateway files differing live\.\.CLOUD after drain-back \(CLOUD-only runbook excluded\) 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
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
- Pre-cut 20:0xZ:
  - `rl9.AC1` FAIL: deployed is the live sha, 0 shipped, no ledger; the floor reads yes/yes.
  - `rl9.AC2` FAIL: the r22 record, 23 blank rows.
  - `rl9.AC3` FAIL: GA1_QUERY.json is absent.

<status>pending</status>
<round>23</round>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
