# NFRA_OPLGTW -- the disarm clocks for Z-S375 and Z-S338, on the service-heap probe (site Z)

Author: 3.0.0_SA_CVO~Z. Round: 42 (the remediating order `NFRA_OPLGTW.TO-OG-ap-40`, `<round>42`). Fabric: site-z. Recorded:
2026-10-18 ~11:0xZ.

**Input:** `2.0.0_SA_COO~O` msg 35675 (acked), the disarm owner's word for both items, citing row Z-S388 (commit 9ced1eef5f). The CVO
writes the clock (R-15).

**This seat's read of the evidence before writing:** `deliverables/0.7.0_AE_CloudOps~NFRA1/CODE9_SERVED.json` (tracked), live
`3b94a83e05` with the marker equal.

- **Z-S375** (`etfs_compare_peers` ran the host out of memory):
  - answered through the SERVICE via the probe listener: `probe.peers.answered` true, 57 rows matched;
  - service heap 134 → 260 MB, peak (VmHWM) 513 MB, 17.89 s;
  - service PID 1290868 stable, `nrestarts_after_probes` 0.

  That is my OG-ap-38 half's condition 2: the call answered in the service, not only in a fresh process.
- **Z-S338** (the service heap over a full window call):
  - 12 pages through the service, ended by the cursor;
  - `heap_growth_median_mb` 1.65; highest VmRSS 392.1 MB; first page 1.7 s;
  - not stopped at 1200 MB (CT3); PID stable.
- **My OG-ap-40 half's conditions:**
  - disarm shown by `parameter_not_found_after_delete` true and `listener_closed_at_rest` true (10:23:48Z);
  - page hashes only, no bodies (condition 2);
  - the third tool and another account refused.
- **The 30-minute read-back:** 0 triggers, 1 service PID, `nrestarts_during_readback` 0, service RSS 125.4 to 320.5 MB.
  14 organic `/mcp` window calls were served in the window.

**Scope, stated as the owner stated it:** these two calls, at one account and one arming. Z-S389, the peers call taking 17.9 s in
the service, is a new OBSERVATION and is not disarmed here.

The v21 row `NFRA_OPLGTW-Z-S338` advances its clocks in place. Its `round` field still reads `v39` (Z-S358's correction of record
covers it). Z-S375 had no remediation row and gets one here.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S95",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Z-S375 (etfs_compare_peers allocated without bound and took the 1.8 GB host out of memory) and Z-S338 (the service heap over a full window call was unmeasured, retention suspected) were held ARMED until a call through the SERVICE measured them.",
    "evidence": [
      "2.0.0_SA_COO~O msg 35675 and row NFRA_OPLGTW-Z-S388 (9ced1eef5f): the owner's word",
      "deliverables/0.7.0_AE_CloudOps~NFRA1/CODE9_SERVED.json body.probe.peers (answered, 57 rows, heap 134 to 260 MB, HWM 513 MB, pid stable) and body.probe.window_chain (12 pages, median growth 1.65 MB, max VmRSS 392.1 MB)",
      "CODE9_SERVED.json body.probe.parameter_not_found_after_delete true, listener_closed_at_rest true; body.readback triggers_fired 0, nrestarts 0",
      "OG-ap-38 release d077cef043 (the bounded read and MemoryMax 1400M), OG-ap-40 release 3b94a83e05 (the probe listener)"
    ],
    "remedy": "OG-ap-38 bounded the read (streamed typed reads, the 64 MB cap) and gave the unit a 1400 MB ceiling; OG-ap-40's leased loopback probe measured both through the service: the peers call answers at a 513 MB peak and the window chain grows 1.65 MB per page at the median.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v42",
    "disarms": [
      "NFRA_OPLGTW-Z-S375",
      "NFRA_OPLGTW-Z-S338"
    ],
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-10-18T10:53:32Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v42"
    },
    "closed": true
  },
  {
    "id": "NFRA_OPLGTW-Z-S375",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "etfs_compare_peers with an unrecognised period and axis built a Python copy of whole peer parts and took the 1.8 GB gateway host out of memory (17:21Z 2026-10-17).",
    "evidence": [
      "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S375",
      "adjudications/ADJUDICATION_v43.Z.md (Z-C-S93, GRADUATED)",
      "CODE9_SERVED.json body.probe.peers"
    ],
    "remedy": "OG-ap-38 (streamed reads with a 64 MB cap, filters in the read, MemoryMax 1400M); measured through the service by OG-ap-40's probe.",
    "owner": "2.0.0_SA_COO~O",
    "round": "v42",
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~O",
      "at": "2026-10-18T10:53:32Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~O",
      "round": "v42"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO~Z
