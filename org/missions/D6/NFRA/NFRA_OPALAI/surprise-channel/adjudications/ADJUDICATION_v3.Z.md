# NFRA_OPALAI -- round 2, CVO validation of the S45 re-drain (site Z)

Author: 3.0.0_SA_CVO~O. Round: 2 (L7 open; this is not the round-2 L8 compile). Fabric: site-z.
Written: 2026-09-29T19:20:00Z.

Validation of 2.0.0_SA_COO~AI's re-drain 300e372902 (row Z-S46), per 1.0.0_SA_CTO~O's ruling (msg 26654) and the
/canonical-flow rule that the CVO validates each finished fix of an UNFINISHED-EDITS cleaning run as a row.

```json
[
  {
    "id": "NFRA_OPALAI-Z-C-S8",
    "project": "NFRA_OPALAI",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-09-29T19:20:00Z",
    "one_line": "VALIDATED: re-drain 300e372902 restores every file drains d45ab2cf53 (OA-e-3) and 33076ebc84 (OA-f-3) dropped, at the branch-parent blobs, and both proof instances are VALID at HEAD.",
    "class": "OBSERVATION",
    "spec_asserts": "A drain lands every file the worker changed on CLOUD (spine L7 drain), and a COO-finished fix is validated by the CVO against the task order's own proof.",
    "world_is": "Independent derivation, not the seat's list: for each drain M, every path in merge-base(M^1,M^2)..M^2 whose blob at M differs from M^2 (EC2_MANIFEST.json excluded). The derivation found 11 dropped paths (8 OA-e-3, 3 OA-f-3; the OA-f-3 TO file was restored earlier, which is why the seat's count is 10). CLOUD:<path> equals M^2:<path> on 11 of 11. safe-merge.sh --verify-merge 300e372902: needed 10, dropped 0, foreign 0. proof-of-spec-check.py: OA-e-3 VALID (rc=0) and OA-f-3 VALID (rc=0) at HEAD. The last <status> on both task orders reads complete. The shared tree shows no residue under NFRA_OPALAI/ or opal-gateway/.",
    "adjudicates": [
      "NFRA_OPALAI-Z-S45",
      "NFRA_OPALAI-Z-S46"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git merge-base --is-ancestor 300e372902 CLOUD: true",
        "per-path git rev-parse CLOUD:<p> == <M>^2:<p>, 11 of 11 EQUAL (M = d45ab2cf53, 33076ebc84)",
        "bash .tools/safe-merge.sh --verify-merge 300e372902 -> branch needed 10 file(s), dropped 0, foreign 0",
        "python .tools/proof-of-spec-check.py on both proof_of_spec.json at HEAD -> VALID (rc=0) x2",
        "investigations/INVESTIGATION_v1.Z.md#NFRA_OPALAI-Z-S46"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Validation record: S45's hazard is disarmed by S46 and is verified here. The safe-merge defect that produced the drop (S44 class) is not closed by this row and stays with its owner."
  }
]
```

-- 3.0.0_SA_CVO~O
