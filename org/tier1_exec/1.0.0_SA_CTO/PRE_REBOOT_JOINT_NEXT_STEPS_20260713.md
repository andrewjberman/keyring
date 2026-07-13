# PRE-REBOOT JOINT NEXT-STEPS LOG — 2026-07-13

**Authors:** `1.0.0_SA_CTO~B` (drafted) + `1.0.0_SA_CTO` (base — section merged on receipt). **Andrew-direct:** *"i need you and CTO Base to discuss and collaborate on a joint log of next steps, then im going to reboot the fabric partially. in this log we need /stimulus-scan qualification of which agents are tasked with what to get the next steps for each current hot project done."*

**THIS DOC IS THE SURVIVAL ARTIFACT.** Assume every agent named here is dead and re-spawned. Each must be able to self-onboard from this doc alone: it names the serial, the exact deliverable, the artifact/commit to resume from, and what it is blocked on.

---

## 0. FABRIC QUALIFICATION AT WRITE TIME (stimulus-scan, 0442Z)

**LIVE (7):**

| Serial | State | Holding |
|---|---|---|
| `0.0.0_AB_MSTR` | LIVE | Spawn authority; fabric coordination |
| `1.0.0_SA_CTO` (base) | LIVE | Resuming base duties after an identity mis-adoption incident (self-disclosed, corrections in flight) |
| `1.0.0_SA_CTO~B` | LIVE | AoR go-live principal + never-widen; OPAL_ASSETS arch-gate |
| `2.0.0_SA_COO` | LIVE | /drive cycle 4; co-sign paused; OPAL_ASSETS backfill executing |
| `0.7.0_AE_CloudOps` | LIVE | **08335338 backfill HALTED + HELD-SOVEREIGN-GATED** (residue held, IAM staged, ledger `69983008e`) — awaits Andrew ruling |
| `0.7.0_AE_CloudOps~A` | LIVE (idle) | OPAL_ASSETS P0-A table built + gated; emitter/backfill |
| `0.8.0_AE_CloudComp` | LIVE | OPAL_ASSETS G4 ownership fold + G5 — **UNBLOCKED** (both my rulings issued 0438Z) |

**DEAD / NOT REGISTERED — BUT REQUIRED FOR THE HOT PATH. THESE MUST BE RE-SPAWNED FIRST:**

| Serial | Why it must come back | Resumes from |
|---|---|---|
| **`0.4.0_DS_ClientPlatform`** | **Owns ROUND-8.2 — the single blocker on the AoR go-live.** Also owns OPAL_ASSETS P0-B and the D_02b grounding. | `docs/briefs/advisor-of-record-go-live-gate-findings-20260713.md` @ `66f8f1e06` (F1–F10 ranked, file:line) |
| **`3.0.0_SA_CVO~B`** | Owns gate-2 re-verify of round-8.2. Her battery + fixtures exist (`scratchpad/aor_round8_battery.py`). | Same doc §3.2/§5 + my 0433Z re-verify scope msg |
| `3.0.0_SA_CVO~A` | OPAL_ASSETS FP-R0 schema review of the PRD | `docs/architecture/OPAL_ASSETS_PRD.md` @ `79231da3e` |
| `0.4.2_RD_AdvisorIntelligence` | FE noel_soderblom card — DONE but HELD (`73ee2705` + `b005545e`, **unpushed on portal DEV**) | Awaits the coordinated go-live ping only |

**COLD (not needed for the hot path):** `3.0.0_SA_CVO` (base), `1.0.0_SA_CTO~D` (LIVELEARN part-1 complete), `0.7.0_AE_CloudOps~C`.

---

## 1. HOT PROJECT — INF Advisor-of-Record go-live (P0)

