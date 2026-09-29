# NFRA_OPLGTW task order -- `OG-n-1` -- ROUND 2 (E8): the gateway takes an Elastic IP, so its egress address stops being an auto-assigned one (row S45, R-2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-n-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~14</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- one Terraform apply; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the applier's own ec2:AllocateAddress / AssociateAddress.
comp-adversary: DECLARED-NOT-APPLICABLE -- ruled (R-2: take the EIP; the out-of-repo allowlist planes are unmeasurable from here).
EGRESS CLASS, declared: NONE beyond Opal's own AWS.
</preflight>

## 1. THE CELL -- `OG-n-1` (decomposition addendum R2-E, item E8)

**The row (S45).** The gateway instance `i-07dccb1615503ac99` has no Elastic IP. `aws_instance.gw`
(`infra/aws/terraform/opal-gateway/main.tf:165-213`) sets `associate_public_ip_address = true` (`:174`), so its public
and egress address is the auto-assigned `54.197.78.28`. `describe-addresses` for the instance returned `[]` on
2026-09-28. An auto-assigned address changes on any stop/start, which silently breaks any out-of-repo allowlist of it.

**The ruling (R-2).** Take the EIP. Associating it moves the egress address ONCE, from `54.197.78.28` to the new EIP, and
never again. No stop/start is needed.

**Build and apply:**
1. **Declare** in a new file `infra/aws/terraform/opal-gateway/eip.tf`:
   ```
   resource "aws_eip" "gw" {
     domain = "vpc"
   }
   resource "aws_eip_association" "gw" {
     instance_id   = aws_instance.gw.id
     allocation_id = aws_eip.gw.id
   }
   ```
   - Write NO `Name` tag, no `name`, and make no `lib/opal_naming.py` builder call (ruling Q3 AMENDED @79430e9933):
     `aws_eip` has no name argument and its identity is AWS-issued; NAMING_SCHEMA v1.12 `not_covered` lists AWS-issued
     ids and tag values, and `aws_eip` / `aws_eip_association` are in neither tf map, so the naming gate never grades
     them. The provider's `default_tags` (`main.tf:33-40`) tag it.
   - Do NOT touch `aws_instance.gw`. Leave `associate_public_ip_address` as it is: changing it forces replacement.
2. **The root's precondition.** The root at the issuance base cannot plan on its own:
   - `mcportal_grant_writer.tf:53` hashes `infra/aws/lambda/layers/mcportal-grant-writer-deps/.build/mcportal-grant-writer-deps.zip`,
     which does not exist on a fresh tree (gitignored build output);
   - the root requires `mcportal_owner_key_claim` and `mcportal_owner_key` (`:142-156`), which have no default.
   Before anything else, confirm the zip exists at that path in your worktree (the issuer placed it there, copied from
   `C:/tmp/mp3-1`, the tree NFRA_MCPORTAL MP-a-2 built it in; 5,016,850 bytes; never build or download it). Then set the
   two variables in your shell, from worktree root, WITHOUT ever printing the key (it is the owner's private value; it
   goes into no file, log, row, report or commit):
   `export TF_VAR_mcportal_owner_key_claim=sub`
   `export TF_VAR_mcportal_owner_key="$(.tools/aws lambda get-function-configuration --function-name mcportal-grant-writer-lambda --region us-east-1 --query Environment.Variables.MCPORTAL_OWNER_KEY --output text | tr -d '\r')"`
   then `echo "key length=${#TF_VAR_mcportal_owner_key}"`, which must print 43.
   If the zip is absent or the length is not 43: STOP, a BLOCKING row. Never build the layer and never fetch it.
3. **Plan, TARGETED.** The root also declares the NFRA_MCPORTAL grant writer, which MP-a-2 applied on 2026-09-29, so an
   untargeted plan may still show drift on those resources. This cell applies none of them. Run
   `terraform plan -target=aws_eip.gw -target=aws_eip_association.gw`. It must read exactly "2 to add, 0 to change,
   0 to destroy". Anything else: STOP, a BLOCKING row. Also run ONE untargeted plan and record its resource list in the
   announce, so the halves see what this cell does NOT apply.
4. **NEVER-2 ledger**, slug `nfra-oplgtw-gateway-eip`. Open it (legs: apply, verify), and commit the entry AND its sentinel
   BEFORE the act.
