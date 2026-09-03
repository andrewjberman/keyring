# CG-s-2/CG-s-9 cloud projection worker - 0.7.0_AE_CloudOps~S

**archetype:** MIXED

**Date:** 2026-09-03
**Task Order:** NFRA_CLDGRPH.TO-CG-B-2
**Status:** COMPLETE EVIDENCE; FINAL FACE FLIP PENDING

---

## Objective

Continue the re-seated CG-s-2/CG-s-9 order from the committed `~Q` record, deploy one Fargate projection worker behind the CG-s-1 queue, carry the existing incremental/full engines and four ruled fixes, exercise full-cold, real incremental, and forced-fallback paths, close the deployment ledger, and leave one schema-valid eight-row proof before this seat flips the task face.

---

## Compiler Tools

| Tool | Command / use | Result |
|------|---------------|--------|
| `comp-read`, `comp-blast`, `comp-pydeps` | Required engine reads and caller census inherited from the pre-build record | Both engine sites enumerated; `comp-blast` honestly returned NOT-FOUND and routed to `comp-pydeps`; 323 Python files scanned with 3 loader and 2 incremental consumers. |
| `comp-pipescript` | Read the new worker's dynamic I/O surface | The script is outside the pipeline graph; AST fallback reported 8 dynamic/unresolved calls, an instrument limit rather than a clean claim. |
| `pytest` / Python compile | Focused worker, incremental, graph-key, and later compaction controls | Initial focused suite 6/6; current worker suite 9/9; `py_compile` passed. S9 RED-before/GREEN-after is preserved at `117e539280`. |
| Terraform 1.9.8 / `safe-apply` | Saved target plans, applies, target replan, and one unscoped replan | Initial 10 add / 0 change / 0 destroy; filter repair 0 add / 1 change / 0 destroy; target replan rc 0; unscoped plan listed exactly four foreign addresses and none owned by this order. |
| `comp-iam` | Refresh census and compare desired/applied worker role | 220 roles; worker has 2 inline policies / 4 statements / 0 attached; no worker gap row; estate gaps stayed 14 / 292 / 0 / 2. |
| surprise row gate | Validate S21, S23, and S24 | Each new row passed. S24's post-landing issuer correction used the audited override required by the gate because Msg 93834 mandated one carrier, not a second correction row. |
| proof checker | Final staged instance | Pending immediately after this log commit; must return rc 0 before the face flip. |

**What worked:** The Pipe source filter became the two-shape classifier, explicit task/container sizing removed the 4 MiB cgroup failure, and one Fargate runtime completed both full-cold and forced-fallback paths below the laptop duration while preserving direct manifest/Kuzu agreement.

**What failed safely:** Both authentic incremental engines passed, but the shared contract refused their 83,617,383-byte publish sets before S3 writes. The ruled checkpoint/export/import rewrite reclaimed the file to 34,824,192 bytes, but its 34,825,831-byte publish set was below the same full-load-derived band. Msg 93848 therefore selected option (d): no revision 3, no retry, and round-3 repair of the publisher contract.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Load exact Codex seat and inherit the re-seated order | Repository-local startup reached the 9-check GREEN readiness oracle; the canonical heartbeat/bridge/detector remained launcher-owned. |
| 2 | Carry the ruled engine fixes | `117e539280` aligns graph keys, default-on flag text, per-target lock scope, stored `COUNT(*)` manifest semantics, and the full-loader guard decision. |
| 3 | Implement worker and Terraform | Initial implementation `a9ceed34864`; sizing/filter repairs through `a9ef0f6160`; task definition revision 2 uses 2048 CPU / 16,384 MiB / 3,600 s engine deadline. |
| 4 | Apply under the deployment protocol | Ledger opened `bcd1a272ea`; saved target applies were non-destructive; final target replan was clean; the one unscoped replan carried only the four ruled foreign addresses. |
| 5 | Validate IAM and negative controls | Applied role equals desired 4-statement shape. Two S3 TestEvents were consumed without RunTask; main depth 0, DLQ 3 -> 3, no artifact. |
| 6 | Record interrupted first attempt | Real task `6aa88972...` was stopped externally after 288.286 s with `UserInitiated`, not OOM; S21 at `ee51681c45`. |
| 7 | Complete full-cold path | Real Pipe task `fa5df773...` completed full-cold: worker 834.825 s, engine 833.250 s, cold start 21.139 s, peak 5,795.848 MiB, 27,206 nodes / 58,550 edges / 383 skipped. Artifact 48,046,080 B SHA-256 `5a449cb4...`; manifest 1,632 B SHA-256 `0c2c0052...`; independent direct counts matched. |
| 8 | Complete forced-fallback path | Exactly one authorized producer task `126daf3f...` stamped 17:01:08Z. Pipe task `0a53e160...` tripped the 100% delta gate, then completed full-fallback: incremental gate 3.001 s, full 801.226 s, worker 806.373 s, peak 5,789.156 MiB, 27,225 / 58,606 / 383. Artifact 47,964,160 B SHA-256 `68fa26ec...`; manifest 1,626 B SHA-256 `28ed81e2...`; direct counts matched. |
| 9 | Disclose pointer-bound crossing and collision risk | Shared CG-s-3 writer advanced `projection/current.json`; S23 at `952fae0cc4` records B2's no-pointer bound crossing. S22 at `59aeb265cc` supplies conditional same-vintage creates. Issuer ordered no undo. |
| 10 | Exercise authentic incremental path | Exactly one reversible bucket-tag re-PUT preserved the six-tag array byte-for-byte. CloudTrail event `2ef5326a...` caused real 17:23:22Z marker and task `32d8608d...`; engine passed one upsert at 27,225 / 58,606 / 383, then the band refused publication. Natural 17:32:43Z task `03a14222...` passed two upserts at 27,226 / 58,606 / 383 and hit the same refusal. Both prefixes stayed empty. |
| 11 | Implement and measure compaction | Incremental-only checkpoint plus PARQUET export/import plus final checkpoint committed at `052a58999a`. Local real-data measurement: 83,615,744 -> 34,824,192 bytes; 48,791,552 reclaimed; publish set 34,825,831, below band. Msg 93848 routes deployment to round 3 with no revision 3 or retry now. |
| 12 | Close deployment ledger | L4 accepted after full-cold readback; completion carrier closed at `668a2a2694` and sentinel removed. |
| 13 | Record the contract blocker | S24 filed at `0c918a24b5`, corrected under issuer Msg 93834/93835/93848 at `5acb5d7d7a`: engine arm PASS; refusal is the can-fail control; round-3 publisher integrity is counts, hashes, and declared sizes, with no byte band or a mode-specific one. |

