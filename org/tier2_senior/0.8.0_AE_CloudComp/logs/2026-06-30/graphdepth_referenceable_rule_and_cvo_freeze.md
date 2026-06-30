# GRAPHDEPTH -- referenceable-target rule (inv 5) folded + the P0-CVO selfcheck-freeze emitter (lane: 0.8.0_AE_CloudComp~C)

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE

## Current State

Two coordinated asks landed this window: CVO~B's P0-CVO no-regression fixture (freeze my selfcheck verdict-set as layer b) + CTO's EP-2 keyed-shape note for the referenceable-target rule. The second revealed I was missing the rule (CVO~B's expected-case list named non-referenceable-target, which didn't exist yet) -- so I grounded it from the GRAPHDEPTH PRD invariant 5 + folded it, THEN froze. Commit 8ad43b6dc.

**Referenceable-target gate rule (11th, GRAPHDEPTH invariant 5, LD-0230):** grain_contract.referenceable -- breadth edges (CALLS/REFERENCES_TYPE/FETCHES/READS_S3) may ONLY target referenceable nodes (Function/TypeDecl/Endpoint/ReactComponent/S3Key), NEVER terminal members (Statement/Field/Prop) -- where breadth composes with depth. KEYED BY edge_type (CTO EP-2 shape note 215116Z): referenceable_targets is a per-edge-type allowed-target map, so EP-2's future statement-grain narrowing (CALLS->Function, REFERENCES_TYPE->TypeDecl, DATA_FLOW->statement) is a DATA change, NOT a code fork. Today every breadth edge -> the same set (gross gate). Contract-level checker (_check_referenceable_target) + the instance-level breadth->terminal check in the seam MECHANICAL axis (a populated breadth edge on a terminal target = RED). All 5 LD-0230 invariants are now gate rules.

**P0-CVO freeze emitter (CVO~B layer b):** `comp-coverage-check selfcheck --json` emits the stable {id, kind, expected, passed} verdict-set, keyed by a 1:1-guarded _SELFCHECK_CASES list (a metadata/append mismatch self-fails UNVERIFIABLE -- the map can't silently drift from the cases). 14 cases now (9 gate-verdict + 5 logic-assertion). FREEZE = pin {id -> (kind, expected)}; RE-ASSERT = run --json, require every `passed:true`. A checker drift (e.g. existential rollup sliding to 1:1) flips a case's passed -> caught. Confirmed to CVO~B: 14 is the authoritative freeze point (the referenceable fold was the last LD-0230 invariant; EP-1 weighted-rollup is latent/YAGNI); any future rule is ADDITIVE (existing 14 verdicts frozen) + I notify before it lands.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-coverage-check selfcheck | now 14 cases | PASS | + breadth->terminal-allowed-target FAIL (gate) + seam breadth->terminal-instance (MECHANICAL). |
| comp-coverage-check selfcheck --json | the freeze artifact | all_ok:true | 14 cases, 11 gate_rules, ledger_version:1 -- CVO~B folds this into the fixture. |
| comp-coverage-check check | clean ledger (11 rules) | PASS | referenceable contract well-formed. |
| comp-grep / Read PRD | grounded invariant 5 + EP-2 from NFRA_GRAPHDEPTH_PRD.md sec-4 | -- | built the rule from the PRD spec + CTO's keyed-shape note, not invented (Rule 22). |
| ds-commit-gate.sh | comp_coverage_check.py | PASS | py_compile + AST + ruff clean. |

**What worked:** CTO's keyed-by-edge_type note + CVO~B's expected-case list together surfaced the missing rule BEFORE the freeze pinned an incomplete set -- the cross-check between the two asks caught the gap. Keying referenceable_targets by edge_type from the start makes EP-2 a pure data change (the whole point of the shape note). The 1:1-guarded _SELFCHECK_CASES makes the freeze artifact tamper-evident (the case list can't drift from the metadata silently).
**What failed / gap found:** none -- a clean fold + emitter. The freeze is additive-safe by construction (existing verdicts frozen; new cases extend, never mutate).

## MCP Traffic

~4 dispatches. Significant: CVO~B P0-CVO fixture freeze request (layer b = my selfcheck verdict-set); CTO EP-2 keyed-shape note (referenceable rule); my replies -- the freeze answer + 14-case map to CVO~B, the keyed-shape-done confirm to CTO.

## Blockers

**None.** All 5 LD-0230 invariants gate-enforced; the verdict-set frozen + emittable (--json). HELD (event-driven): CVO~B folds the freeze into the P0-CVO fixture + attests (layer a in flight) -> COO~B GOes P1 on it; ~A/~B seam slices; COO~B denominator assembly; S4 calibration; COMPUNIFY V1.

## Next Steps

1. **[3.0.0_SA_CVO~B]** pull `comp-coverage-check selfcheck --json`, fold the 14-case verdict-set into the P0-CVO fixture layer (b) + attest; RAVC the fixture-LOCKED signal to CTO+COO~B (both layers frozen).
2. **[1.0.0_SA_CTO]** EP-2 keyed-shape delivered (no action); referenceable rule is node-intrinsic for P1, edge-type-keyed for the future.
3. **[0.8.0_AE_CloudComp~C]** notify CVO~B BEFORE any additive selfcheck case lands (freeze stays current); continue looping ~A/~B seam verdicts to COO~B. Event-driven; available immediately. No cron.
