# Brief: add and subtract a person's access per channel, at the MC Portal (midstream, NFRA_MCPORTAL)

**Author:** 4.0.0_SA_CRO~Z, 2026-10-20 ~17:3xZ (1:3x PM ET). **Mode:** `/brief-create --midstream`.
**Order:** Andrew-direct ~16:xxZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261020_16xxZ_MCPORTAL_ENTITLEMENT_EDITING_AND_MCPINDEX_VENDOR_TABLE_LINKING.md`
@790786dcfc. **Asked by:** 1.0.0_SA_CTO~Z (ferried message, 2026-10-20T17:08:34Z). The brief folds into 2.0.0_SA_COO~MP's
workstream.

**Andrew, verbatim:** "the ability to add and subtract entitlements for various channels with ease for users at the mcportal
itself, i.e. at mcp.opalinvest.dev/opalgateway".

## PART 0 -- How the blind constraint was honoured, and where it bent

**Not read:** NFRA_MCPORTAL's or NFRA_OPLGTW's task orders, and their phase and blocking fields.

**Read:**
- the served reality: the gateway's mounted admin routes at HEAD, which equals the served release for these files, measured
  2026-10-19;
- the deployed grant-writer Lambda's code identity;
- the portal bundle the last portal release deployed;
- the source of the modules the CTO named.

**Where it bent:**
1. **Task-order labels.** The modules' own docstrings and commit subjects carry task-order labels (MP-pd-3, MP-pd-4, OG-cl-7).
   I read them as code, not as the plan, but they name work in flight.
2. **Deploy ledger.** I read one portal deploy entry (MP-pf-9, 2026-10-16) to learn which bundle is served.
3. **My own prior audit.** My gateway audit of 2026-10-19 (parts 1-3) and my employee roster of 2026-10-19 are my own earlier
   findings, not this project's branch. Its grant mechanics shape Part IV.
4. **The CTO's list.** The CTO's ask named the six surfaces to grade, so the inventory follows the CTO's list rather than a
   blind census.

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (FWD-1 shape).** Andrew, signed in at the portal, opens one staff member (for example Alyssa Keith).
- He switches one channel off.
- The next call that person makes to a tool in that channel is refused.
- He switches it back on, and the next call is admitted again.

Each act shows who did it and when.

### O1 -- The owner sees, per person, every channel and tool they can reach today, with how they reach it
For each person: the tier, the profile, the data grant, any per-person record, and the channels and tools that result. It is
the same answer the gateway's own per-call chain gives, not a re-typed rule.

### O2 -- The owner subtracts one channel, or one tool, from one person in one act, and the person loses it on their next call
This is a narrowing: no review is needed, and it is undone by O3.

### O3 -- The owner restores a channel or tool he subtracted, in one act

### O4 -- The owner adds a channel a person does not reach today, in one act, and the act states it is a WIDENING before it lands
For example, opal-data-assets for the operations team, per the roster of 2026-10-19.

### O5 -- The owner stops a person entirely, and restores them, in one act each

### O6 -- Every add, subtract and stop is listed with who, when, and the before and after, for every person, in one place

### O7 -- A person granted a channel finds that the tool they now see answers them, not a refusal from a different gate
Today an "add" can land in one layer while another layer still refuses; see Part IV F5.

## PART II -- WHERE THE BOUNDARY SITS

- **Owns.** NFRA_MCPORTAL (2.0.0_SA_COO~MP): the portal pages and their calls to the admin API.
- **Relies on: NFRA_OPLGTW (2.0.0_SA_COO~O).**
  - the gateway's admin API routes;
  - the per-person record's enforcement (`data_entitlement.person_denial` and `person_widens`);
  - the data-grant model;
  - the grant-writer Lambda's actions, deployed through Terraform.

  Mounting a route and deploying the writer are NFRA_OPLGTW's acts.
- **Relies on: NFRA_MCPINDEX (2.0.0_SA_COO~MI).** What a "channel" is: the catalog's grouping of tools into buckets, stores
  and integrations. A channel id that moves under a saved per-person record changes what that record denies.
- **Not in this project:**
  - **the tier rosters:** Secrets Manager `gateway/principals/rosters`, written into the gateway's `.env` at deploy;
  - **the identity tool allowlist:** a file in the release.

  Both change only by release. Whether they move to the portal is Andrew's call, not this brief's.
- **Not in this project: the Schwab data grant's dimensions.** These are masters, datasets, accounts, columns, dates and
  operations. They are served today by the MCP Server > Entitlements page. "Channel" in Andrew's words is the coarser grain.

## PART III -- THE QUALITATIVE BAR

- **Ease.** Andrew changes one person's access to one channel without opening a terminal, a secret, a release or an agent.
- **Effect.** The change takes effect on that person's next call, and the person's next answer shows it.
- **Widening is visible.** The page never lets a widening pass as a narrowing. Every act that gives a person reach they lacked
  says so before it lands.
- **Honest switches.** What the page shows as switched on is what the gateway admits. A switch that is on while the gateway
  still refuses is the failure this bar exists to catch.

## PART IV -- THE SUBSTRATE (findings, each measured)

| # | Surface the CTO named | Built | Served | Finding |
|---|---|---|---|---|
| F1 | `/gateway` page | yes | yes (the portal bundle from the 2026-10-16 release) | read-only: channels, tools, indexes and holders; no write control |
| F2 | People page (`/people`) | yes | the page is served; its access panel is in the served bundle (c66ca82952) | `GET /api/admin/people` is mounted and served; the panel's own API is not (F3) |
| F3 | `admin_people_access.py` (`GET`/`POST /api/admin/people/{tid}/{oid}/access`) | yes, in source | **no** | **not mounted**: `app/admin_api.py` routes list `/grants/*`, `/changes`, `/gateway/*`, `/people` and the rest, but not `admin_people_access.routes`. So the served panel's read and write would answer 404 |
| F4 | grant-writer Lambda `mcportal-grant-writer-lambda` | yes | **old build** | deployed 2026-10-11T20:32:52Z from ad17fa128f (CodeSha256 equals the function map's artifact hash). That build has **0** `set_person_access`. Source has the action since f40bf7dded5 (2026-10-14). Deployed actions: `narrow`, `widen`, `revoke` (and `register_tenant`) |
| F5 | `person_access` record (`tools_allow/deny`, `channels_allow/deny`, `stopped`) | yes | the enforcement is served; **0 records** exist (scan of `gateway-access-state-table`, 2026-10-19) | the record can **subtract** any channel or tool for anyone (deny wins, master_admin included). Its `allow` lists **widen only past the identity-scope floor** (`person_widens`: an Opal principal, a served tool), so they cannot open the data-grant family, the `client_*`, `schwab_*` or Black Diamond tools, or tier-gated write tools |
| F6 | `ops/schwab_entitlement_admin.py` | yes | n/a (an operator script, not a portal surface) | an operator-side admin for the Schwab grant. It is neither a page nor an API the portal can call |
| F7 | data grant (`principal_profile` + versioned `data_entitlement`) with `portal_channels` | yes | yes (3 active profiles) | the MCP Server > Entitlements page narrows and widens it through the deployed writer. Its change shape (`ScopeChange`) carries masters, datasets, accounts, dates, columns and operations, and **not `portal_channels`**; `portal_channels` is named nowhere in the writer's source |
| F8 | the `client_*` tools (opal-data-assets) | yes | yes | **no grant can admit them for a non-master person.** `allowed_tools()` derives only Schwab tools from a grant; `client_*` and `blackdiamond_list_fees` pass only for the `master_admin` tier (`TIER_ADMITTED_TOOLS`) |

**What one click needs (the gap), per act:**

| Act | Path today | Gap to one click | Never-widen consequence |
|---|---|---|---|
| Subtract a channel or tool (O2) | none served: the panel exists, but its API (F3) is unmounted and the writer (F4) is the old build | mount F3's routes, deploy the writer from source | **none: a narrowing.** The deny wins over every other gate. Risks: a channel id that later moves no longer denies (Part II), and a stopped Andrew locks the owner out of the data family |
| Restore (O3) | same | same | none beyond restoring what was held |
| Stop / restore a person (O5) | same | same | stop: none. Restore: re-opens exactly what the floor and grant allow |
| Add a channel the person lacks (O4) | **no path for most channels.** Bucket reads such as harvest, ETFs and portal are already open to every Opal principal (no add needed). The data family (`client_*`, `schwab_*`, Black Diamond) needs a profile and grant, and `client_*` needs a code change (F8). `portal_channels` has no page control (F7) | **(a)** a channel-level "add" that writes the right layer for that channel; **(b)** a grant dimension or rule that can admit `client_*` for a non-master person; **(c)** a `portal_channels` control on the grant | **WIDENING: Andrew's call and never-widen sign-off.** Each add names its blast radius: the tools it opens, for whom, and the rollback (the record's prior revision) |
| Audit every act (O6) | `/api/admin/changes` is served, reading the writer's own table | the per-person history is on the unmounted panel only | none |

**Canonical pattern.** This is the estate's existing shape:
- one writer (the grant-writer Lambda);
- an owner-gated admin API that never writes itself;
- per-principal records with revisions and optimistic checks;
- one shared admission rule (`admin_gateway_breakdown._admits`) reused by the people view.

The gap is wiring, plus one missing grant dimension. It is not a new mechanism.

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The portal page and the gateway agree on what a "channel id" is. A per-person record keyed by channel id is only as stable
  as the catalog's grouping.
- Every act that widens is distinguishable from one that narrows before it is written, and the writer refuses a widening that
  lacks its sign-off.
- The writer that serves the portal is the writer in source, deployed by Terraform; there are no hand deploys.
- Andrew decides whether "add opal-data-assets" for a non-master person is to exist at all (F8). The roster of 2026-10-19
  proposed it for Alyssa Keith and Menachem Goldstein.
- Andrew's URL `mcp.opalinvest.dev/opalgateway` is not a route: the portal's routes are `/gateway` and `/people`. The page he
  means needs naming.

## PART VI -- STATUS (NOT OUTCOME-BEARING)

| Claim | Measured |
|---|---|
| admin routes mounted: no `admin_people_access` | `app/admin_api.py` at HEAD, 2026-10-20 ~17:2xZ (HEAD equaled the served release for the audited files on 2026-10-19) |
| grant writer deployed 2026-10-11T20:32:52Z, CodeSha256 `894RI63/...` | `lambda get-function-configuration`, 2026-10-20 ~17:2xZ |
| that build has no `set_person_access` | `git show ad17fa128f:` the Lambda source, 0 matches |
| portal bundle with the access panel served | deploy ledger MP-pf-9 (mcportal c66ca82952, 2026-10-16), and the panel file present at that commit |
| 0 `person_access` records, 3 active profiles | DynamoDB scan, 2026-10-19 ~14:4xZ |

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- **Not exercised.** I did not open the served portal in a browser or call any admin route, so the 404 for the panel's API
  is inferred from the mount list, not observed.
- **Not read: whole-scope merge.** Whether the deployed writer's `narrow`/`widen` carries `portal_channels` through a
  whole-scope merge; the name is absent, but the behaviour is not read.
- **Not read: later portal releases.** Whether a portal release after 2026-10-16 changed the People page.
- **Not decided.** Whether tiers and the identity allowlist should become portal-editable. That is out of this project
  (Part II).
- **No order or count.** No sequencing, cells or effort; those are step 5.

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/mcportal-entitlement-add-subtract-brief-20261020.md
  PROJECT           NFRA_MCPORTAL (2.0.0_SA_COO~MP), midstream
  EXISTING PRD      org/missions/D6/NFRA/NFRA_MCPORTAL/prd/ (not re-read here)
  SIBLING PROJECTS  NFRA_OPLGTW (routes, enforcement, writer deploy), NFRA_MCPINDEX (channel ids)
  PRIOR ART         infra/aws/ec2/opal-gateway/app/admin_people_access.py, admin_grants.py, data_entitlement.py
                    (person_denial, person_widens, allowed_tools, TIER_ADMITTED_TOOLS);
                    infra/aws/lambda/mcportal/mcportal-grant-writer-lambda/lambda_function.py (set_person_access);
                    mcportal src/pages/people/PersonAccessPanel.tsx, personAccess.ts; src/pages/mcp-server/entitlements/
                    org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_EMPLOYEE_ROSTER_BUCKET_MAP_20261019.md (dc5a0b1b0b)
  MEASURED AT       2026-10-20 17:1xZ-17:3xZ (Part VI rows carry their own clocks)
```
