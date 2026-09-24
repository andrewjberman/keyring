# Final adjustments -- /canonical-flow and /canonical-drive against spine v3.18

**Author:** `4.0.0_SA_CRO`. **UTC:** 2026-09-23 ~17:1xZ. **For:** `1.0.0_SA_CTO~C`, which implements.

**Authority:** Andrew-direct ~17:0xZ at the `0.0.0_AB_MSTR` terminal, relayed as message 99697, VERBATIM: *"let's hold
the push until the /closer and associated work and /canonical-flow and /canonical-drive workflows are handled.
1.0.0_SA_CTO~C should be taking CRO's final adjustments and working it in as needed to the key surfaces in the
ajb_workspace"*. Record: `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20260923_1700Z_PUSH_HELD_UNTIL_CLOSER_AND_CANONICAL_FLOW_WORK_LANDS.md`
@`8a5c01207d`.

## What was checked (MEASURED at HEAD, spine v3.18 @`89e75f1dd8`)

| Surface | Last change | Verdict |
|---|---|---|
| `.claude/skills/closer/SKILL.md` + 4 templates | `893aa7463c` 16:58Z | **CONFORMS.** It carries the propose, run and review forms, the project state while a closer runs, and call 5 and 5b "live" |
| `.claude/skills/canonical-drive/SKILL.md` | `ffa7a1533c` 16:51Z | **ONE GAP** (A2 below) |
| `.claude/skills/canonical-flow/SKILL.md` | `3ae8c4bf7b` 15:57Z, before v3.17 and v3.18 | **STALE.** Zero hits for `closer`, `thread` or `enrichment` in 48,304 bytes (A1) |
| `org/tier1_exec/2.0.0_SA_COO/DRIVE.md` | `a8b4b5bf9c` 09-14 | no conflict. It restates none of the changed obligations (zero hits for `WIDTH`, `every cell`, `later round`, `thread`) |
| `.claude/agents/worker.md` | `6c118c12de` 09-16 | no conflict. It hard-codes no typecheck, lint or suite run (zero hits), so the diet reaches it through the face |
| Codex projection | `install-codex-load-skill.py --check` | 13 of 13 projected skills in sync (`closer` 5 files, `canonical-flow` 1), 3 Claude-only not projected |

## A1 -- `/canonical-flow` does not know the closer, the thread or enrichment rounds (HIGHEST)

**Why it matters now:** `IRPT_FNTEND` and `IRPT_BCKEND` carry `closer_contract` since v3.17. `/canonical-flow` runs on
either one would do three wrong things:
- measure a limb that is no longer running;
- classify limbo from stale rounds, for example `SLUG-UNREAD`;
- route a hand-off into the canonical loop that `/canonical-drive` now skips.

`canonical-flow` is also a `both` row in `PARITY.yaml`, so Codex seats read the same stale text.

Edits, all text:
1. **Step 1 (LOCATE) or Step 2 (MEASURE):** read `closer_contract` on the row first. If present, report
   `CLOSER -- measured by the seats' STATUS files and the CVO reviews under <contract path>; no limb is measured` and
   route to `/closer status` and `/closer run|review`. Classify no limbo class and hand nothing into L5-L10.
2. **Step 2 measurement, one new line for a threaded project:** `thread: NOT LIVE | LIVE (trace path@commit)`.
   Read it from the FWD-1 trace artifact. It is the headline stage fact under v3.16.
3. **`ARTIFACT-GAP` class (`:207`)**, three more named inputs:
   - a product PRD without its THREAD and ENRICHMENT BACKLOG sections;
   - a round-1 decomposition not over the thread's hops;
   - a round-N analysis without an ENRICHMENT LIST.
4. **Tree map and role table:**
   - The PRD row (`:108`, `:154`) adds the THREAD and ENRICHMENT BACKLOG sections.
   - The decomposition row (`:110`) reads "the rectangle of THIS round".
   - The COO row (`:336`) replaces "`/atom-decomp` over the manifest" with: "round 1 over the thread's hops; an
     enrichment round over the enrichment list; lenses `DECLARED-NOT-APPLICABLE` on round 1 except `comp-iam` when
     the thread touches IAM".
5. **Transition sentence:** a round cut before v3.16 finishes under its cut orders (spine section 5). So the
   measurement names the law a round was cut under and never re-grades a pre-v3.16 round for lacking a thread.

## A2 -- `/canonical-drive` WIDTH can push round 1 off the thread

`:70` obligation 2 reads *"Every uncovered cell serving an ungraded FWD ... is cut THIS tick"*. Obligation 5 reads
*"Idle lane + uncovered FWD-serving cell = a DEFECT"*.

On round 1 of a threaded project, FWD-2 onward are ungraded by design and belong to the enrichment backlog. A tick
reading the PRD's FWD ids against the decomposition's `cell_refs` (Step 1, `:33-36`) will count them as uncovered and
cut or nudge work the thread round must not carry.

Edit, one sentence under obligations 2 and 5: *"On round 1 of a threaded project only FWD-1 is in scope; an ungraded
FWD with no cell is enrichment backlog for the round-N analysis, never a WIDTH gap or an idle-lane defect."* Also add
`thread NOT LIVE|LIVE` to the Step 1 row.

## A3 -- nothing further on `/closer`

It conforms as landed. No edit.

## Cost

A1 is about 15 lines in one skill and A2 is two sentences, text only, no gate. After both land, this seat has no
further adjustments for the push the hold names. Whether the work is "handled" remains Andrew's call.
