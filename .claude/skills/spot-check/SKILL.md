---
name: spot-check
description: CVO-scoped alignment-sweep cycle. Reads recent commits from ajb_workspace agents (since `.spot-check-checkpoint`), verifies each touched system still works (verify-channel discipline), checks cross-doc alignment (REGISTRY vs project JSON vs TO `<status>` vs PRD `Status:` etc.), and — uniquely for this mode — fixes alignment-metadata drift directly under CVO author line before MCPing the change to COO. Out-of-scope drift (code, infra, runtime, other-agent authoring lanes) routes as a normal CVO finding to the responsible driver + CC COO. `/spot-check` arms a 20m cron + runs one cycle now; `/spot-check 30m` / `1h` / `90s` overrides cadence; `/spot-check once` runs a single cycle no cron; `/spot-check off` cancels any running cron. CVO-only — other agents invoking this skill should halt at Step 0. Full doctrine + fix-scope table at `org/tier1_exec/3.0.0_SA_CVO/SPOT_CHECK.md` (charter Andrew directive 2026-05-23).
---

# /spot-check — CVO Alignment-Sweep Cycle

The agent-commit-grain analogue to `VALIDATION_LOOP.md`'s artifact-and-key-juncture focus. Sweeps recent agent commits, verifies their systems still work, repairs alignment-metadata drift directly within bounded scope, MCPs the change to COO. Coexists with `/loop 30m`.

**Authoritative charter:** `org/tier1_exec/3.0.0_SA_CVO/SPOT_CHECK.md` — this skill is the executable entry point; the charter has the full doctrine, fix-scope table, and coexistence rules. Read the charter once per session if not in context.

---

## Invocation forms

| Form | Behavior |
|---|---|
| `/spot-check` | Run one cycle now + arm a 20m recurring cron (default, off-marks `13,33,53 * * * *`). |
| `/spot-check 30m` / `1h` / `90s` / `15m` | Run one cycle now + arm a recurring cron at the given cadence. Off-marks chosen automatically. |
| `/spot-check once` | Run one cycle. Do NOT arm a cron. |
| `/spot-check off` (or `stop`) | Cancel any existing `/spot-check` cron via `CronList` + `CronDelete`. No cycle. |

The recurring cron auto-expires after 7 days per `CronCreate` default. Re-arm on session restart or at the 7-day boundary.

---

## Step 0 — Identity gate (CVO-only)

This skill is scoped to `3.0.0_SA_CVO`. If the invoker is not CVO, halt with:

> `/spot-check is a CVO-scoped skill. Your serial is {serial}, not 3.0.0_SA_CVO. If you want an alignment sweep, MCP CVO directly with the ask; CVO will handle from its own session.`

If CVO, continue.

---

## Step 1 — Arm / cancel cron per invocation form

| Invocation | Cron action |
|---|---|
| Bare `/spot-check` or `/spot-check {interval}` | `CronList` → if no existing job whose prompt contains "spot-check", `CronCreate(cron=<off-marks expression>, prompt="/spot-check 20m -- run one cycle of the CVO spot-check loop per org/tier1_exec/3.0.0_SA_CVO/SPOT_CHECK.md. You are 3.0.0_SA_CVO.", recurring=true)`. If a cron already exists at the same cadence, no-op. If different cadence, `CronDelete` + re-create. |
| `/spot-check once` | Skip — no cron action. |
| `/spot-check off` / `stop` | `CronList` → for each job whose prompt contains "spot-check", `CronDelete(id=<id>)`. Report what was cancelled. End turn (no cycle). |

**Off-marks cadence picks:** 20m → `13,33,53 * * * *`; 30m → `7,37 * * * *`; 1h → `17 * * * *`; 15m → `2,17,32,47 * * * *`; 90s → not supported (cron is minute-grain — clamp to `1m`); arbitrary `Nm` → pick prime-ish minutes spaced N apart starting at 7. Avoid `:00` and `:30` per CronCreate jitter guidance.

---

## Step 2 — Cycle body (Steps 0-4 from `SPOT_CHECK.md`)

### 2a — Plumbing
- `check_inbox("3.0.0_SA_CVO")` + `get_agent_status("3.0.0_SA_CVO")` (act on any new message this cycle).
- Heartbeat refresh.
- If `/loop 30m` plumbing has already run in the last few minutes, skip the redundant calls.

### 2b — Agent-commit delta
- `git fetch origin CLOUD --quiet`.
- Read `org/tier1_exec/3.0.0_SA_CVO/.spot-check-checkpoint` (separate from `.cvo-loop-checkpoint`). If absent, default to `HEAD~10` and create it.
- `git log {checkpoint}..origin/CLOUD --pretty=format:"%h %an %s"`.
- **Filter:** drop CVO's own author-line commits; drop pure session-log / doc-hygiene commits unless they carry a status/registry claim.
- **Timestamp discipline (added 2026-05-23 after AE~C catch):** for any commit-age claim in a finding, use `%aI` (author ISO-UTC with explicit offset) — never the default `git show` output which displays local-tz-with-offset-suffix and is easily mis-read as UTC. See `/cvo-loop` SKILL.md §1b for the full normalization protocol.

