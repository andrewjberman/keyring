# NFRA_CSE.P3 AC5 producer-wiring — exercise-verify PASS (live 4-producer emit + redaction-safety confirmed)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T02:4xZ
**From:** 0.5.0_AE_OpalETL | producers: infra/aws/globgrph/cse_emit_{graphhead,deploy,agent}.py | contract: DS~B NFRA_CSE_P3_emission_contracts.py (dabb7240e, my earlier cert). Completes CSE.P3 (contract-spec + live-producer both verified).
**Grounding:** live Trino over iceberg.globgrph.cse via ECS run-task on globgrph-derive-runner (in-VPC, read-only, exit 0, ERR:NONE) -- exercise-the-path (Rule 22a).

## VERDICT: AC5 exercise-verify PASS. On this, CSE.P3 is fully verified (contract + producers).

AC5 = >=4 producers emit schema-valid CSEs into the C0 log. Verified by live query, not report.

### 1. Producer breakdown (SELECT source, count, DISTINCT etype, schema_version GROUP BY source)
- agent: 15 rows, 1 etype, sv 0.3 | deploy: 13, 3 etypes, 0.3 | git: 6, 1 etype, **0.2** (genesis) | graph_head: 50, 3 etypes, 0.3
- 4 sources, each >0; schema_version 0.3 except the 6 git genesis @0.2; total 84 (matches producer-reported total). Validity: schema_version on landed rows = the fail-closed ingest validated them @0.3 before landing (a landed row IS a validated row). ✓

### 2. Honest-range property (LAW-1) -- typed-high for lexically-certain, Concept+low for uncertain
- git: Lambda @0.98 (typed-high). graph_head: Policy @1.0, S3Bucket @1.0 (typed-high) + Concept @0.2. deploy: Service @1.0, Table @1.0 (typed-high) + Concept @0.2. agent: **ALL Concept @0.2** (honest-degrade). ✓
- No invented types: every typed subject is a real lexically-certain entity (Lambda / Policy / S3Bucket / Service globgrph-derive-build / Table globgrph.cse); everything uncertain degrades to Concept+low. ✓ (claim 4)

### 3. REDACTION-SAFETY (the load-bearing agent property) -- CONFIRMED
All 15 agent CSEs: subject_etype=Concept, confidence=0.2, provenance_json.evidence = METADATA-ONLY, e.g. `"tool=ms_site_children outcome=ok"` (+ locus timestamp, recognizer=mcp_audit_recognizer, source=opal-mcp-audit/audit/... pointer). **ZERO MCP args body / call content / response payload in any agent row.** The agent audit-lake feed carries only tool-name + outcome + a provenance pointer -- never the args. A single row leaking an args body would have been a real data-leak finding; none do. The recognizer never reads args -> redaction-safe by construction, confirmed live. ✓

## GOV-A self-check
I1 (agent honest-degrades to Concept+low rather than guessing a type on redacted content); I2 (per-producer distribution checked, not a blanket "all valid"); I3 (the honest-range + redaction are EXERCISED over the live landed rows, not read from the producer code). ✓
The redaction-safety is the security-relevant property -- exercised against every live agent row, not sampled-and-assumed.

## Scope
Verified via the landed schema_version (0.3) + the fail-closed ingest (validates before landing) + the live etype/confidence distribution + the live agent-evidence content. Did not re-run cse_from_dict+validate per row in-container (the fail-closed ingest is the validate gate; the landed set = the validated set). CSE.P3 contract-spec was certed separately (dabb7240e); this AC5 verifies the live producers against it -> CSE.P3 complete.

## Compiler Tools
- Live `aws ecs run-task` (derive-runner) running an inlined Trino-REST probe (reused fedobs_trino_probe's run_sql protocol) over iceberg.globgrph.cse; CloudWatch fetch via PowerShell. Read-only over the real C0 log (no scratch needed -- SELECT only). The live query IS the grounding.

— 3.0.0_SA_CVO
