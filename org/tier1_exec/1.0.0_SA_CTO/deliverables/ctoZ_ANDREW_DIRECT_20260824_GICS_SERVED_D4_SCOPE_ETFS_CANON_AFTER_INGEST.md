# ANDREW-DIRECT 2026-08-24 ~22:12Z -- all three open calls ruled in one line

**Seat:** `1.0.0_SA_CTO~Z` (site Z) · **Surface:** the CTO~Z terminal, in response to `/open-calls`
cards 1-3 put at 22:07Z · **Recorded + broadcast same turn** (5340-5345, 6/6 DELIVERED).

## HIS WORD, VERBATIM AND COMPLETE

> **"Agreed with your recs + We can revisit ETFS_CANON After INGEST is done"**

That is the entire utterance. Everything below is my reading of what it binds, marked as mine.

## WHAT HE WAS AGREEING TO -- the three recs, as they were put to him

**CALL 1 -- the served sub-category vocabulary.** REC: *"GICS served, Bloomberg's as cross-check.
GICS industry group is per-security and free: it rides the Bloomberg pull that already runs, and we
compute the rollup ourselves -- the shape you described at 21:47Z. Bloomberg's sector labels exist
ONLY as a fund-level aggregate, with no per-security member at all (measured: gics 0, hb_ 0, sector
0, industry 0 on the per-security file). Serving those means taking Bloomberg's own weighting after
all -- the thing you said we don't need. Only one of the two is free to serve."*

**CALL 2 -- D4's completion scope.** REC: *"Complete D4 on ETFS_POSITIONING + ETFS_INGEST; let
ETFS_CANON stand as its own directive."*

**CALL 3 -- sub-category colour at ~24 values.** REC: *"Leave it as ruled"* (DE~Z: recessive text +
filter, matching the estate's existing SecurityScanner precedent; zero colour keyed on industry
group anywhere in `src`).

## WHAT IT RULES

| # | ruling | consequence |
|---|---|---|
| 1 | **GICS is the SERVED vocabulary; Bloomberg's `HB_*` sector labels are the cross-check, not the source.** | `INGEST-T3-3` scope settled. `GICS_INDUSTRY_GROUP_NAME` joins the `CHAR` list; the rollup is computed by us from issuer weights x per-security GICS. |
| 2 | **D4 completes on `ETFS_POSITIONING` + `ETFS_INGEST`. `ETFS_CANON` is DEFERRED, re-entering after INGEST is done.** | Stronger than the rec: he SEQUENCED it rather than orphaning it. `/self-drive D4` has no UNREACHABLE member; the loop can terminate. Register edit is MSTR~Z's, as a deferral not a removal. |
| 3 | **Sub-category renders as recessive text; no colour keyed on industry group.** | DE~Z's AC6 determination stands. |

## ⚠ WHAT THIS RULING IS *NOT* -- and the distinction is load-bearing

**It does NOT retroactively make "HB_* becomes a tie-out oracle" his word.** That phrase was MSTR~Z's
inference and mine, and CVO~Z (5205) correctly caught it being written into a PRD bullet carrying his
verbatim -- his 21:47Z words contain no `HB_*`, no "fund-level", and no "tie-out". What closed the
question is **his explicit agreement to a rec that stated the measured structural fact**, which is a
different and better thing than an inference that hardened by repetition.

**Two seats reaching the same inference independently did not make it his word. His agreement did.**
The record must keep those separable, because the next inference will feel equally obvious.

## ⛔ THE IMMEDIATE CONSEQUENCE, NAMED AGAINST MYSELF

With scope settled, D4's critical path is `ETFS_POSITIONING.TO-5` -- **which carries the ONLY
gold -> platinum schedule (`cron(0 13)` UTC) and is committed-not-applied, HELD by me on the Z-S19
ruling.** Census, token-walked, denominator stated: **136 EventBridge rules total, 7 ETF-named, and
not one produces etf-positioning gold or platinum.** Bronze and silver are exercised; the served
surface is verified by nobody.

The hold was correct -- applied as written, TO-5's ENV error would have silently reverted his C2 gold
home while its IAM error failed loud, the two cancelling into a green pipeline where his ruling did
not happen, with `_assert_write_boundary` keyed to the configured values and therefore *validating*
the reverted target. **I would place it again. But a correct hold left standing is still a stopped
pipeline**, and it is now the only thing between a proven capture and a rendered page. Discharge is
the top item; Rule 26 binds the apply to this box.

## Grounding

Vocabulary asymmetry measured independently at three seats (DE~Z 5213, CVO~Z 5234 case-insensitive
with a firing positive control and clean negative, COO~Z 5241 corroborating from headers). Schedule
census: `aws events list-rules`, materialised and token-walked, 136 rules single page, `NextToken`
absent -- never a `--query` over a paginated list.
