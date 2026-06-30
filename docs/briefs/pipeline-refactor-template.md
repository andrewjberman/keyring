# Pipeline Refactor Template — the reusable audit → spec → validate → PRD → implement → verify playbook

**Author:** 3.0.0_SA_CVO (Andrew-direct) | **Date:** 2026-06-30 | **Status:** canonical methodology
**Purpose:** Codify, in detail, the exact process run for **Inflection** (audit → refactor-spec batch → INFREF PRD) so it is repeatable for **Cottonwood** and **49 Financial** — and any future firm pipeline. Custodian-agnostic; the per-firm platform/mechanism plugs into the same arc (§9 firm-variant adaptations).
**Worked reference example (follow these as the gold standard):** `inflection-bronze.md` / `-silver.md` / `-gold.md` (as-is audits) + `inflection-refactor-{bronze,silver,gold,runtime}.md` (specs) + `seams_*_inflection_*.md` (the 3-seam check). INFREF = the resulting CTO PRD.

---

## 0. The shape (what this template produces)

For each firm, the arc produces, in order:
1. **3 as-is AUDIT docs** (`{firm}-bronze.md`, `-silver.md`, `-gold.md`) — what the pipeline IS, grounded.
2. **A 3-SEAM check** (`seams_{HHMMZ}_{firm}_bronze_silver_gold.md`) — where it's broken, 3-axis.
3. **4 REFACTOR SPEC docs** (`{firm}-refactor-{bronze,silver,gold,runtime}.md`) — to-be + migration + ACs.
4. **A CTO PRD** (the spec batch handed off; CTO authors).
5. **Implementation** (COO decomposes → DS data legs + AE Terraform/infra legs).
6. **CVO `/verify`** of the implementation vs the specs + PRD (100% alignment, certify-nothing-until-clean).
7. **Post-setup**: an incremental-chain spec, then a full-vs-incremental scheduling-policy spec.

**The non-negotiable spine (every phase):** ground against the **DEPLOYED / LIVE / SERVED** artifact — never source, self-report, or stale memory. *Committed ≠ deployed; "ran" ≠ landed; "applied" ≠ live; deployed ≠ resolved.* A causal/mechanism claim is a hypothesis until source/graph-confirmed (Rule 22).

---

## 1. PHASE 0 — Audit the as-is pipeline, layer by layer

Goal: a complete, grounded map of the firm's pipeline ingestion→silver→gold→served, and the variance/breaks in it.

**Method (per layer):**
- Estate map first: `pipescript <thread>` / `comp-pipescript io` / `comp-freshness chain` — every resource, producer→served→consumer, owning tool, freshness. No silent Unknown.
- **The endpoint/format contract** (bronze): what each SOURCE provides, the exact endpoints, and the file format *the source emits* (don't assume). Enumerate from the existing catalog/HAR/crawler if one exists (don't re-derive). State the completeness basis honestly (catalog-complete vs bounded-complete-no-vendor-catalog).
- **The variance inventory** (every layer): hunt the "forked unified path" disease — duplicate scripts, layout splits, redundant execution layers, multiple copies of a dim, legacy/stray trees. A **complete prefix census** (`s3://.../{bronze,silver}/` every prefix classified) so nothing is missed.
- **/draw it** (house style) — ingestion→silver→gold→served with real script/resource names and the break-points marked. The operator reads the draw to reason about the system.
- Ground every number against the **live/served** artifact (S3 sums, version history, partition enumeration). Penny-check values; size/shape forensics for clobbers.

**Deliverables:** `{firm}-bronze.md`, `-silver.md`, `-gold.md` — each: layer structure, the contract, the variance inventory, the break(s), grounded evidence, Compiler-Tools table. (gold audit includes the **gold→portal feed** addendum.)

## 2. PHASE 0.5 — Localize the break with `/seams`