**State:** Round-8 SSOT refactor BUILT + GATED. Andrew's design (resolve AoR once at a front-of-chain resolver; every view inherits a canonical field; zero per-view structuring) is implemented: fold census 10→1, household 4→1. **Gate-2 CLOSED VERIFIED** (r8+r8.1). **Gate-1: architecture SOUND — no round-7-class false-green — but F1–F10 require ROUND-8.2 before switch-ON.** **Nothing served. Switch OFF. Everything SERVE-HELD. Zero live impact.**
**Commits:** `345c85daa` + `5581c0de1` (round-8) · `68be1809d` (r8.1 firebreaks) · `63dd76201` (CHANGE-3 silver raw passthrough, SERVE-HELD, a HARD go-live precondition).
**Full record + ALL raw workflow artifacts (32-agent journal + both review outputs):** `docs/briefs/advisor-of-record-go-live-gate-findings-20260713.md` @ `66f8f1e06`.

**NEXT STEPS (ordered) + AGENT→TASK:**

1. **`0.4.0_DS_ClientPlatform` [RE-SPAWN] → ROUND-8.2.** Fix F1–F10 from the findings doc. **F1 is the blocker:** `orion-gold-dispatch.sh:353/354` gates the resolver `INF_A_0` entry on `INF_AOR_FOLD_ACTIVE=1` while ALL migrated consumers call `load_resolution()` UNCONDITIONALLY (raises if absent) — **so a switch-OFF, our documented rollback, DROPS the resolver → consumers raise → the nightly ABORTS. The rollback is not a rollback.** Make the resolver entry UNCONDITIONAL. Then F2 (NaN advisor_key on A_00/resolver as-of skew), F3 (incomplete state-cache greens a real change), F4 (**CTO~B RULED: KEEP the fail-closed RAISE** — plurality fallback would resurrect the per-view derivation the SSOT kills; fix C_02's try/except gap + reconcile D_02c's contract), F5–F10. Keep SERVE-HELD + switch OFF.
2. **`1.0.0_SA_CTO~B` → gate-1 re-review** of the round-8.2 delta. I hold the F4 ruling and the pending D_02b ruling.
3. **`3.0.0_SA_CVO~B` [RE-SPAWN] → gate-2 re-verify.** **F1 must be exercised THROUGH THE DISPATCH, not resolver-direct** — her DELTA-0 (0/871) was measured resolver-direct, which is exactly the instrument gap F1 exposes.
4. **`2.0.0_SA_COO` → co-sign PAUSED** until both gates clear. Owns the release checklist: CHANGE-3 silver deploy → round-8.2 in → switch ON + sentinel-lift + **resolver entry UNCONDITIONAL (F1)** + FE promote → V4 served-verify.
5. **`0.4.2_RD_AdvisorIntelligence` [RE-SPAWN at go-live only]** → push the held FE noel card.
6. **`0.4.0_DS` → D_02b grounding** (post-round-8.2): `INF_D_02b` carries a LOCAL rep_id map reversing peter↔patrick vs canonical. **HYPOTHESIS ONLY** (live mis-attribution vs different partition semantics) — Rule-22 source-grounding required; **NO fix until CTO~B rules on the grounded mechanism.**

**ANDREW-GATED:** the never-widen co-sign + GO.
**⛔ SMS / ALERT-DELIVERY: CANCELLED, STRUCK FROM THE CHAIN.** Andrew-direct: *"we're not doing sms... i dont like to talk about alerts until the actual process is done because usually the alerts are miscalibrated and then its spam on my devices."* Detectors still WRITE findings (stdout + ops queue); nothing pages Andrew. **Do NOT re-raise alert wiring/calibration until the process is DONE and PROVEN.**

---

## 2. HOT PROJECT — OPAL_ASSETS (14-cohort daily AUM)

**State:** PRD v0.1 + registry authored + MSTR-accepted (`79231da3e`). **P0-A base table `opal-assets-daily-aua` is DEPLOYED and LIVE — COO-verified 14 rows with honest states; backfill executing.** Andrew has a queryable daily table.

**NEXT STEPS + AGENT→TASK:**

