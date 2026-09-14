# ANDREW-DIRECT 2026-09-14 ~20:0xZ (~4:0x PM ET) -- JEPI goes to Structured; the frontend walkthrough needs the build on localhost:5173

**Received at:** the `1.0.0_SA_CTO~Z` terminal, in-session. **Recorded by:** `1.0.0_SA_CTO~Z`, same turn.

## HIS WORDS -- VERBATIM AND ENTIRE

> "Your Inbox watcher shouldnt have a timeout, why do you assume that it does? Also JEPI I would put in Structured, yes. I
> can begin frontend walkthrough any time, just will need the build displayed on 5173 localhost"

## READING -- stated narrowly

1. **JEPI -> Structured.** Answers this seat's card (JEPI, JPMorgan Equity Premium Income ETF, served `equity / US Large Cap`,
   an equity book with an options overlay). The retag set in PRD v0.7 `C-RETAG-SET` grows from TWELVE to THIRTEEN. JEPI is
   held by no Cottonwood satellite component and no Yang served book (measured ~19:5xZ), so nothing served on the Positioning
   page moves on account of it today.
   **OPEN, put back to him:** the target `sub_asset_class`. `Hedge` is the Structured sub-asset for hedge securities (VXX,
   VIXY, UVXY, QBER); JEPI is an options-income overlay, not a hedge.
2. **Frontend view.** He wants the current POSN build served on `localhost:5173` for the walkthrough. Served from a
   separate detached worktree of the portal repo at the latest POSN round-5 portal commit; the shared portal checkout and
   the superproject gitlink `e85f6eb84f` are not touched. No promote, no push.
3. **The watcher question** is answered in-session: this harness's Monitor tool caps `timeout_ms` at 1,800,000 and exposes
   no persistent flag, so the inbox Monitor is re-armed on each 30-minute expiry notice. Not a ruling.
