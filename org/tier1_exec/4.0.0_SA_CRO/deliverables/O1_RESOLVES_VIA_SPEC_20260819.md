# O1 — THE resolves_via PROTOTYPE: SPEC + PRE-REGISTRATION (commits BEFORE the first resolver run)

**Author:** 4.0.0_SA_CRO · **Date:** 2026-08-19 (evening window) · **Status:** SPEC — no resolver has run at this commit.
**Authority chain:** the Andrew-ordered adversarial exchange (record `ADVERSARIAL_EXCHANGE_CRO_CVO_FOUR_OPTIONS_20260819.md`, closed @1801d5b164) converged O1 rank 1 with an upgraded bar; execution commitment recorded ("Executing O1 (upgraded bar) tonight"). Predicate authority: Andrew R1 Q3 ("compilable not just conceptual or hand-drawn") + the confirmed read (b) "everything resolves = the ruled compile predicate" (@7241d0dfd7 record).
**What O1 measures — stated per the convergence:** RESOLVABILITY + CONSISTENCY between two pinned vintages, never world-truth. "Derived==declared over one substrate is a consistency property, and that is what the ruled predicate asks for."

## 1. The bar this run executes under (all six converged conditions, restated as controls)

1. **PRE-REGISTRATION (this document, this commit).** Every attempted term's DECLARED value is pinned
   below WITH its source and git vintage, committed before any resolver runs. Retro-pre-registration
   is discharged by the vintage pairs being PRINTED: every declaration lives at or before its pinned
   commit; every resolver run tonight postdates this spec's commit. The pins:
   - Declarations: `infra/system/ontology/SYSTEM_DEFINITIONS.yaml` @7241d0dfd7 (v3.4, 2026-08-19T16:24-04)
   - `org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml` @27f941ede5 (2026-08-19T11:23-04)
   - `org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml` @2f8c55f192 (2026-07-31)
   - `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/NFRA_MOTIF_P1_canonical_ab_catalog.py` @c7048f4846 (2026-07-18)
   - `org/modules/graph/estate-coverage-resolver.json` @97dc3e07b6 (2026-07-30, FROZEN — W-16)
   - Live graph: comp-kuzu at run time (provenance header quoted in results)
2. **DERIVATION INDEPENDENCE, per term.** The declaration leg and the derivation leg must differ in
   SOURCE. Where they cannot (Chain: the declared 138 comes FROM the artifact the resolver counts),
   the term is flagged `derivation_independent: false` and its agreement is VACUOUS — reported, and
   excluded from the agreeing count.
3. **DURABLE PER-TERM RESULTS BEFORE ANY EDIT.** The runner emits
   `O1_RESOLVES_VIA_RESULTS_20260819.jsonl` (one row per term: term, declared value+source+vintage,
   derived value+instrument+invocation, verdict, derivation_independent, run timestamp). That file
   COMMITS before any registry or resolver-rule edit is legal. A FAIL with no committed result row
   preceding its fix is undetectable chasing — this ordering is what makes the audit falsifiable.
4. **BOTH-LEGS CHASE-AUDIT.** Post-FAIL, an edit to EITHER leg — the DECLARED value (registry) or
   the DERIVING RULE (resolves_via) — on that term carries an evidence row in `O1_CHASE_AUDIT.md`
   (term, which leg, the FAIL row it follows, why the edited leg was the wrong one). "I fixed the
   resolver" is audited identically to "I fixed the declaration." An edit with no row is an
   exit-bar finding.
5. **THE STATED TERMINATOR.** Chase-audit rows are CVO-reviewable at the s4 exit bar. This spec
   states it so the terminator is a control, not an assumption about CVO's attention.
6. **THREE-NUMBER OUTPUT.** `attempted / writable / agreeing` — the middle number is the finding
   (terms for which no resolves_via can be stated are the coverage-universe defects a pass rate
   hides). No pooled percentage is reported (Substrate_Side binding_residue: denominators
   per-population, never pooled — here per-class).

## 2. Scope: attempted = 21 of the 26 A1a universes

**HELD (5, roster-race pre-concession):** C3, C3.i, C3.ii, Vertical, System — the C3 family's
membership is mid-flight (W-15, 28-vs-29, 0.8.0 Wave-1 lands 08-20). Roster-independent terms only
tonight; the held five re-run post-W-15.

## 3. Pre-registered declarations + deriving rules (the term table)

Class W-I = writable, independent derivation. W-D = writable, source-degenerate. L = legislated
single-home (membership hand-RULED via the naming-act register — LEGAL per the predicate's own
clause; nothing external to diff). NW = not writable tonight, reason named.

