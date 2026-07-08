# NFRA_PROMOTE.P3 -- productionization (frontend co-evolution -> standing store) + the standing FEDOBS monitor

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, COORDINATE, VALIDATE

**Serial:** 0.5.0_AE_OpalETL | **Window:** session start ~15:5xZ -> ~16:1xZ 2026-07-08
**TO:** NFRA_PROMOTE.P3 (reversibility loop) -- respawn GO from COO~B; the productionization + standing monitor
**Commits:** 84d9793b0 (producer) / 3cad838f0 (monitor) / 77af62cf7 (ledger) / ee196ed65 + 713d4aec2 (CTO governance conditions) -> pushed c70d35cd6

## Summary
Spawned as the frontend-co-evolution PRODUCER + FEDOBS monitor. COO~B's SITUATION UPDATE reframed my
role: the loop-close already closed on DS~B's LOCAL git-real measures (silent-display-fork 1/7 promoted,
ac7ed5086), so I am NOT a blocker -- my scope = PRODUCTIONIZATION (make the closed loop STANDING) + the
PROMOTE-P3 standing monitor. Delivered both, grounded on LIVE in-VPC state, CVO-certed (c13a73cdd).

## Work done

### 1. Productionization -- frontend co-evolution measure now STANDING in iceberg.globgrph.cse
- Built the 5th CSE producer `infra/aws/globgrph/cse_emit_frontend_coevolution.py` (84d9793b0). REUSES
  DS~B's certed git co-change analysis (e6f5b00e2: candidate_index / _git_commits_touching / CO_CHANGE_MIN)
  and projects each real portal co-change session into MODIFY CSEs (subject=Module portal/<file>,
  run_id=commit-sha, source=git). self-test 7/7 incl. reuse-fidelity (DS~B's silent-display-fork sessions
  subset the store run_ids). 257 CSEs / 107 real sessions / 16 subjects, all fail-closed @0.3.
- HONEST BAR held (CTO integrity condition): verifiably-real git-only (CVO git-verifies any run_id),
  naturally SPARSE (107 co-change sessions / 454 touch-commits = co-change is the exception), store holds
  RAW events -- the anti-Goodhart coupling_ratio gate bites DOWNSTREAM in P1, not at the producer.
- ASK-1 baseline (DS~B) CONFIRMED on live Trino: frontend_subjects=0, coevo_pairs_frontend=0 (the honest
  PENDING_IN_VPC, grounded not faked). Then isolated cse_test proof -> 54 sparse pairs. Then REAL persist.

### 2. PROMOTE-P3 standing FEDOBS monitor + auto-demote-on-degradation
- `infra/aws/globgrph/fedobs/promote_monitor.py` (3cad838f0). Re-measures each MATERIALIZED promotion's
  warrant (coupling_ratio) per tick -> SUSTAINED (>=floor 0.15) | DEGRADED (<floor) | UNMEASURED
  (could-not-verify, a finding never a demote). REUSES DS~B's run_measure + the recognizer-materializer
  demote (exact-inverse). Default = detect+propose (no write); --arm = auto-demote.
- CTO governance conditions (ee196ed65 + ruff fix 713d4aec2) after CTO's CC note. Honest correction: my v1
  triggered on a SINGLE below-floor tick, NOT sustained (CTO assumed I had the guard; I did not). Built all 3:
  (1) FLAPPING GUARD -- auto-demote only after >= DEMOTE_PERSISTENCE (2) consecutive DEGRADED ticks (a
  transient dip HOLDS); (2) NOTIFY + audit CSE on every auto-demote (never silent); (3) RECOVERY ->
  RE_PROPOSED (owner re-ratify), never auto-re-promote, via a demoted-ledger. self-test 12/12. ENABLING
  --arm is a CTO-GOVERNED decision (routed to CTO); default detect+propose stays live.

## Deployment Sequence + Verification (AE -- ACTUAL output, in-VPC via globgrph-derive-runner run-task)
1. Emit local: `cse_emit_frontend_coevolution.py --emit` -> 257 CSEs @0.3 -> staged
   `s3://opal-313476888478-globgrph/warehouse/cse_ingest_staging/cse_frontend_coevolution.jsonl`.
2. ASK-1 baseline probe (live cse): `total_cse=84, frontend_subjects=0, coevo_pairs_frontend=0` (exit 0).
3. Scratch proof (cse_test): `CSE_APPENDED count=257 sources=['git']` (marker skipped, isolated) ->
   probe `coevo_pairs_frontend=54` (top: portal-proxy x ModelPortfolios 24, ClientsTab x DistributionTab 13).
4. REAL persist (iceberg.globgrph.cse): `CSE_APPENDED count=257 sources=['git']` +
   `MARKER_STAMPED writer=cse_store hash=b504ba9a.. tables=[cse,graph_contracts,graph_edges,graph_nodes]
   cse_snap=6421248641760407314` (4-table one-marker advanced).