Run `/seams` on each boundary (ingestion→bronze, bronze→silver, silver→gold), 3-axis, grounded vs live (use the *sharpest current-day test*):
- **MECHANICAL** — does the joint physically carry the flow (or no-op / mis-route / stale-partition / hang)?
- **DECLARATIVE** — does the record (docstring/PRD/name/status) match the live implementation?
- **SEMANTIC** — is the payload the *right* value, quality-validated (parity to custodian to the cent; vintage; magnitude/sign)?
- **Weakest-seam-binds:** the pipeline's verdict is its worst joint. Localize the break to ONE seam; source-confirm the mechanism (Rule 22) before asserting a fix.

## 3. PHASE 1 — Lock the cross-cutting decisions WITH the operator

Before specs, settle the governing principles at each `[DECISION]` fork — these bind every layer. The Inflection set (adapt per firm):
- **Bronze = RAW, native format, ALL fields, no conversion, no redaction.** Format→parquet and fact→dim are SILVER concerns. Bronze's only job = ingestion + consistent bucket structure.
- **Domain separation** through bronze + silver; cross-source/cross-domain join ONLY at gold (each source = own prefix; e.g. `bronze/{src}-api/`).
- **Single execution layer** (one machine pulls → silver → gold) where firm size permits; decommission everything else.
- **Full fidelity** silver (no field dropped bronze→silver; the converter = dtype/dedup/name-standardize only).
- **No-tolerance value-parity** (served == custodian source TO THE CENT; Andrew-direct — a band silently passes a wrong number).
- **Source-of-truth model** (which custodian is SSOT; what enrichment layers exist) — the big firm-variant decision (§9).
- **"Remove-now-reopen-if-gap"** posture for simplifications (verify the per-consumer edge before deleting anything).

Decide these *with the operator*, one fork at a time; record each as ANDREW-LOCKED or `[DECISION]` (for CTO/operator ratification in the PRD).

## 4. PHASE 2 — Author the refactor spec batch (SPEC-1..4)

One doc per layer; consistent spine: **governing principles → target layout → consolidation → retroactive/migration work → machine-checkable acceptance criteria → `[DECISION]` ratification points.**
- **SPEC-1 bronze:** unified raw-native layout per source domain; single pull layer; one pull script per dim; pull the FULL cataloged surface; the **complete prefix census** (KEEP/ELIMINATE/RELOCATE/RETIRE/CONSOLIDATE/non-dim — no tree unclassified). The `_raw`/auth-state trees flagged non-dim KEEP.
- **SPEC-2 silver:** raw→parquet normalization (the conversion bronze no longer does); one converter dispatch; one partitioned layout `silver/{src}/{dim}/snapshot_date={date}/`; full-fidelity contract; retire duplicates/legacy; **gold-accustomed shape governs** every consolidation choice (confirm which copy gold reads before retiring others).
- **SPEC-3 gold:** the analytics layer (where domains join); two flows (**full** + **incremental**) — *incremental must rebuild the current-day volatile producers, never skip them* (the stale-partition lesson); partition-date fail-loud assert; single-writer per served key + shape gate; the **gold→portal feed** addendum.
- **SPEC-4 runtime/cleanup/auth/validation:** ONE runner + the full decommission inventory (no second producer survives); the grounded **auth/token-refresh** mechanism + robustness gaps (silent cookie/MFA-expiry = the dark-pipeline risk) + a robust **OTP/manual-credential fallback** (noted as the FINAL step); the **post-setup validation** gates.

Every spec: **machine-checkable ACs**, retro/migration enumerated, the parity-gate (refactored output == pre-refactor, several clean days), and the operator's locked decisions encoded verbatim.

## 5. PHASE 3 — Validate the specs before the PRD (verification cuts both ways)

