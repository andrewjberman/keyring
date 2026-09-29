# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- irpt-performance-adapter qfxZ0DzB -> qosuSxAf: 49 Financial Performance read from the holdings-basis gold, the engine read retired (IB-pr-201/202)

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_ADAPTER_HOLDINGS_GOLD_49F_20260929.md`
blob `189aaef2` (at `bdc080a0a1`, at HEAD, and on disk; read 2026-09-29 04:3x-05:1xZ).
- **Word diff:** a new packet for a new act (PRD ADDENDUM v0.19 rulings 10 and 12). No prior packet to diff against.
- **Asked by:** 2.0.0_SA_COO~P, msg 102579. **Other half:** 1.0.0_SA_CTO. **Ledger:** `irpt-adapter-holdings-gold-49f-20260929`.
  This seat is not in the act. The act applies only after window 21 closes, so this refusal holds nothing live.

## VERDICT: REFUSED on blob 189aaef2 -- the input the act chains carries figures the act itself exists to retire

The code does what the packet says. The gold it reads does not carry what the packet claims. Read from the producer's
own rule (`data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` @e29adc9fa7, HEAD) and its own
output, row A's AFTER column ("the holdings chain, prod(1+r)-1 over status-OK days") is, for a measured population of
49 Financial accounts, a figure over +100% (18 accounts over +1,000% year to date, the largest 1.1e57) and, for
others, a figure at or under -100% -- the shape ruling 12 retires with no fallback. Two mechanisms, both in the
producer, both reproduced here. Sections 5 and 6 name what a re-ask needs.

## 1. The artifact, read here on its own bytes (consistent with the packet)

- **Bytes:** S3 `opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip` VersionId
  `ABB89j26` hashes to `qosuSxAf`; the live `5bmwADQs` hashes to `qfxZ0DzB`, equal to the function's CodeSha256.
- **Census:** 69 -> 70, `holdings_gold.py` added, nothing removed; four members differ and each is byte-equal to
  HEAD and to `a595a14264`: `retained.py` bf5f00e8, `entry.py` b34a1171, `installed.py` a2125b3a, `holdings_gold.py`
  afc37c0a. The zip's `PerformanceReport.schema.json` (c4e2fdb1) is `docs/contracts/investor-reporting/v1/`'s copy at
  both pins and carries OPAL_HOLDINGS beside OPAL_ENGINE (78eeb223f8).
- **Tests on the zip's modules:** 13/13 and 19/19 pass on the new bytes; the live zip fails exactly the two new
  tests, so the tests tell the two zips apart.
- **Terraform:** every prefix in `performance/retained.tf` and `shared-infra/s3-49financial.tf` (ae20e904e6) is
  `lib/opal_naming.address()` output for `irpt/49financial/gold/holdings_performance_daily/`.
- **The gold's shape:** 557 partitions under the prefix = 557 trading days (2024-07-09..2026-09-25, `lib/trading_calendar.py`);
  3,188,339 rows over 8,818 account keys; the adapter's `map_account` resolves all 7,540 keys of 2026-09-25 through
  the zip's `ids.opaque_account`.

## 2. Where the packet's claim and the world differ: the manifests

"557 of 557 days, every manifest complete=True" (CTO ruling 102520 as MET) is **556 of 557** measured.
`holdings_performance_manifest/date=2026-09-25/manifest.json` (1,477 bytes, written 03:04:26Z) carries none of
`complete`, `computable_count`, `not_computable_count`, `accounts_with_prior_holdings`: the shape from before
`manifest_counts` landed (e29adc9fa7). `date=2026-09-24/manifest.json` (2,197 bytes, 01:42:39Z) carries
`complete=True`, 6,326 computable of 6,328. The 2026-09-25 partition is the last day of every window.

## 3. Mechanism 1 -- every cusip-less position is priced as ONE security

- **Silver** (`opal-data-assets/schwab/08335338/silver/dim_position/`, 2026-09-24 and 2026-09-25): 106,513 and 106,835
  rows; **41 rows per day carry `cusip == ''`** (the empty string, never null; `ticker_symbol` blank too) across
  **33 accounts**, with **18 distinct closing prices** among them (0.00, 1.00, 2.96, 4.87, ... 14.685) and **21 rows
  priced 1.00 whose quantity equals their market value** (cash-like).
- **Producer rule** (`holdings_performance.py:264-275`): the t-1 price is the account's own (`first` per account and
  key), but the day-t price is looked up PER KEY, `px1 = p1.groupby(["cusip"])["_p1"].first()` -- "a closing price is
  an attribute of the security". With a blank key every cusip-less position shares one day-t price: the partition's
  first cusip-less row, **14.685** on both days (51.2671 / 51.6872 on 2025-09-08 / 2025-09-09).
- **Reproduced in the gold:** a cash-like position priced 1.00 at t-1 reads `r = 14.685 / 1.00 - 1 = 13.685`;
  **17 OK rows at 2026-09-25 carry exactly that**, each a one-holding account whose only position is priced 1.00 on
  both days in the silver. The window's largest OK row, `r = 439.43` on 2025-09-09 (account ..0273), is one
  cusip-less position at 0.31 (value 225.48) priced at 51.6872, over a base of 85.04 (cash -140.44).
- **Window census** (2,780,996 OK rows): **4,061 rows with |r| > 0.5 across 44 accounts**.
- `tests/test_holdings_performance.py` (cases 1-4, lots, padding, the status enum, the manifest) has no cusip-less
  fixture; the per-key rule is untested exactly where it breaks.

## 4. Mechanism 2 -- an OK row over a near-zero net base

The base is `included_value + cash`, cash the SIGNED `net_credit_debit` (a margin debit lowers it). OK requires only
`base > 0`. **Four OK rows carry `r <= -1`:** 2024-08-01 ..4581 -1.122 (base 1,023.70; included 99,799.23; cash
-98,775.53), 2024-11-18 ..9176 -3.466 (base 4.87), 2025-02-20 ..9461 -2.103 (base 65.45), 2026-03-18 ..0695 -1.886
(base 752.91; included 109,226.44; cash -108,473.53). The producer's docstring (`:26-28`) says a holdings-based
return "CANNOT reach -1 while any held position keeps a price"; its own output has four OK rows that do.

## 5. What the act would serve -- both readers, read from the adapter's own rule

`holdings_gold.py:191-203`: `running *= 1 + daily_return` over the account's OK rows inside the window; the ONLY guard
is `math.isfinite(value)`. Applied here to the gold over calendar windows ending 2026-09-25 (YTD from 01-01, 1Y from
2025-09-26, SI all):

| window | accounts with an OK row | chain >= +100% | of which >= +1,000% | chain <= -100% | chain in (-100%, -50%] | non-finite (the only refusal) |
|---|---|---|---|---|---|---|
| YTD | 7,127 | 22 | 18 (max 1.13e57) | 2 (min -236%) | 10 | 0 |
| 1Y | 7,300 | 36 | 32 | 2 | 7 | 0 |
| SI | 7,814 | 42 | 33 | 5 (min -320%) | 11 | 1 |

28 of the 34 YTD accounts outside (-50%, +100%) held a cusip-less position at t-1 of their extreme day (mechanism 1);
the other 6 are near-zero-base rows (mechanism 2: ..0695, ..4276, ..8878) or one- and two-position accounts.

- **Fresh reader:** publishes the chain and returns it through `reopen(pointer, check_engine_series=False)`
  (`retained.py`) -- no plausibility read on this path.
- **Reopen reader:** `implausible_engine_series` (any point <= -1) runs on every 49F pointer's SECOND read, whatever
  its basis. So a chain at or under -100% is served once, then refused; a chain at +1.1e57 is never refused.
- **Rows D, E, F** read as the packet says: an OPAL_ENGINE pointer sits at the old key namespace and is not reopened;
  an OPAL_HOLDINGS pointer reopens; no Cottonwood or Inflection member moves.

**The packet's own before/after reads cannot see either mechanism.** The 23 retained 49F reports belong to six
accounts and none holds a cusip-less position at 2026-09-24. Read from the rule, for the same account and window:
NEW-01's account (790fe675 1Y, 74fb35a4 YTD; served -100%) chains **+0.49%** over 69 OK days (183 and 112 non-OK
days disclosed PARTIAL); the control (e386cdc8 YTD, served 5.93%) chains **5.16%**. The other four accounts: 5.25 ->
4.39, 7.77 -> 6.61, 7.33 -> 4.95, 9.57 -> 0.04 (YTD) and 8.80 -> -0.85 (1Y). Every comparable account reads below
the engine, consistent with a price-only return (income is disclosed as the `fees_and_income` absence); the 9.5-point
pair (..558d) is wider than income explains and is not measured further here. Named, not a refusal ground.

## 6. What a re-ask needs

1. **Producer (workstream ~E):** a cusip-less position is never priced by key. Ruling 4's own words already cover it
   ("a holding without a positive price on BOTH days is EXCLUDED"; a blank key has no price of its own); whether a
   cash-like row (price 1.00, quantity == value) is carried as cash instead is the CTO's ruling. Re-emit the 557
   partitions and manifests (557 of 557 `complete=True`); one unit test with two cusip-less positions at different
   prices; a census printed in the proof: OK rows with |r| > 0.5 before and after.
2. **Producer, the near-zero base:** a rule for an OK row whose base is a small residual of a large book -- a base
   floor, or a fifth status member with its four-postulate record (CLAUDE.md rule 24). The CTO's call; this half only
   names the four rows.
3. **Adapter:** the fresh path refuses the shape the reopen path refuses (any series point <= -1, reusing
   `implausible_engine_series`), so the two readers agree; a ceiling is the CTO's call.
4. **The after-read** adds one cusip-less-holding account and one near-zero-base account beside NEW-01 and the
   control, so it discriminates on both mechanisms; the packet's manifest claim is re-measured on the re-emitted gold.

Surprise row: `IRPT_BCKEND-S195` in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`.

