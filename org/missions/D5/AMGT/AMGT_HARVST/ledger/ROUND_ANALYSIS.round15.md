# AMGT_HARVST -- ROUND 15 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~10:2xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26562, READ-acked, subject *"L10 SLUG AMGT_HARVST round 15 @698c4741c2"*,
citing `surprise-channel/adjudications/ADJUDICATION_v23.md`. The served rebuild ran under the pair `ba195dc1c6` (COO) +
`939395dd8d` (this seat) and was drained @`3cfbfb5147`.

**Round 15 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **Common-name aliases are served.** The CVO read the text around each of the 12 new matches: **12 of 12 are the company**, with 0
  river or rainforest hits. Ten are co-mentions (Amazon named as a rival or a stock inside another company's story). The tier gate
  places them B/C/D, and none forms or joins an event. The alias adds recall without adding false events.
- **The first HELD-OUT event is correct.** AMZN 2026-09-07 holds 3 articles (barrons A lead "Scene of Fatal Amazon Plane Crash in
  Miami Is 'Devastating'", wsj A, bbg B): one story about Amazon's own crash, with a naming lead. **It is a sample of one**, not a
  precision rate, and the >= 5-article multi-day shape stays **UNEXERCISED**.
- The CVO corrects its round-14 mechanism to the one this seat measured at round 14 (the matcher's missing name form, not a missing
  lead). Nothing further is owed.

## 2. THE CVO'S DECISION -- `Z-W41-S2`, the double count -- RULED: fix before `mention_score` is read as a magnitude

The matcher sums per alias, so one text span that several aliases match counts more than once. "Amazon.com Inc." is hit by
"Amazon", "Amazon.com" and "Amazon.com Inc", because a word-bounded "Amazon" matches inside "Amazon.com". This inflates
`mention_count` (for example 2 -> 10 on the 09-06 crash report) and the daily `mention_score`. It does not touch tier (title/lead
flags) or events. **Ruling: count each matched text span once, keeping the longest alias that covers it, with no overlapping
spans.** The rebuild of `article_security_mention` and `chatter_daily` moves served counts, so it goes under a never-widen pair that
names every moved security, both before and after. The pair also measures events (expected: 0 moved, since tier and flags are
unchanged; any event move is a finding).

## 3. FWD GRADES

`FWD-5` / `FWD-6`: NOT REALIZED, served half met. The page half is the timeline panel `92a2576254`, held by Andrew's *"lets hold
on pushes and merges for now"* (~20:3xZ 09-28, to `0.0.0_AB_MSTR~Z`). The others stand as `ROUND_ANALYSIS.round14.md` left them.

**On the rule's generality:** one held-out event is all today's harvest can give. More held-out reads wait on new captures, and the
Seeking Alpha capture (`w-2`) is blocked by the account's HTTP 402. That is not a cell to cut; it is the account holder's act below.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 16 in ONE issuance

| # | cell | note |
|---|---|---|
| 1 | **One text span, one count** (ruling above) | a longest-match, non-overlapping count; rebuild mention and daily under a pair (every moved security named, events measured as expected 0); JUDGMENT: the 09-06 crash report and two co-mention articles read as one count per actual mention |

**Fan-out:** 1 cell. **NOT cells:** more held-out reads (no new data); the event route (`Z-W39-S1`, still not wanted); the portal push
(Andrew's hold).

## 5. ACTS ONLY ANDREW CAN DO (cited; no decision is listed)
- Read the Seeking Alpha subscription state (`Z-W37-S4`, HTTP 402) [entitlement]. Restoring it re-opens held-out reads on new captures.
- Lift *"lets hold on pushes and merges for now"* for the timeline panel push [a hold set by name].

## Compiler Tools
The CVO's text reads of the 12 matches and its S3 event read (v23) taken as measurements; this seat's own round-15 rebuild
(`d2_check.py`, in the CTO half @`939395dd8d`) as the before/after reference.
