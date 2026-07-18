# CHECK LIVE, NOT FROZEN — the frozen-reference-drift doctrine

**A binding principle, not history.** Earned across FIVE independent instances in a single session
(2026-07-18), at four different altitudes — mechanism, schema, coverage, and the SDK abstraction itself.
**Ratified:** LD-0314 (0.0.0_AB_MSTR, doctrine-governor), on CTO's 5th-instance flag. Member of the
verification-doctrine family alongside [`CONTROLS_OVER_CARE.md`](CONTROLS_OVER_CARE.md); the general form
of Verification Laws #7 ("well-grounded != FRESHLY grounded") and #8 ("a stale record says something
false with authority").

> # **A thing defined against a FROZEN reference drifts silently. The fix is to track LIVE state on a cadence.**

## The principle

Whenever an artifact is DEFINED-AGAINST a reference that can change — a snapshot, a schema, a coverage
set, a count, an abstraction of a live system — it does not announce when reality moves past it. It keeps
reporting the frozen answer with full authority while the truth quietly diverges. The failure is
**silent** by construction: nothing errors, the number just stops being true.

The fix is never "be careful to keep it updated" (that is care, not a control — see
[`CONTROLS_OVER_CARE.md`](CONTROLS_OVER_CARE.md)). The fix is a **live-cadence check**: ground the APPLIED
state, print the denominator, re-census against the moving reference, on a schedule the drift cannot
outrun.

## The five instances that earned it (2026-07-18)

1. **Materialize emit-vs-applied** — the C3 materialization emit reported 100%; grounding the APPLIED
   live-graph caught a **silent 21% edge loss** (79% pre-fix, an id-space seam) the emit alone would
   have shipped as a clean 100%. DESIRED is a frozen claim; APPLIED is live truth. (Hardened into a
   derive-time auto-classifier invariant so a real id-space regression can never hide inside hand-waved
   "drift.")
2. **Semctl denominator invariant** — a scan that does not print *what its number is OF* silently drifts
   as the population moves; the denominator report (with a LOUD WARN) is the live check.
3. **OWNED_BY census** — a live census of the ownership edges, not a frozen count carried forward.
4. **AC4 `--live-coverage`** — coverage verified against the live surface, not a frozen coverage
   assumption that ages out. **CONCRETE RUN-#1 CATCH (2026-07-18):** the live-cadence lane-2 check
   (sha-verified container==HEAD) caught **2 unmapped edge-types (`IN_SUBNET`, `SENDS_TO`)** that
   lane-1's careful point-verification MISSED — root cause an AXIS error (Verification Law #6):
   lane-1 read comp-kuzu PROJECTED (53 edge-types), the producer emits from the RAW `graph_edges`
   table (55); the 2 raw-only types lived in the gap (CTO source-confirmed: both absent from
   cse_schema.py; cse_emit_graphhead.py:152 scans raw `graph_edges`). A rigorous instrument on the
   WRONG axis survived review; the live-cadence detector on the RIGHT axis caught it first run. This
   instance is not just a principle — it has a scalp.
5. **NFRA_NESTEDABSTRACT (the SDK altitude)** — the GENESIS SDK is *itself* a frozen abstraction of
   Opal's mechanism; as Opal's mechanism evolves, the SDK drifts from it silently. NFRA_NESTEDABSTRACT
   is the live-cadence loop (IDENTIFY the abstraction behind every enhancement → LOG → INCORPORATE +
   a drift-gate) that keeps the abstraction tracking its live source.

Five independent instances across mechanism, schema, coverage, and abstraction — that is a pattern that
binds future behaviour, not a coincidence.

## How it binds

- **Ground APPLIED, never DESIRED**, for any "did it land / is it true now" claim (CLAUDE.md Rule 22a).
- **Print the denominator** of every scan you reason from (Rule 22, "put the control on the RETRIEVAL").
- **An abstraction of a live system needs a live-cadence back to its source**, or it silently ossifies.
- **A frozen reference is not a control** — the live-cadence check against it is.

## The sibling boundary (do not over-apply)

This is NOT license to call every unmoving number a defect. The inverse case is equally binding: a
correctly-frozen value (Friday's T-1 AUM read on a Monday) is HEALTHY, and treating its age as a
staleness finding is the false-alarm this doctrine's cousin (CLAUDE.md NEVER#1, the trading-calendar
default) exists to prevent. The unifying rule: **do not reason from a frozen artifact's age in EITHER
direction — ground the live state and count in the right frame.** Frozen-reference-drift (check live) and
frozen-but-correct (don't false-alarm) are two faces of the same discipline: the answer is always to
GROUND, never to infer from staleness.

## Pointer

Instances captured alongside the semctl invariants (COO @8e96ebf5f); CTO's 5th-instance doctrine flag
(2026-07-18). Ratification: LD-0314.
