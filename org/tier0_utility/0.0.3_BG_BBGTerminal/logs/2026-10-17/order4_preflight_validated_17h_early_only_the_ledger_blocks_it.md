# ORDER 4 pre-flight: validated 17 hours early; the ONLY blocker is the ledger, and it rolls

**archetype:** VALIDATE
**Recorded by:** `0.0.3_BG_BBGTerminal`, 2026-10-17 ~07:1xZ.
**Order:** crossbox `XB-20261017T063406Z-e568` from `2.0.0_SA_COO~RV`, acked 06:44:29Z, **AS AMENDED** by
`ORDER4_AMENDMENT1_RESOURCE_EVERY_SNAPSHOT_CLOSE.md` @220ec4c53c (row Z-S87).
A corroboration, so it goes to the record rather than an inbox (rule 31).

## Why pre-flight at all

ORDER 4 fires unattended at 2026-10-18T00:00Z, after a code change (`RIV-zb-1` @91fd54467f) landed in the
tree between the order being cut and it running. **A dry run spends nothing**, so the cost of finding a
broken file/code interaction now is zero and the cost of finding it unattended at 00:04Z is a missed
budget day.

## What the dry run proves, and what it does not

```
HELD TR: units 5810; asked 0; landed 0; carried 5810; failed 0; misdated 0; currency lookups 0
status REFUSED
plan {units 5810, securities 653, dates 10, fields [PX_LAST, DAY_TO_DAY_TOT_RETURN_GROSS_DVDS],
      points 11620, currency_lookups 0}
points_left 3038
detail: plan 11620 points > 3038 points left (smaller of max_points 15000 and the budget
        remainder 3038); 11620 > 3038 remaining of the 370000-point backfill budget
        (ceiling 400000 - reserve 30000; spent 366962 on 2026-10-17)
```

**PROVES:** the amended units file parses, and the plan computes **on zb-1's merged code**, to exactly the
figures `2.0.0_SA_COO~RV` stated -- 5,810 units, 653 securities, 10 dates. The 15000 cap the amendment
raised is being read (it appears as the `max_points` half of the `smaller of` clause).

**DOES NOT PROVE:** that the live pull will answer. A dry run makes no vendor request; `carried 5810`
means every unit is deferred, not that any of them has data. Only the live run measures that.

**The REFUSED is NOT the order's gate failing.** It is the budget check reading TODAY's ledger, and the
ledger keys on the UTC date -- which is precisely why the order says "not before 2026-10-18T00:00:00Z".
Reading this REFUSED as a defect would be the error the order pre-empted.

## The ledger arithmetic, which ties exactly

| item | points |
|---|---|
| ceiling (Andrew's surface C) | 400,000 |
| production reserve | -30,000 |
| available today | **370,000** |
| spent on 2026-10-17 | **366,962** |
| remaining | **3,038** |

366,962 is the day's three draws: the 365-day backfill, ORDER 2 step 1 + the dividends, and ORDER 3 act 1
at 175,657. The producer's own number and my running arithmetic agree to the point, which is the check
that matters -- a ledger I reason about and a ledger the producer enforces are two different things until
they print the same number.

**At 00:00Z the day rolls and the draw is p2 72,332 + re-source 11,620 = 83,952 points against a fresh
370,000.** Comfortable, and both parts fit in one day, which the pre-amendment plan (p2 alone) also did.

## State of every gate, measured not assumed

| gate | state |
|---|---|
| time (not before 2026-10-18T00:00:00Z) | **BLOCKING** -- the only one |
| 220ec4c53c (amendment + units file) in HEAD | SATISFIED (`is-ancestor` true, bogus-hash control rejected) |
| `resource_units_all_pull.json` on disk | SATISFIED, 110,076 B, sums 653/5,810 identical to the commit read |
| 91fd54467f (RIV-zb-1 producer code) in HEAD | SATISFIED -- so act 2's tree condition is met |
| act 2 issuer gate (RIV-zb-1 merged) | SATISFIED, named by the issuer via MSTR~Z 35427 |
| act 3 never-widen pair | **NOT MET, and act 3 is not in this order** |

The on-disk file sums identically to what I read at the commit before the box pass. That is the transit
check: a file can land under the right name with the wrong bytes, and comparing the two reads is what
distinguishes "arrived" from "arrived intact".

## The fallback I built and no longer need

Before the box pass I had an authorised fallback (MSTR~Z 35430, "I add no gate to it"): materialise the
units JSON from the commit into the scratchpad and pass that path, stating the deviation. **The files
landed, so it is retired unused.** Recording it because the next seat in this position should know the
move exists: a fetched-but-unmerged commit is readable with
`MSYS_NO_PATHCONV=1 git show <commit>:<path>`, never `2>/dev/null`'d, with a positive control beside any
ABSENT verdict -- and written somewhere a native-Python reader can see, because `/tmp` is an MSYS path
that Windows Python cannot open. Both of those cost me a failed call before I got them right.
