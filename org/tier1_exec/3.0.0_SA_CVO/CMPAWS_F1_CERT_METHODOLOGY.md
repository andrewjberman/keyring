# CMPAWS F1 Certification Methodology — the sovereign done-gate

**Author:** 3.0.0_SA_CVO · **Date:** 2026-06-08 · **Status:** v1.0 (Wave-1 proving ground)
**Mandate:** Andrew-sovereign session goal (Stop-hook-enforced, COO 150807Z): every CMPAWS
per-class compiler reaches **≥95% F1 + brittleness-pass**, declared by **CVO-independent cert**.
This doc defines the measurement. It is the *done-gate* — a class is DONE only when CVO measures
it over this bar.

---

## 0. Independence protocol (non-negotiable — the whole point)
- **AE builds the compiler. CVO measures it. The 95% is CVO's number, never AE's self-report.**
- CVO runs the delivered compiler itself, against (a) CVO's own fresh live re-pull and (b) CVO's
  CERTIFIED hand-audit oracle, and computes F1 with CVO's scorer. AE-reported F1 is advisory only.
- The cert artifact (§7) carries CVO's author line. A class is CERTIFIED only on a CVO-signed
  scorecard. This mirrors the S3/IAM-EC2 "AE cross-check → CVO adjudicate" separation, now quantified.

## 1. What is scored — items
A per-class compiler emits a typed graph. The scored **items** are:
- **NODES** — each resource (id/ARN, type, purpose_class, owning-TF-module, provenance/drift-class).
- **EDGES** — each typed relationship (source, target, edge-type) + its provenance/drift-class.
- **PROPERTIES** — the certified per-node/edge attributes (e.g. versioning/PAB for S3; imdsv2/profile
  for EC2; the full normalized statement-set for a bucket policy per the D3 rule).

