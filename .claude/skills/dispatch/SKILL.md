---
name: dispatch
description: The COO's L6-L7 act under spine v3 -- turn a ratified decomposition into ONE issuance covering every cell, spawn the worker slots, drain them, and end the round with the COO's single message to the CTO. `/dispatch <CODE>` runs the whole limb; `/dispatch <CODE> --plan` renders the chain read and the fan-out and commits nothing; `/dispatch <CODE> --drain` re-enters an issuance already spawned. The spawn IS the GO -- no broker message carries it. 2.0.0_SA_COO only (base or ~lane).
---

# /dispatch — one issuance, N workers, one drain, one message

Spec: `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` L6 (:149-183) and L7 (:184-232). This skill is the
COO's half of those two limbs and adds nothing to them. Where this file and the spine disagree, **the
spine wins and this file is the defect.**

⛔ **2.0.0_SA_COO ONLY** (base or `~lane`). Lane `TREE_COO` refuses any other author's issuance, so
another seat running this produces a refused commit, not a dispatch. Halt at Step 0 if you are not COO.

---

## Step 0 — Refuse early, on the four things that make an issuance illegal

Read, in this order, and stop on the first that fails:

1. **The decomposition is RATIFIED and the round is open.** `dep_stage` reads `DECOMP` or `ROUND_CLOSE`
   on the project row. Any other stage means someone else holds the limb.
2. **You are the COO** (`$OPAL_AGENT_SERIAL`, or the session serial file — never `.agent_context`).
3. **Every cell has text.** A cell you cannot inline is a cell you cannot issue.
4. **The spec is FROZEN.** Mid-round the decomposition does not move. A cell that looks wrong is a
   surprise row, never an edit.

## Step 1 — The chain read: M, then N, then K

**M is measured, not chosen.** M = the number of dependency-independent chains in the decomposition's
edge set. Two cells joined by an edge are one chain; a cell with no edge is a chain of one.

**N is chosen and defended.** N = workers spawned. **K = the cap you state; the default is eight**, and a
larger K travels with its reason on the same line.

```
fanout: N of M chains, cap K, reason: <one line>
```

⛔ **This line is DATA in the issuance commit message, not prose.** It is the dispatch record; nothing
else records the fan-out.

**The queue rule, which decides N:** two task orders on one chain belong to ONE worker's queue, because
the second depends on the first. Two chains may take two workers. **So N is bounded above by M** — asking
for more workers than there are independent chains buys nothing and serialises anyway.

⛔ **NO CELL IS LEFT FOR A LATER ROUND.** The issuance covers the whole decomposition. A later round
exists only when the CTO's round-N analysis sends work back. If you cannot cover a cell, you are not
ready to issue.

## Step 2 — Cut the task orders: two faces, one file

One task order per cell at
`org/missions/D<n>/<MACRO>/<CODE>/task-orders/<CODE>.TO-<id>.<slug>.md`.

**THE WORKER FACE IS THE WHOLE OF THE WORKER'S CONTEXT.** It starts with fresh context and gets nothing
else — no law you did not inline, no message, no answer to a question, because it cannot ask one.

> ⛔ **A task order whose worker face is not sufficient ON ITS OWN is DEFECTIVE AT L6, and it is never
> patched by a message.** There is no channel to patch it through: the worker has no broker tool. The
> defect surfaces as a surprise row hours later, or as silence.

The worker face carries, and a face missing any of these is not cut:

| element | rule |
|---|---|
| `<decomp_ref>` + `<owned_cells>` | delimited list, and the **text of every owned cell inlined** |
| surfaces and bounds | what it may read and write, and what it may not |
| battery findings | inlined **where they touch the owned cells**, not the whole battery |
| `<paths>` | every file it reads or writes, **absolute from the root** |
| `<proof_of_spec>` | **one clause per criterion** — see the refusal below |
| `<issued_to>` | `0.9.0_WK_<CODE>~<n>`, `~<n>` = the slot, reused across that slot's queue |

**The record face never travels.** Status, seating, the preflight's disposition narrative, the authority
chain, the provenance: they stay in the file for the gates and are not given to the worker.

⛔ **THREE REFUSALS AT THE CUT, all yours, none automatic yet** (they bind by reading, spine s.4):
- **A criterion that conjoins clauses is REFUSED.** Split it. One clause, one criterion.
- **A mechanical criterion without its `<invocation>` AND its `<expect>` is REFUSED** — its pass must be
  decided by a MATCH, not by the worker's opinion.
- **A judgment criterion is flagged `judgment="true"`, is never self-graded, and carries no verdict.**
  The CVO grades it at L9. A judgment row arriving with `PASS` on it is the failure this flag prevents.

## Step 3 — ONE issuance commit

Every task order, plus the `dep_stage` flip to `EXECUTING`, in **ONE commit**:

```bash
export OPAL_AGENT_SERIAL=2.0.0_SA_COO
bash .tools/safe-commit.sh --author "2.0.0_SA_COO <2.0.0_SA_COO@opal.agent>" \
  -F <msgfile> -- <every task order> <project.json>
```

The message carries the `fanout:` line. `<msgfile>` is written with the **Write tool**, never a heredoc
(rule 14a: a shell-built message file re-opens the injection one step earlier).

