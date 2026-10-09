# IRPT_BCKEND -- rounds 97-102 L8 adjudication (~P), with four rounds-86-93 leftovers

<sweep_watermark>2026-10-09T07:30Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~07:3xZ. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_97_102_P_DRAIN_END_20261009.md @274fa2a6e7 (msg 2793)`. 0 judgment criteria; rounds 97-102
MAY-CLOSE. 15 rows dismissed below; 6 graduate OPEN in `remediations/REMEDIATION_v37.md`, three ARMED. This seat's correction: D2-S15,
W188-S3, W189-S2 and W189-S5 belonged to the rounds-86-93 compile (REMEDIATION_v32/v34) and were missed there; they are dispositioned here.

**For the analysis:**
1. **A served change went live unsigned** (D2-S28): IB-pr-384's runner rode IB-pr-383's open ledger at 04:16:44Z. It was ratified after
   the fact, and the hook fix (a ledger admits only the build it pins) is live. The never-widen law's 'sign before you move served output'
   was not met for that act; the mechanism that let it happen is closed.
2. **served.py runs stale on 8 functions** (W201-S4/S7): every staged_from row names an old blob. IB-pr-395 restages 6; irpt-holdings is
   IB-pr-398; irpt-narrative is held (W201-S6, W262-S1: its rebuild WIDENS a no-row internal caller).

```json
[
  {
    "id": "IRPT_BCKEND-C-S322",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T07:30:51Z",
    "one_line": "Rounds 97-102 (~P) and four rounds-86-93 leftovers dismissed: D2-S15 (IB-pr-378 graded on a full-page read; recorder half carried by D2-W159-S1), D2-W188-S3 (source_removed_on written to termination.effective_date plus a capability fact: the schema's own home, as built), D2-W189-S2 (the W2-S57 mutant pin follows rule c, as built), D2-W189-S5 (three bounded costs disclosed), D2-W200-S1 with D2-S28 and its resolution D2-S30 (the IB-pr-384 runner went LIVE UNSIGNED by riding IB-pr-383's open ledger; both halves given retroactively, the APPLIED-UNSIGNED-THEN-RATIFIED ledger opened and closed, and the hook fix ccbe8b8be1 now admits only the build a ledger pins -- measured an ancestor of HEAD), D2-W260-S1 (ruling read from its commit), D2-W201-S1/S3 (IB-pr-390's lane refusal and the ALL-never-admits test, both resolved under AMENDMENT 1 with an in-cell restage; 2/2), D2-W201-S2 (the stale route counts live in the contract file; carried by TCKT_VNEXT-D2-W6-S3), D2-W201-S5 (holdings BUILD_ONLY, fixed by IB-pr-394's parity fix), D2-W201-S8 (the held-out releases now have cells: IB-pr-398, IB-pr-399), D2-W261-S1 (multi_asset is already refused at contract validation, before the gate: redundant, not missing), D2-W261-S2 (ARMED; resolved by PRD v0.33 and IB-pr-396 @5eeef73870).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_BCKEND-D2-S15",
      "IRPT_BCKEND-D2-W188-S3",
      "IRPT_BCKEND-D2-W189-S2",
      "IRPT_BCKEND-D2-W189-S5",
      "IRPT_BCKEND-D2-W200-S1",
      "IRPT_BCKEND-D2-S28",
      "IRPT_BCKEND-D2-S30",
      "IRPT_BCKEND-D2-W260-S1",
      "IRPT_BCKEND-D2-W201-S1",
      "IRPT_BCKEND-D2-W201-S2",
      "IRPT_BCKEND-D2-W201-S3",
      "IRPT_BCKEND-D2-W201-S5",
      "IRPT_BCKEND-D2-W201-S8",
      "IRPT_BCKEND-D2-W261-S1",
      "IRPT_BCKEND-D2-W261-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "this seat's reads ~07:3xZ: round-close-check MAY-CLOSE for rounds 97, 98, 99, 100, 101, 102; ccbe8b8be1 (the hook fix: a ledger admits only the build it pins), 5eeef73870 (IB-pr-396), f8b570d0f4, 42793c81fc, 8a832194f2 are ancestors of box/dell2 HEAD. Round 94 (IB-pr-383, pending) and the ~Y release lanes keep their rows (D2-S18, S19, S21, S22, S24, S25, S27, S29, W190-S1..S3, W223-S4) for their own compile.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S15, D2-W188-S3, D2-W189-S2, D2-W189-S5, D2-W200-S1, D2-S28, D2-S30, D2-W260-S1, D2-W201-S1, D2-W201-S2, D2-W201-S3, D2-W201-S5, D2-W201-S8, D2-W261-S1, D2-W261-S2",
        "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_97_102_P_DRAIN_END_20261009.md @274fa2a6e7 (msg 2793)",
        "this seat's reads ~07:3xZ: round-close-check MAY-CLOSE for rounds 97, 98, 99, 100, 101, 102; ccbe8b8be1 (the hook fix: a ledger admits only the build it pins), 5eeef73870 (IB-pr-396), f8b570d0f4, 42793c81fc, 8a832194f2 are ancestors of box/dell2 HEAD"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "As built, resolved by amendment or a landed commit (measured), redundant, carried by a named row, or ratified with the defect's mechanism fixed."
  }
]
```
