# TO COMM_ASSIST.TO-CA-d-1 -- round 11 CA-d-1: the mail key's wiring in the assistant's module, inert until one variable is set

<to_id>COMM_ASSIST.TO-CA-d-1</to_id>
<project>COMM_ASSIST</project>
<issued_to>0.9.0_WK_COMM_ASSIST~5</issued_to>
<issued_by>2.0.0_SA_COO~R</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>

**Directive:** D9 | **Fabric:** laptop | **Decomp cell:** `CA-d-1` (`decompositions/COMM_ASSIST_DECOMP.round11.md`) | **outcome_ref:** FWD-4 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CA-d-1`. Andrew's assistant runs as two Lambdas from `module "ldo_001"` in `infra/aws/terraform/transcripts/chat_assist.tf`
(read the whole file). Its new mail poller reads the gateway's mail route with a bearer it fetches by the secret name or ARN in
the env var `MAIL_BEARER_SECRET`. Without that env var the poller does nothing, by design. The bearer will be handed over later by
secret reference. This cell prepares everything else so the deploy is one value.

- The functions' environment is `local.ca_env`, given to both `handler` and `ingress`.
- The module grants `secretsmanager:GetSecretValue` on the list `secret_arns` (`infra/aws/terraform/modules/ldo/main.tf` ~line 295).

### BUILD, IN THIS ORDER

1. `chat_assist.tf` only:
   - add `variable "chat_assist_mail_bearer_secret_arn"` (string, default `""`), described as the mail route's bearer secret
     handed over by NFRA_OPLGTW release r29;
   - when it is non-empty, `MAIL_BEARER_SECRET = <that value>` joins the environment both functions get (a `merge` on
     `local.ca_env`), and the value joins `secret_arns` (a `concat`);
   - when it is empty, the environment and `secret_arns` are exactly what they are today;
   - one comment line saying so. No other change.
2. Two READ-ONLY targeted plans, as cell CT-i-6 of NFRA_CTLPLN did (read its notes: the root does not load until both packages
   exist on disk, so build `bash infra/aws/lambda/transcripts-pull/build.sh` and `bash infra/aws/lambda/teams-chat-assist/build.sh`
   first; building uploads nothing):
   - `TF_DATA_DIR` set to a NEW scratch directory outside every git tree; `terraform -chdir=infra/aws/terraform/transcripts init
     -input=false` against the declared backend (stop if it prompts to migrate or reconfigure; never `-reconfigure`);
   - `terraform -chdir=infra/aws/terraform/transcripts plan -input=false -no-color -lock=false -target=module.ldo_001` saved
     to `PLAN_EMPTY.txt`;
   - the same plus `-var 'chat_assist_mail_bearer_secret_arn=arn:aws:secretsmanager:us-east-1:000000000000:secret:comm-assist-plan-probe'`
     saved to `PLAN_SET.txt`;
   - both saved in your deliverables folder `org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~5/`.
3. `PLAN_READ.md` in the same folder: each plan's summary line and every changed address with its changed arguments, in your own
   reading. The empty plan is expected to change only the two functions' `source_code_hash` (the package moved since the last
   deploy) and nothing else. The set plan adds the env var on both and the probe ARN in the policy.

### RULES FOR THIS CELL

- **Apply nothing.** No `apply`, no `safe-apply`, no `import`, no `state` write, no `-lock=true` plan. `plan -lock=false` and `init`
  in a scratch data directory are the only Terraform commands. No other AWS call. Do not run `init -reconfigure` or `-migrate-state`.
- Edit nothing but the files in `<paths>`. `dist/` builds are never committed. The probe ARN is fake on purpose; never a real one.
- No non-ASCII. Bake no absolute path.
- Refuse a criterion you cannot satisfy as written and report the refusal with its measurement; do not repair or widen it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CAd1-AC1" cell_refs="CA-d-1"><invocation>python "org/missions/D9/COMM/COMM_ASSIST/deliverables/2.0.0_SA_COO~R/checks/check_ca_d_1_plans.py"</invocation><expect>PLANS-CA-d-1 ok=True</expect></criterion>
`CAd1-AC1` -- the issuer's check (read it; do not edit it) on your two saved plans: empty is inert (no env var, no probe ARN, nothing outside the module, 0 add, 0 destroy); set wires both functions and the read. It fails at the base.

<criterion id="CAd1-AC2" cell_refs="CA-d-1"><invocation>python infra/aws/terraform/transcripts/tests/check_chat_assist_bus.py</invocation><expect>CHAT-ASSIST-BUS ok=True</expect></criterion>
`CAd1-AC2` -- the bound: the module's four bus statements are unchanged.

<criterion id="CAd1-AC3" cell_refs="CA-d-1" judgment="true"/>
`CAd1-AC3` -- JUDGMENT, never self-graded: `PLAN_READ.md` names every change in both plans and nothing in the empty plan beyond the package hash.
</proof_of_spec>

<expected_criteria>CAd1-AC1,CAd1-AC2,CAd1-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Record `CAd1-AC3` with NO verdict (status `UNVERIFIABLE-BY-INSTRUMENT`, the reason naming
`3.0.0_SA_CVO`). Write the proof instance to
`org/missions/D9/COMM/COMM_ASSIST/deliverables/0.9.0_WK_COMM_ASSIST~5/COMM_ASSIST.TO-CA-d-1.mail-key-wiring.proof_of_spec.json`,
validate it with `python .tools/proof-of-spec-check.py <instance> CAd1-AC1,CAd1-AC2,CAd1-AC3`, and flip `<status>` to `complete`
only when both mechanical criteria pass and the instance is VALID. Your surprise rows are `COMM_ASSIST-W5-S<k>`; append lines only
to the investigation file and keep its existing line endings.

<decomp_ref>
<decomp_doc>org/missions/D9/COMM/COMM_ASSIST/decompositions/COMM_ASSIST_DECOMP.round11.md</decomp_doc>
<owned_cells>CA-d-1</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/transcripts/chat_assist.tf
org/missions/D9/COMM/COMM_ASSIST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: RUN -- denominator: 1 policy (module.ldo_001's exec policy), 1 statement changed only when the variable is set: GetSecretValue gains ONE ARN, the one handed over; nothing when empty (proved by PLAN_EMPTY). BLIND: a cross-account secret (if site Z's store is another account) would also need a resource policy there; the reference is read at the deploy.
comp-adversary: RUN -- a wiring that changes the live policy or env before the reference exists (PLAN_EMPTY must show neither); an apply by a build cell (forbidden; plan -lock=false only); a real ARN typed in (a fake probe only); a backend migration prompt (stop). BLIND: the package hash change in PLAN_EMPTY is rounds 8-10's code, deployed with round 9's pair, not here.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/COMM_ASSIST_PRD.md` v0.2 (ADMITTED, `805fec22c5`), FWD-4, C-MAIL; site Z msg 32236 (relay 107602).
