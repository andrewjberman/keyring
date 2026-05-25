---
name: verify-channel
description: Two-mode independent verification. **Surface-level mode** confirms a pipeline / gold-script / S3 artifact / repair actually DELIVERS fresh, usable data by reading actual S3/DynamoDB/artifact state (the 4-check method EXISTS/FRESH/SCALED/NOT-FROZEN + sharp structural test + decision-useful meta-gate). **Project-level mode** runs comprehensive project-scope verification (commits + PRDs + intent + end-to-end trace) triggered event-based on closeout-class signals (project status flip / close-out RAVC2 / Andrew direct / /spot-check escalation) + a 2h lightweight threshold-scan baseline that detects phase-transitions / wave-gates / PRD ratifications / multi-project blast-radius and queues the comprehensive pass. Trigger: any audit -> repair -> re-verify cycle, a proactive sweep of "done"/GREEN items, a RAVC4 / project close-out adequacy check, or a closeout-class composite trigger fire. Core bar: "the pipeline pulls data AND the data is fresh and usable — not merely that crons/chains fire."
---

# /verify-channel — Two-mode independent verification

This skill has TWO modes, distinct in scope, cadence, and invocation pattern:

| Mode | Scope | Trigger | Output |
|---|---|---|---|
| **Surface-level** (existing substance) | One pipeline / artifact / repair | Per audit / repair / proactive sweep item | PASS / CONCERN / CONDITIONAL on the 4-check + sharp + meaning gates |
| **Project-level** (LD-0062 + Andrew addendum 2026-05-25) | One project (all pipelines + PRDs + ACs) | Closeout-class composite trigger (immediate-fire) OR 2h lightweight scan detecting closeout-threshold (scan-detected) | CLEAN / CONCERN / MISALIGNED per-AC grid + verdict-routing |

The two modes share the four non-negotiable core principles. **Project-level mode invokes Surface-level mode as a sub-routine** when tracing pipeline artifacts at Step 3(d) of its 4-component body.

---

## Core principles (BOTH modes)

The bar is **"the pipeline pulls data AND the data is fresh and usable — not merely that the cron / SSM chain / Lambda fired."** The recurring failure mode this skill exists to catch is **config-OK != delivering**: a cron ENABLED, an SSM chain `exit=0`, a partition existing, a `status: ok` log, a TO marked `complete` — none of them prove fresh, usable data landed. (Anchors in ajb doctrine: `[[feedback-ship-attestation-vs-deploy-attestation-distinct]]` — a commit/RAVC-request is not proof the runtime changed; `[[feedback-s3-pull-dispatcher-no-auto-propagate]]` — a push to CLOUD does not mean the runner runs that code; the 2026-05-20 INFGRO rebuild — a "verbatim trigger" that fired `exit=0` but ran append-only and re-materialized nothing.)

Four non-negotiable rules:

1. **Verifier != fixer.** The agent who made (or will make) the repair never verifies it. If asked to verify your own work, refuse and route to a third agent. This binds Project-level mode too — CVO's own commits in a project window are flagged transparently per `[[feedback-cvo-self-validation-mitigation-pattern]]`.
2. **Read the artifact, never the self-report.** Inspect actual S3 / parquet / DynamoDB / platinum-JSON state with your own read. A producer's "ran fine, N rows" is not evidence.
3. **Sharpest-test-binds.** When a coarse check PASSes and a sharp check CONCERNs, the CONCERN binds. A coarse-PASS that misses a sharp defect launders a bad repair into a clean verdict.
4. **Decision-useful != mechanically-delivered.** Fresh + scaled + non-frozen + structurally-non-degenerate is necessary, NOT sufficient. The final and highest gate (Step 3.5) is whether the output is actually *decision-useful and meaningful for its consumer*. Verification never concludes on a mechanical/structural pass alone.

---

# Mode A — Surface-level verify (per-artifact / per-repair / per-sweep-item)

