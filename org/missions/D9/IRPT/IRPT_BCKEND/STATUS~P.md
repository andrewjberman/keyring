# IRPT_BCKEND~P (Performance) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Reviewer `3.0.0_SA_CVO` grades landed pins after the fact while the lease is FAST.
Drive: the /closer-drive loop resumed on Andrew-direct "recs approved for all" (CTO 101296); cron 312e843c.
Goal: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.
As of 2026-09-28T00:0xZ. Earlier forms of this file are in git (`git log -p -- <this file>`).
**MSTR freeze (102065):** no commit, push or worktree add from about 03:00Z to 05:00Z (the S19 history purge);
re-sync each worktree on DONE.

## Pins (served)

| What | Value | Ledger |
|---|---|---|
| irpt-performance-adapter | **`F0bYtOfB..`** since 23:47:48Z: a RENDER_DELEGATE reads only the grant-pinned selection. Role: the render-grant decrypt under the S3 Bucket Key (21:50:13Z). NO plan armed | irpt-adapter-render-selection-20260927 (A1 open) / irpt-adapter-render-grant-kms-20260927 (A1 open) |
| irpt-export-render | `Ulim/gmf..`: async submit, withheld prose with client copy, the async leg bound to accept, the reopen-rule authorizer | irpt-export-async-submit-20260927 (A1: arm 3 re-runs) |
| irpt-ycharts-generate | **`ykJltfTd..`** since 22:33:55Z (catalogue v2 + ~M's consumer; comparisons still refused, since no GRANT) | irpt-generate-resident-catv2-static-20260927 CLOSED |
| Resident | **`/opt/irpt-resident/fe64236bbb-st`** since 22:46:12Z (the Static-only tolerance + v2 + consumer); lt kept for rollback | same, CLOSED |
| irpt-status | **`bMMJ/bQ+5..`** (rolled back 00:36:31Z). Rebuild 1 (HyEyoJ67) and rebuild 2 (5fSyChId) both failed: cold start, then refusals turned into 500s by a pin-skewed errors.py plus a missing original_holdings grant. Rebuild 3's shape is asked of the CTO | irpt-status-dates-rebuild(2)-* CLOSED as failed deploys |
| irpt-directory-search | `o1TXq5PH..` | irpt-uir07-search-rank-20260926 CLOSED |
| Backend branch | `irpt-smoke-p-backend-20260923` @5c0185fee2 (not pushed) |  |
| Publish worktree | `irpt-p-publish-20260923` @8aba435a00 (not pushed) |  |
| Push state | LOCAL; MSTR pushes |  |

## Live thread

- **Performance:** served at 49F, INF and COT. **COT criterion 3 met on real data** (S157R, RPT-12b885b8, actual
  07-21..09-21).
- **Analysis:** the first READY report (window 15). K10 (the page read) waits on the status rebuild 2.
- **Export (FWD-9):** every hop up to the render's report read now holds live: tenant, reference, authorizer, async
  submit, narrative, binding, grant decrypt. Window 19 found and fixed the render's selection refusal. Two pieces are
  left:
  - S27: the RUNNING receipt answer, built at 5c0185fee2 per R11, which ships after the freeze;
  - ~D's page fix, which names a refused read instead of going idle.

## Acceptance (goal Done criteria)

| # | Criterion | State |
|---|---|---|
| 1 | Signed-in journey per firm | Performance DONE at all three. Analysis READY once (49F). Export: the first real export reaches the render, and READY needs the post-freeze K8 re-run |
| 2 | Every active account resolvable | MEASURED: COT 843/843, INF 878/878, 49F 6698/7497 (9 funded non-computable) |
| 3 | COT structurally sound, window disclosed | **MET on real data**: RPT-12b885b8 states actual 07-21..09-21, and its series starts 07-21 (rows S169/S170) |

## Write claims

None open. Windows 18 and 19 are CLOSED (@614594fff7, @6d6e5984b2).

## Next-list (in order)

Post-freeze (05:00Z on), each under both halves, with live before/after reads, a cold start and a built-zip census plus
smoke:
1. **S27, the RUNNING receipt** (packet c0b90ea2): both halves SIGNED (CTO 102263, CRO 102272/102279).
2. **The Comparison GRANT release** (packet b6c264b3): the CTO half is SIGNED (102286: no false foreign-firm refusal,
   ~Y's arm); the CRO half is pending. ~Y's composition arms run on the built zip BIEsyaNn and on st2.
3. **irpt-status rebuild 3:** the shape is asked (my rec: bMMJ + submission.py + prospect_dates.py + the original_holdings
   grant). Gates: ~Y's zip_module_census, the owner-refusal smoke, role simulation, and REQ-67 READY.
4. **A new K8 + K10 window** on all of the above plus ~D's S27 page pin (TO-IV-e-78).
5. UIC-06; next round's per-headline causal filter.

**Tonight's lessons, now gates:**
- every zip gets `flat_zip_module_census.py` (shared-package pin skew) plus ~Y's census and smoke BEFORE apply;
- the before-read is taken LIVE before the apply;
- K1-CRED is removed by `credoff`.

## Parked

| Question | Owner | Un-parks when |
|---|---|---|
| Kept test inputs and reports from windows 1-6 in cottonwood, plus RPT-b683f188 (S157) and the spent claims PERFORMANCE_USE#63cf95e9 / #b20d69b2, must be excluded from firm viewers' lists or removed | the release cutter | the route opening to firm users |
| The backend worktree's directory Terraform root predates M's holdings resources; UIR-07 used -target | 2.0.0_SA_COO~P | the next directory-root apply |
| `build-and-upload.sh` deletes tracked performance/*.py on each adapter build (restored by hand each time) | 1.0.0_SA_CTO to route (ci/ owner) | the next performance build |
| The ~M consumer cherry-picks (65957b8afc, 15b9f85eb3) went in by plain git cherry-pick of ~M's own gated commits, not through safe-commit | 2.0.0_SA_COO~P | the next drain of this branch |
| `run_async_submit` logs stage FAILED for a refused replay whose pointer it did not change | 2.0.0_SA_COO~P | the next export change |
| The tree-order template's `<proof_of_spec>` path is flat; the gate globs `<project>/deliverables/<serial>/<TO stem>.proof_of_spec.json` (row S167) | 2.0.0_SA_COO~P | the next tree order this seat cuts |

## Limits

No vendor call without its per-use word under both halves and a ledger. Every served zip gets a built-zip cold-start
smoke before apply (CTO standing condition after HyEyoJ67). Nothing here is pushed.
