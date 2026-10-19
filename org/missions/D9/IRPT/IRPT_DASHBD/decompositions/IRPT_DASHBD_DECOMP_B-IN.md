# IRPT_DASHBD -- decomposition, workstream B-IN (Inflection), issuer 2.0.0_SA_COO~I2

This file is the B-IN workstream's own decomposition. The shared file `IRPT_DASHBD_DECOMP.md` stays `2.0.0_SA_COO~D2`'s (workstream B, its
sections 1 to 115), so two issuers never append to one file. Cell ids here are `DB-i-<n>`; worker slots `~301` and up are this seat's
(D2's run `~184` and up; the two ranges do not meet). Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md`
(@a6d9baacaf) and msg 7899. FWDs are unchanged; no PRD change.

## 1. ROUND 114, WORKSTREAM B-IN (2026-10-15 ~01:4xZ)

**Where B-IN stands (measured from the tree, not from a status word).** The Inflection adapter (account_dim, household key) is done in rounds
108-109. The sample (DB-b-222) and the render (DB-b-223) passed the CVO's regrade (round 111 J1 PASS). The household return comes from Orion's
client-grain factor (contract 0.5.0). What is NOT done: Inflection's ACCOUNT-grain return. Round 109's derivation (`DB-b-216`, record
`deliverables/0.9.0_WK_IRPT_DASHBD~174/TWR_TIEOUT_R109.json`) derived 926 accounts and tied the accounts, aggregated per client, to Orion's client
return: QTD compares 287 of 320 households, of which 16 sit under 5 bp, 87 at 5 to 25 bp, 175 at 25 to 100 bp and 9 at 100 bp or more; YTD, the last
12 months and since inception compare NONE. The CTO's round-109 analysis ruled "this seat rules the tolerance on that read" and the account pages
stay "Account-level returns are not available for this firm yet." until it does. Two open rows block the ruling: `IRPT_DASHBD-D2-W174-S2`
(Orion has no `fact_positions` partition for two NYSE trading days, so every longer window is not comparable) and `IRPT_DASHBD-D2-W174-S5` (rows with
`isActive` false carry non-zero value and the value basis includes them until the CTO rules).

**Round 114 is the two reads that make the CTO's tolerance ruling possible. Both are LOCAL, both are reads, and nothing is written to AWS.**

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-1` | The QTD tie-out under three value bases: all rows (round 109's basis, the control), active rows only, cash lines excluded. Per basis the gap distribution; the count of households that move down at least one bin against the control | FWD-2 | LOCAL (a read; a private table; counts only in the repo) | none | I-A |
| `DB-i-2` | The two missing `fact_positions` days: whether any Orion layer holds them (every silver table, and bronze under the granted prefix), whether each is a trading day, how many accounts a bridge across the gap would touch and how many of those had an external flow in the gap, and the producer and schedule that writes the Orion silver | FWD-2 | LOCAL (a read) | none | I-B |

**Decisions inside this decomposition (the issuer's, stated).** (a) Cell `DB-i-1` reuses round 109's cached per-account-day values
(`positions_daily_cache.parquet`, a private file with the value under three bases already summed), so it reads `fact_transactions` and `fact_performance`
once each and no positions partition; the control criterion makes the `all` basis reproduce round 109 household by household, so a wrong reuse fails.
(b) Only QTD is re-run: it is the only window with any comparable household, and YTD, 12 months and since inception wait on `DB-i-2`'s answer.
(c) `DB-i-2` measures the bridge's exposure and does NOT bridge: whether a no-flow link across a missing day is an admissible method is the CTO's
ruling on the read. (d) The enrichment that follows the ruling (the tolerance applied, the account pages switched to derived figures, the gold
partition and its schedule) is NOT cut now: each waits on the CTO's tolerance ruling, and the gold partition is a WORLD act under a never-widen pair.

**fanout:** 2 of 2 chains, cap 8, reason: the two cells are dependency-independent with disjoint write sets (each its own worker folder and private folder). Workers `0.9.0_WK_IRPT_DASHBD~301` (`DB-i-1`) and `~302` (`DB-i-2`).

## 2. ROUND 115, WORKSTREAM B-IN (2026-10-15 ~02:3xZ, issuer 2.0.0_SA_COO~I2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_115_20261015.md`, msg 7956, answering the round-114 drain-end packet @fe51225396: 2 of 2 PASS, 0 judgment criteria)

The CTO's one cell is cut as ONE order. No tolerance is set and the account pages stay `NO_SOURCE_YET`; no no-flow bridge across a missing day (windows over 2026-07-01 and 2026-09-28 carry `SOURCE_BREAK` words until `~P2`'s re-pull); the two missing Orion days are `~P2`'s (msg 7913).

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-3` | The gap decomposition read: about 12 households across the QTD gap bins (every household at 100 bp or more plus the lowest-sha household of each other bin), five named differences between the Opal derivation and Orion's client factor each tested ALONE against the round-109 baseline (gross against net of fees, trade against settlement date, flow timing inside a day in two forms, income accrual, the cash sweep in two forms), and the explained share per household per variant | FWD-2 | LOCAL (a read; a private table; counts, bp and shares only in the repo) | none | I-C |

**Decisions inside this decomposition (the issuer's, stated).** (a) The sample is a RULE, not a choice, so the checker recomputes it from round 114's private variant file (all 9 households at 100 bp or more, plus one per other bin: 12). (b) The differences are tested through nine variants (`base`, `identity`, `gross_fees`, `settle_timing`, `flow_start_of_day`, `flow_midday`, `income_accrual`, `ex_cash_value`, `ex_cash_no_flows`): the CTO's "flow treatment inside a day" and "cash sweep" each take two forms so a single reading is not mistaken for the difference. `identity` is the difference control: a variant that changes nothing must change nothing. (c) A difference the Orion frame cannot support (no settlement-date column, no accrual date) is reported NOT_TESTABLE with the reason in words, never invented. (d) The share is the SIGNED form `(base - variant) / base`, unclipped, so an overshoot or a widening is visible.

**fanout:** 1 of 1 chains, cap 8, reason: one independent read cell with a disjoint write set (its own worker folder and private folder). Worker `0.9.0_WK_IRPT_DASHBD~303` (`DB-i-3`).

## 3. ROUND 116, WORKSTREAM B-IN (2026-10-15 ~03:2xZ, issuer 2.0.0_SA_COO~I2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_116_20261015.md`, msg 7978, answering the round-115 drain-end packet @d64cf8f469: 1 of 1 PASS, 0 judgment criteria)

