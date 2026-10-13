# DIRECTION PACKET -- dell1 -- 2026-10-13 (Andrew's voice memos, his answers, and the cluster ruling, in full)

## 0. Header

- **To:** `1.0.0_SA_CTO~DELL1` (rules and cuts) and `0.0.0_AB_MSTR~DELL1` (seats, relays, register carriers on dell1).
- **From:** `1.0.0_SA_CTO` (laptop, cluster lead), 2026-10-13 ~17:5xZ.
- **Status:** ACCEPTED. Andrew answered the positioning calls and asked that the box leads receive his words and direction "in full
  rich capacity versus solely just a light little directive, as I want to make sure these things are all done completely and
  correctly as I dictated" (Andrew, laptop terminal, ~17:5xZ).
- **Authority (every record this packet carries):**
  - the six voice memos of 2026-10-13 morning, of which three bind dell1 (AMGT, MDPF, ADVI), quoted in full in section 1;
  - `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md` (@f469cb665f,
    flipped to ACCEPTED @0b8380acf8);
  - `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_174xZ_POSITIONING_CALLS_ANSWERED_ARTIFACT_AND_CLICKABLE_PATHS.md`
    (@0b8380acf8);
  - `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261013_131xZ_DELL_BOXES_GET_THEIR_OWN_PERMISSIONS_NO_CROSSBOX_CLOUDOPS.md`;
  - `org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md` and the
    CTO ruling @d2f79ea8dd (the Dell agent users join `AdministratorAccessOpalCapital`; three deny classes kept);
  - `ANDREW_DIRECT_20261013_134xZ_LAPTOP_PARE_DOWN_UNSEATED_CLOSES_EXCEPT_SPMOVE.md` (dell1 section: six closed projects; the
    LGIC_ENFORCE gate owner is NFRA_CTLPLN);
  - `ANDREW_DIRECT_20261013_140xZ_FOUR_OPEN_CALLS_ANSWERED_DEVPLN_TAILNET_SSH_BDFEE_CTLPLN_SCOPE.md` (call 1: the whole-DEV portal
    promote holds until NFRA_DEVPLN lands);
  - the CRO pivot aggregate and the AMGT, MDPF and ADVI alignment reports
    (`org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/`, @d737bd0ed1). Every state claim below that is not
    re-read here carries its source from those reports.
