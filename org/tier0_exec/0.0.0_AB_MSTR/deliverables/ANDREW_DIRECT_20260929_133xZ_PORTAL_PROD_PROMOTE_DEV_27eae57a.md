# ANDREW-DIRECT 2026-09-29 ~13:3xZ -- promote portal DEV 27eae57a to PROD; seat a DT to run /prod-deploy

**Channel:** Andrew at the `0.0.0_AB_MSTR` terminal (laptop), answering a one-question card at ~13:3xZ.

## The card, verbatim

> Promote portal DEV 27eae57a to PROD now? It is 136 commits ahead of PROD (a0314f22, 09-26), mostly ~D's
> investor-reporting design work, recorded item by item in DSGN_IRPTV1 STATUS.md. It now gates two release orders:
> ~M's Holdings CATEGORY step and AD-10's directory reader. Without it the directory re-mint is held, because the PROD
> reader would refuse the new account_masks key and client search would fail. /prod-deploy is DT-only; on yes I seat
> 0.2.0_DT to run it.

## His answer, verbatim

> Yes, seat DT and promote (Recommended)

The option text he selected: "I spawn 0.2.0_DT to run /prod-deploy for DEV 27eae57a (clean DEV, zero TypeScript errors,
merge forward, push, CI-verified), then tell ~D and ~M."

## Measured at the card

- origin/DEV 27eae57abe (ls-remote 12:14Z by 2.0.0_SA_COO~D; re-read by MSTR), origin/PROD a0314f22a5, 136 commits
  apart.
- Contains 6c163889f4 (2.0.0_SA_COO~M msg 102614) and the account_masks reader (2.0.0_SA_COO~D msg 102776).

## Routing

- Seat: `0.2.0_DT_PortfolioAnalytics~P`, a fresh lane. The base holds 6 open task orders on 2 projects, so the lane
  is used. The lane holds 0 open task orders and has no live process.
- The promote is /prod-deploy's own procedure. Its never-override line cites this record.
- Asks it serves: 2.0.0_SA_COO~M 102614 and 102812, and 2.0.0_SA_COO~D 102776.
- The investor-reporting bundle skip (102500 / 102812) stays in force until the served PROD bundle is read admitting
  account_masks.
