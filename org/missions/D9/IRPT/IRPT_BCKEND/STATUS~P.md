# IRPT_BCKEND~P (Performance) -- status (FROZEN for hand-back, brief A2)

Seat `2.0.0_SA_COO~P` (CLAUDE). Workstream scope (brief section 3 Phase D): shared auth, routes, IaC and packaging,
plus Performance/Reporting.
As of 2026-09-28T18:0xZ. This is the A2 freeze of `org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_CLOSER_TO_CANONICAL_RETURN_BRIEF_20260924.md`
section 3, act 3 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20260928_174xZ_RELAUNCH_CANONICAL_DRIVE_PMY_CLOSER_D.md`
(CTO 102385). Lease IRPT_BCKEND~P is FULL; the /loop 20m goal row is struck; the /closer-drive cron 312e843c is gone
(CronList empty at relaunch). The goal record stays the done-criterion:
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`.
Round 19 is cut from the next-list below. Earlier forms of this file are in git.

## Served function -> deployed artifact -> source commit

Live CodeSha256 read 2026-09-28 ~17:5xZ (`get-function-configuration`), each equal to the ledger readback. Source
commits are on the backend branch `irpt-smoke-p-backend-20260923` and are NOT on CLOUD (`merge-base --is-ancestor`,
all six checked N); the S19 purge map leaves every one of them unchanged. B3 of the brief is the proof that the drain
carries them.

| Function | Live CodeSha256 | Applied (Z) | S3 version | Source (backend branch) | Ledger | Rollback |
|---|---|---|---|---|---|---|
| irpt-performance-adapter | `F0bYtOfBw3qwHtHAALuGcP77bzMB98mTYSBr+eO6rlM=` | 09-27 23:47:48 | G4UtfeeR.. | `entry.py` @c8ef8b7751 over the live 69-member set | irpt-adapter-render-selection-20260927 (+ render-grant-kms-20260927) | S3 8uohgNwE (bOefL9nx) |
| irpt-export-render | `BORQ2shbblG4OIG387kkAKTxUUtbPhw6LoLVx0mqGM4=` | 09-28 12:51:49 | O1Vu8CyD.. | `export/entry.py` @5c0185fee2 (R11 RUNNING) | irpt-export-receipt-running-20260928 | Ulim/gmf |
| irpt-ycharts-generate | `AdE17rT6f3IZKuh/VWMLTB+HuCZql50ZJzZXUYs90e8=` | 09-28 13:11:54 | BIEsyaNn.. | `generate_installed.py` @2e3d50caac, `publication.py` @c1fd6c5e52, `maintained_sources.py` @15b9f85eb3, `templates.json` @6096ee740b | irpt-generate-resident-grant-20260928 CLOSED | S3 Iu3nADja (ykJltfTd) |
| Resident (i-0167fd745ad906a66) | root `/opt/irpt-resident/fe64236bbb-st2`, tar sha256 f681024b.. | 09-28 13:17:56 | 2ZLL.I5j.. | st overrides + the same four files as generate (6096ee740b, 15b9f85eb3, c1fd6c5e52) | irpt-generate-resident-grant-20260928 CLOSED | root fe64236bbb-st |
| irpt-status | `ZYr+IDMpN0vtwnpxz+kOXKDMcjNpLrbbHdRm4TZerkY=` | 09-28 14:04:55 | 7Uz6kDd_.. | publish @6389be7a9b (submission.py 9929a829, prospect_dates.py e5bae585); IAM original_holdings grant @75df934b23 | irpt-status-dates-rebuild3-20260928 | code S3 7xPCOM83 (bMMJ); grant = ops root at 5c0185fee2 iam.tf |
| irpt-directory-search | `o1TXq5PH1+/VVff+hf4U+b+H6Kf1VCJkUJJjAaN+y7Q=` | 09-26 22:54:06 | -- | directory `handler.py` + `entry.py` @49b935c213 | irpt-uir07-search-rank-20260926 CLOSED | S3 7ENQv_0N (o9Qu0Jm7) |

Branches (local, not pushed; MSTR drains per brief B1, ~P first):
- backend `irpt-smoke-p-backend-20260923` @101ec0d8eb. WIP: none. The worktree's untracked files are `.scratch/`
  commit-message drafts and `org/pipescript-suite-gate-audit.log`; its `portal` path reads modified (237bdfda vs the
  recorded 10141b6d, no `.gitmodules` mapping in that worktree). Neither is ~P work, and neither is committed.
- publish `irpt-p-publish-20260923` @b4f5492e9e. WIP: none (status clean).
- Branch-side ledger residue: both branches still carry `.open_deploys` files (irpt-p-live-scope-20260923,
  irpt-performance-window-rearm-20260924, irpt-upload-hop2-20260924, irpt-performance-49f-engine-20260924,
  irpt-performance-inf-one-use-20260925) that CLOUD already closed (each has one completion file on CLOUD). At the
  drain the CLOUD state wins; none is a live deploy.

## Open ledger entries (CLOUD `org/critical_paths/.open_deploys/`), each open on A1 only

