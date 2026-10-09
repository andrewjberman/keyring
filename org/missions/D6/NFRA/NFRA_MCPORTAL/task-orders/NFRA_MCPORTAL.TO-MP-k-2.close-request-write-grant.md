# NFRA_MCPORTAL task order -- `MP-k-2` -- WORKSTREAM CP2 ROUND 1: the gateway role's one write, close requests only (FWD-17 hop)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-k-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-k-2</to_id>
<issued_to>0.7.0_AE_CloudOps~MP</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- an IAM grant; no cron, alarm, monitor or cadence.
comp-iam: RUN -- `comp-iam gaps` after the .tf change and before the apply; its output goes in the ASK and the ledger entry (necessary, not sufficient; AC2's simulation is the truth).
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2's four refused arms (the list, the result, the activity store, delete) are the adversary reads.
EGRESS CLASS, declared: none beyond AWS control-plane calls in Opal's own account.
</preflight>

## 1. THE CELL -- `MP-k-2` (workstream CP2 round 1, decomposition sections CP2.1 and CP2.6)

Work in a linked worktree you cut from `box/sitez` HEAD (CLAUDE.md 14b). Use the NO-CONE sparse pattern list that worked
for MP-x-3 (`.tools/`, `org/`, `lib/`, `infra/aws/terraform/opal-gateway/`). Commit there; the issuer drains it.

The FWD-17 page lets Andrew close an open call with his ruling. The gateway writes ONE request object, and the box's own
scan applies it through the box's writer (C11: the page never edits a list). For that, the gateway's instance role
`opal-gateway-role` (`infra/aws/terraform/opal-gateway/main.tf:151`, `aws_iam_role.gw`) needs exactly ONE new action:
`s3:PutObject` on `arn:aws:s3:::opal-313476888478-globgrph/fabric/open-calls/v1/box=*/requests/*`.

It already holds READ on `fabric/activity/v1/*` and `fabric/open-calls/v1/*`
(`mcportal_fabric_read.tf`, `gateway-mcportal-fabric-read-policy`, you applied it as MP-x-3). The `graph-read.tf` R3
paragraph records the carve-out. The bucket is SSE-S3 with no bucket policy, so the identity grant alone admits the write.

**The ruling** (`1.0.0_SA_CTO~O` msg 32404, on Q3): "NFRA_MCPORTAL builds ONLY the gateway side ... writing close-request
objects, on one PutObject grant scoped to `requests/` (never-widen, C10, this project's pair)". The pair is
`1.0.0_SA_CTO~Z` (CTO half; AMENDMENT 3: `~O` is retired) and `2.0.0_SA_COO~MP` (COO half). Both sign against YOUR ASK before you apply.

Build and apply, in order:
1. **`infra/aws/terraform/opal-gateway/mcportal_close_request_write.tf` (new).** It holds ONE `aws_iam_role_policy`,
   `gw_mcportal_close_request_write`.
   - **Name:** `"gateway-mcportal-close-request-write-policy"`, a LITERAL. This is the output of `lib/opal_naming.py
     name('gateway', None, 'mcportal-close-request-write', 'policy')`, read by the issuer at the cut. It has the same
     form as the sibling MCPORTAL policies (row Z-S21: an interpolated name is refused at apply).
   - **Role:** `aws_iam_role.gw.id`.
   - **Statement:** ONE, `s3:PutObject` on that one resource pattern, and nothing else.
   - **Header comment,** in the style of `mcportal_fabric_read.tf`:
     - what is granted and what is not (no list write, no result write, no delete, no other prefix);
     - the ruling quoted as "1.0.0_SA_CTO~O msg 32404";
     - that it is a separate, removable file;
     - the rollback;
     - the post-apply live check.
   - **`graph-read.tf`, comments only:** extend the R3 carve-out sentence to name this one write, citing msg 32404.
     Change no resource line.
   - **If the naming gate refuses the name,** do not override it. File a BLOCKING row with the refusal text and stop.
2. **Plan, and the ASK.**
   - Run `comp-iam gaps`.
   - Run the plan with `safe-apply`, targeted to `aws_iam_role_policy.gw_mcportal_close_request_write` only.
   - Anything other than `1 to add, 0 to change, 0 to destroy` STOPS the act with a BLOCKING row.
   - Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/NEVER_WIDEN_ASK_MP-k-2.md` with:
     - the blast radius: the one action and the one resource pattern;
     - what it may touch: request objects under any box's `requests/`;
     - what it may never touch: `open_calls.json`, `request_results/`, the activity store, any delete;
     - the plan counts and the policy document as planned;
     - the `comp-iam gaps` line;
     - the rollback per resource: a targeted destroy, or `aws iam delete-role-policy --role-name opal-gateway-role
       --policy-name gateway-mcportal-close-request-write-policy`;
     - the read-back you will run (AC1, AC2).
   - Commit the `.tf`, the `graph-read.tf` comment and the ASK. Then send ONE message, to BOTH `1.0.0_SA_CTO~Z` and
     `2.0.0_SA_COO~MP`, naming the ASK path and its commit, and asking each for its half.
3. **WAIT for both halves, at HEAD of `box/sitez`:**
   - `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_MP-k-2_<date>.md`;
   - `.../deliverables/2.0.0_SA_COO~MP/NEVER_WIDEN_HALF_COO_MP-k-2_<date>.md`.

   Each cites your ASK by path. A refused half STOPS the act; report it.
4. **NEVER-2 ledger, on THIS branch, in this order.**
   - Run `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-cp2-close-request-grant`. The legs are: apply,
     read-back.
   - Commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-cp2-close-request-grant.json`.
   - ACT with `safe-apply`, targeted to the same resource. Never run bare `terraform apply`.
   - Read back with AC1 and AC2.
   - Close every leg with its proof, and commit the close BEFORE you report the AC reads.
5. If `terraform init` needs a provider it cannot get from the local plugin cache, STOP with a BLOCKING row naming the
   provider and version.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No other Terraform resource moves and no other policy is edited. The
   gateway is not redeployed. No S3 object is read or written by you (the simulation is the exercise).
2. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report.
3. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its
   measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/mcportal_close_request_write.tf
infra/aws/terraform/opal-gateway/graph-read.tf
org/critical_paths/change_management/*nfra-mcportal-cp2-close-request-grant*
org/critical_paths/.open_deploys/nfra-mcportal-cp2-close-request-grant.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/terraform/opal-gateway/main.tf`, `mcportal_fabric_read.tf`, `mcportal_grant_writer.tf`,
`lib/opal_naming.py`, `.tools/open-calls-scan.py`, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-S<k>` (the next free seat-row k). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`. Rows are append-only.

## 4. PROOF OF SPEC (literal; run from your worktree root after the close commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-k-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/k2.AC1.sh; echo "exit=$?"</invocation><expect>actions=s3:PutObject resources=1 problems=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-k-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/k2.AC2.sh; echo "exit=$?"</invocation><expect>simulation arms matched 6 of 6 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-k-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/cp2/checks/k2.AC3.sh; echo "exit=$?"</invocation><expect>ask=yes; halves citing the ask=2 of 2; entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/NFRA_MCPORTAL.TO-MP-k-2.close-request-write-grant.proof_of_spec.json`.
Report once, to `2.0.0_SA_COO~MP`, with:
- the plan counts;
- the `comp-iam gaps` line;
- the three check outputs;
- the ledger entry path and its CLOSED state;
- every commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the CP2 issuance (decomposition v6) on the CTO's Q3 ruling (msg 32404). Policy name read from the builder
at the cut: `name('gateway', None, 'mcportal-close-request-write', 'policy')` -> `gateway-mcportal-close-request-write-policy`.
Checks dry-run at base 2851a9190d: AC1 FAIL (get-role-policy rc=254, NoSuchEntity), AC2 FAIL (5 of 6: the put-request arm reads
implicitDeny before the grant; the other five match, the control arm included), AC3 FAIL (no ASK, 0 halves, no entry). The
applier seat gets its GO by message (a seat, not a worker). Starts at the issuance; the apply waits on the pair.

**AMENDMENT 3 (issuer, 2026-10-09 ~09:3xZ, on the applier's msg 32611):** the CTO half is re-pointed from `1.0.0_SA_CTO~O`
to `1.0.0_SA_CTO~Z`. Andrew-direct ~07:4xZ retired `~O`: "we don't need CTO~O anymore, you just lead the fabric here"
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_074xZ_CTO_O_RETIRED_CTO_Z_LEADS_SITEZ_FABRIC.md`; every
never-widen half `~O` held on site Z passes to `~Z`). `~Z`'s own self-drive row in `org/ref/LIVE_ARMS.md` already names
NFRA_MCPORTAL. Ruling msg 32404 stands as `~O` wrote it. `k2.AC3.sh` now reads the `1.0.0_SA_CTO~Z/` half.

**DRAIN:** drained by 2.0.0_SA_COO~MP 2026-10-09 ~10:1xZ. The issuer re-ran all three checks from the applier's branch against live
IAM: AC1 `actions=s3:PutObject resources=1 problems=0`, AC2 6 of 6, AC3 2 of 2 halves with the ledger closed. Instance VALID.
The applier left the flip to the issuer, since the order file is outside its paths. Was: pending

<status>complete</status>
<round>1</round>
<workstream>CP2</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
