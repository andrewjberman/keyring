# comp-tool STRUCTURED PROFILE — 93 tools across five axes

    author:  3.0.0_SA_CVO
    task:    Andrew-direct 2026-07-28 — structured output over all 93 tools covering
             (1) universe (2) retrieval + freshness semantics (3) definitive coverage
             (4) wall clock + variance (5) return format + truncation risk
    data:    per-tool rows persisted as JSON (`tool_profile.json`, `tool_time.json`);
             this document is the ROLLUP — the primitive is the organizing key, because
             **the primitive predicts all four other axes.**

---

## §0 The organizing finding

**A tool's ENUMERATION PRIMITIVE predicts its universe, its freshness semantics, its wall clock,
and its truncation risk.** All five axes collapse onto one key. That is why this is a rollup by
primitive rather than 93 prose entries — and it is what makes the profile maintainable rather than
a one-time census.

## §1–§4 ROLLUP BY PRIMITIVE

| primitive | n | ① UNIVERSE | ② FRESHNESS SEMANTICS | ④ WALL CLOCK (measured) |
|---|---|---|---|---|
| **REGISTRY** | 66 | authored ledgers: coverage-map, manifest, tools_index, project JSONs | **PERSISTED-AUTHORED.** Stale iff the author didn't update. Gate-enforced where a gate exists (`comp-coverage-check` PASS) | **0.34 s** — sub-second, read-a-file |
| **GRAPH-DB** | 34 | the derived globgrph (kuzu) — cross-layer nodes/edges | **PERSISTED-DERIVED. STALENESS IS REAL.** Auto-refresh on HEAD-advance; **read the provenance header**; a `--db-path` scratch DB is a frozen vintage | not measured — needs a query arg |
| **GIT** | 29 | tracked files + commit history | **DERIVED-ON-DEMAND. Never stale** — git *is* the write history | **2.50 s** (comp-heat over 24,769 files) |
| **AWS-API** | 24 | the live plane (S3/Lambda/EC2/EventBridge/IAM) | **LIVE. Fresh by construction** — cost is latency, not staleness | latency-bound; my own live census calls ran 1–10 s |
| **FS-WALK** | 19 | working tree under declared roots + extension filter | **DERIVED-ON-DEMAND**; sees UNCOMMITTED state (a feature, not drift) | **22.65 s** (comp-clobber over `data/`+`infra/`) |
| **AST** | 12 | parsed Python source at the read vintage | DERIVED-ON-DEMAND | folded into FS-WALK cost |
| **SQL/TRINO** | 10 | the Trino federation by physical catalog | LIVE federation | **~3–4 min/call** (in-VPC Fargate one-shot) — analytical, never a gate |
| **SIMULATE** | 5 | actual IAM reach, by exercising every candidate | **LIVE EXERCISE — the only primitive that PROVES reach** rather than reading a declaration | N×M live calls; the most expensive and the most conclusive |
| **SUBPROC** | 3 | inherits the callee's universe | inherits the callee's freshness | inherits |
| **FS-GLOB** | 1 | pattern-matched tree | derived-on-demand | **1.63 s** |

**MEASURED SPREAD: 0.34 s → 22.65 s = 67×, and the primitive predicts the ordering**
(REGISTRY < GIT < FS-GLOB < FS-WALK+regex), with SQL/TRINO an order of magnitude beyond at ~3–4 min.

### ④ The design consequence Andrew asked for
- **Sub-second (REGISTRY):** safe in a commit hook / rail route. `comp-coverage-check` already is.
- **Seconds (GIT, FS-GLOB, AWS single-call):** safe interactively, **not** per-keystroke.
- **Tens of seconds (FS-WALK + regex over the estate):** **needs a scoped/incremental mode.**
  `comp-clobber` at 22.65 s is the clearest candidate — it re-walks `data/` + `infra/` every call
  with no `--path` narrowing used by default.
- **Minutes (TRINO, SIMULATE):** analytical only. **Never gate on these**, and never inline them in a
  loop body.

### ② The stale-vs-fresh distinction Andrew flagged specifically
**Three genuinely different semantics, and conflating them is the error:**
1. **DERIVED-ON-DEMAND** (GIT, FS-WALK, AST, FS-GLOB) — **cannot be stale.** Recomputed each call.
2. **LIVE** (AWS-API, SIMULATE, TRINO) — **cannot be stale.** Cost is latency.
3. **PERSISTED** (GRAPH-DB, REGISTRY) — **the only class where staleness is a real question.**

>> **And within (3), Andrew's incremental-vs-full-rewrite point is the operative one: a surface taking
>> regular INCREMENTAL WRITES is not stale merely because it was not fully rebuilt.** The graph
>> auto-refreshes on HEAD-advance; the registries are gate-enforced on registration. **So "when was
>> it last fully rewritten" is the WRONG staleness question for both** — the right one is *"has the
>> update mechanism fired since the last relevant change,"* which is what the provenance header and
>> the registration gate each answer. **This is the same shape as NEVER#1: an old timestamp is not a
>> staleness finding.** Only **34 GRAPH-DB + 66 REGISTRY** tools need a freshness question asked at
>> all; the other classes are structurally exempt. <<

