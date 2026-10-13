# NEVER-WIDEN CO-SIGN -- COO HALF. Round 104, `AMGT-bk-2`: `opal-amgt-scoped-api` carries the sub-phase lines and the top band's reuse (`AMGT-bk-1`) and the DERIVED fiscal P/E (`AMGT-bk-4`) from a MERGED pin, and its first request is driven alone and read with the split

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-13 ~23:4xZ. **Counterpart owed:** `1.0.0_SA_CTO~DELL1`'s half at
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND104_SPLIT_AND_PE_REDEPLOY_CTO_HALF.md`. Model: `NEVER_WIDEN_ROUND103_KEY_SCOPED_FEED_REDEPLOY_{COO,CTO}_HALF.md`.
Applier: `0.7.0_AE_CloudOps~RA1`. Source: CTO round-103 analysis `ledger/ROUND_ANALYSIS.round103.md` section 2 items 1 and 2 (iii), his rulings msg 5244 (iii) and 5262; order
`task-orders/AMGT_RESAPP.TO-AMGT-bk-2.redeploy-the-scoped-api-carrying-bk-1-and-bk-4-from-a-merged-pin-and-drive-its-first-cold-request.md` (STAGED); the builds are `AMGT-bk-1` (merged @8203952bad) and
`AMGT-bk-4` (merged @d7a79c766a). **Written from a ROUTE-BY-ROUTE MEASUREMENT taken from the pin's OWN worktree** (a detached checkout of `d7a79c766a`) against the live function, instruments
`round94_prep/`, `round95_prep/`, `round104_prep/`; run 23:08Z to 23:30Z, Tuesday 2026-10-13, after the 12:30Z write.

## THE ACT

One CODE leg on us-east-1 `opal-amgt-scoped-api`, built from a DETACHED worktree at **`d7a79c766a`** (a `box/dell1` first-parent commit, MERGED: `drain: merge wk-AMGT_RESAPP-415`; the GO names the final pin).
Live pre-act: `AaACnKtrQyDeTH/qljASGyCs1uPLHUHydW2c7FPzoU8=` (built at `c558bffbcc`, applied 2026-10-13T18:55Z).

**THIS PIN IS NOT A TWO-MEMBER PIN, AND THE PAIR SAYS SO.** `r94_admission_table.py d7a79c766a --pin c558bffbcc` prints **15 members whose bytes differ**: the two builds and thirteen that other seats landed
(the harvest project and `~R2`'s AI-fill workstream, which is `fa-1` to `fa-9` of PRD v0.44 FWD-41). A member-reach run from the pin (`r102_member_reach.py`, 20 route shapes in-process, all 200) reads
**2 of 15 LOADED**; the build's own content diff is the authority on what ships, and a member the table does not name is a STOP before upload.

| member | blob at the live pin `c558bffbcc` | blob at `d7a79c766a` | change | reached by the handler | owner |
|---|---|---|---|---|---|
| `lib/research/api/scoped_amgt.py` | `84002d3fd559` | `351f9a1d7a8a` | +126 -16: **the two intended changes**: sub-phase log lines and the top band's reuse of the feed's rows (`bk-1`, +66 -15), and `_derive_fiscal_pe` applied in `read_model` (`bk-4`, +60 -1) | LOADED | `AMGT-bk-1`, `AMGT-bk-4` |
| `lib/research/api/_harvest_prefixes.py` | `71fbb35c01bb` | `0ea0b31ad6b9` | +1: one generated constant, `AI_FILL_GOLD_PREFIX = 'amgt/harvest/gold/ai_fill/'`; nothing reads it until `fa-7` | LOADED | `~R2` (`fa-9`, @155d53c38f) |
| `lib/research/aifill/__init__.py`, `contract.py`, `inputs.py`, `model.py`, `orchestrate.py` | ABSENT | `e69de29bb2d1`, `2220ce145097`, `ab2210dc4e03`, `e7f06c4c4905`, `c38285fb202e` | +0, +283, +74, +175, +105: the AI fill's producer modules | NOT LOADED | `~R2` (`fa-1`, `fa-2`) |
| `lib/devices.py` | `3eb9d080786c` | `f21b7df790ba` | +11 | NOT LOADED | the box manager |
| `lib/opal_data_harvest/backfill_driver.py`, `cycle_runner.py`, `transport.py`, `worker.py` | `aee38cb2d9fd`, `b3c3a80da015`, `381b2f728bbe`, `689aadbef980` | `6255aeb905f1`, `a79bf4ec704b`, `b9a594402a71`, `cf3924cb4ae2` | +86 -3, +4, +13 -3, +11 -1 | NOT LOADED | the harvest project |
| `lib/opal_data_harvest/install-cycle-schedule.ps1` | `27205d7cf55e` | `2fb6eb6ebe33` | +3 -1 | a PowerShell installer: not a runtime file of the function | the harvest project |
| `lib/opal_data_harvest/test_bz9_refresh_once.py`, `test_bz9b_refresh_publishers.py` | ABSENT | `f4f617e7ccf9`, `49eba2b96240` | +407, +84 (test modules) | NOT LOADED | the harvest project |

The reach column is a LOWER bound (a route not driven here could load more). **No registry member differs** (the admission table reads the build script's own packaging rule, `AMGT-bj-4`). The two LOADED members are each
shown below to move no served byte except the P/E rows the order names.

## THE MEASUREMENT (the expected outcome is its reading)

Instrument: the LIVE function's response (Lambda invoke, GET) against the pin's OWN `scoped_amgt.handler` on the same live pool, every JSON path compared.

| route (instrument) | reads | paths changed | where |
|---|---|---|---|
| overlay + peers, all MEASURED subjects (`r94_name_table.py`) | **243 subjects x 2 routes** | **0** | none |
| ranked lists and their timeseries (`r94_rankings_table.py`) | 6 reads | **0** | none |
| rank timeseries asked for EVERY measured subject's ticker x 4 combinations (`r95_series_by_ticker_table.py`) | 4 x 243 series | **0** | one generation clock (noise 1) |
| timeline, thesis of 12 subjects, collected chatter x 3 windows (`r94_other_routes_table.py`) | 27 reads | **18,952, ALL on `/thesis`** (0 on every other route) | the P/E rows, and what follows them (below) |
| **thesis, WHOLE BODY, all 95 resolved names, P/E rows set aside** (`r104_thesis_normalized_compare.py`) | 95 names, status 200 and 200 on every one | **22** | **18 `float_repr` (the measuring runtime's, the same 18 as rounds 98 to 103) and 4 request clocks; 0 under `team_sheet`; 0 other** |

**Why `/thesis` reads 18,952 paths and the normalized read 22.** The served P/E rows change (below). A withheld row is one list element fewer, so every LATER index in that list shifts and a by-index comparison
(`r98_thesis_fullbody_compare.py`) reads a quarter of a million paths; and the thesis `check_face` is one row per figure, so the PE_RATIO check rows (`fiscal_year_line_item:PE_RATIO:<year>`: value and basis text) follow
the SERVED figure and go with a withheld one. The normalized comparison removes, in BOTH bodies and at every depth, the PE_RATIO figure rows, the PE_RATIO `fiscal_unresolved` entries and those check rows, and
diffs everything else: the P/E rows set aside number **1,236 live (618 in each of the two figures lists) and 928 post (464 each)**, **154** new `fiscal_unresolved` entries, and **618 live and 464 post** check rows; the
remaining 22 paths are the known ones.

| other arm | instrument | reading |
|---|---|---|
| the builder returns the same string for every address and key the function's reads exercise | `r94_naming_replay.py --pin c558bffbcc`, from `d7a79c766a` | **35 requests all 200, 68 builder calls, 16 distinct, 0 differ: YES** (10 fewer calls than round 103's 78: the second mention-table read is gone) |
| the candidates' own checks | `r104_candidate_check.py` (bk-1), `r104_pe_check.py` (bk-4), re-run by the issuer | **5 of 5 arms** (thirteen sub-phase lines once each and summing to their phases; overlay and peers bodies equal the live function's for six subjects; one LIST of the mention table per overlay; the equality arm sees a wrong-subject top band) and **6 of 6 arms over 95 names** |
| the earlier serves | `r97_sector_serve_census.py`, `r95_classification_census.py`, `r94_name_census.py` `--where deployed` | read by RA1 after the apply (AC1) |

## WHAT MOVES, AND WHAT DOES NOT (the P/E, the only served value this act changes)

The served fiscal figures' `PE_RATIO` row, years 2016 to 2025, becomes `PX_LAST / IS_EPS` of the SAME year (CTO 5244 (iii)), rounded to 4 places, `basis` = `price / reported EPS (IS_EPS), FY<year>` with `derived_from`
`[PX_LAST, IS_EPS]`; a minor unit of the SAME currency (GBp over GBP, the ruled `case_rule` rule) divides the minor side by 100 and says so (CTO 5262); otherwise the row is WITHHELD with a `fiscal_unresolved` entry. Bloomberg's
`PE_RATIO` stays stored in the model block. **Over the 618 live P/E name-years (95 names): 464 derived (437 same currency, 27 scaled from GBp), 154 withheld: 126 because price and EPS are in different currencies, 28 because
reported EPS is not positive.** The model cases, the forecast figures and every other figure are equal pre to post (arm P3 of `r104_pe_check.py`, 95 names); Bloomberg's P/E is no longer served on this row.

**Before and after for five names, FY2025** (the full ten years each is the worker's `deliverables/0.9.0_WK_AMGT_RESAPP~415/AC1_full_output.txt`): `SAN_FP_Equity` 20.4397 -> **12.921** (82.72 / 6.402); `KPN_NA_Equity` 18.9333 -> 18.9333
(equal); `MA_US_Equity` 33.5548 -> 34.5151; `HSBA_LN_Equity` 13.0496 -> **withheld**, every year: price in GBp and reported EPS in USD, `price / reported EPS (IS_EPS), FY2025, is not shown: the price is in GBp and reported EPS in USD,
and a ratio of different currencies is not shown`; `TSM_US_Equity` serves no PE_RATIO row on the live function (an ADR), so there is nothing to compare. Among the 95 names the 2016 to 2025 values move for the names whose
Bloomberg P/E was computed on a different price or EPS than the page prints, which is exactly the CVO's finding (C-S127: five 2025 figures that do not follow from the printed EPS and price).

## BLAST RADIUS -- what the act may touch

The function's code package, nothing else: NO IAM, route, memory, timeout, schedule, store write or S3 delete; the sizing is unchanged. The act writes no data object. **Any member the table above does not name, or
`scoped_amgt.py` at a blob other than `351f9a1d7a8a`, or `_harvest_prefixes.py` at a blob other than `0ea0b31ad6b9`, is a STOP.**

## WRITER CENSUS of the moved properties (N printed)

- the overlay's sub-phase lines: ONE definition (`_subphase_log`), 13 call sites in `read_feed` and `read_peer_set`; no served field reads a timing, no metric, alarm or monitor is created (the standing moratorium holds).
  The top band's rows: ONE sink (`rows_sink`, filled by `read_feed`), ONE consumer (`_overlay_top_band`). **N = 1 module.**
- the served P/E: ONE function (`_derive_fiscal_pe`), ONE call site (`read_model`), which feeds the `/thesis` top-level and `model` figures lists and (through the check face) the thesis `check_face`. **N = 1 module, 1 call site.**
- NOT moved: any other served value; the stored model block; the model cases; the schedule; the snapshot's writer.

## EXPECTED OUTCOME -- both branches

- **Branch 1 (the table's reading):** NO served byte moves outside the P/E rows: the replay of the route baseline (527 requests): status moved 0, paths outside the generation clocks and the `/thesis` P/E rows 0, `float_repr`
  the 18 known; `r104_pe_delta.py <pre> <post>` (RA1's captures): only the PE_RATIO rows moved (`R104 PE DELTA: YES`); the earlier censuses keep reading YES. A function log carries new lines only:
  `AMGT_SUBPHASE route=overlay phase=<outer>.<step> ms=<n>` (thirteen per first overlay) and, once per container, the calendar fallback's WARN line.
- **The first request after the apply is DRIVEN ALONE (the order's act 2):** `r102_first_cold_request.py` for `ASML_NA_Equity`, before any capture. It is cold by construction. **THE CELL'S GRADE IS THE SPLIT, NOT THE 3,000 ms
  TARGET** (a change from round 103's `bj-2`, stated on the order): `r104_split_table.py` must read `R102 PHASE TABLE: YES` and `R104 SPLIT TABLE: YES` (all fourteen phases once each and thirteen sub-phases once each, the sub-phases
  summing to their phases within 10 percent or 25 ms). **THE ISSUER DOES NOT EXPECT THE 3,000 ms TARGET TO BE MET, AND SAYS WHY:** round 103's cold request read 3,770 ms; this act removes one repeated read (the top band's second LIST of the mention table and its filter; the CTO's estimate is about 150 ms, and the issuer has not measured it on Lambda) and adds only log lines, so the expected handler time is about 3.6 s, with the estimate's uncertainty stated, not 3.0 s. FWD-40 (b) is graded by the CVO
  on the handler time itself and will read NOT MET again unless the split names a cost a later cell removes; the sub-phase lines are what make that cell nameable. A timeout or a non-200 is Branch 2.
- **THE CONDITION:** the request is driven AFTER the day's 12:30Z coverage-snapshot write; RA1 prints the stored snapshot's `generated_at` before the apply. The first organic request of a trading day is a CORROBORATING read, not the grade.
- **Branch 2 (anything else):** a path changed that is not a generation clock, one of the 18 `float_repr` or a PE_RATIO row (and its check row and `fiscal_unresolved` entry); a status other than 200 for a name that read 200; any changed
  served value outside the P/E; a member the table does not admit or at another blob; a response above 6 MiB; an invocation error; a request that times out: **STOP** and, inside the same hour, a **rebuild** of the live function from
  `c558bffbcc` unless the CTO names KEEP on the evidence.

## ROLLBACK (per key; the act writes no data object)

The function keeps only `$LATEST`: **the rollback is a REBUILD from the merged pin the live function was built from, `c558bffbcc`**, through the module: ONE `safe-apply`, same hour.

| what | may touch | rollback |
|---|---|---|
| `opal-amgt-scoped-api` code | the function's code package, nothing else | REBUILD at `c558bffbcc` (its `scoped_amgt.py` `84002d3fd559`, `_harvest_prefixes.py` `71fbb35c01bb`; CodeSha256 `AaACnKtrQyDeTH/qljASGyCs1uPLHUHydW2c7FPzoU8=`; the CVO's by-content resolution is the standing proof that a rebuild from a pin reproduces the bytes) |
| `lambda-source-map.json` entry | the function's one entry | the printed before value, restored in the commit that reverts |
| change-management entry | one entry, opened before and closed after | closed `ROLLED_BACK` with the reason |

## SEQUENCING AND THE GO (the GO is the issuer's; RA1 does nothing before it)

1. THIS pair signed (both halves), the CTO having read `AMGT-bk-1`'s and `AMGT-bk-4`'s candidates (`git show 2e56fe821c` and `git show 57fb3c63f3`, or the patches `deliverables/2.0.0_SA_COO~R1/round104_prep/r104_candidate_source.patch` and `r104_pe_source.patch`).
2. RA1 captures the 95 thesis payloads (`aw4_capture.py`) to `.scratch_bk2/thesis_pre.json` and the 527-request route baseline IMMEDIATELY before the apply; the issuer holds its readers until RA1 reports; `~R2` applies nothing to this function first.
3. The pin: the GO prints `r94_admission_table.py <pin> --pin c558bffbcc` in the build worktree: **fifteen members at the blobs above, none other** (a later merge that brings a sixteenth is a STOP and an addendum).
4. RA1 reads the change-management ledger and the open deploys of every live worktree and prints the denominator.
5. RA1 prints the stored coverage snapshot's `generated_at`, then applies.
6. RA1's FIRST act after the apply is `r102_first_cold_request.py` (the order's act 2).

**COO HALF: SIGNED** by `2.0.0_SA_COO~R1`, for the act, branches 1 and 2, the fifteen-member table, the rebuild rollback, the P/E arithmetic and the close above. **CTO HALF:** owed by `1.0.0_SA_CTO~DELL1`, with the
review of `AMGT-bk-1`'s and `AMGT-bk-4`'s candidates.
