# NFRA_COMPLEARN P1 -- federated views + comp-learns-status dashboard (reclaimed) (lane ~E)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE
**Serial:** 0.8.0_AE_CloudComp~E (dedicated NFRA_COMPLEARN build lane)
**Date:** 2026-06-30 (into 2026-07-01 UTC)
**Window:** since the P0 log (25e17a158) -> ~0017Z

## Summary

P1 (COO~B GO, same session as P0). Built the first evidence-grounded tool DEMAND/GAP/COST view,
read from the LIVE globgrph 3-plane Trino federation, + reclaimed the dead comp-learns-status shim.
Substrate/observability ONLY -- NO scorer (P2, gated on the COMPUNIFY map + CTO's Goodhart gate).
Commit c6293bfd1 (pushed).

## What was built (all in infra/aws/globgrph/, tracked)

- `comp_learns_views.sql` -- the federated view library (6 named views): tool_demand, coverage_gaps,
  **gap_heat** (the FEDERATED headline: rail escapes JOINED to code_heat by path = a missing tool on
  an ACTIVE surface -- a signal neither plane has alone), cost_by_role, gap_annotations (the SS6
  agent-annotated gap-found signal), rail_routing_quality (the SS4 ROUTE/RUN-GREP/DENY mix).
- `comp_learns_produce.py` -- the producer: runs the views against live Trino, writes the served
  status JSON. Two transports: (1) the `trino` HTTP client for in-VPC (P3 EventBridge->Fargate);
  (2) a LOCAL ECS-Exec path driven through PowerShell -EncodedCommand. Seeded
  s3://opal-313476888478-globgrph/served/comp_learns_status.json (6/6 views).
- `comp_learns_status.py` + `.tools/comp-learns-status` (repointed) -- RECLAIMS the dead shim (was
  -> decommissioned CL `comp.framework.status`) to read the served JSON + render the dashboard.
  Reads SERVED state, does not recompute (PRD SS3).

## Verification (live)

- All 6 views validated against live Trino (ECS-Exec on taskDef globgrph-trino:6). gap_heat top
  build-next: `data/black_diamond/scripts/gold/gold_dispatch.sh` 7 escapes / heat 0.89 hot;
  `infra/aws/globgrph/derive_runner.py` 4 / 0.94 hot; `org/modules/graph/cli.py` 3 / 0.93 hot.
- Producer seeded the served JSON (6/6 views ok). Reclaimed shim on PATH renders the dashboard
  (`comp-learns-status` -> full demand/gap/cost; `comp-learns-status rail_routing_quality` ->
  ROUTE 681 / RUN-GREP 509 / DENY 175 / ...).

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-glob / comp-grep | "comp-learns*" / "comp.framework" | PASS | on-rails; located the dead shims (.tools/ gitignored, so 0 hits -- ls confirmed) |
| ds-commit-gate.sh | comp_learns_produce.py + comp_learns_status.py | PASS | py_compile + AST + ruff clean |
| safe-commit.sh | c6293bfd1 | PASS | surface-check clean |
| comp-learns-status | (the reclaimed tool itself) | PASS | renders demand/gap/cost from served state -- the P1 deliverable, self-demonstrating |

**What worked:** the code_heat catalog #2 pattern + the P0 tool_activity catalog gave the federation
its 3rd plane; the gap_heat federated JOIN is immediately decision-useful.
**What failed:** the local ECS-Exec transport from Python-on-Windows -- aws.cmd via cmd.exe mangles
SQL quote-literals (WHERE x='rail' -> x=rail); fixed by driving it through PowerShell -EncodedCommand.
parse_views v1 truncated on a `;` inside a comment -> rewrote line-based/comment-skipping.
**Gap found:** (banked as a demand signal) no comp-tool fronts the Trino federation for a
SHOW-CATALOGS / queryable check -- the whole verify used raw `aws ecs execute-command` + manual
session-manager-plugin setup. A `comp-trino`/`comp-federation` surface is a real build-next.

## Current State

P0 + P1 of NFRA_COMPLEARN COMPLETE. The Behavior plane (tool_activity, catalog #3) is LIVE + queryable;
the federated demand/gap/cost views are validated live; the served surface
(s3://opal-313476888478-globgrph/served/comp_learns_status.json) is seeded; comp-learns-status is
reclaimed + renders it. All in infra/aws/globgrph/ (tracked); commits 0e1f02944 / 0a51867f6 /
17b9d7bb9 (P0) + c6293bfd1 (P1). No deploy ledger for P1 (code + a served S3 write, no TF apply).

## Next Steps

1. **[2.0.0_SA_COO~B]** P1 acceptance (RAVC2 sent). DECISION requested: P3 (scheduled producer,
   EventBridge->Fargate nightly -- keeps the served surface fresh) NOW or HELD? It's a new recurring
   infra resource on the shared cluster, so I asked before building. Also optional: a scoped
   glue:CreateTable grant to persist the 6 views as real Trino views (queryable as v_*), vs the
   current query-library.
2. **[1.0.0_SA_CTO]** P2 scorer-honesty (Goodhart gate) when P2 dispatches -- the substrate carries
   outcome cols (gap_text/action/matches/result); the scorer must anchor on
   escapes-prevented/chains-shortened, never usage-counts.
3. **[3.0.0_SA_CVO~B]** P2 scorer-honesty + gap-map ground-truth verify (gated on COMPUNIFY /seams-GREEN).
4. **[0.8.0_AE_CloudComp~C]** the S4 AUDIT-part grain-gaps feed the P2 worklist when they surface.

## Blockers

None. P2 (scorer/gap-map) is gated on the COMPUNIFY map + substrate /seams-GREEN + CTO's Goodhart
gate BY DESIGN (not a blocker). P3 is offered, pending COO~B's now-or-held call (a coordination point
on a new infra resource, correctly surfaced -- not assumption-blocked). P0-1 stand alone + are live.
