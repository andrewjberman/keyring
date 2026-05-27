# ws-charter cycle 0077 — 2026-05-27T~15:37Z — NOVEL (FIND_INSURE inaugural FIND-macro scribe)

**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE

---

## Classification

**NOVEL** — new macro `FIND` + new project `FIND_INSURE`. HARD-BLOCK #7 (New project code creation / REGISTRY.md Active-section additions) override path = Andrew direction this cycle (the direction message itself IS the override authorization).

## Inbox classification

**ANDREW_DIRECTION** (verbatim 2026-05-27T~15:15Z): "We have a new project, will need a new macro, called 'FIND'. The Find macro will be all about research pipelines. The initial project will be FIND_INSURE...I think you have enough grasp here to start building."

Direction is unambiguous + authorizing. NOVEL classification triggered. Per /ws-charter Step 4c NOVEL action: scribe new charter (PRD) + commit-anchor to Andrew direction.

## Action

Authored four artifacts as one safe-commit scope:

1. **`docs/architecture/FIND_INSURE.md`** — PRD v0.1
   - 11 sections: Objective, Background, Architecture (bucket structure + medallion layout + external deps + orchestration sketch), Phase plan (0/1/2/3), Source-list binding, Compiler-tools mandate, Acceptance criteria (6 ACs), Out of scope, Open questions (Q1-Q5), Cross-domain coordination, Decomposition guidance for ws COO.
   - Bucket structure per Andrew direction: `opal-data-imo/corp/{slug}/{channel}/{bronze,silver,gold}/` + `opal-data-imo/serving/{companies,employees,scoring}.{json,parquet}` at root.
   - 3-phase plan with explicit Phase-1-informs-Phase-2 gating (Andrew said "stage 1 will start to give us ideas of what IMOs we want to pursue deeper").
   - Compute target = Lambda preferred (parallelizable per IMO); EC2 fallback only if any IMO crawl >15min.
   - DS lane proposal = `0.1.0_DS_MarketIntelligence` (closest fit to YALP_MACROS Phase 2a multi-source reconnaissance); flagged as ws COO routing decision pre-Phase-1.
   - AE lane = `0.7.0_AE_CloudOps` for bucket + IAM + secrets + orchestration.

2. **`org/projects/FIND_INSURE.json`** — registry entry
   - status: active; phase narrative cites PRD ship + awaits COO TO decomposition.
   - 5-item blocking list (COO decomp + Andrew lane confirm + LushaAI key confirm + IR team consumer identification + Q1-Q5).
   - pods: ["0.1", "0.7"].
   - pipeline field describes the new `find_insure` pipeline.

3. **`org/projects/REGISTRY.md`** — Active Projects table row insertion
   - Inserted at top of Active table (newest-first convention).
   - Row content mirrors JSON narrative + cites PRD path + 5-item blocking.

4. **`org/tier1_exec/1.0.0_SA_CTO/logs/2026-05-27/ws-charter_1537Z.md`** — this log

## Authority chain

- Andrew direct directive 2026-05-27T~15:15Z (the user message) — ANDREW_DIRECTION class per /ws-charter Step 2.
- HARD-BLOCK #7 (New project code creation / REGISTRY.md Active-section additions) — override path is NOVEL classification triggered by Andrew direction, satisfied.
- Scribe authority: ws CTO autonomous NOVEL scribe per /ws-charter Step 4c (direction received, no additional ratification needed pre-scribe).
- Downstream: ws COO autonomous FIX-class authority over TO decomposition once PRD lands (LD-0072 lane discipline).

## Pre-classification HARD-BLOCK self-check

- #1 (TIER0_LAW): no — this is a PRD, not Constitution/Directives/Stakes Matrix.
- #2 (cross-fabric coordination): no — ws-only scope.
- #3 (destructive ops): no.
- #4 (S3/S4 procurement / Stakes-Matrix amendment): no.
- #5 (MCP broker config): no.
- #6 (git remote-network ops): no — standard push-to-CLOUD only.
- **#7 (new project code creation / REGISTRY Active additions): YES → override via Andrew direction this cycle = SATISFIED**.
- #8 (agent spawn/kill): no.
- #9 (memory-bank contradictory writes): no.
- #10 (safe-commit --force / TIER0_LAW override): no — clean safe-commit, no bypass.
- #11/#12/#13 (CL-specific): N/A.

