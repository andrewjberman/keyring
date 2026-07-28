# comp-tool REGISTRATION ARCHITECTURE — colocation, registries, gates, and where the freshness classes thread in

    author: 3.0.0_SA_CVO
    task:   Andrew-direct 2026-07-28 — map the current registration/colocation architecture so the
            three freshness classes can be threaded into tool registration rather than parked in a doc.
    method: measured against the live artifacts, 2026-07-28T19xxZ

    HEADLINE: **the slots already exist.** `graph-call-manifest.yaml` declares `cost:` and
    `freshness:` per entry and they are **105/105 populated** — but as **PROSE, not a typed
    vocabulary** (94 distinct values across 105 entries). So the fields cannot be checked, diffed,
    or gated, and they drift silently. **Threading the classes in is a TYPING change to a populated
    field, not a new field.**

---

## §1 THE PHYSICAL LAYOUT — where things actually live

```
.tools/comp-*                          93 executables  -- THE SURFACE (what an agent calls)
  |                                                       23 self-contained; 70 are thin wrappers
  +--> org/modules/graph/*.py         121 engine refs   -- THE ENGINES (centralized, dominant home)
  +--> org/modules/graph/debtscan/      3
  +--> infra/aws/globgrph/              6
  +--> .tools/<sibling>.py              1               -- comp-missions, comp-tagauthz

REGISTRIES (all under org/modules/graph/)
  comp-coverage-map.yaml     1,062 ln   SOURCE OF TRUTH for tool INVENTORY  (CTO ruling #1)
  graph-call-manifest.yaml   1,386 ln   use-case catalog + tools_index (a PROJECTION target)
  comp-tools.yaml              864 ln   reference catalog
  drift-topology.yaml          247 ln   seam IDs -- REFERENCED by the map, never duplicated

GATES (commit-time)
  comp-coverage-check    COMPUNIFY S2 -- one home per tool, every overlap declared, inventory complete
  comp-manifest-check    canonical-call enforcement (no ad-hoc graph access); advisory->blocking ramp
  comp-routable-check    REGISTERED-IMPLIES-REACHABLE (a catalogued tool must survive the router filter)
```

**Colocation verdict: the ENGINES are well centralized** (121 of ~131 engine references in one
directory), and **the REGISTRIES are all colocated** in that same directory. This is a healthier
architecture than the tool count suggests.

## §2 THE AUTHORITY MODEL — and the one place it is not yet wired

CTO ruling #1 (locked, per the map's own §6): **`comp-coverage-map.yaml` is the source of truth;
`graph-call-manifest.yaml#tools_index` becomes a GENERATED VIEW.** The map carries the contract:

    source_of_truth: org/modules/graph/comp-coverage-map.yaml
    target:          org/modules/graph/graph-call-manifest.yaml#tools_index
    generator:       org/modules/graph/comp_coverage_view.py
    keeps_in_manifest: [does, subcommands, entries, routing, examples]

**So the intended split is clean:** the map owns *which tools exist and what each is for*; the
manifest owns *how you call it and for which use-case*.

**THE UNWIRED PART — measured count cascade:**

| population | count | what it is |
|---|---|---|
| `.tools/comp-*` on disk | **93** | the executables |
| homed in `comp-coverage-map` | **89** | 36 `tools[]` + 53 `meta_tools[]` |
| in `graph-call-manifest#tools_index` | **69** | the PROJECTION |
| use-case `entries` in the manifest | **105** | authored, many-to-one against tools |

**The projection is 20 behind its own declared source of truth.** The map states why:
`manifest_marker_status: "AUTHORED-in-working-tree ... graph-call-manifest.yaml is ANY_EXEC lane (not
AE-committable); the GENERATED-VIEW marker edit is ready ... but lands via an exec commit or a lane
grant."` **The generator exists, the contract exists, the marker has not landed — and the blocker is
a LANE PERMISSION, not a technical one.**

>> **CONSEQUENCE FOR ANYONE READING A COUNT: there are four different "how many tools" numbers and
>> none of them is wrong. 93 is the disk, 89 is the inventory, 69 is the projection, 105 is the
>> use-cases. Any statement of the form "we have N comp-tools" must say WHICH population** — this is
>> the same denominator discipline the tools themselves need, applied to the registry that describes
>> them. <<

## §3 WHERE THE THREE CLASSES THREAD IN — the slot exists and is populated

The manifest's per-entry schema, verbatim from its own header:

    cost:            "~ms" | "~2s" | "~9.8s" | "~8min"
    freshness:       how current the answer is + what backs it
    mode:            query | query-cached | rebuild
    rebuild_trigger: when to force a rebuild INSTEAD of querying (staleness-preempt)

**Population measured: `cost` 105/105, `freshness` 105/105, `mode` 102/105, `rebuild_trigger` 92/105.**
**Nothing is missing. The defect is TYPE, not presence.**

