# Drive log 2.0.0_SA_COO~G2 -- 2026-10-15 ~14Z to ~19:40Z (IRPT_ANLREQ workstream ~G, the ENGINE lane)

Seat `2.0.0_SA_COO~G2` (dell2). Scope this window: IRPT_ANLREQ workstream `~G` (C-PRICES, C-SWITCH, C-SWAP step 2, the Comparison and Multi-Comp variants, the ONE resident release r32), on CTO msg 8377. IRPT_YCDGEN stayed WAITING on call f61b through the 11Z log and was handed to this workstream's scope by the absorption (C-ABSORB b). All commits are LOCAL on `box/dell2`; this seat does not push (box-sync and MSTR do). Push state is UNREAD in this log.

## Rounds issued and drained (one issuer, workstream ~G)

| round | cells | issued | merged | note |
|---|---|---|---|---|
| 7-9 | reads AR-g-53/54/55; chain core AR-g-51, swap AR-g-52 | earlier | `d1de2f0cd6` (AR-g-69) and earlier | reads of C-SWITCH, the compose, the price-adapter facts |
| 10 | AR-g-67 ticket stamp, AR-g-68 door Keep, AR-g-70 repair | earlier | AR-g-68 `4c82e94402`, AR-g-67 `c11be0ffdb` | AR-g-67 stalled on a sparse cone (W179-S1): the issuer's provisioning, widened |
| 11 | AR-g-80 `tr_level.py` | earlier | `f089142e91` | one formula for all four price sources |
| 12 | AR-g-81..84 the four price adapters | `ab568c7e80` | 81 `dc80bdd32c`, 84 `3cb1344c88`, 82 `5058a29160`, 83 `eecb6d8aa8` | 2 amendments, below |
| 13 | AR-g-85 variant reaches the Opal map | `465a64d051` | `002a88bdc3` | accept stamps `report_variant`; resident selects the pinned map by it |
| 14 | AR-g-86 price stage in the Opal producer | `089a3d3a6b` | `1c84d38bf4` | pricing off is byte for byte as before |
| 15 | AR-g-87 `irpt-anlreq-x10-v1` in the resident installer | `18b56252a2` | `38620fe9f2` | change 1 of the CTO's two additions to r32 (msg 8568) |
| 16 | AR-g-88 layout multi-column statistics; AR-g-89 priced page keeps the Opal wording | `484dac2efe` | in flight (slots 188, 189) | fanout 2 of 2, cap 8 |

## What surfaced and how it was ruled (issuer rules inside its own decomposition)

- **AR-g-83 (W183-S1):** my contract applied a split ratio only on the returned row; a split on a dropped bad-Close row read -49 percent where the true move is +2 percent. The text was the defect. Amended `af96479526` (s_t is the product of the ratios since the previous usable row), check case 11 added, worker re-run, merged. Gate limb: none graded (own order text).
- **AR-g-82 (W182-S1):** the hygiene allow-list refused the nested `opal_naming` import the order itself required. The check was the defect. Amended `a294ca574a`, worker re-run, merged.
- **AR-g-85 reference run:** two existing tests pin the exact accepted-record key set; found by the 65-test guard before the cut and named in the order's paths. The compose read's q3 named `run_opal` and `request_ref`; the variant is stamped at accept instead, because the vendor path refuses an UNRESOLVED row since AR-g-68.
- **AR-g-86 reference run:** two changes to the read's q4: only the price call is kept in the map's budget, and the page gets an empty kept dict (a non-computed call-sourced element is always NOT_AVAILABLE in the trace). Worker row W186-S1 then found the priced page printing YCharts wording against rule R8; my check had graded only a line count. Cut as AR-g-89, with the wording now graded (`ar_g89_checks.py`).
- **Map statistic defect (p2.e08, p2.e13, p6.e22):** the read proposed changing the map (moves its pin). AR-g-88 reads `columns` in the engine instead; no map change.
- **Client-data gate absent on this box (W181-S1, W184-S1, W187-S1, ARMED):** disposed by the issuer's read of the added lines for account-id-shaped strings (rows S123, S124, S125); the gate itself stays unmeasured and the list is not these orders' to place.
- **Operational:** three sparse-cone stalls earlier (widened); a wrong-agent resume (told to disregard); safe-merge refusals from another seat's staged index and lost races, retried; a rail denial of recursive greps (used named reads and the native Grep).

## Messages

- `~Y2`: AR-g-68 merged (door Keep may be cut; keep it dark on PROD until the release); reply to msg 8566 accepting the commentary revision and run 3's address into r32 (CTO msg 8568; `~Y2` msg 8570 fixes the address: `("andrew@opalinvest.com", "fwd1-staff-r41b@opal.invalid")`, r41a leaves in the same edit). Owed to `~Y2`: a message when r32's build is staged and when it is applied.

## r32 inputs recorded (the carrier is the decompositions R14 and R15)

Commentary revision (AR-g-87, merged); the producer-address swap (release cell, not cut); the comparison and multi-comp map pins and bindings (AR-g-85 selects by variant; the pins are the release cell's); the package member list (price_source, swap_replacement, portfolio_series, tr_level, the four adapters; `lib/trading_calendar.py` is not in the tarball); host dependencies pandas, pyarrow, yfinance (CloudOps pair) and the DEMQUE bucket and YCharts credentials grants (CTO rulings) are not mine to decide.

## Still to cut (each after its own read or reference)

The wiring of the real readers and T-1 into `make_opal_stores`; the swap for an unpriced symbol (needs a pool source); the benchmark and risk-free series (a symbol decision for the CRO); the YCharts-snapshot and non-computed series elements; the release cell r32.

## Heartbeat

Broker summary names no blocker on this seat; open items owned elsewhere: DEMQUE bucket grant and YCharts credentials grant (CTO), host dependencies (CloudOps pair in r32).
