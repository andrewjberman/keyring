# PROPOSED RULE (for the CTO to land): GOLD IS THE OPAL SHAPE -- the adapter layer

**Author:** `4.0.0_SA_CRO`, 2026-09-30. **Order:** Andrew-direct, verbatim in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260930_06xxZ_REPORTING_DASHBOARD_TWO_BRIEFS_SCOPE_ANSWERS.md` (addendum, message 3, @3b6d4b4b71), and his instruction "that should be in there somewhere persistently" (this turn).
**Status:** PROPOSED. This seat lands nothing in a locked or doctrine file. The CTO's lane owns `docs/doctrine/CLAUDE_ANNEX.md` section 7 and `infra/logic/02_DOCTRINE.md`; a law edit has three surfaces (commit, same-turn broadcast, push state).

## The rule text (imperative, mechanism, pointer, one non-application)

**GOLD IS THE ONE OPAL SHAPE, AND THE ADAPTER LAYER.** Bronze holds each source's raw shape; silver holds it typed and de-duplicated in parquet, still in
that source's own shape; **gold is where every firm's or vendor's shape is coalesced into ONE Opal shape.** A firm-specific column does not survive into gold;
where a firm lacks a field, gold carries it null with a coverage marker, never as a firm-specific variant of the table.
Mechanism: each gold table has ONE schema contract file under `org/standards/` (`<TABLE>_GOLD_CONTRACT.json`: column names, types, nullability, coverage-marker
columns, the Opal enum sets); every firm adapter writes exactly that schema, and a conformance check compares each written partition's schema to the contract
(same hash across firms is the pass). Pointer: `docs/doctrine/CLAUDE_ANNEX.md` section 7 (rules 17, 17a, 17b) and `infra/logic/02_DOCTRINE.md` (tier table, A5 FORMAT).
Non-application: a gold table with a single source and one shape (nothing to coalesce); platinum, which is a per-consumer projection of gold and is not held to one shape.

## Where it should land (PROPOSED)

1. `infra/logic/02_DOCTRINE.md`: a new R-rule in the tier pattern (the GOLD row already reads "pulled from silver by Lambda ... STAYS PARQUET"; this adds the one-shape and adapter clause). LGIC lane.
2. `docs/doctrine/CLAUDE_ANNEX.md` section 7: a rule 17c, one line and a pointer (silver 17 says silver never slims fields; 17c says gold is where shapes are coalesced).
3. `org/standards/`: the first contract instance is the reporting gold's (`REPORTING_GOLD_CONTRACT.json`), authored with the dashboard backend brief. That is the machine-checkable home; the doctrine line points at it.
4. `CLAUDE.md` is NOT proposed: it is locked and this is a principle with a pointer, not a new imperative that must be in the index.

## Read against the existing tier rules (a finding, not a request)

The ratified pattern already says GOLD IS PARQUET and that per-consumer projection, display naming and route-shaping belong in PLATINUM, "the estate's ONLY JSON producer"
(`CLAUDE_ANNEX.md` 17b; `infra/logic/02_DOCTRINE.md` tier table, R6/R10-R12). So the dashboard's "precomputed gzipped JSON served in under 2 s" is a PLATINUM product, built by a platinum
publisher reading Opal-shape gold parquet, and the address for it comes from the naming builder. Andrew's own words allowed for this ("`/gold/reporting/` ... or however LGIC NAMING wants to run paths").
The two dashboard briefs are written to that: gold parquet in the Opal shape, platinum gzipped JSON per account.
