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

**CLASS D — SCOPE-MISMATCH (structural, must not false-fail).** Canonical = Schwab-custody only ($1.63B); BD-served firm AUA = the firm-wide union (BD+Schwab+held-away, $1.83B+). Comparing firm totals would ALWAYS "fail." Contract: compare only the **Schwab-custody subset** of the BD surface (filter BD to Schwab-custodied accounts), exact-tie within Class-A tolerance on that subset; the held-away/Fidelity remainder is explicitly OUT of parity scope (covered by the residual BD bridge per §2/§4, bounded by the DERISK-2 census).

## 4. Two cross-cutting gates (every surface, every class)
1. **VINTAGE GATE (both sides) — the false-PASS killer.** comp-freshness BOTH the canonical side AND the bd-served side before any verdict counts. A frozen-canonical matching a frozen-BD is a FALSE PASS (PRD §10 mtime-fresh/content-stale). If either side is STALE for the compared date → verdict = **STALE-SKIP** (neither PASS nor FAIL; does NOT advance the clean-streak, does NOT reset it; surfaced loud). The streak only advances on a day where both sides are fresh AND all surfaces PASS.
2. **CONTENT not mtime.** Compare actual values (the §3 classes), never partition mtime. A gold table that ran on stale silver looks fresh but is content-stale — the value comparison + the canonical-side vintage gate catch it.

## 5. Daily verdict + the clean-streak counter (the gate mechanic)
- Per surface per day: one of **PASS / FAIL / EXPECTED-DIVERGENCE-OK / STALE-SKIP**.
- Day verdict = **CLEAN** iff every in-scope surface is PASS or EXPECTED-DIVERGENCE-OK AND no surface is STALE-SKIP on a date that should be fresh. Any FAIL = day NOT-CLEAN.
- **Clean-streak counter:** consecutive CLEAN days. A FAIL **resets to 0** (a real divergence breaks the proof). A STALE-SKIP **holds** (does not advance, does not reset — but is escalated, because a stalled cadence is its own problem). The streak value + the per-surface history is the artifact handed to the P4 never-widen gate.
- **Andrew decision (D3-adjacent):** what N = "several days"? Propose **N = 5 consecutive CLEAN trading days** as the default cutover threshold (Andrew to confirm/raise).

## 6. Harness design (build spec)
- **Form:** a daily script (candidate home `.tools/` as `comp-parity` OR `data/canonical/schwab/parity/` — CTO to rule the lane; it reads canonical S3 directly + comp-pipescript/comp-freshness for the BD side). Read-only; emits a per-surface verdict JSON + a running streak file + a human table.
- **Inputs:** canonical = direct S3 read of `canonical/schwab/gold/{table}/date=D/`; BD = the served `advi-bd` artifact per surface (paths to be confirmed by base-DS — REQUESTED).
- **Per-surface:** load both, align grain/keys (account_id 10-digit zero-padded STRING per §4), scope to Schwab-custody + Schwab-era, apply the surface's D3 class test, emit verdict + the |Δ| evidence.
- **Vintage:** comp-freshness on both sides first; STALE-SKIP short-circuits the value compare.
- **Output:** `parity/date=D/verdict.json` (per-surface) + `parity/streak.json` (the counter) + a printed table. NEVER writes to served paths.
- **Cadence:** runs daily AFTER both cadences land (canonical gold + bd gold). Sequencing: spec+comparator NOW; it RUNS once P2 (G3-G10 wired, DS TO-2) + P1 (DERISK-1 Schwab ingest) make the canonical cadence parallel-live.

## 7. Open items / asks
- **base-DS (0.4.0):** confirm the canonical-gold S3 artifact paths + the BD-served surface artifact paths per Gn (the exact `platinum/firm` / served keys), so the comparator's surface map is ground-truthed not assumed. REQUESTED via MCP.
- **CTO:** rule the harness lane/home (.tools comp-parity vs data/canonical/schwab/parity) + arch-gate the Class definitions (esp. Class C drift-on-delta + Class D Schwab-custody subset filter).
- **Andrew (the D3 queue):** the exact tolerance numbers (Class A/B bands), the Class-C explained-envelope %, and N (= the clean-streak threshold; proposed 5). The CLASSES + the gate mechanic are the CVO proposal; the NUMBERS are the Andrew decision.

## 8. Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| pipescript advi-bd | parity-target inventory | PASS | 15 in-scope served surfaces, S3 served keys per surface |
| (read) 08_GOLD_SCOPE.md | canonical Gn -> BD prod-equiv map | PASS | the backbone of the §2 mapping |
| comp-freshness | (design dependency) both-side vintage gate | N/A-design | the §4 false-PASS killer; both sides must be fresh for a verdict to count |

— 3.0.0_SA_CVO
