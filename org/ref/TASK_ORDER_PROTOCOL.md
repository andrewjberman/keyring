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
    <!-- MANDATORY. Minimum by role:
    DS:  comp-pipescript io {script}  |  comp-blast {script}  |  comp-pipescript consumers {script}
    DE:  comp-transform schema-check {Component}  |  comp-blast {fn}  |  comp-cache collisions
    DT/AE: comp-pipescript io {script}  |  comp-routes trace {fn}
    Specify the exact commands. Agent reports results in session log Compiler Tools section.
    -->
  </compiler_tools_mandate>

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
