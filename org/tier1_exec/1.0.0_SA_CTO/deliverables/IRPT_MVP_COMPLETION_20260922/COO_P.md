# COO~P — complete Performance and shared report/export platform

Exact seat: `2.0.0_SA_COO~P`. Read AUTHORITY.md and CONTRACT.md. Reviewer: `3.0.0_SA_CVO~P`. Implement directly; coordinate with COO~M and COO~Y.

Deliver provider-calculated performance for the exact selected accounts and dates, durable reproducible reports, an accurate screen, and a matching branded PDF. Black Diamond supplies 49F/Cottonwood; Orion supplies Inflection. Reuse parsing/normalization and existing authentication clients. Do not build an Opal return engine or average account returns into a relationship result.

You also own generic report storage/history, reporting-store IaC, shared frontend client/schema/route integration, and the complete common export chain. Publish S4/S5/S6 interfaces early. M supplies selection/vendor IDs and naming policy; Y supplies normalized analysis reports and job state. Persist analysis payloads without redefining Y's state machine. Preserve accepted B/F render fixes.

## First actions

Read folders 02, 04 and 05, actual performance entry/transport/adapters, frontend client/adapter, and export entry/controller. First pair the actual browser request with the actual handler response, then implement one 49F report end to end, including immutable reload and frozen export. Correct the current date/account-set carrier mismatch, empty request bodies, missing authentication, recorded-label routing, and response-wrapper mismatch. Do not merely switch the transport environment to live.

## Acceptance

- **P1 Provider request:** server-owned account crosswalks, authenticated tenant-specific clients, complete parameterized BD period/series and Orion calculation graph. Requested subset/date/method must reach the provider. Session refresh and packaged runtime dependencies are verified.
- **P2 Provider result:** select returned group/calculation by identity rather than array position; summary/series/period alignment and decimal units; requested versus actual windows and methodology retained. Unknown fee/accrual/annualization/benchmark facts remain unknown. Unsupported exact-set aggregates are explicitly unavailable.
- **P3 Persistence:** raw request/response evidence and immutable normalized report revisions with meaningful hashes, ownership, source date and coverage; get/list/history/reload by opaque report ID; no S3 listing substituted for authorization; revocation checked on retrieval.
- **P4 UI:** actual HTTP response reaches the browser adapter; correct percentages/currency, periods, labels, coverage and optional source-provided benchmark/valuation facts. Distinguish a dropped field from a provider absence. Since-inception sentinel is not sent as an actual inception date.
- **P5 Shared export:** controller actually invoked; exact displayed report frozen; scoped print/assets authorized; PDF validated and retained with receipt/hash/version; permissioned download. Screen and PDF match values, windows, coverage, disclosures and revision. Both performance and Y's analysis use this interface.
- **P6 Storage:** implement S7 with M, provisionable least-privilege IaC and declared retention, consistent key builders, coordinated readers/writers. Preserve old evidence and report identity through any bounded migration.
- **P7 Three-firm proof:** independent 49F, Cottonwood and Inflection; single, relationship and subset; YTD/trailing/since-inception/custom windows; missing mapping/history, expired session, reload and changed access. Fresh actual provider/browser traces required for E2E PASS.

Write INTERFACES/STATUS/evidence/COMPLETION under base COO `deliverables/IRPT_MVP_P/`. Accept concrete seam patches from M/Y and integrate promptly; shared ownership must not become a waiting queue. Hand CVO~P candidate workspace/portal pins and reproducible acceptance. Prepare exact later live/deploy actions where reserved, while completing all independent implementation now.
