# NFRA_OPLGTW task order -- `OG-pr-1` -- the gateway read secrets and their one exact-ARN grant (C11, row Z-S24)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-pr-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~18</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- three secrets and one grant, created once; no cron, alarm, monitor or cadence.
comp-iam: RUN -- one new role policy on opal-gateway-role; the worker runs `comp-iam gaps` after the .tf edit (PHASE A step 3) and records it.
comp-adversary: DECLARED-NOT-APPLICABLE -- the shape is the CTO's (org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_20261001_OPAL_GATEWAY_RELEASE_TRAIN.md @cf5989190d R3).
EGRESS CLASS, declared: NONE beyond Opal's own AWS (Secrets Manager, IAM via safe-apply, read-only SSM).
</preflight>

## 1. THE CELL -- `OG-pr-1` (decomposition addendum R3-T.1)

`opal-gateway-role` gets `secretsmanager:GetSecretValue` on EXACTLY three secrets, which this order creates:
`gateway/transcripts/bearer`, `gateway/mail/bearer` and `gateway/principals/rosters`. Each name already reads
CONFORMANT under `lib/opal_naming.py` `grade(<name>, "SECRET")`. The gateway reads these on the host at deploy time,
as it does `MS_INGEST_BEARER` and `GRAPH_READ_BEARER`. No running service changes in this order.

The rosters' only copy today is the site-Z file `%LOCALAPPDATA%/opal/og-principals/part_d_20260930.json`. Its mapping
to the deploy variables `OG_MASTER_ADMIN_PRINCIPALS` (one `<tid>/<oid>` pair) and `OG_WRITE_CAPABLE_PRINCIPALS`
(comma-separated pairs) is in `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/PART_D_RECORD_20260930.md`.

### PHASE A (no AWS write)

1. **Terraform.** Write `infra/aws/terraform/opal-gateway/gateway-read-secrets.tf` on the
   `infra/aws/terraform/opal-gateway/graph-read.tf` pattern:
   - three metadata-only `data "aws_secretsmanager_secret"` blocks, one per name above;
   - ONE `aws_iam_role_policy` named `"gateway-read-secrets-policy"` (the builder's output,
     `lib/opal_naming.py` `name("gateway", None, "read-secrets", "policy")`, cited in a comment beside it; amendment
     A2) on `aws_iam_role.gw.id`, ONE statement,
     `Action = ["secretsmanager:GetSecretValue"]`, `Resource` = the list of exactly those three `.arn` references;
   - no `aws_secretsmanager_secret_version`;
   - a header comment on `graph-read.tf`'s pattern: why, mechanism, values created out of band, the post-apply verify.
2. **Secret script.** Write a python script in your deliverables that creates the three secrets with boto3
   (`us-east-1`; each description names this order). It builds each value in memory:
   - each bearer: 32 random bytes as hex (`secrets.token_hex(32)`);
   - the rosters: JSON `{"master_admin": "<tid>/<oid>", "write_capable": "<tid>/<oid>,..."}` from the Part D file,
     per the Part D record.

   It prints only each ARN and the roster pair counts. It refuses if a secret of that name already exists. Run
   nothing against AWS yet.
3. `comp-iam gaps`, then `safe-apply plan` on `infra/aws/terraform/opal-gateway`. The data sources need the secrets,
   so a plan refusal on the missing secrets is expected here: record it.
4. Write `ANNOUNCE_OG-pr-1.md` in your deliverables:
   - the files, the three names with their `grade()` verdicts, and the roster pair counts (never values);
   - the plan reading;
   - the rollback per key: remove the role policy with Terraform; delete each secret with a 7-day recovery window.

   Commit it and report. STOP for the issuer's GO.

### PHASE B (on the issuer's GO)

5. Open the NEVER-2 ledger, slug `nfra-oplgtw-gateway-read-secrets`, with `python .tools/deploy_ledger.py open ...`
   (legs: secrets, grant, simulate, host-read). Commit the entry AND its sentinel BEFORE the act.
6. Run the secret script. Then run a TARGETED `safe-apply` of `aws_iam_role_policy.<yours>`, fed as `OG-n-1` was
   (amendment A1, row Z-W18-S1):
   - `TF_VAR_mcportal_owner_key_claim=sub` and `TF_VAR_mcportal_owner_key` read from the LIVE Lambda
     (`aws lambda get-function-configuration --function-name mcportal-grant-writer-lambda --region us-east-1 --query
     Environment.Variables.MCPORTAL_OWNER_KEY --output text`) into the variable, never printed or written to a file;
   - the grant writer's `.build/staged` made by `python infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/build_package.py`
     in your worktree, and `infra/aws/lambda/layers/mcportal-grant-writer-deps/.build/mcportal-grant-writer-deps.zip`
     copied from the main tree `C:/Users/Opal Bloomberg/Desktop/ajb_workspace/` (untracked build output; neither is
     targeted, so neither is applied). The plan must read
   exactly 1 to add, 0 to change, 0 to destroy. This is Terraform act #2 of the gateway train: if another
   `safe-apply` on `infra/aws/terraform/opal-gateway` is in flight, wait for it and record that.
