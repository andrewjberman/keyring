# AMGT_CORPUS ROUND 33 -- L8 COMPILE -- every magnitude-guessed DECIMAL label retired (77 -> 0), values unmoved; ORA's 0.22% ROIC is a real low year; 4 older rows closed; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~19:3xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND33_DRAIN_END_PACKET.md` @`6303d98bce` (3,932 B, read to EOF), msg 28680.
**L7:** no task order was cut.
- `CRPS-ai-1` is a direct act @`f64efce667`, with AMENDMENT 1: the EQY_DVD_YLD_IND ground is a (0.5, 2.0) band.
- `CRPS-ai-2` is SERVED: ledger `amgt-corpus-r33-ai2` CLOSED with 5 legs (map `31c1e10888`, blocks `795cf57788`).
- **0 judgment criteria**, so this seat's read below is the plausibility check.

## 1. The plausibility read (packet section 4: ORA's FY2025 ROIC 0.22% against a 3.7-7.3% history)

**ORA is Orange SA (`ORA_FP_Equity`).** Its newest served block is `20261002T180214Z`, one of leg c's 11 stamps. This seat read the
block's other FY2025 figures:

| figure | FY2023 | FY2024 | **FY2025** |
|---|---|---|---|
| SALES_REV_TURN (MILLIONS) | 39,677 | 40,259 | **40,397** |
| IS_OPER_INC (MILLIONS) | 4,761 | 5,464 | **3,624** |
| OPER_MARGIN (PERCENT) | 12.00 | 13.57 | **8.97** |
| NET_INCOME (MILLIONS) | 2,440 | 2,350 | **538** |
| RETURN_COM_EQY (PERCENT) | 8.43 | 8.10 | **1.42** |
| RETURN_ON_INV_CAPITAL (PERCENT) | 4.67 | 4.52 | **0.22** |

- **Not a partial year.** FY2025 revenue is full-year scale (40,397 against 40,259).
- **A real low year.** Net income fell 77% and ROE fell from 8.1% to 1.4% in the same block, so the 0.22% ROIC follows the earnings
  collapse; it does not stand alone.
- **The label reads right.** PERCENT matches the series (median 4.47) and the sibling ratios. As DECIMAL it would claim 22%, against a
  4-5% history and a collapsing year.
- **BP's 0.096% ROE and JD's 0.21% operating margin** are low and consistent with the years the packet names. This seat did not read
  their blocks further, so they are accepted as plausible, not as measured.

## 2. The served census (packet section 3), as stated

- **Labels:** DECIMAL-by-magnitude **77 -> 0**; UNRESOLVED units **11 -> 19** (the 8 named no-ground figures).
- **Scope:** exactly the 11 keys moved, and **0 value moves**.
- **Negative arms:** BA's BEST_DIV_YLD stays PERCENT with its stamp unmoved; 0 of 89 other stamps moved. The DECIMAL-confirmed arm
  is EMPTY (count 0). Both halves named it, and it is not claimed as passed.
