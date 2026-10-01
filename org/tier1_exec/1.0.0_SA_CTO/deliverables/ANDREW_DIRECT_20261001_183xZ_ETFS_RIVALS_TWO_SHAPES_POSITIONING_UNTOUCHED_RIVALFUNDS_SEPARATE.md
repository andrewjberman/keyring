# ANDREW-DIRECT 2026-10-01 ~18:3xZ -- ETFS_RIVALS: two data shapes for IDVZ and PFOE, Positioning untouched

**Channel:** terminal, session of `1.0.0_SA_CTO~Z` (site Z).
**Answers:** my report of PRD v0.8 @`951a2b6a35`, which closed with "Say if you meant something different on the history pull or on SCHY."

## Verbatim

> Correct. We have two different data shapes needed for IDVZ and PFOE. On one side there is the existing Positioning page
> shape. That should not be touched at all. Now, there is a rivalfunds angle. This is separate for separate use case.

## What it settles

- **v0.8 is CONFIRMED as written.** That covers:
  - IDVZ and PFOE on the rivalfunds Bloomberg leg, daily and backfill;
  - one producer inside this pipeline;
  - the controls, ACWI and IWM;
  - SCHY staying a member.
- **The basis for two Bloomberg requests of the home funds is two data shapes for two use cases**, not an exception to
  "never two producers":
  - the Positioning page's shape, which is not touched at all;
  - the rivalfunds shape, which is separate.
  "Never two producers" binds ONE shape. PRD C-HOME-PRODUCER v0.8 is reworded to that basis.
