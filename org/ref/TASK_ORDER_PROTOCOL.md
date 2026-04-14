# Task Order Protocol

Full XML template, filename convention, instance rules. Referenced from XXX.md.

---

## Location

Task orders go in the **receiving agent's** `task_orders/` folder:
```
{receiving_agent_folder}/task_orders/{MACRO}_{6CHAR}.{task-code}.{description}.md
```
One file per feature. Never overwrite into a monolith.

---

## XML Template

```xml
<task_order>
  <metadata>
    <id>{issuing_serial}-{YYYY-MM-DD}-{short_slug}</id>
    <issued_by>{issuing_serial}</issued_by>
    <issued_to>{receiving_serial}</issued_to>
    <date>{YYYY-MM-DD}</date>
    <status>staged | pending | complete</status>
    <project_code>{MACRO}_{6CHAR}</project_code>
  </metadata>

  <objective>
    <!-- 1-3 sentences: what needs to be accomplished and why -->
  </objective>

  <context>
    <!-- Background, PRD references, architecture decisions the agent needs -->
  </context>

  <compiler_tools_mandate>
    <!--
    MANDATORY. THREE-PHASE structure (all TOs, no exceptions).
    For each <run>, fill in the specific command and an <expect> block.
    <expect> encodes what "normal" looks like — agents verify output against it.
    <if_mismatch> tells the agent what to DO if output is unexpected (not just that something is wrong).

    Example (filled):
    Phase 1 — before writing:
      <run>comp-blast DistributionTab</run>
      <expect>8 downstream nodes; all via opal-partners-data Lambda; OFC is additive so count unchanged</expect>
      <if_mismatch>Flag to COO — unexpected blast radius may mean shared S3 artifact with another active TO</if_mismatch>

      <run>comp-pipescript io D_01</run>
      <expect>COLUMN GAPS: 0 gaps. S3-DYNAMIC: dim_advisor_office.csv present. PORTAL CONSUMERS: partner_analytics → DistributionTab</expect>
      <if_mismatch>If COLUMN GAPS shows any gap, fix before proceeding — silent column omissions have caused zero-valued output in prod</if_mismatch>

    Phase 2 — before committing:
      <run>comp-transform schema-check DistributionTab</run>
      <expect>0 MISSING fields; ofc types in rendered set; NOTE fields are expected aliases</expect>

    Phase 3 — after committing:
      <run>comp-blast [changed function]</run>
      <expect>Blast radius identical to Phase 1 — no new downstream nodes</expect>
      <if_mismatch>Flag to COO — new downstream consumers appeared unexpectedly</if_mismatch>

    WHEN <expect> is required: whenever the tool output gates a decision (blast radius before cross-domain TO,
    column gaps before modifying load logic, validate before signaling AE). If the run is purely orientation,
    a short note is acceptable.

    Results must appear in session log Compiler Tools table.
    A TO with no compiler check logged is NOT accepted as complete.
    See: org/standards/TO_COMPILER_GATE.md
    -->
  </compiler_tools_mandate>

  <cross_domain_coordination>
    <!-- Fill this section ONLY when this TO touches a file, S3 key, or data contract
    that is also touched by another active TO in the same wave.
    COO/CTO must identify cross-domain resources during PRD decomposition using comp-blast.

    If applicable:
    - shared_resource: {file or S3 key}
    - also_in_to: {other TO IDs}
    - last_write_owner: {serial that commits last}
    - required_action: "Message {serial} via MCP before committing to {file}. Pull latest before writing."

    If not applicable: <none/>
    -->
  </cross_domain_coordination>

  <acceptance_criteria>
    <!-- MANDATORY. Specific, machine-checkable. Not "code runs" or "build clean."

    STANDARD CRITERIA (include for every gold-touching DS TO):
    N.   comp-validate {script} --artifact /tmp/{artifact}.json exits 0
         (all ERROR checks pass; WARN count documented in session log)
    N+1. comp-pipescript deployed {script} shows MATCH after S3 upload

    STANDARD CRITERIA (include for every portal-touching DE TO):
    N.   comp-transform schema-check {Component}: 0 MISSING fields
    N+1. bun run build (or bunx tsc -b): zero TypeScript errors

    Role-specific examples:
    - DS: fee_earning_aua > 0 for at least one advisor with aua > $1M (Travis Penfield spot-check)
    - DS: geo_drill present in timeseries_chart.json with >= 5 state keys
    - DS: comp-validate {script} --artifact /tmp/{artifact}.json exits 0
    - DE: comp-transform fields shows all rendered fields present in TypeScript type
    - DE: state legend items are <button> elements (clickable), not <div> (static)
    - AE: comp-pipescript deployed {script} shows MATCH before triggering gold run
    - AE: comp-iam gaps shows no new permission gaps after iam.tf change

    Agent confirms each criterion explicitly in session log before marking complete.
    -->
  </acceptance_criteria>

  <scope>
    <files>
      <file action="create | modify | reference">path/to/file</file>
    </files>
  </scope>

  <requirements>
    <requirement id="1"><!-- specific, testable --></requirement>
  </requirements>

  <deliverables>
    <deliverable type="commit | document | spec"><!-- description --></deliverable>
    <deliverable type="document">Session log with Compiler Tools section</deliverable>
  </deliverables>

  <do_not>
    <rule><!-- specific anti-pattern to avoid --></rule>
  </do_not>
</task_order>
```

---

## Status Values

| Status | Meaning | Who sets it |
|--------|---------|-------------|
| `staged` | Assigned but no GO received — do NOT start | COO |
| `pending` | GO received — active or queued | Agent (on receiving GO) |
| `complete` | Work done, deliverables confirmed | Agent (self-marks) |

`staged` → `pending` happens when the agent receives a GO message from COO. Flip it immediately and begin. The GO message IS the authorization — do not ask Andrew.

---

## Filename Convention

**Project work:**
```
{MACRO}_{6CHAR}.{task-code}.{description-words}.md
```
- Dots separate segments. Dashes separate words within a segment.
- Project codes: `org/projects/REGISTRY.md` | Macro codes: `org/projects/MACRO_CODES.md`

```
ADVI_49PUSH.012.de-wire-books-tab.md
ADVI_V1VERS.004.adv-drill-cla.md
ADHC_DESIGN.027.de-tooltip-migration-pod-0.2.md
```

**Ad-hoc (no registered project):**
```
{description-with-dashes}.md
```

---

## Parallel Instances (~B, ~C)

When Andrew runs multiple workers for the same role:
- `register_agent("0.4.0_DS_ClientPlatform~B")` — instance B
- All instances share the same org folder, logs, task_orders
- Commits: use BASE serial as `--author` (no `~` suffix in git)
- Log filenames: include suffix — `nna_fix~B.md`
- Task orders: append suffix when issuing to a specific instance — `ADVI.012.de-books~B.md`
- MCP: sending to base serial delivers to ALL live instances; `~B` delivers to only that instance

---

## Completion Protocol

- Receiving agent edits `<status>` from `pending` to `complete` when done
- This is the done signal — no separate notification required
- Tier 1/2 agents verify completion against logs and commits, not just the status field
