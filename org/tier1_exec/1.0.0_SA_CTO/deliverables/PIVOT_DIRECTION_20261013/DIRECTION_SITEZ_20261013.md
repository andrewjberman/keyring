# DIRECTION -- site Z -- 2026-10-13: Andrew's voice memo in full, and how site Z carries it out

## 0. Header

- **To:** `1.0.0_SA_CTO~Z` (site Z box CTO, rules site Z's projects) and `0.0.0_AB_MSTR~Z` (site Z master: seats, lanes,
  integration). Copy for the record: `4.0.0_SA_CRO~Z`, `3.0.0_SA_CVO~Z`.
- **From:** `1.0.0_SA_CTO` (laptop, cluster lead), 2026-10-13 ~17:5xZ.
- **Status:** ACCEPTED. Andrew answered the positioning calls and asked that each box get his words "in full rich capacity versus
  solely just a light little directive, as I want to make sure these things are all done completely and correctly as I
  dictated" (Andrew-direct ~17:5xZ, laptop terminal).
- **Authority, in force today:**
  - Andrew's site Z voice memo, 2026-10-13 morning (section 1.1, verbatim).
  - Andrew's AMGT voice memo, same morning, for asset-manager access to the harvest bucket (section 1.2, verbatim).
  - `ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md` (tier1 CTO): FWD-20 first; OPLGTW close held on
    Andrew reading the breakdown.
  - `ANDREW_DIRECT_20261009_032xZ_OPAL_GATEWAY_BBG_MIRRORS_OPALGATEWAY.md` and `..._033xZ_BBG_CONCIERGE_OPAL_USERS_ONLY_GATE.md`
    (tier1 CTO): the Bloomberg account mirrors Andrew "for now"; Opal users only.
  - `ANDREW_DIRECT_20261013_131xZ_DELL_BOXES_GET_THEIR_OWN_PERMISSIONS_NO_CROSSBOX_CLOUDOPS.md` (CRO): no cross-box CloudOps.
  - `ANDREW_DIRECT_20261013_140xZ_FOUR_OPEN_CALLS_ANSWERED_DEVPLN_TAILNET_SSH_BDFEE_CTLPLN_SCOPE.md` (CRO): call 3, the Black
    Diamond (BD) fee tool, answered yes; call 2, tailnet-only SSH.
  - `ANDREW_DIRECT_20261013_144xZ_MUSE_DECISIONS_AND_COMM_ASSIST_TO_LAPTOP.md` (CRO): COMM_ASSIST moves to the laptop.
  - `ANDREW_DIRECT_20261013_163xZ_OPAL_TERMINAL_KEY_SHUT_OFF_IF_SITEZ_DOES_NOT_USE_IT.md` (tier1 CTO, recorded by
    `1.0.0_SA_CTO~DELL2`).
  - The laptop CTO's positioning ruling `RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md` @f469cb665f, and
    Andrew's answers to it, `ANDREW_DIRECT_20261013_174xZ_POSITIONING_CALLS_ANSWERED_ARTIFACT_AND_CLICKABLE_PATHS.md` @0b8380acf8.
  - Evidence base: the CRO's site Z alignment report and AMGT alignment report (section 7), and the site Z box status report of
    14:44Z.
