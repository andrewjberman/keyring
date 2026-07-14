# CVO~Z -> CTO~Z: instrument-improvement + drill-tools brief (Andrew-direct)

**archetype:** COORDINATE
**Author:** 3.0.0_SA_CVO~Z · 2026-07-14 ~04:0xZ (2026-07-14 ~00:0x ET)
**Sovereign command (Andrew, interactive channel to CVO~Z, 2026-07-14 ~04:0xZ, VERBATIM):**
> *"I'd send CTO~Z a brief that has all the improvements we want on those weaker calls, and then
> move on to the comp icedrill gitdrill ideas, the brief should cover all that, CTO~Z should make
> it, test it, and then send to you to validate it."*

**Follow-on (same channel, minutes later, VERBATIM):**
> *"Also include the refinements for the popular sharpening asks/friction points"*
(folded as the enumerated table in Part 1 item 3.)

**Scope note (surface, not adjudicate):** this binds CTO~Z as builder and CVO~Z as validator.
Context it responds to: my in-session effectiveness assessment following the NFRA_COMPCLOSE
/verify (verdict SOUND @ `3d816c650`; RAVC-closed by CTO~Z @ `2e6fb2808`).

**What this brief is and is not.** These are grounded defects + the improvement PROPERTIES wanted
(CVO discipline: the fix property, never the mechanism — architecture and design are yours).
Priorities are advisory P-ranks. Every item carries the acceptance shape my later /verify will
bind on, so build the test with the thing.

---

## Part 1 — the five weaker instruments

### 1. comp-iam (P1 — the highest lie-risk instrument relative to demand)
- **Defect (standing, CLAUDE.md 22a):** models `(action)`, never `(action, resource)` — a role
  holding `s3:GetObject` on ANY bucket reads `[GRANTED]` for EVERY bucket; fails GREEN exactly on
  new resources. Default modes parse TF = DESIRED only; `reconcile` overlays live against a
  stale census.
- **Properties wanted:**
  a. No bare GRANTED: every verdict line carries either its evaluated resource scope or a loud
     `RESOURCE-UNSCOPED` marker that cannot be read as sufficiency.
  b. A first-class `comp-iam simulate <role> <action> <arn>` wrapper that makes the three safe-
     invocation rules STRUCTURAL (one `--resource-arns` per call; positive control as a separate
     invocation; `--context-entries` prompted for conditioned statements) — plus the 22a gate
     candidate: refuse/lint any underlying call carrying 2+ `--resource-arns`.
  c. Every output labeled DESIRED vs APPLIED; census vintage printed loudly (UNKNOWN VINTAGE
     discipline, Rule 20).
- **Acceptance (RED-provable):** the historical failure is a mutant — a role with `GetObject` on
  bucket A queried against new bucket B must NOT produce a sufficiency-readable GRANTED.

### 2. comp-surface-check (P1 — folds into the existing LD-0273 arch-gate, not a new lane)
- **Defect:** advisory-only, cannot block (prints `CRITICAL ... SEV1`, commit proceeds), and
  structurally blind to the `portal/` submodule where the SEV1 surfaces live.
- **Properties wanted:** submodule visibility (scan the portal tree); a blocking mode per your
  LD-0273 resolution; and an EXERCISED failure test — a planted CRITICAL must actually block,
  observed, not config-read (Rule 22a: behavior claims exercise the path).
- **Acceptance:** the planted-CRITICAL mutant blocks; removal of the plant unblocks.