The CTO's one cell is cut as ONE order. The ruling: stop reconstructing Inflection account returns; read whether Orion itself exposes an account-level performance series. If it does, `~P2` adds that feed to the Orion pull under a never-widen pair and the accounts switch to Orion's figure (`source: orion`); if not, the account pages stay `NO_SOURCE_YET` and the reconstruction is not shipped. The round-114 and round-115 decomposition stays recorded as the reason.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-4` | The Orion account-level performance read: the endpoint, the grain, the fields (return, period, gross or net) and whether the pull's credential reaches it, from the estate's pull code, the investor-reporting performance adapter, its fixtures and the repo docs; the endpoint inventory of those directories as the denominator | FWD-2 | LOCAL (a read of repo code and docs; no vendor call, no AWS call, no secret read) | none | I-D |

**Decisions inside this decomposition (the issuer's, stated).** (a) The CTO's phrase "as the existing pull reaches it" is read as BOTH code families that reach Orion: the `inf-pipeline` pull that feeds the silver, and the investor-reporting performance adapter, whose header already names `POST /api/v1/Reporting/Scope` with "native household and account scopes"; the answer to "does the pull call it" and "does the estate already hold it" are different facts and the order asks for both. (b) The endpoint inventory is the DENOMINATOR (every `/api/vN/` literal in the `*.py` files directly inside each `inf-pipeline` directory and the performance directory), so a "no such endpoint" cannot rest on a partial read. (c) The credential question is answered from code only, since the CTO ruled no new vendor call; the record names the secret and never reads it, and says what the code cannot prove. (d) Each section carries a claim word and verified evidence lines (the checker opens each cited line and requires the quote on it).

**fanout:** 1 of 1 chains, cap 8, reason: one independent read cell with a disjoint write set (its own worker folder). Worker `0.9.0_WK_IRPT_DASHBD~304` (`DB-i-4`).

## 4. ROUND 117, WORKSTREAM B-IN (2026-10-15 ~03:3xZ, issuer 2.0.0_SA_COO~I2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_117_20261015.md`, msg 7985, answering the round-116 drain-end packet @e14658f347: 1 of 1 PASS, answer YES)

The CTO's one cell is cut as ONE order. The ruling: Scope (not ExcelReports) is the source for Inflection account returns; ONE probe settles the three unknowns of round 116 (does the Account grouping return one group per account with a daily series for a multi-account household; is the fee flag honoured; is the credential accepted and from which store). If (a) and (c) pass, `~P2` adds the feed in the Orion pair and the accounts show Orion's figure with the fee basis stated; if (a) fails, one call per account if `~P2` costs it acceptable.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-5` | The Scope probe: the household (lowest-sha with 2 or more accounts), at most 4 paced POSTs to `/api/v1/Reporting/Scope` (fee flag false, then true) over 2026-10-01 to 2026-10-13, the raw responses private, three verdicts recomputed by the checker from the saved bodies | FWD-2 | WORLD (a vendor read: no write, no deploy; the output is LOCAL) | none | I-E |

**Decisions inside this decomposition (the issuer's, stated).** (a) The class is WORLD, the CTO's own word ("a WORLD read, LOCAL output, no write"), though no infrastructure path or deploy verb forces it: a call to the vendor with the estate's credential is not a LOCAL record. (b) The household is a RULE (lowest sha256 among households with 2 or more accounts in the private dimension), so the checker recomputes it and the worker cannot choose a convenient one. (c) The three verdicts are defined by exact rules over the saved response bodies, so the checker recomputes them without a vendor call; the fee verdict `NET_WHEN_FALSE` needs the gap to tie to the summed `feeAmount` over the start value, as the CTO's ruling says. (d) The pace and the cap are in the order (at most 4 calls, at least 5 s apart, one retry per flag on a timeout or 5xx, no retry on a 4xx), and a refusal stops the cell; no other principal is tried. (e) The token is used in memory and never written anywhere.

**fanout:** 1 of 1 chains, cap 8, reason: one independent probe cell with a disjoint write set (its own worker folder and private folder). Worker `0.9.0_WK_IRPT_DASHBD~305` (`DB-i-5`).

## 5. ROUND 118, WORKSTREAM B-IN (2026-10-15 ~04:1xZ, issuer 2.0.0_SA_COO~I2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_118_20261015.md`, msg 8034 @103b76689f, answering the round-117 drain-end packet @577b13ddad: 1 of 1 PASS, 0 judgment criteria)