U1 and D1 are closed in every completion file; the JSON legs lag on U1/D1 for four of the six. The open proof in each
is a live walk:

| Entry | Open leg | Proof owed |
|---|---|---|
| irpt-adapter-render-grant-kms-20260927 | A1 | the render's Performance read as RENDER_DELEGATE succeeds (no AccessDenied); READY %PDF |
| irpt-adapter-render-selection-20260927 | A1 | the same read answers (no SelectionRefused); READY %PDF |
| irpt-export-async-submit-20260927 | A1 | ONE POST answers QUEUED with an exr_ revision under 29 s; BUILDING -> SUBMITTED; receipt NOT_READY -> READY %PDF or a named FAILED |
| irpt-export-receipt-running-20260928 | A1 | a pending receipt reads RUNNING and the page polls to READY |
| irpt-export-reopen-rule-20260927 | A1 | a second in-scope principal exports READY; a principal missing one account is refused; grant/receipt name the caller |
| irpt-status-dates-rebuild3-20260928 | A1 | the page reads REQ-67e12718 READY PER_SECTION |

## Acceptance (goal done criteria)

| # | Criterion | State |
|---|---|---|
| 1 | Signed-in journey per firm | Performance DONE at 49F, INF, COT, but NEW-01 puts a wrong figure on one 49F account. Analysis READY once (49F). Export reaches the render; READY needs the K8 window |
| 2 | Every active account resolvable | MEASURED: COT 843/843, INF 878/878, 49F 6698/7497 (9 funded non-computable) |
| 3 | COT structurally sound, window disclosed | MET: RPT-12b885b8, actual 07-21..09-21 (rows S169/S170) |

## Next-list, in priority order (round 19 cells)

1. **NEW-01 (HIGH, row S176, CTO 102357):** an invested 49F account answers YTD -100.00% (the series falls from 0.00%
   on 04-15 to -100.00% on 04-16 and holds). Trace to file:line in the adapter F0bYtOfB and the gips series, then fix.
   Acceptance: an account with positive holdings never answers -100%; a first-day funding flow is not a return. Source:
   `docs/briefs/irpt-ui-cleanup-status-20260928.md` (shots 20260928T133602Z#138/#139). Risk WORLD.
2. **The first live Comparison + export window (one packet, both halves before the principal):** K4 window 15's
   Dollars CSV; K5 ONE Comparison, opal_long_term, via `live_chain.py` @898fda7783 (~Y 102340); K8 the export, closing
   the five export/adapter A1 legs above (needs ~D's page pin TO-IV-e-78); K10 the page reads REQ-67 READY (rebuild 3
   A1). Risk WORLD.
3. **UIC-06, backend half:** NOT MET at the CRO re-walk @f330857833; no work recorded.
4. **Per-headline causal filter** (carried from the goal loop).
5. **Hygiene, owner ~P:** `run_async_submit` logs stage FAILED for a refused replay whose pointer it did not change;
   the tree-order template's `<proof_of_spec>` path is flat while the gate globs
   `<project>/deliverables/<serial>/<TO stem>.proof_of_spec.json` (row S167); the backend worktree's directory
   Terraform root predates ~M's holdings resources (UIR-07 used -target); the ~M consumer cherry-picks 65957b8afc and
   15b9f85eb3 went in by plain cherry-pick, not safe-commit (review at the drain).

## Andrew acts in flight

None at this lane. No one-use plan is armed on the adapter (live env has no PLAN key, read ~17:5xZ). A future vendor
call (a Performance one-use window, a 49F SmartX or INF Orion Scope call) needs a fresh per-use word, both halves and
a ledger.

## Parked (owner outside ~P, or un-park condition not met)

| Question | Owner | Un-parks when |
|---|---|---|
| Kept test inputs and reports from windows 1-6 in cottonwood, plus RPT-b683f188 (S157) and the spent claims PERFORMANCE_USE#63cf95e9 / #b20d69b2, must be excluded from firm viewers' lists or removed | the release cutter | the route opens to firm users |
| `build-and-upload.sh` deletes tracked performance/*.py on each adapter build (restored by hand each time) | 1.0.0_SA_CTO to route (ci/ owner) | the next performance build |
| Row S175: an unknown comparison key and a catalogue edit both raise MaintainedSourceRefused, mapped to UNEXPECTED; remedy two subclasses declaring `public_reason_code` in `_scope/maintained_sources.py`. UI-unreachable | 2.0.0_SA_COO~M | the next maintained_sources.py change, or a portal path that sends a free key |

## Gates in force

- Every served zip: `flat_zip_module_census.py` + ~Y's `zip_module_census` + a built-zip cold-start smoke BEFORE apply.
- A LIVE before-read on the served bytes before the apply, and the same read after; any unnamed difference is a
  same-turn rollback.
- Served moves need both never-widen halves (CTO + CRO) at HEAD naming the packet blob.
- Walk principals: password to SSM SecureString only; K1-CRED removed by `walk_principal.py --kind=uiwalk credoff`;
  deleted within the 120-minute cap.
