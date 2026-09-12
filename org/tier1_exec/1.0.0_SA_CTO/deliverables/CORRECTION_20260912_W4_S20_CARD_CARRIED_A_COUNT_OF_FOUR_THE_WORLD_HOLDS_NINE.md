# CORRECTION 2026-09-12 ~01:4xZ -- the W4-S20 card put a count of FOUR in front of Andrew; the world holds NINE

**Author:** `1.0.0_SA_CTO`. **Class:** this seat's own defect, on a SOVEREIGN card for an
UNRECOVERABLE act. **Status of the act:** NOT TAKEN. Nothing was deleted. The bucket is unchanged.

## WHAT HAPPENED

At 01:17Z this seat put card 2 of 4 to Andrew: *"Do the four noncurrent S3 versions go too?"* He
approved it at ~01:2xZ (*"All recs approved"*). It was routed to `2.0.0_SA_COO~B` at 01:25Z with an
explicit stop condition: *"If the row's four VersionIds do not resolve to exactly four objects when
you go to take it, STOP and come back rather than reconciling it yourself."*

`2.0.0_SA_COO~B` ran the pre-act read, hit the stop condition, and **refused the act** (row
`IRPT_BCKEND-S41`, BLOCKING/ARMED, disarm owner `1.0.0_SA_CTO`, at `ede2f4099b`).

## RE-MEASURED AT THIS SEAT, because a number that was wrong once does not get relayed twice

`aws s3api list-object-versions --bucket opal-data-ycharts --prefix
firms/49financial/generations/GENIBS14SYN/attempts/1/exports/` -- rc=0, 8808 bytes,
`IsTruncated: None` (so the page IS the population).

**DENOMINATOR: 10 versions, 5 delete markers, 5 distinct keys.**

| key | noncurrent versions | named by W4-S20 |
|---|---|---|
| `r1/report.pdf` | **3** (43848 B each) | 1 |
| `v0-11-overview/report.pdf` | **2** (41859 B each) | 1 |
| `v0-11-comparison/report.pdf` | **2** (41859 B each) | 1 |
| `v0-11-multicomp/report.pdf` | **2** (41859 B each) | 1 |
| **the four synthetic export PDFs** | **9** | **4** |
| `probe/probe.txt` | 1 (5 B) | 0 -- not an export PDF, out of scope |

`2.0.0_SA_COO~B`'s count is confirmed exactly. **Nine, not four. The four named VersionIds are all
live and all resolve** -- so the enumeration was not stale, it was INCOMPLETE.

## ⛔ WHY THE STOP WAS RIGHT EVEN THOUGH THE LETTER PERMITTED PROCEEDING

The stop condition as this seat wrote it was *"if the row's four VersionIds do not resolve to exactly
four objects"*. They DO. Read narrowly, `2.0.0_SA_COO~B` could have proceeded. **It refused anyway,
and its reason is better than my condition:** deleting exactly those four leaves FIVE retrievable
versions of the same four PDFs, so the qualifier the whole call exists to remove would STILL STAND
after an irreversible act. An unrecoverable act that does not achieve its stated purpose, taken on a
count wrong by five, is not a partial success.

>> **MY STOP CONDITION WAS KEYED TO THE RESOLVABILITY OF THE NAMED SET, NOT TO THE COMPLETENESS OF THE
   SET.** Those are different questions and only the second one protects the act. A boundary written
   around the members cannot detect that the enumeration of members is short -- which is the very
   failure it was written to catch, one grain down. <<

## THE DEFECT IS MINE, AND IT IS NAMED PRECISELY

Not "COO~B's row was wrong". The row was complete for the instrument that produced it: **IB-rt-8
re-ran the render, so each key accumulated versions, and the pre-act evidence was a HEAD-OBJECT read
per key -- a head read returns ONE version while a versioned key holds MANY.** The instrument answered
a narrower question than the card asked of it.

**What was mine:** I carried that count into a SOVEREIGN CARD for an UNRECOVERABLE ACT without
measuring it. Rule 22 puts an act on the world at DISCRIMINATION; the never-widen rule says to COUNT
THE WRITERS OF THE NAMED PROPERTY and PRINT the number. One `list-object-versions` -- the same command
run above, taking under a second -- would have put NINE on the card the first time.

**And Rule 24's subtraction clause is the direct remedy and would have caught it:** the authorized set
was written as a FORWARD LIST of four remembered VersionIds instead of as *the printed denominator of
versions on those keys MINUS what is excluded*. A forward list cannot lose a member without the count
disagreeing -- but only if a count was ever taken.

## WHAT IS OWED

The corrected number goes back to Andrew as a choice he can actually make. He approved deleting four
things **believing that made them gone**, and on the corrected count it does not. Re-asked at
~01:4xZ. `2.0.0_SA_COO~B` is not choosing and has not been asked to.

## THE CLASS -- FOURTH INSTANCE TONIGHT, FIRST TO REACH AN IRREVERSIBLE ACT

`S38` a Terraform root holding two cells' desired state; `S39` a zip carrying two cells' code;
`W4-S28` a coordinate no certification leg inspects; and this, a versioned key holding more versions
than the head read that enumerated it. **A SCOPE THAT ENUMERATES ITS MEMBERS CANNOT SEE WHAT THE
ENUMERATION MISSED.** `2.0.0_SA_COO~B` carries all four into the L10 slug as one finding, and this
record is the CTO-side half of it.
