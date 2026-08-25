# /self-drive D4 -- ticks 25-26 log (2026-08-25 03:22Z - 03:50Z) -- state: ARMED

**archetype:** COORDINATE · **secondary:** VALIDATE, SCRIBE
**Driver:** `1.0.0_SA_CTO~Z` · cron `71ae484c` · carrier `org/XXX.md:408` · continues `ctoZ_self_drive_D4_tick24.md`.
**Andrew gave two new asks. Both were measured rather than estimated, and the first one turned out to be MOSTLY ALREADY PULLED — 109 tickers x 5.6 years sitting in S3 that the producer has never read.**

## SCOPE + COMPLETION

```
D4 -> ETFS_CANON(scoping) · ETFS_POSITIONING(active) · +ETFS_INGEST(claimed, active)
  COMPLETION TEST: NOT DONE -- 0 of 2.  REACHABLE 2 / UNREACHABLE 0.  open TOs 6
  1 of 9 live directives · device SITEZ · 1 ahead of origin/SITEZ (AE~Z's finding commit)
  open calls: 0 ADJUDICABLE · 1 RESERVED (Pathfinder weekend stamp) + 1 override FYI
```

## ANDREW-DIRECT ~03:2xZ -- TWO ASKS

VERBATIM: **(1)** *"we need to figure out how to get 'Performance' on each individual security, which
means the holdings need to get fed back in to pull that data from Bloomberg on the relevant dates."*
**(2)** *"the 'Sub Asset-Class' weights thing... in the 'ETF Characteristics' main panel. That should
be very doable at the outset based on the holdings, shouldn't even need BBG to do that."*

## ⭐ THE FINDING OF THIS WINDOW: A 5.6-YEAR RETURNS BACKFILL EXISTS AND NOTHING READS IT

`etf_daily_pull.py:132-135` mentions it in a COMMENT. **I did not trust the comment — I measured the
prefix:**
```
s3://opal-data-etfs/bbg-testpull/tickers/{TICKER}/history.csv
   109 tickers · 222 objects · WM = 1,415 rows · 2020-12-31 .. 2026-08-20
   columns: date, price, return        <- EXACTLY what compute_returns consumes
   load_history() reads ONLY bbg/{date}/history_topup.parquet -- IT HAS NEVER READ THIS.
```
**COVERAGE, and the split IS the answer to ask 1:**
```
PFDE  90 rows   87 covered   97%   <- PLUMBING. No Bloomberg call.
PFOE  24        22           92%   <- PLUMBING.
DIVZ  29         8           28%   <- needs a backfill
IDVZ  44         3            7%   <- needs a backfill
```
⭐ **CORRECTED UPWARD 20 MIN LATER: PFDE/PFOE's "missing 3 and 2" are `CASH&OTHER` (a declared
SENTINEL), `FXFXX` (a money-market fund) and `2602335D` (the unresolvable TPG id) — NONE of which
should carry a daily equity return. Those denominators included rows that are not securities, so
PFDE/PFOE are effectively COMPLETE on the plumbing alone.**

## ⭐ THE BACKFILL, SIZED AND DE-RISKED

```
FUND   need backfill   RESOLVES at BBG   unresolvable
DIVZ         21              21 (100%)    --
IDVZ         41              40 (97.6%)   ICT   <- already-known identifier failure, MER's family
```
**PROBE RUN (authorised by his own "pull that data from Bloomberg" — an explicit per-use word):
2 securities x 2 fields, window 2020-12-31 -> 2026-08-24, capped at 6 points. I deliberately chose
the TWO HARDEST CASES — both ADRs, both absent from `bbg-testpull`:**
```
AZN   2026-08-21  ret 0.9058  px 165.98   <- TIES EXACTLY to our stored history_topup
BBSEY 2026-08-21  ret 3.3661  px 7.37     <- TIES EXACTLY
AZN   2026-08-24  ret 0.4398              <- *** BLOOMBERG ALREADY HAS MONDAY ***
```
✅ ADRs resolve · the 5.6y window is accepted · same field, same units, no conversion.
⚠ **`3.0.0_SA_CVO~Z` correctly declined to VERIFY it: his word authorises MY pull, not a second
seat's re-run as a check. Recorded SINGLE-SOURCE — "not doubt, a denominator."** ⭐ **Then they found
HALF of it IS verifiable without a vendor call (re-deriving the stored side) and did so. My
"structurally unverifiable" was too strong, and someone else found the way to check it.**
⛔ **UNMEASURED AND NOT GUESSED: wall-clock for 61 securities x ~1,415 rows. A CAPPED probe proves
SHAPE and RESOLUTION, never VOLUME.**

## ✅ ASK 2 -- MEASURED, AND HE IS RIGHT THAT IT NEEDS NO BBG

