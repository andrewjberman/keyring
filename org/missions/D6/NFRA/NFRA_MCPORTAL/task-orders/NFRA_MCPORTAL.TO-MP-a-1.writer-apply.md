# NFRA_MCPORTAL task order -- `MP-a-1` -- ROUND 2, E3: apply the grant writer with the owner key the header proves

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-a-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~1</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot apply; no cron, alarm, monitor or cadence.
comp-iam: RUN by this cell after the apply (AC2's live invoke plus the two grants' shape at MP-b-2's AC3).
comp-adversary: DECLARED-NOT-APPLICABLE -- the writer's refusal arms are the adversary read (A1n).
EGRESS CLASS, declared: ONE pinned-wheel fetch from PyPI to build the writer's layer, on Andrew's word (G-PYPI, recorded
in the issuer's spawn note); nothing else leaves Opal's AWS.
</preflight>

## 1. THE CELL -- `MP-a-1` (round 2, decomposition section R2.1)

Your branch carries the grant writer as a staged package (MP-b-1), with both owner-key branches built and its own record
table in Terraform (MP-b-2), in `infra/aws/terraform/opal-gateway/mcportal_grant_writer.tf`. Nothing is applied yet. The
gateway is live with the claim capture (MP-d-1): Andrew has opened the dashboard once (G-HDR), so the gateway's journal
holds an `OWNER-HEADER-CLAIMS keys=... oid=... sub=... iat=... exp=...` line.

In order:
1. **Read the measurement** (AMENDED to the CTO's privacy condition @384fd85543: the line carries claim KEYS only, and
   the owner-key VALUE is written ONLY into this function's configuration, never into a log, an audit record or a
   committed file). Over SSM on `i-07dccb1615503ac99`, read the latest `OWNER-HEADER-CLAIMS keys=...` line from
   `journalctl -u opal-gateway`. Then pick the branch:
   - `oid` among the keys: `MCPORTAL_OWNER_KEY_CLAIM=oid`, and the key is the measured oid ruling R-1 accepted,
     `2e21f8e5-55ca-45c1-91b9-a4607bf28d4f`;
   - no `oid`: `sub`. The value is the one Andrew reads from his own `/api/admin/whoami` response and supplies in the
     issuer's spawn note, and you pass it straight to the variable. Never echo, log or commit it.
   If `oid` or `iat` is absent from the keys, the PRD's C4 must already say so: `org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md`
   at HEAD names the subject identifier (or the header's own lifetime), and `python .tools/prd-signoff.py status NFRA_MCPORTAL`
   shows the ratified-text half SIGNED at the current bytes. If not: STOP, a BLOCKING row. If the line is missing, or
   neither `oid` nor `sub` is present: STOP, a BLOCKING row.
2. **Build the layer** from `infra/aws/lambda/layers/mcportal-grant-writer-deps/requirements.txt` exactly as its header
   and the `irpt-common` precedent say (`pip download --platform manylinux2014_x86_64 --implementation cp --python-version
   312 --only-binary=:all:`, then unzip into `python/`, then zip). This is the ONE egress this order is granted.
3. **Rollback, named before the act:** the resources are all new, so the rollback is a targeted destroy of exactly them.
   Name the command.
4. **NEVER-2 ledger, on THIS branch, in this order:**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-r2-writer-apply`. Legs: layer build, staged
     package build, apply, live refusal run. Plus the branch picked and its line, and the rollback;
   - commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-r2-writer-apply.json`;
   - ACT with `safe-apply` (never bare `terraform apply`), targeting ONLY this file's resources, with the owner-key
     claim, the key, and the changes table supplied as variables;
   - invoke the function once with no owner header (AC2's refusal);
   - close every leg with its proof, and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. No other Terraform resource moves: the plan's add/change/destroy counts are printed, and anything outside this
   file's resources STOPs the act.
2. The gateway is not redeployed here (MP-d-1 already set its env). If a leg fails mid-act: roll back with the named
   command, close the entry as rolled back, and report.
3. Standing: no push, no vendor call beyond step 2's fetch. REFUSE a criterion you cannot meet as written, and report
   the refusal with its measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/lambda/layers/mcportal-grant-writer-deps/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcportal-r2-writer-apply.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read (never write): `infra/aws/terraform/opal-gateway/`, `infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md`.

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id
`NFRA_MCPORTAL-Z-W1-S<k>` (next free k for W1).

## 4. PROOF OF SPEC (literal; run from your worktree root, after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-a-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/a1.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-a-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/a1.AC2.sh; echo "exit=$?"</invocation><expect>no header -> REFUSED NO-OWNER-HEADER; table items with reason NO-OWNER-HEADER>=1 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-a-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round2/checks/a1.AC3.sh; echo "exit=$?"</invocation><expect>ssm status=Success; line=yes values_in_line=no; have_claim equals want_claim; value_ok=yes; verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~1/NFRA_MCPORTAL.TO-MP-a-1.writer-apply.proof_of_spec.json`.
Report once:
- the claim line read and the branch picked;
- the layer's versions;
- the plan counts;
- the ledger path;
- the commit hashes;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** E3.

SPAWN ONLY when ALL hold:
- MP-b-2 has drained;
- MP-d-1 has drained with AC3 PASS;
- G-HDR is done (Andrew opened the dashboard; the journal line exists);
- G-PYPI is given (Andrew's word, quoted in the spawn note);
- on an absent-claim branch, G-C4 is signed.

The slot continues here after MP-b-2.

<status>superseded -- CLOSED for round 2 by 2.0.0_SA_COO~O, 2026-09-28T13:0xZ, on Andrew's direction to close out the rounds so the CVO can slug. HELD, never spawned: its spawn precondition G-HDR (Andrew opens the dashboard; the journal line exists) has not landed. Holding it open would deadlock round 2's L10 on an Andrew act. NOTHING IS RE-GRADED BY THIS CLOSE. The cell RE-CUTS in round 3, unchanged, once G-HDR lands. Was: pending.</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>

