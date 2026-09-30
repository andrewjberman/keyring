# NFRA_MCPINDEX task order -- `MX-r-6` -- the Schwab enable release: `schwab` in ENABLED_INTEGRATIONS, the reader role's dim_transaction read, MX-s-15 and MX-q-3 shipped; then the FWD-1 cold run (r6.J1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-r-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~19</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a one-shot deploy.
comp-iam: RUN -- 2026-09-30 ~08:4xZ by the issuer: `comp-iam role opal-gateway-role` shows sts:AssumeRole under the schwab ExternalId condition; `comp-iam role gateway-schwab-read-role` returns no match (its TF index does not resolve the reader role by name), so the APPLIED plane was read directly: simulate-principal-policy on gateway-schwab-read-role -> dim_position allowed, dim_transaction explicitDeny. This cell safe-applies the two dim_transaction prefixes (one policy change); the gateway role, the ExternalIds and the secrets are unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE -- the MX-r-4/MX-r-5 release pattern; never-widen halves (CTO + COO) and a G-A delta before PHASE B.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (S3 upload, SSM, IAM).
</preflight>

## 1. THE CELL -- `MX-r-6` (round 5; `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/1.0.0_SA_CTO~O/REINSTATE_RULINGS_20260930.md` @4e598ab7be, rulings B1, B2, B4, B7)

**Start after MX-s-15 AND MX-q-3 are complete and drained.** The issuer continues you with this order.

The worked precedent is MX-r-5. READ its A1/A2 blocks, and MX-r-4's they cite:
`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-5.release-and-thread-rerun.md` and
`org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-r-4.thread-live-enable.md`. They cover the release tree
cut at the LIVE deployed commit, the census, the rollback tree, and the DEPLOY-ONLY tree the halt gate admits. The
Schwab enable procedure is `docs/architecture/NFRA_INTEGRATIONS_STANDARD.md:101,170` (env + IAM + deploy), and its
rollback is `infra/aws/ec2/opal-gateway/runbooks/SCHWAB_PILOT_RUNBOOK.md:233-276`.

**AMENDED A1 (2.0.0_SA_COO~MI, 2026-09-30 ~10:0xZ) -- on row Z-W19-S2 (BLOCKING, ARMED, issuer-owned), ruled by row Z-S63.**
- **A 7th surface.** `org/standards/NFRA_OPLGTW_CONTRACT.json` lists the datasets and fields the gateway serves and a
  grant may carry. It names only the three dims, so the running gateway answers `dataset_invalid` for `dim_transaction`
  and `tests/acceptance/test_local_acceptance.py` regresses from 14 passed to 8 failed (`KeyError` at
  `tests/acceptance/conftest.py:289`).
