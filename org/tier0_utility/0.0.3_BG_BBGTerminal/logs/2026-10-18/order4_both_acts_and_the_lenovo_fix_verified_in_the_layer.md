# ORDER 4 acts 1+2: both pulls landed, and the Lenovo fix is VERIFIED in the layer

**archetype:** VALIDATE
**Recorded by:** `0.0.3_BG_BBGTerminal`, 2026-10-18 ~00:3xZ.
**Order:** crossbox `XB-20261017T063406Z-e568` from `2.0.0_SA_COO~RV`, acked 2026-10-17T06:44:29Z,
**AS AMENDED** by `ORDER4_AMENDMENT1_RESOURCE_EVERY_SNAPSHOT_CLOSE.md` @220ec4c53c (rows Z-S85, Z-S87,
D1-S21). Fired from the 00:04Z trigger this seat set 17 hours earlier.

## STEP 0 -- measured, not assumed

Clock **2026-10-18T00:05:39Z**, past the order's `not before 2026-10-18T00:00:00Z`. All three commits
`is-ancestor` TRUE in HEAD (220ec4c53c, 91fd54467f, ec21b4e150) with a bogus-hash negative control
rejected beside them. Both units files on disk (p2 531,531 B; all-pull 110,076 B), so **the authorised
fallback was retired unused**. Layer held order 3's 168 objects. Inbox empty: no further amendment.

## ACT 1 -- dry run first, then live, sequentially

Both dry runs returned **OK**, so nothing was sent back and nothing stopped. The live pair ran
**sequentially on purpose**: they share one layer and one budget ledger, and parallel runs would race
both.

| | units | asked | landed | carried | failed | misdated | lookups | points |
|---|---|---|---|---|---|---|---|---|
| (a) TR p2 | 36,166 | 36,166 | **34,717** | 0 | 0 | 0 | 56 | 72,388 |
| (b) re-source | 5,810 | 5,810 | **5,618** | 0 | 0 | 0 | 0 | 11,620 |

(a) covered **78 dates, 2025-10-13..2026-02-03** -- exactly p2's window, complementing p1's
2026-02-04..2026-10-12, so the 365-day span is now whole. (b) landed **all 10 dates** 2026-10-02..10-15
with `failures: {}`.

**Layer 168 -> 256 objects, 6.5 MB.** 78 + 10 = 88 new objects, and 256 - 168 = 88 exactly. Nothing was
written to S3 by either act.

The shortfalls (1,449 on p2, 192 on the re-source) are securities with no close on a given date. Stated
as unexplained-BY-MEASUREMENT rather than explained: `carried 0` proves nothing was deferred and
`failed 0` that nothing errored, but I did not count the no-close set, and the step-1 lesson was exactly
that a pre-declared cause is a hypothesis until someone counts it.

## THE POINT OF THE WHOLE EXERCISE: the fix is VERIFIED, not assumed

Read 992 HK Equity straight out of the layer and compared against the BDH truth measured on 10-17:

| date | layer now | BDH truth | the shifted value it replaced |
|---|---|---|---|
| 2026-10-12 | **32.34** | 32.34 | 31.10 |
| 2026-10-13 | **31.10** | 31.10 | 30.40 |
| 2026-10-14 | **30.40** | 30.40 | 25.98 |
| 2026-10-15 | **25.98** | 25.98 | 28.06 |

4 of 4 correct, every row `as_of_source` **held-tr**. **The arc closes:** Andrew's *"check out that
lenovo price history ... get that corrected properly"* -> the one-day shift -> the venue-wide finding ->
my own correction that it is capture-TIME not venue -> RV's amendment extending the set to 653
securities -> and now the true closes sit in the layer.

**Scope discipline, stated plainly: this is the LOCAL LAYER, not served data.** Nothing a dashboard reads
has changed. Publishing is act 3, which is not in this order.

## ACT 2 -- the replay, gate met

`91fd54467f` is in the tree, so the condition was satisfied without forcing anything.

```
day 2026-10-16 | held-tr objects in the layer: 256
funds equal: 0 of 13 | whole table A == B: False
```

`implied_days A -> B` collapses far further than order 3's replay did on the p1-only layer:

| fund | order 3 (p1 only) | ORDER 4 (p1+p2+re-source) |
|---|---|---|
| CGIC | 94,158 -> 20,358 | 94,158 -> **2,990** |
| PCLG | 15,631 -> 3,386 | 15,631 -> **16** |
| TSEL | 14,983 -> 3,091 | 14,983 -> **16** |
| PFOE | 12,137 -> 1,198 | 12,137 -> **22** |
| INEQ | 55,389 -> 12,619 | 55,389 -> **2,866** |
| **GQGU** | 19,924 -> 15,267 | 19,924 -> **14,882** |

`contrib_moved` now equals `rows` outright for seven funds (CGIC 1374/1374, ETFT, PCLG, PFOE, TSEL,
TXUE, WCMG): every holding's contribution moves.

**THE OUTLIER, and it is the one thing here worth someone's attention: GQGU improves ~25% where every
other fund improves 95-99%.** Order 3's layer barely moved it either (15,267 from 19,924). Two readings
fit and I have measured neither: its holdings may sit largely outside the rivalfunds universe, so no
held-tr row exists for them; or its implied-days are driven by something the layer does not supply.
Flagged to the issuer, not diagnosed here -- it is their fund table, and a wrong guess from me would
cost them a look in the wrong place.

Table: `C:/opal-elev/rvht1o2/heldtr_replay_2026-10-16.json`, 16,441 bytes, site-Z local.

## ACT 3 -- NOT RUN, and not in this order

Order 3's act 3 still needs BOTH never-widen halves named by the issuer, and the served-rankings pair is
`1.0.0_SA_CTO~DELL1`'s, not CTO~Z's (CTO~Z 35409 said so explicitly when I mis-addressed that ask to
him). Given act 2 reads 0 of 13 funds equal, publishing would move every fund's rankings -- which is
precisely what the pair exists to adjudicate.

## Two instrument traps, each of which cost one failed call

1. **The comp-rail denied an `rglob` of `C:/opal-elev/rvht1`** as a blind recursive repo search. That
   path is OUTSIDE any checkout, which the rail's own FREE list admits; the hook matched the verb without
   reading the root. Re-run with the audited `# rail-checked:` marker naming exactly that. A rail false
   positive is still a rail doing its job, and the escape is audited for this case.
2. **The harness heredoc unescaped `\` to `\`**, turning `str(p).replace('\','/')` into an unterminated
   string literal. Already a banked site-Z lesson and it still caught me. The fix that avoids the class
   entirely is `pathlib.Path.as_posix()` -- no backslash to escape.
