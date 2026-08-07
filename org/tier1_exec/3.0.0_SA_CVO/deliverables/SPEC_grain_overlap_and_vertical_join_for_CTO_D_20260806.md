# SPEC — two builds for `1.0.0_SA_CTO~D`: multi-grain overlap in comp-blast, and the path→vertical JOIN in comp-estate

**Author:** `3.0.0_SA_CVO`. **Date:** 2026-08-06 ~22:45Z.
**Andrew-direct:** *"comp-blast should be able to run at various grain levels for overlaps, definitely
at c3.i, likely at c2. comp-estate definitely needs that join. I need you to figure out how to spec
both, I will hand those off to `1.0.0_SA_CTO~D`."*
**Andrew, on cost:** *"Shouldn't be that crazy, there aren't that many c2 and c3 elements in the big
scheme of things, and because they are deterministically constructed, that means that it should be
very very easy to track their sub components and associated blast."*
**Grounded, and he is right — see §0.** Every count below is a live query I ran, not a doc read.

## 0. The grounding that sizes both builds

```
MATCH (n) WHERE n.node_type IN ['C2Motif','C3System'] RETURN n.node_type, count(*)
  ->  C3System   4
      C2Motif   19
```
```
MATCH (a)-[e]->(b) ... RETURN from_t, edge_type, to_t, count(*)
  ->  C3System CONTAINS C2Motif            12
      C2Motif  CONTAINS DataFetch          50
      C2Motif  CONTAINS ServedURL          45
      C2Motif  CONTAINS EC2_INSTANCE       38
      C2Motif  CONTAINS S3_BUCKET          34
      C2Motif  CONTAINS CW_ALARM           20   ... (25 rows total)
```

**THE MEMBERSHIP HIERARCHY IS ALREADY MATERIALISED AS EDGES:
`C3System —CONTAINS→ C2Motif —CONTAINS→ C0`.**

> **So neither build is a derivation. Both are TRAVERSALS OVER EDGES THAT ALREADY EXIST.** Andrew's
> read is confirmed at source: the partitions are deterministically constructed and their membership
> is a graph hop, not a computation.

⚠ **BLOCKING DISCREPANCY, must be resolved before either build:** the graph holds **4 `C3System`
nodes**; `STATE_FRICTION_DESIGN` §1 states **"14 structures over 138 chains."** F1's headline figure
is `structures_touched: K of 14`. **Those cannot both be the denominator.** Either the graph
materialises a subset, the census is stale (2026-07-30), or the two use different definitions.
**Whoever builds this must settle 4-vs-14 FIRST — a K-of-14 emitted against a 4-node partition is a
denominator error in the battery's headline number.** Not mine to rule.

---

# SPEC A — `comp-blast`: overlap at C2 and C3.i grain

## A1. The defect this fixes, measured

`--overlap-sweep` today: **21,412 candidates of 358,281 pairs, 15 displayed (0.07%)**, and **all 15
shown pairs are EC2-instance × EC2-instance, every one scoring `WEIGHTED 1.000`**, dominated by
`CONTAINS=807`.

**Two mechanisms, both structural:**
1. **`weighted_jaccard` saturates at 1.000 whenever `shared == union`** — the ratio maxes out *before*
   idf weighting can apply. **The specificity damping is inert exactly where the ranking puts its top
   results.**
2. The pairs that saturate are **co-members of one partition**. Two EC2 instances in the same motif
   share their membership surface completely.

>> **GRAIN IS THE FIX, NOT A FILTER.** A verb-exclusion list would suppress the symptom and leave the
> saturation. **At C2 grain those two EC2 instances are ONE UNIT, so the degenerate pair cannot be
> formed at all.** The artifact disappears by construction. <<

## A2. Interface

```
comp-blast --overlap-sweep --overlap-grain {c0,c2,c3i}     # default c0 = today's behaviour
```

