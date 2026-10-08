# FUTURE PAGE (noted on Andrew's word; not scheduled) -- the fabric activity / overlap map

**Noted by:** `4.0.0_SA_CRO`, 2026-10-08 ~17:3xZ. **For:** whichever seat takes NFRA_MCPORTAL up after its park.
**Andrew, verbatim (laptop, 4.0.0_SA_CRO terminal):** "Command is fine for now, interface design and etc can exist on
the MCPORTAL and we'll handle that at a later date" and "I would make a note to that end because it is a good idea and it
does deserve a page on there". Record:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261008_173xZ_OVERLAP_COMMAND_IS_FINE_INTERFACE_ON_MCPORTAL_LATER.md`.

**Status:** a note, not a task order and not a PRD change. It enters the project only through its own loop (an L10
addendum or a later round), at a date Andrew sets.

## What the page would show

The same three reads the command gives today (`.tools/fabric-activity.py`, build record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/GRAPH_COHERENCE_BUILD_20261008.md`):

1. **Per box:** commits, seats, surfaces touched, and how many of those another box is also on (`boxes`).
2. **Overlap:** the parts of the estate with two or more boxes on them, Terraform first, with each box's commits marked
   on-box or merged (`overlap`).
3. **Who is on one surface:** commits by box, open task orders that declare it, open deploys that hold it, and what the
   estate graph says it is (`who <surface> --graph`).

## Source of truth for the page

- Records: `s3://opal-313476888478-globgrph/fabric/activity/v1/dt=<day>/box=<box>/*.json` (schema
  `fabric-activity/1`; one per commit, written by the box that made it).
- DECLARES and HOLDS: task orders' `<paths>` and `org/critical_paths/.open_deploys/`.
- Estate: the served graph (`mcp.opalinvest.dev/graph/cypher`).

Read on open, never an alert, consistent with the portal's existing contract ("read when opened, never an alert").
