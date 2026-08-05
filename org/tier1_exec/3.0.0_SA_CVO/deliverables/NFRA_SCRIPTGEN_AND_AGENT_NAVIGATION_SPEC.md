# NFRA_SCRIPTGEN — comp-pipescript as SCRIPT GENERALIST, plus the agent-navigation layer (comp-find / comp-read)

**Status:** SPEC — Part A ready for build · Parts B/C for CTO routing
**Author:** `3.0.0_SA_CVO~B` · **Date:** 2026-08-05
**Authority:** Andrew-direct, ~2015Z at the CVO~B terminal (recorded + broadcast `20260805T201606Z`)
**Predecessor evidence:** P8 cold descent `@a2be6600c` · shipped engine `@e07b9a29a` · doc/router
fix `@4b50ddcf3` · false-clean fix `@6fb81a231` · gate registration `@df3f5786f`

---

## 0. WHAT ANDREW ASKED FOR, VERBATIM, AND HOW THIS SPEC MAPS TO IT

> **(1)** *"we do want this built, let me know when the spec for comp-pipescript (evolved as script
> generalist) is complete."*
> **(2)** *"the purpose of the corp-\* tooling was helping 'AGENTS' figure out what files they needed
> to read and what files they needed to edit… replace comp-grep/glob with comp-find (no SLM rerank
> required, just have it structure paginated results like all the other comp-tools do). We then will
> definitely want a comp-read tool… agents actually grep to the right file, and simply don't read the
> information that was actually crucial to read… facilitating key context reads, not just file id."*
> **(3)** *"Comp-tool registration has to be a rigid, always-followed process… fully registered in all
> canonical locations as required from comp-tooling registration canon, as well as having all
> relevant assets for those tools referenced canonically with proper paths."*

| Part | Covers | State |
|---|---|---|
| **A** | comp-pipescript evolved as script generalist | **the spec he is waiting on** |
| **B** | comp-find (replaces comp-grep/glob) + comp-read (key-context reads) | design; needs CTO routing — it touches CLAUDE.md Rule 21 |
| **C** | registration canon, binding on A and B | design + a measured gap |

---

# PART A — comp-pipescript as SCRIPT GENERALIST

## A.1 The defect, measured (not asserted)

Denominators re-derived live, exclusions named (1,541 dependency-bundle files excluded from 4,961
tracked `.py`):

| universe | count | tool addressed |
|---|---:|---:|
| curated DAG universe (4 trees × gold) | 262 | — |
| all `data/*/scripts/**.py` | 498 | **52.6%** |
| all first-party repo `.py` | 3,420 | **7.7%** |

Six script trees resolve to **no graph at all**: `assets` (77 — the OPAL_ASSETS monolith, and
**DEPLOYABLE** per CLAUDE.md Rule 13), `smartx` (31), `seeking-alpha` (14), `etfs` (5), `demo` (4),
`yang_pkl` (1).

**The defect is the tool's UNIVERSE, not its behavior.** `--pipeline` accepts a fixed 15-value
`choices` list derived from the deploy map. That is a hand-drawn roster where a re-derived predicate
belongs — the *a-predicate-is-not-a-roster* class (CTO, 2026-08-04). It also recasts the 07-30
`--pipeline REQUIRED` change: that correctly killed a silent bd-gold default, but **hardened the
roster premise rather than removing it.** A correct fix inside a wrong frame.

## A.2 What already shipped (`@e07b9a29a`) — the floor this spec builds on

`org/modules/graph/script_io_ast.py` + a fallback in `cmd_io`. On a curated-DAG miss, if the argument
is a real `.py` on disk, `io` answers from deterministic AST derivation instead of refusing.

Live behavior, verified against source (all four rows hand-checked; `ASSETS_BUCKET:87` and
`STAGING_KEY:88` fold exactly; loop-var and attribute targets correctly stay unresolved):

```
OUT-OF-GRAPH SCRIPT -- the [mdpf] curated DAG does not carry this file.
  ENGINE:  AST (deterministic, source-derived) -- NOT the curated pipeline graph.
  ABSENT:  chain membership, run order, column gaps, portal consumers.
  DENOMINATOR: 4 recognized I/O call site(s) scanned
  READS (2):  s3://opal-data-assets/{?}  <- get_object() :196 …
  WRITES (1): s3://opal-data-assets/gold/…/aggregate_aua_timeseries_interpolated.json <- put_object() :736
  UNRESOLVED (1): READS open() :712
```

Measured over the previously-100%-invisible assets tree: 0 parse errors · 37 of 77 files with ≥1 I/O
site · 140 sites · 40 fully-named targets · 100 UNRESOLVED-but-named. **Resolution rate 29%.**

