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

---

## PROGRESS LOG

### 05:49Z -- first-moves grounded + Wave-2 dispatched live
**FIRST MOVES:**
- DRV flip: CTO GROUNDED it = the AFFINITY-ON second-flip (07-01 flipped the structural router w/ affinity=None; THIS turns --live-affinity ON). Needs a FRESH CVO~B shadow-cert (07-01 green doesn't cover affinity-on; a 0-regression test would be WRONG -- affinity-on SHOULD move routes). SEV1 seq: step-0 confirm router-live -> ~C/~E affinity-on shadow (4 checks: routes-are-improvements + no-oscillation + E1/rail/structural-dominance-hold + cold-start-graceful) -> CVO~B fresh cert -> ~C flip -> CTO confirm. AE-executes/CVO-certs/CTO-gates (independence preserved). FAST (existing harness re-run). CVO captured the pre-flip BASELINE (0/280 applied, 0/679 affinity, 0/679 outcomes = fully inert).
- G1 + P0: 0.7.0~A grounded both in the LIVE gateway (G1 layers on certified enforce() + destructive_ops blast_dimensions registry, over-cap->escalate-G3-not-die; P0 revocation.py mirrors blocklist.py hot-reload + existing jti). GO'd -> CTO arch-gate -> build -> CVO live-cert.

**COMPLEARN = 2 LIMBS (CTO + CVO independently grounded):** (1) affinity-ON [this flip -> CONSUMES the accumulated 280] + (2) FLYWHEEL-close [outcome-capture -> TRAINING; outcome-loop is ALSO empty 0/679]. Post-flip cert validates limb-1; if applied>0 but outcomes-still-0 = limb-2 surfaced (a separate follow-on charter = COMPLEARN's completion tail, NOT a limb-1 failure).

**WAVE-2 dispatched (MSTR-verified LIVE lanes):**
- NFRA_INTEGRATIONS P3 -> 0.5.0_AE_OpalETL (PID 27464), EXECUTE-NOW (not flip-gated). Closes INTEGRATIONS 3/3.
- NFRA_TOOLHEALTH TH-C -> 0.8.0~D (PID 9856), DESIGN-now/EXECUTE-on-DRV-flip.
- NFRA_COMPPROOF C1 -> 0.8.0~E (PID 38976), DESIGN-now/EXECUTE-on-flip (coord affinity-shadow w/ CTO COMPROUTE).

**RETIRES:** 0.6.0 /log written (--full-rebuild is DEPLOYED not holding; respawn-hook = 2-min exercise-verify account_is_open dtype==bool on next scheduled full run -> RAVC CTO; tracked bd-durable, self-heals) -> MSTR retiring. 0.6.1 /log pending (slow) -> retire-direct if stays dark.

**WAVE-3 (after retire frees 2 -> 13):** AGENTBUS (DE+CVO~B) / CMTQUE (0.7.0~B) / DEBTSCAN+TSGRAPH (0.4.0_DS~A) / COMPTEAM+COMPAWS (0.8.0-family) / SCTY-umbrella (0.7.0~B/~C). Sequenced post-retire on MSTR freed-slot map.

### 06:55Z -- 2 CLOSES + a named first-move DONE
**CLOSED (2/13):** NFRA_INTEGRATIONS (3/3, firm-sep bites deploy+runtime) + NFRA_COMPPROOF (honest: solve 55.6% / route C1 / learn accumulates-but-inert-BY-DESIGN; LEARN-activation chartered to COMPLEARN).
**SCTY SAFETY-CAPS DONE (Andrew's named 2nd first-move):** G1 blast-cap + P0 token-revoke DEPLOYED to live gateway + CVO-live-cert PASS (both BITE: revoke->DENIED, >cap->confirm+SEND-fn-called=0). Ledger CLOSED edb6ecbf5.
**TOOLHEALTH TH-C clause A CERTED:** headline close-the-loop proven at dispatch layer (KEEP->None / FIX->fix-commission on a live tool). Clause B on the calibration-tail.
**DRV-FLIP = HELD-ENTIRELY -> CALIBRATE-FIRST (the honest measure-first outcome):** tail-efficacy measured MIXED/cold-start-NEGATIVE (-9.1) -> value DENIED-on-merit; safety-flip ruled NOT-actually-safe (degrades cold-start live). Andrew's #1 first-move honestly-scoped: safe-but-not-yet-valuable. COMPLEARN completion re-scoped to 2 charters: (1) BASE oblique-precision [PRIMARY, the dominant lever -- base buries right tool rank-11/9%] + (2) affinity intent-conditioning [confidence-gate thin->0 + min-N=5 + intent-condition, held per CTO strict-sequence] + flywheel.
**IN-FLIGHT:** DEBTSCAN D1 (fix-landed!=fix-live: stitch-regenerate authorized -> structural promote ~1.0 + retire blanket-FP + unmask aaii-v2 orphan); TSGRAPH P3-2 (6 detectors building, D1 catches PRD-anchor live; P2-2 already-materialized); SCTY PREMCP P1 (0.7.0~A, next gap: verify=False fix); COMPROUTE Charter-1 (~E base-precision).
**PENDING (gated/tracked):** AGENTBUS S3/S4 (DE on Andrew-portal), CMTQUE cutover (MSTR off-peak go), COMPTEAM/COMPAWS (own gates), NFRA_PPL trio (staged), INFRPT P1-P3, COMPLEARN calibration (longer-tail), NFRA_GLDINV PRD (CTO).

### 09:20Z -- 2 more NFRA cores CLOSED (CVO-e2e-validated) -> CTO intent-ruling pending = 4/13
**TSGRAPH P3-3 fold-gate CLOSED** (CVO~B b4ffd39 e2e block-cert: NEW fork -> promotion HALTS on the REAL kuzu_nessie_load path -- decides AND enforces; the fires-but-doesn't-block gap CVO flagged is CLOSED). BONUS: 0.8.0 caught+fixed a hazard the test surfaced (perturbed committed baseline left the LIVE gate falsely firing -> restored + durable COMP_DETECT_BASELINE scratch-copy fix 3d8440b25). Residual: P2-2 cluster-materialize re-homed to MOTIF per CTO synergy analysis -> CTO close-intent-ruling routed.
**TOOLHEALTH TH-C clause-B CLOSED** (CVO~B c5100eaa0 causal-chain e2e: PROMOTE verdict -> w_s commission on comp-depth -> rank 6->0 flip; caused_by_commission=TRUE; NEG-control holds; clause-A 11/11). The close-the-loop headline PROVEN (verdicts demonstrably change behavior). Residual: TH-A EFFECTIVE-feed = tracked follow-on (non-blocking). -> CTO close-intent-ruling routed.
**Both CVO-e2e-validated; awaiting CTO intent-ruling to formally mark COMPLETE (Andrew's CTO-intent+CVO-e2e standard).** = 4/13 on CTO-YES.

### 09:37Z -- CTO intent-YES on BOTH -> TOOLHEALTH + TSGRAPH FORMALLY CLOSED = 4/13
**CTO ruled both COMPLETE (intent-YES)**, each with the load-bearing re-home-legitimacy check (a re-home is a dodge ONLY if the piece doesn't belong to the receiver -- CTO verified both BELONG):
- **NFRA_TOOLHEALTH CLOSED**: primary intent (used-consistently-correctly + a proven queryable CLOSED LEARNING LOOP) SATISFIED (2-of-3 axes live USEDxRAIL + causal-loop proven CVO~B c5100eaa0). EFFECTIVE axis RE-HOMED to FEDOBS (legit: effectiveness-over-agentOps IS a federated observation). Honest-narrative recorded (NOT spun as full-3-axis-live).
- **NFRA_TSGRAPH CLOSED**: core intent (P1 semantic-graph + P4 field-lineage + P3 fold-gate DECIDES-AND-ENFORCES CVO~B b4ffd39) COMPLETE. P2-2 cluster-materialize RE-HOMED to MOTIF (legit: it IS MOTIF's C2-in-graph; sequenced early as a MOTIF-accelerator). Honest-narrative recorded (P2-1 CLI delivered, P2-2=MOTIF's).
**Re-home CONDITIONS met via the SEMCTL registration: EFFECTIVE->FEDOBS + P2-2->MOTIF are committed deliverables (both forming-registered), NOT limbo.** = **4/13 NFRA CLOSED** (INTEGRATIONS, COMPPROOF, TOOLHEALTH, TSGRAPH).
**ALSO DONE:** COMPROUTE role-passing (built 87bc48d3f + CVO~B GREEN 51d3034b1, authoritative-role via OPAL_AGENT_SERIAL env; charter-2 prereq + un-cold-starts affinity -- it's what enabled clause-B); safe-ec2-deploy deployed_by fix (aba336c09, 5x defect killed) + telemetry-twin sweep (~A).
**IN-FLIGHT:** C3-WAF design at CTO arch-gate (~B); charter-2 affinity intent-conditioning (~E, role-passed basis); DEBTSCAN D3-scorer + comp-debt (0.8.0-base + DS~A, post-TSGRAPH-close unblocked); PREMCP L2-403 (Andrew identity-gate) + phase-2 (CTO-deferred).
