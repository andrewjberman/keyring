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

### META-CHECK HEURISTIC (Step 2c.4 SCAN — added per MSTR charter LD-0012, 2026-05-23)

When a commit body / session log / artifact surfaces a numeric assertion, run these heuristics. Any failure triggers a substance-meta finding (Step 3, routes to code-owner + COO + MSTR via verify-channel verdict). The SCAN extends CVO's reach; the FIX still belongs to the code-owner.

1. **Magnitude vs surrounding context.** Does the number's magnitude make sense given (a) book size / asset class / advisor scale, (b) prior values for the same metric, (c) typical-range expectations for this asset class? Example: a -$54.8M `capital_gains_ttm` on a ~$200M book reads as -27% of book — sense-test against what kind of event would have to occur (market drop, mass selling, account churn) and whether such an event is consistent with the surrounding period.
2. **Sign expectations.** Does a metric named "growth" / "gain" / "balance" / "yield" coming out wrong-signed (or zero) admit a reasonable explanation? Wrong-sign on a metric whose name implies a direction is a strong meta-signal.
3. **Naming-vs-semantic alignment.** Does the field name match what the code actually computes? The LD-0012 class: `capital_gains_ttm` (name says "realized TTM gains") computed as delta cumulative UNREALIZED (per `INF_D_02.advisor_client_detail.py:627-677`). Portal display had already been renamed (INFFIN.019 Fix C) but the data layer kept the misleading name — anyone reading the raw field hits the same mismatch. **Naming mismatches in data layers cascade through every downstream reader (analysts, agents in session logs, future debugging).**
4. **Verdict shape.** When emitting a substance-meta finding, structure as GREEN/YELLOW/RED with MECHANICAL / NOVEL / META layered evidence per `/verify-channel` skill discipline. The LD-0012 verdict file at `logs/2026-05-23/spot_check_0453Z_LD0012_capital_gains_verdict.md` is the worked example template.
5. **D-001 v1.4 META invariant.** A mechanically-functional output that fails this test IS NOT a success. It is a finding that gets chartered to a fix.

**What this heuristic is NOT.** Not a numeric-correctness audit (that's the code-owner's gold-script test suite). Not a full forensic dive (cap at a sharpest-test probe per cycle; deeper investigations route to the producer). Not a substitute for the producer's own Phase-N validation — but a cross-check on whether the producer's framing of their finding got the semantic right (the LD-0012 case: DS flagged it as "TTM rolling realized" — wrong, the computation is delta unrealized — and that semantic confusion is what CVO catches independently).

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
   - **A new TO file** (`org/tier*/...task_orders/{PROJECT}.{NN}*.md`) — does its number `.NN` match what the project JSON's phase narrative says is in that slot? Added 2026-05-23 after /spot-check cycle 11 caught an ADVI_VALFIN TO-5 collision (COO authored field-rename at .005 while JSON narrative + DS commits cited .005 as pipeline-robustness); COO suggested this as a structural backstop on TO-authoring discipline. Cross-check the new TO's number against `org/projects/{CODE}.json` phase narrative + REGISTRY before treating the assignment as aligned.
4. **Substance meta-check on numeric assertions** (added per MSTR charter LD-0012, 2026-05-23 Andrew directive). When a commit body / session log / changed artifact surfaces a number with magnitude (currency, percentage, count), apply the **META-CHECK HEURISTIC** from the Fix-authority section above (magnitude-vs-context, sign expectations, naming-vs-semantic alignment, D-001 v1.4 META invariant). A mechanically-functional output that fails the meta-check IS NOT a success — it is a finding that routes to the code-owner via a verify-channel-style verdict (Step 3 "substance-meta finding" branch). This is the SCAN extension; FIX still belongs to the producer via the safe-deploy chain.

### Step 3 — Decide: nothing / fix / escalate

- **Nothing wrong → quiet log line, advance checkpoint, done.** Three or more consecutive quiet cycles → no log at all (just checkpoint advance + heartbeat refresh).
- **Misalignment, IN SCOPE for CVO → fix it directly** under CVO author line via `.tools/safe-commit.sh`. Then MCP COO with: what was misaligned, what was fixed, commit hash. One MCP per fix; multiple fixes in a cycle = one MCP with a list.
- **Misalignment, OUT OF SCOPE → MCP the responsible driver + CC COO** with a priority-marked finding per the normal CVO discipline. Do not touch the file.
- **Substance-meta finding (numbers fail the META-CHECK HEURISTIC) → MCP the responsible driver + CC COO + MSTR** with a verify-channel-style verdict (MECHANICAL / NOVEL / META layered, GREEN/YELLOW/RED shape) per the LD-0012 worked example. **Never CVO-fixed directly**, even if the fix would be metadata-only (e.g., a field rename) — substance findings always route to the code-owner via the safe-deploy chain. The substance-meta SCAN is the verifier extension; the FIX routing is unchanged.
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
