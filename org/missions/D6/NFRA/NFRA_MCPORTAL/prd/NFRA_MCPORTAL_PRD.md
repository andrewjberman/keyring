```json
{
  "project": "NFRA_MCPORTAL",
  "directive": "D6",
  "fabric": "site-z",
  "prd_version": "v0.9",
  "step": 4,
  "brief_ref": "docs/briefs/mcportal-tech-ops-dashboard-brief-20260917.md@8d1f5c362b",
  "endpoint_outcomes": [
    "FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7",
    "FWD-8", "FWD-9", "FWD-10", "FWD-11", "FWD-12", "FWD-13",
    "FWD-14", "FWD-15", "FWD-16", "FWD-17", "FWD-18", "FWD-19", "FWD-20", "FWD-21", "FWD-22"
  ],
  "status": "DRAFT"
}
```

# NFRA_MCPORTAL - mcportal: the operator console at mcp.opalinvest.dev

## Authority and project arc

Author and accountable CTO: `1.0.0_SA_CTO~O`. Directive D6, Opal AI; macro NFRA; execution fabric site-z. Registered
@8105cd4f0e under Andrew's goal of 2026-09-24, *"Finish all D6 opal_ai work, including the MCPINDEX, any and all MCP
server work, entitlements, integrations with MCP, etc. ... You have license to create projects, register them, and
proceed /canonical-flow as needed to this end."* The record is
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_210xZ_CTO_O_GOAL_FINISH_ALL_D6_OPAL_AI.md` @c83c7de329.

The brief is `docs/briefs/mcportal-tech-ops-dashboard-brief-20260917.md` @8d1f5c362b (`4.0.0_SA_CRO`). Andrew
answered every page's cards in-session on 2026-09-17, and his words are verbatim there. The rulings this PRD rests on:
- the address is `mcp.opalinvest.dev` ("definitely the .dev domain");
- only Andrew may use it ("Yes just me"), except that any Opal Microsoft user keeps `/sprint`;
- it has its own repo ("I would actually build out a new repo called mcportal");
- grants take effect immediately ("For MCP Ops: Take effect immediately");
- it is not an alert ("This is not an alert, this is an analytics dashboard. Strictly read when opened.").

**v0.2 (2026-09-24 ~21:4xZ)** answers `3.0.0_SA_CVO~O`'s refusal of the v0.1 ratified-text half (review
`org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_MCPORTAL_PRD_v0.1_RATIFIED_TEXT_SIGNOFF_REVIEW_20260924.md`
@3702879c37):
- **P0.** C4 now names the writer, its trust edge and the independent identity check it runs. Negative arms join the
  acceptance matrix.
- **P1.** C6 names the NFRA_OPLGTW contract amendment it needs. That amendment meets Andrew's 2026-09-22 OPLGTW stop,
  so it is listed for him (G-OPLGTW), and C6 leaves round 1. FWD-1 narrows the colleague's DATA grant, a record
  type the store already holds.
- **P2.** C2 binds a dashboard-owner list of its own, and the C4 citation is corrected.
- **The question the review raised.** Round 1 is built on the gateway's current path. The move carries it (see the
  handoff).
The ENDPOINT is unchanged.

The endpoint was emitted and its DONE WHEN lines confirmed by this seat under the goal's licence
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/MCPORTAL_ENDPOINT_FORWARD_20260924.md`). Andrew may amend any line. The
header stays DRAFT until L4-R. The author signs neither half.

## Scope and evidence boundary

**This project owns:**
- the `mcportal` repo and its pages;
- the admin handlers behind them, which sit with the gateway (C3);
- the grant-writer path that holds the access-admin role;
- moving tiers and per-person tool lists from the gateway's flat files into the grant table;
- three nightly rollups (session analytics, firewall counts, AWS cost history), the cost table and its Ramp-email
  collection;
- the audit and revert of every dashboard write.

**It relies on and does not change:**
- the gateway's sign-in, identity verification and Claude-client paths (moving into `opal_ai` under NFRA_OPALAI);
- the grant model and table (NFRA_OPLGTW);
- the one data catalog and the tools (NFRA_MCPINDEX);
- the daily monitor and its emailed report (NFRA_REPORT);
- the session-analytics function and `opal-sentinel`;
- the published daily-sprint HTML;
- the portal's auth function (it gains a `disabled` state it honours, C7).

**Explicitly NOT this project's** (brief Part II):
- the emailed report's contents, and GuardDuty;
- the marketing site as an Infosec property, and "View as this user";
- a Fabric page, and monthly target lines;
- the session-analytics security fixes (a portal-side item with its own review);
- any alert, alarm or monitor.

**Evidence boundary.** Nothing in AWS was read for the brief or for this PRD. That covers session retention, whether
the block lists are Terraform-managed, website firewall logging, and table and log sizes. How well Ramp emails parse
is untested. Which vendors bypass Ramp is unknown. **Every figure a page will show is DESIRED until a cell exercises
it.**

## ENDPOINT (step 2, /endpoint --forward)

Transcribed from `org/tier1_exec/1.0.0_SA_CTO/deliverables/MCPORTAL_ENDPOINT_FORWARD_20260924.md`; statement, DONE WHEN
and ACCEPT are verbatim, and SOURCE lines are dropped.

