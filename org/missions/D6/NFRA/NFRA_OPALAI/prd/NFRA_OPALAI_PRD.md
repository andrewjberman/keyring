```json
{
  "project": "NFRA_OPALAI",
  "directive": "D6",
  "fabric": "site-z",
  "prd_version": "v0.5",
  "step": 4,
  "brief_ref": "docs/briefs/opal-ai-microproduct-repo-brief-20260923.md@a47993af9c",
  "endpoint_outcomes": [
    "FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7",
    "FWD-8", "FWD-9", "FWD-10", "FWD-11", "FWD-12", "FWD-13"
  ],
  "status": "DRAFT"
}
```

# NFRA_OPALAI - opal_ai V1: the Opal Analyst as a product, built in the workspace, running on its own

## Authority and project arc

Author and accountable CTO: `1.0.0_SA_CTO~O`. Directive D6, Opal AI; macro NFRA; execution fabric site-z. Registered
@6be4dcdb29.

Andrew commissioned this at the `1.0.0_SA_CTO~O` terminal on 2026-09-24: *"i want to start getting that developed
immediately, so I want to assess what needs to happen to stand that up so that we can begin assigning projects on this
box to get it going (finishing MCPINDEX, getting a proper OPAL ANALYST back online on Teams, and other such work that
ties to that repo function)."* His rulings that shape this PRD, each recorded verbatim in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/`:

| ruling | his words | record |
|---|---|---|
| one repo `opal_ai`, this seat routes it, CI in the repo | "Yes to all but ..." (cards 1, 2, 4) | `ANDREW_DIRECT_20260924_193xZ_OPAL_AI_CALLS_1_2_4_YES_ANALYST_SEPARATION.md` @489fbcd6e0 |
| develop in the workspace; no workspace access for team-facing agents | "I want to develop the opal_ai repo using the ajb_workspace tools, it really is an ajb_workspace project just like the portal, I just don't want the actual team-facing agents, and ultimately external agents, being so close for comfort having ajb_workspace repo access." | `ANDREW_DIRECT_20260924_195xZ_OPAL_AI_CARD3_DEV_IN_WORKSPACE_RUNTIME_WITHOUT_REPO_ACCESS.md` |
| a separate non-admin Windows account; no broker for the Teams agent | "both recs approved" (R1, R2) | `ANDREW_DIRECT_20260924_200xZ_OPAL_AI_R1_R2_APPROVED.md` @11881eb192 |
| endpoint FWD-1..FWD-13 confirmed; D6 = [NFRA] | "yes to both" | `ANDREW_DIRECT_20260924_202xZ_OPAL_AI_ENDPOINT_CONFIRMED_D6_NFRA_RATIFIED.md` @6be4dcdb29 |

He also corrected one premise: *"The bloomberg daily pull is programmatic, an agent does not do that in the current state
as far as I know."* So no agent duty stays behind in the workspace when the Analyst moves.

**The product:** an Opal colleague asks the Opal Analyst a question in Teams and gets an answer from the firm's MCP, fast,
with its date, source and scope. The Analyst runs from a released copy of `Opal-Capital/opal_ai`, under its own Windows
account, which the operating system bars from the development workspace. Engineering seats build and improve it inside
the workspace, as the portal is built.

Two L1 briefs feed it: `docs/briefs/opal-ai-microproduct-repo-brief-20260923.md` @a47993af9c (RCN-0014, the header's
`brief_ref`) and `docs/briefs/opal-ai-gitops-split-brief-20260923.md` @40b964f616 (RCN-0015).

**v0.2 (2026-09-24 ~20:5xZ)** adds C10 and pulls the minimum of S10 into round 1, on Andrew-direct at the
`2.0.0_SA_COO~O` terminal (record `org/tier1_exec/2.0.0_SA_COO~O/deliverables/ANDREW_DIRECT_20260924_204xZ_OPAL_AI_AGENT_NAME_AND_ENTITLEMENTS_SYNTHESIZE.md`
@6426ebff2b): *"we dont have to name it a whole serial anymore if we don't want to, could just be \"Opal_Agent\".
Effectively the purpose is that it's dynamic and the real engineering comes in its entitlements per user/entra-id. A
lot of this work has already been done is just needs to all be synthesized cleanly."* Ruled by this seat on
`2.0.0_SA_COO~O`'s question (msg 25752). The Analyst today calls the gateway as ONE service identity, so every
colleague would get that identity's reach, and a round-1 thread built that way would bake in the wrong authorization
model. The ENDPOINT is unchanged. The runtime account and agent are named `Opal_Agent` (C4).