## A.3 The three invariants — these are the acceptance criteria, not aspirations

**A.3.1 — FACT ENGINE, NEVER A RANKER.**
`io` answers a question whose correct output is complete-or-honestly-incomplete. A missing edge is a
**wrong answer**, not a lower score, and its consumer is a deploy-gate obligation (XXX.md per-role
minimums) where CLAUDE.md Rule 22 forbids grounding a source-confirmed claim on a rank. **No ML
ranking, no learned reranker, no confidence score may enter this path.** *(This is why anatomy's
`corp_write` stack — L0 reach → CatBoost → qwen3-coder:30b — was surveyed and deliberately not
recycled here. Its capability belongs in Part B, where ranking is correct.)*

**A.3.2 — SILENCE IS THE DEFECT.**
Every unresolvable call site is emitted as `UNRESOLVED` with `file:line`; never dropped. Every result
prints its **denominator** (sites scanned). A parse failure or missing file renders `UNPARSEABLE` —
never an empty I/O set. *Rationale: an under-reporting I/O instrument does not fail loudly; it
produces a clean zero that reads as "this script has no I/O." Same class as the comp-iam
under-reporting lesson (Rule 22a) one tool over.*

**A.3.3 — UNDER-CLAIM OVER FABRICATE.**
Constant folding stays module-scope, single-assignment, string-literal only. A **rebound** name
refuses to fold. A wrong target is worse than an honest unknown, because a wrong one is silently
actionable. Mutation-checked: breaking the rebound-refusal yields `s3://two/k` and the
anti-fabrication test catches it.

## A.4 The build — four workstreams

### WS-1 (P1) — Replace the roster with a re-derived predicate

Replace `--pipeline {15 fixed choices}` with resolution in this precedence:

1. explicit `--pipeline <key>` (unchanged; still authoritative)
2. **path-derived tree**: `data/<tree>/scripts/<layer>/…` → `(tree, layer)` read *from the path*
3. auto-walk on a bare id (existing behavior)
4. **no guess** — refuse loudly, naming what it tried (existing `rc=2` discipline, preserved)

**The 07-30 no-silent-default ruling is preserved and strengthened**: it stops being "name a member
of this list" and becomes "the tool states which tree it resolved, and refuses when it genuinely
cannot." A new `data/<newtree>/` requires **no code change** to become visible.

**Acceptance:** a new tree added under `data/` is resolvable without editing any allowlist; the
refusal path still fires with no path hint; every existing `--pipeline` value keeps its meaning.

### WS-2 (P1) — Curated-first, AST-always dispatch

One resolution order for every `io` call:

```
curated DAG has it   -> curated answer (RICHER: chains, run order, column gaps, portal consumers)
curated DAG misses   -> AST answer, engine + limits declared in the header
neither (not a file) -> loud unknown-in-tree (unchanged)
```

**The curated graph stays authoritative wherever it has the script.** AST never overrides it.
**Acceptance:** in-universe scripts are byte-identical to today (verified: AST engine used 0 times on
`A_00 --pipeline bd`).

### WS-3 (P2) — Raise the resolution rate above 29%, honestly

Ordered by value/risk, each independently acceptance-tested:

| step | converts | risk control |
|---|---|---|
| function-local constant folding | locals assigned once from a literal | same rebound-refusal rule |
| `os.environ.get("X", "default")` | env-shaped targets → `env:X (default=…)` | never resolve to the *runtime* value |
| helper-call tracing (one hop) | `_write(df, KEY)` wrappers | one hop only; deeper → UNRESOLVED |
| `Path(...) / "literal"` joins | path builds | literal segments only |

**Hard rule:** every step may only convert `UNRESOLVED → named`. **No step may convert a named target
into a different named target**, and none may reduce the denominator. A step that cannot meet that is
not shipped.

### WS-4 (P2) — Extend beyond `io`

`feeds` / `consumers` / `overlap` become answerable out-of-graph by composing per-file AST manifests
over a target set (artifact-key join). `deployed` is **explicitly out of scope** — its universe is the
deploy map and moving it changes a deploy gate. That is a separate, CTO-scoped decision.

## A.5 Contract surface that must move WITH the tool

`--pipeline REQUIRED` is encoded in **two law surfaces**: `org/XXX.md` per-role minimums (DS/DT/AE
rows) and `CLAUDE.md`'s compiler-tools trigger table. COO has flagged and is holding the edit
(`20260805T154544Z`).

> **The silent failure to avoid, in COO's words:** a mandatory flag naming a member of a roster that
> no longer bounds the tool will *either* start refusing legitimate calls *or* — worse — **keep
> passing while meaning something narrower than the caller thinks.** The second survives review.