Independently verifies that a data pipeline (a gold/silver/bronze script, a Lambda, a portal/platinum artifact, a DynamoDB-backed surface) — or a repair to one — **delivers fresh, usable data**, by inspecting the actual artifact, not any claim about it. This is the codification of the independent-verification layer behind RAVC4 acceptance and `comp-validate`.

## When to invoke (Mode A)

- **Re-verify a repair**: an agent RAVC2'd a fix; confirm it holds before it counts toward close-out.
- **Field-audit a pipeline**: confirm a "fixed"/passing surface is genuinely delivering.
- **Proactive sweep of the done set**: adversarially re-check items marked complete — a completed TO is a claim, not evidence (Step 0).
- **Close-out adequacy input**: feeding a project-closure verdict — each surface enters as UNVERIFIED until this skill confirms it.
- **Mode B sub-routine**: invoked by Project-level mode at Step 3(d) when tracing pipeline artifacts end-to-end.

## Step 0 — "Complete" / GREEN is a claim, not evidence

A TO marked `complete` is NOT proof. A completed fix can break a *different* artifact two ways — (a) regress it, or (b) be entirely CORRECT yet amplify a pre-existing latent defect to critical scale. A scale-jump on a completed fix is itself a trigger to re-check cardinality even when the fix is right. Every completed/GREEN surface enters verification as UNVERIFIED. The proactive adversarial sweep of the done set is loop-essential, not optional. See `[[feedback-identity1-masks-absolute-value-class]]` — a gate can PASS to-the-cent while the per-component values are wrong.

## Step 1 — Identify the pipeline's actual delivery contract

For the target surface, establish from code/config (not assumption):
- The S3 key / DynamoDB table / platinum-JSON path the **consumer** reads (often the `latest/` promoted path, not the dated partition the producer writes — verify the one consumers actually resolve). `comp-platinum reverse <key>` and `comp-pipescript consumers <script>` resolve this.
- The cadence + expected landing time, in **UTC** (crons + SSM are UTC).
- The expected scale (rows / bytes) from recent good runs.
- For a repair re-verify: the commit, what it claims to change, and whether its output was actually **run to the consumer path**. A committed fix not executed to S3 is NOT deployed; a script pushed to CLOUD but not `aws s3 cp`'d to the runner's code path is NOT what runs (`[[feedback-s3-pull-dispatcher-no-auto-propagate]]`). `comp-pipescript deployed <script>` gives MATCH/STALE/MISSING.

## Step 2 — The 4-check method (run all four; existence alone is never sufficient)

| Check | Question | Method | Failure |
|---|---|---|---|
| **EXISTS** | Is the latest expected partition/object present at the consumer path? | `aws s3api head-object` (UTC LastModified) / DynamoDB query | absent |
| **FRESH** | Is its write recent on cadence, AND does any freshness stamp reflect real data recency (not write-time, not an unconditional `CURRENT_DATE`)? | head-object UTC + inspect the freshness column vs the underlying data vintage | stale / dishonest stamp |
| **SCALED** | Is row/byte count in-family with recent runs (max-of-N prior; reject < ~50%)? | independent `COUNT(*)` / ContentLength vs baseline | partial run |
| **NOT-FROZEN** | Is content genuinely different from the prior partition? | **ETag / content-hash**, NOT size (byte-identical size with a distinct ETag = real new content; size-only false-positives) | stale-duplicate |

For overwrite-in-place single artifacts (no dated history): SCALED's "max-of-N prior runs" is N/A — use PARITY vs the grain it should match instead. Don't manufacture a check that doesn't apply; say so. ajb note: `comp-validate <script> --artifact <file>` runs a config-driven battery of these for gold scripts — use it where a validate config exists; it does not replace your own artifact read.

## Step 2.5 — The sharp structural test (mandatory for join / aggregate / cohort data)

Coarse guards (existence, headline counts, cross-group spread) are necessary but NOT sufficient. Ask: **"what is the strongest degeneracy this data could still have that my coarse test would NOT catch?"** and test THAT.

