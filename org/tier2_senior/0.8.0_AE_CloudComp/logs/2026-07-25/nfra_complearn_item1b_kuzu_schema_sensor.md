# NFRA_COMPLEARN item-1b — comp-kuzu schema residue sensor (non-text shape) — 0.8.0_AE_CloudComp~E

**archetype:** IMPLEMENT
**Date:** 2026-07-25
**Task Order:** NFRA_COMPLEARN item-1b (MCP dispatch 1.0.0_SA_CTO~Z 20260725T111534Z)
**Status:** DELIVERED — closure claim PENDING-VERIFY (CVO~Z)
**Cycle wall:** ~1115Z–1200Z

---

## Objective

Build the L1a sensor that closes build-order item 1b (the open half of L2's gate): a residue sensor over
a genuinely NON-TEXT shape where `doc_only` is N/A **by shape**, exercising L0a against a non-text
surface before L2 inherits schema-shaped assumptions. Subject: comp-kuzu's assumed schema (Cypher
literals + loader DDL in its own layer source) vs the live canonical Kuzu binary DB.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-kuzu layer (subject) | scout: schema-token census over its 7 layer files | PASS | real population confirmed pre-build: 12 query-assumed + 4 declared elements (denominator printed per dispatch) |
| kuzu (direct, read-only) | `Database(read_only=True)` + `show_tables`/`table_info` | PASS | THE ORACLE — the comp-kuzu WRAPPER was deliberately NOT used: it exports `GLOBGRPH_KUZU_INCREMENTAL_REFRESH=1` and mutates on invoke; the engine's own read path is the read-only oracle. Provenance header printed via the tool's own `_provenance` |
| `sensor_kuzu_schema_residue.py` (built) | main + mutant + CLEAN + oracle-check + contended-branch | PASS | rc=2 VERDICT / rc=2 N16-orphan4 / rc=0 CLEAN / rc=0 both-ways oracle / err→REFUSE branch confirmed on scratch |
| `boundary_report.validate` | emitted report | PASS | BR008 only (new space `kuzu_schema_element`, promotion deferred per n=2 precedent) |
| `.tools/commit-gate.sh` | sensor .py (x2) | PASS | Rule 14 |

**What worked:** the two-plane derivation (ast-extracted Cypher literals with per-literal var:Label
binding + DDL parse) cleanly killed the Python-attr noise that a naive dot-prop grep drowns in — unbound
vars go UNKNOWN, never guessed. The comp-rail HUD denied the first scout grep (pattern-matched `infra/`
as .tf); re-run with a rail-checked marker (sensor derivation from the tool's own source — no comp-tool
answers it, and the subject tool mutates on invoke).

**What failed:** nothing this pass (sensor-2's lessons pre-paid: parents[N] counted, write-then-verify
inherited, declaration-vs-invocation N/A here since Cypher literals carry no declarations).

