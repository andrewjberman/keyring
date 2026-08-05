# P8 COLD DESCENT — comp-pipescript — plus the generalist-design finding from anatomy-main

**Author:** `3.0.0_SA_CVO~B` · **Window:** 2026-08-05 ~1540–1610Z · **archetype:** VALIDATE
**secondary:** EXPLORE, DIAGNOSE
**Authority:** Andrew-direct GO at my terminal ~1540Z (recorded + broadcast to MSTR/CTO/COO,
`20260805T154138Z`). Assignment half: CVO base split record `@7a3e7117d`.

---

## CONTAMINATION DECLARATION (required per `@9e0003473`)

**comp-pipescript: NONE.** I had read no dial record, no source, and no prior analysis of this tool
before the descent below. CVO base's 08-05 log — which `org/XXX.md` Step 2 obliged me to read at
startup — discusses `comp-heat` and `comp-iam` in detail and **does not mention comp-pipescript**.
That absence is why I picked this tool: I picked around my own burn, not around difficulty.

I did **not** open `DIAL_RECORD_comp-pipescript` or any sibling dial record before running the
descent. Everything in §1 comes from the tools_index/manifest doc surface plus exercise.

---

## 1. THE DESCENT — docs only, then a real task

**Doc surface read (the whole of it):** `graph-call-manifest.yaml` entries
`trace.pipeline.gold_dag:290-300`, `pipeline.pipescript.deployed_match:437-448`,
`pipeline.pipescript.postdeps_before_adhoc_run:516-524`, and the `tools_index` one-liner `:1470`.

### F-1 — THE DOCUMENTED CANONICAL CALL DOES NOT RUN. `rc=2`, first try, verbatim.

`:292` documents the call as:

```
comp-pipescript <io|dag|chain|feeds|consumers|deployed|overlap> <script>
```

Typed verbatim against a real gold script, that is **`rc=2 REFUSED`** — `--pipeline/-p` is
required. The requirement is real and correct (07-30, Andrew-direct, killed a silent bd-gold
default that returned clean zeros for other trees). **The doc never followed the fix.** A cold
reader's first action fails, and the canonical_call field — the one field whose entire job is to be
copy-pasteable — is the field that is wrong.

*This is the same shape as the `/watcher` `/c/` literal and the `--force` scope line: the fix landed
on the mechanism and not on the record an agent reads first.*

### F-2 — THE ROSTER GAP, MEASURED. The tool sees **52.6%** of `data/` scripts and **7.7%** of the repo.

Denominators re-derived live, exclusions named (dependency bundles: `layers/`, `site-packages`,
known package dirs — 1,541 files excluded from 4,961 tracked `.py`).

| universe | count | tool sees |
|---|---:|---:|
| comp-pipescript's universe (4 trees × gold) | 262 | — |
| all `data/*/scripts/**.py` (any tree, any layer) | 498 | **52.6%** |
| all first-party `.py` in the repo | 3,420 | **7.7%** |

`--pipeline` accepts exactly: `bd-gold, inf-gold, bd-silver, inf-silver, bd-bronze, inf-bronze,
cot-bronze, inf-manual-api, mdpf, cot-gold, cot-silver, cot, all, bd, inf`.

**Script trees on disk that are INVISIBLE to the tool** — every one refuses with `rc=2` on its own
name:

| tree | script `.py` | note |
|---|---:|---|
| `data/assets` | **77** | **OPAL_ASSETS — the monolith.** CLAUDE.md Rule 13 names `data/assets/scripts/{gold,silver}` as a SHARED repo home that **DOES deploy** under the S3-membership guard |
| `data/smartx` | 31 | |
| `data/seeking-alpha` | 14 | |
| `data/etfs` | 5 | live month-end email trigger (MEMORY.md) |
| `data/demo` | 4 | |
| `data/yang_pkl` | 1 | |

**`data/assets` is the sharp one: it is DEPLOYABLE but not ANALYZABLE.** The deploy rail knows the
tree; the IO rail does not. A DS agent is obliged by XXX.md to run `comp-pipescript io` on every gold
script they touch, and for 77 of them **that obligation cannot be discharged at all.**

Andrew's framing — *"bound to a handful of gold pipelines"* — is exact, and it is
**a-predicate-is-not-a-roster** (CTO 08-04) landing on a second tool. It also recasts the 07-30
change: making `--pipeline` mandatory correctly killed the silent default, but it **hardened the
roster premise rather than removing it.** A correct fix inside a wrong frame.

### F-3 — THE FALSE-CLEAN GUARD HAS A HOLE THE SIZE OF THE ROSTER. `rc=0`, all-zero summary.

`deployed` on an out-of-universe script (`data/assets/scripts/gold/build_cottonwood_interpolated_backfill.py`)
auto-detects `mdpf`, prints one `not-in-tree` row, and returns:

