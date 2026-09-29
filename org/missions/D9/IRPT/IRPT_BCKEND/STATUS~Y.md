# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE), `/canonical-drive 10m` standard form (cron 8b04fff7, lease FULL; Andrew-direct record
@79764ce520). As of 2026-09-29T01:2xZ. The hand-back freeze text of @37cb971b4a is kept below it for the pins and the
served-artifact map; section 0 supersedes its next-list.

## 0. Round 19 ~Y CLOSED (2 of 2 orders drained); round 20 list

Decomposition `decompositions/IRPT_BCKEND_DECOMP_R19_Y.md` (@89f619e28b, amendments 1 @ecbb08548f and 2 @81cb041780).
Close record `deliverables/2.0.0_SA_COO~Y/R19_Y_DRAIN_CLOSE_20260928.md` @89966f267c.

| item | where it stands |
|---|---|
| 6 saved-type refusal before generation | TO-IB-yr-1 DRAINED @ec8f69f718; rides ~P's next resident + generate build (~P 102430), and ~Y runs the four gates on the built artifact when asked |
| 8 lookup test without env var | TO-IB-yr-2 DRAINED @7b99390ae3 |
| 1-4 Comparison window, W15 screen/export, Y2 arms, first 49F + INF reports | ride ~P's ONE window packet (~P 102407, 102410); in STATUS~P's next-list @522946a513 |
| 5 recovery and revocation | unit-, real-entry- and live-organic-covered; the deliberate live revocation arm rides the same ~P packet (~P 102423) |
| 7 branded Analysis export | ~P's by CONTRACT.md:23 (amendment 2); on ~P's next-list after K8 (~P 102471); ~Y supplies the AnalysisReport schema and owner shape on ask |

Round 20 ~Y rectangle (issuer acts, no cells uncovered):
1. The four gates (zip_module_census `--expect`, zip_cold_start_smoke `--owner-refusal`, status_role_sim, offline_submit_proof
   `--live-env`) on ~P's built resident + generate artifact carrying @ec8f69f718.
2. At ~P's window drain: `case_trace.py <firm> <REQ>` on every ~Y body (Comparison, Y2 XLSX, Y2 Target Weight, the
   INF and 49F Overviews) and the revocation arm (plus the resident journal). Commit each trace under
   `deliverables/2.0.0_SA_COO~Y/`.
3. On ~P's cut of the branded export: supply the AnalysisReport schema and the request-owned retained shape.

Rows: W63-S1 (INERT, the issuer's proof-path stem; the same class as S167/W42-S4), S187 (INERT, worker-slot reuse; owner
1.0.0_SA_CTO), DSGN_IRPTV1-S35 (~D portal surface). 0 ARMED rows without a seated owner.

## 0a. Window 22 WALKED -- round 20 item 2, partly discharged (2026-09-29T14:4xZ, after the 13:4xZ respawn)