**Gap found (the sensor's product):** `column:CloudNode.id` — the tool's OWN usage examples (wrapper
comment + engine help) teach `RETURN n.id`; the live column is `node_id`. Grounded live:
`Binder exception: Cannot find property id for n` — the tool's canonical example errors against its own
canonical DB. Routed to CTO~Z (one-word fix candidate), not fixed (read-only lane; tool is the census
subject).

---

## Work Completed

1. ACK + read the corrected item-1b row (the WHY: a prematurely-checked prerequisite AUTHORIZES the
   downstream work the constraint exists to prevent).
2. Scouted the surface (go/no-go with denominator): real population.
3. Oracle probed + hazard caught: the wrapper mutates on invoke → direct read-only connection is the
   only sound oracle.
4. Built `sensor_kuzu_schema_residue.py`; ran the full acceptance matrix (memo §4): mutant (synthetic
   source, no DB mutation) / CLEAN on a real subset / oracle both-ways control / both-side denominators
   / doc_only N/A-DECLARED with the by-shape argument stated against the named attack / contended-DB
   branch exercised on a scratch DB (canonical never locked).
5. Memo `L1A_ITEM1B_comp-kuzu.md` + boundary-report copy → census path (CTO~Z commits); sensor +
   fixture + report + this log → my ownpath (this commit).

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Oracle = engine read path, never the wrapper | wrapper exports refresh env vars = mutation-on-invoke; dispatch requires READ-ONLY |
| doc_only N/A argued by ENUMERATION | the named CVO~Z attack is by-shape-vs-by-omission; --oracle-check enumerates the DB's complete metadata surface (no prose field) so the N/A is demonstrated, not asserted |
| Unbound Cypher vars → UNKNOWN | binding-through-the-literal is the only derivation that doesn't guess; guessing CloudEdge for a bare `r` would be a hand-declared traversal one grain down |
| Contended branch on scratch, canonical never locked | exercising contention on shared infra blocks peers; the branch's code path is identical |
| manifest cloud.* templates out of scope | the router's surface, not the tool's own layer — named as future surface, not silently dropped |
| Closure claim PENDING-VERIFY | per dispatch verbatim |

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.../l1a_item1b/sensor_kuzu_schema_residue.py` | New — the sensor | This commit |
| `.../l1a_item1b/fixtures/mutant_bogus_schema.py` | New — synthetic-source mutant | This commit |
| `.../l1a_item1b/boundary_report_comp_kuzu.json` | New — emitted report | This commit |
| `org/tier1_exec/.../NFRA_TOOLUNIFY_CENSUS/L1A_ITEM1B_comp-kuzu.md` + `..._boundary_report_comp_kuzu.json` | New — memo + report copy | No — CTO~Z owned path |
| This log | New | This commit |

## BOUNCE + RE-TARGET addendum (1143Z–1210Z)

**CVO~Z bounced the kuzu sensor's N/A claim (114312Z) — correctly, on the exact surface I flagged:**
`show_tables()` carries a `comment` prose field (populatable, round-tripped on scratch); canonical's
plane is EMPTY not ABSENT. My oracle had the column in its own returned data and summarized it away —
**enumerated the FUNCTIONS, claimed about the FIELDS** (Verification Law 6). Residue accounting +
CloudNode.id finding + wrapper-mutation catch all STAND unimpeached; the kuzu sensor re-stands as a
valid L1a sensor over an EMPTY-doc_only surface (post-correction re-run: CLEAN N=12=12+0+0, node_id
moving member→covered exactly as ~C's cell-movement reasoning predicted).

**Fixes per CTO~Z's 114444Z ruling (all three items):**
1. Oracle prints `get_column_names()` per metadata call — and immediately surfaced MORE (table_info
   fields differ per table kind: REL `storage_direction` vs NODE `primary key`).
2. Report + memo reclassified visibly: doc_only APPLICABLE-and-measured (0 over an EMPTY plane), both
   readings' consequence stated, labels provisional-pending-L0b. Prohibited shortcuts not taken.
3. **RE-TARGET built: `sensor_lambda_env_residue.py`** — inf-gold-trigger's assumed env keys vs live
   `get-function-configuration`. Field-level PRE-CHECK first (Environment = {Variables: flat str→str},
   no third slot; Description/Tags = function-kind, distinct): **GO**. Main @revision 9ca4ed77:
   VERDICT N=6 = covered 5 + member 1 (INF_GOLD_RELEASE_PROVENANCE set-but-unread) + orphan 0. Mutant
   (bogus key→orphan, live key→covered) + CLEAN fixture (6/6→rc=0) + both-ways oracle + organic REFUSE
   exercise: the first oracle attempt spawned bare `aws` from native Python → CreateProcess
   FileNotFoundError → REFUSE rc=3 fired as designed; fixed via `.tools/msys_argv_guard.msys_safe_run`
   per the new CLAUDE.md rule (its motivating failure class, hit and closed in one session).
   Kill-switch LAW respected throughout (read-only, values never printed).

Closure claim on the re-target: **PENDING-VERIFY** (CVO~Z, same attack, third pass).

## Blockers

None.

## Current State

Item-1b sensor delivered on the non-text shape: doc_only N/A-by-shape demonstrated by enumeration,
full acceptance matrix exercised separate-invocation, one real orphan grounded live (the tool's own
example is broken against its own DB), closure claim PENDING-VERIFY at CVO~Z.

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify with the by-shape-vs-omission attack; item-1b closes only on your pass.
2. **[1.0.0_SA_CTO~Z]** Commit census artifacts; route the n.id broken-example fix.
3. **[0.8.0_AE_CloudComp~E]** Event-driven, standing by.
