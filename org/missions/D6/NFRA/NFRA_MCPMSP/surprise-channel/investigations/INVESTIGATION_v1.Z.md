# NFRA_MCPMSP -- surprise channel, INVESTIGATION v1 (site-Z fabric)

**Home:** the project tree's channel. Lane `ANY`; `.tools/surprise-row-gate.py` validates every NEW row
(schema, identity, coordinate, folder == project). **Append-only.**

**Id grammar on this fabric:** a seat's row is `NFRA_MCPMSP-Z-S<k>`; a worker's row is
`NFRA_MCPMSP-Z-W<n>-S<k>` with `<n>` its slot; `<k>` restarts at 1 per coordinate. `"project":
"NFRA_MCPMSP"` and `"fabric": "site-z"` on every new row. The CVO's adjudication rows live in
`adjudications/`, never here.

---

```json
[
  {
    "id": "NFRA_MCPMSP-Z-S1",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MS",
    "surfaced_at": "2026-09-30T06:05Z",
    "one_line": "A1 names Inflection figures at platinum/mdpf/inflection/, which live only in the shared bucket opal-data-portal-v2 (read today by the gateway's own identity through query_v0), while C5 says the Inflection role reads ONLY opal-data-inf and the gateway identity reads no firm data; opal-data-inf/platinum/ holds no mdpf/ prefix, so round 1's hop 2 cannot satisfy A1 and C5 as written.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/query_v0.py:58 `BUCKET = \"opal-data-portal-v2\"`; asker_scope.handle_asker_query fetches through query_v0._fetch_capped (asker_scope.py:408), i.e. with the gateway's own credentials.",
        "infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml:638 primary: platinum/mdpf/{49financial|inflection|cottonwood|global}/{aggregate-aua-timeseries|aum-metrics|account-distribution}.json (catalog bucket opal-data-portal-v2).",
        "Live listing 2026-09-30 ~06:00Z: s3://opal-data-portal-v2/platinum/mdpf/inflection/ holds account-distribution.json, aggregate-aua-timeseries.json, aum-metrics.json, category-views.json (all 2026-09-29).",
        "Live listing 2026-09-30 ~06:00Z: s3://opal-data-inf/platinum/ holds only _rebuild/, advisors/, clients/, firm/; s3://opal-data-inf/platinum/mdpf/ --recursive returned no object.",
        "infra/logic/01_CENSUS.md:85 names platinum/mdpf/{49financial,cottonwood,inflection}/*.json in opal-data-portal-v2 as LIVE non-conformance against the firm-bucket rule."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.1 C5: the Inflection role reads ONLY opal-data-inf and the gateway identity carries no read on any firm's data; A1: the answer comes from Inflection's model-portfolio figures the portal already serves (platinum/mdpf/inflection/).",
    "world_is": "The platinum/mdpf/inflection/ figures exist only in opal-data-portal-v2 and are reached today by the gateway's own identity; opal-data-inf has no mdpf platinum. A role scoped to opal-data-inf alone cannot fetch A1's figures, and stripping the gateway identity's portal-v2 read would also move the internal Analyst's served mdpf answers.",
    "notes": "Blocks only the cut of round 1's hop-2 cell (the Inflection role's resource list and A1's data source). Three resolutions, the CTO's to pick: (a) the Inflection role reads opal-data-portal-v2 under key-prefix platinum/mdpf/inflection/* with a Deny on the other firms' prefixes (CLAUDE.md shared-bucket shape) and A1n's gateway arm is scoped to opal-data-inf/opal-data-cot only; (b) A1 is answered from an opal-data-inf platinum artifact the portal serves Inflection (advisors/clients/firm), with a catalog row for it; (c) round 1 carries A1 on portal-v2 through the gateway identity and C5's role lands in the FWD-2 enrichment. Hops 0, 1, 3 and 4 are cut independently of this."
  },
{
  "id": "NFRA_MCPMSP-Z-W2-S1",
  "project": "NFRA_MCPMSP",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~2",
  "surfaced_at": "2026-09-30T07:00Z",
  "one_line": "t2.AC1's trust_gateway_role predicate matches only the literals opal-gateway-role / aws_iam_role.opal_gateway / aws_iam_role.gateway, but the order directs referencing aws_iam_role.gw; the first build read trust_gateway_role=n.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MS",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/t2.AC1.sh (trust_gateway_role line) vs infra/aws/terraform/opal-gateway/main.tf:146 aws_iam_role.gw"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order: trust the gateway role by referencing aws_iam_role.gw; AC1 expects trust_gateway_role=y.",
  "world_is": "AC1 is a text grep that does not recognise aws_iam_role.gw; it passed only after a comment naming opal-gateway-role was added to the .tf. The trust itself (Principal AWS = aws_iam_role.gw.arn) was correct before the comment.",
  "notes": "Worker added a one-line comment naming opal-gateway-role; no behaviour change."
},
{
  "id": "NFRA_MCPMSP-Z-W2-S2",
  "project": "NFRA_MCPMSP",
  "fabric": "site-z",
  "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~2",
  "surfaced_at": "2026-09-30T07:10Z",
  "one_line": "safe-commit's naming limb (LGIC_ENFORCE DEC-6) refuses mcpmsp_firm_roles.tf with 14 REFUSE lines: the bucket literals and role/policy names the order and t2.AC1 require are hand-kept carriers; the file cannot be committed as specified.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "disarm_owner": "2.0.0_SA_COO~MS",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh run 2026-09-30 on infra/aws/terraform/opal-gateway/mcpmsp_firm_roles.tf: 'ERROR: BLOCKED -- the naming limb refused ... NAMING-GATE: REFUSE 14 graded'; inline policy name inf-firm-read -> {system}-inf-firm-read-policy; bucket literals -> lookup('inflection'|'cottonwood'|'49financial')"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Task order: write the file with literal bucket ARNs and the builder-named role; t2.AC1 greps for those literals; commit on the worktree branch.",
  "world_is": "The file is written, AC1 and AC2 PASS on the worktree (Plan: 3 to add, 0 to change, 0 to destroy), but the naming gate blocks the commit. The file is left uncommitted in C:/tmp/ms-2. No bypass used.",
  "notes": "Needs either a registry/lookup route for the bucket ARNs and policy names, or an audited gate exemption; both outside the worker's paths."
}
,
  {
    "id": "NFRA_MCPMSP-Z-W3-S1",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~3",
    "surfaced_at": "2026-09-30T08:00Z",
    "one_line": "The gateway's access_state.py in this tree does not know the tenant_firm record type, so the real store refuses the register_tenant write MS-w-1 builds; the offline tests (fake store) cannot see it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/access_state.py@c5dc123f42 POLICY_RECORD_TYPES = (principal_profile, data_entitlement, operator_audit, email_deny); _expected_type/_as_key refuse a POLICY key whose record_type is not in it, so Key('POLICY#TENANT#<tid>','tenant_firm','tenant_firm') raises AccessStateRefused in get() and operator_transact().",
        "access_state.py operator_transact: requires an operator_audit put in the same transaction and exactly one non-email_deny principal partition; a lone tenant_firm put is refused, and the audit record (POLICY#<tid>#<oid>) would be a second partition.",
        "org/standards/NFRA_OPLGTW_CONTRACT.json v1.3 record_types already lists tenant_firm and key_namespaces.POLICY names POLICY#TENANT#<tid>; the contract was amended, the adapter was not."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO MS-w-1: the writer writes the tenant_firm record at POLICY#TENANT#<tid> 'through the store's conditional write' with no IAM change; the contract declares the record type.",
    "world_is": "Writer code builds acs.Key(pk, 'tenant_firm', 'tenant_firm') and calls store.get / store.operator_transact(one put with attribute_not_exists(pk)); against the real AccessState both calls refuse until access_state.py adds tenant_firm to POLICY_RECORD_TYPES and lets operator_transact carry a tenant_firm put without an operator_audit (the writer's changes-table item is the audit). access_state.py is read-only for this cell.",
    "notes": "Op is not deployed; tests pass on fakes (AC1 7 passed, AC2 12 passed). The gateway-reader cell's own access_state change, or a follow-on cell, must land this before MS-a-2 makes the op live. Exact shape written: pk POLICY#TENANT#<lowercased tid>, sk tenant_firm, record_type tenant_firm, fields tid, firm, registered_at, registered_by."
  },
  {
    "id": "NFRA_MCPMSP-Z-S2",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MS",
    "surfaced_at": "2026-09-30T07:55Z",
    "one_line": "The naming builder cannot name Inflection's LIVE bucket opal-data-inf: the registry's scope_bucket['inflection'] is opal-data-inflection and the live bucket is an alias with lookup false, and the ENFORCE naming gate refuses the literal; round 1's firm role therefore reads only the builder-built opal-data-portal-v2 prefix, and C5's firm-bucket read has no conforming carrier until the registry or an R20 entry gives one.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~O",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/logic/registry/scopes.json inflection row: bucket opal-data-inflection (bucket_managed_by s3-lgic-firm-buckets.tf); alias opal-data-inf planes [bucket], provisioned true, routed true, lookup false, where 'the deployed router's target ... opal-data-inflection does not exist yet'.",
        "infra/aws/terraform/modules/opal_name/generated_locals.tf:65-79 scope_bucket: inflection -> opal-data-inflection; global -> opal-data-portal-v2.",
        "naming gate (ENFORCE) on MS-t-2's first file, 2026-09-30: 14 REFUSE, e.g. 'arn:aws:s3:::opal-data-inf/* -> lookup(inflection)', and even the builder's own output string gateway-inf-firm-reader-role typed as a literal.",
        "infra/aws/terraform/investor-reporting/holdings-performance/iam.tf:7-21: the firm buckets carry a live DenyForeignFirmPrincipals statement admitting only role/*-<short>-* principals, so other firms' buckets already refuse gateway-inf-firm-reader-role."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.3 C5: the per-firm role reads its firm's bucket (opal-data-inf for Inflection, record s.10 card 5 'current buckets for now') AND its firm's prefixes in opal-data-portal-v2, with a bucket-scoped Deny on every other firm's bucket.",
    "world_is": "Round 1's role (MS-t-2 AMENDMENT 1) reads only opal-data-portal-v2/platinum/mdpf/inflection/*, named and addressed through module opal_name; no firm-bucket Allow and no literal cross-firm Deny (the buckets' own live fences deny foreign principals). FWD-1 is served; C5's firm-bucket read is not yet expressible through the builder.",
    "notes": "Not blocking round 1 (A1's figures live only under the portal prefix). Needed before any cell reads opal-data-inf: a registry route that yields the routed bucket for a firm (an LGIC act), or an R20 departure Andrew acknowledges. The CTO rules which."
  },
  {
    "id": "NFRA_MCPMSP-Z-W2-S3",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~2",
    "surfaced_at": "2026-09-30T09:20Z",
    "one_line": "safe-apply.sh's naming-plan limb (ENFORCE) REFUSES the whole opal-gateway apply because the tree's UNTARGETED plan shows aws_iam_role_policy.gw_rivalfunds_read (rivalfunds-iam.tf, name opal-gateway-rivalfunds-read) as an ADDITION; the gate plans the full tree and ignores -target and a saved planfile, so MS-a-1's three targeted additions cannot pass it; nothing was applied.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Targeted plan (TF_DATA_DIR private copy, 2026-09-30): 'Plan: 3 to add, 0 to change, 0 to destroy.' for aws_iam_role.inf_firm_reader, aws_iam_role_policy.inf_firm_reader, aws_iam_role_policy.gw_assume_inf_firm_reader.",
        "safe-apply run 3 (HALT_ACK=1, after the staged dir was supplied): '[naming-plan-gate] NAMING REFUSE aws_iam_role_policy.gw_rivalfunds_read opal-gateway-rivalfunds-read -> gateway-rivalfunds-read-policy ... (ADDITION)', 'NAMING-PLAN: REFUSE 59 graded', 'safe-apply: BLOCKED by the naming plan limb (LGIC_ENFORCE DEC-6, ENFORCE mode, rc=1). Nothing was planned further or applied.' .tools/safe-apply.sh lines ~100-130 run 'terraform plan -input=false -lock=false' with no -target; org/mcp/naming-gate.enforce exists.",
        "Live read after the block: iam get-role gateway-inf-firm-reader-role = NoSuchEntity (nothing landed). a1.AC2 simulate = NoSuchEntity; a1.AC3 AssumeRole = implicitDeny.",
        "Two earlier safe-apply faults, both environment: (1) HALT-GATE 'blocked' on 208 pending ROUTINE messages about other seats' ledgers, cleared per its own protocol with HALT_ACK=1 (no STOP-class line, 0 matches); (2) the full-tree plan the gates run needs a SECOND gitignored build input beyond the layer zip the order named: infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/.build/staged (archive_file source_dir); copied from the main tree, untracked and gitignored, outside this order's <paths>."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO MS-a-1 section 1 item 2: 'Plan, then apply, targeted ... through bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply -target=...' with the plan reading only additions for the targets; the directory 'needs' the layer zip and the key vars.",
    "world_is": "A targeted plan reads 3 to add / 0 / 0, but safe-apply's gates plan the WHOLE tree, and under ENFORCE the naming-plan limb refuses it on an unrelated pre-existing addition (gw_rivalfunds_read, rivalfunds-iam.tf, which this order may not touch). No override for that limb exists short of removing org/mcp/naming-gate.enforce or an R20 entry, both outside this order; bare terraform apply is barred. The apply did not run; the ledger entry nfra-mcpmsp-r1-firm-role stays OPEN (nothing landed, blast radius untouched). The saved plan and TF_DATA_DIR sit in this worktree's .scratch for a retry.",
    "notes": "Ways through, issuer's call: (a) a different cell lands the rivalfunds policy name (or its state import) so the full plan has no refused addition; (b) the CTO rules a one-apply naming-gate exemption for these three additions; (c) apply from a tree whose full plan is clean. Fresh time cost: each safe-apply run spends ~4.5 min in three full-tree refreshes before it reaches the refusal."
  }
]
```
