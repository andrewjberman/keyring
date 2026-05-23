# CVO Spot-Check Loop — 3.0.0_SA_CVO

`3.0.0_SA_CVO` runs a second, tighter-cadence loop alongside `VALIDATION_LOOP.md`: the **spot-check**. Every 20 minutes, sweep recent commits from `ajb_workspace` agents, verify the systems those commits touch still work, check cross-system alignment, and — uniquely for this mode — **fix alignment issues directly** (within scope) before MCPing the change to COO.

This is the agent-commit-grain analogue to the artifact-and-key-juncture focus of `VALIDATION_LOOP.md`. Both loops coexist:

| Loop | Cadence | Focus | Authority |
|---|---|---|---|
| `VALIDATION_LOOP.md` (`/loop 30m`) | 30m | workspace-wide delta sweep; closure-gate / wave-gate / PRD-ship deep passes; per-driver findings | verifier-not-fixer — findings only, drivers act |
| `SPOT_CHECK.md` (`/spot-check 20m`) | 20m | recent agent commits; do-the-systems-still-work + cross-doc alignment | **fix-authorized within scope** — CVO repairs alignment, then tells COO |

`prompt.md` Operating Doctrine §1-§9 (file:line citations, per-driver framing, P0/P1/P2, mechanism-specific, mandatory unknown-unknowns) governs both loops. Spot-check inherits the same quality bar.

---

## Fix authority — explicit scope

Andrew directive 2026-05-23 (verbatim): *"if you catch issues, you need to address them (fix it) and then write your changes in to COO."*

This carves a bounded exception to the verifier-not-fixer mandate, specifically for spot-check. Scope:

### IN SCOPE — CVO fixes directly, then MCPs COO

Alignment artifacts where the fix is *metadata reconciliation*, not code or production state:

- `org/projects/{CODE}.json` — `status` field drift (e.g., a project marked `pending` whose authored TOs are all `complete`), stale `phase` narrative, missing `completed` date on a clearly-closed project, `blocking` field out of date with reality.
- `org/projects/REGISTRY.md` — row in the wrong section (Active row for a closed project, Completed row for an in-flight one); missing closure date column; out-of-order rows.
- `org/tier*/...task_orders/*.md` — `<status>` flips that obviously should have happened (e.g., a TO whose RAVC2 has been COO-accepted but the file still says `pending`).
- Doc cross-ref drift — `docs/architecture/**`, `docs/reference/**`, briefs — broken `:line` citations from a renamed/refactored file, dead links to moved files, PRD `Status:` lines stale.
- Stale "current"/pointer files — `.cvo-loop-checkpoint`, equivalent CTO/COO checkpoint files (only if they own the convention and the drift is obvious), README-pointer-to-latest-version drift.
- Author-line / commit-identity registry drift in `org/standards/` or equivalent if obviously wrong.

The unifying property: **the fix is in-folder metadata**, the kind of repair that a careful documentarian would make after an external observation — no deploy chain, no agent code, no production state.

### OUT OF SCOPE — CVO does NOT touch; MCPs the responsible driver + COO instead

Anything that requires the safe-deploy chain, has a code-owner lane, or carries production blast radius:

- `data/*/scripts/{gold,silver,bronze}/*.py` — DS lane; deploy chain.
- `infra/aws/lambda/**/*.py` (excluding doc/comment-only changes) — AE lane; deploy chain.
- `infra/aws/terraform/**`, `infra/aws/ec2/**`, IAM, manifests, source-maps — AE/DT lanes.
- `portal/src/**` — DE/RD lanes; build chain.
- Any S3 artifact, DynamoDB row, Lambda LastModified, EC2 state — runtime state, not repo state.
- Another agent's `task_orders/` `<scope>`/`<acceptance_criteria>` — TO scope is COO's authoring lane.
- Any PRD substance (architecture decisions, scope changes) — CTO's authoring lane; CVO can only fix `Status:` line drift.

For OUT-OF-SCOPE issues, follow the normal CVO findings pattern: MCP the responsible driver + CC COO with a P0/P1/P2 priority-marked, mechanism-specific finding.

### ESCALATE — Andrew

- Lane reassignments, mandate changes, Tier-0 decisions, project cancellations — these are not CVO's call. Flag to Andrew via MCP `0.0.0_AB_MSTR` (or directly if MSTR is down per his per-instance authorization).

---

## The cycle — every 20 minutes

### Step 0 — Plumbing

Standard `/loop` plumbing: inbox pull (`check_inbox` + `get_agent_status`), heartbeat, watcher health. If `/loop 30m` plumbing has already run within the last few minutes, skip the redundant calls — but at minimum ensure heartbeat is fresh.

### Step 1 — Agent-commit delta

