# IRPT_BCKEND: CVO adjudication, round 2 (workstream ~PE, 49 Financial's lost account across Schwab's files)

<sweep_watermark>2026-10-15T13:03Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T13:03Z, on msg 8288 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_2_PE_DRAIN_END_20261015.md` @d989c30f42). One order, IB-pr-575 (risk SERVED, read-only), complete, merged @23eff77fbb (worker record, criteria output, proof instance and the channel only), issued @f724242ca0. Re-run here at HEAD: IB214-1-AC1..AC3 PASS (exit 0). `round-close-check --round 2 --workstream "~PE"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE.

**The fact_trn leg, measured here** (read-only `list` + `get-object` of `s3://opal-data-assets/schwab/08335338/silver/fact_trn/`; counts only, no id printed or recorded). The listing holds 197 partitions from 2026-01-02 to 2026-10-14. Over the 52 trading-day partitions from 2026-08-03 to 2026-10-14:
- **Daily size is highly variable:** median 3,407 rows, p10 1,028, minimum 509 (2026-10-12). Neighbours: 10-01 10,996; 10-02 1,388; 10-05 16,557; 10-06 28,807; 10-07 1,407; 10-08 19,490; 10-09 5,561; 10-12 **509**; 10-13 11,906; 10-14 9,777.
- **10-12 is the smallest of 52**, but small days recur. Four trading days fall under 25 percent of the median (08-26 813, 08-27 559, 09-09 764, 10-12 509). So "509 against 11,906" overstates the anomaly: 11,906 is not a typical day, it is 3.5x the median. 2026-10-12 is Columbus Day, a Federal Reserve holiday when banks and DTC are closed but NYSE trades; that is a plausible reason for a thin transaction file (inferred, not read from Schwab). Truncation is therefore NOT shown, and completeness is NOT shown either.
- **The lost account in fact_trn:** it has rows on the large days through 2026-10-08 (for example 6 rows on 10-08) and **0 rows on 10-09, 10-12, 10-13 and 10-14**, including the large 10-13 day where its pattern would usually show rows. Positive control: the busiest account of the 10-13 partition, present in the 10-13 balance file, has 5,500 rows across the window.

**Does "closed" hold without the fact_trn leg? Only as rule (a)'s definition, not as a fact.** By the CTO's rule (a) the account is closed_at_source because it has no positions on the last two days: it is absent from `dim_balance` and has 0 `dim_position` rows on 10-13 and 10-14 (worker-measured; the dim_balance half re-measured here in v116). But a real closure of an account holding 20 positions moves those positions out by transactions. No closing or transfer transaction exists in ANY partition from 10-09 to 10-14. The only day that could hide one, 10-12, is the thinnest partition in 52 trading days. Absence of a closing transaction is ABSENT, not EXERCISED-AGAINST. The read cannot tell a closure from a feed omission (an account dropped from Schwab's files while still live). **The closure is UNPROVEN.**

**IB-pr-576 (~PG, status pending).** As cut, it does not rest on fact_trn. It exempts on "no positions in BOTH tables (positions, balance) on the candidate date AND the prior trading day, both partitions complete (at least 95 percent of the prior day)". That 95 percent condition fits dim_balance (7,626 to 7,664 across five days). It would be meaningless or refusing if ever applied to fact_trn, whose day-over-day swing is 10x. The exemption is therefore sound as LOGIC, but its name and the manifest reason assert "closed", which the evidence does not establish. **Recommendation (P1, to the CTO):** do not let the build or its never-widen pair record "closed" as a measured fact. The manifest reason should read absent-at-source over two complete days, with the closure itself `inferred`. The pair's blast radius must cover the other branch: if the account is live at Schwab (a feed omission), the exemption drops a live account from 49 Financial's served holdings until it reappears. Confirming the account's state with the custodian, through the Schwab ingest owner (`schwab_conversion.py`, the AE PartnerETL seat), is the act that turns inferred into measured.

**Rows and owners.** The 509/11,906 caveat is carried by `D2-S198` (ARMED, owner `2.0.0_SA_COO~P2`). The worker row that measured it, `D2-W418-S2`, reads INERT with no owner, although the packet says it "stays ARMED, owner me". The live carrier is S198, so the hazard has an owner; the packet's description of W418-S2 is inaccurate.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S25",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T13:03:00Z",
  "one_line": "Round 2 ~PE. CLOSURE UNPROVEN. Measured here over 52 trading-day fact_trn partitions (2026-08-03..10-14): median 3,407 rows, 10-12 the minimum at 509 (Columbus Day, inferred reason), small days recur (4 under 25% of median), so 11,906 is not typical and truncation is not shown. The lost account has fact_trn rows through 10-08 and none 10-09..10-14, with no closing or transfer row anywhere; a 20-position account vanished with no transaction, which cannot tell closure from a feed omission. Rule (a) holds by definition (no positions two days), not as a fact. IB-pr-576 rests on positions + balance (95% completeness, fits dim_balance), not fact_trn: sound as logic, but its manifest must not record 'closed' as measured, and its pair must cover a live account dropped by omission. IB214-1-AC1..AC3 PASS; read-only. Dismissed (2): D2-W418-S1 (BLOCKING, INERT; grant widened), D2-W418-S3 (reading). Held: D2-S198 (ARMED, ~P2, carries the caveat; W418-S2 itself reads INERT, no owner, contrary to the packet).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W418-S1",
   "IRPT_BCKEND-D2-W418-S3"
  ],
  "spec_asserts": "Evidence law (CLAUDE.md rule 22, annex): ABSENT != EXERCISED-AGAINST; section 4: a value carries its claim; never-widen (section 5): a sign-off covers BOTH branches of the act's outcome.",
  "world_is": "49 Financial's lost account is absent from Schwab's balance, position and transaction files from 10-13 (transactions from 10-09). Whether it closed or was dropped from the feed is not known; no closing transaction is in the data. The exemption build IB-pr-576 is pending and does not depend on fact_trn, but it labels the case 'closed'.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T13:0xZ of the invocations in IB-pr-575: IB214-1-AC1..3 PASS, exit 0",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 2 --workstream ~PE: orders=1 proof_ok=1 judgment=0 verdict=MAY-CLOSE",
    "scratch pe2_trn.py, read-only, s3://opal-data-assets/schwab/08335338/silver/fact_trn/: 197 partitions listed 2026-01-02..2026-10-14; 52 trading-day partitions 08-03..10-14, median 3,407, p10 1,028, min 509 (10-12); under 25% of median: 08-26 813, 08-27 559, 09-09 764, 10-12 509; lost account rows 0 on 10-09, 10-12, 10-13, 10-14, 6 on 10-08; positive control 5,500 rows",
    "lib/trading_calendar.py: 2026-10-12 a trading day (Monday)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~418/IB214-1_49f_presence_read.json: dim_balance 7,626..7,664; dim_position 20/0/0; fact_trn 0/0/0; classification closed_at_source",
    "org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-576...md line 1, 32, 34 (positions and balance, 95 percent completeness)",
    "investigation rows D2-W418-S1..S3 (S2 INERT, owner None), D2-S198 (ARMED, 2.0.0_SA_COO~P2)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_2_PE_DRAIN_END_20261015.md @d989c30f42 (msg 8288)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An issuer grant defect fixed and a reading. The closure question is not dismissed: it is held on S198 with ~P2 and named for the CTO before IB-pr-576's pair is signed."
 }
]
```
