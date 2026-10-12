# NFRA_OPLGTW task order -- `OG-ap-13` -- APPLY: remove `gateway/teams/bearer` from the dell group's `ReadPlatformKeys` grant (31 -> 30 ARNs), at the census source

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ap-13</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ap-13</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- an IAM managed-policy document change; no scheduled producer reads it, and the two dell agent users read the bearer 0 times in 90 days (OG-tb-1 TB1_READ.json).
comp-iam: RUN-BY-ISSUER at the cut (2026-10-12 ~13:3xZ) -- arn:aws:iam::313476888478:policy/cloudops-dell-agent-platform-secrets-policy default v4, Sid ReadPlatformKeys 31 ARNs including gateway/teams/bearer-93ZHiU; simulate cloudops-dell1-agent-user GetSecretValue on the bearer reads allowed, on a kept ARN allowed. Attached to cloudops-dell-agents-group only (TB1_READ.json).
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the signed pair over org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~59/NEVER_WIDEN_ASK_OG-tb-1.md: COO org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_HALF_COO_OG-tb-1_20261012.md @f9cb4c5dca, CTO @fa2892a777, its cross-fabric condition met by the laptop CTO's YES (org/tier1_exec/1.0.0_SA_CTO/deliverables/SELF_DRIVE_CLUSTER_TICK1_RULINGS_20261012.md section A row 1, sitez-ffaf).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-ap-13` (decomposition addendum R3-T.47)

Narrow, never widen. Managed policy `cloudops-dell-agent-platform-secrets-policy`, Sid `ReadPlatformKeys`, loses ONE
resource: `arn:aws:secretsmanager:us-east-1:313476888478:secret:gateway/teams/bearer-93ZHiU`. Its 31 ARNs become 30;
nothing else changes. The document is BUILT by `module.routes_policy` in `infra/aws/terraform/nfra-ctlpln-identity/`
from the secrets census `tests/vendor_secrets_census.json` (`decisions[name].granted`). The census is produced by
`tests/derive_vendor_secrets.py`. So the change lands at the SOURCE, or the next apply restores it. READ the ask and
both halves; they BIND.

1. **Ledger** `nfra-oplgtw-tb1-bearer-narrow`: entry AND sentinel committed first. The entry names the one policy and
   the rollback.
2. **Source.** In `tests/derive_vendor_secrets.py`, re-class `gateway/teams/bearer` from PLATFORM-KEY to OTHER (the one
   class that is not granted) with its own RULINGS entry. The entry cites the record above (sitez-ffaf, ruled YES) and
   OG-tb-1. Keep the other five gateway tokens in the loop at line ~213 unchanged.
   - Regenerate `tests/vendor_secrets_census.json` by that script's own documented run; never hand-edit the JSON. The
     diff shows `gateway/teams/bearer` with class OTHER and `granted: false`, and no other decision moves.
   - Update any count the root's tests or preconditions pin, such as the OTHER and PLATFORM-KEY totals and the comment
     at line 7, so the root's tests pass.
   - Run `.tools/commit-gate.sh` on the `.py`.
3. **Apply.**
   - Run Terraform from a worktree of box/sitez HEAD, never a release branch root.
   - Plan the root; the TARGETED plan, read at rc=0, shows `aws_iam_policy.dell_agent_platform_secrets` in place,
     `0 to add, 1 to change, 0 to destroy`. The `description` (ForceNew; see the comment near iam.tf line 283) must NOT
     change, and the document diff is the one ARN. Any other row is a STOP.
   - Apply with `bash .tools/safe-apply.sh -target=aws_iam_policy.dell_agent_platform_secrets`. Never edit the policy by
     console or CLI.
4. **Read-back** (COO condition B):
   - The new default version's `ReadPlatformKeys` lists 30 ARNs, without the bearer.
   - `simulate-principal-policy` for `cloudops-dell1-agent-user` on the bearer ARN reads `implicitDeny`, and on one kept
     ARN reads `allowed`.

   Write `W/ap13_readback.json` = `{"default_version", "arns", "bearer_listed", "sim_bearer", "sim_kept",
   "prior_version": "v4"}`.
5. Close the ledger, commit, run AC1 and AC2, and report once to `2.0.0_SA_COO~O`.
6. **Rollback**, if any read-back disagrees:
   - `aws iam set-default-policy-version --policy-arn arn:aws:iam::313476888478:policy/cloudops-dell-agent-platform-secrets-policy --version-id v4`;
   - revert the census source in one commit;
   - file an ARMED row naming `2.0.0_SA_COO~O`.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`.

## 2. BOUNDS

- In scope: the one policy and one ARN, plus the census source that builds it. Do not touch any other secret's class,
  the group's other policies, the gateway, the COMM_ASSIST role, the admin user, or the secret itself.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; bare `terraform`; a console or CLI policy edit (except the
  rollback's `set-default-policy-version`); override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/terraform/nfra-ctlpln-identity/tests/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-tb1-bearer-narrow.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after the ledger close)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ap-13"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r35/checks/ap13.AC1.sh; echo "exit=$?"</invocation><expect>(?s)entries at HEAD [1-9]\d*; status CLOSED=yes; sentinel at HEAD=no.*ReadPlatformKeys ARNs 30 \(want 30\); bearer listed: no.*simulate dell1 on bearer: implicitDeny \(want implicitDeny\); on kept ARN: allowed \(want allowed\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ap-13"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r35/checks/ap13.AC2.sh; echo "exit=$?"</invocation><expect>(?s)bearer granted=False; PLATFORM-KEY granted \(kms default\) 30 \(want 30\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the live grant is narrowed, with a kept ARN as the control. `AC2`: the source agrees, so the next apply keeps it.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ap-13.teams-bearer-narrow-apply.proof_of_spec.json`. Validate it after
your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, and flip
the ONE `<status>` tag to `complete` only if both PASS.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 35, workstream APPLY-R35-T. Un-held by `1.0.0_SA_CTO~Z` msg 33492 (the laptop CTO's YES under Andrew's 12:5xZ
  self-drive arming). Per that record, the issuer sends the receipt to laptop `2.0.0_SA_COO~C` and laptop
  `1.0.0_SA_CTO`.
- Pre-cut (2026-10-12 ~13:3xZ), both FAIL as expected:
  - ap13.AC1: no ledger; v4 31 ARNs, bearer listed; sim bearer allowed, kept allowed (the control discriminates).
  - ap13.AC2: bearer granted=True; PLATFORM-KEY 31.

<status>pending</status>
<round>35</round>
<workstream>APPLY-R35-T</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
