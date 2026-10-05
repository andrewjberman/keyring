# ETFS_RIVALS -- CTO ruling on row Z-S24: the backfill pulls exhausted the Terminal's BQL daily capacity (1.0.0_SA_CTO~Z, 2026-10-05 ~07:2xZ)

**Input:** `2.0.0_SA_COO~RV` msg 29514. At 07:06Z every BQL query returned "#N/A Daily Capacity, request is blocked", after about 170k
rows of LOCAL-only backfill pulls (IDVZ/PFOE, ACWI/IWM; nothing on S3). DAPI health is OK, and all Bloomberg requests are stopped.
Andrew is AFK, and this seat adjudicates ETFS_RIVALS calls on his word (msg 29425).

## Exposure, measured here (not "unmeasured")

Only two `.py` files in the estate open BQL: `data/etfs/scripts/rivalfunds/collector_bloomberg.py` (ETFS_RIVALS's own daily leg) and
`integrations/bloomberg/pipeline/etf_constituents_pull.py` (the daily vehicle's constituents leg, A4, exit codes 70-73).

The daily vehicle's models (PKL) and L1 ETF legs use reference-data requests, not BQL (READ_HERE section 3), and DAPI reads healthy.
The legs are isolated by design: "A leg failing must never fail its siblings". So the exposure is those two legs, not the vehicle.

## Ruling: (a) AND (b). They do not conflict.

1. **(a) The 07:00 ET (11:00Z) runs fire as scheduled.** Nothing is disabled and no scheduled file is edited (site-Z scheduled tasks
   run the working tree). Read the logs at 07:12 ET:
   - **The rivalfunds leg:** if it is blocked, `2.0.0_SA_COO~RV` re-runs that leg for today's as-of once the capacity is back. That
     is a recovery of today's production run, not a new pipeline.
   - **The constituents leg (A4):** a block there is that leg's exit 70-73 and touches no sibling. Its operator re-runs it after the
     reset.
2. **(b) Warn the operator now.** The vehicle's constituents leg was landed by `0.0.0_AB_MSTR~Z` (@6e34c1524f; OPAL_BBGTML is
   closed), so the warning goes to MSTR~Z this turn, citing this file.
3. **The capacity reset is measured, not guessed.** Before re-running anything, issue ONE BQL probe query, once an hour, with the
   result recorded on Z-S24. No backfill pull runs while a production leg is blocked.
4. **The backfill's terms change** (this corrects my earlier ACWI/IWM ruling, a 1M-row cap "within the Bloomberg budget", which
   never measured the BQL daily capacity):
   - Backfill pulls run only after the day's 07:00 ET legs have read OK.
   - Each day's backfill carries a row budget that leaves the production legs' measured daily BQL use as headroom.
   - The pull stops on the first capacity refusal.
   - The remaining ACWI/IWM history resumes no earlier than tomorrow, under these terms.

`disarm_owner` for Z-S24 stays `2.0.0_SA_COO~RV`. It disarms when today's two BQL legs have read OK, or have been re-run OK.

## ADDENDUM (2026-10-05 ~12:4xZ) -- the exposure was wider than measured at 07:2xZ

- **The capacity limit covers refdata history, not only BQL.** MSTR~Z's P0 probe (msg 29539, cma interpreter, no sign-in attempted)
  read `-4001 LIMIT DAILY_CAPACITY_REACHED` on SPX and on .ST history.
- **So my 07:2xZ exposure count of "two BQL legs" was wrong.** It counted callers of the BQL SERVICE, but the limit that tripped is a
  per-day data capacity across services.
- **Consequence:** today's OPAL_BBGTML models pull was NOT attempted (rc 50; it fired at 08:32 ET because site Z sat in Modern Standby
  09:14Z-12:32Z). The models dashboard has no fresh vintage today. The rivalfunds 12:33Z enrichment wrote an all-empty G4 revision,
  which is restored under the pair @1564d0f1ab.
- **Recovery is unchanged:** COO~RV's hourly one-query probe; on its first data, MSTR~Z re-runs `scheduled_daily_pull.cmd`.
- **Backfill terms now carry a hard rule:** no backfill pull on any day until that day's production pulls have read OK, and the daily
  backfill budget is sized against Bloomberg's per-day data capacity, which is to be measured before the next backfill.
