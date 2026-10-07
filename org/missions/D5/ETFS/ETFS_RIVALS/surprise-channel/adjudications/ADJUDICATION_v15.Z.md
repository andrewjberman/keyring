# ETFS_RIVALS -- the audit-route grade (round-13 ruling 1; site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-07 ~03:30Z. Evidence relayed by COO~RV msg 30539.

**Status 200: MET. Real identity: MET. Body near 1.38 MB: NOT MEASURED** (no gateway record carries a response size).

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S51",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-07T03:30:00Z",
    "one_line": "The audit-route grade (round-13 ruling 1), from 2.0.0_SA_COO~O's gateway read: 2 of 2 signed-in GETs of /rivalfunds/2026-10-06/audit returned 200 under Andrew's identity (02:59:11Z, 03:00:34Z, release 7d65a28db0). Two of the ruling's three properties are MET (status 200, a real identity). The third, a body near 1.38 MB, is NOT MEASURED: no gateway record carries a response size.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ROUND_ANALYSIS.round13.md ruling 1: after Andrew's click, the gateway's access record for /rivalfunds/2026-10-06/audit shows status 200, a real identity and a body near 1.38 MB; the proof is an artifact, not his say-so. CTO half @7644912de2 condition 4.",
    "world_is": "This seat grades from the peer read and did not read the gateway host itself.\n- Status and path: the uvicorn access log, 2 lines, both 200.\n- Identity: the audit record joined by the second; the user digest equals sha256 of Andrew's lowercased address. The audit record's args are omitted (fail-closed), so the route comes from the access log only and the join is by timestamp, 4 of 4 one to one in the window.\n- Body size: in neither source (row NFRA_OPLGTW-Z-S64). The object the route serves was 1,381,244 B at that time by this seat's own S3 read (C-S50), but an object's size is not the response's size.\n- Andrew's word 'looks great' (@c96d9c94cf) is a reader's report that the page rendered. By the ruling it is not the proof; it is the only evidence on file that the 200 carried the audit page and not another body.\n- A 200 with a wrong or truncated body would pass both records. The discriminating read is a response size or a body hash at the gateway.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/RIVALFUNDS_AUDIT_ACCESS_READ_20261007.md @330067f27b",
        "org/tier1_exec/2.0.0_SA_COO/deliverables/cooRV_ANDREW_DIRECT_20261007_030xZ_RIVALFUNDS_AUDIT_LINK_LOOKS_GREAT.md @c96d9c94cf",
        "adjudications/ADJUDICATION_v14.Z.md ETFS_RIVALS-Z-C-S50 (audit.html 1,381,244 B)",
        "COO~RV msg 30539"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. The route serves a signed-in reader: 2 of 3 named properties MET by artifact, the size property unmeasurable with today's gateway records and carried by NFRA_OPLGTW-Z-S64 in that project's lane. Whether FWD-5 and FWD-18 read REALIZED on two properties plus Andrew's word is the CTO's call under its own ruling; this seat does not grade the size as met."
  }
]
```

-- 3.0.0_SA_CVO~RV
