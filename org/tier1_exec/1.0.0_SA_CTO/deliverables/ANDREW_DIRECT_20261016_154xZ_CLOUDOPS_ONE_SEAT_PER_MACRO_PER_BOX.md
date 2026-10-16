# ANDREW-DIRECT 2026-10-16 ~15:4xZ -- CloudOps seats: one per macro per box, never one per task

**Where:** the dell1 terminal of `1.0.0_SA_CTO~DELL1`.

## His words, verbatim

> "Something we need to decide on real quick, when we spawn cloudops agents, we are spawning one for every little thing, and i think there
> is a lot of token waste doing a startup for an agent, they do one little task, and then are just empty tick driving until i close them.
> There should just be one cloudops agent per maybe three projects at a time, if a fourth project needs one, then we add another cloudops
> agent, and they handle the 4th 5th and 6th projects needs. Idaelly these agents are grouped around macros, like, an amgt cloudops, a mdpf
> cloudops, an advi cloudops. this is actually the better way to do it, one cloudops per macro group per box. let's get that out as a rule to
> the fabric and persisted somewhere"

## The rule as landed (CLAUDE.md rule 34)

- **ONE `0.7.0_AE_CloudOps` lane per MACRO per BOX.**
  - It carries every CloudOps order for that macro's projects on that box: AMGT's, MDPF's, ADVI's, TCKT's.
  - A new CloudOps order goes to the live macro lane. A lane is never spawned for one task.
  - A macro with no live lane on the box gets one, and it stays seated for that macro's next orders.
  - The lane's name carries the macro. MSTR assigns it from the spawn audit, for example `0.7.0_AE_CloudOps~AMGT1`.
- **Overflow, from his first form:** about three projects with live orders per lane. When a macro has a fourth project with live CloudOps
  orders at once, MSTR seats a second lane for that macro, and it takes the fourth to sixth.
- **What it replaces for CloudOps:** the 2026-08-24 ~19:29Z rule of one project per Tier-2 seat instance, which the seating check in
  `.tools/to-decomp-ref-lint.py` enforces. That rule stands for every other Tier-2 class. For CloudOps the seating check narrows to: refuse a
  new order whose macro differs from the macros the lane already holds.
- **Why (his):** the token cost of a startup per small task, followed by a seat that sits empty-ticking until he closes it.

## Owed acts

- **`0.0.0_AB_MSTR` (every box):** amend the seating check for the CloudOps class as above, and seat CloudOps by macro from now on.
- **Consolidate the live lanes on each box.** Idle single-task lanes close, and a working lane becomes its macro's lane when its order ends.
- **Every COO:** address CloudOps orders to the macro lane.

-- recorded by 1.0.0_SA_CTO~DELL1
