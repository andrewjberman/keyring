# NFRA_OPLGTW task order -- `OG-rl-12` -- the r26 release on live r25 (240ac2fe5a): the concierge's status-tool allowlist row (OG-al-2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-12</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~28</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release ships Andrew's ruled row (record @4403ac63df), as the CTO's msg 30555 routes it.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-rl-12` (decomposition addendum R3-T.19, item 2)

Handed only after BOTH hold: release r25 (`OG-rl-11`) is live and closed, and `OG-al-2` is drained to CLOUD. FOLLOW
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md` IN FULL: Phase A steps 1-8 with 7
(7a does not apply: no tool and no route is added), Phase B 9-12, and Phase D 13. Step 10 names the deploy line, the
deploy identity and the manifest commit. Reuse the `r25_*` tooling in
`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/`; copy to `r26_` names.

- **Live:** `240ac2fe5abde944f15358ab563cb4b2ab63f09f` (r25). Re-read it by host md5 first. If the manifest names
  another sha, STOP and report: this order was cut before r25 deployed.
- **Ledger:** `nfra-oplgtw-gateway-release-r26`.
- **Release branch** `rel-nfra-oplgtw-r26`, a NEW worktree `/c/tmp/og-rel21` at the live sha. **Rollback tree:** a NEW
  `/c/tmp/og-rb20` at the live sha, proven against the live S3 artifact.
- **The release set:** every gateway difference between live and CLOUD at the hand-off, except the CLOUD-only
  `runbooks/SCHWAB_PILOT_RUNBOOK.md`. Expected: `identity_tool_allowlist.txt` (one added row and its comment lines;
  it ships to the host) and `tests/test_identity_scope_status_row.py` (source-only).
  - If CLOUD carries any OTHER gateway difference, STOP before the release commit and report its files and commits.
    Another seat's change needs its own release request and halves; do not carry it silently.
- **Served output WIDENS, by Andrew's word.** The ANNOUNCE names it:
  - the one scoped identity gains ONE tool, `opal_data_refresh_status`, read-only, on any client;
  - its Graph consent does not change (the tool maps to no scope);
  - every other identity and every other tool is unchanged.
  - Rollback per key: redeploying live `240ac2fe5a` removes the row.

**BEFORE and REHEARSAL (form step 5), host runs one at a time, each in its own scratch directory.**
- BEFORE, on the installed code: the scoped identity is DENIED `opal_data_refresh_status`; the overlay's row count.
- REHEARSAL, on the staged release bytes with the installed tree untouched: the scoped identity is ADMITTED for it; a
  tool that neither seed nor overlay names is still DENIED; `consent_scopes` for the scoped identity is still 9; the
  tool count is still 66.
- Read the decision through `app/identity_scope.py`'s own functions. Never print an email address: refer to the
  identity as "the scoped concierge".

**The post-deploy read, IMMEDIATELY after the verify script, through the INSTALLED code.** Write
`W/RL12_ALLOW.json` as `{"body": {...}, "ssm_command_id", "instance_id"}`. The host prints `RL12_DIGEST <sha256>` of
`json.dumps(body, sort_keys=True)`. Body fields, exactly: `served_release`, `installed_code: true`,
`status_tool_allowed_for_scoped`, `unnamed_tool_allowed_for_scoped`, `scoped_scope_count`, `tools`,
`overlay_rows_before`, `overlay_rows_after`, `grants_written: 0`.
Also re-read the standing floor into `W/RL12_FLOOR.json`: the portal login OK, and the real holder on both paths.
- **Rollback triggers:** the scoped identity not admitted for the status tool; an unnamed tool admitted; the consent
  count moved; a floor read off its bar.

**ONE STOP for the halves.** Run Phase A, write `W/ANNOUNCE_OG-rl-12.md`, commit and report. Phase B starts on the
issuer's GO, with CTO + COO + CVO halves SIGNED on the release sha.

## 2. BOUNDS

- No grant or state-store write. No `.env`, secret, Terraform or IAM write.
- Never run `opal_data_refresh_upload` with `confirm=True`, and never POST `/trigger`.
- No `/login` for the concierge in this order.
- Never print or commit a tid, oid, account id, credential or token; never print an email address to a log or a record.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; call a vendor. R13 (a) applies on the release branch only.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r26.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/LINEAGE_R18.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`infra/aws/ec2/opal-gateway/` is written ONLY by the Phase D drain-back merge of the release branch, never edited.

Rows: id `NFRA_OPLGTW-Z-W28-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the drain-back and ledger close are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-12"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r26/checks/rl12.AC1.sh; echo "exit=$?"</invocation><expect>(?s)descends from 240ac2fe5a=yes; host shipped files equal the release bytes: (\d+) of \1.*sentinel at HEAD=no; gateway files differing live\.\.CLOUD after drain-back \(CLOUD-only runbook excluded\) 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-12"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r26/checks/rl12.AC2.sh; echo "exit=$?"</invocation><expect>(?s)nothing else widened: fields=yes ssm=Success digest=yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the release is live, the ledger is closed, CLOUD equals live, and the floor holds.
- `AC2`: the served gateway admits the concierge for the status tool and nothing else moved.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rl-12.gateway-release-r26.proof_of_spec.json` and validate it with
`python .tools/proof-of-spec-check.py <instance>`. Flip the ONE `<status>` tag to `complete` only if both PASS. Report
once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 25 (R3-T.19, item 2), after `OG-al-2` and after r25 closes. Halves: CTO + COO + CVO (CTO msg 30555).
- `rl12.AC1` pins the live sha to r25's release sha `240ac2fe5a`, the value the manifest will carry once r25 deploys.
  Should r25 roll back or re-cut, the issuer amends the pin before the hand-off.
- Pre-cut 04:3xZ: `rl12.AC1` FAIL (r25 is not live yet; no ledger). `rl12.AC2` FAIL (the record is absent).

<status>pending</status>
<round>25</round>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
