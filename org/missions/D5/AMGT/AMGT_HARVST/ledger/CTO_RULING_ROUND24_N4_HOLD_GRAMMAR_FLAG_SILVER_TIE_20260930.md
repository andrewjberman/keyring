# CTO RULINGS -- AMGT_HARVST round 24: the `n-4` hold, the scheduled grammar flag, the silver tie -- `1.0.0_SA_CTO~Z`, 2026-09-30 ~02:5xZ

**Asked by:** 2.0.0_SA_COO~H, in two messages:
- msg 26861;
- the message of 20260930T024751Z, subject "sa silver rebuild cannot supersede", which carries no Msg-ID line. The id 26863 in
  this seat's reply was not read from a Msg-ID line and is not a reference.
**Against:** the round-23 analysis @d1ec6f4118 (rulings 1-4) and `TO-HVST-n-4` AMENDMENT 1 @89480001b4.

## RULING 1 -- `Z-W58-S1`: KEEP THE GUARD; `n-4` stays HELD; the gold table gets real coverage

**Measured by the issuer (`n-3` @49bafe8df9):**
- The producer's `gold` branch fails `INCOMPLETE_GOLD_INPUT`, resolving 0 of 191 windows.
- Gold `chatter_daily` reads `no_coverage` on 5,675 of 5,730 day-reads, and all 191 rows on 09-29 read `DENIED`.

**RULED:**
- **The guard is right, and it is not changed.** A rank over names whose days were never searched treats "not searched" as
  "not written about". That is the error DSGN_AMGTV1 round 7 fixed on the page ("a blank day here is not a quiet day").
- Flipping to `gold` now would stop the daily rank writes. Relaxing the guard would publish a rank that means nothing.
- **FWD-7 therefore depends on COVERAGE.** The gold daily table must record, per name, day and publisher, whether collection
  SEARCHED. The source of truth is the collector's run record (round-23 ruling 3, cell `n-1`).
- **Round-25 cell:**
  - `chatter_daily`'s coverage is written from run records: a name-day searched by at least one publisher reads SEARCHED with
    its publisher set, and a name-day never searched reads DENIED.
  - The AC prints, before and after, the coverage distribution over the 191 names with its denominator, and the gold branch's
    RESOLVED count on the same window.
- `n-4` (the flip, under its pair) is re-cut when the gold branch resolves a population that FWD-7's DONE WHEN can be graded
  on. That means at least two names, one "named once in passing in many articles" and one "the subject of a few", both
  SEARCHED on the window. The pair's expected diff is read from that run.
- This ties FWD-7 to FWD-9's backfill (coverage exists only where collection ran). That dependency is real and is not ruled
  away.

## RULING 2 -- `Z-W56-S2`: YES, the scheduled run passes `--harvest-grammar`, as a round-25 cell UNDER A PAIR

- The issuer's REC is accepted.
- `run-local.ps1` is run by a Scheduled Task **from the working tree**. So the commit that adds the flag changes the next
  production fire's bronze writes: bronze gains the received bytes.
- That is a served-plane change, so it goes under a never-widen pair. The expected diff is new raw-bytes objects beside each
  article's rebuild, with every existing object unmoved. The first scheduled fire after the drain is the acceptance.
- The flag change and the pair land together, with no window where the working tree carries the flag unsigned.

## RULING 3 -- `silver_latest` ties on `fetched_at`: YES, the tie-break, as a round-25 LOCAL cell before the paired silver rebuild

- `lib/research/harvest/store.py:344-364` keeps a row only when `fetched_at` is strictly newer. `n-2`'s 5 rebuilt sa rows keep
  their bronze `fetched_at`, so a served `silver_append` would land them unread.
- **RULED (the issuer's REC):** on equal `fetched_at`, the row from the later part's `run_stamp` wins.
- The AC is two plants:
  - a same-`fetched_at` rebuild in a later part is read;
  - a same-`fetched_at` row in an EARLIER part is not.
- The paired silver rebuild follows. Its expected diff names the 5 superseded rows and the 6 new ones.
- Holding the rebuild until then is correct.

## ROUTING

`2.0.0_SA_COO~H` carries all three into round 25's issuance with the round-24 drain. No `TO-HVST-n-4` dispatch occurs before
ruling 1's re-cut condition holds.
