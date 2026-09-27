# IRPT_BCKEND~P (Performance) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Reviewer `3.0.0_SA_CVO` grades landed pins after the fact while the lease is FAST.
Drive: the /closer-drive loop resumed on Andrew-direct "recs approved for all" (CTO 101296); cron 312e843c.
Goal: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.
As of 2026-09-27T20:3xZ. Earlier forms of this file are in git (`git log -p -- <this file>`).
**MSTR freeze (102065):** no commit, push or worktree add from about 03:00Z to 05:00Z (the S19 history purge);
re-sync each worktree on DONE.

## Pins (served)

| What | Value | Ledger |
|---|---|---|
| irpt-performance-adapter | `bOefL9nx..` since 05:22:03Z (09-27); NO armed plan (`approved_performance_plan = null`) | irpt-cot-actual-window-20260927 CLOSED |
| irpt-ycharts-generate | `G/TqLPdL..` since 02:15:03Z (09-27) | irpt-cross-viewer-title-20260927 CLOSED |
| Resident (i-0167fd745ad906a66) | `/opt/irpt-resident/fe64236bbb-lt` since 15:51:47Z | irpt-resident-level-tolerated-20260927 CLOSED |
| irpt-status | `bMMJ/bQ+5..` | irpt-status-reads-20260926 CLOSED |
| irpt-directory-search | `o1TXq5PH..` | irpt-uir07-search-rank-20260926 CLOSED |
| irpt-export-render | **`Ulim/gmf..`** since 20:0xZ. Async submit (the POST answers QUEUED with an `exr_` id; ONE marked self-invoke builds; retries 0), withheld rejected prose with client copy, the async leg bound to accept's principal and permitted-set digest, and the reopen-rule authorizer (3EST/hewG) | irpt-export-async-submit-20260927 (A1 open) / irpt-export-async-binding-20260927 CLOSED / irpt-export-reopen-rule-20260927 (A1 open) |
| Backend branch | `irpt-smoke-p-backend-20260923` @118612b599 (not pushed) |  |
| Publish worktree | `irpt-p-publish-20260923` @842156ee01 (not pushed) |  |
| Push state | LOCAL; MSTR pushes |  |

## Live thread

- **Performance:** served at 49F, INF and COT; a second authorized viewer reopens a retained report.
- **Analysis:** the first READY report (window 15, RPT-5288c06d). K10 (the page read) waits on ~D's selected_tenant fix
  and ~Y's irpt-status rebuild (item 4).
- **Export:** window 17's K8 reached the narrative build and failed there after 60 s (CTO 102026). Both defects are
  fixed and SERVED: the rejected prose is withheld, and the submit is async. Window 18 runs the five arms.

## Acceptance (goal Done criteria)

| # | Criterion | State |
|---|---|---|
| 1 | Signed-in journey per firm | Performance DONE at all three. Analysis READY once (49F). Export: the async path is served, and the first real export is window 18's K8 |
| 2 | Every active account resolvable | MEASURED: COT 843/843, INF 878/878, 49F 6698/7497 (9 funded non-computable) |
| 3 | COT structurally sound, window disclosed | The fix is served (bOefL9nx). A real-data corrected report needs ONE use: the S157R packet is out for halves, on the session refreshed 18:42Z (AWSCURRENT 9da4e781) |

## Write claims

Window 18 (`irpt-ui-walk-principal-w18-20260927`, OPEN): both halves SIGNED on blob b74de7e4 (CTO @7ffe09ff0b 102078;
CRO @8d09b3994c 102079). It opens after the CRO's ui-walker reports DISARMED (about 20:55Z).
- CRO citation fix for part C: its authority is CTO 102028 (1) on Andrew's 09-26 word "egress is permitted for API
  calls". It is not MSTR 101850 via CTO 101854.
- CTO item: part C's audit prints the resident journal's host re-capture and session_refresh counts; either
  non-zero is BLOCKING.

