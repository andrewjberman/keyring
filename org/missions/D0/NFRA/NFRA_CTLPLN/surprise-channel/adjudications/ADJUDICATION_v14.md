# NFRA_CTLPLN: CVO L8 dispositions at the round-11 close (2026-10-12)

L8 by `3.0.0_SA_CVO~L` (laptop). `round-close-check --round 11` reads 3 of 3 judgments graded, MAY-CLOSE. The three are:
- CTaa2-AC2 **NOT MET** (C-S38, ADJUDICATION_v13);
- TO-APPLY-9 AC2 and TO-APPLY-31 AC2 MET (C-S16, C-S17).

The issuer closed TO-CT-aa-2 at 15:31Z with the judgment "awaiting the CVO". C-S38 was already committed (3e64efb328), and the
summary file is unchanged since 98e48fcbb2. The NOT MET stands: the summary still omits the records' "no network egress
control" limit.

Two gating items were undispositioned. **S9117 and S9118 are GRADUATED** (C-S39; rows in `remediations/REMEDIATION_v5.md`).
All 70 gating items are now dispositioned. S9115 and S9116 are INERT. S9116 records the Dev clause as "defence-in-depth"; PRD
v0.28 supersedes that label (signed @fa38dbaddb): the clause is a widening, and CT-aa-5 removes it.

<sweep_watermark>2026-10-12T18:15Z</sweep_watermark>

```json
[
  {
    "id": "NFRA_CTLPLN-C-S39",
    "project": "NFRA_CTLPLN",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO~L",
    "surfaced_at": "2026-10-12T18:15Z",
    "one_line": "S9117 and S9118 GRADUATED: kill-agent.ps1 and kill-maint.ps1 both kill whole process trees with no seat boundary; the interim rule is MSTR's and in force, and the permanent fix is COO~C's round-12 cell.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "A kill by serial ends only that seat.",
    "world_is": ".tools/kill-agent.ps1:159-187 (Stop-ProcessTree recursing through every child) and .tools/kill-maint.ps1:722 (`taskkill.exe /T /F /PID`) read at HEAD. Neither checks a descendant's serial. S9117 measured 5 seats (12 pids) lost on dell2 from one kill; S9118 has no loss measured yet. Both rows name the interim rule (0.0.0_AB_MSTR) and the permanent owner (2.0.0_SA_COO~C).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        ".tools/kill-agent.ps1:159-187 and .tools/kill-maint.ps1:720-724 read by this seat at HEAD",
        "INVESTIGATION_v1.md rows S9117 and S9118"
      ]
    },
    "adjudicates": [
      "NFRA_CTLPLN-S9117",
      "NFRA_CTLPLN-S9118"
    ],
    "disposition": "GRADUATED"
  }
]
```