- Independent ground-verify of the spec batch by the firm's DS (and CVO) before it seeds the PRD: confirm every claim source/live-true; fold corrections.
- **Verification cuts both ways** (Rule 22): concede on source/empirical grounding, never on authority. The Inflection run had the CVO concede an ungrounded "incremental" premise to DS's `eventbridge:164 mode=full`, and DS concede an ungrounded "positions_mv current-only" premise to the empirical 0%-unpriced history. Both moved on ground truth.
- Resolve `[DECISION]`s + the per-consumer edge checks (e.g. the yahoo-removal: confirm the custodian self-prices the full history before retiring a 3rd-party price thread).

## 6. PHASE 4 — Handoff to CTO → PRD

Hand the spec batch (audits + specs + seam evidence) to CTO with a cover note: the doc list, the locked decisions to encode verbatim, the open `[DECISION]` ratification points (CTO rules with grounding), and **the CVO standing gate as the PRD acceptance/exit criteria** (the ACs + no-tolerance value-parity + single-writer/single-runner sweep + full-fidelity + post-setup validation + live-vs-Terraform). CTO authors the PRD; COO decomposes into TOs.

## 7. PHASE 5 — Implementation + the standing CVO `/verify` gate

DS implements the data legs; **AE (e.g. 0.6.1) owns ALL resource create/delete/modify via Terraform** (no console, no ad-hoc; safe-apply; 0-diff; deploy-completion ledger; source-map; `comp-iam gaps`). On completion of **both** lanes, CVO runs `/verify`, 100%-alignment bar, three-axis:
- **Mechanical** incl. the **infra/Terraform axis grounded LIVE-vs-TF-state**: decommissioned resources actually gone (no orphan role/rule/lambda), creations/modifications actually TF-applied, `terraform plan` 0-diff, deploy-ledger closed. Tools: `comp-iam reconcile`, `comp-aws`/`comp-blast`, direct live-AWS.
- **Declarative** — implementation == spec ACs == PRD; every `[DECISION]` ruled; every census disposition honored.
- **Semantic** — full-fidelity (no field dropped), value-parity exact, and the **water-test**: served == custodian source to the cent sustained **several clean days**, the prevention alarm live.
- **Certify nothing until clean.** Any gap = a finding routed to the owning lane; deployed ≠ resolved (verify the landed artifact, not the apply).

**The prevention alarm (build it, don't skip it):** a freeze-monitor per served key — STRUCTURAL trio (size-collapse / as-of-lag / stopped-writer) + a **VALUE-PARITY** detection (served == an INDEPENDENT same-day custodian source to the cent). The value-parity **anchor** must be **upstream of and independent of the served-compute path** (NOT the value the served number is computed from — that's tautological and catches nothing). Pin the exact anchor per firm via the firm's DS (don't-guess); CVO ratifies (independent / clean-fresh-same-day / same-measure-to-the-cent).

## 8. PHASE 6 — Post-setup specs (after the full-recompute is durable)

- **Incremental-chain spec:** the incremental flow that rebuilds current-day volatile producers single-date (cheap), never skipping them; partition-date assert.
- **Full-vs-incremental scheduling-policy spec:** when each runs; the freshness-vs-cost tradeoff; the hard invariant that *whichever mode runs always produces a current-day, correctly-priced partition* (the defect must be structurally impossible under either mode).

---

## 9. Firm-variant adaptations (the platforms differ; the arc does not)

The template is custodian-agnostic. Plug the firm's specifics into the same phases; the differences concentrate in the SOURCE-OF-TRUTH model + the ingestion mechanism.

