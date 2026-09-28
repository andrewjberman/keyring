# IRPT_BCKEND~Y (Analysis) -- status (HAND-BACK FREEZE)

Seat `2.0.0_SA_COO~Y` (CLAUDE). As of 2026-09-28T18:0xZ. This file is the brief section 3 A2 freeze
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/IRPT_CLOSER_TO_CANONICAL_RETURN_BRIEF_20260924.md`), owed under act 3 of
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20260928_174xZ_RELAUNCH_CANONICAL_DRIVE_PMY_CLOSER_D.md` (CTO 102387).
Lease IRPT_BCKEND~Y: FULL (CTO act 1, 17:47Z). The goal loop row is struck, and the goal record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md` is the done-criteria.
Its open criteria are the next-list below, which becomes round 19's cells.
The prior closer-era narrative (windows 3-15, hops 1-10, rulings) is in git at `33addf0c02`, the last version of this file before
the freeze, and in `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/STATUS.md`.

## 1. Pins

| What | Value |
|---|---|
| Work in progress | NONE. The Y worktree `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922` is clean (0 lines of `git status --short`); the main tree holds 0 uncommitted Y-owned paths. |
| Y branch | `irpt-mvp-y-20260922` @`0a24edfe38`, 25 commits not on CLOUD. It is LOCAL (not on origin); the drain is MSTR's act 4, after P's branch. |
| Y records on CLOUD | log `b0adb91aac`; handoff `465692aa2b`; case_trace Comparison `33addf0c02`; resident SSM read `add7a41cfd`; rebuild 3 gates 3+4 `3f40796915`; GRANT release arms `46b975e6aa`. These are the POST-S19 hashes; any older pin resolves through `org/tier0_exec/0.0.0_AB_MSTR/deliverables/S19_PURGE_COMMIT_MAP_20260928.txt`. |
| Tools | `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/` (live_chain, case_trace, offline_submit_proof, zip_module_census, zip_cold_start_smoke, status_role_sim, served_drift_census) |

## 2. Deployed artifact -> source commit, per served function (Y's surface; read live 2026-09-28 17:4xZ)

| Served function | Live identity (read by Y) | Source |
|---|---|---|
| `irpt-ycharts-generate` | CodeSha256 `AdE17rT6..`, LastModified 13:11:54Z, Successful; S3 `investor-reporting/irpt-ycharts-generate.zip` VersionId `BIEsyaNn..` | P branch `irpt-p-publish-20260923` cherry-picks `3f80724d2e`/`3b10bc336c`/`3523706d32`/`987689c242` (= backend `2e3d50caac`, `6096ee740b`, `c1fd6c5e52`, `15b9f85eb3`). Members: templates.json `54656584` (Y `0a24edfe38`), publication.py `6aa82b3a` (Y `14568b9ec1`), maintained_sources.py `774eca9b` (M `15b9f85eb3`), generate_installed.py `b4f33b37` (`2e3d50caac`), publisher.py `68900af6`. Ledger `irpt-generate-resident-grant-20260928` CLOSED 13:19:08Z. |
| resident `irpt-analysis-resident.service` on `i-0167fd745ad906a66` | SSM `cce9269f` (17:4xZ): ExecStart root `/opt/irpt-resident/fe64236bbb-st2`, active, MainPID 235902 since 13:17:56Z, NRestarts 0, 0 Tracebacks over 4 h | tar `ec2/investor-reporting-ycharts/resident/irpt-resident-fe64-st2.tar.gz` VersionId `2ZLL.I5j..`, sha256 `f681024b..`; `build_resident_package.py` = st's overrides + templates.json `6096ee740b`, maintained_sources.py + publication.py/publisher.py `c1fd6c5e52`/`15b9f85eb3`. Rollback root `fe64236bbb-st` kept on the host. |
| `irpt-status` | CodeSha256 `ZYr+IDMp..`, LastModified 14:04:55Z, Successful; S3 `investor-reporting/irpt-status.zip` VersionId `7Uz6kDd_..` | rebuild 3 MINIMAL: bMMJ members + submission.py `9929a829` (pin `5cec1a3892`) + prospect_dates.py `e5bae585`; ops/entry.py at bMMJ's `9da6a1a6`; P's ci record `b4f5492e9e`. Plus the irpt-status-role original_holdings read grant (3 firms, registry-derived). |
| `irpt-intake-poller` | CodeSha256 `YpE2MyUw..`, LastModified 2026-09-11T12:55:52Z | unchanged since 09-11. The 09-27 served drift census (`SERVED_DRIFT_CENSUS_20260927.md`, `64953b61a7`) shows 4/4 Y modules identical to source. |

Live proof that the four compose: REQ-67e12718 reads READY ANALYSIS_READY, date_basis PER_SECTION, 51 section dates on
the served `ZYr+IDMp` (P's after-read 14:05:33Z in ledger `irpt-status-dates-rebuild3-20260928` leg D1, equal to Y's
gate 4). Y did not re-invoke it: the next check would not change the next-list.

## 3. Open ledger entries touching Y's surface

| Entry | Owner | Open leg | Closes when |
|---|---|---|---|
| `irpt-status-dates-rebuild3-20260928` | 2.0.0_SA_COO~P | A1: K10, the page reads REQ-67e12718 READY PER_SECTION | 2.0.0_SA_COO~D walks the page (the API half is already READY) |

Y opens no ledger entry of its own; deploys and served installs are P's. Every other `irpt-*` entry open on CLOUD
(`adapter-render-*`, `export-*`) is P's or M's and does not touch Analysis. Census: every one of the 9 worktrees was read
with `ls-tree` of `org/critical_paths/.open_deploys/`.

## 4. Next-list, in priority order (becomes round 19's cells)

1. **The first live Comparison window (FWD-4 arms).** K4 is W15's CSV. K5 is `opal_long_term` via `live_chain.py`
   `WALK_COMPARISON_KEYS`, one Comparison and two Multi-Comp bodies, each schema-valid. Then `case_trace.py cottonwood <REQ>`.
   Everything the window needs is served (generate `AdE17rT6` + resident st2). It needs one window packet from ~P; no
   code is owed.
2. **Close window 15's two NOT_EVALUATED links.** (a) The screen: ~D's K10 on REQ-67e12718, the same act as the rebuild 3
   A1 leg. (b) The export: window 16. The Analysis export is unbuilt and refused by name; the CTO ruled it an enrichment
   under FWD-9 (101465).
3. **The Y2 arm windows.** The XLSX template and Target Weight arms are ready in `live_chain.py` (`e29a2e7d27`, pre-S19
   `5d371a403e`). Each needs one window.
4. **The first certified Analysis report per remaining firm: 49financial, then Inflection.** No certified vendor PDF
   exists yet for either; each firm's first window produces one. The certifier's firm check already derives every
   firm's name from the registry (`14568b9ec1`, `0a24edfe38`).
5. **Recovery and revocation, proven live.** The goal's recovery/revocation requirements have offline proofs only
   (retained-PDF recovery, ownership checks at `2874e37647`). A cell drives each deliberately, with the organic case as
   the negative arm.
6. **Enrichment: read back the saved `model_portfolio_type` before the report is generated.** This is the W15-3
   Static-only rule's pre-check (CTO 102021).
7. **Branded Analysis export (FWD-9 enrichment).** Unbuilt; it follows item 2(b).
8. **Hygiene, at the drain:** `intake/tests/test_security_resolution.py:31` needs IRPT_LOOKUP_FIXTURE_ROOT (Y). The Y
   worktree is a sparse checkout, so two `test_broker_recovery_evidence` arms fail only there (Y).

Parked, not a cell: the Shares price source (CTO 100887 refused it by name for v1; re-ask when the Dollars journey is
graded). The unknown-key refusal's public code UNEXPECTED is P's surprise row, unreachable from the UI.

## 5. Andrew acts in flight

None at this lane. Standing word at ~Y (09-27 12:4xZ): "yes you can run as many analysis attempts as needed". Vendor egress
is permitted but ledgered; a served move needs the never-widen halves.

## Standing directives (carried)

- No firm id typed in code or JSON; run `.tools/naming-gate.py --diff <diff> --enforce` explicitly (the Y worktree does not
  enforce it).
- Before any irpt-status or generate apply, P asks for Y's four gates on the BUILT artifact: zip_module_census (with
  `--expect` intents), zip_cold_start_smoke `--owner-refusal`, status_role_sim (planned policy), offline_submit_proof
  `--live-env`.
- The walk-principal password is read BY NAME from SSM into memory and never printed.
- "Nobody runs AC8 again"; do not remove the `wk-nfra-oplgtw-og-v-4-p1` worktree.