**`freshness` is prose:** 94 distinct values across 105 entries — **distinct/total = 0.90.** A typed
enum sits near 0; free text sits near 1. Examples: *"live"*, *"live TF state + code scan (no Kuzu
dependency)"*, *"kuzu DB <- latest Nessie/Iceberg commit (nightly + intraday); every call prints a
provenance header..."*. **Every one is individually informative and collectively uncheckable.**

### The proposed threading — additive, no new field

```yaml
freshness_class: DERIVED_ON_DEMAND | LIVE | PERSISTED     # typed, gateable, 3 values
freshness: "<the existing prose, retained verbatim>"       # unchanged, still informative
# PERSISTED only -- because it is the ONLY class where staleness is a real question:
refresh_mechanism: "auto-refresh on HEAD-advance" | "gate-enforced at registration" | ...
refresh_is_incremental: true|false                         # Andrew's distinction, made checkable
```

**Why this shape:**
- **It types the field without deleting the prose** — the prose carries the *why*, the class carries
  the *check*. Same pattern as the estate's `[MEASURED]`/`[INFERRED]` tags.
- **`refresh_is_incremental` is the load-bearing new bit, and it is Andrew's point made mechanical:**
  a surface taking regular incremental writes **is not stale because it was not fully rewritten.**
  Without this flag, any freshness check on the graph or a registry asks *"when was it last fully
  rebuilt"* — **the wrong question**, and the same error class as NEVER#1's wall-clock staleness.
- **Only the PERSISTED class needs the extra fields.** DERIVED_ON_DEMAND and LIVE are structurally
  exempt — which means the annotation burden falls on **34 GRAPH-DB + 66 REGISTRY** tools, not all 93.

### `cost` should become measured, not asserted — and here is why, with an instance
**Declared-vs-measured, run today:** `meta.comp_which.router` declares `cost: "<0.2s"`. **Measured:
1.07 s — under-declared ~5×.**
**One comparable entry only** (my matcher joins on the manifest's `tool:` string and the others did
not match), so **this is a single instance, NOT a rate** — I am not claiming the cost fields are
broadly wrong. But it demonstrates the class: **a hand-authored cost is a claim that nothing checks,
on a field the router and the rail are meant to make decisions from.** Proposal: keep `cost` as the
declared band, add `cost_measured` + `cost_measured_at`, populated by the timing harness
(`tool_time.py`, committed) — **so the declaration becomes falsifiable instead of decorative.**

## §4 THE REGISTRATION FLOW, as it stands

1. Author the tool at `.tools/comp-<name>` (wrapper) + engine under `org/modules/graph/`.
2. **Home it in `comp-coverage-map.yaml`** — `surface` | `seam`, `granularity`, `concern`, plus
   `touches_resource` and `distinct_from` if it overlaps another tool's resource.
3. `comp-coverage-check` enforces at commit: exactly one home, every overlap declared, inventory
   complete, projection current, grain stable. **Currently PASSING.**
4. Add use-case rows to `graph-call-manifest.yaml#entries` with `canonical_call`, `cost`, `freshness`,
   `mode`, `rebuild_trigger`.
5. `comp-routable-check` enforces registered ⇒ reachable through `comp_route.py`'s candidate filter.
6. `comp-manifest-check` enforces that consumers use the canonical call rather than ad-hoc access.

**The gap in the flow, stated plainly: step 2 records what a tool COVERS; nothing records what it
CANNOT see.** That is the `excludes:` field from the prior spec, and §3's `freshness_class` is its
sibling — **both are per-tool negative/typed declarations that the schema has no slot for today.**

## §5 RECOMMENDATION — three increments, ordered, all additive

1. **Type `freshness` → `freshness_class` enum + `refresh_is_incremental`** on the PERSISTED class
   only (≈100 tool-entries, mechanically derivable from the primitive census in `tool_profile.json`).
2. **Add `excludes:`**, populated from the per-primitive blind-spot table — same mechanical source.
3. **Land the generated-view marker** so `tools_index` (69) stops trailing the map (89). **Blocked on
   a lane permission, not on engineering** — `graph-call-manifest.yaml` is ANY_EXEC and the authoring
   lane could not commit it. **This is the cheapest of the three and the only one currently blocked.**

**All three attach to `comp-coverage-check`, which already passes — so they inherit enforcement rather
than needing a new gate.** No new registry, no new process, no new obligation on any other agent.

## §6 Limits

- **§3's cost finding is ONE instance**, not a rate. My join matched a single entry; the other five
  measured tools did not match the manifest's `tool:` strings. **Not evidence the cost fields are
  broadly wrong** — evidence that they are *uncheckable*, which is the actual claim.
- Registry contents read, **not** exercised, except `comp-coverage-check` which I ran (PASS).
- I did **not** assess `comp-tools.yaml` (864 lines) — a fourth catalog whose relationship to the
  other three I have not established. **Named as unassessed rather than assumed redundant.**

— 3.0.0_SA_CVO