- **Aggregate-identity masking**: an `aggregate == sum(parts)` reconciliation can PASS to-the-cent while per-component values are wrong — a residual component silently absorbs whatever leaks from the others. PASS = "internally consistent," NOT "values correct." Detect via a per-component series-walk + day-over-day plausibility, not the identity gate. (`[[feedback-identity1-masks-absolute-value-class]]`.)
- **Join degeneracy**: a join can return exact headline counts while being a near-cartesian — test the within-group completeness ratio, not just the total.
- **Freshness-stamp honesty**: for every row stamped "fresh today", is its payload provably NOT byte-identical to the last frozen snapshot? Zero today-but-frozen rows is the bar; "the distribution looks mixed" is not.
- **Consumer-output-vs-bucket-write-state alignment** (added 2026-05-25 per ws COO ADVI_DEMOV1 Phase 5 AC5 empirical anchor `b097b9826`): for consumer-facing output (leaderboard.json / platinum field / portal artifact): verify that the consumer-output cardinality + content matches the bucket-write-state LastModified partition for the CURRENT run, disjoint from prior-run residuals. Detection: per-row LastModified read from S3 head-object vs the run's expected window. Identity-masking check: a stale residual can pass headline-count + non-frozen ETag while being current-run-disjoint at the row level. This is the output-vs-purpose alignment axis applied at AC-verification stage.
- **Dead-column class**: when a column is reported uniform-constant / all-0 / all-NULL while its rows EXIST and are fresh, do NOT scope the check to the reported column — scope it to the CLASS via the structural boundary that separates dead from live (usually a semantic subfamily — e.g. current-window metrics dead while cumulative metrics on the same rows are live, the signature of a point-in-time join landing on an empty period). Enumerate every column on the dead side across all artifacts sharing the lineage; per-column assert distinct >> 1. A representative-column check FALSELY PASSES the class.
  - **Broken-compute vs absent-data discriminator**: before concluding "data is missing", check whether a SIBLING family on the SAME rows is richly populated. If the sibling is rich, the data is present — the defect is a broken computation, not absent input.
  - **Cascade**: a dead base metric propagates into everything derived from it (percentiles, scores, rollups) — they go uniform-constant even though their own producer "ran fine". Add every derived artifact in the lineage to the checklist; for derived scores, "non-degenerate" means *genuinely discriminating*, not merely distinct > 1.

## Step 3 — Timing & timezone discipline

Two false-positive classes:
- `aws s3 ls` renders LastModified in **host-LOCAL** tz; crons are UTC. Use `aws s3api head-object` (UTC ISO8601) or normalize.
- Checking **before** the expected landing time is a true-but-transient absence = a false RED. Sample only **after** expected_landing + a cadence-variance margin. "Absent now" is a stall only if `now > expected_landing + margin`.

## Step 3.5 — Meta-analysis: decision-useful & meaningful (the FINAL gate — runs last, binds the verdict)

Everything above confirms the pipeline **mechanically delivers** fresh, scaled, non-frozen, structurally-non-degenerate data. That is necessary and NOT sufficient. The final question — implied by none of the above — is: **is the output actually decision-useful and meaningful for the thing that consumes it (the portal surface, the leaderboard, the partner-facing report), or is it mechanically churning?** Run this LAST, every verify; it binds the verdict.

Three sub-checks, in order:
1. **Gate-coverage honesty.** Does the structural gate (Step 2.5) even *structurally cover this artifact's class*? Score-/model-/embedding-derived and continuous-weight classes are routinely outside exact-match / cardinality-ratio gates by construction. If so, a clean Step-2.5 PASS is **zero evidence** of meaningfulness — state that scope-honestly.
2. **Quality-erosion under completion-pressure.** Did a multi-iteration "make it pass / faster / fit the window" arc quietly slash quality knobs (a lookback window, a sample size, a K, a tolerance band) "for speed"? Completion-pressure trades meaning for throughput while every status stays GREEN. If yes, the completion bar itself may be the defect.
3. **Consumed-output meaning probe.** (i) Run-to-run stability of the *consumed* output (the decision artifact's set/assignment stability — top-K membership, cohort labels, the rendered number's day-over-day plausibility — NOT raw scores that are scale non-identifiable). (ii) Structural sanity vs a baseline — does the output discriminate, or is it ~constant noise on a meaningful-sounding name?