## What this half refuses against

- Packet blob `189aaef2`; artifact `qosuSxAf` (S3 `ABB89j26`), commits a595a14264, 78eeb223f8, ae20e904e6.
- The gold at 2026-09-29 04:3x-05:1xZ: 557 partitions (`date=2026-09-25/data.parquet` version `mPmlDTUG`, 03:04:26Z),
  the silver `dim_position` partitions of 2026-09-24/25 and 2025-09-08/09, and the chain census in section 5.
- Not refused: the design (rulings 10 and 12), the code, the plans, the prefixes. Everything in section 1 carries to
  the re-ask unchanged; the before-read this seat owes (packet section 3 step 2) stands and is taken when the
  re-cut packet lands.

## Addendum 1 (2026-09-29 ~07:0xZ) -- precision on section 2: the two manifest surfaces of 2026-09-25 disagree

Section 2 read `manifest.json`. The manifest has TWO surfaces built from one dict (`holdings_performance.py:453-467`),
and `~P`'s E3-AC4 check (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r3e/e3_ac4_49f_reemit_v020.py`)
reads the PARQUET surface, which is why its base run prints 557 of 557. Measured here, `holdings_performance_manifest/date=2026-09-25/`:
- `data.parquet` (11,448 bytes, **01:48:56Z**): carries the four completeness keys; `complete=True`, computable 6,338,
  not computable 3, accounts with prior holdings 6,341.
- `manifest.json` (1,477 bytes, **03:04:26Z**): 16 keys, none of the four.
- The daily partition `holdings_performance_daily/date=2026-09-25/data.parquet` was ALSO written at **03:04:26Z**
  (version `mPmlDTUG`), 76 minutes after the manifest parquet. So the served 2026-09-25 rows come from a later run on
  producer bytes that predate `manifest_counts` (e29adc9fa7 writes both surfaces and both keys), and the manifest
  parquet describes an earlier write of the same day. 2026-09-24's three objects were written together (01:42:38-39Z)
  and agree.

So: "556 of 557" is true of the json surface and "557 of 557" of the parquet surface; the fact under ruling 17 is that
one day's surfaces disagree and its rows and its manifest are from different runs. The re-emit ordered by TO-IB-er-301
amendment 1 rewrites all 557 days and both surfaces, which retires this; the re-read of the re-cut packet checks BOTH
surfaces agree on every day. Not a refusal ground then or now; recorded so the CTO's v0.20 source paragraph and
E3-AC4's "557/557" are read against the same object.