`:697` builds the sector map as `if h["sub_asset_class"] and not h["is_cash"]` — **cash and FI rows
are excluded BY CONSTRUCTION:**
```
DIVZ 99.22 vs 99.80 · IDVZ 95.93 vs 99.51 · PFDE 99.65 vs 100.01 · PFOE 97.67 vs 99.99
missing buckets: Ultra Short Duration (all four) · Cash & Cash Equivalents (PFDE, PFOE)
IDVZ ALSO carries 2 rows at sub_asset_class=None -- 2.69% (ICT + MER)
```
⛔ **RULE 24 ON THE PANEL: the buckets must be COLLECTIVELY EXHAUSTIVE or the weights do not sum to
100. IDVZ's 2.69% needs an EXPLICIT bucket; dropping it silently makes IDVZ read 96.8 with nothing
on the page saying why.**

## ⛔ A DEFECT I CREATED, FOUND WHILE LOOKING FOR SOMETHING ELSE

```
bbg/2026-08-21/history_topup.parquet   167 rows, internal date 2026-08-21
bbg/2026-08-24/history_topup.parquet   167 rows, internal date 2026-08-21   <-- MY 02:50Z RE-KEY
```
`load_history()` concatenates every partition; `compute_returns:502-506` iterates rows and compounds
**without deduplicating**. >> **A duplicated (ticker,date) is compounded TWICE — a 2% day becomes
(1.02)^2 = 4.04%. Not a crash: a well-formed wrong number.** <<
✅ **LATENT (every window is incomplete, so all returns are null) and SELF-HEALING (the 11:00Z pull
writes the SAME key with genuine 08-24 rows).** ⛔ **The hazard is a WINDOW, not a state: any producer
run BEFORE 11:00Z. It ARMS ITSELF exactly when the plumbing cell lands — i.e. when someone believes
they are only ADDING data.** **Asked for `(tkr,date)` dedupe in `load_history` REGARDLESS.**
*(Not deleted: S3 deletion needs Andrew's word, and it removes itself in ~7h.)*

## ▶ TWO RULINGS

**1. THE SECTOR-ORDER THREAD, CALLED.** Six seats, five verdicts, twenty-five minutes.
`0.4.0_DS_ClientPlatform~Z`'s reframe ends it: **"nobody reads `segment.sector`" is TRUE (0 hits /
415 files, positive control `allocation.cash`=3 FIRES) and "therefore redundant" is FALSE — the
consumer is the panel Andrew asked for.** One workstream: COMPLETE the buckets · ORDER them ·
RENDER them. **Piece 2 only looked like dead code because it shipped before its reader.**

**2. THE 15h OPEN PROD-PROMOTE LEDGER — `0.7.0_AE_CloudOps~Z`'s find, and the measurement INVERTS it.**
```
LEDGER: 6 legs OPEN, log has ONE entry (OPENED 2026-08-24T12:41Z), RED alarm never fired
LIVE:   origin/PROD 8a96c916 == the ledger's own BEFORE sha · portal-v2.1.164^{} == same
        portal-v2.1.165 DOES NOT EXIST · tree on DEV · no ephemeral worktree
```
>> **NOT ONE LEG EXECUTED. STALE-OPEN, NOT HALF-LANDED. Nothing stranded, nothing to roll back, and
the dormant ADVI cutover code is NOT on PROD.** <<
⛔ **RULED: NOBODY FINISHES IT TONIGHT.** An open promote ledger invites *"finish the promote"* —
CLAUDE.md's own named trap (*"the reflex a drift alert invites is DEPLOY"*). **NEVER#6 binds a BEGUN
deploy; nothing began. The obligation is to CLOSE THE RECORD, DT's call in daylight.**
⭐ **The real finding stands and is AE~Z's: a DECLARED control sat silent 15h. An existing gate that
did not fire is a legitimate report, not a proposal to build (the moratorium bans BUILDING).**

## ⛔ AND MY OWN INSTRUMENTS FAILED THREE TIMES, ALL RETURNING A CLEAN ZERO

```
comp-find sweep      returned 0 for `allocation` TOO -- my grep did not match its output format
ledger status grep   returned 0 across ALL EIGHT files, including ones known fine
(earlier)            the `Real Estate` token -- present in BOTH versions, so not a discriminator
```
**Each caught ONLY by an implausible zero or an in-sweep positive control.** Banked as
`memory/i-validate-on-the-axis-i-searched-not-the-axis-asked.md`.

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| boto3 paginator + csv | `bbg-testpull/` inventory + per-fund coverage | **109 tickers x 1,415 rows, UNREAD by the producer** |
| boto3 overlap compare | `bbg-testpull` vs `history_topup` at 2026-08-20 | 6/6 MATCH, price AND return, 4 dp |
| bloomberg_historical_data | 2 ADRs, 5.6y window, capped 6 | resolve + tie out + **08-24 already available** |
| git ls-remote | PROD head, tags, worktree | **promote never started** |
| aws lambda get-function + zipfile | deployed vs tree | **byte-identical, sha b80f8af6a942ce50** |

## Blockers

None at this seat. **RESERVED at Andrew: the Pathfinder weekend provenance stamp; plus an FYI that I
RULED the sector sequence on his own "whatever we can get" — overridable in one word.**
Deployed == tree, verified with both controls, so **the 13:00Z run executes exactly what is in the
tree.** Duplicate-history hazard binds any producer run before 11:00Z.
