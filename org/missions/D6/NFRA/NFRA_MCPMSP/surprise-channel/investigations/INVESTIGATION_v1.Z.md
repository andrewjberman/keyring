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
  },
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
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~1",
    "surfaced_at": "2026-09-30T09:40Z",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "id": "NFRA_MCPMSP-Z-W1-S1",
    "one_line": "app/access_state.py refuses the tenant_firm record type: POLICY_RECORD_TYPES lacks it, so AccessState.get/query/operator_transact raise AccessStateRefused (or DependencyUnavailable on decode) for POLICY#TENANT#<tid>, and the reader (MS-t-1) and the writer (MS-w-1) cannot touch the registry through the adapter until that one tuple is extended.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/app/access_state.py:59 POLICY_RECORD_TYPES = (principal_profile, data_entitlement, operator_audit, email_deny); _as_key (:185-190) and _decode (:320-322) return/raise unless key.record_type is in it (via _expected_type :172-181).",
        "org/standards/NFRA_OPLGTW_CONTRACT.json declares tenant_firm in state_store.record_types and key_namespaces.POLICY (POLICY#TENANT#<tid>), but access_state.py was not amended.",
        "Measured in worktree wk-NFRA_MCPMSP-1: asker suites run 22 passed 1 failed; the failure is tests/test_asker_binding.py::test_resolve_asker_class -- resolve_asker_class(<foreign guid>) with the default store raises AccessStateRefused 'not a well-formed POLICY# or RUNTIME# key: Key(pk=POLICY#TENANT#9999..., sk=tenant_firm, record_type=tenant_firm)' before any AWS call.",
        "Remedy measured, not applied (access_state.py is read-only for this cell): with acs.POLICY_RECORD_TYPES extended by 'tenant_firm' in-process, the same four files (test_asker_scope, test_asker_binding, test_asker_nochannels, test_mcpmsp_asker_firm) run 29 passed 0 failed, including the default-store read of an absent tenant_firm key returning None."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MS-t-1 item 1: firm_of reads the tenant_firm record 'through the existing store (app/access_state.py: strong reads; an unreachable store raises DependencyUnavailable)'; MS-t-1 AC2: the existing asker suites stay at >=23 passed, 0 failed; decomposition section 2 treats access_state.py as read-only for every cell and names the key as a fixed name.",
    "world_is": "The adapter cannot read or write a tenant_firm key at all. firm_of therefore raises AccessStateRefused for every GUID tid that is not Opal's own, and resolve_asker_class surfaces that as asker_store_unavailable for a real asker (fail closed, no data read; never read as 'unregistered'). AC2 reads 22 passed / 1 failed because one pre-existing test calls resolve_asker_class with the default store.",
    "notes": "Fails closed (no exposure), so hazard INERT; BLOCKING for the live hop (MS-d-1) and for MS-w-1's register_tenant write through the same adapter. The fix is one tuple entry in a file owned by NFRA_OPLGTW (a cell outside this round's paths), plus the writer-side operator_transact admission for that type if it differs. MS-t-1 deliberately does NOT treat AccessStateRefused as 'absent' (that would make every registered tenant read as tenant_denied and hide this cause). AC2 is recorded as measured, not met."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~1",
    "surfaced_at": "2026-09-30T09:40Z",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "id": "NFRA_MCPMSP-Z-W1-S2",
    "one_line": "The task order fixes the partition key and says the firm value is one of KNOWN_FIRMS ('inflection','cottonwood') but names no attribute for the firm in the tenant_firm record, and catalog_gate.KNOWN_FIRMS is actually ('49financial','inflection','cottonwood'); MS-t-1's reader and MS-w-1's writer must agree on both.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/NFRA_OPLGTW_CONTRACT.json key_namespaces.POLICY: 'one Microsoft tenant id -> one firm_id' (no attribute name is given).",
        "infra/aws/ec2/opal-gateway/app/graphql_plumbing/catalog_gate.py:40 KNOWN_FIRMS = (\"49financial\", \"inflection\", \"cottonwood\").",
        "infra/aws/ec2/opal-gateway/app/tenant_registry.py (this cell): firm_of reads attribute 'firm', accepts 'firm_id' when 'firm' is absent, Malformed when both are present and unequal; the firm must be in catalog_gate.KNOWN_FIRMS as written (so 49financial is accepted by the reader; the writer's own BAD-FIRM/LIVE_FIRMS refusals keep it from being registered)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MS-t-1 item 1: 'The firm value is one of catalog_gate.KNOWN_FIRMS (\"inflection\", \"cottonwood\")'; MS-w-1 item 1 refuses a firm not in (inflection, cottonwood) with BAD-FIRM.",
    "world_is": "KNOWN_FIRMS carries a third member, 49financial. The reader follows the named constant (three firms); the writer's own two-firm refusal is what keeps 49financial out of the registry. No firm attribute name is fixed by the contract or either order.",
    "notes": "Reconcile at the merge: if MS-w-1 writes the attribute as 'firm' the reader is exact; if it writes 'firm_id' the reader also accepts it. No change needed if so."
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
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~1",
    "surfaced_at": "2026-09-30T11:10Z",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "id": "NFRA_MCPMSP-Z-W1-S3",
    "one_line": "MS-t-1 AC2 cannot reach 0 failed: tests/test_access_state.py::test_ogd1_ac03 also asserts the literal POLICY key count is 3 (counts == {'POLICY': 3, 'RUNTIME': 6}), stale since email_deny landed; with tenant_firm admitted the count is 5, and the test file is outside this order's paths.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/ec2/opal-gateway/tests/test_access_state.py:293 `assert counts == {\"POLICY\": 3, \"RUNTIME\": 6}` where counts tallies every contract record type that is in acs.POLICY_RECORD_TYPES (:284-293).",
        "Measured in wk-NFRA_MCPMSP-1 after AMENDMENT 1 items 7-8 (access_state.py adds tenant_firm): `pytest tests/test_access_state.py` -> 1 failed, 6 passed; E {'POLICY': 5} != {'POLICY': 3}. The first assert (sorted(types) == sorted(RECORD_TYPES)) now PASSES; this is the next assertion in the same test.",
        "The literal 3 pre-dates email_deny (3e936f77bd, NFRA_OPLGTW OG-e-1, made the POLICY set 4): at CLOUD before this cell the set was 4 against a literal 3, so the test was red on its first assert AND would have been red here on this one; the amendment's 'test_ogd1_ac03 red at the amendment, the contract gap this cell closes' counted only the first.",
        "t1.AC2.sh on the branch: 'asker + adapter suites: 1 failed, 40 passed' -> RESULT: FAIL, exit=1. AC1 (7 passed) and AC3 (verdict=OK) PASS."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "MS-t-1 AMENDMENT 1 / AC2: the asker suites and the adapter's own suites (incl. test_access_state.py) pass with 0 failed and at least 41 passed once tenant_firm is added to POLICY_RECORD_TYPES; test_ogd1_ac03 is 'the contract-vs-adapter gap this cell closes'.",
    "world_is": "The gap this cell closes is two gaps: the contract-vs-adapter record-type set (closed: first assert passes) and a stale literal count in the test (3, now 5 with the contract's five POLICY types). tests/test_access_state.py is NFRA_OPLGTW's file and is not in this order's <paths>, so the worker cannot edit it.",
    "notes": "Fails closed, INERT. Remedy for the issuer: grant tests/test_access_state.py (one literal, 3 -> 5) or amend AC2's floor to exclude test_ogd1_ac03 (40 passed + this one named red); the adapter change itself is complete and measured (7 passed in test_mcpmsp_asker_firm.py incl. test_tenant_firm_admitted_by_adapter; test_email_deny.py and the other three asker suites all pass)."
  },
  {
    "id": "NFRA_MCPMSP-Z-S3",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~MS",
    "surfaced_at": "2026-09-30T12:20Z",
    "one_line": "MS-t-2's merge (@289bde0b4a) put the first local-module call (module opal_name) into infra/aws/terraform/opal-gateway, so every plan or apply there from a .terraform that has not run `terraform get` since fails 'Error: Module not installed'; the site-Z main tree was repaired by the issuer, other checkouts (the laptop, any linked worktree with its own .terraform) will hit it once.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Main tree, 2026-09-30 after the MS-t-2 drain: `terraform plan -target=aws_iam_role.gw` (TF_DATA_DIR = the main tree's .terraform) -> 'Error: Module not installed' x3; .terraform held providers/ and terraform.tfstate only (no modules/).",
        "Issuer's repair: `terraform get` in the main tree (local module path ..\\modules\\opal_name, no network) registered inf_firm_assume_policy_name, inf_firm_reader_policy_name, inf_firm_reader_role_name; the same plan then read 'No changes. Your infrastructure matches the configuration.'",
        "infra/aws/terraform/opal-gateway/mcpmsp_firm_roles.tf (CLOUD @289bde0b4a): three module blocks with source ../modules/opal_name."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Decomposition section 7 (iv): MS-t-2 builds and names; it creates no resource -- and by the cut's reading moves no other seat's workflow in the directory.",
    "world_is": "The directory's plans now need a one-time `terraform get` per .terraform. The failure is loud (a named Terraform error with an obvious one-command fix, no network), never silent, so INERT. Site-Z main tree: repaired.",
    "notes": "Remedy on any other checkout: run `terraform get` once in infra/aws/terraform/opal-gateway (local only). Carried to the drain-end read for the other fabric's seats that plan this directory (NFRA_OPLGTW, NFRA_MCPORTAL, NFRA_MCPINDEX)."
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
  },
  {
    "id": "NFRA_MCPMSP-Z-W3-S2",
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~3",
    "surfaced_at": "2026-09-30T10:50Z",
    "one_line": "build_package.py stages lambda_function.py byte-for-byte from the WORKING TREE, which on this Windows checkout is CRLF (git ls-files --eol: i/lf w/crlf) while HEAD's blob is LF, so the first apply shipped bytes that failed a2.AC2 (identical=False); the staged copy was re-written from `git show HEAD:` bytes and re-applied.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "a2.AC2.sh after apply 1: 'live sha256=72337fe88658 head sha256=7e80d4359859 identical=False register_tenant=True verdict=NO'; sha256sum of the working-tree file and of .build/staged/lambda_function.py = 72337fe88658...; `git ls-files --eol` = 'i/lf w/crlf attr/text eol=lf'; 381 CRLF pairs in the staged file, 0 in `git show HEAD:` (python bytes count).",
        "Every other staged file (10 of 11) equals its HEAD blob byte-for-byte; only lambda_function.py differed.",
        "Fix inside this order's .build path: wrote `git show HEAD:<path>` bytes over .build/staged/lambda_function.py (sha256 7e80d4359859 = HEAD), re-planned (0 add, 1 change, 0 destroy, code hash only), re-applied: CodeSha256 s+PDoMXpUn7YuMQqBThoLKezBNNIthyDhT8P75BN19A= -> nhz+dwJsDJLO9X3o1exvKdQ+OYE+PraxZSop2BJt9zI=; a2.AC2 then read identical=True verdict=OK. The writer's source file was not edited.",
        "Consequence for the next applier on a Windows checkout: a2-style 'deployed == HEAD' checks fail unless the staged handler is LF; apply 1's package was live for about 4 minutes and differed from HEAD only by line endings."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO MS-a-2 section 1 item 2: 'build_package.py stages the package' and AC2 expects the deployed lambda_function.py byte-identical to HEAD's.",
    "world_is": "The staged handler is a copy of the working-tree file, whose line endings follow the checkout (CRLF here), not HEAD's blob (LF, .gitattributes eol=lf); the order's steps, as written, produce a package AC2 refuses. Worked around in .build only."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~1",
    "surfaced_at": "2026-09-30T11:00Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_MCPMSP-Z-W1-S4",
    "one_line": "MS-d-1's release census names 10 files and AC2's allowed set is the same 10, but the order's own commit list (343534a883 and 2d15859595, MS-t-1's AMENDMENT 1 and 2) also writes app/access_state.py and tests/test_access_state.py; the narrow release tree therefore carries 12 gateway files and AC2 would print 'outside NFRA_MCPMSP's set 2'.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Release tree /c/tmp/ms-1-rel (branch rel-nfra-mcpmsp-r1-gateway, base 093fc247c6), staged, not committed: git diff --cached --stat lists 12 files under infra/aws/ec2/opal-gateway: the 10 of the census plus app/access_state.py (12 lines, commit 343534a883) and tests/test_access_state.py (3 lines, commit 2d15859595).",
        "org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round1/checks/d1.AC2.sh: allowed=(tenant_registry, firm_role, asker_scope, audit, config, test_mcpmsp_asker_firm, admin_tenants, test_admin_tenants, admin_api, deploy-to-ec2.sh) -- neither access_state file is in it.",
        "Both files are this project's own writes (MS-t-1 amendments; the order's section 2a names tests/test_access_state.py in its pytest run and lists both commits to carry)."
      ]
    },
    "spec_asserts": "TO MS-d-1 item 2 census: the diff names ONLY the 10 listed files, 'any other file: STOP, a BLOCKING row'; AC2 expects 'outside NFRA_MCPMSP's set 0'.",
    "world_is": "The release that carries the listed commits touches 2 more files, both the project's own and both needed (access_state.py is what admits the tenant_firm record; without it a firm asker is refused). The census and AC2's allowed set are stale against the MS-t-1 amendments. Nothing deployed.",
    "notes": "Fix is the issuer's: add app/access_state.py and tests/test_access_state.py to the census and to d1.AC2.sh's allowed set. Everything else of the prep is done in /c/tmp/ms-1-rel."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~1",
    "surfaced_at": "2026-09-30T11:00Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_MCPMSP-Z-W1-S5",
    "one_line": "In the release tree (PREV 093fc247c6 + the project's gateway commits) the amendment-2 pytest run reads 1 failed, 59 passed: tests/test_access_state.py::test_ogd1_ac03 reads org/standards/NFRA_OPLGTW_CONTRACT.json, which on PREV lacks tenant_firm (c2f5d5a071, the CTO's PRD commit, added it on CLOUD); with that one file from CLOUD the same run reads 60 passed.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd /c/tmp/ms-1-rel/infra/aws/ec2/opal-gateway && python -m pytest <the nine files of amendment 2> -q -> '1 failed, 59 passed' (FAILED tests/test_access_state.py::test_ogd1_ac03: 'Right contains one more item: tenant_firm').",
        "test_access_state.py: _CONTRACT = _HERE.parents[5] / 'org' / 'standards' / 'NFRA_OPLGTW_CONTRACT.json'. git log 093fc247c6..CLOUD -- that file: c2f5d5a071 only.",
        "Diagnostic only: the CLOUD version copied into the release tree, same nine files -> '60 passed'; the file was then written back to PREV's bytes (git status org/ clean)."
      ]
    },
    "spec_asserts": "TO MS-d-1 2a: the nine test files read 0 failed in the release tree; a failure is a BLOCKING row naming the file and the foreign commit it needs -- STOP, no deploy.",
    "world_is": "One test depends on a repo-side contract file outside the gateway directory, at a revision the release base does not have. The commit it needs is not another project's: c2f5d5a071 is this project's own PRD/contract commit. The shipped code is not affected (tests are not shipped); the amendment's gate as written cannot read 0 failed on this base. Nothing deployed.",
    "notes": "Options, issuer's: (a) the amendment accepts this one test as read against CLOUD's contract (60 passed with it); (b) the release tree also carries org/standards/NFRA_OPLGTW_CONTRACT.json (a non-gateway file, which AC2's 'gateway files' scope does not see). The worker took neither and stopped."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~1",
    "surfaced_at": "2026-09-30T11:00Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_MCPMSP-Z-W1-S6",
    "one_line": "Applying c19f86c295 onto PREV conflicts in app/config.py on adjacent context only: the commit's hunk sits beside MDPF_TAXSMA's TAXSMA_WORKBOOK_* block (present on CLOUD, absent on PREV); the conflict is resolved by keeping only this project's FIRM_ROLE_ARNS block.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git cherry-pick --no-commit c19f86c295 in /c/tmp/ms-1-rel: 'CONFLICT (content): Merge conflict in infra/aws/ec2/opal-gateway/app/config.py'; git show c19f86c295 -- app/config.py adds only _firm_role_arns() and FIRM_ROLE_ARNS; the TAXSMA lines in the conflict are unchanged context.",
        "Release tree after resolution: git diff --cached app/config.py = +13 lines _firm_role_arns(), +6 lines FIRM_ROLE_ARNS, no TAXSMA text. The commit also touches org/.../INVESTIGATION_v1.Z.md (modify/delete on PREV), left out of the release; the other commits were applied path-limited to infra/aws/ec2/opal-gateway."
      ]
    },
    "spec_asserts": "TO MS-d-1 2a: a cherry-pick conflict is a BLOCKING row naming the file and the foreign commit it needs.",
    "world_is": "The conflict is textual adjacency to another project's unreleased config block; the ported lines do not use it (60 of 60 tests read with the contract). Resolved by hand, recorded, not treated as a dependency.",
    "notes": "A judgment by the worker that the order's 'conflict is BLOCKING' aims at a dependence on foreign work, not at adjacency; S4 and S5 are what stop the release."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~1",
    "surfaced_at": "2026-09-30T11:45Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_MCPMSP-Z-W1-S7",
    "one_line": "The deploy script builds the dashboard from a nested $WORKSPACE_ROOT/mcportal checkout, and the release tree carries none: mcportal is a gitlink pinned at fa1ff9693b (a README-only commit) while the served artifact was built at a3bff71ffa, so the worker added a detached git worktree of the mcportal repo at a3bff71ffa inside /c/tmp/ms-1-rel and /c/tmp/ms-1-rb.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deploy-to-ec2.sh: MCPORTAL_DIR=$WORKSPACE_ROOT/mcportal; 'ERROR: no mcportal checkout' when package.json is absent. git ls-tree 093fc247c6 mcportal = fa1ff9693b ('initial README only'); EC2_MANIFEST services.opal-gateway.mcportal_commit = a3bff71ffa3f5c73aa0fb7ea1e7386434e233054; the MX-r-5 ledger and /c/tmp/mx-rb7 name the same pin.",
        "git -C <workspace>/mcportal worktree add --detach /c/tmp/ms-1-rel/mcportal a3bff71ffa (and /c/tmp/ms-1-rb/mcportal): the release build log reads 'built artifact opal-gateway-288fa78c93.tar.gz ... dashboard bundle mcportal@a3bff71ffa3f5c73aa0fb7ea1e7386434e233054'; the PREV rebuild from the rollback tree matched the live artifact 79 of 79 files."
      ]
    },
    "spec_asserts": "TO MS-d-1 item 2: the release tree is PREV plus cherry-picked commits; nothing names the nested mcportal checkout the deploy script requires.",
    "world_is": "The order's act cannot run from a bare release worktree: the script needs a mcportal checkout and the gitlink would pin the wrong (empty) commit. The worker pinned a3bff71ffa, the manifest's own mcportal_commit, so the dashboard shipped is the one already served. The two worktrees add entries to the shared mcportal module's worktree list (they are outside the repo tree of this order).",
    "notes": "The two mcportal worktrees /c/tmp/ms-1-rel/mcportal and /c/tmp/ms-1-rb/mcportal are left in place for the drain to remove; git worktree prune in the mcportal module clears them after the trees are deleted."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~1",
    "surfaced_at": "2026-09-30T11:45Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_MCPMSP-Z-W1-S8",
    "one_line": "The amendment-2 pytest run in the release tree modifies the TRACKED file infra/aws/ec2/opal-gateway/audit.jsonl (6 lines appended), which would make safe-ec2-deploy.sh stop at its 'Deploy with uncommitted changes? (y/N)' prompt; the worker rewrote the file from `git show HEAD:<path>` before the act (source path clean) and left nothing staged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C /c/tmp/ms-1-rel status after the suites: ' M infra/aws/ec2/opal-gateway/audit.jsonl' (6 insertions); safe-ec2-deploy.sh Step 1 runs `git diff --quiet $SOURCE_PATH` and prompts on a difference; after the restore `git diff --quiet infra/aws/ec2/opal-gateway` = clean and run 2 passed Step 1 without a prompt.",
        "The tarball build excludes audit.jsonl (--exclude='audit.jsonl'), so the dirt never shipped."
      ]
    },
    "spec_asserts": "TO MS-d-1 2a/5: run the suites, then the act from the release worktree; the order does not say the suites dirty the source path.",
    "world_is": "A test side effect on a tracked runtime log blocks the deploy wrapper interactively. No served effect.",
    "notes": "Any future release that runs the gateway suites in its release tree before the act meets the same prompt; the restore from git content is the one-line cure."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_at": "2026-09-30T14:00Z",
    "id": "NFRA_MCPMSP-Z-W4-S1",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~4",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "MS-a-3 item 0: provision-account.ps1's -Description literal (86 chars) shortened to 'Opal runtime agent (provision-account.ps1)' (42) in the nested opal_ai worktree, commit 47cfd4b on wk-NFRA_MCPMSP-4-opal_ai; t3.AC2 PASS after.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "t3.AC2.sh rc=0: 'default config -> PLAN: CREATE-USER Opal_Agent; msp config -> PLAN: CREATE-USER Opal_MSP' RESULT: PASS",
        "git -C opal_ai diff --stat: 1 file, 1 insertion, 1 deletion; literal was at line 116 of the nested worktree (old length 86, new 42)."
      ]
    },
    "spec_asserts": "TO MS-a-3 AMENDMENT 1 item 0: the description literal is a valid New-LocalUser -Description.",
    "world_is": "The literal exceeded the 48-char limit, failing binding before any act. Fixed in the nested branch only; the issuer drains it.",
    "notes": "The same literal exists at opal_ai DEV fd8ab8a line 101 until the drain lands; Opal_Agent provisioning is unblocked by the same change."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_at": "2026-09-30T14:30Z",
    "id": "NFRA_MCPMSP-Z-W4-S2",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~4",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "MS-a-3 item 0b: the nested opal_ai commit 61841f5 (verify-boundary run-as route) cannot be recorded as a parent gitlink bump -- safe-commit's gitlink-publication-check refuses it as NOT PUBLISHED and the worker may not push; the parent branch carries only the CLOUD merge (222e02f51c).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit.sh -- opal_ai rc=1: 'BLOCKED: gitlink-publication-check: opal_ai -> 61841f50ae is NOT PUBLISHED' (ls-remote rc=0, 9 heads tested).",
        "git -C /c/tmp/ms-4/opal_ai log: 47cfd4b (item 0) and 61841f5 (item 0b) are on wk-NFRA_MCPMSP-4-opal_ai, local only."
      ]
    },
    "spec_asserts": "TO MS-a-3 AMENDMENT 2: commit in the nested repo naming OA-t-2/OA-t-3; the issuer drains the commit.",
    "world_is": "The nested commit exists locally on its branch; the issuer drains it from the nested branch (as with 47cfd4b). No parent gitlink commit was possible. verify-boundary.ps1 run from the worker shell prints 'BOUNDARY: CANNOT-RUN-AS-ACCOUNT deny probe could not start as Opal_MSP: Access is denied', exit 5 (the measured shell restriction; replaces the false BREACH).",
    "notes": "The real AC2 run remains Andrew's after the drain."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_at": "2026-09-30T16:10Z",
    "id": "NFRA_MCPMSP-Z-W7-S1",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~7",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "MS-s-1: safe-apply's two OTHER plan-reading gates (tag-authz and tombstone) still re-plan the whole tree with none of the caller's args, so for a targeted or planfile apply they grade a plan the apply does not run; the TO scopes only the naming stage.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/safe-apply.sh tag-authz stage and tombstone stage (after the naming plan stage): each runs `plan -input=false -lock=false -out=...` then `show -json` with no -target/-var/planfile; unchanged by this cell per 'Keep every other gate as it is'.",
        "test_safe_apply_targeted.sh isolates them by fixture (tree has no default_tags; sandbox has no tombstone register), so its 5 of 5 PASS says nothing about them."
      ]
    },
    "spec_asserts": "TO MS-s-1 section 1: keep every other gate as it is; a targeted or planfile apply is graded on the plan the apply runs.",
    "world_is": "Only the naming plan stage renders the apply's own plan now. For a planfile apply the tag-authz and tombstone gates (when they run) plan the live tree afresh, and for a targeted apply they plan the whole tree; each can over-block a scoped apply on an unrelated resource or grade a different plan than the one applied. Not widened here.",
    "notes": "Candidate follow-on cell: factor one scoped-plan renderer (SA_PLAN_ARGS / SA_PLANFILE in safe-apply.sh) and feed it to all three plan-reading stages."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~1",
    "surfaced_at": "2026-09-30T18:30Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_MCPMSP-Z-W1-S9",
    "one_line": "MS-c-1 item 2: the host's /opt/opal-gateway/.env cannot be shell-sourced (set -a; . ./.env fails with exit 127), so the baseline capture parsed .env as KEY=VALUE in python before calling query_v0._fetch_capped; MS-dn-1's re-run must do the same.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SSM command fd5c458a-8cca-4993-8d22-2b26ed6ef983 Failed: './.env: line 14: ...: command not found', 'line 15: cot: command not found', 'line 23: opal_portal: command not found', 'line 33: arn:aws:iam::313476888478:role/gateway-inf-firm-reader-role}: No such file or directory', exit status 127.",
        "The python-parse run succeeded: 9 keys hashed, bytes equal the head-object ContentLength of each key; the recipe is in r2_c1_delta_baseline.json captured_on."
      ]
    },
    "spec_asserts": "TO MS-c-1 item 2: over SSM, cd /opt/opal-gateway, load .env, run .venv/bin/python calling app.query_v0._fetch_capped(key).",
    "world_is": "Unquoted values with spaces and a JSON value make .env a non-shell file; a shell load stops before python runs. No host write occurred in either attempt.",
    "notes": "The gateway reads credentials from the instance role, so the .env values do not affect the S3 read itself."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~1",
    "surfaced_at": "2026-09-30T18:30Z",
    "disposition": "UNDER_INVESTIGATION",
    "id": "NFRA_MCPMSP-Z-W1-S10",
    "one_line": "MS-c-1 item 1: the census denominator (call_sites_scanned=24) counts the order's boto3.client('s3') and get_object sites plus head_object, list_objects_v2 and non-literal client() sites, because opal_discover reads by HEAD and sprint_view lists; sprint_view.py (daily-reports/*) is a fifth reader beyond the three known at the cut.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python ast scan of infra/aws/ec2/opal-gateway/app/**: 24 sites in 11 files; census r2_c1_census.json readers[] has 5 entries, not_readers[] 6 files.",
        "opal-gateway-daily-reports-read grants GetObject on opal-data-portal-v2/daily-reports/* and config.DAILY_REPORTS_BUCKET defaults to opal-data-portal-v2."
      ]
    },
    "spec_asserts": "TO MS-c-1 item 1: call_sites_scanned counts boto3.client('s3'...) and .get_object( sites; known readers are three.",
    "world_is": "A narrower count would omit the HEAD and list reads that the same IAM grants permit. The sprint_view reader reads daily-reports/, which is not firm data, so it falls outside the Deny's keys.",
    "notes": "The Deny keys platinum/mdpf/{firm}/* do not touch daily-reports/*."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_at": "2026-09-30T15:30Z",
    "id": "NFRA_MCPMSP-Z-W3-S3",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~3",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "MS-sg-1 AC2 cannot be met as written: the gate refuses an absent sender address (asker_sender_domain, per the TO), and every existing asker/adapter test fake returns chat members with no `email`, so 17 of 48 existing tests fail; the existing tests are outside this order's <paths>.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "e2g.AC2.sh at df4d410b66: 'asker + adapter + round-1 suites: 17 failed, 31 passed' RESULT: FAIL exit=1; at parent 0e3760b480 the same script read 48 passed, RESULT: PASS.",
        "Cause isolated: the same six suites run with sender_gate.check patched to return None (scratch plugin, not committed) read '48 passed'; the failures are all code asker_sender_domain.",
        "infra/aws/ec2/opal-gateway/tests/test_asker_binding.py:89-90 members fake returns {userId, tenantId} only; test_asker_scope.py, test_asker_nochannels.py and test_mcpmsp_asker_firm.py return no /members value at all (their default branch is {'chatType': 'oneOnOne'}), so sender_address() is None."
      ]
    },
    "spec_asserts": "TO MS-sg-1 BOUNDS 2 / AC2: the existing asker/adapter suites stay green (>=48 passed, 0 failed) while an absent sender address is refused asker_sender_domain.",
    "world_is": "Both cannot hold: a gate that refuses an absent address fails every existing test whose fake carries no member email. Not made to pass: treating an absent address as a pass would fail OPEN for any sender whose member record hides its email. Remedy for the issuer: amend those suites' fakes to carry an `email` per member (opalinvest.com for the Opal tenant, the firm's domain for a firm tenant) in a TO whose <paths> include them, or amend AC2.",
    "notes": "AC1 and AC3 pass. Nothing is deployed; the branch is local."
  },
  {
    "project": "NFRA_MCPMSP",
    "fabric": "site-z",
    "surfaced_at": "2026-09-30T15:30Z",
    "id": "NFRA_MCPMSP-Z-W3-S4",
    "surfaced_by": "0.9.0_WK_NFRA_MCPMSP~3",
    "disposition": "UNDER_INVESTIGATION",
    "one_line": "The commit-time naming gate (ENFORCE) refused app/sender_gate.py as written to the TO: the firm ids 49financial / inflection / cottonwood and the domain 49financial.com are 'hand-kept carriers'; sender_gate.py now reads the firm ids from catalog_gate.KNOWN_FIRMS and builds each domain as id + tail.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "2.0.0_SA_COO~MS",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit.sh first attempt: 'naming-gate NAMING REFUSE app/sender_gate.py:23 49financial -> lookup(49financial)' (also :24, :25, :27), NAMING-GATE: REFUSE 5 graded; commit aborted, files unstaged.",
        "app/sender_gate.py at df4d410b66: ALLOWED_DOMAINS built from catalog_gate.KNOWN_FIRMS zipped with tails (.com, wealth.com, mail.com); tests/test_mcpmsp_sender_gate.py::test_allowed_domain_matching_tenant_served pins the exact four domain->firm pairs."
      ]
    },
    "spec_asserts": "TO MS-sg-1 build item 1: ALLOWED_DOMAINS written as the four domains mapped to firm.",
    "world_is": "The mapping is derived by KNOWN_FIRMS position, so a reordered or extended KNOWN_FIRMS moves which domain maps to which firm; the pinned test fails first. A tidier carrier (an R20 exception or a registry row for the four domains) is outside this order's paths.",
    "notes": "The gateway app cannot import lib/opal_naming (not in the deployed tree), so lookup() was not an option."
  }
]
```
