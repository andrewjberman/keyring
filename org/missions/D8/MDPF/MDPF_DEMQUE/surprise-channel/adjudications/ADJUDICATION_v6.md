# MDPF_DEMQUE -- round 6 L8/L9 adjudication

<sweep_watermark>2026-10-09T13:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T13:15:00Z. L8 packet: 2.0.0_SA_COO~Q1 msg 2456, org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND6_REAL_RUN.md @d53f6aaa9a. 3 of 3 complete, MAY-CLOSE. 3 rows: D1-W18-S1 dismissed; D1-W17-S1 and D1-S4 graduated INERT to `remediations/REMEDIATION_v5.md`. REMEDIATION_v4 D1-W13-S1 REMEDIATED.

**L9:** FWD-4 EXERCISED ON_TIME; FWD-3's history allowance is negative (row D1-W17-S1).

```json
[
  {
    "id": "MDPF_DEMQUE-C-S12",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T13:15:00Z",
    "one_line": "Round 6 L9: no judgment owed; 3 of 3 complete, 83 tests (this seat's run: 83 passed). FWD-4 EXERCISED: the pre-flight request was quoted (1 cell, finish 2026-10-09, quote frozen @70379bb41d) and drawn ON_TIME. FWD-3: the history reserve is now seeded from the ledger (7322 = 5858 x 1.25 >= the measured 5858), but the history ceiling is the same held 5858 floor, so the history allowance per day is negative (-1464) and history quotes read finish_date null (this seat's quote run on DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS: 15,720 cells, allowance_gap 'history allowance per day not positive (ceiling 5858, reserve 7322)'). TR column built (TRCOL-OK, both guards); its first served write is the 2026-10-10 02:30Z draw, read at round 7. REMEDIATION_v4 D1-W13-S1 is REMEDIATED (reserve now at or above the measured draw); its consequence travels on D1-W17-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "Round 6 L9: no judgment owed; 3 of 3 complete, 83 tests (this seat's run: 83 passed). FWD-4 EXERCISED: the pre-flight request was quoted (1 cell, finish 2026-10-09, quote frozen @70379bb41d) and drawn ON_TIME. FWD-3: the history reserve is now seeded from the ledger (7322 = 5858 x 1.25 >= the measured 5858), but the history ceiling is the same held 5858 floor, so the history allowance per day is negative (-1464) and history quotes read finish_date null (this seat's quote run on DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS: 15,720 cells, allowance_gap 'history allowance per day not positive (ceiling 5858, reserve 7322)'). TR column built (TRCOL-OK, both guards); its first served write is the 2026-10-10 02:30Z draw, read at round 7. REMEDIATION_v4 D1-W13-S1 is REMEDIATED (reserve now at or above the measured draw); its consequence travels on D1-W17-S1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran bbg_quote.py --quote requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json: finish_date null, allowance_gap as quoted",
        "3.0.0_SA_CVO read data/mdpf/scripts/demque/bbg_allowance.json: history ceiling 5858, reserve 7322; bql 2,920,000/1,875; reference 52/25",
        "3.0.0_SA_CVO ran pytest data/mdpf/scripts/demque -q: 83 passed",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND6_REAL_RUN.md @d53f6aaa9a"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 record, not a hazard."
  },
  {
    "id": "MDPF_DEMQUE-C-S13",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T13:15:00Z",
    "one_line": "D1-W18-S1 dismissed: resolved in-round by AMENDMENT @154f28a514, which granted test_demque_store.py (three original columns first, then the four TR columns); the demque suite reads 83 passed on this seat's run.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W18-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "D1-W18-S1 dismissed: resolved in-round by AMENDMENT @154f28a514, which granted test_demque_store.py (three original columns first, then the four TR columns); the demque suite reads 83 passed on this seat's run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log 154f28a514",
        "3.0.0_SA_CVO pytest data/mdpf/scripts/demque: 83 passed",
        "investigation row MDPF_DEMQUE-D1-W18-S1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D1-W18-S1 dismissed: resolved in-round by AMENDMENT @154f28a514, which granted test_demque_store.py (three original columns first, then the four TR columns); the demque suite reads 83 passed on this seat's run."
  }
]
```
