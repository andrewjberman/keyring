# IRPT_BCKEND -- sweep 6 addendum: rows W90-S1 to S3

<sweep_watermark>2026-10-01T12:08Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-02 ~04:3xZ. The three rows sweep 6 (ADJUDICATION_v20.md) left undispositioned because TO-IB-yr-271 was open. That order is superseded and TO-IB-yr-281 is complete. 1 row dismisses W90-S2 and W90-S3; W90-S1 is graduated and closed in remediations/REMEDIATION_v17.md. Rows filed after sweep 6 (S249 on) are not compiled here; they wait for sweep 7.

```json
[
  {
    "id": "IRPT_BCKEND-C-S271",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T04:35:00Z",
    "one_line": "W90-S2 and W90-S3 are moot: S2 explained why TO-IB-yr-271's falsifier could pass while the control stayed red for cause F, and the seam suite is now green; S3 is a criterion defect of TO-IB-yr-271, which is superseded by TO-IB-yr-281 (complete).",
    "class": "OBSERVATION",
    "adjudicates": [
      "IRPT_BCKEND-W90-S2",
      "IRPT_BCKEND-W90-S3"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "The seam suite reads 0 failed at HEAD, so no control is red for a second reason; the order whose owned cells did not match its criteria will never be graded.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "cd infra/aws/lambda/investor-reporting && python -m pytest -q -p no:cacheprovider _contracts/tests/test_seam_paired.py at CLOUD HEAD (this seat, 2026-10-02 04:3xZ; Y28-1-AC1's own invocation): 62 passed, 0 failed; git status over investor-reporting, docs/contracts and portal identical before and after the run",
        "task-orders/IRPT_BCKEND.TO-IB-yr-271.seam-parser-resolves-opal-refs.md <status>superseded; IRPT_BCKEND.TO-IB-yr-281.seam-suite-six-remaining-causes.md <status>complete (2.0.0_SA_COO~Y 07d17ac44f)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Moot in the world: the red that S2 qualified is gone, and the order S3 faulted is superseded."
  }
]
```
