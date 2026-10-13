# AMGT (Asset Management) -- voice memo vs projects, alignment report, 2026-10-13

Input: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/AMGT_REVIEW_TRANSCRIPT.md` (Andrew, morning of 2026-10-13).
Readers: Andrew Berman and the laptop CTO. Read-only report; read window about 16:00Z-16:30Z on 2026-10-13. Workspace branch box/laptop.
Every claim carries its source. `unknown` means the item was not read, and the reason is given.

**Conclusion.** None of Andrew's three AMGT priorities is owned as a defined outcome today. (1) The Security Analysis page is
live for staff on PROD, but its first request still takes about 20 s cold. The current work (round 102) adds timing log lines and
does not fix load time or check that every page is complete. Newer page work is held behind a PROD promote listed as "waiting on
Andrew", although the push rules exempt an internal page. (2) No project owns an AI fill (a model call backed by web search) for
thin text sections. Model-call code exists for the thesis, posture and CEO search, but not for a management bio or recent
developments, and the two site Z batch tasks for those areas are disabled. (3) Asset managers cannot reach the harvest bucket
through the gateway today. The live catalog has no harvest or research entry, and the catalog project is parked. Most AMGT effort
is going to the item Andrew asked to run "at its pace" (harvest collection, 3 seats) and to performance instrumentation (2 seats).
No seat works priority 2 or 3.

---

## 1. What Andrew asked for (ranked)

1. **A usable Security Analysis page: the 93 research pages fully loaded, correct, with a clean interface, loading fast.**
   "we need to assess really what needs to happen to at least get the 93 research pages completely loaded in here, we need to make
   sure that all information is displaying correctly that the user interface is clean and easy to use, that the pages load fast,
   that we, which I believe we should have handled already." He conditions the full app on time: "if that is going to take too
   long ... if that's held up on certain backfill elements, which are dependent on the DEM QE project, MDPF underscore DEM QE".
2. **AI fill for thin text sections on every page (executive management bio summary, recent management developments, hard thesis
   items), using our own sources first and web search where we have nothing.** "I essentially want to fill in these gaps with
   dedicated, open AI calls that do the AI analysis to fill out obvious text sections" / "whatever we were not able to get, uh,
   dedicate to web search". The premise: "we want to be able to display information for all of them."
3. **Asset managers reach the opal-data-harvest folders from their own Claude, through the gateway and an MCP index on that
   bucket, set up quickly.** "figure out the, open gateway mechanics for how to connect the ... open dash data dash harvest folders,
   uh, and set up the MCP index for that bucket. How to set that up quickly and easily so that the asset managers can use that with
   their cloud" ("cloud" here is the transcript's rendering of "Claude").
4. **Lower priority, run at current pace:** "harvest, the design, everything else can kind of continue along on its pace."
   **Bar for closing:** "We need to close at least a functional V1."

## 2. Project table

FWD-n = a numbered outcome in the project's PRD ENDPOINT section. Box status report = `org/tier1_exec/4.0.0_SA_CRO/deliverables/BOX_STATUS_REPORT_<box>_20261013.md`
(byte-identical, by md5, to the copies in `C:\Users\AndrewBerman\Desktop\today_report\`).

| Project | Andrew's intent | Chartered (PRD outcomes) | Delivered / live (evidence) | Verdict | Move |
|---|---|---|---|---|---|
| **AMGT_RESAPP** (D5, dell1, round 102 executing) | Priority 1: the 93 pages complete, correct, clean, fast. Priority 2 sits on this page. | 39 outcomes (`prd/AMGT_RESAPP_PRD.md` :491-1092). They cover a first-draft pack (FWD-1), defensible numbers (FWD-3), recent news (FWD-4/16), a management roster with tenure (FWD-17, from filings, then Lusha, then an IR-domain search for the CEO, :2177), a filings-read thesis (FWD-18), posture vs a comparable (FWD-19), a machine-prose marking (FWD-9), the export (FWD-30) and the team's management passage (FWD-31). FWD-21..29 (presentation) moved to DSGN_AMGTV1 (:915). **No outcome covers a management bio summary, management recent developments, or a section-by-section fill for every name.** | Live on portal PROD 37aa1247 (2026-10-09), staff-only route (dell1 box status report :471, :519). Outcomes realized: 22 of 30, inferred; no full tally since round 78 (dell1 box status report :477). **Cold first request 20.05 s; warm overlay about 1.3 s from the snapshot** (`ledger/ROUND_ANALYSIS.round101.md`, @067d69e91b, 2026-10-13 13:58Z). Officer list non-empty on 93 of 95 names (`ledger/ROUND_ANALYSIS.round77.md`:15). Round 102 adds per-phase log lines, the steady-state read and the portal continuous-integration (CI) red test; no fix for the cold start is planned until the log lines name the slow phase (round 101 section 3). The PROD promote of the newer page work waits on Andrew (`project.json` "blocking", call dell1-20261011T033643Z-e7f2), although the push rule exempts an internal page (dell1 box status report :528). Live S3 read: `s3://opal-data-harvest/packs/` holds **105** per-name prefixes (2026-10-13). | **PARTLY** (live but slow cold; completeness across the 93 is not measured). **CONTRADICTED** on "pages load fast ... handled already": cold load is about 20 s. | **REPOINT.** Stop cutting cold-start instrumentation rounds. Cut one V1 round with three parts: (a) the PROD promote, (b) a census of the 93 showing every section filled or its reason, (c) a cold-start remedy, or keeping one instance warm, to bring the cold load under a stated limit. Also add priority 2 as a PRD addendum here. **Disagrees** with the dell1 CRO's PARK (:515), which assumes the page is finished pending user feedback; Andrew ranks it first. |
| **AMGT_HARVST** (D5, dell1; runner host at site Z, round 84) | "continue along on its pace". Its bucket is the subject of priority 3. | 18 outcomes (`prd/AMGT_HARVST_PRD.md` :170-427): collection with provenance from Seeking Alpha, Bloomberg.com, WSJ, Barron's and FT; chatter series; FinBERT tone (FWD-16); a 4-publisher continuous run (FWD-18). **No outcome covers access by asset managers or the gateway.** | 8 of 18 realized (dell1 :544); site Z reads 8 of 17 (sitez :446). The difference is FWD-18, added 2026-10-08, so dell1 has the current denominator. Continuous collector PINNED-AND-RUNNING at site Z on 1c69fa35a3 (dell1 :581). The bucket exists. Live listing: 24 top-level prefixes (amgt, packs, management, filings, seeking-alpha, wsj, barrons, ft, ...). FT is held on Andrew's word. | **COVERED** for collection at his stated pace; **NOT COVERED** for his access ask (outside its charter). | **KEEP at current pace, no added seats.** Scope it to runner upkeep (the windowless runner, so a console click cannot silently stall it) and the WSJ/Barron's sessions. Sits between dell1's KEEP (:575) and site Z's PARK (:469). |
| **AMGT_CORPUS** (D5, dell1, closed) | Feeds the 93 pages ("our embedded sources"). | 22 outcomes. FWD-19: **all 93 research-folder names dispositioned**: prose served, resolved without prose, or unresolved with a reason. 11 can never carry prose by construction (`prd/AMGT_CORPUS_PRD.md` :547-560). | Closed 22 of 22 on 2026-10-12, @6837ec55d7 (dell1 :715, :736). A census of 95 live payloads on **DEV** found 0 values under a wrong header (dell1 :737). Its Model-tab changes reach PROD only with promote e7f2 (dell1 :722). The site Z task `amgt-induction-daily` (lib.research.corpus) returned **rc 4 today** and has no owner (sitez :47, :689-690). | **COVERED** (corpus side of the 93), but not yet on PROD. | **CLOSE** (agrees with dell1 :732). Hand the PROD promote to RESAPP. Give the failing `amgt-induction-daily` task an owner (RESAPP), since it inducts new names. |
| **DSGN_AMGTV1** (D13, dell1, closed) | "the design ... can kind of continue along on its pace." Clean interface is part of priority 1. | Page presentation, including re-homed RESAPP FWD-21..29: labelled tiles, designed empty states, the render check. | Closed 26 of 26 at round 68, 2026-10-09; promoted to PROD (dell1 :764-787). Last commit naming it was 2026-10-11 (git log). | **COVERED** (closed). Whether all 93 pages look clean on PROD today is unmeasured: no walk was done in this read. | **CLOSE** (agrees with dell1 :783). Interface defects found by the V1 census go to RESAPP. |
| **MDPF_DEMQUE** (D8, dell1, round 9) | Andrew suspects it gates the page backfill. | Price, rank and draw history backfills within the Bloomberg and Yahoo budgets. | 1 of 9 realized (dell1 :276). RESAPP's **only** DEMQUE dependency is the scanner-currency slice (`AMGT_RESAPP-S14-CRNCY-SCANNER-US-SLICE1`, order bi-5), queued at site Z with no quote yet (`AMGT_RESAPP/project.json` "blocking"; dell1 :483, :489). The site Z drawer lane `0.7.0_AE_CloudOps~ZQ` has no process (sitez :32, :682). | **CONTRADICTED** (his hypothesis): DEMQUE does not gate the 93 pages, only one scanner currency field. | **KEEP** (agrees with both box reports). Ask for one act: quote and draw the RESAPP slice, or drop it from V1. |
| **NFRA_MCPINDEX** (D9, site Z, parked at round close since 2026-10-11) | Priority 3: an MCP index on the harvest bucket. | One catalog in which "every Opal data property is answerable in Claude" (sitez :112). The PRD has **0** mentions of harvest and 3 of "research", all about its own research passes (`prd/NFRA_MCPINDEX_PRD.md` :80, :443, :444). | 2 of 19 realized (sitez :117). **Live gateway read, 2026-10-13:** `opal_discover` returns `catalogued: false` for "harvested news articles and chatter" and for "security analysis research pack". The positive control ("Schwab account positions") returns 8 datasets, so the tool works. Catalog v0.4, `app/refs/DATA_CATALOG.yaml`. | **NOT COVERED.** | **REPOINT: un-park** and add the harvest and research properties to the catalog. If the served packs are JSON, the existing `gateway_query_catalog` read may need only catalog rows, not a new tool (build ladder step 2). **Disagrees** with the site Z CRO's PARK (:140). |
| **NFRA_OPLGTW** (D9, site Z, round 36 issued today) | Priority 3: "open gateway mechanics". | A verified Opal employee reaches Schwab and Black Diamond data from a work Claude account, with per-user entitlements (sitez :64-65). The PRD has **0** mentions of harvest or research. | 0 of 18 realized (sitez :69). Round 36 issued 2026-10-13 16:01Z (@919f6822eb) on the Black Diamond fee deny and the dead-letter-queue sweep. Close is held until Andrew sees the full gateway breakdown (sitez :79-80). | **NOT COVERED** for research data. It is the delivery path: sign-in, principals and grants. | **KEEP** its charter (agrees with sitez :92). Add one act: give asset-manager principals a research grant once MCPINDEX has the catalog rows. |

