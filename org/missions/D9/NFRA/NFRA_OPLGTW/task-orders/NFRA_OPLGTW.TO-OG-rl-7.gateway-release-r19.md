# NFRA_OPLGTW task order -- `OG-rl-7` -- the r19 release: the CLOUD-only items onto live 37be3485db, then CLOUD = live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-rl-7</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~15</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the release is the CTO's round-18 analysis item 2 (R16).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, audit-bucket reads) and the public gateway URL.
</preflight>

## 1. THE CELL -- `OG-rl-7` (decomposition addendum R3-T.12, item 2; CTO R16, R21)

Handed only after `OG-ts-2` is drained to CLOUD. FOLLOW `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md`
IN FULL: Phase A steps 1-8 (including step 7, the pre-GO check exercise, and step 7a, R21's route inventory), Phase B
steps 9-12, and Phase D step 13 (DRAIN-BACK).

- **Live:** `37be3485db9a00522c55a260666f708336c918f3`.
- **Ledger:** `nfra-oplgtw-gateway-release-r19`.
- **The release set:** every CLOUD-only item in `deliverables/0.9.0_WK_NFRA_OPLGTW~22/LINEAGE_R18.json` (18 items, all
  `SHIPS_IN_RELEASE`), plus OG-ts-2's test fixes, so that after the drain-back CLOUD equals live for the gateway tree.

**The behaviour changes; the ANNOUNCE names each with both branches:**
- `app/admin_refusals.py`, NFRA_MCPMSP MS-sg-1: sender fields come from entry args only.
- `app/integrations/schwab/envelope.py`, OG-o-4: the narrow page.
- `app/server.py`, NFRA_OPALAI OA-e-10 (@8ed37b3266): `/login` narrowed to the configured server identities, failing
  closed.

**OA-e-10's admit lists (R16): the BLOCKING precondition, read in Phase A.**
- From the gateway audit lake (`opal-mcp-audit`), read every identity that used `/login` over the 30 days before the
  read.
- Name the set `/login` admits BEFORE (live) and AFTER (the configured server identities).
- ANY identity in the 30-day window that falls outside the AFTER set BLOCKS the release. File a BLOCKING row naming it
  (redacted to its label or principal id) and STOP before GO. It is never discovered as an outage.

Write `RL7_LOGIN.json` (AFTER keys filled in Phase B):
- `{served_release, window_days, admit_before:[...], admit_after:[...], outsiders_in_window:[...]}`;
- `after: {configured: "ADMITTED", unconfigured: "REFUSED <code>"}`, from a synthetic, host-local exercise;
- `grants_written: 0`.

The runbook, walkthrough protocol and tests ride along. They are not service behaviour.

## 2. BOUNDS

- No grant is created or changed. Never source `/opt/opal-gateway/.env`.
- Terraform, IAM, the ALB and the template are untouched (the template already equals live after OG-ln-1).
  `safe-ec2-deploy.sh` is READ only.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; call a vendor. The one sanctioned override is R13 (a), on
  the release branch only.
- PHASE B only on the issuer's GO, with CTO + COO + CVO halves SIGNED on the release sha.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-release-r19.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~22/LINEAGE_R18.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W15-S<k>` (next unused), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the drain-back and ledger close are committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-rl-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r19/checks/rl7.AC1.sh; echo "exit=$?"</invocation><expect>(?s)host shipped app files equal the release bytes: 3 of 3.*audit window days >= 30: True.*outsiders in window 0: True.*configured identity admitted after: True.*unconfigured identity refused after: True.*grants_written 0: True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-rl-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r19/checks/rl7.AC2.sh; echo "exit=$?"</invocation><expect>(?s)sentinel at HEAD=no; deployed=\w+ descends from 37be3485db=yes; gateway files differing live\.\.CLOUD after drain-back 0.*floor: rl4.AC1 yes; ht.AC2 yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~15/NFRA_OPLGTW.TO-OG-rl-7.gateway-release-r19.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 19 (R3-T.12, item 2), after `OG-ts-2`. Halves: CTO + COO + CVO. Served output moves: `/login` narrows, MSP
  sender fields narrow, and the Schwab envelope page narrows.
- AC2 grades the drain-back: CLOUD equals live afterwards.
- Pre-cut: see the issuance commit.

<status>pending</status>
<round>19</round>
<slot>~15</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
