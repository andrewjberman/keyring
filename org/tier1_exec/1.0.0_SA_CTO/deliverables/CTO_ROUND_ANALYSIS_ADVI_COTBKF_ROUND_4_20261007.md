# ROUND ANALYSIS -- ADVI_COTBKF round 4 (L10)

**Author:** `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~08:5xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES (origin 2f61412157: a Dell CTO lane
writes L2-L4 and the L10 answers for the projects placed on its box; laptop ruling 1, `CTO_RULINGS_FOR_THE_DELLS_20261007_0740Z.md`).
**On:** `3.0.0_SA_CVO`'s slug (msg 140). Remediations `surprise-channel/remediations/REMEDIATION_v2.md` @2114a2a7a2. Grade file
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_4_L9_GRADE_20261007.md`. Drain-end packet
`deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_4_DRAIN_END_20261007.md` @29479eeb61. 5 of 5 orders are terminal, with proof VALID on all
5. L9: CB4d1-AC3 NOT MET; CB4d2-AC3 MET; CB4d3-AC3 MET; CB4d5-AC3 owed at the apply. ARMED after the compile: W12-S1 and S9 (BLOCKING).
**Issuing lane for round 5:** `2.0.0_SA_COO~C2` (dell2).

Claim words: `measured` = read by this seat today on dell2; `held` = cited from the record named; `inferred` = not read.

## 1. Row S9 -- CAUSE NAMED: the trading-calendar fallback on dell2

**Verdict: NAMED, reproduced row for row (measured).** dell2 has no `pandas_market_calendars` (row W12-S1). So `lib/trading_calendar.py`
falls back to `NYSE_HOLIDAYS_FALLBACK`, which lists holidays for 2024-2027 only; dell2's `calendar_source()` reads
`NYSE/hardcoded-fallback-2024-2027`. Before 2024, every NYSE holiday therefore counts as a trading day. The links rule is measured in
trading days: `TradingIndex` (`commonwealth_account_links.py:179-186`) feeds both the exit window that rebuilds an account's end
positions (`:227`, `WINDOW_TD = 10`) and the receipt-gap filter (`:288-291`). A holiday wrongly counted widens the trading-day distance.
That pushes an in-kind exit out of the 10-day window, which empties the end positions ("closed to cash"), or lets a second candidate
through (cv0QF879185). The two dropped links exit on 2023-02-14 and 2023-12-22, 4 and 1 calendar days before the 2023-02-20 and
2023-12-25 holidays.

**Reproduction** (read-only; this seat, dell2; the script's own functions over the issuer's `.scratch/advi_cotbkf/tx_cache`, 1,416,497
rows; nothing written outside the session scratchpad; script `s9_repro.py` kept there):

| run | calendar | LINKED | differs from the laptop deliverable (`0.9.0_WK_ADVI_COTBKF~13/account_links_r4.csv`) | differs from the dell2 real run |
|---|---|---|---|---|
| A | as on dell2 (fallback 2024-2027) | 211 | 3 of 1,450 (0QF879348, B3S780328, cv0QF879185) | 0 of 1,450 |
| B | fallback plus the NYSE full-day closures of 2013-2023 | 212 | **0 of 1,450** | 3 of 1,450 |

Under B, 0QF879348 -> B3S606523 and B3S780328 -> B3S782287 read LINKED, and cv0QF879185 reads NOT_LINKED, "ambiguous: 0QF879185 (1.0),
0QF879621 (1.0)". That is the laptop deliverable exactly, on (status, new_account), for all 1,450 rows. **Limit:** run B's 2013-2023
closure list is model-prior (inferred), not read from `pandas_market_calendars`. The row-for-row reproduction is the evidence; the list
itself must come from the package before it lands anywhere (section 4, E1).

**Rejected candidates:**
- (a) Line endings: both runs read the same parquet cache, and A reproduces dell2 exactly, so line endings cannot explain it.
- (b) Library versions: same cache, same code, and only the calendar varies between A and B.
- (c) Input listing: the links read only `tx_cache` and `pos_cache`, never the two unlisted buckets.
- (d) Ordering: the candidate sort is deterministic (`:297`, key (-score, account)).

**Which output is right: the laptop's.** The CVO re-read both dropped links' evidence on the transactions (123 of 123 items hold).
cv0QF879185 has two candidates at score 1.0, so dell2's LINKED is a guessed link, which FWD-9's ACCEPT forbids.

**RULING:** S9 stays ARMED. No `--apply` of the links from any box whose `calendar_source()` is a fallback that does not cover the
table's dates. S9 disarms when the run that is applied reproduces the committed laptop deliverable row for row (E1, E2).

