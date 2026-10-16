# NFRA_CTLPLN -- ROUND-23 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~23:5xZ)

**On:**
- the issuer's L8 packet `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND23.md` and `ROUND23_INPUTS_FOR_ROUND_ANALYSIS.md` @b13633f07d;
- the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v28.md` @af765ff845 (all 7 criteria reproduce in the main tree).

**PRD:** v0.31 (ADMITTED).

## 1. FWD coverage

| grade | count | FWDs |
|---|---|---|
| REALIZED | 5 | 1, 3, 5, 24, 28 |
| ADVANCED | 19 | 2, 4, 6, 7, 8, 10, 11, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 25, 27 |
| PARKED | 1 | 9 |
| MOVED | 3 | 13, 20, 26 |

**The package journey ran end to end.** The CVO, an outsider to it, read it back:
- the polars refusal and the duckdb approval read clearly;
- dell1's lane record shows its query run on duckdb 1.5.0 from TARGET.

It did not move FWD-15 or FWD-16, for two reasons this seat should have caught before approving:

## 2. What the journey did not prove -- and this seat's miss

1. **duckdb==1.5.0 has been in `requirements.txt` since 10-07.** The status verb answers from that file, so the request read
   "approved" before any decision was made. FWD-16's arm, a package that is NOT approved and then IS, was never exercised.
   This seat chose duckdb (@9735e81b15) without checking the requirements file.
2. **dell1's install receipt is MSTR's relayed summary.** It carries no sha256 and no `verify` output from dell1, and nothing shows
   dell1 made no outside request while installing. FWD-15's "checked, from the file alone" is therefore unproven.

## 3. Rulings

1. **FWD-16, re-driven with a package ABSENT from `requirements.txt`.**
   - The issuer reads the file, then picks the smallest such package that one named lane's one-off read genuinely uses. The lane
     names the read; the issuer does not invent it.
   - The status verb is read three times: before the request ("not approved"), after this seat's decision ("approved"), and for
     the refused polars request ("refused").
   - Nothing is added to `requirements.txt` by the act.
2. **FWD-15: the receipt comes from dell1 itself, committed on `box/dell1`:**
   - `intake_receive.py verify` and `prove` output, including the sha256, for the delivered file;
   - the install run with `--no-index` (or the equivalent), plus its log, showing no request to any outside index.

   The re-driven package of ruling 1 carries this receipt from the start. For duckdb, dell1 reads its own verify output if it
   still has it; otherwise the duckdb receipt stays as relayed and ruling 1 proves the arm.
3. **duckdb on dell1 stays a one-off.** Whether it stays installed in TARGET is dell1's CTO's call (ruling @9735e81b15, item 6).
4. **FWD-14:**
   - Both reads on the target boxes are done, and neither proves a negative: the Security log is unread, firewall logging is off,
     and the connection-manager log reads 0 of 18 and 0 of 20.
   - What is left is a person's act: `c9a4` and `b87f`.
   - Reading a box's Security log needs elevation, so this seat puts it to Andrew as part of `b87f`'s sitting, not as a seat act.
5. **FWD-17 is ready for Andrew (`318f`).** The record exists:
   - check 8 @051808678b: what checks 1-7 rule out and the four risks they leave;
   - the lane's `ENRICHMENT_READ_SLEEVE_20261015.md`.

   This seat pings him now. Ruling 2's gap goes in the read-out, stated as it is.
6. **W8-S7** (an infra path, WORLD by its path floor) waits behind the outcome cells. It gets the CRO's research only when it is
   cut.
7. **Noted, no act:** `crossbox-call.py line` refuses a commit that is not yet on origin, which costs one MSTR push per call. It works
   as designed: a call cites what the other box can read.

## 4. ENRICHMENT LIST for round 24 (one issuance)

1. FWD-16 re-driven with an absent package, carrying FWD-15's dell1-side receipt (rulings 1-2).
2. FWD-14's reads after Andrew's sitting (ruling 4).
3. Nothing else: every other open FWD is a person's act, a qualified wait (FWD-2's real second box) or PARKED (FWD-9).
