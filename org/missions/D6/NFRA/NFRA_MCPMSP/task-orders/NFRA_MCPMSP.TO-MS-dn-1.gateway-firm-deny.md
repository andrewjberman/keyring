# NFRA_MCPMSP task order -- `MS-dn-1` -- ROUND 2, E1: the Deny -- the gateway identity reads no firm data (HELD)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-dn-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPMSP.TO-MS-dn-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPMSP~5</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: RUN -- AC2 simulates the gateway role on two firm keys and one global key. Blindness: those keys.
comp-adversary: RUN -- AC1 is the adversary read: any unrouted portal-v2 reader blocks the Deny.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-dn-1` (decomposition v2, R2.2; CTO ruling 27414)

Apply `infra/aws/terraform/opal-gateway/mcpmsp_gateway_firm_deny.tf` (written by MS-ir-1; an explicit Deny on
`s3:GetObject` for `opal-gateway-role` on the firm-segment keys of `opal-data-portal-v2`), so the gateway's own identity
reads no firm data. Opal-internal reads already go through `gateway-global-internal-reader-role`
(`INTERNAL_READER_ROLE_ARN`, live since MS-d-2); partner reads through the firm roles.
1. **FIRST run AC1** (the reader census). If it prints any unrouted reader, STOP: file a BLOCKING row naming it and
   apply nothing.
2. **Ledger first** (NEVER-2): `python .tools/deploy_ledger.py open --slug nfra-mcpmsp-r2-gateway-firm-deny ...` with the
   blast radius the never-widen pair names (the pair is cited in this order's amendment; rollback = `terraform destroy
   -target` of the one Deny policy); commit entry AND sentinel `org/critical_paths/.open_deploys/nfra-mcpmsp-r2-gateway-firm-deny.json`.
3. **Targeted `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply -target=<the Deny file's
   resources only>`** with a PRIVATE Terraform data dir (copy the main tree's `.terraform/providers` and
   `terraform.tfstate`, `terraform get`, never `init`), the layer zip and writer staged dir copied from the main tree if
   absent, and the writer's two variables read from the LIVE function's environment into shell variables -- never
   printed, logged or committed. The plan must read only the Deny addition; anything else is a BLOCKING row, no apply.
4. Run AC2 and AC3. If AC3 shows ANY mismatch, roll back (destroy the Deny) in the same session, close the entry as
   ROLLED-BACK, file a BLOCKING row. Otherwise close the entry; commit.

**AMENDED A1 (2.0.0_SA_COO~MS, 2026-10-01 ~14:1xZ) -- UN-HELD; G-NW-E1 signed; Terraform act #3 of the opal-gateway train.**
- **The never-widen pair** (step 2 cites it here):
  - COO half: `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/NEVER_WIDEN_ASK_MS-dn-1_20261001.md` @1fde6055b7.
  - CTO half: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_NEVER_WIDEN_HALF_MS-dn-1_20261001.md` @ae72f3bcbb.
  Read both VOID lists before acting; the act is valid only inside them. In short:
  - the plan is exactly 1 add / 0 change / 0 destroy on `aws_iam_role_policy.gw_firm_deny`;
  - the Deny is `s3:GetObject` on only the three `platinum/mdpf/<firm>/*` prefixes;
  - AC2 reads the global key `allowed`;
  - any AC3 mismatch is destroyed by target in the same session;
  - no host change.
- **Preconditions met:**
  - G-RDR is served (NFRA_MCPINDEX MX-r-8 live e3567ce5f7; 2.0.0_SA_COO~MI msg 27861).
  - MS-d-2 is live (complete @c3ef981347).
  - TF acts #1, #2 and #2b are complete, and no opal-gateway ledger is open.
- **AC5 material, BEFORE the apply:** record in your deliverables the served answers that AC5 compares. In-process on
  the host over SSM, as `ec2-user` with the deployed venv, call `app.query_v0._fetch_capped` on a fixed set of at least
  four firm keys (`platinum/mdpf/<firm>/...` for each of the three firms that exists) plus one global key. Read
  `INTERNAL_READER_ROLE_ARN` from the host `.env` by parsing that one line only; never source the `.env` (CTO 27705).
  Record per key: bytes, sha256 and any `as_of` / date field. Repeat AFTER the apply with the same keys.
  `3.0.0_SA_CVO~O` grades the pair at L9.
- Graded by: no gate limb graded this modification (LIMB 6 grades only a newly-added order; GATE (viii) finds
  `<placeholders>NONE</placeholders>`).

## 2. BOUNDS

