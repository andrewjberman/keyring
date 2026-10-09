# Every project being worked on, by box -- state, last 12 hours, dependencies, and what is actually material

**For:** Andrew. **By:** 1.0.0_SA_CTO (laptop), 2026-10-09 ~19:4xZ. **Window:** 2026-10-09 ~07:25Z-19:25Z (UTC).

**Sources:**
- 3,000 distinct commits across `CLOUD` and the four box branches in the window.
- Each project's register row, latest round analysis and issue rows.
- The cluster open-calls list.
- Three per-box readers, whose entries are below.

Client data in git is left out, on your word. It appears only where it consumed a project's time.

**Words used:**
- **Round:** one build cycle. The CTO lists the work, a COO issues task orders, workers build, the CVO grades, and the CTO analyses.
- **FWD-n:** one of a project's promised outcomes.
- **MATERIAL:** it blocks an outcome or risks served data or money. **NEGLIGIBLE:** friction only.

---

## Verdict: is what we are seeing material?

**Mostly no. The fabric is producing, and most of the friction you have been hearing about costs minutes, not outcomes.**

- **Output in 12 hours:**
  - 3,000 commits; 34 projects with real work.
  - **5 closed with every outcome met:** DSGN_AMGTV1 (26 of 26), NFRA_GATSCP (8 of 8), LGIC_BLANKFIX (9 of 9), LGIC_ENFORCE (7 of 7), NFRA_REPORT.
  - Live releases: gateway r29, Control Plane page, COMM_ASSIST mail, IRPT gold R44, the transcripts pipeline, trade Lambdas, Security Analysis on portal PROD, rival-fund Lambdas, COT classification.
  - First end-to-end journey of a dell2 product: TCKT_VNEXT.
- **Git:** about 1 sync in 4 held in the morning. Since 15:20Z it is **4 holds in 134 runs (3%)**. Each hold cleared within minutes to an hour. **Not material now.**
- **Box switching:** 9 projects changed box in the last ~24 hours. Each was seated and moving within about an hour of its move. The costs were one stale ruling of mine and register fields that lag the move. **Not material.**
- **Cross-box dependencies:** about **10 are live**. Most cost minutes: password windows on the laptop (5 today, each under 25 minutes), sign-off halves, a permission grant. Only **two are structural and material to throughput**, both on site Z hardware:
  1. **The single Opal Gateway host.** Three site Z projects and dell2's releases deploy through it one at a time. Pins go stale and sign-offs are redone: NFRA_MCPINDEX re-cut its deploy 3 times, and ADVI_BILLING's Excel tool has waited since 10:13Z.
  2. **The publication-harvest runner on site Z.** It serves AMGT_HARVST, a dell1 project, so every fix is a cross-box round trip. The collector also currently collects almost nothing (see below).
  - The Bloomberg Terminal on site Z is a third, but it is correctly served through the DEMQUE queue and is not friction.
- **The issues that ARE material** are ordinary product defects inside a box, not box plumbing:

