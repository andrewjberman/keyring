# Andrew-direct 2026-10-14 ~09:0xZ (laptop, 1.0.0_SA_CTO terminal) -- there is no hold on the Bloomberg sign-in repairs

## VERBATIM

> "What is the hold you are referring to? There should be no hold"

He was asked about site Z call `sitez-20261013T215225Z-6c9f`: "does your 'make sure that's functional' lift the 10-06 no-modify hold
on the Bloomberg sign-in scripts for repairs R2 (landed @f6cc68d6bf) and R3 (held)? No answer by 10:30Z = R2 reverted before the
07:00 ET pull".

## What the record shows

The 10-06 record (`ANDREW_DIRECT_20261006_201xZ_BLOOMBERG_NO_MODIFY_IS_POSITIONING_AND_ETFS_VIEW_RESEARCH_OUTSIDE_OPEN_SEASON.md`)
quotes his words as: "What i wanted to avoid with this process was accidentally overwriting any operations in the 'Positioning'
pipeline and ETFS view operations." Its "Unchanged" section extended the order to "the vehicle and the sign-in scripts". That is
the recording seat's reading (via call 5 of the 10-06 18:18Z record), not his words.

## Applied

- **No hold applies to the Bloomberg sign-in repairs.**
  - R2 (the 8194 gate fix, landed @f6cc68d6bf) STAYS. It is NOT reverted at 10:30Z.
  - R3 (the focus-loss fix, held) may land, as a change-managed repair, before or after the 07:00 ET pull, at site Z's judgement.
- Call `6c9f` is closed by Andrew's word (site Z's list, `--ruled-by andrew`, this file).
- **What still binds, as he said it:** do not accidentally overwrite Positioning pipeline or ETFS view operations. Any change that
  touches those runs carries a read showing it does not.
- **Not decided here:** whether the same word lifts the wider no-modify reading for `sitez-20261013T021538Z-2da6` (merge TO-GUARD-4,
  a third file in `integrations/bloomberg/`). That is asked of him separately.