Audit log `org/ws-charter-hard-block-audit.log` exists (verified Step 4a pre-classification gate). No HARD-EXIT.

## Follow-on dependencies (immediate next-cycle expected)

1. **ws COO** receives this scribe in /drive cycle next-tick; TO decomposition Phase 0 ~3-4 TOs expected (bucket+IAM, secrets wiring, source-list extractor, comp-graph registration).
2. **Andrew** has 5-item open-question queue per JSON `blocking` field — Q1-Q5 can wait until pre-Phase-2; lane routing question (item 2) is the only pre-Phase-0 gate.
3. **AE 0.7** (post-COO-dispatch) Phase 0 first TO will be bucket + IAM + secrets provisioning; AE confirms Bright Data secret namespace + asks Andrew re: LushaAI key (per JSON blocking item 3).

## Commit-tag intent

Single safe-commit:

```
.tools/safe-commit.sh --author="1.0.0_SA_CTO <1.0.0_SA_CTO@opal.agent>" \
  -m "..." \
  -- \
  docs/architecture/FIND_INSURE.md \
  org/projects/FIND_INSURE.json \
  org/projects/REGISTRY.md \
  org/tier1_exec/1.0.0_SA_CTO/logs/2026-05-27/ws-charter_1537Z.md
```

Trailer: `ws-charter-cycle:0077 class:NOVEL`.

## Compiler tools

| Tool | Run | Outcome |
|---|---|---|
| `comp-blast` | N/A | No code touched — pure PRD/JSON/REGISTRY scribe; no functional blast radius. |
| `comp-pipescript io` | N/A | No script touched; data/find_insure/ subtree creation deferred to Phase 0 TO (AE author). |
| `comp-iam service` | N/A | No Lambda authored. |
| `comp-routes` | N/A | No portal/CF surface touched. |

No comp-tool run was applicable — this is pure architectural scribe at the project-charter layer. PRD §6 enumerates the compiler-tools mandate that BINDS implementers once TO authoring lands.

## Banking observations

### Inaugural macro introduction pattern (FIND macro first-fire)

REGISTRY.md doctrine: "Multiple projects can share the same macro code. The macro code identifies the surface area; the project code identifies the specific initiative." — macros are introduced implicitly by their first project's PRD + JSON + REGISTRY row landing. No separate "macros file" exists. FIND is the 8th-ish active macro (ADVI, ADHC, MDPF, SXIN, SXPL, TRSB, YALP, now FIND). PRD §1 enumerates the FIND surface (research / discovery / alt-data pipelines) so future FIND_xxxxx projects inherit the convention cleanly.

### NOVEL-with-clear-direction → same-cycle scribe pattern

Andrew direction came in mid-cycle 0076 quiet steady-state; PRD authored + JSON + REGISTRY + log all in cycle 0077 same wall-window. Compare to ADVI_DEMOV1 v0.1 (~few hours direction-to-ship; Phase 0 probe required first) and YALP_MACROS Phase 2 RE-OPEN (~minutes; Andrew override countermanded prior CVO ruling). FIND_INSURE is the cleanest novel-direction-to-scribe path of the session — explicit 3-stage plan + bucket structure + dependencies all named in the direction itself.

### CTO direction-only constraint satisfied transparently

Per /ws-charter Step 4b: "ws CTO does NOT autonomously originate NOVEL. Andrew direction in inbox this cycle is the gate." Direction satisfied gate; HARD-BLOCK #7 override path engaged; no CTO autonomy-overreach. Clean precedent for future NOVEL fires.

## Next-cycle expected state

- /drive cycle next (ws COO) will surface FIND_INSURE in JSON-driven sweep; COO authors Phase 0 TOs.
- /spot-check cycle next (ws CVO) may verify alignment of REGISTRY row vs JSON narrative vs PRD authoring (REGISTRY-vs-JSON drift class per `feedback_drive_read_json_not_registry`) — expectation = GREEN, all three authored together in same commit.
- No /verify-channel finding expected — no pipeline output to verify yet (Phase 0 hasn't run).

— ws CTO cycle 0077 NOVEL log complete
2026-05-27T~15:37Z
