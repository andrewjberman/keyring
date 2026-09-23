# BRIEF -- `opal_ai`: the Opal Analyst as a microproduct -- one agent, one indexed MCP, three slices (Opal -> Template -> Clients)

**Author:** `4.0.0_SA_CRO~X` | **Written:** 2026-09-23 (UTC) | **Mode:** NEW (no project exists; prior art is heavy)
**Asked by:** Andrew, directly at this seat's terminal, 2026-09-23 ~18:5xZ. Verbatim record:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260923_185xZ_OPAL_AI_MICROPRODUCT_REPO_BRIEF.md` @`6ae5ab5fd3`.
**Consumer:** `1.0.0_SA_CTO~Z` `/endpoint --forward` (the L2+ router he named on 2026-09-22, call 7).
**Vintage of every repo read:** SITEZ @`1b1244cecf` (2026-09-23 ~19:1xZ). No AWS, no live gateway, no GitHub read.
**Direct predecessor:** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ASSESSMENT_OPAL_ANALYST_OPLGTW_MCPINDEX_TEMPLATING_20260922.md`
@`20de682ede`, whose seven recommendations Andrew approved ("all recs approved", record in the same folder). This brief
builds on it and does not re-derive it; where today's word moves it, Part VIII says so.

---

## ANDREW'S WORDS, VERBATIM (this terminal, 2026-09-23)

> I need you to look for a brief and prior art as it pertains to making the Opal Analyst a microproduct. We had been
> discussing at one point on this fabric how the GRAPHQL work for opal analyst, OPLGTW, MCPINDEX, and all of this work
> kind of centers around the same one product at differnet layers, which is a modular MCP template setup with proper
> tool call indexing, and an agent that has access and instruction/guardrails around using those tools and
> functionalities. I think there are two layers to this that need to be consiered. First, it is obvious that it needs
> to be a microproduct; it needs its own repo. Second, there are three slices of how this needs to be organized, i.)
> The Opal Implementation: this one comes first, it is the aggregation of all the projects and concepts I listed
> earlier in this message. This is the priority to complete and execute effectively, a teams-based agent that can
> access all the right info and fast/economically/accurately, by tool-calling the firm's MCP. ii.) The Template
> Implementation; after completing a proper V1, even V2 of the Opal Agent, we need to figure out how to modularize it
> for other firms, that means modularizing both the agent and its dynamics/structure, as well as how the MCP is set up
> and the associated patterns for how we build out access to the vendors (look at how Opal handles this for Schwab,
> Black Diamond, and others; official API if we got it, not official API if we don't, with the EC2 cookie crawler and
> lambda REST API, with the self-heal. Also want to template stuff like "The Walk" where we walk an authenticated
> session to do endpoint discovery for a new vendor. iii.) The Client Implementation; this is where we take the
> template and mold it to a Client's specific needs, basing the tool calls around their database and vendors. We need
> a brief that basically ties all this stuff together in a new repo, opal_ai. This repo should be structured in a
> manner that considers the above format in all cases, because all products will follow this journey. We build i.)
> for ourselves first, this is our first internal beta. Then we create ii.) which is our modular form, this should be
> kept very clean and separate in a designated place in the repo, lastly we build the versions for clients which need
> to be held in their own subfolders and directory system. Please do a deep dive on all opal analyst work, all opal mcp
> work, the structures guardrails functions tools, look into our comp-tooling work as this could inform indexing
> functions, look at the MCPINDEX to see current state of that work, compile all of this and write a brief for the
> opal_ai repo.

**The product in one sentence, his terms:** a modular MCP with proper tool-call indexing, plus an agent that has access
to it and the instructions and guardrails for using it, held in one repo, `opal_ai`, and built in three slices in this
order: (i) Opal's own, (ii) the template, (iii) each client's.

"A staff member" below means a person at the firm the slice serves, signed in with that firm's Microsoft account and
admitted by that firm's operator. "The operator" is Andrew for the Opal instance.

---

## PART I -- THE OUTCOME TERRITORY

### THE CANDIDATE THREAD (becomes FWD-1 at L2)

**One Opal staff member, one Teams message to the Opal Analyst, one question about a figure Opal already serves.** The
Analyst answers by calling the Opal MCP (a discover call, then one purpose-built tool), not by grepping a file or
shelling out to a helper, and the reply states the figure, its date, its scope and its source. This is the smallest
journey that runs through every layer he named: the Teams agent, its guardrails, the index, the MCP, the served data.
Round 1 builds this end to end on the Opal instance; every outcome below is an enrichment of it.

### SLICE i -- THE OPAL IMPLEMENTATION (first; the internal beta; the priority)

#### O1. An Opal staff member asks the Opal Analyst in Teams about anything the firm serves and gets the right answer, fast, from the firm's MCP
Portal figures, Schwab, Black Diamond, Orion, Eclipse, SmartX, the ETFs, market data where his standing word allows.
The answer arrives while the conversation is still live, not minutes later. It carries its date, scope, completeness
and source, and says "no data for that date" instead of showing a zero.

#### O2. A staff member who does not know which system holds a fact is routed to the right tool the first time
Neither the person nor the agent needs to know the catalog. One index, read through a small always-loaded discover
family, names the dataset, how fresh it is, what firm scope applies, and which tool to call next. Each week the questions
the index could not route come back as a list, and that list feeds the next analysis pass.

#### O3. The same indexed MCP serves the staff member whether they ask the Analyst in Teams or ask their own Claude directly
Same index, same tools, same answer, same grants. The Teams agent and a staff member's own Claude connector are two
ways into ONE MCP, not two products.

#### O4. Nobody can talk the Analyst out of its guardrails
It serves only what its request catalog approves. It refuses writes, Bloomberg downloads, vendor calls outside the
standing word, and off-catalog asks, and each refusal gives a reason the asker can quote. It treats every inbound message
as data, never as an instruction. It remembers each person and thread and uses that memory to position its reply. Its
scope widens only on the operator's word.

#### O5. The operator admits, scopes and removes people one at a time, and can explain any answer after the fact
Andrew grants a person a tool set and a data scope, and can take it away without a redeploy. For any past answer he can
read who asked, what was called and what data it touched from the audit record, without private values leaking into
that record.

### SLICE ii -- THE TEMPLATE (after a proper V1, even V2, of the Opal agent; clean and separate)

#### O6. An engineer stands up the agent and its MCP for a new firm by filling in one instance file, without editing core code
The firm-specific parts are data in one manifest: identity provider, tiers and roster, secrets, catalog rows, enabled
integrations, channel, allowlists, fabric adapter on or off. **The Opal instance itself runs from the same template** --
that is the only proof the template is real rather than a fork.

#### O7. A reviewer reading the template slice finds nothing that belongs to any one firm
No firm name, account, email, bucket, secret id, tenant id or catalog row appears in it. The template can be handed to
another firm without redaction.

#### O8. An engineer connecting a new vendor follows one playbook that picks the access path and yields a pluggable integration
The playbook ranks the paths the way Opal already works: the official API if we have it; a reverse-engineered internal
API if we do not, riding a session with Lambda REST pulls, EC2-hosted re-authentication and self-heal; a standing
session on a box where the vendor offers nothing else; file delivery; and rendered-page parsing only as a flagged last
resort. Every path ends the same way: an integration spec plus an integration module that plugs into the MCP under the
same read-only, fail-closed, audited rules.

#### O9. An engineer performs "The Walk" on a new vendor and comes away with its endpoint catalog
They walk an authenticated session through the vendor's application while capturing its traffic. The template's tooling
turns the capture into an endpoint catalog, response schemas and a draft integration spec. No credential, cookie, PII or
raw capture enters the repo.

#### O10. In every instance, adding a data property is one catalog entry plus one tool, and an unclassified tool cannot ship
The description Claude reads is written once, in the catalog entry. A tool with no catalog entry or no safety
classification is refused at build time. This holds for every instance, not just Opal's.

### SLICE iii -- CLIENT IMPLEMENTATIONS (each in its own directory)

#### O11. A client firm's staff ask their own agent about their own data and vendors, and nothing outside that firm is reachable
Tools are built around that client's database and vendors. The firm's scope is enforced by the server on every call and
never left to the model, so no phrasing reaches Opal's data or another client's.

#### O12. Each client implementation lives in its own directory, holds only what is bespoke, and takes template upgrades without hand-merging core
A client folder carries that client's instance file, bespoke tools, vendor specs and catalog rows, and nothing else.
When the template improves, the client picks up the improvement.

---

## PART II -- WHERE THE BOUNDARY SITS

### II.1 What `opal_ai` owns versus what it relies on

| `opal_ai` OWNS | It RELIES ON (and does not change) | Sibling / holder today |
|---|---|---|
| The agent: the Teams concierge function of `0.0.3_BG_BBGTerminal` (prompt, refs, the two Teams skills, the fence and its suite, the launcher contract, `portal_lookup.py`, thread memory) | The Bloomberg OPERATOR duty (`/terminal-upload`, `/bbg-daily`, the OS scheduled tasks, DAPI on loopback) -- **stays in `ajb_workspace`**, split per the 09-22 ruling (call 1) | `0.0.3_BG_BBGTerminal`, OPAL_ANALYST (closed 08-20) |
| The MCP core: guard chain, identity providers, tiers, OAuth AS, audit, integrations framework, deploy path | The live EC2, ALB, Entra app, secrets and audit bucket (instance bindings, not code) | NFRA_OPLGTW (D9), NFRA_OPLMCP (build-complete), SCTY_MCPGUARD (complete), NFRA_INTEGRATIONS (complete) |
| The index layer: catalog schema, its one writer, generation into the MCP, discover family, per-property tool kit, typed query engine, tool-name validator | The silver tables, the portal's precomputed tables, and their producers | NFRA_MCPINDEX (D9), D6 GraphQL plumbing |
| The vendor-access KIT: the playbook, one scaffold per access path, The Walk tooling, the integration-spec template, the self-heal auth pattern as a reusable module | Opal's LIVE ingest pipelines (bronze/silver/gold, Lambdas, EC2 boxes), which stay in `ajb_workspace` under LGIC; each reaches conformance through its own migration (Rule 30, R19) | AUTH_SELFHEAL (D8, PRD stage) owns DESIGNING the self-heal pattern; `opal_ai` templates the pattern once it is designed |
| The instance manifest contract and one manifest per deployment | The naming canon and its builders (`lib/opal_naming.py`, `infra/logic/registry/`) for Opal's names | LGIC_NAMING, LGIC_ENFORCE |
| Client directories | Each client's own data, vendors and credentials | none yet -- partner/client access is ZERO until Andrew names a first consumer (his 2026-08-20 ruling) |
| | The fabric (broker, inbox, `org/XXX.md`), as an OPTIONAL adapter: on in the Opal instance, off in the template (09-22 ruling, call 2) | `ajb_workspace` |

**Explicitly NOT `opal_ai`'s:** the portal; the data pipelines; the Bloomberg operator duty; any new vendor egress
(YCharts, Bloomberg and every vendor API stay on Andrew's per-use word); alarms or monitors of any kind (standing
moratorium -- Part IV finding 12 names the one place prior art conflicts with it); partner or client access before he
names a first consumer.

### II.2 The shape of the repo (recommendation; the two alternatives are Part VIII call 2)

He asked for a structure that "considers the above format in all cases, because all products will follow this journey".
Recommended: **slice-first** -- the three slices are the top-level directories, and each product (agent, MCP, index,
vendor-access) is a folder inside every slice. That places slice (ii) in one designated place, as he asked, and gives
each client its own subtree.

```
opal_ai/
  README.md                  the journey: opal -> template -> clients; which slice a file belongs to
  opal/                      SLICE i   the Opal implementation, the internal beta, built first
    instance.yaml            Opal's bindings (identity, tiers, secrets, catalog, integrations, channel, adapters)
    agent/                   the Opal Analyst: prompt, refs, skills, fence, launcher, thread-memory home
    mcp/                     the Opal MCP: gateway core + Opal's integrations (schwab, ycharts, portal, globgrph ...)
    index/                   Opal's catalog rows + per-property analyses + its tools
    vendors/                 Opal's integration specs (schwab, blackdiamond, orion, eclipse, smartx, ycharts, bloomberg)
  template/                  SLICE ii  the modular form -- firm-neutral, kept clean
    instance.schema.json     THE contract every instance fills
    agent/                   seat template: prompt skeleton, ref skeletons (request catalog, guardrails, memory),
                             the serve-loop skill, the fence + its suite, launcher contract, channel + fabric adapters
    mcp/                     gateway core, identity providers, tier model, OAuth AS, audit, integration framework
    index/                   catalog schema + writer + generator, discover family, typed query engine, tool kit,
                             tool-name validator
    vendor-access/           playbook, one scaffold per access path, the-walk/, self-heal/, integration-spec template
    tests/                   firm-neutrality check (O7), planted-unclassified-tool refusal (O10), routing harness (O2)
  clients/                   SLICE iii
    <client-slug>/           instance.yaml + bespoke tools, vendor specs, catalog rows -- and nothing else
  docs/                      the standards the slices share
