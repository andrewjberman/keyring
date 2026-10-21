# DELL1 self-drive box -- ticks 227-228, 2026-10-21 ~08:18-08:49Z (hour floor; the backfill's per-file landing rule; run 5 ahead of the first scheduled fire)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 08:49Z. Acked since tick 226: 9030, 9035, 9037.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool. The
  per-firm Groups act for Andrew stands (ruling @4c536cb554).

## Acts and rulings
- **The 07:49Z 403** (P1 9030, record @f04bb4c8466): the agent profile's password POST was refused after P1 cleared that profile's
  cookies and storage (a cold profile scores as a bot; the Track A shape of last night). P1 stopped under the one-attempt rule.
  **Ruled** (07:53Z): keep the 09:45Z fire (the puller profile is untouched and warm); run 4 on the puller profile at 08:22Z or
  later; the agent profile rests until the first fire is read, warms by browsing before any sign-in, and no one clears a profile
  again. Read as a profile verdict, not a user flag (earlier puller-profile 403s did not lock the user).
- **Backfill run 4** (08:22Z, puller profile, one sign-in, no 401/403, logout ok; P1 9035, row D1-S17): 2026-10-20 six files in 31 s;
  2026-10-19 five files served in 4 s, the transact body TRICKLED past the 120 s idle bound and the 480 s budget ended the day with
  nothing landed. **Ruled** (08:37Z): GO on REPAIR 7 (a 90 s total cap per file beside the idle bound) and the per-file landing rule
  restated: each served file lands the moment it completes under its content date, never held for the sixth; a capped file is named
  missing with bytes_received. P1 (9037): REPAIR 7 closed @60c2971a770 for run 5 at 08:56Z (step 3E @6ea3c143a50, 29th delivery
  @8e76e29e403); REPAIR 8 (land every downloaded file on any mid-day stop) reopened @0c0dbc4f0ba for the runs after.
- **AMGT_HARVST:** W1 at 60m per my 07:25Z ruling; co-7 stage 7 waits for its apply span.

## Scope state
- **NFRA_FIDUPL:** FT-s-11, FT-s-7 (REPAIR 8), FT-s-8, FU-s-11, FU-x-1 pending. 26 objects under `fidelity/alongside/bronze/` (6
  data for 20261019, 20 run records). Rules ENABLED; first fire 09:45Z. No firm prefix; the earliest SERVED day is 2026-10-19 (twice)
  but no earlier day has LANDED, so no earliest-date row. The "split to firms" half stays UNREACHABLE until Groups exist (Andrew's
  act).
- **AMGT_HARVST:** round 100, co-7 stage 7 pending; W1 at 60m until 2026-10-22 09:30Z.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **Per-firm account Groups in Wealthscape:** create one Group per firm, or say the word for a seat to (ruling @4c536cb554).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a back-dated export profile, only if the wizard's date field cannot be automated on the backfill (CRO 8916).

## Compiler Tools
- `s3 cp` of run records (counts only); `list-objects-v2`; `git log`.
