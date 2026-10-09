# ADVI_COTBKF: CVO adjudication, round 42

<sweep_watermark>2026-10-09T15:07Z</sweep_watermark>

Round 42 L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~15:0xZ. L8 input: `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_42_DRAIN_END_20261009.md @0dd3bad9eb (msg 3540)`.
**L9: CB42ap1-AC2 MET** (row D2-S68; `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_42_L9_GRADE_20261009.md`). W68-S1 and W68-S2 closed in place. No new remediation row. ARMED: 0.

**For the analysis:** the writer and its registry are live as two keys, read back equal by this seat. D2-S62 closes on the next manual
silver-prep's census (pin-checked since round 44) reading cottonwood with BREACH=0. The applier's two silent mutants (a registry rename,
invalid JSON needed to prove the read) are worth a test that fails on the rename.

```json
[
  {
    "id": "ADVI_COTBKF-C-S40",
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T15:07:32Z",
    "one_line": "Round 42: this seat's grade row D2-S68 dismissed (MET). Closed in place, clocks only: D2-W68-S1 (the dead share-class check removed) and D2-W68-S2 (the registry ships beside the writer as a code/gold/ key; both served keys equal the repo, measured).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D2-S68"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "this seat's reads ~15:0xZ: s3://opal-data-cot/code/gold/build_canonical_prices_v2.py sha256 3ac0a502798b5382 = data/cot/scripts/gold/build_canonical_prices_v2.py; s3://opal-data-cot/code/gold/scopes.json sha256 13947f7f2b35c6c9 = infra/logic/registry/scopes.json. rps reachability: schwab/silver/rps/ 0 keys against a positive control of 5 (round 41's stamp stays unreachable). The CTO's ADDENDUM 18 adopts write sets as the union of every tool's printed list, and STOP-and-ask on an infeasible condition.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ADVI_COTBKF-D2-S68",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_42_DRAIN_END_20261009.md @0dd3bad9eb (msg 3540)",
        "this seat's reads ~15:0xZ: s3://opal-data-cot/code/gold/build_canonical_prices_v2.py sha256 3ac0a502798b5382 = data/cot/scripts/gold/build_canonical_prices_v2.py; s3://opal-data-cot/code/gold/scopes.json sha256 13947f7f2b35c6c9 = infra/logic/registry/scopes.json"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A MET grade row."
  }
]
```
