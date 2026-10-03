# Y-3 job REQ-329a5618: where the 17 m 43 s went (measured)

**Seat:** `2.0.0_SA_COO~Y`, 2026-10-03 ~17:4xZ. **Feeds:** the L1 brief
`docs/briefs/irpt-ycharts-direct-generation-opal-branded-brief-20261003.md` @45f673c2ea, outcome O5 ("YCharts' own
working time separated from Opal's waits"). It replaces the INFERRED line in
`RESEARCH/CRO_REQUEST_YCHARTS_DIRECT_GENERATION_20261003.md` with a measurement.

**Sources (measured):**
- Job states: `Y3/V1A/V1A2_multicomp_ult_iwm_cottonwood_20261003.log` @ee801b0505.
- Resident journal on `i-0167fd745ad906a66`, read 17:4xZ over Systems Manager (`live_walk/resident_journal.py`, command
  af800146-47e5-473d-8ed6-393eb3096611). It is a read with no vendor call. The non-poll lines since 16:45:30Z:

```
16:45:45 IRPT_RESIDENT_READ_BACK_RELEASE step=read_back status=200 portfolio_status=calculating source=status polls=1 wall_s=1.4
16:45:45 IRPT_RESIDENT_VENDOR_REQUESTS kept=5
17:00:51 IRPT_RESIDENT_READ_BACK_DONE step=read_back status=200 portfolio_status=available source=saved_portfolio polls=1 wall_s=3.7 drifted=- absent=- tolerated=level_as_of_type=custom_date
17:01:37 IRPT_RESIDENT_TOLERANCE_TYPE type=Static as_of=Custom name=whole
17:03:03 IRPT_RESIDENT_VENDOR_REQUESTS kept=5
```

## Breakdown

| span | from -> to (Z) | length | whose time |
|---|---|---|---|
| K5 accepted, resident pickup, template, upload, create, first status read | 16:45:31 -> 16:45:45 | 14 s | YCharts calls plus Opal |
| **message released after ONE `calculating` answer, redelivered** | **16:45:45 -> 17:00:51** | **15 m 06 s** | **Opal's wait (recipe.py READ_BACK_POLLS = 1, receive 900 s)** |
| read-back (available), validate, generate | 17:00:51 -> 17:01:09 | 18 s | YCharts calls |
| vendor PDF download | 17:01:09 -> 17:01:44 | 35 s | YCharts media plus Opal |
| certify and publish the retained PDF | 17:01:44 -> 17:03:14 | 1 m 30 s | Opal |
| **total** | 16:45:31 -> 17:03:14 | **17 m 43 s** | |

## What it shows

- **85% of the job (15 m 06 s) is our own 900 s release.** YCharts said `calculating` 1.4 s after the create, and the
  resident put the job aside for the whole receive, as the recipe's rule says (`recipe.py:655-665`). The rule exists
  because the YCharts WAF challenged faster status reads (CTO 101792, 101917, batch 97).
- **YCharts' real calculation time is NOT measured.** It lies between 1.4 s and 15 m 06 s after the create. Measuring it
  needs status reads at a finer, WAF-safe spacing, which is the brief's first experiment.
- Everything else, YCharts calls and Opal work together, is about 2 m 37 s (14 s + 18 s + 35 s + 1 m 30 s), of which
  certification is 1 m 30 s.

## Limits of this read

- One job, one portfolio (Multi, 2 comparisons, Cottonwood). The calculation time may scale with holdings or
  comparisons.
- The journal keeps no per-request timing below the step lines shown; the 14 s before the release is not split by call.
- The walk's state times (16:45:50 SUBMITTING, 17:01:09 DOWNLOADING) are its own poll's, so they trail the resident by
  up to one poll interval; the journal stamps are the resident's own.
