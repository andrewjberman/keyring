# NFRA_MCPORTAL task order -- `MP-a-2` -- ROUND 3, E2: apply the grant writer on the `sub` branch (re-cut of MP-a-1, plus R-9)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-a-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~1</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot apply; no cron, alarm, monitor or cadence.
comp-iam: RUN by this cell after the apply (AC2's live invoke exercises the writer's role and its table grant).
comp-adversary: DECLARED-NOT-APPLICABLE -- the writer's refusal arms are the adversary read (A1n, MP-c-1).
EGRESS CLASS, declared: ONE pinned-wheel fetch from PyPI to build the writer's layer, on Andrew's word (G-PYPI: "Go
ahead.", org/tier1_exec/2.0.0_SA_COO~O/ANDREW_DIRECT_20260928_152xZ_NFRA_GATES_ANSWERED.md row 6); nothing else leaves
Opal's AWS.
</preflight>

## 1. THE CELL -- `MP-a-2` (round 3, decomposition section R3.2)

The grant writer is built and NOT applied: a staged package (`infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/`,
`build_package.py`), both owner-key branches selected by configuration, and its own record table, all in
`infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf`. The gateway is live and already sets the writer's function
and table names in its env.

The measurement is TAKEN (issuer's E1 @c8b42c8913): the gateway's one `OWNER-HEADER-CLAIMS` line reads
`keys=email,exp,family_name,given_name,iss,name,picture,sub`. So the branch is **`sub`**:
`MCPORTAL_OWNER_KEY_CLAIM=sub`, and `MCPORTAL_OWNER_KEY` is Andrew's own `sub`. The issuer gives you that value in the
spawn message, OUTSIDE this file. Pass it straight to the Terraform variable. Never echo, log, commit or write it into
any file, including a plan file, a ledger entry or your report; refer to it only as "the owner key". The PRD's C4 says
exactly this at v0.3 @963fff9f5a (the writer matches `sub` and refuses a header past its own `exp`), and the
ratified-text half is re-signed @24ef97a3b7.

In order:
1. **Re-read the line** (it may have been re-printed): over SSM on `i-07dccb1615503ac99`, run `journalctl -u
   opal-gateway --no-pager -o cat | grep OWNER-HEADER-CLAIMS | tail -1`. If `oid` is now among the keys, or `sub` is
   absent: STOP with a BLOCKING row. AC3 is the recorded form of this read.
2. **Build the layer** from `infra/aws/lambda/layers/mcportal-grant-writer-deps/requirements.txt` exactly as its header
   and the `irpt-common` precedent say: `pip download --platform manylinux2014_x86_64 --implementation cp
   --python-version 312 --only-binary=:all:`, then unzip into `python/`, then zip. This is the ONE egress you are granted.
3. **Rollback, named before the act:** every resource is new, so the rollback is a targeted destroy of exactly this
   file's resources. Write the command into the ledger entry.
4. **NEVER-2 ledger, on THIS branch, in this order:**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-r3-writer-apply`. Legs: layer build, staged
     package build, apply, live refusal run. Record the branch picked (`sub`), the line's keys, and the rollback;
   - commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-r3-writer-apply.json`;
   - ACT with `safe-apply` (never bare `terraform apply`), targeting ONLY this file's resources, with the owner-key
     claim, the owner key and the changes table supplied as variables;
   - invoke the function once with no owner header (AC2's refusal);
   - close every leg with its proof, and commit the close BEFORE the AC reads.
5. **R-9, the source-map note (row Z-W1-S5):** `infra/aws/lambda/ci/lambda-source-map.json` names the retired
   `MCPORTAL_OWNER_OID` once, in the grant writer's note. Rewrite that note to name `MCPORTAL_OWNER_KEY_CLAIM` (`oid` or
   `sub`) and `MCPORTAL_OWNER_KEY`, and to say the writer refuses a header past its own `exp`. The note must say APPLIED
   only after the apply's leg closes. Touch no other entry in that file.

## 2. BOUNDS

1. No other Terraform resource moves. Print the plan's add, change and destroy counts; anything outside this file's
   resources STOPS the act.
2. The gateway is not redeployed. If a leg fails mid-act: roll back with the named command, close the entry as rolled
   back, and report.
3. Standing: no push and no vendor call beyond step 2's fetch. REFUSE a criterion you cannot meet as written and report
   the refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.
4. The writer's source at your base already carries MP-b-3's change: a WRITTEN item's `who` field holds the claim NAME
   and the email, never the owner-key value. You apply that source as it is, and you do not change the writer's code.
   Your only live write is a REFUSED item (`who`=UNVERIFIED).

## 3. SURFACES

<paths>
infra/aws/lambda/layers/mcportal-grant-writer-deps/
infra/aws/lambda/ci/lambda-source-map.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcportal-r3-writer-apply.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/terraform/opal-gateway/`, `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W1-S<k>` (the next free k for W1; S1-S5 are taken).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the ledger close is committed)

AC4 is a fourth criterion because R-9's note is a separate record file that none of AC1-AC3 reads (analysis R-9).

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-a-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/a2.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-a-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/a2.AC2.sh; echo "exit=$?"</invocation><expect>no header -> REFUSED NO-OWNER-HEADER; table items with reason NO-OWNER-HEADER>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-a-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/a2.AC3.sh; echo "exit=$?"</invocation><expect>ssm status=Success; line=yes values_in_line=no want_claim=sub have_claim=sub value_ok=yes verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="MP-a-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round3/checks/a2.AC4.sh; echo "exit=$?"</invocation><expect>MCPORTAL_OWNER_OID=0 and MCPORTAL_OWNER_KEY_CLAIM>=1 and MCPORTAL_OWNER_KEY>=1 at HEAD -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/NFRA_MCPORTAL.TO-MP-a-2.writer-apply-sub.proof_of_spec.json`.
Report once, with:
- the claim keys read and the branch picked;
- the layer's versions;
- the plan counts;
- the ledger path;
- the commit hashes;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E2 of ROUND_ANALYSIS.round2.md @33ca99c40e, plus R-9. Checks dry-run at base 2026-09-28 ~20:4xZ: AC1,
AC2, AC3 and AC4 FAIL as expected. AC3 read `want_claim=sub have_claim=UNSET`.

SPAWN ONLY when ALL hold (this is a CONTINUATION of slot `~1` after MP-b-3 drains):
- MP-b-3 has drained (its merge is in the base this order's apply packages);
- G-HDR is done (E1 @c8b42c8913);
- G-C4 is signed (@24ef97a3b7);
- G-PYPI is given (row 6 of the 09-28 record);
- **G-SUB:** Andrew has given the issuer his `whoami` `sub`, off-repo. It is passed in the spawn message only.

Slot `~1` continues to MP-c-1 after this order drains.

<status>complete</status>
<round>3</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
