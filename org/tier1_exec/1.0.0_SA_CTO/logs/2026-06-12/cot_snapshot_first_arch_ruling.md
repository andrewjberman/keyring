# COT snapshot-first restructure — CTO architecture ruling (DS proposal 9e045e02f, Andrew-direct)
**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

Trigger: DS 0.4.0 [ARCH REVIEW] 202925Z + COO parallel route 202950Z. Brief read in full
(docs/briefs/cot-snapshot-first-restructure-proposal-20260612.md). Andrew-direct strategic direction
("Cottonwood should be very light and easy to work with"); design rulings are this document.

## RULING 1 — SNAP_00 design: CONCUR. Snapshot-first is the right architecture for cot.
The decisive facts are DS's two survey findings: qt1 reconciles 0.1% to certified AUA AND captures
transferred-in positions FIFO structurally misses (the snapshot is MORE correct, not merely sufficient);
qt4 IS the per-lot table B_01 reconstructs. The FIFO fork was shaped by 49F constraints (deep history,
corrupted txns, dual custodians) cot does not have. Principle ratified: per-day state FROM the snapshot;
transactions for FLOW classification only. Zero bd changes (firm separation holds); 4-phase
shadow-gated sequencing follows banked doctrine exactly. Design conditions on SNAP_00:
(a) parallel loads (if any) follow the standing convention — index-slot or A_01-provenance;
(b) the built-in AUA reconciliation gets EXPLICIT thresholds (config constants, fail-closed, logged
    daily) — DS proposes numbers from the empirical distribution; shape = WARN band + hard-FAIL band;
(c) the MV/Units price reference guards zero/dust Units, and gap-day yfinance fills carry a SOURCE
    column so snapshot-priced vs fallback-priced rows are distinguishable forever (provenance, not
    silent blending — the S_00 4-tier lesson);
(d) Rule 17 unchanged: the new silver merges (holdings/unrealized/realized) are passthrough
    dedup+dtype; exclusions/ghost-account judgment stays in SNAP_00 (gold) as proposed;
(e) E_00/E_01: REFRAME not retire — E_00 becomes the external snapshot-vs-allocations reconciliation
    monitor (the oracle watching SNAP_00's built-in check from outside; producer-verifies +
    independent-observer is the GLDINC pattern). DS shapes it at P3.

## RULING 2 — Shadow gate: N = 3, and "match" means EXPLAINED, not byte-identical.
Three consecutive clean nightly shadow runs before P2. Critically: FIFO-vs-snapshot WILL legitimately
diverge (transfers-in = the snapshot being RIGHT). So the gate is NOT diff=0 — it is: AUA within
threshold + per-account MV deltas enumerated + EVERY divergence classified (expected-superior
[transfers-in/custodian-basis] vs unexplained). 3 nights with ZERO unexplained divergences = gate pass.
**P2 framing follows: this is a never-widen DRIFT-ACCEPTANCE, not a DELTA=0 deploy** — served output
MOVES (toward the more-correct snapshot truth), so P2 takes full CTO+COO sign-off with the 3-night
divergence census as the evidence body. Say it now so nobody frames P2 as no-hold later.

## RULING 3 — bd-securities DynamoDB: KEEP SHARED.
It is a firm-agnostic security-classification reference (market data), not firm data — firm separation
doctrine targets firm DATA PLANES (buckets, pipelines, served artifacts), and forking a security master
creates exactly the config-drift class DEBTSCAN 3b hunts (one logical truth, N copies, M values).
Conditions: cot's access is READ-ONLY on the shared table (verify the IAM shape at P3); the S3
cross-bucket Deny architecture is untouched (DynamoDB reference reads are not in its scope). The
"bd-securities" NAME is now a misnomer for a shared estate table — cosmetic, banked for some future
rename window, NOT now.

## RULING 4 — Backfill bridge: A-then-C ratified; B REJECTED-by-default; no Andrew escalation needed.
Probe BD as-of holdings first (existing harness; the MM/DD/YYYY + top-level asOfDate requirements are
already banked from the 06-09 probes). Probe succeeds → backfill the window, done. Probe fails → C
(accept the 06-09 position-level floor; account-level AUA to 04-22 survives via allocations) — with the
record that no position-level consumer for that window exists today. B (one-time FIFO bridge) is
REJECTED as a default: it would bake the known transferred-in blind spot into the permanent historical
record; and retirement ≠ deletion — the FIFO scripts live in git history forever, so B remains
exercisable LATER if a real consumer for that window ever materializes. That reversibility is why this
needs no Andrew escalation: C forecloses nothing.

## RULING 5 — P0 TONIGHT (the time-sensitive call): SPLIT IT. COO's baseline instinct is right.
P0's legs differ in chain exposure:
- **HOLD until tomorrow:** the cot_silver_merge.py TABLE_CONFIG change. The new tables are additive,
  but the MERGE SCRIPT IS SHARED — transactions/allocations (tonight's served-chain inputs) flow
  through the same code; a config edit carries nonzero risk of breaking the whole merge step on
  exactly the night COO needs a clean post-fix 5/5 baseline. Lands tomorrow on a clean baseline.
- **RIDE tonight (observe-only):** qt3/qt4 LANDING validation — pure observation of whether the xlsx
  arrive (zero chain impact); that evidence is wanted from tonight regardless.
- **holdings.json working-tree delta:** commit tonight ONLY if it is parity with the S3 template
  already in use (git hygiene); if committing CHANGES tonight's pull behavior, it holds with the
  TABLE_CONFIG. DS knows which; default = hold.

## Registration + sequencing (COO lane, my recommendation)
This meets the project bar (multi-session, multi-agent, phased, never-widen-gated): register a project
code (suggest ADVI macro, e.g. ADVI_COTSNP); the DS brief + THIS ruling = the governing design pair (no
re-authored PRD needed — the brief is PRD-grade; efficiency over ceremony); COO decomposes P0–P3 TOs
with the phase gates as written + the conditions above folded into TO bodies. The D2X orphan
(hybrid_price_fill precondition) closes at P3 as proposed — DEBTSCAN's first ledger item to burn down.

## Compiler Tools
| Tool | Run? | Why / result |
|---|---|---|
| comp-* (any) | NO | Ruling on a proposal whose survey evidence (live S3 listings, 43-script census, dispatch chains, template extractions) IS the empirical layer; no change by me this session. Phase TOs carry mandates: comp-pipescript io/deployed on every touched script, comp-blast on retire targets at P2 (verify-before-delete), comp-validate cot configs updated for SNAP_00 outputs. |
