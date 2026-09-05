# CG-s-3 projection contract Phase A and pre-Phase-B proof - 0.7.0_AE_CloudOps~T

**archetype:** MIXED

**Date:** 2026-09-03
**Task Order:** NFRA_CLDGRPH.TO-CG-B-3
**Status:** COMPLETE

---

## Objective

Define the S3 projection artifact, manifest, and forward-only pointer contract; reconcile the 2,256 duplicate-edge excess; and prepare a schema-valid proof record before the publisher dependency releases Phase B.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `python .tools/comp-read infra/aws/globgrph/kuzu_nessie_load.py --for "the MERGE identity key for edges, the manifest writer and every field it stamps"` | PASS | Located the normalized MERGE identity, post-load stored count, and current manifest writer without rebuilding the canonical DB. |
| comp-read | `python .tools/comp-read infra/aws/globgrph/kuzu_incremental_refresh.py --for "the manifest writer and the post-apply count"` | PASS | Located incremental manifest and post-apply count behavior within the Phase A read-only bound. |
| comp-which | `python .tools/comp-which "where is a git push invocation recorded with its exact timestamp and command in this repository"` | PARTIAL | Correctly reported that no dedicated audit tool matched; the exact Codex rollout carrier was then read narrowly. |
| surprise-row-gate | `python .tools/surprise-row-gate.py org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` | PASS | Checked 1 new row of 15 total; S16 passed schema, ownership, and append-only checks. |

**What worked:** `comp-read` exposed the loader and refresher contract surfaces without running `comp-blast`, preserving the other seat's database fingerprint control. The surprise gate validated the newly filed producer finding.

**What failed:** Bare `comp-read` did not resolve in PowerShell, and `bash .tools/comp-read` treated the Python entrypoint as shell. `python .tools/comp-read` was the correct repository-local invocation. `comp-which` had no dedicated exact push-audit route.

**Gap found:** The compiler-tool forwarder is not usable bare from this PowerShell session even though the repository tool works via its Python entrypoint. No project-spec gap beyond filed surprise row NFRA_CLDGRPH-S16 was found.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read both engine sources under the Phase A bound | Loader and incremental manifest/count behavior pinned; no engine execution and no bounded infrastructure edit. |
| 2 | Write the projection contract | `PROJECTION_CONTRACT.md` defines immutable versioned artifacts, canonical manifest fields, pointer-last publication, reader straddle handling, and S14 recovery. |
| 3 | Reconcile duplicate identities | `61,071 - 383 = 60,688`; `60,688 - 58,432 = 2,256`; split into 13 expected repeated observations plus 2,235 and 8 producer findings. |
| 4 | File the finding | NFRA_CLDGRPH-S16 appended with source owners; surprise-row-gate PASS. |
| 5 | Commit Phase A | `823ea90776e5a8239c8a6b43588330e8cb714ee8`, exact author `0.7.0_AE_CloudOps~T`. |
| 6 | Prior push incident | `git push origin CLOUD` invoked at `2026-09-03T14:11:04.027Z`, completed at `14:11:36.862Z`, rc 0. This crossed Andrew's standing hold; issuer notified and shared-branch law accepted. |
| 7 | Phase B release | Issuer Msg 93769 released the bounded engine edits after ~S reported no further Python edit pending. |
| 8 | Publisher implementation | Pointer/manifest conformance and completeness checks committed at `5bb91c894d`; conditional same-vintage immutability and S22 committed at `59aeb265cc`. Focused tests passed 10/10 twice. |
| 9 | Runtime exercise | Tasks `968bf1a3...` and `fa5df773...` exited 0 on digest `sha256:1e1aaa14...`, publishing vintages `13:23:55.222893Z` then `16:27:39.471730Z`; both logged `pointer_written=true`, `pointer_status=advanced`. |
| 10 | Producer agreement | The released full artifact and a local invocation of the committed incremental engine on the identical pinned graph both produced 27,206 nodes / 58,550 edges / 383 skipped; direct Kuzu COUNT(*) matched both manifests. |
| 11 | Reader/refusal controls | Pointer-manifest-pointer vintages and manifest SHA matched. The 71-byte incomplete prefix and the older complete vintage were both refused with the pointer unchanged. |
| 12 | Boundary accounting | S21 records this seat's out-of-scope stop of B2 task `6aa889...` after 288.286 s at 16:26:35.641Z; S23 records B2 task `fa5df773...` crossing its no-pointer bound. No further B2 task launch/stop or Pipe/queue mutation by this seat. |

