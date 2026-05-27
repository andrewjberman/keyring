# ws-charter cycle 0078 — 2026-05-27T~15:57Z — REPAIR-AMENDMENT-class (FIND_INSURE v0.2 5-message Andrew-cluster + COO ARCH-ASK Option (a) ruling)

**archetype:** SCRIBE
**secondary_archetypes:** COORDINATE

---

## Classification

**Self-correction-upstream-of-verify-channel** (per [[feedback_self_correction_upstream_of_verify_channel]]) — NOT a true REPAIR-AMENDMENT (no CVO finding gate fire). 5 Andrew-direct follow-on messages in ~30min window expand the v0.1 PRD scope + correct authoring inconsistencies pre-impl. ws COO surfaces the path-conflict as ARCH-ASK 16:05Z; my v0.2 commit IS the ruling (Option (a) = honor existing scaffolding + fabric medallion convention).

Not a NOVEL-extension either (no new project; same FIND_INSURE PRD evolution v0.1 -> v0.2). FIX-class within active-project authoring is the cleanest classification — autonomous CTO authority per /ws-charter Step 4b ladder.

## Inbox classification (this turn — 5 Andrew direct messages + 2 fabric replies)

| # | From | Class | Substance |
|---|---|---|---|
| 1 | Andrew | ANDREW_DIRECTION | "include Lusha API docs somewhere relevant" + "data/find/ folder, first subfolder imo" |
| 2 | Andrew | ANDREW_DIRECTION | canonical Lusha docs URL `https://docs.lusha.com/apis/openapi/section/data-source-and-privacy` |
| 3 | Andrew | ANDREW_DIRECTION | Stage 2 Part B = Glassdoor/Indeed/etc job-posting scrape; investment-keyword + Series-license + corp-finance/tech-hire detection; M&A/growth-activity rationale |
| 4 | Andrew | ANDREW_DIRECTION | Stage 2 Part B staged-attack — HAR-analysis primary, Bright Data fallback (Andrew supplies HARs) |
| 5 | Andrew | ANDREW_DIRECTION | Lusha API key handoff [SYNC] for AWS Secrets Manager provisioning |
| 6 | Andrew | ANDREW_DIRECTION | Lusha REST endpoints (Search/Enrich/S&E/Prospecting/Lookalikes/Signals) inform Stage 2+3 process architecture |
| 7 | ws COO | DRIVE_ESCALATION + ARCH-ASK | (a) Phase 0 TO trio decomposed `2d6e29170`; (b) ARCH-ASK on data/find_insure vs data/find/imo path conflict + 8-stage-named vs 5-medallion subdir conflict |
| 8 | ws CVO | CVO_CC | Mode B PRE-EXECUTION pre-propagate gate verdict `a5920688c` CLEAN-with-2-additives (additives routed to COO; no CTO action) |

## Action

### Scribe artifacts landing this commit (6 files)

1. **`docs/architecture/FIND_INSURE.md`** (v0.1 -> v0.2 amendment):
   - §3.2 bucket layout extended to add `job-posting-scrape` channel under bronze/silver/gold
   - §3.3 external dependencies extended (Bright Data dual-use; LushaAI v3 reference link; job-board providers TBD per Stage Bα/Bβ matrix)
   - §3.4 orchestration sketch redrawn (Phase 2 = TWO PARALLEL CHANNELS Part A LinkedIn + Part B Job-postings)
   - §4 Phase 2 split into Part A + Part B with full deliverable enumeration
   - §4 Phase 2 Part A — Lusha endpoint mapping table (Search / Prospecting / Enrich / Search-and-Enrich / Account) baked into deliverables
   - §4 Phase 2 Part B — staged-attack-plan (Stage Bα HAR-analysis + Stage Bβ Bright Data fallback) + 4 deliverables (per-board endpoint manifest brief + crawler + parser + scorer)
   - §4 Phase 3 extended with Lookalikes + Signals + Webhooks enrichment overlay (Stage 3 sub-class)
   - §6 + §7 (AC3a/AC3b split) + §9 (Q6/Q7 added) + §10 (Stage Bα brief + Lusha key landed) + §11 path corrections (`data/find_insure/` -> `data/find/imo/` global replace_all)
   - Authoring lineage extended with v0.2 5-message cluster + COO ARCH-ASK ruling + CVO Mode B pre-propagate verdict

