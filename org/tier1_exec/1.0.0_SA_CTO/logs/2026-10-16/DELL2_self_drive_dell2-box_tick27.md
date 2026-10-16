# /self-drive dell2-box -- tick 27 (2026-10-16 ~02:56Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md` (cadence
change @9bfb404220). **Since tick 26 (@08a2a01213):** the CVO signed v0.21 (msg 8923; PRD ADMITTED; ~T2 told to cut FWD-4). The 30m word
was landed in LIVE_ARMS with all eleven dell2 COO seats named (@1fa81e75a7; msgs 8949-8960). The cron moved to `23,53`.

## Calls ruled this tick

| call | REC = ruling | why | routed |
|---|---|---|---|
| `~Y2` msg 8966: the door's yfinance checker is unwired (C-SWAP step 2) | A real gap. `~G2` wires the checker into every session the door builds. It folds into r34 if D1 has not started (re-packet, re-sign), else ships as r35. FWD-1 run 3 waits on it | Verified: across investor-reporting, `YfinanceChecker` is constructed only in tests, and neither r33's nor r34's changed members wire it. A yfinance-known symbol is filed TICKER_NOT_FOUND, against C-SWAP (2) | msgs 8968/8969 |
| `~T2` msg 8967: the commentary fail op needs a write on irpt-jobs (A grant / B requests item) | (A): UpdateItem on irpt-jobs with the leading-key condition, `dynamodb:Attributes` limited to `hop_failure` plus keys, ReturnValues NONE, conditional set-once; a simulate battery in the pair | (B) would force a second status reader, because the page reads irpt-jobs. The PRD is unchanged | msgs 8970/8971 |

## Open calls (dell2 list: 4 open; every one is an act or approval only Andrew can give)

## ACTS ONLY ANDREW CAN DO

- **40fa (new):** approve for portal PROD the prospect composer with no price date ("Prices are the T-1 close.", header as-of "T-1 close").
  The row's class is client-facing (Investor Reporting > Analysis tab), so it waits on his word (CLAUDE.md Agent Autonomy: "a portal PROD push
  that changes a CLIENT-FACING page ... waits on his word"). Precondition: r33 live. Until then the live door still asks a share-quantity file
  for a price date.
- **dbfb:** the client-facing Performance-tab candidate for portal DEV (CLAUDE.md Portal).
- **c02c:** the Inflection send, his word (an outward send to a partner firm; "we will get to this later").
- **e260:** the Opal_Terminal key, his ("i will handle it").

Completion test: NOT DONE. state: ARMED

## Compiler Tools

open-calls.py list, Grep (checker construction census), safe-commit.sh.
