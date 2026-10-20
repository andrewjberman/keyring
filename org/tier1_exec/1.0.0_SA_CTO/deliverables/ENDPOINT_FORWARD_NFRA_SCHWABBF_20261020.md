# ENDPOINT (step 2, /endpoint --forward) -- NFRA_SCHWABBF: Schwab masters, full backfill and canonical bronze paths (`1.0.0_SA_CTO`, 2026-10-20 ~01:1xZ)

**Brief:** `docs/briefs/nfra-schwabbf-schwab-masters-backfill-canonical-paths-brief-20261020.md` @f0e33a4317 (`4.0.0_SA_CRO`, 235 lines,
13,620 bytes). **Order:** Andrew-direct ~21:0xZ 2026-10-19 (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261019_210xZ_SCHWAB_COTTONWOOD_MASTERS_PULL_AND_BACKFILL.md` @c031634941):
"we need to start pulling all of these and also getting as much backfill as we can from them. Furthermore, we need full backfill from the
0840 account ... organized in the opal-data-assets bucket in canonical LGIC_NAMING path form". **Placement:** the laptop owns it end to end
(Andrew via ms, 2026-10-20 01:02Z, laptop msg 109881).

**Held with Andrew, not ruled here:** (a) whether the other 210 entitled masters are pulled; (b) moving the stored partitions to the
builder form. Each outcome below holds under either answer to (b).

```
  FWD-1  An analyst reads master 08403355's balances for Schwab's oldest served
         business day, from Opal's own store, and the files behind it came from
         Schwab's history into the builder's address
         DONE WHEN  EXERCISED -- one trace: the oldest day pulled from Schwab, stored
                    at the builder's address, converted the existing way, and the
                    balances read. If Schwab's oldest day has moved by then, the
                    trace uses the oldest day it serves at the time
         ACCEPT     An analyst can say what that 0840 account held on its oldest
                    day without asking Schwab again, and the figure came from a file
                    Opal pulled from Schwab, not from a stand-in
         SOURCE     brief Part I, candidate thread

  FWD-2  Each of the three entitled Schwab account groups has every business day
         Schwab still serves
         DONE WHEN  EXERCISED -- the stored days read against Schwab's served days,
                    per account group
         ACCEPT     For 0824, 0833 and 0840, nobody can name a business day Schwab
                    still serves that Opal does not hold
         SOURCE     brief O1, Part VI

  FWD-3  Anyone can read which days are held, per account group and file type
         DONE WHEN  EXERCISED -- the record is read and agrees with the store
         ACCEPT     An engineer or ops person can see, for each account group and
                    file type, which business days are held and which Schwab served
                    but Opal lacks, judged by the trading calendar; it sends nothing
         SOURCE     brief O2

  FWD-4  A Schwab file is found where the naming builder says it is, and only
         there
         DONE WHEN  APPLIED -- every stored Schwab raw file sits at the builder's
                    address, with no second form beside it
         ACCEPT     Someone who only knows the naming builder finds any stored Schwab
                    raw file on the first try, and never finds the same day stored
                    two different ways
         SOURCE     brief O3, Part III second test

  FWD-5  Every report built from Schwab data gives the same answer for an already
         stored day before and after the change
         DONE WHEN  EXERCISED -- sampled days rebuilt after the change and compared
                    with the figures from before it, read once at the change and not
                    kept running afterwards
         ACCEPT     The day after the change, nobody can find a holdings, balance or
                    activity figure for an already stored day that differs from the
                    day before
         SOURCE     brief O4, Part III third test

  FWD-6  Each new business day lands in the builder's form by itself
         DONE WHEN  EXERCISED -- a scheduled daily pull lands its day at the
                    builder's address
         ACCEPT     A new day's Schwab files appear where the builder says, with no
                    later fix-up step
         SOURCE     brief O5

  FWD-7  When Schwab opens a Cottonwood account group to Opal's login, it starts
         flowing, daily and history, with only its setup entry added
         DONE WHEN  EXERCISED -- QUALIFIED WAIT: only Cottonwood and Schwab can open
                    the four account groups to Opal's login (today they are absent
                    from its list and a download returns nothing); needs Andrew's
                    word that the wait is accepted
         ACCEPT     The day Cottonwood says "Schwab has opened them", the honest
                    answer is "it is landing", and nothing new had to be built
         SOURCE     brief O6, Part III fourth test
```

## CONFIRMED by Andrew 2026-10-20 ~13:0xZ

"1.) Yes as written. 2.) Yes, rec is accurate. 3.) We don't care about these at this time."
FWD-1..7 are confirmed as written, and FWD-7's qualified wait is accepted. (b) The stored-partition move is YES. (a) The other 210 masters
are OUT OF SCOPE. Record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_130xZ_NFRA_SCHWABBF_DONE_WHEN_CONFIRMED_PATH_MOVE_YES_210_MASTERS_OUT.md`.

## Reachability

- **Reachable by working: FWD-1 to FWD-6 (6 of 7).** FWD-4 and FWD-5 need Andrew's word on (b) before they are cut, because they move
  stored input.
- **Qualified wait: FWD-7**, on Cottonwood's and Schwab's entitlement.
- **Time-sensitive, measured 2026-10-20 01:09Z:** Schwab's floor still read 2023-10-17, but the Eastern business date had not rolled since
  the first read (2026-10-19 21:21Z). If the window rolls, the oldest 0824 days are lost one per business day until pulled. The first
  enrichment is to re-read it after the 2026-10-20 delivery.

## Provenance

- GROUNDED ON: the brief above, read in full; the record @c031634941; this seat's floor re-read at 2026-10-20 01:09Z (SSM, read-only).
- NOT READ: the task-order register and any PRD (none exists).
- NOT YET LANDED IN A PRD. It goes under the section `ENDPOINT (step 2, /endpoint --forward)` of
  `org/missions/D8/NFRA/NFRA_SCHWABBF/prd/NFRA_SCHWABBF_PRD.md` at L4.

-- 1.0.0_SA_CTO (laptop)