**v0.3 (2026-09-24 ~21:1xZ)** resolves a contradiction `2.0.0_SA_COO~O` found in C4 (msg 25756). An account that
cannot write its checkout cannot pull into it. The pull moves to the operator account, and `Opal_Agent` holds no
GitHub credential. C3 and C4 are amended; the ENDPOINT is unchanged.

**v0.4 (2026-09-24 ~21:3xZ)** adds C11, found by this seat reading the request catalog against C4. The Analyst's
catalog row 7 (Bloomberg view-side lookups) is served today by a Bloomberg MCP server that launches from the workspace
(`integrations/bloomberg/mcp/server.py`, 456 lines). `Opal_Agent` cannot launch it, and the decomposition places it
outside round 1. The cutover would otherwise drop a capability colleagues use today with no word to them. The ENDPOINT
is unchanged.

**v0.5 (2026-09-24 ~22:1xZ)** retires G-GH. The org policy refuses deploy keys, and the operator-side pull (v0.3)
already makes a narrow credential redundant. The boundary is unchanged: `Opal_Agent` holds no credential. The
ENDPOINT is unchanged.

The design this PRD binds is `org/tier1_exec/1.0.0_SA_CTO/deliverables/OPAL_AI_RUNTIME_ISOLATION_DESIGN_20260924.md`
@45ce8406fc. The header stays DRAFT until L4-R. The author signs neither half.

## Scope and evidence boundary

**This project owns:**
- the `opal_ai` repository's layout and its wiring into the workspace as a real submodule, with the workspace's gates,
  CI, worker provisioning and census tools reaching it;
- the Opal Analyst's product files (prompt, guardrails, request catalog, Teams serve loop, the Teams watch, the fence)
  and their move out of `org/tier0_utility/0.0.3_BG_BBGTerminal/`;
- the runtime account, its read-only checkout, its narrow Claude setup and its launch gate;
- the gateway's move into `opal_ai` and the re-pointing of its release path.

**It relies on and does not change:**
- the Opal Gateway's guard chain, identity providers, tiers and audit (moved, not redesigned);
- the catalog and index layer, which NFRA_MCPINDEX finishes and delivers into `opal_ai` (FWD-4, FWD-12);
- the Schwab query engine and grant model (NFRA_OPLGTW);
- the gateway's EC2, ALB, Entra app, secrets and Terraform root, which stay in the parent.

**Explicitly NOT this project's:**
- the template slice, client slices and off-box hosting (stated outside the endpoint);
- NFRA_OPLGTW's walkthrough grading, which is under Andrew's 2026-09-22 stop;
- the self-heal pattern (AUTH_SELFHEAL);
- the Bloomberg daily pull and its scheduled tasks;
- any new vendor egress. YCharts and Bloomberg stay on Andrew's per-use word;
- alarms or monitors of any kind (standing moratorium).

