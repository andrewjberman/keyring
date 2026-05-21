# Session Log — ADVI_DEMOV1.002 Transform Engine

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-21
**Task Order:** ADVI_DEMOV1.002 (issued by 2.0.0_SA_COO~C; org lane CTO base <- COO~C <- DS~C)
**Status:** COMPLETE — engine built, reviewed, dry-run CLEAN. RAVC2 to COO~C.

## Current State

Phase 2 of ADVI_DEMOV1 complete. Built the deterministic, seeded, two-pass
demo-dataset transform engine that clones `s3://opal-data-bd/platinum/**` (the
49 Financial dataset) into a fully fake `opal-data-demo` tree. The TO builds +
dry-runs the engine; the live populate run is TO-4.

Engine: `data/demo/scripts/transform/` — `demo_transform.py` (the engine),
`fake_identities.py` (the deterministic faker), `README.md`.

### Final dry-run — CLEAN

```
mapping built: 168 advisors, 2962 clients, 6693 accounts (9448 z-ids swept)
sample files transformed : 63   (all 14 firm files + 16 each advisor/client/account)
unmapped ids encountered : 0
leak self-check          : 0 surviving real identities (CLEAN)
```

`--value-mode scalar` smoke: clean. `--selftest`: PASS. `--apply`: correctly
refused (TO-4 gate). ds-commit-gate: exit 0.

### Design — how the four TO requirements are met

- **R1 two-pass / hard-error.** Pass 1 builds the COMPLETE id map before Pass 2;
  an unmapped z-id in Pass 2 raises `HardError` (non-zero exit). Pass 1 is a full
  z-id sweep of every non-account `.json` object — no id source is assumed.
- **R2 reuse ANONYM field map / replace hash with faker.** The engine is a fresh
  standalone module (pseudonymizer.py NOT modified). Output is realistic fake
  names from a seeded curated generator — not `Client a3f9..` hashes.
- **JSON-path-context-awareness (Phase-0 delta).** Solved by **value membership**:
  a string is replaced iff it IS a known real identity. A ticker (`QQQ`) is
  structurally never in the identity map, so it is never touched — regardless of
  field. Composite `"Name (zid)"` strings get zid-anchored repair; the substring
  scan triggers on any spaced/suffixed string (catches `"Name_inflow"` column
  keys); object KEYS and bare LIST-STRINGS get the same treatment as values.
- **R4 mapping = secret.** Never written to the demo bucket / git / logs; only to
  an explicit `--save-mapping` local path with a warning. Reports carry counts.
- **R6 EC2 one-shot.** Standalone script, S3-artifact model, no third-party dep.
- **R7 no jitter.** `--value-mode` switch: verbatim (default, numbers untouched)
  | scalar (one global constant on monetary fields). No per-value jitter.

### Dry-run hardening — bugs caught by the engine's own contracts

Each dry-run against the real bucket surfaced one concrete defect; the
hard-error + leak-check contracts caught every one (leaks 206 -> 11 -> 0):

| # | Caught | Fix |
|---|--------|-----|
| 1-2 | ownership_map / clients/0 reference ids beyond the folder set | Pass 1 -> full z-id sweep of every file |
| 3 | leak-check false-positives (z-ids substring-nest) | whole-token id match |
| 4 | composite object keys `"Name (zid)"` not rewritten | keys run through the composite-aware path |
| 5 | engine flagged its own injected fake z-id | hard-error checks SOURCE ids only |
| 6 | advisor-name column keys `"Name_inflow"` survived | substring scan triggers on any spaced/suffixed string |
| 7 | `_walk_alias_pairs` misclassified 1,175 geo/category labels as advisors | advisor aliases filtered to real advisor folders (geography stays real) |

## PII-inventory reconciliation (TO requirement 7 — vs TO-0 brief §3)

Every PII class the Phase-0 brief enumerated is handled, verified on the 63-file
dry-run sample (which includes the high-PII firm files — partner_analytics_*,
cumulative_chart, leaderboard, ownership_map):

| TO-0 PII class | Engine mechanism | Verified |
|---|---|---|
| firm_id / firm_name | exact-match value + key | clean |
| advisor slug / name (S3 keys + content) | path re-key + exact + substring | clean |
| client name / z-id | exact + zid-anchored composite repair | clean |
| account z-id | exact whole-token | clean |
| `adv_drill` object KEYS + bare LIST-STRINGS | key + list-string walk | clean |
| `"Name (zid)"` composites | zid-anchored repair | clean |
| suffixed column keys `"Name_inflow"` | spaced-string substring scan | clean |
| exec_summary free-text | free-text substring scan | clean |
| context-dependent label/key (tickers vs names) | value-membership (ticker never in map) | clean |

## Files Modified

| File | Change |
|------|--------|
| data/demo/scripts/transform/demo_transform.py | CREATED — the two-pass transform engine |
| data/demo/scripts/transform/fake_identities.py | CREATED — deterministic seeded fake-identity generator |
| data/demo/scripts/transform/README.md | CREATED — engine docs (R4/R6, usage, scope) |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_DEMOV1.002....md | status staged -> pending |
| org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-21/advi_demov1_to2_transform_engine~C.md | CREATED — this log |

## Compiler Tools

| Tool | Result | What it showed |
|------|--------|----------------|
| `git log --oneline -- data/demo/` | empty | No prior demo-transform bulk walker — confirmed new path (mandate Phase 1). |
| `comp-pii audit` | 3 PII refs (ClientsTab), rest clean | Component-layer model; used as a cross-reference baseline alongside TO-0's data-layer inventory (the engine's coverage is verified against TO-0 §3, not comp-pii). |
| `.tools/ds-commit-gate.sh` | exit 0 (py_compile + AST scan + ruff py39) | Clean on demo_transform.py + fake_identities.py at every commit (mandate Phase 2). |
| `--dry-run` reconciliation | 0 unmapped / 0 leaks on 63 files | The embedded leak self-check exits clean; every TO-0 PII field is handled (mandate Phase 3). |

## Next Steps

| Recipient | Item |
|-----------|------|
| **2.0.0_SA_COO~C** | RAVC2 — ADVI_DEMOV1.002 COMPLETE. Engine built + reviewed + dry-run CLEAN; 11 ACs met. |
| **DS~C (self)** | Hold TO-4 (the live populate run) — gated on TO-1 infra (opal-data-demo bucket + OAI policy). |
