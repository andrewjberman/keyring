---
name: charter
description: Authors a project charter / PRD framework in the Tier-0 house format, for 0.0.0_AB_MSTR to originate work that Tier 1 (CTO/COO) then decomposes and executes. Invoked from within a /govern cycle once a candidate move has been ledgered. Produces a structured charter — objective, scope, non-goals, workstream decomposition, TO candidates, success signals, the Tier-1 owner, and an explicit "not authorized" section bounding what downstream agents may NOT do. Every charter traces to a Directive and an originating ledger entry; it never grants authority beyond its Directive.
---

# /charter — Tier-0 charter / PRD-framework authoring

How MSTR turns a ledgered decision into a charter Tier 1 can act on. `/govern`
decides *whether* to originate; `/charter` defines *how* the charter is written.
Kept standalone so the format is consistent and testable, and so the `/govern`
loop stays inspectable.

## When to invoke

- From inside a `/govern` cycle (Step 4), after the originating decision has its
  `LD-NNNN` ledger entry. A charter is itself an S1 (or S2 if it redirects an
  active Tier-1 lane) — it must already be ledgered before `/charter` runs.
- Never as a way to originate work *around* the ledger — the `LD` comes first.

## What it produces

A charter document with this frontmatter and structure:

```
charter_id:           CH-NNNN
directive_refs:       [D-NNN]          # the mandate this serves
originating_ld:       LD-NNNN          # the /govern decision that authorized it
stakes_class:         S1 | S2          # the charter act itself
tier1_owner:          1.0.0_SA_CTO | 2.0.0_SA_COO   # who decomposes + runs it
ratification_required: false | true   # true if any workstream is S3/S4
```

Body sections:

- **Objective** — what the charter is for, traced to its Directive.
- **Current state** — the empirical situation, evidence-cited (Art. VIII:
  claimed vs verified separated).
- **Scope** — what is in.
- **Non-goals** — what is explicitly OUT. Required, never empty — the cheapest
  drift control.
- **Workstreams** — the decomposition into coherent units of work.
- **TO candidates** — concrete task-order seeds for Tier 1 to author.
- **Success signals** — how completion is recognized (verifiable, not asserted).
- **Open questions** — what is unresolved and who must resolve it.
- **NOT AUTHORIZED** — an explicit statement of what this charter does **not**
  permit downstream agents to do: it does not authorize spend, irreversible or
  production-mutating actions, or scope beyond the Directive. Anything an
  executing agent reads here as out-of-bounds stays out-of-bounds unless
  separately ratified.

## Rules

- A charter **never grants authority beyond its `directive_refs`**. It is a
  decomposition of an existing mandate, not a new one (Constitution Art. II, XIII).
- A charter is handed to **Tier 1 only** (Constitution Art. VI). Tier 1 may
  accept, modify, or reject it on operational grounds — record the receipt.
- If any workstream would require an S3/S4 action, the charter sets
  `ratification_required: true` and that workstream cannot start until ratified.
- The charter is committed as part of the `/govern` cycle; the `mstr-ledger-check`
  hook requires its originating `LD` in the same commit.

## Notes

- A charter is a *proposal of structure*, not an instruction to execute gated
  work. Execution authority still flows through the Stakes Matrix and Tier 1.
- Design + law: `org/tier0/README.md`, `CONSTITUTION.md` Art. II / VI / XIII.