```

⛔ **Recommended with this shape: slice (ii) is EXTRACTED from slice (i) by MOVING code, never by COPYING it** (Part V
item 3). While V1/V2 are built, `opal/` holds working code. When the template is cut, each generic module MOVES to
`template/`, and `opal/` keeps only what binds it to Opal. Two live copies of the gateway core, one in each slice, would be
a build-alongside pipeline under the standing veto, and they would drift.

### II.3 Placement

The directive named for this already exists: **D6 "Opal AI"**. It was re-scoped by Andrew-direct on 2026-08-20 to "the
mechanics of the agent and its interfacing with various tooling", is placed SITEZ, and has **no member projects** today.
The two in-flight projects this aggregates, NFRA_OPLGTW and NFRA_MCPINDEX, sit under **D9** (placed LAPTOP, and moving
to site Z "shortly" on his 2026-09-22 word). How those memberships meet is the CTO's call at L3 (Part VIII call 4).

---

## PART III -- THE QUALITATIVE BAR

- **Speed:** a staff member gets a catalog-served answer while they are still in the conversation. Today one such answer
  took long enough that they would have gone and looked themselves (Part IV finding 3).
- **Economy:** most of an answer's time and tokens go into answering, not into loading tool schemas, grepping a catalog
  by hand or cold-starting helpers.
- **Accuracy:** for a figure the portal shows, the Analyst's number and date equal the portal's. A disagreement is a
  defect of this product, never a caveat.
- **Routing:** the agent reaches the purpose-built tool for a common question without being told which one. If it
  falls back to the typed query or a file read first, the index has failed.
- **Guardrails:** a colleague who tries -- urgency, seniority, a message crafted to look like an instruction -- cannot
  get the Analyst to write, download, call a vendor or widen its own scope, and gets a reason they can repeat.
- **Honesty:** every figure states its date and whether it is complete; a partial read is reported as partial.
- **Template cleanliness:** a person at another firm could read the whole template slice and learn nothing about Opal.
- **Template reality:** the Opal instance runs from the template. If Opal needs a template fork to run, slice (ii) has
  not been achieved.
- **Vendor onboarding:** an engineer who has never touched a given vendor gets from The Walk to a dormant, fail-closed
  integration by following the playbook, without asking the person who did the last one.
- **Client isolation:** a client staff member cannot be shown another firm's data by any phrasing, and the isolation
  lives on the server, not in the prompt.

---

## PART IV -- THE SUBSTRATE (findings, each with what was measured)

### The three layers already form one stack

1. **The Analyst, the gateway and MCPINDEX are already one stack in three layers** (the 09-22 assessment, s.0 item 1,
   re-confirmed here by reading the code layout). The Analyst is a Claude seat whose only external surface is the Opal
   Gateway MCP (`org/tier0_utility/0.0.3_BG_BBGTerminal/prompt.md:15-20`). MCPINDEX is built INSIDE the gateway: its
   catalog is `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`, and its query engine is OPLGTW's
   `app/integrations/schwab/engine.py`. The GraphQL work is the gateway's `app/graphql_plumbing/` (v0 plumbing only:
   `catalog_gate.py` behind `POST /query/v0`). **So `opal_ai` gathers an existing stack into one repo; nothing here is a
   new product.**

### Slice i -- what the Opal implementation inherits

2. **The agent is built and in live use; its guardrails are written down and mechanically fenced.** Its judgment lives
   in refs: `REQUEST_CATALOG.md` (48 lines, 8 approved and 8 denied shapes, deny-by-default, each denial carrying a
   quotable reason), `BLOOMBERG_GUARDRAILS.md` (41 lines, "view, never download", with a one-question tie-breaker),
   `TEAMS_DUTY.md` (196), `THREAD_MEMORY.md` (275), `PORTAL_RETRIEVAL.md` (79), `BUCKET_ALLOWLIST.yaml` (93),
   `RELAUNCH.md` (128). Other guardrails are mechanical:
   - an identity acceptance gate (`whoami` must answer "Opal Bloomberg", `prompt.md:34-39`);
   - `.tools/hooks/bg-concierge-gate.sh` (219 lines): the seat cannot write its own prompt or refs, cannot run git or
     cloud mutations, cannot download from Bloomberg, and cannot use the non-bbg gateway;
   - a server-side per-identity tool allowlist (`app/identity_scope.py`, `identity_tool_allowlist.txt`).

   The serve loop is `/bbg-teams-assist` (150 lines): ack first, recall, classify, research, reply with vintage, record.
   Memory is one directory per thread plus a per-person standing block in `threads/INDEX.md` (5 thread dirs at this
   read). **The instruction-and-guardrail half he names is prior art to template, not a design to invent.**
3. **Speed is already measured, and the data layer is not the bottleneck.** OPAL_ANALYST PRD §11.1 (2026-08-20, one
   real exchange): 5m45s from question to answer. The data layer took 0.92 s, **0.3% of elapsed**. The time went to:
   - detection: a Teams poll with a mean floor of 7.5 s, measured at 51.1 s that day;
   - turn overhead: about 50-60 s of deferred-MCP schema-load round trips doing no work;
   - routing: a HAND-GREP of a 1,336-line catalog;
   - extraction: a second Python cold start.

   §11.2 designs the remedies: resident schemas for the hot tools, a routing call exposing the gateway's existing
   `query_v0`/`catalog_gate`, one-call retrieval, and Graph change notifications (push) to remove the poll. Their landing
   state was not re-measured here (Part VII). The launcher sets `ENABLE_TOOL_SEARCH=auto:25` for this seat
   (`.tools/ajb.ps1:268`). **"Fast and economical" for slice (i) is these four fixes plus the index, and the
   measurement method (a real exchange, two clocks, timed per stage) is already defined.**
4. **The gateway is modular where it matters and bound to Opal only in its configuration.** It has 256 tracked files;
   `app/` holds 16,185 Python lines. The generic core:
   - the `_run` chain in `app/tools.py:109` onward: identity -> tier -> data entitlement -> identity scope -> guard ->
     write entitlement -> blast cap -> destructive confirm -> token -> audit;
   - five identity providers and an OAuth AS with dynamic registration;
   - the integrations framework: `IntegrationSpec`, three `AuthKind`s (DELEGATED_USER / SHARED_SECRET / NONE), a lazy
     fail-closed registry, and `validate_integration_spec` run both before deploy and at runtime
     (`docs/architecture/NFRA_INTEGRATIONS_STANDARD.md` v1.3, s.2-8);
   - the 5-step add-checklist;
   - an integration that is inert until listed in `ENABLED_INTEGRATIONS`.

   What is bound to Opal (Entra ids and scopes, the tier roster by email, the audit bucket, secret names, the catalog) is
   configuration in code or env, listed in the 09-22 assessment s.2. **Slice (ii)'s MCP half is extracting that
   configuration into one instance manifest, a refactor rather than a rebuild.**
5. **OPLGTW already specifies the per-person access model a template needs.** Its PRD contracts C1-C6 cover:
   - `tid`/`oid` principals, never email, as the authorization identity;
   - versioned grants in DynamoDB, keyed by principal and scoped by master, dataset, accounts, dates, columns and
     operations, re-read on every request;
   - a keyed account alias (HMAC);
   - a typed query only: no SQL or expressions, with limits of 20 filters, 10 group fields and 10 aggregates;
   - DuckDB in a capped child process: 256 MiB, 30 s, 12 objects / 64 MiB;
   - a result cap of 500 rows / 131,072 bytes, and a response envelope carrying scope, date, completeness and truncation;
   - one fenced reader role per data scope, named by the builder;
   - revocation without a redeploy.

   (`org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md:125-193`.) **This is the template's access layer, already
   ratified for one data property.**
6. **The indexing design is written and a quarter built.** MCPINDEX PRD v0.5 (ADMITTED @`b7dc80e2cc`) sets out:
   - ten outcomes, FWD-1 to FWD-10;
   - ONE catalog, versioned in S3, with exactly one writer (C1);
   - no tool ships without a catalog entry and a safety classification (C2);
   - tool names `{system}_{function}[_{qualifier}]` with scope always an explicit argument (C3, the CRO's reading of
     "Refer to LGIC naming", not a canon rule);
   - the answer envelope (C4); portal parity (C5); the typed query (C6); one read role per property (C7); a beta roster
     (C8);
   - a three-rung tool ladder: discover -> purpose-built -> typed query
     (`docs/briefs/opal-mcp-tool-index-scoping-20260917.md` s.3).

   Its FWD-10 is the template sentence in so many words: *"Adding the next property or tool is one catalog entry plus a
   tool."* **Built state: 9 of 38 cells** (Part VI).
7. **The GraphQL layer is the client-plane design, and Andrew wrote it.** The client data-access schema brief (Andrew,
   ingested 2026-08-19,
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/CLIENT_DATA_ACCESS_SCHEMA_BRIEF_INGEST_20260819.md`) separates two planes:
   - a CLIENT plane: natural language -> entity resolution -> a constrained five-tool business surface
     (`find_account`, `get_account_details`, `get_account_performance`, `find_accounts_missing_fee_splits`,
     `get_account_data_issues`) that compiles to GraphQL internally, business-semantic types only, storage invisible to
     the client;
   - an INTERNAL plane: SQL over parquet, never forced through GraphQL.

   His §9 guardrail: *tenant authorization server-side on every resolver -- "never rely on the model to scope access
   correctly"*. His phasing qualifier: the parquet plane is *"100% going to be something we want to develop internally
   first."* The five tools are parked by name in `graphql_plumbing/DESIGN.md:41-49`; entity resolution is scaffolded
   (`app/entity_resolution/`) and hard-gated on D3's residual enum. **Slice (iii) has a written design: it is this
   client plane, instanced per firm.**

