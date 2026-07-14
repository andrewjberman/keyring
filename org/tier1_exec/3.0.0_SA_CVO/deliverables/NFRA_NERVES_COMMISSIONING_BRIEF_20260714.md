# NFRA_NERVES — commissioning brief: activate the hive mind (sense → address → accrete → evolve → serve)

**archetype:** COORDINATE
**Author:** 3.0.0_SA_CVO~Z · 2026-07-14 (compiled from an Andrew-direct strategy session, interactive channel, ~04:3x–05:1xZ)
**Ferry:** Andrew carries this brief to its owner personally. It is a COMMISSIONING BRIEF (goal + grounded diagnosis + property sets), not a PRD — architecture, mechanism, and sequencing-in-the-small belong to the owning CTO lane.
**Validation:** builder tests ship with each layer; delivery hands off to 3.0.0_SA_CVO~Z for /verify (claims → sharpest-re-take pattern, per `ed3686c72`).

**THE GOAL (Andrew, verbatim):** *"We want to be able to know what is hot, what is cold, what systems are evolving and how, danger zones, breakage points, high risk, etc, maybe even more things I havent even thought of. A big part was that the graph would kind of evolve based on the activity of the agents, like roads that become wider with lots of foot traffic... The ultimate goal is to create the ultimate hive mind, fully lexical, extremely information liquid."*

---

## 1. Diagnosis (grounded 2026-07-14, live measurements)

The estate has a certified skeleton and no nervous system. The graph records STRUCTURE (what exists); every signal the goal names — hot, cold, evolving, dangerous, fragile — is BEHAVIORAL and lives in event streams the graph cannot see.

- C1 estate tier: strong — 19,985 nodes / 35,034 edges, marker-fresh, auto-refreshing. C2 motifs: **7 nodes**. C3: first-instance only.
- The learning loop (MOTIF→PROMOTE→FEDOBS→demote): built, invariant-gated, CVO-certified end-to-end — **idle**. Observe surface: coevolution_pairs=6. `fedobs_signals` = **27 KB**; CSE log **frozen since 07-08** (the day its project closed). The GO'd standing-producer cadence: **zero** EventBridge producers exist (138 rules + 7 schedules scanned); `/log` host wiring absent.
- Trino: always-on Fargate (2 vCPU/8GB, 24/7), near-zero query traffic. Warehouse accrual since 06-09 spin-up: 1.03 GB / 167,887 objects — **99.7% is one table** (`graph_nodes`: 811 MB, ~17,912 Iceberg commits vs `graph_edges` 56 — an unbatched writer drowning in snapshot metadata; no expire/compact maintenance). Learning-plane content: <7 MB in 35 days.
- Agent traffic exists but is exhaust: telemetry hooks fire on every tool use; the rail logs every search; the outcome sink (built in NFRA_COMPCLOSE) records every run; git carries 35 days of atomic, message-dense history; CloudTrail flows. None of it addresses the graph.
- The danger zones are ALREADY WRITTEN DOWN — holds, frozen files, incident costs, stamp-order traps — in memory/, ledgers, CLAUDE.md, with file:line citations. Fully lexical, zero graph presence: an agent querying blast on a frozen file gets no warning unless it happened to read the prose.

**Root pattern:** build-discipline is excellent; adoption-wiring (a trigger, a producer, a consumer) is what slips. NFRA_NERVES is an ACTIVATION project — feed and connect what exists; build new machinery only where a layer is genuinely missing.

## 2. The five layers (property sets; mechanism is the owner's)

### L1 — SENSE: capture the streams that already flow
Standing producers over: agent telemetry (PostToolUse), the comp-which rail log, the outcome sink (`comp-tool-runs.jsonl`), git commits, deploy/apply ledgers, CloudTrail (via comp-debris), inbox/broker traffic, cert records. ~10 producers over existing streams; the FEDOBS producer API already defines the shape. This subsumes the GO'd-but-unbuilt Q4 cadence.
- **Acceptance:** each producer exercised live (a real event lands as a real record); the CSE/fedobs tables show sustained daily accrual for 7 consecutive days; an all-producers-dead state is LOUD (the seed-fed silence of 07-08→07-14 must be impossible to miss again).

### L2 — ADDRESS: one shared resolver (the keystone)
`resolve(path|ARN|tool|function|script) → node_id(s)`, extracted as ONE library from the pieces scattered in comp-blast / pipescript / comp-aws. Every sensed event becomes the universal traffic record: `(ts, actor, verb, [node_ids], outcome)`. An event without an address is exhaust; with one, it is traffic.
- **Acceptance:** resolver hit-rate measured and printed on a real day's event stream (denominator visible); unresolvable events land in a visible UNADDRESSED band (they are the F-5-class blind spots), never dropped.

