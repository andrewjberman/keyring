# NFRA_OPLGTW task order -- `OG-rl-11` -- the r25 release on live 7d65a28db0: the send split (OG-up-1) and the scoped consent envelope (NFRA_OPALAI OA-f-14)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-11</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~28</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release is the CTO's round-23 analysis item 3 (ledger/ROUND_ANALYSIS.round23.md @c8a3b2911e) and the CTO's msg 30365 for OA-f-14.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM), the public gateway URL, Opal's own portal front door, and Microsoft Graph read probes under the gateway's existing delegated tokens.
</preflight>

## 1. THE CELL -- `OG-rl-11` (decomposition addendum R3-T.18, item 3)

Handed only after `OG-up-1` is drained to CLOUD. FOLLOW
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md` IN FULL: Phase A steps 1-8 with 7
and 7a (a TOOL is added, so the tool census and the route inventory both run), Phase B 9-12, and Phase D 13.
Reuse the r23b tooling in `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/`
(`r23b_*`, `r24_*`). Copy to `r25_` names; do not edit the originals.

- **Live:** `7d65a28db026a44d7199ffe52a97e44952df75a1`. Re-read it by host md5 first.
- **Ledger:** `nfra-oplgtw-gateway-release-r25`.
- **Release branch** `rel-nfra-oplgtw-r25`, a NEW worktree `/c/tmp/og-rel20` at the live sha. **Rollback tree:** a NEW
  `/c/tmp/og-rb19` at the live sha, proven against the live S3 artifact.
- **The release set:** every gateway difference between live and CLOUD at the hand-off, except the CLOUD-only
  `runbooks/SCHWAB_PILOT_RUNBOOK.md`, so that after the drain-back CLOUD equals live. Two parts:
  - **Part 1, OG-up-1 (CTO R33):** the send split in `app/integrations/opal_portal/integration.py`, the new read-only
    tool `opal_data_refresh_status`, and the files that enumerate it.
  - **Part 2, NFRA_OPALAI OA-f-14 (CLOUD `af10f7d42b`, requested by `2.0.0_SA_COO~AI`):** `app/graph_scope_map.py`
    (new), `app/identity_scope.py`, `app/token_broker.py`, and `tests/test_scoped_consent_r253.py`. Behaviour: the ONE
    scoped identity's `/login` consent and silent acquire narrow from 17 Graph scopes to 8, or 9 under a Tax binding.
    An unscoped identity is unchanged.
  - Prove each file's hunk set equals its cell's own diff.

**Condition from the CTO's msg 30365, BEFORE GO (Phase A).** Read on the live host whether each of
`OG_TAXSMA_WORKBOOK_IDENTITY`, `MS_INGEST_IDENTITY` and `OTP_MAILBOX` names a SCOPED identity.
- Never source `/opt/opal-gateway/.env`. Read the three keys' values in-process and compare them to the scoped
  identity set in-process.
- Record only a boolean per key. Never print or store a value.
- A `true` means that non-tool caller mints under the scoped identity, so its scopes must be in the consent union.
  Confirm the release's `consent_scopes` covers it. If it does not, STOP before GO and file a BLOCKING row.

**BEFORE and REHEARSAL (form step 5), host runs strictly ONE AT A TIME (row Z-W28-S9).**
- BEFORE, on live code: the tool count (expected 65); the scoped identity's consent scope count (expected 17).
- REHEARSAL, on the staged release bytes with the installed tree untouched:
  - the tool count is 66, and `opal_data_refresh_status` answers for a known execution id. Use the execution of
    2026-10-07 ~01:26Z, whose id is in `deliverables/0.9.0_WK_NFRA_OPLGTW~29/UP1_0126Z_READ.json` or readable from
    Step Functions;
  - the scoped identity's consent scopes are 8 or 9, and a subset of the 17; an unscoped identity's are 17;
  - **the scoped identity still works with the narrowed set.** Its silent acquire returns a token. With that token,
    one read-only Graph probe per scope family its allowlisted tools need answers 200. Run at least three probes,
    the SharePoint site resolve of `opalinvest.sharepoint.com:/sites/Shared` among them: that is the delegated leg of
    the daily Bloomberg send. A probe that does not answer 200 is a STOP before GO.
  - Never print a token. Never send a message, an email or a file under any identity.

**The post-deploy reads, IMMEDIATELY after the verify script, through the INSTALLED code.**
- `W/RL11_SEND.json` as `{"body": {...}, "ssm_command_id", "instance_id"}`. The host prints `RL11S_DIGEST <sha256>` of
  `json.dumps(body, sort_keys=True)`. Body fields, exactly: `served_release`, `installed_code: true`, `tools_before`,
  `tools_after`, `status_tool` (`"OK"` or the error text), `status_value`, `max_inline_wait_s` (the most the real-send
  path can wait after `/trigger`, read from the installed module's constants), `confirm_true_run: false`,
  `grants_written: 0`.
- `W/RL11_SCOPES.json`, same shape, with `RL11C_DIGEST <sha256>`. Body fields, exactly: `served_release`,
  `installed_code: true`, `unscoped_scope_count`, `scoped_scope_count`, `scoped_subset_of_full`,
  `scoped_silent_acquire` (`"OK"` or the error text), `probes_run`, `probes_ok`, `sharepoint_site_resolve` (the HTTP
  status), `identity_keys_scoped` (`{"OG_TAXSMA_WORKBOOK_IDENTITY": bool, "MS_INGEST_IDENTITY": bool,
  "OTP_MAILBOX": bool}`), `grants_written: 0`.
- Also re-read the two standing properties: the installed code's portal login is still OK (the r24 hotfix), and the
  real holder still gets returned = distinct = held with 0 unheld on the query and download paths (the r23 fix).
  Record both in `W/RL11_FLOOR.json`.
- **Rollback triggers:** a scoped silent acquire that is not OK; any probe not 200; a status tool that errors; a
  portal login that is not OK; a real-holder read off its bar.

**The halt gate.** In the deploy shell `unset OPAL_AGENT_SERIAL`, create no `org/mcp/sessions/` in the release tree,
and pass `AGENT_NAME=0.9.0_WK_NFRA_OPLGTW~28 HALT_ACK=1`; the gate then resolves `2.0.0_SA_COO~O`. Deploy line:
`bash infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`, from the release
worktree. The wrapper's own manifest commit is refused by a lane gate after the deploy lands (row Z-W28-S8): record
the manifest by hand in your worktree.

**ONE STOP for the halves.** Run Phase A, write `W/ANNOUNCE_OG-rl-11.md`, commit and report. Phase B starts on the
issuer's GO, with CTO + COO + CVO halves SIGNED on the release sha.

## 2. BOUNDS

- No grant is created or changed. `identity_tool_allowlist.txt` does not change. No `.env`, secret, Terraform or IAM write.
- Never run `opal_data_refresh_upload` with `confirm=True`, and never POST `/trigger`. This project runs no real send.
- Never print or commit a tid, oid, email, account id, credential or token.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; call a vendor. R13 (a) applies on the release branch only.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r25.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~28/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/LINEAGE_R18.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`infra/aws/ec2/opal-gateway/` is written ONLY by the Phase D drain-back merge of the release branch, never edited.

Rows: id `NFRA_OPLGTW-Z-W28-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the drain-back and ledger close are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-11"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r25/checks/rl11.AC1.sh; echo "exit=$?"</invocation><expect>(?s)descends from 7d65a28db0=yes; host shipped files equal the release bytes: (\d+) of \1.*sentinel at HEAD=no; gateway files differing live\.\.CLOUD after drain-back \(CLOUD-only runbook excluded\) 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-11"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r25/checks/rl11.AC2.sh; echo "exit=$?"</invocation><expect>(?s)no real send run\): fields=yes ssm=Success digest=yes.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-rl-11"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r25/checks/rl11.AC3.sh; echo "exit=$?"</invocation><expect>(?s)identity keys read: fields=yes ssm=Success digest=yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the release is live, the ledger is closed, CLOUD equals live, and the floor holds.
- `AC2`: the served gateway has the status tool and a send that returns within 60 s.
- `AC3`: the scoped identity's consent is narrowed and still works; the unscoped one is unchanged.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-rl-11.gateway-release-r25.proof_of_spec.json` and validate it with
`python .tools/proof-of-spec-check.py <instance>`. Flip the ONE `<status>` tag to `complete` only if all three PASS.
Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 24 (R3-T.18, item 3), after `OG-up-1`. Halves: CTO + COO + CVO.
- Part 2 rides this release because `af10f7d42b` is on CLOUD and rl11.AC1's drain-back arm reads CLOUD against live
  (the same footing as OG-rl-9 A1). The CTO's round-23 list names only part 1; the CTO's msg 30365 sets part 2's
  pre-GO read.
- The risk the rehearsal exists for: the scoped identity is the Teams concierge, the seat that sends the daily
  Bloomberg files. A scope the map omits would break that send only after its token is next refreshed.
- Pre-cut 02:5xZ: `rl11.AC1` FAIL (no ledger; 4 gateway files differ; floor yes/yes). `rl11.AC2` and `rl11.AC3` FAIL
  (the records are absent).

<status>pending</status>
<round>24</round>
<slot>~28</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
