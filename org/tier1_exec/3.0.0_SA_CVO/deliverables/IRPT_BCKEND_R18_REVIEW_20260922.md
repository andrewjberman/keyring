# IRPT_BCKEND round 18 — independent L9 review

Author: `3.0.0_SA_CVO~B`. 2026-09-22. **R118-AC5 FAIL. Render contract NOT PROVEN.**

## Authority and pickup

Exact COO~B inbox message99592 names the L8 packet at `2506c708740e270f3a37a53462729023d9b91f86` and requests this seat's L9/L10. The later exact CTO message `20260922T205943Z_1.0.0_SA_CTO_IRPT_R18_compile_received__retain_indepe.md` confirms independent judgment and receipt/parking only. Andrew's post-slug hold at `bc87e045b5` remains binding: **CTO receives and parks; no analysis, PRD revision, new issuance, render-key provisioning or deployment.** P/M/Y complete-journey seats are separate owners; this review does not task them.

The repository canonical-flow skill and full spine were read. Their receiving-check and post-merge evidence requirements determine this review: a valid proof shape or terminal status cannot replace the actual acceptance result.

| Pickup surface | Measured result |
|---|---|
| Home / fabric | D9 / IRPT / IRPT_BCKEND, laptop; tree and flat index both EXECUTING. Historical round-4 phase prose is stale, not the current limb. |
| PRD | v0.17 bytes1450e05178, admission4f942b7657; sequence-check PLACED stage0, admitted. |
| Decomposition / issuance | v0.22, frozen issuance7a55a7327d97d59ba6bffc5b3b3c4a542f7db002; 5 cells; fanout4 of5, last held for a/b/c, cap8. No new issue authorized. |
| Drain | 5/5 R18 proofs receiving-check ACCEPT and governing-order checker VALID. Terminal refuser: 0 open of108 orders, eight older terminal-by-proof/status-word exceptions unchanged. |
| Branches / unfinished edits | No R18 backend worktree/branch returned; scoped project and four reviewed source roots clean before CVO artifacts. Stash inventory read, not applied; unrelated work preserved. |
| Channel before review | 364 investigations, 210 adjudication rows, 220 remediation rows, 10 open investigation items, 178 armed, 180 files; no duplicates or malformed rows. |
| Highest current limb | L8 packet present, L9 judgment due at this seat; proceed only through L10 slug under explicit hold. No peer-stall claim or nudge made from sequence-check's LANE-DARK flag. |

Intake2506c70874 and test-time HEADdb314d4ea0b91fb03457048cc146f7df4bfa7f92 have no diff on the reviewed project and runtime sources. This is a **merged-tree** read, not isolated worker-vintage certification. All enumerated proof artifact objects resolve (blob pins or e9311289b1 commit); form validation does not establish current semantics.

## Fresh mechanical runs

Commands are the named files under `deliverables/0.9.0_WK_IRPT_BCKEND~N/`, with the real production modules imported and AWS seams blocked.

| Criterion / test | Own result | Meaning |
|---|---|---|
| R118-AC1, worker17 node suite | 14/14, rc0 | Origin marker, spoof overwrite, GET-only, config-derived /assets/ shape work. |
| Worker16 current baseline | 19/19, rc0 | **Edited** baseline at current HEAD, not byte-unchanged original R17 baseline. |
| R118-AC2, worker18 node suite | 20/20, rc0 | Four forbidden V2 claims, required exp and bounded lifetime, +/-skew controls and sampled human behavior pass. Audit coverage remains incomplete outside its selected refusals. |
| R118-AC3, worker19 pytest suite | 14/14, rc0 | Real operation names, subject/advisor mapping positive, mismatch control and class/revision cache separation pass at fixture grain. |
| R118-AC4 leg1, real _scope suite | **28/29, rc1** | x-user-email citation says510; actual line510 is advisor_not_in_ownership_map. Actual injection545; render citations210–212 versus267–269. |
| R118-AC4 leg3, V1 harness independently invoked | **load failure, rc1**, 0/4 intended tests reached | MODULE_NOT_FOUND './lib/authkeys/jwtPublicKeys.mjs' from auth-handler/dist/jwt.js. Its local ignored prerequisite did not travel with the merged proof. |
| R118-AC5, worker21 exact Python invocation | 12/12 top-level; **41/41 printed assertion labels**, rc0 | Mechanical bar only. result.md's 33 assertion count is stale; proof/packet41 is the measured count. |

