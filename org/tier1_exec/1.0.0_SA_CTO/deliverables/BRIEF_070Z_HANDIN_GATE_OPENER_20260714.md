# HAND-IN BRIEF — 0.7.0_AE_CloudOps~Z: the gate-opener lane

**archetype:** COORDINATE
**Author:** 1.0.0_SA_CTO~Z · 2026-07-14 ~08:0xZ · commissioned by Andrew-direct (verbatim below)
**You are:** `0.7.0_AE_CloudOps~Z` — a ~Z-lane instance, instantiated by Andrew THIS SESSION for one
mission: **open the two 0.7.0-side gates the ~Z work-track is held on.** You are NOT base 0.7.0 and
you do not touch base 0.7.0's world (their queues, holds, C9 tripwire, connector sweeps — all theirs).

**Authority (Andrew-direct to CTO~Z, 2026-07-14 ~08:0xZ, VERBATIM):**
> *"ill instantiate 0.7.0~Z now, prepare a brief to hand them"*

## 0. Startup mechanics (before anything)

1. Register the **FULL suffixed serial** `0.7.0_AE_CloudOps~Z` (a bare-0.7.0 registration will be
   REFUSED — base 0.7.0 is LIVE at another PID, and that is fine: different serial). Run `/watcher`
   (orphan-check first — a fresh session finding a matching `inbox-watch.sh 0.7.0_AE_CloudOps~Z stream`
   process has found a thief, not a watcher). Write the LD-0290 session-serial file. Zero crons.
   `org/XXX.md` is the full protocol.
2. **Comms partition (Andrew-direct, session-scoped, recorded @ `76fad8514`):** the ~Z group —
   `1.0.0_SA_CTO~Z`, `3.0.0_SA_CVO~Z`, `0.8.0_AE_CloudComp~Z`, and now you — **communicate only with
   each other this session.** The base agent group (including base 0.7.0) is a separate work track.
   Verbatim in the record file. Cross-partition needs route through Andrew.

## 1. Mission — two gates, one module, one conversation

Everything below is currently **built-to-the-gate and held loud** by `0.8.0_AE_CloudComp~Z`. Your job
is the applier/image side; theirs stays the producer/code side.

### GATE A — derive-image rebuild (FEDOBS(b))
`0.8.0~Z`'s delta @ **`78143ad7f`**: marker pin in `fedobs_observe.py`, scheduled task-def
`fedobs_producer.tf`, a **Dockerfile COPY whose new source must be in the CodeBuild zip**, lock-file
repair. The derive-image pipeline is your lane's machinery — rebuild the image so the new COPY source
is actually IN it.
**Acceptance (22a — exercise, not config-read):** the rebuilt image demonstrably contains the new
source (exercise the container path or an equivalent test that FAILS if the COPY is absent), and the
task-def resolves against the rebuilt image.

### GATE B — globgrph TF applies (ONE-APPLIER)
Two applies ride the same module:
1. **`fedobs_producer.tf`** (the scheduled FEDOBS producer task-def — **the standing-producer
   keystone**: the estate currently has ZERO standing producers and the certified learning loop is
   seed-fed without this). Two prior plan reads exist AND THEY MEASURED DIFFERENT SCOPES — 0.8.0~Z
   **6/0/0 for their delta**, CVO~Z re-take **7/1/0 exact** (fuller scope) — enumerate what YOUR
   plan is *of*, then read it yourself before apply (verification law 6; neither prior read is
   your read).
   **⛔ APPLY-SCOPE CAVEAT (CVO~Z cert `454394604`, surfaced-not-adjudicated):** a module-wide apply
   would CREATE the drift SNS email subscription (`item2c_surface_alarm.tf:30`, declared 06-17) —
   against Andrew's LATER no-alerts posture (`cfb741306`). 0.8.0~Z made the exclusion DURABLE in
   `fedobs_producer.tf`'s header checklist @ `01233e8d4` (CVO-validated) — **follow that checklist;
   if your plan shows the SNS subscription as a to-add, your scope is wrong. Latest +
   most-restrictive binds; only Andrew re-opens alerts.**
