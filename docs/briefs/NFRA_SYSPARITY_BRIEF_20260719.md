# NFRA_SYSPARITY — Brief: does `infra/system/` + `sdk/` represent Opal's reality?

**To:** 1.0.0_SA_CTO (for PRD + arch-gate + decomposition) · **From:** 0.0.0_AB_MSTR · **Date:** 2026-07-19
**Charter:** LD-0318 · **Companion Part 2:** NFRA_ONTOCLARITY (scoped in §8) · **Status:** brief issued, PRD pending CTO

---

## 0. Origin (Andrew-direct, 2026-07-19, verbatim intent)

> "is `/system`, and the underlying `/sdk` folder, completely representative of how the engineering,
> ontology, comp tools, infrastructure, etc actually work in reality? ... do a comprehensive analysis to
> that end first to establish how close these folders represent the reality of the system so as to attempt
> to reach parity. write a brief on that and issue to CTO for an NFRA_SYSPARITY project."

Plus a **Part 2** (a separate audit): *"establishing that there is no semantic fogginess in ontology, that
there are clear rules on layering, nesting, definitions, processes, etc. and ... that they are correctly
logged and referenced in the system and sdk folders."*

## 1. Method (grounded, not recollected)

Four independent analysts, one per named domain, each comparing the **representation** (`infra/system/` +
`infra/system/sdk/`) against the **live reality** (the real comp-tools, ontology artifacts, terraform,
pipelines). Read-only; every claim cited `file:line` / command output; counts grounded on
`comp-manifest-check` / `comp-system`, never on a doc or memory. MSTR independently re-verified the four
load-bearing findings against live state (§3 footnote).

## 2. Headline

**The architecture representation is high-fidelity and unusually self-aware. What has lapsed is the
LIVE-CADENCE: parity is held by *care* — hand-passes and on-demand sweeps — rather than by a fail-closed
*control*.** This is the CHECK-LIVE-NOT-FROZEN doctrine (LD-0314) and CONTROLS-OVER-CARE playing out on the
system's own self-description. The gap is **not uniform** — it is concentrated in (a) the ontology layer
and (b) the live-refresh artifacts, while the infra and comp-tools representations are ~80-85% faithful and
honest about their own maturity.

A single parity number is misleading (the domains and their failure modes differ), so the brief reports
per-domain with the caveat baked in. Composite, weighted, within the tree's *declared* scope: **~70%**.

## 3. Per-domain parity

| Domain | Parity | Character of the gap |
|---|---|---|
| **Comp-tools** | ~85% | Catalog/families/maturity/decommission/FEDOBS ~90-95% faithful + honestly scoped (marks prototypes/HELD/retired correctly). Two real gaps: `03_comp_tools.md` **names the rail without describing its enforcement** (the COMPRAIL DENY-gate / `# rail-checked` marker / HUD / audit / `/freeform` — CLAUDE.md Rule 21 — all absent from the text); and the SDK's "genesis reuses comp-tools tenant-neutral" claim is **overstated** — 11+ tools hardcode `opal-313476888478`/`opal-data-*`; only comp-genesis + comp-which parameterize; porting the 61 query CLIs to a tenant graph is UNBUILT. Count lag 59/80 -> live 61/82 (self-aware, auto-regenerable). |
| **Infrastructure** | ~80% | Within the graph-platform scope it claims, the SDK terraform is a genuine, **FRESH** (built 07-18) parameterization of the real `globgrph/*.tf` (version pins in sync). Reality has *not* evolved past it. The risk is that it is **UNEXERCISED**: the SDK's only acceptance is local loop-closure — **no tenant has ever been `terraform apply`'d to AWS** (Rule 22a: DESIRED, not EXERCISED). Fidelity gaps: intraday Lambda IAM omits a describe-grant (would AccessDeny on first real event), producer plane is 3/6 with a scheduler-mechanism divergence, and several toggle vars are declared-but-never-wired. |
| **Engineering / learning-loops / current-state** | ~70-75% | Architecture docs (00/05/07) faithful + self-critical (07_maturity ships its own 13-row gap table). But **`06_current_state` is measurably stale** — 250 commits behind, and the system's own `comp-system --check` returns **SYSTEM STALE** right now (ledger 80->82, tools 59->61). And the NESTEDABSTRACT loop *detects* drift soundly but has *incorporated* only 1 of 5 logged abstractions into the SDK — **4/5 pending**. 11 of 16 knowledge-classes in 06 have no live producer (UNKNOWN-VINTAGE). |
| **Ontology** | **~40%** | The 14 Roles / 10 Relations / 6 Variance verdicts (ratified LD-0311) appear **0 times** in the 8 core system docs; the SDK carries a self-labeled **v0.1 stub** pinned `adapter-pattern-only` (honestly logged as P6 work). Two GENUINE silent drifts (not honest gaps): `06_current_state.json` reports `cse_schema @0.4` while **live is 0.5** (the OWNS/Custodian bump); and the drift-gate that watches the ontology is **blind to the ratified vocabulary** — its surface-map watches `canon-patterns.yaml` but not `NFRA_ONTOLOGY_RULE_BANK.yaml` or `variance_dimensions.yaml`. |