**HARVST placement (the aggregate lists it on both dell1 and site Z):** the project of record is **dell1**. `org/missions/D5/AMGT/AMGT_HARVST/project.json`
reads `"fabric": "dell1"`, `"placement": "DELL1"`, `"coo_lane": "2.0.0_SA_COO~W1"`. Site Z hosts the runner and the lane that
applies changes to it (`0.7.0_AE_CloudOps~ZW`), which is why the site Z report also has a block (sitez :15, :473). That block is
out of date in three places:
- it names `2.0.0_SA_COO~H`, which issued the stale bo-1/bp-1 orders, as a seat;
- it uses the 17-outcome denominator;
- it lists the WSJ/Barron's sign-in as an act for Andrew, while dell1 records that ask as WITHDRAWN at about 12:2xZ today (dell1 :583-584).

## 3. Gaps: wanted by Andrew, owned by no project

1. **AI fill for thin text sections.** Nothing owns a management bio summary, management recent developments, or a "fill any thin
   block from our sources, else web search" pass across all names. What exists:
   - model calls (Anthropic, not OpenAI) for the filings thesis (`lib/research/filings/analyze.py`), the posture judge
     (`lib/research/posture/judge.py`) and the CEO search (`lib/research/management/ceo_search.py`). No OpenAI call appears in
     those three files or in `management/bloomberg_fallback.py`.
   - the machine-prose marking (RESAPP FWD-9).
   - the harvest news, which is a natural "recent developments" source.

   The site Z batch tasks `OpalResearch-ExecManagement` and `OpalResearch-FilingsAnalyzer` are **disabled** (sitez :49-50).