2. **MOTIF.P0 TF/infra leg** (if the derive path needs any module change — see §2; it may need none).
**Mechanics that bind:** `.tools/safe-apply.sh` only (NEVER bare apply); commit-before-apply;
deploy-completion ledger opened at deploy-start in `org/critical_paths/change_management/`, closed at
completion (NEVER#5 — a stranded leg is RED-ALERT material); 0-diff re-plan after apply; new IAM =
live `simulate-principal-policy`, ONE `--resource-arns` per call, positive control as a SEPARATE
invocation (comp-iam fails GREEN on new resources — Rule 22a).

### §2 MOTIF.P0 assist — GROUND FIRST, it may be verify-only
P0 (`org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_MOTIF.P0.tsgraph-p2-2-cluster-materialize.md`,
owned by 0.8.0~Z) has a **RECORDS CONFLICT**: a 07-02 record claims the ~91 clusters are
"materialized+verified"; the fresher 07-07 CVO grounding says the cluster edges are **NOT live** on
the canonical graph. **Ground on the live canonical graph first** (comp-kuzu/comp-cluster query for
`CLUSTERS`/`CONTAINS_DRILLDOWN`/`SHARES_SOURCE` edges, layer='portal'), then:
- **live already** → the whole leg collapses to verify-only; say so loud, apply nothing.
- **not live** → the derive plumbing EXISTS (`infra/aws/globgrph/derive_runner.py::ingest_cluster_producer`
  L1240-1290, invoked L1696, best-effort/skip-if-absent). 0.8.0~Z publishes/locates the producer JSON
  and runs the derive per their TO; you own any TF/image change the run needs. The DE publish/verify
  leg stays DE-gated (base-track) — not yours, not theirs this session.

## 3. The one-applier resolution (and its residual)

The redirect constraint (`14c2aeeba`) says: *0.7.0 owns globgrph TF today — agree one applier before
any apply.* Andrew instantiating YOU inside the partition IS the sovereign routing of the applier
role **for these two applies**. Residual risk, surfaced not adjudicated: **base 0.7.0 must not
concurrently apply the same module this session.** Their live queue (connector sweeps, C6, smartx
hold) does not name globgrph, but only Andrew bridges the partition — this brief flags it to him;
if base 0.7.0 needs globgrph this session, HE arbitrates, not you.

## 4. Standing constraints (not waivable here)

INF chain hold + the frozen three: untouched — nothing you run may advance the INF chain (functional
test, not lexical). All NEVER rules stand. TF-only deploys. Comp-rail applies (Rule 21: `comp-which`
first; raw aws INSPECTION carries `# rail-checked:`). Times to Andrew in US Eastern.

## 5. Comms + delivery discipline

- **Deliver with evidence, never self-report:** commits, plan/apply outputs with denominators, the
  exercised test. `3.0.0_SA_CVO~Z` re-verifies your gate work — their FEDOBS(b) re-verify is already
  queued **UNVERIFIED-PENDING-APPLY**, i.e. *your apply is what un-gates their live-exercise limb.*
- **On gate-open, notify (same turn):** `0.8.0_AE_CloudComp~Z` (their measure path goes live →
  PROMOTE candidates start flowing), `3.0.0_SA_CVO~Z` (re-verify can take the live limb),
  `1.0.0_SA_CTO~Z` (me — PROPOSED promotion commissions then route to my ratify lane; I also hold
  the graph-substrate arch-gate: structural edits to `nerves_*.py` / `comp_pydeps.py` / the blast
  path / the node_type SSOT route through me).
- RAVC on everything; a HALTGT pass is not evidence you were not halted (Rule 18); SENT is not READ
  (22b) — close loops on ACKs.

## 6. Pointer pack

| What | Where |
|---|---|
| FEDOBS(b) delta (Gate A+B payload) | `78143ad7f` (0.8.0~Z) |
| PROMOTE.P1 build (context: what the gate feeds) | `becdf0c19`; 7 candidates held at measure, honest refusal |
| Redirect chain | `14c2aeeba` → `552667ccd` → `b251c596e` → `c650bf0d3` (P3 ext.) |
| Partition + P3 record (verbatims) | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_ZGROUP_COMMS_PARTITION_20260714.md` @ `76fad8514`/`c650bf0d3` |
| NERVES architecture (why this matters: L1 standing producers + L4 loop-feed) | `docs/architecture/NFRA_NERVES_PRD.md`; L2+L3 VERIFIED SOUND @ `2d2080e1e` |
| MOTIF.P0 TO (records-conflict note inside) | `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_MOTIF.P0.tsgraph-p2-2-cluster-materialize.md` |
| Deploy ledger home | `org/critical_paths/change_management/` |

**First act after startup:** MCP `0.8.0_AE_CloudComp~Z` — confirm the Gate A image contents and the
Gate B plan against their `78143ad7f` delta, then open Gate A. The whole ~Z track is waiting on you;
build order is A → B(1) → §2 ground-check.

— 1.0.0_SA_CTO~Z
