# NFRA_SPRINTWIN ROUND 1 -- L8 COMPILE + L9 -- FWD-1 PASS: the live thread counts 386 commits over the union, and git agrees to the commit (336 pushed + 2 site-Z + 48 laptop not yet pushed)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-04 ~22:1xZ
**Input:** `4.0.0_SA_CRO~Z`'s message of 21:57Z (solo build, no COO lane), naming ledger `sprintwin-union-20261004`, CLOSED @`709caf16b1`
(4 legs), and rows Z-S1 to Z-S4. The served re-run of 2026-10-04 at 21:55Z ran under Addendum A, with both halves signed
(COO @`7fa231405f`; CTO @`cd417a0586` and @`a647b1dcdf`).

## FWD-1 -- what this seat read (not taken from the ledger)

**The watermark at the QA home** (`s3://opal-data-portal-v2/sprint/global/platinum/qa_page/date=2026-10-04/watermark.json`, 477 B):
- window `2026-10-03T21:05:36Z` .. `2026-10-04T21:05:36Z`;
- devices_reported sitez 21:05:36Z and laptop 21:34:58Z; devices_missing none;
- commits 386, unpushed 50 (laptop 48, sitez 2); origin_head `b7f2fb4dc7`.

`window_end` equals the EARLIER of the two census times, which is the v0.2 C-WINDOW amendment this seat asked for.

**Git's own count over the same window:**

| set | count | instrument |
|---|---|---|
| reachable from `b7f2fb4dc7`, no merges, commit time in the window | **336** | `git log` on this device |
| site Z, `--all`, in the window, not reachable from `b7f2fb4dc7` | **2** | `git log --all` on this device |
| laptop census (`s3://opal-data-assets/sprint/global/bronze/device_census/date=2026-10-04/laptop.json`, generated 21:34:58Z, 7,860 rows), in the window, not reachable from `b7f2fb4dc7` | **48** | this seat's join |
| **union** | **386** | equals the report's 386 and its 50 unpushed (48 + 2) |

**The page** (Desktop html, 47,941 B). Its source line reads: "Oct 3 5:05 PM to Oct 4 5:05 PM ET: 386 commits, 46 workers; pushed
history plus device censuses from site Z (5:05 PM), laptop (5:34 PM); 50 of 386 counted commits not yet pushed". It names both
computers, with their census times, and the unpushed count.

**The rest of DONE WHEN:**
- Each device's list was written by its own script: both census files are on S3 with their `device` and `generated_at`.
- The cloud job ran over the union, which the count above shows.
- The page was rendered and read: the CRO's headless render; this seat read its text.
- No fixture: every input is a real census and the real clone.

**Grade: FWD-1 PASS. A REALIZED candidate.**

## Observations (no row owed by this seat)

- **The site-Z census key is overwritten within the day.** `sitez.json` now reads generated 21:51:00Z, because the served re-run wrote
  over the 21:05:36Z copy that the QA trace read. So the trace's site-Z input is no longer stored as it was read. The counts still
  reproduce, because the watermark's window bounds them, but the evidence object is mutable. This matters for FWD-2's dated re-run, and
  it is left to the round-1 analysis.
- **The page reads `opal_ai UNAVAILABLE` for the other repos' subjects.** That is outside the FWD-1 counts, which cover ajb_workspace
  only.

## Rows

- Z-S1 and Z-S3 are GRADUATED by their author.
- Z-S2 (an empty pinned copy exits 0; it binds FWD-7) and Z-S4 (a NaN break marker) are INERT and UNDER_INVESTIGATION with
  `4.0.0_SA_CRO~Z`. They are for the analysis.

## L10 PRECONDITION

- The one ledger is CLOSED (4 of 4 legs).
- `python .tools/comp-surprise.py --armed --project NFRA_SPRINTWIN`: ARMED 0, 4 items, 0 defects.
- 0 BLOCKING rows.

**MET.**

```json
[
  {
    "id": "NFRA_SPRINTWIN-Z-C-S1",
    "project": "NFRA_SPRINTWIN",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-04T22:10:00Z",
    "one_line": "Round 1 L8/L9: FWD-1 PASS -- QA watermark window 10-03 21:05:36Z..10-04 21:05:36Z (window_end = the earlier census), 386 commits / 50 unpushed; git agrees: 336 reachable from b7f2fb4dc7 + 2 site-Z-only + 48 laptop-census-only = 386; the page names both computers and the unpushed count.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-portal-v2/sprint/global/platinum/qa_page/date=2026-10-04/watermark.json and Desktop_DAILY_REPORT_2026-10-04.html",
        "git log --no-merges b7f2fb4dc7 over the window: 336; git log --all: 338 (2 not reachable from b7f2fb4dc7)",
        "s3://opal-data-assets/sprint/global/bronze/device_census/date=2026-10-04/laptop.json (generated 21:34:58Z): 384 rows in the window, 48 not reachable from b7f2fb4dc7"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A compile record: FWD-1 is graded on the served QA artifacts and an independent git count.",
    "spec_asserts": "FWD-1: the page shows work done on either computer, counted once, and says which computers reported.",
    "world_is": "386 counted once over the union; both computers named; 50 unpushed counted.",
    "notes": "The site-Z census key was overwritten at 21:51Z by the served re-run; left to the round-1 analysis for FWD-2."
  }
]
```

-- 3.0.0_SA_CVO~Z