| # | Term | Class | DECLARED (pinned @7241d0dfd7 registry prose) | DERIVES VIA |
|---|---|---|---|---|
| 1 | Substrate | W-I | value set {aws, portal, codebase, ms} (v1.9 re-ruling, in-definition) | comp-kuzu: distinct node substrate-column values + counts, live graph |
| 2 | Estate | W-I | union of Substrate (degenerate whole) | inherits #1 |
| 3 | Subject | W-I | {client, market, estate} (v2.1) | canonical `c4_subject_function_grid.subject.values` |
| 4 | Function | W-I | {acquisition, analysis, serving, experience} (v3.1 build-collapse) | canonical `...function.values` |
| 5 | C4 (grid) | W-I | 3x4 = 12 cells | \|subject\| x \|function\| from #3/#4's derivation |
| 6 | Segment | W-I | {partner-data, market-intelligence, interactive-products, access-delivery, andrew-infrastructure} (v2.1 rename) | canonical — BOTH candidate blocks run: `c4_segments` keys AND `c4_subject_function_grid.segment_definitions` keys; an intra-file disagreement is itself a result |
| 7 | Domain | W-I | 9 values enumerated in-definition (object-data, compute-orchestration, pipeline, table-data, identity, api-serving, artifact-serving, observability, ui-dataflow) | ANCHOR_CATALOG distinct domain values (@c7048f4846) |
| 8 | Role | W-I | closed set of 14 (in-definition) | bank `roles` keys |
| 9 | Relation | W-I | closed set of 10 (in-definition) | bank `relations` keys |
| 10 | C2 | W-I | 12 canonical agnostic families (in-definition) | canonical `c2_motif_families` keys |
| 11 | Motif | W-I | same universe as C2 (unit term) | same resolver as #10 |
| 12 | Contract_Record | W-I | required [intent_source, obligation, lifecycle_class, revalidate_by, locality]; optional [successor, expiry_condition, cadence, vintage_probe] (in-definition) | bank `contract_record.required` / `.optional` lists |
| 13 | C0 | W-I | NO DECLARED COUNT (graph-derived by nature) | comp-kuzu node count → verdict UNDECLARED-b |
| 14 | C1 | W-I | NO DECLARED COUNT | comp-kuzu edge count → UNDECLARED-b |
| 15 | Estate_Contracts | W-I | NO DECLARED COUNT (store of D3 instances) | count subject records across `org/modules/graph/estate-contracts/*.contracts.yaml` → UNDECLARED-b |
| 16 | Chain | W-D | 138 (in-definition via A10; source = the frozen resolver artifact) | count chains in `estate-coverage-resolver.json` @97dc3e07b6 — SAME SOURCE as the declaration: `derivation_independent: false`, agreement VACUOUS; the honest resolves_via names the regen path, which is the W-16 defect |
| 17 | Deploy_State | L | {deployed, undeployed} — Andrew verbatim, naming acts v2.0 + v2.2 | the naming-act register (this registry's changelog) IS the deriving source; hand-RULED membership through a register is the predicate's stated legal form |
| 18 | D1 | NW | — | A9-COORDINATE: instance-universe counts are CORE's to declare; census cites, never re-derives CORE |
| 19 | D2 | NW | — | A9-COORDINATE (same) |
| 20 | D3 | NW | — | A9-COORDINATE (same) |
| 21 | Name_Variant | NW | — | DATA-GRAIN: the a07 alias-surface row count; scores at the instrument pass, not tonight |

**Expected three-number frame (pre-registered so the result cannot be quietly reframed):**
attempted 21 · writable 17 (15 W-I + 1 W-D + 1 L) · agreeing computed at run over the 12
member/count-comparable W-I terms (#1–#12; #13–#15 are UNDECLARED-b: writable, nothing declared to
agree with — they are findings of the UNDECLARED class, not passes or fails).

## 4. Runner + provenance

`o1_resolver_prototype.py` (this folder) — reads ONLY the pinned files + two comp-kuzu capture
files produced immediately before the run (invocations quoted in-results). Pure ASCII output,
utf-8 explicit. It writes the JSONL and a summary block; it edits NOTHING (the runner is
structurally incapable of chasing — edits are human acts that the chase-audit binds).

## 5. Seam notes

- **CTO (c)-pin:** sync message sent at this spec's commit (same turn). The registry
  `resolves_via` annex-field seeding that follows the results commit is PROTOTYPE-grade content;
  CTO's post-flip design note remains the arch frame for the permanent mechanism (checker
  run-mode), and annex fields are additive — reshaping under the design note is cheap and expected.
- **CVO:** the 63 prose-vs-authority comparisons trigger on O1's landing (their stated arm). The
  results file is the seam artifact.
