# DIAL RECORD — comp-kuzu (+ -full / -inc variants) — CLOSE, P8 routed

**Dialer/Verifier:** 3.0.0_SA_CVO · **Date:** 2026-08-04 ~1315–1400Z (Andrew-present session;
start word ~1300Z @74451794e/@fa4279588, sequencing CTO-concurred 131701Z).
**Method:** DIALED_TOOL_FLOW_DESIGN_20260731.md. **Baselines:** `dial_baselines/comp-kuzu_P0_20260804.txt`
@41601d82e (incl. the pipe-rc correction block — see Method notes).

## VERDICT: DIALED-PENDING-P8 — every closed phase passed on a probe that could have failed

| Phase | Verdict | Evidence (exercised) |
|---|---|---|
| P0 scope+baseline | PASS | Units: 3 shims (`comp-kuzu`/`-full`/`-inc`) -> `kuzu_cli.py` (+`_provenance`,`_canonical`) + 4 loaders + 4 DB stores. Baselines Q1–Q6: 20,495 nodes / 41,010 edges / type census / A_00 2-hop=23, provenance current (snapshot 6120433618380034963) |
| P1 purpose | PASS (K2 low) | Registry `does:` crisp; LD-0307 three-tool model (derive=producer, full=MSTR-startup, inc=worker default) declared on all 3 rows. K2: engine docstring carries usage only, no purpose line |
| P2 name+aliases | PASS | 3 live names all in tools_index w/ entries; no retired kuzu aliases; retired-alias invariant PASS. (K5 found on an ADJACENT name — below) |
| P3 registration+contracts | PASS (K3) | manifest-check completeness PASS post-K1; comp-kuzu contract verified CURRENT incl. exit_source line-cites re-checked against the 07-25 engine (DB-missing ~:65, query-error ~:89 — hold). Provenance contract EXERCISED live: current-vs-HEAD, per-table vintage, two-producer cohort note, UNKNOWN-VINTAGE. K3: `-full`/`-inc` sit in the declared 49-pending contract tail — the `-inc` labeled-stale rc semantics is verdict-bearing and undeclared |
| P4 vocab+structure | PASS-partial | Canon vocab (node_type/layer/drift_class); structure exposure via `CALL TABLE_INFO` exercised. `--head` not adopted (`--limit` instead) — per the Andrew-ratified rollout rule (adopt AS TOUCHED) this is noted, not a defect |
| P5 dependency alignment | PASS (K1 closed, K4/K5 routed) | K1 found+repaired+CVO-verified same hour (below). CLAUDE.md Rule 20 + trigger-table row verified CURRENT against measured behavior. Secondary mentions swept (3 skills, 2 doctrine docs): doctrine = accurate history; molecule:68 = K5 |
| P6 exercise gates | PASS (1 skip-with-reason) | Malformed Cypher rc=1/stderr-only/stdout-empty; honest-empty (0 rows) rc=0; dead `--db-path` rc=1 LOUD; manifest-less DB = UNKNOWN VINTAGE loud warn-and-serve (BY DESIGN — scratch DBs legitimate; Rule 20 is the compensating control; hazard demonstrated: frozen Jun-12 copy answers 1,166 vs canonical 20,495); TEMPLATE-comment copy-blind path rc=0 (kuzu accepts `//`). SKIPPED-WITH-REASON: `-inc` labeled-stale serve path — requires a behind-HEAD state I will not manufacture on the shared canonical store mid-session; converted to re-dial trigger 6 |
| P7 residue audit | CENSUS DONE, deletions ruled-not-taken | NECESSARY: kuzu_nessie_db(+manifest), kuzu_cli.py, loaders, incremental_refresh. HISTORICAL: kuzu_db (Jun-12 scratch, 1,166 nodes), kuzu_cost_enrich.py (TO-D4 one-shot). HISTORICAL-AT-RISK (do NOT delete): kuzu_ac7.db + kuzu_ac_traversals.py — tied to open NFRA_GLOBGRPH.ITEM-3 (AC-gates honestly UNVALIDATED). AT-RISK: kuzu_stitch_db = K4 |
| P8 independent descent | OPEN — ROUTED | A non-dialer agent cold-exercises from docs alone; seat pick routed via COO/CTO. Close of P8 folds its defects here |

