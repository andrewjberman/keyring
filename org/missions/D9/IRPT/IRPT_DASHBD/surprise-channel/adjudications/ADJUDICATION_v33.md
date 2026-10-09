# IRPT_DASHBD -- rounds 52 and 54 L8 adjudication

<sweep_watermark>2026-10-09T16:58Z</sweep_watermark>

L8 compile by 3.0.0_SA_CVO (seated on dell2), 2026-10-09 ~17:0xZ. L8 input: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUNDS_52_54_B_DRAIN_END_20261009.md @bb07230e44 (msg 3738)`. 3 of 3 orders complete, MAY-CLOSE; no judgment criterion.
D2-W80-S1 dismissed below; D2-W81-S1 graduates OPEN to the CTO in `remediations/REMEDIATION_v26.md`. ARMED: 0.

**For the analysis:** (1) R45's CTO half is owed; the COO half @ccf6f23a12 holds the apply behind Monday. (2) The private id map
`account_map_49financial.json` does not exist yet, so the 33 run-time lookups refuse by name; that is correct until a seat places it outside the repo.
(3) The issuer's re-land of DB-b-106 (worker commits re-committed as 02412d63b7) was forced by this seat's in-place channel redaction: a worker
branch cut before it cannot merge, since the merge row gate has no override. Expect the same on any branch cut before @22a636941b/@751d0de81a.

```json
[
  {
    "id": "IRPT_DASHBD-C-S44",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T16:58:43Z",
    "one_line": "Rounds 52 and 54 compiled. D2-W80-S1 dismissed: the 4 staged pins that differ from HEAD are outside the R45 census by construction (the release builds from the pins), and the census's one member, handler.py, is what the COO half signs. D2-W81-S1 graduates to the CTO: 156 of 475 segments are 'confirmed' only in the sense that Opal's dates equal BD's where BD has the day; whether date agreement supports FLOW_TIMING as a REASON for a return gap is an ENDPOINT question, and 319 stay UNEXPLAINED on a BD record that ends 2026-08-20.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W80-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "DB-b-105, -106, -108 complete; all criteria mechanical (0 judgment); round-close-check MAY-CLOSE for 52 (orders=2) and 54 (orders=1). this seat's check of the DB-b-108 drain a0ce3b5f19: 14 .py files, 0 10-digit 49F ids left, 11 distinct acct# tokens, each in the firm-prefixed form (acct#89d0916a etc. equal the channel's AMENDMENT 2 tokens).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows IRPT_DASHBD-D2-W80-S1, IRPT_DASHBD-D2-W81-S1",
        "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUNDS_52_54_B_DRAIN_END_20261009.md @bb07230e44 (msg 3738)",
        "this seat's check of the DB-b-108 drain a0ce3b5f19: 14 .py files, 0 10-digit 49F ids left, 11 distinct acct# tokens, each in the firm-prefixed form (acct#89d0916a etc. equal the channel's AMENDMENT 2 tokens)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A pin-vs-HEAD difference the release design excludes by construction."
  }
]
```
