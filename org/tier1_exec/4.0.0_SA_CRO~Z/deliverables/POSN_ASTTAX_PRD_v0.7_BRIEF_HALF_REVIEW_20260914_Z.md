# L4-R REVIEW -- POSN_ASTTAX PRD v0.7 @3c42ed05d0, BRIEF HALF -- SIGN

**Reviewer:** 4.0.0_SA_CRO~Z (brief half; `TREE_PRD_SIGNOFF`)
**Delivered by:** `1.0.0_SA_CTO~Z` msg 22872, 2026-09-14T17:37:25Z; half_hash `c68851b23d52`
**Reviewed:** 2026-09-14 ~17:4xZ (thirteenth review of this PRD by this seat)

## CONTROLS RUN BEFORE THE STAMP

| control | read | result |
|---|---|---|
| last-touch of the PRD == the review pin | `git log -1 -- prd/POSN_ASTTAX_PRD.md` -> `3c42ed05d0` (1.0.0_SA_CTO~Z, 2026-09-14T13:37:19-04:00) | MATCH |
| bump scope measured, not taken from the description | `git diff --stat ded02d9a9c 3c42ed05d0 -- <prd>` -> 1 file, +81 / -8 | one new s.0 ADDENDUM v0.7 block (71 lines), the header version line, and the FWD-6 rewrite in ENDPOINT (-7 / +10); nothing else moved |
| which half changed | the ENDPOINT byte change is FWD-6 only (CVO's half); everything else in the diff is brief-half | both halves re-open, as the delivery says |
| gate state at review | `prd-signoff.py status POSN_ASTTAX` -> WITHHELD; ratified-text STALE (owed by 3.0.0_SA_CVO~Z), brief STALE (owed by this seat) | consistent |

## CONTENT CHECK -- each addendum entry against the word it carries, CONTENT not pointer

| entry | carries | source word / measurement | verdict |
|---|---|---|---|
| verbatim block | Andrew ~17:2xZ and ~17:3xZ, entire | this seat's records `_172xZ_` @727b82e8d2 and `_173xZ_` @e406e99122 | byte-faithful |
| C-POSITIONING-ONLY | 14 files at `e85f6eb84f` + `src/lib/chartColors.ts`; three modes; Attribution NOT touched; Philosophy/CMA not a focus; the ACCEPTED consequence (VXX drops out of Attribution's per-class groups, weight stays in totals); settles `Z-W15-S2` | ~16:34Z + ~17:3xZ words; file set measured by this seat (`git ls-tree`, 14 files) | content present; matches |
| C-SATELLITE-SOURCE | one total per ticker from BD, summed across sleeves; **Yang's copy never added (LT VXX: 1.87, not 1.87 + 1.50)**; class + sub-asset from the served table; characteristics by an additional lambda with per-ticker inputs (Yang `current_holdings` -> BBG pull -> NULL, null share disclosed); Models mode unchanged; supersedes C-SATELLITE-DATA's "touches NO holding" clause for Satellites; disarm route for `Z-S65` | ~17:2xZ card 1 + card 6; item A approved ~17:3xZ; brief R1-R4 as ruled | content present; matches; `Z-S65`'s disarm condition (a satellite-source constraint in the PRD) is MET by this text -- the citing disarm row is `1.0.0_SA_CTO~Z`'s |
| C-SUB-ASSET | Metals = GLD/IAU/SLV; Hedge = VXX/VIXY/UVXY/QBER; Real Estate = VNQ; others keep current; encoding: `Hedge` is a `sub_asset_class` under `Structured`, top-level `hedge` dissolves, every write level-explicit | item B approved incl. VNQ Real Estate | content present; matches |
| C-RETAG-SET | the 12 by class; BIPC Equity; both stores; runs LAST behind deploy, seeder guard, satellite artifacts, frontend | item C; C-RETAG-SAFETY | content present; matches |
| C-COLOURS | new yellow token for Commodities, never amber; pink Structured; sub-asset colours for Metals/Hedge | card 3 | content present; matches |
| C-BENCHMARK | labelled-zero rows in BOTH functions under ONE sign-off naming both functions and both artifacts; the widening of the 2026-09-13 approval named | card 5 + item F + this seat's N1 | content present; matches |
| C-CUTS | `is_hedge()` / `HEDGE_TICKERS` out (`Z-W1-S1`/`Z-C-S1` carried out of scope); `bd-securities` reconciliation out (`Z-W17-S3` settled) | item E | content present; matches |
| C-DONE | backend deployed + Positioning frontend built and committed behind the freeze; promote is Andrew's separate word | item F; Andrew 05:31Z | content present; matches |
| surface manifest | S1 += satellite holdings producer + characteristics lambda (FWD-1/FWD-2 on Satellites); S3 = the three modes; MECE = assignment, cells serve | brief s.4 / breakdown s.3 | content present |
| heading denominator | `brief_ref` unchanged @03f1d00ec4; `endpoint_outcomes` FWD-1..6 unchanged | header | matches |

## ONE CORRECTION, RETURNED BY PINNED LINE, NON-BLOCKING

`POSN_ASTTAX_PRD.md` @3c42ed05d0, s.0 ADDENDUM v0.7, paragraph 1: cites the aligned breakdown as "(v0.5)" with
no commit. At review time the breakdown's HEAD is v0.4 @c81724453a (msg 22867: "v0.5 lands next"). A citation
without a vintage is not a citation (Rule 22); when v0.5 lands, pin it -- a header-only touch that re-opens no half.

## VERDICT

**SIGN.** The brief half carries every ruling of 2026-09-14 as content, at the pin the CTO delivered, with the bump
scope measured. Stamp: `python .tools/prd-signoff.py sign POSN_ASTTAX --half brief --review <this file>@<its pin>`.
