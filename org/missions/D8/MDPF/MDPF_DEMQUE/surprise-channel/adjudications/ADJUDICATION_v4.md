# MDPF_DEMQUE -- round 4 L8/L9 adjudication

<sweep_watermark>2026-10-09T09:01Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T09:01:00Z. L8 packet: 2.0.0_SA_COO~Q1 msg 2147, `deliverables/2.0.0_SA_COO~Q1/ROUND4_REAL_RUN.md` @f05cdc86dd.
5 of 5 complete, proofs OK, 59 tests. 4 rows swept: BLOCKING D1-W9-S1 and Z-W1-S1 dismissed; D1-S2 and Z-W1-S2 graduated INERT to
`remediations/REMEDIATION_v3.md`.

**L9:** FWD-3 reserve claim exposed (held); FWD-4 NOT REALIZED (no finish date; standing requests unpriceable); FWD-2 ledger live at site Z;
FWD-9 ranking and FWD-5 unresolved list run on real data. The lock floor is graded on the 2026-10-10T02:30Z draw.

```json
[
  {
    "id": "MDPF_DEMQUE-C-S7",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:01:00Z",
    "one_line": "Round 4 L9: FWD-3's reserve now carries its claim (held) on every quote; FWD-4 still NOT REALIZED -- no finish date (the reference and model-block ceilings are absent) and a standing request is not priceable; FWD-2's demand ledger is live at site Z (rows=4, cells=17,878); FWD-9 ranks real holdings (AMLP P1); FWD-5's unresolved list is seeded (5 YAHOO_NO_DATA). The 90 pct lock floor (REMEDIATION_v2 D1-S1) is graded on the 2026-10-10T02:30Z scheduled draw.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 4 L9: FWD-3's reserve now carries its claim (held) on every quote; FWD-4 still NOT REALIZED -- no finish date (the reference and model-block ceilings are absent) and a standing request is not priceable; FWD-2's demand ledger is live at site Z (rows=4, cells=17,878); FWD-9 ranks real holdings (AMLP P1); FWD-5's unresolved list is seeded (5 YAHOO_NO_DATA). The 90 pct lock floor (REMEDIATION_v2 D1-S1) is graded on the 2026-10-10T02:30Z scheduled draw.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO ran bbg_quote.py --quote requests/SITEZ-SIGNIN-PREFLIGHT-REFDATA-20261009.json at 08:5xZ: cells bloomberg_reference 1, claims ceiling absent / reserve held, finish_date null",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND4_REAL_RUN.md @f05cdc86dd: ABNB model-block 989 cells, claims absent/absent; ETFS_RIVALS standing request ValueError 'request has no securities'; rank.py RANK 1 00162Q866 P1; unresolved 5 rows; LEDGER-OK rows=4 cells=17878",
        "round-close-check --round 4: 5 orders, proof_ok 5, judgment 0, MAY-CLOSE"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 record, not a hazard."
  },
  {
    "id": "MDPF_DEMQUE-C-S8",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:01:00Z",
    "one_line": "D1-W9-S1 (BLOCKING) dismissed: resolved in-round -- t10 amended @015c0038fa to grant bbg_quote.py, quote() now returns the claims, and t10 AC1 PASSED RESERVE-OK @c2a05ea64f.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-D1-W9-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Resolved: this seat's own quote run prints claims.reserve = held.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log c2a05ea64f: proof(TO-DQ-t10) AC1 PASS RESERVE-OK, AC2 PASS RSEAM-OK",
        "3.0.0_SA_CVO bbg_quote.py run (claims present)",
        "investigation row MDPF_DEMQUE-D1-W9-S1"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved: this seat's own quote run prints claims.reserve = held."
  },
  {
    "id": "MDPF_DEMQUE-C-S9",
    "project": "MDPF_DEMQUE",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T09:01:00Z",
    "one_line": "Z-W1-S1 dismissed: handled by the deployed uploader (candidate @492cb5a2f1, deploy closed @ca3b056946) -- the two known mixed backfill shapes are priced by batch identity, and an unresolvable mixed mode keeps cells absent per channel instead of a wrong multiplier.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_DEMQUE-Z-W1-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The ledger states absent where it cannot measure; no mispriced figure is written.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row MDPF_DEMQUE-Z-W1-S1",
        "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/ROUND4_REAL_RUN.md @f05cdc86dd t-14 row (CTO~Z half @3607c76017)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The ledger states absent where it cannot measure; no mispriced figure is written."
  }
]
```
