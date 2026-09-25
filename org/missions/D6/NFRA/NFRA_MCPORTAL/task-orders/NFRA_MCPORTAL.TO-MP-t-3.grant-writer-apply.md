# NFRA_MCPORTAL task order -- `MP-t-3` -- HOP 3 (live): the grant writer applied, and its refusals shown live

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-t-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~3</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot apply; no cron, alarm, monitor or cadence.
comp-iam: RUN -- AC2 simulates the gateway role on the APPLIED plane: invoke on the one function ALLOWED, AssumeRole on the operator role DENIED. Blindness: this lens sees the two roles and the one function, not the rest of the account.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: AWS WRITE on Opal's own plane through safe-apply (one function, one role, one invoke grant) and two lambda invocations that must be refused. No vendor.
</preflight>

## 1. THE CELL -- `MP-t-3` (round 1, decomposition s.2/s.3)

`MP-t-2` (your previous order) built the grant writer: the `mcportal` row in `infra/logic/registry/systems.json`, the
source under `infra/aws/lambda/mcportal/<builder name>/`, and
`infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf`, with Andrew's owner Entra object id as a variable with no
default. It is merged at your worktree's HEAD. Apply it:
1. **Andrew's Entra object id.** Find it in an EXISTING record, never by asking the gateway to authenticate anyone. For
   example: a principal record the gateway's audit or policy store already holds for `andrew@opalinvest.com`, or a
   committed operator artifact naming it. Cite where it came from. **If no existing record names it, STOP: file a
   BLOCKING row** (`G-OWNER-OID`, owner Andrew) and do not apply. Never guess or derive it from an email.
2. **Ledger first (C10 / NEVER-2).**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-r1-grant-writer`, naming the blast radius (one
     function, its execution role, one `lambda:InvokeFunction` grant on the gateway role) and the rollback (`safe-apply`
     of the prior Terraform state = destroy the three);
   - commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-r1-grant-writer.json`;
   - then apply with `safe-apply` (never bare `terraform apply`; read `.tools/safe-apply*` for its interface). The plan
     must show ONLY the new resources, with 0 to change and 0 to destroy on existing ones. Anything else: STOP, a
     BLOCKING row;
   - then close each leg with its proof, and commit the close BEFORE the AC reads.
3. Packaging the function's code follows the map's `tf_resource` / build convention in
   `infra/aws/lambda/ci/lambda-source-map.json`. A zero-diff apply with no artifact built is a failed leg, not a pass.

## 2. BOUNDS

1. The operator role, its trust policy, the `LeadingKeys` guard and `ops/schwab_entitlement_admin.py` are untouched.
2. No grant is written: the only invocations are AC3's two, which must be refused.
3. If a leg fails mid-act, roll back with the named rollback, close the entry as rolled back, and report. Never leave
   it half-landed.
4. Standing: no push, no install, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal
   with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcportal-r1-grant-writer.json
infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf
infra/aws/lambda/mcportal/
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

(The `.tf`, source and source-map entries are granted so the apply's tooling can record a build hash or a variable
file. Change no logic in them; a needed logic change is a BLOCKING row.)

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_MCPORTAL-Z-W3-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-t-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t3.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-t-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t3.AC2.sh; echo "exit=$?"</invocation><expect>state=Active; gateway invoke=allowed; gateway assume operator role=implicitDeny or explicitDeny -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-t-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t3.AC3.sh; echo "exit=$?"</invocation><expect>no header -> REFUSED NO-OWNER-HEADER; forged header -> REFUSED HEADER-UNVERIFIED -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~3/NFRA_MCPORTAL.TO-MP-t-3.grant-writer-apply.proof_of_spec.json`. Report once: where Andrew's oid came from, the plan summary, the ledger entry path, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** WORLD: the CTO's exercised read. G-OWNER-OID routes to Andrew only if AC-free step 1 files it.

<status>superseded -- CTO ruling R-1 (D-2, @aed83d11fe): the grant writer cannot import from its own zip; re-cut in round 2 behind the staged-build cell</status>
<round>1</round>
<slot>~3</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
