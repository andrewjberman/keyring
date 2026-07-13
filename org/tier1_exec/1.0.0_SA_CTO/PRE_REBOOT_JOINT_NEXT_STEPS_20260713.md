# PRE-REBOOT JOINT NEXT-STEPS LOG — 2026-07-13

**Authors:** `1.0.0_SA_CTO~B` + `1.0.0_SA_CTO` (base) — jointly authored, base-CTO section merged verbatim. **Andrew-direct:** *"i need you and CTO Base to discuss and collaborate on a joint log of next steps, then im going to reboot the fabric partially. in this log we need /stimulus-scan qualification of which agents are tasked with what to get the next steps for each current hot project done."*

**THIS DOC IS THE SURVIVAL ARTIFACT.** Assume every agent named here is dead and re-spawned. Each must self-onboard from this doc alone: it names the serial, the exact deliverable, the artifact/commit to resume from, and what it is blocked on.

---

## ⚠️ 0. DO THESE **BEFORE** THE REBOOT — uncommitted work a reboot would STRAND

| # | Item | Owner | Action |
|---|---|---|---|
| **L1** | `build-and-upload.sh` **upload-verify patch** — EXERCISED (T-pos / T-neg1-404 / T-neg2-stale-sha) but sits **UNCOMMITTED in the shared working tree**. | `0.7.0_AE_CloudOps~A` (owned-paths = its lane) | **COMMIT BEFORE SHUTDOWN.** If lost: re-derive from base-CTO's 043244Z handoff msg (design is ~30 lines). |
| **L2** | **Any other agent's uncommitted lane work.** | every MUST-RETURN serial below | **commit-or-stash before shutdown.** (07-12 peer-sweep lesson: uncommitted work in a shared tree is *the* hazard surface.) |

*Everything in §2 (AoR) and §3 (OPAL_ASSETS) is fully committed + pushed — those workstreams are reboot-safe.*

## 0b. REBOOT DOCTRINE — applies to EVERY respawn

This reboot is the **first live exercise of identity gate G-B** (landed `b531c5c0a`): `org/XXX.md` Step 1 now carries identity-resolution precedence — **Andrew's word > session serial file > own Monitors > own registrations; `.comp-graph/.agent_context` is NOT an identity source**; liveness.json PID cross-check; inverse-first rule. Every respawned agent self-onboards through it. **G-A (broker-side PID refusal) is NOT yet built**, so post-reboot the identity check is *each agent's own responsibility*. (Context: base-CTO mis-adopted another serial post-compaction this session — this gate exists because of it.)

---

## 1. FABRIC QUALIFICATION (stimulus-scan @ 0442Z) + MERGED RE-SPAWN ROSTER

**LIVE at write time (7):** `0.0.0_AB_MSTR` · `1.0.0_SA_CTO` (base) · `1.0.0_SA_CTO~B` · `2.0.0_SA_COO` · `0.7.0_AE_CloudOps` · `0.7.0_AE_CloudOps~A` · `0.8.0_AE_CloudComp`

### MUST RE-SPAWN (hot path blocked without them)

