# DIAL inputs ledger — comp-pipescript (pre-dial, committed as accrued)

**Author:** 3.0.0_SA_CVO · **Date:** 2026-08-03 · **Status:** INPUTS ONLY — the dial itself has
not started; Andrew queued comp-pipescript as the next DIALED-TOOL-FLOW subject this session
(verbatim @ ANDREW_DIRECT_comptools_dial_session_20260803.md). Template:
DIALED_TOOL_FLOW_DESIGN_20260731.md. **Lesson applied: the comp-blast dial's 28 SEV1/SEV2
findings lived in an uncommitted workflow journal that no longer exists — this ledger commits
inputs the moment they accrue.**

## Known blindnesses to carry into P0 (census) / P6 (exercise gates)

1. **DISPATCH-STAGED WRITES INVISIBLE** (0.2.0_DS_PortfolioAnalytics, T2.A close 2026-08-03,
   via COO 205716Z; diagnosis @0b5acf3148): `comp-pipescript io dim_mdpf_aggregate_aua_timeseries`
   (with the now-required `--pipeline mdpf` flag) reports WRITES none-detected — the
   revamp/platinum writes are staged by the dispatcher (`mdpf-daily-dispatch.sh:476-488`), not by
   the gold script, so the extractor cannot see them. Hazard class: under-reporting drives
   deletion (a future tracer reads no-writes as orphan — same class as comp-iam Rule 22a).
   epistemic_status: OBSERVED (measured live by DS).

2. **ASSETS MONOLITH TREE ABSENT FROM THE PIPELINE MAP — TWO-LAYER** (via CTO 210613Z + COO
   211830Z): (a) SILVER case — `comp-pipescript io` rc=2 on `data/assets/scripts/silver/*`
   (0.4.0_DS_ClientPlatform, OPAL_VENDORPROVENANCE.WS1); (b) GOLD case, independently measured —
   all three cottonwood producers, the tool's own error naming its valid trees as bd/inf/cot/mdpf
   (0.2.0_DS, T1.C). The deploy-verify instrument cannot see the estate's CANONICAL tree at
   either layer. **Build TO staged @2f256a3830 to `0.8.0_AE_CloudComp~B` (CTO route-as-build);
   its Phase 3 report is addressed to 3.0.0_SA_CVO for register closure — OPEN CVO OBLIGATION.**
   epistemic_status: OBSERVED (measured live by DS, twice, independently).

3. **INTERFACE DRIFT MARKER**: the `--pipeline mdpf` flag is described by DS as "now-required" —
   a recent interface change; P5 (dependency alignment) must sweep every canon surface that
   still shows the flagless invocation (CLAUDE.md comp-tools table, XXX.md role minimums,
   skill docs). epistemic_status: ASSESSED (inferred from DS's phrasing; verify at dial start).

## Adjacent register notes accrued the same evening (NOT comp-pipescript; recorded so they land somewhere durable)

- **comp-estate — TWO distinct rendering blindnesses on the mdpf vertical**: (a) the accrual
  producer family renders as a C0 fact (`mdpf-accrual-trigger`) rather than its own chain block
  (DS via COO 205716Z); (b) the cottonwood MDPF legs render in NO chain at all — only `advi-cot`
  exists, a different thread (0.2.0_DS, T1.C Phase 1, via COO 211830Z). Register-only residuals
  on comp-estate's record; candidate P6 exercise gates for a future comp-estate re-dial.
- **comp-routes**: cache-policy identity/TTL blindness @aeca48e395 RE-CONFIRMED by ~F's T3.A
  (worked around on live `get-distribution-config`; DESIRED/APPLIED agreed 25=25 this
  instance) (CTO 210613Z). Existing register entry stands, now with a live workaround record.
- **comp-estate (c) + CROSS-TOOL — mdpf freshness family is PHANTOM in the shared census**
  (CTO 212228Z; evidence `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/MDPF_GLOBAL_T1A/`
  @389c528ddb, instrument_drift block): the mdpf chain prose describes `mdpf-freshness-checker`
  (Lambda + cron rule + alarm); T1.A measured ALL THREE absent live (ResourceNotFoundException,
  passing positive control) and absent from the 07-29 trigger-map baseline. epistemic_status:
  OBSERVED. **Cross-tool corollary (OBSERVED this session): comp-blast's graph carries the same
  phantom — a NOT-FOUND probe tonight offered `lambda:mdpf-freshness-checker` as a near-match
  candidate — so the defect sits in the SHARED estate census/snapshot layer, and any re-dial
  should target the census producer, not each tool's rendering.** Context (ASSESSED): the
  described instrument is of the class the 2026-07-28 moratorium bans building — the prose
  likely predates the moratorium; the map describes an instrument that was legislated away.

## comp-blast carry-forward (from the unclosed 07-31 dial — for whoever closes it)

Still live at `org/modules/graph/` (zero commits since 07-31 evening), in AE's stated fix order:
(a) cp1252 crash safe-not-absent (rc=1, 20/2252 nodes, cli.py:378->:364); (b) `--direction up`
inverts `--check-consumers` into a false phantom (rc=4, wrong); (c) substring `find_node` +
`matches[0]` answers about a DIFFERENT node at rc=0; (d) upstream traversal does not follow
FETCHES edges (6 real component callers reported as 0). P8 + DIAL record synthesis never ran;
no DIAL record exists in the tree; the workflow journal is gone from temp. Three naming acts
undecided at Andrew: comp-blast purpose (P1), `chain` reserved-term collision, deletion rulings.

— 3.0.0_SA_CVO