- **How to use this packet:**
  1. Read sections 1 and 2 IN FULL before cutting anything. Section 1 is Andrew's own words; section 2 turns them into outcomes.
     When this packet and his words differ, his words win, and you file a surprise row naming the difference.
  2. Mid-round, the spec and the decomposition are FROZEN (CLAUDE.md rule 27). Every re-point here lands at that project's NEXT
     round-N analysis (the CTO's L10) or as a PRD addendum, never inside a live round. A live round drains as cut.
  3. The box CTO rules what touches only dell1. A cross-box item (section 5) goes through `0.0.0_AB_MSTR` on the laptop.
  4. Every path you post to Andrew is ctrl+click accessible (CLAUDE.md rule 33, @0b8380acf8): an absolute `file:///` URI or a
     markdown link to one, plus the repo-relative form when it crosses boxes.

---

## 1. Andrew's words in full

The three transcripts below are copied whole from
`org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/` (auto-transcripts, verbatim; only non-ASCII punctuation in the
headers was converted to ASCII). Transcription errors are kept as spoken: "DEM QE"/"DEM QUE"/"D-E-N-Q-U-E" = MDPF_DEMQUE; "Tainin"/
"Cainan" = MDPF_CANON; "Y-chart"/"white charts" = YCharts; "BV price"/"BVPRCE" = ADVI_BDPRCE; "open AI calls" = model calls (see 1.4,
answer 5); "cloud" (end of AMGT) = Claude; "open gateway" = the Opal gateway.

### 1.1 AMGT (Asset Management) memo -- verbatim

#### AMGT Review -- Voice Memo Transcript

- **Source audio:** AMGT_REVIEW.m4a
- **Recorded:** October 13, 2026 (morning)
- **Speaker:** Andrew Berman
- **Recipient:** MSTR on cloud-local (via Taildrop)
- **Note:** Auto-transcript, delivered verbatim. Acronyms as spoken; AMGT = Asset Management, DEM QE / MDPF_DEM QE = data-quota polling project, Opal Data Harvest folders.

---

I'd like to go through some of our highest priorities here. So there are a lot of projects actively being run. I'm going to handle them for the most part on each individual device because sometimes we just need to get really into the weeds very quickly here. So I've been running around for the last two hours since about 9 a.m. Eastern today on October 13th, 2026 to move these along where possible. But I want to ideally have a mechanism for managing this on the control plane. I don't think that we need to build anything new for this. I simply just want to bring you as the CTO of the cloud dashboard, go laptop box up to speed on what needs to happen here. So we can make the allocation decisions needed to accelerate our high profile wins that we need to happen. And potentially deprioritize some of the lower impact items. So moving through the macro groups, I will start with the AMGT that is the asset management. So we want to get this project up with the ability for the asset managers to access all of this data easily. And ideally, we have the functional web application, the security analysis page with all of the relevant information available there. But if that is going to take too long, if we are too far away from that outcome, like for example, if that's held up on certain backfill elements, which are dependent on the DEM QE project, MDPF underscore DEM QE, if we need to assess really what needs to happen to at least get the 93 research pages completely loaded in here, we need to make sure that all information is displaying correctly that the user interface is clean and easy to use, that the pages load fast, that we, which I believe we should have handled already. But yeah, we want to make sure that at least this page is usable. And so one of some things that I can think of immediately off the top that we want to implement here is that there are a lot of cases where a, their may or may not be immediately obvious in available executive management, for example, or some of the thesis stuff is hard to weigh. There are various things are hard to weigh. And I essentially want to fill in these gaps with dedicated, open AI calls that do the AI analysis to fill out obvious text sections. So that would be getting the, an executive management bio summary. So like any recent developments on the executive management, we would want that to surface. So that probably just going to be a web search. And the premise here is that no matter what data that we have for any of these given pages, some are going to have more complete data than others, we want to be able to display information for all of them. And we want to be able to fill out these key text sections for all of them. So that what that looks like is whatever we were able to get, use from our, our, our, embedded sources, whatever we were not able to get, uh, dedicate to web search and just, that's how we fill out some of these, the high profile blocks on the asset management web app. And separately, we need to figure out the, open gateway mechanics for how to connect the, uh, the various, open dash data dash harvest folders, uh, and set up the MCP index for that bucket. How to set that up quickly and easily so that the asset managers can use that with their cloud. So that those are the all the high priority items for the AMGT segment, uh, harvest, the design, everything else can kind of continue along on its pace. But the point is that we need to close these out. We need to close at least a functional V1. So that's how I would break out this AMGT, uh, into, yeah, what we need to do to get the web functioning, what we need to do to get the Opal data harvest folders accessible for the asset management research team. Now I'm going to move on to the next transcript, which will be focused on the various, uh, MDPF macro items.

### 1.2 MDPF (Market Data Pipeline Framework) memo -- verbatim

#### MDPF Review -- Voice Memo Transcript

- **Source audio:** MDPF_REVIEW.m4a
- **Recorded:** October 13, 2026 (morning)
- **Speaker:** Andrew Berman
- **Recipient:** MSTR on cloud-local (via Taildrop)
- **Note:** Auto-transcript, delivered verbatim. DEMQUE / DENQUE = DEM QE data-quota polling project; SEC HIST = security history; HILGAP = HIL-GAP; STRATID = strategy ID; SEC CLASS = security classification.

---

Now moving through the MDPF items, the DEMQUE, I am handling that on the Dell 1 device. So this I think is going to be gating a lot of our objects here because we need to be able to have a standard card which the Dell 1 device is already put together, which effectively covers a 1 through 7, the various needs, depth, breadth, et cetera for these various polls where they sit in priority and so on because we need to make sure that backfill is moving conclusively across the board here. Something else that we need to examine specifically for this project is that we have access to Y-chart. So we should do a little bit of digging on the HAR file side, do some network traffic recording to see what exactly lives here, what exactly endpoints Y-chart has because the truth of the matter is that Y-chart's may be a more viable source than Bloomberg and Y-finance for getting a lot of this information together and the cost and the quota for pulling information from Y-chart is non-existent cost and thus far we have not seen any quota limits on it. So this is something that we're going to want to explore. It may be a separate project but we'll directly feed into the D-E-N-Q-U-E project. Now moving on through the rest of the items here, it seems like SEC history or security history, SEC H-I-S-T may need to understand if that's done if we can close that out. Tainin, M-D-P-F under score, Tainin, we need to establish where that's at, what we need to do to continue that process forwards. H-I-L-G-A-L-G-A-P, that seems like it's most we've done, strategy, ID, ST-R-A-T-I-D, that project seems for the most part done. The SEC class, security classification seems like the largest one and this is an ongoing project and it relates directly to mechanisms in H-I-L-Gap and otherwise because as information is coming in through various channels which we will qualify further in D-E-N-Q-U-E. We need to establish how these are being classified, how they're coming in. We already know how they're being classified in the sense that we have our format and use go to the ETF classifier table in AWS. But this is probably going to be something that may be an add-on to, or at least highly related with D-E-N-Q-U-E. How on a daily basis, the various surfaces which are qualified, all the 17 surfaces are qualified in D-E-N-Q-U-E. How we are handling those for SEC, CLA-S-S, for the security classification project. So for the MDPF project, the highest priority ones I can see here are making sure that Cainan proceeds making sure that we have a synchronized synergistic flow between the D-E-N-Q-U-E data-Colda polling and the SEC class security classification polling because those two are highly related as well as exploring how we can potentially walk and translate white charts and their backend into a data-poled source potentially could be a great substitution for some of these processes and free up some of that Bloomberg quota.

### 1.3 ADVI (Advisor Intelligence) memo -- verbatim

#### ADVI Review -- Voice Memo Transcript

- **Source audio:** ADVI_REVIEW.m4a
- **Recorded:** October 13, 2026 (morning)
- **Speaker:** Andrew Berman
- **Recipient:** MSTR on cloud-local (via Taildrop)
- **Note:** Auto-transcript, delivered verbatim. ADVI = Advisor Intelligence; BVPRCE = Black Diamond pricing; COT BKF = Cottonwood backfill.

---

Now we're going to move through the ADVI, the Advisor Intelligence Macro, AdV. We've there are four projects I can see in here. The firm buckets, the BV price or buck diamond price, the cottonwood backfill, the COT, BKF and the billing project. So starting from the top firm buckets, that is obviously if peak importance, we want to make sure that we have locked that in. And that it's working synergistically with the existing setup that we have a clear plan for the migration to these buckets, including all current operating functions that run for Advisor Intelligence, as well as a decommissioning plan for legacy buckets and legacy operations that will no longer be necessary after this is successful. So you want to stay on top of that. The BVPRCE, the Black Diamond pricing, I don't really understand where we're at or the purpose of that. That's a new project that needs to be explored. The cottonwood backfill, COT, BKF. So cottonwood has a backfill to 2013. We're working through this with the MDPF, DEM, QUE, the data quota Q project. Because the truth of the matter is with cottonwood backfill, these goes back to 2013. We want to make sure that any active account has backfill for its various securities that have any securities that have been held for the period that they were held. And how we maintain the pricing of these active securities on a daily basis per account. So that is a whole function that needs to be taken care through DEM QUE. But again, we're throwing back the DEM QUE for securities that were held by a client accounts that no longer are even active. This we don't need to waste quota on this stuff. This is a deep, deep, deep, pistorical priority. Something that we will cross when all of our other needs are taken care of. The issue, the reason I bring it up here is because I want to make sure that there's some clear matching mechanism through whatever mechanism that the Commonwealth backfill data, which clearly all of these accounts are from fidelity or the most of them are, that we're able to match those through to the black diamond repository and the black diamond information. Because if we are not able to adequately match these to the various files, then we don't know what is an arc of all accounts. So that's something I want to make sure is clear that we're able to be efficient with our data quota. Moving on to the billing. So something that we need to clarify here is that a lot of billing information. We need to establish what billing information we've already carved out pathways for because you will notice that on the advisor intelligence page, we do track quarter-to-date year-to-date and max billing from the various firms. We've already built out functions for that. So we don't want to duplicate work here. We want to make sure we're being synergistic in our efforts and not duplicating or re-treading old grounds. So this is just something that I want to bring up there because there are existing UI pipelines for houses displayed to the client and there's clearly existing mechanisms for getting this. Obviously the purpose of the billing project is that we want to be able to figure out how we handle this from the custodian level data, not so we relying on black diamonds. So there's fertile grounds there to explore, but that's what we want to cover there.

### 1.4 Andrew's later answers that bind dell1 (verbatim where he wrote them)

From `ANDREW_DIRECT_20261013_174xZ_...` (~17:4xZ), answering the cluster ruling's seven calls:

> "5.) We can use anthropic path, that's fine. 6.) Yes that is fine, it is loading quite quickly for AMGT already but worth
> exploring the individual security pulls."

> "4.) I do not know what these items are, and mockadv is almost certainly deprecated/useless/not displayed anywhere."
> (call 4 = the ADVI_FIRMBKTS decisions; re-asked with the plain explanation in section 3.)

What those answers and the ruling settle for dell1:

1. **AI fill provider:** the EXISTING Anthropic path (the code and key already in `lib/research/`, with the Anthropic server-side
   web search tool). Not OpenAI.
2. **"Load fast" number:** under 3 s for the FIRST request of the day on PROD (the warm path is already about 1.3 s). Andrew adds
   that the page already loads quickly for him and that the individual security pulls are worth exploring: measure what each name
   pulls and how long each pull takes.
3. **Security Analysis PROD promote:** the page is staff-only (route `requireInternal`, dell1 box status report line 471), so the
   push law needs no word from Andrew for it (CLAUDE.md, Agent Autonomy; `ANDREW_DIRECT_20261009_044xZ_*`). **Read this condition
   carefully:** what needs no word is a release that changes ONLY Opal-internal pages. Open call `dell1-20261011T033643Z-e7f2` as
   recorded is a whole-DEV promote that also carries two CLIENT-FACING changes (Model Portfolios `/portfolios`, MDPF_CANON CN-d-3;
   Advisor Intelligence fee panel, ADVI_BILLING) per
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/E7F2_PORTAL_DEV_NOT_ON_PROD_BREAKDOWN_20261011.md` lines 7-13. Andrew answered e7f2
   "NO for now" on 2026-10-11 (`ANDREW_DIRECT_20261011_161xZ_..._E7F2_NO_14A_YES.md` line 13), and on 2026-10-13 ~14:0xZ ruled that
   the whole-DEV promote holds until NFRA_DEVPLN lands (140xZ record, call 1). So: promote the Security Analysis work as ONE
   FEATURE cut from the last PROD release (NFRA_DEVPLN C-FEATURE, `org/missions/D0/NFRA/NFRA_DEVPLN/prd/NFRA_DEVPLN_PRD.md`
   line 108), approved by the dell1 box CTO as Opal-internal (DEVPLN decision (b), 143xZ record), with a push receipt naming every
   page changed and its class. Never the live DEV whole. The `AdvisorBookFeePanel` never rides it.
4. **Former Cottonwood clients:** EXCLUDED from every vendor draw (Bloomberg and Yahoo), not ranked last. His memo: "we don't need
   to waste quota on this stuff. This is a deep, deep, deep, [historical] priority."
5. **YCharts:** a separate small project that feeds DEMQUE ("It may be a separate project but we'll directly feed into the
   D-E-N-Q-U-E project"). The laptop CRO writes its L1 brief; the dell1 CTO is its L2 consumer and its host box.
6. **Harvest for asset managers, V1:** derived layers (packs, chatter, scores, management, filings outputs) and article links
   only, not raw publisher text. Andrew may widen this.
7. **Billing:** custodian-computed fees feed the EXISTING Fee Summary panel; no second panel on PROD ("we don't want to
   duplicate"). ADVI_BILLING is dell2's; dell1's leg is only that no dell1 promote carries the second panel.
8. **DEMQUE depth:** stays with Andrew's own dell1 session. His words: "the DEMQUE, I am handling that on the Dell 1 device."
   This packet does not re-ask or pre-empt his depth pick.

---

## 2. Outcomes Andrew dictated (dell1)

Order of work on dell1 (his ranking, as measured in the alignment reports): AMGT V1 page and AI fill first; FIRMBKTS lock-in and
plan; MDPF (CANON proceeds, DEMQUE card and backfill, the DEMQUE<->SECCLASS sync, YCharts); then closes. Harvest collection and
design "continue along on [their] pace".

### O1. Security Analysis V1: all 93 names complete, correct, clean and fast

- **His words:** "at least get the 93 research pages completely loaded in here, we need to make sure that all information is
  displaying correctly that the user interface is clean and easy to use, that the pages load fast"; "We need to close at least a
  functional V1."
- **DONE WHEN (as Andrew would see it):** an analyst opens any of the 93 names on PROD Security Analysis; the first request of the
  day returns in under 3 s; every section shows content or a stated reason; nothing renders a raw code or a broken value.
- **Proof read:** (a) a per-name completeness census over the 93: for each name, each section filled or its reason, read from the
  PROD-served payload; (b) a cold-start timing read on PROD at the first request of a trading day; (c) a per-security pull census:
  for each name, which pulls it makes (corpus, filings, management, news, price, scanner) and the time each takes -- Andrew's added
  ask; (d) a browser walk of a sample on PROD (`/ui-walk` or `/frontend-dev`), screenshots read.
- **Owner:** AMGT_RESAPP, `2.0.0_SA_COO~R1` with `0.7.0_AE_CloudOps~RA1`; rulings `1.0.0_SA_CTO~DELL1`.
- **Measured state:** live on portal PROD 37aa1247 (2026-10-09), staff-only (dell1 box status report lines 471, 519). Cold first
  overlay 20.05 s, warm about 1.3 s (`AMGT_RESAPP/ledger/ROUND_ANALYSIS.round101.md` @067d69e91b, per AMGT alignment line 44). Round
  101's cold overlay was attributed: "feed 18,796 ms of 20,566" (round 102 L8 packet, commit @aa2314ca47). Officer list non-empty on
  93 of 95 names (round 77). `s3://opal-data-harvest/packs/` holds 105 per-name prefixes (live read 2026-10-13, AMGT alignment).
  Round 102 work: per-phase log lines and the steady-state read. Newest commit on the price axis: TWR pricing on every surface
  (@bd2bd6722e).
- **Gap:** no census of the 93; no cold-start remedy (only instrumentation); the promote is mis-recorded as waiting on Andrew; the
  population is unpinned (93 folders, 95 covered names, 105 pack prefixes). Ruling: **V1 = the 93** (AMGT_CORPUS FWD-19's
  population), the rest reported beside it.
- **Box CTO's act:** at the round-102 L10, re-point RESAPP from instrumentation to three V1 cells: (1) the promote of the Security
  Analysis feature (section 1.4 item 3); (2) the 93-name census plus the per-security pull census; (3) a cold-start remedy brought
  under 3 s (the feed phase is named as the cost; fix it, or keep one instance warm, the cheaper that meets the number). Close the
  stale qq-2 order (round 92, worker gone; dell1 report line 501). The scanner-currency slice (`AMGT_RESAPP-S14-CRNCY-SCANNER-US`,
  gating bh-5/pp-4) is NOT a V1 gate: drop it from V1 or place it on the DEMQUE form Andrew is working; do not hold V1 for it.
  Give the failing site Z task `amgt-induction-daily` (rc 4 on 2026-10-13, no owner; sitez report lines 689-690) to RESAPP.
- **Order:** first.

### O2. AI fill of thin text sections, for all 93

- **His words:** "fill in these gaps with dedicated ... calls that do the AI analysis to fill out obvious text sections. So that would
  be getting the, an executive management bio summary. So like any recent developments on the executive management, we would want
  that to surface. So that probably just going to be a web search"; "whatever we were able to get, use from our ... embedded
  sources, whatever we were not able to get, uh, dedicate to web search"; "we want to be able to display information for all of
  them."
- **DONE WHEN:** for every one of the 93, the Executive Management tab carries a management bio summary and a recent-developments
  block, and any other thin high-profile text block (the hard thesis items) is filled. Each is built from Opal sources where they
  exist, else from a web-search-backed model call on the existing Anthropic path, cited, and marked as machine-written (RESAPP
  FWD-9 marking).
- **Proof read:** a census of the 93 showing, per name and per block, the source class (Opal source / web search / none with
  reason) and the citation; a sample read on PROD by the CVO for correctness of five names.
- **Owner:** AMGT_RESAPP, by a PRD addendum (new FWD). Seats: `~R1` and the dell1 COO seats freed in section 4.
- **Measured state:** no outcome covers a bio summary, management recent developments, or a fill for every name (RESAPP PRD
  :491-1092 per AMGT alignment line 44). Model-call code exists for the filings thesis (`lib/research/filings/analyze.py`), the
  posture judge (`lib/research/posture/judge.py`) and the CEO search (`lib/research/management/ceo_search.py`), all Anthropic. The
  roster with tenure is FWD-17. The site Z batch tasks `OpalResearch-ExecManagement` and `OpalResearch-FilingsAnalyzer` are
  DISABLED (sitez report lines 49-50). Harvest news is a natural recent-developments source (AMGT alignment line 68).
- **Gap:** the outcome, the producer and the batch run.
- **Box CTO's act:** write the RESAPP PRD addendum (L10 addendum; the CVO signs the changed ratified-text half). Reuse
  `ceo_search.py` and the FWD-9 marking (build ladder step 2). Decide whether the disabled site Z tasks are re-enabled or replaced;
  a site Z producer path needs `1.0.0_SA_CTO~Z`'s half (dell1 report line 636 states that rule).
- **Order:** second, in parallel with O1 on a separate seat.

### O3. Harvest folders reachable by asset managers from their own Claude, through the gateway

- **His words:** "figure out the, open gateway mechanics for how to connect the, uh, the various, open dash data dash harvest
  folders, uh, and set up the MCP index for that bucket. How to set that up quickly and easily so that the asset managers can use
  that with their cloud."
- **DONE WHEN:** an asset manager, in a work Claude account, asks about a covered name and gets that name's pack and chatter from
  `opal-data-harvest` through the gateway, scoped to research data only (derived layers and article links, section 1.4 item 6).
- **Proof read:** a live gateway call by an asset-manager principal returning harvest data, plus a negative arm (the same principal
  refused raw publisher text, and a non-research principal refused harvest).
- **Owner:** the build is SITE Z's (NFRA_MCPINDEX catalog rows; NFRA_OPLGTW principals and grant). **dell1's leg:** the list of
  servable prefixes, owned by AMGT_HARVST `2.0.0_SA_COO~W1` with RESAPP for the packs.
- **Measured state:** `opal_discover` returns `catalogued: false` for "harvested news articles and chatter" and "security analysis
  research pack" (live read 2026-10-13; positive control "Schwab account positions" returned 8 datasets). 24 top-level prefixes in
  the bucket (amgt, packs, management, filings, seeking-alpha, wsj, barrons, ft, ...). MCPINDEX is parked; its PRD has 0 harvest
  mentions; OPLGTW's charter is Schwab and Black Diamond (AMGT alignment lines 49-50).
- **Box CTO's act:** produce `SERVABLE_PREFIXES` for `opal-data-harvest`: each prefix, its content class (derived vs raw publisher
  text), and serve/withhold under the V1 rule. Send it to site Z through `0.0.0_AB_MSTR` as the input to their MCPINDEX round.
