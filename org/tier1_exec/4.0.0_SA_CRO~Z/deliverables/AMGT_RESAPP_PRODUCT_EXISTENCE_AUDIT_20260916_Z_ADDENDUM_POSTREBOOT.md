# AMGT_RESAPP -- PRODUCT EXISTENCE AUDIT, ADDENDUM: the served plane re-measured after the 07:56Z reboot

**Author** `4.0.0_SA_CRO~Z`. **Written** 2026-09-16 13:45-13:58Z at HEAD `933a40dab2` (SITEZ). **Push state:** LOCAL
(LD-0522; `0.0.0_AB_MSTR~Z` pushes; none requested). **Extends** `AMGT_RESAPP_PRODUCT_EXISTENCE_AUDIT_20260916_Z.md`
@`a10eece02e` (PRD v0.8) and `AMGT_RESAPP_POST_ROUND12_RESIDUAL_PROJECTION_20260916_Z.md` @`1d5454312a`.

**Why now.** Site Z rebooted at 07:56:32Z and every ~Z seat and the six round-12 workers died with it. Andrew-direct
~13:33Z (record @`933a40dab2`, msg 23438): pick up `/canonical-flow AMGT_RESAPP`. This seat's role on the project is
his item 5 (record @`c05a41c0f4`): refer back to the PRD and assess whether the product exists. The PRD moved
v0.8 -> v0.10 while this seat was down, and a reboot can move box-plane preconditions in BOTH directions, so the
audit's box-plane rows were perishable and are re-read here rather than carried forward.

---

## 0. THE VERDICT, UNCHANGED, WITH TWO MOVES

**Nothing on the served plane moved between 04:57Z and 13:50Z.** The four gaps G1-G4 stand exactly as measured.
Two things did move, neither on the plane a person touches:

| move | direction | evidence |
|---|---|---|
| the Bloomberg DAPI on this box is UP | in the product's favour | `bloomberg_health` 13:4xZ `ok: true`, `//blp/refdata` at `127.0.0.1:8194` (04:5xZ read `ok: false`). The model-block producer's precondition (G2) and the on-demand pull's terminal (G4) are reachable again; the producer itself is still a script a person runs |
| the union universe was rewritten by a worker whose branch is NOT merged | world ahead of record | `s3://opal-data-harvest/universe/v1/2026-09-16.json` written 07:32:10Z (pool now 133 objects, was 132); by its `resolution` field 191 MEASURED / 59 UNRESOLVED of 250 rows (the audit read 33 / 223 of 256 on the 2026-09-15 object). Its producer, proof instance and four rows `W25-S1..S4` sit on `wk-amgt_resapp-12-25` @`0a5064ded5` (rk-4), unmerged at HEAD |

**The PRD delta v0.8 -> v0.10 adds one outcome and no surface.** FWD-20 (a filings-and-history-seeded house
free-cash-flow forecast with Divergence on the Model tab, bar EXERCISED) was appended at L10 of round 11; it has no
route, no component and no producer on any plane this seat read. **1 of the 16 round-12 task orders names it**
(`comp-find 'FWD-20' task-orders/`: 3 hits in 1 of 80 files scanned): rk-5, and only for its REPORTING side --
Divergence D on the Model tab, with the order's own line *"FWD-20's house forecast does not [serve]"*. No cell produces
the house forecast itself. It is a fifth no-surface outcome beside FWD-7, FWD-12 and FWD-14, with the difference that
its producer has no cell yet. (A first draft of this line said "0 of 16"; the rail census corrected it before commit.)
The corrected contract `C-ROUND12-PULL-WIRED` (no Lambda consumer) matches this seat's projection note K.

---

## 1. THE GAPS, RE-READ (same instruments, new vintage)

| gap | 04:57Z | 13:50Z | round-12 cell that owns it | state of that cell at HEAD |
|---|---|---|---|---|
| G1 page not served | DEV `be8cf218` 0 of 48 files | DEV `be8cf218` (= `origin/DEV`) **0 of 47** files under `src/pages/SecurityAnalysis`, 0 route lines; drain `refs/drains/rj-portal` `b616b759` 47 files (this instrument is `ls-tree -r` on the folder; the earlier 48 is not re-derived here). Portal branch `wk-amgt_resapp-12-23-portal` exists, checked out in a worktree, unmerged | rk-1 (`~23`) | pending; worker died at the reboot |
| G2 model block does not reach the page | `/thesis` 200 `model_status ABSENT`, 0 figures | **same**: 200, `ABSENT`, `header_figures 0`. Adapter `opal-amgt-scoped-api` LastModified `2026-09-15T19:01:10Z`, CodeSha `9ubWPnhz`, env 2 keys (no `MODEL_BLOCK_ROOT`) -- unchanged. `derived/model_block` 14 objects / 4 keys, newest 2026-09-11 -- unchanged | rk-2 (`~24`) | pending; the never-widen halves for the model-block read are landed (`ledger/NEVER_WIDEN_ROUND12_MODEL_BLOCK_READ_{COO,CTO}_HALF.md`) |
| G3 print 500 | `/print` 500 | **same**: 500 | rk-6 (`~24`) | pending |
| G4 on-demand pull disconnected | `/refresh` 501; enqueue Lambda unwired; 0 consumers | enqueue Lambda `opal-research-pull-enqueue` unchanged (2026-09-11); **0** consumer processes on the box; queue not re-read (no change signal) | rk-7 (`~24`) | pending |
| posture route | cited Z-S107 (adapter predates the route) | **now MEASURED**: `/posture` **404** on the deployed adapter -- CODE-AHEAD-OF-DEPLOY confirmed by direct invoke | rk-2 / rk-8 | pending |
| box collection plane | 3 of 3 Opal research tasks DISABLED | **same**: `Opal Data Harvest - Local Publications`, `OpalResearch-ExecManagement`, `OpalResearch-FilingsAnalyzer` all Disabled after the reboot (6 other `OPAL_*` tasks Ready) | reserved to Andrew (@`9db2a36cdc`) | -- |