**Gates that fire here:** `to-proof-of-spec-check.sh` (no `<proof_of_spec>` or no `<decomp_ref>` → refuse),
`.tools/to-pipeline-gate.py` (absent project row, `dep_stage`/`fabric` off enum, incomplete preflight, PRD
failing L2/L4, row and folder disagreeing, or `<issued_to>` naming a Tier-0/Tier-1 seat → refuse; override
lands in `org/to-pipeline-override-audit.log`), and lane `TREE_COO`.

⚠ **THE FLIP AND THE ROW LANE — RESOLVED, and the way it was got wrong first is the lesson.** The spine
(:410-412) says the row lane admits only the CTO to `project.json`, so an issuance carrying the flip is
refused until the grantor widens it. **That grant LANDED at `7668568ed6` (LD-0534):** `TREE_PROJECT_ROW`
now admits `2.0.0_SA_COO`, verified by the grantor on the pre-edit bytes (REFUSED, rc=1) against the
committed bytes (PERMIT, rc=0). The flip should pass; you do not self-grant, and if it ever refuses the
CTO flips the row in the same window.

⛔ **THE TRAP THAT COST THIS CLAUSE A RETRACTION — READ HEAD WITH `git show`, NEVER THE PATH.** Before
that grant landed, this seat exercised `check_agent()` against `.owned-paths.yaml` **by path**, got
PERMIT, and reported it *"at HEAD"* — concluding the grant was unnecessary. It was reading the
**WORKTREE**, which already carried the grantor's uncommitted edit. **The HEAD bytes refused.** The
controls were fine and the negative control was real; the **VINTAGE was asserted and never measured**,
which is Rule 22's GRAIN limb — discrimination passes cleanly inside a wrong grain, and every arm agrees
about the wrong object. On a tree this dirty, an unlanded edit by another seat is the normal case.

```bash
# WRONG on a dirty tree -- reads whoever's uncommitted edit is sitting there
python -c "...load_yaml('.owned-paths.yaml')..."
# RIGHT -- the record, at a stated vintage
git show HEAD:.owned-paths.yaml > "$tmp"   # then resolve against "$tmp"
```

**Still true and still worth doing: MEASURE BEFORE YOU OVERRIDE.** Exercise the checker on your serial
and the path, with a seat that should REFUSE as the negative control, **on bytes you pulled with
`git show`**. An override taken against a gate that would have passed writes an audit row asserting a
refusal that never happened.

## Step 4 — Spawn: the spawn IS the GO

Per worker slot, the harness subagent call with **`subagent_type: "worker"`** and
**`isolation: "worktree"`**. The prompt is **the worker face of that slot's FIRST task order, verbatim**,
plus the L7 identity line naming its serial.

⛔ **NO BROKER MESSAGE CARRIES A GO, AND NO INBOX RECEIVES ONE.** A worker cannot register, send or
receive. If you find yourself composing a message to a worker, the thing you are trying to say belonged
in the worker face and the task order is defective.

⛔ **Do NOT use `/mstr-spawn`.** That provisions a SEAT. A worker is a subagent and is registered nowhere.

Model: the cheaper one, unless the preflight marks the cell hard and you override **per task order**.

## Step 5 — The drain, per terminal task order

When a task order goes terminal:

1. **Read the worker's final report AND the proof-of-spec instance.** Both. The report is the worker's
   account; the instance is the artifact the checker graded.
2. **Merge only when the instance is VALID.** `pull-merge, NEVER rebase` (NEVER#3 — `CLOUD` is shared).
3. **Remove the worktree and its branch EXPLICITLY.** Not left for later.
4. **Read every row the branch carries.** An `ARMED` row whose `disarm_owner` is dark is **yours to
   re-seat, because you are the seat that spawns.** One you cannot seat rides the drain-end read.
5. **Hand the next task order by CONTINUING the same subagent**, context intact. **No respawn, no cold
   start** — a respawned worker re-reads its whole face and loses what it learned.

**A worker with an empty queue ends. A worker that dies mid-task-order leaves a branch:** merge it if its
instance is valid, otherwise discard it and re-dispatch that task order to a fresh slot.

⛔ **A `BLOCKING` row is read in the worker's final report of that task order.** An `OBSERVATION` never
interrupts.

## Step 6 — The drain-end read: your ONE message of the round

**The COO sends nothing for the whole round until this.** Then one message, to `1.0.0_SA_CTO`, carrying:

- the **CVO's watermark against the channel's row count**, and
- **every armed row whose owner you could not seat.**

⛔ **This is the ONLY carrier for an armed row with a dead owner.** A worker cannot send; the CVO's one
send is the slug; under v3.0 such a row had no carrier at all and sat dark. That gap is why v3.1 exists
(specimen: NFRA_CLDGRPH S26/S27/S28 with the `~A` team down).

---

## Cost, and where this does not apply

**COST:** the chain read (Step 1) and the coverage check (Step 2) are the only additions to what cutting
task orders already costs, and both are read-only against a decomposition already in hand.

**NON-APPLICATION:** a project with no tree home (use the flat protocol); a NEW project (those enter at
`/brief-create` or `/endpoint --forward`, never here); a midstream pickup where the limb is not L6 (that
is `/canonical-flow`); and a single-cell decomposition, where M = N = 1 and the fan-out line still gets
written because the dispatch record is the only place the fan-out is recorded.

**`--plan`** renders the chain read, the fan-out line and the coverage table, and **commits nothing** —
use it when N is arguable. **`--drain`** re-enters Step 5 for an issuance already spawned, for the case
where the COO session turned over mid-round.