## Verification

- Phase A JSON blocks parse successfully.
- `git diff --check` passed for the three Phase A artifacts before commit.
- Surprise gate: `1 new row(s) of 15 total checked`; `OK: 1 file(s)`.
- Focused worker/incremental/key suite: 10/10 passed twice; Python commit gate passed for both changed files.
- AC3 incremental engine: rc 0 in 5.450 s, zero delta, exact manifest/direct agreement at 27,206 / 58,550.
- AC5 reader: pointer1 = manifest = pointer2 vintage `2026-09-03T16:27:39.471730+00:00`; observed manifest SHA `0c2c0052...` matched pointer.
- AC5 backward control: `backward vintage refused: candidate=2026-09-03T13:23:55.222893+00:00 current=2026-09-03T16:27:39.471730+00:00`; pointer SHA `432ec284...`, ETag `3e945885...`, and LastModified unchanged.
- Pre-final no-push measurement: local HEAD `fca007a4cf`, origin/CLOUD `351f309e0a`; local-is-ancestor rc 1. The exact post-final state is measured and reported after the co-commit; this seat does not push.
- Launcher readiness after reload: GREEN, all 9 checks satisfied, exactly one heartbeat, bridge, and detector, with no consuming watcher.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Use the project-tree contract fallback | `docs/architecture` is an ANY_CTO lane and refused this seat; the task order explicitly names the fallback. |
| Define the pointer as a single forward-only `PutObject` after verification | Bucket versioning is off; artifact-first/pointer-last keeps failed partial publishes invisible and supports S14 next-stamp recovery. |
| Classify 13 excess rows as expected and 2,243 as findings | Live and source-code evidence distinguishes repeated EC2 observation from uncollapsed C2 edges and lost EventBridge target identity. |
| Never push from this seat | The load contract and issuer Msg-ID 93713 carry the shared-branch law; only MSTR seats push shared branches on Andrew's terminal word. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/PROJECTION_CONTRACT.md` | Projection artifact/manifest/pointer contract | Yes - `823ea90776` |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/CG-s-3.projection-contract.result.md` | Phase A result, census, handoffs, and explicit Phase B boundary | Yes - `823ea90776` |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md` | Append-only S16 finding and denominator update | Yes - `823ea90776` |
| `infra/aws/globgrph/projection_worker.py` and focused tests | Contract conformance, verified pointer-last writer, and same-vintage immutable create | Yes - `5bb91c894d`, amended `59aeb265cc` |
| `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/NFRA_CLDGRPH.TO-CG-B-3.artifact-manifest-pointer-contract.proof_of_spec.json` | Six-row proof instance, all PASS | Interim `327ab20f58`; final revision in the face co-commit |
| `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-09-03/cg_s3_phase_a_and_proof_1346-1603Z.md` | This complete session record | Final face co-commit |

---

## Blockers

None. The issuer released Phase B in Msg 93769, and ~S relayed the first accepted artifact at 16:44:10Z.

---

## Current State

CG-s-3 is complete: all six acceptance rows pass; the contract and conditional writer are committed; two real cloud publishes advanced strictly forward; full/incremental/direct counts agree; both refusal controls fired; and all four surprise entries resolve. The task face, final result, proof instance, and this log are co-committed under the exact seat author. The fixed conditional publisher is intentionally not redeployed in this order; issuer Msg 93803 carries that B2 runtime act to round 3.

---

## Next Steps

1. Validate the final proof instance with all six rows PASS and all four surprise rows resolved.
2. Co-commit the task face, proof, result, and this log under `0.7.0_AE_CloudOps~T`.
3. Measure `origin/CLOUD` and `merge-base --is-ancestor` after the commit, report every criterion to `2.0.0_SA_COO~A`, and do not push.