**The same defect bears on two more round-4 outputs:**
- W12-S1: the census's `security_days_*` figures (`commonwealth_price_census.py` and `commonwealth_price_need.py` both import the
  calendar). The priced counts do not depend on it.
- The wider estate, routed in section 6.

## 2. Outcome state -- 2 of 9 REALIZED

| FWD | verdict | evidence | what still holds it |
|---|---|---|---|
| FWD-1 | REALIZED | held: CB-a-3 complete, proof @0beab88f77; the decomposition names that run as FWD-1's EXERCISED read | -- |
| FWD-2 | NOT REALIZED | measured: bronze holds the ClientDelivery zip (v0.4 ADDENDUM, SHA-256 equal to the manifest) and the three imaging archives `bronze/imaging/date=2026-06-23/plan_id={4XF,HJH,HKE}` (113,362,389; 1,503,993,172; 1,554,270,895 bytes) | The CRM zip waits on C-RESTRICTED, which is not applied (CB-d-4, row S7). The imaging archives' manifest fingerprints are not re-read by this seat |
| FWD-3 | NOT REALIZED | none this round | Prices: C-DAILY's sources are ruled (v0.4 ADDENDUM 2), but the pull waits on MDPF_SECHIST's securities-history store (dell1) |
| FWD-4 | NOT REALIZED | none | The CRM records sit behind C-RESTRICTED |
| FWD-5 | NOT REALIZED | CB-d-5 plan: 11,119 unique documents, every source verified, 0 refused (held, drain-end packet) | The apply. CB4d5-AC3 is graded on one statement and one tax form found and opened |
| FWD-6 | NOT REALIZED | the coverage store exists (`silver/coverage/date=2026-06-23/`, measured listing) | Not read by someone who was not told. The census's completeness is NOT MET (W12-S2) |
| FWD-7 | NOT REALIZED | CB-d-4 merged, plan only | The C-RESTRICTED policy is not applied, and no unauthorised read has been refused |
| FWD-8 | NOT REALIZED | CB4d3-AC3 MET; the round-3 crosswalk is applied (`silver/crosswalk/`, 2026-10-06) | The round-4 crosswalk is not applied. The 21 near-matches await Andrew's answer from Cottonwood (rows stay "not linked, awaiting a person") |
| FWD-9 | REALIZED | held: CB3c4-AC3 MET (`ADVI_COTBKF_ROUNDS_2_3_L9_GRADE_20261007.md:60`: `cvB3S606716 -> B3S606716 -> 0QF886265` read on the applied round-3 table); round 4 extends it to every ended account (CB4d2-AC3 MET) | The round-4 extension's apply is behind S9 |

## 3. Disposition of the open rows

| row | standing | disposition | owner | act |
|---|---|---|---|---|
| S9 | BLOCKING, ARMED | Cause named (section 1). Cut: E1, E2 | `2.0.0_SA_COO~C2` | Disarm row filed when E2's applied run equals the laptop deliverable 1,450 of 1,450 |
| W12-S1 | ARMED | Same cause. Cut: E1. Do not provision the package on dell2: a PyPI install is egress (CLAUDE.md Agent Autonomy), and E1 needs none | `~C2` | Disarms when the census's `security_days_*` are re-run under a calendar that covers 2013 onward and are reported against round 2 |
| W12-S2 | INERT | Routed. Listing `opal-data-cottonwood` and `opalinvest-portal` needs a principal permitted on them. The Dell bucket fences are NFRA_CTLPLN round 4's first cell (laptop decision 106062, `2.0.0_SA_COO~C`); a one-off listing goes, like S338, to a laptop seat by relay | `~C2` asks through this seat | CB4d1-AC3 is re-graded on that listing |
| W12-S4 | INERT | Owned by `0.0.0_AB_MSTR~DELL2`, unchanged: ratify ruff as dell2's provisioning on Andrew's word for the egress, or remove it | `0.0.0_AB_MSTR~DELL2` | -- |
| S7 | INERT | CB4d4-AC1 is re-run on the box that applies C-RESTRICTED, immediately before the apply. A bucket policy is the laptop's under ruling 1 (access by write-in) | `~C2` writes the write-in (E4) | -- |
| W13-S1, W14-S2, W14-S3, W12-S3 | INERT | Accepted as the issuer read them. No cell | -- | -- |
| W14-S1 | closed | Disarmed by S8 | -- | -- |

## 4. ENRICHMENT LIST -- round 5, ONE issuance by `2.0.0_SA_COO~C2` (each item at most three mechanical criteria)

