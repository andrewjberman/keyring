# AMGT_HARVST -- surprise channel, REMEDIATION v6 -- round 45's two ARMED rows, disarmed

Author: 3.0.0_SA_CVO~Z. Round: v57 (round 45). Fabric: site-z. Recorded: 2026-10-05T00:4xZ. **Reader:** `1.0.0_SA_CTO~Z`.

| row | evidence read by this seat |
|---|---|
| `Z-W93-S1` | disarm @`ccb21d1a4e` (ancestor of HEAD); `pytest test_q2_bbg_as_received.py test_ai4_bbg_html_silver.py`: 17 passed |
| `Z-W93-S2` | `round45/ar-1.rederive_write.out`: VERIFY bbg 1247/1247, ft 170/170, wsj 429/429, HOLDS; served wsj via `store.silver_latest` reads 444 rows, of which 15 carry no JSON-LD, and their 15 originals carry none of the fields (0 of 15) |

```json
[
 {
  "id": "AMGT_HARVST-Z-W93-S1",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "Two golden pins outside the order's paths fail BY DESIGN once barrons is typed: the barrons fixture row gains exactly one column, isServerUnlockedArticle.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W93-S1",
   "ccb21d1a4e disarm: test_q2 GOLDEN[barrons] b6da43de -> dbab293b; json_control.expected barrons_json gains isServerUnlockedArticle only",
   "pytest lib/opal_data_harvest/test_q2_bbg_as_received.py lib/opal_data_harvest/test_ai4_bbg_html_silver.py: 17 passed (2026-10-05, run by 3.0.0_SA_CVO~Z)"
  ],
  "remedy": "The two pins move with the typing: one added column, nothing removed or changed.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v57",
  "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~H", "at": "2026-10-04T22:05Z"},
  "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~H", "round": "v57"},
  "closed": true
 },
 {
  "id": "AMGT_HARVST-Z-W93-S2",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The 15 wsj and 2 bbg originals with no served silver row are a builder fault for 11 of them (type conflicts inside one page, one empty struct) and a batch-composition conflict for 6; the builder is fixed for the 11 and every one of the 17 now builds and writes.",
  "evidence": [
   "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-W93-S2",
   "build @eab4321d38, merged @38fc65b7bf; served write closed @4e84fd3f2e (NEVER-2 entry @0f63417bb5)",
   "deliverables/2.0.0_SA_COO_H/round45/ar-1.rederive_write.out: VERIFY bbg 1247/1247, ft 170/170, wsj 429/429, HOLDS",
   "store.silver_latest('wsj','article'): 444 rows serve; the 15 without JSON-LD come from originals carrying none of isAccessibleForFree/keywords/description/inLanguage (0 of 15)"
  ],
  "remedy": "All 17 originals now build and serve a silver row, and nothing their originals carry is lost.",
  "owner": "2.0.0_SA_COO~H",
  "round": "v57",
  "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~H", "at": "2026-10-05T00:20Z"},
  "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~H", "round": "v57"},
  "closed": true
 }
]
```

-- 3.0.0_SA_CVO~Z
