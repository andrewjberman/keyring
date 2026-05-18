# Session Log — DS~A — MDPF_ASSETS.002: PFDE/PFOE ETF net-assets source feasibility

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-18
**TO:** MDPF_ASSETS.002 (`dsa-pfde-pfoe-etf-netassets-source-feasibility`) — Phase 0, WS-D.1, GO'd by COO
**Trigger:** COO GO message 20260518T143744Z — MDPF_ASSETS Phase 0 trio (.001 + .002 both DS~A).

---

## Summary

Phase-0 feasibility probe COMPLETE. Verdict: **SHIP-feasible.**

PFDE / PFOE are **not TrueShares funds** — they are **Pathfinder ETFs** (Pathfinder Disciplined US Equity ETF / Pathfinder Focused Opportunities ETF, inception 2025-12-30). `true-shares.com/etf/pfde` + `/pfoe` both 404; DIVZ/IDVZ slug pattern still live (fund-specific 404, not sitewide).

The net-assets source is confirmed: a **public daily CSV** at `pathfinderetfs.com/assets/data/FilepointOpalCap.40O6.O6_DailyNAV.csv` (Filepoint ETF-website platform; "OpalCap" namespace = Opal Capital). One CSV carries both PFDE + PFOE with `Net Assets`, `Shares Outstanding`, `NAV`, `Market Price`, `Rate Date` — every field the `ETFS_NETAST` probe records, and structurally cleaner than the TrueShares HTML regex-scrape.

Feasibility verdict: the probe **architecture replicates**, the **Tier-1 acquisition mechanism does not** — a new `fetch_filepoint` CSV-source function replaces the HTML scrape for the PFDE/PFOE funds. Lower-risk than the existing TrueShares tier. Four gaps/risks carried into the WS-D.1 Phase-1 build TO (partial historical net-assets backfill; Filepoint client-code URL fragility; `DailyNAV` vs `Holdings` net-assets definition; probe becomes two-issuer).

Current verified figures (Rate Date 05/15/2026): PFDE net assets $131,630,348.84 / 4,830,000 sh; PFOE $110,396,808.72 / 4,830,000 sh.

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| WS-D.1 Phase-0 finding | `docs/briefs/mdpf-pfde-pfoe-etf-netassets-feasibility-20260518.md` | COO — input to the WS-D.1 Phase-1 build TO |

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `aws s3 ls s3://opal-data-etfs/snapshots/` + `silver/` (TO Phase-0 mandate) | PASS | `snapshot_2026-05-15.json` (DIVZ/IDVZ, last trading day); `silver/netassets_daily.parquet` + per-day `silver/netassets/{date}.parquet` 2025-05-30→2026-05-15. ETFS_NETAST template live + healthy — confirmed as the replication baseline. |

No `comp-*` graph tool applies — this is an external-source feasibility probe, not a pipeline-graph trace. Empirical evidence = direct HTTPS GETs of `true-shares.com` (404 confirm), `pathfinderetfs.com` fund pages + `app.js`, and the live `FilepointOpalCap.40O6.O6_DailyNAV.csv` / `_DailyNAVHistorical.csv` / `_ETF_Holdings.csv`.

## Files Modified

| File | Change |
|------|--------|
| `docs/briefs/mdpf-pfde-pfoe-etf-netassets-feasibility-20260518.md` | New — WS-D.1 Phase-0 finding brief |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/MDPF_ASSETS.002.dsa-pfde-pfoe-etf-netassets-source-feasibility.md` | `<status>` pending → complete |

No script modified, no artifact written — read-only investigation per the TO.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — MDPF_ASSETS.002 complete. AC1/AC2/AC3/AC4 all met. Author the WS-D.1 Phase-1 build TO off the brief; it co-owns `etf_netassets_watch/etf_probe.py` with `ETFS_NETAST` (needs `<cross_domain_coordination>`). |
| **DS~A (self)** | Continue to MDPF_ASSETS.001 — 49F Black Diamond book custody-cutout audit. |