2. **Harvest bucket access for asset managers through the gateway.** The catalog has no row (live read above), the catalog project
   is parked, and the gateway project's charter is Schwab and Black Diamond.
3. **A completeness census of the 93 on PROD:** for each name, each section filled or its reason. CORPUS FWD-19 dispositioned the
   corpus layers only. The last correctness census was on DEV (95 payloads). The population is not pinned: 93 research folders,
   95 covered names (round 77) and 105 pack prefixes (live).
4. **The PROD promote (call e7f2).** It is recorded as Andrew's act, but the push rule (CLAUDE.md, Agent Autonomy) needs his word
   only for a client-facing page. Both the RESAPP and CORPUS box status blocks flag this as probably moot, and nobody is acting on it.
5. **Cold-start remedy.** RESAPP owns it, but only instrumentation is planned. The fix waits on per-phase logs (round 101 section 3).
6. **Unowned failing producer:** `amgt-induction-daily` at site Z, rc 4 today (sitez :689-690).

## 4. Fast defined outcomes (functional V1)

1. **V1-PAGE: an analyst opens any of the 93 names on PROD Security Analysis, it loads in under a limit Andrew sets, and every
   section shows content or a stated reason.**
   - Missing: the PROD promote; the per-name section census; the cold-start remedy (about 20 s now).
   - Owner today: dell1, `2.0.0_SA_COO~R1` with `0.7.0_AE_CloudOps~RA1` and `1.0.0_SA_CTO~DELL1`. They are working cold-start log
     lines, not these three items.
