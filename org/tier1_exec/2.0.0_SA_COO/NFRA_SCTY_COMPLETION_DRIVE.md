# NFRA + SCTY COMPLETION DRIVE — tracker

**Andrew-direct 2026-07-07 ~05:30Z:** "Flip DRV and safety cap for SCTY then drive all of NFRA and SCTY to completion -- finalize AND validate AND complete all the NFRA and SCTY work."

**Definition of DONE per project:** every outstanding PRD mission built + deployed + **CVO exercise-cert PASS** (finalize AND validate). A config-read PASS is NOT a completion.

**Drive model:** COO /drive (20m) drives each project's outstanding-missions -> owner -> build -> CTO arch-gate -> CVO exercise-cert. MSTR wakes/holds the worker-set alive. Source of the outstanding-missions = the 3-cluster gap-analysis 2026-07-07.

---

## FIRST MOVES (Andrew-named)
| # | Move | Owner | Why (leverage) | Status |
|---|---|---|---|---|
| A | **FLIP DRV** (shadow-validate -> flip default compiler-router) | CTO | Unblocks 3: TOOLHEALTH TH-C + COMPPROOF C1 + activates COMPLEARN (0/236 inert) | DISPATCHED CTO 0532Z |
| B | **SCTY MCPGUARD G1** blast-radius cap ("don't delete OneDrive") | 0.7.0 AE | Named safety-cap; no active TO; only indirect protection today | DISPATCHED 0.7.0 0533Z |
| B | **SCTY PREMCP P0** token-revocation kill-path | 0.7.0 AE | Highest standalone sec gap: leaked 30d refresh token has no revoke | DISPATCHED 0.7.0 0533Z |

---

## NFRA (10) — outstanding missions to DONE
| Project | ~% | Outstanding to complete | Owner | Gate/blocker |
|---|---|---|---|---|
| NFRA_TOOLHEALTH | 80 | TH-C close-the-loop: verdicts DRIVE fix/promote/retire (demonstrably change behavior) | 0.8.0 | DRV flip (move A) |
| NFRA_COMPPROOF | 75 | C1 COMPROUTE eval (precision@1/recall); B-01/B-08 judge-completion; D2 spike stays FENCED (Andrew) | 0.8.0~D/~E | C1 on DRV flip (A) |
| NFRA_CMTQUE | 45 | Production cutover of 1338 callers onto the queue; durable-queue+alarms leg; contamination-guard retire | 0.7.0~B | MSTR off-peak go for RUN |
| NFRA_AGENTBUS | 45 | S3 broker-adapter (4-of-5 controls enforce here); S4 CVO live re-verify all 5; AB-ACTIVATE fenced (Andrew) | DE + CVO~B | S3 on MCPGUARD/PREMCP/COMPTEAM |
| NFRA_INTEGRATIONS | 70 | P3 STORAGE canonical schema (code-loc/dep/firmsep/egress) | 0.5.0 AE_OpalETL | active TO #13 |
| NFRA_DEBTSCAN | 75 | D3 canon-deviation motif-mining (needs CTO canon-patterns.yaml); D1 reachability off 0.70 ADVISORY -> 0.80 gate; comp-debt standing scan | DS + CTO | D3 on canon-patterns.yaml (CTO) |
| NFRA_TSGRAPH | 80 | P3 frontend bug/logic detector library; P2-2 graph-materialize + DE-verify (cluster edges live) | DS + DE | P2-2 was AE-dark; re-seq |
| NFRA_COMPAWS | 65 | Full 13/13 class taxonomy (9/13 now); SFN blast-edge coverage hole; snapshot-archive; SFN->Lambda bridge (staged) | 0.8.0 | Andrew-parked -> unpark for completion |
| NFRA_COMPTEAM | 25 | A distributable agent-kit + strip-list gate; B2 scoped read-partitions | 0.8.0 | B2 on SCTY entitlements; may need Andrew Directive |
| NFRA_INFRPT | 55 | P1 freshness+drift sections; P2 cost-depth+reaper; P3 contract-integrity (on NFRA_GCONTR) | (unassigned) | P3 on GCONTR live |

**NFRA_PPL* trio (PPLINF/PPL49F/PPLCOT, ~5% each):** deliberately STAGED behind ETLFIX/COTETL durable legs -- un-stage on grounded milestone; NOT force-completable now (genuine dependency). Track, don't force.
**NFRA_GLDINV PRD:** CTO authoring (3 inv x 2 arms) -- doctrine deliverable, folds tonight's cases.

---

## SCTY (3) — outstanding missions to DONE
| Project | ~% | Outstanding to complete | Owner | Gate |
|---|---|---|---|---|
| SCTY_MCPGUARD | 45 | **G1 blast-radius cap** (move B) + G3/G4/G5 guardrails; S0 destructive-surface enum | 0.7.0 | CTO gate + CVO live-cert |
| SCTY_PREMCP | 30 | **P0 token-revoke** (move B); P1 write-scope 2nd-gate + verify=False fix + rate-limit/WAF; P2 net isolation + broker review | 0.7.0 | CTO gate + CVO live-cert |
| SCTY (umbrella) | 35 | W1/W2 close; WS2 vendor/partner diligence (BD/Orion/Eclipse/SmartX); WS4 fabric-hardening; macro self-assessment cert | 0.7.0 + children | CVO cert per WS |

---

## VALIDATION (CVO) — every completion exercise-certed (dispatched 0533Z)
Priority: DRV-flip effects (TOOLHEALTH behavior-change, COMPPROOF C1, COMPLEARN-active) -> SCTY caps (G1 blocks a destructive-op live; P0 revoked-token rejected live) -> AGENTBUS S4 -> INTEGRATIONS P3 -> CMTQUE mutex-retired.

## Cadence: 20m /drive restored (500c241d). MSTR waking worker-set. Drive each row to CVO-cert-PASS.