### 2c — Per-commit work + alignment check + substance meta-check
For each surviving commit:

1. **What system did it touch?** `git show --name-only` → classify (gold/silver/bronze script, Lambda, Terraform, portal, TO file, project JSON, REGISTRY, doc, brief, infra `.tools/`, Tier-0, etc.).
2. **Does the system still work?** Cheapest applicable verify-channel check (charter §2 Step 2 lists the per-class checks). For gold scripts: `comp-pipescript deployed` + downstream artifact landed. For Lambda code: `infra/aws/terraform/{pipeline}/CHANGELOG.json` shows deploy + Lambda LastModified consistent. For TO files: `<status>` claims consistent with linked commit/log/artifact. For project JSON / REGISTRY: in-sync with TO statuses + each other.
3. **Cross-doc alignment.** TO marked complete → REGISTRY entry still in Active? Project JSON status=complete → `completed` date set + REGISTRY row moved + PRD `Status:` updated (the Closure Discipline 3-step)? New doc/PRD → inbound cross-refs updated? Deploy commit → source-map / manifest / `CHANGELOG.json` updated in the same commit? **New TO file** → does its number `.NN` match what the project JSON's phase narrative says is in that slot? (Added 2026-05-23 after /spot-check cycle 11 caught an ADVI_VALFIN TO-5 collision; cross-check `.NN` vs `org/projects/{CODE}.json` phase narrative + REGISTRY.)
4. **Substance meta-check on numeric assertions** (added per MSTR charter LD-0012, 2026-05-23 — Andrew directive "3.0.0 should be all over that with their spot check skill"). When a commit body / session log / changed artifact surfaces a number with magnitude, apply 4 quick heuristics: **(a) Magnitude vs context** — does this number make sense given book size, prior values, asset-class typical ranges? Example trigger: a -$54.8M `capital_gains_ttm` on a ~$200M book reads as -27% of book — sense-test what kind of event would have to occur and whether that event is consistent with the surrounding period. **(b) Sign expectations** — a metric named "growth"/"gain"/"balance"/"yield" coming out wrong-signed (or zero) needs to admit a reasonable explanation. **(c) Naming-vs-semantic alignment** — does the field name match what the code actually computes? Naming mismatches in data layers cascade through every downstream reader (analysts, agents in session logs, future debugging) — the LD-0012 class. **(d) D-001 v1.4 META invariant** — a mechanically-functional output that fails this test IS NOT a success; it is a finding that gets chartered to a fix. See `SPOT_CHECK.md` "META-CHECK HEURISTIC" section for the canonical reference + the LD-0012 worked example at `logs/2026-05-23/spot_check_0453Z_LD0012_capital_gains_verdict.md`.

### 2d — Decide per item: nothing / fix / route-substance / escalate
- **Nothing wrong** → no action. Quiet.
- **Misalignment, IN SCOPE for CVO fix** → make the fix under CVO author line via `.tools/safe-commit.sh`. Then MCP COO with the fix description + commit hash. Multiple fixes in one cycle = one MCP with a list.
- **Misalignment, OUT OF SCOPE** → MCP the responsible driver + CC COO with priority-marked finding (P0/P1/P2 per `prompt.md` §3). Do NOT touch the file.
- **Substance-meta finding (numbers fail the META-CHECK HEURISTIC)** → MCP the responsible driver + CC COO + MSTR with a verify-channel-style verdict (MECHANICAL / NOVEL / META layered, GREEN/YELLOW/RED shape) per the LD-0012 pattern. **Never CVO-fixed directly**, even if the fix would be metadata-only (e.g., a field rename) — substance findings always route to the code-owner via the safe-deploy chain. The substance-meta SCAN is the verifier extension; the FIX routing is unchanged.
- **Beyond-CVO judgment** → escalate to MSTR / Andrew.

