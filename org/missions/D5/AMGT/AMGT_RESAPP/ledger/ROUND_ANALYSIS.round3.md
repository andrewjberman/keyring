# AMGT_RESAPP -- ROUND 3 ANALYSIS (L10, 1.0.0_SA_CTO~Z) -- the corrective round (informal "2b")

**archetype:** SCRIBE (ledger) · **written by** `1.0.0_SA_CTO~Z` · **2026-09-11**

| | |
|---|---|
| **Answers** | the L10 slug `surprise-channel/remediations/REMEDIATION_v3.md` @`13ae38f3f89b` from `3.0.0_SA_CVO~Z`; ADJUDICATION_v3 + CVO evidence JSON ride the same pin; source/review pin `bb654d2d4f` |
| **Round mapping** | canonical ROUND 3 (v3) = the corrective continuation of round 2 (informal "2b"), per this seat's carrier ruling (msg 21335). rb- cell ids unchanged |
| **Graded against** | each round-2-routed defect's fix landing (a corrective round), not an FWD realization -- surfaces remain DESIGN_SPEC-gated |
| **Routes to** | `2.0.0_SA_COO~ZZZ` (round 4 recut of the consumer-wiring completion: C-S16/C-S19/C-S20) |

---

## 1. THE VERDICT: 4 of 5 corrective fixes LANDED; the one FAIL is the consumer-wiring, and it FAILED for the right reason

Round 3 fixed round 2's three failed fixes + the two new source findings. **4 PASS / 1 FAIL.** 26 orders
terminal, 26/26 proof instances VALID, 23 tests pass, 29 investigations dispositioned, 0 channel defects.
**0 FWD newly REALIZED** -- unchanged; this is pre-surface correctness, and no surface is built (still
gated on Andrew's DESIGN_SPEC).

| cell | fixes round-2 finding | grade | disposition |
|---|---|---|---|
| rb-10 | C-S12 checkface salience | **PASS** | C-S12 DISARMED / REMEDIATED |
| rb-12 | C-S13 identity decision note (34 MEASURED + up to 15 INFERRED) | **PASS** | C-S13 REMEDIATED |
| rb-15 | C-S14 impostor predicate (now AND, identity-bound) | **PASS** | C-S14 REMEDIATED; the 16 well-typed combos all correct; W5-S2 test-scope sweep narrowed to 3 files, CLOSED |
| rb-1 | C-S15 fiscal direction (UNRESOLVED when no on-or-before price) | **PASS** | C-S15 closed |
| rb-2 | C-S16 consumer-wiring (correct join reaches the served consumer) | ⛔ **FAIL** | C-S16 stays OPEN; two new mechanisms found (s.3) |

So the round-2 defect-fixes are now LANDED (C-S12/C-S13/C-S14/C-S15 all closed/remediated), and the
impostor predicate is genuinely fixed (executes AND, binds to company identity, all 16 combinations
correct) -- the security-adjacent fix I flagged for a must-fail control is now real.

## 2. THE ONE FAIL, AND WHY IT IS THE GENERALIZATION WORKING (not a regression)

**rb-2 / C-S16 -- the corrected fiscal price does not flow to the served consumer end-to-end.** The
POSITIVE arm works: the live 30-row sample and a scratch PDF render the corrected **132.23**. But the
consumer-wiring-as-its-OWN-acceptance-criterion (the tick-2 generalization I folded into rb-2) did exactly
what it was added to do -- it refused to certify "connected end-to-end" on a passing sample alone, and
found two concrete failures a sample-only check passes:

- ⛔ **C-S19 (BLOCKING, ARMED) -- a silent revert to the stale price.** `render_print.py`'s corrected-price
  overlay includes only rows whose price is not None and skips missing years; so an UNRESOLVED corrected
  fiscal row (future-only boundary: period_end 2025-03-31 with only a 2025-04-02 price -> rb-1 correctly
  returns None -> loader returns `{}`) makes the consumer **silently retain the old calendar-year 146.58
  with NO unresolved marker.** A stale figure served as trusted, at exactly the boundary the fiscal fix
  exists for. ⭐ Synthetic control -- NOT a claim that a currently-landed row is missing its price; the
  point is the MECHANISM would serve the stale value if a row ever resolves UNRESOLVED.
- **C-S20 (OBSERVATION, ARMED) -- the corrected derivation vintage is lost.** The consumer substitutes the
  price OBSERVATION DATE for the vintage and drops the corrected artifact's derivation key
  (`derived/model_block_fye/BABA_US_Equity/<ts>/...`); `render_figure_line` hardcodes "Bloomberg" and does
  not emit `fig.source`. So the served provenance cannot distinguish two derived vintages sharing an
  observation date -- a Rule-22 GRAIN gap, and within rb-2's own named-vintage acceptance.

This is the FWD-3/FWD-10 discipline biting correctly: a corrected number that silently reverts to its
stale predecessor, unmarked, is exactly what "a failed check is visible as failed" and "defend every
number" exist to forbid. rb-2 held the line.

## 3. ROUTING -- round 4 (v4) recut, still NOT surface work

**Round 4 (the NEXT canonical issuance, v4) -- `2.0.0_SA_COO~ZZZ`, ONE issuance:** complete the
consumer-wiring so C-S16 closes -- (i) C-S19: preserve explicit UNRESOLVED corrected rows, distinguish
missing-lane/year from resolved data, and MARK-or-REFUSE a fiscal price with no valid corrected evidence
(never silently keep the old calendar price); test the named consumer from a full corrected-join `None`
straight through to the rendered value. (ii) C-S20: carry observation date and derivation identity as
DISTINCT fields; retain the corrected artifact key through the consumer + its provenance; a test that
distinguishes two derived vintages at the same observation date. Owner per the rows: COO~ZZZ routes to the
consumer owner.

⛔ **ROUND 4 IS STILL PRE-SURFACE CORRECTNESS, not the surface exercise.** Per this seat's carrier ruling,
the carrier numbers by issuance sequence; this corrective continuation is simply the next issuance = round
4. The DESIGN_SPEC-gated SURFACE EXERCISE is a SEPARATE, LATER issuance (v5+ if it follows round 4),
assigned its number when Andrew approves the DESIGN_SPEC and it is cut -- NOT pinned to v4.

## 4. FWD STATE + WHAT CARRIES

No FWD grade changes -- all 14 NOT_REALIZED (every surface needs an EXERCISED served page; none built).
Round 3 landed the round-2 correctness fixes and left ONE end-to-end wiring gap (C-S16), now reduced to
two concrete, testable mechanisms (C-S19/C-S20) for round 4. Nothing invalidates the closed cells
(AMGT-s-3/s-5 still stand -- see the tick-6 adjudication; the corrected value flows through rb-2/round 4).
Round 3's grades and the DISARMED C-S12/13/14/15 are historical and stand.

**Round 3 CVO stamps:** L8/L9/L10.r3 (canonical mapping). Surface exercise: Andrew-gated, v5+.

**Push state:** LOCAL at write time. `0.0.0_AB_MSTR~Z` pushes.
