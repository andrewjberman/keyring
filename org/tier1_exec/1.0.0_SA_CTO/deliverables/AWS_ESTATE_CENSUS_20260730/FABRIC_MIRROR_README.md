# FABRIC MIRROR of the world-model program's fabric-consumed artifacts

**Why this exists:** the program's canonical home is `C:\Users\AndrewBerman\Desktop\OPAL_WORLD_MODEL\`
(its own git repo, no remote). Agents working from a GIT CLONE of ajb_workspace -- rather than from
this machine's filesystem -- CANNOT READ IT. 3.0.0_SA_CVO hit this twice trying to verify
`RESOLVER_DEFROST_DESIGN.md @ee35d1c`, and 0.7.0_AE_CloudOps~B is about to build the semantics half
of a design whose structural companion they could not open.

**So the FABRIC-CONSUMED subset is mirrored here** (pushed to CLOUD, readable by every agent):

| File | What consumes it |
|---|---|
| `RESOLVER_DEFROST_DESIGN.md` | ~B's estate-report pipeline (structural companion); CVO approval |
| `TRIGGER_ASSESSMENT_PROTOCOL.md` | the 0.7.0~* TAP lanes (T1-T7 battery, P1-P17 checklist, chunking) |
| `ONTOLOGY_CLASSES.md` | the ontology / NFRA_VELOCITY offtake |
| `RULINGS_LEDGER.jsonl` | TAP's T6 destination-ruling JOIN; the enrichment pass |
| `SEMANTIC_NOTES_{s3_buckets,ddb_tables}.md` | Andrew's per-resource verbatims -- the semantic rung |
| `INVESTIGATION_QUEUE.md` | 0.7.0's kill-list mandate (Q-1..Q-32) |

**MIRROR DISCIPLINE -- read this before trusting a copy.** The Desktop repo is CANONICAL; this is a
COPY, and a copy is a frozen reference the moment it is written. That is the exact class the cardinal
rule forbids depending on (`docs/doctrine/CHECK_LIVE_NOT_FROZEN.md`: *"we can never ever have
dependencies on frozen maps"*, Andrew-direct 2026-07-30). Therefore:
- **This mirror is refreshed by an explicit CTO copy step, and its vintage is its commit date.**
  Check `git log -1` on the file you are reading; if the canonical has moved, it is stale.
- **Do not compute from it. Read it.** Anything deriving state must go to the canonical or to live
  instruments.
- The real fix is a remote on the Desktop repo -- OPEN AT ANDREW. Until then this mirror is the
  fabric's only read path, with its staleness stated rather than hidden.
