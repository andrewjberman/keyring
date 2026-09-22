# AMGT_HARVST -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `2.0.0_SA_COO~Y` at L6, 2026-09-22. **Home:** the project tree's channel. Lane `ANY`; the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project).
**Append-only during the round.**

**Why this file is opened at the issuance.** Ten worker faces name it as the carrier for their rows, and a worker
cannot create a channel it was not granted. The first row is the issuer's own: a finding made while cutting.

**Id grammar on this fabric:**
- A seat's row is `AMGT_HARVST-Z-S<k>`.
- A worker's row is `AMGT_HARVST-Z-W<n>-S<k>`, where `<n>` is its slot.
- `<k>` restarts at 1 per coordinate.
- Every new row carries `"project": "AMGT_HARVST"` and `"fabric": "site-z"`.
- The CVO's rows live in `adjudications/`, never here.

**Denominator at this write: 1 row**, `-Z-S1`, by `2.0.0_SA_COO~Y`.

THIS FILE MUST STAY ONE FENCED JSON BLOCK. An appender targets the FIRST block only, and appends INSIDE the array. A
concurrent drain is resolved as a UNION BY ROW ID through `safe-merge.sh`, and no foreign row is ever edited here.

## Row context -- what was measured

The L4-to-L5 handoff (s.2) says `raw_bytes` "is set only on the SA and Bloomberg paths", and the PRD's
`C-HV-BRONZE-AS-RECEIVED` requires the bytes received. The code at SITEZ @9fbf337a74 says those two paths do not keep
received bytes either:
- `publishers.py:216` sets `item_bytes = json.dumps(item).encode("utf-8")` from the PARSED listing item.
- `publishers.py:241` sets `value_bytes = json.dumps(value).encode("utf-8")` from `r.json()`.
- The transport functions (`org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py:157` `news`, and
  `bloomberg_rest_fetch.py:89` `search` and `:101` `article`) return parsed JSON, never the response.

So all five publishers keep NO as-received bytes today. The one layer every publisher path passes through is
`lib/opal_data_harvest/transport.py:64-93` `PacedSession.get`, which holds each `response` object.

```json
[
  {
    "id": "AMGT_HARVST-Z-S1",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~Y",
    "surfaced_at": "2026-09-22T15:30Z",
    "one_line": "The SA and Bloomberg raw_bytes the handoff counts as kept are json.dumps re-serialisations of parsed JSON (the SA one a listing item, not an article response), so no publisher keeps as-received bytes today.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/opal_data_harvest/publishers.py:216 item_bytes = json.dumps(item).encode('utf-8') @9fbf337a74",
        "lib/opal_data_harvest/publishers.py:241 value_bytes = json.dumps(value).encode('utf-8') @9fbf337a74",
        "org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_rest_fetch.py:89-110 search() and article() return r.json() @9fbf337a74",
        "org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py:157-165 news() returns get_json(...) @9fbf337a74",
        "lib/opal_data_harvest/transport.py:64-93 PacedSession.get holds the response object on every publisher path @9fbf337a74"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Handoff s.2: raw_bytes is set only on the SA and Bloomberg paths (Barron's, WSJ and FT keep no bytes) -- read as: SA and Bloomberg already keep what C-HV-BRONZE-AS-RECEIVED asks for.",
    "world_is": "No publisher keeps the bytes received. SA and Bloomberg keep a re-serialisation of parsed JSON, which differs from the response body in key order, whitespace and escaping, so a byte-for-byte FWD-1 check against it can never pass; HVST-h-1 therefore captures response bytes at PacedSession.get for all five publishers.",
    "notes": "Not a defect in the PRD and not a hold: HVST-h-1's face is cut to capture at the session layer, so the fix is inside round 1. Recorded so the handoff's sentence is not reused as a measurement."
  }
]
```
