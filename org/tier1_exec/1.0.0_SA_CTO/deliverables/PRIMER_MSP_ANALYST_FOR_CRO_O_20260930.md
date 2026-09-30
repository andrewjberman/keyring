# PRIMER -- the MSP Analyst: Opal-hosted Teams agents for partner firms (for 4.0.0_SA_CRO~O)

**From:** 1.0.0_SA_CTO~O (site Z), 2026-09-30 ~01:0xZ.
**Why you have it:** Andrew-direct, same session, verbatim: *"This MSP analyst process, i want you to send everything
you've got on it, to CRO~O. Tell them that we need to discuss it (me and them), but you can give them a primer."*
**What it is:** a primer for a conversation between Andrew and you, not a brief, PRD or ruling. Nothing here is decided.
It is the design fork as it stood at the end of the 2026-09-29 session, with the grounding facts measured this session.

## 1. Andrew's words that frame it (verbatim, in order)

1. On harness vs API key: *"My question here is where the analyst is operating on a harness basis. For example, when we
   were running 0.0.3_BG out of a terminal, yes, it is running tools over GraphAPI to engage with Teams users. However,
   it is harnessed in Claude Code, it is connected to a repo, it is committing logs on its convos and has some processes
   built in. If we run it straight API key through some headless structure, where is it living? Where is our real-time
   supervision? Is running it in a Claude Code session a superior strategy because of this? I want to explore ideal
   setup on harness mechanics, governance, etc. for this operation, because we need to know how to best scale it."*
2. On the MSP: *"I know we are going to end up building these for clients. What I am wondering, is what is the best way
   for the clients to use this. I think Teams is a really low-impact way to do it, kind of like a market penetration
   strategy. But ultimately, they may want something with a UI. They might graduate. I want you to /draw the
   architecture for how we'd run this as an MSP for multiple partners with Teams agents. I think the approach would be
   that we build a server in our cloud which will be their specific MCP, hooked up to the relevant tables for them,
   which we also host in our cloud. What I'm wondering is, do we run the actual powershell sessions claude.exe on the
   sitez box or similar dedicated box? Then we have visibility directly into if these things are behaving and instant
   access/governance? Or is there a better way? /draw me the architectural layout of how this would look if we were to
   set up a teams agent for inflection and for cottonwood."*

## 2. What exists today (measured 2026-09-29/30, site Z)

- **The internal Analyst (NFRA_OPALAI)** runs as a separate local Windows account, `Opal_Agent`.
  - It is non-admin and DENIED the workspace (`verify-boundary.ps1`: DENIED-OK).
  - It reads a checkout of `opal_ai` PROD at `C:\opal_runtime\opal_ai` and writes only `C:\opal_runtime\state`.
- **It is already a Claude Code harness, not a bare API loop.**
  - `launcher.ps1` fetches PROD fast-forward, runs `launch-gate.ps1` as Opal_Agent, and only on `GATE: PASS` starts an
    interactive `claude.exe` as Opal_Agent.
  - That session loads its own `opal/runtime/CLAUDE.md`, which imports `opal/agent/prompt.md`: the `/bbg-teams-assist`
    serve loop, `teams_watch/`, `hooks/`, thread memory, the request catalog and an identity-acceptance gate.
  - It uses ONE MCP server, `opal-gateway-bbg` (`https://mcp.opalinvest.dev/mcp`).
- **Gaps in today's design, measured:**
  - Opal_Agent is read-only on the repo, so it cannot commit conversation logs; records stay in `state_dir` only.
  - The launcher starts an interactive session in the operator's console with no restart, so one crash takes it down
    (the site-Z crash of 2026-09-29 11:34 ET is the live example).
  - It reaches Teams by polling ONE Opal user account (Opal Bloomberg) in OPAL's own tenant.
- **Enforcement lives at the gateway, not the harness.** The gateway runs on EC2 `i-07dccb1615503ac99`, EIP
  3.214.118.242, release `093fc247c6` (52 tools), and applies three checks on every call, however the agent runs:
  - `identity_scope` (per-identity tool allowlist);
  - `asker_scope` (a read is bound to the SENDER of the cited Teams message);
  - fail-closed grants (no grant or no channels means no catalog), plus `audit.jsonl`.
