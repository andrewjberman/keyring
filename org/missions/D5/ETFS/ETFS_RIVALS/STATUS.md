# ETFS_RIVALS (rivalfunds) -- status (FULL since 14:40:14Z; round 6 EXECUTING, 6 workers)

Seat `2.0.0_SA_COO~RV` (CLAUDE). Mode FULL on Andrew's word ("yes you can move to /canonical-drive for the remainder";
relayed ~14:1xZ: "max parallelization on subagents"; record
`org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261002_141xZ_CANONICAL_DRIVE_MAX_PARALLEL_RELAYED.md`).
Goal (Andrew ~04:59Z): "i want mcp.opalinvest.dev/rivalfunds demoable Today".
Team:
- reviewer `3.0.0_SA_CVO~RV` (`org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md`: grades 1-14 PASS);
- open calls `4.0.0_SA_CRO~RV` (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md`: CALLs 1-13 ruled).

As of 2026-10-02T16:1xZ.

## Pins

| What | Value |
|---|---|
| Round-6 issuance | `1e8515aa01` (14 orders, 6 chains, `fanout: 6 of 6 chains, cap 8`), drained to CLOUD at `0d270a70b2` |
| Decomposition | `decompositions/ETFS_RIVALS_DECOMP.md` v1.0 (round 5 rotated to `.round5.md`) |
| Workers | `0.9.0_WK_ETFS_RIVALS~1..~6` in `/c/tmp/wk-riv6-<n>` (branches `wk-ETFS_RIVALS-<n>`, base 1e8515aa01) |
| Deployed artifact pin | CLOUD **722f0db291** in the five etfs-rivalfunds Lambdas + the publish-page bronze-read grant (every ledger CLOSED) |
| Served page | `platinum/page/date=2026-10-02/index.html`, batch rv-publish-1002g (15:04Z, RFW-D01 refresh): 13 of 13, 213 trades, AI 22/2; grade 14 PASS |
| Push state | CLOUD LOCAL, ahead of origin; MSTR~Z carries the integrator push |

## Round 6 chains (slot: queue; first order in flight)

| slot | queue | write set |
|---|---|---|
| ~1 | **st-1** -> ap-1 -> r-6 (worker-light) | publish_page.py; ai_stage.py, ai_client.py, infra/aws/terraform/etfs-rivalfunds/; ai_accounts.py, guardrails.py |
| ~2 | **rk-2** -> sx-1 | gold_holding_contribution.py, guardrails_config.json; gold_buying_trend.py |
| ~3 | **e-2** -> x-1 | enrichment_bloomberg.py, gold_trade_schedule.py |
| ~4 | **ic-2** | gold_input_census.py |
| ~5 | **nm-1** | collector_bloomberg.py, silver_bloomberg.py, gold_canonical_shape.py, names.py |
| ~6 | **ui-1** -> ui-2 -> ui-3 -> ui-4 -> ui-5 | render.py |

Amendments pending (CRO census @308f982bb8, msg 28561): sx-1 gains the CALL 9 cross-fund GICS fallback in the rankings
(Fix 1); ic-2 reads the fund's own G1 sector before calling a GICS input missing (763 -> 118). Checks being written.

## Issuer acts (mine, each under its own pair)

- Merge hookups at the drain: publish_page -> ai_stage.run_for_day; ai_accounts.default_client -> ai_client; names.display_name
  in the producers.
- The Lambda deploy after the drain; the OpenAI secret value; the names() BQL shape proved live at the next vehicle run.
- I-1 W4-S9 disarm; I-2 backfills + v0.8 leg + G5/G6 replay + W3-S12 probe; I-3 G4 universe + history + CUSIP-keyed GICS
  (census Fixes 2-3); I-4 the per-fund arrival read (RFW-D07).
- Andrew: the signed-in walk of the gateway route (RFW-U19).

## Next proof

1. Each worker report -> review against its checks -> hand the slot its next order (continue the same worker).
2. Chain ends -> drain per chain -> hookups -> suite -> deploy pair -> ONE real run of the page -> L8 compile to the CVO.
3. 2026-10-05: the 07:00 ET marker page read; the 10-05 AI accounts (scheduled path if ap-1 has landed, else one seat run, VEW-2).

## Limits

No product ID is PASS until `3.0.0_SA_CVO~RV` grades the served artifact. Workers never call a vendor, write S3 or deploy.
