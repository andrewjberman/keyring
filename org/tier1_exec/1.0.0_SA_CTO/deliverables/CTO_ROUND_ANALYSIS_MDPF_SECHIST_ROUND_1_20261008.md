# MDPF_SECHIST round 1 -- the CTO's L10 answer

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-08 ~13:2xZ. **Input:** `3.0.0_SA_CVO` slug msg 903 (`ADJUDICATION_v2.md` @0de91553e2, on L8
packet @ebe4f1d305; 2 of 2 orders terminal). PRD v0.2.

## 1. Coverage

| FWD | grade | read |
|---|---|---|
| FWD-1 | NOT REALIZED (QA PASS) | The 10-08 scheduled pull FAILED (Terminal signed out, 0 attempts). The QA re-pull (2,929 rows under the ledger) served CSCO, BX, LNVGY and 9 more at 8 of 8 windows with class and sector (CVO read 13:01:38Z). Acceptance is the first unassisted scheduled pull, earliest 10-09 (ruling cb6fb2a52c). **One hop fails FWD-1's own ACCEPT, "clean name"**: see 2.2 |
| FWD-2 | NOT STARTED | card A (Bloomberg backfill, 1,319 securities) approved by Andrew ~18:5xZ 10-07; held at site Z by ruling 31292 until claims 2 and 3 record in bbg_budget |
| FWD-3..9 | not graded this round | round 1 built the thread |

## 2. Rulings

**2.1 The id collision (CVO's call).** A remediation row's id IS the investigation row it graduates (the remediation row schema).
REMEDIATION_v1's rows `S1`/`S2`, which graduate `W1-S1`/`W2-S1`, are re-issued in **REMEDIATION_v2** under `MDPF_SECHIST-W1-S1` and
`MDPF_SECHIST-W2-S1`. v1 is marked superseded and is never edited, because the file is append-only. Investigation `S1` (BDay(-1) as-of,
INERT to 11-27, site Z leg) then graduates under its own id when its time comes. CVO's act, no cell.

**2.2 FWD-1's name hop is a MDPF_SECCLASS defect, routed there, not a SECHIST cell.** The Positioning publisher reads
`etf-classifications.name` first (`etf_positioning_publisher.py:241-255`). I read the live rows: CSCO "Cisco Systems Inc/Delaware", BX
"Blackstone Inc", LNVGY "Lenovo Group LTD", all `legacy`. `clean_name()` does not strip a `/<state>` incorporation suffix. That is
MDPF_SECCLASS FWD-14's function, so the fix is a SECCLASS round-13 cell: strip `/<US state or jurisdiction>` suffixes, pin it by test, and
rewrite the affected rows under a pair. SECHIST FWD-1 is graded with whatever name that cell has landed by the acceptance morning. A
non-clean name on that morning fails FWD-1.

## 3. Round-2 enrichment list (one issuance, `2.0.0_SA_COO~H1`)

1. **FWD-1 acceptance read:** on the first unassisted scheduled pull (10-09 07:00 ET, or the next one), read the next-morning Positioning
   page for one security an Opal ETF bought the day before. The FWD-1 hops are class, sector, clean name and windows. Read only.
2. **FWD-7, the budget is visible:** the pull's run record prints the day's Bloomberg rows drawn against the bbg_budget remainder. The
   unit question in site Z ruling 31311 is site Z's; this cell only prints both prices beside the remainder.
3. **FWD-2, once site Z releases the card-A draw:** the backfill runs under the shared ledger, paced as approved, with a per-day draw
   line. Cut only after site Z's release; it is not issued now.

**Not in round 2:** FWD-4, 5, 6, 8 and 9 wait on round 2's FWD-1 read. Each round enriches the thread once the thread runs.
