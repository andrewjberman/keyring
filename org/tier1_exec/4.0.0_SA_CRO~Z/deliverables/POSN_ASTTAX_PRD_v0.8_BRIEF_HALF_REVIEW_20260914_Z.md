# L4-R REVIEW -- POSN_ASTTAX PRD v0.8 @709d7b4221, BRIEF HALF -- SIGN

**Reviewer:** 4.0.0_SA_CRO~Z (brief half; `TREE_PRD_SIGNOFF`)
**Delivered by:** `1.0.0_SA_CTO~Z` msg 22919, 2026-09-14T20:32:14Z; half_hash `805c3ea988fb`
**Reviewed:** 2026-09-14 ~20:3xZ (fourteenth review of this PRD by this seat)

## CONTROLS RUN BEFORE THE STAMP

| control | read | result |
|---|---|---|
| last-touch of the PRD == the review pin | `git log -1 -- prd/POSN_ASTTAX_PRD.md` -> `709d7b4221` (1.0.0_SA_CTO~Z, 2026-09-14T16:32:06-04:00) | MATCH |
| bump scope measured | `git diff --stat 99cc431075 709d7b4221 -- <prd>` -> 1 file, +32 / -1 | the header version line and ONE new s.0 ADDENDUM v0.8 block (31 lines); nothing else moved |
| which half changed | no ENDPOINT byte in the diff | brief half only; `prd-signoff.py status` read before the stamp: ratified-text SIGNED current (3.0.0_SA_CVO~Z), brief STALE owed by this seat |

## CONTENT CHECK -- each addendum entry against the word it carries, CONTENT not pointer

| entry | carries | source word | verdict |
|---|---|---|---|
| verbatim block | Andrew ~19:5xZ (Structured is a pink base for all volatility/options/overlay assets regardless of prior class), ~20:0xZ (JEPI to Structured), ~20:2xZ ("b, Options Income") | relayed to this seat as msgs 22912 / 22916; the third at the CTO terminal | byte-faithful to the relays this seat holds |
| C-RETAG-SET = THIRTEEN | the twelve + JEPI under Structured; BIPC Equity; both stores; last; C-RETAG-SAFETY unchanged | ~20:0xZ word | content present; matches |
| C-SUB-ASSET | `Options Income` = JEPI added; Metals / Hedge / Real Estate unchanged; encoding rule unchanged (level-explicit, top-level `hedge` dissolves) | ~20:2xZ word | content present; matches |
| C-COLOURS | Structured = the pink family; every Structured sub-asset on a pink token distinct from `pink500`, minted where absent; existing `SUB_ASSET_COLORS` keys `Hedge` (green900) and `Volatility` (blue900) re-bind; Commodities stays yellow; amber stays Cash | ~19:5xZ word; portal `chartColors.ts` lines as measured by the CTO (22912) | content present; matches |
| membership basis | 285 rows, one page, 31 distinct sub-assets; `Volatility` only on the four Hedge members; JEPI the one options-overlay name; `Structured Credit` (JAAA, LONZ) stays Fixed Income despite the shared word; JEPI held by no satellite component and no Yang book | CTO census 22912 / 22916 | denominator printed; the shared-word guard is the right one |
| scope of change | brief half only; ENDPOINT untouched; cuts no order; `TO-V8-1` / `TO-V5-1` amended by their issuer | -- | consistent with the gate read |

## ONE CORRECTION, RETURNED BY PINNED LINE, NON-BLOCKING

`POSN_ASTTAX_PRD.md` @709d7b4221, s.0 ADDENDUM v0.8, third verbatim bullet (~20:2xZ): the record
`ANDREW_DIRECT_20260914_202xZ_JEPI_SUB_ASSET_OPTIONS_INCOME.md` is cited without a commit pin, while the two bullets above
it carry `@edbee96c07` and `@114a697fca`. A citation without a vintage is not a citation (Rule 22). Same class as the v0.7
correction; carry it on the next brief-half touch or in the round analysis, never as a touch of its own.

## VERDICT

**SIGN.** Stamp: `python .tools/prd-signoff.py sign POSN_ASTTAX --half brief --review <this file>@<its pin>`.
