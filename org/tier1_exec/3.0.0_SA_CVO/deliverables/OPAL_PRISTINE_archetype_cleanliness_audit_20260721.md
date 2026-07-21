# OPAL PRISTINE — archetype + cleanliness audit (CVO)

**Author:** 3.0.0_SA_CVO · **Date:** 2026-07-21 · **For:** Andrew (direct request)
**Method:** two grounded estate surveys — (A) archetype/taxonomy posture, (B) comp-tool debt census (comp-dups, comp-clobber, comp-drift, comp-similar, comp-debris). All findings record-cited; read-only.
**Thesis:** cleanliness is a CONTROL, not a cleanup. An archetype is only real when it climbs the ladder **PROSE -> TEMPLATE -> GATE -> DETECTOR**. We have built the DETECTOR rung; the leverage is the middle two.

---

## 0. THE VERDICT (one paragraph)

**Opal is cleaner than it feels, and the machinery to lock it in is ~80% built.** The debt is SMALL and CONCENTRATED, not sprawling: comp-dups filtered 677 benign pairs down to **15 real TF-label collisions**; comp-clobber found **2-3 real clobbers**; the "dead" tail is a recognizable graveyard (news/scraper cruft) plus one supersede cluster (the `yang-generate-*` family). mdpf/portal are near-clean. The gap is **not detection** — we have that. It is three things: **(1)** the one missing archetype — a generator for a new Opal data pipeline / partner firm (today it is "clone the closest exemplar," which is *where new debt is born*); **(2)** flipping the taxonomy gates that are already BUILT but left WARN-first; **(3)** a standing burn-down loop on 4 named concentrations. Do those and the estate becomes **archetypal-by-construction** with a single debt score that trends to zero and stays.

---

## 1. ARCHETYPE MATURITY MAP (the 3 classes x the ladder)

| Class | Archetype | Rung today | Evidence |
|---|---|---|---|
| **PROCESS** | comp-tool registration (atomic bundle + 5-member completeness gate) | **GATE** (most mature in the estate) | `comp-manifest-check`; `COMPTOOL_REGISTRATION_FLOW.md` |
| **PROCESS** | deploy flow (TF-only, safe-apply/safe-commit/safe-deploy) | **GATE** | never-rules-gate.sh; Rules 1-6,14 |
| **PROCESS** | firm separation bd/cot/inf | **GATE** (commit + IAM Deny) | safe-deploy PIPELINE_MAP |
| **PROCESS** | partner-firm onboarding (4 planes) | **PROSE checklist** ("clone 49financial/inflection") | PARTNER_FIRM_ORGANIZATION_STANDARD.md |
| **RESOURCE** | new-COMPANY semantic system | **TEMPLATE (generator exists)** | `infra/system/sdk/` genesis (`company.yaml` -> tenant TF) |
| **RESOURCE** | new Opal DATA PIPELINE / feed | **NONE — ad-hoc** | no generator; the #1 gap |
| **RESOURCE** | opal-data-assets key grammar `{source}/{scope}/{layer}/{type}/{date}` | **PARTIAL GATE** (only bronze-parquet deny, 1 bucket) | 17a policy @d89cc4fc9; off-grammar keys (`code/`,`_probe/`x22,`_ops/`) still land |
| **RESOURCE** | IAM `{resource}-role`, scope-exact, PAB-on | **PROSE** (no lint) | TAXONOMY_STANDARD §E |
| **TAXONOMY** | medallion bronze/silver/gold discipline | **PARTIAL GATE** | 17a bucket-policy (partial); commit-gate silver-ids |
| **TAXONOMY** | `fact_*` silver / `dim_*` gold | **PROSE** (zero lint) | TAXONOMY_STANDARD §A |
| **TAXONOMY** | scheduler grammar `{unit}-{function}-{cadence}` | **GATE built, WARN-first (un-flipped)** | trigger-census.py `--enforce-grammar` |
| **TAXONOMY** | OS baseline AL2023 + region co-location | **GATE built, WARN-first** | manifest-lint.py check_os_baseline |
| **TAXONOMY** | absence-twin per scheduled producer | **PROSE + PAUSED** (alert-suspension) | DC-12; Door-6 emitter measured untwinned |