## Findings

- **K1 (SEV-MED, canon-surface drift) — CLOSED same hour.** graph-call-manifest canonical calls
  cited nonexistent `id` property x4 (:101/:114/:127/:920); live schema PK is `node_id`
  (TABLE_INFO exercised). Each failed as written. CTO repaired @e0d657799 (+ TEMPLATE markers per
  my recommendation); CVO-verified by exercise: residual census 0, flagship verbatim rc=0/50 rows,
  and the repair's own new surface probed — inline `//` TEMPLATE comment is kuzu-legal, so the
  copy-blind failure did not relocate. comp-system 06 recompile @e1df5bb21.
- **K2 (LOW):** purpose line in registry only, not the engine docstring (P1 rule: verbatim into BOTH).
- **K3 (LOW-MED):** `-full`/`-inc` output contracts pending — `-inc`'s labeled-stale serve is a
  VERDICT-BEARING behavior with undeclared rc/stdout semantics. Declare on next touch.
- **K4 (MED, routed CTO):** manifest xlayer entry (:915ff) declares kuzu_stitch_db freshness
  "reload on the nightly cycle" while the store's mtime is **Jul 7 = 28d stale**; post-K1 the same
  entry now carries both `status: canonical # LANDED` and a `TEMPLATE (planned, post P2-STITCH)`
  marker — internally contradictory. Either the stitch reload is a broken pipeline or the entry's
  freshness claim is fiction; CTO to adjudicate which.
- **K5 (LOW-MED, routed CTO + skill owner):** bare `pipescript` (retired rc=2 stub, Andrew 07-29
  prohibition) is NOT declared in `retired_aliases`, so the retired-alias invariant is
  structurally blind to its citations — live citation at `.claude/skills/molecule/SKILL.md:68`.
  Declare the alias; the invariant then polices it estate-wide.

## Method notes (banked)

- **The tail-rc pipe class bit twice in one hour, two seats** (my Q4–Q6 first cut; CTO's own :101
  re-exercise). Both self-caught by re-measure. The dial's standing rule: rc capture direct,
  display after — never through a pipe.
- The negative-control-first discipline surfaced K1 inside the first 10 minutes of P0 — the
  finding fell out of a control, not a read (CONTROLS_OVER_CARE holding again).

## DECLARED RE-DIAL TRIGGERS

1. CloudNode/CloudEdge SCHEMA change (mirrors comp-blast trigger 1 — one event reopens both dials).
2. The census-layer seam fix landing (json/-tier ingestion, identity primitive @655e3f551) —
   changes population semantics of every query.
3. Any manifest edit touching the comp-kuzu family rows or canonical calls.
4. Engine change >~50 lines across kuzu_cli.py / _provenance / _canonical / loaders.
5. NFRA_KUZUSPLIT discipline change (full/inc modes, `GLOBGRPH_KUZU_*` env flags, liveness lock).
6. First real exercise of the `-inc` labeled-stale path (converts the P6 skip).
7. P8 descent completion.

— 3.0.0_SA_CVO

## P8 FOLD -- independent descent COMPLETE (~D @150dd98d7, 2026-08-04 ~1650Z); trigger 7 CONSUMED

Descent: 10 cold captures, independence held (zero dial-record reads pre-diff, gate-cited).
Convergence: the K1 repair HELD under cold use (primer taught node_id correctly); the off-default
findings (K3/K4/K5, -inc skip) were never hit cold -- consistent with defect mass off the default
path. Two COLD-FOUND findings folded, one verdict of mine amended:

- **K6 (MED, descent-found; amends my P6 "honest-empty PASS"): 0-rows carries no universe/scope
  statement.** My P6 scored bare "(0 rows)" as honest-empty -- TRUE from the dialer's frame,
  INSUFFICIENT from cold use: 3 of ~D's 8 real questions returned 0 rows whose honest reading was
  out-of-universe (tool sources, config yamls, dispatch harnesses) or wrong-pattern, and nothing
  discriminates. This is the kuzu instance of trace-T1 -- the family design point (with DEPTH-1)
  now has instances measured on THREE instruments. Remedy shape per the family rule: a one-line
  scope note on 0-rows or unmodeled-class naming in the primer.
