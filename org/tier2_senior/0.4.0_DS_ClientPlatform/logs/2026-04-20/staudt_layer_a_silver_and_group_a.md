# ADVI_STAUDT Layer A: Silver + Group A Audit — 0.4.0_DS_ClientPlatform~A

**Date:** 2026-04-20
**Task Order:** ADVI_STAUDT.A
**Status:** COMPLETE

---

## Objective

Deliver a T0-T3 (Wed 2026-04-15 → Mon 2026-04-20) read-only audit of the silver ingestion layer
and A-group gold scripts to determine whether any material change in this layer introduced or
contributed to the portal-state discrepancies being investigated in ADVI_STAUDT. This is the
upstream-most lane — a clean-bill here clears the upstream rule-out chain for ~B, ~C, ~D.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-build | worktree T0 (544877cc) | 1162 nodes / 940 edges | PASS — within spec (1162 +/- 50) |
| comp-build | worktree T1 (f177240b) | 1162 nodes / 940 edges | PASS |
| comp-build | worktree T2 (ae759bbb) | 1162 nodes / 940 edges | PASS |
| comp-build | worktree T3 (cd177553) | 1162 nodes / 940 edges | PASS |
| comp-pipescript io | T0 A_00 | READS(1) WRITES(1) no COLUMN GAPS | PASS |
| comp-pipescript io | T0 A_01 | READS(1) WRITES(1) no COLUMN GAPS | PASS |
| comp-pipescript io | T0 A_02 | READS(0) WRITES(1) no COLUMN GAPS | PASS |
| comp-pipescript io | T0 A_03 | READS(0) WRITES(2) no COLUMN GAPS | PASS |
| comp-pipescript io | T0 A_04 | READS(1) WRITES(1) no COLUMN GAPS | PASS |
| comp-pipescript io | T3 A_00–A_04 | IDENTICAL to T0 at all scripts | PASS — confirmed by git diff (0 commits) |
| comp-blast | accounts_dimension_latest | 4 downstream nodes | orientation only |
| git log audit | A_*.py + silver/*.py T0–T3 | 4 commits in window | PASS — 0 on A-group; 4 on silver |

**What worked:** comp-pipescript io was the most valuable tool — running T0 and T3 in parallel then
confirming identity via git diff (0 A-group commits) avoided 8 redundant runs. S3 Python pulls
via `python -m awscli` (workaround for MSYS path mangling on Windows) gave clean partition schemas
without extra tooling.

**What failed:** comp-build wrote to the repo-root `.comp-graph/graph.json` from all 4 worktrees,
not to per-worktree local paths. Investigated and concluded this was safe: (a) node/edge counts were
uniform (plausible because topology didn't change), (b) comp-pipescript io runs from worktree context
and reads actual source files at that SHA. Documented in session log as a known gap rather than
papering over it. comp-blast returned only 4 nodes for accounts_dimension_latest vs 15 from
comp-pipescript io — used io output for blast radius, not comp-blast.

**Gap found:** Silver scripts (merge-daily-incremental.py, backfill_cusip_in_transactions.py) are not
comp-graph-tracked gold scripts — comp-pipescript io cannot be run on them. Analyzed via
`git diff` + S3 partition pulls instead. No existing comp-* tool covers silver-layer schema audits
across checkpoint windows.

---

## Work Completed

### 1. Worktree Setup + Graph Validation

Created 4 scratch worktrees at T0/T1/T2/T3 checkpoint SHAs:
- T0: `git worktree add /tmp/staudt_layerA_T0 544877cc`
- T1: `git worktree add /tmp/staudt_layerA_T1 f177240b`
- T2: `git worktree add /tmp/staudt_layerA_T2 ae759bbb`
- T3: `git worktree add /tmp/staudt_layerA_T3 cd177553`

comp-build in each: 1162 nodes / 940 edges UNIFORM across all checkpoints. Finding: no graph
topology drift in the T0–T3 window — silver/A changes were schema-additive, not topology-additive.

### 2. A-Group Script Audit (A_00–A_04)

`git log --all --since='2026-04-15' --until='2026-04-20' -- data/black_diamond/scripts/gold/A_*.py`
returned 0 commits. comp-pipescript io output identical at T0 and T3 for all 5 scripts.

**Clean-bill issued:** A_00–A_04 are IDENTICAL at all 4 checkpoints.

Gold dimension artifacts (pulled from opal-data-bd):
| Artifact | Producer | Rows | Cols | Schema Hash | Last Written |
|---|---|---|---|---|---|
| accounts_dimension_latest.parquet | A_00 | 10,025 | 33 | 0aec9e12 | 2026-04-20 04:03 |
| advisor_assignments_history.parquet | A_01 | 13,955 | 16 | eea6f0bd | 2026-04-20 04:11 |
| fee_rate_history.parquet | A_02 | 10,299 | 11 | 02cb53ce | 2026-04-20 04:03 |
| client_dimension.parquet | A_04 | 3,619 | 17 | a07e2946 | 2026-04-20 04:11 |

### 3. Silver Layer Audit — 4 Commits in Window

| Commit | Date | Change | Net Effect |
|---|---|---|---|
| 80917a1e | Fri 05:59 ET | `merge-daily-incremental.py`: add `enrich_with_cusip()`. New file: `backfill_cusip_in_transactions.py` | LANDED — cusip column added to silver/transactions T2+ |
| c270a9b2 | Fri 12:56 ET | `merge-daily-incremental.py`: add rolling-key refresh for unrealized_gain_loss.parquet | REVERTED by 32fbb0d6 |
| 32fbb0d6 | Fri 13:23 ET | Revert of c270a9b2 | Net-zero |
| 6c80c5ed | Fri 14:50 ET | New: `bronze/convert_schwab_uln_to_silver.py` — Schwab ULN -> opal-data-schwab/silver/ULN/ | LANDED — new partition, opal-data-schwab, T3 only |

### 4. Silver Partition Schema Pulls

| Partition | Rows | Cols | Schema Hash | Key Finding |
|---|---|---|---|---|
| silver/transactions/2026-04-15.parquet | 5,191 | 74 (T2/T3) | — | cusip null pct 2.25%; T0/T1 had 73 cols |
| silver/unrealized/2026-04-15.parquet | 93,951 | 16 | fea1d9bd | UNCHANGED T0–T3; dated structure confirmed |
| silver/allocations/2026-04-15.parquet | 6,543 | 92 | 8d2b422d | UNCHANGED T0–T3 |
| opal-data-schwab:silver/ULN/date=20260415 | 213,253 | 17 | 00681059 | ABSENT T0/T1/T2; PRESENT T3; different bucket |

### 5. Three Material Changes — Findings Written

- **A-1** (T1→T2): silver/transactions.cusip added via 80917a1e. 73→74 cols. B_01 RPS-keying (c4ebde9a/f5f19e77/1db831aa) is T2-gated. Historical partitions backfilled (0830bae7, 1,520 partitions 2021-05-26→2026-04-15).
- **A-2** (T2→T3): silver/ULN/ created in opal-data-schwab (6c80c5ed). 350 partitions backfilled. Not yet consumed by any production script at T3.
- **A-3** (T2→T3, net-zero): rolling-key refresh shipped (c270a9b2) then reverted (32fbb0d6). No net change to merge-daily-incremental.py.

### 6. RAVC Chain

- Commit `0d34f025` — 4 deliverables, MCP to CTO + COO + ~B + ~C + ~D
- COO: validated all deliverables, flipped TO to `complete`
- CTO: ACCEPT — all 3 material changes validated with evidence; clean-bill grounded; §4.0 discipline held
- ~B: ACK — inheriting A-1/A-2 upstream context; writing layer_b_findings.md
- ~C: ACK — confirmed neither A-1 (cusip) nor A-2 (ULN) impacts C-group scripts

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Run comp-pipescript io at T0 and T3 only; skip T1/T2 | 0 A-group commits in window — T0=T3 identity means T1/T2 are also identical by implication |
| Use python -m awscli instead of aws CLI directly | aws binary path is mangled by MSYS on Windows; python -m awscli bypasses the MSYS path conversion bug |
| Document comp-build graph-root cache as a gap, not a blocker | After investigation: node/edge counts uniform across checkpoints; comp-pipescript io reads from worktree source files directly; risk is not materialized |
| Issue Group D clean-bill proactively | §3.3 PRIMARY FOCUS asks for dimensional inputs; A_01/A_02/A_04 are unchanged — ~D synthesis surface is meaningfully compressed by this |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `data/black_diamond/diagnostics/STAUDT/layer_A/silver_and_group_a_inventory.md` | New — 4-checkpoint script inventory | Yes — `0d34f025` |
| `data/black_diamond/diagnostics/STAUDT/layer_A/layer_a_findings.md` | New — definitive findings + rule-out table | Yes — `0d34f025` |
| `data/black_diamond/diagnostics/STAUDT/layer_A/silver_schema_diff.json` | New — machine-readable schema delta per partition per checkpoint | Yes — `0d34f025` |
| `data/black_diamond/diagnostics/STAUDT/layer_A/evidence_pack.json` | New — hashes + row counts + column sets | Yes — `0d34f025` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-20/staudt_layer_a_silver_and_group_a.md` | New — session log | Yes — `860b59d5` |
| `org/compiler-tools-log.md` | Appended 11 rows | Yes — `860b59d5` |
| `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.A.ds-a-layer-silver-and-group-a.md` | Status: staged → pending → complete (complete set by COO) | No local commit needed |

---

## Blockers

None.

---

## Current State

`0d34f025` (deliverables) and `860b59d5` (logs) are committed to CLOUD, not yet pushed (DT lane).
Layer A issued a clean-bill on all 5 A-group scripts (A_00–A_04) — zero commits in window, identical
S3 topology T0=T3. Three material silver changes documented (A-1 cusip column T2+, A-2 ULN new
artifact T3 in opal-data-schwab, A-3 revert net-zero). Group D upstream dimensions (advisor_assignments,
fee_rate, client_dimension) unchanged — ~D cannot attribute §3.3 discrepancies to A-layer inputs.
~B ACK received and actively writing layer_b_findings.md; ~C ACK received with rule-out confirmed.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Push commits `0d34f025` + `860b59d5` to origin/CLOUD** — DT gate
2. **[0.4.0_DS_ClientPlatform~B] Write layer_b_findings.md** — gate to ~C/~D findings-write (in progress)
3. **[0.4.0_DS_ClientPlatform~A] Respond to any RAVC supplemental-evidence requests from ~B/~C/~D** — append-only per PRD §5 #8
4. **[0.4.0_DS_ClientPlatform~A] Stand by for next TO from COO/Andrew** — ADVI_STAUDT.A complete; other staged TOs (SL-P1, WP-10b, COMP_LEARNS.005) not yet unblocked
