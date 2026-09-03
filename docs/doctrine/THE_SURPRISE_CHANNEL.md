# THE SURPRISE CHANNEL

**An observation you are not authorized to chase needs somewhere to go, or it becomes one of two
failures.** Suppressed, and a real defect dies at the seat that found it. Chased, and a velocity mandate
turns into an investigation. **Give it a third path: ONE ROW appended to the project's surprise channel,
no action taken, work continues.**

Named by Andrew, 2026-08-06. **CARRIER CORRECTED 2026-09-03 (Andrew-direct at the `3.0.0_SA_CVO` terminal
~03:1xZ, VERBATIM: *"claude.md should not have that rule to do this over mcp"*): the surfacing act IS THE
ROW, never a broker message.** A row is what the commit-time row gate validates (`.tools/surprise-row-gate.py`:
`spec_asserts` + `world_is`), what the step-8 notifier delivers to `3.0.0_SA_CVO` with its exact path
(`org/surprise_channel/surprise-watch.sh`), and what the proof-of-spec `surprises` limb binds a task order's
`complete` flip to (`.tools/proof-of-spec-check.py`). A notifier that watches files is structurally blind to
a surprise that only ever reached an inbox -- measured 2026-09-03: one surprise cost three broker messages,
an issuer reply and a CVO assembly in place of one file append. **Where the row goes:** a tree project's
`org/missions/D*/<MACRO>/<CODE>/surprise-channel/investigations/INVESTIGATION_v{N}.md` -- lane ANY, the
worker appends it (measured: `owned-paths-validate.py check_agent 0.8.0_AE_CloudComp` admits that path). A
legacy flat channel `org/surprise_channel/<CODE>/` is lane CVO_WORKSPACE (CVO, CTO, COO only -- measured the
same way): there the ISSUER appends the worker's row; a message carries the row's text to the issuer, never
the surprise to CVO. That lane asymmetry is itself a finding, owner `2.0.0_SA_COO` (registry grantor).

---

## The rule

**When work is scoped — a shape project, a build to a rubric, a drive loop, any mandate that says
*do this and not that* — every seat still sees things outside the scope.** That is not a failure of
scoping; it is what competent attention produces. The question is only where the observation goes.

```
SUPPRESS  -> a real defect dies at the seat that found it, and the seat learns not to look
CHASE     -> the scope dissolves; one surprising number becomes an investigation
REPORT    -> ONE ROW in the project's channel (spec_asserts + world_is). NO ACTION TAKEN. Work continues.
             CVO triages FROM THE ROW the notifier delivers -- never from a message (2026-09-03).
```

**The channel must be named explicitly in the task order.** A seat told only *"do not chase"* has been
given one instruction and two options, and will pick suppression — because suppression looks like
compliance. **Naming the channel is what makes "do not chase" safe to obey.**

## What travels, and what does not

| the report carries | the report does NOT carry |
|---|---|
| the observation, one line | an investigation |
| its grounding, or an explicit *ungrounded* marker | a proposed fix |
| the fact that **no action was taken** | a paused task |

**The seat keeps working fail-closed on its actual task.** A surprise report is not a blocker, not a
question, and not a request for a ruling — the coordinator decides whether it becomes any of those.

## The loop is only closed when the channel has a DESTINATION

**Andrew-direct 2026-08-07, VERBATIM:** *"once we have a plan, you just do the fucking plan, remediation
suggestions go through the surprise channel and get added to a remediation doc."*

Two halves, and the second is what makes the first survivable:

```
ONCE THERE IS A PLAN -> DO THE PLAN.   A remediation idea is NOT a reason to deviate from it.
A REMEDIATION IDEA   -> SURPRISE CHANNEL -> A REMEDIATION REGISTER -> a RUBRIC, on sovereign word.
```

> **⛔ A CHANNEL WITH NO DESTINATION MOVES THE SUPPRESSION ONE SEAT UP.** The seat is saved from
> choosing suppress-or-chase — and the coordinator inherits that exact choice, with a fuller board and
> no more authority to act. **If the report lands in a person rather than a document, it dies in a
> person.** The register is what makes the channel terminate somewhere rather than accumulate somewhere.

**THE REGISTER IS NOT A BACKLOG ANYONE WORKS.** A row landing in it is the **END** of a seat's
involvement, not the start. Rows leave only through a rubric the sovereign authorizes — **which is what
stops "we should also fix X" from becoming scope by accretion.**

**And it makes "we knew about that" checkable rather than claimed.** A compromise accepted knowingly and
a compromise missed look identical six weeks later unless one of them was written down at the time.

*Working instance: `docs/architecture/MDPF_REMEDIATION_REGISTER.md` — opened while its build was still
running, with the compromises that build knowingly shipped.*

## Why the coordinator, not the owner of the surprising thing

Routing to the owner invites a conversation; routing to the coordinator invites a **triage**. The
coordinator is the only seat with the whole board, so they can tell in one read whether the observation
is already ruled, already known, out of scope, or genuinely new — **the four answers the finding seat
cannot distinguish from where it sits.**

## The failure this prevents, stated as a property

**A scope instruction without a reporting channel silently converts every out-of-scope observation into
a decision the least-informed seat has to make alone.** The seat must choose suppress-or-chase with no
knowledge of whether the thing is already handled. **Both choices are bad and it cannot tell which is
worse.** The channel removes the choice.

---

*Worked instance (cited, not retold): `MDPF_CANONICAL_PLATINUM`, 2026-08-06/07. Under an explicit
no-chasing mandate, a verification seat measured a served field as `ABSENT` where the governing contract
said `null`, took no action, and routed one line. The contract amended before the build emitted —
removing a regression verdict the comparator would otherwise have manufactured on the exact transition
the contract ordered. Suppressed, it surfaces at acceptance as a failure; chased, it costs the drive
loop. Records: `docs/architecture/MDPF_CANONICAL_PLATINUM_DELIVERABLE_CONTRACT.md` §B1,
`docs/architecture/MDPF_CANONICAL_PLATINUM_PRD.md` §0.*
