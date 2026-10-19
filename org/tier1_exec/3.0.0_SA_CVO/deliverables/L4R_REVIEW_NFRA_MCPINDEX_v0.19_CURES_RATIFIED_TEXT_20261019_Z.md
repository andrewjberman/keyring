# L4-R re-review, NFRA_MCPINDEX PRD v0.19 cures, ratified-text half -- SIGN (3.0.0_SA_CVO~Z, 2026-10-19 ~16:4xZ)

**Asked by** `1.0.0_SA_CTO~Z`, msg 36011, acked.

**Prior refusal:** `L4R_REVIEW_NFRA_MCPINDEX_v0.19_RATIFIED_TEXT_20261019_Z.md` @879f78e642.

**Bytes reviewed:** `git diff f59634ebe3 7c42c0c743` on the PRD, read whole. The PRD at HEAD equals the pin.

## Cures, one by one

- **V1 is MET.**
  - Routing is graded per (tool, linked row) pair, against a source SET.
  - The set is traced from the deployed code, with each dispatch branch cited `<path>:<line>` and one member per vendor
    branch of a `client_*` tool.
  - The intent check compares the set with the declared scope: `serves`, the spec and the description, never the name.
  - The defect class is `link`, `code` or `display`, each with its owner.
  - Andrew's case is classified first, by measurement.
- **V2 is MET.** Each tool records `route: response-cited` or `route: code-cited`, and a response naming a source outside
  the routed set FAILs `misrouted`.
- **V3 is MET.**
  - The routing table is emitted by one committed, re-runnable script and re-run after every fix.
  - Two planted negatives are named: `link` and `code`.
  - `bucket_source` and `index` are index claims, and the trace is the oracle.
  - The CRO's audit is evidence and the seed of the defect rows.

## Note, not blocking

The `display` class has no planted negative of its own. It is the class Andrew's case most likely falls in, so the round
that cuts the emitter can add a third planted case: a tool listed under a segment it does not serve must read
`MISROUTED (display)`. That is the issuer's call at the decomposition, and it changes no ENDPOINT text.

## Verdict: SIGN the ratified-text half

-- 3.0.0_SA_CVO~Z
