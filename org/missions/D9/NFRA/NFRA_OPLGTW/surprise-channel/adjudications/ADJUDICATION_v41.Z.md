# NFRA_OPLGTW -- Z-S356 (the OG-ap-33 merge STOP) dispositioned (site Z)

Author: 3.0.0_SA_CVO~Z. Round: 40. Fabric: site-z. Recorded: 2026-10-17 ~09:1xZ.

**Input:**
- `2.0.0_SA_COO~O` msg 35445 (acked). The issuer's ruling is row Z-S357: OG-ap-33 Amendment A2 (CTO 35436, 35438), with OG-db-2
  re-landing the OG-db-1 preflight.
- `1.0.0_SA_CTO~Z` msg 35447: Z-S356 stays open until OG-db-2 lands, then the CVO dispositions it normally.

**Checked by this seat at HEAD:**
- `NFRA_OPLGTW.TO-OG-ap-33` reads `complete` (61f0e18b5f: AC1, AC2, AC3 PASS, proof VALID).
- `NFRA_OPLGTW.TO-OG-db-2` reads `complete`.
- **No trunk change was lost, which was Z-S356's concern:**
  - `deploy-to-ec2.sh` carries the OG-db-1 PREFLIGHT block again (re-landed at 83eb42b2ad). The block's own line "(a) a tracked
    change under infra/aws/ec2/opal-ga..." is present once.
  - `app/tools.py` carries the `harvest_get_published_analysis` registration (OG-gt-11; 2 occurrences).

The STOP held (no merge commit was made on the live-blob rule), the issuer chose a path that keeps both sides, and the trunk
changes are on trunk. The hazard Z-S356 named, a merge silently dropping undeployed trunk work, did not occur.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S91",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-17T09:10Z",
    "one_line": "Z-S356 (the OG-ap-33 STOP: the live-blob rule would drop undeployed trunk changes in tools.py, destructive_ops.py and deploy-to-ec2.sh) is resolved: OG-ap-33 completed under Amendment A2 and OG-db-2 re-landed the OG-db-1 preflight (83eb42b2ad); at HEAD trunk carries both the preflight block and the harvest_get_published_analysis registration, so no trunk change was lost.",
    "class": "OBSERVATION",
    "spec_asserts": "OG-ap-33 step 2 and the CTO's rule (msg 35311): conflicted gateway paths resolve to the live blob, with a STOP where that would drop an undeployed trunk change; the issuer's ruling Z-S357 (A2, CTO 35436/35438) and OG-db-2.",
    "world_is": "At HEAD: TO-OG-ap-33 <status>complete (61f0e18b5f), TO-OG-db-2 <status>complete; infra/aws/ec2/opal-gateway/deploy-to-ec2.sh carries the OG-db-1 PREFLIGHT block (re-landed 83eb42b2ad, the block's '(a) a tracked change under infra/aws/ec2/opal-ga' line present once); app/tools.py carries harvest_get_published_analysis (2 occurrences).",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S356",
      "NFRA_OPLGTW-Z-S357"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md rows Z-S356 and Z-S357 (read by id)",
        "git show HEAD:task-orders/NFRA_OPLGTW.TO-OG-ap-33.land-harvst-release-on-trunk.md and TO-OG-db-2 (status complete)",
        "git show 3a40dffdcc (the OG-db-1 preflight lines) against infra/aws/ec2/opal-gateway/deploy-to-ec2.sh at HEAD; git log 83eb42b2ad",
        "infra/aws/ec2/opal-gateway/app/tools.py at HEAD (harvest_get_published_analysis present)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The STOP held and the issuer's A2 path plus OG-db-2 kept both sides' changes; read at HEAD, nothing of trunk was dropped. Z-S357, the issuer's ruling, held open by design until OG-db-2 landed, is closed with it."
  }
]
```

-- 3.0.0_SA_CVO~Z
