# TCKT_VNEXT: CVO adjudication, round 20 part 6b (the CTO's D2-W6-S2 and D2-S50, sent at his word)

<sweep_watermark>2026-10-20T05:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-20.

L9 disposition by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-20T05:45Z. Input: the updated
`org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_ARMED_ROWS_OWNED_BY_COO.md`, blob e57c81d1b60f (msg 11225; the CTO's word msg 11224).
D2-S46 (an IAM read in progress) and D2-S53 (Andrew's) are not disposed of here.

## What this seat read itself

1. **D2-W6-S2: REMEDIATED by another repair (NFRA_OPLGTW `TO-OG-da-1`).**
   - The arming condition: the data-refresh routes admitted a caller whose `userType` was absent.
   - **Live code.** `opal-data-refresh-api` CodeSha256 is `qHMjXkK1/1NhmBmkK/6Q+q+WdXMRoTOprNfTixBIxaM=` (LastModified 2026-10-09T07:59:39Z).
     The package was downloaded by this seat: its zip sha256 equals that CodeSha256, and its `lambda_function.py` equals the tree
     byte for byte after line-ending normalisation (83,888 bytes).
   - **The gate.** `validate_user_type` admits `userType == 'Dev'` or `is_opal_internal(context)`. `is_opal_internal` admits only `tier ==
     internal` or an exact `firmId` match and fails closed. An empty or `null` userType without those is refused, and a call with no
     authorizer context returns `(False, 'unknown')`.
   - **Tests.** `test_admission_gate.py`, run by this seat: 5 passed.
   - **Limit, for D2-S53.** The gate trusts the authorizer's `firmId`. A users row on an outside domain that carries the internal firm id,
     D2-S53's hazard, is still admitted here. That row is Andrew's and stays ARMED.
2. **D2-S50: REMEDIATED (`TO-R9-st1`, 97d2d4bedec).**
   - The arming condition: the no-row refusal read whether a row EXISTED, so a DISABLED row still admitted.
   - **Live code.** `_profile_scope` in the live ticket service (its source equals 17073aff04e, read by this seat in v14) refuses at line 422:
     `if got.get("status") != "active"` gives 403 with `FIRM-SCOPE-NOT-ACTIVE`.
   - **Tests.** `tests/test_status_active.py` and `tests/test_profile_scope_fail_closed.py`, run by this seat: 25 passed.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S11",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-20T05:45Z",
    "one_line": "The CTO's D2-W6-S2 and D2-S50 closed on evidence read by this seat: the live data-refresh gate fails closed (5 tests), the live ticket service refuses a non-active row (25 tests); D2-S53 stays ARMED.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "TCKT_VNEXT-D2-W6-S2",
      "TCKT_VNEXT-D2-S50"
    ],
    "spec_asserts": "An ARMED row is disarmed only when its arming condition is measured ended; L10 waits until every BLOCKING or ARMED row is dispositioned (CLAUDE.md rule 27).",
    "world_is": "opal-data-refresh-api live source equals the tree (zip sha256 = CodeSha256 qHMjXkK1...); validate_user_type admits Dev or tier/firmId internal, else refuses; test_admission_gate.py 5 passed. opal-ticket-api live _profile_scope refuses status != active (line 422); 25 tests passed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_ARMED_ROWS_OWNED_BY_COO.md blob e57c81d1b60f (msg 11225)",
        "live: lambda get-function opal-data-refresh-api (downloaded, compared)",
        "infra/aws/lambda/data_refresh/test_admission_gate.py; infra/aws/lambda/ticket_center/tests/test_status_active.py, test_profile_scope_fail_closed.py",
        "ADJUDICATION_v14 (live opal-ticket-api source = 17073aff04e)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "D2-W6-S2: REMEDIATED by NFRA_OPLGTW TO-OG-da-1 (live equals tree, fail-closed admission). D2-S50: REMEDIATED by TO-R9-st1 (live refuses a non-active row). D2-S53's firmId exposure is not closed by either and stays Andrew's."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