> **MSTR live-verification footnote (2026-07-19):** independently confirmed the four load-bearing findings
> against live state, not the analysts' reports: (1) `comp-system --check` = SYSTEM STALE (ledger 80->82,
> tools 59->61); (2) `06_current_state.json:81,83,85` = `cse_schema @0.4` vs `cse_schema.py:42
> SCHEMA_VERSION="0.5"`; (3) `surface_map.json:77-79` watches canon-patterns + AB_MATERIALIZE_SPEC, NOT
> RULE_BANK.yaml/variance_dimensions.yaml; (4) `grep -il 'NFRA_ONTOLOGY|archetype|custodian'
> infra/system/*.md` = 0 files.

## 4. Three structural findings (the real thesis — these outrank the per-domain numbers)

### 4a. Scope is *declared* but *incomplete* — the first deliverable is a scope contract.
`infra/system/README.md:25-28` faithfully declares the tree covers the compiler/graph plane and **excludes**
the client-data pipeline estate (INF/49F/COT/TAXSMA/OPAL_ASSETS — ~54 TF modules / 26 EC2 / 95 lambdas) and
the taxonomy/consolidation plane. That boundary is sound and should hold. **But two omissions are
UN-declared:** (i) the ontology is absent from the core docs with no boundary sentence saying whether that
is scoping or oversight; (ii) the "tenant-neutral comp-tools" claim over-reaches its real scope. A parity
metric is meaningless until the tree states *explicitly* what it commits to representing. **Naive parity
would falsely score the ~90% of Opal infra that is out-of-scope-by-design as "missing" — do not let it.**