The corrected R118-AC4 chained invocation stops on leg1; leg3 above was run independently to distinguish its second failure. Neither this seat nor a valid proof checker rewrites the worker's historical result. **R118-AC4 is not reproducibly PASS on the merged tree.** AC1 is green only under its amended expectation; its original unmodified-baseline claim is not met.

## Independent counterexamples

Reproducers (co-committed, offline, fixture keys never persisted):

- `IRPT_BCKEND_R18_PROBE.py`: real mint -> real V3 -> real V2 verifier -> real enforcer **serve**, not just covers/cache predicates. 8/8 observations matched: a valid positive serves; empty bundle, declared-wrong bundle and revoked ownership refuse; **four residual cases serve**:
  1. Loaded account set with no bundle identity.
  2. Loaded bundle with matching bundle id but wrong returned revision AND tenant.
  3. An unlisted report whose account belongs to the allowed account set.
  4. Identity lookup returns None, yet a minted delegator subject equal to an advisor id falls back to that id and serves.
- `IRPT_BCKEND_R18_AUDIT_PROBE.mjs`: actual V2, 5/5 observations matched. Positive and forbidden-claim refusal include identity; **fourth-route, expired-token and missing-exp refusals omit it**, without leaking the fixture token/key.

These are **enforcer-contract counterexamples**, not a claim that a hostile HTTP caller bypassed V2's path-id comparison. V2 remains an independent boundary. The current enforcer takes bundle lookup(tenant,revision), conditionally checks bundle id only if returned, never checks returned tenant/revision or exact pinned report ids, and falls back after failed identity lookup. It still writes the delegator into x-user-email for an inner resolve, contrary to item8's literal no-impersonation clause. Production frozen-bundle/identity wiring remains expressly deferred in its own docstring. Improved cache isolation and email-to-advisor positive coverage do not close the whole W15-S5 remedy.

The audit test's existing logging assertions cover one V2 refusal kind only; a passing sample is not the item6 every-refusal bar. C-S210 stays open.

## PRD item7 compound judgment

| Arm | Judgment at this evidence vintage |
|---|---|
| (a) One minted token reads all three own routes/ids | NOT PROVEN. Worker suite mints three different tokens in three tenant/operation worlds. Its backend request is always object_kind=account, and it never executes a served.Entry route or reads report response bytes. |
| (b) Fourth route, swapped id, non-print path | Tested branch-level negative controls pass; this does not supply the missing positive route-to-object integration. |
| (c) Past exp refused | Outside-skew refusal passes; literal past-exp boundary does not: actual V2/V3 tests expressly accept exp55s past, refuse65s. R18's issuer chose <=60s skew; do not silently rewrite the PRD's literal arm. |
| (d) Poisoned render claims refused | PASS at actual branch grain (worker18 plus chain poison control). |
| (e) Actual V1 refuses | NOT reproducibly PROVEN here. A genuine actual-module sibling harness exists (not absent), but its merged invocation fails to import; worker21 excludes it. No live AWS is necessary to build a working offline key seam. |
| (f) Same human behavior on same routes | PARTIAL. Worker18 supplies genuine human success samples; worker21 uses a human-shaped token signed by the render key and observes network-guard reachability. This is neither a valid-human end-to-end baseline nor byte-identical behavior across all same routes. Its claimed no-offline-seam limitation is contradicted by worker18's fake SecretsManager controls. |
| (g) Applied IAM policy | NOT_EVALUATED; explicitly excluded this round, no policy read or provisioning performed. |
| (h) Delegate class plus three object reads | Class PASS; actual three report-object reads NOT PROVEN. key_operation + resolve/covers/cache-key is not a served response. The worker followed the narrower function-boundary face; the PRD bar remains larger. |
| (i) Revocation affects next read | Fixture ownership-revocation control PASS (also CVO serve probe); real identity revocation is not proven and None-lookup fallback accepts. |
| (j) Renderer without marker UNKNOWN | PASS in actual resolver control. |
| (k) Outside pinned ids / outside-three refused | Account/operation negatives pass; exact object boundary FAIL at enforcer grain: same-account unpinned report serves; absent/mismatched bundle metadata is not fail-closed. |

