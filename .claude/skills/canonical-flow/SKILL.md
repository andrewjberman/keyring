---
name: canonical-flow
description: Pick up ANY project that is already in flight or in limbo at the limb of the canonical fabric workflow the invoking seat owns. `/canonical-flow <PROJECT_CODE>` at a Tier-1 seat -- the seat reads the spine (org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md), LOCATES the project on both roots, MEASURES the limb it is actually at from its artifacts (never from status prose), names its limbo class from a closed set, maps its own role to the next limb, and either PICKS THE PROJECT UP there (an execution entry point, through the normal gates) or hands off to the limb's owner and stops. Never for a new project: those enter through /brief-create or /endpoint --forward. `--report-only` measures and reports without acting. Tier-1 seats; MSTR and Tier-2 report and route only.
---

# /canonical-flow -- pick up an in-flight or limbo project at your limb

**Purpose (Andrew-direct, 2026-09-03 ~05:0xZ, MSTR terminal, verbatim):** *"I think we should make
/canonical-flow skill which is basically just a reference to the doc with the instruction that the agent to
whom its sent (which will invariably be a tier1) pick up the project based on their role and current status.
[...] This skill is basically for projects that are already in some kind of limbo state, if they were totally
new we'd just be running it from the initial /brief-create or /endpoint --forward."* And: *"Don't overfit to
one case, it should be for any in limbo project."*

**The reference is the spine: `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`.** This skill restates none of
it. It does three things the spine does not: it MEASURES where a given project actually is, it names WHY it
is stuck from a closed set, and it tells THIS seat which limb is its to pick up and which are not.

## Invocation

| Form | Behavior |
|---|---|
| `/canonical-flow <PROJECT_CODE>` | locate, measure, classify, then PICK UP at your limb (or hand off) -- an execution entry point |
| `/canonical-flow <PROJECT_CODE> --report-only` | locate, measure, classify, report; no act |

**Who runs it:** the Tier-1 seat it is sent to (`4.0.0_SA_CRO`, `1.0.0_SA_CTO`, `2.0.0_SA_COO`, `3.0.0_SA_CVO`, or a
`~lane` of one). `0.0.0_AB_MSTR` owns no limb: it measures, reports and routes to the owner. A Tier-2 seat
enters a project only through an L6 task order: it measures, reports, and routes to its issuer.

## Step 0 -- Read the spine

Read `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` in full at HEAD: section 1 (the limbs, their owners,
instruments and artifacts), section 2 (role exclusivity), section 3 (limb, owner, `dep_stage`, refuser).
Everything below keys on that file's grammar; where this skill and the spine differ, the spine governs.

## Step 1 -- LOCATE the project on both roots, and stop if it is not yours to pick up

Measure each of these; ABSENT is a value, not a guess. Print the table.

| what | where to look |
|---|---|
| tree home | `org/missions/D*/<MACRO>/<CODE>/` -- `project.json` (`dep_stage`, `fabric`, `directive`), `brief/`, `prd/`, `decompositions/`, `task-orders/`, `deliverables/`, `surprise-channel/`, `ledger/` |
| flat register | `org/projects/<CODE>.json` (`dep_stage`, `fabric`, `phase`, `blocking`), the `REGISTRY.md` row, `org/missions/DIRECTIVES.yaml` membership + the directive's `placement` |
| brief | tree `brief/`, or the `brief_ref` the PRD header names, or `docs/briefs/` |
| PRD | tree `prd/<CODE>_PRD.md` (PRD_HEADER block, ENDPOINT section, surface manifest) or `docs/architecture/<CODE>_PRD.md` |
| decomposition | tree `decompositions/`, or `workflows/atom_decomposition/runs/<code-ish>/` |
| task orders | `python .tools/to-check.py --all --project <CODE>` (both roots); `python .tools/to-liveness-join.py` for assignees that are not live |
| surprise channel | `comp-surprise --project <CODE>` (both roots); the latest row citing each item decides its state |
| step logs / compilation | tree `ledger/STEP_LOG.*` |
| holds | the register `phase` / `blocking` text, the directive's `placement`, any Andrew-direct record the row cites |

**Stop conditions, before anything else:**
- **Not found on either root** -> the project is NEW. Print `NEW: not in the loop -- enter through
  /brief-create or /endpoint --forward` and stop. This skill never registers a project.
- **Placed on the other fabric** (the directive's `placement`, or the project's `fabric`, names the device you
  are not on) -> print the placement and stop; it is that device's MSTR and seats who pick it up.
- **Closed** (`status` complete/cancelled with its closure) -> print it and stop.

## Step 2 -- MEASURE the limb from artifacts, then name the limbo class

