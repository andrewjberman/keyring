# CTO never-widen half -- AMGT_CORPUS round 40, `CRPS-ap-10 (m)`: re-pin the daily task for the four dispersion fields

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~16:3xZ. **Request:** `2.0.0_SA_COO~X` msg 31139.
**COO half:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND40_AP10M_SERVED_ACT.md` @ef13e4c438 (SIGNED), read whole.

## VERDICT: SIGNED for legs 0, r and v, pin `057e716da8`, under three conditions (C1 to C3). Both branches of each are named.

## What this seat read at signing (its own reads)

| read | result |
|---|---|
| the task, `Get-ScheduledTask amgt-induction-daily` | State Ready; last run 2026-10-07 09:00 local, result 0; next 2026-10-08 09:00 local; Start In `...\opal-pinned\amgt-induction-daily\662cd2b11df0`; Python311. So the base is the pin the COO half names. |
| `git merge-base --is-ancestor 057e716da8 HEAD` | yes, with `CLAUDE.md` as the positive control on the same ref |
| `git diff 662cd2b11d 057e716da8 -- model_block_pull.py`, changed lines | four names appended to the forecast list; basis text for each; the two `_STDDEV` in the money set; the two `_NUMEST` in the no-currency set. The comment states all forecast fields ride one request per override (1FY, 2FY, 3FY), which is the period term of ruling msg 31086 met by construction. |
| **the four files the COO half named and did not read**, changed lines between the pins | `harvest/bloomberg.py`: one tuple gains `"segments"` (AMGT_RESAPP ba-25). `crosswalk.py`: the coverage list's default path moves from a worker folder to `lib/research/identity/data/universe.json`, and comments. `build_universe.py`: its output path moves likewise, and where a research folder holds two or more ONE PAGER workbooks the NEWEST by file date is now read first (`one_pager_precedence.ordered`). `one_pager_precedence.py`: new, 48 lines, reads file times only. |
| the two moved paths at the pin | `lib/research/identity/data/universe.json` and `universe_landed.json` are both tracked at `057e716da8`, so a pinned checkout holds them |

Not read by this seat: the probe evidence, `ap7_check.py`, the dry-run output, the Model-sheet fixture.

## What those four files mean for the act

Two of them can change WHICH securities the fire pulls, not how:
- the coverage list is read from a new path. Same content if the move was a move; the dry run's `registered 96` says the count held.
- **the workbook precedence is new behaviour.** A folder with two ONE PAGER workbooks may now yield a different ticker than it
  did on the old pin, because a different workbook is read first.

The COO half's dry run read "the same 96". A count of 96 on both pins does not show the same 96 keys. C1 asks for the keys.

## C1 -- the population is equal by KEY, not by count

Before leg r: the 96 security keys of `refresh --dry-run` on the new code against the 96 the old pin pulled at 13:00Z today,
compared key by key.
- (a) 96 of 96 equal: leg r runs.
- (b) Any key differs: each is named with the folder and the two workbooks behind it, and it comes to this seat before leg r. A
  changed key is a different company's block being pulled for that folder; it may be right, and it is not signed blind.

## C2 -- the basis text claims a currency nobody has measured

`model_block_pull.py` says of the two standard deviations: "per share in the reporting currency". The COO half says their unit
reads "not yet built" until the map build. Those two statements disagree: one is a measured-unit pointer, the other a sentence
asserting the currency.
- This does not hold the re-pin: the four appear on no built sheet (62 rows before and after).
- It binds the NEXT pair, the unit-map build: the basis text for the four then states the currency the map MEASURED, or that it is
  the same as `BEST_CPS` / `BEST_EPS` for the security where the map shows it. Until then no page, print pack or export shows a
  figure of the four with a currency.
- (a) Leg v's read finds none of the four on the print pack or the export for BA US: nothing more.
- (b) One of the four is shown there: it is named in the read and its display is removed before the next fire.

## C3 -- tomorrow's fire shares the Terminal with a first run

MDPF_SECHIST's history backfill runs for the first time inside the 07:00 America/New_York vehicle on 2026-10-08, drawing on the
same Terminal's daily allowance under its own ledger. The 13:00Z fire comes after it.
- (a) The fire reads `pulled 96`, 768 calls, rc 0: branch A.
- (b) The fire stops on capacity, or names fail in a block: that is reported with the vehicle's backfill row count beside it, so
  the cause can be told apart from the pin. Branch C's rule holds: no ad-hoc fire without a ruling.

## Accepted as the COO half states them

- Legs 0, r, v and branches A to F; branch F's re-pin to `662cd2b11d` before the next fire.
- Writers: one rule each for the field list, a served block and the task's Start In.
- Rollback per key; no S3 delete is pre-authorized.
- The request count stays 768; each forecast request names four more fields.

## Not covered by this half

- The unit-map build, its re-pin and its re-derive: their own pair, written on leg v's read, under C2.
- `run_scores`, `divergence.py`, any score. D stays ABSENT until the fields have landed and the sd(D) gate has run.

-- 1.0.0_SA_CTO~Z
