# TCKT_VNEXT: CVO adjudication, round 20 part 6 (five ARMED rows owned by the issuer: closed on evidence)

<sweep_watermark>2026-10-20T05:30Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-20.

L9 disposition by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-20T05:30Z. Input:
`org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_ARMED_ROWS_OWNED_BY_COO.md`, blob 9d98ef0db9cf (msg 11216; verified by
`git hash-object`). `comp-surprise --armed --project TCKT_VNEXT` read 9 ARMED at 05:23Z. This file disposes of the five whose
`disarm_owner` is `2.0.0_SA_COO~V2`. The CTO's four (D2-W6-S2, D2-S46, D2-S50, D2-S53) are untouched and ride the slug.

## Each row: its arming condition, and what this seat read

1. **D2-W41-S6 (BLOCKING): REMEDIATED.**
   - The arming condition: running `tests/test_authz_matrix.py` by path reached the real SES notifier.
   - Read by this seat at HEAD: `tests/_no_live.py` and `tests/test_no_live_by_path.py` exist.
   - `python -m pytest tests/test_no_live_by_path.py -q -p no:cacheprovider` gives **3 passed**.
   - `test_authz_matrix.py` names `_no_live` twice, the by-path entry's guard.
   - This seat did not run the matrix file by path to prove it: that run is the hazard the guard exists for, and the test above is its
     control.
2. **D2-W43-S1 (BLOCKING): REMEDIATED.** The arming condition: one `TICKET_ATTACH_BUCKET` could not serve a per-firm home. The live
   `opal-ticket-api` environment, read at ~05:2xZ:
   - `TICKET_ATTACH_BUCKET_TEMPLATE = "opal-data-{firm}"`;
   - `TICKET_ATTACH_BUCKET` is absent (null), so one bucket per firm comes from the template.
   - This seat also graded the builder output and the per-firm grant in v8 (R18TR1, R18TR3).
3. **D2-W43-S2 (BLOCKING): REMEDIATED.** The arming condition: the naming gate refused the table segment `ticket-attachments`. Live:
   `TICKET_ATTACH_KEY_TEMPLATE = "portal/{firm}/state/ticket_attachments/trade-form/"`, which is snake_case and the builder's output
   (v8, R18TR1).
4. **D2-W42-S1 (OBSERVATION): REMEDIATED.**
   - The arming condition: the candidate was cut from `origin/DEV`, not the last PROD release.
   - The meeting form reached PROD from the PROD-based re-cut `4e1e35bfa0` (v10).
   - This round's page change `e83292d0` sits on `facddeb6`, the PROD release at its cut: `merge-base --is-ancestor` reads yes. It is now
     in both PROD and DEV.
5. **D2-W42-S4 (OBSERVATION): CLOSED_UNREMEDIATED, NOT_A_DEFECT.**
   - The arming condition: three trade-named gating lines were replaced by `drawsOwnForm()`, and the merge was the issuer's to decide.
   - The merge was decided and shipped. This seat read in v10 that `drawsOwnForm` carries PROD's trade guards forward unchanged.
   - The spec's ban on trade-named lines was withdrawn when Andrew lifted the Trade Request hold (CTO msg 10728). The lines are the
     intended state, not a defect.

The disposition of record for all five is DISMISSED_WITH_REASON, with each reason above. None is a hazard today.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S10",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-20T05:30Z",
    "one_line": "Five ARMED round-18 rows owned by 2.0.0_SA_COO~V2 closed on evidence read by this seat: W41-S6, W43-S1, W43-S2 and W42-S1 remediated; W42-S4 not a defect after the Trade hold was lifted.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "TCKT_VNEXT-D2-W41-S6",
      "TCKT_VNEXT-D2-W43-S1",
      "TCKT_VNEXT-D2-W43-S2",
      "TCKT_VNEXT-D2-W42-S1",
      "TCKT_VNEXT-D2-W42-S4"
    ],
    "spec_asserts": "An ARMED row is disarmed only when its arming condition is measured ended; L10 waits until every BLOCKING or ARMED row is dispositioned (CLAUDE.md rule 27).",
    "world_is": "test_no_live_by_path.py 3 passed at HEAD; live opal-ticket-api reads TICKET_ATTACH_BUCKET_TEMPLATE opal-data-{firm}, TICKET_ATTACH_KEY_TEMPLATE portal/{firm}/state/ticket_attachments/trade-form/, no TICKET_ATTACH_BUCKET; portal e83292d0 based on PROD facddeb6; Trade hold lifted (CTO msg 10728).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_ARMED_ROWS_OWNED_BY_COO.md blob 9d98ef0db9cf (msg 11216)",
        "infra/aws/lambda/ticket_center/tests/test_no_live_by_path.py (pytest, 3 passed, 2026-10-20 ~05:2xZ)",
        "live: lambda get-function-configuration opal-ticket-api Environment",
        "git -C portal merge-base --is-ancestor facddeb6 e83292d0",
        "ADJUDICATION_v8 (R18TR1, R18TR3), ADJUDICATION_v10 (R20PP-AC4J)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "W41-S6, W43-S1, W43-S2, W42-S1: REMEDIATED, each arming condition measured ended (see the file). W42-S4: NOT_A_DEFECT, the spec's ban was withdrawn when the Trade hold was lifted."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
