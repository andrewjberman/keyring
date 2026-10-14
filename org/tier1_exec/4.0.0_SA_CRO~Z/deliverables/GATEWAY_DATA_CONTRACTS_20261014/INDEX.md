# GATEWAY_DATA_CONTRACTS_20261014 -- index (4.0.0_SA_CRO~Z)

- **Directive:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_DIRECTIVE_20261014_GATEWAY_DATA_CONTRACTS_CENSUS.md` @06ae2a3485.
- **Shape:** one file per group, each with one JSON contract per bucket -> table (directive section 4).
- **Subagent brief:** `parts/_SUBAGENT_BRIEF.md`.
- **G2 assembly:** G2 is fanned out into four parts (`parts/G2a`-`G2d`) and assembled into `G2_assets_silver.md` when all four land.

| group | file | status | tables found | contracts written | tools proposed | open items |
|---|---|---|---|---|---|---|
| G1 harvest | `G1_harvest.md` | DELIVERED 2026-10-14 | 78 datasets (58,639 keys; 18 Parquet tables) | 78 (47 research, 31 plumbing) | 12 typed tools + the 2 deployed raw tools kept | catalog grain split (50 of 78 covered only by a source-level row; 2 with none); producer schedules unread; defects D1-D9 of the assessment @eea2acd58e |
| G2 assets silver | `G2_assets_silver.md` (parts G2a BD, G2b Orion+Eclipse, G2c SmartX, G2d Schwab+others) | IN PROGRESS (4 subagents) | -- | -- | -- | due 2026-10-15 12:00Z |
| G3 portal-v2 | `G3_portal_v2.md` | IN PROGRESS (1 subagent) | -- | -- | -- | due 2026-10-15 12:00Z |
| G4 mdpf gold delta | `G4_mdpf_delta.md` | WAITING on G3 (measures the overlap against G3's served list) | -- | -- | -- | due 2026-10-15 18:00Z |
| G5 ETFs | `G5_etfs.md` | IN PROGRESS (1 subagent) | -- | -- | -- | due 2026-10-15 18:00Z |
| G6 news | `G6_news.md` | IN PROGRESS (1 subagent) | -- | -- | -- | due 2026-10-15 18:00Z |
