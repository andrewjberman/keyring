# MDPF_CANON -- round 10 L9 and row sweep (dell1)

<sweep_watermark>2026-10-16T14:02:04Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T14:02:04Z, on 2.0.0_SA_COO~D1 msg 6727, org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/ROUND10_DRAIN_END.md @3ea8caffab (FINAL).
Rows swept by id-set difference: 3 dell1 rows never named, dispositioned here. D1-S29 stays as graded at ADJUDICATION_v17, carried by round 11.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S92",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T14:02:04Z",
    "one_line": "ROUND 10 L9: JUDGMENT MDPF_CANON.TO-CN-r-1 AC4 MET. The first scheduled fire carrying the code (pin b6352de8f8) reads 11 of 11 arms on this seat's own run. The served groups are unchanged on today's data, which has 0 leg-gap dates, so only the negative arm of the carry rule is exercised organically; the positive arm stands on the merge-time oracle and delta.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "MDPF_CANON.TO-CN-r-1 AC4 (judgment): /seams on the producer-to-served seam after the first scheduled run carrying the code, with the first-fire readback. MECHANICAL: the four keys stay aligned to dates[]; every pre-existing key equals the prior day's rule; carried_dates equals the no-total dates plus the dates on which a leg actually carried; partition identity R4 and oracle R3 hold. DECLARATIVE: meta.trend_groups unchanged. SEMANTIC: the served output is unchanged on today's data.",
    "world_is": "MDPF_CANON.TO-CN-r-1 AC4 MET. THIS SEAT RAN round10/checks/r9_trend_groups_readback.py read --pin b6352de8f843f3726ad5c51c650d9035ca8336db at 2026-10-16T14:0xZ against the served objects: 11 of 11 arms. MECHANICAL: R1 (Global, 498 dates, none missing or misaligned) and R2 (single-firm scopes all-None and aligned); R3 (the period-end oracle at 9 period ends); R4 (the partition identity on 489 dated rows); R5 (carried_dates = the 9 no-total dates plus 0 leg-gap dates); R6 (against the prior dated object, pre-existing keys equal except 12 restated cells on model_aua and non_model_aua for 2026-10-12..14, within the at-most-5-per-array allowance); R11 (no leg lost from 2026-10-14 to 2026-10-15). DECLARATIVE: R8 (meta.trend_groups names the SMArtX partition read 2026-10-16, 1,286 dates and the 2026-05-18 boundary). R9: the run manifest has no errors and run.code.commit equals the pin. SEMANTIC: the new rule acts only on a total-bearing date whose leg is missing; today's object has none, so its trend groups are what the round-9 rule gives, consistent with the merge-time DELTA 0 of 497 (packet section 1). LIMIT: the carry itself has not fired on a served object. A NIT IN THE RECORD: the packet's section 4 invocation names the pin 'b6352de843f3726ad5c51c650d9035ca8336db', which is not a commit. This seat's first run with that string read R9 FAIL, and the run with the true pin b6352de8f843... read PASS. The issuer's FINAL read states 'read' with no pin.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/checks/r9_trend_groups_readback.py read --pin b6352de8f843f3726ad5c51c650d9035ca8336db -> 11 of 11 arms (3.0.0_SA_CVO, 2026-10-16T14:0xZ)",
        "git rev-parse b6352de8f8 -> b6352de8f843f3726ad5c51c650d9035ca8336db",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/ROUND10_DRAIN_END.md @3ea8caffab (FINAL)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record: CN-r-1 AC4 MET."
  },
  {
    "id": "MDPF_CANON-D1-C-S93",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-16T14:02:04Z",
    "one_line": "Round 10 rows dismissed (3, all BLOCKING, INERT): two sparse worktrees without data/ or infra/aws, and a worker face missing its <status> element. Both cells later ran and are complete, so none leaves a hazard.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-W29-S1",
      "MDPF_CANON-D1-W30-S1",
      "MDPF_CANON-D1-W30-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "round-close-check --project MDPF_CANON --round 10 (this seat, 2026-10-16T14:01Z): 2 orders, 2 complete. CN-r-1 merged b6352de8f8 (the drain merge of wk-MDPF_CANON-29) and its code is in the served run (C-S92 R9). CN-r-2's publisher fire published 22 of 22 (packet section 4.1). The three rows are the issuer's sparse-cone and order-shape defects, resolved by the re-seats.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python .tools/round-close-check.py --project MDPF_CANON --round 10 (orders 2, complete 2)",
        "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/ROUND10_DRAIN_END.md @3ea8caffab (FINAL)",
        "investigation rows listed in adjudicates"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by the re-seated cells; both orders complete."
  }
]
```

-- 3.0.0_SA_CVO
