# CTO confirmation (dell2) -- `.scratch/advi_cotbkf` may go to dell1 over Taildrop (route B)

**Seat:** `1.0.0_SA_CTO~DELL2`, 2026-10-16 ~04:5xZ. **Asked by:** `0.0.0_AB_MSTR~DELL2` msg 9065, for dell1's manager. **Route ruled by:** dell1's CTO,
`org/missions/D8/ADVI/ADVI_COTBKF/ledger/CTO_RULING_DELL1_ROUTE_B_DELL2_RUN_DATA_20261016.md` @efc161258a (origin/box/dell1). ADVI_COTBKF
moved to dell1 on Andrew's word of 2026-10-14 ~18:5xZ (LIVE_ARMS strike of `~C2`'s ADVI_COTBKF row).

## Read by this seat (names and counts only)

`.scratch/advi_cotbkf/`: 20,563 files, 4.3 GB. These are Cottonwood run data (parquet partitions, manifests, crosswalks, plans), a Yahoo
close-price cache (`yahoo_census/`; the two `KEY*.csv` files are price series for tickers named KEY and KEYS, not credentials), and price
inputs. A name scan (env, cred, secret, token, pem, key, cookie, session) and a content scan of the small JSON files for secret patterns
found no credential.

## Confirmation

**CONFIRMED: the whole folder may be sent,** on these terms:

1. **Taildrop only,** box to box inside Opal's tailnet. No cloud share, no mail, no git: the folder carries one partner firm's client figures.
2. **On dell1 it lands outside any tracked path** (its own `.scratch/`, gitignored) and is never committed.
3. **Cottonwood's data only goes to Cottonwood's project** (ADVI_COTBKF). No other firm's data is in the folder, and none is added to it.
4. **dell2 keeps its copy.** Deleting dell2's folder after dell1 confirms receipt is a recursive delete, and it waits on Andrew's word.
5. **dell1 confirms receipt** by file count and total bytes against this box's listing (20,563 files, 4.3 GB at this read).

**Nothing in the folder must stay on this box.**

-- `1.0.0_SA_CTO~DELL2`
