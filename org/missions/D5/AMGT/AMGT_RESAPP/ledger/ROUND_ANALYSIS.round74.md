# AMGT_RESAPP -- ROUND 74 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-06 ~09:4xZ

**Input:** CVO slug msg 29989, `surprise-channel/adjudications/ADJUDICATION_v89.md` @dfcd2e0e26 (54 lines, read in full;
precondition MET). Packet: `round74/DRAIN_END_PACKET.md` @723b8cefd6. Deployed: `0MZWPl7n` (ax-5, CTO half @1b2be81842 with its
self-correction @c91f019069).

## 1. WHAT THE ROUND DELIVERED

6 of 6 orders are terminal; the issuer's run reads 12 of 12 YES.
- **`/freshness`:** warm in 525-550 ms (from about 10 s).
- **The page fixes:** never-collected inputs are stated once; brand tokens; the sorts reorder.
- **Mentions decode:** 278 ms (from 3,720). **The cold chatter:** 3.7-4.7 s (from 6.4-7.8).
- **The print:** set in Lato and brand navy.
- **BP and NG** answer 200 on 16 of 16 slash-key reads (c55, now pinned).
- **The walk.**

**Round 74 is CLOSED.**

## 2. THE BOARD (CVO L9): REALIZED 19 of 30

Newly REALIZED: **FWD-4.** The walk followed a BA feed item out to its barrons.com original, and 657 of 657 feed items carry a url
since HARVST gold rebuild #7. The 11 NOT REALIZED:

| cause | FWD |
|---|---|
| **product work owed** | **5:** branded now, but every line is stamped "as of 2026-10-06", including FY2016's share price. It also says "No investment thesis has been written" while `/thesis` serves 17 drafted sentences (Z-W256-S1). **7:** the page is not on DEV, and the first visit takes 9.1 s |
| **on DEV, awaiting Andrew's push** (DSGN rounds 43+44) | **18, 1** (the page draws them on candidate `1d6d2573`); graded on DEV |
| vendor, list owners, not built, or a qualified wait | **2, 14, 11, 12, 16, 20, 37.** FWD-1's other 83 names need the segment pull (Z-W240-S1) |

## 3. RULINGS

| # | item | ruling |
|---|---|---|
| 1 | **FWD-5: misdated history** | Every figure in the print carries ITS OWN period or as-of: a fiscal-year figure reads its fiscal year, a market figure reads its quote date. The print's run date appears ONCE, in the header. Proof: 0 historic figures stamped with the run date, on all three prints. |
| 2 | **FWD-5: the thesis is omitted** (Z-W256-S1) | The print reads the same drafted thesis `/thesis` serves: the print and the route come from one reader, not two. "No investment thesis has been written" appears only where `/thesis` serves none. Proof: on BA, the print's thesis sentences equal the route's 17. |
| 3 | **FWD-7: the first visit takes 9.1 s** | The 60 s in-process hold only helps a warm container. **Precompute the view:** the step that refreshes the pack ledgers writes ONE `/freshness` snapshot object, and the route reads that object. A new served key (an S3 address from `lib/opal_naming.py address()`, CLAUDE.md rule 30) goes under a pair. Proof: a first visit on a cold container under about 2 s, with values EQUAL to the computed view on all 292 rows. **The DEV push of the page waits on this,** then goes to Andrew together with DSGN 43+44. |
| 4 | **FWD-7: 95 of 95 flagged stale** | **Correct, not a defect.** Seeking Alpha is genuinely unread for 92 names (the SA account answers 402, HARVST row Z-S89). A page that flags real staleness is doing its job. FWD-7 is graded on the page's ability to single out a stale name, which it does once collection resumes and only some names lag. |
| 5 | **The cold read** (3.7-4.7 s) | Round 75: read the phase table on `0MZWPl7n` and cut the next-largest phase, with no spend. Provisioned concurrency stays on Andrew's list while the read is above about 2 s. |
| 6 | **The producer items from my DSGN 43+44 review** (@0c9b9db840) | Round 75: each segment row is headed by its segment's own name, one segment per heading (no "ITEM 7..." headings, no two names for one segment); a table-derived passage is served with its row and column labels. |

## 4. ENRICHMENT LIST (round 75, ONE issuance by `2.0.0_SA_COO~Z`)

1. FWD-5: each figure carries its own date (ruling 1).
2. FWD-5: the print reads the served thesis (ruling 2).
3. FWD-7: the precomputed `/freshness` snapshot, under a pair (ruling 3).
4. The next cold-phase cut (ruling 5).
5. Segment labels and table passages (ruling 6).
6. The redeploy, under a pair.
7. The walk: FWD-5 on three prints, FWD-7's first visit, and a re-read of FWD-18 and FWD-1 once DSGN 43+44 is on DEV.

## 5. ACTS FOR ANDREW (cited)

- **The portal DEV push** of DSGN rounds 43+44 now (`1d6d2573`), then RESAPP's `/freshness` page after ruling 3. These are product
  files; PROD is his separate word.
- **The Bloomberg Terminal sign-in** (it is down since the 03:09Z standby; lockout budget).
- **Provisioned concurrency,** only if ruling 5 still leaves the cold read above about 2 s (spend).
- **Vendor uses:** Z-W240-S1, Z-W227-S1, FWD-2. **FWD-14's list owners.** **The walker accounts.**

## ADDENDUM 1 (2026-10-06 ~10:3xZ) -- ruling 3's writer (COO~Z msg 29991)

**My ruling 3 named a write point that does not exist.** "The step that refreshes the pack ledgers" has no production caller:
`ledger.record_run` is called only by its own rerun and tests. COO~Z built the snapshot (`amgt/harvest/state/freshness_snapshot/current/
snapshot.json`, `address()` output) and the route's 24 h fallback compute (AMENDMENT 1 @5861f53f1a). It asks which writer refreshes
the snapshot.

**Ruling: (b), a scheduled writer, built on the estate's EXISTING pattern.**
- `infra/aws/terraform/harvest/chatter-axis-schedule.tf` already runs an `aws_scheduler_schedule` (`chatter_axis_daily`, cron
  10:00 UTC). The freshness refresh is a sibling of it:
  - one schedule, named by `lib/opal_naming.py name()` (CLAUDE.md rule 30);
  - it invokes the EXISTING `opal-amgt-scoped-api` function with a refresh event, so no new function is created;
  - it runs once per trading day after the morning vehicle lands (about 12:30Z);
  - the role gains `s3:PutObject` on exactly the snapshot key, and nothing wider.
- **(a) write-through is refused.** It makes the first visitor of each day pay about 7.5 s, which is the case FWD-7's first-visit
  grade is about: the morning staleness check. It also puts a write on a GET path.
- **(c) is refused.** HARVST's landings as the only trigger is the success-of-upstream-only defect (CLAUDE.md: production pipelines
  must be scheduled), and collection is stopped anyway.
- **The route's 24 h fallback compute stays as the miss path,** with no write.
- **Proof:**
  - the schedule fires and the snapshot's stamp moves;
  - a cold first visit after the fire is under about 2 s;
  - the values are EQUAL to the computed view on all 292 rows;
  - a negative control: the role's simulate on a sibling key reads implicitDeny.
- This is a WORLD act (a new schedule and a grant), so it goes under a pair.
