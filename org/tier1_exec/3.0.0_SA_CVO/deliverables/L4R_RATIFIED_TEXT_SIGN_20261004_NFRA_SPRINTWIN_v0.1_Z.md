# L4-R ratified-text half -- NFRA_SPRINTWIN v0.1 -- SIGN, with two CONTRACTS amendments owed before H3

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-04 ~19:5xZ, after the site-Z relaunch
**Delivery:** `1.0.0_SA_CTO~Z` msgs 29173 and 29174 at `b72b0dbf30`. HEAD is `bbfd37b595`, which changed only the header (seats).
The ratified-text half hash, recomputed by this seat, is `5d3955112dd8` at both pins. The ENDPOINT hash is `8f2a0e0dd91c`.
**Form:** proportionate (CLAUDE.md rule 27). Both halves bind to the ENDPOINT hash alone (`.tools/prd_signoff_lib.py:116-118`), so
the two amendments below are CONTRACTS edits and re-open nothing.

## What holds (checked at HEAD)

- **ENDPOINT.** FWD-1..7 match the seven one-line summaries in Andrew's record
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_18xxZ_NFRA_SPRINTWIN_ENDPOINT_CONFIRMED.md`) one for one. The
  record holds summaries, not the presented text, so "verbatim" is checked only at that grain.
- **C-NAMES.** The builders reproduce: `opal-sprint-daily`, `opal-daily-sprint-scheduler-role`, and the refusal
  "source 'daily-sprint' is not a systems.json key" word for word. `sprint` is refused the same way today, which is H0's row.
- **C-ONE-PIPELINE.** The cited functions exist: `commit_census.py` `bin_of` :63, `classify` :151; `project_census.py`
  `commits_for` :125, `classify` :145. The "two censuses disagree" refusal is `lambda_function.py:287`.
- **C-SCHEDULE.** The fixed summer offset it removes is `lambda_function.py:550` (`timedelta(hours=-4)`). The old rule is
  `aws_cloudwatch_event_rule.sprint` (`main.tf:212`).
- **C-SERVED.** Keep-last-5 is `aws_ecr_lifecycle_policy.sprint`, `countNumber = 5` (`main.tf:103`).
- **C-WINDOW axis.** The bin count is derived from the span (`commit_census.py:55`), so the axis spans any window; "48 bins" is the
  24-hour case.

## Findings

1. **C-WINDOW: `window_end` is not defined, and the run time loses work. Amendment owed before H3.**
   The device census runs at 15:55 ET (retry 16:02). The report runs at 16:10. Take an unpushed commit made on a device after that
   device's census and before the run. It is inside the window but in no census file. The next window starts after it, and C-UNION
   keeps only rows inside the window. So it is lost for good, even after a later push. That breaks FWD-2's "nothing missed".
   **Fix:** `window_end` = the earliest `generated_at` among the devices that reported, and never later than the run. The gap then
   falls into the next window, where it is counted once.
2. **C-CENSUS / H3: a 48-hour look-back cannot serve a 7-day window. Amendment owed before H3.**
   H3 downloads "the day's census files", and each file looks back 48 hours. C-WINDOW allows a window of up to 7 days. Any window
   longer than about 48 hours loses the older unpushed commits. Two skipped runs are enough. With finding 1 applied, one skipped run
   is already at the edge, because the census time varies (15:55 or 16:02). The brief carried this in (D3: "the 48 hours cover the
   report window plus margin", which assumed a 24-hour window).
   **Fix, either one:** H3 unions every census file dated inside the window (deduplicated by sha), or the look-back covers the cap
   (8 days).
3. **L9 basis (this seat's lane, not an ENDPOINT edit).** FWD-2's DONE WHEN compares the reports with "git's own total for the
   whole span". The pushed history cannot see an unpushed commit, so that test passes with finding 1 unfixed. At L9 this seat grades
   FWD-2 with one unpushed commit made after a device's census and before the run. It must appear in exactly one report.
4. **Placement (CTO).** C-SERVED puts the first served publish under a never-widen pair (COO + CTO; CLAUDE.md NEVER-1). After the solo
   change, the header names only the CTO half (`1.0.0_SA_CTO~Z`). The COO half has no named holder. Name one before that publish.
5. **Citation.** The solo-build record the header cites
   (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261004_184xZ_NFRA_SPRINTWIN_CRO_Z_BUILDS_SOLO.md`) is not at HEAD.
   It is on branch `croz-sprint-census-20261004` and resolves when that branch drains.

## Why SIGN and not REFUSE

The ENDPOINT is faithful to Andrew's word, and every contract that H0-H2 build on holds. Findings 1 and 2 bind at H3, and fixing them
is a CONTRACTS edit that re-opens no half. A refusal would add a round trip to a solo build Andrew ordered and change nothing that
the amendment does not. This seat grades H3 against the amended text, and FWD-2 per finding 3.

**Verdict: SIGN.**

-- 3.0.0_SA_CVO~Z
