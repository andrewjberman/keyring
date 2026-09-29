# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- RE-CUT: irpt-performance-adapter qfxZ0DzB -> hD7G6YT1, 49 Financial Performance read from the v0.20 holdings gold (IB-pr-201/202/211/214, TO-IB-er-301 step 0)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_HOLDINGS_GOLD_49F_R2_20260929.md`
blob `a4679360` (at `ac4ad83de7`, an ancestor of HEAD; at HEAD and on disk; read 2026-09-29 07:5x-08:3xZ).
- **Word diff:** the re-cut of blob `189aaef2`, which this seat REFUSED
  (`NEVER_WIDEN_SIGNOFF_CRO_HALF_ADAPTER_HOLDINGS_GOLD_49F_20260929.md` @eca8083ad2, addendum 1 @b2215bcedc). The
  carried sections (surfaces, rows B-F, rollback per key, the CTO's rollback condition) read here as unchanged.
- **Asked by:** 2.0.0_SA_COO~P, msg 102646. **Other half:** 1.0.0_SA_CTO. **Ledger:** `irpt-adapter-holdings-gold-49f-r2-20260929`
  (U1, P1 closed; D1, A1 open). This seat is not in the act.

## VERDICT: SIGNED on blob a4679360, with three conditions and six named items

Every item of the refused half's section 6 is done and measured here independently. One hazard the first refusal did
not see is measured in section 3: a custody price discontinuity has TWO edges, and ruling 16 voids only the one that
crosses the band, so one account (a ~$1.9M relationship) would serve a 1-year figure of -91.5% computed against a
price the producer itself marked implausible. It is bounded (2 accounts, both named), it is the CTO's ruling to make,
and condition 2 asks that the choice is recorded before the apply rather than discovered after it.

## 1. What the re-cut answers, read here (not from the packet)

- **Artifact `hD7G6YT1`** (S3 `3donK_gT`, 424,559 bytes, 07:39:13Z): 70 members. Vs the refused `ABB89j26`: only
  `entry.py` (8465a60d) and `retained.py` (ea895201) differ, each byte-equal to HEAD. Vs live `qfxZ0DzB` (still the
  function's CodeSha256, Active): `holdings_gold.py` added and the four members the first packet named.
- **The two deltas, read at their lines:** `retained.py:225-231` -- after `holdings_gold.calculate`, the fresh path
  raises `f49_engine.EngineReturnImplausible` when `implausible_engine_series(outcome["report"])` (any linked point
  <= -1), before persist or return, so both readers refuse one shape (ruling 16). `entry.py:61` --
  `_authorize_release` now passes `request` into `_resolve_selected(scope, ctx, reference, request=None)`, which only
  the RENDER_DELEGATE branch consumes (`_resolve_render_selection`); every other principal's path is unchanged. That
  is window 21's K8 refusal (`corr-d490a5849a80`, "a render read carries no request to name its grant").
- **Tests on the zip's own modules** (`retained`, `holdings_gold`, `f49_engine`, `entry` imported from the zip,
  asserted): new zip **20 passed**; the refused zip **1 failed, 19 passed**, the one failure
  `test_fresh_path_refuses_an_ok_day_at_or_below_minus_one` (DID NOT RAISE) -- the test tells the two zips apart.
- **The gold, re-emitted 06:43:07-07:08:21Z under v0.20** (`holdings_performance.py` @f302ab14cd, read: identifier
  = first non-empty of the declared columns with a per-row sentinel for none; cash rows into the basket at zero;
  `in_basket = member & (value >= 0)` with `negative_value`/`leveraged`; a second-pass band emitting
  `IMPLAUSIBLE-RETURN`; the manifest population on `held_count`). E3-AC4 re-run by this seat 07:51Z: `days 557 |
  partitions absent 0 | OK rows |r|>=1: 0 | OK rows |r|>0.5: 4 | days without leveraged: 0 | manifests complete 557
  of 557` -- PASS. This seat's own read of all 557 partitions: 3,188,339 rows, 19 columns; status census OK
  2,781,208 / NO-PRIOR-HOLDINGS 405,142 / NON-POSITIVE-BASE 1,541 / ALL-HOLDINGS-EXCLUDED 446 / **IMPLAUSIBLE-RETURN
  2**; `leveraged` on 7,483 rows over 679 accounts; OK-row min -0.9233, max +0.5047. Both manifest surfaces
  (parquet and json) carry the four completeness keys and agree on `computable_count` on 557 of 557 days, which
  retires addendum 1 of the refused half.
- **The chain census, re-run by this seat** (the adapter's rule, windows ending 2026-09-25): the packet's section 3
  numbers are this seat's numbers -- YTD 7,127 accounts: >= +100% **2** (was 22), <= -100% **0** (was 2),
  (-100%, -50%] 2, max +197.9%, min -61.2%; 1Y 7,300: 4 / 0 / 4; SI 7,814: 7 / 0 / 5, non-finite 0 (was 1).
- **Plans, prefixes, IAM:** carried from the first half (ae20e904e6; every prefix builder output); the packet's fresh
  plans 0/2/0 and 0/1/0 are the ledger's P1 leg and are not re-run here.

## 2. The 49F silver under ruling 13, measured (for the record, not a ground)

The Schwab `dim_position` carries no description column, so the declared identifier chain is cusip then
`ticker_symbol`. Of the 41 cusip-less rows at 2026-09-25, both are blank on all 41; one row carries an ISIN/SEDOL
(not in the chain); **21 are ruling-14 cash** (price 1.00, quantity == value) and **20 are excluded** under ruling 4.
The producer's own count at 2026-09-24 agrees (21 of 41, 22,037,392.89).

## 3. The remaining hazard: a discontinuity has two edges, and ruling 16 voids one

The two `IMPLAUSIBLE-RETURN` rows, traced to the silver:

| account | day voided | what the silver did | the next day, still OK | window figure the act would serve |
|---|---|---|---|---|
| ..0090 (28 holdings, ~$1.9M) | 2025-12-17 | DLCFX 17.48 -> **546.00** -> 16.21; DIEFX 16.12 -> **384.00** -> 14.61 (x31 and x24 for one day, then back) | 2025-12-18 `r = -0.9233`, computed against the glitched t-1 price, inside the band, status OK | YTD +7.7% (clean); **1Y -91.5%** (250 OK of 251); **SI -91.4%** |
| ..4714 (3 holdings, ~$12k) | 2025-12-12 | MSOX 3.82 -> 7.94 -> 6.91 -> 9.50 | 2025-12-15 -13.0%, 12-16 +37.5%, 12-18 -50.6% | YTD -7.1%; **1Y -69.8%**; SI -69.8% |

The producer implements ruling 16 as written (a day at or beyond +/-100% is not computable); the day AFTER prices
its holdings against the price the producer just declared implausible, and a -92% day is inside the band. The
remedy is one of two producer rules, both the CTO's to choose: the day after an IMPLAUSIBLE day is not computable for
that account (its reason named), or the affected keys price against the last plausible price. Population today: 2
accounts, both in the served directory; every other chain at or under -50% (..8878 ~$123; ..7501 ~$1.1M, JFB
29.87 -> 17.00 -> 20.90 -> 9.01 -> 8.23 across February-March, a sustained fall, not a one-day edge; ..7828 ~$33k, no
day beyond +/-30%) is the custody price path as given.

## 4. The read set and what the rule says the act serves (read from the v0.20 gold at signing)

NEW-01, the control and the ..558d pair sit under ONE directory relationship (three accounts), so one client walk
reads all three. ..0273 (the refused half's cusip-less account) is **not in the served directory** (4,620 entries): the
page cannot read it, so it is replaced on the page by ..4714 (in the directory) and read from the adapter's own log
only if ~P invokes it; its gold reads YTD 0.00% over 79 OK days, SI 0.00% over 171 OK of 452 (PARTIAL).

| read (page, walk) | BEFORE on qfxZ0DzB (engine, as retained) | AFTER on hD7G6YT1, predicted from the rule |
|---|---|---|
| NEW-01, YTD and 1Y | named refusal (DEPENDENCY_UNAVAILABLE; the retained -100% reports) | **+0.49%** over 69 OK of 181 / 252 days, PARTIAL; provider OPAL_HOLDINGS |
| the control (same relationship), YTD | 5.93% | **+5.16%** (181 of 181) |
| ..558d (same relationship), YTD / 1Y | 9.57% / 8.80% | +0.04% / -0.85% (the widest engine-vs-holdings gap; named in the refused half) |
| ..0695 (near-zero base), YTD | engine figure as served | **+4.38%** over 137 OK of 139, PARTIAL (2), `leveraged` on 8 days |
| ..4180 (one stock, MRVL), YTD | engine figure as served | **+197.9%** over 135 OK of 137, PARTIAL (2); MRVL 84.98 -> 261.94 in the silver, a smooth path (99.05 at 03-31, 290.79 at 06-02) |
| ..2297 (DELL-led, 2 -> 28 holdings), YTD | engine figure as served | **+149.7%** (184 of 184); DELL 125.88 -> 562.89, smooth (164.13, 435.31, 431.46) |
| ..0090 (section 3), YTD and 1Y | engine figure as served | YTD **+7.7%**; 1Y **-91.5%** PARTIAL (1) |
| ..4714 (section 3), 1Y | engine figure as served | **-69.8%** PARTIAL (2) |
| one Cottonwood and one Inflection figure | as served | unchanged (row F) |

## 5. Blast radius (the first packet's, with what section 3 adds)

- **Row A, moves:** every 49F account's figure to the holdings chain. Population read above: 2 YTD accounts serve
  over +100% on smooth custody price paths; 0 serve at or under -100% on either reader (the fresh-path guard makes
  the reopen guard's refusal shape unreachable on a first read); **2 accounts serve a 1Y between -70% and -92% off a
  one-day price glitch's reversion edge** (section 3).
- **Rows B-F:** as the first packet and this seat's first half read them; F re-read here as unchanged code.
- **Rollback per key:** unchanged (Lambda -> `5bmwADQs`; the two .tf files reverted, both roots re-applied).

## Conditions

1. **The before-read is this seat's, on qfxZ0DzB, before the apply; the after-read on hD7G6YT1 is the same set**
   (section 4, by `/ui-walk`, shots kept under `tmp/ui-walk/`, never committed). ..0273 is read on the page as
   ..4714. Any figure at or under -100% on either reader, or any unnamed difference, is the packet's own rollback.
2. **The two-edge case is ruled before the apply, in the CTO's half:** either the producer re-emits under a v0.21
   rule for the day after an `IMPLAUSIBLE-RETURN` day first, or the interim is accepted by name (..0090 1Y -91.5% /
   SI -91.4%; ..4714 1Y -69.8%) with row `IRPT_BCKEND-S200` as its carrier. This seat signs either branch; it does not
   sign the figure served with the choice unrecorded.
3. **The after-read includes ..0090's 1Y and ..4714's 1Y as served**, recorded in the ledger beside the packet's
   reads; a served figure there that differs from section 4's prediction is a row the same turn.

## Named items (not refusal grounds)

1. The two +100% accounts are single-stock or single-stock-led, and the silver's price paths are smooth; the served
   figure is the custody price's. Whether a +198% year is what the client sees elsewhere is the advisor's read.
2. A chain over in-band days is unbounded above (each day < +100%, the product not); the band bounds a day, not a
   window, and that is the ruling as written.
3. ..558d's engine 9.57% -> holdings +0.04% YTD remains the widest gap among the retained accounts; not measured
   further here.
4. 679 accounts carry `leveraged` on at least one day (7,483 rows); the page shows no such flag today.
5. The since-inception read costs 557 partition reads; the CTO's 48-second rollback condition is the CTO's and is
   not re-derived here.
6. The refused half's addendum 1 (the 2026-09-25 manifest's two surfaces) is retired by the re-emit: 557 of 557
   agree.

## Addendum 1 (2026-09-29 09:4xZ) -- condition 2 met by the CTO's option (a); the BEFORE-read taken on qfxZ0DzB; GO from this seat

**Condition 2:** 1.0.0_SA_CTO ruled option (a) (msg 102670; PRD ADDENDUM v0.21 ruling 18 @c0c0ae5606: the trading day after
a NOT COMPUTABLE day is not computable, reason "follows a price discontinuity"); ~E re-emitted the 49F gold 09:05:02-09:25:55Z.
**Re-verified here 09:41Z:** E3-AC4 PASS (557 days, 0 OK rows at |r| >= 1, 3 at |r| > 0.5, `leveraged` on 557, manifests
557/557); status census now carries `FOLLOWS-DISCONTINUITY` 2 beside `IMPLAUSIBLE-RETURN` 2 (..4714 2025-12-12, ..0090
2025-12-17); OK-row min -0.5463, max +0.5047. Chains (the adapter's rule): YTD 7,127 accounts, >= +100% 2, <= -100% 0,
(-100%, -50%] 2; **1Y: ..0090 +10.20%** (was -91.5%), **..4714 -65.35%** (was -69.8%; the MSOX days of 12-15/16/18 are inside
the band and stay), 1Y (-100%, -50%] 3; SI 7,814, (-100%, -50%] 4, min -73.5% (the ~$123 account ..8878). Both halves
stand on this census.

**BEFORE-read on qfxZ0DzB** (`/ui-walk`, walks `20260929T082535Z`, `085346Z`, `090329Z`, `092109Z`, `093437Z`, 08:25-09:40Z,
each disarmed with the login REFUSED; shots under `tmp/ui-walk/`, never committed; the default period YTD as the page
answers it; 1Y for NEW-01 stands from the reopen-guard walk of 00:12Z):

| read | BEFORE (engine, `opal-gips-engine`) |
|---|---|
| NEW-01 (the ~$99k account of the three-account relationship), YTD | "temporarily unavailable" -- DEPENDENCY_UNAVAILABLE by name (the retained -100% report refused at reopen); 1Y the same at 00:12Z |
| the control (~$154k, same relationship), YTD | 5.93%, "Partial -- qualified answer, not a complete report" |
| ..558d (~$148k, same relationship), YTD | 9.57% |
| ..0695 (near-zero base, ~$141k), YTD | "temporarily unavailable" -- DEPENDENCY_UNAVAILABLE |
| ..3510 (one stock, MRVL, ~$307k), YTD | **196.32%**, answered March 16th to September 22nd ("the source answered a different window") |
| ..2297 (DELL-led, ~$790k), YTD | **145.08%** |
| ..0090 (section 3, ~$1.89M), YTD | 8.41% (1Y to be read after, per condition 3) |
| ..4714 (section 3, ~$12.5k), YTD | not settled in the shot ("Loading"); the after-read takes it. Its relationship shows a second account with the SAME mask `****4714 / S1` (~$1.43M) |
| Inflection (a ~$241k individual account holding a retained report), YTD | 7.98%, Partial |
| Cottonwood (a ~$1.83M 401K holding a retained report), YTD | DEPENDENCY_UNAVAILABLE; a 24-account Cottonwood household read the same on 8 of 8 performance GETs -- the Black Diamond dependency is refusing today, before this act |

The engine already serves the two +100% accounts at 196.32% and 145.08%, so the holdings figures of +197.9% and +149.7%
are the same custody facts on a second basis. **GO from this seat** for packet section 4 steps 3-4; the AFTER-read is a
`--deep` walk (period presets pressed) over the same clients, reading NEW-01, ..0090 and ..4714 at 1Y as condition 3 asks,
plus the Inflection and Cottonwood reads unchanged.

Named beside (a DSGN_IRPTV1 finding, routed separately): the account picker labels every account of a relationship with
the relationship's mask (three `****9079 / IRA`, five `****3302 / JOINT`, two `****4714 / S1`), so accounts are told apart
by value alone.

## Addendum 2 (2026-09-29 10:5xZ) -- AFTER-read on hD7G6YT1: NOT MET; row IRPT_BCKEND-S204 ARMED; the CTO's all-accounts census

**Apply:** ~P applied hD7G6YT1 at 10:14:14Z (msg 102712); CodeSha256 read here at 10:21:28Z, Active. **Walks**
`20260929T102651Z` (per-account period presets on the NEW-01 relationship, ..0090, ..4714) and `103746Z` (..3510, ..2297,
..0695, the Inflection and Cottonwood reads), 10:26-10:48Z, both disarmed with the login REFUSED.

| read | AFTER on hD7G6YT1 |
|---|---|
| ..0090 YTD / 1Y | **"Unavailable / UNEXPECTED / Contact support"** on both (picker "YTD pending", "1Y unavailable") |
| ..4714 ($12,522) YTD / 1Y | UNEXPECTED on both; the same-mask $1.43M account the same |
| NEW-01 relationship (3 accounts), every period | UNEXPECTED (4 answers at the client load) |
| ..3510, ..2297, ..0695 | UNEXPECTED (9 of 13 performance answers in walk B) |
| Inflection ~$241k, Cottonwood 401K | unchanged from BEFORE (PARTIAL 7.98%; DEPENDENCY_UNAVAILABLE) |
| since-inception reads | served (10 `irpt_holdings_phases` lines, 554 partitions, frame 9-10 s) |

**Cause, read from the served log and the two zips:** `/aws/lambda/irpt-performance-adapter` 10:26-10:50Z carries 104
UNEXPECTED events, every one `ModuleNotFoundError: No module named 'parity_period_returns'`. `installed.py` on
qfxZ0DzB inserted `data/assets/scripts/gold/runners_49f` onto `sys.path` inside `_engine_source()`; hD7G6YT1's
`_holdings_source(s3)` replaced that function and inserts nothing, while `f49_engine.ruled_period_for` (:71-73) still
imports `parity_period_returns` lazily and `holdings_gold._period_for` calls it for every window except since
inception. The packet's read-back (a cold-start invoke and ONE since-inception answer) exercised exactly the branch that
does not import it. Verdict: **NOT MET -- an unnamed difference at the read, now named; the packet's own step 5 applies
(rollback to 5bmwADQs, or a rebuild with the path restored).** Alerts 102734/102735 and the cause 102739/102740 to ~P
and the CTO; row `IRPT_BCKEND-S204` ARMED, disarm owner 2.0.0_SA_COO~P.

**The CTO's added condition (102705, an all-accounts served-figure census):** run here through the adapter's own
`holdings_gold.calculate` (hD7G6YT1's bytes, the fresh path's `implausible_engine_series` applied, the runners directory
on the path) over a versioned local cache of the re-emitted gold, and by ~P over the served gold
(`IRPT_MVP_P/ADAPTER_49F_SERVED_PERIOD_CENSUS_20260929.txt`): the two agree -- 0 figures at or below -100% in any
window, 0 refused as implausible; at or above +100%: YTD 2 (..4180 +197.85%, ..2297 +149.67%), 1Y 4 (+ ..8562, ..7477),
SI 7 (+ ..2191, ..4060, ..4172). Their read-back by name on the page waits on a working ruled-period path; ..3510 and
..2297 answered UNEXPECTED in walk B.

**Lesson carried into the next packet (this seat's condition on any re-ask):** the read-back requests each ruled window
once (YTD, 1Y) beside since-inception, and the after-read presses each period per account (the walker's
`--periods-per-account`, added today for this read).

## What this half signs against

- Packet blob `a4679360`; the first packet's carried sections (`189aaef2`); artifact `hD7G6YT1` (S3 `3donK_gT`) with
  its 70-member census; commits f302ab14cd, eee6a7a721, dd3be9a28a, 78f7ffb758, ae20e904e6; PRD ADDENDUM v0.20
  @613bfc6ecf.
- The gold as re-emitted 06:43-07:08Z (E3-AC4 PASS, this seat's run 07:51Z) and the chain census in section 1.
- The blast radius in section 5, the read set in section 4 and the three conditions.
