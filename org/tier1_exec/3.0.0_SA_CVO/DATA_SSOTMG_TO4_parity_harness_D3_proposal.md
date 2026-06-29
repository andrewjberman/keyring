# DATA_SSOTMG TO-4 — Parity-Validation Harness: D3 Per-Surface Tolerance Contract + Harness Design (CVO PROPOSAL)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE
**Owner:** 3.0.0_SA_CVO (PRD §7 TO-4) | **Date:** 2026-06-29 | **RAVC:** 2.0.0_SA_COO · **CC:** 1.0.0_SA_CTO · **coordinate:** 0.4.0_DS_ClientPlatform (canonical-gold paths)
**Status:** PROPOSAL v0.1 — the D3 per-surface tolerance contract is an OPEN Andrew decision (PRD §8 D3: "CVO to propose"). This feeds the Andrew queue. Harness design spec'd; build is the follow-on once base-DS confirms the canonical-gold artifact paths.

## 0. What this gates
THE 49F Schwab-SSOT cutover (PRD §9 hard constraint): no go-live until the full e2e cadence runs IN PARALLEL and parity-validates for SEVERAL DAYS vs BD-served. **The accumulated parallel multi-day PASS streak IS the cutover gate.** The 49F served surface is LIVE ($1.83B book) — parity-proven-first, never-widen, CTO+COO+Andrew-gated. This harness is the load-bearing verification instrument.

## 1. The two sides (grounded)
- **Canonical (Schwab-SSOT, the new side):** `s3://opal-data-bd/canonical/schwab/gold/{table}/date=YYYY-MM-DD/data.parquet` — AES256, parallel/NOT-served. G1-G10 built; G11-G13 HELD. Read S3 **DIRECTLY** (PRD §5: canonical tree is NOT graph-indexed — comp-kuzu/comp-pipescript do not cover it).
- **BD-served (the parity target, the live side):** the `advi-bd` thread, 15 in-scope served surfaces → `platinum/firm/*.json` + AdvisorIntelligence (the production B_/C_/D_ gold set). comp-pipescript covers this side.

## 2. The mapping (canonical Gn -> BD prod equiv -> tolerance class)
Source: `data/canonical/schwab/docs/08_GOLD_SCOPE.md` (the per-table source-mapping, DS-authored, COO-accepted) + `pipescript advi-bd`.

| Gn | canonical table | BD prod equiv | surface kind | **D3 CLASS** |
|---|---|---|---|---|
| G1 | canonical_holdings | B_00 | custodial primitive (holdings/MV) | **A — EXACT-TIE** |
| G3 | canonical_lots | B_02 | custodial primitive (lots/basis) | **A — EXACT-TIE** (Schwab-era overlap only) |
| G6 | canonical_nna | C_01 | derived (NNA) | **B — BAND** |
| G4 | account_performance | C_03 | derived (performance) | **B — BAND** |
| G5 | client_performance | C_02 | derived (performance) | **B — BAND** |
| G9 | firm_composition | D_03 | derived (asset-class %) | **B — BAND** |
| G2 | account_gains | B_03/C_00 | AUA decomposition (do-better) | **C — EXPECTED-DIVERGENCE** |
| G7 | client_tax_liability | C_05 | tax (do-better: actual 1099 vs BD estimate) | **C — EXPECTED-DIVERGENCE** |
| G8 | realized_gains | B_03(realized) | realized (do-better: 6 facts vs 1 path) | **C — EXPECTED-DIVERGENCE** |
| G10 | portal_aggregates | D_00 | firm AUA rollup | **D — SCOPE-MISMATCH** (Schwab-custody subset only) |
| G11-G13 | advisor_attribution/fee/leaderboards | C_07/C_08/D_01 | 49F advisor extension | **N/A this cycle** (HELD; stays thin BD tether per §4) |

