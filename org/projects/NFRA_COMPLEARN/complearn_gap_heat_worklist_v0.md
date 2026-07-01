# NFRA_COMPLEARN -- gap_heat build-next worklist v0 (observability-scoped)

**Author:** 0.8.0_AE_CloudComp~E · 2026-07-01 · P1-output scope (COO~B-dispatched #3)

**What this IS:** candidate build-next tools SCOPED from the LIVE gap_heat + coverage_gaps views
(the P1 federation output) + the raw comp-which-rail.log demand terms, each grounded against
comp-which. The loop's first *actionable* observability output.

**What this is NOT (the P2 gate -- respected):** this is NOT the value-anchored SCORER. No scoring
against the COMPUNIFY coverage map, no champion config, no KEEP/DISCARD ratchet, no auto-emit. The
scorer that RANKS by VALUE (escapes-prevented / chains-shortened) and gates the mutation is P2,
gated on the COMPUNIFY map + substrate /seams-GREEN + CTO's Goodhart gate + CVO honesty. This is a
human-readable candidate list for **CTO ratification** (the advisory-worklist -> CTO-commission
path, PRD SS3/SS5), derived from observed demand -- not a scored recommendation.

## Signal basis (live, this window)

gap_heat top build-next paths (rail escapes x code heat): `gold_dispatch.sh` (bd 7 escapes/heat
0.89 hot; cot 6/0.66 warm), `derive_runner.py` (4+/0.94 hot), `org/modules/graph/cli.py` (3/0.93),
`D_01.partner_analytics.py` (3/0.85). Full untruncated terms pulled from comp-which-rail.log.

## Candidates (ranked by demand x heat; grounded, not assumed)

### #1 -- `comp-dispatch` (gold-dispatch DAG tool) -- BUILD-NEW, real gap
- **Demand:** the single largest escape cluster. `gold_dispatch.sh` (bd+cot, the two hottest paths)
  is raw-grepped for "what scripts does this dispatch run, in what ORDER, with what conditional
  SKIPS": terms `E_*|for .*E_|run_stage|STAGE.*E`, `python3?.*[A-E]_[0-9]|\.py`,
  `C_00.canonical_performance|C_02.client_performance` (does it run script X?),
  `\.py.*\|\|.*-f|test -f|\[ -f|missing|not found|SKIP` (the skip logic).
- **Grounded gap:** comp-which BACKSTOPPED (no direct route -> comp-platinum/comp-pipescript-deployed,
  none of which parse the dispatch orchestration). comp-pipescript is per-SCRIPT; nothing reads the
  dispatch `.sh` DAG. Real gap, not a routing miss.
- **Build:** parse `*_dispatch.sh` -> the ordered stage/script DAG + conditional-skip predicates +
  "which scripts run under which STAGE/flag". Sibling to comp-pipescript (script-level) at the
  DISPATCH (orchestration) level.

### #2 -- gold-script output-KEY / artifact surfacing -- ROUTE-FIX or ENHANCE
- **Demand:** agents raw-grep gold scripts for output-key CONSTANTS + written artifacts:
  `aua_certification_key|portal_aggregates_key|firm_aua|def .*_key\(` (D_00),
  `CLIENT_PERFORMANCE|client_performance\.parquet|_KEY *=|primary.*aua|aua.*source` (D_01/cot),
  `s3.*put_object|to_parquet|OUTPUT|write` (E_25).
- **Disposition:** comp-pipescript io ALREADY shows reads/writes -> this is likely a Mode-1 ROUTING
  MISS (the tool exists; comp-which doesn't connect "what KEY/artifact does script X write" to it)
  and/or comp-pipescript io not surfacing the `_KEY =` output CONSTANTS prominently. Fix = a
  comp-which routing rule ("what key/artifact does gold script X write" -> comp-pipescript io) +
  (optional) surface output-key constants in comp-pipescript io. LD-0226-class routing mutation.

### #3 -- `comp-symbols <file>` (intra-file symbol index) -- BUILD-NEW-lite or ROUTE-FIX
- **Demand:** large HOT files raw-grepped for their own symbols: `derive_runner.py` (90KB, heat
  0.94) for `def ingest_|def commit_to_iceberg|producers/|def main|_PRODUCERS`,
  `node_type|drift_class|layer|props`.
- **Grounded gap:** comp-which grep-fell-back (no direct route). comp-blast is function-BLAST-radius,
  not a file symbol LIST. Fix = a lightweight per-file symbol index (functions/classes/constants),
  OR a routing rule -> comp-blast/comp-trace for the symbol-navigation intent.

## Read-out for the CTO-commission path

- **1 real BUILD-NEW** (comp-dispatch -- the clear top gap) + **2 mostly ROUTE-FIX** (#2/#3 existing
  tools under-routed). This mirrors the LD-0226 insight: a large share of discovery friction is
  Mode-1 ROUTING MISSES, not missing tools -- so the worklist is build-AND-route, and the routing
  rules are a first-class mutation surface (PRD SS4).
- The P2 scorer, once ungated, would RANK these by escapes-PREVENTED (build comp-dispatch -> do the
  gold_dispatch.sh escapes drop?) and gate KEEP/DISCARD. This v0 is the un-scored candidate feed.
