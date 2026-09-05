# ANDREW-DIRECT 2026-09-04 ~13:00Z -- /open-calls at `1.0.0_SA_CTO~Z`, ALL FIVE APPROVED

**Channel:** Andrew, in person at the `1.0.0_SA_CTO~Z` terminal (site Z), immediately following
`/open-calls` run at this seat.
**Time:** 2026-09-04 ~13:00Z.
**Recorded by:** `1.0.0_SA_CTO~Z`, same turn as receipt, per `org/XXX.md`
("ANY AGENT RECEIVING AN ANDREW-DIRECT INSTRUCTION RECORDS IT DURABLY AND BROADCASTS IT -- SAME TURN").

---

## HIS WORDS, VERBATIM

> Approved for all of these

That is the whole of it. Five words, answering a five-card `/open-calls` frame.

---

## WHAT "ALL OF THESE" REFERS TO -- THE EXACT FRAME PUT TO HIM

⛔ **SCOPE IS THE FIVE RECS AS WRITTEN, NEITHER WIDER NOR NARROWER.** He answered a card frame; the
cards' RECs are the referent. This record reproduces them so no later reader has to reconstruct
what was approved from a five-word answer. `org/XXX.md`: SURFACE, DO NOT ADJUDICATE.

| # | Class | The call | The REC he approved |
|---|---|---|---|
| 1 | BLOCKING | Run today's two skipped Bloomberg legs? PERISHABLE | **YES** -- run `etf_daily_pull.py` + `etf_constituents_pull.py`, `ETF_RUN_CLASS=scheduled` |
| 2 | BLOCKING | Are the duplicated SPHY/SPYM rows on 2026-08-18 intentional split lots? | **(a) INTENTIONAL** -- and harden the loader to SUM them |
| 3 | CARRIED | May an agent mint a short-lived token for the TEST FIXTURE identity? | **(a) YES, BOUNDED** -- fixture identity only, short TTL, read-only, mint DISCLOSED in the proof |
| 4 | CARRIED | Does the daily security digest get EMAILED, or stay a FILE? | **Keep it a FILE** -- no new channel; the sentinel email already carries the urgent events |
| 5 | CARRIED | Object Lock (governance mode) on the evidence store's `cases/` prefix? | **ON** |

---

## CALL 1 -- EXECUTED IMMEDIATELY, AND VERIFIED ON THE ARTIFACT

Fired at once because the capture is current-day-only and unrecoverable after today
(`integrations/bloomberg/READ_HERE.md` s.4: *"There is no backfill. Every uncaptured day is gone
permanently."*).

```
etf_daily_pull.py          EXIT 0   7 objects
etf_constituents_pull.py   EXIT 0   9 objects
```

⛔ **NOT TAKEN FROM THE PRODUCERS' OWN SUCCESS LINES.** Verified by `s3api list-objects-v2` against
`s3://opal-data-etfs/bbg/2026-09-03/`: **16 objects**, 7 at `13:01:32Z` and 9 under `constituents/`
at `13:02:17Z`, every one non-zero size. Counted with `length(Contents)` rather than `KeyCount`,
which is absent when the CLI auto-paginates.

Both legs landed under as-of **2026-09-03**, which is correct: it is `prev_trading_day` of 2026-09-04.

Leg 1b returned `refused:entitlement` on all four tickers -- **that is the EXPECTED and documented
state**, not a fault (READ_HERE.md s.4: BQL is refused at service level; the issuer CSV is the
designed fallback). Leg 2 filled from `silver/holdings/2026-09-03.parquet` for all four funds.

---

## WHY CALL 1 EXISTED AT ALL -- THE DEFECT IT EXPOSED

The 07:00 scheduled run failed inside the models leg (a duplicated-row `ValueError`, Call 2's
subject). `scheduled_daily_pull.cmd:129` sends a failed pull to `goto :prune`, and `:prune` (:281)
sits AFTER both `:etf_leg` (:210) and `:cons_leg` (:261) -- so a models fault skips both landing
legs.

⛔ **THE FILE CONTAINS BOTH SIDES OF THE CONTRADICTION, 50 LINES APART:**

- `:195-200` -- skipping is deliberate *"in those cases **Bloomberg is unreachable or broken**, so
  the ETF pull would fail for the same reason and add noise, not information."*
- `:252-256` -- *"the derived layer this script pulls is CURRENT-DAY-ONLY at the source -- an
  uncaptured day is gone permanently. **Skipping it because a sibling leg failed would convert one
  leg's fault into two legs' permanent data loss.**"*

The second comment names precisely the harm the first branch causes. The guard is correct for the
failure mode it was written against; **today's failure was a spreadsheet, and Bloomberg was up** --
now proven twice over, because both legs just ran clean against it. `READ_HERE.md` s.3 (*"a leg
failing must never fail its siblings"*) and s.4:155 (*"this is why the constituents leg runs even
when a sibling leg has failed"*) side with the comment, not the code.

Found by `0.0.3_BG_BBGTerminal` (report 20260904T120113Z), corroborated at source by this seat.
`:185` names the work order owner as `1.0.0_SA_CTO`.

---

## STANDING EFFECT OF EACH APPROVAL

1. **Call 1 is SPENT, not standing.** It authorised today's two legs. A future skipped day is a
   fresh vendor-egress call unless and until the `:129` branch is fixed, which is the real remedy.
2. **Call 2 is a SEMANTIC ruling with a code consequence.** Duplicated `(date, ticker)` rows in the
   model templates are INTENTIONAL SPLIT LOTS and the loader sums them. Evidence that made it the
   right read: the raw 2026-08-18 column sums to EXACTLY 1.0 with both pairs present, and
   `drop_duplicates` breaks it to 0.9575.
3. **Call 3 is a BOUNDED STANDING PERMISSION.** Fixture identity ONLY -- never a real partner human's
   session -- short TTL, read-only probes, and **the mint disclosed in the proof rather than presented
   as a password login**. Originated by `2.0.0_SA_COO~Z` (msg 19983) and carried here.
4. **Call 4 CHANGES NOTHING and that is the ruling.** C-6 stays a FILE in the evidence store. The
   digest EMAIL remains a carried option and is NOT authorized. The standing alert moratorium is
   undisturbed.
5. **Call 5 amends C-8:** Object Lock, governance mode, on `cases/` in `opal-security-evidence`.
   That bucket is a round-2 build, so this is an INPUT to the cell that creates it, not a change to
   anything live.

---

## ROUTING

Broadcast same turn to `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z`, `0.0.0_AB_MSTR~Z`.
Calls 3, 4 and 5 land in `NFRA_OPSEC202609` and are `2.0.0_SA_COO~Z`'s to carry into the cells
(C-6 unchanged, C-8 amended, the fixture-token permission recorded against the faces filing
`UNCOMPUTABLE-BY-CONSTRUCTION` on a login-dependent limb).
Call 2 and the `:129` branch are this seat's work order.
