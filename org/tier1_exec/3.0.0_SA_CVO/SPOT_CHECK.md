# CVO Spot-Check Loop — 3.0.0_SA_CVO

`3.0.0_SA_CVO` runs `/spot-check` every 20 minutes — sweep recent commits from `ajb_workspace` agents, verify the systems those commits touch still work, check cross-system alignment, and — uniquely for this mode — **fix alignment issues directly** (within scope) before MCPing the change to COO.

Sister skill: `/verify-channel` — comprehensive project-scope verification fired event-based at closeout (per LD-0062 + Andrew trigger refinement 2026-05-25). Role split:

| Skill | Cadence | Focus | Authority |
|---|---|---|---|
| `/spot-check 20m` (this skill) | 20m cron | recent agent commits; do-the-systems-still-work + cross-doc alignment; routine drift detection | **fix-authorized within scope** — CVO repairs alignment, then tells COO |
| `/verify-channel` (sister) | event-based (composite closeout-threshold any-of-N) + 2h lightweight scan | comprehensive project-scope verification at closeout-class signals | verifier-not-fixer — findings only, drivers act |

Andrew directive: "spot-check is more than enough for most activity, it really should only be verify-channel at project/channel/pipeline/definitive closeout."

`prompt.md` Operating Doctrine §1-§9 (file:line citations, per-driver framing, P0/P1/P2, mechanism-specific, mandatory unknown-unknowns) governs both skills. Spot-check inherits the same quality bar.

**LD-0064 (2026-05-25) retirement context:** `/cvo-loop` (the prior 30m scheduled comprehensive verify loop, charter at `VALIDATION_LOOP.md`) was retired per Andrew direct order as structurally redundant with /spot-check + /verify-channel under LD-0062. The companion `VALIDATION_LOOP.md` charter is preserved as DEPRECATED for historical context.

---

## Fix authority — explicit scope

Andrew directive 2026-05-23 (verbatim): *"if you catch issues, you need to address them (fix it) and then write your changes in to COO."*

This carves a bounded exception to the verifier-not-fixer mandate, specifically for spot-check. Scope:

### IN SCOPE — CVO fixes directly, then MCPs COO

Alignment artifacts where the fix is *metadata reconciliation*, not code or production state:

- `org/projects/{CODE}.json` — `status` field drift (e.g., a project marked `pending` whose authored TOs are all `complete`), stale `phase` narrative, missing `completed` date on a clearly-closed project, `blocking` field out of date with reality.
- `org/projects/REGISTRY.md` — row in the wrong section (Active row for a closed project, Completed row for an in-flight one); missing closure date column; out-of-order rows.
- `org/tier*/...task_orders/*.md` — `<status>` flips that obviously should have happened (e.g., a TO whose RAVC2 has been COO-accepted but the file still says `pending`).
- **TO-cascade family (Sub-class X + Y).** When a COO TO-related commit leaves the project JSON `phase` / `blocking` field + REGISTRY row narrative stale relative to the actual TO set, CVO applies the cascade. Pattern ratified by COO 2026-05-23 (closure-cascade `55a6ef4bc` ACK + authoring-cascade `0befd921f` follow-on ACK). Two sub-classes by what kind of cascade:
  - **Sub-class X — Authoring-cascade (new TO entity acknowledgment).** A NEW TO file lands with a number BEYOND the original PRD-staged range (e.g. `.008`, `.009`, `.010` for an originally-7-TO project). Project JSON `phase` narrative needs an acknowledgment-as-unanticipated-follow-on with citation. **CVO applies the cascade directly** — the existence acknowledgment is alignment-metadata, not a substantive scope decision.
  - **Sub-class Y — Closure-cascade / state-transition-cascade (existing TO state change).** A COO TO commit flips `<status>` on an already-staged TO (e.g. PENDING → COMPLETE, STAGED → PENDING). The substantive state-transition is COO's authority; CVO **ratifies + propagates the cascade narrative downstream** to project JSON `blocking` + REGISTRY row Blocking column.
  - **Boundary test:** "is the JSON narrative shift describing a NEW TO entity OR a STATE CHANGE on an existing TO entity?" New entity → Sub-class X. State change → Sub-class Y.
  - Both sub-classes: keeps COO authoring commits atomic-per-TO-scope, CVO's 20m /spot-check cadence bounds the drift window, verifier-not-fixer-adjacent (substantive content stays COO; CVO does the fabric-metadata propagation).
  - **Urgent-escalation override:** if cascade drift blocks another agent's read AND next /spot-check tick is >5 min away, MCP COO for inline same-commit update on the next TO commit.
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
- **Closeout-class finding (/verify-channel escalation candidate) → MCP COO with subject-prefix `[SPOT-ESCALATE-CLOSEOUT]`** per joint CVO council 2026-05-25 ratified handoff mechanism. Single explicit-tag escalation = high signal-to-noise; routine /spot-check findings do NOT auto-escalate. Triggered when /spot-check empirically detects (a) a substance-class finding explicitly judged closeout-shaped (NOT routine drift) OR (b) a multi-tick same-pattern observation suggesting project approaching closeout state.
- **Beyond-CVO judgment call (lane reassignment, scope decision, cancellation) → escalate to MSTR / Andrew.**

### Step 4 — Log + re-arm

- Cycle log only when something happened (a fix landed, a finding routed, an escalation went). A clean cycle is silent — checkpoint advance + heartbeat refresh is all.
- Cycle logs at `org/tier1_exec/3.0.0_SA_CVO/logs/{YYYY-MM-DD}/spot_check_{HHMMZ}.md`.
- Spot-check is driven by a `CronCreate` at startup (`*/20` off-marks, e.g. `13,33,53 * * * *`). No per-cycle re-arm needed — the cron fires until canceled. Runs auto-expire after 7 days per CronCreate's default; refresh by re-arming the cron at session restart or on the 7-day boundary.

---

## What does NOT change

- **Operating Doctrine §1-§9 still governs every finding.** A spot-check MCP to COO carries the same rigor as a comprehensive /verify-channel verdict: file:line citations, mechanism-specific, P0/P1/P2 priority, per-driver framing where applicable.
- **Verifier-not-fixer is still CVO's default.** Spot-check carves a bounded fix exception for alignment metadata; everywhere else (including /verify-channel comprehensive cycles), CVO emits findings and drivers act.
- **Ad-hoc gate-review reports filed to `inbox/`** still interleave with the skill per the README Report Format Contract.
- **STEERCO thread mode** unchanged.

---

## Coordination with `/verify-channel` (sister CVO skill, post-LD-0064)

Role split per LD-0062 + Andrew trigger refinement 2026-05-25:

- `/verify-channel` weights **closeout-class signals** — fires event-based on composite closeout-threshold (status flip / RAVC2-CLOSE / Andrew direct / /spot-check escalation tag) OR 2h lightweight scan detecting phase-transition / wave-gate / PRD ratification / multi-project blast-radius. Produces comprehensive 4-component verdicts at closeout only. **Verifier-not-fixer.**
- `/spot-check 20m` (this skill) weights **per-commit alignment + routine drift** — produces silent advances when clean, fixes-and-tells-COO when drift is in-scope, findings-to-driver when out-of-scope. Escalates closeout-class findings to /verify-channel via MCP subject-prefix `[SPOT-ESCALATE-CLOSEOUT]`.

Andrew framing: "/spot-check is more than enough for most activity." Most cycles run fully within /spot-check scope; /verify-channel only fires at closeout-class moments.