The CTO ruled BOTH options in parallel: `~P2` cuts the Scope account feed now by addendum to its pair (b), with a coverage rule inside the feed (each account-day carries Orion's return or an ABSENT row with `NO_GROUP` or `GROUP_NO_SERIES`, never a zero or an Opal fill) and `fee_basis` UNPROVEN until a fee window ties; this lane runs ONE more probe. The feed is `~P2`'s and is not a cell here.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-6` | The second Scope probe: the same household as round 117, the quarter that ended 2026-09-30, the fee flag false then true, the INNER scope body; at most 4 calls (a second pair over 2026-01-01 to 2026-09-30 only if the Q3 pair held no fee); (i) coverage of the short accounts, (ii) the fee tie, (iii) the cause class of each short account from the position cache and a category column of the newest `fact_positions` partition | FWD-2 | WORLD (a vendor read; no write, no deploy; the output is LOCAL) | none | I-F |

**Decisions inside this decomposition (the issuer's, stated).** (a) The CTO's "cap 4 calls ... flag false then true" needs two calls; the other two are spent only on a fallback the order states (a longer span when the Q3 pair holds no fee, since a fee tie needs a fee), never as a retry. (b) The inner-scope body is stated in the order and the checker's posture: round 117 lost two of its four calls to a wrapper dict. (c) The verdict words follow round 117's amended rule (a 400 is `REQUEST_REJECTED`, never `REFUSED`) and add `NO_FEE_IN_WINDOW`, so a window with no fee cannot read as a failed tie. (d) The short accounts are named by digest, and their cause class is read from the position cache (a count) and a coded category column of Orion's own positions, never a name or an account number. (e) The checker recounts coverage, the fee verdict, the short list and the position days from the saved bodies and the cache; it never calls the vendor.

**fanout:** 1 of 1 chains, cap 8, reason: one independent probe cell with a disjoint write set (its own worker folder and private folder). Worker `0.9.0_WK_IRPT_DASHBD~306` (`DB-i-6`).

## 6. ROUND 119, WORKSTREAM B-IN (2026-10-15 ~04:5xZ, issuer 2.0.0_SA_COO~I2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_119_20261015.md`, msg 8048 @712ede60c4, answering the round-118 drain-end packet @a75f9982df: 1 of 1 PASS, 0 judgment criteria)

The CTO's rulings: `fee_basis` is NET (the feed's, `~P2`'s, with the sample note); the missing account is a coverage fact the feed carries as ABSENT `NO_GROUP`; before anyone contacts Orion, ONE cell reads Orion's own account record for the missing account against a present one (WORLD read, cap 3 GETs, paced, no retry). The adapter cell waits on `~P2`'s feed landing its first bronze and silver.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-7` | The Orion account-record read: the missing account, the series-less account and one present account of the round-117 household, found in the roster the pull already reads (`GET /api/v1/Portfolio/Accounts/NewPortfolio`, then, only while the missing account is still not found, the same with `isActive=false`, then `GET /api/v1/Portfolio/Accounts`), every performance-relevant field path compared, the differing field names reported as verdict words | FWD-2 | WORLD (a vendor read; no write, no deploy; the output is LOCAL) | none | I-G |

**Decisions inside this decomposition (the issuer's, stated).** (a) The estate's own account pull (`pull_inflection_new_portfolio.py`) asks for `isActive=true`, so the roster it lands holds ACTIVE accounts only: an account Scope omits may simply be inactive in Orion's record. The GET order is built on that: the pull's own request first, the same request for inactive accounts only if the missing account is not found, the base roster last, and NO GET after the account is found. That is the "cap 3" used as a decision tree, not as three calls spent by default. (b) "Every performance-relevant flag" is made mechanical: a field path is relevant by a stated regular expression and exclusion-type by a second, both applied by the checker to the saved bodies; only field NAMES and booleans enter the repo, never a date, a string or a number. (c) The roster is whole-firm client data: private folder only; if it carries any other firm's accounts the worker records the row count and nothing else. (d) No vendor contact is made or drafted here; that is the CTO's, for Andrew, after this read.

**fanout:** 1 of 1 chains, cap 8, reason: one independent read cell with a disjoint write set (its own worker folder and private folder). Worker `0.9.0_WK_IRPT_DASHBD~307` (`DB-i-7`).

## 7. ROUND 120, WORKSTREAM B-IN (2026-10-15 ~05:2xZ, issuer 2.0.0_SA_COO~I2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_120_20261015.md`, msg 8081 @54c0c541c9, answering the round-119 drain-end packet @1721081b18: 1 of 1 PASS)

The CTO adopted the reason classes `NO_START_DATE_AT_SOURCE` and `NO_MODEL_AT_SOURCE` for `~P2`'s feed with `claim: inferred`, and ruled ONE second-household probe (cap 2 Scope calls, inner-scope body) to measure the link: if the null-start account is missing from Scope, the no-model account is short and every other account is present, the claim becomes `measured (2 households)`; the page words stay neutral until then. Fixing the 40 accounts at the source is a request to Inflection's operations, an act for Andrew filed after this probe.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-8` | The second-household Scope probe: a household other than round 117's with a null-start account, a no-model account and no account outside the active roster, chosen by a rule fixed before any call; two Scope calls (Q3, then YTD), calcGrossOfFees false, inner-scope body; the state of each account recomputed by the checker from the saved bodies, against a prediction written before the call | FWD-2 | WORLD (a vendor read; no write, no deploy; the output is LOCAL) | none | I-H |

**Decisions inside this decomposition (the issuer's, stated).** (a) The CTO's "both missing from Scope" is made exact: the null-start account must have NO group in every window run; the no-model account must be not `GROUP_WITH_SERIES` in Q3 (round 118 saw it short in Q3 and complete over YTD); every other account must carry a series in both windows. (b) The two calls are Q3 then YTD with the fee flag false, since the fee basis is settled and the YTD window is where the round-118 series-less account recovered. (c) The household rule excludes households with an account outside Orion's active roster, because such an account is absent for a different reason and would confound the claim "every other account is present"; a candidate exists (15 households qualify before that exclusion, one of six accounts with 4 FULL, 1 NO_START, 1 NO_MODEL after it). (d) The prediction is in the order and the checker before any call, and the worker may not change the rule or the household. (e) The source fix is not in this decomposition.

**fanout:** 1 of 1 chains, cap 8, reason: one independent probe cell with a disjoint write set (its own worker folder and private folder). Worker `0.9.0_WK_IRPT_DASHBD~308` (`DB-i-8`).

## 8. ROUND 122, WORKSTREAM B-IN (2026-10-15 ~16:3xZ, issuer 2.0.0_SA_COO~I2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_118_20261015.md` ADDENDUM 2 @b3e3124d72, msg 8455, answering my msg 8453)

