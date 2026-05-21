# VALGATE D-3 — Multi-Axis Envelope-Validation Sentinel Gate

**Project:** ADHC_VALGATE Phase 2 (Class-D render-fidelity suite) — TO `ADHC_VALGATE.005`
**Owner:** `0.4.0_DE_ClientPlatform~B`
**PRD:** `docs/architecture/ADHC_VALGATE.md` v0.1 — §4.D (D-3 spec), §3.2, §7 Q1.

D-3 generalizes the **shipped INFFIN.006 `AdvisorBookView` 6-axis threshold-2
sentinel** into a reusable, configuration-driven gate. The shipped instance
(`portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx`,
`warnOnInflectionAdvisorDrift`, lines ~93-118) hardcodes one entity, six axes,
a null-or-zero check, and a `console.warn` — inline in one React component.
D-3 lifts the core (the per-axis envelope check + the joint ≥N-axis fire rule)
into a gate driven by an `(entity type, metric vector, per-axis envelopes,
threshold)` config that applies to any entity-metric surface in a platinum
artifact, post chain-emit.

## §3.2 — Six-field gate anatomy

| Field | D-3 |
|---|---|
| **Trigger** | Post chain-emit — run against the freshly-emitted platinum artifacts (PRD §3.3). Standalone + config-driven; D-3 does **not** modify the gold chain (TO `<cross_domain_coordination>`). |
| **Input** | Each entity's metric vector inside a platinum artifact, per the surfaces declared in the config (`metric_path` within each artifact). |
| **Reference** | A per-axis plausibility envelope declared in the config — `nonzero`, `non_null`, and/or `min`/`max` (inclusive) / `min_exclusive`/`max_exclusive` bounds. |
| **Comparison** | Count the axes whose value falls outside its envelope; the entity fires when count ≥ the surface's `threshold` (default 2 — a single off-axis is often legitimate sparse-emit; two jointly is a signal). |
| **Verdict** | `PASS` no entity hit its threshold. `WARN` ≥1 entity hit its threshold. D-3 ships **WARN-not-BLOCK** in v1 (PRD §7 Q1). |
| **Action** | `WARN` → printed report + an optional JSON report file for a session log / post-chain step. D-3 never BLOCKs. Exit 0 = PASS, 1 = WARN, 3 = gate internal error. A post-chain caller treats exit 1 as WARN — log it, do not fail the chain. |

## Config

`d3-seed-config.json` — each `surfaces[]` entry:

| Field | Meaning |
|---|---|
| `name` / `entity_type` | Surface identity. |
| `artifact_filename` | The artifact filename to load when `--artifacts` is a directory tree (platinum layout: `.../advisors/<name>/book.json`). |
| `entity_id_path` | Dotted path to the entity identifier within the artifact. |
| `metric_path` | Dotted path to the metric-vector object. |
| `threshold` | Joint-implausibility fire threshold (default 2). |
| `axes[]` | `{key, envelope}` per axis. |

Config-driven by design — cover a new entity-metric surface by adding a
`surfaces[]` entry; no gate-code change.

## Seed coverage — AdvisorBookView (AC2)

The seed `advisor_book` surface reproduces the shipped sentinel exactly:
- the six axes of `warnOnInflectionAdvisorDrift` — `total_aua`,
  `fee_earning_aua`, `nna_ytd`, `client_count`, `account_count`,
  `implied_annual_revenue`;
- a `{"nonzero": true}` envelope on every axis — implausible iff `value`
  is `null` or `0`, reproducing the TS `v == null || v === 0` check;
- `threshold: 2`.

So the existing AdvisorBookView coverage is preserved **through** the
generalized gate — no coverage lost in the lift. The TS sentinel remains in
place as a client-side defensive `console.warn`; D-3 adds the same check as a
post-chain-emit gate over the platinum artifact.

## Files

| File | Role |
|---|---|
| `.tools/valgate/d3_multi_axis_envelope_gate.py` | The gate — config-driven multi-axis envelope evaluation. |
| `.tools/valgate/d3-seed-config.json` | Seed config — the `advisor_book` surface. |
| `.tools/valgate/d3_gate_test.py` | Verification harness — envelope logic, threshold logic, end-to-end, AC2 coverage. |
| `.tools/valgate/VALGATE_D3.md` | This document. |

## Verification

`python .tools/valgate/d3_gate_test.py` — 24/24 cases:
- Envelope logic: `nonzero` (0/null fire, positive OK), `min`/`max` range,
  `non_null`, empty envelope (never fires).
- Threshold logic: 0/1 implausible axes → PASS (threshold-2 holds for a single
  off-axis); ≥2 → WARN; threshold is configurable (threshold 1 fires on 1).
- End-to-end: synthetic platinum `book.json` artifacts with the seed config —
  an advisor with ≥2 jointly-implausible axes WARNs; a one-off advisor and a
  healthy advisor do not; all-healthy → exit 0 / PASS.
- AC2: the seed config's axes/threshold/envelope match the shipped 6-axis set.

Real-data smoke: run against the live `inflection_wealth_management` and
`peter_lee` platinum `book.json` artifacts → PASS (no false positive).
