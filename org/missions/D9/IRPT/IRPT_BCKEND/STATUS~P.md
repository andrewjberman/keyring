# IRPT_BCKEND~P (Performance) -- status

Seat `2.0.0_SA_COO~P` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Reviewer `3.0.0_SA_CVO` grades landed pins after the fact while the lease is FAST.
Drive: the /closer-drive loop resumed on Andrew-direct "recs approved for all" (CTO 101296); cron 312e843c.
Goal: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.
As of 2026-09-28T13:2xZ. Earlier forms of this file are in git (`git log -p -- <this file>`).
**MSTR freeze (102315, 12:50Z, Andrew-direct "Purge now, then push"):** no commit, merge, push or worktree add in any
tree until MSTR's CLOSE; file edits are fine. On CLOSE: `git reset --mixed HEAD` in each worktree, then commit the
ledgers, this file, row S175 and the drive log.

## Pins (served)

| What | Value | Ledger |
|---|---|---|
| irpt-performance-adapter | **`F0bYtOfB..`** since 23:47:48Z: a RENDER_DELEGATE reads only the grant-pinned selection. Role: the render-grant decrypt under the S3 Bucket Key (21:50:13Z). NO plan armed | irpt-adapter-render-selection-20260927 (A1 open) / irpt-adapter-render-grant-kms-20260927 (A1 open) |
| irpt-export-render | **`BORQ2shb..`** since 12:51:49Z: S27, a pending `exr_` receipt answers RUNNING per R11 (on `Ulim/gmf`'s async submit, withheld prose, binding, authorizer). Before = after on the refusal branch | irpt-export-receipt-running-20260928 (D1 closed, uncommitted; A1 = the RUNNING branch live) |
| irpt-ycharts-generate | **`AdE17rT6..`** since 13:11:54Z: the GRANT. Comparison and Multi-Comp ADMITTED on the served bytes (P:1728413; P:1728415 + P:1728315); Overview unchanged; unknown key REFUSED (as UNEXPECTED, row S175). Rollback Iu3nADja | irpt-generate-resident-grant-20260928 CLOSED (uncommitted) |
| Resident | **`/opt/irpt-resident/fe64236bbb-st2`** since 13:17:56Z (st + GRANTED catalogue + foreign-firm name check); st kept for rollback | same, CLOSED |
| irpt-status | **`bMMJ/bQ+5..`** (rolled back 00:36:31Z). Rebuilds 1 and 2 failed (cold start; pin-skewed errors.py + no original_holdings grant). Rebuild 3 (ZYr+IDMp, 31fbdcbf): both halves SIGNED (CTO 102307 @472a6d0d94, CRO 102327 uncommitted), ~Y gates 3+4 PASS (102329, uncommitted); applies once ~Y's gates are COMMITTED and cited | irpt-status-dates-rebuild(2)-* CLOSED as failed deploys |
| irpt-directory-search | `o1TXq5PH..` | irpt-uir07-search-rank-20260926 CLOSED |
| Backend branch | `irpt-smoke-p-backend-20260923` @5c0185fee2 (not pushed) |  |
| Publish worktree | `irpt-p-publish-20260923` @8aba435a00 (not pushed) |  |
| Push state | LOCAL; MSTR pushes |  |

## Live thread

- **Performance:** served at 49F, INF and COT. **COT criterion 3 met on real data** (S157R, RPT-12b885b8, actual
  07-21..09-21).
- **Analysis:** the first READY report (window 15). Comparison selection is now admitted in generate and the resident
  runs st2. K10 (the page read) waits on status rebuild 3.
- **Export (FWD-9):** every hop up to the render's report read holds live, and S27's RUNNING receipt is served. ~D's
  page fix (TO-IV-e-78) is the one piece left before the K8 re-run.

## Acceptance (goal Done criteria)

| # | Criterion | State |
|---|---|---|
| 1 | Signed-in journey per firm | Performance DONE at all three. Analysis READY once (49F). Export: the first real export reaches the render, and READY needs the K8 re-run |
| 2 | Every active account resolvable | MEASURED: COT 843/843, INF 878/878, 49F 6698/7497 (9 funded non-computable) |
| 3 | COT structurally sound, window disclosed | **MET on real data**: RPT-12b885b8 states actual 07-21..09-21, and its series starts 07-21 (rows S169/S170) |

## Write claims

None open. Windows 18-20 are CLOSED.

## Next-list (in order)

1. **After MSTR's CLOSE:** re-sync each worktree (`git reset --mixed HEAD`); commit the S27 and GRANT ledgers, this
   file, row S175 and the drive log.
2. **irpt-status rebuild 3:** apply once ~Y commits gates 3+4 and the ledger cites both (CTO 102307, CRO 102327):
   live before-reads (owner refusal + REQ-67), safe-apply 0/2/0, readback + cold start, after-reads (refusal unchanged,
   REQ-67 READY PER_SECTION) or a same-turn rollback of code AND grant.
3. **A new K8 + K10 window** on all of the above plus ~D's S27 page pin (TO-IV-e-78); it also carries S27's A1
   (the RUNNING branch live) and the first live Comparison.
4. UIC-06; next round's per-headline causal filter.

**Gates in force:**
- every zip gets `flat_zip_module_census.py` (shared-package pin skew) plus ~Y's census and smoke BEFORE apply;
- the before-read is taken LIVE on the served bytes before the apply, and the same read after;
- K1-CRED is removed by `credoff`.

## Parked

| Question | Owner | Un-parks when |
|---|---|---|
| Kept test inputs and reports from windows 1-6 in cottonwood, plus RPT-b683f188 (S157) and the spent claims PERFORMANCE_USE#63cf95e9 / #b20d69b2, must be excluded from firm viewers' lists or removed | the release cutter | the route opening to firm users |
| The backend worktree's directory Terraform root predates M's holdings resources; UIR-07 used -target | 2.0.0_SA_COO~P | the next directory-root apply |
| `build-and-upload.sh` deletes tracked performance/*.py on each adapter build (restored by hand each time) | 1.0.0_SA_CTO to route (ci/ owner) | the next performance build |
| The ~M consumer cherry-picks (65957b8afc, 15b9f85eb3) went in by plain git cherry-pick of ~M's own gated commits, not through safe-commit | 2.0.0_SA_COO~P | the next drain of this branch |
| Row S175: an unknown comparison key and a catalogue edit both raise MaintainedSourceRefused, which `_authz/errors.reason_for` maps to UNEXPECTED; the remedy is two subclasses declaring `public_reason_code` (INVALID_INPUT for an unknown key, NOT_READY for a changed entry) in `_scope/maintained_sources.py`, never message-matching. UI-unreachable | 2.0.0_SA_COO~M (the consumer's owner) | the next maintained_sources.py change, or a portal path that sends a free key |
| `run_async_submit` logs stage FAILED for a refused replay whose pointer it did not change | 2.0.0_SA_COO~P | the next export change |
| The tree-order template's `<proof_of_spec>` path is flat; the gate globs `<project>/deliverables/<serial>/<TO stem>.proof_of_spec.json` (row S167) | 2.0.0_SA_COO~P | the next tree order this seat cuts |

## Limits

No vendor call without its per-use word under both halves and a ledger. Every served zip gets a built-zip cold-start
smoke before apply (CTO standing condition after HyEyoJ67). Nothing here is pushed.