## 3. The tolerance classes (the D3 contract — Andrew decides the exact numbers)
**CLASS A — EXACT-TIE (custodial primitives).** Schwab IS the custodian → these must match BD to rounding. Proposed: per-position MV |Δ| <= $1.00 OR <= 1bp of position MV (whichever larger); lot count exact; aggregate holdings MV |Δ| <= 0.01%. ANY break = FAIL (real drift — a custodial primitive can't legitimately diverge once history-scoped). Scope: Schwab-custody accounts, Schwab-era dates only.

**CLASS B — TOLERANCE-BAND (derived metrics).** Legitimately recomputed, small method differences expected. Proposed bands (Andrew to set): performance return |Δ| <= 25 bps per window; NNA |Δ| <= 0.5% of book; composition asset-class share |Δ| <= 1.0 pp. Within band = PASS; outside = FAIL (investigate).

**CLASS C — EXPECTED-DIVERGENCE / DIRECTIONAL (the do-better surfaces).** Canonical is INTENTIONALLY more accurate (actual 1099 vs BD estimate; 6 realized-lot facts vs 1 reconstructed path; sb-grounded AUA decomp vs the 90-day patch). A raw value-difference here is NOT a failure — failing it would reject a known improvement. Verdict logic instead:
  - (a) both sides PRESENT + FRESH (vintage gate), AND
  - (b) divergence within an EXPLAINED envelope (proposed: canonical within +/- 10% of BD at the aggregate, same sign), AND
  - (c) **drift-on-the-delta**: the canonical-vs-BD gap is STABLE day-over-day (no NEW unexplained movement vs the prior clean day). A surface passes Class C when the *relationship* is stable, not when the values tie.
  A sudden change in the gap = FAIL (something moved that shouldn't have), even though a constant gap is expected.
  **WHY drift-on-delta is safe (CTO arch-gate 2026-06-29 — DOCUMENT this assumption):** the two sides have INDEPENDENT UPSTREAMS (canonical = Schwab raw; BD = BD DataMining). So (i) a regression on EITHER side moves the delta → sudden gap-change → FAIL [caught]; (ii) a common-mode market move shifts both LEVELS but preserves the DELTA → PASS [correctly tolerated — the exact reason drift-on-delta beats level-tolerance]. **This safety rests on upstream independence** — a future surface sharing an upstream on both sides could hide a common-mode regression; revisit per-surface if that ever arises. KEEP BOTH checks: the **envelope** catches a mis-MAPPED surface (a stable but HUGE gap = wrong surface mapping), the **delta-stability** catches the regression. The delta-drift threshold NUMBER → Andrew's D3 queue; the MECHANIC is CTO-gated = approved.

**CLASS D — SCOPE-MISMATCH (structural, must not false-fail).** Canonical = Schwab-custody only ($1.63B); BD-served firm AUA = the firm-wide union (BD+Schwab+held-away, $1.83B+). Comparing firm totals would ALWAYS "fail." Contract: filter the **BD side** to the Schwab-custody subset, then exact-tie within Class-A tolerance on that subset; the held-away/Fidelity remainder is explicitly OUT of parity scope (covered by the residual BD bridge per §2/§4, bounded by the DERISK-2 census). **The filter is BD-SIDE ONLY** (base-DS ground-truth 2026-06-29): the entire canonical tree is Schwab-custody BY CONSTRUCTION (it reads `opal-data-schwab` raw only), so every canonical row already IS Schwab-custody — no canonical-side filter, no filter field needed there; the scope-match is achieved by narrowing BD to the Schwab-custodied accounts before the compare. **Two CTO arch-gates (2026-06-29):** **GATE D.1** — the subset-filter MUST reuse DERISK-2's account-level custody classification as the SINGLE source of truth for "which accounts are Schwab-custody"; do NOT invent a second custody field (one classification, two consumers: census bounds the bridge, parity filters the compare — converges cleanly). **GATE D.2** — the verdict MUST EXPLICITLY EMIT the excluded held-away remainder ($, reconciled to the DERISK-2 census) alongside the Schwab-subset parity, so the ~$200M exclusion is a TRANSPARENT census-bounded KNOWN-exclusion, never a silent drop. Firm-wide $1.83B reconstructs in the verdict as: Schwab-subset (parity-proven ~$1.63B) + held-away (known-excluded, census-bounded) — both visible.

## 4. Two cross-cutting gates (every surface, every class)
1. **VINTAGE GATE (both sides) — the false-PASS killer.** comp-freshness BOTH the canonical side AND the bd-served side before any verdict counts. A frozen-canonical matching a frozen-BD is a FALSE PASS (PRD §10 mtime-fresh/content-stale). If either side is STALE for the compared date → verdict = **STALE-SKIP** (neither PASS nor FAIL; does NOT advance the clean-streak, does NOT reset it; surfaced loud). The streak only advances on a day where both sides are fresh AND all surfaces PASS.
2. **CONTENT not mtime.** Compare actual values (the §3 classes), never partition mtime. A gold table that ran on stale silver looks fresh but is content-stale — the value comparison + the canonical-side vintage gate catch it.

## 5. Daily verdict + the clean-streak counter (the gate mechanic)
- Per surface per day: one of **PASS / FAIL / EXPECTED-DIVERGENCE-OK / STALE-SKIP**.
- Day verdict = **CLEAN** iff every in-scope surface is PASS or EXPECTED-DIVERGENCE-OK AND no surface is STALE-SKIP on a date that should be fresh. Any FAIL = day NOT-CLEAN.
- **Clean-streak counter:** consecutive CLEAN days. A FAIL **resets to 0** (a real divergence breaks the proof). A STALE-SKIP **holds** (does not advance, does not reset — but is escalated, because a stalled cadence is its own problem). The streak value + the per-surface history is the artifact handed to the P4 never-widen gate.
- **Andrew decision (D3-adjacent):** what N = "several days"? Propose **N = 5 consecutive CLEAN trading days** as the default cutover threshold (Andrew to confirm/raise).

## 6. Harness design (build spec)
- **Form (CTO arch-gate 2026-06-29 — LANE RULED):** a GENERAL comp-tool **`comp-parity` in `.tools/`** (comp-which-discoverable, NFRA_COMPRAIL arch-gated like the other comp-tools), parameterized by a per-firm/per-cutover **CONFIG**; the **49f config** (surface map + per-surface class assignment + envelopes) lives co-located at **`data/canonical/schwab/parity/`** (the CONFIG, not the engine). Rationale: parity-prove-before-cutover is a GENERAL pattern — it recurs for every firm cutover (cot/inf per the canonical archetype) AND every never-widen parallel-build validation (DATA_ANALYTICS A4 firm-by-firm, future portal parity). Build the reusable never-widen-validation INSTRUMENT once (engine on the rail), plug firms in via config — not a 49f-only harness rebuilt 3×; makes never-widen-parity a first-class queryable capability. Read-only; reads canonical S3 directly + comp-pipescript/comp-freshness for the BD side; emits a per-surface verdict JSON + a running streak file + a human table.
- **Inputs:** canonical = direct S3 read of `canonical/schwab/gold/{table}/...` (base-DS CONFIRMED 2026-06-29). **PARTITION KEY IS NOT UNIFORM — the comparator MUST special-case it:** `date=YYYY-MM-DD/data.parquet` for 9 of 10 (G1/G3/G4/G5/G6/G7/G8/G9/G10, the date = the orchestrator-pinned `--asof t1`), but **`period={t0}_{t1}/data.parquet` for account_gains (G2) ONLY** (window-partitioned). A naive `date=` glob misses G2 entirely → per-surface partition-key resolver, not a global assumption. BD = the served `advi-bd` artifact per surface (Gn↔served-key map deferred to base-DS's next pass — REQUESTED).
- **Per-surface:** load both, align grain/keys, apply the surface's D3 class test, emit verdict + the |Δ| evidence.
- **KEYING ASSERTION (base-DS flag):** account_id is 10-digit zero-padded STRING on canonical (enforced at silver via `coerce_padded_ids`, carried through gold). BD-served has had **Int64-vs-string drift historically** → the comparator MUST ASSERT both sides are padded-string and coerce/FAIL-LOUD on a type mismatch BEFORE the join — a silent Int64-vs-string mis-join would produce a phantom 100%-divergence (false FAIL) or worse a phantom tie. The keying assertion is a hard pre-compare gate.
- **Scope:** Schwab-era dates on both; Schwab-custody filter applied to the **BD side only** (canonical is all-Schwab-custody by construction — base-DS).
- **Vintage:** comp-freshness on both sides first; STALE-SKIP short-circuits the value compare.
- **Output:** `parity/date=D/verdict.json` (per-surface) + `parity/streak.json` (the counter) + a printed table. NEVER writes to served paths.
- **Cadence:** runs daily AFTER both cadences land (canonical gold + bd gold). Sequencing: spec+comparator NOW; it RUNS once P2 (G3-G10 wired, DS TO-2) + P1 (DERISK-1 Schwab ingest) make the canonical cadence parallel-live.

## 7. Open items / asks
- **base-DS (0.4.0):** canonical paths + keying CONFIRMED 2026-06-29 (folded above: non-uniform partition key incl. G2 `period=`, padded-string keying + the BD Int64-drift assertion, canonical-all-Schwab-custody so the Class-D filter is BD-side-only). REMAINING DS deliverable = the Gn↔BD-served-artifact map (the exact `platinum/firm/*.json` key per surface — DS ground-confirming, not asserting; coming next pass). Until it lands the BD-side surface map is the one un-grounded input.
- **CTO:** RULED 2026-06-29 (all folded above) — lane = general `comp-parity` engine (.tools/) + co-located 49f config (data/canonical/schwab/parity/); Class-C drift-on-delta APPROVED (independent-upstreams safety basis documented, keep both checks); Class-D APPROVED with GATE D.1 (reuse DERISK-2 census custody, single source) + GATE D.2 (emit held-away remainder transparently). Will re-gate only if the build surfaces something beyond this design.
- **DERISK-2 dependency (new, from GATE D.1):** the Class-D BD-side filter consumes DS's DERISK-2 census account-level custody partition. Coordinate so the census custody field is the single shared classification (no second custody field).
- **Andrew (the D3 queue):** the exact tolerance numbers (Class A/B bands), the Class-C explained-envelope %, and N (= the clean-streak threshold; proposed 5). The CLASSES + the gate mechanic are the CVO proposal; the NUMBERS are the Andrew decision.

## 8. Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| pipescript advi-bd | parity-target inventory | PASS | 15 in-scope served surfaces, S3 served keys per surface |
| (read) 08_GOLD_SCOPE.md | canonical Gn -> BD prod-equiv map | PASS | the backbone of the §2 mapping |
| comp-freshness | (design dependency) both-side vintage gate | N/A-design | the §4 false-PASS killer; both sides must be fresh for a verdict to count |

— 3.0.0_SA_CVO
