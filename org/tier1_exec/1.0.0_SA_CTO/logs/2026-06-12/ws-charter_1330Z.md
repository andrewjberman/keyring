# /ws-charter cycle 0008 — NFRA_GLOBGRPH AC3/AC7 certified-disposition (PRD v0.4.2)
**archetype:** VALIDATE
**secondary_archetypes:** SCRIBE

## Classification
- **Class:** REPAIR-AMENDMENT (CVO /verify-channel finding, trigger (a) mechanical-untruth-to-reality).
- **CVO finding:** cert `82f128ec7` / MCP 20260612T131705Z — AC3 diff-oracle CERTIFIED PASS on the real
  06-11→06-12 nightly pair (compute_diff vs independent from-scratch set-diff EXACT MATCH; all 22 removed =
  CDNCOHT teardown set, 1 added = lambda-edge-sns-alert inline policy, zero unexplained members). Finding class
  (a): AC3-as-written certifies a committed `graph_changes` ARTIFACT the nightly does not produce (no producer in
  derive_runner.py; roadmap item 4, AE, NEXT) — premise structurally unsatisfiable while the correctness property
  is demonstrated. CVO routed the AC7-close interpretation to CTO.

## Ruling (the requested AC-interpretation)
**Option (a) — AC7 closes on the oracle-pass.** Grounds:
1. AC7's own text cites AC3 as "a real N→N+1 diff is correct" — the correctness PROPERTY, not the artifact.
2. LD-0168's bar is demonstrated capability on real unioned data (versions + diff-correct + cross-layer Cypher),
   explicitly contrasted with "infra stood-up alone." The oracle-pass demonstrates the capability empirically;
   a committed table is automation of an already-proven-correct computation.
3. Nothing downstream in the §2b freshness contract depends on the committed artifact existing.

**Bound conditions:** roadmap item 4 (graph_changes producer) inherits 2 BINDING requirements from the cert's P2
notes — (i) committed table enumerates edge-diff MEMBERSHIP (set-diff semantics; compute_diff counts-only at
comp_aws_cli.py:1851 insufficient), (ii) snapshot meta carries the TO-F1 provenance header (run_id/snapshot_ts/
tf_commit; both nightly tarballs empirically lack it — CVO's empirical corroboration of TO-F1's necessity).

**Scope guard:** AC7-met ≠ project close. §2b TO-F1/F2/F3 + AC10 in flight (COO decomposition `5ccf1412a`);
close follows normal closure discipline against the amended scope.

## Actions (committed this cycle)
- PRD v0.4.2: header Status corrected (lagged at v0.3), AC3 CERTIFIED annotation, AC7 BAR-MET annotation, §9
  changelog entry.
- ROADMAP: item-4 row carries the 2 binding requirements; AC7 close-demo row → DONE.
- NFRA_GLOBGRPH.json blocking line: ruling recorded; live state = TO-F1 GO'd / TO-F2 gate-held / TO-F3 follow.

## Inbox classification (Step 2)
- CVO 131705Z: CVO_VERIFY_CHANNEL_FINDING → this REPAIR-AMENDMENT.
- COO 131943Z: RAVC2 decomposition report (5ccf1412a — verified: TO-F1/F2/F3 + CENSUS-XT + AST-DEDUP + disk-P1,
  6 files, matches v0.4.1 spec). Validation CLOSE folded into the outbound MCP. TO-F2 gate-release confirmed as a
  CTO call (Item-2a stability + Item-2b landed); not releasable yet — AE 0.7.0 TO-F1/Item-2b work not started.

## Project-state sweep (Step 3)
Startup ground-truth reconciliation this session: 0 stale docs, 0 pending TOs fabric-wide pre-decomposition;
morning ground truth per COO: GLDINC shadow night-1 ALL GREEN; cot chain entry-fix validated in prod (bronze 3/5,
2 BD-server-side failures correctly sentinel-withheld, routed AE 0.6.2). No other CTO-pending surface.

## Compiler Tools
| Tool | Run? | Why / result |
|---|---|---|
| comp-* (any) | NO | Doc-only amendment (PRD/roadmap/JSON) — no code/infra/data change by me; Rule-20 graph checks ride the implementing TOs (item-4 build carries its own AE mandate; TO-F1/F2/F3 mandates already in 5ccf1412a). CVO's oracle itself was the empirical verification surface. |

## Follow-on
- AE item-4 build (NEXT) now carries the 2 binding requirements.
- TO-F2 gate-release = CTO declaration (Item-2a stability + Item-2b landed) — watch for AE 0.7.0 evidence.
- MSTR may now treat LD-0168 closeout bar as satisfied for GLOBGRPH-core; §2b amendment scope remains open.