2. **V1-FILL: for every one of the 93, the Exec Management tab carries a bio summary and a recent-developments block. Each is built
   from our sources where present, otherwise from a web-search-backed model call, cited and marked as machine-written.**
   - Missing: the outcome, the producer, and the batch run. The roster (FWD-17), the model-call path and the marking already exist.
   - Owner today: **none.** The natural home is a PRD addendum on AMGT_RESAPP (dell1).
3. **V1-ACCESS: an asset manager, in a work Claude account, asks about a covered name and gets that name's pack and chatter from
   opal-data-harvest through the gateway, scoped to research data only.**
   - Missing: catalog rows (NFRA_MCPINDEX, parked); asset-manager principals and a research grant (NFRA_OPLGTW); the list of which
     prefixes may be served (dell1 HARVST/RESAPP).
   - Owner today: **none.** Both gateway projects are placed at site Z.

## 5. Resourcing vs Andrew's ranking

| Andrew's rank | Item | Seats on it today (source) | Effort, 7 days (commit-subject counts, from the box status reports) |
|---|---|---|---|
| 1 | Page V1 | dell1: `2.0.0_SA_COO~R1`, `0.7.0_AE_CloudOps~RA1` (dell1 :481), working cold-start log lines and the CI test (round 101 section 3) | RESAPP 1018 (dell1 :506; inflated by integrations) |
| 2 | AI fill | **0** | 0 |
| 3 | Harvest access | **0** for harvest. Site Z MCPINDEX: `0.7.0_AE_CloudOps~MI` on a Black Diamond document-retirement read due 10-19/20; its issuer `2.0.0_SA_COO~MI` has no process (sitez :32, :119). Site Z OPLGTW: 4 seats on Schwab/Black Diamond entitlements (sitez :73). | MCPINDEX 178, OPLGTW 614 (not on harvest) |
| 4 (own pace) | Harvest collection | dell1 `2.0.0_SA_COO~W1`, `0.7.0_AE_CloudOps~HV1`; site Z `0.7.0_AE_CloudOps~ZW` (dell1 :548; sitez :450). **3 seats.** | HARVST 536 (dell1) / 567 (site Z) |
| 4 (own pace) | Design | 0 (closed) | DSGN 315 (to 10-09) |
| Dependency | DEMQUE | dell1 `2.0.0_SA_COO~Q1`; site Z drawer lane ~ZQ with no process | DEMQUE 315 |