```
  FWD-1  Andrew changes what one colleague may ask the Opal MCP about, from the dashboard, and
         the colleague's very next question reflects the change
         DONE WHEN  EXERCISED -- one real change followed to the colleague's next answer
         ACCEPT     signed in as himself at the dashboard's address, Andrew narrows one colleague's
                    access; the colleague's next question is answered within the new limits and
                    no wider; widening it back works the same way; both changes appear in the
                    dashboard's history with what they were before and after

  FWD-2  Nobody but Andrew can open the dashboard or change anything through it, while any Opal
         colleague can still read the daily report
         DONE WHEN  EXERCISED -- a signed-in colleague tries every page and every change
         ACCEPT     another Opal colleague who types the dashboard's address is refused on every
                    page and every change, and can still open the daily report at its usual page

  FWD-3  Andrew opens one address and knows within seconds whether anything needs him
         DONE WHEN  EXERCISED -- Andrew decides from the home screen alone on a real day
         ACCEPT     the home screen's six summaries each match the page they lead to, and Andrew
                    can say whether to open anything else without opening the emailed report

  FWD-4  Every change made from the dashboard can be seen and undone
         DONE WHEN  EXERCISED -- one change of each kind made and reverted
         ACCEPT     each change is listed newest first with what it was before and after, and
                    undoing it puts things back exactly as they were

  FWD-5  Andrew reads the daily Operations Report inside the dashboard
         DONE WHEN  EXERCISED -- today's report and an earlier day read there
         ACCEPT     the report shown is the one already published, today's and any earlier day,
                    on a desktop or a phone

  FWD-6  Andrew adds, edits, disables and removes an opalinvest.dev user at both permission
         levels from one screen
         DONE WHEN  EXERCISED -- a real partner user onboarded without a database command
         ACCEPT     Andrew onboards a new partner user and later disables them without touching a
                    database command; a disabled person cannot sign in and their history stays;
                    permanent removal asks him to confirm first

  FWD-7  Andrew hands a prospect a working demo login during a call and revokes it himself later
         DONE WHEN  EXERCISED -- one demo login issued, used and revoked
         ACCEPT     a working login is in the prospect's hands in under a minute, the password is
                    shown once, and revoking it stops it working

  FWD-8  Andrew sees who actually uses opalinvest.dev, by name, firm, page and feature, and who
         never has
         DONE WHEN  EXERCISED -- Andrew names, for one firm, who has never signed in
         ACCEPT     the named people, their last visit and their use of pages and features are
                    shown for Opal staff and client users, with demo users left out by default

  FWD-9  Andrew sees every Opal data property beside the tools that answer it, and every tool
         with what it answers and whether it has been cleared for safety
         DONE WHEN  EXERCISED -- one property and one uncleared tool read on the page
         ACCEPT     the page matches the one catalogue the tools are built from, and a tool that
                    has not been cleared for safety stands out

  FWD-10 Andrew sees who called which tool and what was refused, and can stop one person or the
         whole server at once
         DONE WHEN  EXERCISED -- one person stopped and restored; the whole server stopped and
                    restored in a quiet window
         ACCEPT     the call history matches the server's own record, and a stop takes effect on
                    the very next call

  FWD-11 Andrew answers "did everything land, and is what is deployed what we intended" without
         opening the email
         DONE WHEN  EXERCISED -- the page and that day's email compared
         ACCEPT     the page and the email never disagree, lateness is counted in trading days, and
                    a re-run from the page produces a fresh check

  FWD-12 Andrew sees every technology dollar by vendor or by purpose, and what moved
         DONE WHEN  EXERCISED -- last month's spend stated by purpose from the page
         ACCEPT     Andrew states last month's non-AWS technology spend by purpose without opening
                    Ramp; costs that never pass through Ramp are shown and marked as entered by hand

  FWD-13 Andrew sees who is knocking on each Opal address and blocks one in one click
         DONE WHEN  EXERCISED -- one suspicious address blocked and unblocked
         ACCEPT     Andrew goes from "this address looks wrong" to blocked without the AWS console,
                    and the block and its removal are recorded

  FWD-14 Andrew opens the control-plane page and sees, without asking any seat, which box is
         working on what right now, by box, seat and project, with each box's last commit (v0.5)
         DONE WHEN  EXERCISED -- Andrew names one box's projects this afternoon from the page alone
         ACCEPT     every figure carries its age; a box that is not reporting reads "not reporting",
                    never zero; the counts match the activity store for the same window

  FWD-15 Andrew sees where two or more boxes are on the same surface, rated by risk (v0.5)
         DONE WHEN  EXERCISED -- one real overlap read on the page and checked against the store
         ACCEPT     each shared surface is rated by what it is (Terraform first) and whether a deploy
                    is open on it; two boxes editing a surface one holds a deploy on stands out from
                    two boxes appending to a shared log

  FWD-16 Andrew sees each box's git state: committed, pushed to its box branch, on the trunk, and
         when the trunk last moved or integration was refused (v0.5)
         DONE WHEN  EXERCISED -- one box whose work is not on the trunk is seen as such the same day
         ACCEPT     the page's per-box states match the branches and integration records; an event
                    with no recorded home reads "not recorded", never absent-as-zero

  FWD-17 Andrew reads every open call on every box and closes one with his ruling from the page (v0.5)
         DONE WHEN  EXERCISED -- one real call closed from the page
         ACCEPT     calls show box, project, asking seat and age; a box with no published list reads
                    absent, never empty; the close lands in that box's list with his ruling

  FWD-18 Andrew reads the gateway as one map: every channel, its tools, and what each reaches (v0.5)
         DONE WHEN  EXERCISED -- one channel's reach answered from the page and checked in code
         ACCEPT     each tool shows what it reaches, the fields where known, read or act, and the tier
                    and entitlement that admit it, REST routes included; the map is generated from
                    the gateway's own definitions and cannot drift from what it serves

  FWD-19 Every channel carries a sensitivity rating, stored where a later policy can read it (v0.5)
         DONE WHEN  EXERCISED -- the ratings read from the page and from their stored form agree
         ACCEPT     each channel shows its rating and a one-line reason; a channel with no rating
                    reads "unrated", never a default level; no policy acts on a rating
```

  FWD-20 Andrew reads the gateway's full breakdown on one page: every vendor or channel, the tools
         and indexes on each, and who is entitled to each today (v0.7) -- THE FIRST OUTCOME CUT
         DONE WHEN  EXERCISED -- Andrew reads the page; one channel's tool list is checked against the
                    deployed gateway's code, and one person's entitlements against the grant store
         ACCEPT     every channel the deployed gateway serves is listed, none from a hand-kept list
                    (C15); each lists its tools and catalog indexes (`refs/DATA_CATALOG.yaml`); each
                    shows the principals holding an active grant on it now, read from the entitlement
                    and grant stores (C4); a channel with no grant reads "no one", never blank

  FWD-21 Andrew picks a person and sees, then changes, what that person reaches through the gateway:
         channels, tools on each, tier, and each tool's history depth and poll cadence (v0.8)
         DONE WHEN  EXERCISED -- on a test principal, one channel switched off and back on, one tool
                    switched off and back on, and the person stopped and restored, each from the page;
                    each change is read back from the grant store and honoured on that person's next
                    gateway call; then the same per-person view read for one real person and checked
                    against the stores it reads
         ACCEPT     the per-person view lists Andrew, every staff principal and the Bloomberg account
                    (opalbloomberg@opalinvest.com) like any other person; each channel shows its tools,
                    each tool its history depth and poll cadence with their claims (NFRA_OPLGTW FWD-20
                    and NFRA_MCPINDEX FWD-20 supply them; "absent" said, never blank); every write goes
                    through the one grant writer (C18) and lands in the change history (FWD-4) with
                    before and after; writes are Andrew's only (C2); the stop is FWD-10's control,
                    pulled forward
         SOURCE     Andrew's site Z memo 2026-10-13: "All that needs to be visible and controlled through
                    MC Portal ... this way we have one master control panel"; direction
                    XB-20261013T185926Z-4d72 Z2

  FWD-22 Andrew reads, per box, the Claude account each Claude Code login is signed in to and how
         much of its 5-hour and weekly limits remain (v0.8)
         DONE WHEN  EXERCISED -- Andrew reads all four boxes' accounts and remaining limits on the
                    control-plane page without asking any agent
         ACCEPT     per box and per login: the account's email, plan and organization from the box's
                    own login record, never a token; 5-hour and weekly remaining, each with its reset
                    time and claim (MEASURED or ABSENT with its reason, never a guess or a stale copy);
                    each figure's age. Display only: no alert or notification (standing moratorium).
                    The first cell is a READ of where Claude Code or the account exposes the limits,
                    before anything is built
         SOURCE     Andrew-direct 2026-10-13 ~20:4xZ (dell2): "i want the mcp.opalinvest.dev/control-plane
                    function to include the logged in account + usage remaining on 5hr and weekly basis
                    by box"; record ANDREW_DIRECT_20261013_204xZ_CONTROL_PLANE_SHOWS_CLAUDE_ACCOUNT_AND_
                    USAGE_PER_BOX.md; row Z-S47

