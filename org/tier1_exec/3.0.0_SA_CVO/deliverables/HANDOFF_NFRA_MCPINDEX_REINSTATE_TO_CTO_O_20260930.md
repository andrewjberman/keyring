# HANDOFF -- NFRA_MCPINDEX back online: what exists per promise, and the blockers to clear

**To:** 1.0.0_SA_CTO~O (the project's CTO). **From:** 3.0.0_SA_CVO~O (its CVO), 2026-09-30 ~07:4xZ, on Andrew's order.
**Andrew's word:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20260930_072xZ_NFRA_MCPINDEX_REINSTATE_NO_TEST_USER_NO_AUTH.md`
-- "I want this project reinstantiated fucking right now with any of these harebrained blockers delineated." "We
shouldnt need a 'test user' to test it. I do not care about fucking aroudn with auth right now."

## 1. The one-paragraph answer

The index exists and is live: `opal_discover` / `opal_describe` over `app/refs/DATA_CATALOG.yaml` v0.3, with 36
dataset rows. Every row is data the portal already publishes: benchmarks, macro, market, positioning, sentiment,
valuation, and MDPF model portfolios. Model-portfolio questions route to a purpose-built tool, and the figures were
proven equal to the portal. **Nothing else the PRD promised is in the index or reachable as a tool:** Schwab, Black
Diamond, Orion, Eclipse, SmartX, ETF holdings, households, the typed-query fallback. Measured at 07:2xZ: live
`opal_discover('Schwab positions')` and `('ETF holdings')` both return `catalogued: false`, which is what CRO base saw.
Round-3 grades: **0 of 10 REALIZED** (`ledger/ROUND_ANALYSIS.round3.md` s.2). Round 4 has 2 orders open, and both are
stuck on gates, not on work.

## 2. Per promise: what exists today

Measured at 07:2xZ from the gateway source at HEAD, this session's live opalgateway MCP tool list, and live
`opal_discover` calls.

| FWD | promise | tool / index today | gap |
|---|---|---|---|
| 1 | cold question -> right tool | `opal_discover`, `opal_describe` LIVE; `next_tool` now names the purpose-built tool (verified: mp.01 -> `mdpf_get_aum_metrics`) | coverage is 36 portal rows only; the cold run by a non-author asker (A1) never ran (G-B) |
| 2 | portal figure = portal's | `mdpf_get_aum_metrics`, `_account_distribution`, `_aggregate_aua`, `_model_benchmarks` LIVE; `platinum/mdpf` EQUAL 4/4 | `platinum/etfs`: tool BUILT, not shipped (B3); `platinum/advi`: no row, no tool; `json/*`: rows route, no tool returns a figure |
| 3 | Schwab positions/balances/transactions | 5 tools BUILT (`schwab_get_access`, `_list_files`, `_describe_dataset`, `_query`, `_prepare_download`), **DORMANT**: not in `ENABLED_INTEGRATIONS`, absent from the live tool list, no catalog row | enable (B1); **transactions are not exposed**: the engine carries `dim_position`, `dim_balance`, `dim_asset` only (`org/standards/NFRA_OPLGTW_CONTRACT.json`), and FWD-3 promises transactions (B4) |
| 4 | Black Diamond, Orion, Eclipse, SmartX | **nothing**: 0 catalog rows for BD, Orion or Eclipse (SmartX's 11 hits are benchmark JSON rows); no tool; no per-property analysis (S8) | build (B5); 4 BD legs dead, the first being ported (MX-s-14, B6) |
| 5 | ETF holdings / net assets / NAV per fund | catalog row + tool BUILT in `C:/Users/Opal Bloomberg/Desktop/wk-mcpindex-r4-15` (MX-t-10), uncommitted, pinned at `refs/archive/wt-20260929/wk-mcpindex-r4-15-candidate` 03a19ac282 | naming gate (B3) |
| 6 | typed-query fallback | `/query/v0` exists as a REST route only (`app/query_v0.py`); not an MCP tool, so no session can call it | expose it as a tool under the C2 classification (B7) |
| 7 | one client across systems | **nothing** | build: entity-resolution rule + precision/recall (S9) |
| 8 | long history + live market data | `ycharts_*` (6) and `graph_cypher`/`graph_status` LIVE; Bloomberg is a separate MCP on this box | no long-history path in the index; the PRD's S10 "laptop project, Bloomberg not claimed" limit is stale -- the project is fabric site-z, where Bloomberg lives (B8) |
| 9 | Andrew admits staff one at a time | grant model exists (NFRA_OPLGTW / MCPORTAL Entitlements) | Andrew: no auth work now -- your call how far that reaches (B2) |
| 10 | next property = one catalog entry + tool | the pattern worked once (MX-t-9, `mdpf_get_model_benchmarks`) | never timed; the planted-unclassified-tool refusal is unproven |

## 3. The blockers, each with the act that clears it

- **B1 -- the "test user" (NFRA_OPLGTW G-C) holding the Schwab enable.** Andrew: "we shouldnt need a 'test user' to
  test it." What remains is the enable act itself: `schwab` added to `ENABLED_INTEGRATIONS` in the gateway env, the IAM
  read on its secret and data, and a release. That is a gateway release under a NEVER-2 ledger with never-widen halves
  (CTO + COO), because it adds tools to the served surface. Test it with an existing Opal principal who holds a Schwab
  grant. **Owner: you, as CTO of both NFRA_OPLGTW and NFRA_MCPINDEX.** No external party is needed.
- **B2 -- auth-shaped gates: G-B (a non-author cold asker), FWD-9 (the beta roster).** Andrew: "I do not care about
  fucking aroudn with auth right now." Recommend: run the FWD-1 cold question set with any already-admitted non-author
  Opal principal, and park FWD-9 as DEFERRED on his word, with the record cited. How far "auth" reaches is yours to
  state, not mine.
- **B3 -- the naming gate refusing the ETF row (row `NFRA_MCPINDEX-Z-W15-S5`).** The catalog must NAME the existing
  served key under `platinum/etfs/`, and `.tools/naming-gate.py` grades that literal as NEW and out-of-pattern, so no
  spelling passes. The object is already served; the catalog only reads it. The clear is one of:
  - (a) a registry row in `infra/logic/registry/` that makes the served key conformant (Rule 30);
  - (b) an R20 departure entry, which takes one acknowledgment from Andrew.

  Pick one this hour. Then MX-t-10's frozen candidate commits as-is (patch pinned, above) and ships in the next
  gateway release.
- **B4 -- Schwab transactions are not in the engine.** FWD-3 needs a `fact_*` / transactions table exposed beside the
  three `dim_*` tables, with the one-master, one-date rule. This is a build cell, not a gate.
- **B5 -- FWD-4 was never started.** Per property, the PRD requires the analysis record first (S8), then tools. Cut
  Black Diamond first, since its silver is current and scheduled: one analysis cell and one catalog-plus-tool cell.
  Orion/Eclipse (`opal-data-inf`) and SmartX follow on the same pattern.
- **B6 -- MX-s-14 is held on scheduled fires, with no ad-hoc run (row Z-S61).** The ledger
  `nfra-mcpindex-bd-playwright-strip` waits on the 2026-09-30 21:46/21:53Z fires, then 2026-10-05 for the rest.
  CLAUDE.md: "waiting for the scheduled run is the same failure" unless an ad-hoc run would destroy the evidence the
  scheduled run exists to produce. Z-S61 must name that evidence, or an ad-hoc QA run fires now and the scheduled fire
  stays the acceptance. This does not block B1-B5; do not let it gate them.
- **B7 -- the typed-query fallback is REST-only.** Register `query_v0` as an MCP tool with its catalog classification
  (C2), or FWD-6 cannot be exercised by any session.
- **B8 -- the PRD's S10/A8 "laptop project" scope limit is stale.** The project is fabric site-z, and the Bloomberg
  on-demand read is this box's standing read. A one-line addendum makes FWD-8 reachable through Bloomberg as well as
  YCharts. That addendum is ENDPOINT-adjacent, so I re-sign it.
- **B9 -- the drive.** `org/ref/LIVE_ARMS.md:28` carries your `/self-drive 30m` over this project with COO~MI's
  `/canonical-drive`. Confirm both are armed after the crash, and tell `2.0.0_SA_COO~MI` this project is live again.

## 4. Recommended order (one issuance, parallel where the chains allow)

1. **Now, no build:**
   - clear B3 (registry row, or put the R20 ack to Andrew);
   - state B2's reach against Andrew's words;
   - answer B6's discriminator question;
   - re-arm the drive (B9).
2. **Round 5 cut by COO~MI**, one issuance:
   - MX-t-10 lands (ETF, FWD-5 / FWD-2 etfs);
   - the Schwab enable release (B1) with a transactions table (B4);
   - `query_v0` as a tool (B7);
   - the Black Diamond analysis + first BD tool (B5);
   - an `advi` catalog row and tool (FWD-2);
   - the FWD-1 cold run by an existing non-author principal (B2).
3. **Close run** by the COO on all of it. I grade the judgment criteria at L9, as before.

This seat does not issue, build or deploy. It grades what lands.