Proof and per-body route record: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/W22/PART_Y_EVIDENCE_20260929.md`
@`827cbc166f` (LOCAL; `ls-remote` origin/CLOUD `15655f4a25`). Authority: ~P's packet blob `1f3bf0914f` (@6550c62cdf),
halves CTO `3b209c072c` / CRO `af1940e31d`, ledger `irpt-ui-walk-principal-w22-20260929`. Cap 5 submissions, all 5 used,
one login / one K4 / at most one K5 each, no retry, no replay. All five terminal by name 39 min inside the 15:10:37Z cap.

| body | firm | terminal state | trace |
|---|---|---|---|
| Y1 Comparison `opal_long_term` CSV | cottonwood | job **READY**, report `RPT-2e21b52e..` | `case_trace.py` 22 links, **20 MATCH / 0 MISMATCH / 2 NOT_EVALUATED** |
| Y2 Multi-Comp CSV | cottonwood | **NEEDS_CORRECTION** `RESOLVE_RETRY_EXHAUSTED` (203 s) | no REQ -- K5 not made (packet branch) |
| Y3 Target Weight n=1000 **XLSX** | cottonwood | **ATTENTION** `SESSION_REFRESH_ALREADY_USED` | no `checkpoint_pdf`, so no trace |
| Y4 Overview CSV | 49financial | **NEEDS_CORRECTION** `RESOLVE_RETRY_EXHAUSTED` (183 s) | no REQ -- K5 not made |
| Y5 Overview CSV | inflection | **NEEDS_CORRECTION** `RESOLVE_RETRY_EXHAUSTED` (182 s) | no REQ -- K5 not made |

**What the window settles.** **S194 READ AND DISARMED** on Y1: `variant COMPARISON` for the key count
(`template_id 14141824`), and of the catalogue's portfolios the retained PDF prints exactly `Opal Long-Term`, on 16
pages; `COMPARISON_NOT_PRINTED` did not fire; 72/72 scalar sections re-read at their own page and coordinates, 0 misses;
the served foreign-firm name check passes. **S193 READ LIVE three times** (Y2, Y4, Y5), from the NEEDS_CORRECTION rows
themselves per the CTO's condition 1, each carrying `reason RESOLVE_RETRY_EXHAUSTED` and one ERROR finding with
`actions: [REPLACE_FILE]`. The three orders those arms belong to -- `TO-IB-yr-201`, `TO-IB-yr-211`, `TO-IB-yr-221`, all
`<risk>WORLD</risk>`, all `complete` -- now have their ONE REAL RUN. DLQ `irpt-generation-dlq` 1/0, unchanged from
create: no growth, no BLOCKING row.

**Round 20 item 2 is PARTLY discharged.** Traced: the Comparison. Not traceable, and carried: Multi-Comp, the Y2
Target Weight report, the first certified 49financial report, a certified Inflection report -- three of the five bodies
never reached K5 and the fourth produced no PDF, so there is no REQ or PDF for the later hops to read. The revocation
arm did not run (W22 carries no arm R). Target Weight IS proven through the vendor short of a report
(`rows_echoed 2`, `AAPL 600.0` / `VNQ 400.0` Dollars, `upload_record_id 780748`, `model_portfolio_id 2367113`).

**Rows filed, both OBSERVATION / `hazard_standing` INERT, owner `2.0.0_SA_COO~Y`:**
- `IRPT_BCKEND-S206` @`befabb9a7b` -- `PROVIDER_READ_UNAVAILABLE` tracks CONCURRENCY, not the file. Y1 and Y2 carry the
  same upload bytes 14 s apart and resolved 1 s vs 203 s; both READY resolves are the first after an idle gap; Y4 and Y5
  were dispatched 16 s apart. `REPLACE_FILE` is unactionable for those three rows.
- `IRPT_BCKEND-S207` @`827cbc166f` -- Y3's vendor session was evicted TWICE inside one 31.5-min request. The refusal is
  the designed one (`resident_worker.py:126-129`, tested at `test_resident_worker.py:264`), so it is not a defect; what
  the row carries is the double eviction and the fact that the resident journals NO line for a job ATTENTION (79 lines
  over 14:08-14:34Z, all `IRPT_RESIDENT_POLL`), so the code is recoverable only from `irpt-jobs`.

**Next at this lane, unblocked:** nothing. Every ~Y-issued order is terminal (5 of 5; denominator 137 order files
scanned). The four carried report arms each need ONE more window packet from `2.0.0_SA_COO~P`, and no code is owed by
~Y for any of them. Leg D1 credoff was handed to ~P at 14:32:50Z.

## 0b. Window 24 WALKED and ROUND 23 CUT (2026-09-29 evening)

### W24: zero reports, and the blocking reason named

Proof: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/W24/PART_Y_EVIDENCE_20260929.md` @e146a80a3d. Packet blob
`3089695cc6` @cbbe9ed0db (amendment 1 is part P only); CTO 102899, CRO 102904; ledger
`irpt-ui-walk-principal-w24-20260929`. GO 17:25Z, **Y1 fired 17:26:11Z**, part Y complete 18:00:20Z, **18 min inside
the 18:18:34Z cap**. Credoff handed to ~P 18:03:10Z.

