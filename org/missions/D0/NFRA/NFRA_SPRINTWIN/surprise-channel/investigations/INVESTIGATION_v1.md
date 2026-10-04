# NFRA_SPRINTWIN -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `4.0.0_SA_CRO~Z`, the project's solo builder (Andrew-direct ~18:4xZ 2026-10-04), at hop H4, 2026-10-04.
**Home:** the project tree's channel. Lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row.
**Append-only during the round.**

**Id grammar on this fabric:** a seat's row is `NFRA_SPRINTWIN-Z-S<k>`; every new row carries `"project": "NFRA_SPRINTWIN"` and
`"fabric": "site-z"`. The CVO's rows live in `adjudications/`, never here.

**Denominator at this write: 1 row**, `-Z-S1`, by `4.0.0_SA_CRO~Z`.

THIS FILE MUST STAY ONE FENCED JSON BLOCK. An appender targets the FIRST block only, and appends INSIDE the array.

```json
  [
    {
      "id": "NFRA_SPRINTWIN-Z-S1",
      "project": "NFRA_SPRINTWIN",
      "fabric": "site-z",
      "surfaced_by": "4.0.0_SA_CRO~Z",
      "surfaced_at": "2026-10-04T20:30Z",
      "one_line": "The area chart labels its hour ticks as hours since 00:00 (String(h%24)), so a window that starts at the previous report (16:10) would read 00, 01, ... over an afternoon-to-afternoon axis; the renderer needed one change beyond its bins.",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
        "status": "GROUNDED",
        "evidence": [
          "daily_reports/templates/_shared_viz.js AREA(): lab=String(h%24).padStart(2,'0') @8032cd9a61 -- the tick label counts hours from 00:00",
          "daily_reports/scripts/commit_census.py timeline_frame(): start/end are the window's own HH:MM in New York time @493b50dde5",
          "fixed @608559d4fe: the label is the hour of tl.start + h; a 00:00 start labels as before"
        ]
      },
      "disposition": "GRADUATED",
      "disarm_owner": "4.0.0_SA_CRO~Z",
      "spec_asserts": "Brief PART VII and PRD 'WHAT THIS PRD DOES NOT CLAIM': the window change needs nothing from the renderer beyond its existing bins -- an inference left to H4's render to prove or disprove.",
      "world_is": "The bins and the series assertion hold unchanged, but the axis labels assumed a midnight start. One line in _shared_viz.js now derives the label from tl.start. The schema's timeline description ('from 00:00 Eastern through now') is prose only and was not edited.",
      "notes": "Fixed inside round 1 by the builder; the H4 render of the QA page is the check that the axis reads from the window's start."
    }
  ]
```
