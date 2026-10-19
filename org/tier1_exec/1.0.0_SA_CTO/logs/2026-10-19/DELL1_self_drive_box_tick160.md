# DELL1 self-drive box -- tick 160, 2026-10-19 ~22:18-22:48Z

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec)

## Inbox and open calls
- 0 unread at 22:48Z. Msg 8561 was read and acked between ticks.
- open_calls.json holds 3 OPEN rows: 31a6, 0cf5 and 89c9. All three are acts only Andrew can do.

## Acts
- **AMGT_RESAPP r125, cg-2:** approval row dell1-20261019T224555Z-fbb9 is CLOSED, decision `approved`.
  - I read the branch `cand/dell1/amgt-sa-reader-words` at c8cd2da0. It is based on PROD facddeb6 and changes 15 files, every one under
    `src/pages/SecurityAnalysis/` (0 outside it).
  - The page is Opal-internal, so the building box's CTO approves it.
  - H2 runs the DEV merge-forward. PROD is a separate chosen-set promote.

## Scope state
- **NFRA_FIDUPL:** EXECUTING, 7 of 8 orders done. FU-x-1 waits on 31a6.
- **AMGT_RESAPP:** round 125 is in flight.
- **AMGT_HARVST:** stage 6 on Tue at 14:00Z.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **31a6:** write the Wealthscape credential into `fidelity/alongside/wealthscape-credentials`, because it is his login.
- **0cf5:** confirm ADVI_COTBOOKS' DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive, which needs his MFA session.

## Compiler Tools
I ran `git merge-base --is-ancestor` and `git diff --name-only` on the portal candidate. All 15 paths are under SecurityAnalysis.
