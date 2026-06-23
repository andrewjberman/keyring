# Opal Internal Tooling Platform -- SCOPE (the "Company Tools" page + serverless->server) -- FIRST-CUT

**Author:** 3.0.0_SA_CVO | **2026-06-23** | **For:** CTO architecture + Andrew product-direction. To develop into a CTO-led PRD.
**Origin:** Andrew-direct -- (1) a portal page = a repository of UI-wrapped tooling for ALL key SKILLS, with per-skill cron/automation; "needs a better name." (2) consider transitioning the dashboard serverless->server -- "may be getting to that time we need a persistent application." **The two are COUPLED** (automation + stateful tools NEED persistent compute). The M365 portal front-end (separate committed scope) = **tool #1** in this platform.

## 1. The vision (the "Company Tools" page)
Turn the org's key SKILLS (today CLI/agent-invoked) into UI-wrapped, runnable, schedulable tools -- one portal surface where an employee (or an automation) runs a skill from the browser, sees the result, and can put it on a cron. The M365 AI-assistant is the first; the catalog grows from there.
- **NAME** (better than "Company Tools"): candidates -- **Workbench** / **Operations Console** / **Launchpad** / **Automations Hub** / Studio. (Minor; defer.)

## 2. The model -- what a "tool" is here
A registered SKILL + a UI wrapper + an execution path + (optional) a schedule:
- **Registry:** the catalog of skills -- ideally auto-derived from the existing definitions (`.claude/skills/`, the comp-* tools, the agent workflows).
- **UI wrapper:** a per-skill form/panel (inputs -> run -> results), generated from the skill's input schema.
- **Execution:** the backend runs the skill on trigger (UI or cron). Agent/Claude skills -> Claude (API) + tools; comp-tools/data-ops -> the CLI/job; M365 -> the M365 backend.
- **Automation:** a per-skill cron/schedule + run-history + audit + alerting.
- **Auth/entitlements:** who can run/schedule which tool (the portal's JWT-firm auth + per-tool entitlements).

## 3. Candidate tools (Andrew defines the actual "key skills")
Seed examples: the M365 AI-assistant; comp-* graph/freshness/IAM queries; deck-generation; data-pipeline runs (gold/silver triggers); reporting/analytics exports; the agent workflows (research/review/audit). [Andrew's call on the v1 set.]

## 4. THE SERVERLESS -> SERVER QUESTION (the coupled infra decision)
The automation + stateful/long-running tools are the DRIVER. Current portal = serverless (Lambda/CloudFront). What serverless does NOT fit well:
- Long-running tasks (agent/Claude workflows, data-jobs) > Lambda's 15-min ceiling.
- The AI-assistant = streaming + stateful sessions.
- The cron/scheduler + run-engine = a persistent process.
- Real-time (WebSocket/SSE for streaming results / progress).

**PROS of a persistent server:** long-running + stateful + streaming + a real scheduler + no cold-start + persistent connections/caches/queues.
**CONS:** always-on cost; ops burden (patch/scale/monitor/the-app-is-now-a-thing-to-keep-alive); migration effort; loses serverless zero-idle + auto-scale; a new always-on attack surface.

**RECOMMENDED DIRECTION (first-cut): HYBRID, not a full migrate.** Keep the serverless analytics-serving (read-mostly, scales well, works today -- the ADVI/MP dashboards). ADD a persistent application layer (EC2/ECS/Fargate, Terraform-managed, fits the existing EC2 estate -- the M365 gateway is already an EC2) for the NEW stateful/long-running/automation capabilities (the run-engine + the AI-host + the scheduler). The "Company Tools" execution + crons live on the persistent app; the existing dashboards stay serverless. **DECISION: hybrid-add (recommended) vs full serverless->server migrate.**

## 5. Architecture (first-cut)
- **Portal frontend** (React/bun, existing): + the Company Tools catalog UI + per-tool panels + the cron-config + the AI-assistant chat.
- **Persistent app layer (NEW):** the run-engine (executes skills on UI/cron trigger), the scheduler, the AI-host (Claude API + tools), the M365 broker, the run-history/audit. EC2/ECS, Terraform, EC2_MANIFEST.
- **Serverless (existing, kept):** the analytics dashboards / data-serving.
- **Shared:** the portal auth/JWT/firm-scope, the comp-tools/skills, the M365 backend, the audit/lake.

## 6. Security / governance (CVO lens -- this is the big one)
- The run-engine executes skills with REAL privileges (data-ops change state; agent skills act broadly) -> a serious privilege + audit surface. EVERY run audited + scoped to the user + a kill-switch; **confirm-before-destructive** for state-changing tools; per-tool entitlements (not everyone runs every tool).
- The agent/Claude-workflow tools + the data-pipeline tools inherit the workspace's existing governance (CLAUDE.md rules, safe-* wrappers, the comp-rail) -- the platform must NOT bypass those (a UI "run gold" button still goes through safe-deploy/ds-gate).
- AI/M365 data-governance (AC5) applies (M365/data -> Anthropic).
- The persistent app = a new always-on attack surface -> EC2 hardening (the gateway's model).

## 7. Open decisions (CTO + Andrew)
- a. The name.
- b. The "key skills" v1 set (what's in the catalog first).
- c. Hybrid-add (recommended) vs full migrate.
- d. The run-engine tech + the agent/Claude orchestration (how a "skill" actually executes -- esp. the agent/workflow skills; is this the agent-fabric exposed via UI?).
- e. v1 scope (catalog + a few tools + crons, or start with the M365 assistant as tool-1 and grow).
- f. Governance model for UI-triggered privileged skills (the entitlements + the don't-bypass-the-gates requirement).

## 8. Relationship to the in-flight work
- The **M365 portal front-end** (committed scope) = tool #1; its AI-host + its persistent need are the FIRST instance of the run-engine + the server question -> scope them together (the M365 front-end rides this platform's persistent layer).
- **.06** (the Claude-native M365 front-end) is unaffected -- it's the Claude-client path; this is the portal-platform path. Two front-ends, one M365 backend (CTO framing) -- and now this platform is the broader home for the portal front-end.

## 9. Net
"Company Tools" = the Opal portal evolving into an internal tooling + automation PLATFORM (UI-wrapped skills + crons), which DRIVES a persistent application layer (hybrid serverless+server). The M365 assistant is tool #1. This is a significant platform initiative -- this is a FIRST-CUT for the CTO's architecture + Andrew's product direction; it should become a CTO-led PRD. The governance of UI-triggered privileged skills (S6) is the part I'd flag hardest for careful design. Decisions (name, key-skills, hybrid-vs-migrate, v1, the run-engine, the governance) are Andrew's + the CTO's.
