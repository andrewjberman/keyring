# NFRA_FEDOBS P1 CORE -- design (federate the 5 shipped observers over C0/C1)

**Author:** 0.5.0_AE_OpalETL (Trino/Iceberg federation lead) | **TO:** COO 20260707T110412Z | **Date:** 2026-07-07
**Arch-gate:** 1.0.0_SA_CTO | **Refs:** NFRA_FEDOBS_PRD.md (charter), NFRA_CSE_PRD.md (the log), NFRA_GLOBGRPH_PRD.md (the store + cost locks), NFRA_TOOLHEALTH.json (the re-homed EFFECTIVE axis)
**Boundary:** P1 = federate + prove the horizontal join. NOT the observation library (P2) nor the reflective surface (P3). The DS/DE query-library lane (0.4.0_DE) is ANDREW-PARKED; this is the CORE only.

## 1. What P1 CORE is
Stand up the federated analytical surface that JOINS, in one query, (a) the C0 Iceberg CSE event-history, (b) the C1 runtime graph (current state), and (c) the 5 shipped observers' findings -- proving the HORIZONTAL cross-producer correlation none of the 5 can do alone. FEDERATE-not-build: wire the observers' EXISTING outputs; never re-implement observation. READ-ONLY on semantic truth (only PROMOTE writes).

## 2. Grounded reality (what exists today -- federate-not-build is real)
- **Store (live):** `s3://opal-313476888478-globgrph`, Iceberg-on-Nessie (warm Fargate+DynamoDB); already multi-namespace (`globgrph`/`tool_activity`/`code_heat`); F6 branch-head marker live. (Per my CSE store-consult 28cf707f9.)
- **C1 runtime graph EXISTS now:** `graph_nodes`/`graph_edges`/`graph_contracts` Iceberg tables + the Kuzu projection. Federatable immediately.
- **The 5 observers' outputs are already structured + on-disk (adapter targets, grounded):**
  | Observer | State | Output shape (federation source) |
  |---|---|---|
  | COMPDRIFT | complete | `drift-topology.yaml` (coverage ledger COVERED/PARTIAL/SELF-HEAL/GAP) + `drift_cli.py` findings. *Already models Trino "fan-in seams."* |
  | COMPDIFF | complete | comp-xray / FREEZE-MONITOR structured findings (frozen-but-fresh value-motion) |
  | PIPESCRIPT | complete | named-thread estate traversal (structured resource/producer/consumer rows) |
  | DEBTSCAN | active | **JSON** ledgers (`dups_latest.json`, `*_candidates.json`: score/verdict/tier/a/b/dead_status) |
  | GRAPHS-D8 | active | `D8-findings.md` + `critical-surfaces.yaml` + ledger, **already F6-vintage-anchored** (nessie_commit_hash + snapshot_ids) |
- **tool_activity (live Iceberg namespace):** the TOOLHEALTH substrate; partitioned `source=<producer>` -- the pattern + the home for the re-homed EFFECTIVE axis.
- **CSE log does NOT physically exist yet** (CSE-P2 builds it). See sequencing (S8) -- P1 proves the join on C1 + observer-findings NOW; the C0 arm lights up as the CSE log fills.

## 3. Federation topology
```
  C0  Iceberg CSE event log      (history: how the org evolves)   [gated on CSE-P2]
  C1  runtime graph tables       (current: what the org IS)       [EXISTS now]
  OBS 5 observers' findings ----> observer-findings tables        [adapter, S4]
        |                              |                               |
        +---------- one federated read (SQL) : HORIZONTAL correlation --+
                            |
                    measured signals  ---->  MOTIF (compose) / PROMOTE (validate)
                    (READ-ONLY; never writes semantic truth -- AC2)
```

## 4. The observer-federation ADAPTER (federate-not-build -- the load-bearing P1 mechanism)
Each observer keeps producing its native output; a THIN per-observer adapter PROJECTS that output into one queryable Iceberg `fedobs.obs_findings` table (or a per-observer table under a `fedobs` namespace), keyed for join. **Zero re-implementation of observation logic** -- the adapter reads the finding the observer already emits.

- **Common finding grain (the join key):** `{observer, finding_id, subject_key, subject_kind, verdict, tier/score, vintage (nessie_commit_hash | date), evidence_ref}`. `subject_key` = the ARN / artifact-path / logical-key that also keys the C1 graph nodes (per GLOBGRPH `S4.2` identity rule) -> the join to C1 is by the shared identity, not a fuzzy match.
- **Per-observer adapter (thin, structured-in):** DEBTSCAN JSON -> direct map; COMPDRIFT YAML coverage ledger -> a GAP/PARTIAL row per seam; GRAPHS-D8 already carries the F6 vintage -> map its ledger rows (vintage-join is free); PIPESCRIPT / COMPDIFF comp-tool output -> structured rows. Prose-only fragments (D8 markdown narrative) are NOT parsed -- only the structured ledger/YAML/JSON surface federates (never a fragile NLP parse of prose).
- **Cadence:** adapters run as a bounded landing step (the observer emits -> adapter lands the finding table -> Nessie commit), IN-VPC (the same in-VPC-commit constraint as the CSE log, per my CSE consult C1/C2). Observer findings become a versioned, vintage-anchored, joinable surface.

