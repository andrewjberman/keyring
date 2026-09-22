# L4-R REVIEW -- AMGT_HARVST PRD v0.1, BRIEF HALF -- verdict: REFUSE (the brief moved on Andrew's word after the pin)

**Reviewer:** `4.0.0_SA_CRO~Z`. **PRD:** `org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md` @`16db74edea`,
v0.1, brief half hash `919df3b82f7e` (msg 24273). **brief_ref:**
`org/missions/D5/AMGT/AMGT_HARVST/brief/BRIEF_AMGT_PUBLICATIONS_BRONZE_SILVER_GOLD_20260922.md@48f31e8fd0`.

## Independence limit

This seat authored the brief. It grades whether the brief half carries the brief's CONTENT at the named pin and
whether that pin is the brief's current state, not whether the plan is right.

## The one ground for refusal: the pin is superseded, and the difference is Andrew's, not stylistic

Between the pin (`48f31e8fd0`, 14:4xZ) and this review, Andrew gave two words at this seat's terminal (record
`ANDREW_DIRECT_20260922_AMGT_PUBLICATION_RETRIEVAL_STRUCTURE_BRIEF.md`, addendum 2, @`5b90a0b839`):

1. *"sticking to absolute figures or derived absolute figures, never do relative, because relative can be handled in
   a lambda or some other more ephemeral function"*
2. *"the first job is basically going to be doing a backfill back to the start of 2026"*

The brief was re-landed at its tree home @`5b90a0b839` (byte-identical to the deliverables copy) with both folded
in: s.0 items 7-8, s.3.3 (floor + watermark), s.5 (`retrieval_mode`), s.6.2 (absolute columns only; ratios and
z-scores moved to the serving Lambda), new s.6.5 (the backfill), s.8 call 8.

**Where v0.1 as written contradicts those words, by pinned line:**

| line | half | text at v0.1 | conflict |
|---|---|---|---|
| `:216-218` (`C-HV-DAILY-DENSE`) | ratified-text (`3.0.0_SA_CVO~Z`'s to grade; noted here because the brief half's manifest row H5 `:295` and FWD-5/FWD-7's SOURCE lines `:114`, `:133` rest on it) | gold `chatter_daily` "carries ... the prior-30-day baseline mean and SD, `breakout_ratio`, `z_score`" | stores RELATIVE figures in gold; his word puts them in the Lambda |
| `:276` (constraints) | brief | "retrieval provenance and watermark" | no FLOOR; the first job is a backfill to 2026-01-01, which a watermark alone cannot express |
| `:287-299` (surface manifest H1-H9) | brief | no row for the backfill run, dense gold from 2026-01-01, or `retrieval_mode` on silver | the first job is missing from the manifest |
| FWD-8 `:135` | ratified-text | "Articles already collected but never delivered reach the store" | that is the desktop outbox (83 bodies); it is not the 2026 backfill, and no FWD names the backfill |

Nothing else in the brief half is wrong against the pinned brief: the boundary, constraints, manifest, the calls
kept as Andrew's, and the silver-from-bronze ruling (his s.8 call 7, ruled by the L4 author) all carry the pinned
content faithfully.

## What v0.2 needs (recommendation)

- re-pin `brief_ref` to `@5b90a0b839`;
- `C-HV-DAILY-DENSE`: absolute columns only (`baseline_30d_sum`, `baseline_30d_days`, cumulative YTD totals), and a
  sentence that ratios, z-scores and 0-100 normalisation are computed at serve time (the CVO's half);
- one FWD for the backfill: dense gold from 2026-01-01 for every in-scope security, retrieval by floor + watermark,
  page counts printed before each run under the quota word, `retrieval_mode` on every silver row,
  `published_utc` as the only event clock;
- manifest rows for the backfill run and the retrieval floor (brief s.6.5);
- constraint: no relative figure is stored in any gold table of this project.

## Timing

Delivered at 14:48Z; the words arrived at this terminal minutes earlier and the brief re-landed at 14:5xZ. The
refusal is stamped inside the 60-minute window so the status reads honestly rather than OWED.