**The limb is the highest limb whose OUTPUT artifact exists and conforms** (the spine's section 1 names each
limb's output). Read `dep_stage` too, but as a CLAIM: when the measured limb and `dep_stage` disagree, that
disagreement is a finding of its own (the row is stale; owner `1.0.0_SA_CTO` under the tree, the register
grantor for a flat row) and it goes into the report; it never overrides the measurement.

```
  output present and conforming                                  -> past limb
  brief (citable lines)                                          -> L1
  endpoint section / ratified FWD-n set                          -> L2
  project.json under the tree, macro in the ratified enum,
    fabric + directive set, index derived                        -> L3   (flat-only = NOT past L3 under the tree grammar)
  PRD at the tree home with PRD_HEADER + ENDPOINT + manifest     -> L4
  decomposition with its cells and four-postulate record         -> L5
  task orders with decomp_ref + proof block, GO paired           -> L6   (in L7 while any is open)
  every TO terminal with a VALID proof instance, surprises -> rows -> L7 done
  investigation rows filed                                       -> L8
  every item dispositioned by its latest citing row              -> L9
  a route row / stamp with loop_target                           -> L10  (next = the re-entry limb it names)
```

**Limbo classes -- closed, exhaustive over "what is missing / whose turn / is a hold named":**

| class | meaning | owner of the next act |
|---|---|---|
| `STALLED-AT-OWNER` | the next limb's input exists and conforms; its owner has not acted | the next limb's owner |
| `ARTIFACT-GAP` | the next limb's input is missing or non-conforming (a PRD without an endpoint section or manifest; a decomp without its record; a TO without a proof block) | the limb that should have produced it |
| `PRE-TREE` | exists only in the flat register; no tree home | `1.0.0_SA_CTO` (L3 under the tree, then L4 at the tree home) |
| `DEAD-SEAT` | open task orders whose assignee is not live | `2.0.0_SA_COO` (re-address, or seat a fresh lane) |
| `OPEN-ROUND` | every TO terminal; rows undispositioned or no stamp | `3.0.0_SA_CVO` (L8-L10) |
| `ROUTED-UNPICKED` | a stamp names a loop_target and the route owner has not re-entered | `2.0.0_SA_COO` (5 or 6) or `1.0.0_SA_CTO` (2) |
| `SEQUENCED-BEHIND` | a named hold blocks the next limb (a register phase, a directive placement, an Andrew-direct record) | nobody: report the hold's carrier; only Andrew lifts a hold |

A project can carry more than one class; list all, the blocking one first.

## Step 3 -- YOUR ROLE maps to exactly one pickup

| your seat | limbs you may pick up | what the pickup is |
|---|---|---|
| `4.0.0_SA_CRO` | L1 | the brief (`/brief-create`, `--midstream` when the project is already in flight) |
| `1.0.0_SA_CTO` | L2, L3, L4 (and L2 re-entry from an L10 scope change) | `/endpoint --forward` on the brief; registration under the tree; the PRD at the tree home with header, endpoint and manifest; a version bump when the PRD is the gap |
| `2.0.0_SA_COO` | L5, L6 (and L5/L6 re-entry from an L10 route) | `/atom-decomp` over the manifest and the battery; task orders, tight, GO paired; re-address a dead seat; seat a fresh lane |
| `3.0.0_SA_CVO` | L8, L9, L10 | rows, dispositions, the one slug at L10 to the route owner |
| `0.0.0_AB_MSTR`, any Tier-2 | none | report and route |

**Decide, in this order:**
1. If a `SEQUENCED-BEHIND` hold is named -> report it and stop. Do not lift it, do not work around it.
2. If the next limb is YOURS -> pick it up (Step 4).
3. If the next limb is yours but its input has an `ARTIFACT-GAP` owned by an earlier limb -> hand BACK to that
   owner (a decomposition does not proceed on a PRD without a manifest; the COO does not write the manifest).
4. If the next limb is NOT yours -> hand off and stop: the spine's handoff for that limb where one exists (the
   L4 to L5 notifier fires on the PRD commit; a task order carries its own GO), otherwise one message to the
   owner naming the measured limb, the class and the gap. Never do another seat's limb.

## Step 4 -- Pick it up, through the gates

This is an execution entry point. After the report, do your limb's act in your own lane and under every
standing law: `safe-commit`, the L6 gate for any task order, the L4 to L5 notifier, record + broadcast for any
Andrew word met on the way, a surprise as a ROW. The pickup ends when your limb's output artifact exists and
the handoff to the next limb has fired; say which artifact and which handoff. Nothing here skips a limb.

## Step 5 -- Output

```
CANONICAL FLOW -- {serial} on {CODE} ({date time})

LOCATE   home: {tree path | flat only}   placement: {laptop | site-z} ({carrier})   status: {..}
         brief {path@vintage | ABSENT}  endpoint {..}  PRD {..}  decomp {..}  TOs {n open / m terminal}
         rows {n items, k undispositioned}  stamp {..}  dep_stage (claimed): {..}
MEASURED limb: {Ln} -- highest conforming output: {artifact@vintage}
         claimed vs measured: {AGREE | DISAGREE: dep_stage says X, artifacts say Y -> finding, owner ..}
CLASS    {class} [, {class}]: {one line each, with the missing or stale artifact named}
ROLE     {serial} owns {limbs}; next limb {Ln} is {MINE | NOT MINE -> {owner}}
ACT      {what I do now, or: handed off to {owner} by {handoff}; or: HOLD {carrier}, stopped}
```
Then the act itself, or the handoff message, or nothing (report-only).

## Rules

- **Measure, never infer.** A `<status>` field, a `phase` sentence and a `dep_stage` value are claims; the
  artifact at its vintage is the measurement. Cite paths and hashes.
- **Role exclusivity is absolute** (spine section 2). A pickup at a limb you do not own is refused by this
  skill's Step 3 before any gate sees it.
- **No new projects, no holds lifted, no task orders from anyone but the COO, no CVO act before L8.**
- **General by construction.** The classes above are defined by artifact grammar and ownership, not by any
  project; a case this skill cannot classify is a defect in the class set, surfaced as a row, never
  special-cased in the skill.

## Notes

- Authority + provenance: Andrew-direct 2026-09-03 (verbatim above), recorded at creation in
  `org/tier0/ledger/LD-0524.md`; authored by `0.0.0_AB_MSTR`. A skill is accepted on an observed run: the
  first run is the Tier-1 seat Andrew sends it to, on the project he names.
