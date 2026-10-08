# CTO never-widen half -- ETFS_RIVALS round 24: deploy RIV-cu-1 (the dialog chart's UI) at `f9f8334ef6`, one republish

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~21:1xZ. **Ask:** `2.0.0_SA_COO~RV` msg 31403.
**COO half:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round24/NEVER_WIDEN_HALF_COO_R24_DEPLOY.md` @47cbfebcf2
(SIGNED, conditional on J1). Its message was read; the file was read at one line (the before-set).

## VERDICT: SIGNED at pin `f9f8334ef6`, CONDITIONAL on RIV-cu-1 J1 MET on file by `3.0.0_SA_CVO~RV`. Two conditions.

Why this deploy at all: Andrew-direct ~19:0xZ, three asks on the chart
(`ANDREW_DIRECT_20261007_190xZ_RIVALFUNDS_SMOKED_POPUPS_GOOD_CHART_UI_NEXT.md`).

## What this seat read at signing

| read | result |
|---|---|
| the live base, `aws lambda list-functions` filtered to rivalfunds, 5 of 5 | all at 3,008 MB; hashes begin `cTM1SBuG` (daily), `99BqkcrG` (fetch), `tyGN8WS/` (canonical), `TLYlfz3r` (silver), `RHlHCL0l` (publish). The three the COO half names as its before-set are equal. |
| the pin | `6124b079f3` (live) is an ancestor of `f9f8334ef6`; the reverse is not (the control) |
| `git diff --stat 6124b079f3 f9f8334ef6` over the packaged paths | 11 files, +609/-144: `render.py` (67 lines) and its test are this round's. **Nine are riders from the origin pull-merge**: `lib/opal_naming.py` (+73) and `NAMING_SCHEMA.json`, and seven registry files (`root_map.json` +271, `systems.json` 190 lines, `key_rulings.json`, `exemptions.json`, `event_rules.json`, `legacy_addresses.json`, `resources.json`). |
| the script, in `render.py` at the pin | `fetch(` appears once in the file. The added lines hold one `http` string, the SVG namespace, which is not a request. No `src=`, `import(`, `XMLHttpRequest`, `WebSocket`, `sendBeacon`, `eval(`, storage or cookie use is added. |
| the plan text | `Plan: 0 to add, 5 to change, 0 to destroy` |

Not read by this seat: `render.py`'s 67 lines for what they draw, the screenshots, the naming library's diff, the registry files.

## C1 -- the riders: the act writes the SAME keys as round 23, and the grade shows it

Round 23 was `render.py` alone. This act also ships a changed naming library and seven registry files, which decide the S3
addresses the publisher writes. The COO half read 10 of 10 address functions equal under both libraries and did not read the
library's diff. So the served grade carries one more read:
- the keys written by the republish are the same keys as round 23's (index, audit, the 13 chart objects, the manifest, the state
  record, the copies under `revisions/`), and no object appears under any OTHER key of the product's prefix in that minute.
- (a) Equal: nothing more.
- (b) A key differs or a new one appears: roll back to `6124b079f3` the same hour and it comes to this seat. Nothing is deleted
  without Andrew's word; the stray object is named.

## C2 -- the one script still makes one kind of call

The script grows from 7,369 to 9,348 bytes. `C-NO-SCRIPT` as amended (PRD F.7) allows one inline block and no network call but
to this product's chart route. The render check's count of script blocks reads 1, and the grade states the one fetch's target.

## Accepted as the COO half's message states them

- One republish of 2026-10-07, `refresh_a1` false; no table write; memory stays 3,008.
- The page at 1,693,555 B, 13.2 percent under the cap; 0 missing sections.
- C1 of the round-22 half holds for the republish (manifest newer than index, 13 chart objects, or it is a partial state).
- The audit page has no copy under `revisions/` by design (`publish_page.py` line 951).

## Not covered

- Whether the chart now reads as Andrew asked: that is J1, and then his own look.
- `FWD-24` (the year of closes): no part of it is in this deploy.

-- 1.0.0_SA_CTO~Z
