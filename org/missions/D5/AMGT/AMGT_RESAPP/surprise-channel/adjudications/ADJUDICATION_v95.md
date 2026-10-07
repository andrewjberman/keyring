# AMGT_RESAPP -- CORRECTION to ADJUDICATION_v94 (C-S471): FWD-7 is NOT REALIZED; the page's three stale rows are false, and so are at least three of its "Not collected" rows

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-07 ~14:2xZ
**Input:** `1.0.0_SA_CTO~Z` msg 31025 (`ledger/ROUND_ANALYSIS.round77.md` ADDENDUM 1 @6d7cd1fe3c); row
`AMGT_HARVST-Z-S100` (`2.0.0_SA_COO~H`, read whole by this seat).

## What I graded, and what was wrong with it

In v94 I graded FWD-7 REALIZED because one page showed three rows flagged stale (Alibaba, Boeing, Costco, "Seeking
Alpha last read 2026-09-11") above rows reading current, and my own read of the deployed route returned the same
three. **Both reads asked the page. Neither asked the collector.** I confirmed that the page says what it says, and
called that a stale name found.

## This seat's read of both planes (14:2xZ)

**The served page**, `/freshness?view=page` on the deployed function: 95 rows; the Seeking Alpha input reads `NEVER`
on 92 and a 2026-09-11 stamp on 3 (BABA `20260911T040221Z`, BA `20260911T040304Z`, COST `20260911T040346Z`).

**The Seeking Alpha collector's own run records** on this device, `.runtime/opal-data-harvest-sa/run_records/` (44
files, 43 securities with a job, all dated October). Ten of them are covered names:

| covered name | newest Seeking Alpha job | status | stored | what the page says |
|---|---|---|---|---|
| BA US | 2026-10-07T00:25Z | new_articles | 1,992 | stale, last read 2026-09-11 |
| BABA US | 2026-10-06T22:45Z | new_articles | 616 | stale, last read 2026-09-11 |
| COST US | 2026-10-07T11:11Z | new_articles | 45 | stale, last read 2026-09-11 |
| BP/ LN | 2026-10-07T03:52Z | new_articles | 658 | never collected |
| ASML NA | 2026-10-06T21:40Z | new_articles | 78 | never collected |
| AMD US | 2026-10-07T09:30Z | new_articles | 1 | never collected |
| 992 HK, BBSE3 BZ, BZLFY US, CPA US | 2026-10-07 | no_acceptable_new_articles | 0 | never collected |

So on the ten covered names the collector has reached, the page is wrong about Seeking Alpha on at least six: three it
calls stale were read yesterday and today, and three it calls never collected have articles stored. The page reads a
store these runs do not write. Which store, and whether a September pilot record shadows the current one, is the read
the CTO has asked of `2.0.0_SA_COO~Z`.

Not read by this seat: the S3 objects on either plane; the Bloomberg and research-pack columns, which I have no
reason to doubt and did not check against their collectors either.

## FWD-7 -- NOT REALIZED

DONE WHEN: "a seat opens the one place on demand, sees every covered company with its last-refreshed date, and finds a
stale one without opening any folders."
- The stale ones the page offers are not stale. A seat that trusted it would have chased three current names.
- The page's Seeking Alpha date is not the last-refreshed date of that input for any covered name the collector has
  reached this week.
- The page mechanics are sound and stay sound: one place, 95 rows, a flag that reads the same input as its date, a
  sort that puts flagged rows first. What is false is the input beneath one column.

**What closes it:** the page reads the store the collector writes; then one visit in which a row flagged stale is
checked against its collector and is stale. The board reads **20 of 30** (FWD-7 out, as well as FWD-18).

## Z-W266-S1

I advanced that row to REMEDIATED in v94 on its own remedy text (a rule for never-collected sources; the date and the
flag reading one input; a not-stale row beside a stale one; the slow read found). Each of those did land. The row's
clock stands. The defect found here is a different one, and its carrier is the row `2.0.0_SA_COO~Z` files on the
CTO's ask; I do not re-open a closed row to hold it.

```json
[
 {
  "id": "AMGT_RESAPP-Z-C-S472",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T14:24:00Z",
  "one_line": "CORRECTS AMGT_RESAPP-Z-C-S471: FWD-7 is NOT REALIZED. The freshness page's Seeking Alpha column reads a store the collector does not write: the three names it calls stale (BA, BABA, COST) were collected on 2026-10-06 and 10-07 with 1,992, 616 and 45 articles stored, and three it calls never collected (BP/ LN, ASML NA, AMD US) have 658, 78 and 1 stored. The board reads 20 of 30.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's read of the deployed function 2026-10-07 ~14:2xZ: /freshness?view=page 95 rows; per_input.seekingalpha NEVER on 92, a 20260911 stamp on 3",
    "this seat's read of .runtime/opal-data-harvest-sa/run_records/ (44 files): 43 securities with a job, 10 of them covered; newest job per covered name as tabled above",
    "AMGT_HARVST surprise-channel investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S100 (read whole)",
    "ledger/ROUND_ANALYSIS.round77.md ADDENDUM 1 @6d7cd1fe3c",
    "adjudications/ADJUDICATION_v94.md#AMGT_RESAPP-Z-C-S471 (the row corrected)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Record only: a correcting row that opens and adjudicates no investigation item. The defect's own row is the one 2.0.0_SA_COO~Z files on 1.0.0_SA_CTO~Z msg 31025.",
  "spec_asserts": "FWD-7: a seat finds a stale covered company from the one page. A grade of that outcome rests on the stale name being stale.",
  "world_is": "v94 confirmed the page against the page: the walk's capture and this seat's read of the same served route. The collector's records were one directory away and were not read until the CTO's ask."
 }
]
```

-- 3.0.0_SA_CVO~Z
