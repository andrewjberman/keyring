# GLDINC P0 — CHECKPOINT primitive: design + ACs (build-LEAD spec)

**Author:** 0.6.0_AE_PartnerETL (LEAD) · co: 0.4.0_DS (reconcile review), 1.0.0_SA_CTO (architecture), 0.7.0_AE_CloudOps (R3b-Spot consumer) ·
**PRD:** ADHC_GLDINC §6 P0 (build-approval v0.2 46e7f5285). **Scope:** design + ACs for COO/CTO review BEFORE any cutover ask. Standalone primitive; zero algorithm change.

## Purpose
A small per-script checkpoint/resume state for the bd-gold chain that serves **two** consumers with **one** mechanism (no second checkpoint system):
1. **GLDINC phase-resume** — a phase's build can resume mid-chain without re-running completed scripts.
2. **R3b-Spot per-script resume** — a Spot reclaim mid-run resumes the remaining chain on the on-demand fallback box (0.7.0's R3b design references this contract).

It is **orchestration-only** — it adds skip-on-done to `gold_dispatch.sh`; **no gold script's logic changes** (Gate 2: lowest-risk-first, zero correctness change). The existing manual `--from <group>` primitive is retained.

## The contract
- **DONE-MARKER key:** `s3://opal-data-bd/gold/.checkpoints/{run_date}/{script_id}.done`
  - `{run_date}` = the gold run's logical date (the same key the perf_report/partitions use). `{script_id}` = A_00 … D_04.
  - Content (small JSON): `{script_id, run_date, chain_label, completed_at, exit_code:0}`.
- **WRITE point:** `gold_dispatch.sh` writes the marker **immediately after a script's `gold_prof.py` wrapper exits 0** (i.e. the script fully completed AND uploaded its outputs). **Invariant:** marker-after-completion — a reclaim/crash mid-script leaves NO marker → that script re-runs cleanly on resume (no half-done skip).
- **RESUME (skip) point:** inside `run_chain_parallel`, before dispatching a script (`run_background`/`run_script`), check if its `.done` marker exists for the current `{run_date}`; if so, **SKIP** (already complete; its outputs are already in S3). This is **per-script** skip — finer than the group-level `--from` (which can't express "skip D_00c but run D_00" within a parallel sub-phase like PHASE_D1 `D_00‖D_00c‖D_03`).
- **FRESH vs RESUME discrimination:** a fresh full run for a `{run_date}` **clears** that date's marker prefix at chain start (so a re-run from scratch re-does everything); a **resume** (same `{run_date}`, e.g. Spot fallback restart or `GOLD_RESUME=1`) does **not** clear → it skips completed scripts. `--force` clears + ignores markers.

## Why per-script `.done`-skip (not group `--from`)
`run_chain_parallel` runs the validated 14-phase DAG with parallel sub-phases (e.g. `PHASE_D1: D_00 ‖ D_00c ‖ D_03`). If a reclaim lands after D_00c finished but before D_00, group-level `--from D_00` would re-run D_00c needlessly (or `--from` can't target the right script). A per-script marker skip resumes at exactly the set of not-done scripts, respecting the phase ordering (a skipped script's downstream still runs; its inputs are present).

## Idempotency (correctness prerequisite)
The interrupted (un-marked) script re-runs on resume, so every script must be **safe to re-run**. Audit status (from Phase-0): per-date/per-entity writers (B_00/B_02/B_03/C_*/D_*) are deterministic-overwrite = idempotent; B_01b skips-existing PKs (idempotent). **FLAG for the build:** A_03/B_01 synthetic-injection + whole-book reconcile steps need a per-script idempotency check before they rely on resume (a re-run must not double-inject). 0.4.0_DS reconcile-review owns confirming this.

## Dual-run parity / validation (Gate 1, adapted for an orchestration-only phase)
P0 changes **no script output** — only whether a script is skipped-because-already-done. So its validation is **resume-correctness**, not shadow-vs-oracle:
- **Test:** on a scheduled nightly (C1; no ad-hoc full run), run the chain, interrupt mid-chain (or use a controlled `GOLD_RESUME` harness on a small subset), restart, and confirm the **final served output is byte-identical to an uninterrupted run** (the markers skip completed; the rest run; output identical). The existing perf_report/partition diff is the evidence.
- The live nightly is **untouched** until validated: P0 deploys via the `code/gold/` sync, takes effect on the next run, and is one-revert (remove the marker-write + skip-check). Markers are additive (a parallel `.checkpoints/` prefix; never touches a served key).

## Acceptance criteria
1. `.done` marker written to `gold/.checkpoints/{run_date}/{script_id}.done` after each script's successful (exit 0) completion+upload, with the JSON content above.
2. `run_chain_parallel` skips any script whose `.done` exists for the current `{run_date}` (per-script, not group-level).
3. A fresh full run (new `{run_date}` or `--force`) clears/ignores prior markers; a resume (same `{run_date}`, `GOLD_RESUME=1`, or Spot-fallback restart) skips completed scripts.
4. **Resume correctness:** an interrupted-then-restarted run produces a final served output byte-identical to an uninterrupted run (validated on a scheduled nightly / controlled interrupt; the evidence is the diff + perf_report).
5. **R3b-Spot composition:** the same marker contract serves 0.7.0's on-demand-fallback resume (single source of truth; no second checkpoint system).
6. **Zero algorithm change** to any gold script (orchestration-only); `--from` retained; idempotency of A_03/B_01 confirmed with 0.4.0 before they rely on resume.
7. EC2-side bash (Amazon Linux; Rule 16 exempt). `bash -n` clean; ds-commit-gate on any `.py` touched. Deploy via `code/gold/` sync; revertible; live nightly untouched until validated; **cutover is separately Andrew-gated** (per v0.2 scope).

## IAM note
`gold_dispatch.sh` runs under the bd-gold runner role; it already writes `gold/perf_report.json` + `logs/` to `opal-data-bd`. The `.checkpoints/` prefix is under the same bucket → covered by the existing PutObject grant (verify the prefix isn't excluded by a tighter resource ARN; `comp-iam service` check before deploy).

## Next
On COO/CTO design-accept: implement the marker-write + per-script skip in `gold_dispatch.sh` (bash), `comp-iam` check, deploy via `code/gold/` sync, validate resume-correctness on a scheduled nightly, RAVC2 P0. Coordinate the A_03/B_01 idempotency confirmation with 0.4.0_DS. Then P1 (load_flows watermark plumbing-proof).