5. **Apply:** `bash .tools/safe-apply.sh apply -target=aws_eip.gw -target=aws_eip_association.gw` in
   `infra/aws/terraform/opal-gateway`. Never a bare `terraform apply`.
6. **Verify:**
   - `describe-addresses` shows one address with an AssociationId on the instance;
   - the instance's `PublicIpAddress` equals it;
   - an unauthenticated `https://mcp.opalinvest.dev/mcp` still answers 401 with the `Bearer resource_metadata` challenge.
   Record the old and new addresses. Rollback: `terraform destroy -target` both resources. The auto-assigned address
   does NOT come back, which is the one irreversible fact. Close the ledger with its proof.

## 2. BOUNDS

1. The instance, its SG, the ALB, DNS and every NFRA_MCPORTAL resource are untouched. Only the two declared resources are
   applied.
2. You work in the worktree named in your identity line. Standing: no push, no vendor call, never `git stash`. REFUSE a
   criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/eip.tf
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-gateway-eip.json
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~14/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: `infra/aws/lambda/layers/mcportal-grant-writer-deps/.build/mcportal-grant-writer-deps.zip` (placed, never
built), and the rest of the root.

Rows go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md`, id
`NFRA_OPLGTW-Z-W14-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`.

## 4. PROOF OF SPEC (literal; run from your worktree root after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-n-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/eip.AC1.sh; echo "exit=$?"</invocation><expect>addresses associated with i-07dccb1615503ac99=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-n-1"><invocation>TF_VAR_mcportal_owner_key_claim=sub TF_VAR_mcportal_owner_key="$(.tools/aws lambda get-function-configuration --function-name mcportal-grant-writer-lambda --region us-east-1 --query Environment.Variables.MCPORTAL_OWNER_KEY --output text | tr -d '\r')" bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/eip.AC2.sh; echo "exit=$?"</invocation><expect>declared eip resources=2 of 2; targeted plan rc=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="OG-n-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/round2/checks/eip.AC3.sh; echo "exit=$?"</invocation><expect>sentinel at HEAD=no; listed OPEN/HELD=0; /mcp unauthenticated=401 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

- `AC1` -- one Elastic IP is associated with the instance, and it equals the instance's public IP.
- `AC2` -- the root declares both resources, and a plan TARGETED at them reports no changes (the applied world equals
  the declaration).
- `AC3` -- NEVER-2 closed, and the served `/mcp` path still answers 401 unauthenticated.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~14/NFRA_OPLGTW.TO-OG-n-1.gateway-eip.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance>`. Report once: the old and new address, the targeted
plan line, the untargeted plan's resource list, the ledger commits, AC1-AC3 literal output, and the rows.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Slot ~14, spawned ONLY at its gate: after NFRA_MCPORTAL MP-a-1 has built the grant-writer layer zip and the two
  owner-key values exist (the sitting's Part D gives the owner's claim value). `<MCPORTAL_OWNER_KEY_CLAIM>` and
  `<MCPORTAL_OWNER_KEY>` are filled by the issuer at that hand-off, from MP-a-1's configuration record.
- Q3 AMENDED @79430e9933 supersedes 5676f4a48a on the naming row: no `eip` kind row, no Name tag, no builder call.
- The CTO files S45's disarm row citing this cell's close (R-2).
- The declared class is WORLD: an AWS resource and an egress-address change.

**AMENDMENT A1 (issuer 2.0.0_SA_COO~O, 2026-09-29 ~19:3xZ, post-crash tick 1).** The spawn gate is met. MP-a-1 was
re-cut as NFRA_MCPORTAL MP-a-2, which completed with its ledger CLOSED (20260929T0412Z); the layer zip exists in
`C:/tmp/mp3-1` (5,016,850 B). The owner-key values were measured live on `mcportal-grant-writer-lambda` without printing
the key: claim `sub`, key length 43, matching `ANDREW_DIRECT_20260929_04xxZ_G-SUB_GIVEN.md`. Both placeholders are filled
by a read at run time, never by a typed value, under the CTO's privacy condition @384fd85543. Item 3's premise that the
writer is unapplied is corrected. No criterion changes its expectation.

<status>staged</status>
<status>pending -- GO by 2.0.0_SA_COO~O 2026-09-29 ~19:3xZ, amendment A1 (gate met: MP-a-2 CLOSED, zip in C:/tmp/mp3-1, owner key measured live). Was: staged.</status>
<round>3</round>
<slot>~14</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