7. Run AC2 and AC3. Close every leg with its proof and commit.

## 2. BOUNDS

1. Never print, commit or write to a repo file a secret value or a principal value.
2. No other IAM change; every other `.tf` file is untouched. No gateway release, restart or `.env` change.
   `deploy-to-ec2.sh` is not edited here; `OG-rl-1` does that.
3. Work in the worktree named in your identity line. Never push, merge, rebase, stash, `checkout --` or `clean`.
   REFUSE a criterion you cannot meet as written.
4. Commit with `.tools/safe-commit.sh` under your serial; every `.py` passes `.tools/commit-gate.sh`.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/gateway-read-secrets.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-read-secrets.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~18/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows: id `NFRA_OPLGTW-Z-W18-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-pr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/pr.AC1.sh; echo "exit=$?"</invocation><expect>(?s)secret data sources: 3 .*actions named: \['secretsmanager:GetSecretValue'\].*resource statements 1;.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-pr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/pr.AC2.sh; echo "exit=$?"</invocation><expect>(?s)granted ARNs 3 \['allowed', 'allowed', 'allowed'\]; sibling gateway/\* ARNs 1 \['implicitDeny'\].*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-pr-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/trnspt/checks/pr.AC3.sh; echo "exit=$?"</invocation><expect>(?s)host read status=Success; ROSTERS master 1 write [1-9]\d* all-pairs True.*sentinel at HEAD=no.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: one statement, one action, exactly the three secrets, metadata-only.
- `AC2`: the CTO's R3 acceptance: `allowed` on the three, `implicitDeny` on a sibling `gateway/*` secret.
- `AC3`: the host reads the roster secret under its own role, shape only; NEVER-2 is closed.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~18/NFRA_OPLGTW.TO-OG-pr-1.principal-rosters-secret.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once per phase: files, pair counts (never
values), the plan and apply readings, the literal AC output, commits and rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Its own single-cell issuance, round label 9 (round 8's issuance is closed to new files; one issuance per round label),
  cut from addendum R3-T.1 on CTO ruling R3 (C11) and tick-1 ruling (b) for
  row Z-S24. Slot `~18`, new. Edge `OG-pr-1` -> `OG-rl-1` PHASE B. Until `OG-rl-1` serves, the issuer hands the
  rosters off-repo to `2.0.0_SA_COO~MI` (MX-r-7, msg 27497) and `2.0.0_SA_COO~MS` (MS-d-2), per C2.
- Blast radius for the GO: three new secrets and one new role policy (one action, three ARNs); no running service
  changes.
- `<risk>` WORLD: an IAM grant and secrets.

<status>pending</status>
<status>complete</status>
<round>9</round>
<slot>~18</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

## AMENDMENT A1 (issuer `2.0.0_SA_COO~O`, 2026-10-01 ~05:2xZ; rules row Z-W18-S1)

Graded by: no gate limb (a modification; GATE (viii) reads `<placeholders>NONE</placeholders>`). Step 6 names how the
targeted apply is fed: the owner-key variables from the live Lambda (the `OG-n-1` precedent in this project,
`deliverables/0.9.0_WK_NFRA_OPLGTW~14/NFRA_OPLGTW.TO-OG-n-1.gateway-eip.proof_of_spec.json` AC2), the grant writer's
staged build made locally, and the deps-layer zip copied from the main tree. None of those resources is targeted, and
the plan's 1-to-add / 0 / 0 reading is the guard against any spill. PHASE B's GO waits on Terraform act #1 of the
gateway train (MX-r-7, CTO ruling C4: targeted, never concurrent, in train order).

## AMENDMENT A2 (issuer `2.0.0_SA_COO~O`, 2026-10-01 ~07:5xZ; rules BLOCKING row Z-W18-S2)

Graded by: no gate limb (a modification; GATE (viii) reads `<placeholders>NONE</placeholders>`). PHASE B's targeted
`safe-apply` was refused by the naming plan limb (LGIC_ENFORCE DEC-6): `opal-gateway-gateway-read-secrets` grades
OUT-OF-PATTERN as an IAM_POLICY. The order typed that name, which is the issuer's defect (CLAUDE.md rule 30: every
resource name is builder output). The policy is now `gateway-read-secrets-policy` = `name("gateway", None,
"read-secrets", "policy")`, CONFORMANT. The worker stopped, rolled the three secrets back to a 7-day recovery window and
closed the ledger ROLLED BACK (@cf4426a167, drained @8e87440071) -- the correct act. RESUME of PHASE B:
- re-open the ledger with the same slug `nfra-oplgtw-gateway-read-secrets` (a new entry; commit entry and sentinel
  before the act);
- `aws secretsmanager restore-secret --secret-id <name>` for the three names (values preserved; the creation script is
  NOT re-run; its refusal on an existing name stands);
- edit the one name line in `gateway-read-secrets.tf`; then the targeted `safe-apply` per step 6 (1 / 0 / 0);
- step 7 as written.