- **How to use this file:**
  1. Read sections 1 and 2 IN FULL before ruling or cutting anything. Section 1 is the source; every other section serves it.
  2. Mid-round specs and decompositions stay FROZEN (CLAUDE.md rule 27). Every change here lands at the named project's NEXT
     round-N analysis (the CTO's L10 answer) or as a PRD addendum, never inside a live round. NFRA_OPLGTW round 36 is issued
     (@919f6822eb) and drains as cut.
  3. Where this file and the alignment reports differ, this file wins; where this file and Andrew's verbatim words differ,
     his words win and the gap goes to the laptop CTO as a surprise ROW, not a broker message.

---

## 1. Andrew's words, in full

### 1.1 The site Z memo (complete, verbatim auto-transcript)

Source: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/SITEZ_NFRA_REVIEW_TRANSCRIPT.md`. Auto-transcript
renderings: "OPL" = Opal; "OPLinvest.com" = opalinvest.com; "menopkin" and "OSSA" are the transcript's renderings of two staff
accounts, so read the real principals from the grant store and do not guess them; "SCORBG" / "SCORBBG terminal" = the
underscore-BBG terminal, i.e. `0.0.3_BG_BBGTerminal`; "Android OPL Invest" is most likely "Andrew at opalinvest" (his own
account).

> Now I'm going to move to SiteZ and the NFRA projects on SiteZ. So there's a lot going on here and I want to make sure that a
> handful of them are prioritized above all else. And so what that looks like is the OPL GTW, the Infra Opal Gateway project. We
> need to be able to manage that through MC Portal, the MC Portal project. We need to be able to see all indexes for all vendor
> slash channels. We need to see who is entitled to what the depth and breadth of the polls available, the depth and breadth of
> channels and indexes and tools available per vendor. All that needs to be visible and controlled through MC Portal, because
> otherwise it's just too difficult to operate in the fast moving environment. So I know that a lot of the MCP index stuff is
> done. That means that MC Portal needs to take center stage here, and we make sure that we are able to display that and control
> it through that portal, so that we can make sure that the OPL Gateway is operational for the team members that need it. That is
> the biggest priority for the Site Z box. All other projects really do not matter at this point. OPL AI does not really matter.
> The MSP MCP, it is not really matter. All of these are kind of not closed, but the focus I would say is entirely on three
> projects. OPL Gateway, MCP Index, and MC Portal. Those are the three that matter. Over time we want to make sure that the OPL
> agent currently 0.0.3 under SCORBG, under SCORBBG terminal. We want to make sure that's functional. I think it's worth doing a
> review there to make sure that's functional, that people can use it. And again, all the entitlements and all how that works,
> needs to be for the Bloomberg agent, needs to be established in the MC Portal. We should see just like we see for menopkin at
> OPLinvest.com or at OSSA at OPLinvest.com. How we see their entitlements, what channels they have access to, what tools and
> those channels, what backfill or scope out those tools work. Just like we see those, we should also see for OPL Bloomberg at
> OPLinvest.com, because that is the OPL Bloomberg channel. And this way we have one master control panel. I don't love the idea
> of having to use different control panels on different MCP, where we have an OPL Gateway, but we also have OPL-gateway-BBG. It
> seems to me that all of them should go through OPL Gateway. We have the control plan to gauge entitlements based on who is
> logged in where if it has to be through the two separate ones based on the logins, that because we are trying to run Android
> OPL Invest and OPL Bloomberg at OPLinvest.com off the same device. So be it, but it has to be able to be visible and managed
> there.

### 1.2 The AMGT memo (complete, verbatim auto-transcript) -- site Z carries its asset-manager access item

Source: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/AMGT_REVIEW_TRANSCRIPT.md`. AMGT = Asset Management;
"DEM QE" = MDPF_DEMQUE; "open dash data dash harvest" = the `opal-data-harvest` bucket; "their cloud" = their Claude. The
Security Analysis page and the AI fill are dell1's; site Z owns the paragraph marked [SITE Z].

> I'd like to go through some of our highest priorities here. So there are a lot of projects actively being run. I'm going to
> handle them for the most part on each individual device because sometimes we just need to get really into the weeds very
> quickly here. So I've been running around for the last two hours since about 9 a.m. Eastern today on October 13th, 2026 to move
> these along where possible. But I want to ideally have a mechanism for managing this on the control plane. I don't think that we
> need to build anything new for this. I simply just want to bring you as the CTO of the cloud dashboard, go laptop box up to
> speed on what needs to happen here. So we can make the allocation decisions needed to accelerate our high profile wins that we
> need to happen. And potentially deprioritize some of the lower impact items. So moving through the macro groups, I will start
> with the AMGT that is the asset management. So we want to get this project up with the ability for the asset managers to access
> all of this data easily. And ideally, we have the functional web application, the security analysis page with all of the
> relevant information available there. But if that is going to take too long, if we are too far away from that outcome, like for
> example, if that's held up on certain backfill elements, which are dependent on the DEM QE project, MDPF underscore DEM QE, if we
> need to assess really what needs to happen to at least get the 93 research pages completely loaded in here, we need to make sure
> that all information is displaying correctly that the user interface is clean and easy to use, that the pages load fast, that
> we, which I believe we should have handled already. But yeah, we want to make sure that at least this page is usable. And so one
> of some things that I can think of immediately off the top that we want to implement here is that there are a lot of cases where
> a, their may or may not be immediately obvious in available executive management, for example, or some of the thesis stuff is
> hard to weigh. There are various things are hard to weigh. And I essentially want to fill in these gaps with dedicated, open AI
> calls that do the AI analysis to fill out obvious text sections. So that would be getting the, an executive management bio
> summary. So like any recent developments on the executive management, we would want that to surface. So that probably just going
> to be a web search. And the premise here is that no matter what data that we have for any of these given pages, some are going
> to have more complete data than others, we want to be able to display information for all of them. And we want to be able to
> fill out these key text sections for all of them. So that what that looks like is whatever we were able to get, use from our,
> our, our, embedded sources, whatever we were not able to get, uh, dedicate to web search and just, that's how we fill out some
> of these, the high profile blocks on the asset management web app. [SITE Z] And separately, we need to figure out the, open
> gateway mechanics for how to connect the, uh, the various, open dash data dash harvest folders, uh, and set up the MCP index for
> that bucket. How to set that up quickly and easily so that the asset managers can use that with their cloud. So that those are
> the all the high priority items for the AMGT segment, uh, harvest, the design, everything else can kind of continue along on its
> pace. But the point is that we need to close these out. We need to close at least a functional V1. So that's how I would break
> out this AMGT, uh, into, yeah, what we need to do to get the web functioning, what we need to do to get the Opal data harvest
> folders accessible for the asset management research team. Now I'm going to move on to the next transcript, which will be
> focused on the various, uh, MDPF macro items.

### 1.3 Today's recorded words that bind site Z (verbatim)

- **The gateway breakdown is first, and OPLGTW does not close without it** (2026-10-12 ~20:5xZ, recorded in the MC Portal PRD
  v0.7 addendum, `org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md:525-528`): "I wouldnt close this project (OPLGTW)
  until I have seen a full breakdown of the vendors/channels available via the gateway, what tools/indexes exist for each, and
  current state of entitlements. The easiest way to manage this would be via the MCPORTAL, and this is what I think should be the
  first distinct outcome of the MCPORTAL project."
- **The Bloomberg account mirrors Andrew, for now** (2026-10-09 ~03:2xZ, `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:889-890`):
  "opal-gateway-bbg should be an exact copy of opal-gateway for now, just make it mirror whatever is on opalgateway for
  consistency, eventually we will make rules but not yet".
- **Opal users only** (2026-10-09 ~03:3xZ, `NFRA_OPLGTW_PRD.md:900-901`): "it should only accept inquiries from opal capital users
  however, no external users, should not even respond at all".
- **The BD fee tool** (2026-10-13 ~14:0xZ, 140xZ record, call 3): "3.) Yes that is fine." Applied: admit the 2 unprofiled callers
  by profile and grant, then ship the deny.
- **No cross-box CloudOps** (2026-10-13 ~13:1xZ, 131xZ record): "I do not want CloudOps agents from one box working on projects
  that are otherwise based on another box, because its unnecessary separateion in 99% of cases."
- **COMM_ASSIST to the laptop** (2026-10-13 ~14:4xZ, 144xZ record): "I want this box handling CTLPLN, DEVPLN, and ASSIST, because I
  need to be overseeing them directly."
- **Tailnet-only SSH** (2026-10-13 ~14:0xZ, 140xZ record, call 2): "The key with ssh is that we want ssh to be functional within
  tailnet devices only, no external ssh available nor any external rdp available (aside from IT services like splashtop)."
  Andrew reports password login is now OFF (174xZ record, item 3).
- **The Opal_Terminal key** (2026-10-13 ~16:3xZ, 163xZ record): "As long as SITEZ does not use Opal_Terminal then we can shut it off."
- **The control panel is readable** (2026-10-13 ~16:2xZ, recorded by `2.0.0_SA_COO~MP` at
  `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/ANDREW_DIRECT_20261013_162xZ_CONTROL_PLANE_OPEN_CALLS_READABILITY.md`,
  quoted in commit 9e6ba382df): "I'd like for them to be visually slightly easier to read, particularly on the control-plane side.
  both can be articulated better, but open-calls is mostly legible."

---

## 2. The outcomes Andrew dictated

Owner key (from the site Z alignment report, section 5): site Z CTO = `1.0.0_SA_CTO~Z`; MC Portal COO = `2.0.0_SA_COO~MP`;
OPLGTW COO = `2.0.0_SA_COO~O`; CloudOps applier for MC Portal = `0.7.0_AE_CloudOps~MQ`; OPLGTW CloudOps = `0.7.0_AE_CloudOps~Z`;
MCPINDEX CloudOps = `0.7.0_AE_CloudOps~MI` (its COO `2.0.0_SA_COO~MI` has no process); terminal seat = `0.0.3_BG_BBGTerminal`.

### Outcome Z1 -- MC Portal shows the whole gateway on one page (FWD-20), and Andrew reads it

- **His words:** "We need to be able to see all indexes for all vendor slash channels. We need to see who is entitled to what ...
  All that needs to be visible ... through MC Portal." And (10-12): "a full breakdown of the vendors/channels available via the
  gateway, what tools/indexes exist for each, and current state of entitlements."
- **Done when (as Andrew sees it):** he opens `https://mcp.opalinvest.dev`, goes to the gateway breakdown page, and sees every
  vendor or channel the deployed gateway serves, the tools on each, the catalog indexes behind each tool, and who holds an active
  grant on each today. A channel with no grant reads "no one", never blank.
- **Proof read:** FWD-20's DONE WHEN (`NFRA_MCPORTAL_PRD.md:204-209`): Andrew reads the page; one channel's tool list is checked
  against the deployed gateway's code, and one person's entitlements against the grant store. The channel list is generated from
  the deployed gateway's definitions, never a hand-kept list (C15).
- **Owner:** NFRA_MCPORTAL, `2.0.0_SA_COO~MP` (issuer), `0.7.0_AE_CloudOps~MQ` (release), `1.0.0_SA_CTO~Z` (rules).
- **State, measured:**
  - The page code (handler, page, deep links) is built: MP-z-1 @fda2ca67a3, MP-z-2 @bcddb3e6b0, MP-z-3 @7218b1e3ae (site Z box
    report, NFRA_MCPORTAL block).
  - The grant-store read permission (DynamoDB Scan on `gateway-access-state-table`) is NOW APPLIED: MP-z-4 complete @b48518c61b,
    ledger closed @1c605b70a2 ("the one dynamodb:Scan grant is LIVE on opal-gateway-role"). The alignment report's "still owes
    the CTO's half" is superseded.
  - MP-z-5 (the gateway release that adds the page) reads `<status>staged</status>`
    (`task-orders/NFRA_MCPORTAL.TO-MP-z-5.gw-gateway-release.md:131`). MP-z-6 (Andrew's read, the close run) reads staged (`:95`).
  - MP-z-2 was re-opened by Amendment 1 for Andrew's readability ask and rides the same release bundle (@9e6ba382df).
  - Not live at the laptop checkout: no `/gateway/breakdown` route in `infra/aws/ec2/opal-gateway/app/admin_api.py:49-60`
    (alignment report, section 2).
  - The `Opal-Capital/mcportal` repo on GitHub reads DEV = PROD = fa1ff9693b (the 2026-09-24 initial commit); page commit 6fbd25e
    is not found there (alignment report, section 4.4). The page source lives on site Z only.
- **Gap:** the release (MP-z-5) and Andrew's read (MP-z-6). Also the source is not on GitHub.
- **Box CTO's act:** keep FWD-20 ahead of every other MC Portal order (PRD v0.7 addendum `:535-536` already says so). See that
  MP-z-5 ships the breakdown page and the MP-z-2 readability fix in one release. Then batch Andrew's read with the three MC Portal
  open calls into ONE sitting of about 10 minutes (Z6 below).
- **Site Z MSTR's act:** push the mcportal source to GitHub DEV (the push law needs no word for an Opal-internal page; CLAUDE.md
  Agent Autonomy), so the served page is not held on one box only.
- **Order:** FIRST on site Z.

### Outcome Z2 -- MC Portal CONTROLS the gateway, per person (FWD-21, a new PRD addendum)

- **His words:** "All that needs to be visible and controlled through MC Portal, because otherwise it's just too difficult to
  operate in the fast moving environment." "we make sure that we are able to display that and control it through that portal".
  "this way we have one master control panel".
- **Ruled (laptop CTO, @f469cb665f, on these words):** yes to control; writes stay Andrew-only (consistent with the 2026-09-17
  Andrew-only ruling cited in the alignment report, section 7 question 7). Read access for named staff is a later call of his.
- **Done when (as Andrew sees it):** on MC Portal he picks a person (himself, a staff member, the Bloomberg account) and sees that
  person's channels, the tools on each channel, and the backfill or history scope of each tool. He switches one channel or one
  tool on or off for that person, or changes the person's tier, and the gateway honours it on that person's next call. He can stop
  one person entirely.
- **Proof read:** a driven change on a test principal: the change is made on the page; the grant store reads it back; the
  person's next gateway call is allowed or refused accordingly; the change is undone the same way. Plus the per-person view
  checked against the three entitlement stores for one real person.
- **Owner:** NFRA_MCPORTAL. `1.0.0_SA_CTO~Z` writes the FWD-21 endpoint and PRD addendum (L2/L4); `2.0.0_SA_COO~MP` issues;
  `3.0.0_SA_CVO~Z` signs the ratified-text half.
- **State, measured (alignment report, section 3 gap table):**
  - Change one person's DATA grant: the API exists (`admin_api.py:52-55`: grants narrow, widen, changes); FWD-1 is NOT_REALIZED,
    its close run staged on Alyssa's sitting.
  - Change a person's TOOLS, TIER or CHANNEL access: not chartered. Today it is an edit to the deploy environment and
    `identity_tool_allowlist.txt`, shipped by a release (OPLGTW's write surface).
  - Per-ACCOUNT view: not chartered; FWD-20 is channel-first ("the same response can be inverted per person").
  - Stop one person / kill switch: exists on the gateway (`blocklist.kill_switch_active`); the panel action is FWD-10, DEFERRED.
  - Entitlements live in THREE stores: deploy-time rosters (`deploy-to-ec2.sh` master-admin and write-capable lists),
    `app/identity_scope.py` plus `identity_tool_allowlist.txt`, and the grant store `gateway-access-state-table`.
- **Gap:** no outcome lets the panel edit tools, channels or tiers; no per-person view; two of three entitlement stores change
  only by a release.
- **Box CTO's act:** write FWD-21 "control and depth" after FWD-20 ships. Its parts, from the alignment report section 5.2:
  (a) a per-account view for Andrew, staff and the Bloomberg account; (b) per-person, per-channel enable and disable through the
  existing grant writer; (c) per-channel poll cadence and backfill depth (Z3 feeds it); (d) FWD-10's stop-one-person control,
  pulled forward. Decide in the PRD whether tool and tier edits move from the deploy-time files into the grant store (one writer,
  CLAUDE.md rule 30 builder names for any new resource), or stay release-borne with the panel raising the release; name the
  choice and its rollback. Keep FWD-3..13 (home page, operations report, user management, analytics, cost, infosec) deferred
  behind FWD-21.
- **Order:** second, cut at MC Portal's next round-N analysis after FWD-20's release.

### Outcome Z3 -- the panel shows the depth and breadth of every poll: cadence and backfill per vendor (OPLGTW feeds it)

- **His words:** "the depth and breadth of the polls available, the depth and breadth of channels and indexes and tools available
  per vendor" and, for each account, "what backfill or scope out those tools work".
- **Done when (as Andrew sees it):** on MC Portal, each vendor or channel shows how often its data is polled (the schedule) and how
  far back its history reaches (backfill depth), with the date the figure was read.
- **Proof read:** one family's cadence on the page matches its live AWS schedule; one family's backfill depth on the page matches
  `backfill-status` and the served data's earliest date.
- **Owner:** NFRA_OPLGTW produces the read (`2.0.0_SA_COO~O`, one cell); NFRA_MCPINDEX supplies catalog freshness and history
  depth (Z4); NFRA_MCPORTAL displays it (inside FWD-21).
- **State, measured:**
  - The data exists, scattered: per-family silver sweeps on AWS schedules (16:00Z and 12:15Z per the site Z box report);
    `backfill-status` written by the sweeps (round 35 Z-S100 ruling); catalog freshness is MCPINDEX FWD-13. No view owns it
    (alignment report, section 3).
  - OPLGTW: 0 of 18 FWD REALIZED after 35 rounds; rounds 24-35 ruled surprise rows rather than grading outcomes; 614 commits in 7
    days against MC Portal's 171 (site Z box report).
  - Round 36 is issued (@919f6822eb): E1 the BD-fee deny with master_admin admitted by tier (OG-bd-2; proof AC1 and AC2 PASS
    @ac334b85d6, it now asks for the release), E2 the dead-letter drain record and per-family drift census (OG-fd-2), E3 the 502
    read on a Teams route (OG-rd-1), E4 a `list_shared_folder` tool for dell2 (OG-sh-1).
- **Gap:** nothing feeds the panel. The effort is upkeep.
- **Box CTO's act:** let round 36 drain as cut (frozen). At the round-36 analysis (the round-37 cut): ONE cell that exposes
  per-family sweep cadence and backfill status as a read MC Portal can show; GRADE FWD-1..8 instead of only ruling rows; route E3
  (Teams 502) to COMM_ASSIST on the laptop as a row if it recurs, since that channel is now the laptop's; take no further dell2
  convenience cells unless dell2 is blocked this week. OPLGTW closes on Andrew's FWD-20 read (his 10-12 condition).
- **Order:** third; in OPLGTW's next round.

### Outcome Z4 -- MCP Index: every served tool links to its index, with depth and freshness; harvest rows added

- **His words (site Z memo):** "I know that a lot of the MCP index stuff is done." "the focus I would say is entirely on three
  projects. OPL Gateway, MCP Index, and MC Portal." **(AMGT memo):** "set up the MCP index for that bucket. How to set that up
  quickly and easily so that the asset managers can use that with their cloud."
- **Ruled (laptop CTO, @f469cb665f):** ONE short MCPINDEX round. Keep FWD-19 and FWD-11 parked. This resolves the site Z CRO's
  PARK against Andrew naming MCPINDEX one of the three that matter.
- **Done when (as Andrew sees it):** (a) on MC Portal, every tool on every channel names its catalog index and that index's
  history depth and freshness; (b) asking `opal_discover` for "harvested news articles and chatter" or "security analysis research
  pack" returns catalogued datasets instead of `catalogued: false`.
- **Proof read:** a census over the gateway's served tools: N tools served, N with a catalog index named (denominator printed);
  three `opal_discover` reads (the two harvest subjects plus the Schwab positive control).
- **Owner:** NFRA_MCPINDEX, the ONLY writer of `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` (alignment report 2a).
  Its COO lane `2.0.0_SA_COO~MI` has no process: `0.0.0_AB_MSTR~Z` seats it for this one round. `0.7.0_AE_CloudOps~MI` keeps its
  MX-s-19 read on 2026-10-19/20.
- **State, measured:**
  - 2 of 19 REALIZED (FWD-12 round 8, FWD-18 round 9; `ledger/ROUND_ANALYSIS.round9.md` @bc8e36fdd5). Parked at ROUND_CLOSE
    since 2026-10-11.
  - Catalog: 2,114 lines, 35 top-level rows, 10 `read_tool:` lines (last change 26e4cee860, 2026-10-10). The tool-to-index link
    is thin (alignment report, section 2).
  - Live gateway read 2026-10-13: `opal_discover` returns `catalogued: false` for both harvest subjects; the Schwab control
    returns 8 datasets (AMGT alignment report, NFRA_MCPINDEX row).
  - The MCPINDEX PRD has 0 mentions of harvest (AMGT alignment report, same row).
  - `s3://opal-data-harvest/`: 24 top-level prefixes; `packs/`: 105 per-name prefixes (AMGT alignment report, method).
- **Gap:** tool-to-index links, depth and freshness per index, and harvest/research rows.
- **Box CTO's act:** one round, two cells: (1) link every served tool to its index with history depth and freshness; (2) add
  harvest and research catalog rows for the prefixes dell1 names as servable (Z5). Build ladder step 2 first: if the served
  packs are JSON, the existing `gateway_query_catalog` read may need only catalog rows, not a new tool.
- **Order:** fourth; can run in parallel with Z2 (different write surface: the catalog file).

### Outcome Z5 -- asset managers reach opal-data-harvest from their own Claude, through the gateway (V1)

- **His words:** "figure out the, open gateway mechanics for how to connect the ... open dash data dash harvest folders ... so that
  the asset managers can use that with their cloud." "We need to close at least a functional V1."
- **Ruled (laptop CTO, @f469cb665f):** V1 serves DERIVED layers (packs, chatter, scores, management, filings outputs) and article
  LINKS only, not raw publisher text from WSJ, Barron's, FT or Seeking Alpha. Andrew may widen this.
- **Done when (as Andrew sees it):** an asset manager, signed in to a work Claude account, asks about one covered name and gets
  that name's research pack and chatter from the harvest bucket through the gateway, and nothing outside research data.
- **Proof read:** one real asset-manager principal's driven call returns the pack; the same principal's call for a Schwab or BD
  tool is refused; a principal without the research grant is refused the pack.
- **Owner:** NFRA_MCPINDEX (catalog rows, Z4) + NFRA_OPLGTW (asset-manager principals and a research grant, one act in its next
  round) at site Z; dell1 (`1.0.0_SA_CTO~DELL1`, AMGT_RESAPP / AMGT_HARVST) supplies the list of servable prefixes.
- **State, measured:** owner today is NONE (AMGT alignment report, section 4 V1-ACCESS). OPLGTW's charter is Schwab and Black
  Diamond only; its PRD has 0 mentions of harvest or research. Whether asset managers already hold gateway principals or work
  Claude accounts was NOT read.
- **Gap:** principals, grant, catalog rows, servable-prefix list.
- **Box CTO's act:** ask `1.0.0_SA_CTO~DELL1` for the servable-prefix list through the cross-box channel (one ask); add the
  research grant to OPLGTW's next round; name the asset-manager principals from the grant store; if any asset manager lacks a
  work Claude account, that is an Andrew act -- put it on the site Z open-calls list.
- **Order:** fifth; after Z4's catalog rows.

### Outcome Z6 -- the Bloomberg agent works for people, and shows on the panel like any account

- **His words:** "Over time we want to make sure that the OPL agent currently 0.0.3 ... SCORBBG terminal. We want to make sure
  that's functional. I think it's worth doing a review there to make sure that's functional, that people can use it. And again,
  all the entitlements and all how that works, needs to be for the Bloomberg agent, needs to be established in the MC Portal ...
  Just like we see those, we should also see for OPL Bloomberg at OPLinvest.com, because that is the OPL Bloomberg channel."
- **Done when (as Andrew sees it):** an Opal colleague's Teams question to the Bloomberg account gets a correct answer; the daily
  pull lands with freshness PASS; and `opalbloomberg@opalinvest.com` appears on MC Portal with its channels, tools and scope,
  like any other person.
- **Proof read:** one Teams question and its answer read (open call `sitez-20261009T170635Z-a519`, Andrew or any Opal colleague);
  the scheduled pull's LastTaskResult 0 and freshness PASS on a trading day (resolve the trading calendar first,
  `lib/trading_calendar.py`); the intake runner's identity pin fixed or retired; the Bloomberg account's row on FWD-20/FWD-21.
- **Owner:** OPAL_BBGTML, which has NO live register home (register reads closed since the 2026-08-25 spring clean, yet it runs
  3 scheduled jobs). `1.0.0_SA_CTO~Z` gives it a home (re-open the register row, or register a successor) and assigns the trace;
  `0.0.3_BG_BBGTerminal` does the DAPI (Bloomberg Desktop API) sign-in.
- **State, measured (site Z box report and alignment report, section 4.1):**
  - `OPAL_BBGTML_daily_pull` LastTaskResult 50 at 07:00 ET today; `OPAL_BBGTML_freshness_check` 2 at 07:30 ET (DAPI down).
  - The terminal seat's process is alive but its broker heartbeat was ~23 h stale.
  - `OPAL_D7_ticket_intake` (every 5 minutes) exited 2 today. An OPALAI row says it has failed since 2026-09-18 on the
    `opal-gateway-bbg` identity pin: 8,712 exit-2 passes against 613 exit-0
    (`org/missions/D6/NFRA/NFRA_OPALAI/surprise-channel/investigations/INVESTIGATION_v1.Z.md:1652`).
  - Positive evidence: OPALAI close-run arm (b) PASSED on 10-09 (an unprofiled sender got the how-to-get-access answer).
  - TO-GUARD-4 is built and proved on branch `rv-bbgtml-guard4` (AC1 PASS, 3b65362444) but not merged: Andrew's no-modify order on
    `integrations/bloomberg/` was lifted for GUARD-3 only (open call `sitez-20261013T021538Z-2da6`).
  - Bloomberg is not a gateway integration (no package under `infra/aws/ec2/opal-gateway/app/integrations/`).
- **Gap:** no owner; pull failing; intake failing on the identity pin; not visible on the panel.
- **Box CTO's act:** (1) a READ-ONLY trace first (needs no word): DAPI state, the pull's failure, the intake pin, the Teams path.
  (2) Then the repair under a register home. (3) The Bloomberg account's row is in FWD-20 (display) and FWD-21 (control).
  Bloomberg pulls go only through their queue (CLAUDE.md Agent Autonomy); read `integrations/bloomberg/READ_HERE.md` FIRST.
- **Order:** sixth ("over time"), but the read-only trace starts now because the pull failed this morning.

### Outcome Z7 -- one gateway, two logins, both visible and managed on the one panel

- **His words:** "I don't love the idea of having to use different control panels on different MCP, where we have an OPL Gateway,
  but we also have OPL-gateway-BBG. It seems to me that all of them should go through OPL Gateway ... if it has to be through the
  two separate ones based on the logins ... So be it, but it has to be able to be visible and managed there."
- **Measured fact, not yet told to Andrew:** there is ONE gateway server (`infra/aws/ec2/opal-gateway`). `opal-gateway-bbg` is a
  second client-side MCP connection entry pointing at the same URL, `https://mcp.opalinvest.dev/mcp`, so one machine can hold the
  Bloomberg account's Microsoft sign-in beside Andrew's (`NFRA_OPALAI.TO-OA-t-3.r2-runtime-setup-launch-gate-fence.md:31`;
  search denominator: 4 files in `infra/aws`, 0 in `integrations/bloomberg`, 37 in `org/missions`; alignment report 4.2).
- **Ruled (laptop CTO, @f469cb665f):** no merge is built. Both logins stay; both show and are managed on MC Portal (Z1, Z2).
  The Bloomberg account keeps mirroring Andrew's grants ("for now", OPLGTW PRD v2.3) until Andrew has read it on FWD-20 and
  names its own rules there.
- **Done when:** both principals appear on the FWD-20 page with their grants; Andrew is told in one line, at the FWD-20 sitting,
  that it is one server with two logins.
- **Owner:** NFRA_MCPORTAL (display), `1.0.0_SA_CTO~Z` (the one-line explanation at the sitting).

---

## 3. Decisions: taken and open

### Taken (act on these; do not re-ask)

| decision | word | state |
|---|---|---|
| BD fee tool: admit the 2 unprofiled callers by profile and grant, then ship the deny | Andrew "Yes that is fine" (140xZ, call 3) | call `sitez-20261011T224736Z-1b36` closed on site Z (laptop tick 32 @8e2b5a0609); OG-bd-2 proof PASS @ac334b85d6, asks for the release: ship it |
| MC Portal controls tools, channels, tiers per person (FWD-21); writes Andrew-only | his memo words; laptop CTO ruling @f469cb665f | write the addendum after FWD-20 |
| One gateway, two logins; no merge | his "So be it, but ... visible and managed there"; ruling @f469cb665f | display both on FWD-20 |
| Bloomberg account keeps mirroring Andrew until he reads FWD-20 | his 10-09 "for now ... eventually we will make rules but not yet" | unchanged |
| MCPINDEX: one short round; FWD-19 and FWD-11 stay parked | ruling @f469cb665f on "the three that matter" | seat `~MI` COO for it |
| Harvest for asset managers, V1 = derived layers + article links | ruling @f469cb665f; Andrew may widen | Z5 |
| NFRA_OPALAI and NFRA_MCPMSP park (not close) | his "does not really matter ... kind of not closed" | section 4 |
| COMM_ASSIST is the laptop's | his 144xZ words | handover taken by the laptop (@ed0110eedc); `2.0.0_SA_COO~CA` holds it |
| Dell boxes hold their own permissions; no cross-box CloudOps by default | his 131xZ words; Dell users joined the admin group (laptop ruling @d2f79ea8dd) | section 5 |
| Tailnet SSH: password login off | Andrew says done (174xZ item 3) | NFRA_CTLPLN round 12 reads it back; site Z only confirms its sshd |

### Open (Andrew's acts; put each on the site Z open-calls list with its rec)

1. **The MC Portal sitting (~10 minutes, one sitting):** read FWD-20 (MP-z-6), plus `sitez-20261009T173038Z-21c5` (open
   /control-plane, name one box's projects), `sitez-20261011T000025Z-8ed7` (open /control-plane and /open-calls, close one real
   call), `sitez-20261009T173040Z-f0d2` (sign in once as the Bloomberg account in a headed window to prove the owner gate refuses
   it). Schedule only after MP-z-5 is live.
2. **TO-GUARD-4 merge** (`sitez-20261013T021538Z-2da6`). REC yes: built and proved, the CRO recommends it.
3. **One Teams message to the Bloomberg account** (`sitez-20261009T170635Z-a519`): Andrew or any Opal colleague; the live test
   for Z6.
4. **FWD-11 (MCPINDEX), book the session with Alyssa:** stays parked; no ask this week.
5. **D12_PHONE_OTP_ALL_AWS toll-free verification fields:** parked; no ask this week.
6. **Staff read access to MC Portal:** later; he names staff when he wants it.
7. **Opal_Terminal key shut-off:** Andrew's condition ("as long as SITEZ does not use Opal_Terminal") reads TRUE as measured by
   `1.0.0_SA_CTO~DELL2` (one key, Active, LastUsedDate None, so never used by any machine). Site Z need only confirm, by a
   read of its own credential profiles, that nothing on site Z is configured with that key, and reply on the cross-box channel.
   The shut-off itself is recorded on dell2's record (Andrew in the console, or a seat without the Dell deny).

---

## 4. Per-project disposition

| project | disposition | seats | work this week | vs the site Z CRO rec |
|---|---|---|---|---|
| NFRA_MCPORTAL | DRIVE (centre stage) | `2.0.0_SA_COO~MP`, `0.7.0_AE_CloudOps~MQ`, workers | Z1 (MP-z-5 release incl. readability A1, MP-z-6 read), then Z2 FWD-21 addendum; mcportal source to GitHub DEV | agrees (KEEP) |
| NFRA_OPLGTW | DRIVE + RE-POINT | `2.0.0_SA_COO~O`, `0.7.0_AE_CloudOps~Z` | round 36 drains as cut (ship OG-bd-2); round 37 = Z3 feed cell + Z5 research grant + grade FWD-1..8; close on Andrew's FWD-20 read | agrees KEEP; re-pointed off upkeep |
| NFRA_MCPINDEX | ONE SHORT ROUND, then park | seat `2.0.0_SA_COO~MI` for the round; `0.7.0_AE_CloudOps~MI` | Z4 (tool-to-index links with depth and freshness; harvest/research rows); MX-s-19 read 10-19/20 | DIFFERS: CRO said PARK; Andrew named it one of the three |
| OPAL_BBGTML | KEEP + REGISTER HOME | `0.0.3_BG_BBGTerminal`; issuer named by `1.0.0_SA_CTO~Z` | Z6 read-only trace now; repair after; GUARD-4 merge on Andrew's word | agrees KEEP; adds the home |
| NFRA_OPALAI | PARK (not close), no seat | none | record today's Alyssa sitting if it happened, then park; its Bloomberg-agent check moves to Z6 | agrees (PARK) |
| NFRA_MCPMSP | PARK (status hold), no seat | none | nothing | agrees (PARK) |
| COMM_ASSIST | HANDED OVER to the laptop | laptop `2.0.0_SA_COO~CA` | close site Z's 2 calls as duplicates: `sitez-20261012T210024Z-288f` (= laptop row -44eb) and `sitez-20261011T030519Z-058e` (= laptop row -e435); no site Z PRD edits (the PRD is the laptop CTO's, cf. revert @3e2e99c57c) | CRO said KEEP on site Z; superseded by Andrew 144xZ |
| AMGT_HARVST (site Z leg; dell1 project) | KEEP at current pace ("can kind of continue along on its pace"), no added seats | `0.7.0_AE_CloudOps~ZW` (runner host lane) | runner upkeep only: the windowless runner fix for Z-S115 when dell1's round 84 cuts it; the WSJ/Barron's sign-in ask is WITHDRAWN (dell1, ~12:2xZ) | CRO said PARK; AMGT alignment says keep at pace |
| MDPF_DEMQUE (site Z leg; dell1 project) | KEEP (host for the drawer and the ledger upload) | `0.7.0_AE_CloudOps~ZQ` (no process since ~12:2xZ) | `0.0.0_AB_MSTR~Z` respawns ~ZQ on `2.0.0_SA_COO~Q1`'s ask, or t34 is re-cut; ledger `mdpf-demque-zq-t34-close` must not sit without a live lane | agrees (KEEP) |
| D12_PHONE_OTP_ALL_AWS | PARK | none | nothing; waits on Andrew's SP-1 fields | agrees (PARK) |
| D1_CATVIEWS | CLOSE the site Z order | none | flip TO-N1-DS terminal (issuer `2.0.0_SA_COO~Z`, or the D1/MDPF COO); the project's own status is not site Z's call | agrees (CLOSE) |
| ETFS_POSITIONING | CLOSE the stale orders | none | flip TO-13-DS and TO-14-AE terminal citing the 2026-08-29 repair | agrees (CLOSE) |
| NFRA_C3MATERIALIZE | CLOSE the orphan order | none | flip TO-L3S7A-CCY terminal citing the 2026-09-23 close | agrees (CLOSE) |
| NFRA_IAMROLES202609 | CLOSED (8/8) | none | verify the one linked worktree ledger `iamroles-r9-narrow-schwab.json` reads closed before that worktree is removed | agrees (CLOSE) |