**If the generalization lands before the contract edit, that gap must be reported the same turn.**

## A.6 Out of scope (named so it is not inferred)

Chain/run-order inference from AST · `deployed`'s roster · portal-consumer derivation · any ML.

---

# PART B — THE AGENT-NAVIGATION LAYER (needs CTO routing)

## B.1 Andrew's diagnosis is a COMPREHENSION failure, not a retrieval failure

> *"agents actually grep to the right file, and simply don't read the information that was actually
> crucial to read, resulting in a scenario where we are propagating errors and/or missing key context
> despite having hit the right file."*

**Retrieval succeeded. Reading failed.** That reframes the tool: comp-read is not a nicer `Read`.

**Three specimens from ONE session (2026-08-05, mine), which is why the diagnosis holds:**

| # | Right file, unread line | Cost |
|---|---|---|
| 1 | Read comp-pipescript's `tools_index` line; inferred `shadow-detect` mapped to the 08-04 shadow veto. Its own `help=` — two commands away — says *"post-condition lock-in chain for a function."* | A false association between a benign subcommand and a sovereign prohibition, in a doc routed to CTO/COO. Struck at `@aa6910d1a`. |
| 2 | `.owned-paths.yaml`'s *"EXERCISED with a positive control"* note documents a **2-arg** `check_agent`; the real signature takes **4**. The disproof sits in the same file. | Anyone copying it gets a `TypeError` and may read it as a lane refusal. |
| 3 | Read the suite gate's summary (green, 64 passed); did not read `WATCH_GLOBS`. It covers **10 of 90** test files. | My own new battery sat outside the gate guarding the tool it tests. |

**The pattern is not random.** In all three the missed content is a **correction, exception, or
scope-limit adjacent to the claim** — the `⚠ CORRECTED`, the `NEVER`, the signature line, the
allowlist behind the green number. **Agents read the assertion and skip its qualifier.** That is the
design target.

## B.2 comp-find — replaces comp-grep/comp-glob

Per Andrew: **no SLM rerank.** Deterministic only.

- **Ranking:** recycle anatomy's `corp_hooks` **grade ladder** — `HEAD / SURFACED / REL / CONFIG /
  TEST / COLD` — computed from a graded universe built once per repo. Deterministic, reject-first, so
  reject-worthy hits sink and dive-worthy float. **Architecture recycled; models not.**
- **Structure + pagination** like every other comp-tool: stable ordering, explicit page/total, and a
  **denominator on every page** (`scanned N of M files in scope`).
- **Keeps** comp-grep's on-rails properties: repo-scoped, `.gitignore`-aware, logged, dependency
  context per hit.
- **Uncapped grading:** every hit gets a grade. A capped list is how a coupled file goes missing.

**Migration risk, surfaced not adjudicated:** CLAUDE.md **Rule 21** names comp-grep/comp-glob as the
sanctioned on-rails fallback, and Gate-1 enforcement (`org/mcp/comprail-gate1.enforce`) denies raw
estate grep *on the premise those exist*. **Replacing them is a law-surface change.** Sequence:
comp-find ships and is exercised → Rule 21 + the HUD/gate repoint → comp-grep/glob retire as declared
aliases (the retired-alias invariant already polices this). **Not mine to land.**

## B.3 comp-read — the one that fixes the named failure

**Purpose:** given a file and the question being asked of it, surface **which parts must be read**,
and make what was *not* read visible.

| # | Behavior | Why (tied to B.1) |
|---|---|---|
| 1 | **Structure map first** — sections/defs with line spans, so the file's shape is visible before any excerpt | You cannot know what you skipped without the whole shape |
| 2 | **Salience ranking** against the question (deterministic: BM25 over section text + structural proximity) | Right file, wrong region is the failure |
| 3 | **QUALIFIER EXTRACTION — the load-bearing feature** — near every returned hit, surface adjacent `CORRECTED`/`NEVER`/`EXCEPT`/`NOTE`/`⚠`/negations/scope-limits/signatures | All three specimens were a qualifier next to a claim |
| 4 | **UNREAD LEDGER** — `you have seen X of Y lines / A of B sections`, naming the unread high-salience ones | Converts a silent omission into a stated one |
| 5 | **Contradiction flag** — when two regions of one file disagree (a note vs the code it describes) | Specimen 2 exactly |
| 6 | **Never summarize away the primary text** — excerpts are verbatim with line numbers | A summary is a map; Andrew's own ruling: fetch the territory |

**What to mine from anatomy:** `corp_read.py` + `corp_read_pipeline/_params/_hud` (read-efficiency:
what to show, how wide, in what order) and `corp_peek.py` / `corp_line.py`. **`corp_write`'s ranking
is legitimate HERE** (which files to edit *is* a ranking question) — the A.3.1 prohibition is scoped
to `comp-pipescript io`, not to navigation. Andrew's *"no SLM rerank"* applies to comp-find; whether
comp-read may use one is **his call, not mine** — I recommend deterministic-first, since the
qualifier-extraction that fixes the named failure is structural, not learned.

**Acceptance (behavioral, not configural):** replay the three B.1 specimens. comp-read must surface
`shadow-detect`'s `help=`, the 4-arg signature beside the note, and `WATCH_GLOBS` behind the green
summary. **A tool that cannot catch the three failures that motivated it is not done.**

---

# PART C — REGISTRATION CANON (binding on A and B)

## C.1 The measured gap

**There is no written registration procedure and no route to one.** `comp-which "how do I register a
new comp tool"` returns a near-tie on `comp-genesis`/`comp-kuzu` — and **two independent prior agents
recorded the same result** (`NFRA_MSBEFF/nl_structured/chunk_10.txt:2260`;
`0.8.0_AE_CloudComp` log 2026-07-18): *"near-tie … no registration rule; expected, used to confirm no
curated route exists."*