- **K7 (LOW-MED, descent-found): lineage edge-direction convention stated nowhere** -- READS_S3
  points script->key, so BOTH lineage edges point INTO the key and a naive flow traversal
  silently 0-rows (~D K7, self-corrected K7b -> 17 readers). One primer line kills the class.
- **Cross-instrument (shared with trace record): scope asymmetry, no cross-pointer** --
  gold_dispatch in trace's universe not kuzu's; AWS planes in kuzu's not trace's; neither
  instrument points across on a miss. NAVIGATE-consolidation material, routed CTO.

## K4 DISPOSITION (CTO ruling 191057Z) -- RETIRE-CANDIDATE AT THE PRD

The stitch DB's fate is adjudicated at the C-indexed consolidation PRD (canonical cross-layer
already rides kuzu_nessie_db per the corrected entry); NO interim rebuild machinery gets built
-- standing machinery for an unsettled surface is the route-first doctrine's exact target. The
K4 fix seat waits on the PRD deliberately; the entry stays TEMPLATE-marked meanwhile. K4 moves
from "routed, awaiting adjudication" to DISPOSITIONED-PENDING-PRD.

## RE-DIAL (K-set landing) -- ~B fixes CLOSED-VERIFIED 2026-08-04 ~2333Z

My own exercises, rc direct: **K6 CLOSED** @834c87c00 -- out-of-universe 0-rows now prints the
scope note beside the count ("only what the graph MODELS can match... Ground the class first" +
the grounding pointer); --json stdout stays pure (note to stderr); non-zero output byte-stable.
**K7 CLOSED** @834c87c00 -- DIRECTION block in --schema states the convention exactly
(actor->acted-on; BOTH lineage edges point INTO the key; start lineage at the script side).
**K3 CLOSED** -- -full/-inc contract entries moved pending->contracts, source-grounded
(-inc labeled-stale declared rc-NEUTRAL/verdict-in-band from source; the live exercise stays
trigger 6 BY DESIGN, declared-not-manufactured). Gate proof: output-contract invariant now
"declared 26 + pending 44" (was 20+49 pre-fan-out) over 70 tools. **K4 untouched verified**
(commit stat: kuzu_cli.py only) per the CTO 191057Z disposition. ATTRIBUTION (per NEVER#7, no
rewrite): K3 entries = ~B authorship inside ~F's @ffb41a8495 (shared-file interleave, both
seats' honest maps on record); K6/K7 = ~B @834c87c00.


## P7 RE-STATEMENT 2026-09-09T16:29Z (NFRA_CLDGRPH ADJUDICATION_v1.md C-S26)

The P7 row above is not edited; it is superseded on every class as of this line, on measured ground recorded at C-S26:
- **NECESSARY** (kuzu_nessie_db + manifest, kuzu_cli.py, loaders, incremental_refresh): superseded by PRD R7 and FWD-7 -- the store is retired and switched off (TO-CG-D-7/D-8), kuzu_cli.py is a thin client, the engine files are byte-pinned by D7-AC5.
- **HISTORICAL** kuzu_db: HOLD LIFTED -> RETIRE_WITH_TOMBSTONE (0.8.0_AE_CloudComp). Reproducible from s3://opal-313476888478-globgrph/snapshots/20260612/graph-20260612.tar.gz (71,671 B, present 2026-09-09); 0 readers by two instruments. kuzu_cost_enrich.py: already deleted on the CTO's ruling @1266d65641.
- **HISTORICAL-AT-RISK** kuzu_ac7.db + kuzu_ac_traversals.py: HOLD LIFTED -> ARCHIVE_UNDER_PROJECT (NFRA_GLOBGRPH.ITEM-3; 0.8.0_AE_CloudComp) for the store; the traversal tool is repointed through the served projection (TO-CG-D-7 pass 4) and names no local store. The tie the hold rested on no longer exists.
- **AT-RISK** kuzu_stitch_db (K4): CG-s-20's question (TO-CG-E-4), in flight.
Nothing in P7 remains a hold on any deletion after this line. -- 3.0.0_SA_CVO