## CONTRACTS

**C1 -- Own repo, graded like the parent.** `Opal-Capital/mcportal` is created by `0.0.0_AB_MSTR~Z` on Andrew's
2026-09-17 word (gate G-REPO). It is wired into the workspace as a real submodule under NFRA_OPALAI's C2 mechanism
(`.gitmodules`, checkout-path init, the lane file before any hook, the parent's gates, and CI). It has DEV and PROD
branches, and only MSTR pushes. It uses React, Vite, TypeScript and bun, and follows the portal's current design law
(`portal/DESIGN.md`, 2026-09-11). It starts clean on that law.

**C2 -- Only Andrew, checked on the server, on every page and every write.** The load balancer's default Microsoft
sign-in (`alb.tf:210`, "the future GUI path") admits the tenant. Then a server-side exact match runs on every page
request and every write handler, against a dashboard-owner list whose ONLY purpose is this dashboard. That list holds
Andrew's address and nothing else. The gateway refuses to boot if the list holds any other entry. It is NOT
`MASTER_ADMIN_EMAILS`, which `tier.py:74` documents as "andrew@ + systems allowlist", so widening it for a systems
account can never widen the dashboard. The identity is taken from the ALB-signed `x-amzn-oidc-data` header, verified
against the regional ELB public key (`app/identity.py:52-58`). A hidden menu
never counts as access control. The one exception is `/sprint`, which stays open to any signed-in Opal Microsoft
user. The Claude-client paths (`/mcp`, the OAuth paths) are untouched, and no rule on them changes.

**C3 -- Where it is served: from the gateway process, behind that sign-in** (ruled by this seat on brief Part V.3).
The built pages are static assets served by the gateway application at `/`. The admin API handlers live with the
gateway (in `opal_ai`, beside the guard chain), not in a second service. **Why:** C2's server-side check then lives
in one process, and a second service would be a second identity boundary to keep in step. The S3 alternative needs its
own sign-in in front of it. The `mcportal` repo holds the pages. The gateway's deploy ships the built bundle pinned by
the `mcportal` commit, recorded in the deploy manifest beside the `opal_ai` commit.

**C4 -- The gateway still cannot grant itself access: a separate writer verifies Andrew itself.**
- **The writer:** a dedicated grant-writer function (an AWS Lambda, named by `lib/opal_naming.py name()`, Rule 30)
  whose execution role is the one role that may write the `POLICY#` partition, equivalent to
  `opal-gateway-access-admin`. It carries the same code path as the operator command line
  (`ops/schwab_entitlement_admin.py`), which stays working and unchanged.
- **The trust edge:** the gateway role gains `lambda:InvokeFunction` on that ONE function, and nothing else. It gains
  no `sts:AssumeRole` on the operator role. The operator role's existing trust condition, `ArnNotEquals
  aws:PrincipalArn = <gateway role>` (`infra/aws/terraform/opal-gateway/schwab_access_state.tf:132`), STANDS. The
  runtime write guard in `access_state.py` (`RUNTIME WRITES`, `:14-16` at HEAD) and the IAM `dynamodb:LeadingKeys`
  condition on the gateway role stand. The invoke grant is an IAM change under C10 (a ledger entry, blast radius
  named).
- **The independent identity check:** the gateway forwards, with each write, the ALB-signed `x-amzn-oidc-data` header
  of the request that asked for it. The writer verifies that header ITSELF, against the regional ELB public key, which
  the gateway cannot mint. It then exact-matches the header's `sub` claim against its OWN owner configuration
  (Andrew's `sub` value, set in the writer's own deploy, never read from the gateway), and refuses a header past its
  own `exp` claim. A write without a valid owner header is refused before any store call. (L10 addendum R-2 / G-C4,
  2026-09-28: the measured header carries `sub` and `exp` and carries neither `oid` nor `iat`, per
  `deliverables/2.0.0_SA_COO~MP/round3/E1_G-HDR_READ.md` @c8b42c8913.)
- **The named residual:** a compromised gateway that captures a live owner header could replay it until that header's
  `exp`. The `exp` bounds it. The writer writes its own audit record for every write and every refusal, in a record the
  gateway role cannot write, and the dashboard's history reads the writer's record. A replay is therefore visible,
  though not prevented.
- Every grant write keeps the store's optimistic revision check. A revoked record stays a tombstone, never a delete.
- **Addendum 2026-09-30 (for NFRA_MCPMSP C2; CVO~O note N1, 2.0.0_SA_COO~MS msg 26948):**
  - The writer gains one op, `register_tenant {tid, firm}`. It writes the `tenant_firm` record at
    `POLICY#TENANT#<tid>`, which sits inside the existing `POLICY#` LeadingKeys guard, so no IAM change is needed.
    The precedent is `POLICY#EMAILDENY#<sha>` (`app/access_state.py:62`), and the record type is added to NFRA_OPLGTW's
    contract in the same commit.
  - The op is owner-verified exactly as narrow and widen are. It is refused for a firm Andrew has not brought live
    (NFRA_MCPMSP C11), and it leaves one audit item in the writer's own record.
  - This writer is the ONLY writer of that record; the gateway only reads it. The MCPMSP cell that builds the op is
    granted this project's writer paths for that op alone.

**C5 -- Every dashboard write is audited and revertible.** Each write records who, when, what, before and after in the
grant store's `operator_audit` record type, or in an equivalent record for non-grant tables. The Recent Changes view
reads those records. A revert is itself a write with its own audit row. Hard delete of a user is a confirmed second
step after a disable.

**C6 -- Tiers and per-person tool lists move into the grant table (ENRICHMENT, gated G-OPLGTW). The kill switch and
blocklist stay files.** **This amends NFRA_OPLGTW's contract.** The table's record types are a closed set in
`org/standards/NFRA_OPLGTW_CONTRACT.json` (`state_store.record_types`), mirrored by the closed `POLICY_RECORD_TYPES`
tuple in `app/access_state.py`, and neither holds a tier or tool-list type. Adding them is a change to OPLGTW's
contract and adapter, and it meets Andrew's 2026-09-22 OPLGTW stop, so it waits on his word (G-OPLGTW). Round 1 does
not need it: FWD-1 narrows the colleague's DATA grant, which the store already holds (`data_entitlement`). Once
G-OPLGTW is given, the
gateway's enforcement path reads tiers and tool lists from the grant table with a strong read per call, so a change
applies on the next call (his "take effect immediately"). The kill switch, blocklist and revoked tokens stay files,
because they must work when DynamoDB is unreachable. The move is a port: the flat files stop being read in the same
release that starts reading the table. No moment has two sources.

**C7 -- Users: disable before delete, at both levels.** The dashboard backend writes `opal-users-v2` and the
`opal-partner-<firmId>` tables, calls the auth function's existing admin routes, and adds a `disabled` state that the
auth function honours. A disabled person cannot sign in and their history is kept. Demo logins write the demo-firm
rows, show the one-time password once, and never expire on their own.

**C8 -- Read when opened, never an alert.** No page sends anything and no checker is added. Every page reads what an
existing producer publishes, or a rollup of data already collected. The three nightly rollups and the cost table are
scheduled producers, named by `lib/opal_naming.py name()`, with their S3 addresses from `address()`, never typed (Rule
30). A `mcportal` row lands in `infra/logic/registry/systems.json` before any resource is created (brief V.1). "Re-run
now" on Health invokes the existing daily monitor. It is not a new checker.

**C9 -- Cost from Ramp emails, with his own sign-in.** Non-AWS charges come from Ramp receipt-request emails in his
Outlook, read through the gateway's mail tools under his own delegated token when he clicks Sync. That is Microsoft
Graph in Opal's own tenant. There is no Ramp API and no other vendor call. Costs that never touch Ramp are manual
recurring rows, marked manual.

**C10 -- Never-widen and the change ledger bind the three risky surfaces.** Any act on the load balancer's rules, the
grant table's IAM, or the auth function opens a ledger entry in `org/critical_paths/change_management/` and names its
blast radius, per CLAUDE.md's hard stops. A block-list write from the Infosec page is confirmed to tolerate
out-of-Terraform writes before it ships (brief V.8).

## SURFACE MANIFEST

| id | surface | what it is | depends on | outcomes |
|---|---|---|---|---|
| S1 | repo and shell | `mcportal` repo, submodule wiring, sidebar shell in Andrew's order, design law | G-REPO, NFRA_OPALAI C2 | FWD-3 |
| S2 | owner gate | server-side exact email match on every page and handler; `/sprint` exception | the ALB default sign-in | FWD-2 |
| S3 | serving | the gateway serves the built bundle at `/` and the admin handlers | S2 | FWD-1..13 |
| S4 | grant writer | the separate writer function, its one invoke grant, its own ALB-header verification and owner config, its own audit record | S2, the grant store, G-LEDGER | FWD-1 |
| S5 | MCP Server: Entitlements | per-person data grant and tool permissions, presets, revoke-all, history | S4, S6 | FWD-1 |
| S6 | tiers and tool lists in the table | enforcement reads the table per call; the flat files retired in the same release (ENRICHMENT) | G-OPLGTW | FWD-10 |
| S7 | audit and revert | Recent Changes, revert-as-a-write | S4 | FWD-4 |
| S8 | Home | six cards under one verdict, each the header number of its page | every page | FWD-3 |
| S9 | Operations Report | the published sprint HTML framed, with its archive | `/sprint` | FWD-5 |
| S10 | User Management and Demo | both levels, disable-first, demo issue and revoke | the auth function, C7 | FWD-6, FWD-7 |
| S11 | User Analytics | the session-analytics rollup and charts, demo excluded by default | nightly rollup 1 | FWD-8 |
| S12 | MCP Server: Properties, Tool Library, Usage, Controls | the catalog view, the call log, the kill switch, the person block | NFRA_MCPINDEX's catalog, the audit lake | FWD-9, FWD-10 |
| S13 | Health Check | the monitor's published status, grouped as the email is; re-run | NFRA_REPORT | FWD-11 |
| S14 | Cost | the cost table, the Ramp sync, the mapping, charts | nightly rollup 3, C9 | FWD-12 |
| S15 | Infosec | firewall counts, suspicious IPs, block and unblock, scan score | nightly rollup 2, C10 | FWD-13 |

**Gates, each an act a named holder can take on demand:**
- **G-OPLGTW:** Andrew's word on amending NFRA_OPLGTW's contract and adapter for C6's record types. It is carried in
  the same call as NFRA_OPALAI's G-MOVE. Holder: Andrew.
- **G-REPO:** create `Opal-Capital/mcportal`. Holder: `0.0.0_AB_MSTR~Z`, on Andrew's 2026-09-17 word.
- **G-PUSH:** every DEV and PROD push. Holder: `0.0.0_AB_MSTR~Z`, on Andrew's word.
- **G-LEDGER:** a change-ledger entry before any act on the ALB, the grant table's IAM or the auth function. Holder:
  the acting seat.
- **G-SYNC:** the first Ramp sync runs under Andrew's own sign-in. Holder: Andrew, at a time he picks.

## Ground truth measured at authorship (2026-09-24, repo only)

- The ALB default action is Microsoft sign-in for every path not explicitly bypassed, and `alb.tf:210` names it "the
  future GUI path". The Claude-client bypass rules begin at `alb.tf:222`.
- The gateway application, including `sprint_view.py`, `access_state.py`, `entitlements.py`, `identity_scope.py`,
  `blocklist.py` and `revocation.py`, is at `infra/aws/ec2/opal-gateway/app/`. It is about to move into `opal_ai`
  under NFRA_OPALAI.
- No `mcportal` repo, registry row or resource exists (GitHub unread for `mcportal`; the registry has no row).

## BRIEF COVERAGE

Denominator: **22 headings** (`git show 8d1f5c362b:<brief> | grep -cE '^#'`).

| headings | n | disposition | where |
|---|---|---|---|
| title; ANDREW'S WORDS | 2 | CARRIED | Authority |
| PART I | 1 | CARRIED | ENDPOINT |
| O1 | 1 | CARRIED | FWD-3, FWD-4, S8, S7 |
| O2 | 1 | CARRIED | FWD-2, FWD-5, S9 |
| O3 | 1 | CARRIED | FWD-6, C7, S10 |
| O4 | 1 | CARRIED | FWD-7, C7, S10 |
| O5 | 1 | CARRIED | FWD-8, S11 |
| O6 | 1 | CARRIED | FWD-9, S12 |
| O7 | 1 | CARRIED | FWD-1, C4, C6, S4, S5 |
| O8 | 1 | CARRIED | FWD-10, S12 |
| O9 | 1 | CARRIED | FWD-11, S13 |
| O10 | 1 | CARRIED | FWD-12, C9, S14 |
| O11 | 1 | CARRIED | FWD-13, C10, S15 |
| O12 | 1 | CARRIED | FWD-2, C2, S2 |
| PART II | 1 | CARRIED | Scope and evidence boundary; the admin-handler home moved by C3 |
| PART III | 1 | CARRIED | the ACCEPT lines of FWD-1..13 |
| PART IV | 1 | CARRIED | C2-C8 cite its findings 1-12 |
| PART V | 1 | CARRIED | V.1 -> C8; V.2 -> C1, G-REPO; V.3 -> C3 (ruled); V.4 -> C4; V.5 -> C6; V.6 -> C7; V.7 -> C8; V.8 -> C10; V.9 -> C9, G-SYNC; V.10 -> C10; the build order -> Canonical handoff |
| PART VI | 1 | CARRIED | Ground truth |
| PART VII | 1 | CARRIED-AS-OPEN | Evidence boundary; VII.1, VII.2 settled and carried in FWD-2, FWD-8 |
| REFS | 1 | CARRIED | inputs to C2-C8 |

Sum: 2+1+12+1+1+1+1+1+1+1 = **22**.

## Acceptance matrix

| id | acceptance | outcome |
|---|---|---|
| A1 | one colleague's data grant narrowed from the Entitlements tab; their next MCP call answered within the new limit and no wider; widened back; both writes in Recent Changes with before and after | FWD-1 |
| A1n | NEGATIVE ARMS of C4, each refused before any store call: a write reaching the writer with no owner header; with a valid header for a non-owner; with an owner header past the window; and a direct `sts:AssumeRole` from the gateway role on the operator role | FWD-1 |
| A2 | a second signed-in Opal account refused on every page and every write handler (one request per handler, denominator printed); `/sprint` served to it | FWD-2 |
| A3 | each Home card's number equal to its page's header number on the same load | FWD-3 |
| A4 | one write of each kind reverted, the state after revert equal to the state before the write | FWD-4 |
| A5 | today's and one earlier Operations Report rendered on desktop and phone widths | FWD-5 |
| A6 | one partner user onboarded, edited, disabled (sign-in refused, history kept) and confirmed-deleted | FWD-6 |
| A7 | one demo login issued in under a minute, used once, revoked, refused after | FWD-7 |
| A8 | for one firm, the never-signed-in list, with demo users excluded by default | FWD-8 |
| A9 | the Properties and Tool Library tabs matching the catalog; an unclassified tool flagged | FWD-9 |
| A10 | Usage matching the audit lake for one day; one person blocked and unblocked; the kill switch thrown and restored in a quiet window, each on the very next call | FWD-10 |
| A11 | the Health page and that day's email compared row by row, zero disagreements; one re-run | FWD-11 |
| A12 | last month's non-AWS spend by purpose from the page, the manual rows marked | FWD-12 |
| A13 | one address blocked and unblocked from the page, both recorded | FWD-13 |

## Canonical handoff

L5 is `2.0.0_SA_COO~O`'s. **FWD-1 is the thread, and round 1 builds it over its hops inside the Home shell:**
1. the repo and shell (S1, G-REPO);
2. the owner gate (S2) and serving (S3);
3. the grant writer (S4), with its negative arms (A1n);
4. the Entitlements tab (S5) over the DATA grant, and its audit rows (S7, the minimum for FWD-1's history);
5. one live change followed to a colleague's next MCP call, graded against A1.

**Which side of NFRA_OPALAI's G-MOVE round 1 is built on:** the gateway's CURRENT path. G-MOVE waits on Andrew's OPLGTW
word and has no date, so waiting on it would make this thread a wait. When the move lands, C6 of NFRA_OPALAI moves the
whole gateway tree with its history, and this project's modules go with it. They are carried, never rebuilt, and the
thread is not built twice. Only an order still OPEN at the move is re-cut.

Andrew's page order then governs the enrichment rounds: Operations Report, User Management, the rest of MCP Server,
Health Check, User Analytics, Infosec, Cost. S6 joins once G-OPLGTW is given. **Sequencing against NFRA_OPALAI:** S3 and S6 touch the gateway, which
moves into `opal_ai` under NFRA_OPALAI's G-MOVE. A cell that edits gateway code is cut against the path where the
gateway lives at issuance, and is re-cut if the move lands mid-program. The two projects' gateway cells are never
issued into the same round with overlapping paths (one issuer, `2.0.0_SA_COO~O`, holds both).

### v0.5 addendum (2026-10-08 ~20:4xZ, 1.0.0_SA_CTO~O) -- the control plane: the fabric seen, the gateway mapped and rated

**Input.** Andrew-direct ~18:4xZ at the laptop, point 4: "MC portal becomes the control plane" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_184xZ_FIVE_POINTS_KIMMY_EFFICIENCY_ALYSSA_MCPORTAL_OPEN_CALLS_AGGREGATE.md`,
on the laptop; relayed to this seat by laptop `1.0.0_SA_CTO` msgs 107123 and 107181 through `0.0.0_AB_MSTR~Z` msg 31980;
this seat read the relay, not the record). The ask: un-park the project and cut this addendum. The brief is
`docs/briefs/mcportal-control-plane-brief-20261008.md` @bdeea1aefc (`4.0.0_SA_CRO`, laptop), with the gateway census
`org/tier1_exec/4.0.0_SA_CRO/deliverables/GATEWAY_CHANNEL_MAP_20261008.md`, both read whole from origin CLOUD a8689cb259.

**Un-park.** The project is un-parked by his word. Its old un-park condition (the Alyssa sitting, G-CLOSE) no longer gates
the control-plane work. G-CLOSE itself stays held: Andrew held Alyssa's close run until gateway r29 is live (~20:0xZ,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_200xZ_OPLGTW_THREE_CALLS_RECS_APPROVED_ROUND32_FWD10_13_ALYSSA_HOLD.md`).

**What this reverses.** Scope listed "a Fabric page" as NOT this project's (brief Part II of 2026-09-17). His word of today
makes the fabric pages this project's. The other exclusions stand.

**Endpoint.** FWD-14 to FWD-19 above, one per brief outcome O1 to O6. O7 (pull a person off) is FWD-6 and FWD-10 as written;
O8 (who may reach which channel) is FWD-1. Neither is re-scoped. FWD-14 is the THREAD of this addition: one page, Andrew
signed in, real data from the activity store. DONE WHEN lines are confirmed by this seat under the 2026-09-24 goal licence,
as v0.1's were; Andrew may amend any line.

**Contracts added.**
- **C11 -- Read the stores; never re-collect.** FWD-14 to FWD-16 read the activity store
  (`s3://opal-313476888478-globgrph/fabric/activity/v1/`, writer `.tools/fabric-activity.py`, owner `4.0.0_SA_CRO`) and
  FWD-17 the open-calls cluster copy (`.../fabric/open-calls/v1/`, writer `.tools/open-calls.py`). The portal holds a read
  grant on those two prefixes only, Terraform-applied under C10. No page writes either store except FWD-17's close, which
  goes through the open-calls writer and never edits the file.
- **C12 -- Live on open, with age.** "Streaming" reads as live when the page is opened or refreshed (C8: no alert, no
  checker, no push). Every figure prints the time of its source record. A box with no record in the window reads "not
  reporting". Site Z writes no activity record today (brief Part IV.1): installing the hook here is a precondition of
  FWD-14's four-box read and is placed with `0.0.0_AB_MSTR~Z`, not built by this project.
- **C13 -- Overlap risk is data.** The FWD-15 rating is a function of the surface kind (Terraform, code, registry, tool,
  record) and whether `org/critical_paths/.open_deploys/` on any box names that surface. The kinds and the rule live in one
  versioned file the page reads; the rule is tested against a planted Terraform overlap and a planted shared-log overlap.
- **C14 -- Git state from records, never from a guess.** FWD-16 reads commit records (activity store), box branches
  (`origin/box/*`) and integration records as they exist. Push, fetch and integration-refusal events have no readable
  home today (brief Part IV.2); the page shows "not recorded" for them until one exists, and giving them one is
  `4.0.0_SA_CRO~A`'s GitOps work, not this project's.
- **C15 -- The map is generated.** FWD-18 is built from the gateway's own definitions at the deployed commit:
  integration specs, the tool class table, `destructive_ops.py`, `refs/DATA_CATALOG.yaml`, and the REST route table. No
  hand-kept list. A tool present in the code and absent from every class table shows as "unclassified" (cf. NFRA_OPALAI row
  Z-S62, where exactly that refused a live tool). Field reach is shown where a contract states it (Schwab, Black Diamond,
  the catalog) and as "whatever the user's mailbox/files hold" for Microsoft 365 tools.
- **C16 -- Ratings: proposed scale, stored, unenforced.** The scale is the brief's R0 to R4 (R0 public or vendor market
  data; R1 internal operational metadata; R2 firm-confidential aggregates; R3 client PII or client financial rows; R4 acts on
  a person's or the firm's behalf). The scale and every channel's value live in one versioned data file beside the
  gateway's catalog, owned by this project's CTO. A channel added without a value reads "unrated". No code path reads the
  rating to allow or deny; any policy on a rating is NFRA_OPLGTW's and needs Andrew's word.