This is the B-IN round after round 120 (round 121 was the CTO's analysis with no cell). It is cut on an ADDENDUM, not on a new analysis: the CTO ruled that the Scope account feed carries a one-time history backfill (a forward-only feed leaves the QTD, YTD, last-12-month and since-inception windows without history for months), that `~I2`'s 2-call probe comes first, and that the backfill's request and time bound comes from that measurement. `~P2` has added an optional `--from-date` to IB-pr-586 (AMENDMENT 1 @7890b746be) and writes pair (b) ADDENDUM 2 after this probe lands.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-9` | The Scope history probe: two households (round 117's and round 120's), one Scope call each from the household's earliest Orion account start date to 2026-10-13, Daily, calcGrossOfFees false, inner body; the series length of every account, whether the chained daily factors reproduce Orion's period return, whether each series is as long as the trading days since the account's start, the call time and response size, and the universe bound (requests, serial seconds, bytes) | FWD-2 | WORLD (a vendor read; no write, no deploy; the output is LOCAL) | none | I-I |

**Decisions inside this decomposition (the issuer's, stated).** (a) The CTO named one household; two are called so that the bound rests on two calls of different size, not one, within the 2-call cap he set. (b) The chain check and the completeness check are in the cell because a backfill that lands a short or gapped daily series would let the windows print wrong figures: the series is only usable if its chained daily factors reproduce Orion's own period return and it covers the trading days since the account started. (c) The timeout is 180 s, not the transport's 60 s, because a multi-year daily series is larger than the one-day call the live path makes; a call that hits it is a result, not a retry. (d) The bound is a SERIAL upper bound (requests times the slowest call); it assumes no parallelism, no retry and no rate-limit headroom beyond what the feed's own limiter allows, which this probe does not measure. (e) No date enters the repo: the window start is a hash.

**fanout:** 1 of 1 chains, cap 8, reason: one independent probe cell with a disjoint write set (its own worker folder and private folder). Worker `0.9.0_WK_IRPT_DASHBD~309` (`DB-i-9`).

## 9. ROUND 123, WORKSTREAM B-IN (2026-10-15, issuer 2.0.0_SA_COO~I2, on `CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_118_20261015.md` ADDENDUM 4 and `2.0.0_SA_COO~D2` msg 8574, contract 0.4.0 @ef923dab52)

Contract 0.4.0 is merged, so the adapter that turns the Scope feed's rows into `account_return_daily` rows can be built now, offline, ahead of the feed's first real data (the CTO's earlier word that the adapter cell waits on the feed's first bronze and silver is kept for the RUN of the adapter on real rows, which is a later cell).

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-10` | The Scope feed adapter: a pure function (standard library only, no I/O) from the feed's silver rows, an Orion-to-dimension account map and the sorted trading-day list to contract-0.4.0 rows, with its offline tests and a mutant | FWD-2 | LOCAL (code and tests; nothing wired, scheduled, served or deployed) | none | I-J |

**Decisions inside this decomposition (the issuer's, stated; each is open to the CTO at the round analysis).** (a) The dimension's `account_id` is Orion's id as a string (round 108), so "mapped through `account_dim`" is membership in an injected map `{orion id: dimension id}`; the real map is read from the dimension in the later run cell. (b) The contract has no column for an ABSENT row's reason, and `market_value_eod` and `account_id` are non-nullable, so ABSENT days are NOT written as contract rows: they are returned as `absent` records (account, trading day, reason class) beside the rows, counted in the manifest. If the CTO or `~D2` want ABSENT rows inside the table, the contract needs a reason column and a nullable value; that is their call. (c) `market_value_eod` of a trading day is the next calendar day's `start_market_value` (else the last day's `end_market_value`); the feed carries no per-day end value, so this is INFERRED and the manifest says so. (d) Three reason classes are added by the module for cases the feed's classes do not cover: `NO_FEED_ROW`, `INCOMPLETE_WINDOW` (a non-trading day inside the window has no factor, never filled with 1), `NO_EOD_VALUE`. (e) `day_quality` `MEASURED` and `guard_state` `GUARD_NOT_REACHED` are the nearest members of the 0.4.0 enums for a vendor-reported return the holdings guard never saw; the CVO grades the words at L9. (f) `history_scope` is `PARTIAL_HISTORY` on every row until the backfill is read. (g) `method_version` is an argument: no `dim_return_method` row for an Orion return exists yet.

**fanout:** 1 of 1 chains, cap 8, reason: one independent build cell with a disjoint write set (a new module and its test file). Worker `0.9.0_WK_IRPT_DASHBD~310` (`DB-i-10`).

## 10. ROUND 124, WORKSTREAM B-IN (2026-10-15, issuer 2.0.0_SA_COO~I2, on the CTO's round-118 ADDENDUM 5 (msg 8584) and ADDENDUM 6 (msg 8605))

The CTO ruled (open call dell2-20261015T193100Z-cf2a) that the run wrapper is cut now, offline, and that the first real-row run stays a later cell on the feed's silver. ADDENDUM 6 carries worker row W310-S2 (a repeated key) into this round and says the wrapper writes contract 0.4.1 if it has landed by the cut, otherwise ABSENT beside the rows, and says which. Contract 0.4.1 has not landed (the file reads 0.4.0 at the cut), so ABSENT sits beside the table and the run record says `BESIDE_TABLE`.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-11` | The Scope feed run wrapper: from feed silver partitions (pandas frames) and the dimension frame, the complete-day rule, a repeated-key refusal, the account map from the dimension's own key form, `adapt()`, then contract-0.4.0 date partitions, an ABSENT-records file and a run record; a 299-day chain fixture; plus the CTO's three round-123 enrichments (a `market_value_eod_claim` row field, the 0.4.1 shape of ABSENT records with the UNMAPPED_ACCOUNT inversion fixed in the adapter, the `reason_class_status` proposed marks); fixtures only, no AWS | FWD-2 | LOCAL (code and tests; local files under a handed directory; nothing wired, scheduled, served or deployed) | `DB-i-10` (merged, @90862adf60) | I-K |

**Decisions inside this decomposition (the issuer's, stated).** (a) The complete-day rule is the wrapper's guard of the feed's own rule (a day's key is written only when the day is complete, round PN1 item 4): the wrapper cannot see the feed's household universe, so it grades the rows it is given: an unknown status, a RETURNED row without a factor or an ABSENT row without a reason class makes the whole calendar day incomplete, and every row of that day is dropped and counted. A dropped day then reads ABSENT through the adapter's own rules (NO_FEED_ROW / INCOMPLETE_WINDOW), never filled. (b) A repeated key is refused (ValueError carrying the count, nothing written) rather than read as "last wins". (c) The 238-to-365-day fixture (round-122 analysis item 2) is 299 calendar days, Monday to Friday, one account: the fixture's "source" is the product of its own daily factors, because the adapter stores and chains the daily factor and never reads a window summary (ADDENDUM 3); a real Orion summary comparison belongs to the real-row run. (d) The wrapper reads the dimension's key form (Orion's id as a string) as ADDENDUM 6 item 6 rules. (e) `proposed_reason_classes` in the run record names the three module-added classes while 0.4.1 has not admitted them (ADDENDUM 6 item 3). (f) The round-123 analysis (msg 8610, items 1 to 3) is in this cell and not a second one: its items edit the merged adapter, whose rows the wrapper writes, so one worker owns both files and the wrapper's golden grades the adapter's new shapes end to end. The edit supersedes the round-123 checker's shapes for an unmapped record and a row; that checker graded the closed order. (g) `market_value_eod_claim` is written beside the contract's 22 fields, outside its hash, until 0.4.1 admits it; the contract's own validator ignores an undeclared column.

**fanout:** 1 of 1 chains, cap 8, reason: one independent build cell with a disjoint write set (a new module and its test file). Worker `0.9.0_WK_IRPT_DASHBD~311` (`DB-i-11`).

## 11. ROUND 125, WORKSTREAM B-IN (2026-10-15, issuer 2.0.0_SA_COO~I2, on the CTO's round-124 analysis @e5c8b143fe, msg 8654, answering my packet @1190b13f77)

Round 124 does not close on its own: the CVO graded the landed tree NOT MAY-CLOSE (contract 0.4.1 landed after the cut; AC2 and AC3 fail and 2 of 38 tests are red on trunk). The CTO accepted my proposed batch and added three items. Round 125 is cut on contract 0.4.1 (the file reads 0.4.1 at the cut; 0.4.2 has been asked of `~D2` and has not landed). It closes round 124 when it lands green on trunk, graded on the landed tree.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-12` | The Scope feed adapter and run wrapper on contract 0.4.1: Orion PRESENT rows `VENDOR_REPORTED` with `row_status` PRESENT (disarms W221-S3); ABSENT rows written INTO the table in the 0.4.1 shape with the contract's reason precedence (the `absent/` file and `BESIDE_TABLE` retire); the wrapper reads its field list and version from the contract file; refusals for a bad dimension key, a mismatched partition and a non-empty output directory; the adapter gets the full domain and account set so that a dropped first or last calendar day leaves 0 trading days unaccounted (W311-S1, S3); the 'proposed' marks removed; the end-of-day claim in the table when the contract declares it, else in the run record; fixtures only, no AWS | FWD-2 | LOCAL (code and tests; local files under a handed directory; nothing wired, scheduled, served or deployed) | `DB-i-11` (merged, @6c7b7ccb56) | I-L |

**Decisions inside this decomposition (the issuer's, stated).** (a) One cell, not two: the adapter and the wrapper change together (the wrapper's golden grades the adapter's rows end to end) and one worker owns all four files. (b) The checker is driven by the contract FILE at HEAD (version, fields, hash, validator), so a 0.4.2 that declares `market_value_eod_claim` as a column changes what the checker expects, never its code, and the wrapper switches the claim from the run record to the table by reading the contract; the order names both placements. (c) An ABSENT row's unlisted columns follow `~D2`'s own `_absent` fixture in `test_account_return_contract_041.py` (`return_basis` and `day_quality` NOT_MEASURABLE, `guard_state` GUARD_NOT_REACHED); `carried_days` 0 and `flow_claim` absent are mine (the contract does not say; the validator accepts both). (d) W311-S1 is a criterion, as the CTO ruled: the wrapper passes the adapter the full domain and every account, and counts `trading_days_unaccounted` itself from the output. (e) W311-S2 is settled as: the repeated-key count is the number of distinct keys repeated. S3 is closed by the account set; S4, S5 and S6 are refusals with a count and no write. (f) The closing grade is the landed tree: at the drain I re-run all three criteria on the merged tree, not only in the worker's.

**fanout:** 1 of 1 chains, cap 8, reason: one cell with a disjoint write set of four existing files. Worker `0.9.0_WK_IRPT_DASHBD~312` (`DB-i-12`).

## 12. ROUND 126, WORKSTREAM B-IN (2026-10-15, issuer 2.0.0_SA_COO~I2, on the CTO's round-122 analysis item 3 and ADDENDUM 1 (msg 8678, open call dell2-20261015T211904Z-4255 ruled yes))

The round-122 analysis left the series-ended cause read to this seat "at the next B-IN round"; rounds 123 to 125 took other analyses, so it was uncut. The CTO ruled it cut now, after round 125's drain (the call was queued during it), and ruled (msg 8679) that the TWR flip of the module rides contract 0.4.2 in the same merge window as `~D2`'s file, never ahead of it. That flip is a separate cell, cut when 0.4.2 lands, with the next round number; it is not in this issuance.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-13` | The series-ended cause read: the two saved round-122 Scope bodies against Opal's `fact_positions` silver (GET-only reader, no vendor call): for each Account series that ends before the window end, its days-before-window-end, how many positions partitions follow it, on how many the account is held, whether it is held on the newest, and the verdict STALE_AT_SOURCE / CLOSED_OR_TRANSFERRED / NOT_DETERMINED; counts and words only | FWD-2 | LOCAL (a GET-only read of Opal's own silver and private files; no vendor call, no write, nothing deployed) | none | I-M |

**Decisions inside this decomposition (the issuer's, stated).** (a) The CTO asked to print "its last date"; the repo carries days-before-window-end (an integer) and the account as a sha256, because a date next to a client's account would be a client fact in the repo. (b) STALE_AT_SOURCE means Opal's positions still hold the account on the newest partition after Orion's series ended; it does NOT prove a vendor fault (a position can outlive a vendor's performance record for another reason), and the basis words say so. (c) The read is bounded: LIST plus GETs under 200; a cap hit is a recorded result, not a widening. (d) The checker recomputes everything it can from the saved bodies and the worker's private extract; it cannot re-read S3, so the issuer spot-reads the newest partition at the drain. (e) The risk class is LOCAL as the CTO wrote (a GET-only read of Opal's own estate, as rounds 108 to 111 were).

**fanout:** 1 of 1 chains, cap 8, reason: one independent read cell with a disjoint write set (its own worker folder and private folder); worker `0.9.0_WK_IRPT_DASHBD~313` (`DB-i-13`) runs alone; round 125's worker has already drained.

## 13. ROUND 127, WORKSTREAM B-IN (2026-10-15, issuer 2.0.0_SA_COO~I2, on the CTO's round-125 analysis (msg 8695, 8698) and his 0.4.2-landed message; contract 0.4.2 merged by `~D2` at 6ac152c83a)

The CTO numbered the module's flip "round 126"; round 126 was already DB-i-13 (the cause read), and he confirmed (msg 8698) that the flip is round 127, cut when `~D2`'s 0.4.2 lands. It has landed: `return_basis` is TWR or NOT_MEASURABLE (VENDOR_REPORTED and `source_requires` are gone; provenance is `source`), and the optional column `market_value_eod_claim` is required on a PRESENT Orion row and null on an ABSENT row. The merged module writes VENDOR_REPORTED and keeps the claim in the run record, so on trunk the r125 checker's AC3 and 4 module tests read red; the CTO asked that the count be named, not suppressed (4 failed, 58 passed across the adapter and wrapper test files, measured at the cut).

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-14` | The Scope feed adapter and run wrapper on contract 0.4.2: PRESENT rows `TWR` (disarms W221-S3); `market_value_eod_claim` a declared column of the table (the run record's `claim_placement` retires; the wrapper refuses a contract that does not declare the column); `contract_version` read from the file; the W311-S3 test line; fixtures only, no AWS | FWD-2 | LOCAL (code and tests; local files under a handed directory; nothing wired, scheduled, served or deployed) | `DB-i-12` (merged, @7a8a2f681f) | I-N |

**Decisions inside this decomposition (the issuer's, stated).** (a) The wrapper REFUSES a contract that does not declare the claim column (count 1, nothing written) instead of keeping the run-record placement: round 125's two-placement code existed only to bridge the gap before 0.4.2, and a writer should not run behind its contract any more than ahead of it. (b) The r127 checker is driven by the contract file at HEAD and uses the 0.4.2 test module's validator; the r125 checker graded 0.4.1 and is superseded. (c) W311-S3 was already closed in the merged wrapper (the CTO accepted this, msg 8698); it is carried as a test line only. (d) DB-i-13 (round 126) is a read cell on a separate chain; the two share no file.

**fanout:** 1 of 1 chains, cap 8, reason: one cell with a disjoint write set of four existing files. Worker `0.9.0_WK_IRPT_DASHBD~314` (`DB-i-14`).

## 14. ROUND 128, WORKSTREAM B-IN (2026-10-15, issuer 2.0.0_SA_COO~I2, on the CTO's round-126 analysis, msg 8730)

The CTO closed round 126 MAY-CLOSE with one enrichment: the read record carries `cause_claim: inferred` (the account is absent from a complete positions partition; its own status was not read). No product change follows; the verdict words stay record vocabulary. The record sits in the round-126 worker's deliverables folder, which the commit lane grants only to a worker holding a non-terminal order naming it (my own commit of the one-line edit was refused by lane TREE_DELIVERABLES), so the edit is a direct-act order.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-15` | Add the single key `cause_claim` = `inferred` to `SERIES_ENDED_CAUSE_R126.json` (the diff is one added line) | FWD-2 | LOCAL (one data record; nothing wired, served or deployed) | `DB-i-13` (merged) | I-O |

**Decisions inside this decomposition (the issuer's, stated).** (a) The round-126 check (`checks/r126/p126_cause.py`, the issuer's file) is amended in this issuance to require `cause_claim` = `inferred`; between the issuance and the worker's merge `DBI126-1-AC1` therefore reads FAIL on trunk, named here so it is not read as a regression. (b) The order's own criterion, `DBI128-1-AC1`, runs the same check and expects its PASS line. (c) A direct act (one cell, a one-line edit, LOCAL) runs no L2, L4-R or L8 to L10; its close is my one real run of the criterion on the landed tree.

**fanout:** 1 of 1 chains, cap 8, reason: one independent direct-act cell with a disjoint write set (one record); worker `0.9.0_WK_IRPT_DASHBD~315` (`DB-i-15`).

## 15. ROUND 129, WORKSTREAM B-IN (2026-10-15, issuer 2.0.0_SA_COO~I2, on the CTO's round-127 analysis ADDENDUM 1, msg 8736; open call dell2-20261015T223117Z-5df4 ruled yes)

The CTO ruled that the first-real-row RUN script is built now, on fixtures, so the real run is a same-day act when the feed's first silver lands (IB-pr-596, `~P2`). He wrote "round 128"; round 128 is the cause-claim line (DB-i-15, drained at b421b07328), so this is round 129.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-16` | The first-real-row run script and its tests: the feed's silver via the GET-only reader into the round-127 wrapper and a private local directory; the Orion boundary measure (pairs, pairs equal, max relative difference in basis points); a 238-to-365-day chain check; NO_SILVER_YET and STOPPED_AT_CAP as recorded results; fixtures only, nothing run on real data | FWD-2 | LOCAL (a new script and tests in the order's own folder; no S3 write, no vendor call, nothing deployed) | `DB-i-14` (merged, @c7d980af1b) | I-P |

**Decisions inside this decomposition (the issuer's, stated).** (a) The boundary measure prints the RELATIVE difference in basis points and counts, not dollar differences: a dollar figure per account is a client value and the repo carries counts and statistics only; "equal" is within half a cent. (b) The chain check as the CTO worded it ("the 238-365 day chain check") compares the table's chained rows with the product of the silver's own daily factors, a consistency check of the adapter and wrapper on real rows; a comparison with Orion's REPORTED period return needs a vendor call and a window the backfill provides, and is NOT built here. The order, the check and the report say so. (c) `method_version` is 0 for this private run (no `dim_return_method` row exists for an Orion return); the record says so. (d) The script's `main` is wired to the estate's own dimension builder, reads two silver tables, and is not exercised until the silver exists; the checker exercises `run_real` through a fake reader. (e) The script lives in the worker's folder, not in a production tree: it is a measurement instrument, not a pipeline.

**fanout:** 1 of 1 chains, cap 8, reason: one independent build cell with a disjoint write set (a script and its tests); worker `0.9.0_WK_IRPT_DASHBD~316` (`DB-i-16`).

## 16. ROUND 130, WORKSTREAM B-IN (2026-10-15, issuer 2.0.0_SA_COO~I2, on the issuer's own defect found at the round-129 drain; no CTO analysis)

At the round-129 drain I read the feed script to check what the run script would meet on real silver. The feed (`pull_inflection_scope_account_returns.py`) writes ONE silver partition per calendar DAY (`write_day(s3, day, ...)`, `date=<day>`) and stamps EVERY row of a pull with the PULL date, so a backfill or a multi-day scheduled pull has rows whose `pull_date` is later than their partition. Round 125's wrapper refuses a partition when a row's `pull_date` differs from the partition (worker row W311-S5, which I worded and the CTO accepted from my batch, msg 8654), so on the first real run it would refuse every such partition. A fixture shaped like the real feed reproduces it: 48 rows refused. The error is mine (I specified the rule from a worker row's one-line description without reading the feed's partition semantics).

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-17` | The wrapper's partition-key rule corrected: a partition `date=<d>` is refused (count, nothing written) when a row's `day` is not <d>; a differing `pull_date` is accepted; one test added for the backfill shape | FWD-2 | LOCAL (a one-condition edit and its tests; nothing wired, served or deployed) | `DB-i-14` (merged) | I-Q |

**Decisions inside this decomposition (the issuer's, stated).** (a) The issuer rules everything inside its own decomposition, so this is cut without a CTO ruling and reported in the next packet for him to read at the analysis. (b) A direct act: one cell, a one-condition edit, LOCAL. (c) The round-127 checker's partition arm (`checks/r127/`) encoded the old rule; `checks/r130/` replaces that arm and adds the backfill-shaped acceptance arm, and supersedes r127 for this order's criteria; r127 is not edited. (d) The round-129 run script (`DB-i-16`) is unaffected: its fixtures key partitions by day and its `run_real` passes the partitions to `run()` unchanged. (e) The first real run must not be attempted before this merges.

**fanout:** 1 of 1 chains, cap 8, reason: one independent direct-act cell with a disjoint write set (the wrapper and its test file); worker `0.9.0_WK_IRPT_DASHBD~317` (`DB-i-17`).

## 17. ROUND 131, WORKSTREAM B-IN (2026-10-16, issuer 2.0.0_SA_COO~I2, on the CTO's round-129 analysis, msg 8779)

The CTO ruled that every fixture standing in for the feed is generated by the feed's own writer (its schema and day partitioning), never hand-shaped, because a hand-shaped fixture hid the round-125 partition-key defect; the next fixture round carries that as a criterion. Round 130 (DB-i-17) fixed the defect; this round adds the permanent regression tests.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-18` | One new test file: the round-127 wrapper and the round-129 run script run on silver partitions written by the FEED'S OWN `run()` over the feed's own offline fakes (backfill window, single day, a day the feed skipped, the pull-date regression, a mutant) | FWD-2 | LOCAL (a new test file; no AWS, no network, nothing deployed) | `DB-i-17` (merged, @cfa6dcab48) | I-R |

**Decisions inside this decomposition (the issuer's, stated).** (a) The criteria are an invariant checker, not a hand-written golden: the checker makes its OWN partitions from the same feed harness (so it cannot disagree with the feed about the shape) and asserts invariants (every account x trading day once, PRESENT + ABSENT = accounts x days, reasons inside the contract's eight, each row valid, 0 unaccounted). AC1 and AC2 are therefore CONTROLS that PASS at base (round 130 landed) and FAIL on the pre-fix wrapper (10 rows refused, measured); AC3, the test file, is the build criterion. (b) The new tests may import the feed's own test module for its harness (a read); the feed's files are not edited. (c) A defect a test finds is a row and a strict xfail, not a fix: the worker's grant is one test file. (d) Measured at the cut, before this order: the feed's own `run()` over its fakes writes three day-partitions with `pull_date` the pull day on every row; the corrected wrapper accepts them (15 rows, 1 PRESENT, 14 ABSENT in the ended-series fixture).

**fanout:** 1 of 1 chains, cap 8, reason: one independent build cell with a disjoint write set (one new test file); worker `0.9.0_WK_IRPT_DASHBD~318` (`DB-i-18`).

## 18. ROUND 132, WORKSTREAM B-IN (2026-10-19, issuer 2.0.0_SA_COO~I2, on the CTO's round-131 analysis (msg 8916 and its erratum @b81e9bc3c4; open call 2d0b), cut when the Scope feed's first silver landed)

The CTO asked for ONE read cell: the live silver and wrapper output, rows counted against the feed's own manifest, with the trading-calendar fix as its criterion, Inflection only. It could not be cut while the table held no partition. The corrected feed script (TO-IB-pn-4) is live and the silver table now lists its first partition, so the cell is cut on the landing, not on the clock.

| cell | what | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| `DB-i-19` | One read script: the round-129 run script run on the landed silver into a PRIVATE directory (the first real run of the wrapper), each landed day's bronze envelope read through the GET-only reader (counts only), silver rows per day counted against the feed's own manifest, trading days from `lib/trading_calendar.py`; the record is counts and verdict words only | FWD-2 | LOCAL (GET and LIST only; writes only the worker's private folder and its own record) | `DB-i-18` (merged), the feed's first silver (landed) | I-S |

**Decisions inside this decomposition (the issuer's, stated).** (a) The criterion is a recount, not a golden: the checker rereads the private extract and recomputes the day count, the per-day agreement of the silver row count with the bronze manifest, the trading-day count from the calendar, and that accounts x trading days = PRESENT + ABSENT with 0 unaccounted; the record is graded against that recount, so the worker's own sentence is never the evidence. (b) The cell reads and records; it fixes nothing. A wrapper refusal, a manifest disagreement or a large boundary difference IS the result and goes to a surprise row. (c) The real shape was first seen by the issuer through a LIST and one row-and-column count only; no value was read. (d) Client values, ids and dates stay in the private folder; the repo, the rows and the report carry counts and verdict words.

**fanout:** 1 of 1 chains, cap 8, reason: one independent read cell with a disjoint write set (one new script and its record); worker `0.9.0_WK_IRPT_DASHBD~319` (`DB-i-19`).

## Cells

| cell id | owner |
|---|---|
| DB-i-1 | 0.9.0_WK_IRPT_DASHBD~301 |
| DB-i-2 | 0.9.0_WK_IRPT_DASHBD~302 |
| DB-i-3 | 0.9.0_WK_IRPT_DASHBD~303 |
| DB-i-4 | 0.9.0_WK_IRPT_DASHBD~304 |
| DB-i-5 | 0.9.0_WK_IRPT_DASHBD~305 |
| DB-i-6 | 0.9.0_WK_IRPT_DASHBD~306 |
| DB-i-7 | 0.9.0_WK_IRPT_DASHBD~307 |
| DB-i-8 | 0.9.0_WK_IRPT_DASHBD~308 |
| DB-i-9 | 0.9.0_WK_IRPT_DASHBD~309 |
| DB-i-10 | 0.9.0_WK_IRPT_DASHBD~310 |
| DB-i-11 | 0.9.0_WK_IRPT_DASHBD~311 |
| DB-i-12 | 0.9.0_WK_IRPT_DASHBD~312 |
| DB-i-13 | 0.9.0_WK_IRPT_DASHBD~313 |
| DB-i-14 | 0.9.0_WK_IRPT_DASHBD~314 |
| DB-i-15 | 0.9.0_WK_IRPT_DASHBD~315 |
| DB-i-16 | 0.9.0_WK_IRPT_DASHBD~316 |
| DB-i-17 | 0.9.0_WK_IRPT_DASHBD~317 |
| DB-i-18 | 0.9.0_WK_IRPT_DASHBD~318 |
| DB-i-19 | 0.9.0_WK_IRPT_DASHBD~319 |
