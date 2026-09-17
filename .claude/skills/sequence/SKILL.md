---
name: sequence
description: Recompile and read THE SEQUENCE (org/missions/SEQUENCE.yaml) -- the ordered projects, their gates and live state -- in one command. `/sequence` recompiles the file's `compiled:` block from the project register, PRD sign-offs, git and the COO roster and renders it; `/sequence <CODE>` one project; `/sequence flags` only flagged projects. Read-only apart from rewriting the compiled block. Any seat.
---

# /sequence -- recompile THE SEQUENCE and read current state

**Authority.** Andrew-direct 2026-09-17 at the `1.0.0_SA_CTO` terminal: ~14:0xZ *"nested json which is compiled at viewtime
that is tied to the underlying projects ... a line at the top that says run the script to recompile"*, and ~15:0xZ *"let's
make a skill called /sequence which runs the recompile. All state data on projects in sequence.yaml should be compile-only.
the list of included projects and intended order can be handwritten ... but the rest should all be compiled."*

## The file has two halves

| half | what | who writes it |
|---|---|---|
| **HANDWRITTEN** | which projects are sequenced (`projects:` keys, `parked:`), the order (`stages:`, each project's `stage`), the ordering constraints (`waits_on`, `hold`, a manual gate's `confirmed`), the human reason (`why`), `capacity`, `change_log` | `1.0.0_SA_CTO` / `1.0.0_SA_CTO~Z`; an ORDER change only on Andrew's word, quoted in `change_log` |
| **COMPILED** | every state fact: dep_stage, status, phase, PRD sign-off, last activity, coo_lane, flags, gate states, capacity used, next-slot order | ONLY `python .tools/sequence-check.py --compile`, between the marker lines at the bottom |

The validator REFUSES a project `notes` key and a `why` that states state (a stage word, a sign-off word, a version, "in
flight", "seated", a lane) -- so state cannot creep back into the handwritten half.

## Run

```bash
python .tools/sequence-check.py --compile           # rewrite the compiled block, print its JSON
python .tools/sequence-check.py                     # the human rendering (stage by stage, flags, capacity)
python .tools/sequence-check.py --project <CODE>    # one project (repeatable)
python .tools/sequence-check.py --flags             # flagged projects only
```

`/sequence` = `--compile`, then the rendering (`--project` / `--flags` when an argument is given). Print, in this order:
1. The compile's `OK:` line (compiled_at, head) -- or its `ERROR:` verbatim. A validation ERROR means the handwritten half is
   malformed or states state: nothing is compiled, and the fix is the handwritten half, never the check.
2. The rendering.
3. One line per flag class with its denominator (`FLAGS (denominator N projects)`), and the CAPACITY line.

## Reading it right

- **The compiled block is a SNAPSHOT** as of its `compiled_at` + `head`. A committed copy is history; recompile before acting.
- **Exit codes:** 0 rendered; 1 nothing rendered (file unreadable or does not validate); 2 rendered with an UNREADABLE source;
  3 a `--project` code neither the sequence nor the register holds (a typo until proven otherwise).
- **Flags:** `WAITING` (a waits_on gate unmet), `HELD` (under a hold, within its cap), `OUT-OF-SEQUENCE` (past a hold's cap:
  Andrew's card the same turn), `NEEDS-SLOT` (next step is a COO's, no lane), `LANE-DARK` (its lane is not live on this box),
  `DRIFT` / `UNREADABLE` (a source disagrees or could not be read -- raised to the owning CTO, never a pass), `IDLE`.
- **Capacity** is the laptop's 3-COO cap (Andrew-direct 2026-09-14); the next slot goes to the first project in
  `next_slot_order`.

## The compiled block dirties the tree

`--compile` rewrites a TRACKED file. Leaving it modified is harmless; commit it only with a handwritten edit or when a
committed snapshot is wanted, via `.tools/safe-commit.sh`. Never hand-edit between the markers.
