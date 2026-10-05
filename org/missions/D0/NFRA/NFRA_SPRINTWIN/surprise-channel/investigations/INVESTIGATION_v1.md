# NFRA_SPRINTWIN -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `4.0.0_SA_CRO~Z`, the project's solo builder (Andrew-direct ~18:4xZ 2026-10-04), at hop H4, 2026-10-04.
**Home:** the project tree's channel. Lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row.
**Append-only during the round.**

**Id grammar on this fabric:** a seat's row is `NFRA_SPRINTWIN-Z-S<k>`; every new row carries `"project": "NFRA_SPRINTWIN"` and
`"fabric": "site-z"`. The CVO's rows live in `adjudications/`, never here.

**Denominator at this write: 5 rows**, `-Z-S1` to `-Z-S5`, all by `4.0.0_SA_CRO~Z`.

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
    },
    {
      "id": "NFRA_SPRINTWIN-Z-S4",
      "project": "NFRA_SPRINTWIN",
      "fabric": "site-z",
      "surfaced_by": "4.0.0_SA_CRO~Z",
      "surfaced_at": "2026-10-04T21:52Z",
      "one_line": "The model wrote a flow diagram's break_after as a stage NAME ('Answers'); the renderer expects an index, so the break marker's cx is NaN and the '!' badge does not draw -- the derived viz contract and the render gate both passed it.",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
        "status": "GROUNDED",
        "evidence": [
          "QA page 2026-10-04 (s3://opal-data-portal-v2/sprint/global/platinum/qa_page/date=2026-10-04/) report JSON: viz {type flow, params.break_after 'Answers', stages [Research, Answers, Overview, Stored]}",
          "daily_reports/templates/_shared_viz.js V.flow :88 bx=xi(p.break_after)+w+gap/2 -- arithmetic on the param; headless console: '<circle> attribute cx: Expected length, NaN'",
          "control: the served 2026-10-03 and 2026-10-04 pages (old image) render with 0 console errors"
        ]
      },
      "disposition": "UNDER_INVESTIGATION",
      "disarm_owner": "4.0.0_SA_CRO~Z",
      "spec_asserts": "The function's render gate (render_daily_report.py + viz_contract.derive()) refuses any report whose diagrams would paint wrong.",
      "world_is": "The contract checks that break_after is present, not that it is an integer index; a name passes and paints one badge at NaN. Not caused by this project's changes (model output); cosmetic, one marker on one diagram.",
      "notes": "Off-thread for NFRA_SPRINTWIN; the template and viz contract are the CTO's surface. Candidate fixes: viz_contract types break_after as an integer, or V.flow accepts a stage name by indexOf. Routed in the round-1 enrichment list."
    },
    {
      "id": "NFRA_SPRINTWIN-Z-S5",
      "project": "NFRA_SPRINTWIN",
      "fabric": "site-z",
      "surfaced_by": "4.0.0_SA_CRO~Z",
      "surfaced_at": "2026-10-04T23:00Z",
      "one_line": "After a safe-merge drain into the shared tree, the shared INDEX still held the merged paths at their PRE-merge blobs (and a staged deletion of a file the merge added): any commit that swept the index would have silently reverted the drain.",
      "class": "OBSERVATION",
      "hazard_standing": "INERT",
      "grounding": {
        "status": "GROUNDED",
        "evidence": [
          "after drain 5ea9119863 (LDO-001 republish redraft): data/transcripts/scripts/teams_chat/tenant.py HEAD=ff676a532b WORKTREE=ff676a532b INDEX=5a6c4a7203 (the 2e2940a4cc blob); assist.py HEAD=c25d333c7b INDEX=88db0c8874; tests/test_teams_chat_eod_republish.py staged D",
          "git status read MM on both files; git diff --cached showed the drain's own change reversed (12 insertions, 58 deletions)",
          "disarmed 2026-10-04 ~23:00Z: git restore --staged on the three paths; INDEX == HEAD after; worktree untouched",
          "same class as 2.0.0_SA_COO~X msg 29189 earlier today: 5 stale AMGT_CORPUS index entries 'left by the parity integration'"
        ]
      },
      "disposition": "UNDER_INVESTIGATION",
      "disarm_owner": "4.0.0_SA_CRO~Z",
      "spec_asserts": ".tools/safe-merge.sh: the merge is committed from the index snapshot taken right after the merge, so a peer's later staging cannot enter it -- read as: the shared tree is left consistent after a drain.",
      "world_is": "The commit was right (tree check: needed 3, dropped 0, foreign 0) but the shared index was left behind HEAD for the merged paths. Observed on this seat's drain; whether every safe-merge drain leaves it, or only one racing a peer's commit, is not measured.",
      "notes": "Off-task for this project; the tool is 2.0.0_SA_COO's. A drain that reads git diff --cached --name-status after MERGED would see it; a sweep commit (git commit -a, or safe-commit with no pathspec) would ship the revert."
    }
  ]
```