### Slice ii -- what the template inherits for vendor access

8. **Opal's vendor access already falls into distinct paths, each documented at source:**

   | path | Opal instance | mechanism (as documented) | record |
   |---|---|---|---|
   | official / documented API | SmartX REST (ROPC-JWT), Orion (JWT), FRED | Lambda REST pull; the API characterized EMPIRICALLY, never from its docs alone | `infra/aws/lambda/smartx_rest_pull/`, `THIRD_PARTY_DATA_INTEGRATION_STANDARD.md` s.3-4 |
   | reverse-engineered internal API, cookie-riding | Black Diamond (49F, Cottonwood) | Lambdas read the `.bd.identity` cookie from Secrets Manager and pull REST with no browser; a TRANSIENT EC2 box (`bd-49f-auto-login`) re-mints the cookie by driving the real login with computer vision, reading any OTP through the gateway; keepalive plus session-trigger chain | `data/assets/docs/BD_API_DESIGN.md:9-16` (LIVE, 2026-07-18) |
   | reverse-engineered internal API, session bundle | YCharts | SHARED_SECRET integration on the gateway, captured by HAR into Secrets Manager | `NFRA_INTEGRATIONS_STANDARD.md` s.3, s.5 step 3 |
   | standing vendor session on a box | Schwab SI2 | a Windows EC2 box holding the vendor desktop session; the pull MUST run as the vault-holding identity (`Administrator`), never `SYSTEM` | `data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md:9-24` |
   | file delivery | Schwab CRS via OneDrive | a sync then silver roll-forward | `.claude/skills/49-schwab-conv` |
   | rendered page (last resort) | the SmartX exporter | a browser on EC2 with an AI-supervised selector layer | `infra/aws/ec2/smartx-exporter/` |
   | device-bound terminal | Bloomberg | DAPI on the terminal box, view-only | `integrations/bloomberg/` (the operator duty, stays in the workspace) |

   **The ranking he stated ("official API if we got it, not official API if we don't") is already law.** The
   Third-Party Data Integration Standard (RATIFIED 2026-05-20, Andrew: *"we do not 'scrape', we 'reverse engineer'"*)
   prescribes a six-step method: discover the real data contract; characterize auth; map each requirement to endpoint,
   params and JSON path; verify fidelity empirically; DOM parsing only as a flagged last resort; drift detection. Its
   deliverable is an integration spec.