Discipline for this step:
- **Honest-limit.** A structural assessment is not an empirical measurement. Assert only what is rigorously assertable; name the empirical probe as the next step — do not claim you ran it. If a probe has a real obstacle (overwrite-in-place precludes run-to-run comparison; a 2nd run would make you the producer-not-verifier), surface it as an honest-limit DEFERRED — never fake it, never silently drop it.
- **Verifier != fixer (still binds).** This step validates meaning; it never restores eroded quality params. Probe-FAIL => STOP + surface.

## Step 4 — Verdict + routing (STOP, do not repair) — Mode A verdict shape

A verifier never fixes — finding the defect IS the deliverable; route it.

- **PASS** — all 4 checks + the sharp structural test clean AND Step 3.5 cleared (meaning probe passed OR the meaning axis explicitly scoped-out with a stated honest-limit + routed as a distinct open axis). State the checks + actual numbers, not "looks fine." A mechanical PASS with an unaddressed Step-3.5 gap is NOT a PASS — it is PASS-mechanical + CONCERN-meaning, two axes, never collapsed.
- **CONCERN** — any check fails, OR the fix is committed-but-not-deployed, OR the artifact is confounded by degraded upstream, OR Step 3.5 surfaces a meaning gap. Do NOT pass. Specify exactly what, with the sharp evidence; tag the axis (mechanical/structural vs meaning).
- **CONDITIONAL** — the repair cannot be verified until a prerequisite lands. State the explicit sequence: prerequisite -> deploy-to-S3 -> re-verify.