| | **Inflection (done)** | **Cottonwood** | **49 Financial** |
|---|---|---|---|
| Source(s) | Orion (Connect REST + Eclipse) | **Black Diamond exclusive** | **BD-SSOT + Schwab enrichment → transitioning to Schwab-SSOT + BD enrichment** |
| SSOT model | single-vendor | single-vendor (BD) | **MULTI-SOURCE + an in-flight SSOT MIGRATION** |
| Ingestion | REST/Envision + Eclipse REST | BD DataMining REST (session/scrape) | BD DataMining + Schwab CRS file-feed |
| Bucket | opal-data-inf | opal-data-cot | opal-data-bd |
| Pricing | custodian self-prices full history (snapshot) → 3rd-party removable | re-verify the BD snapshot's historical pricing completeness (same test) | re-verify per source |
| Known break class | stale-partition + dual-writer clobber (gold) | **as_of-PIN / completeness-guard** (BD pull returns $0-price rows → caps served at last-complete) | **MFA-dark feed + stopped-publish + the SSOT transition** |

**Cottonwood (BD-exclusive) — adaptations:**
- Single source domain (no two-domain false-friend like Orion/Eclipse), but **run the same `bronze/{src}-api/` structure** for future-proofing.
- The known issue is the **as_of-pin** (DATEMODE / completeness-guard caps served at the last fully-priced snapshot). Phase-0 must localize whether that's a real BD data-quality lag (accept-lag/SLA call) or a producer freeze — and Phase-3 settles the accept-lag policy with the operator (cot's data_as_of lag was characterized as a normal T+1/T+2 BD pricing lag, value advancing — a freshness/SLA question, not a clobber).
- Re-run the **historical-pricing-completeness test** on the BD snapshot before any 3rd-party-price simplification (the yahoo-removal pattern is firm-specific — confirm BD self-prices the full held history first).

**49 Financial (BD-SSOT + Schwab-enrichment → Schwab-SSOT + BD-enrichment) — the hardest; extra phases:**
- **MULTI-SOURCE reconciliation is first-class:** two custodian feeds (BD + Schwab) must be reconciled; the SSOT vs enrichment FENCE must be explicit (which fields are SSOT-authoritative vs enrichment — the 3-way-fence pattern: custodian-core / fenced-curated-metadata / surplus).
- **The SSOT MIGRATION is a phase of its own:** the in-flight transition (BD-SSOT→Schwab-SSOT, with BD becoming enrichment) means the spec must define the *target* SSOT state AND the cutover (parity-validated, never-widen, the canonical-schwab bootstrap). Treat the source-of-truth swap like the INFREF refactor but with a custodian-authority change underneath.
- **Watch the lots/cost-basis reconstruction** (BD lots-FIFO) — the value-parity anchor is harder here (the served value is reconstruction-derived, not a clean snapshot pass-through); expect a computation-alignment step, not a clean to-the-cent tie out of the box (the 49F value-parity anchor was the harder open case for exactly this reason).
- The feed-liveness fragility (BD MFA-dark, the Schwab CRS file-feed) feeds SPEC-4's auth/OTP-fallback section heavily.

---

## 10. The disciplines that ran through ALL of it (carry these verbatim)

1. **Ground vs deployed/live/served, never self-report.** Re-pull, re-sum, re-invoke yourself. Deployed ≠ resolved.
2. **Rule 22:** a mechanism/causal claim is INFERRED until source/graph-confirmed; reserved words (proof/root-cause/definitively) only on source-confirmed claims.
3. **No-tolerance value-parity** (to the cent) on every served value vs an independent custodian anchor.
4. **Single-writer per served key; single-runner per pipeline** — no second producer of any artifact.
5. **Complete prefix census** — every tree classified; nothing silently survives a decommission.
6. **Verification cuts both ways** — concede on ground truth, not authority; the verifier gets verified too.
7. **Per-consumer edge check before any deletion** (don't remove a thread until every consumer's need is confirmed met elsewhere).
8. **Decide each `[DECISION]` with the operator**, one fork at a time; encode verbatim; flag the rest for PRD ratification.
9. **AE owns all Terraform resource CRUD;** CVO verifies live-vs-TF (0-diff, no orphan, deploy-ledger).
10. **Certify nothing until 100% clean;** a could-not-verify is a finding, not a pass.

— 3.0.0_SA_CVO
