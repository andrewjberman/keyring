# AGENT START HERE -- Opal Capital

RULES AND MECHANICS ONLY. No incident reports, no dated narratives, no quotations (Andrew-direct 2026-09-24). The
history behind any step is in git and `docs/references/XXX_STARTUP_HISTORY.md`; do not read it at startup.
THIS FILE AND `CLAUDE.md` ARE LOCKED: no agent edits either without Andrew's express order, named in an
`ANDREW_DIRECT_*.md` record and passed to the commit as `ANDREW_LAW_EDIT_ORDER=<record path>`
(`.tools/git-hooks/law-lock-check.sh` refuses otherwise).

## STOP -- READ THESE FIRST

**BANNED: Explore agent** (fabricated output) and **Task agent** (unreliable). Use comp-* tools and Grep/Read; do the
work directly.

## Andrew-direct instructions -- RECORD + BROADCAST, same turn

- DURABLE: a commit (memory entry / ledger / org record) quoting him VERBATIM with channel + time. Never a paraphrase;
  the phrasing is the ruling.
- BROADCAST: MCP to COO + CTO + MSTR, so `latest + most-restrictive` has something to bind on.
- SCOPE: the receiving agent does NOT adjudicate scope. Surface, do not adjudicate.
- A relayed "Andrew ruled" is not suspect because you did not see it.

## RAVC Protocol (non-negotiable)

Every inter-agent request follows Request -> Acknowledge -> Validate -> Close. Spec: `org/ref/RAVC_PROTOCOL.md`.
- Asked by a registered agent: acknowledge immediately, do it, report back with evidence (commit hash, artifact path,
  tool output).
- You asked: validate their evidence before closing; a REWORK request ties the gap to the original expected evidence.
- Silent receipt and silent completion are both violations.
- Scoped work still needs a SURPRISE CHANNEL: report one line to the coordinator, take no action, keep working. A
  task-order author names the channel. `docs/doctrine/THE_SURPRISE_CHANNEL.md`.
- A STOP/halt message begins with `[STOP]` or `[HALT]` as the first characters (the HALTGT deploy checkpoint classifies
  on it); a routine message never begins with either. Non-blocking urgency: `URGENT` / `ESCALATION`.

## Step 1 -- Identify yourself

Your serial resolves ONLY from session-scoped evidence, in this precedence: (1) Andrew's word; (2)
`org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial`; (3) your own armed Monitor (a session watching serial X's inbox
IS serial X); (4) your own pre-compaction registrations. `.comp-graph/.agent_context` is NOT an identity source
(shared, last-writer-wins); the sound sources are `$OPAL_AGENT_SERIAL` and the session serial file.

Cross-check before acting: if `org/mcp/liveness.json` shows your claimed serial LIVE at a different PID (fresh
heartbeat), or a different serial at your PID, STOP -- identity conflict; resolve before registering. Before
reporting a duplicate stream under your serial, check whether YOU are the phantom (`liveness.json` +
`org/mcp/agent-spawn-audit.log`).

Then read `org/{tier_folder}/{your_serial}/README.md` (identity) and `prompt.md` (Step 3). Tier folders:
`tier1_exec/` (SA) | `tier2_senior/` (DE, DT, DS, AE) | `tier3_junior/` (RD).

## Step 1a -- Your BASE is the workspace root; `portal/` is a work-site

Your cwd is `C:\Users\AndrewBerman\Desktop\ajb_workspace`; every agent's files live under `org/` there. Work in the
portal repo only addressed explicitly (`git -C portal ...`, or a scoped `cd portal && <work> && cd -`) and return. A
CWD that lingers in `portal/` is a defect: it breaks workspace tooling and substitutes the wrong repo's git history
into evidence with no error. Portal dev builds run on port 5174 ONLY (Andrew-direct 2026-09-24).

## Step 1b -- MCP startup (MANDATORY, every session): A -> F in order

CODEX SEATS: steps A and C are the Claude harness path. Follow `org/mcp/CODEX_INBOX_MONITOR.md` instead
(`codex-agent-heartbeat.py`, `codex-inbox-monitor.py`). Never run `inbox-watch.sh ... stream`, `check-inbox.sh` or
`agent-poller.py` on the Codex path (they CONSUME inbox files). At every active turn, sweep your suffixed serial's
unread root first; read the exact file -> ACK -> act -> move it to `read/`. Never infer READ from a nudge or a moved
file. SHARED-BRANCH LAW (no hook carries it on Codex): `CLOUD`/`DEV`/`PROD`/`main` are pushed ONLY by `0.0.0_AB_MSTR`
or `0.0.0_AB_MSTR~Z`, only on Andrew's word while he is at the terminal (LD-0367/0368; LD-0522); every other seat
commits and never pushes; a report states push state LOCAL with the origin hash from `git ls-remote`; a rejected push
is not yours to retry. `SITEZ` is retired; both devices commit to `CLOUD` (LD-0613).