Routing: PASS/CONCERN/CONDITIONAL -> the requesting exec (COO for TO-scope / close-out; CTO for an architectural call). If still-broken, STOP — do NOT fix it (that is the owner's lane, and verifier != fixer); RAVC2 the specific finding and let the exec route the repair. When two independent verifies disagree, the sharper-test verdict binds — never average, never treat a coarse PASS as exoneration.

## Step 5 — Feed the close-out (Mode A)

For a project-closure / RAVC4 adequacy verdict: each surface carries **two axes** — `mechanically-delivers {VERIFIED-fresh-and-usable | CONCERN | CONDITIONAL}` AND `decision-useful {VERIFIED-meaningful | CONCERN-meaning | UNTESTED-meaning(honest-limit, routed)}`. A surface is not closeable on the mechanical axis alone. Reopen/annotate any completed TO a sweep regresses; the item stays OPEN until independently re-confirmed on **both** axes. A close-out that rests on the completed-TO list, or on the mechanical axis while the meaning axis is silently assumed, is invalid.

---

# Mode B — Project-level loop-driven verify (per-project comprehensive)

Project-scope comprehensive verification driven by event-based composite closeout-threshold triggers + a 2h lightweight scan baseline. Per LD-0062 ratified architecture + Andrew /verify-channel trigger refinement 2026-05-25 ratified via MSTR ANDREW-LOCKS.

## Trigger model — event-based primary

Comprehensive Mode B fires **ONLY** when a closeout-threshold signal fires. The 2h scan is a lightweight backstop that detects closeout-class signals between explicit-fire events — it does NOT itself run comprehensive verify; it queues projects for comprehensive verify when scan-detected signals fire.

| Component | Mechanic |
|---|---|
| **Primary trigger** | Event-based — composite closeout-threshold any-of-N (see below) |
| **2h backstop scan** | Lightweight threshold-scan across all active projects; queues comprehensive pass on hit |
| **Comprehensive fire** | ONLY at closeout-class signal (Class 1 immediate-fire OR Class 2 scan-detected hit) |
| **Routine drift between closeouts** | /spot-check 20m owns this (unchanged); /verify-channel does NOT run continuous baseline |

### Composite closeout-threshold (2-class shape per joint CVO council 2026-05-25)

**Class 1 — Immediate-fire (within 1 cycle of detection):**

| # | Signal | Detection mechanic |
|---|---|---|
| 1 | Explicit close-out status flip | `org/projects/{CODE}.json` status → `close-out` / `complete` / `terminal` |
| 2 | Close-out RAVC2 dispatched | MCP subject-prefix `[RAVC2-CLOSE]` OR final-phase RAVC2-Accept landed per PRD-phase state |
| 3 | Andrew direct trigger | MCP subject-prefix `[VERIFY-CHANNEL-NOW]` or explicit Andrew request |
| 4 | /spot-check explicit escalation | MCP subject-prefix `[SPOT-ESCALATE-CLOSEOUT]` (TIGHTENED from Round-1 5-condition handoff to single explicit-tag mechanism per joint CVO council) |

**Class 2 — Scan-detected (at next 2h scan moment):**

| # | Signal | Detection mechanic |
|---|---|---|
| 5 | Phase-transition | Project advanced to new phase since last 2h scan (per PRD-phase state machine) |
| 6 | Wave-gate crossed | New wave-gate landed since last 2h scan |
| 7 | PRD ratification | New ratified PRD or PRD-revision committed since last 2h scan |
| 8 | Multi-project blast-radius | A fix-class change touched paths in >1 project's owned-paths.yaml union since last 2h scan |

**Composite rule:** any-of-(1..8) fires comprehensive /verify-channel for the matched project(s). Class 1 immediate-fire signals fire within 1 cycle of detection; Class 2 scan-detected signals fire at the next 2h scan moment.

**Why composite, not single-signal:** single-signal threshold is brittle — relies on discipline of one signal type. Composite any-of-N is robust under partial discipline; multiple discovery paths catch the same closeout even if one signal class misses.

**Note:** canonical composite-threshold MSTR synthesis pending at scribe-time (ws 2-class + CL 3-tier merging per Andrew direction). This SKILL.md ships with ws 2-class shape as scaffold; will absorb canonical-merge refinements when MSTR ships them.

## Invocation forms

| Form | Behavior |
|---|---|
| `/verify-channel {project_slug}` | One-shot per-project comprehensive verify (manual invoke; treats as Class 1 immediate-fire) |
| `/verify-channel scan` | Run 2h lightweight threshold-scan across active projects; queue comprehensive verify for any Class 2 hit |
| `/verify-channel queue` | Process queued projects in priority order (RAVC2-triggered → scheduled-baseline-overdue → /spot-check-escalated) |
| `/verify-channel queue 2h` | Process queue + re-arm 2h scan via ScheduleWakeup (loop mode) |
| `/verify-channel ravc2 {ravc2_id}` | RAVC2-triggered shortcut; treats as Class 1 immediate-fire |
| `/verify-channel once` | Run one /verify-channel scan + queue process, no re-arm |

## Step 0 — HALT-gate

Run `.tools/halt-gate-check.sh` per Rule 18 canonical pattern. Empty inbox passes silently; routine pending surfaces; STOP-class hard-blocks. Bypass via `HALT_OVERRIDE="<reason>"` (audited to `org/halt-gate-override-audit.log`).

## Step 1 — Register + heartbeat

`register_agent("3.0.0_SA_CVO", summary="<current cycle>")` + `heartbeat("3.0.0_SA_CVO")`. Mode B is CVO-scoped; non-CVO invocations halt with identity-gate message.

## Step 2 — Resolve mode + project

- `/verify-channel scan` → resolve to scan body (Step 3a)
- `/verify-channel queue` → process next queued project (Step 4)
- `/verify-channel {project_slug}` / `/verify-channel ravc2 {ravc2_id}` → resolve directly to comprehensive body (Step 4)

PRD-Inventory query identifies active projects; project_paths from PRD-Inventory; last-verify-channel timestamp from PRD-Inventory (for scan diff computation).

## Step 3a — 2h lightweight scan body (distinct from comprehensive)

For each active project:

1. **Phase-transition detection:** read PRD-phase state vs last-scan snapshot; flag advance.
2. **Wave-gate detection:** `git log {last_scan_hash}..origin/CLOUD --grep="wave-gate"` for the project's path.
3. **PRD ratification detection:** `git log {last_scan_hash}..origin/CLOUD --grep="PRD"` for the project's path; filter to ratified-PRD commit subjects (per /charter ROUTINE/NOVEL tagging per LD-0062 Round-2 Q6).
4. **Multi-project blast-radius detection:** `git log {last_scan_hash}..origin/CLOUD --name-only` against owned-paths.yaml union — flag if a commit touched paths in >1 project's owned-paths set.

For any project with a Class 2 hit: enqueue for comprehensive verify (Step 4). Emit scan log (lightweight; one line per project + per-Class-2-signal hit).

Scan does NOT itself run the 4-component comprehensive body; it ONLY queues hits.

## Step 4 — Comprehensive verify body (heavy — fires only on Class 1 immediate-fire OR Class 2 hit)

**4-component body per LD-0062 ratified design:**

### (a) Read commits

`git log {last_verify_channel_hash}..origin/CLOUD --pretty=format:"%h %an %s" -- {project_paths}` — enumerate every new commit in the project window since last comprehensive verify. Filter: drop pure session-log / doc-hygiene unless they carry a status/registry/closure claim. Per `[[feedback-commit-age-use-iso-utc-not-local]]`, use `%aI` for any age claim.

### (b) Read PRDs (current + diff vs prior verify snapshot)

PRD-Inventory query → load current PRD + diff vs prior comprehensive-verify cycle's snapshot (banked in prior cycle log). Catches scope-drift commits. NOVEL/ROUTINE tag from /charter author per LD-0062 Round-2 Q6.

### (c) Assess intent + status (mandate-distance, AC-by-AC)

PRD §1 mandate text vs current artifact set. Per-AC pass/concern grid:
- For each AC in current PRD: identify the deliverable artifact(s) + assess delivery vs claim.
- Flag mandate-distance drift: AC-as-shipped vs AC-as-written delta.

### (d) Trace results end-to-end (Mode A invoked as sub-routine per pipeline artifact)

For each pipeline / Lambda / portal artifact in the project:
- Invoke Mode A 4-check + sharp structural test + Step 3.5 meaning probe (see Mode A above).
- Aggregate Mode A verdicts into per-AC grid.

Per Step 2.5 added 2026-05-25: include "Consumer-output-vs-bucket-write-state alignment" check (LastModified-partition pattern) for any consumer-facing decision artifact (leaderboard.json / platinum field / portal artifact).

## Step 5 — Emit verify_channel artifact

`org/tier1_exec/3.0.0_SA_CVO/verify-channel/verify_channel_{project_slug}_{NNN}.md` with:
- **Verdict:** CLEAN / CONCERN / MISALIGNED
- Per-AC pass/concern grid
- Per-driver findings
- Mandate-distance score (qualitative)
- Recommended next verify-channel cadence for this project (informational — actual next-fire is event-driven per trigger model)
- Surface-level Mode A sub-verdicts per pipeline artifact (PASS/CONCERN/CONDITIONAL)

## Step 6 — Verdict routing

- **MISALIGNED** → P0/P1 MCP to MSTR + responsible driver (drives close-out blocking)
- **CONCERN** → P2 MCP to responsible driver (logged, not blocking)
- **CLEAN** → quiet log on disk; no MCP

For NOVEL PRD pre-propagate gate (per LD-0062 Round-2 Q6): MISALIGNED verdict blocks /drive execution start; CONCERN-with-mitigation permits with conditions; CLEAN permits unblocked.

## Step 7 — Commit + push

`.tools/safe-commit.sh --author "3.0.0_SA_CVO <3.0.0_SA_CVO@opal.agent>" -m "verify-channel({project}): {VERDICT} -- {summary}" -- {verify_channel_path}` + `git push origin CLOUD`.

Per `[[feedback-cvo-loop-cycle-5-spot-check-push-after-each-cycle]]`: push after each cycle so MCP-cited commit hashes are visible on origin.

## Step 8 — Update PRD-Inventory + re-arm

- Update project's last-verify-channel timestamp in PRD-Inventory
- If loop mode (`/verify-channel queue 2h` etc.): re-arm next 2h scan via ScheduleWakeup
- ScheduleWakeup primitive (NOT cron) — preserves wakeup-slot separation from /spot-check cron

```
ScheduleWakeup(
  delaySeconds = 7200,  # 2h baseline
  reason       = "/verify-channel 2h lightweight scan + queue process",
  prompt       = "/verify-channel queue 2h"
)
```

## /spot-check → /verify-channel handoff (TIGHTENED to single mechanism)

Per joint CVO council 2026-05-25: Round-1 5-condition handoff matrix is RETIRED. Replaced with single explicit-tag mechanism:

- /spot-check finding with MCP subject-prefix `[SPOT-ESCALATE-CLOSEOUT]` = Class 1 immediate-fire closeout-class signal.
- All other /spot-check findings = fix-authorized within alignment-metadata scope OR routed to COO/driver via standard /spot-check skill body (per `/spot-check/SKILL.md`).

Single explicit-tag = high signal-to-noise. Routine /spot-check findings (alignment fixes, COO-routed substance, drift catches) do NOT auto-escalate to /verify-channel.

## Pre-propagate gate for NOVEL PRDs (per LD-0062 Round-2 Q6)

When /charter authors a new PRD or addendum:
- **NOVEL PRD** (per /charter author NOVEL tag — new project entity, architectural-scope change, introduces new Stakes-Matrix-level risk, cross-fabric scope) → **/verify-channel pre-propagate gate** before /drive starts execution. Gate verdict: CLEAN (permit) / CONCERN-with-mitigation (permit with conditions) / MISALIGNED (block).
- **ROUTINE PRD** (extends prior PRD, fits existing taxonomy, no new Stakes-Matrix-level risk) → background pickup at next 2h scan; /spot-check continues drift-detection in interim.

NOVEL tag drives the routing; /charter author tags PRD header at authoring time.

## §5.6 outcome-feedback emission to Input 0 (Phase 2 trigger)

Per joint CVO council reconciliation 2026-05-25 (§4(d) multi-source Input 0): /verify-channel verdict stream emits to Input 0 substrate as ONE telemetry source among multiple (paired with /spot-check findings, RAVC2 outcomes, /charter loop tick decisions). Mutually informative:
- /verify-channel MISALIGNED verdict on artifact gated by tool X = X failed-to-prevent (surfaced_finding for X) — feeds Input 1 compiler-asks "we need a tool to catch this class"
- /verify-channel CLEAN verdict on artifact gated by tool X = X prevented_incident_candidate — feeds Input 0 prevented_incidents counter

Emission shape: joint draft pending with CL CVO post-MSTR canonical-merge ratification (single-paragraph add for cross-fabric Input 0 infrastructure consistency).

## D4 holding pattern (parallel cascade revisit threshold)

D4 still under Andrew explainer at time of this scribe (2026-05-25T20:33Z). Substance per joint CVO council reframe: ws fabric uses 2-tick threshold; CL fabric uses 30%/48. Both fabrics accept DEPRIORITIZE-NOW + preserve revisit-after-Phase-2-empirical clause. Final Andrew lock will refine the threshold semantics; SKILL.md absorbs when locked.

---

## Relationship to ajb compiler tools

`comp-validate` (gold-script artifact battery), `comp-pipescript deployed` (runner-has-your-code MATCH/STALE), `comp-pipescript postdeps` (required post-steps), `comp-platinum reverse` (artifact -> portal consumer) are ajb's native pipeline-verification tooling — use them as inputs. They are necessary, not sufficient: they check config + structure; verify-channel adds the independent artifact read, the sharp structural test, the decision-useful meta-gate (Mode A), and the project-scope comprehensive 4-component body (Mode B) that no tool implies.

## Configuration

- **Mode A state:** no state file — event-driven (invoked per audit/repair/sweep/close-out item).
- **Mode B state:** PRD-Inventory tracks per-project last-verify-channel timestamp. Verify-channel artifacts at `org/tier1_exec/3.0.0_SA_CVO/verify-channel/verify_channel_{project_slug}_{NNN}.md`. Mode B ScheduleWakeup chain — one wakeup pending at a time; this loop's wakeup replaces any prior.

## Verifier assignment + identity gate

Mode A verifier assignment is the requesting exec's call, constrained by rule 1 (verifier != fixer).

Mode B is CVO-scoped (3.0.0_SA_CVO for ws fabric, 3.1.0_SA_CVO for CL fabric). Non-CVO invocation halts with: `/verify-channel Mode B is CVO-scoped. Your serial is {serial}, not 3.0.0_SA_CVO. If you want a project-scope verify, MCP CVO with the ask.`

Per `[[feedback-cvo-self-validation-mitigation-pattern]]`: when Mode B reviews a window that includes CVO's own commits, transparently flag self-validation surface area with (a) accurate report of own actions, (b) chartered-not-escape-hatch acceptance path, (c) Andrew/MSTR override remains backstop.

---

## Design + history

- **Mode A substance:** adapted from corporeal's verify-channel skill (the 4-check method + sharp structural test + decision-useful meta-gate). Anchors: 2026-05-19 ADHC_CRYPCT.001 (ship-attestation vs deploy-attestation distinction), 2026-05-20 INFGRO rebuild (exit=0 ≠ delivered), MDPF_ASSETS.031 (identity-masking class).
- **Mode B architecture:** LD-0062 ratified 2026-05-25T20:05Z (Andrew "go with your recommendation" on CVO Round-1 + Round-2 brainstorm-responses) + Andrew /verify-channel trigger refinement addendum 2026-05-25T20:19Z + MSTR ANDREW-LOCKS 2026-05-25T20:31Z (joint CVO council ratification).
- **Composite closeout-threshold:** joint CVO council 2026-05-25 — ws CVO 2-class shape (Class 1 immediate-fire / Class 2 scan-detected) + CL CVO subject-prefix recommendation (`[SPOT-ESCALATE-CLOSEOUT]`) + 8 total signals (4 immediate + 4 scan-detected) — canonical MSTR-synthesis merge pending at time of this scribe.
- **Step 2.5 Consumer-output-vs-bucket-write-state alignment** added 2026-05-25 per ws COO ADVI_DEMOV1 Phase 5 AC5 empirical anchor `b097b9826` (LastModified-partition pattern; advisor disjointness via per-row LastModified read).
- **Cross-fabric coordination:** CL CVO `9ff1ba08a` (initial CL ship) + amendment pending; ws CVO this SKILL.md (initial ws ship 2026-05-25T20:33Z); §5.6 outcome-feedback joint paragraph pending post-MSTR-canonical-merge.

Memory anchors: `[[feedback-corroborate-with-concern-verdict-shape]]`, `[[feedback-cvo-proactive-verdict-landing-pattern]]`, `[[feedback-cvo-self-validation-mitigation-pattern]]`, `[[feedback-ld0022-informal-cc-corroboration-works]]`, `[[feedback-cross-fabric-arch-calls-resolve-clean-via-cc-pattern]]`.
