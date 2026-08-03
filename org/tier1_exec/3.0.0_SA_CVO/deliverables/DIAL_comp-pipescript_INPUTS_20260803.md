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

2. **ASSETS MONOLITH TREE ABSENT FROM THE PIPELINE MAP** (0.4.0_DS_ClientPlatform under
   OPAL_VENDORPROVENANCE.WS1, 2026-08-03, via CTO 210613Z): `comp-pipescript io` returns rc=2 on
   `data/assets/scripts/silver/*` — the opal-data-assets tree is not in the pipeline map, so the
   deploy-verify instrument cannot see the estate's CANONICAL tree at all. COO holds it as a
   build candidate. epistemic_status: OBSERVED (measured live by DS).

3. **INTERFACE DRIFT MARKER**: the `--pipeline mdpf` flag is described by DS as "now-required" —
   a recent interface change; P5 (dependency alignment) must sweep every canon surface that
   still shows the flagless invocation (CLAUDE.md comp-tools table, XXX.md role minimums,
   skill docs). epistemic_status: ASSESSED (inferred from DS's phrasing; verify at dial start).

## Adjacent register notes accrued the same evening (NOT comp-pipescript; recorded so they land somewhere durable)

- **comp-estate**: `comp-estate mdpf` renders the accrual producer family as a C0 fact
  (`mdpf-accrual-trigger`) rather than its own chain block — second producer family lacks a
  chain-block rendering (DS via COO 205716Z). Register-only residual on comp-estate's record.
- **comp-routes**: cache-policy identity/TTL blindness @aeca48e395 RE-CONFIRMED by ~F's T3.A
  (worked around on live `get-distribution-config`; DESIRED/APPLIED agreed 25=25 this
  instance) (CTO 210613Z). Existing register entry stands, now with a live workaround record.

## comp-blast carry-forward (from the unclosed 07-31 dial — for whoever closes it)

Still live at `org/modules/graph/` (zero commits since 07-31 evening), in AE's stated fix order:
(a) cp1252 crash safe-not-absent (rc=1, 20/2252 nodes, cli.py:378->:364); (b) `--direction up`
inverts `--check-consumers` into a false phantom (rc=4, wrong); (c) substring `find_node` +
`matches[0]` answers about a DIFFERENT node at rc=0; (d) upstream traversal does not follow
FETCHES edges (6 real component callers reported as 0). P8 + DIAL record synthesis never ran;
no DIAL record exists in the tree; the workflow journal is gone from temp. Three naming acts
undecided at Andrew: comp-blast purpose (P1), `chain` reserved-term collision, deletion rulings.

— 3.0.0_SA_CVO
