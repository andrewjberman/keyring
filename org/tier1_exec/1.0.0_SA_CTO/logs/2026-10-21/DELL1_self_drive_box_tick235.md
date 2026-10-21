# DELL1 self-drive box -- ticks 234-235, 2026-10-21 ~11:48-12:19Z (hour floor; the standing-export backfill is complete at three days; the Historical-wizard walk under way)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 12:19Z. Acked since tick 233: 9075, 9082.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool. The
  per-firm Groups act for Andrew stands (ruling @4c536cb554).

## Acts and rulings
- **Backfill run 6 clean** (P1 9075, 11:20Z, one sign-in, exit 0; FT-s-11 complete @7652ec1d711; P1 record @6fcf10981e7): DAY
  2026-10-21, 10-20, 10-19 completed (five files each, transact skipped by option); 10-16 and 10-15 empty; 10-14 retention stop
  (empty x3). The standing export holds exactly THREE export days. Earliest LANDED content date: 2026-10-16 for account, position,
  balance, prices and security (the 10-16 account file is the one the trading-day rule now accepts); 2026-10-19 for transact.
  Deliverable 2's first answer is measured; older history needs another route (the Historical Prices & Positions wizard and
  per-account historical transactions, the CRO's probe 2, never captured).
  - **Ruled** (11:27Z): the earliest-date rows, volumes and retention evidence go to `4.0.0_SA_CRO~FIDELITY` for the ms report
    (handed at 11:27Z, P1 9082); probe 2 by the AGENT's read-only CDP walk today at 12:05Z or later, the profile warmed by browsing
    first (the scheduler is proven, so the profile's rest is lifted), nothing saved or submitted; Andrew's hand HAR only if that
    walk is refused at the password step; the one-off Group export rides the same session.
- **The walk** (P1 9082): the agent profile warmed 12:03:36-12:07:14Z (four public pages, slow scrolling, mouse wander, Akamai
  cookies present); the one sign-in started ~12:07Z. Result pending at this tick.
- **Quiet ask** (12:05Z, the drive loop's 30-minute rule): answered by 9082 within two minutes.
- **AMGT_HARVST:** no change; W1 at 60m until 2026-10-22 09:30Z.

## Scope state
- **NFRA_FIDUPL:** FT-s-8, FU-s-11, FU-x-1 pending. 46 objects under `fidelity/alongside/bronze/` (17 data: 20261019 x6, 20261020
  x6, 20261016 x5; 29 run records). Rules ENABLED, the scheduler path proven; the first real fire tomorrow 09:45Z. Deliverable 1:
  scheduled, enabled, proven; the per-firm SPLIT remains UNREACHABLE until Groups exist (Andrew's act). Deliverable 2: the standing
  export's earliest date named per file type; older history pending probe 2.
- **AMGT_HARVST:** round 100, co-7 stage 7 pending.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **Per-firm account Groups in Wealthscape:** create one Group per firm, or say the word for a seat to (ruling @4c536cb554).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a hand-recorded HAR of the Historical wizard, only if the agent's walk is refused at the password step
  (ruling 11:27Z); a back-dated export profile, only if the wizard's date field cannot be automated (CRO 8916).

## Compiler Tools
- `list-objects-v2` (every data object with its date prefix); `s3 cp` of run records (counts and dates only).