## 5. The engine + posture -- THE arch-decision for CTO (Trino vs in-process, reconciling two Andrew locks)
The FEDOBS PRD locks **Trino** (decision-table row 1, Andrew charter boundary). GLOBGRPH locks **serverless-light / "no idle Trino/Spark server"** (AC6) and **gates Trino to P4** (the CloudTrail-activity scale). These two Andrew locks must be reconciled -- I do not override either; I surface the reconciliation for the CTO arch-gate:

- **Recommendation (for CTO ruling): Trino as the TARGET federation engine, provisioned ON-DEMAND (Trino-on-Fargate, scale-to-zero between analytical runs) -- NOT an always-on cluster.** FEDOBS queries feed MOTIF/PROMOTE at batch cadence (not latency-critical), so an idle cluster is pure NFRA cost against GLOBGRPH AC6.
- **P1-CORE proof can run on the existing in-process path first (DuckDB-over-pyiceberg + the Kuzu export), which already works on this exact store**, demonstrating the horizontal join at ~$0 while on-demand Trino is stood up for the multi-connector federation scale. This honors the Trino LOCK (Trino is the engine for the federated multi-source surface) without standing up idle Trino at P1. Trino earns its keep exactly where GLOBGRPH said it does -- when federation spans live heterogeneous connectors at scale.
- **If CTO/Andrew rule Trino-from-P1:** provision it scale-to-zero (Fargate), never always-on; register the footprint in the NFRA scorecard (GLOBGRPH S5a discipline).

## 6. The read-only boundary (AC2 -- enforced, not documented)
- The federation engine runs under a **read-only** service role: `s3:GetObject`/`ListBucket` on the `opal-313476888478-globgrph` warehouse + Nessie read-only ref access; **no `PutObject`, no Nessie commit, no Iceberg write** on any semantic-truth table. IAM-enforced (scoped read-only role, the reciprocal of the writers' commit roles).
- FEDOBS OUTPUT (measured signals) lands in a SEPARATE `fedobs.signals` namespace it MAY write -- signals are evidence, NOT semantic truth; the algebra/graph/CSE tables remain writable only by the CSE materializer + PROMOTE. So "FEDOBS cannot mutate semantic truth" is a structural IAM boundary (write-scope excludes the truth tables), not a convention.

## 7. The proof query (AC1 -- concrete, demonstrable on C1 + observers NOW)
Horizontal correlation joining TWO observers + C1 (C0 arm added when the CSE log fills):
> "For every artifact GRAPHS-D8 flags on a critical surface (observer A) that DEBTSCAN also scores as high-tier debt or a dup-collision (observer B), return its CURRENT C1 graph neighborhood (blast-radius) and -- once C0 is live -- its CSE modify/supersede history (churn rate)."
No single observer answers this: D8 knows criticality, DEBTSCAN knows debt, only the FEDERATION joins them to C1 blast-radius + C0 churn. This is the AC1/P1 done-gate.

## 8. Dependencies + honest sequencing
- **CSE-P1 contract:** design against the PUBLISHED contract (CSE_PRD S4.1 algebra + S4.2 CSE shape) -- no wait on the validator (per COO). The join keys (subject identity, vintage) are contract-stable.
- **CSE-P2 (the physical log):** HARD dep for the live C0-history arm. **P1 CORE is demonstrable NOW without it** -- federate C1 + the 5 observer-findings tables + prove the two-observer+C1 join; the C0 arm is designed-and-wired, lighting up as CSE-P2 lands the log. This is stated plainly so "P1 done" is not overclaimed.
- **OPLMCP .05 audit-lake:** wired as the agent/MCP producer-findings source (100%-coverage, nearly free) -- an existing structured lake, same adapter pattern.
- **DE query-library (0.4.0_DE): ANDREW-PARKED** -- out of scope for this CORE; COO dispatches it on DE-clear.

## 9. TOOLHEALTH EFFECTIVE-axis re-home (tracked FEDOBS deliverable -- TOOLHEALTH close-condition-a)
Tool/directive-effectiveness over real agentOps IS a federated observation (CTO-ruled). It maps to the S4.2 **directive-effectiveness** correlation: join `tool_activity` (USED) + `comp-which-rail.log` (RAIL-CONSISTENT) + the COMPPROOF blind-run REACH x USABILITY probe (EFFECTIVE) over the CSE frame -> the per-tool/-directive effectiveness signal. Federating `tool_activity` (already an Iceberg namespace on the store) is the near-free first EFFECTIVE feed. Tracked as a committed FEDOBS deliverable (not limbo); it is the load-bearing "directive-effectiveness" measure (S4.2) that also gates PROMOTE.

## 10. Arch-decisions for the CTO gate (crisp)
1. **Engine posture:** Trino on-demand (Fargate scale-to-zero) as target + DuckDB-over-pyiceberg for the P1 proof -- OR Trino-from-P1 scale-to-zero. (Reconciles the Trino lock with GLOBGRPH AC6; NFRA-scorecard the footprint either way.) **My rec: in-process proof now, on-demand Trino for scale.**
2. **Observer-findings landing:** one shared `fedobs.obs_findings` table (common grain, S4) vs per-observer tables under a `fedobs` namespace. **My rec: shared table, common grain -- simpler horizontal join.**
3. **Read-only boundary:** confirm the IAM split (read-only on truth tables; write only to `fedobs.signals`) as the AC2 enforcement. 

## Disposition
P1 CORE is buildable now: federate C1 + the 5 observer-findings + prove the two-observer join, engine per CTO ruling, read-only boundary IAM-enforced, EFFECTIVE-axis tracked. C0-history arm sequences on CSE-P2. RAVC to COO + CTO for the arch-gate.
