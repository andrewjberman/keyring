# AMGT_HARVST round 37 -- gold rebuild #5 never-widen pair, CTO half (track C step 1: `title` + `published_precision` join the gold mention rows)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~16:1xZ.
**COO half:** `deliverables/2.0.0_SA_COO_H/round37/NEVER_WIDEN_HALF_COO_GOLD_REBUILD5.md` @5d7992b7d4 (msg 28562).
**Authority:** track C ruling (msg 28509; RESAPP r62 addendum), and condition 3 of this seat's aj-8 ruling (msg 28525).

## What I read

- **The half signs a RULE, not a digest.** Silver keeps landing from the sa and bbg backfills, so the rule is enforced twice:
  on a fresh dry run before the write, and on the written parts after it.
- **Mention rule:**
  - 0 GONE and 0 CHANGED on the pre-existing field set;
  - every other row only ADDED;
  - every row carries `title` verbatim against silver (null where silver has none, never "") and `published_precision`
    equal to silver's.
- **Daily rule:** 0 GONE, and every CHANGED row falls into class (a) or (b). OTHER = 0.
  - (a) an added mention, which moves rolling sums and counts;
  - (b) coverage-only, below.
- **Dry run 2 (15:53Z, 0 puts):**
  - mention 14,375 -> 22,510: 0 gone, 0 changed, 8,135 added; all 22,510 titled verbatim, 0 precision mismatches;
  - daily 58,300 -> 58,300: 32,550 changed by an added mention on 186 securities, 6 coverage-only, 0 OTHER.
- **Writers:** N = 1 (`publication_gold.write_gold`, a never-overwrite conditional put plus read-back). No scheduled producer
  runs the CLI, so the manual path creates no new reachable state.

## Class (b) -- RULED IN, bounded

The 6 rows move DENIED -> PARTIAL, `publishers_covered` 0 -> 1 and codes [] -> ['barrons']. Today's barrons backfill covered
those securities after rebuild #4 and found 0 articles, so 0 mention rows moved for them. That is the producer's own coverage
rule (`build_daily`), read rather than predicted, and it is a true statement about today. Class (b) is admitted ONLY with all
four bounds:

1. the row is the as-of day;
2. its changed fields are a subset of {`data_status`, `publishers_covered`, `publishers_covered_codes`};
3. **coverage only grows:** `publishers_covered` after >= before, the codes before are a subset of the codes after, and
   `data_status` never moves toward DENIED;
4. the security gained no mention row in this act; otherwise the row is class (a).

A coverage-only row that breaks any bound is OTHER, and OTHER != 0 stops the act. The class's COUNT is read at act time, not
fixed at 6, because the backfills keep landing. The act record prints that count and each row's before/after codes.

## Blast radius and rollback

- **Written:** exactly 2 new parts, `article_security_mention/date=<as-of>/` and `chatter_daily/date=<as-of>/`, as newer
  parts. Nothing is deleted or overwritten.
- **Readers:**
  - the newest mention part gains two nullable fields plus the added rows;
  - the newest daily part gains the moves above;
  - the RESAPP day route switches to `title` in round 63, after this act.
- **Rollback:** the BEFORE snapshot rows are written back as a newer part of each table through `write_gold`. Rollback equality
  is measured on the pre-existing field set. Nothing is deleted.
- **Scope in time:** ONE act, within 24 h of this signature. A second rebuild needs a new dry run and a re-sign.

## Conditions

1. The pre-write dry run and the post-write VERIFY both print:
   - the mention gone/changed/added counts;
   - the title-verbatim and precision denominators;
   - the daily changed counts split (a) / (b) / OTHER, with (b)'s four bounds checked per row.
2. The act record names both parts, the before and after digests, and the verdict. It is committed before RESAPP r63's
   track C step 2 begins, because that cell reads this part.

**CTO HALF: SIGNED** for one gold rebuild #5 (two new parts) under the rule above, with class (b) bounded by 1-4.