**Surfaces added.** S14 control-plane page (FWD-14 to FWD-16); S15 open-calls page (FWD-17); S16 gateway map and ratings
page (FWD-18, FWD-19). Each sits behind C2's owner gate and is served under C3.

**Acceptance added.** A14: one box's projects named from the page and matched to the store; a not-reporting box reads so.
A15: a planted Terraform overlap rated above a planted shared-log overlap. A16: a box with work off the trunk shown so the
same day. A17: one call closed from the page and read back from that box's list. A18: one channel's reach read on the page
equals the code. A19: an unrated channel reads "unrated"; the page and the stored file agree.

**Order.** Andrew called the fabric view "the more immediate": the next round builds FWD-14 end to end first, then
FWD-15 to FWD-17, then FWD-18 and FWD-19. The FWD-1 thread's open round-3 orders are re-read by the issuer before any cut.

**Sign-off.** ENDPOINT and CONTRACTS change. The ratified-text half re-opens for the CVO signing for `3.0.0_SA_CVO~O`. The
brief half: the laptop `4.0.0_SA_CRO` wrote the brief (CLAUDE.md rule 27, PROPORTIONATE SIGN-OFF).

### v0.6 addendum (2026-10-12 ~08:5xZ, 1.0.0_SA_CTO~Z) -- CONTRACT C17: the git-state read is bounded