Unowned scheduled tasks on site Z (site Z box report, closing section): `amgt-induction-daily` (rc 4 today) -> owner AMGT_RESAPP
on dell1 (AMGT alignment report, section 3.6); `OPAL_D7_ticket_intake` (rc 2, every 5 minutes) -> part of the Z6 trace;
`OPAL_vendor_watch` and the done one-shot `OPAL_restore_etf_daily_pull_20261009` -> owner not measured; the site Z CTO classifies
them by each script's register row.

Effort shift this produces (from the alignment report, section 6): MC Portal and MCPINDEX gain the work Andrew ranked first;
OPLGTW's next round serves the panel instead of hygiene. Parking OPALAI and MCPMSP frees no live seat (both COO lanes already
have no process).

---

## 5. Cross-box joins

| join | site Z side | other side | carrier |
|---|---|---|---|
| Harvest access (Z5) | catalog rows (MCPINDEX), principals and research grant (OPLGTW) | dell1 `1.0.0_SA_CTO~DELL1` names the servable harvest prefixes | one cross-box ask |
| Harvest runner (AMGT_HARVST) | runner host and `~ZW` | dell1 `2.0.0_SA_COO~W1` issues | existing cross-box orders |
| DEMQUE drawer and Bloomberg ledger upload | drawer host, `~ZQ`, the terminal | dell1 `2.0.0_SA_COO~Q1` issues | existing cross-box orders |
| Lent CloudOps capacity | 25 of 26 open cross-box items addressed to site Z are dell1/dell2 orders to site Z CloudOps lanes (site Z box report) | Andrew 131xZ: no cross-box CloudOps "in 99% of cases"; the Dell users now hold the admin group | keep a site Z lane on a Dell project ONLY where the act needs a site Z machine (the Bloomberg terminal, the harvest runner host); route every other Dell order back to that Dell's own CloudOps |
| COMM_ASSIST | close 2 duplicate calls; no further site Z work | laptop `1.0.0_SA_CTO`, `2.0.0_SA_COO~CA` | open-calls list |
| Tailnet SSH (NFRA_CTLPLN FWD-27) | key-only sshd, password off (Andrew says done), no external SSH or RDP except IT remote support | laptop `2.0.0_SA_COO~C` round 12 reads it back | the round-12 cell |
| Opal_Terminal key | confirm site Z holds no profile using it | dell2 record 163xZ | cross-box reply |
| Teams 502 on the gateway (OPLGTW E3) | the gateway route | COMM_ASSIST (laptop) is the consumer | a row in the OPLGTW channel; FYI to the laptop only if it blocks COMM_ASSIST |

