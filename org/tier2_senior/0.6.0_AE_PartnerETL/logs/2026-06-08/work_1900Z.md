# 0.6.0_AE_PartnerETL session log — 2026-06-08 work_1900Z

**archetype:** IMPLEMENT + CERTIFY
**secondary_archetypes:** COORDINATE, DEPLOY

Continued from work_1820Z. Three deliverables this session: (1) NFRA_COMPAWS StepFunctions sub-compiler (13th/final class), (2) GLDINC P0 B_00 CATALOG status / 14-day lookback answer for Andrew, (3) NFRA_GLOBGRPH P1 already complete from prior session.

---

## NFRA_COMPAWS StepFunctions sub-compiler — 13/13

### First build (8c392512d)
CTO schema §3.12 v0.5 (a6cbb5a29) received 191219Z. Built:
- `live_stepfunctions()`: list_state_machines + describe_state_machine; definition_hash via sha256(normalized ASL JSON)[:16]
- `live_sfn_activities()`: list_activities paginator
- CLASSES + _node_arn + _hcl_declared.name_attrs for aws_sfn_state_machine + aws_sfn_activity
- derive_edges(): ASSUMES (execution role), INVOKES (ASL Task Resource ARNs), LOGS_TO, TRIGGERS env-var scan
- score_stepfunctions(): node F1 + attr accuracy (machine_type, definition_hash, tf_managed) + activity 0-node cert
- Oracle: org/modules/graph/aws-shapes/stepfunctions-hand-audit-fixture-v0.1.yaml

Self-reported F1=1.0000 — RAVC2 CVO.

### CVO REJECT: SFN-INVOKES-NESTED-GAP
CVO ran independent boto3 + recursive ASL walk. Found:
- Compiler INVOKES = 9; live truth = 26 distinct Lambda ARNs
- Recall 9/26 = 0.346 -> full-headline F1 ~0.51, FAILS >=0.95
- Root cause: derive_edges() walked top-level States only; 17 Lambda invocations nested inside 2 Parallel blocks (yang-generate-* analytics fan-out + opal-market-* + yang-canon-interlock) were missed
- Oracle also wrong: INVOKES 9 (should be 26), TRIGGERS 0 (should be 2)
- Scorer methodology gap: score_stepfunctions() never scored the edge layer

### Fix (e13e93391) — CVO CERT PASS
- `_walk_asl_states(states)`: recursive generator — Parallel.Branches[].States, Map.ItemProcessor.States, Map.Iterator.States at all depths
- `_sfn_task_invokes(definition_str)`: shared helper returning (state_name, target_arn) for every Task state; handles direct arn:aws: + states::: SDK integration; used by both derive_edges() + score_stepfunctions()
- derive_edges(): replaces inline top-level walk with _sfn_task_invokes()
- score_stepfunctions(): adds INVOKES edge F1 (invokes_tp/fp/fn/precision/recall/f1 + invokes_missed) scored against oracle edges_certified.invokes[].target_arn
- Oracle v0.2: 26 INVOKES (CVO ground-truth list) + 2 TRIGGERS (yang-pipeline-trigger + opal-data-refresh-api via STATE_MACHINE_ARN env var)

Live score post-fix:
  node_f1=1.0000, invokes_f1=1.0000, AGGREGATE F1=1.0000 (PASS >=0.95)
  invokes_tp=26, fp=0, fn=0

CVO re-cert PASS (194817Z). StepFunctions CERTIFIED full-headline 1.00.

**Lesson locked**: node+attr score was correct; self-score structurally could not see the edge gap because the scorer didn't measure it. CVO independent measurement caught it. Edges are the whole point of a graph compiler. Locked as canonical self-score vs independent-cert example.

### NFRA_COMPAWS tally: 11/13 AE-side classes
Remaining: SNS + IAM (0.7.0_AE_CloudOps lane, in-flight). Done-gate closes at 13/13.

---

## GLDINC P0 status — tonight's nightly

### What's active tonight (~23:00Z BD nightly)
| Script | CATALOG flag | Notes |
|---|---|---|
| B_00 | --upload --force | Full run. CATALOG --force-recent-days 14 update is POST-NIGHTLY |
| A_00 | --upload --incremental | FIRST incremental chain run |
| C_06 | --upload --incremental ... | FIRST incremental chain run |

B_00 runs --force tonight (broader than --force-recent-days 14 — re-processes ALL dates). The 14-day CATALOG update is an efficiency change for future runs, not a coverage change for tonight. 49F data fully covered by tonight's full run.

### 14-day lookback scope (Andrew question answered)
- Applicable ONLY to B_00 (directly reads raw BD data subject to restatement)
- A_00/C_06 use watermark-based incremental — different mechanism, no force-recent-days arg
- Full-run scripts (B_01, B_02, ..., Z_*): always recompute from scratch, concept doesn't apply
- A_00/C_06 restatement gap (won't auto-re-run if B_00 reprocesses old dates) = known GLDINC P1 item (LastModified-fingerprint detection, pending)

### Compiler tools run
| Tool | Result |
|---|---|
| py_compile (comp_aws_cli.py) | PASS |
| ruff --target-version py39 | PASS |
| bash -n (gold_dispatch.sh) | PASS (prior session) |

---

## What to check tomorrow (2026-06-09)

### ~23:00Z nightly results (read first thing tomorrow)
1. **GLDINC P1 shadow scorecard** (A_00 + C_06 first incremental run):
   - `key_set_symmetric_diff=0` — incremental produced same key set as full run
   - `row_count_delta=0` — same row counts
   - `exact_match_rate=100%` — byte-for-byte match on output
   - If PASS: CATALOG is clean, incremental is production-safe
   - If FAIL: diagnose before any further nightly

2. **A_00 + C_06 perf delta** (NFRA_COSTAWS scorecard line):
   - Wall-clock: expect significant reduction (skip dates already processed)
   - CPU/worker load: expect proportional drop
   - Log the delta for the NFRA_COSTAWS record

3. **B_00 full-force run**: should be normal. No regressions expected (CATALOG unchanged).

4. **49F / Inflection data**: verify served surface unchanged post-incremental A_00/C_06. Any anomaly = investigate before attributing to incremental.

### Post-nightly action (AE lane)
5. **B_00 CATALOG update** (DS lane item, post-nightly confirm):
   - Once tonight's nightly confirms DS e81cdba85 is deployed (comp-pipescript deployed MATCH)
   - Update CATALOG: `B_00|B_00.canonical_holdings.py|--upload --force` → `--upload --force-recent-days 14`
   - Andrew sovereign: 14-day BD restatement standard (supersedes CTO's 3)
   - RAVC2 DS when committed

6. **MDPF_CADENCE first event-driven gate fire (~10:21Z)**:
   - BD fresh → dispatch + rollup advanced (expected path)
   - BD stale → defer + alarm
   - RAVC2 CTO + COO with result

### Pending (non-AE, blocking 13/13)
7. **SNS + IAM sub-compilers** (0.7.0_AE_CloudOps): needed for 13/13 NFRA_COMPAWS done-gate. Watch for RAVC2 from 0.7.0_AE; no action from this lane.