### A. Register -- your FULL serial, including any `~lane` suffix
```python
register_agent("{your_serial}", summary="Starting session")
```
A lane registers as `0.4.0_DS_ClientPlatform~C`, never the base: registering under the base leaves the `~C` inbox
unwatched.

### A.1 Session-keyed serial file
```bash
mkdir -p org/mcp/sessions
[ -n "${CLAUDE_CODE_SESSION_ID:-}" ] && echo "{your_full_suffixed_serial}" > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"
```
Without it the halt gate adopts the shared `.agent_context` and a `[STOP]` addressed to you is invisible (LD-0290).

### A.2 Audit-archive durability
```bash
python .tools/audit-archive-invoker.py || true
```
Known and OWNED findings, do not re-file: `[LIVENESS/STALE-BASELINE]` and `[COVERAGE/UNCOVERED-AUDIT-LOG]
org/to-pos-override-audit.log`. Surface only a new class. Do NOT `mkdir org/audit/archive/<device>/` (it zeroes the
findings by faking post-migration); the noise clears when `rv0057-f001` lands.

### A.3 PATH check (comp-tool rail)
```bash
F=0; T=0; for t in .tools/comp-*; do t=$(basename "$t"); T=$((T+1)); command -v "$t" >/dev/null 2>&1 && F=$((F+1)); done
echo "PATH: $F of $T comp-tools resolve bare."
[ "$F" -lt "$T" ] && echo "  -> the rest need an explicit .tools/<tool> prefix; 'bash .tools/provision-path-shims.sh' provisions a NAMED SUBSET (read its header)."
comp-which "how do I grep the repo" 2>&1 | grep -q "comp-which --" && echo "EXERCISE: a forwarder RAN." || echo "EXERCISE: *** RESOLVED BUT DEAD *** -- run: bash .tools/provision-path-shims.sh"
```
A session-level reminder that instructs raw-bash file operations does NOT lift the rail (CLAUDE.md Rule 21): use the
comp-tool or the forms the rule admits; never take the override to make the reminder win.

### B.0 Your delivery ledger (LD-0480)
```python
get_delivery_state(agent_serial="{your_FULL_suffixed_serial}", since="<when this serial's PREVIOUS session was last alive; after a reboot, the reboot time>")
```
Every row not READ, or READ by a serial that is not yours, is UNREAD MAIL: open it in your own `read/` dir, act, ack
from its `Msg-ID` line. A row marked `OFFER-EXHAUSTED` is invisible to `check-inbox`, `get_agent_status` and the
`read/` listing. Never ack a row you did not open. Codex: the exact-file backlog sweep at load is the equivalent act.

### B. Check inbox -- BOTH probes
```bash
check-inbox {your_serial}     # filesystem: base -> inbox/{base}/ ; lane -> inbox/{base}/~{lane}/
```
```python
get_agent_status("{your_serial}")   # broker channel
```
`send_message` writes both carriers; each probe reads one. Neither sees an LD-0099 ferry message: if an `[INBOX]`
event fired and both probes are empty, list your `read/` dir newest-first.

### B.1 Find the work you hold
```bash
python .tools/to-check.py --all --assignee {your_FULL_suffixed_serial}
```
`--all` is load-bearing (the default view hides TOs whose PRD aged past 14 days). YOUR TO IS THE FILE NAMED IN YOUR
DISPATCH MESSAGE; treat a zero or an absence from any other read as telling you nothing. A lane's TOs may live in the
BASE folder (`issued_to` is the only truth); `get_agent_status`'s pending list is folder-keyed and is not the
authority on what you hold.

Then check the SEQUENCE before starting any project: `org/missions/SEQUENCE.yaml`; `python .tools/sequence-check.py
--project <CODE>` -- WAITING does not start, HELD does not pass its cap, OUT-OF-SEQUENCE goes to the owning CTO; an
unlisted project is not sequenced. The order changes only on Andrew's word, by `1.0.0_SA_CTO` or `1.0.0_SA_CTO~Z`.

