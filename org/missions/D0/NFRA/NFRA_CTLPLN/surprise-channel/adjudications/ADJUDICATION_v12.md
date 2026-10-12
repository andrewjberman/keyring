# NFRA_CTLPLN: CVO L8 dispositions at the round-10 drain (2026-10-12)

L8 by `3.0.0_SA_CVO~L` (laptop), on 1.0.0_SA_CTO msg 108555 (COO~C drain msg 108553). HEAD 4f3a2a9694.

`round-close-check --round 10` reads 2 of 2 judgments graded (C-S16 and C-S17, carried), proof_bad 0, MAY-CLOSE. Every order is
terminal (104 complete, 4 withdrawn, 1 cancelled, 1 superseded). Two gating items were undispositioned:
- **W73-S2 GRADUATED** (C-S36; row in `remediations/REMEDIATION_v4.md`).
- **W73-S1 DISMISSED** (C-S37).

All 68 gating items are now dispositioned. S9113 and S9114 (OBSERVATION/INERT) gate nothing. S9113 names the shared portal API
root's owners. Still ARMED at Andrew: W61-S1 and S9112.

<sweep_watermark>2026-10-12T13:35Z</sweep_watermark>

```json
[
  {
    "id": "NFRA_CTLPLN-C-S36",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T13:35Z",
    "one_line": "W73-S2 GRADUATED: thread-trace globs the reading worktree for orders instead of reading git refs, so a checkout missing an order drops it silently; the issuer carries the fix.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "thread-trace.py docstring: 'Read one round's five hops from git.'",
    "world_is": ".tools/thread-trace.py:236 at HEAD 4f3a2a9694 is `for path in sorted(glob.glob(pattern))` inside find_orders. The issuer's row S9114 calls it carried work. On the integrated box/laptop checkout every round-9 order file is present, so it did not bite here; a checkout lacking a CLOUD-held order would bite. The gap is still in code, so it graduates rather than dismisses.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/thread-trace.py:236 read at HEAD 4f3a2a9694",
        "INVESTIGATION_v1.md rows W73-S2 and S9114"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W73-S2"
    ],
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_CTLPLN-C-S37",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T13:35Z",
    "one_line": "W73-S1 resolved by TO-CT-z-1 Amendment 1 (ecc0273a1c): thread-trace now reads seat-home orders and matches by slug-less id, and the round-9 read of TO-CT-y-2 names its dell1 seat.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "W73-S1 (BLOCKING): `thread-trace.py --order TO-CT-y-2` read 0/5 (orders=NONE, rc=1) and could not name the seat 0.7.0_AE_CloudOps~CT1.",
    "world_is": "Run by this seat at HEAD 4f3a2a9694 (ecc0273a1c is an ancestor): `python .tools/thread-trace.py --project NFRA_CTLPLN --round 9 --order TO-CT-y-2` prints HOP 1 PLAN by 2.0.0_SA_COO~C, HOP 2 WORK and HOP 3 PUBLISH by 0.7.0_AE_CloudOps~CT1 on origin/box/dell1, HOP 4 INTEGRATE by 0.0.0_AB_MSTR on origin/CLOUD, HOP 5 GRADE ABSENT; 'THREAD ... orders=TO-CT-y-2 hops=4/5', rc 0. HOP 5 is absent because TO-CT-y-2 carries no judgment criterion (round-close-check lists none for it), not because of the defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git merge-base --is-ancestor ecc0273a1c HEAD: true",
        "python .tools/thread-trace.py --project NFRA_CTLPLN --round 9 --order TO-CT-y-2 (rc 0, hops=4/5)"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-W73-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Fixed in code at HEAD, and this seat re-ran the read."
  }
]
```
