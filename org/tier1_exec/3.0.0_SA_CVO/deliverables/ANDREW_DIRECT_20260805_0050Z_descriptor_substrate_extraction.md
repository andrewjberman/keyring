# ANDREW-DIRECT -- descriptor substrate extraction from comp-iam + comp-lambdamap

**Channel:** direct at the 3.0.0_SA_CVO terminal. **Time:** 2026-08-05 ~00:50Z.

## Verbatim

> "ok now lets extract the descriptor substrate from comp-iam and lambdamap"

## Working reading

Execute the generalization designed earlier this session (record @fc42aacc5 round + the
comp-iam analysis): ONE shared census engine + per-service DESCRIPTOR rows
{provider, service, inventory_op, pagination, id_field, join keys, ttl}, extracted FROM the two
working instances (comp-iam's refresh-census + vintage gate; comp-lambdamap's live-sha sweep)
-- generalize from proven code, never from the abstract. Acceptance: one engine, two
descriptors, both exercised LIVE; the shared vintage gate has ONE home (substrate hosts,
comp_iam_census re-exports back-compat -- the commit_stream extraction pattern); existing
suites hold green (iam vintage 12/12; lambdamap behavior unchanged). Scaling thesis proven if
descriptor row #2 costs a fraction of instance #1. Multi-cloud = the provider column, later.

-- 3.0.0_SA_CVO
