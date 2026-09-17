```json
{
  "project": "NFRA_MCPINDEX",
  "directive": "D9",
  "fabric": "laptop",
  "prd_version": "v0.1",
  "step": 4,
  "brief_ref": "docs/briefs/opal-mcp-tool-index-brief-20260917.md@826ac6925a",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8",
    "FWD-9",
    "FWD-10"
  ],
  "status": "DRAFT"
}
```

# NFRA_MCPINDEX - the Opal MCP tool index: every Opal data property answerable in Claude, from one catalog

## Authority and project arc

Author and accountable CTO: `1.0.0_SA_CTO`. Directive D9, Opal Workflows; macro NFRA; execution fabric laptop.

Andrew commissioned the scope at the `4.0.0_SA_CRO` terminal on 2026-09-17 and answered five cards there, all verbatim in
the brief: tool names follow the LGIC naming canon; the catalog is versioned in S3; the project sits under D9; Opal staff
only, beta one person at a time; the portal's precomputed tables are read as they are, while `opal-data-assets` silver is
queried live. He confirmed the ten endpoint outcomes at this terminal on 2026-09-17 ~19:0xZ ("1 approved"), recorded at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260917_190xZ_OPEN_CALLS_SEVEN_ANSWERED_SEAT_SEQUENCE_IRPT_MCPINDEX_TAXSMA.md`
@57a15b2bbe.

The product: a staff member signed in with their Microsoft account asks Claude a plain-English question about Opal's own
data and gets an answer from the right source, with its date, its scope and its limits stated. A small discover family
indexes everything else, so the model is never guessing which tool to call. **The problem this exists to solve is stated in
his words: the official plugins are poorly indexed, and we will not have that problem.**

The header stays DRAFT until both halves are signed at L4-R. The author signs neither half.

## Scope and evidence boundary

**This project owns:** the catalog (its schema, its versioned S3 home, its generation into the Gateway), the discover
family, the per-property purpose-built tools, the generalisation of the typed query engine beyond Schwab, one fenced read
role per property, and the per-property analysis that decides which questions become tools.

**It relies on and does not change:** the Gateway's sign-in, tiers, guard and audit; `app/refs/DATA_CATALOG.yaml` and its
one writer; the Schwab query engine and grant model built by NFRA_OPLGTW; the silver tables and their producers; the
portal's precomputed tables and their publishers; the naming canon and registry.

**Explicitly NOT this project's:** enabling the five Schwab tools in deployment (NFRA_OPLGTW's act); the admin screen that
grants access (the mcportal brief); new precomputed tables (none are asked for); partner or client access (zero, under his
standing 2026-08-20 ruling); Tax SMA tools (until D9's tax work lands); any new vendor egress (YCharts and Bloomberg stay
on his per-use word).

**Evidence boundary.** The brief measured the repository only: no AWS state was read, table sizes and query timings over
silver are unmeasured, and the per-property "common questions" are not enumerated anywhere yet. **Every capacity claim in
this PRD is therefore DESIRED until a cell exercises it**, and the first analysis cell of each property carries the
measurement.

## ENDPOINT (step 2, /endpoint --forward)

The ten outcomes are `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_MCPINDEX_ENDPOINT_FORWARD_20260917.md` @9da61cab00,
confirmed by Andrew ~19:0xZ. They are carried here unchanged, in one line each; the endpoint document is the text that
governs.

| id | the outcome, in one line | bar |
|---|---|---|
| FWD-1 | a staff member who does not know which system holds a fact is routed correctly on the first try | EXERCISED, cold, by a non-author |
| FWD-2 | for any figure the portal displays, Claude returns the portal's own number and as-of date | EXERCISED per surface |
| FWD-3 | positions, balances and transactions at either Schwab master, from silver | EXERCISED by a granted person |
| FWD-4 | the same question classes for Black Diamond, Orion, Eclipse and SmartX | EXERCISED per property, after its analysis |
| FWD-5 | the ETFs -- holdings, net assets, daily NAV -- per fund | EXERCISED per fund |
| FWD-6 | an uncatalogued question still gets a safe typed answer, and routing prefers the purpose-built tool | EXERCISED, both halves |
| FWD-7 | one client or household seen across custodian and platform | EXERCISED on one real client |
| FWD-8 | long history and live market data on demand | EXERCISED, one answer per half |
| FWD-9 | Andrew admits staff one at a time; each sees only what he granted | EXERCISED: one admission, one removal |
| FWD-10 | adding the next property is one catalog entry plus a tool | EXERCISED on the next property, timed |

## CONTRACTS

**C1 -- ONE catalog, versioned, one writer.** The catalog extends `app/refs/DATA_CATALOG.yaml` (v0.3, 36 served-data rows)
and keeps its single writer `emit_catalog_v02.py`. A second catalog is forbidden, which is the D6 PRD's standing bar
(`D6_OPAL_ANALYST_GRAPHQL_PRD.md:57,102`). Its versioned home is an S3 address produced by `lib/opal_naming.py address()`
and never typed (Rule 30). Each entry carries: business meaning, example questions, grain, freshness field, firm-scope
rule, never-sum rules, producer, and the tools that serve it.

**C2 -- a tool ships only with a catalog entry and a safety classification.** A tool with neither does not ship, and the
mechanism is a refusal, not a review note. The live defect this closes is named in the brief: `read_teams_attachment` is
enabled today and denied to every tier because it has no classification.

**C3 -- tool naming.** `{system}_{function}[_{qualifier}]`, `system` a key of `infra/logic/registry/systems.json`,
`function` a base-form verb, **scope (firm or master) always an explicit argument validated against `scopes.json`, never
folded into the name**; the cross-property discover tools sit under the reserved `opal` system. **The schema-grading call:
`NAMING_SCHEMA.json` v1.10 does not grade MCP tool names (`not_covered` is silent on tools). This PRD RULES that the rule
above binds this project's tools by criterion, and that GRADING it in the schema is a LGIC_NAMING schema bump this seat
raises there -- never a rider on LGIC_ENFORCE, and never a second naming authority here.**

**C4 -- the answer envelope.** Every answer states its master or firm scope, its as-of date, whether it is complete or was
cut short, and its source dataset. "No data for that date" is never rendered as zero. Masters and firms are never summed
across, in any phrasing.

**C5 -- portal parity.** A portal-backed tool reads the same precomputed table the portal reads. A disagreement between
Claude and the portal on the same figure and date is a DEFECT of this project, not a caveat, and its acceptance is a
side-by-side read per surface.

**C6 -- the typed query.** Filters, group-bys and aggregates as a structured object; never raw SQL from a caller; hard
caps on scanned bytes, rows and time; the response states date, completeness and truncation. Its additivity and grouping
rules are enforced ON THE CALL PATH, with a mutant control -- the standing bar this seat set on NFRA_OPLGTW (R-OG-13,
R-OG-15) after two criteria there passed against a module nothing called, and two tests asserted the defect.

**C7 -- isolation.** One read role per property, fenced to exact silver prefixes, generated from the registry under
LGIC_ENFORCE's builders. A staff member granted one master or firm cannot be shown another by any phrasing; the grant
model extends NFRA_OPLGTW's rather than forking it.

**C8 -- the beta roster.** Admission is one person at a time, Opal staff only, controlled by Andrew. Until the mcportal
Entitlements screen exists, the operator command is the path. Removal takes effect without a redeploy.

## SURFACE MANIFEST

| id | surface | what it is | depends on | outcomes |
|---|---|---|---|---|
| S1 | the catalog | the extended schema, its S3 versioned home, its generation into the Gateway | `DATA_CATALOG.yaml`, `address()` | FWD-1, FWD-10 |
| S2 | discover tools | the small always-loaded family that answers "what do we have, how fresh, which tool next" | S1 | FWD-1 |
| S3 | portal tools | per-surface readers over the portal's precomputed tables | S1, the publishers | FWD-2 |
| S4 | custodian and platform tools | per-property purpose-built tools over silver (Schwab, Black Diamond, Orion, Eclipse, SmartX) | S1, S6, S7 | FWD-3, FWD-4 |
| S5 | ETF tools | per-fund holdings, net assets, NAV | S1, S7 | FWD-5 |
| S6 | the typed query engine | generalised beyond Schwab, capped, enforced on the call path | NFRA_OPLGTW's engine | FWD-6 |
| S7 | read roles and grants | one fenced role per property; the grant model extended | LGIC_ENFORCE's registry and builders | FWD-3..FWD-5, FWD-9 |
| S8 | the per-property analysis | the written record of what people actually ask, per property | -- | FWD-4, FWD-5, FWD-10 |
| S9 | entity resolution | the stated matching rule, its precision and recall, its unmatched list | S4 | FWD-7 |
| S10 | on-demand paths | the long-history substrate and the vendor reads in the same index | S1, S6 | FWD-8 |
| S11 | the beta roster | admission, removal, per-person tool lists | S7, the Gateway's identity | FWD-9 |

## Ground truth measured at authorship (2026-09-17, repository only)

- 49 tools registered, 44 enabled; none answers a question about Opal's own data (35 Microsoft 365, 6 YCharts, 1 portal
  upload, 2 estate graph).
- The portal catalog and its gate exist and are unreachable as tools; five business tools were designed and parked.
- The live-query pattern exists for Schwab: five tools, a typed grammar, DuckDB in a capped child process, per-person
  grants, a response envelope -- built, tested, NOT enabled in deployment, and exposing three `dim_*` tables only.
- Silver holds all firms in one bucket, split by key prefix; no Glue or Athena sits over silver or gold.
- Entity resolution is parked; `read_teams_attachment` is the live unclassified-tool defect.

**Not measured, and named as such:** AWS state, table sizes, object counts, query timings, and the per-property common
questions.

## BRIEF COVERAGE

All ten of the brief's outcomes map to FWD-1..FWD-10 one-to-one. Its nine preconditions (Part V) land as: C1 (catalog
schema and writer), S8 (per-property analysis), C7 (roles and grants), C2 (classification), the NFRA_OPLGTW dependency
named at FWD-3, S9 (entity resolution), S10 (long-history substrate), the standing integration checklist, and C8 (the
roster). Its six non-claims (Part VII) are carried into the evidence boundary above rather than silently dropped.

## Acceptance matrix

| id | acceptance | outcome |
|---|---|---|
| A1 | a named cold question set, asked by a non-author, routes correctly; the count routed over the count asked is printed, every wrong route listed | FWD-1 |
| A2 | per portal surface, one side-by-side read: figure and as-of date identical, zero disagreements, denominators printed | FWD-2 |
| A3 | per Schwab question class, a live transcript with row counts reproduced by a second instrument | FWD-3 |
| A4 | per property: the analysis record, the tool list it produced, one live answer per tool class | FWD-4 |
| A5 | per fund: one live answer per question class compared with the served artifact | FWD-5 |
| A6 | the typed query refuses an unsafe shape, states truncation, and the routing set prefers purpose-built tools | FWD-6 |
| A7 | one client answered across two systems, with the match rule, its precision and recall on a named sample, and the unmatched list | FWD-7 |
| A8 | one long-history answer and one market-data answer, each naming its substrate and its cost | FWD-8 |
| A9 | two sessions (admitted, not admitted) with their tool lists, one refusal transcript, one removal with its timestamp | FWD-9 |
| A10 | the next property added as one catalog entry plus a tool, timed; a planted unclassified tool is REFUSED | FWD-10 |
| A11 | every tool that ships carries its catalog entry and classification; the count of tools without either is zero, denominator printed | C2 |
| A12 | every tool name is generated or validated against the C3 rule; a hand-typed non-conforming name is refused | C3 |

## Canonical handoff

L5 (the decomposition) is `2.0.0_SA_COO`'s, on a lane `0.0.0_AB_MSTR` seats when one frees. **Andrew's seat order of
2026-09-17 puts this project SECOND, after IRPT_BCKEND and before MDPF_TAXSMA.** The first cells are the catalog schema
(S1) and the per-property analysis for the first property (S8), because every other cell reads from them. FWD-3's live
exercise waits on NFRA_OPLGTW enabling its Schwab tools -- that project's act, and this project's cells prove their own
half meanwhile.