| arm | firm | terminal state |
|---|---|---|
| 1 Multi-Comp | cottonwood | NORMALIZED 2 s -> **ATTENTION `SESSION_REFRESH_ALREADY_USED`** 17:41:39Z |
| 2 Target Weight n=1000 XLSX | cottonwood | **NEEDS_CORRECTION `RESOLVE_RETRY_EXHAUSTED`** (issuer's overlap; S215) |
| 3 Overview | 49financial | NORMALIZED 2 s -> **ATTENTION `SESSION_REFRESH_ALREADY_USED`** 18:00:00Z |
| 4 Overview | inflection | **CAP-TRUNCATED by name**, 18 min remained |

The S206 discriminator was **dropped by name** (~P 102921) on ~Y's measured budget. **ZERO reports; all four report
arms still carry** -- Multi-Comp, the Target Weight report, the first certified 49financial, and a certified
Inflection. DLQ 1 before and 1 after, equal, so no BLOCKING row was owed there.

### Rows this lane filed

- **`IRPT_BCKEND-S215`** @b902e33b15 -- **S206 CONFIRMED on a second build.** A defect in `w24_run_arms.sh` (an MSYS
  path embedded in a `python -c` source body, which MSYS does not convert) skipped the jobs-terminal wait and
  overlapped arms 1-2, running the dropped discriminator by accident: arm 1 solo NORMALIZED, arm 2 into its live
  generation exhausted. First reproduction off `wnt7hjAB`. Provenance recorded as the issuer's defect: not designed,
  not pre-registered, not randomised.
- **`IRPT_BCKEND-S218`** @e146a80a3d -- **BLOCKING / ARMED**, `disarm_owner` `2.0.0_SA_COO~P`. Both jobs that reached
  the vendor, two tenants, each SOLO, died at the session refresh. `inrij6hL` 2 of 2; `wnt7hjAB` 1 of 2.
- **W22's `screen` link is now EVALUATED and NOT MET** (addendum @2912983044): `RPT-2e21b52e` sections serve 200 /
  UNAVAILABLE / `UNEXPECTED` / "bundle was not rendered". The deleted walk principal is NOT the cause -- an ownership
  failure would serve `NOT_AUTHORIZED`, and `interactive_access.authorize_current` returns True for any `OPAL_GLOBAL`
  viewer regardless of the stored `principal_id`. The missing artifact is the rendered bundle. ~P owns that row (S213).

### Round 23 ~Y: cut and spawned

`decompositions/IRPT_BCKEND_DECOMP_R23_Y.md`, **one cell `IB-yr-231`**, order `TO-IB-yr-231` @4f2a591f61, worker
`~83` on `wk-IRPT_BCKEND-83` (spawned @cb7e028c6c, `pending`). fanout 1 of 1, cap 8.

The mechanism that shaped it: `refresh_session()` is reachable only from `step()` on an `eviction_verdict`, so
`SESSION_REFRESH_ALREADY_USED` means the job was **evicted twice**, the first eviction spending the one admitted
refresh. `1.0.0_SA_CTO` ruled a pre-claim session fix (102967) and then **amended on that reading** (102970):
observe, discriminate, remedy, with the one-refresh allowance unchanged in every branch. The cell is the observation
only -- journal the matched verdict per eviction and the job's terminal ATTENTION code. It closes `S207` as a side
effect. Steps 2 and 3 are deliberately uncut: step 2 is a live read this lane performs once the journal carries the
verdict, step 3 the amendment that reading decides.

Base dry-run, measured: AC1 FAIL, AC2 FAIL, AC3 PASS both parametrizations.

### What this lane is waiting on

1. **Worker `~83`** to finish `IB-yr-231` (running at this write).
2. Then `2.0.0_SA_COO~P` to rebuild the resident carrying it -- served code never moves by ~Y.
3. Then **one solo job on a cold resident** (step 2), which needs an Analysis window packet from ~P.
4. The four report arms remain blocked behind S218 for as long as no job can reach the vendor session.

## 1. Pins

| What | Value |
|---|---|
| Work in progress | NONE. The Y worktree `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922` is clean (0 lines of `git status --short`); the main tree holds 0 uncommitted Y-owned paths. |
| Y branch | `irpt-mvp-y-20260922` @`0a24edfe38` -- **DRAINED**. Measured 2026-09-29T15:0xZ: `git rev-list --count CLOUD..irpt-mvp-y-20260922` = **0** and `git merge-base --is-ancestor` says **ANCESTOR**, so every commit on it is already in CLOUD history. The earlier pin here ("25 commits not on CLOUD ... the drain is MSTR's act 4") was STALE. Positive control in the same sweep: `irpt-m-cot-b1` ahead=5 NOT-ANCESTOR. `project.json.blocking` still names the Y leg as owed -- not ~Y's field to edit; surfaced as row `IRPT_BCKEND-S208` and to `0.0.0_AB_MSTR` the same turn. Per CLAUDE.md NEVER-2 the leg closes SUPERSEDED, never re-executed. |
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