**DO NOT OVERLOAD THE EXISTING `--grain {script,function,any}`.** That flag filters the population by
NODE TYPE. This is a different axis: the **UNIT OF OVERLAP**. Two axes on one flag is Rule 24 (iii),
and it is the class we spent today cleaning up.

## A3. Mechanism — a roll-up, per Andrew

For each unit U at the target grain:
1. **Members:** `U —CONTAINS*→ C0` (one hop for c2, two for c3i).
2. **Unit radius:** `radius(U) = ⋃ blast_radius(m) for m in members(U)`, then **subtract members(U)**
   — intra-unit edges are internal structure, not shared consumption. *(This is the c0-grain
   `CONTAINS=807` problem eliminated at the source rather than filtered downstream.)*
3. Score pairs of unit radii with the existing weighted-jaccard + idf + mass machinery, **unchanged**.

**Population sizes fall out of §0 and are the whole argument:**

| grain | units | pairs | today |
|---|---|---|---|
| c0 | 847 | 358,281 | 21,412 candidates, 15 shown |
| **c2** | **19** | **171** | **every pair displayable** |
| **c3i** | **4 (or 14 — see §0)** | **6 (or 91)** | **trivially complete** |

**At c2 and c3i the display cap becomes unnecessary and `--head` stops hiding 99.93% of the answer.**

## A4. Contract requirements

- **`DECLARED TERRITORY` must carry the overlap grain.** It already prints `grain:` for the node-type
  filter — **add a distinct line, do not reuse it**, or two grains collide on one field.
- **idf reference population is per-grain.** `ln(N/df)` over 19 units is a different statistic from
  `ln(N/df)` over 847 nodes. The existing *"NOT COMPARABLE ACROSS DEFINITIONS"* warning already says
  why; it must now also fire across grains.
- **`shared BY VERB` survives, and at unit grain it becomes the real signal** — `CONTAINS` should be
  near-absent once intra-unit edges are subtracted. **If `CONTAINS` still dominates at c2 grain, the
  member-subtraction in A3.2 is broken.** That is the build's own self-check, and I would make it a
  test.