```
  [mdpf:assets_gold] build_cottonwood_interpolated_backfill.py    not-in-tree
  Summary: 0 MATCH, 0 STALE, 0 MISSING_ON_S3, 0 LOCAL_MISSING, 0 TIMEOUT, 0 AWS_UNREACHABLE, 0 UNCOVERED, 0 AUX-DRIFT
```

**`rc=0`.** `not-in-tree` is counted in **no** summary counter — including `UNCOVERED`, the counter
built specifically so that "tool-blindness is NEVER countable as cleanliness" (`:448`, the tool's own
false-clean guard). **The guard covers the prefix-miss case and not the roster-miss case**, so the
one shape the generalist mandate is about is the one shape that slips it.

**Positive control (separate invocation):** in-universe, the same subcommand prints
`1 MATCH ... All checked scripts are up-to-date on S3.` The zeros are anomalous, not the house style.

This is precisely CVO base's standing rule — *a tool feeding a stratum must distinguish "nothing to
report" from "I was pointed at the wrong universe"* — failing in the direction that reads clean.

### F-4 — 10 of 13 subcommands are undocumented.

`tools_index` declares `io, dag, chain, feeds, consumers, deployed, postdeps, overlap, stats, inject,
postmerge-cols, shadow-detect, skipgate`. Manifest entries exist for **three** (`io`, `deployed`,
`postdeps`). No `use_case`, no `anti_pattern`, no canonical_call for the other ten. `shadow-detect`
is notable given the 08-04 shadow veto — an undocumented subcommand whose name maps onto a standing
sovereign prohibition.

### Descent self-corrections (recorded because the method is the deliverable)

1. I read `rc=0` off a `| head -20` pipeline — that was **head's** exit code. Re-measured unpiped:
   the tool is honest, `rc=2`. *The retrieval, not the tool, was the defect.*
2. My first out-of-universe probe hit a `__pycache__` directory, not a `.py`. Re-ran against a real
   file before resting F-3 on it.

---

## 2. anatomy-main — what is actually in there, and the part that does NOT transfer

Per Andrew's pointer. **Naming note:** the tools are `corp_find.py` / `corp_read.py` /
`corp_write.py` — **underscores, not hyphens**; a hyphen search returns nothing (positive control:
1,823 index lines contain `find|read|write`, so the zero was a real absence of that *spelling*, not a
broken search).

| artifact | path | what it is |
|---|---|---|
| `corp` | `.tools/fabric/corp` | the PULL tool: *"where does the change for this issue live?"* → ranked files + anchors |
| `corp_write.py` | `infra/corp/` + `infra/models/layer1_gbm/` | issue → ranked files **to EDIT**. 3 stages: L0 deterministic reach → L1 per-repo CatBoost → L2 qwen3-coder:30b rerank |
| `corp_find.py` | `infra/models/layer2_slm/` | SLM-backed candidate finder |
| `corp_read.py` | `infra/behavioral/` | read-efficiency pipeline (+ `_server`, `_hud`, `_params`) |
| `corp_grep.py` / `corp_glob.py` | `infra/corp/` | **native grep/glob + a deterministic grade on every hit**, grade-sorted, reject-first |
| `corp_hooks.py` | `infra/corp/` | `Context(issue, build_dir, clone_dir)` — **ONE graded universe per (issue, build), computed once; grep/glob are thin views over it** |
| `corp_localize.py` | `infra/corp_localize/` | the localization engine |
| `corpgraph_schema.py` | `infra/aws/corpgraph/serving/falkordb/` | property-graph schema. **STUB / queued, not wired to a live FalkorDB** |

### ⛔ THE HALF THAT MUST NOT BE RECYCLED, AND IT IS THE HALF THAT SHARES THE NAMES

**`corp_write` does not mean "what does this script write."** It means *"given an issue, rank the
files a human should edit."* `corp_read` is not "what does this script read" — it is a read-efficiency
pipeline for an agent. **The names collide with comp-pipescript's vocabulary and the semantics do
not.**

The two questions differ in kind:

| | comp-pipescript `io` | anatomy `corp_write` |
|---|---|---|
| question | what artifacts does this script read/write | which files should I edit for this issue |
| answer type | **a fact** (static dataflow) | **a ranking** (probabilistic retrieval) |
| correct output | complete, or an honest refusal | top-k, with recall@k as the metric |
| failure mode | a missing edge is a **wrong answer** | a missing file is a **lower score** |

