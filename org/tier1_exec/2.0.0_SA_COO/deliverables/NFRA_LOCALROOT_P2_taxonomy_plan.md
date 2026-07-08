# NFRA_LOCALROOT — P2: the /infra centralization plan (taxonomy + SSOT map + index + migration)

**Project:** NFRA_LOCALROOT (Andrew-direct) · **Author:** 2.0.0_SA_COO (base) · **Date:** 2026-07-08 · **Phase:** P2 (the core deliverable)
**PRD:** docs/architecture/NFRA_LOCALROOT_PRD.md · **P2 direction (committed):** org/tier1_exec/2.0.0_SA_COO/task_orders/NFRA_LOCALROOT.decomp-and-P2-taxonomy-direction.md (9b2db7862)
**Unblocks:** COO~B's NFRA_SYSTEM-P2 arch-gate (CTO holds it pending this) + coordinates NFRA_TERRAFORM-P3.
**Grounded on:** the live `/infra` filesystem audit 2026-07-08 (this is a RECONCILE + INDEX job — /infra is already substantially organized — not a greenfield build).

---

## 1. The governing principle (the load-bearing distinction)

`/infra` is the STRUCTURAL knowledge base for the cloud + resources + architecture. Each knowledge class either:
- **CENTRALIZES INTO /infra** — cloud+resource knowledge, architecture, and the currently-homeless tribal knowledge that has no structural owner today; OR
- **is REFERENCED FROM /infra** (kept in place, indexed) — anything with an existing SSOT (git history, the live graph, the agent org, docs/architecture, doctrine). `/infra`'s README indexes them; it does NOT absorb/duplicate them.

**ONE SSOT per class, no forked truth.** A copy that drifts is worse than a scattered original. STRUCTURE, not content-rewrite.

## 2. The taxonomy table (knowledge class → home → SSOT → static/runtime → indexed-by)

| Knowledge class | Home | SSOT | Static / Runtime | Disposition |
|---|---|---|---|---|
| **Cloud RESOURCES** (the AWS estate) | `infra/aws/` (terraform/ + per-service) | TF state (DESIRED) + live AWS (APPLIED) | static TF + runtime live | **CENTRALIZE** — NFRA_TERRAFORM's domain; P3 organizes it |
| **System CONTENT** (substrate/graph/tools/federated/learning + interplay) | `infra/system/` (00_synthesis..07_maturity) | the infra/system docs + `infra/system/06_current_state` (comp-system runtime output) | static docs + runtime current-state | **CENTRALIZE** — NFRA_SYSTEM's domain (P2 tree built) |
| **Security** (policies/compliance/remediation) | `infra/security/` | the security docs | static | **CENTRALIZE** (already homed) |
| **Operational function-tooling** (linting/orchestration/testing) | `infra/{linting,orchestration,testing}/` | the tool dirs | static | **KEEP AS-IS** (rightly homed) |
| **Architecture decisions** | `infra/architectural_docs/` | the decision records | static | KEEP; cross-reference the broad arch corpus (below) |
| **Project docs-homes** | `infra/{project}/` (e.g. `infra/website/`) | the project's README+inventory | static | **GOVERNED SUB-PATTERN** (see §4) — exec/owner-committable |
| **Prompts / RAG assets** | `infra/prompts/`, `infra/rag/` | the asset dirs | static | KEEP |
| **Logs** (session/daily/git/handoffs) | `org/logs/` + agent home logs/ | org/ | static | **REFERENCE** (index from infra/README; do NOT move — org is the home) |
| **Runtime compilation** (graph/Nessie/Iceberg/Kuzu, markers, tool_activity) | the live substrate + `.comp-graph` | the live graph IS its own SSOT | runtime | **REFERENCE** — index from infra/system (ties to SYSTEM P3); never absorb |
| **Git history** (decisions/rationale) | git | git IS the decision-history SSOT | — | **REFERENCE** — index, never copy |
| **Broad architecture corpus** (docs/architecture ~313, briefs, deployment) | `docs/` | docs/ | static | **REFERENCE** — index from infra/README (the PRDs/specs stay in docs/ per convention) |
| **Agent org** (projects/task_orders/critical_paths/modules/registry) | `org/` | org/ IS the agent-org SSOT | static | **REFERENCE** — index, never absorb |
| **Doctrine** (CLAUDE.md, fabric memory, role docs) | root + memory/ | their homes | static | **REFERENCE** — index |

## 3. Target `/infra` structure (mostly already true — this formalizes + indexes it)

