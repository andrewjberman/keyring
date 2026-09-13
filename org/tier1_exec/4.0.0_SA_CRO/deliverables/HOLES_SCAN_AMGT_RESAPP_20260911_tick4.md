# Holes Scan — AMGT_RESAPP, Tick 4 (20260911 ~11:1xZ)

**Author:** 4.0.0_SA_CRO~Z · **For:** 1.0.0_SA_CTO~Z to fold in
**Builds on:** tick 3 (`dfb9eaf3e5`). **Numbering note:** what tick 3 called "round-2b" is now the
canonical **round 3** (carrier ruling `@21336`); the newest cells below are **round 4**. Adopting
project numbering from here so this scan's rounds match the ledger's.

---

## 1. Round 3 closed 4 of 5 — and the 5th caught something worth real weight

rb-10/12/15/1 all LANDED (C-S12/13/14/15 disarmed/remediated) — the path-grant fix from tick 3
worked. **rb-2 (consumer-wiring, C-S16) still FAILED, and this is the second real catch in a row from
the tick-2 "consumer-wiring as its own AC" recommendation — worth stating plainly, since a mechanism
that keeps finding real defects rather than one-off is the actual proof it was worth adding:**

**C-S19 (BLOCKING) — a silent stale-data fallback, not a rendering bug.** With the path grant fixed,
the consumer now renders the CORRECTED 132.23 for a resolved row. But when the corrected fiscal row
is **UNRESOLVED**, the consumer silently keeps serving the OLD calendar-year 146.58 — **unmarked, as
if trusted.** This is exactly the failure mode the whole provenance/check-face system (S3/S10/S11)
exists to prevent — a wrong number shipping with no signal that it's wrong — except this instance sat
in the price-overlay consumer itself, outside S10's PASS/REFUSE/PROVISIONAL machinery.

**Worth raising as an architecture question, not just noting the fix:** round 4 (below) fixes this as
a bespoke rule inside `load_corrected_price_overlay` — "mark or refuse, never silently keep the old
value." **Should this instead be an S11 qualification rule** (the existing one-rule-per-class
mechanism that already drives S10's badges) so ANY consumer with an unresolved corrected value gets
the SAME REFUSE/PROVISIONAL treatment automatically, rather than each consumer needing its own
hand-written "don't silently fall back" logic? Flagging this now, before round 4 lands a second
bespoke instance of a pattern S11 was built to generalize.

**C-S20 (OBSERVATION, lower severity, chained after C-S19)** — the observation-date field overwrites
the derived-vintage field, so the corrected derivation's own identity is lost; `render_figure_line`
also hardcodes "Bloomberg" instead of reading the figure's actual source. A provenance-accuracy defect,
not a served-wrong-number one.

**Round 4 status:** two cells (`AMGT-rc-19`, `AMGT-rc-20`) decomposed (`06d72ff757`), chained (rc-20
depends on rc-19, same two files), neither DESIGN_SPEC-gated. COO~ZZZ's issuance is the next act.

---

## 2. AMGT-s-3/s-5 — confirmed still standing, no new information this tick

No change since the CTO's direct measurement last tick; not re-litigating it here.

---

## 3. Bucket/pipeline infra — unchanged, confirmed not assumed

No new AMGT-scoped Terraform this tick. Correct sequencing — round 4 is still pre-surface
correctness work; round 5+ is where DESIGN_SPEC-gated surface cells (and the backend gaps from tick
1's scan) actually become buildable.

## 4. No new staleness against an Andrew ruling this tick
