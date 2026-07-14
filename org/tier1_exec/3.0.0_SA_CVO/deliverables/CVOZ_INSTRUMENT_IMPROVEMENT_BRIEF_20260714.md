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
- **CAUTION (surfaced, not adjudicated):** Iceberg is NOT in the estate (verified 07-14,
  comp-grep zero real hits). v1 drills existing substrates. Adopting actual Iceberg is a
  substrate decision for Andrew — surface it separately if you think it's warranted; do not
  fold it silently into the tool.
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