```
infra/
  README.md            # THE INDEX (the entry-point; §5) — routes to every home + the referenced-in-place sources
  aws/                 # cloud RESOURCES [ESTATE — NFRA_TERRAFORM] (terraform/ + ~28 per-service dirs)
  system/              # system CONTENT [BOOKS — NFRA_SYSTEM] (00_synthesis..07_maturity; 06_current_state = comp-system runtime)
  security/            # security policies/compliance/remediation
  linting/  orchestration/  testing/   # operational function-classes (keep)
  architectural_docs/  # arch decisions
  prompts/  rag/       # asset classes
  <project>/           # GOVERNED project docs-homes (e.g. website/) — exec/owner-committable (§4)
```

Only NEW top-level home vs today's audit = `infra/system/` (COO~B's SYSTEM-P2 tree, now committed). Everything else exists — this plan makes the taxonomy + index EXPLICIT + governs new homes so they don't scatter.

## 4. The GOVERNANCE rule for docs-homes (resolves CTO's arch-note + the commit-ownership seam)

CTO's arch-note: website/ + system/ + aws/terraform/ must reconcile into ONE scheme, not three independent precedents. RESOLUTION — the **HYBRID scheme**:
- **By-knowledge-class top-level homes** (infra/aws=estate, infra/system=content, security/linting/orchestration/testing=function-classes).
- **Project docs-homes** (`infra/{project}/`) as a RECOGNIZED, GOVERNED sub-pattern — for a project with substantial standalone platform docs (website is the first). Governance: each carries a README index + resource-inventory + a cross-link UP to infra/README.md + registration in the index. NOT ad-hoc; one convention.

**COMMIT-OWNERSHIP RULE (resolves the SYSTEM-P2 + data-catalog seams — CTO's docs-vs-code logic):**
- `infra/{docs-homes}/` (system/, project docs-homes) are **DOCUMENTATION** — content-owned by exec/the program, **exec/owner-committable**.
- `infra/aws/` (code/TF) + the pipeline CODE stay **AE-owned** (SoD-critical infra).
- Implemented via owned-paths carves: `infra/system/**` → exec (COO~B durably owns the SYSTEM docs); project docs-homes → their owner. Same class as CTO's `data/*/API/**` cataloger carve (docs are knowledge, distinct from AE code + the firm-data plane).

## 5. The INDEX design (Q4: static structural + runtime current-state)

`infra/README.md` = THE entry-point:
- **Section A — knowledge-class homes:** one row per class (§2) → its `/infra` home + a one-line "what lives here."
- **Section B — referenced-in-place:** git (decision history), the live graph (runtime substrate, via comp-tools), org/ (agent org), docs/architecture (the arch corpus), doctrine — each with the pointer + "SSOT lives here, not copied."
- **Section C — the runtime current-state:** link to `infra/system/06_current_state` (the comp-system compiler output — SYSTEM P3; reuse it, don't build a second index).
Static structural index (hand-maintained, low-churn) + the runtime current-state compiled by SYSTEM's comp-system. No second index mechanism.

## 6. Migration / consolidation plan (P3 — STRUCTURAL, reversible)

- **Mostly REFERENCE-in-place** (Q3 default): git/graph/org/docs/doctrine stay put; infra/README indexes them. NO content-rewrite, no forked truth.
- **CONSOLIDATE only the genuinely-homeless:** P1's audit surfaces the homeless tribal knowledge (loose infra/aws/docs with no owner, knowledge encoded only in session logs). P3 gives each a home OR indexes it — a move-map (old→new) so nothing is silently orphaned; grep-proof no dangling reference; AE-lane owned-paths for infra/aws moves.
- **Reconcile the 3 emerging homes** (website/system/aws-terraform) into the §4 scheme (they're instances, not precedents).
- Incremental + reversible (a move that breaks a consumer rolls back).

## 7. Composition with the trilogy (clean seams, no re-owning)

- **LOCALROOT (this)** = the STRUCTURE + taxonomy + index + the docs-home governance. The librarian.
- **NFRA_SYSTEM** = the CONTENT at `infra/system/` (P2 tree committed 3704cee04; its arch-gate CTO-held pending THIS plan — now settled). The books.
- **NFRA_TERRAFORM** = the ESTATE at `infra/aws/terraform/` (P1 coverage running); its P3 org lands within this /infra scheme. The estate.

## 8. Acceptance (CTO arch-gates before P3)

Every knowledge class located + classified (SSOT/scattered/referenced); exactly one SSOT per class (no fork); centralize-vs-reference distinguished; composes cleanly with SYSTEM (/infra/system) + TERRAFORM (/infra/aws/terraform) without collision; the index routes to every class. → On CTO arch-gate, P3 executes (AE-lane for infra/aws moves; exec for docs-homes per §4) + P4 anti-scatter convention.
