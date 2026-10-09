# IRPT_BCKEND -- round 95 remediations (~P)

<sweep_watermark>2026-10-09T04:32Z</sweep_watermark>

Graduated at round 95's L8 (ADJUDICATION_v44.md), round label v96: 2 rows, OPEN; one ARMED (fail-closed: a missing registry refuses, never widens).

```json
[
  {
    "id": "IRPT_BCKEND-D2-W196-S1",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The naming gate refused a typed 'cottonwood' in served.py, so the subject's firm is read through lib/opal_naming lookup(); a release zip without lib/ and the registry admits nobody (fails closed).",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-W196-S1",
      "safe-commit naming-gate REFUSE infra/aws/lambda/investor-reporting/_authz/served.py:265 cottonwood -> lookup('cottonwood') (LGIC_ENFORCE DEC-6), first commit attempt 2026-10-09 ~04:0xZ",
      "served.py _svc_custody_statement_firm() resolves lookup('cottonwood')['long'] by the maintained_sources._comparison_firms pattern (lib/ found in the tree or beside the module in a flat zip); the commit 7e0bfc3222 passes the gate; with lib/ absent the test control fails 5 of 23 (measured in a scratch copy without lib/)"
    ],
    "remedy": "Packaging confirmed in today's source map (this seat's read). It disarms at IB-pr-385's release pair: the built zip, imported offline, resolves cottonwood through lookup() and admits svc-custody-statement, with the negative control (registry removed, refused), per D2-S26.",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v96",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v96"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "0.7.0_AE_CloudOps~DELL2 (IB-pr-385 release pair)",
      "at": null
    }
  },
  {
    "id": "IRPT_BCKEND-D2-W197-S2",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The new Lambda's artifact registration (infra/aws/lambda/ci/lambda-source-map.json) and the commentary role's invoke attachment lie outside this order's <paths>, so the release pair must carry both.",
    "evidence": [
      "investigation row IRPT_BCKEND-D2-W197-S2",
      "infra/aws/terraform/investor-reporting/export/commentary_composition.tf header lists the artifact members the zip must carry.",
      "infra/aws/terraform/transcripts/commentary.tf owns outlook-global-commentary-draft-role (NAMES.json role.name) and its DecryptWithTheIrptKey statement; the order's <paths> hold neither that root nor ci/lambda-source-map.json."
    ],
    "remedy": "IB-pr-386's release pair carries both acts outside the cell's paths: register the composition-read zip in lambda-source-map.json, and attach the invoke policy to the commentary role from the transcripts root (dropping that role's unused kms:Decrypt on the irpt key).",
    "owner": "2.0.0_SA_COO~P2",
    "round": "v96",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~P2",
      "round": "v96"
    },
    "closed": false
  }
]
```
