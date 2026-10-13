# Site Z infrastructure (NFRA) alignment -- Andrew's 2026-10-13 voice memo vs the projects

- **For:** Andrew Berman and the laptop CTO (`1.0.0_SA_CTO`), to repoint site Z work.
- **Source memo:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/SITEZ_NFRA_REVIEW_TRANSCRIPT.md`.
- **Read at:** 2026-10-13 ~16:1xZ to ~16:3xZ, on the laptop checkout `box/laptop` @ec75ee1bef. This was a read-only pass. Site Z's
  own worktrees were not read, so site Z work that has not yet reached CLOUD is not seen here.
- **Companion read:** today's site Z box status report, `org/tier1_exec/4.0.0_SA_CRO/deliverables/BOX_STATUS_REPORT_sitez_20261013.md`
  (as of 14:44Z, @97bc7d4a59; byte-identical to `C:\Users\AndrewBerman\Desktop\today_report\BOX_STATUS_REPORT_sitez_20261013.md`),
  and `C:\Users\AndrewBerman\Desktop\today_report\AGGREGATE_4_of_4_20261013.txt` lines 54-67. Below, "the box report" means that file.
  Section 2 says where this report agrees or disagrees with it.

## 1. What Andrew asked for (ranked)

1. **MC Portal (NFRA_MCPORTAL) takes centre stage as ONE master control panel.** In it you can SEE and CONTROL every
   vendor and channel, its indexes and tools, who is entitled to what, and the depth and breadth of polls per vendor.
   - "All that needs to be visible and controlled through MC Portal"
   - "MC Portal needs to take center stage"
   - "this way we have one master control panel"
2. **The Opal Gateway (NFRA_OPLGTW) is operational for the team, managed through MC Portal.** "so that we can make sure that the
   OPL Gateway is operational for the team members that need it. That is the biggest priority for the Site Z box."
3. **MCP Index (NFRA_MCPINDEX) stays in the top three, framed as mostly finished.**
   - "I know that a lot of the MCP index stuff is done."
   - "the focus I would say is entirely on three projects. OPL Gateway, MCP Index, and MC Portal."
4. **The Bloomberg agent works, and its entitlements are shown like any user's** ("over time").
   - "worth doing a review there to make sure that's functional, that people can use it"
   - The Opal Bloomberg account should show "what channels they have access to, what tools and those channels, what backfill
     or scope", just as other staff accounts do.
5. **One gateway, not two panels.**
   - "all of them should go through OPL Gateway"
   - He accepts two logins if needed: "if it has to be through the two separate ones based on the logins ... So be it, but it has
     to be able to be visible and managed there."
6. **Deprioritised, not closed.** "OPL AI does not really matter. The MSP MCP, it is not really matter." "All of these are kind of
   not closed."

## 2. Project table

Population: 52 mission-tree `project.json` files were read. 11 carry `placement: SITEZ`, and 5 of those are not closed:
OPLGTW, MCPINDEX, MCPORTAL, OPALAI (all active) and MCPMSP (hold). COMM_ASSIST now reads `placement: LAPTOP`, moved today.
OPAL_BBGTML has no placement but runs on site Z, so it is included at the coordinator's request.

| project | Andrew's intent | chartered outcomes | delivered / live (evidence) | coverage | recommended move |
|---|---|---|---|---|---|
| NFRA_MCPORTAL | Centre stage. One panel to see AND control channels, tools, indexes, entitlements, and poll and backfill depth per vendor, the Bloomberg account included | PRD v0.7 FWD-1..20 (`prd/NFRA_MCPORTAL_PRD.md:91-209`). Relevant: **FWD-20** (cut first) is ONE read-only page listing every channel, its tools and catalog indexes, and who holds a grant on it now; it "writes nothing" (`:538-540`). **FWD-1** narrows or widens one colleague's data grant. **FWD-10** is the call log plus stopping one person or the whole server. **FWD-9** is the property and tool catalog. **FWD-14..17** are the fabric control plane | **Live:** Control Plane since 10-09; Overlap, Git state and Open Calls since 10-10 (box report). **Grades:** 0 of 20 REALIZED (`ledger/ROUND_ANALYSIS.round4.md` @460bc0af2f: FWD-1, 2 and 14 NOT_REALIZED, the rest DEFERRED). **FWD-20 build:** handler, page and deep links complete; the storage read permission (DynamoDB Scan) still owes the CTO's half of its never-widen sign-off; release and Andrew's read are staged (box report). **Not live at this checkout:** no `/gateway/breakdown` route (`infra/aws/ec2/opal-gateway/app/admin_api.py:49-60` has whoami, grants get/narrow/widen, changes and the fabric routes). **Source:** the `mcportal` repo on GitHub has DEV = PROD = fa1ff9693b, the 2026-09-24 initial commit, and the page commit 6fbd25e is "No commit found" there (gh api) | **PARTLY.** Seeing: covered once FWD-20 ships. Controlling: only the data-grant narrow and widen (FWD-1, not closed). No outcome covers per-person tool, channel or tier edits, poll cadence or backfill depth | **KEEP + REPOINT:** ship FWD-20 this week, then add a FWD-21 "control and depth" addendum (section 5). Leave FWD-3..13 (home page, Operations Report, user management, analytics, cost, infosec) deferred behind it. **Agree** with the box report's KEEP |
| NFRA_OPLGTW | Gateway operational for the staff who need it, managed through MC Portal | PRD FWD-1..19 less FWD-9 (`prd/NFRA_OPLGTW_PRD.md:55-225`). The outcomes are Schwab read access for a named staff user, accuracy, per-person scope (FWD-3), CSV download (FWD-4), revoke without a new setup (FWD-6) and existing users unharmed (FWD-7); v2.0 adds history, cost basis and the Tax SMA master; v2.1 adds the Tax-account thread. The v2.3 addendum makes the Bloomberg account mirror Andrew's grants "for now" behind an Opal-users-only Teams gate (`:885-905`) | **35 rounds; 0 of 18 FWD REALIZED.** FWD-1..8 were last graded HELD in rounds 18-23, and rounds 24-35 ruled surprise rows (box report). **Live:** the gateway and its per-family silver sweeps; the grant writer was redeployed (project.json `blocking`); the per-family dead-letter queue drain is proven for Schwab (@4c2b4ad9ca). **Round 36** is E1 (deny for the Black Diamond fee tool, on Andrew's yes), E2 (the dead-letter drain for the other families), E3 (a read of 502 errors on a Teams route) and E4 (a sharing-URL tool for dell2) (`ledger/ROUND_ANALYSIS.round35.md` @682d1ced78). Close is held until Andrew reads MCPORTAL FWD-20. 614 commits in 7 days | **PARTLY.** The charter is Schwab and Tax-SMA data depth for named users. The memo's "operational for the team, visible in MC Portal" maps only to FWD-3/6/7 and to MCPORTAL FWD-20 | **REPOINT:** keep E1 (an open entitlement gap on client fee data). Add one cell that exposes per-family sweep cadence and backfill status as a read MC Portal can show; that is Andrew's "depth of polls / backfill". E3 belongs to COMM_ASSIST, now on the laptop. Defer E4 unless dell2 is blocked this week. Grade FWD-1..8 at the next round analysis instead of only ruling rows. Close on Andrew's FWD-20 read. **Agree** with KEEP |
| NFRA_MCPINDEX | "a lot ... is done". One of the three. Its indexes must show per vendor and channel in MC Portal | PRD FWD-1..19 (`prd/NFRA_MCPINDEX_PRD.md:118-282`): one catalog, a discover family, a tool per data property, a fallback query, history and market data, one-at-a-time beta admission (FWD-9), true freshness (FWD-13), vendor data in the same index (FWD-15) | **2 of 19 REALIZED:** FWD-12 in round 8, FWD-18 in round 9 (`ledger/ROUND_ANALYSIS.round9.md` @bc8e36fdd5). **Live:** the catalog and discover release c3af8687e4. **Parked** at round close since 10-11. FWD-19 is blocked on dell2 producers; FWD-11 is HELD on Andrew booking Alyssa (an Opal staff member). One open order, MX-s-19, with its acceptance read on 10-19/20. **Catalog** `app/refs/DATA_CATALOG.yaml`: 2,114 lines, 35 top-level rows, 10 `read_tool:` lines (last change 26e4cee860, 2026-10-10) | **PARTLY.** FWD-20's "indexes" column reads this catalog. The tool-to-index link it needs is thin: MP-z-1's spec says `read_tool` sat on 4 rows when the order was cut. The remaining FWD-19 and FWD-11 do not serve the memo | **REPOINT:** keep FWD-19 and FWD-11 parked. Cut ONE small round so that every tool the gateway serves maps to its catalog index, and each index carries its history depth and freshness for the MC Portal page. **Disagree in part** with the box report's PARK (section 2a) |
| NFRA_OPALAI | "does not really matter" | 13 FWDs: the Opal Analyst in Teams over one indexed MCP, the opal_ai repo, and a non-admin runtime account | 0 of 13 REALIZED (`ledger/ROUND_ANALYSIS.round1.md` @a8baa4b23d). opal_ai PROD 9c0a80b8d0. Close-run arm (b) PASSED on 10-09. 3 pending orders are gated. The issuing COO has no process. Andrew sits with Alyssa today (box report) | **NOT COVERED by the memo's intent, but it OVERLAPS the Bloomberg-agent review:** its runtime signs in as the Opal Bloomberg account through the `opal-gateway-bbg` client entry (`task-orders/NFRA_OPALAI.TO-OA-t-3.r2-runtime-setup-launch-gate-fence.md:31`) | **PARK** with no seat, after today's sitting is recorded. Move the "people can use the Bloomberg agent" check to outcome 3 in section 5. **Agree** with PARK |
| NFRA_MCPMSP | "does not really matter"; "kind of not closed" | 11 FWDs for a partner-firm MSP analyst | 0 of 11 REALIZED. HOLD since Andrew-direct 2026-10-12 item 7. No seat, no open order (project.json `blocking`; box report) | **NOT COVERED (deprioritised)** | **PARK** as it stands (status `hold`). Not CLOSE, since he said "not closed". **Agree** |
| COMM_ASSIST | not in this memo | 4 FWDs | Moved to the laptop today (`project.json` placement LAPTOP; record `ANDREW_DIRECT_20261013_144xZ_MUSE_DECISIONS_AND_COMM_ASSIST_TO_LAPTOP.md`) | out of site Z scope | Already moved. Close its 2 site Z open calls as duplicates of laptop rows `-44eb` and `-e435` (section 2b) |
| OPAL_BBGTML (no placement; runs on site Z) | Andrew's "Bloomberg agent ... functional" review covers the seat that operates this pull | No register home: the code reads closed since the 2026-08-25 spring clean | **Failing today:** daily pull exit code 50 at 07:00 ET and freshness check exit code 2 at 07:30 ET (DAPI, the terminal's data link, is down). The terminal seat's process is alive, but its broker heartbeat is ~23 h stale. GUARD-4 is built but unmerged, waiting on Andrew (open call `-2da6`) (box report) | **NOT COVERED** (no live project) | **NEW PROJECT** (or re-open the register row) to hold BBGTML upkeep plus the Bloomberg-agent review (section 5, outcome 3). **Agree** with KEEP, and add that it needs a register home |

### 2a. Where this report disagrees with the box report

- **NFRA_MCPINDEX: the box report recommends PARK ("2/19", every remaining outcome waits on dell2 or Andrew). The memo names it in
  the top three.** I agree that its current enrichment list (FWD-19, FWD-11) should stay parked. I disagree with parking the
  project outright. Andrew's MCP Index ask in this memo is "see all indexes for all vendor/channels" in MC Portal. That needs
  MCPINDEX, the catalog's one writer, to link every served tool to its index and to state history depth and freshness. No
  other project can write `DATA_CATALOG.yaml`.
- **NFRA_OPLGTW KEEP: agreed, but its cut has drifted from the memo.** Round 36 is mostly hygiene and dell2's request. Only E1
  touches entitlements, and nothing feeds MC Portal.
- **OPAL_BBGTML KEEP: agreed, and it is the natural home for the Bloomberg-agent review.** Same terminal, same seat, failing
  this morning.

### 2b. Site Z's 7 open calls waiting on Andrew, mapped to these projects

Source: `python .tools/open-calls.py list --all --cloud`, read 2026-10-13T16:13:56Z; site Z list written 14:31Z.

| call | project | ask | relation to the memo |
|---|---|---|---|
| sitez-20261009T173038Z-21c5 | MCPORTAL | open /control-plane once and name one box's projects (FWD-14) | the panel; batch with FWD-20's read |
| sitez-20261011T000025Z-8ed7 | MCPORTAL | open /control-plane and /open-calls once and close one real call (FWD-15..17) | the panel; same sitting |
| sitez-20261009T173040Z-f0d2 | MCPORTAL | sign in once AS Opal Bloomberg in a headed window to prove the owner gate refuses it (FWD-2) | Bloomberg account plus the panel |
| sitez-20261009T170635Z-a519 | OPALAI | send one Teams message to the Opal Bloomberg account | the Bloomberg-agent review's live test |
| sitez-20261013T021538Z-2da6 | OPAL_BBGTML (no project) | merge TO-GUARD-4 into the Bloomberg tripwire | Bloomberg pipeline health |
| sitez-20261012T210024Z-288f | COMM_ASSIST | @mention once in a watched channel | duplicate of laptop row -44eb; close on site Z |
| sitez-20261011T030519Z-058e | COMM_ASSIST | a colleague emails the test text | duplicate of laptop row -e435; close on site Z |

Five of the seven serve the memo's priorities: three on MC Portal, two on Bloomberg. The two COMM_ASSIST calls are stale on
site Z. The three MC Portal calls plus FWD-20's read (MP-z-6) fit in ONE sitting of about 10 minutes.

## 3. The "one master control panel" gap table

| capability he named | in MC Portal today? | where it lives instead | owner |
|---|---|---|---|
| every vendor or channel on the gateway | NO. FWD-20 is built but not released, and there is no route at this checkout | code: `infra/aws/ec2/opal-gateway/app/integrations/` (8 packages: advi_billing, blackdiamond, globgrph, opal_discover, opal_portal, portal_index, schwab, ycharts) plus the native Microsoft 365 tools. Which are enabled live was not read | MCPORTAL (view), OPLGTW (gateway) |
| tools per channel | NO (FWD-20 pending) | the server's registered tool list (`app/tools.py`) | MCPORTAL |
| indexes per channel and tool | NO (FWD-20 pending); the link will be thin (section 2) | `app/refs/DATA_CATALOG.yaml` | MCPINDEX |
| who is entitled to what, per channel | NO (FWD-20 pending). Until the Scan grant (MP-z-4) applies, the page reads the grant store as "unreadable" by design | 3 stores: deploy-time rosters (`deploy-to-ec2.sh` .env master-admin and write-capable lists), `app/identity_scope.py` plus `identity_tool_allowlist.txt`, and the grant store `gateway-access-state-table` | OPLGTW (rules), MCPORTAL (view) |
| per ACCOUNT view ("how we see their entitlements" for one login) | NO, and not chartered. FWD-20 is channel-first; the same response can be inverted per person | same 3 stores | MCPORTAL, new cell |
| change one person's data grant | API present (`admin_api.py:52-55`: grants narrow, widen, changes); FWD-1 close run staged on Alyssa's sitting; NOT_REALIZED | grant writer lambda | MCPORTAL |
| change a person's tools, tier or channel access | NO, and not chartered | edits to deploy env and the allowlist file, by a release | OPLGTW. Unowned as a panel action |
| stop one person / kill switch | NO (FWD-10 DEFERRED) | gateway blocklist and kill switch (`blocklist.kill_switch_active`) | MCPORTAL |
| depth and breadth of polls per vendor | NO, and not chartered | OPLGTW per-family silver sweeps (AWS schedules, 16:00Z and 12:15Z, per the box report) | OPLGTW. Unowned as a view |
| backfill or history scope per tool | NO, and not chartered | `backfill-status` written by the sweeps (round 35 Z-S100 ruling); catalog freshness (MCPINDEX FWD-13) | OPLGTW + MCPINDEX. Unowned as a view |
| call log and refusals | NO (FWD-10 DEFERRED) | gateway audit lake | MCPORTAL |
| channel sensitivity | NO (FWD-19; FWD-20 shows "unrated") | `app/refs/channel_ratings.json`, if present | MCPORTAL |
| Bloomberg terminal data as a channel | NO. Bloomberg is not a gateway integration (no package in `app/integrations/`) | site Z terminal pipe (port 8194), `integrations/bloomberg/`, the MDPF_DEMQUE budget queue (dell1) | none (OPAL_BBGTML is closed in the register) |
| fabric control plane (boxes, overlap, git state, open calls) | YES, live (Control Plane 10-09, the rest 10-10) | -- | MCPORTAL |

## 4. Gaps no project owns

1. **Bloomberg agent review.** No live FWD tests "a person can use the Bloomberg agent today". The nearest is OPALAI's close
   run, which is being parked. The evidence it is degraded:
   - Today's pull exit code is 50 and the freshness check's is 2.
   - The terminal seat's broker heartbeat is ~23 h stale (box report).
   - The seat declined a send under its seat hold (msg 33123, cited in call -058e).
   - The `OPAL_D7_ticket_intake` task exited with code 2 today (box report). An OPALAI row says it has failed since 2026-09-18
     on the `opal-gateway-bbg` identity pin: 8,712 exit-2 passes against 613 exit-0
     (`org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md:1652`).

   Positive evidence: OPALAI arm (b) PASSED on 10-09 (an unprofiled sender got the how-to-get-access answer).
2. **One-gateway consolidation: already true on the server; nobody has told Andrew.** There is ONE gateway,
   `infra/aws/ec2/opal-gateway`. `opal-gateway-bbg` is the name of a second client-side MCP connection pointing at the same URL,
   `https://mcp.opalinvest.dev/mcp` (`NFRA_OPALAI.TO-OA-t-3.r2-...md:31`). It lets one machine hold the Bloomberg account's
   Microsoft sign-in next to Andrew's.
   - **Search denominator:** `infra/aws` has 4 files naming it (gateway identity code plus a vendor-secrets census) and no
     separate stack; `integrations/bloomberg` has 0; `org/missions` has 37 files, all of them references to the client entry
     or the mirror ruling.
   - Andrew's 2026-10-09 "make it mirror whatever is on opalgateway" was carried as an IDENTITY mirror: the Bloomberg account
     holds his grants (OPLGTW PRD v2.3; order OG-tg-1 complete).
   - No project charters a merge, and none is needed. There is one panel, and both logins show on it.