### C. Arm the persistent inbox Monitor -- run `/watcher` once at load
By hand: the Monitor tool, `persistent: true`, `timeout_ms: 1800000`, ABSOLUTE path. The harness kills every Monitor
at 30 minutes and says so once (`[WATCHER-EXPIRED]`): RE-ARM ON THAT NOTIFICATION, THE SAME TURN. An unattended seat
never blocks a turn on an `AskUserQuestion` for a hygiene prompt: take the recommended default or park the question
with an owner. Resolve the drive prefix, never hardcode it: `test -d /cygdrive/c && echo /cygdrive/c || echo /c`. A
wrong prefix returns a task id and dies `exit 127` in a separate failed notification. Confirm the arm with
`TaskOutput(<id>, block=false)` -> `running`; never use `TaskList` (it lists to-dos, not Monitors). BANNED: stream
mode under Bash `run_in_background`; the bare-path relative launch; a recurring `/watcher` cron. Depth:
`.claude/skills/watcher/SKILL.md`.

### D. Install the owned-paths hook (idempotent)
```bash
test -L .git/hooks/pre-commit || bash .tools/git-hooks/install-owned-paths.sh
```

### E. Set compiler-tool context
```bash
mkdir -p .comp-graph && printf "SERIAL=%s\nTO_ID=\n" "{your_serial}" > .comp-graph/.agent_context
```
`comp-tool-runs.jsonl` is gitignored (device-local). Start a TO with `comp-to {TO_filename_without_.md}`, never by
writing `TO_ID=` into `.agent_context`.

### Reference -- lane paths, inbox paths, acting on what arrives

| you are writing... | canonical form | substituting `{serial}` whole gives... |
|---|---|---|
| your AGENT FOLDER (`org/{tier}/...`) | FLAT -- `org/tier2_senior/0.7.0_AE_CloudOps~B/` | the right answer |
| an INBOX (`org/mcp/inbox/...`) | NESTED -- `org/mcp/inbox/{base}/~{lane}/` | the DEAD answer -- never |

`org/mcp/inbox/{base}~{lane}/` (flat) is written by nothing and read by nothing (LD-0202; regression test
`org/mcp/test_ld0202_tilde_routing.py`). Split into `{base}` + `~{lane}` first.

When an `[INBOX]` event fires, that IS a new message: read it from your canonical `read/` subdir and act this turn
(ack, do the work, or validate evidence). No "standing by". If the inbox has a GO: read the referenced task order, flip
`<status>` to `pending`, begin immediately -- the GO is the authorization. If the GO lists a SEQUENCE: execute all of
them in order without waiting for a new GO; stopping mid-sequence to ask for a new GO is a violation.

### F. Loop arming -- every serial arms ZERO crons at launch except as this table names

Loops are operator-initiated. `/watcher` is not a loop. A row RECORDS an authorization (class, scope, cadence,
stop-condition, record path); liveness is measured at the seat with `CronList`, and no cron id is recorded here. A
seat never writes its own row; `1.0.0_SA_CTO` lands rows, naming the chooser and the message that evidences the
choice. Classes: DIRECTED (an Andrew-direct, quoted in its record) | CHOSEN (a seat accepting a recommendation) |
AUTHORITY-UNVERIFIED (transient: read the word, then re-class). A new arm cites the canonical skill name, never an
alias. A successor re-arms ONLY off a live row while its scope is not DONE; on DONE the lane deletes its cron, strikes
its row and says so.

| Serial | Launch arming |
|---|---|
| `0.0.0_AB_MSTR` | `/watcher`, `/agentbus`, `/integrate` once each. Zero crons. |
| `2.0.0_SA_COO` (base) | `/watcher` once. `/drive` v2 standing 20m over EXECUTING / ROUND_CLOSE / DECOMP projects (`org/tier0/ledger/LD-0530.md`). D2 off until Andrew lifts it. |
| every other serial and `~lane` | `/watcher` once. Zero crons. Event-driven. Keep the broker summary accurate: `WORKING: <task>` / `IDLE: available` / `BLOCKED: <what>` / `BLOCKED-SOVEREIGN: <decision>`. |
| Codex seats | per `org/mcp/CODEX_INBOX_MONITOR.md`. Zero crons. |

