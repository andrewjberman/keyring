# BRIEF -- the MC portal's control plane: the fabric seen live, the gateway mapped and rated, people removable at once

**Author:** `4.0.0_SA_CRO` | **Written:** 2026-10-08 ~20:0xZ (UTC) | **Mode:** NEW, as an addition to NFRA_MCPORTAL
(in flight, PARKED since 2026-10-01; site Z owns its PRD; this brief is the PRD's input).
**Asked by:** Andrew, point 4 of his ~18:4xZ transcript, verbatim in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_184xZ_FIVE_POINTS_KIMMY_EFFICIENCY_ALYSSA_MCPORTAL_OPEN_CALLS_AGGREGATE.md`;
placed by `1.0.0_SA_CTO` msg 107151. Related Andrew word at this seat (~17:3xZ): "interface design and etc can exist on the
MCPORTAL ... it is a good idea and it does deserve a page on there" (`org/tier1_exec/4.0.0_SA_CRO/deliverables/MCPORTAL_FUTURE_PAGE_FABRIC_ACTIVITY_OVERLAP_20261008.md`).
**Consumer:** the NFRA_MCPORTAL CTO (`/endpoint --forward`, then a PRD addendum).
**Vintage:** laptop, CLOUD, 2026-10-08 19:3xZ-20:0xZ. Repo reads and this seat's own stores. No gateway tool call and no
vendor API call was made for this brief.

---

## PART 0 -- HOW THE BLIND CONSTRAINT WAS HONOURED, AND WHERE IT BENT

This adds to a project in flight, so it was written without reading NFRA_MCPORTAL's task orders. It **bent in one
place**: the census read `project.json`'s `blocking` text to report what is built, which is round 3, 3 of 5 orders
complete, and the grant writer live. That text describes the branch, not the base. The outcomes below do not depend on it:
O7 and O8 restate PRD outcomes as Andrew worded them today, not as round 3 cut them.

---

## ANDREW'S WORDS, VERBATIM (point 4, the parts this brief serves)

> "We really need to be able to understand very quickly, not only where we are, like have certain processes with user
> management, be able to poll users off the platform at a moment's notice. ... what even is on the Opal Gateway, what are
> all of the channels that are open and what tools are available associated with those channels? What an index per
> channel needs to be displayed? Um, and what fields, what information is available through those tools? If they're going
> to data tables, what is there? We need an index. We need a map. And we probably need a ultimately like a risk rating
> based on how sensitive that information is. So in the event that we want to create policies for riskier MCP channels,
> That's a little further downstream, but something that we want to make sure is covered now. ... The more immediate ones
> are probably functions around our ongoing agentic infrastructure. We want to be able to see what is happening on our
> control plane so that covers the The graph, we want to have those, that activity overlap function, that should be
> streaming to that portal. We should be able to see get operations. We should know, commit pace, what commits are coming
> from where, what projects are they touching? Um, potential risk for overlap, what that what those risk ratings look
> like. pushes across boxes. ... we're going to need to be able to have a visible dashboard control plane on item 4 there."

("poll users off" reads as "pull users off"; "get" = git.)

**Three requirements in his words, in his order of urgency:**
1. **The fabric, seen.** Overlap, git operations, commit pace by box and project, overlap risk and pushes across boxes,
   streaming to the portal. He calls this "the more immediate".
2. **The gateway, mapped.** Every channel, its tools, the fields and tables they reach, and a sensitivity rating per channel,
   with policy on the rating left for later.
3. **People, removable at once.** Pull a user off the platform at a moment's notice; entitlements managed.

---

## PART I -- THE OUTCOME TERRITORY

### THE CANDIDATE THREAD (becomes FWD-1 of the addition)

**Andrew opens the control-plane page and sees, without asking any seat, which box is working on what right now and where
two boxes are converging.**
1. One page in the MC portal, signed in as Andrew. It reads the activity store every box already writes to.
2. It shows each box's commits in the last hours by project, and the surfaces two or more boxes are on, Terraform first.
   Every figure carries its age.

It is the smallest journey that serves "the more immediate" requirement end to end on real data, and its source is live
today (Part IV, finding 1). Every other outcome below is an enrichment round on that page or a second page.

### O1 -- Andrew sees commit pace by box and by project

Andrew reads, for each box, how many commits it made in a window, by which seats, on which projects, and when its last
commit landed. He can tell a box that has gone quiet from one that is busy without asking it. Source: Andrew "commit pace,
what commits are coming from where, what projects are they touching"; Part IV finding 1.

### O2 -- Andrew sees where boxes overlap, and how risky each overlap is

Andrew reads the surfaces with two or more boxes on them. Each is rated by what it is (Terraform, code, registry, tool,
record) and by whether a deploy is open on it. The dangerous case, two boxes editing a surface that one box holds a deploy
on, stands out from the safe case, two boxes appending to a shared log. Source: "potential risk for overlap, what ... those
risk ratings look like"; finding 1.

### O3 -- Andrew sees git operations and pushes across the boxes

Andrew reads, per box, what has been committed, what has been pushed to its box branch, and what has reached the trunk. He
also sees when the trunk last moved and whether integration is being refused or stalled. He can see a box whose work is not
reaching the trunk. Source: "We should be able to see get operations ... pushes across boxes"; findings 1 and 2.

### O4 -- Andrew sees every open call across the cluster and closes one himself

Andrew reads every open call on every box (a fork, or an act only he can do), by box, project and asking seat, with its
age. He closes one with his ruling from the page. A box with no list shows as absent, never as empty. Source: Andrew point 5
("open calls need to be manageable instantly"); finding 3. Point 5's store and tool exist; this outcome is the page.

### O5 -- Andrew reads the gateway as one map: channels, tools, and what each reaches

Andrew opens the gateway map and reads every channel. For each tool he sees what it reaches (a mailbox, a SharePoint
drive, a Schwab dataset, a Black Diamond table, the estate graph), the fields where they are known, whether it reads or
acts, and which tier and entitlement admit it. The map is built from the gateway's own definitions, so it cannot drift from
what the gateway serves. It includes the REST routes outside the tool protocol. Source: "what are all of the channels ...
what tools ... what fields ... If they're going to data tables, what is there? We need an index. We need a map."; finding 4.

### O6 -- Every channel carries a sensitivity rating a later policy can read

Each channel shows a rating of how sensitive its information is, with a one-line reason. The rating is stored where a later
policy could read it. No policy is attached now. Source: "a risk rating based on how sensitive that information is ...
policies for riskier MCP channels ... a little further downstream"; finding 5.

### O7 -- Andrew pulls a person off the platform at once, from the page

Andrew stops one person, on the gateway and on opalinvest.dev, from the page, and the stop holds on their very next call or
sign-in. He can restore them the same way, and the history stays. Source: "be able to poll users off the platform at a
moment's notice". This is PRD FWD-6 (users) and FWD-10 (stop a person or the server), restated, not re-scoped: finding 6.

### O8 -- Andrew manages who may reach which channel

Andrew narrows or widens one person's reach to a channel or dataset from the page, and their next call obeys it. This is
PRD FWD-1, already the project's thread. It is named here only so the map (O5) and the rating (O6) attach to the same
screen. Source: "obviously, the entitlements, managing the entitlements".

---

## PART II -- WHERE THE BOUNDARY SITS

| This addition OWNS | It RELIES ON (owned elsewhere) |
|---|---|
| The control-plane pages (O1-O4) inside the MC portal | **The activity store and tool** (`fabric-activity` / `comp-activity`, 4.0.0_SA_CRO, live): the data. The pages read it; they do not re-collect it. |
| The gateway map page and its rating column (O5, O6) | **The gateway's own definitions** (integration specs, the tool class table, the write-tool registry, `DATA_CATALOG.yaml`, the audit lake): the map renders them and never keeps a second list. |
| The rating scale and per-channel values, as data | **NFRA_OPLGTW** (the gateway's contract): any policy that enforces a rating, and the move of tiers and tool lists into the grant table (PRD C6, gate G-OPLGTW, Andrew's word). |
| -- | **NFRA_MCPORTAL's existing PRD**: FWD-1, FWD-6, FWD-9, FWD-10, its owner gate (C2), its repo (C1). O5 deepens FWD-9; O7 and O8 are FWD-6/10 and FWD-1. |
| -- | **Open calls** (`.tools/open-calls.py`, the cluster copy in S3, 4.0.0_SA_CRO): O4 reads it and closes through it. |
| -- | **GitOps** (4.0.0_SA_CRO~A, per-box branches): O3 reads the branches and integration records it produces. |
| -- | **The fabric layer in the served graph** (pending sign-off, 0.7.0_AE_CloudOps to deploy): an alternative source for O1-O2 once live. |

Not in scope: any alert or notification (standing moratorium; "streaming" is read here as live-on-open); the Kimmy routing
of client messages to Andrew's phone (point 1, its own project); Alyssa's Schwab channels (point 3).

---

## PART III -- THE QUALITATIVE BAR

- Andrew learns that two boxes are on the same Terraform module from the page, before a merge conflict or a deploy
  collision tells him.
- Andrew never has to ask a seat "what is dell2 doing?" to know which projects dell2 committed to this afternoon.
- A box whose commits are not reaching the trunk is visible as such the same day. It is not discovered at the next
  integration.
- Andrew can answer "what could an agent with access to this channel read about a client?" from the map, without reading
  gateway code.
- When Andrew decides to put a policy on the riskiest channels, the ratings are already there to point at. Nobody has to
  re-survey the gateway first.
- Pulling a person off takes Andrew one action and no seat. It is not a file edit on a box and a redeploy.
- Every number on the page says how old it is, and a box that is not reporting reads "not reporting", never zero.

---

## PART IV -- THE SUBSTRATE: what exists, measured

1. **The activity store is live and multi-box [READ, measured 2026-10-08 19:1xZ].** Every commit on a box with the hook
   writes one record to `s3://opal-313476888478-globgrph/fabric/activity/v1/dt=<day>/box=<box>/`, with box, seat, project,
   files and rolled-up surfaces. Measured, last hour: dell2 86 commits, laptop 52, dell1 35, all `box_claim=measured`;
   site Z had not installed the hook. `comp-activity overlap | who | boxes` already computes O1 and O2 in seconds:
   15 surfaces had two or more boxes over 36 h, 4 of them Terraform modules. Build record:
   `org/tier1_exec/4.0.0_SA_CRO/deliverables/GRAPH_COHERENCE_BUILD_20261008.md`.
2. **Git operations are partly recorded [READ].** Each record is marked MERGED (on `origin/CLOUD`), PUSHED (on an
   `origin/box/*` branch) or on-box, against the reading box's last fetch (per-box branches are being cut over; row B4 of
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/PER_BOX_BRANCH_BUILD_PLACEMENT_20261008.md`). Integration refusals are
   counted only in each box's `org/git-author-override-audit.log` (MERGE-REFUSED: 91 rows since 2026-10-01 on the laptop
   read). Push and fetch events are not recorded anywhere a page can read.
3. **Open calls are cluster-wide in S3 [READ].** `s3://.../fabric/open-calls/v1/box=<box>/open_calls.json`, written on
   every add and close; `open-calls.py list --all --cloud` reads all boxes. Closing as Andrew exists
   (`close --ruled-by andrew`). At 19:1xZ the laptop held 3 open calls; the other boxes had not yet published.
4. **The gateway map exists as code, not as a page [READ, census of `infra/aws/ec2/opal-gateway/app/`].** 66 MCP tools in
   13 channels: 6 Microsoft 365 families (42 tools) plus 7 enabled integrations (24 tools: YCharts, data refresh, estate
   graph, Schwab, portal index, discover, Black Diamond). 8 are write tools and 58 read. About 47 can return client
   content. 14 REST route families sit outside the tool protocol, including the Black Diamond OTP fetch and the REST mail
   and Teams routes. The pieces a page would read:
   - integration specs (`app/integrations/*/integration.py`);
   - the tool class table (`app/data_entitlement.py:95-127`);
   - the write-tool registry (`app/destructive_ops.py:66-118`);
   - `app/refs/DATA_CATALOG.yaml` v0.4 (16 channels, 5 silver and 5 portal datasets);
   - the per-call audit lake `opal-mcp-audit`.
   Field reach is stated only for Schwab (44 fields over 4 datasets, accounts aliased by keyed hash), Black Diamond (12
   columns, raw account ids and names) and the catalog's portal rows. Microsoft 365 tools reach whatever the user's
   mailbox, files and chats hold. Census, table per channel with file:line evidence:
   `org/tier1_exec/4.0.0_SA_CRO/deliverables/GATEWAY_CHANNEL_MAP_20261008.md`.
5. **No sensitivity rating exists anywhere [READ].** The nearest are the write classes per tool (SAFE /
   WRITE_REVERSIBLE / IRREVERSIBLE_SEND) and the catalog's per-row firm and verdict. A PROPOSED five-level scale, for the
   PRD to ratify or replace:
   - R0 public or vendor market data;
   - R1 internal operational metadata;
   - R2 firm-confidential aggregates;
   - R3 client PII or client financial rows;
   - R4 acts on a person's or the firm's behalf.
   Read that way: YCharts R0; discover and identity R1; portal index R2; Schwab, Black Diamond, files and meetings R3;
   mail, Teams, upload and the data-refresh trigger R4.
6. **Pulling a person off today is files on one box [READ].**
   - The kill switch, the person blocklist and the token-revocation lists are files, hot-reloaded.
   - Tiers are environment lists that need a redeploy.
   - Data grants live in a DynamoDB table, written by the grant-writer Lambda, and take effect on the next call.
   - opalinvest.dev users live in `opal-users-v2` and `opal-partner-*`.
   PRD FWD-6 and FWD-10 are not built, and PRD C6 keeps the files as files until G-OPLGTW.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The MC portal must be un-parked and seated, and its owner gate (C2) holds for every new page.
- Site Z must write activity records (install the hook) before O1-O3 cover all four boxes. Until then the page names site Z
  as not reporting.
- Push, fetch and integration events need a recorded home a page can read (O3). Today only commits are recorded.
- The MC portal backend must read the S3 stores (activity, open calls) with a read grant. Their bucket is the estate
  graph's.
- Ratings (O6) need one owner who keeps them current as channels are added. A new channel with no rating should read
  "unrated", never silently R0.
- The map (O5) must be generated from the gateway's own definitions at read time or at build time from the same commit,
  never hand-kept.
- O7 crosses two systems, the gateway and the opalinvest.dev auth function. The PRD's C6/C7 and G-OPLGTW decide how a stop
  reaches both.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-08 19:1xZ-19:4xZ. Status ages; cut nothing from this part.
- Activity store: 3 of 4 boxes reporting measured records; about 5,000 records over 2 days (including backfill marked
  inferred).
- Open-calls cluster copy: laptop published (3 open); dell1, dell2 and site Z absent.
- NFRA_MCPORTAL: PARKED, placement site Z; FWD-1 round 3 executing when parked; FWD-6/10 unbuilt.
- Gateway: 7 integrations enabled at deploy (`deploy-to-ec2.sh:400`); several module headers still say DORMANT (stale).

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- The live gateway box was not read: its `.env`, its blocklist and kill-switch files, or `list_tools` per tier. The
  enabled set comes from the deploy template.
- The ratings are proposals from a code read, not a data-sensitivity review of the live data. The 47 tools that "can
  return client content" are an inference from what each tool reaches.
- The grant-writer Lambda's code and whether its changes table is set live were not read. The opalinvest.dev auth
  function and user tables were not read.
- Whether the MC portal stack can read S3 from where it is served was not checked.
- How fresh "streaming" must be is left to the PRD; no number is set here.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/mcportal-control-plane-brief-20261008.md
  PROJECT           NFRA_MCPORTAL (addition; PARKED; placement site Z)
  EXISTING PRD      org/missions/D6/NFRA/NFRA_MCPORTAL/prd/NFRA_MCPORTAL_PRD.md (FWD-1, -6, -9, -10; C1, C2, C6, C7; G-OPLGTW)
  SIBLING PROJECTS  NFRA_GRPHCO / fabric-activity (4.0.0_SA_CRO); open calls (4.0.0_SA_CRO); GitOps per-box branches
                    (4.0.0_SA_CRO~A); NFRA_OPLGTW (gateway contract); Kimmy comms routing (Andrew point 1)
  PRIOR ART         .tools/fabric-activity.py + comp-activity; .tools/open-calls.py (cluster copy);
                    infra/aws/ec2/opal-gateway/app/{integrations/*,data_entitlement.py,destructive_ops.py,audit.py,refs/DATA_CATALOG.yaml};
                    MCPORTAL_FUTURE_PAGE_FABRIC_ACTIVITY_OVERLAP_20261008.md
  MEASURED AT       2026-10-08 19:1xZ-19:4xZ, laptop CLOUD
```
