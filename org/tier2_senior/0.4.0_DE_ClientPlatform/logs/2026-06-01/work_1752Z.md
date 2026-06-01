# /work — 0.4.0_DE_ClientPlatform — 2026-06-01 1752Z (A+ diff FINALIZED on CTO ruling)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

## Dispatch
CTO RULING (175xZ) on the 5 verbose tickers: use the CLEANER FE-display names (my default), NOT verbose attr legal names. Principle: display=clean+readable, attr-canonical=fallback. Ship all 22 + portfolios override + row['name'] paths in one consolidated diff.

## Work — A+ diff finalized (brief updated)
- 5 style-flags RESOLVED = FE-display (matches my default; brief note updated to "RULED").
- Part 2 IMPROVED on the row['name'] inclusion: verified lines 1549 + 2032 are the etf_lookup BUILD points (ticker=row.iloc[0]) that ALL name reads flow from (1444 aggregated, 1587 current_holdings, 2071 portfolios via etf_lookup.get). So bake the override at the SOURCE (1549+2032) instead of per-consumer:
  - 1549/2032: `'name': ETF_NAME_OVERRIDES.get(ticker, row['name'] if pd.notna(row['name']) else ticker),`
  - SUPERSEDES the original separate "wrap 2071" (2071 reads the now-clean 2032 lookup). Robust = no whack-a-mole; future consumers can't re-introduce. 1444/1587 read-overrides become redundant-harmless.
  - Note to AE: .strip() ticker if whitespace risk.
- Verified portfolios path: line 2070 etf_meta = etf_lookup.get(ticker) (2032-built) -> 2071 name -> 2097 emit. Baking at 2032 cleans it.

## Commits
- CLOUD `<pending>` — brief A+ finalization + this log

## Comms
- ACK CTO ruling. HANDOFF (finalized diff) -> AE; CC CTO + COO.

## Next
- [AE] apply finalized A+ diff (22 dict adds + bake-at-1549/2032) + deploy + re-emit + CF-invalidate; ping me.
- [me] serving-verify post-deploy (all 22 + portfolios-section + current_holdings clean). Andrew visual.
- [RD~B] FE map slim AFTER backend verified (sequenced). Held: DS~B Schwab re-derive verify; RD~B fold(103f623a) verify. /work cron live.
