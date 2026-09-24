# Inflection Eclipse portfolio membership capture (snapshot model overlay input)

**Prepared by:** `4.0.0_SA_CRO`, 2026-09-24 ~00:4xZ (2026-09-23 ~20:4x ET). **For:** `2.0.0_SA_COO~M` (the snapshot
model-overlay goal, msg 99784), copy `1.0.0_SA_CTO`.

## Authority

Andrew-direct at the 4.0.0_SA_CRO terminal, ~00:3xZ 2026-09-24 UTC, VERBATIM, answering this seat's three open
questions (the Eclipse membership read, the SmartX SFTP receiver route, a draft reply to SmartX):

> *"you have egress for whatever you want. dont worrry about smartx we pull all their shit anyway"*

**Scope as recorded:**
- A standing vendor-egress authorization **to this seat**. It is not transferred to any other seat; each seat's
  own vendor calls still need Andrew's word to that seat.
- The SmartX half closes this seat's two SFTP questions only. SmartX data keeps arriving through the existing API
  pull, so this seat pursues nothing further on the SFTP feed. It is **not** a stop order on anyone else's SFTP work.

## What was called

- **Endpoint:** read-only `POST https://www.orioneclipse.com/v1/portfolio/portfolios/accounts/simple/list`,
  body `{"ids": [...]}`. The vendor OpenAPI titles it "Get list of all Accounts of Portfolio By Ids".
  - The WRITE endpoints beside it, `POST`/`PUT /portfolio/portfolios/{id}/accounts` (assign / un-assign), were NOT
    called.
- **Session:** the production puller's own session: `load_eclipse_jwt()` and `_eclipse_headers()` from
  `data/inf/scripts/bronze/pull_eclipse_portfolios.py`, secret `orion/eclipse_jwt/current`.
- **Portfolio ids:** all 858, from `s3://opal-data-inf/bronze/eclipse/2026-09-23/portfolios_full.json` (VersionId
  `i6sOum3KCgL1WzKMcrb6Rc7lyFY2vtSk`).
- **Calls:** 9, in batches of 100, 100 and 58 ids. All returned HTTP 200 with no retries. Receipts with sha256 are in
  `.runtime/codex-seats/4.0.0_SA_CRO/eclipse_membership/receipts.json`.
- **Raw bodies and map:** `batch_00..08.json` hold raw bodies with names and account numbers. `membership_map.json`
  is a compact map: 860 rows of portfolioId, accountId, modelId, model, isSleeve, sleeveType, sleeveTarget, isSMA,
  managementStyle, isDeleted, status; sha256 `789dd95d3d36...`. Both sit in the same gitignored folder and are
  **not committed** because they contain client data.

## What it shows (measured)

| Measure | Value |
|---|---|
| Portfolios asked / answered | 858 / 858 |
| Account memberships returned | 860 (860 distinct accounts, across 800 portfolios; 58 portfolios empty) |
| Returned count per portfolio vs `numOfAssociatedAccounts` | equal on **858 of 858** |
| Single-account portfolios: member == `/simple` `accountId` | **786 of 786** |
| Multi-account portfolios | 14, holding **74 sleeve accounts** (isSleeve true on 74/74) |
| Sleeve types in those 14 | Normal 32, Distribution 14, Contribution 14, Custodial 14 |
| Sleeve rows carrying a model | 35 of 74 (8 distinct models) |
| All 860 rows carrying a model | 684 (19 distinct modelIds) |
| Accounts in more than one portfolio | 0 |
| Join to Orion positions (`bronze/positions/2026-09-23.parquet`, VersionId `VIcks2ylaVwHg_iPwetptYEI9w8NpJnT`) | 860 of 860 membership accounts present; 98 positions accounts have no Eclipse portfolio |
| Positions value in membership accounts | $208.3M of $209.4M (**99.5%**) |

**Reading:**
- The 14 multi-account portfolios are sleeved portfolios. Each carries one Custodial, one Contribution and one
  Distribution sleeve plus two or three Normal sleeves.
- Models sit on the sleeves, not on the portfolio. The sleeve-to-account link was the gap in the daily pull, which
  records only `numOfAssociatedAccounts` and a single `/simple` `accountId`.
- With this map every Inflection account in the Eclipse estate resolves to its portfolio and, where present, its
  model.
- The 98 positions accounts with no portfolio hold about $1.1M and are outside Eclipse.
- The positions file key `2026-09-23` carries the prior close (see the INF bridge finding @`10f3cf6f9f`).

## Not done here

- This is a point-in-time read, not a pipeline. The same call belongs in the daily Eclipse pull if the overlay is
  to stay current. That build is `2.0.0_SA_COO~M`'s under its goal. This record's egress authorization is this
  seat's only, so whether adding the endpoint to the scheduled pull needs Andrew's word is for `2.0.0_SA_COO~M` or
  `1.0.0_SA_CTO` to confirm with him.
- No builder or Opal data changed.
