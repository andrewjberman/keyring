# CVO Session Addendum — 2026-06-12 ~14:45–15:45Z (Andrew-direct stress test block)

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, COORDINATE

Andrew-direct: "0.7.0_AE just finished TO-F3 so we should be able to stress test now." Full verdict: `stress_test_globgrph_concurrency_AC10.md` (dc06744c6). Arc:

1. Ground-truthed the landed stack: TO-F1/F2/F3 + Item-2b delete-propagation all shipped since 13:00Z (Lambda deployed 14:29Z).
2. Live stress: provenance/UNKNOWN-VINTAGE smoke → SNS create/delete probe → S3 bucket probe → 8-way concurrent storm vs genuine BEHIND-by-1.
3. **AC10(a) CERTIFIED · AC10(c) mechanism CERTIFIED** (single-mutex rebuild observed live 15:30:12–26Z, atomic swap, honest BEHIND, no herd).
4. **P0 caught:** 2b's ICEBERG_COMMIT doesn't reach the served HEAD — metadata lineage divergence (c454b6cd scan=1157/probe-absent vs own summary total=2). Routed AE (operational) + CTO (design).
5. **P1s:** no public-API egress (incremental coverage S3-only since 2b shipped — observed lambda+sns timeouts); kuzu_cli.py:55 reader lock collisions (4/4 storm repro). 3 P2s (key-count telemetry, DEBUG-skip invisibility, extract coverage).
6. **CTO ruled same-hour (PRD v0.4.3, 957513885, validated no-defect):** F6 writer-stamped branch-head marker = HEAD oracle; mtime-scan retired; flip stands with mandatory HEAD-ORACLE-PROVISIONAL interim label (micro-patch first); REST-exposure rejected for query path.
7. Status-lag flag to COO: TO-F1/F2/F3 files still `staged` despite shipped+certified work.

Self-corrections owned in the cert: aged the non-operative manifest fields on the first storm; name-sorted (not time-sorted) S3 metadata listing produced one false HEAD-ADVANCED reading. Both caught against ground truth before any finding was routed on them.

## Standing queue (event-driven)
- Verify AE's PROVISIONAL-label micro-patch when it lands (sequenced ahead of the F6 marker build).
- **AC10(d)** marker-oracle demo + **AC10(b) re-cert** on the c454b6cd-class scenario, post-F6.
- AC10(a)/(c) certs stand. TO-F3 live demo still deferred (Nessie REST unreachable from dev boxes — also the asymmetry F6 exploits).
- Carry-overs unchanged: GLDINC containment/gate verdicts tomorrow AM; RV-0034 window accumulating.

## Compiler Tools (addendum)
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-kuzu | canonical + ac7 + 8-way storm (x18 invocations) | AC10(a) header live; 1-of-8 lock collision x4 | storm = the AC10(c) instrument |
| comp-aws snapshot --help | TO-F3 flag surface | present, opt-in | live demo deferred (Nessie REST) |

Probes ledger: log group + SNS topic + S3 bucket, all created+deleted within the block; ledger in the cert.

— 3.0.0_SA_CVO
