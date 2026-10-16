# OG-ev-1: 16 projected answer bodies for the CVO's AC3 markers, read from the installed code -- 0.7.0_AE_CloudOps~Z

**Date:** 2026-10-16
**Task Order:** NFRA_OPLGTW.TO-OG-ev-1
**Status:** COMPLETE (ev1.AC1 PASS); two markers cannot be shown as worded (rows Z-S168, Z-S169)

---

## Objective

Write `W/ANSWER_BODIES.json`: one projected answer body per marker of the AC3 judgment criteria of OG-ap-18, 19, 20, 21 and 23, read-only from the live host, so the CVO can grade what an answer says rather than which keys it has.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | not used | SKIPPED | every path was a known file or folder |
| comp-iam | not run | SKIPPED | the order declares no IAM change; no IAM was touched |

**What worked:** a discovery pass that printed shapes only, so the final harness could choose its arguments from the host's own answers; compressing the bodies (SSM returns ~24000 characters).
**What failed:** my first discovery pass printed an account reference into a file; I masked it before any commit. The first final run lacked the Schwab fourth body and picked the quiet name by row count.
**Gap found:** two markers name things the tools do not have (a `data_status` on the news tools; a Schwab catalog row).

---

## Work Completed

1. Discovery pass on the host (two runs, shapes only, W/EV1_DISCOVER2.json masked), then the final harness `ev1_answer_bodies.py` (run twice; the second run is the record).
2. The host scrubs every body before it leaves (numbers over 7 digits as separated strings, long digit runs hyphenated, person and contact keys, free-text article fields); a local second scrub masks UUID-shaped allocation ids (30 replaced).
3. Result: ap-18 3, ap-19 3, ap-20 3, ap-21 3, ap-23 4 bodies, each at most 12000 bytes; `ev1.AC1` PASS.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Recorded the real answer with a note for the two markers the tools cannot show | the order forbids substituting a different call; AC1 needs a body, so the body is the real quiet-day / Schwab answer and the note says why it does not show the marker |
| Ran the final harness twice | the first run had a defect of mine (no fourth ap-23 body; quiet name by rows); not a retry to force a marker |
| Masked account aliases in the recorded arguments | the alias is a vendor-issued string tied to an account |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `W/ANSWER_BODIES.json`, `ev1_meta.json` | the record | Yes -- local on `box/sitez` |
| `W/ev1_answer_bodies.py`, `ev1_final_run.py`, `ev1_discover.py`, `ev1_run.py`, `ev1_post_scrub.py` | the harnesses | Yes -- local |
| surprise rows `NFRA_OPLGTW-Z-S168` to `S171` | two BLOCKING, two OBSERVATION | Yes -- local |

---

## Blockers

None for this seat. The client-data account-id hash list is absent on this box (`~/.opal/account_id_hashes.txt`), so the commit hook could not check the file for client account ids: the file holds masked references (`****<last4>`) and position data of one client account. Read it before it is pushed or relayed.

---

## Current State

`W/ANSWER_BODIES.json` holds 16 bodies read from release `3d5c9c8bf1` on 2026-10-16T10:36Z. The CVO grades them; this seat grades nothing.

---

## Next Steps

1. **[2.0.0_SA_COO~O] Relay `W/ANSWER_BODIES.json` to the CVO** and rule rows Z-S168 and Z-S169.
2. **[2.0.0_SA_COO~O] Decide the cap wording** (row Z-S170: the tool caps news at 30 days; the criterion says 14).
3. **[0.0.0_AB_MSTR~Z] Push `box/sitez`** after reading the record once for client data.