9. **"The Walk" exists as a method with preserved tooling.** RCN-0001 (Black Diamond, 2026-07-21): Andrew walked about
   every dashboard section with HAR capture on, and the CRO's `scripts/profile_har.py` + `extract_schemas.py` produced
   229 endpoints and 52 schemas. The re-run reproduced 218 files byte-identical, and the host regex plus noise list is
   the only per-target knob. RCN-0002 (Orion) re-used the tools on a 779-entry capture. Raw HARs stayed outside the repo
   (`RECON_REGISTER.md:22-23, 48-78, 142-173`). **The Walk's template is these two scripts, a capture protocol, and the
   RCN teardown shape.** Two gaps are named in those same rows: a truncated capture silently loses part of the walk, and
   a walk exercises only the sections walked (Orion's was "a billing-and-reporting walk, not a performance walk").
10. **Self-heal is a registered project whose pattern is not yet designed.** AUTH_SELFHEAL (D8, PRD v0.1, `dep_stage:
    PRD`, 2026-08-31) owns the pattern across every cookie-riding consumer:
    - ordering, so a consumer fires after its mint;
    - post-heal recovery (today nothing re-runs);
    - a re-mint decision (the keepalive can extend a session but not renew it);
    - a consumer inventory.

    Its key finding: *"THE SELF-REPAIR REMOVES THE EVIDENCE"* -- once the chain heals, every instrument reads healthy and
    the only defect left is a missing date. **So the template can carry BD's re-auth box as a working scaffold now, but
    the self-heal module it templates is whatever AUTH_SELFHEAL designs.** Templating it earlier would freeze a pattern
    its owner has measured as incomplete.
11. **The gateway's own add-checklist is the vendor onboarding path on the MCP side.** Author the integration; register
    its factory; provision the secret (browser-session credentials via the HAR procedure); grant IAM by Terraform; enable
    through the arch gate (`NFRA_INTEGRATIONS_STANDARD.md` s.5, s.8.1). The storage model carries a firm-separation
    invariant enforced by IAM (s.9.2). **O8's "plugs into the MCP under the same rules" is this checklist, already
    written.**
12. ⚠ **One conflict inside the prior art: the Third-Party Standard requires every reverse-engineered integration to ship
    with a monitor that "alarms to ops" (s.3 step 6), and the standing moratorium forbids building monitors unless
    Andrew asks** (CLAUDE.md s.5; AUTH_SELFHEAL s.3 defers all alarms to GLOBALALARM, D10). A template that ships the
    standard as written ships a monitor. Named, not resolved: Part VIII call 6.

### Indexing prior art from comp-tooling

13. **The comp-tool router is a working index router with measured failure modes, and it maps onto MCPINDEX's needs.**
    `comp-which` (2,739 lines) routes a plain-English question in two layers:
    - CURATED vetted question->tool rules;
    - a MANIFEST-FUZZY backstop over `graph-call-manifest.yaml` (217,678 bytes). Each entry carries `use_case`,
      `canonical_call`, `tool`, `mode`, `cost`, `freshness`, `rebuild_trigger`, `anti_pattern`, `status` and
      `superseded_by`.

    When nothing curated matches it says so first ("NO CURATED RULE MATCHED ... FUZZY GUESSES, not a routing decision"),
    measured live in this session over 78 tools. Around it sit:
    - a rail that denies the off-index path at the hook layer (`.tools/hooks/comp-tool-hud.sh`);
    - routing telemetry (`org/mcp/comp-tool-runs.jsonl`, `comproute-routing.jsonl`);
    - a routing-quality harness (`.tools/comp-which-routing-test.py`, 1,739 lines).

    That harness's docstring records the one lesson a tool index must not relearn: probes drawn from a catalog entry's
    own text measured an 18.2% coverage hole, while real agent questions showed 44.4% -- *"IT IS BRIGHTEST WHERE THE GAP
    IS DEEPEST"*. **So the template's routing test must be scored on questions real people asked, never on the catalog's
    own descriptions** -- which is MCPINDEX FWD-1's "asked cold by someone who did not build the index", generalized.
    Other patterns carry over directly:
    - `anti_pattern`, `cost` and `freshness` fields per entry;
    - a stated vintage on every answer;
    - a printed denominator on every census;
    - "no match" said out loud instead of a best guess.

### Packaging

14. **Anthropic's own FSI plugin shows the external shape, and its indexing is weak.** RCN-0012
    (`briefs/CLAUDE_FSI_PLUGIN_STRUCTURE_AND_DATA_SHAPES_BRIEF_20260922.md` s.1-2) found:
    - a plugin is FILES, not ACCESS: agent prompts, skills, commands and a `.mcp.json` of vendor URLs;
    - the managed-agent cookbooks add `agent.yaml`, depth-1 subagents and `mcp_toolset`s;
    - access is only ever a per-vendor OAuth account;
    - its core connector manifest did not parse at the cloned commit.

    That is the "very poorly indexed" problem Andrew named on 2026-09-17. **The `opal_ai` agent slice can use the same
    packaging (prompt + skills + MCP config) while the index is the difference.**
15. **The repo mechanics were measured at the prior read and still hold.**
    - `.gitmodules` is **0 bytes**; `portal/` and `models/factor_scanner` are unmapped gitlinks. The 09-22 ruling (call 5)
      maps both when the third is added.
    - The org's other product repo is `github.com/Opal-Capital/portal`.
    - Claude Code loads `.claude/skills` and hooks from the directory it is LAUNCHED in, so a submodule-homed agent
      launches with its working directory inside the submodule (09-22 ruling, call 4). That fact was carried as
      "documented behaviour, to be tested on the first carve-out" and is still untested.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

Named, not sequenced. Sequencing is L5's.

1. **One repo decision reconciled with the 09-22 rulings.** Those rulings named the agent's repo `opal_analyst` and
   treated `opal-gateway` and the index as separate packages. Today's word names one repo, `opal_ai`, that ties them
   together (Part VIII call 1).
2. **The agent split into its two functions** (approved 09-22, call 1): the Teams concierge moves; the Bloomberg operator
   stays.
3. **Extraction by moving, never copying.** Every module that becomes template code leaves `opal/` in the same change
   that lands it in `template/`, and the Opal instance is re-pointed to it in that same change. A period with two live
   copies is the build-alongside shape under the standing veto.
4. **The live gateway's deploy path follows its code.** The gateway is a deployed service
   (`deploy-to-ec2.sh` -> S3 -> SSM) with open task orders whose `<paths>` name `infra/aws/ec2/opal-gateway/`.
   Moving the code changes what those orders grant and what the deploy script ships.
5. **One instance manifest contract**, with the bindings listed in the 09-22 assessment s.2 as its first fields, and
   secret and resource names taken from the naming builder for the Opal instance (Rule 30).
6. **The catalog's one live writer identified** (MCPINDEX C1's open obligation: the header names a writer whose own
   docstring disclaims the live file).