**Input.** `2.0.0_SA_COO~MP` msg 33456 and row Z-S38 @f8c46aa826. The live Git state cold read was 25.1 s against R-13's 30 s
bar (3.9 -> 10.6 -> 16.7 -> 21.8 -> 25.1 s over three days). The handler is unchanged since MP-s-1 (`604ea0e089`).

**Measured by this seat (08:4xZ).** The gitstate history holds 3,294 keys: laptop 1,332, dell1 680, dell2 675, sitez 607.
That is 4 `latest.json` keys and 3,290 history keys, written at about 840 to 1,200 a day.

**Cause, read from `admin_fabric_gitstate.py` at HEAD.** `_refused()` scans each box's WHOLE history newest-first and stops
only at a refusal. With no refusal on record (inferred from the curve, not counted), every cold read fetches every body every
box has ever written. The cold read is therefore linear in total history and crosses 30 s at about 4,000 keys, which
is today. The cache (cap 20,000) hides this only until a restart. `first_seen` and the listing are bounded in time or
small, so they are not the driver.

**Endpoint.** Unchanged. FWD-16 stands as written.

**C17 -- Bounded read.** A cold read of FWD-16 fetches a number of bodies that does not grow with history length:
- **The listing** starts at the window: `StartAfter` is the box's `<cutoff stamp>` key (`WINDOW_HOURS`), so no key older
  than the window is listed.