| Serial | Owns | Resume-from |
|---|---|---|
| **`0.4.0_DS_ClientPlatform`** ☠️ | **ROUND-8.2 — the single blocker on the AoR go-live.** Also OPAL_ASSETS P0-B + the D_02b grounding. | `docs/briefs/advisor-of-record-go-live-gate-findings-20260713.md` @ `66f8f1e06` |
| **`3.0.0_SA_CVO~B`** ☠️ | gate-2 re-verify of round-8.2 (**F1 through the DISPATCH**) | same doc §3.2/§5; battery at `scratchpad/aor_round8_battery.py` |
| **`2.0.0_SA_COO`** | /drive; AoR co-sign; LIVELEARN accrual; phantom-consent TOs; serve-gate P2 gating; OPAL_ASSETS backfill | this doc |
| **`0.7.0_AE_CloudOps~A`** | G-A identity gate build; **L1 upload-verify land**; OPAL_ASSETS P0-A emitter/backfill | this doc + `d1aa23968` |
| **`0.8.0_AE_CloudComp`** | OPAL_ASSETS G4/G5 additive-rows (**with `value_class` per CTO~B ruling**) | `43b7d36d5` + §3 |
| **`0.7.0_AE_CloudOps`** (base) | the **LIVE 08335338 backfill** — **resumes from grant `AG-2026-07-13-01` + the manifest, NOT session memory** | `org/mcp/andrew_grants/` |
| **`1.0.0_SA_CTO~D`** | LIVELEARN part-2 gates; aws-shim ratification; COMPLEARN P3a rulings | §4 |
| **`0.0.0_AB_MSTR`** | grant-ledger writer (P-2 depends on it); spawn authority | §4.3 |
| **`0.4.2_RD_AdvisorIntelligence`** ☠️ | FE noel card — **DONE but HELD** (`73ee2705`+`b005545e`, unpushed on portal DEV) | re-spawn **at go-live only** |

### COLD-OK (not hot-path)
`3.0.0_SA_CVO` (base) · `3.0.0_SA_CVO~A` (OPAL_ASSETS FP-R0 review — *can wait, not blocking*) · `0.7.0_AE_CloudOps~C` (LD-0273 awaits Andrew anyway).

---

## 2. HOT — INF Advisor-of-Record go-live (P0) · *CTO~B*

**State:** round-8 SSOT refactor BUILT + GATED. Andrew's design (resolve AoR **once** at a front-of-chain resolver; every view **inherits** a canonical field; zero per-view structuring) is implemented — fold census 10→1, household 4→1. **Gate-2 CLOSED VERIFIED** (r8+r8.1). **Gate-1: architecture SOUND (no round-7-class false-green) but F1–F10 require ROUND-8.2 before switch-ON.** **Nothing served. Switch OFF. SERVE-HELD. Zero live impact — a reboot loses no served state.**
**Commits:** `345c85daa`+`5581c0de1` (round-8) · `68be1809d` (r8.1 firebreaks) · `63dd76201` (CHANGE-3 silver raw passthrough, SERVE-HELD — a **HARD go-live precondition**). **Record + all raw 32-agent workflow artifacts:** `docs/briefs/advisor-of-record-go-live-gate-findings-20260713.md` @ `66f8f1e06`.

1. **`0.4.0_DS` [RE-SPAWN] → ROUND-8.2.** **F1 is the blocker:** `orion-gold-dispatch.sh:353/354` gates the resolver `INF_A_0` entry on `INF_AOR_FOLD_ACTIVE=1` while ALL migrated consumers call `load_resolution()` UNCONDITIONALLY (raises if absent) → **a switch-OFF, our documented rollback, DROPS the resolver → consumers raise → the nightly ABORTS. The rollback is not a rollback.** Make the resolver entry UNCONDITIONAL. Then F2 (NaN advisor_key on A_00/resolver as-of skew) · F3 (incomplete state-cache greens a real change) · **F4 — CTO~B RULED: KEEP the fail-closed RAISE** (a plurality fallback would resurrect the per-view derivation the SSOT exists to kill); fix C_02's try/except gap + reconcile D_02c's contract · F5–F10. Keep SERVE-HELD + switch OFF.
2. **`1.0.0_SA_CTO~B` → gate-1 re-review** of the round-8.2 delta. Holds the F4 ruling + the pending D_02b ruling.
3. **`3.0.0_SA_CVO~B` [RE-SPAWN] → gate-2 re-verify. F1 must be exercised THROUGH THE DISPATCH, not resolver-direct** — her DELTA-0 (0/871) was resolver-direct, which is exactly the instrument gap F1 exposes.
4. **`2.0.0_SA_COO` → co-sign PAUSED** until both gates clear. Owns the release checklist: CHANGE-3 silver deploy → round-8.2 → switch ON + sentinel-lift + **resolver entry UNCONDITIONAL (F1)** + FE promote → V4.
5. **`0.4.0_DS` → D_02b grounding** (post-8.2): `INF_D_02b` carries a LOCAL rep_id map reversing peter↔patrick vs canonical. **HYPOTHESIS ONLY** — Rule-22 source-grounding required; **NO fix until CTO~B rules on the grounded mechanism.**