3. **Entitlements parity.** Entitlements live in three mechanisms, listed in section 3. FWD-20 reads all three for display only.
   No outcome lets the panel edit rosters, tool allowlists or tiers. The Bloomberg account's rule is "mirror Andrew, for now",
   with no stated end state.
4. **The MC Portal source is not on GitHub.** `Opal-Capital/mcportal` has DEV = PROD = the initial commit of 2026-09-24. The page
   code that site Z serves is on site Z only. Under the current push law, mcportal DEV and PROD pushes need no word
   (CLAUDE.md, Agent Autonomy). Owner: the site Z MSTR (`0.0.0_AB_MSTR~Z`), under PRD C1 and G-PUSH.

## 5. Fast defined outcomes (close first)

1. **FWD-20 live, and Andrew reads it** (this also meets OPLGTW's close condition).
   - **Missing:** the CTO's never-widen half on the Scan grant (MP-z-4), then the apply, then the release that adds
     `/gateway/breakdown` (MP-z-5), then Andrew's read (MP-z-6).
   - **Andrew's part:** batch his read with calls -21c5 and -8ed7 into one ~10-minute sitting.
   - **Owners:** site Z CTO, then the CloudOps applier, then the MC Portal COO.
2. **FWD-21 "control and depth" (new PRD addendum).**
   - **Missing:**
     - a per-account view covering Andrew, staff and the Bloomberg account;
     - per-person, per-channel enable and disable through the existing grant writer;
     - per-channel poll cadence and backfill depth, read from OPLGTW's `backfill-status` and the MCPINDEX catalog;
     - FWD-10's stop-one-person control, pulled forward.
   - **Owners:** site Z CTO (endpoint and PRD), MC Portal COO (issuance), OPLGTW COO (one backfill-status read cell), MCPINDEX
     (one catalog-link round).
3. **Bloomberg agent works for people: a read-only trace plus repair.**
   - **Done when:** an Opal user's Teams question to the Bloomberg account gets a correct answer, the daily pull lands with
     freshness PASS, and the intake runner's identity pin is fixed or retired.
   - **Missing:** a DAPI sign-in (two-phase, `integrations/bloomberg/READ_HERE.md` section 2), one Teams message (call -a519,
     Andrew or any Opal colleague), and a register home.
   - **Owners:** site Z CTO assigns it; the terminal seat does the sign-in. A read-only trace needs no word from Andrew.

Owner key: site Z CTO = `1.0.0_SA_CTO~Z`; CloudOps applier = `0.7.0_AE_CloudOps~MQ`; MC Portal COO = `2.0.0_SA_COO~MP`;
OPLGTW COO = `2.0.0_SA_COO~O`; terminal seat = `0.0.3_BG_BBGTerminal`.

## 6. Resourcing

Seat counts are from the box report (as of 14:44Z). Commit counts are from the same report:
`git log --since='7 days ago' --grep=<CODE> HEAD`.

| project | Andrew rank | site Z seats on it | commits 7d |
|---|---|---|---|
| NFRA_MCPORTAL | 1 (centre stage) | COO, CloudOps applier, workers (3 in 24 h), shared CTO and CVO | 171 |
| NFRA_OPLGTW | 1 (with MCPORTAL) | COO, CloudOps applier, shared CTO and CVO | 614 |
| NFRA_MCPINDEX | 2 | CloudOps applier only; the COO has no process | 178 |
| NFRA_OPALAI | deprioritised | none live; the COO has no process | 80 |
| NFRA_MCPMSP | deprioritised | none | 19 |
| other: AMGT_HARVST, MDPF_DEMQUE (dell1), OPAL_BBGTML | not named | 2 CloudOps lanes (one with no process), the terminal seat | -- |

- **Effort is inverted against his ranking.** OPLGTW draws 3.6 times MCPORTAL's commits, and most of it is hygiene.
- **Parking OPALAI and MCPMSP frees no live seat;** both COO lanes already have no process.
- **The real levers:**
  - Point the OPLGTW COO's next round at the MC Portal feeds (section 5, outcome 2) rather than E3 and E4.
  - Free the MCPINDEX CloudOps lane after MX-s-19's 10-19/20 read, or use it for the catalog-link round.
  - Treat site Z's lending to dell1 (25 of 26 cross-box items, per the box report) as a decision, not a default.

## 7. Questions only Andrew can answer

1. **Does "controlled" mean editing tools, channels and tiers per person from MC Portal, beyond data grants and a kill switch?**
   Recommendation: yes. Charter it as FWD-21 on the existing grant writer, after FWD-20.
2. **There is one gateway server, and `opal-gateway-bbg` is only the second login entry on the shared machine. Is that acceptable,
   provided both accounts show on the one panel?** Recommendation: yes. Keep both entries and do not build a merge.
3. **Should the Bloomberg account keep mirroring your grants ("for now", 2026-10-09)?** Recommendation: keep the mirror until you
   have read it on FWD-20, then name its own rules there.
4. **MCP Index: keep FWD-19 and FWD-11 parked, but run one round linking every served tool to its index, with history depth?**
   Recommendation: yes. This resolves the conflict with the box report's PARK.
5. **NFRA_OPALAI after today's Alyssa sitting: PARK or CLOSE?** Recommendation: PARK. Run the Bloomberg-agent check as section 5,
   outcome 3, under a re-homed OPAL_BBGTML.
6. **Merge TO-GUARD-4 (call -2da6)?** Recommendation: yes. It is built and proved, and the CRO recommends it too.
7. **Does MC Portal stay Andrew-only (2026-09-17 ruling), given that the memo says "we need to be able to manage"?**
   Recommendation: keep writes Andrew-only, and name later any staff who should get read access.

## 8. Method

- **Read in full:**
  - the transcript;
  - the box report;
  - the site Z seven-rulings record (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md`);
  - the OPLGTW round 35 analysis.
- **Read in part:**
  - the 5 project.json files (key fields);
  - MCPORTAL PRD lines 85-219, 300-339 and 520-546;
  - order MP-z-1 (handler spec and status);
  - MCPORTAL round 4 grades;
  - FWD headline lines of the OPLGTW and MCPINDEX PRDs, and the OPLGTW PRD v2.3 addendum;
  - MCPINDEX round 9 grades;
  - `integrations/bloomberg/READ_HERE.md` lines 1-200 of 280;
  - gateway `admin_api.py` routes, `identity_scope.py`, `config.py` and `deploy-to-ec2.sh` identity lines;
  - catalog line counts;
  - MCPORTAL non-terminal orders (14 faces);
  - `git log -5` for each of the 5 codes;
  - aggregate report lines 54-67.
- **Denominators:**
  - 52 mission-tree project.json, 11 SITEZ-placed, 5 not closed;
  - 7 site Z open calls of 14 cluster-wide;
  - `opal-gateway-bbg`: 4 files in infra/aws, 0 in integrations/bloomberg, 37 in org/missions.
- **Live reads (4 of the 5 allowed, all read-only):**
  - gh api, mcportal branches: DEV and PROD at fa1ff9693b;
  - gh api, mcportal commit 6fbd25e: HTTP 422, not found;
  - HTTPS GET of `https://mcp.opalinvest.dev/control-plane` and `/routes.json`: both 302 to Microsoft sign-in, so page content
    is unreadable without signing in.
- **Not read:**
  - what the live MC Portal pages render (sign-in required);
  - which gateway integrations are enabled live;
  - whether the Bloomberg account currently holds a grant-store profile;
  - site Z's local worktrees and its mcportal checkout;
  - the OPALAI and MCPMSP PRDs beyond project.json;
  - OPLGTW rounds 24-34;
  - the AWS graph (sweep schedules not counted).
