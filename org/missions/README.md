# org/missions/ — the mission register tree

**Owner: `0.0.0_AB_MSTR`.** Taxonomy + attribution index: `org/tier0/missions.yaml`.
Decision record: `org/tier0/ledger/LD-0341.md`.

```
org/missions/{GROUP}/{SUB_GROUP}/
    commits.jsonl    MACHINE   one JSON record per attributed commit
    state.yaml       HUMAN     stance · frontier · blocked-on · attach · holes
    execsum.yaml     MSTR      prose + the commit it was written against
```

Groups: `PORTAL` · `INFRASTRUCTURE` · `DEBT` · `EXTERNAL`.

---

## How each file is compiled and maintained

| file | written by | when | overwritten? |
|---|---|---|---|
| `commits.jsonl` | `comp-missions emit` | every emit | **YES — regenerated wholesale from git** |
| `state.yaml` | MSTR (from Tier-1 returns / the corpus) | when state actually changes | **NEVER by the machine** |
| `execsum.yaml` | MSTR writes `prose`; machine refreshes `anchor_*` + `activity` | prose on demand, anchors every emit | **prose never; anchors always** |

**`commits.jsonl` is regenerated, not appended.** Git is the source of truth, so a rebuild can never
drift from the repo. Never hand-edit it — an edit is erased on the next emit, silently, which is the
worst kind of erasure.

**`state.yaml` is the machine's hard boundary.**

> **The machine cannot write a stance.** `BUILT` anchors on an **exercised run**, and a commit scanner
> structurally cannot see a run. This was proven on 2026-07-28: a `BUILT` scored off a producer
> *landing* was two hours stale and had to be corrected off the run. **Commit activity is not
> progress** — it tells you what was touched, never whether it works.

**`execsum.yaml` carries `prose_written_against` and `prose_stale`.** When a commit lands after the
prose was written, `prose_stale: true` — the prose is not deleted, it is **labelled**. A summary that
silently ages is how a register starts lying; one that says "I am behind" is still useful.

## Where the content comes from

Andrew-direct: *"largely be attained via the corpus (logs, commits, etc)"*, and it must stay **light**.

1. **Commits** — attribution is automatic. Precedence: a `Mission:` trailer (authoritative) →
   path globs from `missions.yaml` (advisory) → `UNMAPPED`. `AMBIGUOUS` (>1 sub-group) is
   **reported, never tie-broken**; governance/meta is excluded from the denominator.
2. **Session logs + deliverables + PRDs** — read by MSTR when a stance needs re-grounding.
3. **Tier-1 agents** — asked only when the corpus cannot answer it. **They are not asked to
   maintain anything here.** The five-field ask (ATTACH · HOLES · STANCE · FRONTIER · BLOCKED-ON)
   is a pull, not an obligation.

## Cadence

`comp-missions emit` at MSTR startup and after any substantive wave. That is the whole ceremony.
No cron, no gate, no hook on anybody else's commit path.

## The field that earns the tree

**`holes`** — live work covered by **no project code**. The project registry answers *what exists*;
only this layer answers *what is happening that nothing tracks*. Found so far, each positive-controlled:

- `NFRA_TOOLUNIFY` — 109 commits, 113 doc files, **no project JSON**
- `MDPF_CHANNEL_INDEPENDENCE` — PRD'd, cited as law, drove a P0, **no JSON, no registry row**
- **The BD-replacement total-return build** — CRO research delivered, **no project registered**; a
  TWR keyword search over all 281 project JSONs returns **zero active** projects
- **The recurring 49F Schwab silver conversion** — a codified 7-step procedure with **no owning
  project**; its only registry mention is a `cancelled` code whose cancellation basis was retracted
- `OPAL_SCHEDULE` / `OPAL_ALERTS` — briefed and measured against live AWS, **never registered**