## Next-list (in order)

1. **Window 18:** create on the CRO's DISARMED report, then:
   - A. ~D's round-8 walk;
   - B. K7/K8 async export with five arms (the POST timed from the HAR; 2 invocations);
   - C. ~Y's four securities_info reads by `comparison_identity_read_20260927.sh`, with the evidence file path sent to ~Y.
   It closes the A1s of the async-submit and reopen-rule ledgers.
2. **S157R, a corrected COT report:** packet blob 049ea241 (@95f271b30a), out for halves (CTO 102081, CRO 102082).
   Plan 4 b20d69b2 (01-01..09-21), expiring 02:00Z. Arm, read, reopen and disarm in one tick, before 02:00Z.
3. **Resident Static tolerance** (CTO 101971 item 2): ~Y's P_STATIC_TOLERANCE_20260927.patch, applied but UNCOMMITTED
   in the backend worktree (extract.py, recipe.py, resident_worker.py, test_resident_worker.py, new
   test_calculation_settings.py). Ship as the next resident version under its own ledger; run its suites separately.
4. **irpt-status rebuild** (~Y 102050, 102067): HEAD's submission.py + P_TEMPLATE_STATUS_DATES_20260927.patch + the
   entry.py render_ports line. Three changes, under its own ledger and halves, before K10.
5. **Next round's enrichment** (CTO 102041 item 2): filter each causal headline before composition, not the whole
   prose.
6. **S152** (INF holdings 3 trading days behind): ~M's; it disarms on the R4 Monday enable.

**DONE this stretch (20:3xZ):**
- W16 and W17 CLOSED @ca5ae4f5ea. W17's K8 passed the reopen-rule authorizer (arm 1 live) and failed at the narrative
  build; nothing was written; arm 3 held.
- Narrative fix (ac4eb443b3) and async submit (f3995c0d31) served as 8nkjGpT0 (D1 @d43edd47cd). A no-write live
  probe: a marked event with no pointer was refused.
- Binding plus client copy (118612b599) served as Ulim/gmf; ledger CLOSED @ad0590b8f1.
- TO-IB-s158: AC1 amended (@9fa6a3c5d8); ~S flipped it complete (@fe23038617, 3/3). CTO 102044 accepts AC1 as refused
  with an absence proof. S158 closes.

## Parked

| Question | Owner | Un-parks when |
|---|---|---|
| Kept test inputs and reports from windows 1-6 in cottonwood, plus RPT-b683f188 (S157) and the spent claim PERFORMANCE_USE#63cf95e9, must be excluded from firm viewers' lists or removed (CTO 101678, 101825, 101937; CRO 101609) | the release cutter | the route opening to firm users |
| The backend worktree's directory Terraform root predates M's holdings resources; UIR-07 used -target | 2.0.0_SA_COO~P | the next directory-root apply: merge CLOUD in first |
| `build-and-upload.sh` deletes tracked performance/*.py on each adapter build, and zips JSON with checkout EOL | 1.0.0_SA_CTO to route (ci/ owner) | the next performance build |
| 49F engine: 9 funded non-computable accounts; 219 of 5194 divergent vs BD | 1.0.0_SA_CTO to route | the engine lane's next act |
| The adapter answers an internal viewer's GET without `selected_tenant` as UNAVAILABLE/UNEXPECTED, not a named refusal | 2.0.0_SA_COO~P | the next adapter deploy |
| `run_async_submit` logs stage FAILED for a refused replay whose pointer it did not change; the pointer is the record | 2.0.0_SA_COO~P | the next export change |
| The tree-order template's `<proof_of_spec>` path is flat; the gate globs `<project>/deliverables/<serial>/<TO stem>.proof_of_spec.json` (~S 102053, row S167) | 2.0.0_SA_COO~P | the next tree order this seat cuts |

## Limits

No vendor call is made by this seat without its per-use word under both halves and a ledger. Nothing here is pushed.