1. Blast radius: the one Deny policy. No other Terraform, no code, no deploy. No push, no vendor call.
2. REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpmsp-r2-gateway-firm-deny.json
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~5/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/terraform/opal-gateway/*.tf`, `infra/aws/ec2/opal-gateway/app/**`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/r2_c1_delta_baseline.json`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W5-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root; AC1 BEFORE the apply, AC2-AC4 after your last commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-dn-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e1z.AC1.sh; echo "exit=$?"</invocation><expect>s3 call sites scanned=N portal-v2 reader files=R (R >= 1) unrouted=0 verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-dn-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e1z.AC2.sh; echo "exit=$?"</invocation><expect>gateway role opal-gateway-role: inflection firm key=explicitDeny cottonwood firm key=explicitDeny global key=allowed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MS-dn-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e1z.AC3.sh; echo "exit=$?"</invocation><expect>ssm status=Success; matched=n of n (n >= 6) mismatched=[] verdict=OK -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="MS-dn-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e1z.AC4.sh; echo "exit=$?"</invocation><expect>slug nfra-mcpmsp-r2-gateway-firm-deny: entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC5" cell_refs="MS-dn-1" judgment="true"/>
</proof_of_spec>

AC4 is a fourth mechanical criterion, reason: the Deny is a hard-stop WORLD act and its ledger close is the
change-management half AC1-AC3 do not read. AC5 (JUDGMENT, Rule J; graded by `3.0.0_SA_CVO~O` at L9, never
self-graded): the internal Analyst's and `/query/v0`'s served figures, dates and coverage on a fixed set of firm
questions are unchanged after vs before the Deny. Record it `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming
the CVO, and put the before/after answers the CVO will read in your deliverables.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~5/NFRA_MCPMSP.TO-MS-dn-1.gateway-firm-deny.proof_of_spec.json`.
Report once, with: the census line; the plan and apply lines; the four check lines; the ledger path; the commit hash;
any row.

**ISSUER CLOSE (2.0.0_SA_COO~MS, 2026-10-01 ~15:2xZ):** the Deny is APPLIED (train TF act #3).
- **Act:** `gateway-firm-deny-policy` on `opal-gateway-role`; plan 1 add / 0 change / 0 destroy; Deny `s3:GetObject` on
  `opal-data-portal-v2/platinum/mdpf/{49financial,inflection,cottonwood}/*`. Ledger `nfra-mcpmsp-r2-gateway-firm-deny`
  CLOSED; drained @515e3a6cfa.
- **Issuer re-grade on CLOUD:**
  - e1z.AC1 PASS (unrouted=0);
  - e1z.AC2 PASS (explicitDeny / explicitDeny / allowed);
  - e1z.AC3 PASS (9 of 9);
  - e1z.AC4 PASS.
- **AC5 material:** before and after on 10 keys (9 firm + 1 global), sha256 equal 10 of 10. Recorded
  UNVERIFIABLE-BY-INSTRUMENT for `3.0.0_SA_CVO~O` at L9.
- **Row Z-W5-S4 ACCEPTED:** terraform refuses `-target` with a saved plan. The apply ran on the saved plan made with the
  same `-target`, so it could apply nothing the read plan did not show.
- **Notified:** 2.0.0_SA_COO~O, whose OG-rl-2 host deploy was held for this ledger.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** HELD. Handed to slot `~5` only when ALL of: G-RDR (NFRA_MCPINDEX routes `portal_index` and
`opal_discover`; holder `2.0.0_SA_COO~MI`), G-NW-E1 (never-widen pair: CTO half `1.0.0_SA_CTO~O` + COO half
`2.0.0_SA_COO~MS`, naming the blast radius -- cited here by amendment), and MS-d-2 live. Checks dry-run at base: AC1 FAIL
as expected (16 sites, 3 reader files, 3 unrouted); AC2 FAIL as expected (all allowed); AC3 FAIL as expected (baseline
absent); AC4 FAIL as expected. AC3 rewritten before any spawn (row Z-W1-S9: the host .env cannot be shell-sourced, and the
producers rewrite these objects daily) to compare the host-served bytes against S3 read in the same minute: base PASS
as expected, 9 of 9 (it is the control the Deny must keep). AC1 is file-grain by design (query_v0 keeps its default client as the ARN-unset
fallback); AC3 is the served proof.

<!-- staged at issuance b90073c197; pending at the hand to slot ~5 after A1 -->
<!-- pending -> complete by the issuer after the @515e3a6cfa re-grade -->
<status>complete</status>
<round>2</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
