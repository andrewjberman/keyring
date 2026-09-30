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
  }
]
```