- **STEP 0, before the release cut, and it may start before MX-q-3 drains:** add `dim_transaction` to the contract's
  `datasets`, its served fields to `fields` (exactly MX-s-15's 15 served columns, `SCHEMA_MX-s-15.md`), and any
  `additive_fields` entry the schema needs. Fix the acceptance harness's dataset default the way MX-s-15 fixed
  `tests/test_schwab_wiring.py`. `tests/acceptance/test_local_acceptance.py` passes 14 of 14 again. Commit it on your branch.
- **The ANNOUNCE names the contract change** beside the census, because it widens what a grant may name. No grant is
  created or changed (B2): existing grants name the three dims explicitly and stay as they are.
- **Paths granted in addition:** `org/standards/NFRA_OPLGTW_CONTRACT.json`, `infra/aws/ec2/opal-gateway/tests/acceptance/`
  (already inside `infra/aws/ec2/opal-gateway/**`).
- Graded by: no gate limb graded this modification (to-pipeline-gate LIMB 6 grades only a newly-added order; GATE (viii)
  finds `<placeholders>NONE</placeholders>`).

**AMENDED A2 (2.0.0_SA_COO~MI, 2026-09-30 ~09:4xZ), on 1.0.0_SA_CTO~O's ruling msg 27068.** No grant is widened in round
5. B2 bars it, and admitting a principal to data is Andrew's own act (FWD-9). r6.J1's transaction question is graded as a
correct, honest refusal, and the proof names the principal and its grant. The CTO carries "widen one existing Schwab
grant to dim_transaction through the grant admin tool" to Andrew's list. Graded by: no gate limb graded this
modification.

**AMENDED A3 (2.0.0_SA_COO~MI, 2026-09-30 ~12:0xZ) -- on PHASE A rows Z-W19-S7 and Z-W19-S8 (BLOCKING, ARMED, issuer-owned), ruled by row Z-S66.**
- **Z-W19-S7: the Schwab service needs its host inputs, and the release must ship them.** Adding `schwab` alone
  registers 5 tools that all fail closed (`ContractUnavailable` / `RoleConfigError`). The release therefore also ships:
  - the contract file, into the artifact at the path `load_contract` reads, or onto the host by the deploy script;
  - the host `.env` keys the service's own loaders name: the contract path, the two reader-role ARNs, the ExternalId
    source and the account_ref secret id. Take the key names from the code (`load_contract`, `role_configs`), never
    from memory.
  - No secret VALUE is written into the repo, the artifact or `.env`. The ExternalIds and the account_ref key stay in
    Secrets Manager (`opal/mcp/opal-gateway-schwab-reader-external-ids`, `opal/mcp/opal-gateway-schwab-account-ref-key`),
    which the gateway role reads by resource policy. `.env` carries only their ids and the non-secret role ARNs.
  - Prove it before the ANNOUNCE is final: an in-process call of `schwab_get_access` / `schwab_list_files` in the
    DEPLOY-ONLY tree, with the release's `.env` shape and the operator's read credentials, no longer raises either
    error. Record which env keys were added and the census delta.
- **Z-W19-S8: the apply is the SAVED TARGETED PLAN, and only it.** It is
  `-target=aws_iam_role_policy.schwab_data_read_policy`: 0 add, 1 change, 0 destroy, 8 added `dim_transaction` elements.
  At PHASE B, re-plan targeted at the GO. Apply only if it is byte-equal in effect (the same one change), through
  `safe-apply`. Never an untargeted apply. `gateway-rivalfunds-read-policy` and the grant-writer Lambda hash are other
  seats' pending acts and are not touched.
- **Paths granted in addition:** the gateway's artifact build/tar-roots file(s) (inside `infra/aws/ec2/opal-gateway/**`,
  already granted) and `infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` beyond line 197, for the `.env` keys only.
