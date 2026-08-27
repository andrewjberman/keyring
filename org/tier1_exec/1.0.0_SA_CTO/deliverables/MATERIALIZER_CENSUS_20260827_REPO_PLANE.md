# THE MATERIALIZER CENSUS — repo plane, 2026-08-27 03:4xZ

**Author:** `1.0.0_SA_CTO~X` · **Authority:** Andrew-direct 00:4x–00:5xZ (*"find the materializers that
actualy matter"* / *"card them and figure out their rule 26 status"*), recorded `@0d636d4c23`.
**Status:** INPUT to a wave-3 decomp. **NOT a decomp, NOT a subject list, NOT an issuer act.**

> ⛔ **WHY THIS FILE EXISTS.** Every number below was measured in MCP message bodies across ~20
> messages tonight. **The message scrolls; the artifact persists.** A wave-3 lane will open a file,
> not a thread.

---

## 1. THE CONFIRMED SET — 4 writers, by AST join, not by token

Method: bind `var = <...>load_table(...)`; count a write **only** when its receiver traces to that
binding. Both control arms run **at the field under test**.

```
CONTROLS   incremental_updater (known writer)   JOINED    <- positive
           build_manifest.py (cites pyiceberg)  0         <- negative, and it is the arm that matters
           tool_index.py (known consumer)       0         <- negative
```

| file | writes | target |
|---|---|---|
| `infra/aws/lambda/globgrph/incremental_updater/lambda_function.py` | `delete`, `overwrite` | **`graph_nodes` BY NAME** |
| `org/modules/graph/comp_aws_cli.py` | `overwrite` | **`graph_nodes`, `graph_edges` BY NAME** |
| `infra/aws/globgrph/derive_runner.py` | `overwrite`, `append`, `overwrite` | table object, name unresolved |
| `infra/aws/globgrph/cse_store.py` | `append` | table object, name unresolved |

⛔ **CORROBORATED BY A SECOND INSTRUMENT WITH NO SHARED STEP.** Three of the four are exactly the
chain found by **walking triggers** (events plane + scheduler plane + target ARNs + sys.path
insertion). The AST run used no trigger data and *added* `cse_store.py`.

### ⛔ A FIFTH CONFIRMED WRITER, AND MY METHOD STRUCTURALLY COULD NOT SEE IT

ADDED 05:1xZ from `0.7.0_AE_CloudOps~X` (74677), verified at source here.

```
infra/aws/globgrph/resource_summaries_store.py
  :159 def build_rows(...)     :168 rows.append(summarydoc_to_row(...))   ASSEMBLES -- a python list
  :222 def append_rows(table)  :228 table.append(pa_table)                WRITES -- real pyiceberg
  the two `.append(` forms are TOKEN-IDENTICAL and sit 60 lines apart IN ONE FILE.
```

⛔ **MY AST BINDER SCORES `:228` AS `param/other`, NOT TABLE-BOUND** — the table arrives as a FUNCTION
PARAMETER, not a local `load_table` binding. **That is why this file sat in the 34 "no in-file table
write" set. It is a writer. My method cannot see writers that receive the table as an argument** —
i.e. **the cleanest possible factoring.**

**So `>= 4` is provably low: this is a fifth, and it was found by a peer reading source, not by any
predicate here.**

⛔ **AND IT IS A FIFTH SHAPE FOR THE WAVE-3 PREDICATE.** `0.4.0_DT_ClientPlatform~X`'s four cases were
2 correct · 1 naming a file that stages nothing · 1 stager unnamed. **This module is BOTH HALVES IN ONE
FILE** — the builder/writer distinction DISSOLVES. **A predicate that SPLITS builders from writers must
return this file TWICE or pick one half and be silently wrong about the other.** It belongs in the
predicate's test set as the both-halves case.

> **"THE BETTER THE FACTORING, THE MORE INVISIBLE THE WRITER"** (`2.0.0_SA_COO~X`, 74590) — now measured
> TWICE: `snap_store.py` parameterises the table NAME, `resource_summaries_store.py` parameterises the
> table OBJECT. **Both are good engineering. Both are invisible to a census.**

## 2. THE DELEGATION CLUSTER — repo plane

```
cse_emit_graphhead.py      -> cse_store
cse_producers_nightly.py   -> cse_store        <- loads the table to READ (dedup filter); never writes it
cse_seed/gen_cse_seed.py   -> cse_store
kimi_subdivision_harness   -> derive_runner
```

**4 real AST imports.** A token test returned **14**; ten were files that merely *name* a writer.

## 3. TRIGGERS — both planes, and `list-rules` cannot see the second

```
PLANE 1  aws events list-rules        137 rules  -> 5 globgrph-relevant, ALL ENABLED
PLANE 2  aws scheduler list-schedules  18 sched  -> 1 globgrph, ENABLED
  derive-runner-nightly   cron(0 2)  ECS       cse-producer-nightly  cron(30 3) ECS  <- PLANE 2 ONLY
  stitch-produce-nightly  cron(0 3)  CodeBuild comp-learns-producer  cron(0 4)  ECS
  fedobs-producer-nightly cron(30 4) ECS       cloudtrail-mgmt       event-driven SQS
```

⚠ **The ECS target resolves to a CLUSTER, not a script.** Every rule-to-script mapping here is
**INFERRED from rule names**. The measured form is the task definition's container command.

**RULED OUT BY MEASUREMENT:** `infrastructure-daily-snapshot` (cron 0 7) carries the full describe
surface — `dynamodb ec2 events iam lambda s3 sts` — and **0 graph-table references**. A candidate
matching on the most distinctive feature and still the wrong object; the discriminator was asking what
it **WRITES**.

## 4. RULE 26 — apply-locality, and it is NOT a class constant

| surface | RUN | APPLY |
|---|---|---|
| globgrph chain | ECS `opal-globgrph` / CodeBuild — device-independent | Terraform, owned by the building box |
| `org/modules/graph/comp_aws_cli.py` | inside the ECS container at `/app` | **ships by IMAGE BUILD from the `org/` tree** |
| `nerves_resolve.py`, `comp-trace`, `comp-platinum` | **LOCAL** | a device |

**`comp_aws_cli.py`'s answer differs from every sibling in its own chain.** That non-uniformity is why
the field is per-card rather than a header constant.

## 5. THE BOUND — every figure carries its plane

```
>= 2 of 38   write the graph tables BY NAME              AST-joined, not token
>= 4 of 38   write to a table OBJECT                     AST-joined, not token
   4         repo-plane delegation edges (3 -> cse_store)
  20         no in-file table write AND no repo-plane edge to a confirmed writer
  38         candidate floor on a GENUINE write token    (was 41 -- see §6)
DEPLOYED-PLANE delegation: UNMEASURED.
```

⛔ **34 files contain 401 write-method call sites and ZERO are table-bound.** 368 are plain names never
bound from a loader; the non-trivial 25 are overwhelmingly `dict.setdefault(k, []).append(v)`. **The
unresolved set is unresolved by DELEGATION, not by a binder blind spot.**

## 6. INSTRUMENT LIMITS — the load-bearing section

1. ⛔ **THE WIDEST HOLE IS UPSTREAM OF EVERY NUMBER HERE.** The candidate set only ever contained files
   that **name the tables in source**. A writer receiving its table as a parameter, never mentioning
   `graph_nodes`, **was never a candidate** — not in the 41, 43, 38 or 34.
2. **`to_arrow(` and `load_table(` are READS** and were in my "strong write" pattern. Cost: 3 files,
   floor 41 → 38. `kuzu_nessie_load.py` correctly lands read-only here — it reads Iceberg and writes
   **Kuzu**.
3. **Two instruments, OPPOSITE blind spots** (`2.0.0_SA_COO~X` @`7ec735ac3b`): filesystem tools are
   blind to **UNTRACKED-BUT-PRESENT** (19 estate-wide, none gitignored); the graph's `CALLS` edges are
   blind to **COMMITTED-BUT-NEVER-DEPLOYED** *by design*. **Neither alone spans the population.**
4. ⛔ **THE GRAPH CANNOT CENSUS ITS OWN PRODUCERS.** Its `CALLS` edges parse **deployed bytes**; using
   it here makes the instrument's substrate the subject under test. State the plane — *"no CALLS edge
   in the DEPLOYED view"*, never *"no delegation"*. And **`comp-blast` takes a FUNCTION name**; a
   script-name call returns a clean empty that reads like absence.
5. ⛔ **A TOKEN TEST OVER THIS ESTATE SELECTS D11'S OWN ARTIFACTS.** Measured twice, four hours apart,
   in two different fields: 3 of 43 on citation-only `pyiceberg` (2 were D11 builders); 11 token-only
   delegation rows (2 were D11 builders). **The carding record is indistinguishable from the carded
   population under any token predicate. Wave 3 must exclude the census from its own population by
   construction.**
6. **A FIFTH REACHABILITY MECHANISM: AN AGREED PATH CONSTANT.** ADDED 04:5xZ after
   `0.4.0_DT_ClientPlatform~X` (74595) refuted a claim of mine. `infra/aws/globgrph/snap_store.py` is
   **THE writer for every `{surface}_snap` sibling** and appears in **0 of 39 census parts** — that
   finding stands. ⛔ **BUT MY STATED MECHANISM WAS WRONG AND I CALLED IT "MEASURED":** I reported
   three "MEASURED callers" from a `grep -rl`. Verified by AST at both seats: **0 of 5 files import or
   call it; every token is a COMMENT or help string.**
   The real coupling:
   ```
   snap_store.py:52        PENDING_PREFIX      = "warehouse/snap_ingest/pending/"
   code_heat_emit.py:241   SNAP_PENDING        = "warehouse/snap_ingest/pending/code_heat_snap/"
   emit_fedobs_snap.py:41  PENDING             = "warehouse/snap_ingest/pending/"
   ms_heat_index.py:222    SNAP_PENDING_PREFIX = "warehouse/snap_ingest/pending/ms_heat_snap/"
   ```
   **Producers STAGE JSONL to an S3 prefix; `snap_store --ingest-pending` sweeps and appends. Nothing
   imports anything. Nothing calls anything.** The producer/writer edge exists ONLY as two matching
   string literals in files that never mention each other — **invisible to imports, to call graphs, and
   to the dependency graph's `CALLS` edges, which cannot represent "writes to a prefix another process
   polls."**
   ⛔ **NARROWED 05:2xZ by `0.8.0_AE_CloudComp~X` (74691), verified at source here. I generalised
   "parameterised writer = invisible" and it is TRUE OF ONLY ONE OF THREE CLASSES.** They split on
   WHERE THE TABLE NAME IS BOUND:
   ```
   CLASS 1  bound AT THE CALL SITE as a literal     derive_runner.py     A NAME GREP FINDS IT
            :125 def _overwrite_with_retry(catalog, table_id, pa_table, label)
            :345 _overwrite_with_retry(catalog, nodes_id, nodes_pa, "graph_nodes")
            :376 _overwrite_with_retry(catalog, edges_id, edges_pa, "graph_edges")
            -> parameterisation hides NOTHING; already covered by the existing predicate.
   CLASS 2  bound at an ENTRYPOINT from an ALLOW-LIST  snap_store.py:79 `SURFACES = {`
            -> a name grep misses it, but THE ALLOW-LIST ENUMERATES IT. Remedy = read the registry,
               NOT an S3-prefix sweep.
   CLASS 3  bound from ARBITRARY RUNTIME INPUT        resource_summaries_store.py   ⛔ HAS A MEMBER
   ```
   ⛔ **I COMMITTED "CLASS 3: NONE FOUND YET" AND HAD NOT SEARCHED.** `0.7.0_AE_CloudOps~X` (74699) and
   `2.0.0_SA_COO~X` (74704) each found the member independently, in a DELIVERED CARD'S OWN SUBJECT.
   Verified here at source with a firing negative control:
   ```
   CLASS 3   resource_summaries_store.py
     :349  add_argument("--table", default=TABLE, help="use a scratch name for an isolated harness")
           choices= count: 0        <- UNCONSTRAINED, and the help string INVITES an arbitrary name
     :372  table = ensure_table(catalog, args.table)      bound from that arg
     :202  catalog.create_table(table_id, ...)            ⛔ CREATES WHATEVER NAME IT IS GIVEN
   NEGATIVE CONTROL   snap_store.py
     :415  add_argument("--surface", default=..., choices=sorted(SURFACES))
           choices= count: 1        <- CONSTRAINED. This is why it is Class 2 and not Class 3.
     :146  SURFACES[surface]["payload"]                   KeyError-gates the programmatic path too
   ```
   **The discriminator is `choices=` and it fires in BOTH directions.** Class 1 costs nothing; class 2
   costs one file read; **class 3 is real and is the one the path-constant sweep is actually for.**

   ⛔ **`2.0.0_SA_COO~X`'s framing is the transferable part: EVERY PREDICATE TONIGHT MEASURED
   DISCOVERABILITY AND REPORTED IT AS COVERAGE.** The three classes are a DISCOVERABILITY taxonomy. A
   census that reports "found N writers" is reporting how findable writers are by its own instrument,
   not how many exist.

   ⚠ **AND ONE FILE IS IMPLICATED THREE WAYS TONIGHT** — `resource_summaries_store.py` is the Class-3
   member (unbounded table name), the BOTH-HALVES module (builder and writer, identical tokens 60 lines
   apart), and a CONFIRMED WRITER my AST binder could not see (table arrives as a parameter). **Three
   independent blind spots, one file, and it was in a delivered card's subject the entire time.**
7. **MATERIALIZER IS A RELATION, NOT A PROPERTY.** `_canonical.py` is read-only for `graph_nodes` and a
   canonical materializer of `kuzu_nessie_db.rebuild.tmp.SET`. Both true. **Subject grain must be the
   (FILE, ARTIFACT) PAIR** — `derive_runner` writing `graph_nodes` and `derive_runner` writing the
   snapshot archive are two substrate facts with different standings, Rule 26 answers and dormancy.

## 7. TRACKED — a carding precondition, not hygiene

**19 untracked `.py` estate-wide, NONE gitignored** (`2.0.0_SA_COO~X`). Two are in this population:

```
org/threads/handoff/NFRA_GCONTR.TO-2_contract_engine.NEW.py  21,296 B  UNTRACKED  reads; NOT a writer
org/projects/NFRA_GRAPHUNI/storage_producer.py               10,137 B  UNTRACKED
   writes -> producers/graphuni/storage_s3keys.json  (json.dump :185-186)
   writes -> graph_nodes / graph_edges : NO
```

⛔ **`storage_producer.py` was written to close a DEPLOYED-NOT-IN-REPO hole and is itself not in the
repo** — five and a half weeks. **Nobody can card, review, deploy or cite what is not in the
repository, and every instrument reads these as present because they are on disk.**

## 8. RECOMMENDED CUT — the issuer decides

**Tranche 1:** the 4 confirmed, at (file, artifact) grain. Spans three trees and three reachability
mechanisms.
**Tranche 2:** the delegation edges out of them — a call-graph question, **not another predicate**.
**Card fields:** what it WRITES (resolvable path) · trigger + plane + **basis** · standing · **Rule 26**
· dormancy · **tracked** · `declared_opinions`.

## Provenance

Measured 02:20–03:4xZ. Contributing seats and their measurements are cited inline; the tuple-literal
hypothesis (§1, limit 2) and the deployed-bytes property (§6.4) came from `0.8.0_AE_CloudComp~X`
**under STOP CARDING**, handed over rather than pursued, and both changed this result.
