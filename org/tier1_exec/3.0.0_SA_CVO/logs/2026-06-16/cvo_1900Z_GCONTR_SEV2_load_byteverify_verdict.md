# CVO verdict — NFRA_GCONTR SEV2 ceiling load byte-verify (peers+aum) — 2026-06-16 ~19:00Z

**archetype:** VALIDATE

## Verdict: GREEN — peers+aum loaded byte-correct on Nessie main; benchmark unchanged; no regression.

AE loaded the peers+aum SEV2 rows in-VPC (combined load, prefix-aware image fe645e103). I verified **independently against the LIVE Iceberg table** — NOT AE's StaticTable self-report (CLAUDE.md NEVER #5): pyiceberg `StaticTable.from_metadata` on the current S3 metadata
`graph_contracts_bccbceec.../metadata/00000-a2b5eb5e-25fd-495f-90f0-7211bc6c0e54.metadata.json`
(latest by timestamp; 3 rows = the post-load HEAD), diffed vs my authored YAML.

| Row | period_defs | values byte-match | forbidden_writers | models | canonical_writer | ratified_by | ratified_at |
|---|---|---|---|---|---|---|---|
| benchmark (SEV1) | 11 keys ✓ | (unchanged) | ✓ | [UST,ST,INT,LTC,LTA] | yang-pipeline-lambda-role | [Andrew] | `6f21c75c…` **UNCHANGED** |
| peers (SEV2) | 9 keys ✓ | **TRUE** | `[]` ✓ | [UST,ST,INT,LTC,LTA] ✓ | yang-pipeline-lambda-role | [CTO,COO] | `a7bc0aed…` (real hash) |
| aum (SEV2) | 4 keys ✓ | **TRUE** | `[smartx-exporter-role]` ✓ | 7 (incl 2 blends) ✓ | smartx-ingestion-lambda-role | [CTO,COO] | `a7bc0aed…` |

Confirmed live:
1. All 3 rows present; peers+aum period_defs keys AND values byte-identical to my YAML.
2. ratified_at = real Nessie hash `a7bc0aed…` (the `PENDING-CTO-COO-SIGNOFF` placeholder was correctly replaced — the prefix-aware gate fix `fe645e103`, which my peers row first surfaced, works **live**).
3. benchmark ratified_at `6f21c75c…` + 11 period_defs PROVABLY UNCHANGED — the whole-file load did NOT regress the live SEV1 row (already-present guard confirmed live). The seam I flagged is closed with evidence.

## SCOPE PRECISION (do not overclaim)
This byte-verify confirms **contract-row integrity** (the structural value-limb = period_defs loaded present + exact). It is **NOT** the **runtime value-check assertion** (does the SERVED 1M actually equal trailing-1-calendar-month, etc.) — that is the separate CVO-owned TO-3 deliverable (the codified BMKAUD WS-2 check), still pending. Post-06-17: aum's `smartx-exporter-role` tripwire + NNA's policy limb go Q2-ENFORCED on AE's EC2-WRITES derive fix → I run the independent nightly re-verify then.

## TO-3 status after this verdict
- benchmark (SEV1): live + ratified.
- peers + aum (SEV2): live + ratified + **byte-verified** → SEV2 v1 ceiling DONE.
- REMAINING: headline (SEV1, Andrew sign-off + AUA value-contract); NNA (SEV1, value-limb authorable, policy-limb 06-17); the runtime period_defs value-check assertion.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| pyiceberg StaticTable (live Iceberg read) | independent read of live graph_contracts (not self-report) | 3 rows; peers+aum byte-match YAML; benchmark unchanged |
| aws s3 ls (metadata discovery) | find current table metadata.json | a2b5eb5e (18:53Z) = post-load HEAD |
| schema-conformance validator (prior pass) | YAML source-of-truth for the diff | 3/3 conformant |

RAVC: CLOSE -> AE (load byte-verified GREEN); verify-gate PASS -> COO. AE doc-sync of the schedule change committed in-lane c1148c100.

— 3.0.0_SA_CVO