- Row Z-W19-S9 (the grant-writer Lambda's own contract copy) is INERT for this round: no grant is changed (B2). It
  rides with the CTO's "widen one grant" item on Andrew's list.
- Graded by: no gate limb graded this modification (to-pipeline-gate LIMB 6 grades only a newly-added order; GATE (viii)
  finds `<placeholders>NONE</placeholders>`).

### PHASE A -- no deploy, no apply
1. Read the deployed commit from the host's artifact, by content (MX-r-5 left 093fc247c6). Cut the release there and
   cherry-pick MX-s-15's and MX-q-3's gateway commits. The issuer's GO names whether MX-t-10 rides too.
2. `deploy-to-ec2.sh:197`: `ENABLED_INTEGRATIONS` gains exactly `schwab`, giving 6 ids. No other id moves.
3. Terraform: run `terraform plan` in `infra/aws/terraform/opal-gateway/` and save it. The plan must change ONLY
   `gateway-schwab-read-role`'s policy, adding the two `dim_transaction` prefixes. Any other planned change is a
   BLOCKING row; do not proceed.
4. Build the rollback tree at the live commit and prove it per file against the live artifact. The IAM rollback is the
   prefix list without `dim_transaction`.
5. Build the deploy-only tree and prove its gateway tree object equals the release's.
6. Write `ANNOUNCE_MX-r-6.md`: the pin, the census, the saved plan, the tool-count delta (5 schwab tools + 1 query tool,
   plus MX-t-10's if it rides), and MX-s-15's `ENTITLEMENT_MX-s-15.md` finding (whether existing Schwab grants cover
   transactions once declared). Report the pin. The issuer takes it to 1.0.0_SA_CTO~O for the G-A delta and both
   never-widen halves. DO NOT DEPLOY OR APPLY.

### PHASE B -- only on the issuer's GO
7. NEVER-2 ledger `nfra-mcpindex-r5-schwab-enable`, opened before the first act. `safe-apply` the saved plan (never bare
   `terraform apply`), then deploy from the deploy-only tree.
8. Read back: the host `.env` names 6 ids; `/health` is 200; the tool count moves by exactly the announced delta; the
   live reader role is allowed `dim_transaction` for both masters. Record the manifest, then close the ledger.
9. Roll back IAM and host from the rollback tree on any failed leg. Never half-landed.

### The FWD-1 cold run (r6.J1) -- after the deploy
10. Workers have no authenticated route, so the ISSUER runs it. The asker is an ALREADY-ADMITTED Opal principal who
    did not author the index and already holds a Schwab grant (rulings B1, B2), in a fresh session with only the MCP
    connected. You record what you can measure in-process on the deployed tree: which tools the host lists, and what
    discover names for each question in the issuer's set.

## 2. BOUNDS

1. The gateway role, the ALB, the ExternalIds and the secrets are untouched. No identity, grant or sign-in is created,
   changed or tested (ruling B2).
2. Never half-landed: roll back from the rollback tree on any failed leg.
3. Nothing under `data/cot/`. No push. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
infra/aws/ec2/EC2_MANIFEST.json
infra/aws/ec2/opal-gateway/**
infra/aws/terraform/opal-gateway/schwab_reader_iam.tf
org/standards/NFRA_OPLGTW_CONTRACT.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpindex-r5-schwab-enable.json
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~19/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/**
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W19-S<k>`; re-read the file for the next free k at commit time;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`.

## 4. PROOF OF SPEC (literal; run from your worktree root)

<proof_of_spec>
  <expected_criteria>AC1,AC2,J1</expected_criteria>
  <criterion id="AC1" cell_refs="MX-r-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/r6.AC1.sh; echo "exit=$?"</invocation><expect>entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR printed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-r-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round5/checks/r6.AC2.sh; echo "exit=$?"</invocation><expect>status=Success; /health=200; shipped 3 of 3; ids enabled 6 of 6; live reader-role GetObject on dim_transaction allowed 2 of 2 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="J1" cell_refs="MX-r-6" judgment="true"><!-- r6.J1, graded at L9 by 3.0.0_SA_CVO~O, never self-graded: FWD-1 (PRD:102-109) EXERCISED -- a set of real questions, asked cold by an already-admitted Opal principal who did not author the index, routes correctly: discover answers from ONE catalog with property, dataset, freshness, firm scope, caveats and the next tool; a question about an uncatalogued property says so and names nothing. The set includes one Schwab position question, answered for one master and one date, and one Schwab transaction question, which PASSES as a correct, honest refusal naming the principal and its grant (AMENDED A2). No grant is widened in round 5. Denominator: the questions asked, printed. The issuer's cold-run record is the material. --></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~19/NFRA_MCPINDEX.TO-MX-r-6.schwab-enable-release.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the proof instance at the `<instance_path>`. Report once, in your final message. Do not edit this task order.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Reinstatement rulings B1 (the enable; G-C is no precondition), B2 (G-B by any
admitted non-author principal), B4 and B7 ride here; round-5 order items 2, 3 and 6. Dry-run at base: r6.AC1 FAIL (no
entry); r6.AC2 FAIL (ids enabled 5 of 6; reader role GetObject on dim_transaction 0 of 2, explicitDeny, with the
dim_position control allowed).

<status>pending</status>
<round>5</round>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