| # | Issue | Box / project | Why material |
|---|---|---|---|
| 1 | irpt-status shipped from mismatched file versions: two failed releases, about 2 hours of outage | dell2 / IRPT_ANLREQ, IRPT_YCDGEN | blocks two outcomes; one root cause (fix: a single-tree build, IB-pr-416) |
| 2 | 49 Financial bundle not yet published (2 of 3 firms done) | dell2 / IRPT_BCKEND | one firm's served output is missing (fix built and signed: IB-pr-417) |
| 3 | Performance adapter failing on live calls (row D2-S60) | dell2 / IRPT_BCKEND | a live route is failing |
| 4 | The uploader writes ETF-history cells as empty in the served price store (row D1-S6) | dell1 / MDPF_DEMQUE | served data is wrong for ETF history |
| 5 | The publication collector collects almost nothing (Bloomberg 96 cycles, 0 fetched; WSJ/Barron's 0 attempts) | dell1 / AMGT_HARVST (runner on site Z) | its main outcome cannot be met |
| 6 | 197 Black Diamond tie-out segments classed as defects | dell2 / IRPT_DASHBD | gates FWD-8 and, behind it, ADVI_COTBKF's mint |
| 7 | 5 of 34 Teams meetings missing from the transcripts | dell2 / NFRA_TRNSPT | gates FWD-3 |
| 8 | A live silver job broke at 14:51Z on a missing module | dell1 / MDPF_STRATID | contained in 7.5 minutes; import checks are now required before deploys |
| 9 | Every cross-box send fails on Windows (row S9109), so relays went by hand all day | laptop / NFRA_CTLPLN | automation, not outcomes |
| 10 | The data-refresh tool admits any Opal-internal caller (row D2-S17) | site Z / NFRA_OPLGTW | an internal-only authorization gap |

**What I would do about it:**
- Let the boxes fix items 1-8 in their own rounds; they all have owners.
- Remove the structural site Z dependencies, the gateway release lane and the harvest runner, by giving the Dells their own rights or hosts. That is in NFRA_CTLPLN round 7, per your no-cross-box rule.
- Item 9 is the one plumbing fix worth doing now.

---

## The list -- every project worked on, by box

| # | Project | Box now | Moved recently? | Stage / status | Cross-box dependency | Material issue |
|---|---|---|---|---|---|---|
| 1 | AMGT_RESAPP | dell1 | from site Z, 10-08 | executing, round 87 | laptop rights for one republish (grant queued) | no |
| 2 | DSGN_AMGTV1 | dell1 | from site Z, 10-08 | **CLOSED** 26 of 26 | none | no |
| 3 | ETFS_RIVALS | dell1 | from site Z, 10-09 ~01:5xZ | executing, round 28 | a code merge held at site Z until 10-10 06:00Z | no (delay only) |
| 4 | NFRA_GATSCP | dell1 | born here | **CLOSED** 8 of 8 | none | no |
| 5 | MDPF_SECHIST | dell1 | from laptop, 10-09 04:56Z | executing, round 3 | site Z producer half; Bloomberg via the queue | no |
| 6 | AMGT_HARVST | dell1 | from site Z, 10-08 | executing, round 79 | **the runner lives on site Z** | **yes** (#5) |
| 7 | MDPF_DEMQUE | dell1 | -- | executing, round 7 | Bloomberg draws on site Z (by design) | **yes** (#4) |
| 8 | LGIC_BLANKFIX | dell1 | from laptop, 10-09 04:04Z | **CLOSED** 9 of 9 | none | no |
| 9 | MDPF_STRATID | dell1 | -- | executing, round 2 deployed | laptop sign-off (now moved to dell1's CTO) | contained (#8) |
| 10 | AMGT_CORPUS | dell1 | from site Z, 10-09 ~01:5xZ | executing, round 42 | induction job on site Z | no |
| 11 | MDPF_SECCLASS | dell1 | from laptop, 10-09 04:56Z | round 18 closed; round 19 waits on scheduled runs | none | no |
| 12 | LGIC_ENFORCE | dell1 | from laptop, 10-09 15:00Z | **CLOSED** 7 of 7 | none | no |
| 13 | MDPF_HEALGAP | dell1 | -- | round 2 done, round 3 drafted | none | no |
| 14 | LGIC_CANON | dell1 | from laptop, 10-09 18:33Z | executing, round 5 | none | no |
| 15 | MDPF_CANON | dell1 | from laptop, 10-09 18:21Z | executing, round 1 | none | no |
| 16 | ADVI_COTBKF | dell2 | -- | executing, rounds 45-53 | none | gated by #6 |
| 17 | IRPT_BCKEND | dell2 | -- | executing, rounds 103-117 | laptop password windows | **yes** (#2, #3) |
| 18 | IRPT_DASHBD | dell2 | -- | executing, rounds 41-56 | none (rulings only) | **yes** (#6) |
| 19 | IRPT_ANLREQ | dell2 | -- | executing, round 2 | laptop password windows and reads | **yes** (#1) |
| 20 | NFRA_TRNSPT | dell2 | from laptop, 10-07/10-08 | executing, round 22 | site Z gateway (allowlist, deck copy); laptop key changes | **yes** (#7) |
| 21 | TCKT_VNEXT | dell2 | -- | executing, round 1; journey ran end to end | none | no |
| 22 | ADVI_BILLING | dell2 | -- | round 3 closed | **site Z gateway release of its Excel tool** | delay |
| 23 | IRPT_YCDGEN | dell2 | -- | round 7 + releases | laptop password windows | **yes** (#1) |
| 24 | NFRA_OPSWKF | dell2 | -- | executing | one laptop permission grant (done) | no |
| 25 | IRPT_CUSTDY | dell2 | -- | **CLOSED** | -- | -- |
| 26 | NFRA_OPLGTW | site Z | -- | executing, round 33 | **provider:** dell2 projects wait on its host | **yes** (#10; host queue) |
| 27 | COMM_ASSIST | site Z | from laptop, 10-09 ~06:16Z | executing, round 12; mail deploy APPLIED 19:03Z | none now | no |
| 28 | NFRA_IAMROLES202609 | site Z | -- | executing, round 6 | none (fleet-wide blast radius) | one outcome failed (v-2) |
| 29 | NFRA_OPALAI | site Z | -- | executing; test arm (b) passed | none | no |
| 30 | NFRA_MCPINDEX | site Z | -- | executing, round 8; deploy running | shares the gateway host | throughput |
| 31 | NFRA_MCPORTAL | site Z | -- | executing; Control Plane live | shares the gateway host | no |
| 32 | NFRA_MCPMSP | site Z | -- | **HELD** on your act G-MSPID | none | no |
| 33 | NFRA_REPORT | site Z | -- | **CLOSED** 08:06Z | -- | -- |
| 34 | NFRA_OPSEC202609 | site Z | -- | **CLOSED** (register fixed) | -- | -- |
| 35 | NFRA_CTLPLN | laptop | -- | executing, round 6 | **is** the cross-box layer (password windows, grants) | **yes** (#9) |

**Counts:**
- 35 rows: dell1 15, dell2 10, site Z 9, laptop 1.
- 7 closed, 1 held, 27 executing.
- The laptop now runs only NFRA_CTLPLN; everything else moved to the boxes that run it.

**Your list, about 10 minutes in total:**
- `-21c5`: one look at the Control Plane page.
- `-f0d2`: one sign-in as Opal Bloomberg.
- `-9f24`: Barron's sign-in.
- G-MSPID: when you are ready.
- `-3082`: the Research meeting invite or a Microsoft 365 policy.
- `-3cb1`: Alyssa's request.
- `-fbb1`: close a test ticket.
- `-86a2`: rotate the API key.
- `-203a`: the Muni sleeve question.
- Four optional cleanup deletes.

---

## Full entries

### dell1 (15 projects)

**1. AMGT_RESAPP -- Security Analysis research pack, generated automatically per covered company**
- **Box / stage / COO:** dell1 (from site Z, 10-08) | executing, round 87 | COO `~R1`
- **Last 12 hours:** the busiest dell1 project (181 commits).
  - Rounds 85 and 86 closed (64c5f8d6fe). The name list was republished with 102 research folders (004fabb655).
  - The NU company description graded not met (2eba7c172b). Round 87 was issued with four orders (433e2b510d), three complete by 19:18Z; the redeploy pair is signed.
- **What remains:** order ll-3, the redeploy at dossier version /9, then the round-87 grade.
- **Cross-box:** the name-list republish ran on a laptop deploy seat (`~AMG`), because dell1 lacks the rights. Site Z's CTO signed four producer items.
- **Went well:** fast rounds; republish proven end to end.
- **Went poorly:** NU's description failed its grade; an API key was printed into a local transcript.
- **Issues:** NU description, laptop republish rights, key exposure (local only) -- all NEGLIGIBLE.

**2. DSGN_AMGTV1 -- Security Analysis portal page redesign (staff-only)**
- **Box / stage:** dell1 | **CLOSED** at round 68, 26 of 26 (78294bf9ee). Portal PROD moved to v2.1.211.
- **Last 12 hours:** rounds 65-68 ran. FWD-8 (peer tickers) and FWD-27 (one format per measure) were realized.
- **Went poorly:** round 68 was reopened twice over one tile, and a schema refused the lane name `~D1` until fixed.
- **Issues:** none material.

**3. ETFS_RIVALS -- rival active-ETF research (six rivals, holdings, a daily page)**
- **Box / stage / COO:** dell1 (from site Z, 10-09 ~01:5xZ) | executing, round 28 | COO `~V1`
- **Last 12 hours:**
  - Five rival-fund Lambdas deployed (b37de31c54), and the void path merged.
  - The dramatic-move lookup went live at 15:22Z.
  - The code-merge order tc-1 is held at site Z's `~ZV` (stopped at a gate, then a merge-base race); the order was amended twice.
- **What remains:** the tc-1 merge (site Z's manager runs it by 10-10 06:00Z if nothing sooner), then the read of both deploys.
- **Cross-box:** tc-1 must be merged by a site Z seat under site Z's commit lock.
- **Issues:** tc-1 delay -- NEGLIGIBLE to moderate (about 11 hours of delay; nothing is served wrong).

**4. NFRA_GATSCP -- Git gates scoped to the act**
- **Box / stage:** dell1 | **CLOSED** at round 4, 8 of 8 (45f5fc4fd9).
- **Last 12 hours:** a round-3 finding showed FWD-8's premise false; round 4 fixed it, graded MET on a replay of 26 recorded refusals.
- **Went poorly:** two workers lost time to the laptop's broken proof schema.
- **Issues:** none material.

**5. MDPF_SECHIST -- Opal's securities history store**
- **Box / stage / COO:** dell1 (from laptop, 10-09 04:56Z) | executing, round 3 | COO `~H1`
- **Last 12 hours:**
  - A 16-cell Bloomberg read was booked through DEMQUE. Site Z signed its producer half.
  - The gold dry run matched the served page 1,520 of 1,520 cells (9842e9a0d5). Both gold halves are signed.
  - The deploy seat `~SC1` declined, then withdrew the decline.
- **What remains:** the gold deploy, then round 3 close.
- **Cross-box:** site Z producer half; Bloomberg through the queue.
- **Issues:** cross-box sign-off friction (about 1 hour) -- NEGLIGIBLE.

**6. AMGT_HARVST -- publication harvest (every mention of a covered company, with its source)**
- **Box / stage / COO:** dell1 (from site Z, 10-08) | executing, round 79 | COO `~W1`
- **Last 12 hours:** the collector fix merged at 17:44Z under a site Z pair, and the round-79 re-pin was released to site Z. Four cross-box orders went to site Z; one failed and was re-sent.
- **What remains:** the first live collection cycle after the fix, then the FWD-18 read.
- **Cross-box:** heavy. The runner lives on site Z, so every deploy, read and sign-off half goes through site Z. WSJ and Barron's need your Barron's sign-in.
- **Went poorly:** the collector fetches almost nothing (Bloomberg 96 cycles, 0 fetched; WSJ/Barron's 0 attempts; nothing reached silver since about 12:57Z).
- **Issues:**
  - The collector -- **MATERIAL** (FWD-18 cannot be met).
  - The site Z runner -- **MATERIAL as friction** (every fix is a cross-box round trip).

**7. MDPF_DEMQUE -- Bloomberg/Yahoo backfill demand queue (priced, budgeted draws)**
- **Box / stage / COO:** dell1 | executing, round 7 | COO `~Q1`
- **Last 12 hours:**
  - Round 6 closed and round 7 was issued; t22 and t23 merged. Three tier-1 reads were booked for SECHIST.
  - Saturday's backfill at site Z was refused, then amended and signed.
  - **Row D1-S6:** the live uploader writes ETF history cells as empty.
- **What remains:** the 02:30Z draw, Saturday's backfill, and the D1-S6 fix.
- **Cross-box:** Bloomberg draws on site Z, by design (a served interface).
- **Issues:**
  - D1-S6 -- **MATERIAL** (wrong served data).
  - Site Z draws -- NEGLIGIBLE.

**8. LGIC_BLANKFIX -- complete fix for every broken resource name**
- **Box / stage:** dell1 (from laptop, 10-09 04:04Z) | **CLOSED**, 9 of 9 (c23979cd0c).
- **Last 12 hours:** 180 schedules checked: 148 agree, 32 partial with a reason, 0 mismatched. The CVO confirmed it independently.
- **Went poorly:** early-morning collisions while laptop and dell1 seats both worked round 9 (cleared by 09:00Z).
- **Issues:** none material.

**9. MDPF_STRATID -- strategy identification (every Opal strategy and SMA sleeve found at intake)**
- **Box / stage / COO:** dell1 | executing, round 2 deployed | COO `~S1`
- **Last 12 hours:**
  - Round 1 was graded final.
  - **At 14:51Z a live silver job broke on a missing module and was rolled back in 7.5 minutes.**
  - The round-2 pair was signed; deploys D1 and D2 landed (6259c6efbf). The planted-sleeve test graded MET.
- **What remains:** the organic check after the 10-10 13:30Z run.
- **Cross-box:** my sign-off half, now ruled to dell1's CTO.
- **Issues:** the 14:51Z break -- **MATERIAL but contained** (import-closure reads are now required before deploys).

**10. AMGT_CORPUS -- research corpus as a measured base**
- **Box / stage / COO:** dell1 (from site Z, 10-09 ~01:5xZ) | executing, round 42 | COO `~C1`
- **Last 12 hours:** site Z re-pinned the induction job, and the 17:00Z run stamped 96 of 96. Round 41 graded MET. Dossier version /8 was found never served; the /9 rewrite has both halves signed.
- **Cross-box:** the induction job runs on site Z.
- **Issues:** each re-pin is a cross-box act -- NEGLIGIBLE to moderate.

**11. MDPF_SECCLASS -- one canonical classification table per security**
- **Box / stage / COO:** dell1 (from laptop, 10-09 04:56Z) | round 18 closed; round 19 waits on the 23:00Z, 04:00Z and 11:30Z runs | COO `~M1`
- **Last 12 hours:** both gold test suites are green on the CVO's own runs. The COT port shipped live, moving $17.77M of positions out of "unclassified". It signed a half for dell2's 49F release.
- **Issues:** none material.

**12. LGIC_ENFORCE -- the naming rules' executable layer**
- **Box / stage:** dell1 (from laptop, 15:00Z) | **CLOSED** 7 of 7 (65cfdb8978), re-closed after a one-cell follow-up.
- **Last 12 hours:** the commit gate now grades names built at a call site and pattern names.
- **Went poorly:** register lag between boxes (my 18:2xZ lane ruling on it was stale).
- **Issues:** none material.

**13. MDPF_HEALGAP -- Cottonwood rebalancer ingest heals the same day a vendor login lapses**
- **Box / stage / COO:** dell1 (register `fabric` stale) | round 2 done, round 3 drafted | COO `~G1`
- **Last 12 hours:** a normal-day exercise passed (06:00Z complete; 11:32Z re-try correctly skipped; reader OK at 13:50Z).
- **What remains:** the 20:00Z and 10-10 07:15Z checks.
- **Issues:** none.

**14. LGIC_CANON -- the Platform Logic canon**
- **Box / stage / COO:** dell1 (from laptop, 18:33Z; seated 18:42Z) | executing, round 5 | COO `~B1`
- **Last 12 hours:** it had been idle for weeks on the laptop. It moved and was seated in 9 minutes, then round 5 was issued; two of three orders were complete by about 19:10Z (183 names checked, 0 raised).
- **Issues:** none.

**15. MDPF_CANON -- MDPF gold published as per-firm parquet**
- **Box / stage / COO:** dell1 (from laptop, 18:21Z; seated 18:30Z) | executing, round 1 | COO `~D1`
- **Last 12 hours:** PRD v2.9 signed. Round 1 issued at 19:03Z; two of three cells built by 19:13Z (114 tests passed).
- **Issues:** three global-fold gold tests already fail on dell1 before any change (row D1-S1) -- an unowned red, NEGLIGIBLE for this project.

**dell1 roll-up:**
- 15 projects. **4 closed today, every outcome met.**
- 2 moved in from the laptop and were moving within the hour.
- 7 live cross-box ties, 5 of them to site Z hosts.
- Material: the harvest collector, the empty ETF-history cells, and the contained 14:51Z break.

### dell2 (10 rows)

The register's box field still reads `laptop` for seven of these, but their placement and all work are on dell2. This is cosmetic.

**16. ADVI_COTBKF -- 10-year Cottonwood history backfilled from Commonwealth**
- **Box / stage / COO:** dell2 | executing, rounds 45-53 | COO `~C2` (217 commits, the most of any project)
- **Last 12 hours:**
  - Found the price store used dividend-adjusted prices; re-minted the outcome tables on as-traded prices.
  - Removed 49 Financial bond prices from Cottonwood's price files.
  - Redeployed COT gold and read it back equal to the repo.
  - About 3 hours went to the client-data cleanup.
- **What remains:** the Cottonwood mint, waiting on IRPT_DASHBD's producer cell (an in-box dependency), then the 10-year grade.
- **Cross-box:** none.
- **Issues:** the mint hold -- **MATERIAL** (gates the main outcome; an in-box dependency).

**17. IRPT_BCKEND -- Investor Reporting back end**
- **Box / stage / COOs:** dell2 | executing, rounds 103-117 | COOs `~P2` and `~Y2` (212 commits)
- **Last 12 hours:**
  - The narrative service went live, completing a 27-route release; the holdings and commentary readers went live.
  - The 49 Financial bundle was rebuilt with a memory fix (IB-pr-417), both halves signed.
  - The performance adapter was found failing on live calls (D2-S60).
- **What remains:** land IB-pr-417, fix the adapter, then the irpt-status single-tree build (IB-pr-416).
- **Cross-box:** laptop password windows and reads; one dell1 sign-off half.
- **Issues:**
  - 49F bundle -- **MATERIAL**.
  - Adapter -- **MATERIAL**.
  - Laptop windows -- NEGLIGIBLE (8-24 minutes each, all closed inside their limits).

**18. IRPT_DASHBD -- client reporting dashboard**
- **Box / stage / COO:** dell2 | executing, rounds 41-56 | COO `~D2`
- **Last 12 hours:**
  - The R44 gold Lambda went live.
  - Lambda memory raised from 2,048 to 3,008 MB under a signed pair (the heaviest day hit 96.8%).
  - The 990 out-of-tolerance segments were re-graded under a pre-registered rule.
- **What remains:** FWD-8 (the Black Diamond tie-out at 0.35 percentage points): 197 defect segments, plus a sensitivity check owed. The producer cell gates ADVI_COTBKF.
- **Issues:**
  - 197 segments -- **MATERIAL**.
  - Memory -- was material, now fixed.

**19. IRPT_ANLREQ -- one Analysis Request end to end (form to report, PDF and Excel)**
- **Box / stage / COOs:** dell2 | executing, round 2 | COOs `~Y2` and `~V2`
- **Last 12 hours:**
  - irpt-status revision 4 shipped mismatched files and every call crashed; rolled back at 16:43Z.
  - Revision 5 went live at about 17:55Z, failed its R3 check and was rolled back.
  - The design moved to a single-tree build.
- **What remains:** that release, then reads 5-6.
- **Cross-box:** laptop reads and password windows.
- **Issues:** the version mismatch -- **MATERIAL** (about 2 hours of outage; it blocks the journey).

**20. NFRA_TRNSPT -- Opal communications database (Teams transcripts, market updates)**
- **Box / stage / COO:** dell2 (from laptop, 10-07/10-08) | round 21 closed, round 22 issued | COO `~T2`
- **Last 12 hours:**
  - The silver-only reader went live.
  - The first scheduled Teams landing ran at 16:00Z; 29 of 34 meetings landed.
- **What remains:** the missing meetings, the market-update deck (needs site Z's copy tool), and your Research-meeting act.
- **Cross-box:** site Z gateway (allowlist, deck copy); laptop key-policy changes and a verify leg.
- **Issues:** 5 missing meetings -- **MATERIAL** (gates FWD-3). The cross-box ties are NEGLIGIBLE per instance; this is dell2's most cross-box project.

**21. TCKT_VNEXT -- Ticket Center typed requests**
- **Box / stage / COO:** dell2 | executing, round 1 | COO `~V2`
- **Last 12 hours:**
  - A one-firm proof refused Cottonwood on 22 of 22 routes; a census of 82 scoped routes found zero cross-firm leaks.
  - **The main journey ran end to end** (66bfdf5c2e).
  - A signing key was read five times (memory only); one run's deploy ledger was opened after the act.
- **What remains:** the CVO grade, one re-read, and your two acts.
- **Issues:** the ledger-after-act -- NEGLIGIBLE.

**22. ADVI_BILLING -- advisory-fee billing**
- **Box / stage / COO:** dell2 | round 3 closed 10:13Z | COO `~B2`
- **Last 12 hours:** every probe exercised; FWD-3 realized on the real render; the Excel-tool release handed to site Z.
- **What remains:** site Z's gateway release of the Excel tool, queued behind two releases.
- **Cross-box:** the site Z gateway owns the release.
- **Issues:** idle since 10:13Z waiting on site Z -- **MATERIAL to its outcome**. This is the clearest cross-box cost on the list.

**23. IRPT_YCDGEN -- YCharts reports in Opal branding**
- **Box / stage / COO:** dell2 | round 7 plus releases | COO `~G2`
- **Last 12 hours:** per-firm research roles live and checked both ways (each firm reaches its own; all 6 cross-firm attempts denied). **Opal produced the 49 Financial report**, but irpt-status refused to serve it.
- **What remains:** the served read, after the irpt-status fix shared with IRPT_ANLREQ.
- **Issues:** same root cause as #19 -- **MATERIAL**.

**24. NFRA_OPSWKF -- trade submission through Opal**
- **Box / stage / COO:** dell2 | executing | COO `~O2`
- **Last 12 hours:** the trade Lambdas deployed live, all 5 steps proven (trade-pipeline-v1.21). Dell2 at first lacked one email-service permission; the laptop granted it the same hour.
- **Issues:** none material.

**25. IRPT_CUSTDY** -- closed. One related order was issued under IRPT_DASHBD.

**dell2 roll-up:**
- About 1,050 commits.
- Two products now produce end to end: TCKT_VNEXT's journey and the 49F YCharts report.
- The material issues are in-box product defects: irpt-status, the 49F bundle, the performance adapter, the tie-out segments, the missing meetings.
- Cross-box ties are real but cheap, except ADVI_BILLING waiting on the site Z gateway.

### site Z (9 rows)

**26. NFRA_OPLGTW -- the Opal Gateway (authorized Schwab questions and downloads in Claude); also the host other boxes ship through**
- **Box / stage / COO:** site Z | executing, round 33 | COO `~O`
- **Last 12 hours:**
  - r29 went live 12:46Z; dell2's transcript allowlist deployed at about 15:40Z.
  - Round 32 finished 14 of 14; round 34 was cut.
  - ADVI_BILLING's Excel-tool release is cut and signed.
- **Cross-box:** **provider.** dell2's NFRA_TRNSPT, ADVI_BILLING and TCKT_VNEXT wait on this one host, which deploys one release at a time.
- **Issues:**
  - The single host -- **MATERIAL (structural)**.
  - D2-S17, the data-refresh tool admits any Opal-internal caller -- **MATERIAL until scoped**.

**27. COMM_ASSIST -- your Teams and Outlook assistant (messages to your phone, drafted in your voice)**
- **Box / stage / COO:** site Z (from laptop, about 06:16Z) | executing, round 12 | COO `~ZZ`
- **Last 12 hours:**
  - Decoupled from the transcripts encryption key.
  - The first real deploy correctly applied nothing (827 unreviewed lines from other projects).
  - The build was pinned and re-signed. **The deploy APPLIED at 19:03Z: the assistant now polls your mail.**
- **What remains:** the message-count read at about 22:00Z, then round close.
- **Issues:** package drift -- NEGLIGIBLE (caught; cost time only).

**28. NFRA_IAMROLES202609 -- least privilege across every AWS permission role**
- **Box / stage / COO:** site Z | executing, round 6 | COO `~ZI`
- **Last 12 hours:** a permission removal matched its prediction; all 16 roles in FWD-4 now have an owner. An unscoped plan would have deployed three Lambdas; it was caught and every apply is now scoped.
- **Issues:** one outcome failed (four roles have no custody home) -- **MATERIAL to that outcome**.

**29. NFRA_OPALAI -- the Opal Analyst in Teams**
- **Box / stage / COO:** site Z | executing | COO `~AI`
- **Last 12 hours:** Teams fixes live on DEV and PROD. **Closing test arm (b) passed at 17:10Z** after three rulings over about 5 hours of waiting for one fresh message.
- **What remains:** arm (a), which needs Alyssa's own question; site Z lists it for you.
- **Issues:** NEGLIGIBLE.

**30. NFRA_MCPINDEX -- one catalog for every Opal data property in Claude**
- **Box / stage / COO:** site Z | executing, round 8 | COO `~MI`
- **Last 12 hours:** one deploy was re-cut and re-signed **three times**, because other releases went first on the shared host. It is now running.
- **Issues:** the host queue -- NEGLIGIBLE for correctness, **MATERIAL for throughput**.

**31. NFRA_MCPORTAL -- your operator console at mcp.opalinvest.dev**
- **Box / stage / COO:** site Z | executing | COO `~MP`
- **Last 12 hours:**
  - **The Control Plane page went live at 16:29Z.**
  - A ledger-tool defect was fixed at its source.
  - One load check missed by 1.6 seconds (31.6 seconds against 30).
- **What remains:** a re-run, plus your look at the page and your Opal Bloomberg sign-in (about 3 minutes).
- **Issues:** NEGLIGIBLE.

**32. NFRA_MCPMSP -- the Opal MSP Analyst for partner firms**
- **Box / stage / COO:** site Z | **HELD** after rounds 2-3 closed (09:30Z) | COO `~MS`
- **What remains:** only your act G-MSPID ("Not yet"). Not an issue.

**33. NFRA_REPORT** -- closed at 08:06Z.

**34. NFRA_OPSEC202609** -- closed (register corrected).

**Site Z roll-up:**
- Five releases went live.
- The one material structural problem is the single gateway host, shared with dell2.
- The rest is negligible friction.

### Laptop (1 project)

**35. NFRA_CTLPLN -- the four-box control plane**
- **Box / stage / COO:** laptop, by design | executing, round 6 | COO `~C`
- **Last 12 hours:**
  - Permission amendments 29 and 30 applied; Dell parity 1,533 of 1,533 equal.
  - Five dell2 password windows, every one closed early.
  - The base deploy seat went unresponsive at 09:29Z and lane `~CTL` replaced it.
  - dell1's exercise showed the deliberate internet download is not stopped (FWD-18 unmet, and likely obsolete now that internet access is open).
  - New rows include **S9109: every cross-box send fails on Windows**.
- **What remains:** dell1 orders CT-x-1 and CT-x-2, the CVO grade, the round-6 analysis. Then round 7: three Dell grants to remove cross-box dependencies (gateway release lane, dell2's own password window, the republish grant), and S9109.
- **Issues:**
  - S9109 -- **MATERIAL for automation**.
  - The dell2 windows on the laptop -- the dependency your rule removes; round 7.

**Laptop roll-up:** nearly all laptop activity was service to the Dells. Round 7's grants remove most of it.

---

## Registered "active" but no work in the last 12 hours

ADVI_FIRMBKTS (waiting for a COO slot), ADVI_PERFRP, ADVI_ROSTERCOLS, AUTH_SELFHEAL, D12_PHONE_OTP_ALL_AWS (your word), D1_CATVIEWS,
D3_MODELOVERLAY, DSGN_IRPTV1, ETFS_CANON, GLOBALALARM, LGIC_LGCTFM (queued after LGIC_CANON), MDPF_GLOBAL, NFRA_SPMOVE, NFRA_SYSPARITY,
NFRA_VELOCITY_CORE / _ESTATE (your resume word), OPAL_ADVIPOINTERS, OPAL_KIMIPIPELINE, OPAL_SQSCHAT, OPAL_TAXROSTER,
OPAL_TAXSMA (+ _PT2, _REGISTRY), OPAL_TICKET_VNEXT, PLATFORM_OPS_USERMGMT, WSE_COTMDL, YALP_MACROS.

About a dozen of these are stale or duplicate rows and should be closed so that "active" means work in motion.
