# AMGT_RESAPP -- PRODUCT EXISTENCE AUDIT (Andrew-direct 2026-09-16 ~04:3xZ, item 5)

**Author** `4.0.0_SA_CRO~Z`. **Written** 2026-09-16 04:35-05:1xZ at HEAD `afc02ead18` (SITEZ; the addendum
record is `c05a41c0f4`). **Push state:** LOCAL (LD-0522; `0.0.0_AB_MSTR~Z` pushes; none requested).

**The question, in his words:** *"referring back to the PRD and assesing if we actally have a product or if
there is some crucial gap in the development of the application (e.g. data pipeline doesnt exist, frontend
doesnt exist, etc.)"*. So the question is DOES THE THING EXIST on the plane a person would touch -- not is
it good, not does the PRD describe it, not is a row graded. Every verdict below is read from an ARTIFACT
(a file at a commit, an object in S3, a deployed function's configuration and archive, a route's answer to
a direct invocation, a scheduled task's state), never from a task-order status, a proof-of-spec instance
or a packet sentence. Where a packet number is cited it is marked as cited, not re-measured.

**PRD audited:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` v0.8 ADMITTED @`1170b4da69`
(19 outcomes FWD-1..FWD-19, 18 of them EXERCISED-barred; ten contracts; the s.4 surface manifest S1-S16).

---

## 0. THE ANSWER

**We have a deployed backend, a real data store and a page that exists as code. We do not have a product a
person can open tonight, and four material parts the PRD promises are missing on the plane a user would
touch.** Each is exactly the failure mode he named: the record reads complete and the part is not there.

| # | the gap, in his terms | measured state | one line of evidence |
|---|---|---|---|
| G1 | **the frontend does not exist as a served page** | CODE-ONLY on a portal drain ref; on NO branch a person is served from | `portal` DEV @`be8cf218` carries 0 of the 48 SecurityAnalysis files and no `/security-analysis` route; they exist only at `refs/drains/rj-portal` @`b616b759`, whose merge-base with DEV is 2026-09-10 and DEV is 212 commits past it. PROD `portal-v2.1.179` has no such page. Viewable only in a developer worktree (`C:/tmp/portal-resapp-view` @`0e153399`, vite stopped). `git merge-tree --write-tree DEV b616b759` = rc 0, **0 conflicts** -- it is one clean merge from DEV, and that merge has not been made. |
| G2 | **the model-block data pipeline does not exist as a pipeline, and its output does not reach the page** | MANUAL SCRIPT on a signed-out terminal; 4 of 89 covered names; the deployed adapter reads a folder that is not in Lambda | `integrations/bloomberg/research/model_block_pull.py` is run by hand (no scheduled task matches `model`; `bloomberg_health` at 04:5xZ: `ok:false`, "is the Terminal running + logged in?"). Pool `derived/model_block/` holds 4 keys (BA, BABA, NVDA, SAP) of 89 coverage / 256 universe. The deployed `opal-amgt-scoped-api` env carries only two table names; `MODEL_BLOCK_ROOT` defaults to `org/missions/.../0.9.0_WK_AMGT_RESAPP~1` (`scoped_amgt.py:135-138`), absent in Lambda. **Direct invoke 04:57Z, GET `/security/BA_US_Equity/thesis`: 200, `model_status: ABSENT`, `header_figures 0`, `fiscal_year_figures 0`.** The Model tab, FWD-1's whole content, renders nothing on the served plane. |
| G3 | **the print pack -- Adam's artifact, the brief's displacement test (FWD-5) -- does not serve** | DEPLOYED ROUTE, RETURNS 500 | **Direct invoke 04:57Z, GET `/security/BA_US_Equity/print`: 500 `internal error in the AMGT scoped read API`.** Mechanism, read from the bytes: `lib/research/print/render_pack.py` imports `matplotlib` and reads `pypdf` at module level and reads its inputs from the worker-1 deliverables folder and a OneDrive `.docx` template path on this box (`render_pack.py:40-44, 53-57`); the deployed archive `research/opal-amgt-scoped-api.zip` (747,396 B, 183 entries, 15 top-level) carries `matplotlib ABSENT`, `pypdf ABSENT`, `numpy ABSENT`; and `_print_pack` first needs `read_model_block` from the same absent root (`scoped_amgt.py:2475-2505`). The page's Print button (`PrintExportAction.tsx`) would show `[REFUSED: ...]`. |
| G4 | **the on-demand pull (FWD-2, "type a ticker the firm has never covered") is three pieces with zero wiring** | DISCONNECTED | The page's Refresh calls `POST /api/scoped/amgt/refresh`; the deployed adapter answers **501 "refresh has no queue carrier declared"** (`scoped_amgt.py:2463-2468`). The enqueue Lambda `opal-research-pull-enqueue` (LastModified 2026-09-11) hangs on `POST /api/private/research/pull`, a route the page never calls (0 references in `amgt-lead-panel.ts`). Queue `opal-research-pull-requests`: 0 visible, 0 in flight, no event-source mapping. The box consumer `pull_consumer.py` is "a poller a person starts" -- no process, no task. And the terminal it would pull from is signed out. |

**Three more outcomes have NO product surface at all** -- each exists as a Python module a person runs by
hand, with no adapter route (0 of the 11 mounted) and no page component (0 hits on the drain ref):

| outcome | module | what the PRD promised | what exists |
|---|---|---|---|
| FWD-7 coverage freshness ("Adam sees which covered names have gone stale") | `lib/research/freshness/build_view.py` | Adam's one place | "the generator a person runs by hand" (its own docstring); writes a JSON nobody serves |
| FWD-12 input ledger ("see where each input came from and re-run any one alone") | `lib/research/ledger/ledger.py` | per-class source / last run / outcome / re-run | `packs/<key>/input_ledger.json` for 4 keys, all dated 2026-09-11; `rerun()` is a function, not a button; the page's one Refresh button 501s |
| FWD-14 list register + rot signal | `lib/research/lists/rot.py` | owned lists, "somebody is told" | "a script a PERSON runs"; rendered only by the FWD-7 view, itself unserved |

**And the collection plane is off:** all three local pipelines are registered and DISABLED (`Opal Data Harvest -
Local Publications`, `OpalResearch-FilingsAnalyzer`, `OpalResearch-ExecManagement`, read from Task
Scheduler 04:4xZ). The ONE scheduled AMGT job in AWS, `amgt-resapp-chatter-axis` (`cron(0 10 * * ? *)` UTC,
ENABLED), re-ranks a pool of **7 article bodies for 3 names** (BA 2, COST 2, HD 3; newest 2026-09-15T05:01Z)
every day. The harvest mechanism and cadence are reserved to Andrew by name (@`9db2a36cdc`), so this is a
DECISION he holds, recorded here as the measured consequence: the pool is a five-name commissioning set and
nothing refreshes it.

---

## 1. THE COMPONENT TABLE -- every engine the PRD names, by artifact

State vocabulary (four values, one axis: how far the artifact is from a person's hand): **ABSENT** (no
artifact) / **CODE-ONLY** (a file at a commit; nothing deploys or serves it) / **DEPLOYED-NOT-SERVING**
(a live function or route that answers with a refusal or nothing) / **SERVED** (a person on the served plane
would see it; PARTIAL qualifies the denominator).

| surface (PRD s.4 / contract) | outcome | artifact and where | state | denominator | instrument |
|---|---|---|---|---|---|
| The page: header + five tabs (`C-PAGE-LAYOUT`) | FWD-15..19 carrier | `portal` `src/pages/SecurityAnalysis/` 48 files + `src/api/endpoints/amgt-lead-panel.ts`, routed `/security-analysis` in `App.tsx:433-434` -- **only at** `refs/drains/rj-portal` @`b616b759` | **CODE-ONLY** | DEV: 0 of 48 files, 0 route lines; drain: 15 commits DEV lacks | `git ls-tree`, `git diff --stat`, `git merge-base`, `git merge-tree` |
| The adapter (11 routes, `C-ONE-IDENTITY` boundary) | every per-security read | `opal-amgt-scoped-api` python3.11, LastModified 2026-09-15T19:01:10Z, CodeSha `9ubWPnhz...`, 747,396 B, role `opal-amgt-scoped-api-role`, routes CUSTOM-authorized on the portal HTTP API (`infra/aws/terraform/harvest/scoped-amgt-api.tf`) | **DEPLOYED, answering** (200 on overlay and thesis) -- built from `5ae785828e`, so it predates rj-12's posture route (Z-S107, cited) | 11 routes declared = 11 in `scoped_amgt_route_table()` | `get_function_configuration`, `head_object` + zip listing, direct invoke |
| Ranking producer (`C-RANKING-GENERATION`) | FWD-15 | `amgt-resapp-chatter-axis` python3.12, 2026-09-15T20:00:21Z; EventBridge Scheduler `amgt-resapp-chatter-axis-daily` ENABLED `cron(0 10 * * ? *)` UTC | **SERVED** (chatter axis); **ABSENT** (price axis: no generation ever written, Z-S105 cited) | generation `20260915T200841Z-adf383740a9e`, 10 of 10 rows keyed (rj-10 capture, cited) | `list_functions`, `list_schedules`, tf read |
| The pool (`C-ONE-STORE`; FWD-6's store) | FWD-6, FWD-4 | `s3://opal-data-harvest`, versioning **Enabled**, 132 objects | **EXISTS** | inventory in s.2 | boto3 paginated `list_objects_v2` + `get_bucket_versioning` |
| S1 the model block | FWD-1 | producer `integrations/bloomberg/research/model_block_pull.py` (manual, DAPI on this box); pool `derived/model_block/` 14 objects / 4 keys; served by `read_model_block(MODEL_BLOCK_ROOT)` | **DEPLOYED-NOT-SERVING** (0 figures) + producer **CODE-ONLY-MANUAL** | 4 of 89 covered names have a block; 0 of 4 reach the page | direct invoke; env read; `bloomberg_health`; Task Scheduler |
| S2 the on-demand pull | FWD-2 | page button -> `/refresh` (501); `opal-research-pull-enqueue` + SQS `opal-research-pull-requests`; `pull_consumer.py` | **DISCONNECTED** (G4) | 0 messages, 0 consumers, 0 page calls to the enqueue route | handler read; `get_queue_attributes`; `list_event_source_mappings`; ps + Task Scheduler |
| S3 the provenance face | FWD-3 | `ProvenanceLine.tsx`; `lib/research/provenance/` | **CODE-ONLY** in the page; annotates 0 served figures | -- | drain-ref read |
| S4 the coverage reader / header feed | FWD-4, FWD-16 | `lib/research/coverage/pool_reader.py`; `/overlay` serves `description` (SERVED, from D-1) and `feed.items` (WSJ Boeing item) for BA | **SERVED-PARTIAL** on the deployed plane, page CODE-ONLY | 7 bodies / 3 names in the pool | direct invoke; pool inventory |
| S5 the print renderer | FWD-5 | `lib/research/print/render_pack.py` + `/print` | **DEPLOYED-NOT-SERVING** (500) (G3) | 0 printable packs on the served plane | direct invoke; zip listing; source read |
| S6 the version store | FWD-6 | bucket versioning + timestamped `derived/model_block/<key>/<stamp>/` | store **EXISTS**; the compare-two-versions surface **ABSENT** | 0 hits for version / earlier / compare in the page components | `git grep` on the drain ref |
| S7 coverage-freshness view | FWD-7 | `lib/research/freshness/build_view.py` | **CODE-ONLY** (no route, no component) | 0 of 11 routes; 0 page hits; 0 adapter refs (positive control `peers/v1` 2) | grep with controls |
| S8 the peer set (`C-SIMILARITY-RANKER`) | FWD-8 | `lib/research/peers/`; pool `peers/v1/` 33 objects; `/peers` | **SERVED** | 33 objects; 10 of 33 with members, CSC values 1 of 5 marked columns (W18-S13, cited) | pool inventory; adapter read |
| S9 the drafting face (`C-FILINGS-ANALYZER`) | FWD-9 | pool `drafting/v1/` 5 objects; `/thesis` carries `drafted_sections`, `drafting_status`, `held_uncited_count` | **SERVED** for 5 names | 5 of 89; 38 of 38 sentences with passages on the rj-3 capture `f2e7c040...` (cited, not re-read here) | direct invoke (keys present); pool inventory |
| S10/S11 the check face + rules | FWD-10 | `CheckFaceBadge.tsx`; `lib/research/checkface/`, `lib/research/rules/` | **CODE-ONLY**; annotates 0 served figures | -- | drain-ref read |
| S12 the identity layer (`C-ONE-IDENTITY`) | FWD-13 | pool `crosswalk/v1/2026-09-15.json`; `resolve_identity` at the route boundary; `IdentityLine.tsx` | **SERVED** (`identity_status: MEASURED` for BA on `/overlay`) | universe 256 names: 33 MEASURED / 223 UNRESOLVED (holding 167, coverage 86, both 3) | `universe/v1` read directly; direct invoke |
| S13 the social feed | FWD-11 | pool `social/v1/_measurement/2026-09-15.json` (1 object); header prints the server's status sentence | **MEASURED ONLY** -- no feed | 1 Reddit job, 48 records, 0 admitted (rj-13, cited) | pool inventory; `HeaderBrief.tsx:108-109` |
| S14 the input ledger | FWD-12 | `lib/research/ledger/ledger.py`; pool `packs/<key>/input_ledger.json` x4 (2026-09-11) | **CODE-ONLY** (no route, no component) | 0 of 11 routes; 0 page hits | grep with controls |
| S15 the list register + rot | FWD-14 | `lib/research/lists/{build_lists,rot,impostor}.py` | **CODE-ONLY** | rendered only by S7, itself unserved | source read |
| S16 the Lead Panel | FWD-15 | `LeadPanel.tsx`, `RankedList/RankedChart/StarredList`; `/lead-panel/rankings` | **SERVED** data, page CODE-ONLY | Trending x Chatter 10 rows; Price ABSENT | rj-10 capture (cited); handler read |
| Exec Management (`C-EXEC-MANAGEMENT`) | FWD-17 | pool `management/v1/` 5 names + `_pool`; `ExecManagementTab.tsx`; task `OpalResearch-ExecManagement` **DISABLED** | **SERVED-PARTIAL** for 5 names | Lusha 11 of 48 officers matched, no dates (rj-8, cited) | pool inventory; Task Scheduler |
| Filings + the one chart (`C-FILINGS-ANALYZER`) | FWD-18 | pool `filings/v1/` 10 objects / 5 names; `ThesisDriverChart.tsx`; task `OpalResearch-FilingsAnalyzer` **DISABLED** | **SERVED-PARTIAL** (prose); chart **ABSENT** | thesis chart ABSENT 5 of 5 (W18-S12, cited) | pool inventory; Task Scheduler |
| Posture (`C-POSTURE`, `C-UNION-UNIVERSE`) | FWD-19 | pool `posture/v1/` 2 keys (BA, BABA); `read_posture` at HEAD; `PostureTab.tsx` | **CODE-AHEAD-OF-DEPLOY**: the deployed adapter predates the route (Z-S107, cited) | 2 of 256; Opal side 3 names (BA, HD, VLO) | pool inventory; function LastModified vs drain time |

---

## 2. THE POOL, INVENTORIED (boto3, paginated, 132 objects, read 04:4xZ; versioning Enabled)

| prefix | objects | distinct keys | newest (UTC) |
|---|---|---|---|
| `crosswalk/v1` | 1 | 1 | 2026-09-15T08:02Z |
| `universe/v1` | 1 | 1 | 2026-09-15T08:02Z |
| `derived/model_block` | 14 | 4 (BA, BABA, NVDA, SAP) | 2026-09-11T19:18Z |
| `derived/model_block_fye` | 3 | 3 | 2026-09-11T19:18Z |
| `raw/bloomberg` | 13 | 4 | 2026-09-11T19:18Z |
| `raw/seekingalpha` | 18 | 3 | 2026-09-11T19:18Z |
| `packs/<key>` | 5 | 5 (4 ledgers + NVDA `status.json`) | 2026-09-11T19:18Z |
| `publications/v1` | 7 | 5 publishers | 2026-09-15T05:01Z |
| `publication-links/v1` | 7 | 3 (BA, COST, HD) | 2026-09-15T05:01Z |
| `filings/v1` | 10 | 5 | 2026-09-15T09:47Z |
| `drafting/v1` | 5 | 5 | 2026-09-15T09:47Z |
| `peers/v1` | 33 | 33 | 2026-09-15T09:46Z |
| `management/v1` | 6 | 5 + `_pool` | 2026-09-15T15:48Z |
| `posture/v1` | 2 | 2 | 2026-09-15T16:56Z |
| `social/v1` | 1 | `_measurement` | 2026-09-15T16:56Z |
| `lib/local-publications` | 6 | 1 release | 2026-09-15T14:49Z |

Read this table against the universe: 256 names, 33 with a canonical key. Every derived prefix is a
five-name (or smaller) set. Nothing in the pool has moved since 2026-09-15T16:56Z.

---

## 3. WHAT IS REAL AND WORKS -- so the gaps are not read as "nothing exists"

- The adapter is deployed, edge-authorized and answering: identity MEASURED, company description SERVED from
  the drafting object, the publisher feed SERVED (a WSJ Boeing item with its canonical URL), on a direct
  invocation this seat made at 04:57Z.
- The chatter ranking runs daily on a schedule and its rows carry the canonical key.
- The pool is one store with versioning on, a crosswalk, a union universe, filings, drafting, peers for 33
  subjects, management for 5 and posture for 2.
- The page code is whole -- header, five tabs, print action, harnesses -- and merges into DEV with zero
  conflicts (measured, not merged).

---

## 4. WHAT THIS AUDIT DOES NOT CLAIM

- No FWD is graded here; grading is L9's and every EXERCISED bar is a person's act.
- The page was not exercised in a browser by this seat (the round-11 browser half did, against a local vite
  serve of `0e153399`, cited). Whether the page BUILDS against DEV's 212 newer commits is UNMEASURED --
  merge-tree measures conflicts, not TypeScript.
- The drafting sentence count on the served plane was not re-read by this instrument (keys present; the count is rj-3's).
- The CVO's round-11 slug on branch `cvo-amgt-r11-20260915` (msg 23367) was not read; it is the CTO's item.
- No world act: no invoke of a POST route, no watchlist write, no terraform, no merge, no deploy, no pool write.
- A print on the OTHER side of the seam was not tried: the renderer may well run on this box by hand against
  the worker-1 folder. That is not the product; the product is the button on the page.

---

## 5. WHAT THE CTO's L10 CAN TAKE FROM THIS (offered as inputs; the cut is not this seat's)

The four gaps each close with ONE act, and three of the four are already named in `ROUND11_PACKET.md` s.5
(8b the model-block read, 8c the adapter redeploy) or in the PRD's own limits. The two that are NOT named
anywhere in the round-11 record are **G1** (the page onto DEV -- "no portal promote necessary" removes the
PROD step, not the DEV integration; a page on a drain ref is a page nobody opens) and **G3** (the print pack:
as built it cannot serve from Lambda -- the renderer, its libraries and its inputs all live on this box; that
is an L4 contract call: package it, move it, or make print a browser act). **G4** is a wire-or-retire call at
L2/L4: the three pieces exist and none touches another. The three no-surface outcomes (FWD-7, FWD-12,
FWD-14) each need a route and a component or an honest retirement to a script.

---

## 6. INSTRUMENTS AND VINTAGES

| instrument | observes | vintage |
|---|---|---|
| `git ls-tree`, `git diff --stat`, `git merge-base`, `git log`, `git merge-tree --write-tree` on `portal` | which branch carries the page; conflict count | DEV `be8cf218`, drain `b616b759`, 04:4xZ |
| `git grep` on `b616b759` with positive controls | page components / client calls present or absent | 04:4x-04:5xZ |
| boto3 `get_function_configuration` x3, `head_object` + `zipfile` on the artifact, `list_functions` (217), `list_schedules` (23), `list_rules` (144), `list_queues` (26), `get_queue_attributes`, `list_event_source_mappings` (6) | the deployed functions, their env, their archive contents, schedules, the queue | 04:4xZ |
| boto3 `list_objects_v2` paginated + `get_bucket_versioning` + `get_object universe/v1` | the pool | 04:4xZ, 132 objects |
| boto3 `invoke` RequestResponse on GET `/print`, `/thesis`, `/overlay` for `BA_US_Equity` with `x-firm-id` | what the served plane answers | 04:57:42Z |
| `mcp__bloomberg__bloomberg_health` | the terminal DAPI on this box | 04:5xZ, `ok:false` |
| `Get-ScheduledTask`, `ps -ef`, `Get-Process` | box-side pipelines and consumers | 04:4x-04:5xZ |
| source reads: `scoped_amgt.py:135-138, 2389-2530`, `render_pack.py:1-60`, `build_view.py`, `ledger.py`, `rot.py`, `model_block_pull.py`, `pull_consumer.py`, `worker.py`, `install-schedule.ps1`, `scoped-amgt-api.tf`, `sqs.tf`, `api-gateway.tf`, `chatter-axis-schedule.tf` | the mechanisms | HEAD `afc02ead18` |
| cited, not re-measured: `ROUND11_PACKET.md` @HEAD (rj-10 captures, W18-S11/S12/S13, Z-S105/S107), `ADJUDICATION_v10.md`, the PRD s.4/s.9 | round-11 numbers | as stamped there |
