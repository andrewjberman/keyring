# /spot-check cycle 15 — CLEAN (investigation/design progress)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO · 2026-06-05 ~1727Z · checkpoint 9ff63e0d1 -> faee53001

5 non-CVO commits, all investigation/design/progress — no closeout, no shipped production artifact, no drift:
- GLDINC P0 checkpoint primitive DESIGN (e76fcc671, 0.6.0): per-script .done markers + resume-skip + ACs. The build lane started on P0 exactly per the pre-propagate CLEAN (Gate 4 checkpoint-primitive-first, standalone low-risk). Design-only, production untouched. WATCH: P0 build+parity = the first per-phase RAVC2 surface (CTO routes to me).
- MDPF_COUNTS investigation (5418ad8c0 AE~A + 86d77d8f5 DE~A): ROOT-CAUSED (b)=stale-deployed rollup (S3 code 6-01 pre-W2D, 0 account_count refs vs committed 6de57eddc=8; live partitions carry real counts) + (c)=Global structurally count-less (slice_per_firm). 3-part fix: redeploy rollup (C1-safe, nightly) + author Global aggregate-count + backfill pre-5/18 from smartx parquet (method VALIDATED: 202605-derived reproduce live 5/18 within month-vs-daily drift, Ultra-Short exact 169). Investigation-phase -> queued closeout-verify (1727Z scan).
- AE Aho-Corasick demo ~20x (ac3ec69e9, OUT-scope; 33h->80min ~24.75x, plausible). COO drive cyc13 no-action.

CLEAN — no findings, no fix. Checkpoint advances.
