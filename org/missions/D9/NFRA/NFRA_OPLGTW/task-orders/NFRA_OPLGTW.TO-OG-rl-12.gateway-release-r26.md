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
AND 7a (AMENDED A3: a route is added), Phase B 9-12, and Phase D 13. Step 10 names the deploy line, the
deploy identity and the manifest commit. Reuse the `r25_*` tooling in
`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/`; copy to `r26_` names.

- **Live:** `240ac2fe5abde944f15358ab563cb4b2ab63f09f` (r25). Re-read it by host md5 first. If the manifest names
  another sha, STOP and report: this order was cut before r25 deployed.
- **Ledger:** `nfra-oplgtw-gateway-release-r26`.
- **Release branch** `rel-nfra-oplgtw-r26`, a NEW worktree `/c/tmp/og-rel21` at the live sha. **Rollback tree:** a NEW
  `/c/tmp/og-rb20` at the live sha, proven against the live S3 artifact.
- **The release set:** every gateway difference between live and CLOUD at the hand-off, except the CLOUD-only
  `runbooks/SCHWAB_PILOT_RUNBOOK.md`. Expected (AMENDED A1): `identity_tool_allowlist.txt` (one added row and its comment
  lines; it ships to the host), `app/integrations/opal_portal/integration.py` (the execution-id shape check of row
  Z-S65; it ships), and two source-only tests, `tests/test_identity_scope_status_row.py` and
  `tests/test_opal_portal_status_id_shape.py`.
  - **AMENDED A2 (CTO R36):** the set also carries `OG-up-2`, the content-keyed re-send dedupe, in the same
    `app/integrations/opal_portal/integration.py`, with its source-only `tests/test_opal_portal_dedupe_content.py` and
    any send-split or id-shape test fake that cell changed. Handed only after `OG-up-2` is drained too.
  - The dedupe cannot be exercised live without a real send, which this project never runs. The ANNOUNCE says so: it
    rests on the offline tests, and the first corrected same-date re-send is its first live exercise.
  - **AMENDED A3 (release request: 1.0.0_SA_CTO~Z msgs 30765, 30774):** the set also carries ETFS_RIVALS `RIV-rt-1`,
    the chart route. Take its hunks from `git diff f7f2cb7c2e^1 f7f2cb7c2e -- infra/aws/ec2/opal-gateway`: 4 files,
    `app/rivalfunds_view.py`, `app/server.py` (ONE Route line), `app/tests/test_rivalfunds_view.py`, and the
    source-only `tests/test_principal_cutover.py`. The release commit `f1a6582ee1` predates this: RE-CUT it. Reset
    branch `rel-nfra-oplgtw-r26` in `/c/tmp/og-rel21` to ONE new commit on live `240ac2fe5a` carrying all three cells,
    and prove `git diff --name-only <new sha> e3beea0b5c -- infra/aws/ec2/opal-gateway` lists the runbook only.
    - Re-run Phase A steps 1-7 and 7a on the NEW sha. A step whose earlier output does not depend on the release
      bytes (step 1, step 4) is re-read, not rebuilt.
    - The route is ADDITIVE. The verify script's AFTER arms gain, in-process on the host with a synthetic viewer:
      `/rivalfunds/2000-01-01/chart/ABC` answers 404 with `no chart for this fund and day`;
      `/rivalfunds/2026-10-06/chart/abc` answers 400; `/rivalfunds/2026-10-06` and `/rivalfunds/2026-10-06/audit`
      answer as they do on the installed code. Record them in `W/RL12_FLOOR.json` as `chart_404`, `chart_400`,
      `day_page_unchanged`, `audit_page_unchanged`. Any of the four off its value is a rollback trigger.
    - No chart object exists under the page prefix yet (0 of 115 keys), so the 200 arm rests on
      `app/tests/test_rivalfunds_view.py`. The ANNOUNCE says so. Write no object to S3.
    - The ANNOUNCE's blast radius covers all three cells. The route's text is in
      `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/RELEASE_NEEDS_RIV-rt-1_CHART_ROUTE_20261007.md`
      sections 2 and 3 (on CLOUD @ec89bbe212; read it with `git show ec89bbe212:<path>`).
  - If CLOUD carries any OTHER gateway difference, STOP before the release commit and report its files and commits.
    Another seat's change needs its own release request and halves; do not carry it silently.
- **Served output WIDENS, by Andrew's word.** The ANNOUNCE names it:
  - the one scoped identity gains ONE tool, `opal_data_refresh_status`, read-only, on any client;
  - its Graph consent does not change (the tool maps to no scope);
  - every other identity and every other tool is unchanged.
  - Rollback per key: redeploying live `240ac2fe5a` removes the row.
- **One property NARROWS (A1):** `opal_data_refresh_status` refuses a malformed `execution_id` before any request.
  The REHEARSAL and the post-deploy read each show one refused id (for example one containing `/`) and one accepted
  id, the known 2026-10-07 ~01:26Z execution. Record both in `W/RL12_FLOOR.json` as `status_id_refused` and
  `status_id_accepted`.

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

**AMENDED A4 (CTO half, condition C2, @78d524e001).** The post-deploy read shows TWO refused ids through the installed
code, one containing `/` and one containing `.`, each making 0 HTTP requests. Record them in `W/RL12_FLOOR.json` as
`status_id_refused` (the `/` id, as before) and `status_id_refused_dot`. A request made on either is a rollback trigger.

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
- AMENDMENT 1 (04:4xZ, issuer, before any hand-off): the release set gains OG-al-2's item 4 (row Z-S65, CTO msg 30563).
- AMENDMENT 2 (05:2xZ, issuer, before any hand-off): the release set gains OG-up-2 (CTO R36, msg 30594).
- AMENDMENT 3 (10:2xZ, issuer, after the Phase A partial and before any GO): the release set gains ETFS_RIVALS RIV-rt-1
  (the chart route) on 1.0.0_SA_CTO~Z's release ask, msgs 30765 and 30774; form step 7a now applies; the release
  commit is re-cut. No criterion changed. Gate: LIMB 6 does not grade a modification; GATE (viii) reads
  `<placeholders>NONE</placeholders>`.
- AMENDMENT 4 (11:2xZ, issuer, before any GO): the CTO half's C2 adds a second refused-id arm (an id containing `.`).
  No criterion changed. Gate: LIMB 6 does not grade a modification; GATE (viii) reads placeholders NONE.
- OWED BY THE ISSUER after the deploy (CTO half C1): at the first real send, one read of whether each of the two drive
  items carried a readable hash. Unreadable on either: one fallback cell in the next issuance (the r25 name-and-size
  key), and the callers are told a repeat fires. If the send's return does not show it, a cell puts it there.
- Pre-cut 04:3xZ: `rl12.AC1` FAIL (r25 is not live yet; no ledger). `rl12.AC2` FAIL (the record is absent).

<status>pending</status>
<round>25</round>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
