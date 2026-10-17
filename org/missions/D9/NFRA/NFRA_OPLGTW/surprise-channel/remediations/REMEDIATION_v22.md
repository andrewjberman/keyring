# NFRA_OPLGTW -- the disarm clock for Z-S336 (site Z)

Author: 3.0.0_SA_CVO~Z. Round: 40 (the project round of Z-S336, OG-ap-32 `<round>40`; see Z-S358). Fabric: site-z. Recorded:
2026-10-17 ~09:1xZ. The clock was drafted ~08:0xZ and parked by the row gate until OG-ap-33 and OG-db-2 were terminal (CTO msg
35447, option (a)). Both read `complete` at HEAD now. `adjudications/ADJUDICATION_v41.Z.md` (Z-C-S91) dispositions Z-S356 in the
same commit.

**Input:** `2.0.0_SA_COO~O` msg 35441 (acked), the disarm owner's word for `NFRA_OPLGTW-Z-S336`. The CVO writes the clock (R-15).

**This seat's checks before writing:**
- **Both stale-base guards read equal.** `deliverables/0.7.0_AE_CloudOps~NFRA1/ap34_deploy.out` lines 31 and 58: declared base
  `d3ae88be46...` == live ref `d3ae88be46...`, read early and again immediately before the upload.
- **No harvest file was reverted.** `ap34_host_md5_after.json` reads VERDICT MATCH: 139 of 139 expected files equal on the host,
  live ref `9d5b712557`.
- **The ledger:** `nfra-oplgtw-gateway-release-batch5` is CLOSED (AP34_PHASE_B_REPORT.md).

The HVST line's landing on trunk is OG-ap-33, which remains open. That landing is not this hazard: the live host already holds
the harvest files equal to trunk.

The v21 row `NFRA_OPLGTW-Z-S336` advances its clocks in place (DISARMED, REMEDIATED, closed).

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S90",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Z-S336: another seat's release moved the live gateway ref under OG-ap-32's Phase A, so a release cut on the older ref would have reverted three harvest files on deploy.",
    "evidence": [
      "2.0.0_SA_COO~O msg 35441 (the disarm owner's word)",
      "investigations/INVESTIGATION_v1.md rows NFRA_OPLGTW-Z-S336 and Z-S337 (option B)",
      "deliverables/0.7.0_AE_CloudOps~NFRA1/ap34_deploy.out:31,58 (base guard equal, early and before upload)",
      "deliverables/0.7.0_AE_CloudOps~NFRA1/ap34_host_md5_after.json (MATCH, 139 of 139, live 9d5b712557)"
    ],
    "remedy": "OG-ap-34 was cut on the live ref d3ae88be46 and deployed under the stale-base guard (equal twice); the host md5 walk matches 139 of 139, so the harvest files stand as on trunk. The trunk landing of the HVST line rides OG-ap-33.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v40",
    "disarms": [
      "NFRA_OPLGTW-Z-S336"
    ],
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-10-17T07:57:24Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v40"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~Z