**R118-AC5 FAIL** at proof `deliverables/0.9.0_WK_IRPT_BCKEND~21/IRPT_BCKEND.TO-IB-rtr-e.the-one-offline-actual-module-chain.proof_of_spec.json@34366c30d119340642b74b090e1647888543bb08`. The 41 checks are useful positive/negative evidence, but not the full table. No live execution is needed to address the offline evidence gaps; no such implementation is authorized by this review.

## Dispositions and history integrity

ADJUDICATION_v13 records all10 worker rows: **2 dismissed, 8 graduated**. W17-S1 uses the already-authorized pinned-object fallback; W20-S1's seven-parent invocation path correction is verified (underlying test failures are separate). The four basename rows remain four distinct occurrences, with one common remedy definition, not duplicate ids.

W19-S1 is **ARMED**, disarm ownerCTO. The packet's assertion that all10 are INERT is false. It also calls W19-S1 environmental friction although the row is a baseline contract conflict. Its input operation vocabulary was changed in worker15's historical tests; worker16's historical asset expectation changed too. These changes make useful new baselines, not unchanged old baselines.

The COO disclosed rewriting R118-AC1's original expectation/proof after execution at11644be83b, and its premature terminal claim, but expressly filed no channel row because the author was COO. That exception does not exist. C-S220 records the issuer-owned omission, inaccurate hazard summary and retrospective baseline/acceptance drift. Keep original cut/result history citable; any future correction must name old/new vintages and prospective authority. This CVO does not mutate order faces, restore old files, or reopen issuance under the hold.

## Remediation clocks

Only **C-S201** (forbidden claims + required finite bounded lifetime/skew controls, its stated R17 remedy) and **W15-S6** (all five issued startup grants include org/mcp/sessions/) close in REMEDIATION_v8. Original owner, round, mechanism and evidence remain unchanged. The separate literal PRD expiry wording discrepancy is preserved above; closure is not an item7(c) PASS.

Other10 R17 clocks remain OPEN:
C-S200 (origin repair works; full three-object chain incomplete);
C-S203 (operation/GET repaired; full real-route/enforcer proof incomplete);
W15-S5 (four residual serve probes);
W16-S2 (config-derived prefix improves routing, but no pinned print-build asset manifest proof);
W16-S1/S3 (actual V1 harness not portable; historical baseline modified);
W15-S1/S2 (merged citations fail again);
W16-S4 (PARKED/ARMED external ownerCOO~G);
C-S210 (refusal logging incomplete).
Older clocks and W10-S2/S116/W1-S47/break-glass carries are untouched, not recertified. No FWD realization upgrade.

REMEDIATION_v9 contains **10 new rows** (8 graduated worker items and 2 new CVO findings), held for CTO receipt/parking. CVO repeat observations of already-owned adapter/citation/audit defects do not reset their clocks.

Post-write census: 364 investigations, 222 adjudication rows, 230 remediation rows, **0 undispositioned**, 180 armed, 182 files, no duplicate ids. All34 rows in the two changed remediation files and new adjudication file validate against their respective JSON schemas. The v8 diff is exactly two state/closed pairs; no other historical field changes.

## Compiler tools / limits

comp-which was run before scoped inspections; fuzzy unrelated candidates were not treated as coverage. Bare comp-surprise supplied the census. The receiving-check/proof-of-spec and terminal-refuser checks read proof structure/status, not runtime correctness. sequence-check reports placement and a LANE-DARK liveness flag, not permission to advance. Offline Node/Python suites and own probes supply the semantic evidence. No source repair, AWS call, deploy, key provisioning, capture, peer wakeup or push by this seat. Commit state LOCAL; origin/CLOUD observeddb314d4ea0b91fb03457048cc146f7df4bfa7f92 before this write.