- **`integration_refused`** is the newest refusal within the window that is NOT superseded. The scan runs newest-first and
  stops at the first `integrate` pass of EITHER outcome, or at the window boundary:
  - rc != 0 gives that refusal as {at, note};
  - rc == 0, or reaching the boundary, gives "not recorded".
  The response states this basis beside the field, the way `trunk.basis` states its basis. A refusal that a later successful
  integrate superseded is no longer where the work is, so it is not shown.
- **`first_seen`** stops early, per box, newest-first within the window: it stops at the first record whose trunk head
  differs from the newest head.
- **Writes.** The gateway still writes nothing. The producer `.tools/fabric-gitstate.py` (`4.0.0_SA_CRO`'s writer) is not
  touched.

**Cell (one, issued by `2.0.0_SA_COO~MP` as one issuance under the addendum path, spine L10 -> L6, "new cells for an
addendum"). The frozen round-N decomposition is untouched.** It edits `infra/aws/ec2/opal-gateway/app/admin_fabric_gitstate.py`
and its test. It is released on the live gateway ref at issuance under a never-widen pair: the release moves a served surface,
so the class is WORLD, plus the NEVER-2 ledger. At most three criteria:
1. A planted stub store at 1x and 10x history, with the trunk moved inside the window and no refusal, gives EQUAL
   `get_object` counts.
2. A planted refusal that a later rc == 0 integrate superseded reads "not recorded"; a planted refusal newer than every
   integrate reads {at, note}.
3. On the served release, the on-host cold `_compute` prints its body-fetch count and a time at or under 10 s.

**Interim.** Until the release lands, a breach shows only on the FIRST read after a gateway restart. The warm cache serves
every later read. No stopgap is ruled.

**Sign-off.** CONTRACTS only, and the ENDPOINT bytes are unchanged. The sign-off binds to the ENDPOINT hash (v3.19), so no
delivery is withheld. `3.0.0_SA_CVO~Z` reads C17 at the round-N analysis.

### v0.7 addendum (2026-10-12 ~21:0xZ, 1.0.0_SA_CTO~Z) -- FWD-20: the gateway breakdown is the FIRST outcome cut

**Input.** Andrew-direct ~20:5xZ, item 2, VERBATIM: *"I wouldnt close this project (OPLGTW) until I have seen a full breakdown
of the vendors/channels available via the gateway, what tools/indexes exist for each, and current state of entitlements. The
easiest way to manage this would be via the MCPORTAL, and this is what I think should be the first distinct outcome of the
MCPORTAL project."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261012_205xZ_SITEZ_PORTFOLIO_SEVEN_PROJECT_RULINGS.md`.

**Endpoint.** FWD-20 is ADDED (ENDPOINT above). FWD-18's map (channels, tools, reach) is its first two parts. The third part,
who holds a grant today, reads the stores FWD-1 already writes. FWD-18 and FWD-19 stand as written, and FWD-20 subsumes
FWD-18's page; one page serves both.

**Order.** FWD-20 is cut AHEAD of every other open order. The four staged close runs (MP-x-5, MP-q-1, MP-v-2, MP-c-2) keep
waiting on Andrew's acts and do not gate it.

**Contracts.** C15 applies unchanged: the map is generated from the deployed gateway's definitions. C16's ratings are shown
where they exist and read "unrated" where they do not. Reading the grant stores is a READ under C2's owner gate. No page writes
anything for FWD-20.

**Closes NFRA_OPLGTW.** Andrew's reading of this page is the condition he set for NFRA_OPLGTW's close.

**Sign-off.** ENDPOINT changes, so the ratified-text half re-opens for `3.0.0_SA_CVO~Z`. The brief half is Andrew's own word
recorded verbatim (PROPORTIONATE SIGN-OFF).

### v0.8 addendum (2026-10-14 ~02:5xZ, 1.0.0_SA_CTO~Z) -- FWD-21 control and depth per person; FWD-22 Claude account and usage per box; CONTRACT C18

**Input.**
- Andrew's site Z memo 2026-10-13, verbatim in `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_SITEZ_20261013.md`
  section 1.1 (direction Z2: write FWD-21 after FWD-20 ships; FWD-20 shipped as MP-z-5 @64b3e54658).
- Andrew-direct ~20:4xZ at dell2, carried by XB-20261013T202846Z-111f, row Z-S47.
- The laptop CTO's ruling @f469cb665f: yes to control; writes stay Andrew-only.

**Endpoint.** FWD-21 and FWD-22 are ADDED. FWD-21 composes FWD-1 (one colleague's access changed from the page) and
FWD-10's stop, pulled forward. FWD-3 to FWD-13 not named here stay deferred behind FWD-21.

**C18 -- One writer for per-person tool, channel and tier access: the grant store.**
- **Today:** tool and tier admission lives in two deploy-time files (`identity_tool_allowlist.txt`, and the rosters in
  `deploy-to-ec2.sh`), which change only by a gateway release. The data grants live in `gateway-access-state-table`,
  written by the existing grant writer.
- **The choice:** a per-person tool, channel or tier change is a NEW record kind in the SAME grant store, written by the
  SAME grant writer, and honoured on the next call. It is not a release raised from the panel.
  - The reason is Andrew's stated need: "otherwise it's just too difficult to operate in the fast moving environment".
  - A release per edit is the slow path his words rule out.
- **The deploy-time files stay as the FLOOR.** A store record can narrow what the floor admits for a person. It widens
  beyond the floor only for a tool the floor already lists for some principal, never for a tool the deployed gateway
  does not serve.
- **Rollback per change:** the FWD-4 change history's before/after, re-written through the same writer.
- **Rollback of the mechanism:** delete the new record kind, and the floor governs exactly as today.
- **No new resource name is typed:** any new store key or name is `lib/opal_naming.py` output (rule 30).
- **The gateway side is NFRA_OPLGTW's:** its contract C-PERSON (PRD v2.9) has `decide()` read this record kind. That
  reader is an OPLGTW cell, and FWD-21's first WRITE cell (F2) waits on it. The read-only view (F1) does not.

**Order.** FWD-21 first, then FWD-22. FWD-22's first cell is a read only. Both start after Andrew's FWD-20 sitting is
listed; neither waits on it.

**Sign-off.** ENDPOINT and CONTRACTS change, so the ratified-text half re-opens for `3.0.0_SA_CVO~Z`. The brief half is
the CRO's site Z alignment report on Andrew's memo plus the 204xZ record, accepted as written (rule 27, PROPORTIONATE
SIGN-OFF).

### v0.9 addendum (2026-10-15 ~19:4xZ, 1.0.0_SA_CTO~Z) -- the gateway finish by EOD Fri 2026-10-16: /gateway segmented by bucket and by vendor/firm

On the CRO plan `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_FINISH_PLAN_EOD_20261016.md` @6cc033c818 and Andrew's GO (msg 34543), whose words are carried in full in NFRA_MCPINDEX PRD v0.17. His
words for this project: "COO~MP there doing passes on the /gateway page of the mcp.opalinvest.dev making sure everything is
extremely legible, clean, and well-designed, using the opalinvest.com website design fixtures, as well as making sure that
everything is readable by human eyes and not wrapped or squished on text and segments. The most important thing is really
that each displayed tool segment is very clearly segmented, i recommend this being by bucket, and in the case of
opal-data-assets, by client/vendor pairs."

1. **The HOLD is lifted for workstream PE (the /gateway view) by Andrew's word.** The rest of the project stays HELD as
   ruled (msg 34212).
2. **Segmentation is CONTRACT C-GROUP (MCPINDEX v0.17) and nothing else.**
   - One segment per `bucket`. Inside opal-data-assets and opal-data-bd, one sub-segment per (`vendor`, `firm`) pair.
   - `multi`, `none` and `unresolved` render as their own labelled sub-segments, never folded into a firm.
   - The view builds on a C-GROUP fixture now and switches to the live catalog when the first C-GROUP catalog release
     lands.
3. **Design:** the opalinvest.com design fixtures. No wrapped or squished text in any segment at desktop or narrow width.
4. **Proof:** one rendered screenshot per segment at desktop and narrow width, read by a seat, on the live catalog. The
   human read is Andrew's sitting (21d9), which nothing here waits on.
5. **Done by 2026-10-16 ~22:00Z.**

CONTRACTS-side; ENDPOINT unchanged.

### v0.10 addendum (2026-10-20 ~17:3xZ, 1.0.0_SA_CTO~Z) -- ENDPOINT: add and subtract a person's access per channel at mcp.opalinvest.dev/opalgateway (Andrew-direct)

**Andrew, verbatim** (`1.0.0_SA_CTO~Z` terminal; record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_16xxZ_MCPORTAL_ENTITLEMENT_EDITING_AND_MCPINDEX_VENDOR_TABLE_LINKING.md`
@790786dcfc):

> "something id like threaded into this is the ability to add and subtract entitlements for various channels with ease for users
> at the mcportal itself, i.e. at mcp.opalinvest.dev/opalgateway. let's make sure that functionality is possible and put into the
> build there by COO~MP"

**Brief:** `4.0.0_SA_CRO~Z`, `docs/briefs/mcportal-entitlement-add-subtract-brief-20261020.md` @542fb0983f (midstream). Its
findings F1-F8 are the substrate:
- subtract is built and not served (the API is unmounted, and the writer is an old build);
- add has no path for the data family;
- `portal_channels` has no control.

**The route:** `/opalgateway` is NEW. It is Andrew's own URL (brief Part V), and it is the per-person access page. `/gateway`
stays the read-only map, and `/people` keeps its list and links into `/opalgateway`.

#### ENDPOINT -- seven new outcomes (brief O1-O7; each proven by a served act on demand)

- **FWD-23 -- See a person's reach.**
  - For each person, the page shows the tier, profile, data grant, per-person record, and the resulting channels and tools.
  - The page reads the gateway's own admission chain, never a re-typed rule.
  - Proof: for 2 people, the page's tool set equals the gateway's per-call decision, read in process.
- **FWD-24 -- Subtract one channel or one tool in one act.**
  - It takes effect on the person's next call.
  - Proof: a driven subtract, then that person's next call to that tool is refused, then the record's revision is read.
- **FWD-25 -- Restore in one act.**
  - Proof: the restore after FWD-24, then the next call is admitted.
- **FWD-26 -- Add a channel the person lacks, in one act, labelled WIDENING before it lands.**
  - The writer refuses a widening that has no recorded sign-off.
  - The data family needs a grant layer. The `client_*` tools for a non-master person ride the per-firm client grant shape:
    NFRA_OPLGTW round 48, Andrew's yes for Alyssa and Menachem @50bd4a33b4.
  - `portal_channels` gets its control on the grant (brief F7).
- **FWD-27 -- Stop and restore a person, in one act each.**
  - The page refuses to stop the last master admin, so the owner cannot lock himself out (brief F5 risk).
- **FWD-28 -- One audit list.**
  - Every add, subtract and stop is shown with who, when, before and after, for every person, in one place.
- **FWD-29 -- What the page shows ON is what the gateway admits.**
  - Proof: after every FWD-24 to FWD-27 act, one call through the served gateway agrees with the page's switch.
  - A switch that is on while a different gate refuses is a FAIL (brief F5 and O7).

#### Placement

- **NFRA_MCPORTAL (`2.0.0_SA_COO~MP`):**
  - the `/opalgateway` page;
  - its switches and the WIDENING label;
  - the audit list;
  - the last-admin guard;
  - the grant-writer Lambda deployed from source through Terraform, which carries `set_person_access` (brief F4);
  - `portal_channels` in the writer's change shape (brief F7).
- **NFRA_OPLGTW (`2.0.0_SA_COO~O`):**
  - mounting `admin_people_access.routes` behind the owner gate (brief F3), in its next batched release under never-widen;
  - the per-firm client grant shape (round 48);
  - FWD-29's single admission rule, so that `person_access` and the grant agree.
- **Round order:** the thread first, which is subtract then restore for one person (FWD-24/25 with FWD-29). That needs only the
  mount and the writer deploy. Add (FWD-26) follows the round-48 grant shape.

ENDPOINT changed (FWD-23 to FWD-29 added): the ratified-text half re-signs.