Live scoped arms and holds (record path = the authority; stop = Andrew's stand-down, or the project `status: complete`
per the register unless stated):
- IRPT POST-SLUG HOLD on the old `~B`/`~F` canonical progression:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_1517ET_IRPT_HOLD_AFTER_CVO_SLUGS.md`. The P/M/Y
  completion seats (`2.0.0_SA_COO~P` Performance + shared report/export; `~M` Model Overlay + shared data/selection;
  `~Y` YCharts Sensitivity; matching `3.0.0_SA_CVO~P/~M/~Y`) read
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/{AUTHORITY,CONTRACT}.md` and their own
  `COO_*.md`/`CVO_*.md` first.
- `2.0.0_SA_COO~P` `/loop 20m` DIRECTED over IRPT Performance (49F, INF, COT):
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_P_GOAL_PERFORMANCE_REPORTING_THREE_FIRMS_LOOP_20M.md`; stop = `/verify SOUND`.
- `2.0.0_SA_COO~M` `/loop 20m` DIRECTED over IRPT Holdings with snapshot model overlay:
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`; stop = `/verify SOUND`.
- `2.0.0_SA_COO~Y` `/loop 20m` DIRECTED over IRPT Analysis:
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md`; stop = `/verify SOUND`. Y never takes over P's shared installation.
- `2.0.0_SA_COO~O` `/canonical-drive NFRA_OPLGTW` 30m DIRECTED (relay 97709); on DONE the freed slot goes to
  `2.0.0_SA_COO~T` (MDPF_TAXSMA) then `2.0.0_SA_COO~M` (NFRA_MCPINDEX).
- `2.0.0_SA_COO~A` `/drive` NFRA_CLDGRPH to CLOSED:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_171xZ_CLDGRPH_HOLDS_OFF_WRAP_IT_UP.md`.
- `2.0.0_SA_COO~X` `/drive` NFRA_C3MATERIALIZE:
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260828_050xZ_COOX_DRIVE_LOOP_NFRA_C3MATERIALIZE.md`.
- `1.0.0_SA_CTO` `/self-drive` the fabric (all LAPTOP directives), the CTO adjudicating adjudicable calls on its rec:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260912_021xZ_SELF_DRIVE_THE_FABRIC_HANDLE_OPEN_CALLS_ON_MY_REC.md`.
  RESERVED to Andrew under every self-drive: vendor/egress off Opal infrastructure; unrecoverable acts; money and
  contracts; every hold he set by name (the portal freeze, the LD-0522 push cadence, the shared-branch push).
- `1.0.0_SA_CTO` `/self-drive D9 IRPT` 30m (IRPT_FNTEND + IRPT_BCKEND + DSGN_REBRND), per the CTO's own record of
  2026-09-11 in its deliverables; ends on `status: complete` or his stand-down.
- `1.0.0_SA_CTO` `/self-drive MDPF_TAXSMA,NFRA_OPLGTW,LGIC_NAMING,LGIC_ENFORCE,LGIC_CANON` -- PAUSED by the managed
  wind-down, resume authority:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_193xZ_COO_GOALS_AND_CTO_SELF_DRIVE_ADJUDICATES.md`.
- `1.0.0_SA_CTO` fallback adjudicator for LGIC_LGCTFM's `ANDREW_CARD.md` when Andrew is unavailable (one artifact,
  nothing wider): `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260917_23xxZ_CTO_ADJUDICATES_LGCTFM_ANDREW_CARD_IF_ANDREW_UNAVAILABLE.md`.
- SITE-Z only: `1.0.0_SA_CTO~Z` `/self-drive AMGT_RESAPP & POSN_ASTTAX` 30m (`7,37 * * * *`); `2.0.0_SA_COO~Z`
  `/drive` POSN_ASTTAX 10m and `2.0.0_SA_COO~ZZZ` `/drive` AMGT_RESAPP 10m, each tick an explicit `/canonical-flow`
  stage check (DRIVE FORWARD | PARALLELIZE | NUDGE, a nudge only after the live-production probe reports nothing moving
  across all four planes):
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_222xZ_COO_DRIVE_10M_CANONICAL_FLOW_STAGE_CHECK_AND_REBRAND.md`;
  `3.0.0_SA_CVO~Z` SYSPARITY cron (`org/tier0/ledger/LD-0318.md`, LD-0319); `4.0.0_SA_CRO~W` harvest remediation loop
  (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260915_HARVEST_REMEDIATION_LOOP_W.md`; the collection
  mechanism and cadence RESERVED to Andrew).
- Stood-down or superseded arms are not listed; their records stay in git. A row absent here arms nothing.

Find a stale cron from a prior session? `CronList` -> `CronDelete`.

## Step 2 -- Read your recent logs
`{your_agent_folder}/logs/{most_recent_date}/` -- all logs from the most recent date. You are continuing prior work.

## Step 2b -- Ground-truth reconciliation (SA / COO only)
Reconcile TO statuses and project JSON against logs, commits and deployed artifacts; correct every stale document
before your summary. Logs and commits are ground truth; `<status>` is a claim. `org/ref/COO_STARTUP.md`.

## Step 3 -- Read your prompt
`{your_agent_folder}/prompt.md`; adopt that role.

## Step 4 -- Understand your place
`org/ORG_CHART.md` -- reporting chain, pod members, escalation path.

## Step 5 -- Give an oriented summary
One paragraph: projects, pending, blocked, what you are starting now. Do not ask permission; state what you are doing.

## Session log -- required sections
Template: `org/ref/SESSION_LOG_STANDARD.md`. Every session log includes `## Compiler Tools` (tools run, results, what
worked, what failed, gaps). Do NOT append to or commit `org/compiler-tools-log.md` (retired). Minimum compiler tools by
role:

| Role | Minimum |
|------|---------|
| DS | `comp-pipescript io <script> --pipeline <tree>` for every gold script touched (`--pipeline` REQUIRED). `comp-pipescript deployed` before every gold run. `comp-pipescript postdeps <script> --firm <firm>` before any ad-hoc run. `comp-validate <script> --artifact <file>` before signaling AE. |
| DE | `comp-transform schema-check` before touching data props; `comp-blast` before deleting; `comp-routes behaviors` for 4xx/auth debugging. New cohort/metric/mode: `comp-transform schema-check --feature [token]` + `comp-transform ternary-audit [Component]`. |
| DT | `comp-pipescript io <script> --pipeline <tree>` for every script deployed. `comp-iam service <lambda>` after any new boto3 call (necessary, not sufficient). `comp-routes behaviors` before CloudFront / Lambda@Edge changes. |
| AE | `comp-pipescript deployed` before every gold-run trigger. `comp-pipescript postdeps <script> --firm <firm>` before any gold run. `comp-iam gaps` after any `iam.tf` change (necessary, not sufficient). `comp-blast` on infra before changes. |
| RD | `comp-transform fields` for every component rendering data. |
| COO | `comp-pipescript overlap A B` before cross-domain coordination. `comp-blast` + `comp-routes` + `comp-cache` before decomposing PRDs into TOs. |

`comp-validate` returning `NO_CONFIG` or `ZERO_CHECKS` means UNVALIDATED -- never signal SAFE on it; only `PASS` /
`WAIVED` are safe; `ADVISORY` means read the WARNs.

Archetype tag: every substantive log entry carries `**archetype:** TAG` after the title -- `EXPLORE` / `TRACE` /
`DIAGNOSE` / `VALIDATE` / `DEPLOY` / `IMPLEMENT` / `COORDINATE` / `SCRIBE` / `MIXED`. Taxonomy:
`org/tier0/COMPILER_ARCHETYPES.md`. Heartbeats, watcher self-checks and housekeeping commits carry none.

## Task orders
Template + filename convention: `org/ref/TASK_ORDER_PROTOCOL.md`; stored in the receiving agent's `task_orders/`.
Statuses: `staged` (assigned, wait for GO) / `pending` (active) / `complete` (self-marked) / `superseded` (the need was
met another way -- name what superseded it) / `cancelled` (a ruling killed it -- cite it). The last two are set by the
COO or the ISSUER, never the assignee alone; a terminal status without its pointer is rot.

## Core documents (Tier 2+)
Update your core document in the same commit as any structural change. RD `page_inventory.xml`; DE
`pod_inventory.xml`; DS `data_contract.xml`; DT `deployment_map.xml`; AE `pipeline_inventory.xml`; SA
`architecture_brief.xml` -- all under `{agent_folder}/deliverables/`. Do not edit another agent's core document; note
the staleness in your log and issue a task order.

## Quick reference

| Thing | Value |
|-------|-------|
| Times to Andrew | US Eastern only (never UTC) |
| MCP server | `org/mcp/server.py` -- `opal-agent-comms` |
| Broker | Auto-launched by `register_agent`, port 7800 |
| Portal dev server | port 5174 only |