### L3 — ACCRETE: new edge classes, weighted by traffic, with decay
- **ATTENTION** (agent×node, node×node co-attention per session) — from rail + telemetry.
- **CO-CHANGE** (files that commit together) — **backfill from 35 days of git history first**; richest edge class, free. Co-change WITHOUT co-deploy = the drift/breakage predictor.
- **OUTCOME** (route → sufficed/rejected) — already accruing; generalize router-affinity's traffic→weight pattern to edges.
- **RISK / HOLD / DOCTRINE** — entity-link the lexical corpus (memory/, ledgers, CLAUDE.md, incident docs; it is semi-structured: frontmatter, [[links]], file:line citations) into edges on the nodes they protect/indict. THE LEXICAL UNLOCK: danger zones become graph-native.
- **CERT/VINTAGE** — verification verdicts as edges carrying commit vintage ("what do we know about N and how stale is that knowledge" becomes a query; Laws 7/8 mechanized).
- **DECAY:** every traffic-derived weight has a half-life. Roads narrow too; nothing in the estate decays today.
- **Acceptance:** co-change backfill validates against a known-coupled pair (e.g. a lambda + its TF) and a known-independent pair; a HOLD edge on a frozen-three file is returned by comp-blast/comp-kuzu, exercised; decay exercised (a weight demonstrably shrinks over a no-traffic window).

### L4 — EVOLVE: feed the certified loop, let C2/C3 populate from evidence
MOTIF/PROMOTE runs against C1+traffic. Expected discoveries: hot corridors (recurring agent paths → curated routes / learned "agents who touched X did Y next"), danger zones (incident density × traffic × guard concentration × stale verification — all four factors are now edges), organs (co-change + co-fail + shared-owner clusters = C3 systems, discovered not declared), and **phantom limbs** — the rail already logs what agents SEARCHED FOR AND DID NOT FIND (NOFIT + zero-hit); that is a demand map for knowledge that does not exist yet.
- **Acceptance:** C2 population grows from 7 to a measured double-digit set where each motif carries its evidence bundle; ≥1 auto-demote exercised (the loop must be able to unlearn); the phantom-limb report exists and cites its rail denominators.

### L5 — SERVE: liquidity through the tools that already exist
No new UI. comp-blast answers carry traffic + risk + cert-vintage. comp-which flips learned affinity when the accrual gate reaches READY (20/20 — the flip stays gated, per standing rule). comp-debris reads the same traffic from the cold end. 06_current_state gains "hot/evolving this week." ONE new primitive: **comp-pulse** — the estate's vital signs (hot / cold / evolving / danger / phantom-limbs) compiled from traffic, read first each morning. Endgame reflex: a pre-commit advisor scoring a proposed diff against risk edges (the danger map as an active immune response, not a wiki).
- **Acceptance:** each enrichment exercised on a real node (a frozen-three query returns its hold; a hot corridor shows its traffic); comp-pulse grounded per the comp-system no-fabrication discipline (UNKNOWN-VINTAGE, never fabricated).

## 3. Sequencing (leverage order — each step feeds the next)

1. L2 resolver + universal traffic record (days; everything hangs on it).
2. L3 co-change backfill from git (a weekend; instant 35-day history).
3. L3 corpus entity-linking → risk/hold/doctrine edges (the lexical unlock).
4. L1 standing producers (subsumes Q4 cadence; gives the always-on Trino node a job worthy of its bill — or right-size it).
5. L4 MOTIF/PROMOTE on traffic; C2/C3 populate.
6. L5 comp-pulse + tool enrichment + the pre-commit reflex.

## 4. Discipline (non-negotiables, from the estate's own scar tissue)

- **Goodhart gate on ALL reinforcement:** usage ≠ value — a wide road to a wrong answer gets wider. Route every traffic→weight update through the existing certified machinery (PROMOTE's 5 invariants; comp-learns-score's outcome-anchored values). The hive mind learns from OUTCOMES, never popularity.
- **No new certified-but-idle machinery:** every layer ships WITH its consumer wired, or it does not ship. "Exercised on real state" is necessary but no longer sufficient — **utilization is a maturity axis** (07_maturity grades "can it work"; nothing grades "does it work daily" — NERVES adds that axis).
- **UNKNOWN is a band everywhere** (unaddressed events, unresolvable entities, no-visibility resources) — rendered visibly, never dropped, never defaulted to a verdict.
- **Ops pre-work, same lane:** batch the `graph_nodes` writer (edges' 56 commits prove the pattern) + snapshot-expiry/compaction; delete the two `cse_test_*` warehouse tables; owner-check dormant `graph_contracts` (silent since 06-16).

## 5. Composition with in-flight work (do not duplicate)

The CVOZ instrument brief (@ `1b111a6a6`, CTO~Z building now) supplies NERVES organs: comp-debris = the CloudTrail sense + cold-end read; comp-gitdrill/icedrill = the vintage drill; the repo-wide Python edge graph closes F-5 so the tooling layer itself joins the organism; the nine comp-which sharpening asks push traffic down the graph roads. NERVES is the connective tissue those organs plug into — reference, don't re-own.

## 6. Process

Owner: CTO-lane (estate-wide architecture → a PRD; this brief is its input). Builder ships each layer with its acceptance controls; delivery routes to 3.0.0_SA_CVO~Z for /verify; my re-take numbers win ties. Standing constraints bind throughout: INF hold + frozen three untouched, read-only where the brief says read-only, vendor egress rules unchanged.

— 3.0.0_SA_CVO~Z
