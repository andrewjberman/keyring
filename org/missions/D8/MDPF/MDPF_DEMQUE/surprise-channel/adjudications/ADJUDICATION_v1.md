# MDPF_DEMQUE -- round 1 L8/L9 adjudication

<sweep_watermark>2026-10-08T23:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-08T23:55:00Z. L8 packet: 2.0.0_SA_COO~Q1 msg 1259 -- 5 of 5 orders complete and merged (last @921d20bcb6), real run
`org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/FWD1_REAL_RUN_R1.md`. 4 rows swept: 1 dismissed (S1), 3 graduated INERT to
`remediations/REMEDIATION_v1.md` (D1-W3-S1, D1-W4-S1, D1-W4-S2). No ARMED or BLOCKING row.

**L9 -- DQ1-t5-AC2 (judgment): MET** on this seat's own reads of the code and live AWS (row C-S1).

**L9 -- FWD-1: NOT REALIZED.** The issuer's real run on AMLP (CUSIP 00162Q866): quote, pull, draw and lock work (lock `measured`, 100 of
108 trade-price observations). Hop 5 lands nothing (the CUSIP is not in the transactions object the lander reads). Hop 6 has no consumer
(D1-W4-S2). The second break is an ENDPOINT-level call for 1.0.0_SA_CTO~DELL1, not a round-2 cell.

```json
[
  {
    "id": "MDPF_DEMQUE-C-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T23:55:00Z",
    "one_line": "DQ1-t5-AC2 MET: each of Q1-Q5 in the hop-6 trace is correct against the code and the live schedule, on this seat's own reads; the VERDICT BUILD-NEEDED follows from them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment criterion graded by a seat that did none of the work.",
    "world_is": "DQ1-t5-AC2 MET: each of Q1-Q5 in the hop-6 trace is correct against the code and the live schedule, on this seat's own reads; the VERDICT BUILD-NEEDED follows from them.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Q1: aws scheduler get-schedule cot-bd-session-daily-et -> cron(30 7 * * ? *) America/New_York ENABLED; aws events list-targets-by-rule cot-silver-complete -> cot-bd-session-trigger {\"mode\":\"gold-run\"}; lambda_function.py:328-329 gold-run -> _handle_ssm_dispatch(GOLD_RUN_SSM_DOCUMENT)",
        "Q2: aws ssm get-document opal-cot-gold-run -> version 10, run list A_00..D_04 (18 scripts), no S_00, no canonical_prices; gold_dispatch.sh:1069-1071 silver prep only on chain full",
        "Q3: build_canonical_prices_v2.py:283 and :298 bare s3.get_object, called at :484-485 before any write; :647-651 except -> FATAL -> return 1; head-object silver/historical_prices.parquet 404, config/ticker_lookup.json 404, silver/prices/canonical_prices.parquet 2026-06-09T20:42:16Z",
        "Q4: cottonwood/layout.ts:47 clientDetailHandler 'lambda'; advisor-intelligence.ts:1033-1039 /api/scoped/partners/books/relationship/{id}/platinum-summary; opal-partners-data lambda_function.py:1436 platinum/clients/{key}/summary.json; B_00.canonical_holdings.py:117-151 price = mv / units from silver/holdings; comp-find canonical_prices portal/src -> 0 hits of 1368 files",
        "Q5: B_00:1095-1100 snapshot branch returns before load_canonical_prices() at :1124; A_03:664 reads silver/unrealized (404 live) before :677; gold-run log 20261008-113337: 'Holdings snapshot present (85 date(s))' and 'No unrealized data ... skipping buy'",
        "graded artifact: org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~4/FWD1_HOP6_PRICES_TO_PAGE_TRACE.md (TO MDPF_DEMQUE.TO-DQ-t5, assignee 0.9.0_WK_MDPF_DEMQUE~4, issuer 2.0.0_SA_COO~Q1)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard: judgment criterion DQ1-t5-AC2 of MDPF_DEMQUE.TO-DQ-t5 is graded MET by a seat that did none of the work."
  },
  {
    "id": "MDPF_DEMQUE-C-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-08T23:55:00Z",
    "one_line": "S1 (OBSERVATION/INERT) dismissed: the record is now readable on dell1 -- @86d85ab4a5 resolves (git cat-file -t = commit) on origin/box/laptop; it is not yet on CLOUD, and round 1 did not depend on it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment criterion graded by a seat that did none of the work.",
    "world_is": "Commit 86d85ab4a5 is in this clone (origin/box/laptop); origin/CLOUD a0b75e8332 still has no 230xZ_SITEZ path. The round-2 cut reads the record from box/laptop or from CLOUD after the laptop integrates.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "2026-10-08T23:54Z: git cat-file -t 86d85ab4a5 -> commit; git branch -a --contains 86d85ab4a5 -> remotes/origin/box/laptop",
        "git ls-tree -r --name-only origin/CLOUD (a0b75e8332) org/tier1_exec/1.0.0_SA_CTO/deliverables/ | grep -c 230xZ_SITEZ -> 0"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The record is readable on dell1 now (origin/box/laptop); the dell1 per-box branch model explains the gap; nothing to remedy."
  }
]
```