**The canon is enforced by a gate and never written down.** Andrew's directive is that this stops.

## C.2 The surfaces a tool must land in (derived from `comp-manifest-check completeness`, live)

| # | Surface | Invariant today |
|---|---|---|
| 1 | `org/modules/graph/graph-call-manifest.yaml` → `tools_index` | 70 registered; registration-invariant PASS |
| 2 | same → `entries[]` (use_case / canonical_call / anti_pattern) | 71 entry-tools |
| 3 | `org/modules/graph/comp-coverage-map.yaml` | 91 ledgered; one home per tool |
| 4 | **output contract** | 70 declared, **26 declared / 44 pending** |
| 5 | **stage-2 vocab** (rail/grain/plane/scope) | 29 declared, canon enums |
| 6 | **curated `comp-which` route** | *not* the manifest — a separate keyword list |
| 7 | `.tools/comp-which-routing-test.py` baseline | routing regression |
| 8 | `~/bin` forwarder provisioning | `.tools/provision-path-shims.sh` |
| 9 | subcommand declaration | 28 of 70 establishable; **11 drifted** |

## C.3 THE FINDING THAT MAKES THIS URGENT

**Registering a tool in the manifest does NOT make it discoverable.** Measured today: I added ten
`comp-pipescript` subcommand entries (`@4b50ddcf3`), and `comp-which` still ranks `io` #1 for *"what
would a gold script run skip per partition"* rather than `skipgate` — **because comp-which routes
from surface #6, a curated keyword list, not from #1/#2.**

This is the same root as the 11 standing `self-route WARN` rows (`comp-types`, `comp-validate`,
`comp-whoread`, `comp-xray`, `comp-xref`, …): tools that surface only in a near-tie list, never
rank-1, in **the estate's default entry point per Rule 21**.

> **A tool registered in 8 of 9 surfaces is not 89% registered — it is UNDISCOVERABLE, which for a
> routing-dependent estate is indistinguishable from unbuilt.**

## C.4 Proposal (CTO to route — governance, not mine to land)

1. **Write the canon** — one doc, the 9 surfaces, in order, with the command per surface.
2. **Route it**: a curated `comp-which` rule for *"how do I register a comp tool"* — the absence of
   which is itself specimen #1 of the problem.
3. **Gate it**: extend `comp-manifest-check` from *registered?* to *ROUTABLE?* — a new tool that
   cannot be reached rank-1 by its own canonical question fails registration. The self-route WARNs
   become the acceptance signal instead of standing noise.
4. **Bind it to build**: no comp-tool is COMPLETE until all 9 pass. This binds comp-find/comp-read.

---

## Appendix — provenance of recycled material

Source archive `C:\Users\AndrewBerman\Downloads\anatomy-main.zip` (374,494,703 B, mtime
2026-07-20 12:30:59 -0400) — **not tracked, outside git**. Artifacts pinned by sha256[:16] at
`@575718fef` (`corp` `7057f1bf39967a10` · `corp_grep.py` `1483add228270905` · `corp_glob.py`
`2b8ee38a382244bd` · `corp_hooks.py` `6e9bc8c93720c5d4` · `corp_write.py` `8503059bcc84b701` ·
`corpgraph_schema.py` `eeb6b08487a76b90`). **Nothing has been copied into this repo**; Part A recycles
an architecture, and Part B should do the same wherever possible so no unversioned dependency enters.

— 3.0.0_SA_CVO~B