7. **Every tool classified in both safety registries**, with the pinned tool-count tests moving with each tool (MCPINDEX
   C2; the live defect `read_teams_attachment` is the example).
8. **A routing test on real, cold questions**, scored the way the comp-which harness learned (Part IV finding 13).
9. **The four measured speed fixes landed and re-measured** by the §11 method (Part IV finding 3).
10. **The self-heal pattern designed by its owner** (AUTH_SELFHEAL) before the template carries it as a module.
11. **The monitor conflict settled** (Part IV finding 12) before the vendor-access kit ships its standard.
12. **A firm-neutrality check** on the template slice that fails when a firm-specific token appears (O7's instrument).
13. **Server-side tenant scope on every tool and resolver** for any instance serving more than one firm's data (Andrew's
    client brief §9; OPLGTW C2).
14. **A first named client**, before slice (iii) has anything to build (his 2026-08-20 zero-partner ruling stands).
15. **The skill-loading behaviour of a submodule-launched session exercised once**, not assumed (Part IV finding 15).

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-09-23 ~18:5xZ-19:1xZ at SITEZ @`1b1244cecf`, repo reads only.

| thing | state | instrument |
|---|---|---|
| NFRA_OPLGTW | 30 of 33 task orders complete, 2 pending, 1 superseded; last commit 2026-09-20 (G-O read-back: OG-r-1 deployed; "Act 2 (five Schwab tools) NOT enabled") | `<status>` tally over `task-orders/*.md`; `git log -- <project dir>` |
| NFRA_MCPINDEX | 9 of 38 complete, 29 pending; wound down 2026-09-21; MX-c-4 finished, held unmerged on `wk-nfra_mcpindex-1-1d`; AC11 ruled by `1.0.0_SA_CTO` @`5f3b4a20c6`; PRD header still reads `"status": "DRAFT"` while the position doc says ADMITTED | `<status>` tally; `POSITION_20260921_WIND_DOWN.md` |
| Gateway code | 256 tracked files; `app/` 16,185 Python lines; `@mcp.tool` decorators: `tools.py` 35, ycharts 6, globgrph 2, opal_portal 1, schwab 0 (it registers by another path; the 09-17 brief counted 49 registered / 44 enabled) | `git ls-files`, `wc -l`, per-file decorator count -- a decorator count is not an enabled count |
| Analyst seat | refs 7 files (41-275 lines); fence 219 lines; serve skill 150; `teams-watch.py` 653; 5 thread dirs + `INDEX.md` | `wc -l`, directory listing |
| OPAL_ANALYST project | `closed` (2026-08-20) | `org/projects/OPAL_ANALYST.json` |
| AUTH_SELFHEAL | `active`, `dep_stage: PRD`, D8 | project JSON |
| NFRA_OPLMCP / SCTY_MCPGUARD / NFRA_INTEGRATIONS | build-complete / complete / complete | project JSONs |
| D6 "Opal AI" | live, SITEZ, 0 member projects, last touched 09-02 | `directives-check --code D6` |
| D9 "Opal Workflows" | live, LAPTOP, 9 members incl. NFRA_OPLGTW + NFRA_MCPINDEX, 46 open TOs | `directives-check --code D9` |
| Repo | `.gitmodules` 0 bytes; gitlinks `portal`, `models/factor_scanner`; no `opal_ai` or `opal_analyst` repo or path in this tree | `wc -c`, `git ls-files -s` |
| Since the 09-22 approval | no commit subject since 2026-09-22 18:00Z names a carve-out, `.gitmodules`, `opal_ai` or templating act | `git log --since` subject grep -- ⚠ this instrument sees only acts that appear in a SUBJECT; an act recorded elsewhere would read absent |

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