**Evidence boundary.** Measured at authorship: repo and git on site Z, one GitHub `ls-remote`, local ACLs and accounts.
Not measured: gateway liveness (taken from 2.0.0_SA_COO~O's 2026-09-22 log), whether the Bloomberg loopback is reachable
from a second account, the laptop's copy of the MCPINDEX held branch, and the Teams watch's second blocker's cause.
**Every runtime claim here is DESIRED until a cell exercises it.**

## ENDPOINT (step 2, /endpoint --forward)

Confirmed by Andrew 2026-09-24 ~20:2xZ ("yes to both"). Transcribed from
`org/tier1_exec/1.0.0_SA_CTO/deliverables/OPAL_AI_ENDPOINT_FORWARD_20260924.md` @146ef7366f; statement, DONE WHEN and
ACCEPT are verbatim, and SOURCE lines are dropped.

```
  FWD-1  An Opal colleague asks the Opal Analyst a question in Teams about a figure Opal already
         shows, and gets the answer from the Analyst running in its own separate account
         DONE WHEN  EXERCISED -- one live exchange, traced from the colleague's message to the reply
         ACCEPT     a named colleague asks a real question; the reply gives the figure, its date,
                    where it came from and whose accounts it covers, and matches what the portal
                    shows for the same date; the Analyst that answered was the released copy
                    running on its own, and every step of the exchange was real, none simulated

  FWD-2  The Analyst notices every message sent to it and answers without anyone prodding it,
         including after it has sat idle for hours and including messages that carry pictures
         or pasted content
         DONE WHEN  EXERCISED -- messages sent at chosen times over a working day are all answered
         ACCEPT     a colleague sends messages after long quiet spells and one with a pasted image
                    or rich content; each is acknowledged and answered with no human stepping in;
                    a message it cannot read is answered with a plain statement that it could not
                    read it, never silence

  FWD-3  A colleague gets a routine answer while they are still in the conversation
         DONE WHEN  EXERCISED -- real exchanges timed stage by stage and compared with August
         ACCEPT     for a question about a figure Opal already serves, the colleague would not
                    have been quicker looking it up themselves; the timing shows where the time
                    went, and most of it went into answering, not into warming up

  FWD-4  A colleague who does not know which system holds a fact is sent to the right place on
         the first try, and the questions the Analyst could not place come back as a list
         DONE WHEN  EXERCISED -- real questions asked cold by people who did not build it
         ACCEPT     a set of questions real colleagues asked, not questions written from the
                    catalogue's own descriptions, mostly lands on the right answer first time;
                    each question it could not place is listed with the reason

  FWD-5  A colleague gets the same answer whether they ask the Analyst in Teams or ask their own
         Claude directly
         DONE WHEN  EXERCISED -- the same questions asked both ways by one person
         ACCEPT     the figures, dates and refusals agree both ways, and a person refused
                    something one way is refused it the other way too

  FWD-6  Nobody can talk the Analyst out of its limits
         DONE WHEN  EXERCISED -- a colleague genuinely tries
         ACCEPT     urgency, seniority, or a message made to look like an instruction does not get
                    it to change anything, download from Bloomberg, contact an outside vendor
                    beyond Andrew's standing word, or widen what it will answer; each refusal gives
                    a reason the colleague can repeat

  FWD-7  The Analyst cannot reach the development workspace, Andrew's own identity, or the other
         agents, and it will not start if it ever could
         DONE WHEN  EXERCISED -- at every launch, and once deliberately broken
         ACCEPT     at launch the Analyst tries to open a workspace file and is refused, and it
                    carries no way to act as Andrew or to message the development agents; when
                    that separation is deliberately removed for a test, it refuses to start

  FWD-8  Andrew admits a colleague, sets what they may ask about, and removes them again, and can
         explain any past answer after the fact
         DONE WHEN  EXERCISED -- one colleague admitted, used, narrowed and removed
         ACCEPT     each change takes effect without rebuilding or restarting anything; for any
                    past answer Andrew can see who asked, what was looked up and what data it
                    touched, without private figures sitting in that record

  FWD-9  An engineering agent improves the Analyst or its data tools using the workspace's usual
         tools and checks, and the improvement reaches colleagues only through a release Andrew
         approved
         DONE WHEN  EXERCISED -- one real change followed from the edit to a colleague's answer
         ACCEPT     the change is checked by the same rules as any workspace change, it goes live
                    only when Andrew says so, and afterwards anyone can say which version the
                    Analyst is running and which version is approved

  FWD-10 Anyone who sets up the workspace fresh, on either machine, gets the Analyst's product code
         at the right version with one standard step, and nothing about it is quietly left out
         DONE WHEN  EXERCISED -- a fresh setup on each machine
         ACCEPT     the product code arrives at the version the workspace records; an empty or
                    missing copy is flagged loudly, never taken as fine; agents' work reports and
                    progress views count work done in it

  FWD-11 The data gateway is released from the product's own history with no loss of safety
         DONE WHEN  EXERCISED -- one real release of the gateway
         ACCEPT     a release refuses to go out with unsaved changes, the release record names
                    the product version actually running, and the gateway keeps its full history
                    so every older reference to it still leads somewhere

  FWD-12 Adding a new kind of data for colleagues to ask about is one catalogue entry plus one
         tool, and a tool that has not been classified for safety cannot go live
         DONE WHEN  EXERCISED -- one new kind of data added; one unclassified tool refused
         ACCEPT     the new data is answerable after exactly those two additions; a deliberately
                    unclassified tool is stopped before it can reach anyone

  FWD-13 The product can be picked up and checked on its own, without the workspace
         DONE WHEN  EXERCISED -- a copy taken alone passes its own checks
         ACCEPT     someone holding only the product repository can run its checks and they pass;
                    the checks also run automatically on every change to it
```

**Outside this endpoint, and not promised:**
- the template slice (after a proper V1, even V2);
- client slices (they wait on a named first client);
- external agents hosted off this box;
- NFRA_OPLGTW's walkthrough grading (under Andrew's stop).

FWD-4 and FWD-12 are served by NFRA_MCPINDEX's completion and graded here once that project delivers into `opal_ai`.

## CONTRACTS

**C1 -- One repo, slice-first, and code moves: it is never copied.** `Opal-Capital/opal_ai` is the one repo (it exists,
private, `DEV` = `PROD` = `90ca424fc7`). Its top level is `opal/` (slice i, all V1 code), `template/` (reserved: a README
only, no code, until the template project starts) and `clients/` (reserved the same way), plus `docs/`. A module lands
in `opal_ai` in the same change that removes it from the workspace, and every consumer is re-pointed in that change. At
no moment do two live copies of a module run. The Analyst's cutover is one window. The runtime copy goes live and the
workspace seat's Teams duty stops, and nothing in between serves colleagues from both.

