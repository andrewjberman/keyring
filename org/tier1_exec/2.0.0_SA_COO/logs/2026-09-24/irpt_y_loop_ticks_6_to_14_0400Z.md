# 2.0.0_SA_COO~Y -- loop ticks 6 to 14 (2026-09-24 ~01:0xZ to 04:0xZ)

Seat: `2.0.0_SA_COO~Y` (Claude). Goal and loop authority: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md` @fc17929b64. Previous log: `org/tier1_exec/2.0.0_SA_COO/logs/2026-09-24/irpt_y_loop_ticks_2_to_5_0055Z.md`.

## What moved, in order

| Tick (approx Z) | Act | Record |
|---|---|---|
| 6 (01:1x) | Reviewed P's installed factory in P's tree: principal shape lacked `principal_class`, `authorize` was same-actor-only; exact fixes sent; P fixed at 32062e39d2; Y re-ran factory 11 / resident worker 37 per file | STATUS dependency row 1 |
| 7-8 (01:4x-02:1x) | Reviewed the cutover plan (runner-resident policy + host state) 99915/99916 STANDS; CTO GO 99937; P applied 01:52Z; host running since 01:52:51Z with `AutoShutdown=disabled` | STATUS; RUNBOOK precondition A |
| 9 (02:2x) | S119: P's wrapper bundle lacked schema_version / capture_origin / generation / user_agent / identity.user_id the Python resident requires; CTO word 99998 (IRPT-RESIDENT-SESSION-BUNDLE-CONTRACT-20260924); P 282f7ea427; Y reviewed STANDS (25/25 contract test) | STATUS |
| 10 (02:5x) | D1 run 1 (SSM 71d0961f, 02:54Z) loaded the public `/login/` page eight times and never saw a form; CTO word: measured route `/account/login/`, warm-up `/dashboard/`, form scoped to the visible password; P ad8306b769; Y reviewed STANDS on (a)-(h); library pin 5a1a8695 (LF blob) | commit af5c844509 |
| 11-12 (03:0x-03:3x) | D1 run 2 (SSM d89690f8, 03:31Z) signed in first try on the measured form; probe fell to the bare Node port and read NOT_LIVE. Y 100109: probe from inside the page, per-step status, pair records what the port sent; python3.12 for the resident. CTO adopted (100112) | commit d7e6ae0731, 2147a6daf5 |
| 13 (03:4x) | P 160f99b3ea + b1f269c6dd (probe in page, per-step status, pair with full jar + UA); Y checks at that pin: node --check OK, bundle_contract 25/25, offline suite all_pass; STANDS 100118/100119; library pin c8155201; runbook + handoff re-pinned | commit 0c1071f95a |
| 14 (03:5x-04:0x) | D1 run 3 (SSM 248c8bf6, 03:49Z at c8155201): sign-in PROVEN (1 submission, fields matched, 302, dashboard); the legacy market-data probe route is refused by the vendor's edge for the in-page fetch and the Node port alike, so the client-class item stays closed. CTO word 100135: predicate moves to the resident's own two routes (identity, then the Overview template GET); no solver of any kind; one P commit, Y STANDS, one run = the third submission. Y 100150/100151: the template GET is inside the literal text of CRO 6fc3f5f785 line 38; STANDS follows P's commit. Host pydeps verified (59e46a32, python 3.12.14) | commit 32961efbd9 |

## Facts worth keeping

- Two credential submissions were spent on 2026-09-24: 03:31Z (SSM d89690f8) on library 5a1a8695 -- the deploy at 03:28Z pulled pre-upload bytes and the pin read at 03:30Z printed 5a1a8695 before the run fired -- and 03:49Z (SSM 248c8bf6) on c8155201. The next is the third.
- `ycharts/session/current` still has `VersionIdsToStages: null`; queue 0/0; host running; secret unchanged since creation.
- The 09-11 cloud research (`docs/research/investor_reporting_ycharts_cloud_20260911/README.md`) measured the resident's own routes (`/dashboard/` identity and `/custom_pdf_reports/generate/14141822`) at 200 from a Lambda with a captured session; the legacy market-data probe route was never part of that measurement.
- Push state at 04:0xZ: origin/CLOUD 9fd480b74f (ls-remote read); local CLOUD 32961efbd9 (Y commits LOCAL; MSTR pushes on Andrew's word). Message 100150/100151 carried the earlier origin hash f96a0b9dd4 by carry-forward, not by a fresh read -- corrected here.
- Watcher: re-armed 03:45:16Z, one script row (pid 35344).

## Open, with owners

- P: the predicate commit, then Y STANDS-or-the-line, then the ONE run (third submission) -> bundle grade, enrolled id, receipt C1, install-resident.sh, Y `--once` (expected `IRPT_RESIDENT_POLL handled=0`), the 12.03 runbook from precondition B.
- P: route plane for hops 1 and 9 (runbook preconditions D-E); upload-function grant for `ORIGINAL_HOLDINGS`; prospect_dates v2 copy at 7fec957269.
- P (CTO 100132): portal DEV consolidation candidate; Y holds no portal pin and is not part of it.
