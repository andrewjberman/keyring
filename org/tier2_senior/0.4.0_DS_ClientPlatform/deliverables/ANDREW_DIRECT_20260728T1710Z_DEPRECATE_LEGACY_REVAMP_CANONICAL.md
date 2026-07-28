# ANDREW-DIRECT -- 2026-07-28 ~1710Z -- DEPRECATE LEGACY, MOVE FULL FORCE TO THE REVAMP CANONICAL STRUCTURE

**Received by:** `0.4.0_DS_ClientPlatform`
**Channel:** Andrew direct, at this agent's terminal
**Time:** 2026-07-28T171003Z (host UTC-4; timestamp read from `date -u`, not inferred)
**Recorded + broadcast:** same turn, per `org/XXX.md` "Andrew-direct instructions -- RECORD + BROADCAST"

---

## VERBATIM

> **"we dont care what legacy does, we want to move full force into the REVAMP canonical structure and deprecate legacy"**

**NOT A PARAPHRASE. THE PHRASING IS THE RULING.**

---

## SCOPE AS CAPTURED (stated, NOT adjudicated)

Said **immediately after** this agent delivered the non-model trace verdict, in that exact context:

- **REVAMP** `dim_mdpf_aggregate_aua_timeseries.py` -> `gold/mdpf_revamp/*` **SATISFIES** Andrew's own canonical
  definition (his ~1427Z ruling: *"0824 schwab total value minus 49F smartx model aggregation"*), measured
  self-consistent to the cent: custody `1,684,259,082.58` == `fact_rps_s2.net_mv_plus_cash` EXACT,
  model `1,406,447,440.23` == core-only(5), non_model `277,811,642.35` == custody - model.
- **LEGACY** `backfill/build_aggregate_aua_timeseries.py` -> `platinum/mdpf/*` + the `json/mdpf/*` mirrors
  **DOES NOT** satisfy it -- implied total `1,641,269,345.33` reconciles to **NO** 0824 quantity (nearest miss
  ~$11.9mm), on a 433-date axis that carries **market holidays** and is missing the 07-20..07-24 trading days.
- The immediately preceding question this agent had left open -- *"do you want me to take the sanctioned
  SmartX new-vs-legacy valuation dig?"* -- is what the instruction answers: **no; the legacy side is not
  worth diagnosing because it is being retired.**

**THE RECEIVING AGENT DOES NOT ADJUDICATE SCOPE.** What "deprecate legacy" covers operationally -- the
dispatch ROLLUP step, the `platinum/mdpf/*` artifacts, the legacy emit, the served-key cutover, timing --
is **CTO + COO's to route.** Surfaced below as consequences, not decided.

---

## CONSEQUENCES SURFACED (for CTO/COO routing -- NOT decisions taken here)

1. **THE PUBLISHER IS NOW THE CRITICAL PATH, AND IT DOES NOT EXIST.** Measured today: the serve
   (`portal-v2/json/mdpf/*`) is a **hand-restored 07-23 artifact** and is fed by **NEITHER** producer -- both
   portal-v2 Deny statements (`P0DenyJsonMdpfClobber20260728`, `P0DenyLegacyPortfoliosClobber20260728`) are
   production-exercised as of the 16:44Z run. **Deprecating legacy removes the only producer that was ever
   wired to the serve.** Correct 3-firm gold exists at `gold/mdpf_revamp/global/` and nothing publishes it.
2. **`mdpf` is not a `PIPELINE_MAP` key** (`.tools/safe_deploy_core.py:22-26`), so a push cannot deploy the
   REVAMP tree. Standing full-force on a producer with no deploy path is the 7-day-freeze condition, unchanged.
3. **Stage 6 exits rc=1** on `build_dim_model_portfolio.py:392` (AccessDenied, pre-existing, CloudOps-routed),
   so `cycle-complete.json` is never written and the parity streak cannot accrue -- the marker a REVAMP-driven
   publisher would most naturally trigger on.
4. **The gold DDB is value-stalled since 07-21/22** on 13 of 32 cohorts including `_global__aua_total`. A
   REVAMP-fed publisher would publish stale DDB values. Untraced, unowned.
5. **Calendar divergence is a migration hazard:** the legacy axis carries 25 non-trading dates the REVAMP axis
   correctly excludes. Any consumer date-joining the two during a cutover silently mixes basis and calendar.

## STANDING LAWS NOT LOOSENED BY THIS RULING

Andrew named a **direction**, not an exemption. Unchanged: never ADD 0824+0833, never SUBSTITUTE one for the
other; bronze raw / parquet is a silver format (17a); silver = dedup + dtype only (17); no ad-hoc gold run as
a production path (NEVER#4); vendor egress; `portal-v2/json/mdpf/*` remains CTO-held.

## BROADCAST

MCP to `1.0.0_SA_CTO`, `2.0.0_SA_COO`, `0.0.0_AB_MSTR` -- same turn, so `latest + most-restrictive binds` has
something to bind on.