**C2 -- A real submodule, graded like the parent.**
- `.gitmodules` maps `portal`, `opal_ai`, and `models/factor_scanner` (mapped or removed on its owner's word).
- Every checkout path initialises submodules: the startup protocol, `wk-provision.sh` (generalised from its hard-coded
  `portal`) and the sparse-cone recipe. An uninitialised submodule is refused loudly.
- **The lane file lands BEFORE any hook is installed in a nested repo.** `owned-paths-check.sh` is fail-closed on a
  missing lane file in its default block mode (`:41`, `:139-142`), so hook-first is an outage on every commit.
- Commits in `opal_ai` pass the same gates as the parent: Rule 14 (py_compile, ds-precommit, ruff py39), the lane
  check, the ASCII message rule, the surprise-row gate. `safe-commit.sh` is exercised once inside a nested repo, and
  what it cannot find there is fixed.
- CI in `opal_ai` runs py_compile, ruff py39, the gateway's tests and the product's own checks on every push (Andrew's
  card 4).
- `/integrate` settles an `opal_ai` gitlink conflict by `is-ancestor` inside the nested repo, and leaves the checkout on
  a branch, never detached. The census tools (activity-check, fabric-commits, daily-sprint, outcome-check) iterate
  submodules.
- The law text that names the monolith's nested repos (CLAUDE.md Git, `org/XXX.md` Step 1a) is updated only under an
  `ANDREW_LAW_EDIT_ORDER` (gate G-LAW).

**C3 -- Branches and release.** `DEV` integrates and `PROD` is what runs. Only `0.0.0_AB_MSTR` (or `~Z`) pushes
either, on Andrew's word. Never rebase. A release is a merge of DEV into PROD, and the parent's pointer bump names the
PROD commit now running. The launcher's pull step fetches PROD fast-forward only, as the operator account (C4). A pull
that would not fast-forward refuses.

**C4 -- The runtime boundary is the operating system (R1).**
- A standard local Windows account named `Opal_Agent`, in neither `Administrators` nor `CodexSandboxUsers`, runs every
  team-facing agent. The agent names itself `Opal_Agent` too, not a fabric serial.
- Its product files come from a checkout of `opal_ai` PROD. The runtime account can READ that checkout and cannot
  write it, so the agent cannot edit its own prompt, guardrails, hooks or settings. It can write only its state
  directory.
- **The pull runs as the OPERATOR account, never as `Opal_Agent`** (v0.3 ruling on `2.0.0_SA_COO~O` msg 25756: whoever
  pulls must write the checkout, and `Opal_Agent` may not). The launcher's pull step uses the operator account's EXISTING GitHub
  access on this box (v0.5: no new credential is minted; G-GH is retired). The pull is fast-forward only on `PROD`. The checkout is ACL'd
  read-and-execute for `Opal_Agent`. **`Opal_Agent` holds no GitHub credential at all**, and no credential for
  `ajb_workspace`. The launch gate and the agent then run as `Opal_Agent`, and the gate checks (a)-(c) as written. The
  operator side starts the agent as `Opal_Agent` and passes it no operator credential, token or environment.
- Its Claude setup is its own: its own login and credential store, a `CLAUDE.md` holding only the agent's guardrails,
  a `.claude/` holding the fence hook and the Teams serve skills, and an MCP config listing `opal-gateway-bbg` and
  nothing that reaches the workspace. Andrew's proxy gateway `opal-gateway` is never configured in that account.
- No AWS profile or AWS credential exists in that account.
- **The launch gate fails closed.** Before the agent starts, the launcher, running as the runtime account, (a) tries
  to read one named workspace file and requires Access Denied, (b) requires the checkout to be clean at the PROD commit
  it just pulled, and (c) requires the account to hold neither admin group. Any failure refuses the launch. The gate
  has a negative arm: with the workspace read deliberately granted for a test, the launch refuses.
- Paths (the checkout, the state directory, the workspace probe file) are launcher configuration. None is hard-coded in
  product code, and none names a device.

**C5 -- No broker, and state stays out of every repo (R2).**
- The Teams-facing agent has no connection to the agent message system.
- Its hand-offs to an operator go through the gateway, as a Teams message to the operator, or through a one-way drop
  folder that the workspace side reads and the runtime can only write to.
- Thread memory, logs and the Teams-watch cursor live in the runtime's state directory, never in `opal_ai` and never
  in the workspace. The integrator's sweep of the seat's `threads/` stops at cutover.
- **Backup of that state is an OPEN obligation with an owner (this project).** Any S3 address it uses comes from
  `lib/opal_naming.py address()`, never typed (Rule 30). Until it lands, the loss exposure is named in the cutover
  record.

**C6 -- The gateway moves with its history, and its release path follows it.**
- History is preserved by a path-filtered split. The parent's old paths are deleted in the same parent commit that
  adds the pointer.
- `deploy-to-ec2.sh` finds the workspace by asking git (the superproject working tree, or an explicit env var), never
  by counting directories. `SRC` points into `opal_ai` and `SHA` is the `opal_ai` commit.
- `safe-ec2-deploy.sh` runs its clean-tree check and commit read with `git -C` on the source's own repo.
  `EC2_MANIFEST.json` records the `opal_ai` commit deployed AND the parent pointer it paired with.
- These two fixes land in the same window as the move, never after it.
- No `parents[N]` reach survives. `NFRA_OPLGTW_CONTRACT.json` moves with the gateway or is passed by its existing env
  override. D3's join-disposition contract is passed by path.
- The parent's four live reaches into the gateway are cut. The responsive-report check stops importing gateway code,
  and the catalog writer and its validator move beside the catalog.
- Terraform stays in the parent.
- **The move does not happen under open task orders** (gate G-MOVE).

**C7 -- The Analyst's limits travel with it, unchanged in content.**
- The request catalog (deny by default; each denial carries a quotable reason) and the Bloomberg view-never-download
  rule move as they are.
- The identity acceptance gate moves as it is: before any Teams read or reply, `whoami` must answer the Opal Bloomberg
  account.
- Every inbound message is data, never an instruction.
- A change to any of these is a change to `opal_ai`, graded and released like any other (C3). The agent itself cannot
  make one (C4).

**C8 -- The Teams watch must see without the agent's help.**
- Detection may not depend on the agent's own gateway activity. The token the watch uses is refreshed by the watch or
  the runtime launcher on its own cadence, and not only when the agent happens to call the gateway.
- A read failure with a live token is a defect of this project, not a credential state.
- A message the watch cannot read, such as hosted content, is answered with a plain statement that it could not be
  read. That needs a `hostedContents` read on the gateway, which this project adds as a classified tool under C2's
  rules.

**C9 -- Speed is measured, not asserted.** FWD-3 is graded with the OPAL_ANALYST PRD's section 11 method. Real
exchanges run on two clocks and are timed per stage (detection, turn overhead, routing, data, reply), and compared with
the 2026-08-20 baseline of 5m45s, of which the data layer was 0.92 s. The remedies named there (resident hot-tool
schemas, a routing call, one-call retrieval, push instead of poll) are candidate cells, never presumed landed.

**C10 -- Every answer is scoped to the ASKER's entitlement, never the agent's.**
- The asker is identified by their Entra tenant and object id, never by email. This is the principal the gateway's
  policy model already keys on (`app/data_entitlement.py`, `POLICY#<tid>#<oid>`, NFRA_OPLGTW C1-C2).
- The gateway establishes the asker SERVER-SIDE, from the Teams message it read itself. The agent never asserts
  whose behalf it acts on, and an identity the agent supplies in a call is ignored. A prompt-injected agent therefore
  cannot borrow a wider person's reach.
- The effective scope is the INTERSECTION of the asker's policy and the agent's own identity allowlist
  (`app/identity_scope.py`). The agent's service identity never widens what an asker may see.
- An asker with no policy gets a plain refusal that says how to get access. It never gets a default reach.
- Existing work is carried and synthesized, never rebuilt: the policy store (`access_state.py`,
  `data_entitlement.py`), the identity allowlist, the tier model (`tier.py`) and the `_run` guard chain. Each cell's
  first act is to locate the existing implementation it extends.

**C11 -- The cutover drops nothing silently.** At cutover, every APPROVED row of the request catalog is either served
by the runtime through a mechanism it can reach, or answered with a plain, quotable "not available from the Analyst
yet" reason naming who to ask. The catalog row text stays byte-unchanged (C7). The reason lives in the agent's runtime
guardrails, not in the catalog. The cutover record lists every such row, with the enrichment that restores it. **Row 7
(Bloomberg view) is the known case.** Restoring it means moving the view-only Bloomberg MCP server into `opal_ai` and
proving `Opal_Agent` can reach the terminal's loopback API, and that is the first enrichment after round 1. The
Bloomberg operator scripts, sign-in and daily pull stay in the workspace.

## SURFACE MANIFEST

| id | surface | what it is | depends on | outcomes |
|---|---|---|---|---|
| S1 | repo layout | `opal/`, `template/` + `clients/` reserved, `docs/`, README naming the slices | the repo | FWD-9, FWD-13 |
| S2 | submodule wiring | `.gitmodules`, checkout-path init, `wk-provision.sh`, `/integrate`, census tools | S1 | FWD-10 |
| S3 | nested-repo gates | lane file, hook installer, `safe-commit.sh` in a nested repo | S2 | FWD-9 |
| S4 | CI | the `opal_ai` workflow | S1 | FWD-13 |
| S5 | agent product files | prompt, refs, request catalog, serve skills, fence, `portal_lookup.py`, the Teams watch | S1 | FWD-1, FWD-6 |
| S6 | runtime account and checkout | the account, the ACLs, the read-only PROD checkout pulled by the operator | S1, G-ACCT | FWD-1, FWD-7 |
| S7 | runtime Claude setup and launcher | login, `CLAUDE.md`, `.claude/`, MCP config, launch gate, state directory | S5, S6, G-AUTH | FWD-1, FWD-7 |
| S8 | Teams watch and hosted content | token refresh owned by the watch, read-failure fix, `hostedContents` tool | S5, S7 | FWD-2 |
| S9 | speed | stage timing and the section 11 remedies | S7, S8 | FWD-3 |
| S10 | per-asker entitlements and operator controls | round 1: the asker resolved server-side and every answer scoped to the intersection (C10), one un-admitted asker refused; enrichment: admit, narrow and remove without a restart, and explain a past answer from the audit | the gateway's policy store and identity scope | FWD-1, FWD-8 |
| S11 | gateway move | history split, pointer, seams cut | G-MOVE | FWD-5, FWD-11 |
| S12 | gateway release path | the two deploy scripts, the manifest | S11 | FWD-11 |
| S13 | release flow | DEV to PROD, pointer bump, runtime pull | S2, S7 | FWD-9 |
| S14 | the index | delivered by NFRA_MCPINDEX into `opal_ai` | NFRA_MCPINDEX | FWD-4, FWD-12 |
| S15 | Bloomberg view server | the view-only Bloomberg MCP server moved into `opal_ai` and reachable from `Opal_Agent`; until then, C11's plain decline | S7 | FWD-1, FWD-6 |

**Gates, each an act a named holder can take on demand:**
- **G-ACCT:** create the runtime account, an admin act on this box. Holder: a worker under this project, on R1.
- **G-AUTH:** the runtime account's first Claude login and its `opal-gateway-bbg` OAuth, whose MFA goes to Andrew's
  phone. Holder: Andrew, at a time he picks.
- **G-GH: RETIRED at v0.5.** A narrow credential was never reachable: GitHub refused a read-only deploy key (HTTP 422,
  "Deploy keys are disabled for this repository", measured by `0.0.0_AB_MSTR~Z` 2026-09-24 ~22:0xZ). A narrow credential
  also adds nothing once the pull runs as the operator, who already holds GitHub access on this box, while
  `Opal_Agent` holds none.
- **G-MOVE:** the gateway path moves only when no open order names it. That means NFRA_OPLGTW's OG-v-4 and OG-v-5
  (Andrew lifts his stop or supersedes them) and NFRA_MCPINDEX's open round-1 orders (closed and re-cut). Holder:
  Andrew for OPLGTW; the MCPINDEX COO for its round.
- **G-LAW:** the law-text edits. Holder: Andrew.
- **G-PUSH:** every DEV and PROD push. Holder: `0.0.0_AB_MSTR~Z`, on Andrew's word.

## Ground truth measured at authorship (2026-09-24, site Z)

- `Opal-Capital/opal_ai` exists, private, `DEV` = `PROD` = `90ca424fc7`, README only (`ls-remote`, positive control
  on `portal`).
- `.gitmodules` is 0 bytes. The gitlinks are `portal` and `models/factor_scanner`. The portal checkout is on `DEV` with
  0 active hooks.
- The gateway is 256 tracked files under `infra/aws/ec2/opal-gateway/`, last touched 2026-09-21.
- The Analyst runs as `Opal Bloomberg`, a local Administrator with Full control of the workspace.
- The workspace ACL grants SYSTEM, Administrators, `Opal Bloomberg`, `CodexSandboxUsers` and one unresolved SID ending
  `-3194460454`. The profile folder grants only the first three.
- The Teams watch has read nothing today, warm or cold. The Analyst's own log (@0646a96553) records the 15-minute token
  coupling, 33 of 33 read failures with a live token, and no `hostedContents` tool.
- NFRA_MCPINDEX: 9 of 38 complete, 29 pending, no worker running. Its held branch `wk-nfra_mcpindex-1-1d` is not on
  this box or on origin.
- NFRA_OPLGTW: 30 of 33 complete. OG-v-4 and OG-v-5 are pending under Andrew's 2026-09-22 stop.

## BRIEF COVERAGE

Denominator: **63 headings**, every line matching `^#` at each brief's pin. RCN-0014 @a47993af9c has 35 and RCN-0015
@40b964f616 has 28, re-measured here with `git show <pin>:<path> | grep -cE '^#'`. Each row gives its heading count.
Dispositions: CARRIED, CARRIED-AS-OPEN, SUPERSEDED (a later Andrew ruling replaced it) or NOT CARRIED (with the reason).

**RCN-0014 (35):**

| headings | n | disposition | where |
|---|---|---|---|
| title; ANDREW'S WORDS | 2 | CARRIED | Authority |
| PART I; THE CANDIDATE THREAD; SLICE i | 3 | CARRIED | FWD-1 |
| O1 | 1 | CARRIED | FWD-1, FWD-2, FWD-3 |
| O2 | 1 | CARRIED | FWD-4 (via NFRA_MCPINDEX) |
| O3 | 1 | CARRIED | FWD-5 |
| O4 | 1 | CARRIED | FWD-6, C7 |
| O5 | 1 | CARRIED | FWD-8, S10 |
| SLICE ii; O6; O7; O8; O9 | 5 | NOT CARRIED | the template slice is outside the endpoint on Andrew's order ("after completing a proper V1, even V2") |
| O10 | 1 | CARRIED | FWD-12 (via NFRA_MCPINDEX) |
| SLICE iii; O11; O12 | 3 | NOT CARRIED | client slices wait on a named first client (2026-08-20 ruling) |
| PART II; II.1 | 2 | CARRIED | Scope and evidence boundary |
| II.2 | 1 | CARRIED | C1 |
| II.3 | 1 | CARRIED | placement D6, ruled |
| PART III | 1 | CARRIED | FWD-1, 3, 4, 6 ACCEPT lines; the template bars are NOT CARRIED with the template slice |
| PART IV | 1 | CARRIED | Ground truth |
| The three layers already form one stack | 1 | CARRIED | Scope (the stack is gathered, not rebuilt) |
| Slice i -- what the Opal implementation inherits | 1 | CARRIED | C7, C8, C9 |
| Slice ii -- vendor access | 1 | NOT CARRIED | template slice |
| Indexing prior art from comp-tooling | 1 | CARRIED | FWD-4's ACCEPT (real questions, not catalogue text) |
| Packaging | 1 | CARRIED | C4 (the runtime's own `CLAUDE.md`, `.claude/`, MCP config) |
| PART V | 1 | CARRIED | items 1, 3 -> C1; 4 -> C6; 6, 7 -> NFRA_MCPINDEX; 8 -> FWD-4; 9 -> C9; 2 SUPERSEDED (no agent duty stays, per Andrew's correction); 15 SUPERSEDED by C4; 5, 10, 11, 12, 13, 14 NOT CARRIED (template, AUTH_SELFHEAL, one-firm V1, no named client) |
| PART VI | 1 | CARRIED | Ground truth, re-measured |
| PART VII | 1 | CARRIED-AS-OPEN | Evidence boundary |
| PART VIII | 1 | CARRIED | call 1 ruled; 2 -> C1; 3 -> G-MOVE; 4 ruled D6; 5, 6 outside; 7 -> FWD-5; 8 -> this endpoint is V1 |
| REFS | 1 | CARRIED | inputs to S5, S11 |

Sum: 2+3+1+1+1+1+1+5+1+3+2+1+1+1+1+1+1+1+1+1+1+1+1+1+1 = **35**.

**RCN-0015 (28):**

| headings | n | disposition | where |
|---|---|---|---|
| title; ANDREW'S WORDS | 2 | CARRIED | Authority |
| PART I; THE CANDIDATE THREAD | 2 | CARRIED | FWD-9 (one edit in `opal_ai`, graded, pointer bumped) |
| O1 | 1 | CARRIED | FWD-10, C2 |
| O2 | 1 | CARRIED | FWD-9, C2 |
| O3 | 1 | CARRIED | FWD-13, C2 (CI) |
| O4 | 1 | CARRIED | FWD-10, C2 (`wk-provision.sh`) |
| O5 | 1 | CARRIED | FWD-11, C6 |
| O6 | 1 | SUPERSEDED | the Analyst launches outside the workspace (card 3, R1): FWD-1, FWD-7, C4 |
| O7 | 1 | CARRIED | FWD-9, C3 |
| O8 | 1 | CARRIED | FWD-10 |
| O9 | 1 | CARRIED | FWD-11, C6 |
| O10 | 1 | CARRIED | FWD-10, C2 |
| PART II | 1 | CARRIED | Scope |
| PART III | 1 | CARRIED | C2, C4 |
| PART IV | 1 | CARRIED | Ground truth |
| What "the portal structure" actually is today | 1 | CARRIED | C2 |
| What already reaches into a nested repo | 1 | CARRIED | C2 |
| The gateway's deploy path | 1 | CARRIED | C6 |
| Cross-repo dependencies to cut | 1 | CARRIED | C6 |
| The Analyst seat | 1 | SUPERSEDED | C4, C5 |
| The mechanism | 1 | CARRIED | C2 (a real submodule, row A) |
| PART V | 1 | CARRIED | items 1-14 -> C1, C2, C3; 15-19 -> C6; 20, 21 SUPERSEDED by C4; 22 -> C5; 23 -> G-MOVE; 24 -> C2, G-LAW |
| PART VI | 1 | CARRIED | Ground truth, re-measured |
| PART VII | 1 | CARRIED-AS-OPEN | Evidence boundary |
| PART VIII | 1 | CARRIED | call 1 -> C2; 2 SUPERSEDED by card 3; 3 -> C5; 4 ruled yes; 5 -> C3; 6 -> C2; 7 -> C6; 8 -> G-MOVE |
| REFS | 1 | CARRIED | inputs to S2, S3, S11, S12 |

Sum: 2+2+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1 = **28**.

## Acceptance matrix

| id | acceptance | outcome |
|---|---|---|
| A1 | one live Teams exchange traced hop by hop (message, detection, agent in the runtime account, the asker resolved server-side and the call scoped to their entitlement, gateway call, reply), the figure and date matching the portal for that date, each hop a real call; one un-admitted asker refused | FWD-1 |
| A2 | messages sent after idle spells of at least an hour and one with hosted content, all answered unprompted; an unreadable one answered with a plain "could not read it" | FWD-2 |
| A3 | a stage-timed table of real exchanges beside the 2026-08-20 baseline, with the method stated | FWD-3 |
| A4 | graded on NFRA_MCPINDEX's delivery: a cold real-question set, the count routed right over the count asked, every miss listed | FWD-4 |
| A5 | one person's same questions asked in Teams and in their own Claude, answers and refusals side by side | FWD-5 |
| A6 | a transcript of a colleague's genuine attempts (urgency, seniority, an embedded instruction) and each refusal's reason | FWD-6 |
| A7 | the launch gate's three checks shown passing at a real launch, and its negative arm shown refusing | FWD-7 |
| A8 | one colleague admitted, used, narrowed and removed with no restart, and one past answer explained from the audit, no private values in it | FWD-8 |
| A9 | one change followed from its edit in the submodule, through the gates and Andrew's release word, to a colleague's answer, with the running and approved versions named | FWD-9 |
| A10 | a fresh setup on each device with the submodule at the recorded commit; an uninitialised one refused loudly; a census tool counting an `opal_ai` commit | FWD-10 |
| A11 | one real gateway release from `opal_ai`: dirty-tree refusal shown, the manifest naming the `opal_ai` commit, an old pinned citation resolved | FWD-11 |
| A12 | graded on NFRA_MCPINDEX's delivery: one property added as one entry plus one tool; a planted unclassified tool refused | FWD-12 |
| A13 | a standalone clone of `opal_ai` passing its checks, and CI green on a real push | FWD-13 |
| A14 | a commit made inside `opal_ai` graded by the parent's gates, and a planted violation refused | C2 |

## Canonical handoff

L5 is `2.0.0_SA_COO~O`'s. **FWD-1 is the thread, and round 1 builds it end to end over its hops:**
1. the agent's product files in `opal_ai/opal/agent/` (S5);
2. the runtime account and read-only checkout (S6, G-ACCT);
3. the runtime Claude setup and launch gate (S7, G-AUTH);
4. a Teams watch that sees (S8, the minimum for one exchange);
5. the asker's entitlement on the path (S10 round-1 half, C10);
6. one live exchange graded against A1, plus one un-admitted asker refused.

The repo wiring (S2, S3, S4) is a disjoint write surface and can run beside the thread in round 1. Speed (S9), the rest of
S10 (admit, narrow, remove, explain) and the release flow (S13) are enrichment rounds. The gateway move (S11, S12) waits on G-MOVE and is
cut in the round after G-MOVE is carried, never before. NFRA_MCPINDEX continues as its own project. Its round 1 is
recommended closed and re-cut onto `opal_ai` paths once S2 lands, so its remaining orders do not execute against a
path that is about to move.