- **Order:** third; the prefix list is small and can go out this week.

### O4. AMGT_HARVST continues at its own pace

- **His words:** "harvest, the design, everything else can kind of continue along on its pace."
- **Act:** KEEP, no added seats; scope to runner upkeep and the WSJ/Barron's sessions (bz-5/bz-6/bz-7 at site Z). Close the stale
  bo-1/bp-1 orders and the open bs-3 ledger, and reprint the FWD board, whose denominator is 18 (dell1 report lines 560-563). The FT
  hold stands on Andrew's word. The WSJ/Barron's sign-in ask is WITHDRAWN (dell1 report line 583).

### O5. MDPF_CANON proceeds

- **His words:** "making sure that Cainan proceeds"; "we need to establish where that's at, what we need to do to continue that
  process forwards."
- **DONE WHEN (this week):** FWD-3 graded on the first served Global fold; round 7 (frontier account counts) issued.
- **Measured state:** 2 of 8 REALIZED (FWD-1, FWD-7). The FWD-3 Global min-firms fold was DEPLOYED 14:05Z 2026-10-13
  (@eb50646475). Round 7 drafted, not issued (@964a025a44). FWD-2/4/6/8 wait on ADVI_FIRMBKTS per-firm router flips; FWD-5 on the
  M10/M12 un-park (MDPF alignment line 45). The register is stale: `project.json` phase says "none is seated" while a COO
  (`2.0.0_SA_COO~D1`) has run rounds 1-6, and `blocking` cites LGIC_NAMING-S7 although LGIC_NAMING is register-complete (MDPF
  alignment lines 107-111).
