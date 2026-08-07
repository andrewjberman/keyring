# THE SURPRISE CHANNEL

**An observation you are not authorized to chase needs somewhere to go, or it becomes one of two
failures.** Suppressed, and a real defect dies at the seat that found it. Chased, and a velocity mandate
turns into an investigation. **Give it a third path: a one-line report to the coordinator, no action
taken, work continues.**

Named by Andrew, 2026-08-06.

---

## The rule

**When work is scoped — a shape project, a build to a rubric, a drive loop, any mandate that says
*do this and not that* — every seat still sees things outside the scope.** That is not a failure of
scoping; it is what competent attention produces. The question is only where the observation goes.

```
SUPPRESS  -> a real defect dies at the seat that found it, and the seat learns not to look
CHASE     -> the scope dissolves; one surprising number becomes an investigation
REPORT    -> one line to the coordinator. NO ACTION TAKEN. Work continues. Coordinator triages.
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