**Read:** PROCESS is the model (fully gated). RESOURCE and TAXONOMY are where the estate is still prose-or-WARN — and RESOURCE has the single worst gap (no pipeline/firm generator).

---

## 2. THE DEBT PICTURE (grounded — small + concentrated)

| Debt class | Magnitude | Where it concentrates |
|---|---|---|
| **Duplication / double-management** | 15 real TF-label collisions (of 677 filtered) + 1 content dup | **bd pipeline dual-rooted** (`bd_exporter` role/policy/SG/instance-profile + `opal_data_bd` lifecycle in TWO TF roots) · **schwab->consolidation** transitional IAM overlap (migration, expected) |
| **Output-key clobber** | 2-3 live (of 818+ keys) | `aum-timeseries.json` (the deprecated frozen emitter, this session) · `macro_data.json` · `gold/trigger-pending.json` (cross-pipeline candidate — confirm firm-separated) |
| **Functional-overlap / supersede** | 1 clear cluster (of a 15-member twin pool) | **`yang-generate-*` ETF/deck family** — positioning/etf-returns/macro/macro-timeseries twin `allocation-summary`; holdings-attribution + peer-performance cold 21d; cma+volatility stillborn |
| **Resource coldness / dead** | 9 cold + 39 stillborn lambdas; 24 cold + 16 stillborn s3/ddb/ec2/events | **news/scraper graveyard** (seeking-alpha-*, semantic-news-*, keyword-drilldown) · **4 idle-not-stopped EC2** (direct cost) · cold event rules (exec-summary-trigger 79d, smartx-daily-export 51d) |
| **Structural abandonment (comp-drift)** | INCONCLUSIVE this pass | needs `comp-drift --deep` (11/14 seams cost-guarded) |

**Concentration map:** **bd/49f** = most debt (partly the KNOWN allocations deprecation, not fresh rot) · **yang/ETF-deck** = the supersede epicenter · **schwab->consolidation** = transitional migration dup (self-cleans as OPAL_CONSOLIDATION lands) · **news/semantic** = stillborn graveyard · **mdpf/portal** = near-clean. Type: IAM (TF collisions), Lambda (yang + stillborn), EC2 (idle), then S3/DDB coldness.

**Two cautions the census itself flagged:** (a) "cold S3" is only the WRITE half — a read-access check must precede any reap (`comp-whoread`); (b) STILLBORN mixes genuine cruft with LIVE auth/user guards (`opal-users`, `opal-firms`, `auth-validator-edge`) — never reap those. Verify-before-delete is doctrine, not optional.

---

## 3. THE PROGRAM — the two forms, made concrete

### FORM 1 — prospective lock-in (stop new debt being born)