- **Box CTO's act:** grade FWD-3 on the next 13:30Z fire; write the round-6 L10; issue round 7; fix the register lines. The
  `/portfolios` PROD push is CLIENT-FACING and waits on Andrew's word: carry it to him as a card with the before/after, after FWD-3
  grades.

### O6. MDPF_DEMQUE: the standard card for every item, and backfill moving

- **His words:** "we need to be able to have a standard card which the Dell 1 device is already put together, which effectively
  covers a 1 through 7, the various needs, depth, breadth, et cetera for these various polls where they sit in priority and so on
  because we need to make sure that backfill is moving conclusively across the board here."
- **DONE WHEN:** the 7-field card (who uses it, priority, history depth, field breadth, securities, schedule, budget) is answered for
  all 17 qualified request ids, and Bloomberg draws resume inside Andrew's two-week quota budget.
- **Measured state:** 17 distinct request ids (10 Bloomberg, 7 Yahoo) over 5 surfaces (A production daily, B client history, E Opal
  ad-hoc, C product history, D research) in
  `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/QUEUE_QUALIFICATION_20261013.md`. Andrew's form:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md`. The dell1 CTO's form commits today: A5 approved as
  is (5-day exception) and surface B Bloomberg by default with Yahoo only after a 10 bps porting test (@c59326e5ed); the porting test
  sized (326 landed, 1.2 days; 965 requested, 3.6 days) (@2fd11bb891); TWR pricing on every surface as a standing rule (@ce8a5c5cec).
  CARD-A P1 income rows (11,154 across 556 of 606 names) and option C re-priced with a total-return field to 24 days (@54a77c0e82).
  Yahoo incremental path built and proved cell-equal, nothing wired (@9de742d8f9). No new Bloomberg draw starts until the form is
  complete (CTO msg 4892, MDPF alignment line 61). 1 of 9 FWDs REALIZED.
- **Ruled here:** former Cottonwood clients are EXCLUDED from every draw. `rank.py` (DQ-t-13) today ranks "P3 gone" last; it must
  REFUSE P3 until Andrew lifts the exclusion, and P2 (match open) draws only after its match resolves (ADVI alignment line 32 and
  question 1). P1 draws window to each account's held dates, using the active-account set dell2 builds (section 5).
- **Not ruled here:** the CARD-A P1 depth cut. Andrew is working it in his dell1 session. Note for him: the CRO's REC (option D,
  13 days) was priced before option C was re-priced at 24 days (@54a77c0e82); present the current prices.
- **Box CTO's act:** finish the card for the remaining items (A1 models pull, A4 constituents, the B, C and D items); land the `rank.py`
  P3 refusal as a cell; settle who owns TO-DQ-t34 at site Z (its lane has had no process since ~12:2xZ on 10-13 and the two box
  reports name different owners; MDPF alignment lines 104-106) with `1.0.0_SA_CTO~Z` through MSTR.

### O7. DEMQUE <-> SECCLASS synchronized

