# DELL1 self-drive box -- ticks 225-226, 2026-10-21 ~07:18-07:49Z (hour floor; the backfill served its first earlier day; the existing Groups are households; W1's cadence)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 07:49Z. Acked since tick 224: 9021, 9023, 9028.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool. The
  per-firm Groups act for Andrew stands (ruling @4c536cb554).

## Acts and rulings
- **Backfill run 2** (06:47Z) was killed by SSM's 900 s executionTimeout with no DAY lines and an unknown logout (row D1-S15).
  **Ruled** (07:06Z): evidence survives a kill (per-day lines and an incrementally written record), the SSM timeout from the walk's
  own arithmetic, SIGTERM runs the logout, the recovery hook reads the session first, the issuer may allow one more run today. P1
  built it as FT-s-7 REPAIR 4 (@97aa58db10e) and REPAIR 5 (record rewritten per day, @2dffc3b70eb); merged @170a9c69ce8.
- **Backfill run 3** (07:22Z, one sign-in, logout ok; record `deliverables/0.7.0_AE_CloudOps~NFRA1/...step3C_output.md`): 2026-10-21
  empty; 2026-10-20 complete in 30 s; **2026-10-19 the FIRST EARLIER DAY SERVED** (status list 200, six files, five downloaded in
  0-16 s, transact stalled 452 s to the wall budget; nothing landed for that day). **Ruled** (07:37Z): a per-download stall bound
  (no bytes for 120 s), a day lands its served files with the stalled one named missing with its reason, one end-of-run retry of the
  missing files, walk on; transactions older than the standing files come by the per-account historical route, named in the record.
  P1 reopened FT-s-7 REPAIR 6 (a browser-side download with a 120 s idle bound, @832e2436843); row D1-S16 filed by NFRA1. Run 4
  follows under today's session cap of 4.
- **The Group token count** (P1 9021, on the box, names in memory only): firm 0, advisor 0, household 49, unclassifiable 9 (5
  ALL-system including an exact ALL ACCOUNTS, 4 purpose groups of which 3 are first-name groups that may be advisor books). The
  one-off Group export did not run (the wizard tab bounced to the login page in a second agent session); retry on a clean Chrome
  state. **Ruled:** the one-off export reads one of the three first-name groups, not a household.
- **AMGT_HARVST** (W1 9023): everything for addendum 3 is staged; W1 asked to run its canonical-drive at 60m until 2026-10-22 09:30Z
  because empty ticks were pushing filler acts. **Ruled YES**: 60m until 09:30Z, then 30m for the apply span through the Friday
  fire's read; an empty tick commits nothing; W1 tells MSTR so the census reads it as ruled.

## Scope state
- **NFRA_FIDUPL:** FT-s-11, FT-s-7 (REPAIR 6), FT-s-8, FU-s-11, FU-x-1 pending. 24 objects under `fidelity/alongside/bronze/` (6
  data for 20261019, 18 run records). Rules ENABLED (first fire 09:45Z). No firm prefix; the backfill's earliest served day is
  2026-10-19 but no earlier day has LANDED yet, so no earliest-date row. The "split to firms" half stays UNREACHABLE until Groups
  exist (Andrew's act).
- **AMGT_HARVST:** round 100, co-7 stage 7 waits for the apply span; W1 at 60m.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **Per-firm account Groups in Wealthscape:** create one Group per firm, or say the word for a seat to (ruling @4c536cb554).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a back-dated export profile, only if the wizard's date field cannot be automated on the backfill (CRO 8916).

## Compiler Tools
- `git show` of surprise rows; `s3 cp` of run records (counts only); `list-objects-v2`.
