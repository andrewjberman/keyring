# INFRA FINALIZE-AND-VALIDATE PLAN — graph / comp-tooling / ontology / Kimi-SVP

**Author:** `4.0.0_SA_CRO~B` (Chief Research Officer, infra-validate lane)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Commissioned:** Andrew-direct 2026-08-11 (@40ca707f6e) — validate the graph/tooling/ontology/Kimi-SVP
end to end and FINALIZE it so the coming four-month ADVI/49F refactor is *"extremely easy to navigate
and maintain on an infrastructural level"* — *"our tooling and graph have to be immaculate."*
**Posture:** MEASURE + RECOMMEND. CRO does not gate/dispatch/apply. **CTO = arch-gate; COO = execution
decomp; CVO = census/parity authority + verify.** Nothing here is executed off this doc.

**Status of items:** item 1 is GROUNDED (measured) + ORDERED by CTO (074227Z). Items 2–4 are NAMED at
plan-grade with their measurement status stated honestly (doctrine rule 2: an unmarked gap reads as
coverage).

---

## The bar, made checkable

"Immaculate / navigable / maintainable" decomposes into four close-conditions. A refactor of the size
Andrew described (49F-as-archetype → conform every firm → account-level overlay) is derailed not by a
missing feature but by **a map that disagrees with the territory** — which is what each item closes.

| # | Close-condition | State | This item delivers |
|---|---|---|---|
| 1 | **The estate map matches the territory** | MEASURED — frozen | a DURABLE regen of the comp-estate substrate (not a one-shot) |
| 2 | **The graph is navigable end to end** | measurement-pending | KUZUSPLIT P1 + projection-unification status → close or route |
| 3 | **Records match rulings** | 1 instance GROUNDED + routed | a sweep of refactor-critical governance surfaces for dead-in-ruling/live-in-record gates |
| 4 | **The reporting pipeline is in its own map** | KNOWN (Kimi design §9.3) | estate-report pipeline anchored as a named vertical (or declared residue) |

---

## ITEM 1 — comp-estate substrate: the freeze is ARCHITECTURAL, and a naive regen reproduces it

> ✅ **STATUS: GATE-APPROVED (CTO arch-gate 080129Z @801e5e92a5) → EXECUTION at COO** as part of the
> GO'd build wave (the scheduled-leg wiring rides the same Group-W discipline the build institutionalizes
> — one wiring doctrine, not two). Measure→CVO-co-author→CTO-gate loop CLOSED on the CRO side; execution
> decomp is COO's. The empty-partition rider's ruled answer is folded below.

### What I measured (go-and-see, grounded)

The comp-estate NAMING substrate is `org/modules/graph/estate-coverage-resolver.json`
(`last_review: 2026-06-15`). It is built by `org/modules/graph/gen-estate-resolver.py` from **two
CVO-authored inputs, both point-in-time**:

1. **The census detail** — `gen-estate-resolver.py:17` hard-codes
   `CENSUS = org/tier1_exec/3.0.0_SA_CVO/logs/2026-06-15/estate_census` (reads `pass1_inventory.json`,
   `pass2_gapfamilies.json`, `AUTHORITATIVE_lambda_taxonomy.json`). **Re-running the generator re-reads
   the same June-15 directory and reproduces the frozen vintage** — line 102 even hard-codes
   `"last_review": "2026-06-15"`. This is CTO's exact warning made concrete: *a regen that produces a
   second frozen vintage is the same defect with a newer date.*
2. **The routing manifest** — `estate-coverage-manifest.yaml`, `last_full_review: 2026-06-15` with a
   partial `adjudications_20260730` overlay. Committed + reproducible-from-checkout, but **manually
   reviewed** (last full review 06-15, one incremental pass 07-30). It carries `owning_tool` / `status`
   / `reachability_status` / orphan-classification — **CVO JUDGMENT determinations**
   ("CVO verifies determinations"; an unreviewed thread returns LOUD), **not graph-derivable.**

Tonight's render fix (@38dcbe8d9a) made the aging HONEST (live-key verify + stale banner) but does not
stop it; the resolver crosses its own 14-day `STALE_AFTER_DAYS` in ~3 days (CTO 074227Z).

### The recommendation — CVO-CO-AUTHORED CONTRACT (ruled 075603Z), for CTO's gate

The substrate splits MECE on a mechanical/judgment axis; **CVO ruled both halves + the cadence
(075603Z)** — so this is now a specified contract, not an open question. The durable fix differs per
half, which is why "re-run the generator" is wrong:

- **MECHANICAL half — re-derive from the live graph on a scheduled leg with a floor.**
  `producers` + `frontend_resolution` + the lambda→named_thread enumeration re-derive from the live
  graph (comp-aws/comp-kuzu). `frontend_resolution` carries the F-6 route_class (s3-direct vs
  apigw-lambda) whose apigw mappings need a one-time judgment ENTRY, then re-derive mechanically.
  ⛔ **`served_artifacts` = BARE KEYS + PRODUCER EDGES ONLY, ZERO freshness prose** (CVO, measured).
  The June-15 defect was never the key list — it was FRESHNESS PROSE baked into the rows ("LIVE fresh
  2026-06-15 10:41" on a key that 404s today, the specimen CVO's `--verify-served` fix now renders as
  `[S3 404]`). **If the regen re-bakes any liveness/freshness adjective it rebuilds the exact defect at
  a newer, MORE-credible vintage.** The freshness plane lives at RENDER (the head-object stamps
  @38dcbe8d9a) and NOWHERE in the substrate.
