# SSCN_PRICOL — price column landed; project complete (session close)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

Window 2115Z–2220Z, 2026-08-07. Continues
`sscn_pricol_datarefresh_landed_price_fenced.md` (@`f90d869270`).

## Outcome

Both halves committed. Project complete on the DE side.

| commit | half | state |
|---|---|---|
| `7877d7e1` | DataRefresh accepted-file list | **LIVE on PROD** `portal-v2.1.159` |
| `9bd2365b` | SecurityScanner Price column | on DEV, DT promoting |

## The unblock, verified independently

`0.3.0_DT` landed the producer leg (commit `c76aaef814`, Terraform `safe-apply`,
processor re-trigger) and reported green. **I re-derived it rather than accepting
it**, and via different data than DT used:

- r1000 **1020/1022** rows carry a non-null price; acwx **1828/1830**
- S3 write times moved off 15:00:33Z → 21:59:13Z
- **`price` present on the ROW and ABSENT from `values{}`** — it did NOT leak into
  the factor/percentile machinery. This was the check I most wanted; it is correct.

DT verified sp500 + the deployed zip bytes; I verified r1000 + acwx + the `values{}`
exclusion. Two derivations, different paths, same conclusion.

Nulls are genuine per-name nulls (NKE; the cross-universe null `US066922477` is a
CUSIP-shaped identifier, not a real ticker). They render honest-absent as one
em-dash among real values — categorically NOT the dormant all-dashes case the hold
was for.

## The finding that changed the deliverable

**`price` is in LOCAL TRADING CURRENCY, not USD.** Measured on the 2026-08-06 upload:

| universes | measured | verdict |
|---|---|---|
| sp500 / r1000 / r1000v | UNITED STATES only; max 6,304.81 (NVR) | USD |
| acwx / eafe / eafev | 47 / 23 / 23 countries; 126 / 27 / 8 names >10,000; acwx max 2,708,000 (South Korea) | LOCAL |

My first draft formatted `$${value}` — which would have rendered a Korean listing
as **"$2,708,000.00"** to Yang. The `$` is now conditional on `US_ONLY_UNIVERSES`,
reusing the SAME predicate that already drives the Country column (`showCountry`),
with the currency basis stated in the header tooltip either way. Flagged to DT with
an explicit **do not normalize FX at the producer** — that would be a derivation and
outside the fence.

## What the screenshot caught that code review could not

At my first column width (100px), **NVR ellipsized to `$6,304...`**. A truncated
price defeats the entire purpose of a plausibility check — and it would have looked
completely fine in the diff. Widened to 130px, sized for the widest REAL value
(acwx's `2,708,000.00`), and re-rendered to confirm.

**This is the portal screenshot law earning its keep, on a change that was "just a
column."**

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| `ui-smoke.mjs` | `security-scanner --fixtures --click "Universe Data"` | PASS | the decisive instrument; caught the truncation. Fixtures built from REAL served rows, not invented |
| `ui-smoke.mjs` | bare `security-scanner` (first attempt) | **FAIL — did not verify** | landed on Factor Bank, API 403 under the auth stub. Recorded as a non-verification rather than counted as a pass |
| native `Grep` | `activeTab` / `searchParams` | PASS | established the tab is local state, not URL-addressable — which is why the fixture+click route was needed |

**What worked:** fixturing from the actual served artifact meant the render exercised
real magnitudes — the truncation only appears at NVR's 4-digit price, which an
invented fixture would likely have missed.
**What failed:** my one-off DOM probe read the Price column index against
`.ag-center-cols-container` while `ticker`/`name` are `pinned:'left'` and live in a
different container — so it returned Country values and a confident
`ANY "$" PRESENT: false`. **A clean answer from a misaligned retrieval.** I discarded
it and read the PNG instead. Logged because the wrong-domain-clean-answer class is
exactly what CLAUDE.md's retrieval-control rule names.
**Gap found:** none new.

## Files Modified

see commit message: `9bd2365b`.

## Blockers

None.

## Current State

- `portal` main tree on **DEV** (Rule 19), never moved. `9bd2365b` LOCAL/UNPUSHED;
  DT owns push + promote. It sits on top of `7877d7e1`, so one promote carries both.
- `types.ts`: `price: number | null` on `UniverseDataRow` and `ScannerRow`.
- Column def in both tabs immediately BEFORE the `field: 'mktVal'` block, width 130,
  `$` conditional on `!showCountry`.
- typecheck exit 0. Lint unchanged — still only the pre-existing
  `ModelPortfolios.tsx:15` `ReferenceLine` error; DT confirmed `deploy.yml` has no
  lint step, so it never touched PROD.
- Render evidence: `portal/.frontend-dev/screenshots/sscn_price_grid_v2.png` (US) and
  `sscn_price_intl.png` (international). Temp probe script
  `scripts/.tmp-sscn-intl-smoke.mjs` was deleted after use — not committed.
- **Andrew's case works end to end: AU renders `$87.59` beside `$44,234` ($M).**

## Next Steps

1. **[0.3.0_DT_TradingOperations]** Promote `9bd2365b` (second promote of the day;
   they offered while warm).
2. **[none]** No open DE work on SSCN_PRICOL.

## Note for the record — a relay compression worth watching

Andrew's "I see you all saying you cant find the price column or its not in the data
set" did not match what I reported. My finding was that the Excel HAS the column
(citing its presence in `NON_SCORING_COLS` as evidence) and that the SERVED JSON did
not. **The layer distinction WAS the finding**, and it compressed somewhere into "the
data isn't there" — the one reading that makes the work look wrong. The same
compression would turn any producer-vs-served finding into an apparent dead end.
