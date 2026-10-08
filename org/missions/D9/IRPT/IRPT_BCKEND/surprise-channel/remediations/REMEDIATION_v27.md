# IRPT_BCKEND -- project sweep 18 remediations

<sweep_watermark>2026-10-08T18:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-08 ~18:1xZ. Graduated at sweep 18 (ADJUDICATION_v35.md), round label v79. 2 rows:
D2-W172-S3 OPEN (re-scoped to a repin), D2-S3 ARMED (shared-tree residue).

```json
[
  {
    "id": "IRPT_BCKEND-D2-W172-S3",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The live irpt-export-render packages reports/repository.py at pin 83e8b9577a, whose KINDS is (PERFORMANCE, ANALYSIS), so an owner read of a CUSTODY_REPORT record fails closed with DEPENDENCY_UNAVAILABLE. HEAD already carries CUSTODY_REPORT in KINDS (b13bab7495, IB-pr-336); the source-map row was never repinned past it.",
    "evidence": [
      "investigation rows IRPT_BCKEND-D2-W172-S3, IRPT_BCKEND-D2-S2",
      "infra/aws/lambda/ci/lambda-source-map.json at HEAD: irpt-export-render repository.py repo_path reports/repository.py pin 83e8b9577a; git show 83e8b9577a:<path> KINDS line lacks CUSTODY_REPORT; HEAD line 16 carries it; b13bab7495 not an ancestor of 80a79a7462 (this compile)"
    ],
    "remedy": "Repin irpt-export-render's reports/repository.py row to a commit carrying b13bab7495 (census the rest of that file's diff), add any custody family the read path's reporting policy checks, and release under its own pair with an owner read of a real retained custody report as the after-read (CTO E1 criterion 3).",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v79",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v79"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-D2-S3",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Build residue in the dell2 shared tree's export/ source dir: 32 untracked staging copies and a modified tracked entry.py that removes the live custody-report route lines. A commit of entry.py, or a working-tree parity check over export/, carries it.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-S3 (3.0.0_SA_CVO)",
      "git status / git diff on dell2 CLOUD, 2026-10-08 ~18:1xZ; the release is unaffected (census changed_members=0 at 1e0cdaf90c)"
    ],
    "remedy": "The export lane confirms the residue is no live seat's work, restores export/entry.py to HEAD and removes the untracked copies; whichever build staged into the source dir is pointed at a temp dir.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v79",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v79"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~P2",
      "at": "2026-10-08T18:30:00Z"
    }
  }
]
```
