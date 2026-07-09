# NFRA_LOCALROOT — P3: the homeless-knowledge consolidation MOVE-MAP (grep-proof-no-dangling)

**Project:** NFRA_LOCALROOT (Andrew-direct) · **Author:** 2.0.0_SA_COO (base) · **Date:** 2026-07-09 · **Phase:** P3 item (b)+(c)
**Grounds on:** the live `/infra` filesystem audit 2026-07-09 (`find infra -maxdepth 1` + per-subdir `ls`).
**Governing plan:** `NFRA_LOCALROOT_P2_taxonomy_plan.md` (the 13-class taxonomy + the §4 hybrid scheme). **Index:** `infra/README.md` (9ef13fd5c).

---

## 1. Audit result — /infra is ALREADY substantially homed (this is a reconcile, not a migration)

Every `infra/` top-level directory maps 1:1 to a taxonomy-class home (P2 §2/§3). Grounded `find infra -maxdepth 1 -type d`:

| /infra dir | Taxonomy class (P2 §2) | Status |
|---|---|---|
| `aws/` | Cloud RESOURCES (estate) | homed — NFRA_TERRAFORM domain |
| `system/` | System CONTENT | homed — NFRA_SYSTEM domain (06_current_state runtime) |
| `security/` | Security | homed (README + 4 arch docs) |
| `linting/` `orchestration/` `testing/` | Operational function-tooling | homed (each: README + content) |
| `architectural_docs/` | Architecture decisions | homed |
| `prompts/` `rag/` | Prompts / RAG assets | homed |
| `website/` | Project docs-home (governed sub-pattern, P2 §4) | homed |

**No directory is homeless.** The taxonomy is fully realized on disk; LOCALROOT is confirmed a reconcile+index job (as P2 §0 grounded), not a greenfield move.

## 2. Loose files at `infra/` root — disposition (the ONLY move-map entries)

`find infra -maxdepth 1 -type f`:

| File | Disposition | Reason |
|---|---|---|
| `infra/README.md` | **STAY** | It IS the index (P2 §5) — correct at the entry-point root. |
| `infra/.gitignore` | **STAY** | Infra-tree hygiene — correctly scoped at the tree root. |
| `infra/launch_agents_powershell.ps1` | **MOVE → `infra/orchestration/launchers/`** | The ONE genuinely-homeless item: a loose agent-launcher script. Its taxonomy home is Operational function-tooling / orchestration, and `infra/orchestration/launchers/` already exists as the exact home. |

**That is the entire move-map: one file.** /infra carried exactly one homeless artifact.

## 3. grep-proof-no-dangling (the P3 (b) acceptance bar)

`grep -rn "launch_agents_powershell"` across the workspace = **1 hit only**, and it is NOT an operational reference:
- `org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_LOCALROOT.decomp-and-P2-taxonomy-direction.md:26` — my own P2-direction TO describing it as "at root" (a status note, not a path dependency).

No script, launcher, cron, doc, or config references `infra/launch_agents_powershell.ps1` by path. **The move is dangling-free — safe to `git mv`.** (After the move, the P2-direction TO line self-corrects — it described the pre-move state.)

## 4. The 3-emerging-homes reconcile — item (c): CONFIRMED already resolved (P2 §4)

CTO's arch-note (website/ + system/ + aws/terraform/ must reconcile into ONE scheme, not 3 precedents) was resolved in P2 §4 by the **HYBRID scheme**: by-knowledge-class top-level homes (aws=estate, system=content, security/linting/orchestration/testing=function-classes) + **project docs-homes** (`infra/{project}/`) as a recognized, governed sub-pattern. Re-audited 2026-07-09: `website/` is the ONLY project-docs-home; `system/` + `aws/` are class-homes; **no new ad-hoc top-level home has crept in since P2.** Item (c) = closed, and the scheme held (no scatter regression).

## 5. Execution + gating

| Item | Action | Lane / gate |
|---|---|---|
| The 1 move (`.ps1` → `orchestration/launchers/`) | `git mv` + commit | **AE lane** — `infra/` root is `CLOUD_OPS_OR_ETL` (base COO NOT carved for it). Queued for 0.5.0 as a trivial post-BATCH-C hygiene commit (non-urgent, grep-clean). Do NOT interrupt the BATCH-C import flow for it. |
| (a) docs-home carve extension | owned-paths carve `infra/README.md` + `infra/architectural_docs/**` → `ANY_EXEC_OR_AE` | **SoD grant** — base COO is grantee, so COO~B (or CTO) lands it (reciprocal of the `infra/system/**` carve base COO landed for COO~B at 336731af4). Routed to COO~B this tick. |

## 6. P3 status after this deliverable

- **(b) move-map — DONE** (this doc; 1 move identified, grep-proof-clean, execution queued to AE lane).
- **(c) reconcile 3 homes — DONE** (P2 §4 hybrid scheme; re-audit confirms no regression).
- **(a) docs-home carve extension — DISPATCHED** to COO~B (SoD grantor); closes on the carve landing + base COO's confirming commit.
- **P4 anti-scatter convention** follows (the standing "new knowledge → which home" rule; the index §A.1 arch-doc routing rule is the first instance).

LOCALROOT-P3 closes when: the carve lands (a) + the 1 hygiene move executes (AE lane). Both are trivial + non-blocking; no live-system risk.