- **His words:** "making sure that we have a synchronized synergistic flow between the D-E-N-Q-U-E data-Colda polling and the SEC
  class security classification polling because those two are highly related"; "How on a daily basis, the various surfaces which
  are qualified, all the 17 surfaces are qualified in D-E-N-Q-U-E. How we are handling those for SEC, CLA-S-S"; "we have our format
  and use go to the ETF classifier table in AWS."
- **DONE WHEN:** a security entering through any of the 17 DEMQUE items gets its row in DynamoDB `etf-classifications` on
  SECCLASS's scheduled path (SECCLASS FWD-7/10/11), and DEMQUE's unresolved list (FWD-5) uses the same identity key. One real new
  security is traced from a DEMQUE draw to its classification row.
- **Measured state:** DEMQUE's PRD BOUNDARY "Relies on and does not own: MDPF_SECCLASS and the resolvers (identity)"; the SECCLASS
  PRD names DEMQUE 0 times; the queue form has 0 classification mentions (MDPF alignment lines 97-103). Both projects sit under one
  CTO, so no merge is needed.
- **Box CTO's act:** one CONTRACTS row in EACH PRD (the same rule, stated from both sides) and one cell in each project's next
  round: SECCLASS's cell proves the classification of a DEMQUE-entered security; DEMQUE's cell proves the shared identity key.
- **SECCLASS scope this week (agrees with the dell1 CRO):** narrowed to the Black Diamond thread (the e97b read-back, FWD-1 close),
  plus a full 17-FWD board at the round-24 L10 (none printed since round 9). Its client-facing BD Mix restated-history push waits on
  Andrew's word after tonight's 23:00Z acceptance read. SECCLASS is the largest spend on dell1 (697 commits in 7 days, 90 worker
  slots, 283 surprise rows; MDPF alignment line 140) for an item Andrew ranked behind the sync: hold its other FWDs uncut until
  the board exists.

### O8. YCharts as a quota-free source (new small project)

- **His words:** "we have access to Y-chart. So we should do a little bit of digging on the HAR file side, do some network traffic
  recording to see what exactly lives here, what exactly endpoints Y-chart has because the truth of the matter is that Y-chart's
  may be a more viable source than Bloomberg and Y-finance ... the cost and the quota for pulling information from Y-chart is
  non-existent"; "exploring how we can potentially walk and translate white charts and their backend into a data-poled source
  potentially could be a great substitution for some of these processes and free up some of that Bloomberg quota."
- **DONE WHEN (step one):** YCharts coverage of DEMQUE's 17 items is measured, item by item, with the CUSIP-level fixed income of
  CARD-A P1 (370 fixed income and 227 cash-equivalent names of 606) called out. **Step two:** a DEMQUE PRD addendum adds YCharts as a
  third metered vendor only where coverage is proven.
- **Prior art to reuse (do not redo a fresh HAR study first):** YALP_MDSRC, closed complete 2026-05-22: about 40 internal endpoints
  from 3 recorded browser sessions (`docs/briefs/mdsrc-ycharts-internal-api-20260520.md`,
  `docs/briefs/mdsrc-a5-ycharts-har-endpoint-assessment-20260521.md`); 72 of 76 indices, bond indices, commodities and ETFs
  replaceable with 11.7-96.4 years of daily depth (`docs/briefs/mdsrc-wsa-ycharts-history-verification-20260521.md`); Bloomberg
  matched to the cent on 42 of 71 (`docs/briefs/mdsrc-d2-ycharts-bloomberg-comparison-20260522.md`). Three Lambdas deployed and
  dormant since 2026-05-22: `ycharts-market-data-pull`, `ycharts-session-capture`, `ycharts-session-probe`. The gateway client
  `infra/aws/ec2/opal-gateway/app/integrations/ycharts/client.py` shares the endpoint contract and the one session secret. Session
  live: `ycharts_freshness` ok, HTTP 200, 16:57Z 2026-10-13 (MDPF alignment lines 75-90). A new HAR capture is in scope only for
  item classes the old map does not cover.
- **Risk to carry into the brief:** the limit seen so far is eviction of the ONE shared session (403 seat evictions), not a call
  quota. A heavy draw could evict the session the gateway and IRPT use. A pacing rule comes before any bulk draw. On dell2, IRPT_YCDGEN
  aims for "Opal stops calling YCharts" for reports; that is the report generator, not market data, but both use the same session.
- **Owner:** L1 brief by the laptop `4.0.0_SA_CRO`; L2/L3 by the cluster CTO; host dell1, consumer `1.0.0_SA_CTO~DELL1`.
- **Box CTO's act:** none until the brief lands; then seat it on a freed COO seat (section 4).

### O9. Close checks: HEALGAP, SECHIST, STRATID

- **His words:** "SEC history ... may need to understand if that's done if we can close that out"; "H-I-L-G-A-P, that seems like it's
  most we've done"; "strategy, ID ... that project seems for the most part done."
- **MDPF_HEALGAP:** 5 of 6 REALIZED (round-3 analysis and ADDENDUM 1, @f19cedfddc); round 4's close packet: 2 of 2 orders complete,
  HG-t-16 applied and served, MAY-CLOSE (@ed0b90d567). Act: close the round-4 deploy ledger, the CVO's L8 and the CTO's L10 grade
  FWD-6 (20 rows over 164 scheduled pulls, 7 exposed to manual action), then CLOSE. The seat `2.0.0_SA_COO~G1` is freed.
- **MDPF_SECHIST:** NOT done: 1 of 9 REALIZED (MDPF alignment line 48). The Bloomberg pull landed 14:39:56Z (@3423a70a32), so the
  Terminal sign-in blocker in the dell1 report (line 243) is cleared. Act: the CVO grades once; then PARK the seat
  (`2.0.0_SA_COO~H1`) and, at the next DEMQUE and SECCLASS L10s, fold FWD-2/4/5/7 into DEMQUE and FWD-6/8 into SECCLASS; FWD-9 (the
  money-market rule) is its only distinct item. Close after the fold.
