# NFRA_CLDGRPH -- surprise channel, REMEDIATION v2 (round 2, laptop fabric)

**Author:** `3.0.0_SA_CVO~C` (repository-local CVO continuation seat for round 2).
**Issued as ONE SLUG at L10:** this file and the `NFRA_CLDGRPH-S25` adjudication row land in one commit.
**Precondition verified here:** all five project task orders are terminal. The three round-2 faces are complete at
`afd94db0ce` (B-1), `ebe85fd69e` (B-2), and `93c26badf8` (B-3); their proof instances independently return
`VALID (rc=0)` with exact criterion coverage 6/6, 8/8, and 6/6. The round-1 V-1 and V-2 faces remain complete with
their valid 6/6 and 7/7 proof instances.

**Round 2 channel:** 14 items (S10 and S12-S24; S11 is vacated). This slug graduates 12: seven remedies completed
in-round and five `SPEC_ERROR -> L6` carries. S16 and S21 are `DISMISSED_WITH_REASON` by S25. Zero
`DECOMP_INVALIDATING`; zero `SCOPE_CHANGE`.

```json
[
  {
    "id": "NFRA_CLDGRPH-S10",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The engine still defaults KUZU_REBUILD_DEADLINE_S to 1800 seconds and describes that as 5x headroom over a six-minute build, although measured laptop builds take 935.500-1001.172 seconds. The round-2 task safely overrides it to 3600 seconds, but the stale inherited default and explanation remain for every caller that omits the override.",
    "evidence": [
      "infra/aws/globgrph/kuzu_nessie_load.py:464-468 at ebe85fd69e still carries the 1800-second default and stale five-times/six-minute rationale.",
      "infra/aws/terraform/globgrph/projection.tf:237-238 at ebe85fd69e explicitly supplies both projection and Kuzu deadlines as 3600 seconds; B-2 proof at ebe85fd69e records full and fallback cloud tasks completing in 806.373-834.825 seconds under that bound."
    ],
    "remedy": "Re-derive and state the engine-level default from the measured duration, correct the stale source comment, and exercise both an explicit-override caller and a caller that inherits the default. Preserve the current deployed 3600-second task override until that engine contract is independently certified.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v2",
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~A", "at": "2026-09-03T19:16Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~A", "round": "v2"},
    "route": "SPEC_ERROR",
    "loop_target": 6,
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S12",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The original face simultaneously forbade canonical-DB access and mandated comp-blast, whose freshness path can rebuild that DB. The issuer narrowed the bound to the port's own code and runs and required the control baseline after compiler-tool execution.",
    "evidence": [
      "TO-CG-B-2:50 at ebe85fd69e carries the issuer amendment: comp-* refreshes are outside the port bound and the canonical fingerprint baseline is taken after mandatory compiler-tool runs.",
      "CG-s-2-9.projection-worker.result.md at ebe85fd69e records the post-preflight baseline and attributes later canonical mutation to external comp-blast activity, not the worker or its temp-path runs."
    ],
    "remedy": "Make the port/runtime boundary explicit and place the canonical-DB control after mandatory compiler-tool calls so the two clauses are jointly satisfiable.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v2",
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~A", "at": "2026-09-03T13:30Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~A", "round": "v2"},
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S13",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "A module-wide Terraform plan mixed six owned creates with four committed foreign changes, including an Andrew-excluded email subscription, making the original adds-only and zero-diff bar unreachable without scope violation.",
    "evidence": [
      "TO-CG-B-1 and its proof at afd94db0ce carry the issuer's scoped amendment and the six-address targeted apply: 6 add, 0 change, 0 destroy.",
      "The post-apply unscoped plan at afd94db0ce contains exactly the four known foreign addresses and none of the six owned addresses; the independent SNS read confirms no email subscription to andrew@opalinvest.com landed."
    ],
    "remedy": "Apply only the six owned addresses, then verify with one unscoped address-list control that all six disappeared and exactly the four known foreign changes remain.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v2",
    "disarm": {"state": "DISARMED", "owner": "2.0.0_SA_COO~A", "at": "2026-09-03T13:30Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~A", "round": "v2"},
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S14",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "EventBridge Pipes, not the ECS task, receives and deletes the SQS message when RunTask is accepted; task-duration visibility and task-owned redrive semantics were therefore false for the selected mechanism.",
    "evidence": [
      "B-2 runtime decision at 799e2dad0a states that the Pipe is consumer of record, marker idempotency plus the nightly producer is the retry contract, and queue visibility is based on the measured Pipe hold.",
      "B-2 proof at ebe85fd69e records two measured Pipe holds of 0.734-0.766 seconds and the deployed queue visibility of 30 seconds."
    ],
    "remedy": "State the Pipe as consumer of record, size visibility to its measured API hold, and state marker idempotency plus the nightly real stamp as the recovery contract.",
    "owner": "0.7.0_AE_CloudOps~S",
    "round": "v2",
    "disarm": {"state": "DISARMED", "owner": "0.7.0_AE_CloudOps~S", "at": "2026-09-03T14:30Z"},
    "remediation": {"state": "REMEDIATED", "owner": "0.7.0_AE_CloudOps~S", "round": "v2"},
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S15",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "S3 emits s3:TestEvent without Records; forwarding an unfiltered queue body to the task could launch invalid work or redrive the control event.",
    "evidence": [
      "The final Pipe at a9ef0f6160 uses an exact SQS-body source filter for the real Records bucket/key shape and does not forward the event body as a task environment value.",
      "B-2 proof at ebe85fd69e records two TestEvent controls with main queue empty, DLQ unchanged, no ECS task, and no projection object, followed by authentic marker events that did launch the task."
    ],
    "remedy": "Filter TestEvent at the Pipe source, launch only for the exact real-marker Records shape, and exercise both TestEvent refusal and authentic marker acceptance.",
    "owner": "0.7.0_AE_CloudOps~S",
    "round": "v2",
    "disarm": {"state": "DISARMED", "owner": "0.7.0_AE_CloudOps~S", "at": "2026-09-03T16:20Z"},
    "remediation": {"state": "REMEDIATED", "owner": "0.7.0_AE_CloudOps~S", "round": "v2"},
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S17",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Supplying only environment overrides on the Pipe target caused ECS to use the container's four-MiB default memory instead of the task's intended 16-GiB sizing.",
    "evidence": [
      "The failure is preserved at 6c25fd2adb; the corrected Pipe target at a9ef0f6160 repeats CPU 2048 and memory 16384 explicitly.",
      "B-2 proof at ebe85fd69e records accepted cloud full and fallback peaks of 5795.848 and 5789.156 MiB under revision 2, proving the explicit sizing is deployed and exercised."
    ],
    "remedy": "Carry explicit task and container CPU/memory overrides on every Pipe RunTask request and exercise a real task whose cgroup and ECS description both show 2048/16384.",
    "owner": "0.7.0_AE_CloudOps~S",
    "round": "v2",
    "disarm": {"state": "DISARMED", "owner": "0.7.0_AE_CloudOps~S", "at": "2026-09-03T16:20Z"},
    "remediation": {"state": "REMEDIATED", "owner": "0.7.0_AE_CloudOps~S", "round": "v2"},
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S18",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The Pipe passed the literal token <$.body> to ECS instead of the SQS body, so the task could not consume the intended event shape.",
    "evidence": [
      "The literal-token failure is preserved at 07601c54c9; final target input at a9ef0f6160 removes the payload environment override.",
      "B-2 proof at ebe85fd69e records authentic S3-to-SQS-to-Pipe tasks reaching the worker's pipe-filtered-records path and completing the engine arms."
    ],
    "remedy": "Remove unsupported Pipe target JSON-path interpolation and let the source filter classify a real event before the task reads canonical marker HEAD.",
    "owner": "0.7.0_AE_CloudOps~S",
    "round": "v2",
    "disarm": {"state": "DISARMED", "owner": "0.7.0_AE_CloudOps~S", "at": "2026-09-03T16:20Z"},
    "remediation": {"state": "REMEDIATED", "owner": "0.7.0_AE_CloudOps~S", "round": "v2"},
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S19",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "A second attempted target path, <$.Records[0].body>, was also passed literally; target interpolation could not safely distinguish TestEvent from the real marker record.",
    "evidence": [
      "The second literal-token control and the final exact source-filter design are committed at a9ef0f6160.",
      "B-2 proof at ebe85fd69e records two TestEvents producing no task and authentic real-marker paths launching tasks fa5df773, 0a53e160, 32d8608d, and 03a14222."
    ],
    "remedy": "Perform event classification with an exact Pipe source filter, send only a sentinel to ECS, and read marker HEAD inside the task rather than interpolating a nested target payload.",
    "owner": "0.7.0_AE_CloudOps~S",
    "round": "v2",
    "disarm": {"state": "DISARMED", "owner": "0.7.0_AE_CloudOps~S", "at": "2026-09-03T16:20Z"},
    "remediation": {"state": "REMEDIATED", "owner": "0.7.0_AE_CloudOps~S", "round": "v2"},
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S20",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "comp_aws_cli.py catches a failed S3 notification-configuration read and emits no TRIGGERS edges, making unreadable input indistinguishable from a genuine zero; the live graph is empty for an edge type Terraform declares on three targets.",
    "evidence": [
      "NFRA_CLDGRPH-S20 at 72c0022be8 carries the relayed live zero and source read from NFRA_COMPEFFICACY-S15 at a140eed779, with the cross-project handoff at b5d228fe62.",
      "The round-2 port deliberately did not alter the deriver; a fresh worker would publish the same silent zero under a new vintage."
    ],
    "remedy": "Represent a failed notification read as UNREADABLE rather than zero, derive declared S3-to-Lambda notification targets from Terraform as a second source, and publish read-versus-unreadable denominators on every build.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v2",
    "disarm": {"state": "ARMED", "owner": "2.0.0_SA_COO~A", "at": null},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~A", "round": "v2"},
    "route": "SPEC_ERROR",
    "loop_target": 6,
    "closed": false
  },
  {
    "id": "NFRA_CLDGRPH-S22",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The deployed publisher checks target absence before a long build and then uploads unconditionally, so concurrent same-vintage tasks can overwrite immutable objects last-writer-wins while bucket versioning is off.",
    "evidence": [
      "Conditional create plus byte-identical collision handling and its controls are committed at 59aeb265cc.",
      "B-3 proof at 93c26badf8 explicitly classifies that publisher as committed but not deployed; the two live pointer advances ran digest sha256:1e1aaa14 built before 59aeb265cc."
    ],
    "remedy": "Deploy the conditional-create publisher with the round-3 worker revision, then exercise byte-identical same-vintage no-op and non-identical refusal on the running image.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v2",
    "disarm": {"state": "DISARMED", "owner": "0.7.0_AE_CloudOps~T", "at": "2026-09-03T19:16Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~A", "round": "v2"},
    "route": "SPEC_ERROR",
    "loop_target": 6,
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S23",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The B-2 worker's shared publisher advanced projection/current.json despite B-2's explicit no-pointer bound. The written pointer is complete and valid, so undo would create a second defect, but the deployed image still lacks the ruled conditional writer.",
    "evidence": [
      "S23 at 952fae0cc4 records task fa5df773's exact pointer body and independent artifact/manifest/hash/count agreement; issuer ruling forbids undo.",
      "B-3 result at 93c26badf8 verifies completeness, forward-only and straddle controls in source, while disclosing that the 59aeb265cc fixed publisher has not moved a cloud pointer."
    ],
    "remedy": "Keep the valid live pointer, deploy the B-3 completeness/forward/conditional writer through the round-3 worker revision, and prove one authentic strictly-forward advance with the deployed fixed image.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v2",
    "disarm": {"state": "DISARMED", "owner": "0.7.0_AE_CloudOps~T", "at": "2026-09-03T19:16Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~A", "round": "v2"},
    "route": "SPEC_ERROR",
    "loop_target": 6,
    "closed": true
  },
  {
    "id": "NFRA_CLDGRPH-S24",
    "project": "NFRA_CLDGRPH",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "A fixed band derived from full-load bytes rejects both valid raw incremental output at 83.6 MB and the same graph after safe compaction at 34.8 MB. File size is mode-dependent and is not an integrity property.",
    "evidence": [
      "S24 at 5acb5d7d7a records authentic tasks 32d8608d and 03a14222 passing incremental engine/count guards and safely refusing the 83,617,383-byte publish set with no object or pointer write.",
      "Compaction at 052a58999a preserves a queryable graph and measures 34,825,831 bytes including manifest, below the same band; B-2 proof at ebe85fd69e marks compaction committed and not deployed."
    ],
    "remedy": "Deploy compaction with the fixed publisher and replace the fixed cross-mode byte band with integrity checks over direct counts, hashes, and declared exact sizes, or a separately measured mode-specific diagnostic band; exercise the resulting publisher on a real incremental stamp.",
    "owner": "2.0.0_SA_COO~A",
    "round": "v2",
    "disarm": {"state": "DISARMED", "owner": "0.7.0_AE_CloudOps~S", "at": "2026-09-03T19:16Z"},
    "remediation": {"state": "REMEDIATED", "owner": "2.0.0_SA_COO~A", "round": "v2"},
    "route": "SPEC_ERROR",
    "loop_target": 6,
    "closed": true
  }
]
```
