# NFRA_MCPORTAL task order -- `MP-t-6` -- THE JOIN: the gateway deploy that ships the gate, the handlers and the bundle

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-t-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~4</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy; no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- code moves on the existing host and role; no IAM surface is written.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round.
EGRESS CLASS, declared: AWS WRITE on Opal's own plane -- one S3 artifact upload and one SSM pull/restart on i-07dccb1615503ac99 via the existing deploy scripts; `bun install` in the nested mcportal for the build. No vendor.
</preflight>

## 1. THE CELL -- `MP-t-6` (round 1, decomposition s.2/s.3)

Your worktree's HEAD carries these, merged:
- the gateway's owner gate and admin router (`app/owner_gate.py`, `app/admin_api.py`, the `/` mount in `app/server.py`,
  config keys `DASHBOARD_OWNER_EMAILS` and `DASHBOARD_BUNDLE_DIR`);
- the grant handlers (`app/admin_grants.py`);
- the nested `mcportal` repo, at `<worktree>/mcportal`, holding the dashboard pages.

The grant writer is already live. Ship the gateway with the bundle (PRD C3: the gateway serves the built bundle, pinned
by the `mcportal` commit and recorded beside the deploy's commit):
1. **`infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`**:
   - (a) build `mcportal` at its checked-out commit (`bun install` + `bun run build`) and put `mcportal/dist/` into the
     artifact at the path `DASHBOARD_BUNDLE_DIR` names (default `dashboard/` beside `app/`);
   - (b) add `DASHBOARD_OWNER_EMAILS=andrew@opalinvest.com` to the host `.env` it writes (the `printf` at `:170`), and
     change NOTHING else there;
   - (c) record the `mcportal` commit in `infra/aws/ec2/EC2_MANIFEST.json` as `services.opal-gateway.mcportal_commit`,
     beside `deployed_commit`. `safe-ec2-deploy.sh` writes the manifest; extend only what the deploy script hands it,
     or write the key in the same commit, and say which.
   Commit this edit BEFORE the act.
2. **Census what ships** (`git log --oneline <manifest deployed_commit>..HEAD -- infra/aws/ec2/opal-gateway`). Every
   commit must be NFRA_MCPORTAL's or already released. Anything else: STOP, a BLOCKING row naming each commit.
3. **Rollback, named before the act:** the prior artifact in S3 (found by reading the script) and its re-deploy
   command.
4. **NEVER-2, in order:**
   - `python .tools/deploy_ledger.py open` slug `nfra-mcportal-r1-gateway-bundle`, legs = bundle build, artifact build
     + upload, SSM pull + restart, manifest commit;
   - commit the entry AND the sentinel `org/critical_paths/.open_deploys/nfra-mcportal-r1-gateway-bundle.json`;
   - ACT (`infra/aws/ec2/safe-ec2-deploy.sh opal-gateway infra/aws/ec2/opal-gateway/deploy-to-ec2.sh`);
   - close every leg with its proof, and commit the close BEFORE the AC reads.

## 2. BOUNDS

1. Terraform, the ALB, the host and its role are untouched. `safe-ec2-deploy.sh` is read, never edited.
2. If a leg fails, roll back with the named command, close the entry as rolled back, and report. Never half-landed.
3. Standing: no push, no vendor call. REFUSE a criterion you cannot meet as written, and report the refusal with its
   measurement. Never repair a criterion, widen it, or meet it by a route this face does not name.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/EC2_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcportal-r1-gateway-bundle.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~4/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read (never write): `infra/aws/ec2/safe-ec2-deploy.sh`, `infra/aws/ec2/opal-gateway/`, `mcportal/`.

Rows: `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, id `NFRA_MCPORTAL-Z-W4-S<k>`.

## 4. PROOF OF SPEC (literal; run from your worktree root, after the ledger close is committed)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-t-6"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t6.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-t-6"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t6.AC2.sh; echo "exit=$?"</invocation><expect>deployed_commit carries the gate+handlers 2 of 2; mcportal_commit resolves in mcportal=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-t-6"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~O/round1/checks/t6.AC3.sh; echo "exit=$?"</invocation><expect>ssm status=Success; /health=200; /api/admin/whoami=401 or 403; /=401 or 403 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~4/NFRA_MCPORTAL.TO-MP-t-6.gateway-and-bundle-deploy.proof_of_spec.json`. Report once: the census of what shipped, the rollback, the ledger entry path, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the JOIN, WORLD: the CTO's exercised read. Spawned only after chains A, B and C drain AND NFRA_OPALAI's
OA-t-6 closes. Provisioned with `--nested mcportal=<the merged pages branch>`.

<status>superseded -- CTO ruling R-1 (D-2, @aed83d11fe): the grant writer cannot import from its own zip; re-cut in round 2 behind the staged-build cell</status>
<round>1</round>
<slot>~4</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
