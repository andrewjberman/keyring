# CVO Certification — NFRA_GRAPHS D5 grain-sentinel + comp-aws AC-GRAIN (unified)

**Certifier:** 3.0.0_SA_CVO · **Date:** 2026-06-11 · **Verdict: PASS — grain sentinel BUILT, PROVEN on real data, WIRED into the run, and DEFINED as a cert bar. The phantom-node class is now a structural FAIL (enforced-forever).**

## What this closes
- **NFRA_GRAPHS D5 (my leg):** the grain-sentinel cert-integration — an identity/grain ASSERTION that FAILS the run on the wrong-grain phantom class.
- **comp-aws GRAIN methodology proposal (CTO, 2026-06-11):** ACCEPTED + authored into `CMPAWS_F1_CERT_METHODOLOGY.md §6a` with final AC numbering (AC-GRAIN.1 + AC-GRAIN.2). Same primitive, two compilers.

## The hole it closes
AC4's `untyped == 0` PASSED **23,664 phantom S3_BUCKET nodes** that were S3 object-keys mis-typed as buckets (AE~B Item-2b, fixed-once at `b723f3ea1`). They were validly TYPED → the untyped bar is blind to wrong-grain. Typed ≠ correct-grain. The sentinel makes wrong-grain a structural FAIL on every run.

## Deliverables (all gate-clean, Rule-14 PASS)
- `org/modules/graph/grain_sentinel.py` — reusable validator (comp-aws `arn`/`type` + comp-graph `node_id`/`node_type` node shapes).
- `org/modules/graph/test_grain_sentinel.py` — 4-case regression (incl. legit-slash classes NOT flagged).
- `org/modules/graph/grain_baseline.json` — certified per-class baseline (26 classes, from the clean unioned stitch graph).
- `org/modules/graph/comp_aws_cli.py` — `compute_metrics(...)["grain"]` additive field + `cmd_metrics` hard-fail (`sys.exit(3)`).
- `CMPAWS_F1_CERT_METHODOLOGY.md §6a` — the two bars defined as done-gate additions.

## The two bars
- **AC-GRAIN.1 (identity-format, hard-fail):** per-class id invariant. Anchor: `S3_BUCKET.node_id` MUST NOT contain `/` — structurally true (AWS bucket names can't contain `/`), so a `/` is definitionally object-key-as-bucket. Calibrated against the clean baseline so legit slash-bearing classes (IAM_POLICY/S3_DATA_KEY/LOG_GROUP/IAM_ROLE/PORTAL_COMPONENT) are NOT asserted (no false-fail).
- **AC-GRAIN.2 (magnitude band [0.4, 2.5]×, hard-fail):** per-class count vs derive-scope-matched baseline. Catches 20×+ spikes AND collapses. **CVO calibration rule:** baseline must match derive scope (a cloud-only derive vs a unioned baseline false-collapses portal/pipeline classes — observed live; documented in §6a).

## Proof on real data
| Graph | nodes | AC-GRAIN.1 | AC-GRAIN.2 | Verdict |
|---|---|---|---|---|
| `kuzu_stitch_db` (certified-clean unioned) | 2901 | 0 violations | 0 violations | **PASS** |
| `kuzu_nessie_db` (phantom-inflated) | 24831 | 23,656/23,690 S3_BUCKET no-`/` | 696.76× S3_BUCKET spike | **FAIL** |

The sentinel catches the exact 23,664 incident on BOTH bars and passes the clean graph. Regression test green.

## Disposition + honest disclosures
**D5 grain-sentinel: CERTIFIED — built, proven, wired, defined.** The phantom-node class is structurally enforced-forever.
- **Cross-lane touch disclosed:** to land the additive grain wiring in `comp_aws_cli.py` I added one `# noqa: F841` to a PRE-EXISTING unused-var lint debt (`warehouse_uri`, line ~2151, AE~B's iceberg-commit path). It is **reference-only by design** (the existing comment documents it; catalog uses the warehouse *name*, not the URI) — NOT a behavioral bug. Flagged to CTO+AE~B for awareness; the `# noqa` is intent-preserving.
- **Integration point:** wired into `compute_metrics`/`cmd_metrics` (the `comp-aws metrics` surface) as the additive + hard-fail path. The `comp-aws score`/`derive` paths and the comp-graph (`comp-build`) derive should adopt the same `run_grain_sentinel(...)` call — recommended to CTO/AE~B as the follow-through so every graph-producing run carries the bar.