**ANDREW-GATED:** never-widen co-sign + GO.
**⛔ SMS / ALERT-DELIVERY: CANCELLED, STRUCK FROM THE CHAIN** (Andrew-direct: *"we're not doing sms… i dont like to talk about alerts until the actual process is done because usually the alerts are miscalibrated and then its spam on my devices"*). Detectors still WRITE findings (stdout + ops queue); nothing pages Andrew. **Do NOT re-raise alert wiring/calibration until the process is DONE and PROVEN.**

---

## 3. HOT — OPAL_ASSETS (14-cohort daily AUM) · *CTO~B*

**State:** PRD v0.1 + registry MSTR-accepted (`79231da3e`). **P0-A base table `opal-assets-daily-aua` is DEPLOYED and LIVE — COO-verified 14 rows with honest states; backfill executing.** Andrew has a queryable daily table.

1. **`0.7.0_AE~A` → P0-A emitter + backfill.** Table arch-gated **ACCEPT-AS-BUILT** (`70687ba8a`; PK=`run_date`/SK=`cohort_id` + GSI `cohort_history` — the served daily cross-cohort read is strongly-consistent on the base table, *better* than CTO~B's original criterion).
2. **`0.8.0_AE` → G4 ownership fold + G5 convergence.** CTO~B rulings: (a) **additive-rows APPROVED on ONE CONDITION — every row carries an explicit `value_class` (self-classifying)**, else the PK=`run_date` partition read returns base+ownership rows together and a naive consumer mixes/double-counts them into AUM (a served/never-widen defect); (b) **RATIFIED: measured `opal-data-etfs/daily` is the ONE canonical held-source per partner — NEVER mdpf `etf_decomposition` target_weight** (a target weight is intent, not an observation).
3. **`0.4.0_DS` [RE-SPAWN] → P0-B** (G4 interim avgcap-only fold + mdpf emitter) — GO'd only **after** round-8.2 frees DS. Interim rows carry a disclosed `partial: 08242234-only` flag; its removal = G4 DONE (PRD AC4).
4. **`0.7.0_AE` (base) → 08335338 backfill: LIVE, resumes from grant `AG-2026-07-13-01` + manifest.** Residue held, IAM staged (ledger `69983008e`). **Purge-or-keep is Andrew-gated.**
5. `3.0.0_SA_CVO~A` (cold-ok) → FP-R0 schema review when convenient.

**ANDREW-GATED:** P1 sovereign nod (49F/Schwab build) · 2021 back-fill vendor call · 08335338 residue purge-or-keep.

---

## 4. BASE-CTO SCOPE — 7 projects *(merged verbatim from `1.0.0_SA_CTO`)*

1. **NFRA_LIVELEARN part-2** (Andrew /goal, OPEN). Part-1 clear-gate COMPLETE. Close-condition @ `a30637065`: **3 CONSECUTIVE clean AUTONOMOUS cycles** (consumption-driven auto-refresh of a >7d-stale feed, zero human touch, flip-integrity + honesty rails; a forced `--refresh` does NOT count). **NEXT: nothing to build — cycles ACCRUE.** `2.0.0_SA_COO` tracks accrual (multi-session); `1.0.0_SA_CTO~D` gates each observed cycle; `0.8.0_AE` owns the substrate ONLY if a cycle fails. Reboot-safe (committed; feed/probe state on disk).
2. **IDENTITY GATE.** G-B **LANDED** (`b531c5c0a` — this reboot exercises it). **G-A** (broker register/heartbeat REFUSES a PID already live under another serial; identity_override audited) GO'd to `0.7.0_AE~A`; `1.0.0_SA_CTO` arch-gates (**replay falsifier: the 07-12 sequence must FAIL registration**; no-regression on normal re-register). Resume: `SEV_IDENTITY_MISADOPTION_GATE_20260713.md` @ `d1aa23968`.
3. **PHANTOM-CONSENT GATE (P-1/P-2/P-3).** Design CLOSED w/ MSTR concur (`87a8d2ec0`); **P-2 grant-LEDGER is load-bearing** (the vector was a session-opening turn); ledger LIVE with `AG-2026-07-13-01` (the 08335338 grant, `30c7e13e0`) which **doubles as the VENDOR-EGRESS authorization** (one `resolve_grant(action, surface)`, two gates). NEXT: `2.0.0_SA_COO` TO-records + allocates P-1 (headless AUQ DENY hook) / P-2-lint / P-3 (sovereign_held write-path refusal); `1.0.0_SA_CTO` arch-gates. **REBOOT-CRITICAL: any respawned `0.7.0` resumes the live backfill FROM THE GRANT FILE, not session memory.**
4. **UPLOAD-VERIFY GATE** (build-and-upload false-success). Patch exercised 3-ways, **UNCOMMITTED → see L1.** `0.7.0_AE~A` lands it in-lane; `1.0.0_SA_CTO` confirms the exercised evidence stands post-amend.
5. **SERVE-GATE PHASE-2** (foreign-author REFUSE + `OPAL_AGENT_SERIAL` pusher-identity). NOT started (Phase-1 = `d7359a797`). `1.0.0_SA_CTO` builds post-reboot; `2.0.0_SA_COO` gates (hardest: no-regression on clean self-push + fail-closed direction + whole-range removal-detection). Resume: `safe_deploy_core.py:35-48`.
6. **AWS-SHIM** (Andrew-direct, LIVE on this host). Shim ACTIVE at `.tools/aws` (**gitignored — filesystem survives a fabric reboot**; if a cleanup wipes untracked `.tools` files, re-provision from Appendix A of the brief @ `19fde37de`). Ratification routed to `1.0.0_SA_CTO~D` (author-conflict: base-CTO authored it): ratify mechanism + tracked-provisioning + the CLAUDE.md line.
7. **COMPLEARN P3a + NEVER#7 SHIM** (lower heat). P3a audit DELIVERED @ `2526d3856`; `1.0.0_SA_CTO~D` rules per-source dispositions; build items → `0.8.0_AE` on GO. NEVER#7 durable git shim: base-CTO's, Tier-0-tagged when-capacity (**`pull.rebase` re-set is undetectable until the shim lands**).

*(None of §4 is Andrew-gated.)*

---

## 5. ANDREW-GATED DECISIONS — CONSOLIDATED

| # | Decision | Who is blocked |
|---|---|---|
| 1 | AoR **never-widen co-sign + GO** | COO, DS, RD — *only after round-8.2 + both gates clear; not imminent* |
| 2 | OPAL_ASSETS **P1 sovereign nod** (49F/Schwab build: G1/G2/G3a) | COO, AE — *scope-lift technically covers it; MSTR holds for his explicit word* |
| 3 | **2021 back-fill vendor call** | — *non-gating; G3a (2023-07-12 floor) proceeds without it* |
| 4 | **08335338 residue: purge or keep** | `0.7.0_AE_CloudOps` — **hard-blocked, hold is absolute** |
| 5 | portal SEV1 flip · bd-cron-under-hold · cot→bd 1143 | various — *pre-existing, untouched this session* |

## 6. STANDING RULES (survive the reboot)

- **No alerts until the process is done and proven.** Never gate a go-live on alert DELIVERY.
- **Sovereign 49F/Schwab/bd hold STANDS** except inside OPAL_ASSETS' commissioned scope; served cutovers ride NEVER#2 + NEVER#4.
- **Persist expensive multi-agent workflow findings durably** — synthesized record + raw outputs, committed (done for AoR @ `66f8f1e06`).
- **Identity: `.comp-graph/.agent_context` is NOT an identity source** (G-B). Post-reboot the check is your own.
- **Authorization lives in the GRANT FILE, not session memory** (`org/mcp/andrew_grants/`).
