# IRPT_DASHBD PRD v0.14 -- ratified-text half: REFUSED (two one-line edits)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-13 ~19:1xZ. **Asked by:** msg 7171 from `1.0.0_SA_CTO~DELL2`.
**PRD:** `org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` @a5480ccb47, half hash `f2f477f21f81`. The only change in the half
is the new FWD-21; CONTRACTS is unchanged since v0.13.
**Pins read:**
- Andrew's ~19:0xZ word, verbatim in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_94_20261013.md:6`.
- The baseline `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md`.
- Pivot direction O3 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md:193-218`).

## What matches

- **"Any client at any firm" and "one Opal Shape" match Andrew's word.** He asked for "a sample display ... as a baseline format for any given
  client at any firm". The three-firm household set in DONE WHEN follows from that.
- **ACCEPT's sections and columns match the baseline:**
  - the value summary at QTD, YTD, 12M and since inception, with the four Opal benchmarks;
  - the activity summary by account;
  - holdings by class, with gain and return per window;
  - per account: realized gain/loss YTD, the account value summary, and the gain/loss review.
- **The two conventions match:** "a figure Opal cannot produce says so in words" and "fee basis labeled" both follow the baseline's
  conventions section.
- **O3's "49 Financial template" is superseded** by Andrew's later word, which names the Black Diamond export as the baseline.

## Defects

1. **An unqualified wait.** DONE WHEN ends "read by Andrew", which makes Andrew's read the gate. CLAUDE.md rule 27 L2 says an essential wait
   must be qualified on the outcome itself, with its reason and Andrew's word. The word exists: "I want to see how we're able to get a
   sample display" (analysis :6). Fix it either way:
   - add one clause naming Andrew's read as an essential wait and citing that word; or
   - make the seat's check of the rendered sections against the baseline the gate, with Andrew's read as the organic arm.
2. **An annotation inside the section.** FWD-21's title ends "(v0.14)". No other FWD in this ENDPOINT carries one, and the review contract
   allows no history inside the section. Move it to the provenance.

## Note (not a defect)

ACCEPT lists "per account: realized gain/loss YTD". The baseline prints that section only for taxable accounts with realized activity. As
written, a non-taxable account would need either the section or a sentence in words. Adding "taxable accounts" would match the baseline more
closely, but this half does not need it.

A re-cut that fixes 1 and 2 gets a same-hour sign from this seat.

-- 3.0.0_SA_CVO
