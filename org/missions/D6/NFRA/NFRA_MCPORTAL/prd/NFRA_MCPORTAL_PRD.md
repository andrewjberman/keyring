```json
{
  "project": "NFRA_MCPORTAL",
  "directive": "D6",
  "fabric": "site-z",
  "prd_version": "v0.1",
  "step": 4,
  "brief_ref": "docs/briefs/mcportal-tech-ops-dashboard-brief-20260917.md@8d1f5c362b",
  "endpoint_outcomes": [
    "FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7",
    "FWD-8", "FWD-9", "FWD-10", "FWD-11", "FWD-12", "FWD-13"
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
```

## CONTRACTS

**C1 -- Own repo, graded like the parent.** `Opal-Capital/mcportal` is created by `0.0.0_AB_MSTR~Z` on Andrew's
2026-09-17 word (gate G-REPO). It is wired into the workspace as a real submodule under NFRA_OPALAI's C2 mechanism
(`.gitmodules`, checkout-path init, the lane file before any hook, the parent's gates, and CI). It has DEV and PROD
branches, and only MSTR pushes. It uses React, Vite, TypeScript and bun, and follows the portal's current design law
(`portal/DESIGN.md`, 2026-09-11). It starts clean on that law.

**C2 -- Only Andrew, checked on the server, on every page and every write.** The load balancer's default Microsoft
sign-in (`alb.tf:210`, "the future GUI path") admits the tenant. Then a server-side exact match on
`MASTER_ADMIN_EMAILS` (default Andrew's address) runs on every page request and every write handler. A hidden menu
never counts as access control. The one exception is `/sprint`, which stays open to any signed-in Opal Microsoft
user. The Claude-client paths (`/mcp`, the OAuth paths) are untouched, and no rule on them changes.

**C3 -- Where it is served: from the gateway process, behind that sign-in** (ruled by this seat on brief Part V.3).
The built pages are static assets served by the gateway application at `/`. The admin API handlers live with the
gateway (in `opal_ai`, beside the guard chain), not in a second service. **Why:** C2's server-side check then lives
in one process, and a second service would be a second identity boundary to keep in step. The S3 alternative needs its
own sign-in in front of it. The `mcportal` repo holds the pages. The gateway's deploy ships the built bundle pinned by
the `mcportal` commit, recorded in the deploy manifest beside the `opal_ai` commit.

**C4 -- The gateway still cannot grant itself access.** Grant writes go through a path that holds the
`opal-gateway-access-admin` role, invoked only for a request that passed C2 with Andrew's verified identity. The
gateway's own role stays IAM-blocked from the `POLICY#` partition (`access_state.py:16-19`). Every grant write keeps
the store's optimistic revision check. A revoked record stays a tombstone, never a delete.

**C5 -- Every dashboard write is audited and revertible.** Each write records who, when, what, before and after in the
grant store's `operator_audit` record type, or in an equivalent record for non-grant tables. The Recent Changes view
reads those records. A revert is itself a write with its own audit row. Hard delete of a user is a confirmed second
step after a disable.

**C6 -- Tiers and per-person tool lists move into the grant table. The kill switch and blocklist stay files.** The
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
| S4 | grant writer | the access-admin path, verified-identity only | S2, the grant store | FWD-1 |
| S5 | MCP Server: Entitlements | per-person data grant and tool permissions, presets, revoke-all, history | S4, S6 | FWD-1 |
| S6 | tiers and tool lists in the table | enforcement reads the table per call; the flat files retired in the same release | the gateway | FWD-1, FWD-10 |
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
| A1 | one colleague's tool permission narrowed from the Entitlements tab; their next MCP call refused within the new limit and no wider; widened back; both writes in Recent Changes with before and after | FWD-1 |
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
3. the grant writer (S4);
4. tiers and tool lists read from the table (S6);
5. the Entitlements tab (S5) and its audit rows (S7, the minimum for FWD-1's history);
6. one live change followed to a colleague's next MCP call, graded against A1.

Andrew's page order then governs the enrichment rounds: Operations Report, User Management, the rest of MCP Server,
Health Check, User Analytics, Infosec, Cost. **Sequencing against NFRA_OPALAI:** S3 and S6 touch the gateway, which
moves into `opal_ai` under NFRA_OPALAI's G-MOVE. A cell that edits gateway code is cut against the path where the
gateway lives at issuance, and is re-cut if the move lands mid-program. The two projects' gateway cells are never
issued into the same round with overlapping paths (one issuer, `2.0.0_SA_COO~O`, holds both).
