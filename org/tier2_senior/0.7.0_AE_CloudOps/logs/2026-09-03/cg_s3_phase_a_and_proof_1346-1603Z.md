# CG-s-3 projection contract Phase A and pre-Phase-B proof - 0.7.0_AE_CloudOps~T

**archetype:** MIXED

**Date:** 2026-09-03
**Task Order:** NFRA_CLDGRPH.TO-CG-B-3
**Status:** IN PROGRESS

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
| 7 | Phase B | HELD pending either B-2's complete flip or a written issuer release after ~S reports no further Python edit pending. |

## Verification

- Phase A JSON blocks parse successfully.
- `git diff --check` passed for the three Phase A artifacts before commit.
- Surprise gate: `1 new row(s) of 15 total checked`; `OK: 1 file(s)`.
- Current no-push report measured origin/CLOUD at `351f309e0a6ded1a5a5bdf3aacec18a5f9f8dbee`; Phase A commit `823ea90776` is its ancestor.
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
| `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-09-03/cg_s3_phase_a_and_proof_1346-1603Z.md` | This session record | This commit - `PENDING-THIS-COMMIT` at write time |

---

## Blockers

- BLOCKED on [0.7.0_AE_CloudOps~S]: `NFRA_CLDGRPH.TO-CG-B-2.projection-worker-ported.md` - waiting for either its committed complete flip or an issuer-written release after ~S reports no further Python edit pending. Evidence: issuer Msg-ID 93739 amends but does not yet satisfy the release condition.

---

## Current State

Phase A is committed at `823ea90776`: the authoritative fallback contract, result, and S16 row are complete. The pre-Phase-B proof instance is now being authored with B3-AC1, B3-AC4, and B3-AC6 grounded on that commit and B3-AC2, B3-AC3, and B3-AC5 honestly marked pending by construction. No Phase B infrastructure edit, `comp-blast`, face flip, or further push is permitted until the issuer supplies one of the two written release carriers.

---

## Next Steps

1. **Write and validate the pre-Phase-B proof instance** - run `proof-of-spec-check.py` on the exact ~T path and commit it locally.
2. **[2.0.0_SA_COO~A] Relay the Phase B release carrier** - either the B-2 complete-flip commit or the written no-further-Python-edit release.
3. **Execute Phase B after release** - conform both producers, implement and exercise pointer publication/refusals, then make all six proof rows PASS before the face flip.