## §3 DEFINITIVE COVERAGE — what we know we cover, absent a negative oracle

Andrew's constraint: *if we cannot programmatically establish negative control, how do we delineate
what we DO cover?* **Three mechanisms, in descending strength, all already present:**

1. **SIMULATE (5 tools) — definitive by exercise.** `comp-firmsep-sweep` simulates a credential
   against *every* role and asserts only the firm's own are allowed. **This is the only class where
   "definitively covers" is literally true**, because the tool *is* the oracle. Residual: the
   candidate set you enumerated to simulate — **a bounded, stated blind spot rather than an unbounded
   one.** That conversion is the whole value.
2. **ATTRIBUTION COMPLETENESS — definitive within a KNOWN universe.** `comp-coverage-check`'s
   `gate_contract` requires every member carry a disposition; an unattributed member is a declared
   silent gap. **Proves no member of the known set is unaccounted for. Does not prove the set is
   complete.**
3. **CROSS-DERIVE — a negative signal with NO oracle.** Two independent derivations of the same set,
   differenced. `comp-toolgraph` already does this for coupling. **This is the answer to Andrew's
   "even if the negative-control has yet to have a true oracle"** — you never need ground truth, only
   a second, differently-derived view. Every disagreement is a defect in one of the two.

**Where none of the three applies — the DERIVE-only tools — "definitive coverage" is exactly the
primitive's reach and nothing more**, and the §4 blind-spot table (`@a3dac97be`) states it per
primitive: `ls-files` → blind to gitignored/submodule/non-repo; `os.walk` → blind outside roots and
unlisted extensions; regex → blind to variable-interpolated values; registry-read → blind to the
unregistered (**the phantom class: MSBEFF measured 129 referenced vs 83 registered**).

## §5 RETURN FORMAT + TRUNCATION — measured across all 93

    head slice [:N]     81 tools        --limit N     7
    json output         81 tools        --max N       5
    --top N              7 tools        MaxKeys       1
    NO BOUNDING AT ALL   6 tools

    >> DENOMINATOR DECLARED IN OUTPUT: 48 of 93 (52%)
       THE OTHER 45 BOUND THEIR OUTPUT WITHOUT SAYING WHAT IT IS BOUNDED FROM. <<

**Measured output sizes on real invocations:** 317 B (`comp-coverage-check`) · 997 B (`comp-heat
--top 5`) · 1,132 B (`comp-which`) · 2,979 B (`comp-clobber`, 55 lines) · 6,735 B (`comp-grep`) ·
21,357 B (`comp-glob`, 531 lines).

### Can truncation cut semantically meaningful results? **Yes, and I have the worked case.**
`comp-clobber`'s static scan returns **11 multi-writer sinks over 110 scanned**, ranked. When I first
ran it I piped through `head -40` and saw 8 of 11 — **and the MDPF key I was hunting was not in the
visible set.** Had the list been ordered differently I would have concluded "not present" from a
truncation. **The 45 tools that bound without declaring a denominator all carry this exact exposure.**

**Highest-risk shape, ranked:** a **ranked** list, **silently sliced**, with **no denominator** — the
reader cannot tell whether the answer was outranked or absent. **81 tools carry a `[:N]` slice and 45
declare no denominator; the intersection is the population to fix first.**

## §6 LIMITS — declared, because this profile is itself an instrument

- **④ is MEASURED for 5 real invocations and NOT-MEASURED for the rest.** My first timing pass ran 23
  no-arg invocations and **20 returned `rc=1` usage stubs (~180 B)** — that measured argument parsing,
  not scanning. **Reporting that as "median 0.12 s" would have been a fabricated number on the wrong
  axis.** A representative wall-clock profile needs a per-tool realistic invocation, which is itself a
  per-tool contract that does not exist yet. **That is a finding, not an excuse.**
- **70 of 93 tools were NOT TIMED** — they did not declare read-only and I will not run a possible
  writer to produce a benchmark. NOT-MEASURED, never "fast" or "slow."
- **①/③ are DERIVED-from-source, not exercised**, except `comp-heat`, `comp-clobber`,
  `comp-coverage-check`, `comp-which`, `comp-grep`, `comp-glob`, `comp-fedobs` — which I ran.
- **4 tools remain unclassified by the automated pass** (`comp-imgread`, `comp-tagauthz`, `comp-to`,
  `comp-v5-composite-test.sh`); 3 are legitimately non-enumerating and `comp-tagauthz` was resolved
  by inspection to TF-PARSE.

— 3.0.0_SA_CVO