**Porting the ML ranking stack into a dataflow tool would replace a fact with a guess and keep the
fact's interface.** Rule 22's reserved words apply: a CatBoost+SLM rank cannot ground a
`source-confirmed` IO claim. `comp-pipescript io` is consumed by a *deploy-gate obligation* (XXX.md
per-role minimums) — a ranked guess there is strictly worse than today's honest `rc=2`, because
today's refusal is at least legible as a refusal. **This is the "confident wrong insight" hazard CVO
base named, arriving through the recycling channel rather than through the strata.**

### ✅ THE HALF THAT TRANSFERS — and it is the architecture, not the models

1. **`Context` = ONE derived universe per (repo, build), computed once; the verbs are thin views over
   it.** This is the direct structural answer to F-2: the universe is **derived from the clone**, not
   enumerated in an argparse `choices` list. No roster exists to go stale.
2. **`corpgraph_schema.NODES/EDGES` already contains exactly the edges a script-IO generalist needs**
   — `File`/`Symbol` nodes; `CONTAINS`, `IMPORTS`, `CALLS`, and critically **`READS` / `WRITES`
   (labelled "dataflow" in the schema's own comment)**. It is language-level and repo-agnostic. It is
   also **a declared STUB** — so this is a design to adopt, not a running system to import.
3. **`corp_grep` / `corp_glob` = universal primitive + graded overlay.** Our `comp-grep`/`comp-glob`
   already mirror this shape (on-rails search carrying dependency context), which is evidence the
   pattern ports into our estate rather than a hope that it might.
4. **The reject-first grade ladder** (`HEAD / SURFACED / REL / CONFIG / TEST / COLD`) — every result
   graded, **uncapped**, nothing silently dropped. That is the anti-false-clean discipline F-3 wants,
   expressed as an output contract.

---

## 3. RECOMMENDATION (P1) — derive the universe; keep the answer a fact

**For CTO (architecture) — recommend, do not draft:**

**R-1 (P1).** Replace the `--pipeline {…}` roster with a **re-derived predicate over the repo**: a
script is in-universe if it is a first-party `.py` under a `scripts/` tree (or, generalized, any
first-party `.py`), with the tree/firm resolved **from the path**, not from an allowlist. The 07-30
no-silent-default ruling is *preserved and strengthened* — it stops being "name a roster member" and
becomes "the tool tells you which tree it resolved, and refuses when it genuinely cannot."

**R-2 (P1).** Adopt the `corpgraph` SEMANTIC subset (`File`/`Symbol`, `IMPORTS`/`CALLS`/`READS`/
`WRITES`) as comp-pipescript's IO backing, derived by **deterministic AST** — the same substrate
discipline as `census_substrate.py` (`@05144db01d`), which already proved the descriptor-row scaling
thesis in ~25 lines for `comp-lambdamap`. **Do not import anatomy's L1/L2 models.**

**R-3 (P0, and it is cheap).** `not-in-tree` must be **counted and must move `rc`**. A row the tool
could not place is the definition of tool-blindness, and `:448` already declares blindness
non-countable-as-clean. Today it is neither counted nor loud. This is a small fix and it closes a
live false-clean surface *before* any generalization work lands.

**R-4 (P1).** Fix `canonical_call:292` to carry `--pipeline`, and file manifest entries for the ten
undocumented subcommands — or retire the ones that are dead. **A subcommand nobody documented is a
subcommand nobody can P8.**

**For COO (contract surface):** if the universe generalizes, the XXX.md per-role minimums and the
CLAUDE.md trigger table that mandate `--pipeline <tree>` must move with it. Flagged early
(`20260805T154544Z`) so it is not discovered as breakage. **Not proposing the edit — it is your
surface.**

**Naming act, surfaced not resolved (Andrew):** F2 comp-pipescript universe — the declare-now landed
in the F1 guard; the WIDEN rides the typed-AST PRD. This descent supplies the measured denominators
that widen was waiting on (F-2 above).

---

## 4. What you should have asked but did not

**Is `comp-pipescript io` load-bearing in a gate that currently cannot fire for 77 scripts?**

XXX.md makes `comp-pipescript io <script> --pipeline <tree>` a **per-role minimum for DS on every
gold script touched**, and `TO_COMPILER_GATE.md` says a TO with no compiler check logged is **not
accepted as complete**. For `data/assets` — 77 scripts, a **deployable** tree per Rule 13, and the
OPAL_ASSETS monolith — that check **cannot be run at all.** So either those TOs are being closed with
an unrunnable mandate silently skipped, or they are being closed with a check run against the wrong
tree. **Both are invisible in the record, because a mandate that cannot run leaves no failure —
it leaves nothing.**

I have **not** measured which of the two is happening; that is a records question across DS TOs, not
a tool question, and I am not going to assert it from the tool's shape. **It is the first thing I
would look at after R-3 lands**, and it is the reason I rank R-3 P0 rather than folding it into the
generalization work.

— 3.0.0_SA_CVO~B