1. **No live state was read**: no AWS, no running gateway, no EC2, no Teams, no GitHub. Whether an `opal_ai` or
   `opal_analyst` repository already exists in the GitHub org is UNREAD. Deployed-vs-declared parity of the gateway is
   the 09-18 deploy record's, not measured here.
2. **The §11 speed fixes' current landing state was not measured.** The 5m45s baseline is 2026-08-20's, and some
   workstreams may have landed since. Slice (i)'s speed outcome starts from a fresh measurement, not this number.
3. **Documents read in part, by section:**
   - OPAL_ANALYST_PRD (3,372 lines): §1-§4, §10.0-§10.1, §11, §12 in full; §9's atom-decomp program by heading only.
   - The OPLGTW and MCPINDEX decompositions: not read.
   - `TEAMS_DUTY.md` and `THREAD_MEMORY.md`: sized, not read.
   - The client data-access brief: its first 45 lines.
   - The SmartX exporter internals, the Orion and SmartX REST code, the LGIC doctrine: not re-read.
4. **Tool counts are decorator counts per file**, not the registered or enabled surface (the Schwab integration registers
   five tools without that decorator, per the 09-17 brief).
5. **The vendor-path table (finding 8) is built from each design-of-record's own header**, cited at the line. Those
   documents are dated 2026-07-14 to 07-18 and say "LIVE" at their vintage; current liveness is not re-measured.
