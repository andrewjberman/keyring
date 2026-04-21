# COO Session 36 Addendum — ADHC_DSFLOW Decomposition

**Date:** 2026-04-21 (Tue, PM ET)
**Agent:** 2.0.0_SA_COO
**Companion logs:** `session36_hlot2_to_authoring.md`, `session36_trsb_tfimpt_decomposition.md`

---

## Scope

CTO handed off `ADHC_DSFLOW` PRD (commit `35f348c3`) via MCP 20260421T125319Z in parallel with TRSB_TFIMPT decomposition. Response to 2-in-2-days latent-PROD-crash pattern (D_02 `035352c3` KeyError + B_00 `081223b5` NameError). Picked up post-W1-close per CTO-approved sequencing (20260421T125554Z).

## Decomposition decisions

| TO | Owner | Status | Gates (to flip staged→pending) |
|---|---|---|---|
| DSFLOW.001 | 0.4.0_DS_ClientPlatform | **pending** | None (GO dispatches immediately). Tool build: `.tools/ds-precommit-check.py` + `.tools/ds-commit-gate.sh` + `tests/ds_precommit_check_test.py`. ~2h SLA. |
| DSFLOW.002 | 2.0.0_SA_COO (my own lane) | **pending** | Sequencing: commit AFTER .001 so CLAUDE.md Rule 13 cites a real tool path. §11 Q4 DS IAM probe embedded inline. <1h SLA. |
| DSFLOW.003 | 0.4.0_DS_ClientPlatform (any lane) | **staged** | Both .001 + .002 complete. Fires on next natural gold-script commit — no forced dispatch. HLOT2 5f5d0319 exempt per PRD §13 non-retroactive. |

## Open question routing

| §11 Q | Handling |
|---|---|
| Q1 git hook vs startup reminder | Recommend v1 = startup-protocol reminder (simpler, trust-based). v2 = optional git hook if adoption stalls. Folded into DSFLOW.002 — not a separate TO. |
| Q2 historical gate backfill | Recommend YES at .001 complete — 5min wall, low-cost; catches dormant bugs. Not gating dispatch; DS runs post-TO close. |
| Q3 contract drift (Class B, 035352c3 class) | Park as DS code-hygiene per PRD §6.3. Escalate to follow-up ADHC tool project if frequency > 1/mo. Not scoped in v1. |
| Q4 DS IAM s3:PutObject on opal-bd-gold-code/gold/* | Embedded in DSFLOW.002 Phase 1 as a prerequisite probe. If gap, micro-TO to 0.7.0_AE_CloudOps for provisioning. No pre-gate Andrew-ask needed. |
| Q5 cross-pod scope | Pod 0.4 pilot per PRD. Expand to other DS lanes (0.1/0.2/0.3) only if pattern holds + Andrew redirects. Not scoped in v1. |

## Non-retroactive discipline (PRD §13)

- HLOT2 `5f5d0319` (committed 20260421T124009Z pre-gate) EXEMPT.
- BFIX1+2 (`081223b5` → `1a54d46a` fix-forward) EXEMPT.
- Emergency `--chain bcd` / `--chain full` cycles in flight EXEMPT.
- New workflow activates at .001 + .002 completion. DSFLOW.003 training-run is the FIRST post-protocol commit observed.

## Compiler tools run (COO mandate)

| Tool | Command | Result | Purpose |
|---|---|---|---|
| Read | PRD docs/architecture/ADHC_DSFLOW.md | 409 lines | Pattern + acceptance verbatim transcription |
| Read | org/projects/ADHC_DSFLOW.json | baseline state captured | Phase 0 → Phase 1 transition for phase rewrite |
| get_agent_status | 0.4.0_DS_ClientPlatform | baseline: DS is NOT REGISTERED but has pending TO queue + latest log 2026-04-20 STAUDT layer_c_findings. Target agent for GO dispatch. | |

No comp-* runs — pure org-doc + tooling-spec work. Triad format preserved across all 3 TOs. Note: DSFLOW.001 itself is a tooling build, not a pipeline change — its compiler mandate uses py_compile + ast + pytest rather than comp-pipescript / comp-blast.

## Dispatch sequence

Commit (this turn):
1. Single commit bundling all 3 TOs + JSON phase refresh + this log + companion session logs update (if needed).
2. MCP GO → 0.4.0_DS_ClientPlatform on DSFLOW.001 (dispatch fires when commit lands).
3. DSFLOW.002 stays pending — COO self-executes after .001 commit lands (coordinates ordering inline).
4. DSFLOW.003 stays staged — no dispatch; COO monitors for trigger.

## Other in-flight

- HLOT2 qa-runner `cf5bd5ad` in flight (`--chain full`, ETA 15:40Z). Batched B_00 1a54d46a + B_01 5f5d0319. AE escalated to full-chain vs --from-bcd — conservative A-tier invariant coverage.
- TRSB_TFIMPT.W1 COMPLETE (tag trade-pipeline-v1.3.0 shipped 47 min post-GO). W2/W3 staged (Option B locked per CTO 20260421T130918Z). Andrew chat-briefed 13:14Z-ish.
- Andrew §8 Q2 widened + §8 Q4 fixture asks outstanding.

— 2.0.0_SA_COO
