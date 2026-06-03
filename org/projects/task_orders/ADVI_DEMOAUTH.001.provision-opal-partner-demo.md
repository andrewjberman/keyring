<task_order>
<metadata>
  <to_id>ADVI_DEMOAUTH.001</to_id>
  <project>ADVI_DEMOAUTH (demo tenant auth fix)</project>
  <title>Provision opal-partner-demo so the demo login mints firmRole claims + renders AdvisorIntelligence — INFRA half 0.6.0 lead, CONTRACT half auth-domain (0.7.0/DE) confirm</title>
  <assigned_to>0.6.0_AE_PartnerETL (lead, infra + draft contract) · 0.7.0_AE_CloudOps / DE (contract confirm)</assigned_to>
  <issued_by>2.0.0_SA_COO</issued_by>
  <issued_date>2026-06-03</issued_date>
  <status>active — 0.6.0 GO on the infra half + contract draft NOW; 0.7.0 contract-confirm queued behind Andrew-live security (light review)</status>
  <dispatch_held>false</dispatch_held>
  <priority>NORMAL — Andrew wants the demo back, NOT on-fire. Bounded, in-pattern (identical class to the 6-02 Inflection Peter fix).</priority>
  <references>
    <ref type="greenlight">Andrew-direct GO 2026-06-03 (0.6.0 192141Z): in-pattern partner-demo table = "easiest way".</ref>
    <ref type="root-cause">opal-partner-demo never existed; register_demo_tenant.py provisioned only opal-users-v2. demo login -> firmRole=null (required since Peter-era tightening) -> empty AdvisorIntelligence. Demo DATA 100% intact (opal-data-demo 9,282 objs/169 advisors).</ref>
    <ref type="pattern">IDENTICAL class to the 6-02 Inflection firmRole incident 0.7.0 fixed. Mirror opal-partner-49financial (11 items). Auth-handler = infra/aws/opalinvest_dev/lambda/auth-handler/ (Cognito pre-token-gen); resolver infra/aws/lambda/lib/partner/tableName.ts.</ref>
    <ref type="access-model">Demo opal-gated: internal opal users already see all firms incl demo (portal firmAccess.ts:79); the partner table covers the demo login + whitelisted externals.</ref>
  </references>
</metadata>

<scope>
## INFRA half — 0.6.0_AE (lead, NOW; your partner-ETL lane):
1. Create DynamoDB table opal-partner-demo mirroring opal-partner-49financial: key=email HASH, GSI on advisorRole, PAY_PER_REQUEST. NOT TF-managed (CLI/script-provisioned like the peer tables) -> create via CLI OR fold into register_demo_tenant.py (preferred: fold in, so demo re-provisioning is idempotent + captured).
2. IAM CONFIRM (the gate): verify the auth-handler Lambda's role can read opal-partner-demo. If the role policy is wildcard `opal-partner-*`, the new table is auto-covered = NO IAM change (likely, since it reads 49financial/inflection/cottonwood). If per-ARN, the ARN add is the auth-handler role's domain (0.7.0) -> coordinate, do NOT unilaterally edit 0.7.0's auth-handler IAM. Report which.
3. DRAFT the contract entry by mirroring the opal-partner-49financial ADMIN entry (read it as the template) -> hand to 0.7.0/DE for confirm before final put (step below).

## CONTRACT half — auth-domain (0.7.0/DE) confirm:
4. CONFIRM the demo@demo.test entry shape before it's put: firmRole=admin (firm-level full 169-advisor view) + advisorKey/advisorName/advisorRole per the demo-view contract. RISK (0.6.0-flagged): admin-only may need a sentinel advisorKey or a demo slug -- getting this wrong RE-BREAKS it. 0.7.0 did the identical Inflection fix, so this is a light review of 0.6.0's 49financial-mirrored draft, not a full build. Queued behind Andrew-live security (0.7.0) OR a live DE.
5. Put the confirmed demo@demo.test entry. Fresh login (claims bake at login) -> verify AdvisorIntelligence renders (169 advisors, firm-admin view).
</scope>

<acceptance>
- [ ] opal-partner-demo table created (mirror 49financial, CLI/script, ideally folded into register_demo_tenant.py idempotently). RAVC1 the infra to COO.
- [ ] auth-handler IAM confirmed (wildcard = no change, OR per-ARN add coordinated w/ 0.7.0). Reported.
- [ ] demo@demo.test entry CONTRACT confirmed by auth-domain (0.7.0/DE) -- firmRole=admin + advisorKey/advisorName/advisorRole shape, no re-break. 0.6.0 drafts (49financial-mirror), 0.7.0 confirms.
- [ ] entry put; fresh demo login renders AdvisorIntelligence (169 advisors). Andrew/visual smoke = closure. RAVC2 to COO.
</acceptance>
</task_order>