6. **The repo layout in II.2 is a recommendation**, with its alternative in Part VIII. Nothing in this brief decides it.
7. **The skill-loading fact for submodules is carried from 09-22 as untested.**
8. **Citations are this pass's reads at the stated vintage.** Consumers re-verify by printing the bytes at the cited line,
   never by searching for the quote.

---

## PART VIII -- CALLS THIS BRIEF SURFACES (NOT OUTCOME-BEARING; each with a recommendation)

| # | call | recommendation |
|---|---|---|
| 1 | **One repo or several?** 09-22 named `opal_analyst` (agent), with `opal-gateway` and an unnamed index as separate packages. Today's word: one repo, `opal_ai`, "ties all this stuff together". | `opal_ai` is THE repo and supersedes the `opal_analyst` name. The gateway and the index become folders inside it, not repos. The 09-22 split (agent / gateway core / index) survives as the folder split inside each slice. |
| 2 | **Layout: slice-first or product-first?** Slice-first = `opal/ template/ clients/` at the top, with products inside. Product-first = `agent/ mcp/ index/ vendor-access/` at the top, each holding its own `opal/ template/ clients/`. | **Slice-first** (II.2). It matches "kept very clean and separate in a designated place" and "their own subfolders and directory system", gives one firm-neutrality check one directory to scan, and keeps a client's whole deployment in one subtree. |
| 3 | **When does the live gateway code move in?** | After NFRA_OPLGTW's current round reaches its L10 slug, so no open order's `<paths>` breaks mid-round. Move it ONCE with history preserved and the deploy path re-pointed in the same window; never a copy. The agent can move first (09-22 order, call 6). |
| 4 | **Where is it registered?** D6 "Opal AI" is empty and named for this; OPLGTW and MCPINDEX sit under D9. | One program under D6 with three workstreams (agent, MCP + index, vendor-access kit), each slice-ordered. OPLGTW and MCPINDEX finish as their own projects and deliver into `opal/`. Membership mechanics are `1.0.0_SA_CTO~Z`'s. |
| 5 | **Does the vendor-access kit own pipelines?** | No. `opal_ai` holds the playbook, scaffolds, The Walk tooling and the integration-spec template; Opal's live ingest stays in `ajb_workspace` under LGIC. The kit is what a NEW firm's vendors are built from. |
| 6 | **The monitor conflict** (Part IV finding 12). | The template ships the Third-Party Standard with step 6 as a FAIL-LOUD contract in the integration's own response (refuse, never serve stale), and no alarm. Any alarm waits on GLOBALALARM / his word. |
| 7 | **Two front doors in V1?** Teams (the Analyst) and a staff member's own Claude (OPLGTW's Menachem journey, MCPINDEX). | Yes, both, over one MCP. The Teams agent is the V1 thread (FWD-1); the direct-Claude door is the second, since OPLGTW's journey is already specified for it. |
| 8 | **V1 vs V2 before the template.** He said "after completing a proper V1, even V2". | The CTO's L2 states what V1 and V2 each mean as outcomes. This brief does not pick between them. |