### 4b. Parity is held by CARE, not a CONTROL — the live-cadence has lapsed.
The maintenance model is: static docs hand-refreshed "between passes" (last pass 07-17/18, ~2 days + a full
NFRA sprint ago); `06` regenerated by `comp-system` on-demand ("run comp-system, that's the whole
procedure" — nobody ran it, so it is 250 commits stale); incorporation driven by an on-demand COO sweep. **None
of these is a fail-closed gate.** And the one gate that exists — the NESTEDABSTRACT drift-gate — is itself
**under-inclusive** (blind to RULE_BANK.yaml), the *exact* self-referential hole MSTR banked in LD-0314's
amendment this session (a control's own denominator is live state). So the deficit is concentrated in the
*maintenance discipline*, not the architecture. **The fix is not "rewrite the docs" — it is "convert
parity-maintenance from care into a control."**

### 4c. The gap is uneven + the SDK is faithful-but-unproven.
Infra/comp-tools ~80-85% (fresh, honest); ontology ~40% (barely represented). The SDK is a high-fidelity
*snapshot-era* kit that (i) has never been cloud-applied and (ii) ships the pre-ratification v0.1 vocabulary
with 4/5 abstractions un-incorporated. So "reach parity" means different work per domain — not one sweep.

## 5. Scope ruling needed (MSTR recommendation — CTO/Andrew to confirm)

1. **Hold the declared boundary on the pipeline estate + taxonomy plane** — they have their own homes;
   re-representing them in `/system` would duplicate and immediately drift. (Confirm, don't widen.)
2. **Rule the ontology IN scope for `/system` + the SDK.** Unlike the pipeline estate, the ontology is not a
   sibling data-estate — it is the C3 *language the whole compiler plane reasons in*, the semantic core.
   Its ~40% parity is therefore a real gap to CLOSE, not a boundary to declare. (This is the single most
   consequential scope call in the brief.)
3. **Make the boundary EXPLICIT + auditable** — every exclusion gets a one-line "sibling knowledge class +
   pointer" in the README, so a reader can never confuse scoping from oversight.

## 6. Recommended workstream shape (for CTO's PRD to refine — not authored TOs)

- **WS-1 — Scope contract (do first).** Ratify §5; write the explicit scope+boundary statement; define the
  parity *metric* (denominator = declared scope, exclusions named) so future measurement is honest.
- **WS-2 — De-stale + GATE `06`.** Run `comp-system` to clear the SYSTEM STALE state (0.4->0.5, 59/80->61/82);
  then wire `comp-system --check` into a fail-closed cadence/CI gate or HEAD-advance auto-regen so `06`
  cannot silently rot again. (4b, the highest-value structural fix.)
- **WS-3 — Complete the drift-gate denominator.** Add RULE_BANK.yaml + variance_dimensions.yaml (and audit
  the *whole* surface-map for other under-coverage) so the anti-drift control watches what it exists to
  watch. Closes the LD-0314 self-referential hole at its live instance.
- **WS-4 — Represent the ontology.** Bring the 14/10/6 archetype layer into `/system` (a core doc or a
  declared cross-reference) + fold the ratified vocab into the SDK adapter (retire the v0.1 stub / wire
  `binding_mode: vocabulary-bound`). Note: the SDK-incorporation half overlaps NESTEDABSTRACT (§7).
- **WS-5 — Exercise the SDK at the cloud tier (or declare local-only sufficient).** The terraform is faithful
  by construction and unproven; either a one-tenant `terraform apply` smoke (Rule 22a) or an explicit ruling
  that local loop-closure is the accepted acceptance bar — but the choice must be *stated*, not defaulted.
- **WS-6 — Incorporation-debt SLA.** 4/5 NA rows pending; the drift-gate's "age alone is not drift" means
  nothing pressures closure. Track pending-age -> an incorporation SLA (this is NESTEDABSTRACT's to burn
  down; SYSPARITY sets the SLA).
- **WS-7 — Describe the rail + fix the small honest lags.** Add the COMPRAIL enforcement subsection to
  `03_comp_tools.md`; correct the tenant-neutral-comp-tools overstatement; fix the SDK front-end docstring
  (3->4); reconcile the tool-count across CLAUDE.md/docs/memory on the live gate.
- **WS-8 — Resource-manifest cross-walk (optional, high-value).** A machine cross-walk (system doc <-> real
  `globgrph/*.tf` <-> SDK module) so infra parity is auditable against live state, not prose — an extension
  of the `06` auto-gen model to the static sections.

## 7. Relationship to existing projects (no duplication)

- **NFRA_SYSTEM** (complete) built `infra/system/`. **NFRA_GENESIS** (active) is the SDK. **NFRA_NESTEDABSTRACT**
  (active) is the loop that keeps the SDK current with the evolving mechanism.
- **SYSPARITY is NOT NESTEDABSTRACT.** NESTEDABSTRACT is forward/ongoing (fold each new enhancement's
  abstraction into the SDK). SYSPARITY is the **baseline audit** (measure + close the *accumulated* gap) **+
  the make-parity-a-control project** (WS-2/WS-3: gate the refresh, complete the denominator) **+** the check
  on whether the maintenance controls are even *sufficient* to hold parity going forward. The
  ontology-incorporation debt (4/5 NA rows) is NESTEDABSTRACT's to burn down; SYSPARITY sets the SLA and
  verifies closure.

## 8. Part 2 — NFRA_ONTOCLARITY (ontology semantic-clarity audit; sibling, sequence after WS-1)

A **separate** project per Andrew: establish that the ontology has no semantic fogginess — clear rules on
LAYERING / NESTING / DEFINITIONS / PROCESSES — and that they are then correctly logged + referenced in
`/system` + `/sdk`. The ontology analyst surfaced **10 concrete fog spots** as its seed; the load-bearing ones:
1. **"Ontology" is one word for two layers** (the CSE C0-C3 algebra vs the 14/10/6 archetype layer *above*
   it), never disambiguated in one place — the root fog.
2. **"Layer/plane" carries five incompatible numbering schemes** (C0-C3 / the `layer` field / `semctl` / the
   GLOBGRPH L1-L7 / the recognizer A-B-C-D planes->Territories) with no crosswalk.
3. The ratified vocabulary physically lives in 5 split files + a version-fogged pin
   (`v0.1-canon-patterns` names a file that *defers* to the thing being versioned).
4. The Relation-vs-Role composite (3 dual-axis edges) is a stated "load-bearing subtlety" nothing enforces.
5. Polymorphic-type Role resolution has no tie-breaker (a Lambda that guards AND transforms — undefined).
6. **DoR vs rule-bank disagree on whether Observer is settled** (CLOSED_SET "Open for CTO" vs RULE_BANK "CTO
   GRANTED") — internal record drift.
7-10. `variance_dimensions` name invites misreading; "Fork-Shadow = debt" retirement copies may linger; the
   3 incorporation modes are fog-prone; C2->C3 emergence ownership overlaps NFRA_SYSTEM<->NFRA_ONTOLOGY.

**Sequence:** ONTOCLARITY should run AFTER SYSPARITY's WS-1 scope contract (so it audits a defined ontology
scope) and feeds WS-4 (its clarified definitions are what get logged/referenced). It is the *definitions*
audit; SYSPARITY is the *representation-parity* audit — distinct, complementary.

## 9. Doctrine connection (why this is not a one-off audit)

NFRA_SYSPARITY is the operationalization of **CHECK-LIVE-NOT-FROZEN (LD-0314)** + **CONTROLS-OVER-CARE** +
**Rule 22a (exercise, don't assume)** applied to the system's *self-representation*. The strongest evidence:
four independent analysts + MSTR live-verification **re-derived the exact LD-0314 self-referential finding**
(the drift-gate's under-inclusive denominator) from the opposite direction, ~1 hour after it was banked.
The system's map of itself is subject to the same frozen-vs-live law as everything the map describes — and
the fix is the same: ground APPLIED not DESIRED, print the denominator, put the control on the retrieval.

## 10. Verification regime (Andrew-direct standing rule — 3.0.0_SA_CVO)

**Every finding in this brief is an ASSUMPTION until CVO independently re-grounds it.** Because the project's
whole subject is *whether representation matches reality*, the audit's own findings must themselves be
exercised, never trusted (Rule 22a; the self-referential CHECK-LIVE-NOT-FROZEN lesson — an audit that trusts
its own report re-certifies the exact frozen-not-live class it exists to catch). Standing regime (LD-0318):

- **CVO spot-checks all assumptions BY DOMAIN** — comp-tools / infrastructure / engineering+loops / ontology
  — **as the work is done**, continuously, not a one-time sign-off.
- **Per-item basis:** `/molecule` (atomic deep-dive on the exact unit — the file/value/artifact/live state
  an assumption rests on) + `/verify` (3-axis mechanical/declarative/semantic correctness) + `/prd-delta`
  (project completeness vs the CTO PRD as workstreams land).
- **CVO arms an ongoing 30-min `/loop` in its own session** that nudges it to verify MORE items each fire —
  a burn-down of the per-domain assumption list, re-armed each CVO session while the project is active.
- **A workstream is not `done` until its domain's assumptions are CVO-verified on this basis** — in addition
  to the normal per-deliverable RAVC + CTO arch-gate, not a replacement.

The per-domain parity numbers and the §3 verdicts are the **initial assumption list** CVO burns down (they
were produced by 4 analysts + one round of MSTR live-verification — a strong start, but exactly the kind of
report this project's own doctrine says must be exercised, not banked).

---

**Ask of CTO:** author the NFRA_SYSPARITY PRD from this brief (arch-gate WS-2/WS-3 as the load-bearing
control work; rule the §5 scope calls with Andrew where sovereign); confirm NFRA_ONTOCLARITY as the
sequenced Part-2 sibling; and structure the PRD's acceptance so each workstream carries the §10 CVO-verified
gate. MSTR holds the charter (LD-0318) + governance; COO decomposes to TOs on your PRD; CVO runs the §10
standing verification loop.
