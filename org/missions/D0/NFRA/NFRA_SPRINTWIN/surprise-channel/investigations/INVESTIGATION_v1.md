# NFRA_SPRINTWIN -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `4.0.0_SA_CRO~Z`, the project's solo builder (Andrew-direct ~18:4xZ 2026-10-04), at hop H4, 2026-10-04.
**Home:** the project tree's channel. Lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row.
**Append-only during the round.**

**Id grammar on this fabric:** a seat's row is `NFRA_SPRINTWIN-Z-S<k>`; every new row carries `"project": "NFRA_SPRINTWIN"` and
`"fabric": "site-z"`. The CVO's rows live in `adjudications/`, never here.

**Denominator at this write: 3 rows**, `-Z-S1` to `-Z-S3`, all by `4.0.0_SA_CRO~Z`.

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
    },
    {
      "id": "NFRA_SPRINTWIN-Z-S2",
      "project": "NFRA_SPRINTWIN",
      "fabric": "site-z",
      "surfaced_by": "4.0.0_SA_CRO~Z",
      "surfaced_at": "2026-10-04T20:48Z",
      "one_line": "Under Git Bash, `git show origin/CLOUD:.tools/sprint-device-census.py > tmp` is path-converted to a bad revision, writes an EMPTY file, and `python tmp` then exits 0 having sent nothing -- a pinned-copy run that fails reads as a success.",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
        "status": "GROUNDED",
        "evidence": [
          "site Z 2026-10-04 ~20:47Z: git show printed fatal: ambiguous argument 'origin\\CLOUD;.tools\\sprint-device-census.py'; git hash-object of the temp file = e69de29bb2 (the empty blob); python on it rc=0",
          "the same command with MSYS_NO_PATHCONV=1: 7982 bytes, blob 103ad09a7d == origin/CLOUD's; census 8265 commits, put etag MATCH",
          "CLAUDE.md Git: MSYS_NO_PATHCONV=1 for git show <ref>:<path> with a slashed ref"
        ]
      },
      "disposition": "UNDER_INVESTIGATION",
      "disarm_owner": "4.0.0_SA_CRO~Z",
      "spec_asserts": "PRD C-CENSUS: the scheduled task runs the script as it stands on origin/CLOUD (git show origin/CLOUD:<script> to a temporary file) -- read as: that form either runs the pinned bytes or fails visibly.",
      "world_is": "Under MSYS the git show fails, the redirect leaves a zero-byte file, and Python runs it successfully. No census is written and nothing says so. INERT today: no Scheduled Task exists yet (FWD-7 enrichment).",
      "notes": "Binds FWD-7: each device's task must refuse a zero-byte or wrong-blob copy (compare git hash-object of the temp file with git rev-parse origin/CLOUD:<script>) before running it, and must not run under an MSYS shell without MSYS_NO_PATHCONV=1. FWD-5's page line then names the device as not reporting rather than counting on a silent pass."
    },
    {
      "id": "NFRA_SPRINTWIN-Z-S3",
      "project": "NFRA_SPRINTWIN",
      "fabric": "site-z",
      "surfaced_by": "4.0.0_SA_CRO~Z",
      "surfaced_at": "2026-10-04T21:05Z",
      "one_line": "The pinned (origin/CLOUD) copy of the device census still imported lib/opal_naming.py and its registry from the WORKING TREE, so a checkout behind origin failed to resolve its own S3 key.",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
        "status": "GROUNDED",
        "evidence": [
          "laptop 2026-10-04 20:56Z via 0.0.0_AB_MSTR~Z msg 29234: origin copy blob 103ad09a7d failed 'source sprint is not a systems.json key'; its tree was 80 commits behind origin 740fb88d8b",
          ".tools/sprint-device-census.py upload() @6ff1077ddd: sys.path.insert(0, os.path.join(root, 'lib')) -- the working tree's builder",
          "pinned_address() control: rev 43b01c88f8 -> REFUSED (no sprint row); rev 740fb88d8b -> the census key"
        ]
      },
      "disposition": "GRADUATED",
      "disarm_owner": "4.0.0_SA_CRO~Z",
      "spec_asserts": "PRD C-CENSUS / FWD-7: the scheduled task runs the script as it stands on origin/CLOUD, never the working tree, so a half-edited checkout cannot change what is sent.",
      "world_is": "The script's bytes were pinned but its address builder was not: the key depended on the checkout's registry. The failure was loud (no file written), not silent. Fixed in the builder fix commit by exporting the builder, schema and registry at the census's origin_cloud.",
      "notes": "Effective on each device once the fix is on origin. Until then the laptop's re-run after its merge of 740fb88d8b uses the working tree's (now current) registry."
    }
  ]
```