---

## REFS

```
  BRIEF PATH        docs/briefs/opal-ai-microproduct-repo-brief-20260923.md
  ANDREW RECORD     org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260923_185xZ_OPAL_AI_MICROPRODUCT_REPO_BRIEF.md @6ae5ab5fd3
  PROJECT           NONE-YET (placement candidate: D6 "Opal AI"; Part VIII call 4)
  EXISTING PRD      NONE for opal_ai. Constituent PRDs: org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md;
                    org/missions/D9/NFRA/NFRA_MCPINDEX/prd/NFRA_MCPINDEX_PRD.md; docs/architecture/OPAL_ANALYST_PRD.md
                    (closed project); docs/architecture/D6_OPAL_ANALYST_GRAPHQL_PRD.md
  PREDECESSOR       org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ASSESSMENT_OPAL_ANALYST_OPLGTW_MCPINDEX_TEMPLATING_20260922.md
                    @20de682ede + its two Andrew records (@67673ed414 and "all recs approved")
  SIBLING PROJECTS  NFRA_OPLGTW (D9), NFRA_MCPINDEX (D9), AUTH_SELFHEAL (D8), NFRA_SPMOVE (D9), LGIC_NAMING, LGIC_ENFORCE,
                    the mcportal brief (docs/briefs/mcportal-tech-ops-dashboard-brief-20260917.md), OPAL_ANALYST (closed),
                    NFRA_OPLMCP / SCTY_MCPGUARD / NFRA_INTEGRATIONS (complete), AMGT_RESAPP analysis layer (a Claude-agent
                    consumer on D5, not a member)
  PRIOR ART         agent:    org/tier0_utility/0.0.3_BG_BBGTerminal/{prompt.md, refs/*, tools/portal_lookup.py};
                              .tools/hooks/bg-concierge-gate.sh; .claude/skills/{bbg-teams-assist, teams-assist};
                              .tools/ajb.ps1 (BG launch block)
                    MCP:      infra/aws/ec2/opal-gateway/ (app/tools.py _run, app/integrations/*, identity_scope.py);
                              docs/architecture/NFRA_INTEGRATIONS_STANDARD.md v1.3
                    index:    docs/briefs/opal-mcp-tool-index-{brief,scoping}-20260917.md; app/refs/DATA_CATALOG.yaml;
                              app/graphql_plumbing/{DESIGN.md, catalog_gate.py}
                    client:   org/tier1_exec/1.0.0_SA_CTO/deliverables/CLIENT_DATA_ACCESS_SCHEMA_BRIEF_INGEST_20260819.md
                    vendors:  docs/architecture/THIRD_PARTY_DATA_INTEGRATION_STANDARD.md; data/assets/docs/{BD_API_DESIGN,
                              SCHWAB_AUTO_PULL_DESIGN}.md; org/tier2_senior/0.6.2_AE_PartnerETL/deliverables/AUTH_SELFHEAL_PRD_v0.1.md
                    the walk: org/tier1_exec/4.0.0_SA_CRO/{RECON_REGISTER.md RCN-0001/0002, scripts/profile_har.py,
                              scripts/extract_schemas.py}
                    indexing: .tools/comp-which; .tools/comp-which-routing-test.py; org/modules/graph/graph-call-manifest.yaml
                    external: org/tier1_exec/4.0.0_SA_CRO/briefs/CLAUDE_FSI_PLUGIN_STRUCTURE_AND_DATA_SHAPES_BRIEF_20260922.md
  MEASURED AT       2026-09-23 ~18:5xZ-19:1xZ, SITEZ @1b1244cecf, repo reads only
```