Fix-scope: see `SPOT_CHECK.md` "Fix authority — explicit scope" for the canonical IN / OUT / ESCALATE lists. Summary:
- **IN:** `org/projects/{CODE}.json` status drift, `org/projects/REGISTRY.md` row drift, `org/tier*/...task_orders/*.md` `<status>` flips, doc cross-ref drift, stale pointers / checkpoint files, **TO-closure cascade** (COO TO-flip-to-complete commits → CVO propagates the narrative update to project JSON `blocking` + REGISTRY row Blocking column; ratified pattern per COO 2026-05-23 commit `55a6ef4bc` ACK; keeps COO closures atomic + verifier-not-fixer-adjacent because the cascade is alignment-metadata only). Urgent-escalation: if cascade-drift blocks another agent + next /spot-check >5min away, MCP COO for inline same-commit update.
- **OUT:** `data/*/scripts/{gold,silver,bronze}/*.py`, `infra/aws/lambda/**/*.py` code, Terraform, EC2, IAM, manifests, source-maps, `portal/src/**`, runtime state, another agent's TO `<scope>` / `<acceptance_criteria>`, PRD substance.
- **ESCALATE:** lane reassignments, mandate changes, project cancellations.

**Owned-paths block handling.** If a fix is IN SCOPE per charter but the pre-commit hook BLOCKS CVO from the lane (e.g., REGISTRY.md gated by `ANY_EXEC_OR_AE` without CVO in `permitted_agents`): do NOT `--force`. Restore the file in working tree, capture the diff inline in the MCP to COO, ask COO to (a) apply the diff and (b) add `3.0.0_SA_CVO` to the lane's `permitted_agents`. Log as a structural-enforcement finding in the cycle log. Pattern matches `feedback_tilde_lane_owned_paths_gap_route_to_coo` in workspace memory.

### 2e — Log + checkpoint advance
- **Clean cycle (no findings)** → silent log (`spot_check_{HHMMZ}_CLEAN.md` one-liner) + checkpoint advance + heartbeat refresh. **Three consecutive clean cycles → no log at all**, just checkpoint advance. A quiet loop should be quiet.
- **Cycle with findings** → full cycle log at `org/tier1_exec/3.0.0_SA_CVO/logs/{YYYY-MM-DD}/spot_check_{HHMMZ}.md`. Distinct prefix from `cvo_loop_*` so both loops' logs sort separately. Operating Doctrine §1-§9 governs the log's quality (file:line citations, per-driver framing, P0/P1/P2, mechanism-specific).
- Checkpoint: `echo {new_HEAD} > org/tier1_exec/3.0.0_SA_CVO/.spot-check-checkpoint`. Commit the checkpoint + log together via `.tools/safe-commit.sh` (your own folder; no lane issue).

### 2f — Report

Two-line summary to chat:

```
/spot-check cycle {N} -- {N_commits} commits triaged
  Findings: {none | "1 fix applied: {hash}" | "1 finding routed to {driver}" | combinations}
  Next cron tick at {next minute}; checkpoint -> {sha}
```

A clean three-streak cycle prints nothing — just runs and re-checkpoints.

---

## Coexistence with `/loop 30m`

- `/loop 30m` (charter `VALIDATION_LOOP.md`) — workspace-wide delta sweep + closure-gate / wave-gate / PRD-ship deep verdicts; **verifier-not-fixer**.
- `/spot-check 20m` (this skill) — per-commit alignment sweep; **fix-authorized within alignment-metadata scope**.

Both inherit Operating Doctrine §1-§9 quality bar. Deliberate focus split; deliberate overlap.

If both cycles fire same wall-clock minute, run `/spot-check` first (faster, fix-capable), then `/loop 30m` (deeper). The two loops share `org/tier1_exec/3.0.0_SA_CVO/logs/{YYYY-MM-DD}/` but use distinct filename prefixes (`spot_check_*` vs `cvo_loop_*`).

---

## What does NOT change

- Verifier-not-fixer remains CVO's default everywhere except this skill's bounded fix-scope.
- `prompt.md` Operating Doctrine §1-§9 governs every finding emitted from both loops.
- Ad-hoc gate-review reports filed to `inbox/` still interleave with both loops per the README Report Format Contract.
- STEERCO thread mode unchanged.

---

## Notes

- Cron is session-only by default (dies when Claude exits). To survive across restarts: `CronCreate(..., durable=true)` — only if Andrew has asked for durability.
- 7-day auto-expire: re-arm on session restart or at the 7-day boundary; the skill itself logs the cron expiry date in its first cycle.
- The `13,33,53 * * * *` default off-marks pattern is from the `CronCreate` "avoid :00 and :30" jitter-spreading guidance — every Claude session that just asked for "every 20m" gets `*/20` aligned to the same wall-clock instant; the off-marks de-collide.
- This skill is workspace-tracked (`.claude/skills/spot-check/SKILL.md` checked into git, like `/watcher` and `/loop`). Any agent on this workspace can invoke `/spot-check`, but Step 0's identity gate halts non-CVO invocations.
- Design + history: `org/tier1_exec/3.0.0_SA_CVO/SPOT_CHECK.md` (charter); `feedback_cvo_spot_check_loop_fix_authorized.md` in workspace memory; Andrew directive 2026-05-23 (verbatim: "if you catch issues, you need to address them (fix it) and then write your changes in to COO").
