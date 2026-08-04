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
- **comp-estate (d) — frontend row asserts a reader the DEPLOYED artifact refutes** (~F T5.A
  census @b877dbc0f5, via COO 221526Z): mdpf chain prose asserts `portal_data_proxy`
  `/aum/aggregate-mdpf` reads the underscore root — FALSIFIED on the deployed plane (deployed
  proxy sha LpodJICu, 2/2 py files, zero mdpf references; `/v1/aum/*` reads DynamoDB).
  epistemic_status: OBSERVED (deployed-artifact read). Fourth mdpf-vertical staleness instance
  tonight.
- **NEW HAZARD CLASS (its own line, per COO): A NEVER-DEPLOYED DIFF FILE IN THE REPO READS AS
  EVIDENCE OF A LIVE ROUTE to any text-plane instrument** — provenance of (d)'s stale claim is
  `data/mdpf/scripts/backfill/HANDOFF_AE_lambda_route.diff` (never deployed) + the `aum.ts:474`
  comment; the claim propagated diff -> estate prose -> CTO ruling seed before ~F's
  deployed-plane read killed it. Only a deployed-artifact read refutes this class.
  Cross-reference (ASSESSED): this is exactly the ACTIVE x RELEVANT drift class
  NFRA_REPOCOHERENCEGRAPH's relevance_axis exists to catch — a HANDOFF diff whose content
  ceased representing reality; worth naming as an RCG seed-label candidate when the cohorts
  reach `data/`.

## STANDING DIAL CHECK (Andrew-direct RULING 2026-08-03 ~2240Z, verbatim @
## ANDREW_RULING_projections_default_kuzu_full_graph_20260803.md)

Every dial's P0/P1 now asks: **is this tool's universe (a) the kuzudb full resource graph, (b) a
declared TERRITORY-specific full graph (AWS_CLOUD / MS_CLOUD / GIT), or (c) a DECLARED,
intentional exception (hand-drawn registry / amalgamation — comp-estate's C3.ii semantic layer is
the named legal example)?** Anything else — a private, incidentally-scoped universe — is a
finding, not a style choice. Trigger case: comp-blast's private 2,255-node trace graph (4 bucket
nodes) vs comp-kuzu's canonical 20,480-node DB that carried the very node blast missed.
comp-blast specifically: MUST cover all of AWS (build routing at CTO).
**FRAMING (CTO 20260804T003737Z, carried into every universe audit): A HAND-DRAWN REGISTRY CAN
CONTAIN PHANTOMS; A LIVE PROJECTION STRUCTURALLY CANNOT.** The phantom mdpf-freshness-checker
left comp-blast's universe not because anyone fixed it but because a projection from live
canonical state cannot carry a nonexistent node — a categorical property, not a coverage
improvement. A non-conforming tool is therefore not merely under-covered: it is CAPABLE OF
ASSERTING RESOURCES THAT DO NOT EXIST. (Exercised proof: the phantom class now survives only in
comp-estate's census snapshot — one named target with a known mechanism.)

## comp-blast P0-census input (measured this session, Andrew-directed opal-data-mdpf trace)

- **`opal-data-mdpf` is ABSENT from the blast graph universe** — only 4 S3_BUCKET nodes exist
  (bd / inf / portal-v2 / assets), so comp-blast returns NOT-FOUND on the estate's whole mdpf
  feeder bucket and structurally cannot answer "who consumes it." Consumer census had to be done
  by code-plane grep + live primitives (2026-08-03; production consumers DO exist: mdpf-daily-trigger
  Lambda Active, mdpf-daily-refresh-trigger rule ENABLED + firing, EC2 runner last complete run
  07-31 refreshing LEGACY platinum/mdpf/* while the teardown is PARKED). Same mdpf-tree
  coverage-hole family as the comp-pipescript items above. epistemic_status: OBSERVED.
- **Andrew framing to carry into the dial (2026-08-03, this terminal):** a comp-blast NEAR-MATCH
  is itself signal — "probably a good indicator of a duplicated/legacy resource... the reason for
  using comp-blast," not merely a typo aid. Candidate P4 output-vocabulary refinement: label
  near-matches as potential duplicate/legacy candidates, not only "typo candidates."

## comp-trigger caveat (measured 2026-08-04, CTO-corrected census datum)

- **`comp-trigger`'s `LIVE fired-evidence` line reads CloudWatch RULE-METRIC DATAPOINTS, not log
  events — and it MISSED a fire on the trailing edge**: it reported
  `opal-assets-mdpf-portal-publisher-daily` "FIRED 6x (last datapoint 2026-08-02)" while the
  Lambda's log START events show 08-01/08-02/08-03 16:15:2xZ, 3/3 (CTO 022105Z, filter-log-events
  on event CONTENT). Same class as VERIFICATION_LAW #14 (stream metadata is not stream content).
  **Rule for its output: the fired-evidence line is a FLOOR on recency, never a last-fire claim**
  — a trailing-edge absence needs the log-event check before anyone cites "did not fire."
  Candidate dial item when comp-trigger's turn comes. epistemic_status: OBSERVED (both limbs).

## comp-blast carry-forward (from the unclosed 07-31 dial — for whoever closes it)

Still live at `org/modules/graph/` (zero commits since 07-31 evening), in AE's stated fix order:
(a) cp1252 crash safe-not-absent (rc=1, 20/2252 nodes, cli.py:378->:364); (b) `--direction up`
inverts `--check-consumers` into a false phantom (rc=4, wrong); (c) substring `find_node` +
`matches[0]` answers about a DIFFERENT node at rc=0; (d) upstream traversal does not follow
FETCHES edges (6 real component callers reported as 0). P8 + DIAL record synthesis never ran;
no DIAL record exists in the tree; the workflow journal is gone from temp. Three naming acts
undecided at Andrew: comp-blast purpose (P1), `chain` reserved-term collision, deletion rulings.

— 3.0.0_SA_CVO
