---
name: prune-quant
description: The MECHANISM half of the prune pair (sibling /prune-qual): for a script, function, pipeline, trigger, record file or running process, how to simplify without losing material value -- a KEEP/CUT/DEFER report grounded in a consumer census and value ranking, never silent deletion. Deletion beats redirection beats sharding beats compilation. Any agent; report-only, execution routes to the owner's lane.
---

# /prune-quant — simplify a MECHANISM without losing material value

**The pair:** `/prune-quant` is for things that RUN (code, pipelines, triggers, writers, files as
machinery). `/prune-qual` is for things that are READ (PRDs, designs, docs, rules). A target with
both natures (a skill, a gated process) may take both passes — quant on its machinery, qual on its
text.

**Invocation:** `/prune-quant <target>` — a script or function, a pipeline, a trigger/schedule, a
record/log file, a process. Output is a **prune report**, not an edit: analysis here,
execution through the owner's normal lane. (A verifier may run this on anything; pruning your own
lane's artifact still produces the report first — the report IS the reviewable unit.)

## The method — in order, because each step can end the work early

**1. CONSUMER CENSUS FIRST.** Who actually reads/calls/depends on this — by MACHINE (grep for
parsers, importers, subscribers; check the graph) and by HUMAN (who has cited it; when last)?
State the census denominator (what trees/systems you searched) and the residual (what you could
not see — other hosts, other clones, out-of-tree tooling). *A thing nothing consumes converts
redirect-designs into delete-designs — the highest-value single finding this skill produces.*
⚠ **"Unused" and "unobserved" are different verdicts.** An instrument's silence is not a deletion
warrant (the comp-iam lesson: a grant can be REQUIRED and invisible at every call site). For each
CUT candidate, say which you have: *evidenced-unused* (census found zero consumers AND the
mechanism is observable) vs *unobserved* (your instruments cannot see its consumers — DEFER, name
the instrument gap).

**2. ASK WHAT EACH PART IS FOR — the value axis, not the build axis.** Classify every component by
the cost of losing it (accountability record / correctness / convenience / decoration), not by how
it is written or how much effort it took. Two same-shaped parts can classify oppositely (a
governance audit log vs an operational telemetry file: identical append-only shape, opposite
durability requirements — measured 2026-07-29).

**3. SURFACE VALUE QUESTIONS TO THE OWNER — never guess silently.** Where material value is a
judgment call, the report carries the question, one line, answerable with yes/no ("is the per-run
telemetry a record you need to keep, or convenience?"). The owner's ranking dissolves designs that
analysis alone cannot ("the only one I really care about" retired two custody designs in one
sentence). An unasked value question becomes a silently-kept component forever.

**4. PREFER, IN ORDER: DELETE > SIMPLIFY-IN-PLACE > REDIRECT > SHARD > COMPILE/WRAP.** Each step
right of DELETE is machinery that must itself be maintained, verified, and eventually pruned.
**Unbuilt is the best outcome available** — a prune that replaces one mechanism with two lighter
ones has usually failed. (Prose targets → `/prune-qual`; its act-test is the same instinct applied
to sentences.)

**5. THE TWO SAFETY CHECKS BEFORE ANY CUT IS RECOMMENDED:**
- **Custody:** does removing this leave some record/capability with SINGLE-COPY custody or a sole
  carrier? If yes, the cut is PRECONDITIONED on the custody landing first — custody first, cut
  second, never overlapping, never reversed (the window between is a period where the record is
  one command from gone).
- **Retirement evidence:** a cut IS a retirement — state what would prove the thing is actually
  dead after the cut (per-kind: a write → next-cycle non-advance; a trigger → applied-plane absent
  + the window passes; a function → zero references AND zero dynamic invocation paths), not just
  that the replacement/remainder works.

**6. SCOPE GUARD — say what the action targets, every time.** When the prune names a FILE and an
ACTION, state explicitly whether the action targets the file or its CONTENTS/writers ("delete the
auto-append; THE FILE IS PRESERVED"). An instruction whose plain reading contains its own inverse
is a measured recurring class (twice on 2026-07-29 alone). The report's CUT lines must be
un-misreadable by a fresh implementer who has only the report.

## Report format (the deliverable)

```
# PRUNE: <target>   (census denominator: <what was searched>; residual: <what wasn't>)
| # | component | verdict | evidence | value-class |
KEEP  <part>    -- <why it is load-bearing, cited>
CUT   <part>    -- <evidenced-unused how; scope guard: targets X, preserves Y; retirement proof>
DEFER <part>    -- <the unobserved gap or the owner question, stated in one line>
OWNER QUESTIONS: <the one-line value calls only the owner can make>
NET: <N mechanisms -> M; what is now unbuilt/unmaintained>
```

## Notes
- Report-only. Execution rides the owner's lane, normal gates (never-widen on served output,
  RETIRECOND ledger field when it lands, safe-commit).
- Prune the prune: if the report is longer than the thing it prunes, it has failed step 4.
- Provenance: distilled from the 2026-07-29 comp-log arc (reader census -> value ranking -> scope
  guard; record @ecac977a3b + the disposition chain in the same file).