1. **Build the missing RESOURCE archetype: a new-pipeline / new-firm GENERATOR.** This is the highest-leverage move — the highest-frequency creation act (a new firm/feed) is "clone the closest exemplar," and that clone is *exactly* where the transitional dups + off-grammar keys come from. genesis proves it is buildable; generalize its `company.yaml -> template` pattern from "new company semantic system" to "new Opal data pipeline" (bronze->silver fact_*->gold dim_* + IAM + scheduler + platinum, parameterized by firm/vendor). OPAL_CONSOLIDATION's A/B/C/D casebook (WS-C:C7) is the content of this template.
2. **Flip the WARN-first gates to hard (announce->enforce).** scheduler-grammar (`--enforce-grammar`) and OS/region baseline lints are BUILT and grandfather-pinned — they just need the CI flip. ~90% done; the cheapest wins on the board. CTO's call per the ramp.
3. **Gate the PROSE taxonomy the estate has no lint for:** the S3 key grammar as a whole (CLASS-D producer-code check, per OPAL_TAXONOMY's own design), `fact_*`/`dim_*` naming, IAM `{resource}-role` naming. Each is a small lint riding an existing hook (commit-gate / safe-deploy) — "gate what you measured."
4. **Un-pause the absence-twin gate when the alert-suspension lifts** — the Door-6 emitter blind spot (silent stop -> mdpf never fires, nothing pages) is the ledger's highest-consequence open item.

### FORM 2 — retrospective burn-down (eliminate what exists)

The debt is already CATALOGUED + TRIAGED (survey B). The missing piece is a **standing burn-down loop** — the comp-tools emit a ranked worklist; a cadence (or a scoped `/drive`) works it down with verify-before-delete; the debt trends to zero AND stays there because Form-1 gates prevent re-accretion. Prioritized targets:

- **NOW (high-confidence, unambiguous):** reconcile the **bd TF double-management** (one owner for `bd_exporter` + the `opal_data_bd` lifecycle); confirm `gold/trigger-pending.json` is firm-separated (`comp-clobber --live`); stop the **4 idle EC2** (cost, purpose-review); disable the cold-past-cadence triggers (exec-summary 79d, smartx-daily-export 51d) after an owner nod.
- **OWNER-TRIAGE (abandoned == rare-guard until confirmed):** the **yang-generate-* supersede cluster** (ETF/deck owner confirms `allocation-summary` replaced them); the **stillborn graveyard** (reap news/scraper cruft; NEVER the auth/user guards); cold S3 (read-check first).
- **SELF-CLEANING (leave to the migration):** the schwab->consolidation IAM/TF overlap dissolves as OPAL_CONSOLIDATION lands its parity streak + retires the legacy path. Don't hand-clean transitional dup.

### The DETECTORS themselves have debt (fix the instruments so the burn-down is trustworthy)
- **comp-drift** produced no abandonment list (11/14 seams cost-guarded) -> needs a `--deep` mode wired for the resource census.
- **comp-similar** can't grade supersede verdicts here (heat-join yields 0 banded — an ARN/name key gap) -> fix the join or it stays "candidates, never verdicts."
- **comp-kuzu latency** (comp-similar's first run timed out on a cold graph) -> the graph-query path is its own reliability debt.

### The ACCOUNTABILITY layer — ONE debt score
Every comp-tool already prints a denominator. Roll them into a single **estate-debt score** (TF-collisions + live-clobbers + supersede-cluster count + cold/dead + drift-edges), snapshotted (comp-axes already does per-axis time-series) and trended. That number going DOWN and STAYING down is how you *know* it works, versus hoping. It also makes the Form-1 gates auditable: after each gate flips, the corresponding debt-class should flatline (no new accretion).

---

## 4. HOW TO EFFECT IT

**Fold this into OPAL_TAXONOMY** — it is already the exact vehicle (census -> per-DC CTO ruling -> lints-on-existing-hooks -> gate-what-you-measured -> renames-ride-natural-touches, 16 DCs catalogued). Add four deliverables to it (or a sibling program, "OPAL_PRISTINE"):
1. **Template library** — the new-pipeline/new-firm generator (Form-1 move 1); the biggest single lever.
2. **Conformance gates** — flip the WARN-first lints + build the 3 prose-taxonomy lints (Form-1 moves 2-3).
3. **Burn-down loop** — a standing comp-tool worklist + verify-before-delete cadence on the 4 concentrations (Form-2).
4. **Debt score** — one number, trended (accountability).

Plus a meta-item: **sharpen the detectors** (comp-drift --deep, comp-similar heat-join, comp-kuzu latency) so the burn-down is grounded, not guessed.

**CVO role:** I own the VERIFY leg — each gate flip gets an independent "does a violation actually get blocked" exercise (the way I verified comp-clobber's gate + the -F finding); each debt reap gets a verify-before-delete read; the debt score gets an independent recompute. I verify, I don't build.

---

## 5. SEQUENCING (what first)

1. **Flip the two built WARN-first gates** (scheduler-grammar, OS/region) — cheapest, already 90% done, stops two debt classes cold. (CTO, ~days)
2. **Reap the unambiguous Form-2 wins** — 4 idle EC2 + the cold-past-cadence triggers + confirm trigger-pending. Quick, visible, cost-positive.
3. **Scope the pipeline/firm generator** (Form-1 move 1) — the big lever; design it against the OPAL_CONSOLIDATION A/B/C/D casebook while that casebook is fresh.
4. **Stand up the debt score** — so 1-3 are measurable from day one.
5. **The prose-taxonomy lints + the owner-triage reaps** — steady-state, ride natural touches.
6. **Un-pause absence-twins** when the alert-suspension lifts.

**Net:** the estate is tractable-clean today; this program makes it *stay* clean by construction. The detectors are the proof it's real; the generator + the gate-flips are what turn "we clean it once" into "it can't get dirty."
