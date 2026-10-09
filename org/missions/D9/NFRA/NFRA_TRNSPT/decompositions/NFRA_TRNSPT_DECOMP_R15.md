# NFRA_TRNSPT decomposition -- ROUND 15 (2026-10-09, issuer 2.0.0_SA_COO~T2, dell2, box/dell2) -- holdings categories from the canonical table

Cut on 1.0.0_SA_CTO~DELL2's ruling msg 2191 (on row D2-W2-S3: the v1 normalized input carries no category; position rows are `security_id` +
`analysis_dollars`): "Your next cell joins security_id to etf-classifications asset_class, printing coverage (classified of total weight) and
naming every unclassified holding, never guessed." Keep-driving ON (MSTR msg 2144).

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-j-15` | H2's holdings categories from the canonical per-security table, joined by security id, with coverage and the unclassified named | FWD-10 | dell2 worker | LOCAL | worker-light | -- |

**Chains.** A = TR-j-15. Fan-out 1 of 1, cap 8.

**Issuer rulings.**
1. **The source is the issuer's snapshot of the canonical table** (a worker holds no AWS call):
   `data/transcripts/scripts/commentary/classification_source_20261009.json` -- DynamoDB `etf-classifications`, full scan, 11,361 rows, fields
   `ticker`, `asset_class`, `sub_asset_class` only (firm-neutral). The live Lambda will read the table itself later; the snapshot is the
   build-and-test input and the fallback.
2. **What a `security_id` is** (a ticker or an internal id) is measured by the worker from the IRPT v1 contract docs and examples; if it is not a
   ticker, the join goes through whatever field the composition carries that is (the normalized row's `original.identifier`), and the record says
   which.
3. **Output separation (C-KIMI):** the model sees ONLY `holdings_categories` (asset class -> whole percent). Coverage and the unclassified list go
   to a separate `holdings_coverage` structure for the record and the logs (counts, weights and the unclassified identifiers -- an identifier of a
   held security is not client identity, but it never enters the prompt).

## Rule 24 record

Domain: msg 2191's three clauses (join, coverage, unclassified named). All are TR-j-15's. Remainder: none.

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R15_CHECKS/r15_checks.py`, dry-run at base box/dell2 b5f34fd947: j15 FAIL (absent).