2. **`docs/reference/lusha-api-v3.md`** (NEW):
   - Workspace reference doc for Lusha API v3 (Andrew-provided full text + canonical URL <https://docs.lusha.com/apis/openapi/section/data-source-and-privacy>)
   - 12 sections: overview, endpoint catalog, data source + privacy, auth, rate limits, error codes, endpoint summary by category, billing model summary, webhooks (security + payload + ACK + opt-out), error response shape, FIND_INSURE integration mapping table (decision-ready), open questions Q-L1..Q-L4 routed back to Andrew + AE 0.7
   - Notes upstream as source-of-truth; workspace copy for offline reference + change-tracking

3. **`data/find/README.md`** (NEW): macro-level scaffold — per-project subtree convention `data/find/{project_slug}/` + medallion (bronze/silver/gold/serving/_meta) script-layer split + comp-graph + Rule-15 (`from __future__ import annotations`) + emoji-ban discipline + active FIND projects table + external-API reference doc index.

4. **`data/find/imo/README.md`** (NEW): project-level scaffold — phase-entry-point TO-anchor map (TO -> script path) + external dependencies + compiler-tools mandate.

5. **`data/find/imo/scripts/{bronze,silver,gold,serving,_meta}/.gitkeep`** (5 NEW empty files): create the medallion-by-layer subdir skeleton aligned with fabric convention (orion/mdpf/black_diamond pattern).

6. **`org/projects/FIND_INSURE.json`** (UPDATE): narrative + blocking field rewritten to reflect v0.2 amendment cluster + COO Phase 0 decomposition + AMEND-HOLD status + Lusha key handoff.

7. **`org/tier1_exec/1.0.0_SA_CTO/logs/2026-05-27/ws-charter_1557Z.md`** — this log.

### COO ARCH-ASK 16:05Z ruling

**RULING: Option (a) — honor existing scaffolding + fabric medallion convention.**

Reasoning:
- **Fabric consistency:** all existing `data/*/scripts/` trees (orion, mdpf, black_diamond, inflection, demo, smartx) use medallion-by-layer subdirs with stage embedded in filename. Option (b) creates a new fabric pattern; Option (a) preserves cross-fabric consistency.
- **Lambda naming:** `{verb}_{channel}_{layer}.py` (e.g., `crawl_web_bronze.py`) is the natural shape; the medallion subdirs let comp-pipescript treat layer as a first-class axis.
- **Comp-graph clean:** `data/find/imo/scripts/bronze/crawl_web_bronze.py` is the comp-graph-natural representation; the orchestration sketch (PRD §3.4) refers to Lambda function names not directory paths so no PRD redraft needed.
- **Authoring chain caught it pre-impl:** AE 0.7 surfaced the conflict at BLOCKED-ASK before any code was written; per [[feedback_self_correction_upstream_of_verify_channel]], no waste. Clean fold-into-amendment.

This v0.2 PRD IS the ruling artifact. PRD §6 + §11 paths corrected via replace_all. AE 0.7's TO FIND_INSURE.003 AC1 should reflect medallion-by-layer convention; COO authors the amendment-clean re-statement post-CTO-ratify-of-v0.2 (this commit).

### Lusha API key handoff (separate MCP, not in commit)

Andrew handed me the Lusha API key directly. Per Abilities-by-Role (SA = docs only / no AWS deploy), routing to AE 0.7 via MCP for the `secretsmanager:PutSecretValue` call. Key NOT in any committed file. AE 0.7 lane scope per FIND_INSURE.001 TO already includes the secrets-wiring step.

## Compiler tools

| Tool | Run | Outcome |
|---|---|---|
| `comp-blast` | N/A | No code touched in commit — pure architectural scribe + docs + skeleton. |
| `comp-pipescript io` | N/A | No script touched; data/find/imo/scripts/ are empty placeholders. |
| `comp-iam service` | N/A | No Lambda authored. |
| `comp-graph` registration | DEFERRED | TO FIND_INSURE.003 (AE 0.7) handles comp-graph registration once skeleton + first script land. |

Skeleton + READMEs + reference doc are pre-script artifacts; compiler-tool gate fires once Phase 0 scripts land.

## Banking observations

### 5-message-Andrew-cluster pattern

Andrew's NOVEL-direction flow today shipped in 6 messages spanning ~45min:
- T+0 15:15Z: initial NOVEL direction (PRD scope + bucket structure + 3 phases) -> v0.1 ship
- T+~30min 15:45Z: Lusha doc text + data/find/imo/ path
- T+30min+: Lusha canonical URL
- T+35min: Stage 2 Part B addition
- T+40min: Stage 2 Part B HAR-staged-attack
- T+42min: Lusha API key handoff
- T+45min: Lusha endpoints inform Stage 2+3 architecture

Bursty NOVEL direction is normal — Andrew thinks through the project iteratively and lands directions in real time. The clean handling pattern: v0.1 ship fast on the core direction, then v0.2 amendment cluster folds in the follow-ons before downstream impl waste accumulates. AE 0.7 BLOCKED-ASK 16:05Z = the empirical-anchor-data that v0.1-to-v0.2 fold needs to happen FAST (so .001+.003 unblock).

Sister pattern to [[feedback_self_correction_upstream_of_verify_channel]] empirical-anchor: authoring chain caught my v0.1 path inconsistency at AE 0.7 BLOCKED-ASK pre-impl; no /verify-channel REPAIR-AMENDMENT was needed.

### Lusha endpoints-as-architectural-input pattern

Andrew's framing in message #6 ("Lusha uses a RESTful API with numerous useful endpoints which will inform our Stage 2 and 3 process architecture") is a doctrine for ALWAYS scoping external-API integrations endpoint-by-endpoint at the PRD layer, not just at TO authoring layer. Bakes the cost-discipline + capability-mapping conversation EARLIER in the chain. Adopted: PRD §4 Phase 2 Part A + Phase 3 now have explicit Lusha endpoint mapping tables. Lookalikes + Signals + Webhooks all rendered as Stage 3 enrichment-overlay class.

### Path-conflict-at-PRD-vs-scaffolding pattern

PRD v0.1 said `data/find_insure/` (one path). My follow-on scaffolding said `data/find/imo/` (different path, better convention). Untracked scaffolding from `Write` calls landed before commit; subsequent commit would have surfaced the conflict at git-add time IF the .gitkeeps were committed alongside the v0.2 PRD edit. ws COO + AE 0.7 caught the divergence via downstream BLOCKED-ASK pre-commit.

Doctrine refinement: **when authoring scaffolding mid-amendment, the PRD edit MUST land in the SAME commit as the scaffolding to avoid downstream-noise-class conflict**. v0.2 commit lands both in one safe-commit. Banking as a sub-class of [[feedback_self_correction_upstream_of_verify_channel]] — "authoring-chain catches scaffolding-PRD path mismatch pre-impl".

## Next-cycle expected state

- ws COO ACK on v0.2 ratify; AMEND-HOLD on .001+.003 clears; AE 0.7 unblocks for FIND_INSURE.001+.003 execution (post-.012-Fire-1 RAVC2 window ~19:00Z).
- Andrew supplies HAR captures pre-Phase-2-Part-B (Q6 of PRD §9) — timing flexible.
- Lusha API key landed in Secrets Manager via AE 0.7 (separate MCP this turn).
- v0.3+ candidate scope (Lusha Lookalikes + Signals + Webhooks) opens post-Phase-3-RAVC2 — not v0.1 scope.

— ws CTO cycle 0078 REPAIR-AMENDMENT-class log complete
2026-05-27T~15:57Z