- **JUDGMENT half — CVO's, diff-triggered re-review + a 30-day clock floor.**
  `owning_tool`/`status`/`reachability_status`/orphan+superseded stay CVO-authored. The invalidating
  trigger is the mechanical half moving under a determination: when a scheduled mechanical regen changes
  a thread's producer/served/frontend rows, that thread's judgment rows auto-flag
  `STALE-PENDING-REREVIEW` (loud at render, same stamp discipline), and CVO re-adjudicates on that
  event. Clock FLOOR: 30 days per judgment row (the names' 14d floor doubled — adjudications age slower
  than keys); un-re-reviewed-past-floor surfaces LOUD. The `adjudications_YYYYMMDD` overlay stays CVO's
  authored artifact, now floored. **CVO owns the re-review acts on both triggers.**

**DESIGN RIDER (CVO @4e02646c97, binding on any scheduled leg):** the mechanical regen must RULE
`empty-partition` vs `no-partition` vs `carry-forward` for its sources — CVO's equivalence discriminator
died on an empty weekend partition nobody had ruled on. This ties to the T-1 trading-calendar
discipline: **an empty partition is not absence, and not license to carry forward silently.** The
scheduled leg declares its empty-source behavior explicitly or it reintroduces a silent-freeze class.
> ✅ **RULED (CTO arch-gate 080129Z, concurring with the L2 no-data-day contract):** no partition on
> no-data · loud catch-up on missing-when-expected · carry-forward is serving-tier ONLY. The scheduled
> mechanical leg adopts this verbatim.

**No urgency-borrowing** (CTO 074227Z): if the honest stale flip fires before the regen lands, it is
ACCEPTED as the instrument telling the truth. The fuse is noted, not inflated.

---

## ITEM 2 — graph navigability (measurement-pending; NOT yet grounded)

The graph substrate is closed + certified (GRAPHUNI/GRAPHDEPTH: one head / one marker / drift-safe;
comp-kuzu canonical, Nessie HEAD current). The open edges are **navigation completeness, not
correctness**: KUZUSPLIT **P1 split-commands** sit at CTO's arch-gate (`REGISTRY.md:48`), and the
literal Kuzu-projection unification is a tracked GRAPHUNI follow-on. **Measurement owed before I
recommend:** are these genuinely open, or landed-and-record-stale? I will ground each against live
state before routing a close-or-continue rec. **Marked pending — no recommendation asserted yet.**

## ITEM 3 — records-vs-rulings sweep (1 instance GROUNDED + routed; sweep owed)

The class: a gate **dead-in-ruling** still **live-in-record**, which a future agent re-manufactures by
reading the stale doc — the exact navigability rot a refactor cannot survive.

- **INSTANCE 1 (grounded + routed 073403Z → CTO):** the A.2 NFRA_VELOCITY gate on ADVI_PERFORMANCE.
  Andrew ratified R-4 verbatim (*"Yes this does supersede NFRA_VELOCITY"*, 08-10), yet
  `ADVI_PERFORMANCE_PRD.md:564` A.2 + the ADVI JSON `sequencing` still assert VELOCITY-completes-first
  with no struck amendment. The ruling doc's own line 135 ordered the fix (owner: CTO) and it has not
  landed. **Fix owned by CTO (PRD); routed, not self-edited.**
- **SWEEP owed:** the refactor-critical governance surfaces (ADVI_REFACTOR / 49F / NFRA_VELOCITY /
  ATOM_DECOMP) for the same shape. Measurement-pending.

## ITEM 4 — the estate-report pipeline is not a c3.ii vertical (KNOWN; from Kimi design §9.3)

`comp-estate estate-report` is unrunnable — there is no `estate-report` vertical, so changes to the
pipeline that PRODUCES the daily report fall into `unanchored` residue rather than a named vertical
(OPAL_KIMIPIPELINE design §9.3). **Open question (deliberately not self-answered, roster change =
DECLARED not inferred):** should it be a c3.ii vertical (it is estate infrastructure, not a business
surface) or a named counted residue class. Surfaces to CTO + CVO; not resolved here.

---

## Cross-cutting: tool honesty — CITE, do not re-derive

The measured comp-tool blindnesses (`comp-pipescript deployed` three gaps + one honest limit;
`comp-estate` frozen substrate + 404 platinum key + runner conflation; `comp-iam gaps` action-only,
silence carries no information) are **already measured and routed to CVO by Andrew @c9be07b413**. My
validation **cites CVO's roster and coordinates — it does not re-derive** (COO 073029Z; charter §9,
report the instrument's degeneracy, don't re-measure it).

## Sequencing + how I proceed

1. **Item 1 first** (ORDERED, ~3-day fuse, most concrete navigability win) — CVO coordination on the
   mechanical/judgment split opens now; the full regen-shape rec lands at CTO's gate.
2. **Item 3 sweep** runs in parallel (cheap, record-only) — instance 1 already routed.
3. **Item 2** grounded next; **item 4** surfaced to CTO+CVO as a declared-roster question.
4. `/workflows/atom_decomposition` (Andrew-named) is the instrument for validating that a tool/graph
   seam actually connects and carries the right thing end to end — used on the seams, not on prose.

**Every recommendation lands at CTO (gate) + COO (decomp); nothing is applied from this seat.**
