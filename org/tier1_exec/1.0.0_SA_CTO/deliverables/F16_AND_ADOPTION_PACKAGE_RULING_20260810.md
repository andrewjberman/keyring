# METHOD-OWNER RULING — F-16 filed with remedy; adoption package adjudicated (E1/E2/E3 ADOPT, 06 base STAGED-NOT-ADOPTED)

**Seat:** `1.0.0_SA_CTO~A` (ATOM_DECOMP method owner) · **Date:** 2026-08-10 ~18:0xZ
**Authorization:** Andrew-direct this session (*"proceed with the queued items while you wait on CRO"*); CRO routing `20260810T172739Z` (F-16 queue) + `20260807T063652Z`/`071616Z` (adoption package, routed for this seat's decision, "decline any part freely"); CRO sequencing ACK `20260810T175225Z`.
**Landing lane:** every corpus edit below lands via `4.0.0_SA_CRO` (this seat is not enumerated in the ATOM_DECOMP owned-paths lane). Drafted deltas are exact; deviations come back to me pre-landing.

---

## PART 1 — F-16: FILED, severity LOW-MEDIUM, remedy drafted

**The defect (CRO state doc 2026-08-07 §6, previously unfiled):** `02_ADOPTION_AND_EVALUATION.md` §3 (":36") lists nine scoring dimensions with no scale, no threshold, no pass bar. *"Score X"* without a bar is unfalsifiable — an evaluation suite whose scoring instruction cannot fail — while §4's acceptance targets, one paragraph down, ARE crisp.

**The remedy is NOT to manufacture nine thresholds.** The corpus has never run its own stage 1 (§1.1: one manual read-only audit — unexecuted; audit assessment: "authored-not-executed" is the corpus's defect signature). Authored thresholds with no executed run behind them would be bars derived from nothing — the same signature, deepened. The corpus already contains its own pass bar: **§4's eight acceptance targets plus gates G0–G7 are crisp and falsifiable.** Promote them to being THE bar; demote the nine dimensions to the measurement record.

**DRAFTED DELTA — `02_ADOPTION_AND_EVALUATION.md:36`, replace the single "Score ..." sentence with:**

> Measure denominator closure, edge recall, contradiction detection, claim reproducibility, consumer-contract preservation, work-package atomicity, rollback quality, cleanup completeness, and false absence assertions — each reported with its instrument and denominator per the claim contract. The pass bar is §4 plus gates G0–G7 on every scenario: the nine dimensions are the measurement record, not the verdict. Numeric thresholds for the scalar dimensions are deliberately unset until the first §1 stage-1 run provides a measured baseline — an authored threshold with no executed run behind it is a bar derived from nothing.

Nothing new is manufactured; the crisp material that already exists becomes the bar, and the deferral is stated in-band so it reads as a decision, not a gap.

---

## PART 2 — Adoption package section 2: E1 ADOPT · E2 ADOPT · E3 ADOPT

Rung-2 duplication checks run before adoption (comp-find over the skill package): "quoted" 0 hits; "optional field" 0 hits; "grain" appears only as the DATA-modeling grain of artifacts (`SKILL.md:45`, `evidence-model.md:26/37/42` etc.) — a DIFFERENT concept from E3's grain-of-a-count, and the drafted wording below disambiguates deliberately ("count grain") to avoid overloading a term the corpus already uses (Rule-24 intent-coherence).

### E1 (denominator attribution survives the quote) + E3 (class-vs-instance grain) — ADOPTED as Rule 5 surgery, not new rules

Both are the claim contract's own intent, sharpened; a new rule for either would split one intent across two rules (the F-2 class, one layer down). Twice-measured each (E1: 961/961 quoted as population + 4,896 quoted under another probe's denominator; E3: ~13 class vs 1,255 instance under one number, "14" pinned in a served doc).

**DRAFTED DELTA — `SKILL.md:16` Rule 5, replace with:**

> 5. Give every claim a source, locator, measurement time, scope, count grain (class or instance), denominator, and limitation. A quoted figure keeps the instrument that produced it.

(Two-sentence rules are in-voice: Rule 4 already is one.)

**DRAFTED DELTA — `evidence-model.md` claim contract:** extend the `scope and denominator` row's meaning to "What was tested, the full population claimed, and the count grain (class or instance)"; append one sentence after the table:

> A figure quoted from another document or probe carries the instrument and denominator it was produced with; a number that cannot be re-derived from its cited instrument is not a figure.

### E2 (declaration-shape discriminator) — ADOPTED as new Rule 13; gate question stays OPEN

Genuinely new (zero corpus coverage), measured live (declaration exact at 482; the declared guard present on 23 of 482 — the count stayed true while the field went unpopulated), and catches a failure no existing rule reaches: a declaration over an OPTIONAL field is unfalsifiable in the direction that matters, and Rules 3/10 both pass it.

**DRAFTED DELTA — `SKILL.md`, append after Rule 12:**

> 13. Never accept a declaration naming an optional field on its count alone — the count stays true while the field goes unpopulated; measure population.

**The mechanization/gate question is DELIBERATELY OPEN, per CRO's own withdrawn-gate precedent:** it is settled by measuring the method's own declaration surface, and nobody has measured it. No gate is commissioned by this ruling.

### E4 — nothing to do (withdrawn by CRO; already landed in CLAUDE.md @4ff692a9d0). Section 1 (four independent corroborations) was ACCEPTED as evidence on 2026-08-10 ~1731Z.

---

## PART 3 — Adoption package section 3: the `06` PROJECT COHERENCE BASE — STAGED, NOT ADOPTED

**Direction ACCEPTED; adoption of the artifact WITHHELD pending two named measurements.** Andrew asked for exactly this capability class at engagement opening (the verbatim in `06`'s banner), so outright decline is wrong; but the evidence bounds are CRO's own, honestly stated, and they are not adoption-grade yet:

- Applied 3x, only 2 independent of the author; **the mid-flight-driver class is untested** (CRO's own named residual).
- **Two structural blind regions** (no-vertical entry; disconnected substrate), in both of which a traversal returns zero and **zero is indistinguishable from "nothing there"** — the size of the excluded set is `SIZE UNKNOWN — narrower than 37% — exact method named — unrun`.
- The base catches **1 of 5** measured error classes (position/duplication, never instrument honesty) — a ratified ceiling, not fixable by rows.

**The two gates on THIS SEAT'S adoption decision** (conditions on my decision, not holds on anyone's work):

- **G-a — the entry-probe census:** attempt `comp-estate <project>` per active project (81 at last count) and count refusals. This is the exact method `06` v0.4 already names as available-and-unrun; it converts the blind-region cost from an order-of-magnitude guess into a figure. (~few hours; CRO to run or route as they see fit — the E2 lesson applies: that measurement settles it, not argument.)
- **G-b — one independent application on a project with a driver actively mid-flight** — the named untested class, and the class where an intake matrix is most likely to be either useless or disruptive.

**Bound at adoption (if the gates read acceptable), pre-committed now so they are not negotiated later:**
1. The base goes **IN the charter** (Layer A ontological completion), not beside it — a second intake artifact beside the charter is a two-artifact fork of one intent, the F-2 shape one layer up. (Resolves `06` §5 open question 1.)
2. It ships **WITH its tool invocation** — never as a hand-fill document (the independent tester's finding: the structural half is a tool output; hand-filling produces a base whose valuable half is empty or guessed).
3. **Empty cells declare which of the three they are** (correctly-empty | unreachable | not-looked-at) — the v0.4 requirement, which must be EXERCISED at least once before it is trusted (it is currently an untested fix).
4. **A structural-row zero carries its mechanism** — Rule 4 applied to the base's own instrument: a zero from a blind region is not knowledge.
5. The base **scales with the charter's existing depth classification** — no new classification axis (resolves open question 2; Rule-24 hygiene + Build Ladder rung 2).

**Also ruled:**
- `06` §3b (instrument self-contradiction cell): stays OPEN. Correctly refused as a same-night patch; it is the instrument-honesty ceiling, which is outside the tuple by construction.
- `06` §5 open question 4 (NFRA_PYFIELD consumer): **NOT declared.** A project can legitimately declare D1 at artifact grain; this ruling does not manufacture a consumer to resolve someone else's build question. NFRA_PYFIELD Q1's DEFER stands undisturbed by this seat.

---

## Routing

- Parts 1–2 drafted deltas → `4.0.0_SA_CRO` to land in the ATOM_DECOMP lane, same review-then-land shape as F-2 (deviation from the drafted text comes back pre-landing; RAVC-4 validation on the landed diff at this seat).
- Part 3 → no corpus edit now beyond CRO recording the staged status on `06` if they wish; G-a/G-b results come back to this seat, which then re-opens the adoption decision.
- WS-C3's three orphaned vocabulary items (CRO context note `20260810T175225Z`): **CTO BASE territory, explicitly excluded from this ruling** — not inherited by adjacency.
- All of this is loudly surfaced to Andrew this session and cheaply reversible; nothing below builds on it yet.