The effort is inverted against his ranking. The most seats are on harvest collection (his "own pace" item). Priority 1 has two seats
working on instrumentation. Priorities 2 and 3 have none. The pare-down record (`today_report/ANDREW_DIRECT_20261013_134xZ_..._SPMOVE.md`
:39-44) touches AMGT only to confirm CORPUS and DSGN closed. It reassigns no AMGT seat.

## 6. Questions only Andrew can answer

1. **Must the fill use OpenAI, or is the provider open?** Recommendation: use the existing Anthropic path. The key, the code and the
   machine-prose marking already exist in `lib/research/`, and the Anthropic API has a server-side web search tool. Choose OpenAI
   only if you want it specifically.
2. **Is the Security Analysis page Opal-internal, so that the PROD promote (call dell1-20261011T033643Z-e7f2) needs no word from
   you?** Recommendation: yes. Let dell1 promote today, after confirming that the bundle changes no client-facing page.
3. **What does "load fast" mean as a number?** Recommendation: under 3 s for the first request of the day. The warm path is already
   about 1.3 s.
4. **What may asset managers read from opal-data-harvest?** Recommendation: in V1, serve only derived layers (packs, chatter,
   scores, management, filings outputs) and article links, not raw article text from WSJ, Barron's, FT or Seeking Alpha, until the
   publisher terms are read.
5. **Which box builds the harvest access?** Recommendation: site Z, where the gateway and catalog seats and the release queue are.
   dell1 supplies the list of servable prefixes. The work is cut as a short round on the parked MCPINDEX, not as a new project.
6. **Which population is V1: the 93 research folders, the 95 covered names, or the 105 pack prefixes?** Recommendation: the 93
   (CORPUS FWD-19's population), with the remainder reported separately.

## 7. Method

- **Read in full:** the transcript; the AMGT and RESAPP blocks of the dell1 box status report (:456-588, :700-787); the site Z
  NFRA_OPLGTW, NFRA_MCPINDEX and AMGT_HARVST blocks and the closing section (:54-170, :431-473, :674-694); `AMGT_RESAPP/project.json`;
  `AMGT_RESAPP/ledger/ROUND_ANALYSIS.round101.md`; RESAPP PRD outcome headlines :491-1092 with FWD-16..20 and FWD-31 read in full;
  CORPUS PRD FWD-19.
- **Read in part:** the aggregate `today_report/AGGREGATE_4_of_4_20261013.txt` (9 AMGT/dependency rows of 66 lines); the pare-down
  record :36-46; `project.json` placement fields for all 7 projects; HARVST PRD outcome headlines (18).
- **Projects found:** `org/missions/D*/AMGT/*/project.json` matched 3 of 3 (RESAPP, HARVST, CORPUS). DSGN_AMGTV1 (D13),
  MDPF_DEMQUE (D8), NFRA_MCPINDEX and NFRA_OPLGTW (D9) were found by name. The laptop and dell2 box status reports contain 0 "AMGT"
  mentions.
- **Live reads, all read-only:**
  - `opal_discover` x3: 2 subjects, 1 positive control.
  - `s3 ls s3://opal-data-harvest/`: 24 prefixes.
  - `s3 ls s3://opal-data-harvest/packs/`: 105 prefixes, 0 objects.
- **Git:** `git log -3 -F --grep=<CODE>` per project. The latest RESAPP commit is 2026-10-13 16:06Z (@0389729ee5).
- **Not read, so unknown:**
  - RESAPP round 78-100 outcome boards (the 22 of 30 tally is the dell1 report's inference);
  - HARVST, MCPINDEX and OPLGTW round analyses (the box status reports were used instead);
  - the DSGN PRD; `lib/research/filings/translate.py`;
  - the PROD page itself (no browser walk, so "clean interface" on all 93 is unmeasured);
  - PROD response times (the 20 s comes from the round 101 log reading);
  - whether asset managers have gateway principals or work Claude accounts today;
  - DEMQUE's quote status for the RESAPP slice beyond the "no quote yet" line.