**Matching key (canonical):** ARN where the resource has one; resolved name/id fallback only where it
does not (per CTO's IE-GAP-3 invariant). Edges match on `(sourceARN, targetARN, edge-type)`. String
fuzz is disallowed — match is exact on the canonical key.

## 2. The two ground-truth references (COO's split — deliberate)
- **Node ENUMERATION + EXISTENCE → scored vs a fresh CVO LIVE RE-PULL.** Live AWS is authoritative for
  "what is actually there." (Volatility handled in §4.)
- **TYPING, RELATIONSHIPS, PROVENANCE/DRIFT-CLASS → scored vs the CVO CERTIFIED ORACLE.** The oracle is
  the certified judgment layer — declared-vs-shadow, edge-taxonomy, full-statement-sets — which a live
  re-pull alone cannot adjudicate. (This is exactly why the hand-audit exists.)

## 3. F1 — definitions
For each item set (nodes, edges, properties), with the §1 matching key:
- **TP** = compiler item that matches a ground-truth item on existence AND all certified attributes.
- **FP** = compiler item with no matching ground-truth item (hallucinated / wrong key / wrong class).
- **FN** = ground-truth item the compiler failed to emit-or-match.
- **Precision** = TP/(TP+FP) · **Recall** = TP/(TP+FN) · **F1** = 2·TP/(2·TP + FP + FN).

**Headline F1 (the 95% gate) = STRICT, per class:** an item is TP only if existence AND typing AND
provenance/drift-class AND certified properties ALL match. Headline F1 is computed over the union of
node+edge+property items (micro-averaged: pool all items, one F1). A mis-typed-but-enumerated node is
NOT a TP — it is an FN against the oracle item (missed-correct) and an FP for the wrong-typed emission.

**Diagnostic sub-F1s (mandatory, for localization — not the gate, but the cert reports them):**
1. **Enumeration-F1** — existence only (did it find the right node/edge SET, ignoring typing).
2. **Typing-accuracy** — of correctly-enumerated nodes, fraction correctly typed.
3. **Edge-F1** — typed relationships only.
4. **Provenance-accuracy** — of correctly-found items, fraction with the correct DECLARED / LIVE-no-
   DECLARED / DECLARED-no-LIVE / drift class. (This is where D3/D4/IE-GAP-3 failures land.)

A class can hit 95% headline only if all four sub-dimensions are high; the sub-F1s tell AE *where* the
missing 5% is (missed nodes vs mis-typed vs mis-provenanced) so the fix is targeted, not blind.

## 4. Volatile / dynamic-set handling (the hpf-fleet problem)
Some live sets churn between pulls (the historical-prices-fetcher fleet: 8→9 within minutes; IE-GAP-1).
Scoring such a set at pinned-member granularity would charge false FN/FP for *correct* behavior.
**Rule:** for an oracle-declared DYNAMIC SET (modeled as a set, not pinned nodes), score at the
**set-class level** — TP if the compiler (a) discovers the set's current live members at run-time and
(b) classifies the SET correctly (e.g. "unmanaged backfill fleet"), regardless of exact cardinality.
Also: **snapshot live at compiler-run-time** and score the compiler against *that* snapshot, not a
later re-pull, to remove pull-timing skew on the volatile delta. Static (non-churning) resources are
scored at member granularity as normal.

## 5. Brittleness criterion (Andrew's "fluid enough to keep up with new resources")
A high F1 on the exact fixture the compiler was tuned to is necessary but NOT sufficient — that can be
overfit. **Brittleness test:** re-measure F1 on a PERTURBED state, with NO compiler code/fixture change:
- **Perturbation sources (any one suffices; prefer natural):** (a) natural live drift between two pulls
  (the hpf churn, an instance start/stop, a stmt added in TF); (b) a CVO-injected synthetic delta in the
  scoring harness (a new shadow role, a removed bucket, a new edge) — injected into the *ground-truth*,
  never the compiler, to test the compiler's *discovery*.
- **Pass = headline-F1 stays ≥95% on the perturbed state with zero code change.** A drop means the
  compiler hardcoded/overfit (the "discover don't hardcode" failure, CTO's invariant) — NOT brittleness-
  passed. This operationalizes Andrew's fluidity requirement: the compiler must *discover + classify*
  new/changed resources, not recognize a frozen list.

## 6. The done-gate (per class)
A per-class compiler is **CERTIFIED** iff, measured independently by CVO:
1. **Headline-F1 ≥ 0.95** vs (live re-pull for existence) + (certified oracle for typing/provenance), AND
2. **Brittleness-PASS** (§5), AND
3. Zero **UNCATEGORIZED/UNTYPED** items (an untyped node/edge is an automatic cert-fail regardless of F1 —
   "everything typed" is Andrew's explicit bar).
Below 95% or brittleness-fail → NOT CERTIFIED; CVO returns the sub-F1 breakdown + the specific FP/FN
items so AE fixes the named gap, then re-measure. No partial credit on the gate.

## 6a. GRAIN sentinel — structural wrong-grain bar (ACCEPTED 2026-06-11, CTO proposal)
**Ruling (CVO methodology authority):** CTO's GRAIN/identity-sentinel proposal is **ACCEPTED** and added
to the done-gate. Motive: AC4's `untyped == 0` (§6.3) **PASSED 23,664 phantom S3_BUCKET nodes that were
S3 object-keys mis-typed as buckets** (AE~B Item-2b, 20×–700× bloat) — they were validly TYPED, so the
untyped bar is structurally blind to **wrong grain**. Typed ≠ correct-grain. These two bars close that
hole; both are **hard-fail**, complementary to (not a replacement for) the F1/oracle/untyped bars.

- **AC-GRAIN.1 — per-class IDENTITY-FORMAT invariant (hard-fail).** Each node class declares an
  id-format invariant; any violation FAILS the run. **Anchor invariant: `S3_BUCKET.node_id` MUST NOT
  contain `/`** — an S3 bucket *name* structurally cannot contain `/` per AWS naming, so a `/` is
  definitionally an object-key-as-bucket (the exact phantom class). Extended conservatively (a wrong
  invariant would false-fail real data — calibrated against the certified-clean baseline where the
  no-slash classes are 0-slash and slash-bearing classes like `IAM_POLICY`/`S3_DATA_KEY`/`LOG_GROUP`/
  `IAM_ROLE`/`PORTAL_COMPONENT` are explicitly NOT asserted). Implemented in
  `org/modules/graph/grain_sentinel.py::IDENTITY_FORMAT_INVARIANTS` (S3_BUCKET, LAMBDA, SQS_QUEUE,
  SNS_TOPIC anchored; extend per class as obvious ones surface).
- **AC-GRAIN.2 — per-class MAGNITUDE band (hard-fail).** Live per-class node-count must fall within
  **[0.4, 2.5]×** of the certified baseline; a 20×+ spike (wrong-grain explosion) or a collapse
  (accidental dedup) FAILS the run — not the eyeball. **Calibration rule (CVO addition):** the baseline
  MUST be **derive-scope-matched** (a cloud-only derive scored against a unioned baseline will
  false-collapse the portal/pipeline classes — observed live). Baseline persisted at
  `org/modules/graph/grain_baseline.json` (per-class counts of the certified graph).

**Proof (2026-06-11, real data):** the sentinel PASSES the certified-clean unioned stitch graph
(`kuzu_stitch_db`, 2901 nodes, 0 violations) and FAILS the phantom graph (`kuzu_nessie_db`, 24,831 nodes)
on **both** bars — AC-GRAIN.1 flags 23,656/23,690 S3_BUCKET no-`/` violations (the incident), AC-GRAIN.2
flags the 696.76× S3_BUCKET spike. Enforced-forever, not fixed-once. Regression test:
`org/modules/graph/test_grain_sentinel.py` (4 cases incl. legit-slash classes NOT flagged). Wired
additively into the comp-aws run via `compute_metrics(...)["grain"]` with a hard-fail (`sys.exit(3)`) in
`cmd_metrics`. Same primitive serves NFRA_GRAPHS D5 (comp-graph) and the comp-aws cert path.

## 7. The cert artifact (what CVO emits per class)
A CVO-signed scorecard: `{class, compiler_commit, oracle_version, live_pull_timestamp,
headline_F1, P, R, {enum_F1, typing_acc, edge_F1, provenance_acc}, untyped_count,
brittleness:{perturbation, F1_perturbed, verdict}, FP_list, FN_list, VERDICT: CERTIFIED|NOT}`.
Persisted under `org/tier1_exec/3.0.0_SA_CVO/cmpaws_f1/` + the verdict MCP'd to AE+COO. The set of
all-classes-CERTIFIED scorecards is the evidence that Andrew's sovereign goal is MET.

## 8. Wave-1 proving ground
S3 + IAM/EC2 oracles are already CERTIFIED (s3 v1.5, iam-ec2 v0.2), so Wave-1 is where this methodology
is proven: the moment AE delivers the S3 + IAM/EC2 compilers, CVO runs them through §0-§7 and produces
the first two scorecards. Any methodology gaps surface here and are fixed before the ~9-class fan-out.
Wave-1 also validates the live-vs-oracle split (§2) and the dynamic-set rule (§4, the hpf fleet is the
natural brittleness perturbation for the EC2 compiler).

---
*The compiler is AE's. The 95% is CVO's. A class is done when CVO says the number — not before.*
— 3.0.0_SA_CVO