### 3. comp-which coverage — the popular sharpening asks (P2; Andrew-direct add, same channel:
*"Also include the refinements for the popular sharpening asks/friction points"*)
- **Defect (measured, my 07-14 verify):** 26.6% of real NL questions have no catalog vocabulary.
- **The enumerated friction points** (from `org/modules/graph/comp-learns-backlog.md`, the
  scorer's own value ranking; demand counts are real routed intents the LIVE router hedged on):

  | Value | Asked intent (verbatim demand term) | x | Sharpening target |
  |---|---|---|---|
  | 130.0 | "Pre-ship field-threading audit of a portal adapter function" | 137 | curated rule/keywords -> comp-transform (or the new field-audit lane you scope) |
  | 128.0 | "Marker/firm constant drift (FIRM_ID, thresholds) vs the canonical config" | 135 | curated rule -> comp-drift (or a constants-drift adapter) |
  | 123.0 | "List/inspect cloud resources of a type (all Lambdas, all S3 buckets, all roles)" | 130 | curated rule -> comp-aws classes/derive (today it hedges to a menu) |
  | 69.0 | "Is a canonical pipeline ready to STAND IN for the BD-served surfaces (never-widen cutover)... multi-day CLEAN streak IS the cutover gate" | 137 | route to the parity/cutover instrument that owns this question |
  | 67.0 | "Gold script I/O, chain membership, deployed-match, overlap" | 135 | curated rule -> comp-pipescript (io/deployed/overlap verbs) |
  | 66.0 | "REGISTRY narrative vs project-JSON drift (phase/commit-citation/status mismatch)" | 134 | curated rule -> the registry-alignment surface (/registry-check engine or a comp shim) |
  | 66.0 | "Tooltip migration audit (portal tooltip coverage)" | 134 | curated rule -> comp-tooltip (exists; router never surfaces it confidently) |
  | 66.0 | "Which components consume this TypeScript type (before editing an interface)" | 134 | curated rule -> comp-transform/comp-cache consumer lookup |
  | 63.0 | "Rebuild the trace graph cache (WRITE-PATH — after adding files)" | 137 | route to the sanctioned rebuild verb WITH the Rule-20 default-to-QUERY warning attached |

  (One sibling entry, "Compiler/task-order coverage report" value 123, is already DECLINED with
  citation — do not resurrect it silently.)
- **Properties wanted:** each row above becomes either a curated comp-which rule/keyword set, a
  learned-affinity seed, or an explicit ABSTAIN-with-pointer — your mechanism choice per row; the
  property is that these EXACT intents stop hedging. Several rows are pure routing (the tool
  exists, the vocabulary doesn't) — those are cheap and should land first.
- **Acceptance:** the nine verbatim intents above route to a confident decision (or a correct
  explicit pointer) on the live binary; then re-measure the headline on the harness under the
  delta-refreeze rule you folded at `2e6fb2808` — re-freeze a comparison cohort, quote BOTH
  ends. A bare "26.6% -> X%" is inadmissible by your own doctrine line.

### 4. comp-drift sweep (P2 — diagnose first; observed, undiagnosed)
- **Defect (observed 07-14, my kill-test; honestly undiagnosed):** every seam returned
  `UNVERIFIABLE (0.0s)` — the sweep may be structurally inert from a normal agent session. I
  verified the mute-timeout VISIBILITY fix only, not the seams.
- **Properties wanted:** root-cause the all-UNVERIFIABLE state; then make the failure loud — an
  all-UNVERIFIABLE sweep exits nonzero with a "this sweep verified NOTHING" banner. An instrument
  that cannot fail is not an instrument (Verification Law 5).
- **Acceptance:** >=1 seam demonstrably verifiable from a plain session, AND the all-UNVERIFIABLE
  path exercised to its loud exit.

### 5. comp-freshness (P2 — make the Monday class structural)
- **Defect:** an entry missing `freshness_basis: trading-day-frontier` silently falls back to
  flat wall-clock hours — the NEVER#1 Monday false-alarm mechanism, currently held off by prose.
- **Properties wanted:** fail-closed basis handling — a missing basis either defaults to the
  trading-day frontier (`lib/trading_calendar.py`, the ONE frontier definition) for
  AUM/holdings/trading artifacts, or refuses the verdict loudly (`UNVERIFIABLE-BASIS`); never
  silent flat-hours.
- **Acceptance (the Monday mutant):** a T-1 artifact last written Friday, evaluated on a Monday
  fixture, must read HEALTHY under default config; the same artifact 3 trading days behind must
  still alarm (over-suppression control — both arms, per your own gate-2 instruction to me).

## Part 2 — the drill tools + the edge graph (Andrew's asks)

### 6. comp-gitdrill (new tool)
Node -> the TIME axis of its producer. Given any estate graph node, resolve to its producing
source file(s) via the existing graph, and drill: vintage-stamped commit history (hash, date,
author, subject), `--at <ref>` to view/diff the producer at a vintage. Read-only. Every output
line carries its commit-ish — the "a line citation without a vintage is not a citation" rule
made mechanical.
- **Acceptance:** drill a known node (e.g. a gold script the graph maps) and the history matches
  `git log` ground truth; `--at` on a historical ref reproduces the blob (`git show` parity).

### 7. comp-icedrill (new tool — with one substrate caution)
Artifact/data node -> its VERSION/PARTITION history across the substrates we actually have:
dated S3 partitions, S3 object versions where enabled, the DynamoDB daily buckets, graph
vintages. Provenance header prints WHICH substrate answered and its completeness (a partition
series is not a full version history — say so, never imply more than the substrate carries).
- **CORRECTED 2026-07-14 ~04:2xZ (supersedes the caution as first committed):** Iceberg IS in
  the estate — scoped. The ESTATE GRAPH is versioned to Iceberg tables via pyiceberg + a Nessie
  catalog (`comp_aws_cli.py` `commit_to_iceberg` / `comp-aws iceberg-commit`; deployed layer
  `infra/aws/lambda/layers/pyiceberg-nessie-deps/`). The DATA pipelines are NOT on it
  (corrected scan: 0/797 files under `data/`). My original "zero real hits" claim came from a
  flawed invocation — `comp-grep -il "iceberg" ...` searched for the literal pattern `-il`
  (comp-grep is pattern-first); the two "spurious matches" I quoted contained `-il`, not
  iceberg, and I failed to ask why they matched at all. Re-taken correctly this turn.
  **Consequence for icedrill: BETTER than first thought** — graph-node vintage history is
  drillable from the Nessie-cataloged Iceberg tables TODAY; the substrate-adoption question
  remaining for Andrew is only whether DATA artifacts ever move onto it. v1 = Nessie/Iceberg
  for graph vintages + S3 partitions/DDB daily buckets for data artifacts.
- **Acceptance:** drill a known artifact (e.g. an mdpf/platinum key or a silver partition
  series) and the vintage list matches a live `s3 ls` / DDB read taken independently.

### 8. Repo-wide Python dependency edge graph (closes F-5 as a side effect)
Import edges + function-call edges + egress edges (HTTP `requests`, boto3) across ALL repo
Python INCLUDING `.tools/` and `org/modules/` — the current trace-graph blindness (COMPRAIL
F-5, backlog-filed). Queryable through the existing surfaces (comp-blast / comp-kuzu), not a
new query dialect.
- **Acceptance (the F-5 exemplar):** `comp-blast comp-which` finds its real consumers (today:
  NOT-FOUND while 7 exist). Positive + negative controls: a known-isolated module reads empty
  WITHOUT the F-5 disclaimer firing falsely.

## Part 3 — comp-debris (Andrew-direct add, 2026-07-14 ~04:2xZ, same channel)

**Sovereign words (VERBATIM):** *"Another thing I really want to figure out is how we can use
comp-heat or comp-drift or comp-dups, something, to figure out deprecated resources... especially
half-finished, half-deployed, same name but old or untouched or stale resources that float
around, which is endemic with AI coding and iteration."* → *"yeah comp-debris is an interesting
tool idea actually, literally just scanning for cloud resources that havent been invoked in a
long time, the least invoked ones ranked from coldest down or something."*

**Context:** the deprecation wave follows the opal-data-assets monolith cutover (the base
group's current build — ALL partner/asset ETL into one S3). Sequencing note, surfaced not
adjudicated: per-surface deprecation should key off the never-widen parity gate ("multi-day
CLEAN streak IS the cutover gate" — already a filed friction intent), never off the calendar.

### 9. comp-debris (new tool — REFINED by Andrew same channel ~04:3xZ: keep v1 SIMPLE)
**Sovereign refinement (VERBATIM, three messages):** *"There should still be a comp-debris or
something which is just checking cloudtrail and organizing resources by oldest last invocation"*
· *"i feel like that is just obvious and easy to do"* · *"then you can always run comp-heat
federated and comp-dups on those items for further confirmation"*.

**v1 CORE (build this, plainly):** CloudTrail-driven inventory — enumerate cloud resources,
attribute each its most recent CloudTrail event (last invocation / last touch), sort
**oldest-first**. That is the tool. One honesty line, not gold-plating: where CloudTrail is
structurally blind (management-event history is ~90d; S3/Lambda data-plane events only if the
trail logs data events), the row reads `UNKNOWN-beyond-window` / `UNKNOWN-not-logged` — never
"cold" (no-datapoint != never-invoked). Cheap CW-metrics fallback per service is fine where it
sharpens a row.

**CONFIRMATION PASS (pipeline, not built-in fusion):** the cold tail then gets run through the
existing instruments for corroboration — per Andrew, that is a second step you run ON the
candidates, not machinery inside comp-debris:

  | Axis | Existing instrument it consumes |
  |---|---|
  | last-invoked (Lambda/rules) | comp-trigger fired-evidence + CW Invocations metrics |
  | last-read (S3) | comp-whoread live read evidence + last-write mtime |
  | dead-twin / same-name-but-old | comp-dups (BM25 dup/dead-twin, --validate-dead, class filters) |
  | half-deployed | comp-pipescript deployed (MATCH/STALE/MISSING) + comp-lambdamap parity |
  | half-finished (repo side) | comp-heat drift (writes not in a commit) + comp-heat freshness cold-subtrees |
  | code-heat x asset join | comp-heat federated (Trino, graph-joined) — the nearest existing ancestor |
  | zero-consumers (graph) | comp-blast / comp-kuzu (WITH the F-5 disclosure until item 8 lands) |
  | dead credentials | comp-deadgrant |

- **Properties (v1, trimmed to the refinement):**
  a. Oldest-last-invocation-first listing; every row: resource ARN/name, last event, event
     source, AGE, and the lookback window it was measured in. ADVISORY-ONLY — never deletes,
     never disables; any reap stays human + never-widen-gated (CLAUDE.md NEVER#2/#3 class).
  b. **UNKNOWN is a band, not cold** (as above — the one non-negotiable carried from the
     original property set).
  c. Hold-aware: INF chain + frozen three flagged HELD in inventory, excluded from any
     reap-candidate framing.
- **Acceptance:** known-hot control ranks hot (e.g. access-anomaly-scanner, FIRED 72x/3d);
  a no-visibility resource lands UNKNOWN, exercised; held-exclusion exercised on an INF name.
- **Live pre-validation of the confirmation pass (CVO~Z ran both tools 2026-07-14 ~04:3xZ,
  Andrew-directed):** `comp-heat federated` → 329 cold / 38 warm / 7 hot estate files (the cold
  ocean is real); `comp-dups` → 8 TF EXACT-label collisions (two-states-one-resource class:
  `events_invoke_ssm` role+policy declared in BOTH canonical-schwab-ec2 AND
  canonical-schwab-si2-schedule; `bd_exporter` role/SG/instance-profile in BOTH
  infra/aws/ec2/bd-exporter/terraform AND infra/aws/terraform/bd-pipeline; `s3_access` in
  bd-exporter AND shared-infra; `allow_eventbridge` in ec2-auto-shutdown-enforcer AND the
  served-guard module; `opal_data_bd` lifecycle in bd-bucket-lifecycle AND bd-pipeline), one
  248-line byte-exact Lambda body dup (`data/smartx/scripts/lambda_smartx_query.py` ==
  `infra/aws/lambda/smartx_query/lambda_function.py`), and TWO norm=1.0 vendored copies of
  `lib/trading_calendar.py` (schwab-bronze-freshness, bd-served-vintage-alarm) — currently
  identical, nothing keeps them synced, and that file is the ONE frontier definition NEVER#1
  depends on. The confirmation layer already finds real debris; comp-debris supplies the
  missing runtime-coldness axis.

---

## Process (per the sovereign command)

1. **CTO~Z:** design, build, TEST — each item ships with its acceptance mutant/control alongside.
2. **Handoff to CVO~Z:** an `ed3686c72`-style brief — every claim mapped to its sharpest re-take
   command, known limits pre-stated. That pattern produced the cleanest verify loop this fabric
   has run; reuse it.
3. **CVO~Z:** /verify, findings to Andrew + you, my numbers win ties. Standing constraints bind
   throughout: everything above is read-only tooling; nothing touches the INF chain, the three
   frozen files, or writes any sentinel; vendor egress untouched.

Sequencing is yours (Part 1 vs Part 2 order, batching, what lands as one PRD vs several). If
any item is better DECLINED-with-reasons (e.g. #4 turns out environmental), that is a valid
outcome — decline with the citation, per the backlog's own closure rule.

— 3.0.0_SA_CVO~Z
