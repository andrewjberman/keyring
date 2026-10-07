# AMGT_CORPUS round 39 -- `CRPS-ao-2` never-widen half (CTO), `1.0.0_SA_CTO~Z`, 2026-10-06 ~19:5xZ

**Pairs with:** `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND39_AO2_SERVED_ACT.md` @92cf1f322b (msg 30254).

## VERDICT: SIGNED (2026-10-06 ~20:1xZ). It supersedes the HELD verdict of ~19:5xZ kept below.

**Andrew answered the scope question at ~20:13Z:** "Research is outside it, yes. What i wanted to avoid with this process was
accidentally overwriting any operations in the "Positioning" pipeline and ETFS view operations. Research is outside of that
edict." Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261006_201xZ_BLOOMBERG_NO_MODIFY_IS_POSITIONING_AND_ETFS_VIEW_RESEARCH_OUTSIDE_OPEN_SEASON.md`.
The technical review and the four conditions below now bind as the signed half. Legs (r), (p) and (v) may proceed.

## The HELD verdict as first written (~19:5xZ): the technical review is clean, and one scope question is with Andrew.

**The question:** Andrew re-affirmed at ~18:18Z (`ANDREW_DIRECT_20261006_1818Z_ALL_RECS_APPROVED_MSTRZ_OPEN_CALLS.md`, call 5) that
the `integrations/bloomberg/` no-modify order STANDS.
- The re-pin makes the daily scheduled task run `integrations/bloomberg/research/model_block_pull.py` as changed by ao-1
  (`ca74f3938c`, +34/-4).
- AMGT_CORPUS has edited that file under CTO rulings in rounds 34, 37, 38 and 39 (`a97635fc69`, `2ff61a4d6d`, `1712df25cf`,
  `ca74f3938c`), reading the order as covering the vehicle and sign-in scripts.
- This seat cannot find the order's original wording that settles whether `research/` is inside it. So the scope goes to
  Andrew rather than being read narrower or wider here (CLAUDE.md section 2(b)).

**If Andrew says the order does not cover `research/`:** this half flips to SIGNED as written below, with no re-review.
**If it does:** the half is REFUSED, the task stays on `6f6e472641`, and the ao-1 change (and rounds 34-38's edits) go to Andrew
as a question.

## The technical review (done; holds on a SIGNED flip)

- **The pin:** `662cd2b11d` is on CLOUD. The live task `amgt-induction-daily` has Start In
  `...\opal-pinned\amgt-induction-daily\6f6e4726414e`, Next Run 2026-10-07 09:00 local (13:00Z), Last Result 0.
- **`integrations/bloomberg/` between the pins:** 5 files.
  - `research/model_block_pull.py` (ao-1) and two tests.
  - `pipeline/etf_daily_pull.py` (the laptop's DIVZ/IDVZ walk-back fix, Andrew call 1) and
    `pipeline/backfill_extra_securities_history.py`. Neither is in the fire's import closure (the COO half's 21 modules), so
    they are inert under this task.
- **Branches:** A, B, C and D cover every outcome.
  - The plant is one write-once key derived from BA's current raw stamp, so values move 0.
  - Branch D stops before the plant. That is right, because a plant under the old pin is Z-S88 itself.
- **Conditions on the SIGNED flip:**
  1. `-Status` after (r) reads the `662cd2b11d` workdir.
  2. The plant lands between 00:00Z and 12:30Z on 10-07. `refresh --dry-run` lists BA as REFRESH before the fire.
  3. The fire read prints `already_current 0 pulled 96` (or each failure with its name, Branch B), plus the round-38 census at
     build 1/1 and control 1/1.
  4. No ad-hoc Bloomberg pull on any branch.

`1.0.0_SA_CTO~Z`, 2026-10-06 ~19:5xZ.
