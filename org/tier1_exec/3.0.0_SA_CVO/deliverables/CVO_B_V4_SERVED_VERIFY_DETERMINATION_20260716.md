# V4 SERVED-VERIFY DETERMINATION -- **PASS** on the first post-cutover nightly

**agent:** `3.0.0_SA_CVO~B` (Andrew-direct dedicated AoR validation lane, LD-0277) · **date:** 2026-07-16 ~15:2xZ
**verifies:** the served output of the 2026-07-16 13:47Z dispatch -- the FIRST post-cutover nightly under the
standing daily release (AMEND 62) -- against the det-#5 §6 bar, pre-registered 2026-07-15 BEFORE this
artifact existed. **This is the V4 that det-#2/#4/#5 carried as `WITHHELD -- NOT RUN -- EXPLICIT GAP`. It has
now RUN, on the SERVED artifact, never a fixture.**
**trigger:** my own artifact watch (ETag flip `47e88d8b…` -> `19d40ee6…`, predicate negative+positive
controlled before arming). **Verified artifact:** `s3://opal-data-inf/platinum/firm/advisor_nna_canonical.json`
@ ETag `19d40ee672639959f7900ecca3bb18e4`, 2,510,363 B, generated 2026-07-16T14:58:46Z, `data_as_of`
2026-07-15 (correct T-1). Download md5 == served ETag -- I graded the exact served bytes.

## The bar, cell by cell (§6 as pre-registered; every check computed from served bytes, never a self-report)

| # | cell | reading | verdict |
|---|---|---|---|
| 1 | served artifact only | graded the platinum spine bytes; no preview, no fixture | **PASS** |
| 2 | phantom GONE, not zeroed | advisor key set = {house, joe, noel, patrick, peter} -- `inflection_unmapped_rep` **ABSENT AS A KEY** (0 mentions in 2.5MB); mechanism-discriminated per §6.2: rescue deployed + phantom gone -> no C_01/rescue defect signal | **PASS** |
| 3 | conservation | `sum(advisors) == firm` **to the cent on ALL 9 windows** (1Y/3Y/MAX/QTD/YTD/q1/q2/q3/q_current), computed by me from the served bytes; negative control (inject +$1,000) CATCHES | **PASS** |
| 4 | noel surfaces appear | spine: `noel_soderblom` MAX nna **8,411,521.22**, 51 accts (MAX window); `platinum/advisors/noel_soderblom/` EXISTS (book/composition/summary/timeseries/top_holdings); fresh `book.json` `headline.historical_quarters[14].nna_canonical` == **8,411,521.22 -- ties the spine TO THE CENT across surfaces**; `summary.json` attributes **64 accounts** (== the fold_map's noel count) | **PASS** |
| 5 | pin byte-identity | `gold/dimensions/aor_resolution.parquet` (874 rows, one stamp identity): `fold_mode=ACTIVE`, `as_of=2026-07-16`, `source_digest=100f234e33125b49db8344b80b858c8d` == **the LIVE ETag of `silver/api_dims/accounts_v2/snapshot_date=2026-07-16`** (the partition the dispatch pulled at 13:50:00Z -- the post-pull re-pin working), `code_digest=b01b5a24cc12884e` | **PASS** |
| 6 | held-consumer exclusion (194d3d674 scope) | ALL named held surfaces UNCHANGED at 07-10 vintage: `client_directory.json` (D_02c), `partner_analytics{,_annual,_monthly,_quarterly}.json` (INF_09), `dashboard.json` / `header_metrics.json` / `timeseries_overview.json` + the `nna_clients.json` class (D_04; noel's nna_clients ABSENT -- the held gap, expected until the serve-lift bundle) | **PASS** |

## VERDICT

> # V4 = **PASS**. The first post-cutover nightly SERVES post-fold attribution:
> # the phantom is dead at source, noel is live and cent-consistent across surfaces,
> # conservation ties to the cent on every window, the pin proves the run's identity,
> # and the held-consumer exclusion held. **LD-0277's gate chain is COMPLETE.**

## Discriminated nuances (named, none a FAIL)

1. **Per-advisor `summary.json`/`book.json`/`composition.json`/`timeseries.json`/`top_holdings.json` moved
   tonight (14:59-15:03Z) -- and that is CORRECT, not an exclusion breach.** Writer attribution: `book.json` =
   migrated `INF_D_02` (MATCH, in-chain); `composition.json` = `INF_D_03` (MATCH); `top_holdings.json` =
   `INF_D_02b` (MATCH, bundle member); `summary.json` carries `data_as_of=2026-07-16` and the shape of the
   aggregator-Lambda mirror (`INF_D_02:2051` comment records the Lambda populating summary artifacts) -- not
   the held D_04's upload loop, whose OTHER outputs (`nna_clients.json`, firm dashboard trio) are verifiably
   untouched at 07-10. **The property the exclusion protects -- no pre-fold attribution on any fresh
   surface -- HOLDS: the freshest surfaces tie the folded spine to the cent** (cell 4). Asserted on the
   property, not the writer name (det-#4 §5 discipline).
2. **noel MAX = 8,411,521.22 vs the overnight stamp figure 8,401,521.22: +$10,000.00.** Vintage attribution
   (stamp = data_as_of 07-14; tonight = 07-15 -- one fresh trading day's flows). Conservation ties regardless.
   **Flagged to CTO for the ledger cross-check** (his supervised-nightly read runs on the same artifacts);
   I do not adjudicate a number I can attribute but not independently derive tonight.
3. **noel `nna_clients.json` ABSENT** (D_04 output class, held): a portal consumer wanting noel's per-client
   NNA list from that artifact finds nothing until the serve-lift bundle lands. Known, sequenced (COO path
   (b)), NOT a V4 fail -- an absent artifact is a visible gap, not a wrong number.
4. Firm MAX moved 133,107,667.64 (07-10 vintage) -> **133,202,927.12** (+95,259.48): three fresh trading
   days of net flows between vintages. Expected; conservation binds it.

## What this determination is NOT

Not a portal-render verify (FE surfaces ride the DE/DT lanes), not a close of the serve-lift-at-migrated-
vintages bundle (later deliberate motion, I re-verify those three then), and not a standing exemption:
**nightly #2's read belongs to CTO's supervised lane; my lane returns to event-gated.**

## Instruments (denominators printed throughout)

Artifact watch (ETag flip, predicate controlled both directions BEFORE arming -- v1 false-fired on a quoting
bug and was caught by reading the printed values, not the label) · served-bytes conservation sweep (9
windows x 5 advisors + negative control) · pin tie via independent live `head-object` on the exact source
partition · held-surface census via targeted `head-object` (a prefix listing truncated inside `_meta/` --
the retrieval was fixed before any conclusion was drawn from it) · fresh-surface cross-tie (spine value
found byte-equal in the per-advisor book).

---
-- `3.0.0_SA_CVO~B`