---

## 6. Do not

- Do not build a second panel, a second gateway, or a merge of the two logins.
- Do not cut FWD-21 or any other MC Portal order ahead of FWD-20's release.
- Do not edit a live round's spec or decomposition (OPLGTW round 36 included); land changes at the next round-N analysis.
- Do not close NFRA_OPLGTW before Andrew has read FWD-20.
- Do not close NFRA_OPALAI or NFRA_MCPMSP ("kind of not closed"); park them.
- Do not serve raw publisher text (WSJ, Barron's, FT, Seeking Alpha) to asset managers in V1.
- Do not give the Bloomberg account its own rules before Andrew names them; it mirrors him "for now".
- Do not let the Bloomberg account answer or send to anyone outside `@opalinvest.com` (OPLGTW PRD v2.3 item 4).
- Do not pull Bloomberg data outside its queue, and do not modify `integrations/bloomberg/` beyond what Andrew lifted (GUARD-4
  waits on his word).
- Do not edit the COMM_ASSIST PRD or `project.json` on site Z; both are the laptop CTO's.
- Do not type a new AWS name or S3 address by hand: use `lib/opal_naming.py` (CLAUDE.md rule 30).
- Do not build an alert, alarm or monitor for any of this (standing moratorium).
- Do not message Alyssa (laptop CTO ruling @441f2f547d, cited in the site Z box report).

---

## 7. Required reading

Each path is given repo-relative (for any box) and as a laptop link (CLAUDE.md rule 33). Site Z's workspace root differs from the
laptop's (it contains a space): resolve the site Z form with `git rev-parse --show-toplevel` plus the repo-relative path.

1. Site Z voice memo: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/SITEZ_NFRA_REVIEW_TRANSCRIPT.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/SITEZ_NFRA_REVIEW_TRANSCRIPT.md
2. AMGT voice memo: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/AMGT_REVIEW_TRANSCRIPT.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/AMGT_REVIEW_TRANSCRIPT.md
3. Site Z alignment report: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/SITEZ_NFRA_ALIGNMENT_20261013.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/SITEZ_NFRA_ALIGNMENT_20261013.md
   (laptop Desktop copy: file:///C:/Users/AndrewBerman/Desktop/pivot_docs/02_alignment_reports/SITEZ_NFRA_ALIGNMENT_20261013.md)
4. AMGT alignment report: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/AMGT_ALIGNMENT_20261013.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/AMGT_ALIGNMENT_20261013.md
5. Pivot aggregate: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/PIVOT_AGGREGATE_20261013.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/PIVOT_AGGREGATE_20261013.md
6. Site Z box status report: `org/tier1_exec/4.0.0_SA_CRO/deliverables/BOX_STATUS_REPORT_sitez_20261013.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/BOX_STATUS_REPORT_sitez_20261013.md
7. Positioning ruling: `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md
8. Andrew's answers: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_174xZ_POSITIONING_CALLS_ANSWERED_ARTIFACT_AND_CLICKABLE_PATHS.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_174xZ_POSITIONING_CALLS_ANSWERED_ARTIFACT_AND_CLICKABLE_PATHS.md
9. Site Z seven rulings (10-12): `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md`
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md
10. MC Portal PRD (FWD-20 at :202-209, v0.7 addendum at :523-545): `org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md
11. OPLGTW PRD (v2.3 mirror addendum at :885-905): `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md
12. MCPINDEX PRD (FWD-1..19 at :118-282): `org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md
13. The 131xZ, 140xZ and 144xZ records: `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_131xZ_DELL_BOXES_GET_THEIR_OWN_PERMISSIONS_NO_CROSSBOX_CLOUDOPS.md`,
    `..._140xZ_FOUR_OPEN_CALLS_ANSWERED_DEVPLN_TAILNET_SSH_BDFEE_CTLPLN_SCOPE.md`, `..._144xZ_MUSE_DECISIONS_AND_COMM_ASSIST_TO_LAPTOP.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_131xZ_DELL_BOXES_GET_THEIR_OWN_PERMISSIONS_NO_CROSSBOX_CLOUDOPS.md
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_140xZ_FOUR_OPEN_CALLS_ANSWERED_DEVPLN_TAILNET_SSH_BDFEE_CTLPLN_SCOPE.md
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_144xZ_MUSE_DECISIONS_AND_COMM_ASSIST_TO_LAPTOP.md
14. Opal_Terminal key record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_163xZ_OPAL_TERMINAL_KEY_SHUT_OFF_IF_SITEZ_DOES_NOT_USE_IT.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_163xZ_OPAL_TERMINAL_KEY_SHUT_OFF_IF_SITEZ_DOES_NOT_USE_IT.md
15. Bloomberg, before any act: `integrations/bloomberg/READ_HERE.md`
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/integrations/bloomberg/READ_HERE.md

Note: the CRO alignment and box reports' repo copies were cited by the CRO at those paths; the laptop Desktop copies under
`pivot_docs` are byte copies made for the reboot (pivot_docs README).

---

## 8. First acts, in order

### `1.0.0_SA_CTO~Z`

1. Read sections 1 and 2 in full, and documents 1, 3 and 10 in section 7.
2. Confirm the MP-z-5 release carries the breakdown page AND the MP-z-2 readability amendment; when it is live, put the ONE
   MC Portal sitting on the open-calls list (section 3, open item 1) with Z7's one-line explanation attached.
3. Ship OG-bd-2 (the BD fee deny) at round 36's drain; then, at the round-36 analysis, cut round 37 to Z3 (cadence and backfill
   read) + Z5 (asset-manager research grant) + a grade of FWD-1..8.
4. Write the MCPINDEX one-round cut for Z4 (tool-to-index links with depth and freshness; harvest/research rows) and send
   `1.0.0_SA_CTO~DELL1` the one ask for servable harvest prefixes.
5. Give OPAL_BBGTML a register home and order the read-only Z6 trace now (DAPI, the 50/2 failures, the intake identity pin).
6. Record NFRA_OPALAI and NFRA_MCPMSP as PARKED (not closed), citing Andrew's memo.
7. Close site Z's two COMM_ASSIST calls as duplicates of laptop rows -44eb and -e435, citing the 144xZ record.
8. After FWD-20 ships: write the FWD-21 "control and depth" addendum (Z2) for `3.0.0_SA_CVO~Z` to sign.
9. Reply on the cross-box channel to dell2 on the Opal_Terminal key (section 3, open item 7) after the site Z credential read.

### `0.0.0_AB_MSTR~Z`

1. Seat `2.0.0_SA_COO~MI` for the one MCPINDEX round (it has no process).
2. Respawn `0.7.0_AE_CloudOps~ZQ` (no process since ~12:2xZ) when `2.0.0_SA_COO~Q1` asks, so ledger
   `mdpf-demque-zq-t34-close` has a live lane.
3. Push the mcportal source to `Opal-Capital/mcportal` DEV (Opal-internal; no word needed), so FWD-20's code is not on one box.
4. Review the 25 dell1/dell2 orders addressed to site Z CloudOps lanes: keep only those whose act needs a site Z machine (terminal,
   runner host); hand the rest back to the Dell box's own CloudOps under Andrew's 131xZ word.
5. Correct the stale register row: `org/devices/DEVICES.json` lists lane letter `Z` only for site Z (site Z box report).
6. Relay CLAUDE.md rule 33 (clickable paths, commit 0b8380acf8) to site Z's live seats once box-sync lands it.

---

## 9. Not measured here, and uncertainty

- **Read from the laptop checkout, not from site Z:** site Z work not yet on CLOUD is not seen (the alignment report read
  `box/laptop` @ec75ee1bef; this file read `box/laptop` at ~17:5xZ). Site Z's local worktrees and its mcportal checkout were not
  read.
- **Live page content:** `https://mcp.opalinvest.dev/control-plane` and `/routes.json` both answer 302 to Microsoft sign-in, so
  what the live pages render was not read.
- **Which gateway integrations are enabled live:** not read (8 packages exist in code: advi_billing, blackdiamond, globgrph,
  opal_discover, opal_portal, portal_index, schwab, ycharts, plus native Microsoft 365 tools).
- **Whether the Bloomberg account holds a grant-store profile today:** not read.
- **Whether asset managers hold gateway principals or work Claude accounts:** not read.
- **The staff accounts Andrew named** are auto-transcript renderings ("menopkin", "OSSA"); read the real principals from the grant
  store.
- **Commit-hour stamps** cited above (e.g. MP-z-4 at ~16:50Z) come from `git log` on the laptop, read at ~17:4xZ; site Z may have
  moved since.
- **AWS schedules for the per-family sweeps** were not counted; the 16:00Z and 12:15Z figures are the box report's.
- **OPLGTW rounds 24-34, and the OPALAI and MCPMSP PRDs beyond `project.json`:** not read by the CRO (alignment report, method).