- `git fetch origin CLOUD --quiet`
- Read `org/tier1_exec/3.0.0_SA_CVO/.spot-check-checkpoint` (the last-reviewed SHA for spot-check, separate from `.cvo-loop-checkpoint`). If absent, default to `HEAD~10` and create it.
- `git log {checkpoint}..origin/CLOUD --pretty=format:"%h %an %s"` — enumerate every new commit since last spot-check.
- Filter: drop CVO's own author-line commits (`3.0.0_SA_CVO`); drop pure session-log / doc-hygiene commits unless they carry a status/registry claim.

### Step 2 — Per-commit work + alignment check

For each surviving commit:

1. **What system did it touch?** From `git show --name-only`, classify: gold script / Lambda / Terraform / portal / TO file / project JSON / REGISTRY / doc / brief / etc.
2. **Does the system still work?** Apply the cheapest applicable verify-channel check:
   - Gold/silver/bronze script: was it deployed (`comp-pipescript deployed`)? Did a downstream artifact land?
   - Lambda code: did Terraform apply (check `infra/aws/terraform/{pipeline}/CHANGELOG.json` for a record)? Is the Lambda LastModified consistent?
   - Terraform: `terraform plan` clean (or, cheaply, check the `CHANGELOG.json`).
   - Portal: did the bundle/build go through?
   - TO file: are the `<status>` claims consistent with the linked commit/log/artifact?
   - Project JSON / REGISTRY: are they in sync with each other and with the TO statuses?
3. **Alignment cross-check.** Does the commit create drift somewhere?
   - A TO marked complete — is the REGISTRY entry still in Active?
   - A project marked complete in JSON — is the `completed` date set + REGISTRY row moved + PRD `Status:` updated (the Closure Discipline 3-step)?
   - A new doc/PRD — are inbound cross-refs updated?
   - A deploy commit — did the source-map / manifest / `CHANGELOG.json` get updated in the same commit (Rule 4)?

### Step 3 — Decide: nothing / fix / escalate

- **Nothing wrong → quiet log line, advance checkpoint, done.** Three or more consecutive quiet cycles → no log at all (just checkpoint advance + heartbeat refresh).
- **Misalignment, IN SCOPE for CVO → fix it directly** under CVO author line via `.tools/safe-commit.sh`. Then MCP COO with: what was misaligned, what was fixed, commit hash. One MCP per fix; multiple fixes in a cycle = one MCP with a list.
- **Misalignment, OUT OF SCOPE → MCP the responsible driver + CC COO** with a priority-marked finding per the normal CVO discipline. Do not touch the file.
- **Beyond-CVO judgment call (lane reassignment, scope decision, cancellation) → escalate to MSTR / Andrew.**

### Step 4 — Log + re-arm

- Cycle log only when something happened (a fix landed, a finding routed, an escalation went). A clean cycle is silent — checkpoint advance + heartbeat refresh is all.
- Cycle logs at `org/tier1_exec/3.0.0_SA_CVO/logs/{YYYY-MM-DD}/spot_check_{HHMMZ}.md` (distinct prefix from `cvo_loop_*` so the two loops' logs sort separately).
- Spot-check is driven by a `CronCreate` at startup (`*/20` off-marks, e.g. `13,33,53 * * * *`). No per-cycle re-arm needed — the cron fires until canceled. Runs auto-expire after 7 days per CronCreate's default; refresh by re-arming the cron at session restart or on the 7-day boundary.

---

## What does NOT change

- **Operating Doctrine §1-§9 still governs every finding.** A spot-check MCP to COO carries the same rigor as a `VALIDATION_LOOP` cycle log: file:line citations, mechanism-specific, P0/P1/P2 priority, per-driver framing where applicable.
- **Verifier-not-fixer is still CVO's default.** Spot-check carves a bounded fix exception for alignment metadata; everywhere else (including `VALIDATION_LOOP` cycles), CVO emits findings and drivers act.
- **Ad-hoc gate-review reports filed to `inbox/`** still interleave with both loops per the README Report Format Contract.
- **STEERCO thread mode** unchanged.

---

## Coexistence with `/loop 30m` (VALIDATION_LOOP)

The two loops have deliberate overlap (both look at commits) but different focus:

- `/loop 30m` weights **closure gates, wave gates, PRD ships, key junctures** — produces deep verdicts and per-driver findings; does not fix.
- `/spot-check 20m` weights **per-commit alignment** — produces silent advances when clean, fixes-and-tells-COO when drift is in-scope, findings-to-driver when out-of-scope.

A finding that appears in both lenses is still emitted only once (whichever loop catches it first); the other loop's checkpoint advances past it on the next tick. To avoid duplicate work, both loops cite each other's most-recent log in the cycle commit when relevant.

If both cycles fire in the same wall-clock minute, run `/spot-check` first (faster, fix-capable), then `/loop 30m` (deeper).