| # | item (FWD / rows) | criteria | risk |
|---|---|---|---|
| E1 | **The Commonwealth scripts refuse a calendar that does not cover their dates** (S9, W12-S1). In `commonwealth_account_links.py`, `commonwealth_price_census.py` and `commonwealth_price_need.py`: when `calendar_source()` is a fallback and the table's earliest date is before the fallback's first year, exit non-zero and name the uncovered years. No silent run | (1) on dell2 as it is, each of the three scripts exits non-zero and prints `CALENDAR-UNCOVERED 2013..2023`; (2) a unit test with a stubbed calendar covering the dates passes and one not covering them fails; (3) `py_compile` and the commit gate pass | LOCAL |
| E2 | **The links and the census on a covering calendar, then the links applied** (S9, W12-S1; FWD-9). GATED: cut only once `lib/trading_calendar.py` covers 2013 onward on dell2 through the laptop's fix (section 6). dell2 installs nothing from PyPI to get there: that is egress off Opal infrastructure (row W12-S4; CLAUDE.md Agent Autonomy) | (1) the links run, under a calendar whose `calendar_source()` covers 2013 onward, equals `0.9.0_WK_ADVI_COTBKF~13/account_links_r4.csv` on (status, new_account) for 1,450 of 1,450 rows; (2) `--apply` writes the builder key `silver/account_links/date=2026-06-23/`, read back with the 212 LINKED count; (3) the census's `security_days_needed` / `_covered` are re-printed beside round 2's | SERVED |
| E3 | **The unique documents and the documents table applied** (FWD-5) | (1) every plan key is checked against the C-RESTRICTED prefix, and any key under it is held back and counted, not written; (2) `--apply` writes the rest and the documents table, and the count equals the plan less the held-back count; (3) one statement and one tax form found by account and date and opened (CB4d5-AC3, graded at L9) | SERVED |
| E4 | **C-RESTRICTED: the apply write-in** (FWD-7, FWD-4, FWD-2 CRM zip; row S7) | (1) the C-ROLE-REQUEST names the merged policy file, the bucket and prefix, the break-glass role, and each permission tied to its line; (2) it carries the CB4d4-AC1 command to re-run immediately before the apply; (3) it is sent to `1.0.0_SA_CTO~DELL2` by path, which forwards it | LOCAL |
| E5 | **The round-4 crosswalk applied** (FWD-8), with the 21 near-matches left "not linked, awaiting a person" | (1) `--apply` writes `silver/crosswalk/date=2026-06-23/`, read back with matched 439 / not_matched 1,094; (2) `near_matches_applied=0` on the applied run | SERVED |

Chains: E1 then E2. E3, E4 and E5 are independent. Fan-out: 4.

**E2's covering calendar must not come from model memory.** One of two sources: (i) `pandas_market_calendars` on the box that runs it,
which on dell2 needs Andrew's word for the PyPI egress (not asked for here); or (ii) `NYSE_HOLIDAYS_FALLBACK` extended back to 2013, with
the values generated by `pandas_market_calendars` on a box that has it and the generating command committed beside them. Option (ii) is
an edit to the shared `lib/trading_calendar.py`, routed in section 6. `~C2` runs E2 on whichever lands first, and says which.

**Not in this round:**
- The price pull. It waits on MDPF_SECHIST's store (dell1), unchanged from the rounds 2-3 analysis.
- C-RESTRICTED's apply itself, which is the laptop's.

## 5. Acts only Andrew can do (this project), each with its citation

1. **The 21 near-matches, put to Cottonwood** (`0.9.0_WK_ADVI_COTBKF~14/near_matches.md`). Contacting the firm is egress off Opal
   infrastructure (CLAUDE.md Agent Autonomy), and FWD-9's ACCEPT says a link is never guessed. Carried from the rounds 2-3 analysis.
   Nothing in section 4 waits on it.

## 6. Routed outside this project

- **The Dell calendar hazard (estate-wide).** 103 Python files import `trading_calendar` (Grep count at HEAD). On any Dell without
  `pandas_market_calendars`, every one of them that reads a pre-2024 date counts that date's holidays as trading days, and nothing says
  so. In scope here, IRPT_BCKEND's full-history checks and the INF and COT `c02_twr_engine` runners are examples (inferred; not run).
  To laptop `1.0.0_SA_CTO` through `0.0.0_AB_MSTR~DELL2`: either extend `NYSE_HOLIDAYS_FALLBACK` back to the estate's earliest date from
  the package's own output, or make the fallback fail closed outside its years. The shared lib and the Dell bring-up kit are both the
  laptop's.
- **W12-S2's listing:** a laptop seat by relay, as for S338.
- **This seat's REC on the calendar fix: both halves.** Generate the full NYSE closure list from 2010 onward from the laptop's installed
  package, commit it as the fallback data (no network at run time on any box), AND make `calendar_source()` fail closed for any
  date outside the fallback's years. The first fixes the Dells. The second makes the next gap loud instead of silent.

-- 1.0.0_SA_CTO~DELL2
