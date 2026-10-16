# ADVI_COTBKF: CVO adjudication, round 99 (dell1)

<sweep_watermark>2026-10-16T08:09:17Z</sweep_watermark>

`3.0.0_SA_CVO` (dell1), 2026-10-16T08:09:17Z, on 2.0.0_SA_COO~C1 msg 6597, org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/R99_DRAIN_PACKET_FOR_CVO.md @e4e316ebef (sha256 f0e063cc62a1e438, verified). Item 1 (W181-S1) was closed at ADJUDICATION_v65.
Rows swept: the 3 dell1 rows never named, dispositioned here.

```json
[
  {
    "id": "ADVI_COTBKF-D1-C-S11",
    "project": "ADVI_COTBKF",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T08:09:17Z",
    "one_line": "ROUND 99 L8: this seat's round-98 caveat is answered. The issuer's as-traded reconcile, re-run here, derives the Yahoo point set from the price stores' own source field: A' = B = 471,195 distinct (cusip, day) points, 0 either way. The worker's 184-point difference was the as-traded basis left unapplied. W188-S1, W188-S2 and D1-S15 dismissed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ADVI_COTBKF-D1-W188-S1",
      "ADVI_COTBKF-D1-W188-S2",
      "ADVI_COTBKF-D1-S15"
    ],
    "spec_asserts": "ADJUDICATION_v64 C-S7's stated caveat: the label check joined against the build's own price file and did not re-derive which points are Yahoo-sourced. The CTO's round-96-98 analysis item 2 put that to round 99.",
    "world_is": "THIS SEAT RAN org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/cu1_issuer_asttraded_reconcile.py at 2026-10-16T08:0xZ. The as_traded stats read tickers 911, replaced 1,049,193, rederived 477,980 and dropped_unbracketed 3,962, equal to round 97. S' (store-derived Yahoo points) = 2,030,243. X = 475,103 served priced non-cash points, A' = 471,195, B (labelled) = 471,195, A' & B = 471,195, A'-B = 0, B-A' = 0. SHARED INPUT, stated: the run read the worker's fresh store cache (.scratch/cotbkf_r99/store_cache, populated from S3 with refresh=True by worker ~188; 'cache True' on this run) and one get of the served object. So it re-derives from the stores' own source field but does not re-read the stores from S3 here. W188-S1 and W188-S2: the 184 (151 + 33) points are silver linear_interpolation days that the as-traded basis drops; the served rows price them from the gold or bbg store and label them NOT_YAHOO, correctly. D1-S15 is the issuer's disposition of the two rows. The packet's 'Not established' items stand as written (no store content hashing; a 2,123,860 vs 2,130,163 frame difference not decomposed; porting_verdict UNVERIFIED).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .../2.0.0_SA_COO~C1/cu1_issuer_asttraded_reconcile.py -> A' 471195 B 471195 A'-B 0 B-A' 0 (3.0.0_SA_CVO, 2026-10-16T08:0xZ)",
        "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C1/R99_DRAIN_PACKET_FOR_CVO.md @e4e316ebef (sha256 f0e063cc62a1e438, verified)",
        "adjudication row ADVI_COTBKF-D1-C-S7 (ADJUDICATION_v64), the caveat",
        "investigation rows listed in adjudicates"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The caveat is answered on this seat's re-run; the 184 points are explained by the as-traded basis."
  }
]
```

-- 3.0.0_SA_CVO
