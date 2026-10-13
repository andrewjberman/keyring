# ADVI_BDPRCE -- round 1 L8/L9 adjudication, the channel's first compile (dell1)

<sweep_watermark>2026-10-13T15:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T15:55:00Z. L8 packet: 2.0.0_SA_COO~K1 msg 5090,
`org/missions/D8/ADVI/ADVI_BDPRCE/deliverables/2.0.0_SA_COO~K1/round1/R1_CLOSE.md` @c5c796789b (blob e986a4984b, verified).
4 of 4 orders complete, all LOCAL, nothing served moved. 27 investigation rows swept (27 of 27; no prior adjudication): 7 ARMED graduated ARMED, 8 INERT graduated,
12 dismissed. No BLOCKING row; every ARMED row is dispositioned with its disarm owner and cell.

```json
[
  {
    "id": "ADVI_BDPRCE-D1-C-S1",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "Round-1 L8/L9 read (all four orders LOCAL, no JUDGMENT criterion): HOLDS on this seat's own runs from the merged tree (box/dell1 ad4c5ff765). BP-a-1 'WRITERS record ok writers=6 unidentified=0 versions_read=665'; BP-a-2 'TRACE SELFTEST: OK 7 arms' and 'TRACE record ok source=transaction_observed trades=4 match=true'; BP-a-3 'GAP record ok served=1657 equal=1148 explained=429 unexplained=64'; BP-a-4 'THREAD record ok ... trades=4 equal=true'. Scope: three worker worktrees are removed, so scope was read from each merge's file list (f565ce0410, fead753225, 1a44a44918, ff308443a4): every path is the worker's own deliverable folder or the channel, plus the order's own file (its status line). The thread, re-read by this seat: z08334146/detail.json VersionId ZCjWpzPR1n2uZl849onevhS.pIvSQhVA, data_as_of 2026-10-09, EXXONMOBIL HOLDINGS CORP COM SHS current_price 168.94, ticker null; silver/transactions/2026-10-09.parquet 4 rows, 1 distinct transaction_id 745369343, median |market_value|/|units| = 168.94, equal to served. Against the signed PRD v1.0 (half d5ab58f8d868): the thread shows one traced price (FWD-1's mechanism), but it is not FWD-1 REALIZED as worded until the exemplar is a genuinely untickered holding (W4-S9) and the served tie (W4-S5) is ruled; FWD-1's grade is the CTO's. Nothing served moved. round-close-check --round 1: 4 of 4, MAY-CLOSE.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Round-1 L8/L9 read (all four orders LOCAL, no JUDGMENT criterion): HOLDS on this seat's own runs from the merged tree (box/dell1 ad4c5ff765). BP-a-1 'WRITERS record ok writers=6 unidentified=0 versions_read=665'; BP-a-2 'TRACE SELFTEST: OK 7 arms' and 'TRACE record ok source=transaction_observed trades=4 match=true'; BP-a-3 'GAP record ok served=1657 equal=1148 explained=429 unexplained=64'; BP-a-4 'THREAD record ok ... trades=4 equal=true'. Scope: three worker worktrees are removed, so scope was read from each merge's file list (f565ce0410, fead753225, 1a44a44918, ff308443a4): every path is the worker's own deliverable folder or the channel, plus the order's own file (its status line). The thread, re-read by this seat: z08334146/detail.json VersionId ZCjWpzPR1n2uZl849onevhS.pIvSQhVA, data_as_of 2026-10-09, EXXONMOBIL HOLDINGS CORP COM SHS current_price 168.94, ticker null; silver/transactions/2026-10-09.parquet 4 rows, 1 distinct transaction_id 745369343, median |market_value|/|units| = 168.94, equal to served. Against the signed PRD v1.0 (half d5ab58f8d868): the thread shows one traced price (FWD-1's mechanism), but it is not FWD-1 REALIZED as worded until the exemplar is a genuinely untickered holding (W4-S9) and the served tie (W4-S5) is ruled; FWD-1's grade is the CTO's. Nothing served moved. round-close-check --round 1: 4 of 4, MAY-CLOSE.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~K1/round1/checks/r1_checks.py writers|trace|gap|thread on the merged deliverables, run by 3.0.0_SA_CVO 2026-10-13T15:4xZ (outputs as quoted)",
        "deliverables/0.9.0_WK_ADVI_BDPRCE~2/trace_price.py --self-test: TRACE SELFTEST: OK 7 arms",
        "3.0.0_SA_CVO boto3 read of the served detail object at the named VersionId and of opal-data-bd silver/transactions/2026-10-09.parquet",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project ADVI_BDPRCE --round 1: verdict=MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Round-1 L8/L9 read (all four orders LOCAL, no JUDGMENT criterion): HOLDS on this seat's own runs from the merged tree (box/dell1 ad4c5ff765). BP-a-1 'WRITERS record ok writers=6 unidentified=0 versions_read=665'; BP-a-2 'TRACE SELFTEST: OK 7 arms' and 'TRACE record ok source=transaction_observed trades=4 match=true'; BP-a-3 'GAP record ok served=1657 equal=1148 explained=429 unexplained=64'; BP-a-4 'THREAD record ok ... trades=4 equal=true'. Scope: three worker worktrees are removed, so scope was read from each merge's file list (f565ce0410, fead753225, 1a44a44918, ff308443a4): every path is the worker's own deliverable folder or the channel, plus the order's own file (its status line). The thread, re-read by this seat: z08334146/detail.json VersionId ZCjWpzPR1n2uZl849onevhS.pIvSQhVA, data_as_of 2026-10-09, EXXONMOBIL HOLDINGS CORP COM SHS current_price 168.94, ticker null; silver/transactions/2026-10-09.parquet 4 rows, 1 distinct transaction_id 745369343, median |market_value|/|units| = 168.94, equal to served. Against the signed PRD v1.0 (half d5ab58f8d868): the thread shows one traced price (FWD-1's mechanism), but it is not FWD-1 REALIZED as worded until the exemplar is a genuinely untickered holding (W4-S9) and the served tie (W4-S5) is ruled; FWD-1's grade is the CTO's. Nothing served moved. round-close-check --round 1: 4 of 4, MAY-CLOSE."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S2",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "The seven ARMED rows graduate ARMED to REMEDIATION_v1, disarm owner 2.0.0_SA_COO~K1, each carried to the cell that disarms it (packet section 4). None is disarmed in round 1: every disarm is a served price or lot change, which moves only under Andrew's review of a named before/after list (FWD-7). Two are re-read by this seat: W2-S2's repeated-id class (the thread asset: 4 rows, 1 transaction_id) and W4-S8 (73 x 168.94 = 12,332.62 against served 5,000.79). The others rest on the workers' committed evidence, not re-read here. High signal against Andrew's constraint: W3-S4 (cash-dividend rows set a per-unit price of 1.0 and dominate the median) and W4-S2 (61 of 586 sampled untickered lots priced off no canonical row) are served prices whose source is not the written rule.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W2-S2",
      "ADVI_BDPRCE-D1-W2-S4",
      "ADVI_BDPRCE-D1-W1-S3",
      "ADVI_BDPRCE-D1-W3-S3",
      "ADVI_BDPRCE-D1-W3-S4",
      "ADVI_BDPRCE-D1-W4-S2",
      "ADVI_BDPRCE-D1-W4-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "The seven ARMED rows graduate ARMED to REMEDIATION_v1, disarm owner 2.0.0_SA_COO~K1, each carried to the cell that disarms it (packet section 4). None is disarmed in round 1: every disarm is a served price or lot change, which moves only under Andrew's review of a named before/after list (FWD-7). Two are re-read by this seat: W2-S2's repeated-id class (the thread asset: 4 rows, 1 transaction_id) and W4-S8 (73 x 168.94 = 12,332.62 against served 5,000.79). The others rest on the workers' committed evidence, not re-read here. High signal against Andrew's constraint: W3-S4 (cash-dividend rows set a per-unit price of 1.0 and dominate the median) and W4-S2 (61 of 586 sampled untickered lots priced off no canonical row) are served prices whose source is not the written rule.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_BDPRCE-D1-W2-S2, ADVI_BDPRCE-D1-W2-S4, ADVI_BDPRCE-D1-W1-S3, ADVI_BDPRCE-D1-W3-S3, ADVI_BDPRCE-D1-W3-S4, ADVI_BDPRCE-D1-W4-S2, ADVI_BDPRCE-D1-W4-S8",
        "round1/R1_CLOSE.md @c5c796789b section 4"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v1.md (ARMED)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S3",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "Eight INERT rows graduate to REMEDIATION_v1 because work is owed: the missing daily price files on six trading days (W3-S2, all Monday or Tuesday); the served detail objects one trading day behind T-1 (W4-S1, confirmed by lib/trading_calendar.py: 2026-10-12 is a trading day) and the far-older objects (W4-S10); the same-date daily-versus-canonical disagreements (W2-S3, W4-S3, W4-S5), the S33 re-read for the CTO; the trace instrument reading the daily row while the served lot reads canonical (W4-S6, which FWD-3's DEC-10 grade depends on); and the ticker-mapping gap (W4-S9). Price-estimate signal: W2-S3 (linear_interpolation in canonical) and W4-S5 (carry_forward in the daily file) are estimated prices on a same-date served row, the class this seat's L4-R review carried as a note against Andrew's 'any estimation is highly risky'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W3-S2",
      "ADVI_BDPRCE-D1-W4-S1",
      "ADVI_BDPRCE-D1-W4-S10",
      "ADVI_BDPRCE-D1-W2-S3",
      "ADVI_BDPRCE-D1-W4-S3",
      "ADVI_BDPRCE-D1-W4-S5",
      "ADVI_BDPRCE-D1-W4-S6",
      "ADVI_BDPRCE-D1-W4-S9"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "Eight INERT rows graduate to REMEDIATION_v1 because work is owed: the missing daily price files on six trading days (W3-S2, all Monday or Tuesday); the served detail objects one trading day behind T-1 (W4-S1, confirmed by lib/trading_calendar.py: 2026-10-12 is a trading day) and the far-older objects (W4-S10); the same-date daily-versus-canonical disagreements (W2-S3, W4-S3, W4-S5), the S33 re-read for the CTO; the trace instrument reading the daily row while the served lot reads canonical (W4-S6, which FWD-3's DEC-10 grade depends on); and the ticker-mapping gap (W4-S9). Price-estimate signal: W2-S3 (linear_interpolation in canonical) and W4-S5 (carry_forward in the daily file) are estimated prices on a same-date served row, the class this seat's L4-R review carried as a note against Andrew's 'any estimation is highly risky'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ADVI_BDPRCE-D1-W3-S2, ADVI_BDPRCE-D1-W4-S1, ADVI_BDPRCE-D1-W4-S10, ADVI_BDPRCE-D1-W2-S3, ADVI_BDPRCE-D1-W4-S3, ADVI_BDPRCE-D1-W4-S5, ADVI_BDPRCE-D1-W4-S6, ADVI_BDPRCE-D1-W4-S9",
        "3.0.0_SA_CVO lib/trading_calendar.is_trading_day on 2026-10-12 and the six W3-S2 dates: all trading days"
      ]
    },
    "disposition": "GRADUATED",
    "notes": "Graduated to remediations/REMEDIATION_v1.md (INERT)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S4",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W2-S1 dismissed: the instrument walked back to the newest file carrying a transaction_observed row; the order's wording assumed the newest file had one. An order-wording point, the instrument behaved correctly.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W2-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W2-S1 dismissed: the instrument walked back to the newest file carrying a transaction_observed row; the order's wording assumed the newest file had one. An order-wording point, the instrument behaved correctly.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W2-S1",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W2-S1 dismissed: the instrument walked back to the newest file carrying a transaction_observed row; the order's wording assumed the newest file had one. An order-wording point, the instrument behaved correctly."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S5",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W2-S5 dismissed: a row-id grammar mismatch between the order and the surprise-row gate (dell1 rows need the D1 coordinate); the issuer's amendment f3643b94f9 fixed the template.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W2-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W2-S5 dismissed: a row-id grammar mismatch between the order and the surprise-row gate (dell1 rows need the D1 coordinate); the issuer's amendment f3643b94f9 fixed the template.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W2-S5",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W2-S5 dismissed: a row-id grammar mismatch between the order and the surprise-row gate (dell1 rows need the D1 coordinate); the issuer's amendment f3643b94f9 fixed the template."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S6",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W1-S1 dismissed: an identification, not a hazard: the brief's 'emergency rebuild' is the daily S_00 stage plus its chained inject (25 runs in 7 days). It is carried in WRITERS.json, which this seat's run reads 6 writers, 0 unidentified.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W1-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W1-S1 dismissed: an identification, not a hazard: the brief's 'emergency rebuild' is the daily S_00 stage plus its chained inject (25 runs in 7 days). It is carried in WRITERS.json, which this seat's run reads 6 writers, 0 unidentified.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W1-S1",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W1-S1 dismissed: an identification, not a hazard: the brief's 'emergency rebuild' is the daily S_00 stage plus its chained inject (25 runs in 7 days). It is carried in WRITERS.json, which this seat's run reads 6 writers, 0 unidentified."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S7",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W1-S2 dismissed: a co-location fact (the 49F chain dispatcher and the BD gold runner share EC2 i-01003b035d2988dfb), recorded for any FWD-7 blast radius; it moves no served value.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W1-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W1-S2 dismissed: a co-location fact (the 49F chain dispatcher and the BD gold runner share EC2 i-01003b035d2988dfb), recorded for any FWD-7 blast radius; it moves no served value.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W1-S2",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W1-S2 dismissed: a co-location fact (the 49F chain dispatcher and the BD gold runner share EC2 i-01003b035d2988dfb), recorded for any FWD-7 blast radius; it moves no served value."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S8",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W1-S4 dismissed: brief line-number drift (the daily put is :666, not :639) and the silver script's 0 runs, both recorded in WRITERS.md; no served value depends on the brief's line numbers.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W1-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W1-S4 dismissed: brief line-number drift (the daily put is :666, not :639) and the silver script's 0 runs, both recorded in WRITERS.md; no served value depends on the brief's line numbers.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W1-S4",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W1-S4 dismissed: brief line-number drift (the daily put is :666, not :639) and the silver script's 0 runs, both recorded in WRITERS.md; no served value depends on the brief's line numbers."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S9",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W1-S5 dismissed: three trigger attributions of S_00 runs do not close, but every WRITER is identified (this seat's run: writers=6 unidentified=0); run attribution is not writer identity.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W1-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W1-S5 dismissed: three trigger attributions of S_00 runs do not close, but every WRITER is identified (this seat's run: writers=6 unidentified=0); run attribution is not writer identity.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W1-S5",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W1-S5 dismissed: three trigger attributions of S_00 runs do not close, but every WRITER is identified (this seat's run: writers=6 unidentified=0); run attribution is not writer identity."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S10",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W1-S6 dismissed: the channel directory did not exist at the cut and the worker created it, as the first worker on a new project must.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W1-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W1-S6 dismissed: the channel directory did not exist at the cut and the worker created it, as the first worker on a new project must.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W1-S6",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W1-S6 dismissed: the channel directory did not exist at the cut and the worker created it, as the first worker on a new project must."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S11",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W1-S7 dismissed: the same row-id coordinate point as W2-S5, fixed by the issuer's amendment f3643b94f9.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W1-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W1-S7 dismissed: the same row-id coordinate point as W2-S5, fixed by the issuer's amendment f3643b94f9.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W1-S7",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W1-S7 dismissed: the same row-id coordinate point as W2-S5, fixed by the issuer's amendment f3643b94f9."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S12",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W3-S1 dismissed: the denominator is corrected on the record: 1,657 served rows in the window, not the brief's 1,610 (this seat's run of the gap check reads served=1657). The figure moved, not a hazard.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W3-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W3-S1 dismissed: the denominator is corrected on the record: 1,657 served rows in the window, not the brief's 1,610 (this seat's run of the gap check reads served=1657). The figure moved, not a hazard.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W3-S1",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W3-S1 dismissed: the denominator is corrected on the record: 1,657 served rows in the window, not the brief's 1,610 (this seat's run of the gap check reads served=1657). The figure moved, not a hazard."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S13",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W3-S5 dismissed: the same channel-file and row-coordinate point as W1-S6 and W1-S7.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W3-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W3-S5 dismissed: the same channel-file and row-coordinate point as W1-S6 and W1-S7.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W3-S5",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W3-S5 dismissed: the same channel-file and row-coordinate point as W1-S6 and W1-S7."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S14",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W4-S4 dismissed: the counts are a 26-object sample, not a census, and the record says so; the census is the remedy of W4-S2 (read-only, all 3,509 objects).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W4-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W4-S4 dismissed: the counts are a 26-object sample, not a census, and the record says so; the census is the remedy of W4-S2 (read-only, all 3,509 objects).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W4-S4",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W4-S4 dismissed: the counts are a 26-object sample, not a census, and the record says so; the census is the remedy of W4-S2 (read-only, all 3,509 objects)."
  },
  {
    "id": "ADVI_BDPRCE-D1-C-S15",
    "project": "ADVI_BDPRCE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T15:55:00Z",
    "one_line": "D1-W4-S7 dismissed: the thread asset has one trade id on four rows, so it cannot separate FWD-4's repeated-row weighting; FWD-4's own exercise is C6, not the thread.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_BDPRCE-D1-W4-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "D1-W4-S7 dismissed: the thread asset has one trade id on four rows, so it cannot separate FWD-4's repeated-row weighting; FWD-4's own exercise is C6, not the thread.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_BDPRCE-D1-W4-S7",
        "round1/R1_CLOSE.md @c5c796789b"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W4-S7 dismissed: the thread asset has one trade id on four rows, so it cannot separate FWD-4's repeated-row weighting; FWD-4's own exercise is C6, not the thread."
  }
]
```