1. **`0.7.0_AE_CloudOps~A` [LIVE] → P0-A emitter + backfill** of served days. Table arch-gated **ACCEPT-AS-BUILT** by CTO~B (`70687ba8a`; PK=`run_date`/SK=`cohort_id` + GSI `cohort_history` — the served daily cross-cohort read is strongly-consistent on the base table, which is *better* than my original criterion).
2. **`0.8.0_AE_CloudComp` [LIVE, UNBLOCKED] → G4 ownership fold + G5 convergence.** CTO~B rulings issued: (a) the **additive-rows dimension is APPROVED on ONE CONDITION — every row must carry an explicit `value_class` (self-classifying)**, because the base PK=`run_date` partition read returns base + ownership rows together and a naive consumer would mix/double-count them into AUM (a served/never-widen defect); (b) **RATIFIED: measured `opal-data-etfs/daily` is the ONE canonical held-source per partner — NEVER mdpf `etf_decomposition` target_weight** (a target weight is intent, not an observation; a served ownership figure must come from the measurement).
3. **`0.4.0_DS_ClientPlatform` [RE-SPAWN] → P0-B** (G4 interim avgcap-only fold + mdpf emitter extension) — GO'd only **after** round-8.2 frees DS. Interim rows carry a disclosed `partial: 08242234-only` flag; its removal = G4 DONE (PRD AC4).
4. **`3.0.0_SA_CVO~A` [RE-SPAWN] → FP-R0 schema review** of the PRD.
5. **`0.7.0_AE_CloudOps` [LIVE] → 08335338 backfill: HALTED + HELD-SOVEREIGN-GATED.** Residue held, IAM staged, ledger `69983008e`. **Hold is ABSOLUTE pending Andrew's explicit ruling.**

**ANDREW-GATED (3 open):** (a) **P1 sovereign nod** — the 49F/Schwab build (G1 feed-freshness, G2 08335338 ingest + new CBUGL parser, G3a backfill to the 2023-07-12 floor); (b) the **2021 back-fill vendor-channel call** (non-gating on G3a); (c) the **08335338 residue purge-or-keep ruling** (0.7.0_AE is blocked on this).

---

## 3. CTO-BASE SECTION — *[MERGE POINT: awaiting `1.0.0_SA_CTO`'s hot projects + agent→task; will be appended verbatim and re-committed]*

---

## 4. ANDREW-GATED DECISIONS — CONSOLIDATED (everything waiting on him)

| # | Decision | Who is blocked | Notes |
|---|---|---|---|
| 1 | AoR never-widen **co-sign + GO** | COO, DS, RD | Only after round-8.2 + both gates clear. Not imminent. |
| 2 | OPAL_ASSETS **P1 sovereign nod** (49F/Schwab build) | COO, AE | Scope-lift technically covers it; MSTR is holding for his explicit word (surface-don't-adjudicate on the sovereign edge). |
| 3 | **2021 back-fill vendor call** | — | Non-gating; G3a (2023-07-12 floor) proceeds without it. |
| 4 | **08335338 residue: purge or keep** | `0.7.0_AE_CloudOps` (hard-blocked) | Hold is absolute. |
| 5 | (from MSTR's board) portal SEV1 flip · bd-cron-under-hold · cot→bd 1143 | various | Pre-existing open decisions, not touched this session. |

---

## 5. STANDING RULES REAFFIRMED (survive the reboot)

- **No alerts until the process is done and proven** — never gate a go-live on alert DELIVERY (Andrew-direct, above).
- **Sovereign 49F/Schwab/bd hold STANDS** except inside OPAL_ASSETS' commissioned scope; served-output cutovers still ride NEVER#2 never-widen + NEVER#4.
- **Persist expensive multi-agent workflow findings durably** (Andrew-direct) — synthesized record + raw outputs, committed. Done for AoR @ `66f8f1e06`.
- **Nothing in the AoR chain is served.** Switch OFF, SERVE-HELD, zero live impact — a reboot loses no served state.
