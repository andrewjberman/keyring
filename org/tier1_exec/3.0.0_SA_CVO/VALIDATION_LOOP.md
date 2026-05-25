# CVO Validation Loop — 3.0.0_SA_CVO — **DEPRECATED PER LD-0064 (2026-05-25)**

> **STATUS: DEPRECATED.** This charter is retired per LD-0064 (Andrew direct 2026-05-25T~20:40Z: "yeah we need to get rid of cvo-loop first of all"). /cvo-loop is structurally redundant with /verify-channel + /spot-check under LD-0062 + Andrew /verify-channel trigger refinement. Specifically, 30m scheduled comprehensive deep-verdict cycles directly contradict Andrew's discipline that /verify-channel "should be exhaustive ... only at project/channel/pipeline/definitive closeout."
>
> **Post-retirement CVO canonical skill family (LD-0064):**
> - `/spot-check` (20m cron) — fast alignment + drift + substance-meta-check; fix-authorized for alignment-metadata
> - `/verify-channel` (event-based primary + 2h lightweight scan + comprehensive-only-at-closeout per ratified ANDREW-LOCKS 2026-05-25T20:31Z) — verifier-not-fixer
>
> **File preserved for historical context.** Do not invoke `/cvo-loop`. Do not run the cycle body below — it operates on assumptions superseded by LD-0062 + trigger refinement. Rollback per LD-0064 §4 reversible within 4 weeks if empirical use shows /verify-channel + /spot-check insufficient.

---

`3.0.0_SA_CVO` is an MCP-registered Claude agent (Tier-1 exec) running a **continuous validation loop**. This file is the loop charter — the body the agent executes every cycle. It is the CVO's *standing* task; ad-hoc gate-review reports filed by CTO/COO to `inbox/` interleave with the loop. The report-review doctrine (`prompt.md` §1-§9 + README Report Format Contract) governs the **quality of every finding** the loop emits, applied per cycle.

---

## Mode

- Run via `/loop 30m` — re-armed every cycle with `ScheduleWakeup(delaySeconds=1800)`.
- **Never auto-exits.** Runs until Andrew stops it.
- **Workspace-wide** — every pod, every pipeline, every project. Not scoped to one project.
- **Current priority focus:** `YALP_MDSRC` — the yang-pipeline lineage mappings
  authored by `0.7.0_AE` (L1) and the project's general proceedings, including
  the D2/D3 per-surface YCharts-vs-Bloomberg confirmation work. Weight YALP
  commits first in each cycle until YALP closes.

## Standing role (unchanged from the CVO charter)

You VERIFY — you do not fix, do not author TOs/PRDs, do not implement.
**Verifier != fixer.** All findings are advisory; the drivers decide whether to
act. `prompt.md` Operating Doctrine §1-§9 (ground every claim with `file:line`,
respond per-driver, P0/P1/P2 priority-rank, mechanism-specific not generic,
mandatory unknown-unknowns) governs every finding you emit — it now applies
per-cycle instead of per-report.

---

## The cycle — every 30 minutes

### Step 0 — Plumbing
Standard `/loop` plumbing per `org/XXX.md`: check inbox (both paths), heartbeat,
watcher health. Act on any inbox message this cycle — a driver may ask for a
targeted validation; fold it into the cycle.

### Step 1 — Delta detection
- `git fetch origin CLOUD` (and the `portal` submodule).
- Read your checkpoint: `org/tier1_exec/3.0.0_SA_CVO/.cvo-loop-checkpoint` — the
  last-reviewed commit SHA. If absent, default to `HEAD~20` and create it.
- `git log {checkpoint}..origin/CLOUD --pretty=...` — enumerate every new commit
  since last cycle. Same for the portal submodule.

### Step 2 — Triage
Classify each new commit / artifact. **VALIDATION-WORTHY:**
- TO closures / RAVC accepts (a worker or exec marked work complete)
- gold/silver/bronze script changes + any pipeline run they imply
- S3 artifact writes, deployed Lambdas, `terraform apply`s, new pipeline tags
- project closes, PRD ships, wave gates — **KEY JUNCTURES**, deeper pass
- portal DEV/PROD changes carrying a data or behavior claim

**SKIP:** pure session-log / doc-hygiene commits with no deliverable;
watcher/registration churn.

### Step 3 — Validate (verify-channel discipline)
For each worthy item, apply the `/verify-channel` method:
- **Data-pipeline items:** the 4-check — EXISTS / FRESH / SCALED / NOT-FROZEN —
  against **actual S3 / DynamoDB / artifact state**. NEVER the producer's
  self-report, the `rc=0` log, the cron/SSM config, or a TO marked complete.
- **Infra / mapping / portal items:** spot-check the claim against the real
  artifact — the deployed Lambda, the actual S3 key, the rendered component, the
  lineage-map citation.
- **Sharpest-test-binds:** pick the check most likely to fail; if it passes, the
  item is sound.

### Step 4 — Two-lens assessment
Every validated item gets BOTH lenses:
- **(a) Standalone** — does this commit/artifact do what it claims, on its own terms?
- **(b) System-context** — does it break or contradict anything downstream? Fit
  the greater architecture? Introduce drift (a doc / registry / contract now
  stale)? Collide with another in-flight project's blast radius?

### Step 5 — Emit findings
- Write a cycle log: `org/tier1_exec/3.0.0_SA_CVO/logs/{YYYY-MM-DD}/cvo_loop_{HHMMZ}.md`
  — commits reviewed, verdict per item, findings.
- Findings typed **P0 / P1 / P2** (`prompt.md` §3), **per-driver** (§2),
  **mechanism-specific** (§4).
- **P0 / P1 → MCP the responsible driver AND `2.0.0_SA_COO` this cycle.** P2 → logged only.
- A clean cycle (nothing worthy, or all-pass) → a one-line log entry, no MCP
  noise. A quiet cycle is quiet.
- **Key junctures** (project close, PRD ship, wave gate) → the deeper pass + an
  explicit go/no-go-shaped finding to COO (and CTO when architecture is in play).

### Step 6 — Checkpoint + re-arm
- Write the latest reviewed SHA to `.cvo-loop-checkpoint`.
- `ScheduleWakeup(delaySeconds=1800)`; pass the same `/loop 30m` prompt back. Never auto-exit.

---

## Escalation

- A **data-integrity finding** — a pipeline that reports success but delivers
  stale / empty / wrong data — is **P0**. MCP COO + the producing driver the
  same cycle; do not wait for the next.
- If you **cannot reach actual state** (S3 perms, dead runner, missing artifact)
  — that is itself a finding. Report "could not verify, here is why." NEVER
  assume pass on an unreachable check.

## What does NOT change

You are still the external eye the project cannot have on itself. You do not
fix, implement, author PRDs/TOs, or invent file paths. You still accept ad-hoc
gate-review reports filed to `inbox/` per the README Report Format Contract —
those interleave with the loop. The loop is your **standing** task.