- **MDPF_STRATID:** 1 of 7 graded; FWD-2/6/7 measured on the 10-12 fire but ungraded; all 12 orders complete; FWD-3 waits on call 203a
  (Muni sleeve under ALT Strategies; REC yes, matching Andrew's 10-08 wording "SMA strategies Tax and Muni under ALT Strategies").
  Act: one L8/L10 grading pass (FWD-2/6/7 graded, FWD-3/4/5 dispositioned); CLOSE if met, else PARK. The seat `2.0.0_SA_COO~S1` is
  freed either way.

### O10. ADVI_FIRMBKTS: locked in, with a migration plan for every operating function and a decommission plan

- **His words:** "firm buckets, that is obviously if peak importance, we want to make sure that we have locked that in. And that
  it's working synergistically with the existing setup that we have a clear plan for the migration to these buckets, including all
  current operating functions that run for Advisor Intelligence, as well as a decommissioning plan for legacy buckets and legacy
  operations that will no longer be necessary after this is successful. So you want to stay on top of that."
- **DONE WHEN (this week):** (a) the 49 Financial cutover closed (round 7: FWD-1 graded on reader 2; FB-j-3 closed on the first
  chain's WARN text; FB-j-4 region fix and FB-j-7 exec-summary regeneration landed under their signed pairs); (b) ONE written plan
  document: per firm (Inflection, Cottonwood), every Advisor Intelligence operating function (gold chain, exec-summary generator,
  IRPT Lambdas, edge functions, schedules, notifications), the order of moves with a rollback per move, each legacy bucket's
  decommission (the 45-day quiet window, FWD-6), and each legacy OPERATION to retire.
- **Measured state:** 49 Financial platinum moved to `opal-data-49financial` (49,231 keys; 8 of 8 IRPT Lambdas and 3 edge functions on
  the flipped build; dell1 report line 111). 0 of 8 REALIZED; FWD-1 and FWD-4 PARTIAL (`ledger/ROUND_ANALYSIS.round6.md`
  @1c1189d82b). 158 client exec summaries about five months stale until FB-j-7 (dell1 report line 106). Inflection and Cottonwood
  not started. The PRD disowns legacy operations: `FIRMSEP-s3-direct-access-bypass` "its fate is not this project's to rule"
  (`org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md` lines 227-229), and `inf-canonical-prices-daily` stays disabled and
  held (line 226). The dell1 report lists `andrew_acts: []` (line 98) although DEC-12/13/14 are held at Andrew.
- **Ruled here:** an FWD addendum makes ADVI_FIRMBKTS the OWNER of retiring legacy operations (rules, schedules, Lambdas that become
  unnecessary), answering his "decommissioning plan for ... legacy operations". The CVO re-signs the ratified-text half for the new
  FWD.
- **Box CTO's act:** keep round 7 scoped to closing 49 Financial; make the plan document the next enrichment item; carry
  DEC-12/13/14 to Andrew as cards (section 3) and correct `andrew_acts`. Writing the plan does not start the Inflection or Cottonwood
  moves. The laptop CloudOps lane `0.7.0_AE_CloudOps~FBL` stands down when the Dell admin-group grant is read back on dell1
  (section 5); FB1 then does the edge-function and simulate acts itself.

### O11. ADVI_BDPRCE: explained, then kept

- **His words:** "The BVPRCE, the Black Diamond pricing, I don't really understand where we're at or the purpose of that. That's a
  new project that needs to be explored."
- **In plain terms (send Andrew this paragraph):** 49 Financial's holdings come to Opal through Black Diamond. Some holdings have no
  ticker, so no market price can be looked up; Opal prices each from the client's own recent trades (the median trade price of the
  previous trading day). While moving 49 Financial's data, the team found four defects in what 49 Financial sees today: repeated
  copies of one trade tilt the median; two sources on one date can pick different prices on different runs; some readers use the
  file's date instead of the trade date; and "capped" lots compare a scaled-down value with a full cost, so they show large false
  losses. The project delivers one written price rule in one place, every price traceable to its trades, and exact per-lot units
  and cost from Black Diamond's own unrealized-lots export (switched off today). Round 1 (read-only) finished on 2026-10-13; the CTO
  wrote the one rule (trades only, each trade counted once, executed price, previous trading day's median; @cd65a96bb6); the written
  rule reproduces 1,148 of 1,657 served rows, and 61 of 586 sampled lots carry a price that matches no canonical row. Nothing served
  has moved. Round 2 builds the rule; Andrew sees a before/after list of changed prices before any fix goes live (FWD-7). Source:
  ADVI alignment section 2a and line 29; `ENDPOINT_FORWARD_ADVI_BDPRCE_20261013.md`.
- **Act:** KEEP on `2.0.0_SA_COO~K1`. FIRMBKTS's exec-summary position slots wait on its capped-lot fix (dell1 report line 105), so
  it also unblocks O10.

### O12. Active Cottonwood accounts: matched through to Black Diamond, and draws limited to them

- **His words:** "We want to make sure that any active account has backfill for its various securities that have any securities
  that have been held for the period that they were held. And how we maintain the pricing of these active securities on a daily
  basis per account"; "I want to make sure that there's some clear matching mechanism ... that the Commonwealth backfill data ...
  we're able to match those through to the black diamond repository ... if we are not able to adequately match these to the various
  files, then we don't know what is an arc of all accounts."
- **DONE WHEN:** one "active Cottonwood set" file: crosswalk-MATCHED accounts plus current Black Diamond Cottonwood accounts, each with
  its holding windows; a reverse list mapping every CURRENT Black Diamond Cottonwood account to its Commonwealth predecessor or
  "none"; DEMQUE draws limited to that set over those windows.
- **Measured state:** the crosswalk exists, FWD-8 REALIZED: 1,533 Commonwealth accounts, 471 MATCHED, 1,062 NOT_MATCHED with reasons,
  21 near matches awaiting a person (`ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~49/ENDPOINT_READ_20261009.md` line 14). It matches
  one way only. COTBKF sizes its price need over the whole delivery (4,634 securities, 3,421,735 security-days). The crosswalk input
  sits in legacy `opal-data-cot`, so FIRMBKTS's Cottonwood move must repoint it -- a dependency no project records (ADVI alignment
  line 57).
- **Owners:** the set and reverse list: ADVI_COTBKF on dell2 (`2.0.0_SA_COO~C2`), one read-only cell, then COTBKF parks. **dell1's
  legs:** the `rank.py` P3 refusal and per-account windows in DEMQUE (`~Q1`), and a line in the FIRMBKTS plan (O10) naming the
  crosswalk input as a consumer to repoint.

### O13. ETFS_RIVALS (not named in the memos)

- Not in Andrew's memos. Keep as the dell1 CRO recommends (a client-openable page publishing daily; dell1 report lines 603-648) but
  add no seat. One hazard to clear: TO-APPLY-R29 is issued to `0.7.0_AE_CloudOps~RV1`, which the broker read as NOT REGISTERED (line
  622). Seat it or re-issue it to a live lane; do not let the signed pair go stale.

---

## 3. Decisions taken vs open

**Taken (no further word needed):** AI fill on the Anthropic path; first load under 3 s; the Security Analysis feature promote as
an Opal-internal feature cut from PROD (section 1.4 item 3); former Cottonwood clients excluded from draws; YCharts as its own
project; harvest V1 derived layers and links only; billing into the existing panel; FIRMBKTS owns retiring legacy operations;
HEALGAP close; SECHIST and STRATID graded once then close or park; RESAPP re-pointed to V1 (overruling the dell1 CRO's PARK).

**Open at Andrew, re-asked in plain English (call 4: the ADVI_FIRMBKTS decisions).** Andrew said "I do not know what these items
are". They are carried in `org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md` lines 245-266. **Every act on the
Inflection bucket (`opal-data-inf`) waits on both DEC-13 rulings** (PRD lines 259-263); the read-only census does not.

| item | what it is, plainly | REC |
|---|---|---|
| DEC-13 "Door 6" | `opal-data-inf/gold/meta/pipeline-complete.json` is the "done" marker file the Inflection pipeline writes when its gold run finishes. The `mdpf-feeder-accelerator` rule watches it to start downstream work. When Inflection moves to its own bucket, either a successor marker is named in the new home, or the marker and the rule watching it are retired. | Retire it with its watcher, after the box CTO confirms no live consumer reads it. |
| DEC-13 "B2" | `opal-data-inf/orion/jwt/current.json` is the Orion login token. It refreshes itself in place; moving it breaks the chain that refreshes it. It is Andrew's standing exception. | Keep it where it is, and keep `opal-data-inf` open for that one object. |
| DEC-12 write logging | Reads on the three legacy buckets are logged today; writes are logged only under `platinum/firm/`. Before a legacy bucket is deleted, the project must prove nothing wrote to it for 45 days, and a write to `gold/`, `bronze/`, `silver/`, `code/` or `state/` is invisible today. Turning on CloudTrail write data events for the three buckets closes that hole; it is billed. | Yes (the PRD's own recommendation). |
| DEC-14 `mockadv` | `mockadv` is a TEST tenant: `data/firm_registry.json` line 88 ("Mock Advisor (test account)", kind `test`, bucket `opal-data-bd`). The router maps it to 49 Financial's bucket, so retiring `opal-data-bd` moves two map entries. Andrew: "almost certainly deprecated/useless/not displayed anywhere." Measured here: it is still referenced -- a `FIRM#mockadv` partition in `opal-users-v2` (`infra/logic/registry/mail_parties.json` line 29), the firm dropdown ("add MockADV to firm dropdown", yang-pipeline CHANGELOG), test accounts from ADVI_ANONYM, the naming registry (`infra/logic/registry/scopes.json` line 84, `lib/opal_naming.py` lines 1864, 2005), and the IRPT directory and holdings runners (`data/assets/scripts/gold/investor_reporting/directory_runner.py` line 191, `holdings_snapshot.py` line 186). | NEW REC: RETIRE the alias (replacing "follows 49 Financial"), after a consumer census reads zero live use: its user rows, the dropdown entry, the two router map entries and the registry rows removed in one change with a rollback. Tests that use it as a negative case keep a fixture. |

The other questions in the alignment reports are settled above or are dell2's or site Z's (sections 4-5). SECCLASS's `bd-securities`
DynamoDB delete and the two client-facing pushes (CANON `/portfolios`, SECCLASS BD Mix) remain Andrew's acts, carried by the box CTO
as cards when their reads are in.

---

## 4. Per-project disposition (dell1)

Seats are from the dell1 box status report (live 13:10Z): 11 COO lanes (B1 D1 G1 H1 K1 M1 Q1 R1 S1 V1 W1), 6 CloudOps lanes (CT1
DELL1 FB1 HV1 RA1 SC1).

| project | disposition | seats | differs from the dell1 CRO? |
|---|---|---|---|
| AMGT_RESAPP | DRIVE: V1 (O1) and AI fill addendum (O2) | `~R1`, `~RA1`, plus one freed COO seat for O2 | YES: CRO said PARK; overruled by Andrew's #1 ranking |
| AMGT_HARVST | KEEP at its pace (O4); supply servable prefixes (O3) | `~W1`, `~HV1` | agrees (KEEP) |
| ADVI_FIRMBKTS | DRIVE: close 49 Financial; write the plan; FWD addendum for legacy operations (O10) | `~B1`, `~FB1` | agrees on scope; adds the plan and the addendum |
| ADVI_BDPRCE | KEEP (O11) | `~K1` | agrees |
| MDPF_CANON | DRIVE (O5) | `~D1`, CloudOps `~DELL1` | agrees |
| MDPF_DEMQUE | DRIVE: card, P3 exclusion, sync cell (O6, O7) | `~Q1` | agrees; adds the exclusion |
| MDPF_SECCLASS | KEEP, narrowed to the BD thread plus the sync cell and a full board (O7) | `~M1`, `~SC1` | agrees; adds the sync cell |
| MDPF_HEALGAP | CLOSE after the FWD-6 grade (O9) | `~G1` -> freed | agrees with KEEP-to-close |
| MDPF_SECHIST | grade once, PARK, fold, close (O9) | `~H1` -> freed | agrees (PARK); adds the fold |
| MDPF_STRATID | grade once, CLOSE or PARK (O9) | `~S1` -> freed | agrees (PARK); adds close-after-grade |
| YCharts (new) | brief from the laptop CRO, then host here (O8) | a freed seat at L5 | new |
| ETFS_RIVALS | KEEP, no added seat; clear the RV1 hazard (O13) | `~V1`, CVO `~RV1` | agrees |
| AMGT_CORPUS, DSGN_AMGTV1, LGIC_BLANKFIX, LGIC_CANON, LGIC_ENFORCE, NFRA_GATSCP | CLOSED (pare-down record); LGIC_ENFORCE's gate is owned by NFRA_CTLPLN | none | agrees |
| NFRA_CTLPLN (dell1 leg) | laptop project; `0.7.0_AE_CloudOps~CT1` executes crossbox orders only | `~CT1` | agrees |

**Freed COO seats** (`~G1`, `~H1`, `~S1`, three once their grading passes are done) go, in this order: (1) RESAPP's AI fill (O2), as
a `~lane` workstream of AMGT_RESAPP with a disjoint write surface (CLAUDE.md rule 27, one project per Tier-2 seat instance); (2) the
YCharts project once registered; (3) held. `0.0.0_AB_MSTR~DELL1` seats them; `1.0.0_SA_CTO~DELL1` names the lane in the register.

---

## 5. Cross-box joins

| join | the other box's part | dell1's part | route |
|---|---|---|---|
| Harvest access (O3) | site Z: one NFRA_MCPINDEX round (catalog rows for harvest and research) and an NFRA_OPLGTW research grant for asset-manager principals | the servable-prefix list | dell1 CTO -> `0.0.0_AB_MSTR` (laptop) -> `1.0.0_SA_CTO~Z` |
| HARVST and DEMQUE execution legs | site Z hosts the harvest runner (`~ZW`: bz-5/6/7) and the DEMQUE drawer task, Bloomberg ledger upload and the t34 lane | dell1 is the box of record for both (project.json placement DELL1) | settle the t34 owner with `1.0.0_SA_CTO~Z` |
| AI fill producers | site Z's disabled `OpalResearch-ExecManagement` / `OpalResearch-FilingsAnalyzer` tasks; `amgt-induction-daily` rc 4 | RESAPP decides re-enable or replace; owns the induction task | a site Z producer change needs `1.0.0_SA_CTO~Z`'s half |
| Active Cottonwood set (O12) | dell2: ADVI_COTBKF `~C2` builds the set and the reverse list in one read-only cell, then parks | DEMQUE `rank.py` P3 refusal and per-account windows; FIRMBKTS plan names the crosswalk input | dell2 publishes the set's path; DEMQUE reads it |
| YCharts (O8) | laptop: the CRO's L1 brief; the cluster CTO's L2/L3 | host and consumer | arrives as a registered project |
| Dell permissions | laptop: the Dell admin-group grant (@d2f79ea8dd; Andrew 16:5xZ "Sure let's do rec b"); NFRA_CTLPLN round 12 cell 1 applies it | read it back on dell1 (an edge-function admit and an `iam:SimulatePrincipalPolicy` call from the dell1 identity); then FB1 does those acts itself | on read-back, `0.7.0_AE_CloudOps~FBL` (laptop) stands down |
| Billing (dell2) | ADVI_BILLING re-pointed into the existing Fee Summary panel | no dell1 promote carries `AdvisorBookFeePanel` | -- |

---

## 6. Do not

- Do not promote live portal DEV whole. Only the Security Analysis feature, cut from PROD, with a receipt naming every page and its
  class. Never carry the `/portfolios` change or the fee panel without Andrew's word.
- Do not change a live round's spec or decomposition. Re-points land at the next L10.
- Do not start any act on `opal-data-inf` before both DEC-13 rulings are recorded. Do not start the Inflection or Cottonwood moves
  because the plan is written.
- Do not draw Bloomberg or Yahoo for former Cottonwood clients (P3). Do not start a new Bloomberg draw until Andrew's DEMQUE form
  is complete (CTO msg 4892). Bloomberg pulls go through their queue only.
- Do not use OpenAI for the AI fill. Do not serve raw publisher article text through the gateway in V1.
- Do not run a bulk YCharts draw before a pacing rule protects the one shared session.
- Do not hold V1 for the scanner-currency slice.
- Do not add seats to AMGT_HARVST or to SECCLASS's non-BD FWDs this week.
- Do not route a dell1 project's AWS acts to a laptop CloudOps seat once the admin-group grant reads back (Andrew 13:1xZ: "I do not
  want CloudOps agents from one box working on projects that are otherwise based on another box").
- Do not build an alert, monitor or notification for any of this (standing moratorium), and do not stand up a shadow pipeline or a
  parity comparator.

---

## 7. Required reading

Each path: repo-relative form first (valid on every box), then the laptop `file:///` link (CLAUDE.md rule 33). On dell1, open the
repo-relative path under its own checkout.

1. This packet: `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL1_20261013.md` --
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL1_20261013.md
2. The cluster ruling: `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md` --
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261013_173xZ_CLUSTER_POSITIONING_ON_THE_PIVOT_AGGREGATE.md
3. Andrew's answers: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_174xZ_POSITIONING_CALLS_ANSWERED_ARTIFACT_AND_CLICKABLE_PATHS.md` --
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_174xZ_POSITIONING_CALLS_ANSWERED_ARTIFACT_AND_CLICKABLE_PATHS.md
4. The aggregate: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/PIVOT_AGGREGATE_20261013.md` --
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/PIVOT_AGGREGATE_20261013.md
5. AMGT alignment: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/AMGT_ALIGNMENT_20261013.md` --
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/AMGT_ALIGNMENT_20261013.md
6. MDPF alignment: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/MDPF_ALIGNMENT_20261013.md` --
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/MDPF_ALIGNMENT_20261013.md
7. ADVI alignment: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/ADVI_ALIGNMENT_20261013.md` --
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/alignment/ADVI_ALIGNMENT_20261013.md
8. The three transcripts: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/` (AMGT_REVIEW_TRANSCRIPT.md,
   MDPF_REVIEW_TRANSCRIPT.md, ADVI_REVIEW_TRANSCRIPT.md) --
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/
9. FIRMBKTS PRD DEC-7 and DEC-12..14: `org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md` lines 220-266 --
   file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D8/ADVI/ADVI_FIRMBKTS/prd/ADVI_FIRMBKTS_PRD.md
10. DEVPLN C-FEATURE and C-PROMOTE: `org/missions/D0/NFRA/NFRA_DEVPLN/prd/NFRA_DEVPLN_PRD.md` lines 108-112 --
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D0/NFRA/NFRA_DEVPLN/prd/NFRA_DEVPLN_PRD.md
11. The e7f2 breakdown: `org/tier1_exec/1.0.0_SA_CTO/deliverables/E7F2_PORTAL_DEV_NOT_ON_PROD_BREAKDOWN_20261011.md` --
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/E7F2_PORTAL_DEV_NOT_ON_PROD_BREAKDOWN_20261011.md
12. DEMQUE qualification and Andrew's form: `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/QUEUE_QUALIFICATION_20261013.md`
    -- file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/2.0.0_SA_COO~Q1/QUEUE_QUALIFICATION_20261013.md ;
    `org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md` --
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/1.0.0_SA_CTO/deliverables/DEMQUE_QUEUE_FORM_ANDREW_20261013.md
13. The dell1 box status report: `org/tier1_exec/4.0.0_SA_CRO/deliverables/BOX_STATUS_REPORT_dell1_20261013.md` --
    file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier1_exec/4.0.0_SA_CRO/deliverables/BOX_STATUS_REPORT_dell1_20261013.md

---

## 8. First acts, in order

**`1.0.0_SA_CTO~DELL1`:**
1. Read sections 1-2 in full; ack this packet's broker message.
2. AMGT_RESAPP: at the round-102 L10, re-point to O1's three cells; close qq-2; drop the scanner slice from V1 or place it on the
   DEMQUE form. Write the O2 AI-fill PRD addendum and send its ratified-text half to the CVO.
3. Cut the Security Analysis feature branch from the last PROD release, approve it as Opal-internal, and hand it to the portal
   release seat for promote with a page-class receipt.
4. ADVI_FIRMBKTS: correct `andrew_acts` to carry DEC-12/13/14 (section 3 wording); queue the plan document as the next enrichment
   item; write the legacy-operations FWD addendum.
5. MDPF: HEALGAP FWD-6 grade and close; CVO grading passes for SECHIST and STRATID; CANON FWD-3 grade and round 7; the DEMQUE<->SECCLASS
   CONTRACTS rows and cells; the `rank.py` P3 refusal cell; fix the CANON register lines.
6. Produce the harvest servable-prefix list (O3) and send it to site Z through `0.0.0_AB_MSTR`.
7. Settle the t34 owner and the RV1 hazard.

**`0.0.0_AB_MSTR~DELL1`:**
1. Relay this packet's path to `1.0.0_SA_CTO~DELL1` and to every live dell1 COO lane named in section 4 (path plus one line; each
   COO reads its project's section).
2. Read back the Dell admin-group grant on the dell1 identity (one edge-function admit and one `iam:SimulatePrincipalPolicy`); report
   the read to the laptop so `0.7.0_AE_CloudOps~FBL` stands down.
3. As `~G1`, `~H1` and `~S1` free up, re-seat them per section 4 on the CTO's word; force-remove merged worktrees at each drain.
4. Place the client-account hash list on dell1 (RESAPP blocker D1-W381-S1, dell1 report line 496).

---

## 9. Not measured here / uncertainty

- Live AWS, the PROD page itself and PROD response times were not re-read for this packet; state figures are carried from the
  alignment reports (read 2026-10-13 ~15:30Z-17:0xZ) and the dell1 box status report (13:10Z). Rounds may have moved since.
- The `mockadv` census above is a repo text read (255 files carry the token, most under `org/`); live use (logins on the
  `FIRM#mockadv` rows, dropdown display on PROD) was not read. The REC is conditional on that census.
- Whether a live consumer reads Door 6 beyond the `mdpf-feeder-accelerator` rule was not read.
- YCharts coverage of the DEMQUE items, and whether the dormant YCharts Lambdas have a schedule, are unmeasured.
- The share of the 1,062 unmatched Commonwealth accounts that are closed accounts was not read.
- The dell1 seat roster is from 13:10Z; liveness of each lane now was not read.
- The 93/95/105 population difference is ruled (93) but not reconciled name by name.
