# Graph Refresh Audit + comp-kuzu-full / comp-kuzu-inc Split (DRAFT)

**Author:** 0.0.0_AB_MSTR
**Date:** 2026-07-17
**Status:** DRAFT — HELD for Andrew's paired review (with `AGENTBUS_SCHEMA_SPEC_20260717.md`); NOT routed to CTO per his explicit sequencing. Implementation charters to CTO (owns the globgrph platform + arch-gated the original incremental design).
**Citation vintage:** all `file:line` refs resolve at CLOUD HEAD `0ffae035b` (2026-07-17). A line citation without a vintage is not a citation (CLAUDE.md Rule 22).

---

## 0. What Andrew asked

Verbatim, this session:
1. *"do an audit of this whole refresh process on the cloud incremental basis, see if there are any comparable local processes, and how to sequence this mechanically as well as working it into the comp tools so we dont always have to full derive."*
2. Target design (verbatim): *"we should be writing full derive as a function of 0.0.0_AB_MSTR startup, but for the remainder of the session, all agents should just be using incremental update pre comp tool queries. I would recommend something like comp-kuzu-full and comp-kuzu-inc for this purpose, so it is clear and documented in the comp-tool manifest/registry yaml and maybe indicated in the relevant memory.md files claude.md files etc."*

---

## 1. THE HEADLINE FINDING — the symmetric local incremental ALREADY EXISTS

Andrew's premise (*"the sqs/lambda process allows for incremental writes to the cloud graph, but that
actually doesnt account for incremental writes to the kuzudb local **as far as I'm aware**"*) — the
"as far as I'm aware" is the tell. **A symmetric local incremental refresh was built 2026-07-08,
Andrew-directed, CTO arch-gate GO 195732Z, and is LIVE (default-on).** Do not re-build it. The audit's
value is not "the gap exists" — it is *the gap is not existence, it is scheduling + surfacing*, and
Andrew's `-full`/`-inc` design is exactly the right fix for the real gap.

## 2. The full architecture, grounded at source

### Cloud side — writes the versioned graph (Iceberg tables under Nessie, `s3://opal-313476888478-globgrph/warehouse`)

| Half | What | Cadence | Source |
|---|---|---|---|
| **2a FULL DERIVE** | live-AWS scan → **whole-table OVERWRITE** of `graph_nodes`/`graph_edges` (every row a fresh `batch_ts`) | nightly Fargate ~02:00Z | ground-truth reset |
| **2b INCREMENTAL UPDATER** | SQS batch of CloudTrail events (~2min debounce) → bounded live-describe of the changed ARNs → scoped `overwrite(filter)` → **ONE Nessie commit/batch** → stamps `warehouse/_branch_head.main.json` marker + per-table `last_write_iso` | per change, ~2min | `infra/aws/lambda/globgrph/incremental_updater/lambda_function.py` |

The **marker** (`_branch_head.main.json`) is the HEAD oracle for dev boxes — they cannot reach Nessie
REST in-VPC, so they learn HEAD from that S3 object (`lambda_function.py:542`).

### Local side — projects the cloud Iceberg HEAD into a local KuzuDB (`kuzu_nessie_db`)

| Half | What | Cost | Source |
|---|---|---|---|
| **FULL RELOAD** | read HEAD Iceberg tables from S3 (marker-pinned) → full ~55K-row rebuild | **~356s (~6min)** | `_canonical._default_rebuild` → `kuzu_nessie_load.py` |
| **INCREMENTAL REFRESH** | diff HEAD Iceberg set vs the LIVE local DB → `MERGE` upserts + `DETACH DELETE` removals on a file-copy → atomic swap | **~3.9s (92× faster)** | `kuzu_incremental_refresh.py` (Andrew-directed 2026-07-08) |

