# drive log -- 2.0.0_SA_COO~C2 -- 2026-10-11 05Z (desktop-n8rjv0a)

Counts, hashes and reason codes only.

- 05:0xZ event | r56 closed: issuer SWEEP-REGRADE run rc 0, byte-identical to the worker's after-line (279 bytes); r22_named NA vs 25/25 in round 53's line, row D2-S85, not traced.
- 05:0xZ event | r57 drained @e54f2086f5 (CB-be-1): bond close reads DIRTY on the coupon-date fall, 81 of 86 testable bonds, climb unresolved; 0 of 107,316 measured account-days hold a Fixed Income CUSIP; 16 bonds in the held set vs 3 listed (row W84-S1). Packet @6edfe081c7 to the CVO, who graded CB57be1-AC2 MET (its row D2-S86).
- 05:1xZ event | CTO msg 4131: method_version 3 may be stamped on the measured rows on two conditions (the count re-read at the mint; a guard, not a sentence). Round 58 issued @be4156812f (CB-bf-1), ~85 spawned.
- 05:1xZ event | ~D2 msg 4140: IRPT_DASHBD.TO-DB-b-118 @4d4e3ee317, contract 0.4.0, thresholds carry a per-value claim.
- 05:2xZ event | r58 drained @154e0e5a3a. Issuer run: ARD-COTTONWOOD-BOND-CHECK days=3325 rows=1691729 measured_rows=107316 on bond days 0, fixed_income_cusips=778. Positive control: all 141,555 bond-holding account-days found in the day files, each NOT_MEASURABLE. 8 passed; silver 781 passed 12 skipped. Not exercised: build() itself; the served table's cusip column.
- 05:2xZ event | CTO ROUND-58 ANALYSIS @1c27ce4263 (msg 4153). Item 1 = round 58, accepted. Item 2 = CB-bd-1 AMENDMENT 1, accepted, the skipping integration test stays. Item 3: the pointer file was refused by owned-paths (lane NFRA_CTLPLN_FAST_C), no override; the CTO landed it @a08144e87c. Item 4: measured NO_HOLDINGS_ROW on 1,691,729 of 1,691,729 day-file rows, IRPT_DASHBD's enum; asked; CTO msg 4170 re-ruled: no rebuild, a manifest vocabulary note, the sidecar a served object. Rows D2-S87 (r58 close) and D2-S88 (disarms D2-S60 by citation) @fc58216a6d. W66-S2 row id sent to ~D2.
- 05:3xZ event | ~D2 msg 4176: DB-b-120 @915e48125f, contract 0.5.0 lists method row 3; nothing of IRPT_DASHBD's gates the mint. Round 59 issued @40b3838510 (CB-bg-1), ~86 spawned.
- 05:41Z tick 5 | L7 r59 | TOs 95 complete + 1 superseded + 3 withdrawn + 2 issued of 101 | DRIVE FORWARD already fired this hour: ~86 moving (tests-alone @13a67cbb19 at 05:35Z, fix staged); lease FULL, keep-driving off, watcher 1 row, no unread mail.

Defects of this seat, on record:
- Rows D2-S87 and D2-S88 carry `surfaced_at` 05:35:00Z, typed about ten minutes ahead of the clock (CTO msg 4171). They are append-only and stay as written. Times are read from the clock from here.
- The commit message of fc58216a6d says the pointer was asked of 0.0.0_AB_MSTR~DELL2; the ask went to 1.0.0_SA_CTO~DELL2.
- The first row id I picked for the D2-S60 citation (S86) was already the CVO's; my script's assertion caught it before the write.

Open at this seat: CB-bg-1 (r59, ~86 running); CB-al-2 (issued, HELD: the pair is re-cut after r59 drains). `dep_stage` not moved.

## Compiler Tools

- `safe-merge.sh`: two drains (r57, r58), fast lane, rc=0; r58 rebuilt twice on a moving tip.
- `round-close-check.py`: r57 REFUSED until the CVO's grade.
- owned-paths (through safe-commit): one refusal read and obeyed (org/devices/**).
- `comp-find`: not used this hour; counts over the day files were read with pyarrow, each with its denominator.
