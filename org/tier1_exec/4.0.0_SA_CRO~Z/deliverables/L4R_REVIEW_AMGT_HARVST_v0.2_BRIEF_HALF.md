# L4-R REVIEW -- AMGT_HARVST PRD v0.2, BRIEF HALF -- verdict: SIGN

**Reviewer:** `4.0.0_SA_CRO~Z`. **PRD:** `org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md` @`9102ccfe81`,
v0.2, brief half hash `12aa73e8bb31` (msg 24285). **brief_ref:** the tree brief @`5b90a0b839`. **Prior act:** v0.1 brief
half REFUSED @`37abb4289a` on the superseded pin.

**Independence limit:** this seat authored the brief; graded here is whether the brief half carries the brief's content
at the named pin, and whether the refusal's grounds are discharged.

## The pin

`brief_ref` now points at `@5b90a0b839`, the re-landed brief carrying Andrew's two words. `git log 5b90a0b839..HEAD`
on the tree brief is empty, so the pin is the brief's current state. Discharged.

## The refusal's four grounds, against `git diff 16db74edea 9102ccfe`

| v0.1 ground | v0.2 | result |
|---|---|---|
| `C-HV-DAILY-DENSE` stored `breakout_ratio` and `z_score` (ratified half) | absolute columns only, with the serve-time sentence quoting his word; new `C-HV-ABSOLUTE-ONLY` | discharged (the CVO grades the text; the brief half's manifest row H5 now reads "absolute only, dense from 2026-01-01") |
| constraints `:276` had a watermark and no floor | "pages back to the later of the FLOOR (2026-01-01) and ... the WATERMARK" | discharged |
| the manifest had no backfill row | H10: the 2026 backfill run, floor + watermark, page counts printed first, `retrieval_mode=backfill`, depends on H1-H6, feeds FWD-9 | discharged |
| no FWD named the backfill | FWD-9, DONE WHEN EXERCISED, with the printed page count, the dense series from 2026-01-01 and idempotence in its own words | discharged |

## Brief coverage, the rest of the half

The boundary (`C-HV-BOUNDARY`: the Lenovo stage-9 pass runs here, once), the constraints (mention floor never raised;
no relative figure stored; the backfill per security on the word for that run), the manifest H1-H10, and the calls
kept as Andrew's (brief s.8, now including call 8, the backfill order) carry the brief's content, not pointers.

## Notes, none a ground for refusal

1. **`mention_density` is dropped from gold** ("the share of blocks is computed where the tier is assigned and is
   never stored"). The brief s.6.1 lists it as a stored column. The L4 author read a share as relative under Andrew's
   word; `blocks_hit` and `blocks_total` stay, so the share is recoverable at serve time and nothing is lost. The
   brief is not re-landed for one column; the contract binds.
2. **The tier rule is now a partition** (A then B then C then D, first match wins), tighter than the brief's table,
   and it assigns every case. Good.
