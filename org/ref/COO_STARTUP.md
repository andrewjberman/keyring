# COO / CTO Startup: Ground Truth Reconciliation

This step is for SA agents (CTO, COO) only. Regular DE/DS/DT/AE/RD agents skip it.
Referenced from XXX.md Step 2b.

---

## Purpose

Reconcile declared state (task order statuses, project JSON phases, registry rows) against
actual state (agent logs, git commits, deployed artifacts). Every discrepancy found MUST be
corrected immediately using Edit — before presenting the oriented summary.

---

## Protocol

### 1. Check your own task orders
```
list_task_orders({your_serial})
```
For each PENDING task order: is the work actually done? If yes, edit `<status>` to `complete`.

### 2. Audit all agents on active projects

For each active project in REGISTRY.md:
```
query_project({project_code})
```
For each pending task order, check the assigned agent:
```
get_agent_status({agent_serial})
```
Then verify actual completion with evidence — not just the `<status>` field:
- Latest logs: does the log describe the deliverable as done?
- Commits: `git log --author="{serial}" --oneline -10`
- Deployed artifacts: git tags, S3 objects, terraform state

| Evidence | Classification | Action |
|----------|---------------|--------|
| Logs + commits confirm deployed/delivered | Done | Edit status to complete, update project JSON |
| Logs show work in progress, partial commits | In flight | Note in summary, no change |
| No logs, no commits, no activity | Not started | Note as AMBIGUOUS |
| Marked complete but no supporting evidence | Unverified | Flag — do NOT trust without evidence |
| Status is `staged` — no go received | Held | Do NOT begin, wait for GO |

### 3. Check upstream — agents who issued work to you

For each PENDING task order in your `task_orders/`, check `<issued_by>`:
```
get_agent_status({issuing_agent_serial})
```
Did scope change? New dependencies? Are they aware of your blockers?

### 4. Check dependencies — task orders you're waiting on

For each `<dependency>` in pending task orders:
```
list_task_orders({blocking_serial}, project={project_code})
```
If the dependency is complete, update `<dependency status="">` to `complete`.
If deps are met and your TO is `pending`, proceed.
If your TO is `staged`, do NOT begin — wait for GO even if deps are met.

### 5. Update all status documents

After steps 1-4, update:

**Project-level:**
- Project JSON `phase` — rewrite to match actual state
- Project JSON `blocking` — update to reflect current blockers
- Project JSON `status` — set to `"complete"` if ALL TOs done and deliverables verified
- REGISTRY.md — Phase and Blocking columns match project JSON

**Exec-level (CTO):**
- CTO `prompt.md` dashboard — Active Projects, Recently Completed, Pipeline Tags
- COO `prompt.md` dashboard — Pod Delivery Dashboard, Operational Health Checks
  COO boots from these tables. Stale tables = wrong assumptions on next COO session.

### Rules

- **Write, don't report.** Every stale document MUST be corrected before your oriented summary.
- **Logs and commits are ground truth.** `<status>` is a claim; verify before trusting.
- **Flag uncommitted work.** `git status` and `git diff --name-only` catch changes invisible to other agents.
- **Skip gracefully** if no active projects and no pending task orders.
- **AMBIGUOUS** is the honest state when evidence is absent — routes to COO/DE, doesn't stall you.

---

## MCP Tools Reference

| Tool | When to use |
|------|------------|
| `get_live_agents(pod?)` | See who's currently online |
| `get_agent_status(serial)` | Quick check on any agent |
| `read_agent_latest_log(serial)` | Full log when you need completion evidence |
| `list_task_orders(serial, status?, project?)` | Task order status per agent |
| `query_project(code)` | All task orders across all agents for a project |
| `get_org_summary()` | Org-wide view: live agents, active projects, pending work |
| `set_summary(serial, summary)` | Update your work description |
| `send_message(from, to, subject, body)` | Async message to another agent |

---

## Long-Running Operation Polling (SSM / gold runs / deploys)

When you dispatch a long-running async operation, poll — do not sleep.

**Cadence:**
- Poll the operation every tool call cycle (~15-30s natural latency)
- Heartbeat every 2nd or 3rd poll: `set_summary(serial, "Gold run: 45 min elapsed, script 06b running")`
- No `sleep` commands — tool call round-trips are the pacing

**SSM exit conditions:**

| Status | Action |
|--------|--------|
| `InProgress` | Continue polling |
| `Success` | Run post-run validation (S3 ls, spot-check files, cross-validate metrics) |
| `Failed` | Pull stdout + stderr, diagnose. SSM truncates at 24KB — pull full log from S3 path. |
| `Cancelled` | Report to COO via send_message, do not retry without instruction |
| `TimedOut` | Check S3 log path for partial output, report |

**SSM command template (gold layer runs):**
```bash
cd /home/ubuntu/gold-layer/scripts \
  && aws s3 sync s3://opal-data-bd/code/gold/ . \
  && chmod +x *.sh *.py 2>/dev/null; \
  ./run_gold_layer.sh full 2>&1 \
  | tee /var/log/gold-full-run.log \
  && aws s3 cp /var/log/gold-full-run.log \
     s3://opal-data-bd/logs/gold-layer/gold_full_{task_slug}_$(date +%Y%m%d_%H%M%S).log
```
Key: S3 sync first (no stale code), tee for local + remote log, timeout 7200s.
