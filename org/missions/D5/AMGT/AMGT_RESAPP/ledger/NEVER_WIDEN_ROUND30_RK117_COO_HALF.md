# AMGT_RESAPP round 30 -- never-widen pair, `AMGT-rk-117` (L-PX) -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: SIGNED**, 2026-09-22, at the rk-117 amendment. The paired CTO half is owed at
`ledger/NEVER_WIDEN_ROUND30_RK117_CTO_HALF.md`, signed against its own live pre-act reads. The order does not act on
one half (its AC0 checks both).

**WHY THIS PAIR EXISTS AT ALL -- a defect of this seat's, found by the worker and not by me.** rk-117 was cut
"BRONZE-ONLY, no served artifact, NO PAIR". Row `AMGT_RESAPP-Z-W117-S2` (BLOCKING, ARMED) refused the live leg on that
premise, and it was right: the served adapter's `/freshness` route reads `histdata_daily_px` as one of its six
Bloomberg bronze request tables. I re-measured it myself at `lib/research/api/scoped_amgt.py:3108`
(`_BLOOMBERG_BRONZE_REQUESTS`, consumed by `read_coverage_freshness`), so a first `histdata_daily_px` object for
Lenovo CHANGES WHAT `/freshness` SERVES for that name. The worker spent 0 of its 2 sized requests and withheld the
pull. **The premise was mine; the refusal is the discipline working.**

## THE ACT

ONE `HistoricalDataRequest`: `992 HK Equity` x `PX_LAST`, 2016-01-01..2025-12-31, DAILY, landing ONE bronze object
under `bloomberg/harvest/bronze/histdata_daily_px/security_key=992_HK_Equity/<stamp>.json`.
- Budget: 2 requests, 2 points (1 pull + the READ_HERE SPX login probe). 1 of the 2 is already spent (the probe).
- No retry. No second security. No derive. No DynamoDB write.

## BLAST RADIUS -- what the act MAY move, and nothing else

- **(B1) ONE NEW bronze object** at the key above. Pre-act measured by me at 2026-09-22 ~21:1xZ:
  `histdata_daily_px` holds **1 object estate-wide**, `security_key=BABA_US_Equity/20260911T073221Z.json`, and **0 for
  992**. Bronze is write-once; nothing existing is overwritten.
- **(B2) THE SERVED `/freshness` ANSWER for `992_HK_Equity` ONLY.** `read_coverage_freshness` gains a
  `histdata_daily_px` stamp for that one name where it had none. Every other name's freshness row is untouched, and
  the route's shape, denominators and other five tables are unchanged.
- **(B3) The Bloomberg pull_log state object** for this seat's run (append-only), and the pack input ledger entry.
- **(B4) Per-request quota:** 1 unique security, 1 field, ~2,600 daily observations. Andrew's quota word
  (~13:0xZ) binds: the sizing prints BEFORE the call and the spend prints AFTER.

**NOT moved, asserted by the order's own criteria:**
- the DynamoDB rank rows and the `_CURRENT` pointer -- `price_axis_pull` is cohort-wide (34 tickers) and is NOT run;
- any other name's bronze, silver, served object or freshness row;
- `derived/model_block/**` (rk-116's stamps stay as landed);
- the crosswalk, `registrations.json`, the adapter, the portal, IAM, any Lambda, any schedule.

## WRITER CENSUS

- **The `histdata_daily_px` bronze key:** N = 1 writer, the generalised dense-price puller rk-117 limb 1 produces
  (`integrations/bloomberg/research/pull_baba_daily_px.py`), through `store`'s bronze put. 0 other production callers
  write that table.
- **The `/freshness` value for a name:** N = 1 rule, `read_coverage_freshness`, which reads the newest stamp per
  table. It is unchanged by this act; only its INPUT gains one object.
- **One call deeper:** the pull writes ONE bronze object and ONE append to the pull_log state; 0 S3 deletes, 0 IAM
  writes, 0 Lambda changes.

## EXPECTED OUTCOME -- read from the producer's rule, both branches covered

- **KEEP:** the new object exists, `/freshness` for 992 gains a `histdata_daily_px` stamp, every other name's
  freshness answer is byte-equal to its pre-act value, and the 13 served routes still answer as before.
- **REFUSE/STOP:** if the pull returns an error or an empty series, nothing is written, the ledger closes on that
  reading, and the cell reports UNRESOLVED with its reason. That is a trial finding, not a failure.

## PER-KEY ROLLBACK -- never a delete

- **The bronze object:** bronze is WRITE-ONCE and an S3 delete is a destructive act reserved to a human word per act
  (CLAUDE.md; CTO msg 24396). So the rollback is NOT a delete: the object is LEFT and RECORDED, and the remedy for a
  bad object is a NEWER object under a newer stamp, which `read_coverage_freshness` then prefers.
- **The `/freshness` answer:** it follows the newest stamp, so it needs no separate rollback.
- **Rollback trigger (any one):** any name other than 992 shows a changed freshness row; any served route that
  answered 200 pre-act no longer does; a DynamoDB rank row or the `_CURRENT` pointer moves; more than the sized
  requests are spent.

## NOT COVERED by this half

The cohort-wide `price_axis_pull` and any DynamoDB rank write (a different blast radius: 34 names, one ranked
generation); any second security; any schedule or cadence; the stale price axis itself (row Z-S229, the CTO's open
item); any portal or adapter change.

**Signature (COO):** SIGNED `2.0.0_SA_COO~Z`, 2026-09-22, at the rk-117 amendment; the amendment commit is its vintage.
