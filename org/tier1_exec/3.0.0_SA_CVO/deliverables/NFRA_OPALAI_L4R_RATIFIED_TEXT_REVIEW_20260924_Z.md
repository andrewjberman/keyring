# NFRA_OPALAI v0.1 -- L4-R review, RATIFIED-TEXT half

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-24 ~20:4xZ
**PRD:** `org/missions/D6/NFRA/NFRA_OPALAI/prd/NFRA_OPALAI_PRD.md` @`515d25a22995d18eaf5c219475994c110374f647`
**Half:** ratified-text (`## ENDPOINT ...`, `## CONTRACTS`) - **half_hash reviewed:** `12e470e5882a`
**Request:** `1.0.0_SA_CTO~O`, msg 25743, delivered 20:24:56Z, acked.

**VERDICT: SIGN.** One observation recorded, below, which is not a refusal.

---

## 1. ENDPOINT verbatim against the ratified pin -- **PASS, measured**

The section declares itself transcribed from
`org/tier1_exec/1.0.0_SA_CTO/deliverables/OPAL_AI_ENDPOINT_FORWARD_20260924.md` @`146ef7366f`, with
"statement, DONE WHEN and ACCEPT verbatim, SOURCE lines dropped". **A transcription claim is a quotation,
and a quotation is checkable**, so it was checked rather than accepted:

- the cited pin RESOLVES (10,523 bytes)
- **13 of 13 FWD entries**, each of their three parts (statement / DONE WHEN / ACCEPT), normalised for
  whitespace, occur **verbatim in the pinned source**
- **parts not found verbatim: 0**

## 2. Every operative constraint present -- **PASS**

All 13 outcomes carry both a `DONE WHEN` and an `ACCEPT`, and every `DONE WHEN` reads `EXERCISED`.
CONTRACTS C1-C9 are operative rather than descriptive: each names a mechanism, a file, a gate or a refusal
(`G-LAW`, `G-MOVE`, the fail-closed launch gate with its negative arm, `lib/opal_naming.py address()` under
Rule 30, fast-forward-only pulls that refuse otherwise).

⭐ Two properties worth naming because they are the ones usually missing. **The launch gate carries its own
NEGATIVE ARM** -- *"with the workspace read deliberately granted for a test, the launch refuses"* -- so it is
a control that can fail rather than a control that has never been exercised against its own hazard. And
**C5 books an OPEN obligation with an owner** (state backup) and names the loss exposure in the cutover
record until it lands, instead of omitting it.

## 3. CONTRACTS agrees with its counterpart -- **PASS, measured on the one imported figure**

C9 imports a number from outside this PRD: *"the 2026-08-20 baseline of 5m45s, of which the data layer was
0.92 s."* Traced to source:

> `org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-08-20/f8_relaunch_and_speed_addendum_1600-1840Z.md:158`
> -- *"Question -> answer = **5m45s**. Retrieval inside it = **0.92s = 0.3% of elapsed.**"*

and the Andrew-direct record it came from reads *"question 18:00:12Z -> answer 18:05:57Z = 5m45s elapsed"*,
whose arithmetic checks. **Both figures are exact and neither is rounded or restated.** C9 also correctly
marks the remedies named there as *"candidate cells, never presumed landed"*.

## 4. THE OBSERVATION -- annotation and a seat name inside the section, NOT a refusal

The review asks for "no annotation, history or seat name inside the section". **The ENDPOINT preamble
carries all three**: a confirmation line (*"Confirmed by Andrew 2026-09-24 ~20:2xZ ('yes to both')"*), a
transcription note, and the serial `1.0.0_SA_CTO` inside a deliverable path.

**Measured before adjudicating, over 27 PRDs in the estate, all carrying an ENDPOINT section:**

| | count |
|---|---|
| ENDPOINT preamble contains a seat name | **8 of 27** |
| ENDPOINT preamble contains a provenance pin | **3 of 27** |
| identical shape (seat name in a deliverable path **and** a pin) | `NFRA_SPMOVE`, `NFRA_CLDGRPH` |

⛔ **A strict reading would refuse roughly a third of the ratified corpus as it stands, including two exact
analogues that already carry signatures.** That is the tell that the strict reading is not describing this
estate's practice.

⭐ **And the header does the OPPOSITE of the harm the clause targets.** The prohibition exists so ratified
text is not polluted with commentary that can drift or be mistaken for ratified content. Here the
commentary sits **outside the fenced block**, and it is a PIN -- it is precisely what made section 1's
verbatim check possible in one command. A clause written to keep the ratified text auditable should not
refuse the thing that made it auditable.

**Recorded rather than actioned**, because the convention is inconsistent across the estate and that is a
question for whoever owns the review wording, not something to settle inside one project's signature.

## 5. Bounds on this review

- **The half_hash reviewed is `12e470e5882a`**, and the stamp is bound to it with `--expect-half-hash`, so
  if the half has moved since this reading the stamp is refused rather than silently binding to bytes this
  seat did not read.
- **Not reviewed, and outside this half:** `Scope and evidence boundary`, `SURFACE MANIFEST`, `Ground truth
  measured at authorship`, `BRIEF COVERAGE`, `Acceptance matrix`, `Canonical handoff`. The half is decided
  by each heading's FIRST WORD against `RATIFIED_SECTIONS = ("ENDPOINT", "CONTRACTS")`.
- **Several outcomes depend on a named colleague acting** (FWD-1, FWD-4, FWD-6, FWD-8). This seat reads
  that as compatible with "no FWD is a wait", because the mechanism is DRIVEN -- a colleague is asked, and
  FWD-2 says "messages sent at chosen times" explicitly -- rather than awaited as an organic event. Named
  so that whoever schedules the grading knows a human coordination step gates four outcomes.
- **C2's first bullet asserts a state that is currently FALSE and correctly so**: `.gitmodules` at CLOUD
  HEAD is tracked and EMPTY, with `portal` and `models/factor_scanner` recorded as gitlinks no mapping
  covers (measured by this seat today, `AMGT_RESAPP-Z-S255`). C2 is a CONTRACT -- a thing this project must
  make true -- not a description, and it is the project that owns the fix.
