# NFRA_COMPUNIFY S2 (the gate) + S3 (comp-which surface-first reorg) (lane: 0.8.0_AE_CloudComp~C)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

## Current State

CTO PASSED S1 (ground-verified 8d55cd616 himself). COO~B GO'd S2 + S3 parallel (both depend only on S1). Both now built, committed, pushed, self-verified. This closes my S0->S3 build arc on NFRA_COMPUNIFY.

**S2 -- comp-coverage-check (THE GATE, CTO ruling #4).** Commits 6560cc103 (gate) + 1eb50c3cb (routability).
- `org/modules/graph/comp_coverage_check.py` -- reads the ledger's OWN `schema.gate_contract.rules` as its SPEC: enumerates the rule ids and dispatches each to a checker; a contract rule with NO checker -> UNVERIFIABLE (never a silent PASS). Enforces all 6 (one_home / seam_reference_integrity / declared_non_redundancy / coverage_single_home / no_trino_phantom_seam / inventory_completeness) + AC5 projection-currency.
- AC5 projection-currency delegates to `comp_coverage_view.projection_lost` (refactored to expose `ledger_union` + `projection_lost`) -- ONE definition of 'current' shared by the gate + the projector. ASSERTS only, never writes the manifest (no SoD break).
- Tri-state exit 0/1/2; NEVER false-PASS on an unreadable ledger.
- `comp-coverage-check selfcheck` = the CTO arch-gate: injected unplaced-tool -> FAIL, silent-overlap -> FAIL, stale-projection -> FAIL, no-checker-rule -> UNVERIFIABLE, clean -> PASS. All green.
- `.tools/comp-coverage-check` shim (runpy pattern). Placed in ledger meta_tools (enforcement-gate). comp-which-routable via a curated rule (coverage-gate intent).
- WIRED: advisory block B6 in `.tools/safe-commit.sh` (lane ANY; "AE wires hooks") -- triggers only when a commit touches `comp-coverage-map.yaml` or `.tools/comp-*`; `|| true` so it never blocks; ramp-to-blocking documented. bash -n + comp-shell clean. LIVE-FIRED `[coverage-check] PASS` on every COMPUNIFY commit since (real proof). It also caught a real drift mid-build (the new shim made the gate's own tool UNPLACED until I added it to meta_tools).

**S3 -- comp-which surface-first, LEDGER-DRIVEN (ruling #1).** Commit d607b5f32 (+ 1eb50c3cb routability rule).
- New surface-first stage in `.tools/comp-which` READS `comp-coverage-map.yaml` (the taxonomy, NOT a parallel routing table): a surface-named question resolves SURFACE -> drills to the tool by concern-overlap. The LD-0224 raw-grep-fallback fix.
- Positioned AFTER strong-curated (ZERO regression -- the paraphrase-tuned hot path untouched; produces/blast/iam/pii/transform/freshness verified unchanged) and BEFORE the grep fallback (catches the fallback class).
- Two-tier surface detection: SPECIFIC markers beat GENERIC 'cloud X' (so "ms cloud estate" -> MS-CLOUD, not AWS); word-boundary matched ('git' != 'digit'). Drill-ranking strips surface-noise tokens (so "fresh in aws" ranks comp-freshness over comp-aws).
- MS-CLOUD returns the HONEST ledger GAP (no comp-ms invented). Never-dead-end preserved (unmatched -> comp-grep/comp-glob). `comp-which --surfaces` dumps the taxonomy as DATA (AC3, COMPLEARN-readable). ruff clean.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-coverage-check selfcheck | the CTO S2 arch-gate | PASS | 3 injected violations each FAIL + no-checker UNVERIFIABLE + clean PASS; all 5 behaviors correct. |
| comp-coverage-check (B6 live) | fired by safe-commit on every COMPUNIFY commit | PASS | `[coverage-check] PASS` in 5+ commit logs -- the wiring works in the real commit path. |
| comp-which (S2 mandate) | "how do existing gates wire into commit" + grep safe-commit | PASS | matched comp-surface-check's B5 advisory pattern -> mirrored it as B6 (not a bespoke mechanism). |
| comp-which (S3 mandate) | before/after battery (surface + paraphrase + never-dead-end) | PASS | surface-named -> taxonomy route; ms-cloud GAP; paraphrase routes unchanged; "where is X defined" -> comp-grep primitive. |
| comp-shell scan | `.tools/safe-commit.sh` (Rule 16) | PASS | 0 findings; bash -n OK -- safe to edit the universal commit path. |
| ds-commit-gate / ruff | comp_coverage_check.py, comp_coverage_view.py, comp-which | PASS | py_compile + AST + ruff py39 all clean (E402 fixed: docstring before `from __future__`). |

**What worked:** building the gate to READ its own contract (not a parallel rule-set) means the gate can never drift from the map it enforces -- and the gate caught its own tool's unplaced-ness the moment I added the shim (the design proving itself). The B6 advisory wiring (`|| true`, narrow trigger) let me edit the universal commit path with zero blast risk, verified live.
**What failed / gap found:** S3 surface detection had two real bugs caught in testing -- (1) "ms cloud estate" mis-routed to AWS because the generic "cloud estate" keyword (12 chars) beat "ms cloud" (8) under longest-match -> fixed with a two-tier specific/generic split + word-boundary matching; (2) surface-name tokens inflated the wrong tool's drill score ("fresh in aws" ranked comp-aws over comp-freshness) -> fixed by stripping surface-noise tokens before ranking. Both fixed + re-verified.

## MCP Traffic

~4 dispatches. Significant: COO~B GO-S2+S3 (with the CTO regeneration-ownership AC5 ruling baked into S2); my RAVC2 S2+S3 -> COO~B (the unified manifest exec-handoff); CC -> CTO (both arch-gate criteria, self-proven).

## Blockers

**None.** One unified MANIFEST EXEC-HANDOFF open (not a blocker): regenerate `graph-call-manifest.yaml#tools_index` as the generated view (the S1 GENERATED-marker + the now-45-tool inventory incl comp-coverage-check). graph-call-manifest.yaml = ANY_EXEC; RAVC'd to COO~B with the marker text + the `comp_coverage_view.py emit`/`--verify` mechanism. Everything else committed + verified.

## Next Steps

1. **[2.0.0_SA_COO~B]** land the unified manifest regeneration (S1 marker + current inventory); trigger V1.
2. **[1.0.0_SA_CTO]** S2 arch-gate (`comp-coverage-check selfcheck` + the live B6 firings) + S3 arch-gate (the raw-grep-fallback-class improvement). Both demonstrable now.
3. **[3.0.0_SA_CVO]** V1: the gate ACTUALLY enforces (run `comp-coverage-check selfcheck`); surface-first routes data-driven (`comp-which --surfaces` + the battery); completeness + non-redundancy hold (`comp-coverage-check check` = PASS).
4. **[0.8.0_AE_CloudComp~C]** S0->S3 build arc COMPLETE. Holding for V1 findings / any CTO/CVO ruling -- will action immediately. Event-driven via the persistent Monitor; no cron.
