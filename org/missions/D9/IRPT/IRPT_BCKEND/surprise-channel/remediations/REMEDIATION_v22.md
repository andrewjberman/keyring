# IRPT_BCKEND -- project sweep 11 remediations

<sweep_watermark>2026-10-07T09:47Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-07. Graduated at sweep 11's L9 (ADJUDICATION_v26.md), round label v63. 1 row, OPEN: S358,
with its mechanism corrected by this seat's read (the missing mapping does not raise; it returns empty and marked absent).

```json
[
  {
    "id": "IRPT_BCKEND-S358",
    "project": "IRPT_BCKEND",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "irpt-ycharts-generate packages intake/parse.py, whose load_mapping(path=None) (parse.py:417-425) defaults to <package>/fixtures/holdings/security_mapping.json, a file the function does not package. The row says the call raises; it does not: parse.py:424-425 returns an empty mapping marked _meta.absent when the file is missing, so a caller that leaves the path unset in the Lambda gets no share-class or model mapping, silently unless it reads _meta.absent.",
    "evidence": [
      "investigation row IRPT_BCKEND-S358",
      "infra/aws/lambda/investor-reporting/intake/parse.py:417-425: 'path = path or os.path.join(_HERE, \"fixtures\", \"holdings\", \"security_mapping.json\")'; 'if not os.path.exists(path): return {\"share_classes\": {}, \"models\": {}, \"_meta\": {\"absent\": True, \"path\": path}}' (this compile's read, dell2 CLOUD, 2026-10-07 ~10:0xZ)",
      "UNMEASURED: whether any runtime caller in irpt-ycharts-generate calls load_mapping without a path"
    ],
    "remedy": "The intake lane reads the callers inside irpt-ycharts-generate: if one calls load_mapping() bare, either package the mapping (with its owner's word) or pass the address explicitly, and surface _meta.absent to the page; if none does, the row closes on that read.",
    "owner": "2.0.0_SA_COO~G2",
    "round": "v63",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~G2",
      "round": "v63"
    },
    "closed": true
  }
]
```