- **Credential choice (open, Andrew's):**
  - `CLAUDE_CODE_OAUTH_TOKEN` via `claude setup-token` bills the Analyst's Claude subscription (rolling usage limits).
  - `ANTHROPIC_API_KEY` bills metered on the Console org (set a spend cap).
  - The runtime code references neither variable; both drive the same Claude Code harness.
- **Firm data is already separated.**
  - Inflection: `firm_id inflection`, tenant `F-INF`, bucket `opal-data-inf` (LIVE). Cottonwood: `cottonwood` / `F-COT` /
    `opal-data-cot`. Source: `infra/logic/05_IDENTITY_SPINE.md`.
  - The ruled successors `opal-data-inflection` and `opal-data-cottonwood` are not provisioned yet
    (`infra/logic/08_TENSION_MAP.md`).
  - The commit gate `.tools/ds-precommit-check.py` `_CROSS_FIRM_FOREIGN_BUCKETS` / `_KEY_PREFIXES` refuses cross-firm
    reads in pipeline code.
  - Served platinum exists per firm: `platinum/mdpf/{49financial,cottonwood,inflection}/`.

## 3. The harness analysis (as given to Andrew)

| | A. Interactive session (0.0.3_BG; Opal_Agent launcher as written) | B. Headless Claude Code, one run per Teams event | C. Raw Messages API loop |
|---|---|---|---|
| Where it lives | a terminal someone keeps open | a small always-on watcher; each inbound message spawns `claude -p` / Agent SDK | our own code |
| Keeps skills, hooks, CLAUDE.md, MCP | yes | yes, the same files | no, rebuilt |
| Survives a crash | no | yes | yes |
| Real-time supervision | a human watching | per-request transcript + hook logs + gateway audit | whatever is built |
| Scale | one process, one context | parallel, clean context per ask | parallel |
| Fit | dev, supervised pilot | production | not worth it |

CTO~O's recommendation: pilot on A, scale on B; ship transcripts and `state_dir` records to S3 on the operator side;
API key with a spend cap for B.

## 4. The MSP architecture drawn for Andrew (Inflection + Cottonwood)

```
OPAL MANAGED ANALYST (MSP) -- one Opal-hosted Analyst per partner firm, reached from the firm's own Teams

1. The tenancy plane -- each firm gets its own data, its own tools and its own brain, and never sees another's

   FIRM DATA (Opal AWS)       FIRM MCP (tool scope)        AGENT WORKER (brain)          CHANNEL
  ┌──────────────────────┐   ┌───────────────────────┐   ┌──────────────────────────┐   ┌─────────────────────────┐
  │ INFLECTION           │   │ gateway, firm=        │   │ worker: inflection       │   │ "Opal Analyst" Teams    │
  │ firm_id inflection   │──►│ inflection; role may  │──►│ headless Claude Code per │◄─►│ bot = ONE multi-tenant  │
  │ F-INF, opal-data-inf │   │ read ONLY opal-data-  │   │ event; own IAM role, own │   │ Entra app, Opal-owned,  │
  │                      │   │ inf (bucket-scoped    │   │ API key + spend cap, own │   │ admin-consented INTO    │
  │                      │   │ Deny on other firms)  │   │ prompt; ONE MCP server   │   │ each firm's M365 tenant │
  └──────────────────────┘   └───────────────────────┘   └──────────────────────────┘   │ Bot Framework webhook   │
  ┌──────────────────────┐   ┌───────────────────────┐   ┌──────────────────────────┐   │ (push, not polling)     │
  │ COTTONWOOD           │──►│ gateway, firm=        │──►│ worker: cottonwood       │◄─►│                         │
  │ F-COT, opal-data-cot │   │ cottonwood            │   │ (same harness, own role) │   └────────────┬────────────┘
  └──────────────────────┘   └───────────────────────┘   └──────────────────────────┘                │ tid in activity
                                                                                      ┌─────────────────────────┐
                                                                                      │ ROUTER: tid -> firm_id  │
                                                                                      │ unknown tid = REFUSE    │
                                                                                      └─────────────────────────┘
2. Query plane: advisor @Opal Analyst in their Teams -> bot -> router (tid, asker oid) -> firm worker (fresh run)
   -> firm gateway (asker_scope clips to that advisor's grant) -> answer in the thread, vintage attached.

3. Control plane: every run's transcript + tool calls + gateway audit, tagged firm/asker/run -> S3 audit store per firm
   -> OPERATOR CONSOLE (site Z box or any Opal laptop). Kill switches, narrowest first: revoke one asker's grant ->
   disable one firm's worker/role -> spend cap on the firm key -> pull the bot's consent. The site Z box stays the
   DEV + PILOT seat (a new firm runs interactively there, watched, before moving to the cloud worker).
```

**Box vs cloud worker, as given to Andrew:**

| | claude.exe sessions on site Z | headless workers in Opal's cloud |
|---|---|---|
| visibility | a terminal per firm | a console over transcripts + audit, all firms, replayable |
| instant stop | close the window | disable role / grant / key |
| isolation between firms | OS accounts on ONE machine | separate roles, keys, containers |
| crash | every firm goes dark | only the one run fails |
| scale to N firms | N sessions, N MFAs, one box | one more worker + a router row |
| Teams reach | polls ONE Opal user in OUR tenant; cannot see a client's tenant | bot consented into EACH client's tenant; no guest accounts |
| best use | dev, pilot, first watched weeks | production |

**The Teams -> UI graduation:** firm data, firm gateway, worker, grants, audit and console stay the same. Only the
channel changes: a chat panel in the client's portal calls the same router with the same firm_id and asker identity.

## 5. Open questions for the Andrew + CRO~O discussion (CTO~O's list, not exhaustive)

1. **Channel identity.** A multi-tenant Teams bot needs each client's M365 admin consent. What does Opal ask of a partner's
   IT, and what past pattern exists (0.0.3_BG, the NFRA_OPLGTW G-C "new M365 user" experience today)?
2. **Asker identity across tenants.** Grants today key on Opal-tenant identities (tid/oid). How does a partner advisor's
   oid bind to a grant, and who administers it: Opal, or the partner through the MCPORTAL Entitlements tab?
3. **Harness at scale.** Is B (headless Claude Code per event) the target, and what supervision does Andrew need to see
   before a partner goes live: live tail, replay, graded samples, a daily report?
4. **Data home per firm.** Serve from the legacy buckets (`opal-data-inf`, `opal-data-cot`) or wait for the ruled
   successors? The LGIC migrations (R19) are separate projects, so this interacts with sequencing.
5. **Commercials and limits.** A per-firm API key and spend cap versus a pooled key, and per-firm cost visibility.
6. **Governance.** Which acts stay Andrew's (onboarding a firm is his word per the identity spine), what the CVO grades,
   and what a partner-facing SLA would promise.
7. **Scope boundary.** A new project (recommended), or an extension of NFRA_OPALAI / NFRA_OPLGTW?

## 6. Where to read further

- Internal Analyst runbook: `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/1.0.0_SA_CTO~O/ANDREW_SWITCHOVER_RUNBOOK.md`.
- Elevated provisioning handoff (G-ACCT, G-AUTH): `org/missions/D6/NFRA/NFRA_OPALAI/deliverables/2.0.0_SA_COO~O/HANDOFF_G-ACCT_ELEVATED_20260928.md`.
- Runtime code: `C:\opal_runtime\opal_ai\opal\runtime\` (launcher, launch gate, provision) and `opal\agent\` (prompt, skills,
  teams_watch, hooks).
- Firm identity and bucket law: `infra/logic/05_IDENTITY_SPINE.md`, `infra/logic/02_DOCTRINE.md`,
  `infra/logic/08_TENSION_MAP.md`.
- Gateway scoping: `infra/aws/ec2/opal-gateway/app/identity_scope.py`, `app/asker_scope.py`.