**Why the served plane could not have moved:** the three round-12 orders that are complete (rk-9 criteria repair at
the issuer, rk-10 the social source classified, rk-11 the preserved breaches; proof instances VALID at HEAD, 3 of 3)
are record cells. None writes a route, a component, a deployment or a pool prefix a person reads.

---

## 2. THE ROUND-12 RECTANGLE AGAINST THE AUDIT (so the CTO's L10 can grade coverage, not just completion)

| audit item | round-12 cell | worker | status |
|---|---|---|---|
| G1 page onto DEV | rk-1 | ~23 | pending |
| G2 model-block read on the deployed plane | rk-2 | ~24 | pending |
| G3 print pack packaged server-side | rk-6 | ~24 | pending |
| G4 on-demand pull wired | rk-7 | ~24 | pending |
| FWD-7 / FWD-12 / FWD-14 no surface | rk-12 | ~23 | pending |
| FWD-6 compare-two-versions surface | rk-16 | ~23 | pending |
| FWD-18 the one chart | rk-15 | ~23 | pending |
| FWD-13 identity / union universe | rk-4 | ~25 | L7 done on the branch (2 criteria REFUSED with grounds), branch unmerged |
| price axis (Z-S105) | rk-3 | ~26 | pending |
| **FWD-20 house forecast** | rk-5 (reporting side only: Divergence on the tab) | ~25 | pending; **the forecast producer itself is uncut** |

Chain `~23` holds five of the seven product-surface cells (rk-1, rk-8, rk-12, rk-15, rk-16) and `~24` holds three
(rk-2, rk-6, rk-7); with both workers dead at the reboot, every product-surface gap waits on the COO's re-dispatch.
That is the COO's L7 act and this seat does not touch it; it is recorded so that a later "3 of 16 complete" is not
read as "3 of 16 gaps closed" -- **0 of the audit's gaps are closed at HEAD.**

---

## 3. WHAT THIS ADDENDUM DOES NOT CLAIM

- No FWD graded; no world act (GET invokes and reads only; no POST, no pool write, no merge, no deploy).
- The rk-4 branch's two REFUSED criteria are not adjudicated here (L9). The universe object's producer determinism
  and schema checks are the worker's own claims in its proof instance, cited not re-run.
- Whether the page builds against DEV is still UNMEASURED (merge-tree counts conflicts, not TypeScript).
- The residue the reboot left in the shared tree (a merge in progress on `wk-amgt_resapp-12-25` with the channel file
  in conflict, the stranded rows S111/S112) is the COO's; this seat read it and touched nothing.

## 4. INSTRUMENTS AND VINTAGES

| instrument | observes | vintage |
|---|---|---|
| `mcp__bloomberg__bloomberg_health` | the DAPI on this box | 13:4xZ |
| boto3 `get_function_configuration` x3; `invoke` GET `/thesis` `/print` `/overlay` `/posture` for `BA_US_Equity` with `x-firm-id` | the deployed adapter and what it answers | 13:50:40Z |
| boto3 `list_objects_v2` paginated (133) + `get_object universe/v1/2026-09-16.json` | the pool | 13:5xZ |
| `git -C portal ls-tree -r`, `for-each-ref refs/drains/`, `branch --list 'wk-*'` | which branch carries the page | DEV `be8cf218`, 13:4xZ |
| `Get-ScheduledTask`, `ps -ef` | box pipelines and consumers | 13:4xZ |
| `git branch --no-merged`, `git status --porcelain`, `.git/MERGE_HEAD` | the residue | HEAD `933a40dab2`, 13:5xZ |
| `.tools/proof-of-spec-check.py` on rk-9 / rk-10 / rk-11 | the three terminal orders | HEAD |
| `git diff 1170b4da69 49aedcf88b -- prd/` ; `grep FWD-20 task-orders/*rk-*.md` | the PRD delta and its coverage | HEAD |