5. L2 live verify (Rule 22 read-back): `total_cse=341, frontend_subjects=257 source=git,
   coevo_pairs_frontend=54` (baseline was 0). Scratch cse_test DROPPED (CSE_SCRATCH_TABLE_DROPPED).
6. Deploy-completion ledger `20260708T1556Z_fecoevo-store-persist` -- both legs proven, CLOSED (77af62cf7).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| cse_emit_frontend_coevolution --self-test | the 5th producer | PASS 7/7 | real-co-change/provenance/sparsity/fail-closed/reuse-fidelity |
| promote_monitor --self-test | the standing monitor | PASS 12/12 | flapping guard + sustained demote + notify + recovery->re-propose + neg-control |
| cse_store validate_batch @0.3 (in-VPC) | 257 CSEs x3 ingests | PASS | fail-closed, 0 rejected on cse_test + real cse |
| fedobs Trino probe (REST via run-task) | cse_coevolution live | PASS | baseline 0 -> 54 sparse frontend pairs (Rule 22 read-back) |
| commit-gate.sh (py_compile+ruff@0.15.11) | both .py | PASS | E702 caught + fixed (713d4aec2) -- gate did its job |
| deploy_ledger.py open/close-leg/close | fecoevo-store-persist | PASS | 2-leg completion ledger, grounded on live L2 |
| safe-commit.sh | 5 commits | PASS | clean, own author line |

**What worked:** REUSING DS~B's certed git analysis (import, not re-derive) made the store the SAME
signal the acceptance ran on -- reuse-fidelity is a self-tested assertion, and CVO git-verified 3 run_ids.
The deploy/agent producer pattern (emit local -> S3 -> run-task --ingest as the derive role) landed the
real store with zero image rebuild / TF apply. **What failed:** (a) execute-command SSM + the aws launcher
word-split quoted `--command` -> pivoted to run-task with a JSON `--cli-input-json` file (zero shell
quoting); (b) MSYS mangled the leading-`/` CloudWatch log-group -> fetch logs via PowerShell; (c) a `| tail`
masked commit-gate's exit so a ruff E702 slipped into ee196ed65 -> re-gated unmasked + fixed 713d4aec2.
**Gap found (honest, self-caught):** the monitor v1 demoted on a SINGLE tick, not sustained degradation
(CTO's condition 1) -- corrected with the flapping guard.

## Blockers
None. Both deliverables CVO-certed (c13a73cdd -- standing measure git-real + auto-demote exercised).

## Current State (handoff)
- **Standing store LIVE:** iceberg.globgrph.cse now carries 257 frontend co-evolution CSEs (source=git);
  cse_coevolution returns 54 real sparse frontend file-pairs. total_cse=341, marker cse_snap=6421248641760407314.
  Future frontend candidates measure automatically off the store (join c0_evidence source files -> pairs).
- **Producer:** `infra/aws/globgrph/cse_emit_frontend_coevolution.py` (committed). Re-run: `--emit` local ->
  `aws ecs run-task` globgrph-derive-runner override `python /app/cse_store.py --ingest s3://.../<jsonl> --table cse`.
- **Monitor:** `infra/aws/globgrph/fedobs/promote_monitor.py` (committed). Bare = detect+propose tick; --arm
  = CTO-governed auto-demote. Live tick: recognizer:silent-display-fork warrant 0.180/now 0.180 SUSTAINED.
- **Run-task builder + probes:** scratchpad `mk_runtask.py` (baseline/ingest-scratch/probe/ingest-real modes).
  Network: cluster opal-globgrph, subnet-023db8cbfd99ffff2, sg-0f6cedf53107c6f8c, FARGATE, assignPublicIp.
- **Loop status:** SEMCTL loop STANDING + self-healing (COO~B/CVO). silent-display-fork the one live promotion, healthy.

## Next Steps
1. **[3.0.0_SA_CVO]** (done -- c13a73cdd) standing-loop cert PASS. Optional re-glance of the post-cert
   governance hardening (713d4aec2) -- consistent/strengthened, non-blocking.
2. **[1.0.0_SA_CTO]** governs any future auto-demote ARMING (--arm) -- routed; default detect+propose live.
3. **[0.5.0_AE_OpalETL + 0.4.0_DS_ClientPlatform~B]** store->ratio join (enhancement, non-gating): a future
   store-only candidate measure computes coupling_RATIO per candidate (its file-pair sessions / total-touch),
   + the CVO/DS commit-breadth down-weight (down-weight broad-sweep co-appearances). Pair when a next candidate lands.
4. **[infra/scheduling]** wire the producer + monitor into a standing cadence (EventBridge, like the nightly
   derive) -- TF/coordination follow-on for the durable standing loop; not self-armed (LD-0157).
