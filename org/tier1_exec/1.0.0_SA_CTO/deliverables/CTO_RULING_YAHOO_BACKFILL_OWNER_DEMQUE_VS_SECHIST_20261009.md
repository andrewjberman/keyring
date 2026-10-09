# CTO ruling -- ONE owner per piece of the Yahoo price backfill: MDPF_DEMQUE schedules and paces, MDPF_SECHIST writes

**Ruled by:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~04:4xZ, on the overlap `1.0.0_SA_CTO~DELL2` raised (bus 56f7d8bf, relayed by
`0.0.0_AB_MSTR~DELL1` msg 1701). Both projects are seated on dell1, so this seat rules. **Sources:** laptop CRO
`RESEARCH_20261009_CONSOLIDATION_CLIENT_PERFORMANCE_REPORTING.md` section 5.2. MDPF_DEMQUE PRD (title; FWD-7: "Yahoo Finance is used
gently and reliably, and its prices stay right through splits and mergers"). MDPF_SECHIST PRD ADDENDUM v0.2 (C-PULL widened to Yahoo
for ADVI_COTBKF's Yahoo-sourced share; C-SERIES and C-GAP bind Yahoo rows). This seat's msg 1466.

## The split -- no piece has two owners

| piece | owner | why |
|---|---|---|
| The REQUEST: ranking (Andrew's tiers), pacing, stop-on-pushback, resume, and the per-day draw ledger | **MDPF_DEMQUE** | the queue is the budget and priority authority for Bloomberg and Yahoo (Andrew ~22:4xZ: "Only BBG and Yahoo for now"); its FWD-7 pace/stop/resume is this |
| The Yahoo TICKER MAP: resolving each security to a Yahoo symbol, locking it, and listing the unmappable | **MDPF_DEMQUE** | ratified in its brief (Andrew ~19:1xZ, dell2: "the greater issue is resolution of the ticker with yahoo") |
| The STORED SERIES: writing Yahoo price rows, one series per security, gaps blank, and corporate-action adjustments applied to stored history | **MDPF_SECHIST** | it is the one writer of security history (C-SERIES, C-GAP); a second writer of the same rows would be a shadow pipeline |

**How they meet:** a backfill run is a DEMQUE request, ranked and paced, executed through SECHIST's Yahoo writer. That writer reads
DEMQUE's ticker map, writes the rows, and returns the day's actuals to DEMQUE's ledger. DEMQUE's FWD-7 "prices stay right through
splits and mergers" is graded on SECHIST's stored result. DEMQUE builds no price writer, and SECHIST builds no pacing or ranking.

## Carriers

- Msg 1466 stands: the Yahoo pull and its contract live in SECHIST's C-PULL addendum. This ruling adds the request side and the map to
  DEMQUE.
- Each project's next round-N analysis cites this file. Neither PRD's ENDPOINT changes.
- `0.0.0_AB_MSTR~DELL1` relays this file's path to `1.0.0_SA_CTO~DELL2` and to the laptop CRO, whose research section 5.2 raised it.

## ADDENDUM 1 (~04:4xZ) -- KEEP + PORT (`2.0.0_SA_COO~Q1` msg 1715, row MDPF_DEMQUE-D1-S2)

The ruling above names the END state. TODAY the only Yahoo price writer is DEMQUE's `price_store`: live, 32 securities, read by dell2's
ADVI_COTBKF, with up to 150 more at 02:30Z. So:
- **KEEP.** `price_store` stays the one writer, and tonight's draw writes it, until SECHIST's writer exists. No pause: a pause would
  starve a live consumer for no gain.
- **PORT, directly, never side by side** (CLAUDE.md: no shadow pipeline). A SECHIST cell builds the writer on the SAME keys. One window
  switches the writer and dell2 re-points, with a same-window rollback. Then a DEMQUE round-5 cell retires `price_store`'s write path.
  No window has two writers.
- Until the port, the request side (ranking, pacing, ledger) is already DEMQUE's, so nothing else moves.
