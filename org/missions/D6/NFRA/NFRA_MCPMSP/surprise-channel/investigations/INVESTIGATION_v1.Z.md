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
  }
]
```