- **Unassigned residue is DECLARED, never dropped:** C0 nodes belonging to no motif are a counted
  `unpartitioned` residue on every grain-mode run. (§8.3's residue-degraded mode is the same law.)

## A5. What this gives F1

F1's figure is *"which of the 14 c3.i structures the radius touches."* **A3.1's member-hop is exactly
that mapping** — it is the missing `radius → structure` resolver named in `S4_comp_blast_verification`
@6f8da8869. **Building A delivers F1's primitive as a side effect**, which is the strongest argument
for doing A before anything else in the battery.

---

# SPEC B — `comp-estate`: the path → vertical JOIN

## B1. The defect this fixes

**There is no path→vertical join, and the primitive that resembles one is unsound for the purpose.**
`--resource` is a **substring matcher over chain references**. Measured today, both failure
directions:

| direction | measured |
|---|---|
| **MISSES** | the chain name is often a *directory* component: `--resource inf-silver-chain` → rc=0 `advi-inf/inf-silver-chain`, while the file inside that directory does not match |
| **FALSELY MATCHES, SILENTLY, AT rc=0** | `--resource convert` → `advi-bd / bd-allocations` |

>> **THE FALSE MATCH IS THE DANGEROUS ONE. A wrong path→vertical mapping attributes a changed path to
> the WRONG BUSINESS VERTICAL, and then F1/F2/F4 are all computed over the wrong path set — silently,
> at rc=0, with full denominators printed. Contaminated figures with impeccable provenance.** <<

*(Method note, because it is the point: my first pass measured "3 of 25 paths resolve" using file
stems as queries. **That number was wrong and I withdrew it** — it measured my query construction,
not the tool. comp-estate answered its actual question correctly every time. **The tool is sound; the
operation does not exist.**)*

## B2. Interface

```
comp-estate --path <repo-relative-path>          # one path
comp-estate --path-batch <file|->                # N paths, for the battery
```

Emits per path: `(family, named_thread)` **or** an explicit non-answer.

## B3. Mechanism — resolution, NOT substring matching

**Longest-prefix-wins over declared chain paths**, the discipline already proven in
`estate_report_runner.attribute_path` (`:730`), whose own docstring records why order matters:
*"a lambda source_dir is a stronger claim than an area prefix… Reordering these silently downgrades
good attributions to area buckets."* **Reuse that hop-ordering logic; do not reinvent it.**

**THREE OUTCOMES, and the third is what substring matching silently destroys today:**

| outcome | meaning | rc |
|---|---|---|
| `RESOLVED` | exactly one vertical claims this path | 0 |
| `UNANCHORED` | no chain claims it — **§3's explicit residue, WITH COUNT** | 2 |
| **`AMBIGUOUS`** | **2+ verticals claim it — REFUSE, list the claimants** | 3 |

**`AMBIGUOUS` is non-negotiable.** Substring matching resolves `convert` to one vertical by accident
of ordering. **comp-blast already models the right behaviour here** — `AMBIGUOUS-SUBJECT: matches 209
nodes — refusing to pick… comp-blast will NOT answer a change-safety question about a subject it had
to guess.* **Same posture, same reason:** a guessed vertical is worse than no vertical, because
everything downstream inherits it silently.

## B4. Contract requirements

- **Batch mode emits the denominator**: `resolved N / unanchored M / ambiguous K of T paths`. §3
  requires the unanchored residue be explicit and counted; ambiguity needs the same treatment.
- **Vintage on every answer.** The thread NAMES come from `estate-coverage-resolver.json` (census
  **2026-07-30**, 7 days old today) while keys are re-derived live — CLAUDE.md Rule 20 already warns
  a name from a stale snapshot is not a live fact. **Every join result carries the snapshot vintage.**
- ⚠ **A DEGRADED RESOLVER MUST FAIL LOUD, NEVER RETURN ALL-UNANCHORED.** Measured 2026-08-06:
  `load_attribution_maps` degrades gracefully per hop by design; a concurrent commit made its
  resolver hop fail, `prod_to_thread` came back empty, and every downstream consumer reported a
  clean-looking zero *("0 candidates — the funnel working")*. **The join sits on that same resolver.**
  If the resolver is unavailable or empty, the join emits `JOIN_UNAVAILABLE` and **refuses**, because
  an all-unanchored result is byte-identical to an estate where nothing is attributable.
- **`--self-test` extended** with a positive control (a path known to resolve), a negative control (a
  path known to be unanchorable, e.g. `org/**` governance records), and **an ambiguity fixture** —
  the last is the one that proves the refusal path can fire.

## B5. What this gives the battery

**This IS stratum D — the VERTICAL JOIN — which `STATE_FRICTION_DESIGN` §3 makes the battery's
precondition:** *"every changed path → its C3.ii vertical via chain → (family, named_thread) matrix
key."* **F1, F2 and F4 are all defined "per vertical with changes in-window" and none of them can be
computed until this exists.** It is not one of four instruments; it is the thing the other three are
scoped by.

---

## Sequencing, and one honest boundary

**A before B**, for one reason: A delivers F1's `radius → structure` primitive as a side effect (§A5),
and A's correctness is checkable entirely inside the graph. B depends on the resolver, whose
4-vs-14 / vintage / degradation questions (§0, §B4) are live.

**NOT SPEC'D HERE, deliberately:** whether the battery's fan-out is per-vertical or per-axis, and
whether the c3.i denominator is 4 or 14. **Both are architecture calls I do not hold** — they belong
to `1.0.0_SA_CTO~B` (battery owner) and Andrew. Speccing around an unresolved denominator would be
the parallel-build error again, one layer down.

-- `3.0.0_SA_CVO`, for handoff to `1.0.0_SA_CTO~D`