Safety already engineered into the incremental: a **count-guard** (post-apply node/edge counts must equal
the HEAD set or it refuses the swap), a **content-exact `reconcile()` oracle** (all 9 node fields + edge
fields vs a full-rebuild ground truth — catches silent drift a count-guard can't), and a **never-worse-
than-full fallback**.

### The trigger — `_canonical.ensure_fresh` (PULL / LAZY, on-query)

A `comp-kuzu` query checks `needs_refresh` (marker HEAD vs the local pin + a 26h age floor). If BEHIND →
mkdir-mutex → `_incremental_or_full_rebuild` → **prefer incremental, fall back to full** on large-delta /
cold-start / guard-trip (`_canonical.py:345-395`). The canonical DB is **shared across agents on one
machine** (mkdir-mutex + atomic-swap), so one agent's refresh warms the DB for its peers.

## 3. Why full rebuilds STILL happen (the recurring cost Andrew feels)

1. **THE NIGHTLY, by design.** 2a whole-table-overwrites every row with a fresh `batch_ts`, so the first
   BEHIND query after ~02:00Z sees a **whole-table delta** → trips the large-delta gate
   (`FALLBACK_MIN_ABS=4000` AND `≥25%` of head) → full `kuzu_nessie_load` (~6min). This happens **once per
   day, per dev box, ambushing whichever agent queries first** (`_canonical.py:360-367` — "CTO condition 2,
   satisfied BY CONSTRUCTION"). This is the single biggest recurring hit and it lands on a *random* worker.
2. **Cold start** (no local DB) → full.
3. **Guard trip** (count mismatch / rc=1 error) → full.

**The "10-minute" disambiguation — HONEST, and Phase-0 work, not an assumption:** the measured local
full-reload is ~6min (356s). A ~10min "derive" is more consistent with **`comp-aws derive`** (the live-AWS
scan that *builds* `graph_nodes`, a different operation from projecting the Iceberg HEAD into Kuzu) run
directly, or machine variance on the nessie-load. **Phase 0 must instrument which path the operator
actually hits before the fix is sized** — do not conflate the AWS-scan derive with the Iceberg→Kuzu reload.

## 4. So the real gap is three things, none of them "existence"

- **PULL, not PUSH.** The incremental fires *when a query notices BEHIND*, not *downstream of the 2b
  writer's commit*. Andrew's mental model ("directly downstream of the sqs/lambda incremental writer") is
  push; the built one is lazy-on-query. In DATA terms it IS downstream (it pulls the committed Iceberg
  HEAD); in TRIGGER terms it is not.
- **UNSCHEDULED.** The unavoidable daily full-reload lands on whichever agent queries first post-nightly —
  unpredictable, and it ambushes a worker mid-task.
- **UNSURFACED.** "incremental" vs "full" is an internal fallback decision, not two operations an agent
  consciously chooses. There is no `comp-kuzu-inc` an agent can *elect*.

## 5. Andrew's target design — and it fits the grain of the mechanism

> Full derive = a function of **MSTR (`0.0.0_AB_MSTR`) startup**; every other agent uses **incremental
> pre-query** for the rest of the session. Split commands **`comp-kuzu-full`** / **`comp-kuzu-inc`**,
> documented in the manifest/registry yaml + MEMORY.md + CLAUDE.md.

**Why it works with the mechanism, not against it:** MSTR's startup `comp-kuzu-full` **absorbs the nightly
whole-table delta ONCE**, warming the shared canonical to nightly-HEAD. Every subsequent agent that day
then sees only the small 2b `incremental_updater` deltas on top of that baseline → `comp-kuzu-inc` applies
in ~4s. The design **schedules the unavoidable daily full onto MSTR startup** instead of letting it ambush
a random worker. That is a real, correct improvement over today's "whoever queries first eats 6min."

### 5.1 The ONE refinement I must surface (Andrew's call, not silently baked)

For the design to deliver its guarantee, **`comp-kuzu-inc` must be "incremental-OR-serve-labeled-stale",
NEVER "incremental-or-full".** Today's `_incremental_or_full_rebuild` falls back to a full 6min reload on a
large delta. If a worker runs `-inc` when the delta is large — e.g. it queries *before* MSTR's startup full
has landed, or during a burst — the current code would still make that worker eat 6min, defeating the whole
intent. So `-inc` must instead: apply the incremental if the delta is small; if it is large/cold, **DO NOT
full-rebuild — serve the current (labeled-stale) DB and log LOUD** ("BEHIND by N; run `comp-kuzu-full` or
wait for MSTR startup"). That single semantic is what makes "workers never pay full" actually true. It is a
deliberate divergence from the current fallback and worth Andrew's explicit yes.

(Corollary: a worker serving labeled-stale is safe — the DB is a COMPLETE prior-vintage projection, never
half-built, and the label makes the vintage honest. This is strictly better than a 6min mid-task stall.)

## 6. Sequencing (mechanical)

- **Phase 0 — INSTRUMENT (Rule 22 grounding).** Confirm which path is the operator's 10min (`comp-aws
  derive` live-scan vs `kuzu_nessie_load` reload vs an incremental-fallback); measure the real per-box
  morning cost + the fallback rate; confirm the shared-canonical warm actually benefits one machine's peers
  (it should — mkdir-mutex/atomic-swap already shares it). No fix is sized before this lands.
- **Phase 1 — SPLIT THE COMMANDS.** `comp-kuzu-full` = force full `kuzu_nessie_load`, unconditionally.
  `comp-kuzu-inc` = incremental-or-serve-labeled-stale (§5.1), never full. `comp-kuzu` (bare) stays as
  today's auto for back-compat / direct callers. `kuzu_cli.py` gains a mode flag; the two wrappers set it.
- **Phase 2 — MSTR-STARTUP HOOK.** MSTR launcher / `org/XXX.md` Step 1b runs `comp-kuzu-full` once at
  startup (the daily-reset owner). **Idempotent guard:** if the canonical is already at nightly-HEAD this
  cycle (manifest/marker says so), skip — never double-pay. In the two-machine future, each machine's lead
  runs it at its own startup (the canonical is a per-machine local file).
- **Phase 3 — DOCUMENT (ships WITH Phase 1 so the map never leads reality).** `graph-call-manifest.yaml` +
  `comp-tools.yaml` registry rows (the `comp-manifest-check` registration invariant enforces both new
  executables are registered); the CLAUDE.md comp-* situation→command table; one `MEMORY.md` line (the
  who-runs-full rule); `comp-which` routing ("refresh/update graph" → `-inc`; "full/ground-truth rebuild"
  → `-full`).
- **Phase 4 — (optional, two-machine payoff).** Distribute MSTR's built canonical DB artifact via S3 so a
  second machine pulls the pre-built KuzuDB file instead of re-deriving — build-once-distribute, the
  pattern that compounds with N machines. Ties directly to the AGENTBUS / two-machine strategy.

## 7. comp-tool integration specifics

- **Registry:** two new routable `.tools/comp-kuzu-{full,inc}` executables; `comp-manifest-check`'s
  registration invariant blocks any commit that leaves them unregistered (the count is gate-maintained).
- **`comp-which`:** "refresh the graph / update kuzu / my graph is behind" → `comp-kuzu-inc`; "full rebuild
  / ground-truth reset / reconcile" → `comp-kuzu-full`.
- **`comp-graph status`:** already prints kuzu vintage; add a "last mode (full|inc) + behind-by-N" line so
  an agent can see whether a full is owed.
- **CLAUDE.md:** one situation→command row + a one-line rule ("MSTR owns the daily `comp-kuzu-full` at
  startup; all other agents `comp-kuzu-inc` — never full mid-session").
- **MEMORY.md:** one index line pointing at the rule.

## 8. Routing + authority

- **HELD** for Andrew's paired review with AGENTBUS. Not routed to CTO (his sequencing).
- **On release:** implementation charters to CTO — the code (`kuzu_cli.py` modes, the two executables, the
  registry) is Art. VI (MSTR governs, does not edit); CTO owns the globgrph platform and arch-gated the
  original incremental. The CLAUDE.md / XXX.md / MEMORY.md doc edits are MSTR-lane but ship **in the same
  wave** as the CTO implementation so the docs never describe a tool that does not yet exist.
- **§5.1 is the one item that needs Andrew's explicit yes** before it becomes a TO — it deliberately
  diverges from the current fallback semantics.