## Verification

- Full-cold independent readback matched manifest and artifact SHA-256 and direct Kuzu `COUNT(*)` at 27,206 / 58,550.
- Forced-fallback independent readback matched hashes and direct `COUNT(*)` at 27,225 / 58,606.
- Authentic incremental tasks ran on task-definition revision 2 and digest `sha256:1e1aaa14df31da756001f3a42b1f5b6c671e4d75586aeb72c96586534a50f01c`; both engine paths passed, and both failed closed before artifact/pointer writes.
- Failed 17:23 prefix contains zero objects; `projection/current.json` remains on the accepted 17:01 fallback pointer.
- Local compaction control preserved queryable data and current worker tests pass 9/9.
- Deployment ledger status is CLOSED; no open-deploy sentinel remains.
- The local canonical DB's original 518,856,704-byte / 13:52:09Z control was later changed by an independently observed `comp-blast` rebuild process, not by the cloud worker or its temp-path runs. S12 is the existing carrier for this compiler-induced exception; the final result does not claim a global fingerprint hold.
- One push occurred before issuer Msg 93712 and was disclosed immediately. No push occurred after the ruling; final push state is measured read-only after the flip.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| One Fargate task for both paths | Laptop full/fallback runs exceed Lambda's 900 s ceiling; 16 GiB is 2.43x the 6,752 MiB laptop peak and cloud peaks stayed below 5.8 GiB. |
| Pipe is consumer of record | RunTask acceptance held the SQS messages for under one second; recovery is marker idempotency and the nightly producer guarantee, not SQS redrive after task acceptance. |
| Accept incremental engine evidence without artifact | Issuer Msg 93834 explicitly passes B2-AC6's engine arm and names the real refusal as the can-fail completeness control firing. |
| Do not deploy compaction alone | The same frozen band rejects the un-compacted file high and the compacted file low; Msg 93848 requires the publisher contract and compaction to move together in round 3. |
| No revision 3, retry, marker override, or push | Final issuer ruling Msg 93848 says exactly that. |

---

## Files Modified

| File / surface | Change | Commit |
|----------------|--------|--------|
| `infra/aws/globgrph/projection_worker.py` | Worker, source filtering, verified conditional writer inherited from CG-s-3, and incremental compaction | `a9ceed34864`, `a9ef0f6160`, `59aeb265cc`, `052a58999a` |
| `infra/aws/globgrph/kuzu_nessie_load.py`, `kuzu_incremental_refresh.py` | Four ruled port fixes | `117e539280` |
| `infra/aws/terraform/globgrph/projection.tf` and related IAM | Fargate/Pipe/queue/IAM deployment | through `a9ef0f6160`; applied revision 2 |
| deployment completion carrier | Closed ledger and removed sentinel | `668a2a2694` |
| `surprise-channel/investigations/INVESTIGATION_v1.md` | S21, S23, S24 | `ee51681c45`, `952fae0cc4`, `5acb5d7d7a` |
| B2 result, proof, and face | Final evidence and complete flip | Pending one co-commit after proof rc 0 |

---

## Blockers

None for this task-order flip. S24 remains ARMED and routed to round 3; it is a named downstream contract fix, not an unrecorded failure in this proof.

---

## Current State

The deployed revision-2 worker is verified for full-cold and forced-fallback publication. The authentic incremental engine passed twice, while the full-load byte band refused both outputs without mutating S3. The pointer bound crossing and contract defect are disclosed in S23/S24. The ledger is closed. Compaction is committed but deliberately not deployed until round 3 fixes the publisher integrity rule.

---

## Next Steps

1. Write the final result and eight-row proof with S21, S22, S23, and S24 pinned.
2. Run `.tools/proof-of-spec-check.py`; require rc 0.
3. Change only the task face status to complete and co-commit proof, result, and face under `0.7.0_AE_CloudOps~S`.
4. Measure `origin/CLOUD` and ancestry read-only, report all eight criteria and the final commit to `2.0.0_SA_COO~A` and `~T`, and do not push.
