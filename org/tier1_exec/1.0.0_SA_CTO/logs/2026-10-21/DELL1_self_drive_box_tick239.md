# DELL1 self-drive box -- ticks 238-239, 2026-10-21 ~13:49-14:19Z (hour floor; the Historical cap MEASURED; the backfill walk ruled and landing)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 14:19Z. Acked since tick 237: 9094, 9095, 9097, 9098, 9103.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool. The
  per-firm Groups act for Andrew stands (ruling @4c536cb554).

## Acts and rulings
- **P1 unstuck** (MSTR 9095, 13:21Z): idle at an empty composer after "Compacted while idle", no inbox-watch process (expired without
  re-arm); MSTR's by-process keys typed the read pointer and the seat resumed, read its four unread, re-armed. First live test of
  the `/unstick` fix (@2138a1f383): it worked.
- **The Historical session** (P1 9094/9097/9098, agent profile, signed in 13:25Z; record @3131b59046e): the 10/15 request served
  positions and prices in ~30 s (as-of 20261015, the standing layouts). **Andrew's cap question answered by measurement:** positions
  served back to 2026-06-15 (06-12 errors), prices to 2026-06-18 (06-17 errors); the 150/180/270/365/730-day requests were ACCEPTED
  then "COMPLETED WITH ERRORS, file does not exist", never refused: Fidelity's data runs out at about 128/124 days, not at the
  picker's 120. 15 files landed over 8 dates; read by me: `position/` 20260615, 0617, 0618, 0622, 0623, 0821, 0921, 1015 and
  `prices/` 20260618, 0622, 0623, 0821, 0921, 1015, beside the daily days. The CRO carried it into the ms report (third answer,
  @4eac4ec62bd) in place of "cap unproven".
  - **Ruled** (14:16Z): cut the Historical backfill WALK as the next order: one POST per trading day, the existing saved profile,
    positions, balances and prices, from 2026-10-14 back to the proven floor, skipping landed dates, each file by its as-of content
    date, "file does not exist" recorded EMPTY with the text, stop at three consecutive empties per file type; POSTs per run set by
    the issuer from the measured ~30 s; the hourly sign-in cap stands. At 14:19Z the bucket reads 11 position and 9 price objects:
    the walk is landing.
- **Transactions probe unblocked** (CRO 9103): `searchBy="none"`, `timePeriodOption="custom"`, `dateField="T"`, the date pair and the
  account tuple (BROK / IWS); P1 resumes the per-account floor probe on the CRO's record.
- **AMGT_HARVST:** no change; W1 at 60m until 2026-10-22 09:30Z.

## Scope state
- **NFRA_FIDUPL:** FT-s-8, FU-s-11, FU-x-1 pending (the walk order to be cut). 68 objects under `fidelity/alongside/bronze/` (31
  data; 37 run records). Rules ENABLED, the scheduler proven; first real fire tomorrow 09:45Z. Deliverable 1: scheduled, enabled,
  proven; the per-firm SPLIT UNREACHABLE until Groups exist (Andrew's act). Deliverable 2: earliest landed per file type at this
  read: positions 2026-06-15, prices 2026-06-18, account/balance/security 2026-10-16, transact 2026-10-19; balances and
  transactions history pending the walk and the probe.
- **AMGT_HARVST:** round 100, co-7 stage 7 pending.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **Per-firm account Groups in Wealthscape** (and the saved export profile a Group-filtered export needs): create them, or say the
  word for a seat to (ruling @4c536cb554).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a hand-recorded HAR of the Historical wizard, only if an agent walk is refused at the password step (not needed
  so far).

## Compiler Tools
- `list-objects-v2` (every data object with its date prefix); `get_agent_status` (P1); `git log`.