- **Z-S81 is decided** (row Z-S83): 69 PERCENT (60 by series median, 9 by row identity) and 8 UNRESOLVED.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S81` (graduated at v38) | DISMISSED_WITH_REASON | remedied by ai-2: 0 magnitude labels remain over 100 keys (Z-S83) |
| `Z-S83` | DISMISSED_WITH_REASON | the decision record of Z-S81 |
| `Z-W4-S6` (peers pool index keyed by the raw slash segment, ARMED) | DISMISSED_WITH_REASON | remedied in RESAPP am-8 (`a0f3f2d087`, "peers engine finds a slash key's pool model block (Z-W4-S6)"; CTO ruling 2, msg 28540). Served read by this seat: `/security/BP%2F_LN_Equity/peers` answers 12 members, with `cap_source` `model_block:BP/_LN_Equity:CUR_MKT_CAP` |
| `Z-W1-S21`, `Z-W3-S10` (AC populations off by the slash-key copies, BLOCKING) | DISMISSED_WITH_REASON | superseded: the orders they blocked (`CRPS-aa-1`, `CRPS-aa-3`) read `<status>complete</status>`, and every census since rounds 31-33 runs over the 100 slash-free keys |
| `Z-S3` (L4-R notifier sends OVERDUE for an ADMITTED PRD, ARMED, 09-23) | DISMISSED_WITH_REASON | superseded: the notifier now binds to the ENDPOINT hash (spine v3.19). Today it delivered three L4-R halves and their re-deliveries to this seat correctly, and this seat's inbox holds 0 OVERDUE notices |

**Correction to v38's L10 line.** v38 read "no BLOCKING or ARMED row of the round is open". The L10 rule is EVERY BLOCKING or ARMED
row, not the round's, and Z-W1-S21, Z-W3-S10, Z-S3 and Z-W4-S6 were open then. They are dispositioned here, so the slug below meets
the rule as written.

## 4. L10 PRECONDITION

Both cells are DONE (a direct act, and the SERVED act with its ledger CLOSED). No BLOCKING or ARMED investigation row is left
UNDER_INVESTIGATION. Judgment criteria: 0. **MET.**

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S41",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T19:32:00Z",
    "one_line": "Round 33 L8: the 77 DECIMAL-by-magnitude labels are retired (69 PERCENT, 8 UNRESOLVED; 0 values moved); the plausibility read holds -- ORA (Orange SA) FY2025 ROIC 0.22% sits beside the same block's net income 538M (2,350M in 2024) and ROE 1.42% (8.10%) on full-year revenue 40,397M, a real low year, not a partial one and not a unit error; Z-S81 remedied, Z-S83 its record.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S3 opal-data-harvest derived/model_block/ORA_FP_Equity/20261002T180214Z/model_block.json: RETURN_ON_INV_CAPITAL 2023 4.6713 / 2024 4.5237 / 2025 0.2237 PERCENT; NET_INCOME 2440 / 2350 / 538 MILLIONS; RETURN_COM_EQY 8.4343 / 8.0968 / 1.4175 PERCENT; SALES_REV_TURN 39677 / 40259 / 40397; IS_OPER_INC 4761 / 5464 / 3624.",
        "ROUND33_DRAIN_END_PACKET.md @6303d98bce section 3 (census 77 -> 0, UNRESOLVED 11 -> 19, 0 value moves, 0 of 89 other stamps)."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S81",
      "AMGT_CORPUS-Z-S83"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-S81 is remedied by ai-2 (0 magnitude labels over 100 keys); Z-S83 is its decision record.",
    "spec_asserts": "A served unit label says what the number is.",
    "world_is": "Every remaining percent-family label is grounded or UNRESOLVED; the one outlier value is a real year.",
    "notes": "No act owed."
  },
  {
    "id": "AMGT_CORPUS-Z-C-S42",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T19:32:00Z",
    "one_line": "Four older open rows closed: Z-W4-S6 remedied by RESAPP am-8 (served BP/_LN_Equity peers: 12 members, cap from the slash key's model block); Z-W1-S21 and Z-W3-S10 superseded (CRPS-aa-1 and aa-3 complete; censuses since run over 100 slash-free keys); Z-S3 superseded (the L4-R notifier binds to the ENDPOINT hash and delivered today's halves correctly; 0 OVERDUE notices in this seat's inbox).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git log -- lib/research/peers/universe.py: a0f3f2d087 fix(AMGT-am-8): peers engine finds a slash key's pool model block (Z-W4-S6).",
        "opal-amgt-scoped-api invoke /api/scoped/amgt/security/BP%2F_LN_Equity/peers (~19:3xZ): 200, member_count 12, cap_source model_block:BP/_LN_Equity:CUR_MKT_CAP.",
        "task-orders: AMGT_CORPUS.TO-CRPS-aa-1 and TO-CRPS-aa-3 last <status>complete</status>.",
        "org/mcp/inbox/3.0.0_SA_CVO/~Z/read: 0 file names carry OVERDUE."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-W4-S6",
      "AMGT_CORPUS-Z-W1-S21",
      "AMGT_CORPUS-Z-W3-S10",
      "AMGT_CORPUS-Z-S3"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-W4-S6 remedied and served (am-8); Z-W1-S21 and Z-W3-S10 superseded by complete orders and the 100-key population; Z-S3 superseded by the reworked notifier.",
    "spec_asserts": "The L10 slug goes only when every BLOCKING or ARMED row is dispositioned.",
    "world_is": "These four were open at v38; now dispositioned.",
    "notes": "Corrects v38's round-scoped reading of the L10 precondition."
  }
]
```

-- 3.0.0_SA_CVO~Z
