# ETFS_RIVALS -- round 8 L8/L9 adjudication (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-05 ~17:00Z.

Round 8 is drained and applied:
- 11 of 11 orders are terminal;
- LIVE at b166e04416, with ledger etfs-rivalfunds-round8 CLOSED 6/6 @776a95c2da (packet msg 29682);
- this seat's read on the APPLIED plane: 5 of 5 rivalfunds Lambdas hold 37 of 37 files byte-equal to b166e04416, both
  schedules are ENABLED and unchanged, and the served page is r8b (15:33:50Z, 1,837,070 B).

**Scope:** every undispositioned investigation item at the drain (17: S17-S29, W4-S18, W5-S33, W7-S1, W2-S13), plus ui-5's
residue C-S28 and fc-1's J1. Grades: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R8_REVIEW_20261005.md`.

- C-S29, C-S30 and C-S31 dismiss 14 items. S20-S23 owe a disarm at the first real-Terminal D13 run.
- C-S32 through C-S36 graduate 5 items into `remediations/REMEDIATION_v8.Z.md`: S24, S25, S29, C-S35 and C-S36.
- In place: W1-S46 (REMEDIATION_v7) is REMEDIATED by dt-1 at the live pin (ai_client deadline timeout, sweep.REPUBLISH_RESERVE_S = 95).

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S29",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T17:00:00Z",
    "one_line": "Seven round-8 rows are built as recorded, ruled, or resolved: S17 (retracted by S19, CALL 12), S19, S18 (fixed by rp-1), W7-S1 (the bt-1 check amended to the calendar quarter), W2-S13 (the old test amended to the collapsed line), W4-S18 (FAILED/exit 3 on a controls-only day is the honest status) and W5-S33 (grader /5 -> /6 is a different rule, correctly versioned).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S17",
      "ETFS_RIVALS-Z-S19",
      "ETFS_RIVALS-Z-S18",
      "ETFS_RIVALS-Z-W7-S1",
      "ETFS_RIVALS-Z-W2-S13",
      "ETFS_RIVALS-Z-W4-S18",
      "ETFS_RIVALS-Z-W5-S33"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S17/S19: CRO~RV CALL 12 (RATIFIED) keeps the 0 -> 0 row in G5, and round-6 x-1.AC3 pins it. S18: TO-RIV-rp-1 (census price repair Z-S18) reads <status>complete</status> in round 8; the served r8b census reads 'Security prices: 756 of 763 arrived, 3 covered by the holding implied fallback, 4 missing or stale'. W7-S1: issuer amend 4b33f05d4b/ea8dbeba5e sets bt-1.AC1's QTD on 2026-10-02 to Q4. On the served page all 13 funds read 'Quarter to date (Q4 2026), 2026-10-01 to 2026-10-02, 2 trading days'. W2-S13: issuer amend ce381fd792. On the served page 12 data-empty-run lines read e.g. '2 windows, no trades (2026-09-25 to 2026-09-29)' with the notes inside, against 17 '(0 trades)' headings on the 10-02 page. W4-S18 and W5-S33 are worker notes on status and version semantics that the orders allow.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ETFS_RIVALS-Z-S17, S18, S19, W7-S1, W2-S13, W4-S18, W5-S33",
        "commits 4b33f05d4b, ea8dbeba5e, ce381fd792; task-orders/ETFS_RIVALS.TO-RIV-rp-1.census-price-repair.md <status>complete</status>",
        "this seat's rendered read of s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-05/index.html batch rv-publish-1005r8b, 2026-10-05 ~16:20-16:50Z"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Built, amended by the issuer, or ruled. Nothing is owed."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S30",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T17:00:00Z",
    "one_line": "S26 (the G4 daily-return-as-index ratio refusing 28 contribution windows) and S27 (SCHY's role change under the same map_version) are DISARMED as S28 claims, verified on the served page: 0 refused windows, and SCHY reads as a rival under G0 map-2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S26",
      "ETFS_RIVALS-Z-S27",
      "ETFS_RIVALS-Z-S28"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The 13:07Z manifest (batch ai-2026-10-05-a53411fb) refused 28 contribution windows (BASG ETFT GQGU PCLG PFOE TSEL WCMG x 4). The r8b manifest refuses 0, and it reads holding_contribution-20261005T144508Z-b8d441e1966c.parquet (14:45:09Z, the deploy's P1 run). G0 date=2026-10-05 holds map-1 (13:00:18Z, SCHY index_control) and map-2 (14:43:32Z, SCHY rival, map_version 2). The page picker reads 'SCHY' with no 'Benchmark' tag (13:07Z: 'SCHY Benchmark'), and the fund block carries data-role 'rival'.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ETFS_RIVALS-Z-S26, S27, S28",
        "both manifests at platinum/page/date=2026-10-05 (13:07:41Z ai- batch under revisions/20261005T153349Z, and r8b)",
        "s3://opal-data-etfs/rivalfunds/etfs/ G0 date=2026-10-05 map-1 and map-2 (this seat's fork read)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Disarm verified on the served page. comp-surprise still lists S26/S27 as ARMED because it does not apply S28's citing disarm; the disarm_owner (2.0.0_SA_COO~RV) may advance them in place."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S31",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T17:00:00Z",
    "one_line": "S20, S21, S22 and S23 (the Bloomberg leg's 2,000-row cap crash; Range.Value com_error; Value2 serial dates; first-part header merge) are fixed in lg-1 and gated off. They have NOT yet been exercised on the real Terminal: daily capacity has blocked every query since the fix.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S20",
      "ETFS_RIVALS-Z-S21",
      "ETFS_RIVALS-Z-S22",
      "ETFS_RIVALS-Z-S23"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "lg-1 (round 8, complete): f8124d0969 queries each index_control fund on its own under a 10,000-row cap, where an overflow is a per-name PARTIAL, never a traceback (W4-S18), and splits the gate into RIVALFUNDS_LEG_D12 / _D13. Amendment 2 (8fc847bfe7) reads Value2 and converts serial dates (collector_bloomberg.py:366-372, :462-467). Amendment 3 (6fe29f6bfc) makes _merge_parts match columns by name. The lg-1 proof instance grades AC1 arms (a)-(f) OK, with (e) pinning Value2 and (f) pinning the per-part header, on the fake COM only. The only 10-05 Terminal capture (batch-20261005T123303Z, 12:33:12Z) reads '#N/A Daily Capacity, request is blocked.' for all 9 funds.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ETFS_RIVALS-Z-S20, S21, S22, S23",
        "commits f8124d0969, 8fc847bfe7, 6fe29f6bfc; deliverables/0.9.0_WK_ETFS_RIVALS~4 lg-1 proof instance",
        "the 10-05 12:33Z Terminal capture sidecar (this seat's fork read)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The code remedy is built and the gate is off, so the hazard cannot fire. ABSENT is not EXERCISED: the disarm_owner (2.0.0_SA_COO~RV) owes the disarm in place at the first real-Terminal D13 run, read from that run's capture."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S32",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T17:00:00Z",
    "one_line": "S24 (the overnight backfill exhausted the Terminal's daily Bloomberg capacity) GRADUATES. Capacity was still blocked at 12:33Z, and the only guard is a seat's own hold: BACKFILL_D12_PLAN.md has no capacity clause and integrations/bloomberg/READ_HERE.md does not carry the limit.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RV",
    "adjudicates": [
      "ETFS_RIVALS-Z-S24"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "At 07:06Z every BQL query returned '#N/A Daily Capacity, request is blocked.'; the 12:33:12Z capture still reads the same for 9 of 9 funds. S25 widened it to refdata history: the OPAL_BBGTML models pull returned rc 50 ('DAPI no data'). No successful pull is measured after the block. Tomorrow's 07:00 ET vehicle depends on an unmeasured reset.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ETFS_RIVALS-Z-S24, S25",
        "deliverables/2.0.0_SA_COO~RV/round8/BACKFILL_D12_PLAN.md (no capacity or throttle clause)",
        "the 10-05 12:33Z capture sidecar"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S33",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T17:00:00Z",
    "one_line": "S25 GRADUATES on its unbuilt remedy 3: enrichment landed an ALL-EMPTY G4 for 2026-10-02 (601 rows, 0 prices, 0 GICS, 0 names) as the newest revision. Remedy 2 is done: the 10-02 G4 was restored at 12:46:17Z under a never-widen half. No round-8 order makes enrichment refuse an all-error G4.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S25"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The 10-02 G4 now reads market-20261005T124613Z-ea632b9bca87 (12:46:17Z, 46,943 B, byte-equal to the 10-04 revision) under NEVER_WIDEN_HALF_COO_G4_1002_REPUT.md @988544c80c; the empty 12:33Z revision (19,670 B) remains as the record. The models re-run (remedy 1) waits on capacity.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ETFS_RIVALS-Z-S25",
        "deliverables/2.0.0_SA_COO~RV/round8/NEVER_WIDEN_HALF_COO_G4_1002_REPUT.md @988544c80c"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S34",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T17:00:00Z",
    "one_line": "S29 GRADUATES as a CTO call: D12 Step B is not purely additive at G5. The import chain re-derives every fund's trade schedule on 189 dates with current code, and Step B is held at CTO~Z's stop condition (msg 29594).",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S29"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "G1 is additive (189/189 dates), but the chain's G5 rebuild changes every other fund's served Jan-Sep G5, which was built with older code. The row names two options: (A) accept a G5 replay of all funds (wider than the word); (B) a round-9 cell in which the trade schedule rebuilds only the named funds.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ETFS_RIVALS-Z-S29 (6a9aa4fa9e)"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S35",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T17:00:00Z",
    "one_line": "fc-1 J1 NOT MET on the AI text: on the served r8b page, 395 mentions of 43 securities that have a modal are plain text in the AI accounts and AI cards, against 253 linked. The rankings (772), the trend (422) and the trade log (121) are fully linked. 1,568 buttons open 441 dialogs with 0 mismatches. The page is 1,837,070 B, under the 2,097,152 B cap.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "fc-1 J1: on the served page after the deploy, clicking any security name anywhere opens its modal, and the page loads within the gateway cap; Andrew 2026-10-05: 'anytime a stock/ticker is mentioned, it should be clickable to the modal'.",
    "world_is": "Headless Chromium on the served index.html, counting text nodes outside button[data-sec] that equal a dialog heading as a whole word. AI dialogs P 173 + LI 167; AI face leads 49; rf-sec spans 6 (Taiwan Semiconductor Manufacturing Co Ltd, the name 2330_TT_Equity and TSM_US_Equity share, left unlinked as ambiguous). Example, TXUE's face lead: 'added Enel SpA at $1.6 million, Siemens Energy AG at $1.2 million, [E.On Se] at $1.2 million, AstraZeneca PLC ...' -- only E.On Se is a button. Four names are linked in one account and plain in another (Broadcom Inc, GE Vernova Inc, General Electric Co, Netflix Inc). Outside fc-1's four surfaces, the latest-holdings tables carry 334 plain mentions (243 names). Control: the 10-02 page has 0 data-sec buttons. A real click in TXUE opens rf-s-ATD_CN_Equity.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders/ETFS_RIVALS.TO-RIV-fc-1.every-security-opens-its-modal.md J1 and section 1 (AC2: link every whole-word occurrence in the AI text)",
        "this seat's playwright measure over platinum/page/date=2026-10-05/index.html (r8b) and date=2026-10-02/index.html"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S36",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T17:00:00Z",
    "one_line": "ui-5's residue (C-S28) GRADUATES, because no round-8 cell carried it: round 8 was cut before the 13:30Z grade. 22 holdings are still named by their Bloomberg ticker form on the r8b page (e.g. 'ATD CN Equity', 'MSCI US Equity'), now as clickable buttons whose modal headings carry the same form.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-C-S28"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "C-S28 measured 22 of 22 carried ticker-named keys unchanged on the 13:07Z page. The r8b modal for ATD_CN_Equity is headed 'ATD CN Equity'. Round 8's 11 orders (dt-1, an-1, rw-1, rp-1, lg-1, gc-1, hc-1, bt-1, rn-1, fc-1, su-1) carry no LONG_COMP_NAME / security-name cell.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudications/ADJUDICATION_v7.Z.md ETFS_RIVALS-Z-C-S28 (@0fe137ee28)",
        "this seat's r8b click control (rf-s-ATD_CN_Equity heading)"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV
