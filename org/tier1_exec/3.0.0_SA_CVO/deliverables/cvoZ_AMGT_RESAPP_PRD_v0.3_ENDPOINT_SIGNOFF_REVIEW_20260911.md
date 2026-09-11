# AMGT_RESAPP PRD v0.3 — L4-R ENDPOINT SIGN-OFF REVIEW

**Reviewer:** `3.0.0_SA_CVO~Z` · 2026-09-11 ~06:00Z · **Verdict: SIGNED**
**Artifact:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` v0.3, pin `@f68818832b`
**Author:** `1.0.0_SA_CTO~Z` (L4/L2) · **Directive:** D5 (site Z) · **Blocking:** the round-2 issuance (5 orders held by `2.0.0_SA_COO~ZZZ`)
**Scope:** the ENDPOINT section only (Rule 27 L4-R: *"`3.0.0_SA_CVO` signs the ENDPOINT section against the ratified pins"*). The CRO's coverage-map half is `4.0.0_SA_CRO~Z`'s and is not signed here.

---

## WHY THIS IS LATE, STATED FIRST BECAUSE IT IS MINE

⛔ **THIS SIGN-OFF WAS OWED AND I DID NOT SEE IT UNTIL ANDREW ASKED.** Round 1's sixteen orders were
cut BEFORE the L4-R gate reached this fabric (spine v3.14, Andrew-direct 2026-09-10 ~21:2xZ, arriving
in the overnight CLOUD merge), so nothing was owed while I ran L8/L9/L10 on round 1 — that part is a
timing consequence of a mid-project law change, exactly as `2.0.0_SA_COO~ZZZ` said (msg 21212).

**What is NOT excused by the timing:** I watched the round-2 recut being staged, mapped all five orders
to my own round-1 findings in a report, and still did not ask whether the recut faced a gate my seat
holds. The COO measured it and blocked itself correctly, refusing the `# pipeline-override` on the
ground that the gap is real. Andrew asked the question at the same time. **I should have reached it
from my own slug: a recut is a new issuance, and L4-R binds every issuance after it landed.**

## VERDICT: SIGNED. The round-2 issuance is not held by this seat any longer.

### LIMB 1 — FIDELITY TO THE RATIFIED PINS: VERIFIED, 14 of 14

The section's own claim is that the outcomes are *"reproduced VERBATIM from the L2 endpoint
`@3bc8f5f2c4` and are NOT re-authored here."* Checked card by card against that commit's own artifact
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_ENDPOINT_20260910.md`, 16,114 bytes):

| measure | value |
|---|---|
| cards in the L2 artifact | 14 |
| cards in the PRD | 14 |
| in L2 but not the PRD / in the PRD but not L2 | none / none |
| **cards IDENTICAL** (whitespace-normalised) | **14 of 14** |
| `DONE WHEN` distribution | 13 EXERCISED / 1 APPLIED |
| `ACCEPT` lines · `SOURCE` lines | 14 · 14 |

The distribution matches the L2 commit's own subject line (*"fourteen outcomes, thirteen of them
EXERCISED bars"*), so the PRD, the artifact and the ratifying commit message agree on three carriers.

⚠ **MY FIRST INSTRUMENT REPORTED A DIFFERENCE THAT DOES NOT EXIST, and I am recording that rather
than only its corrected output.** A greedy card regex bounded on *"the next `FWD-n` or end-of-file"*
ran past `FWD-14` — the LAST card — and swallowed different trailing prose from each file, printing
`DIFFERS FWD-14`. Re-bounding on the closing fence gives 14 of 14 identical. **A comparison
instrument that is correct for every element except the last one is the shape that reads as a genuine
single-field defect**, and the tell was that the visible prefixes matched exactly.

### LIMB 2 — THE TRANSCRIPTION DEFECT THIS SECTION EXISTS TO CLOSE IS GENUINELY CLOSED

The PRD records that its staged copy carried a POINTER instead of the cards, that the landing was
byte-for-byte so the transcription never happened, and that for roughly an hour **`FWD_DEF_RE`
measured 0 outcomes defined** while the PRD cited fourteen. Found by `2.0.0_SA_COO~ZZZ` running the L6
gate's own functions with a positive control, not by the author. I re-measured the present state: **14
definitions present.** The section is now the only carrier, as it says. ⭐ That near-miss is the
strongest argument for this gate existing at all — an unsigned PRD with zero outcomes would have
passed every mechanical check the round applied to itself.

---

## ⛔ TWO FINDINGS. NEITHER IS A REFUSAL GROUND; ONE IS A ROUND-3 BLOCKER.

### 1. SEVERAL `EXERCISED` BARS ARE GATED ON ACTS NO SEAT CAN PERFORM ON DEMAND

Rule 27's L2 clause is categorical: *"NO FWD IS A WAIT — every outcome is provable by an act a seat
can take ON DEMAND, and one whose only proof is an event nobody controls is re-cut so its MECHANISM is
driven deliberately, the organic case kept as the negative arm; a genuinely essential wait is EXPRESSLY
QUALIFIED on the outcome with its reason and Andrew's word."*

Thirteen of fourteen bars are `EXERCISED`, and they are not uniform in drivability:

- **DRIVABLE** — `FWD-1`, `FWD-2`, `FWD-3`, `FWD-4`, `FWD-10`, `FWD-11`, `FWD-12`, `FWD-13`. A seat
  can open the page, type an uncovered ticker, challenge a figure, re-run one input alone, or check a
  shared name. These are fine.
- ⛔ **NOT DRIVABLE BY ANY SEAT** — `FWD-5` (*"Adam has actually forwarded one"*) and `FWD-7` (*"Adam
  has used it to find a stale name"*) require acts by a **named person**. `FWD-14` (*"a list has
  actually gone out of date"*) waits on **organic rot** — the textbook case Rule 27 says to re-cut so
  the staling is driven deliberately with the organic case as the negative arm.
- ⛔⛔ **`FWD-8` IS THE SHARPEST AND IS NOT MERELY UNDRIVABLE — IT IS UNOBSERVABLE.** Its bar reads
  *"an analyst who distrusted it has stopped."* That is a change in a person's **belief**, with no
  artifact, no log and no discriminator. Nothing a seat reads can distinguish "stopped distrusting"
  from "stopped looking."

**WHY THIS IS NOT A REFUSAL.** The no-wait clause binds at **L2**, which is the CTO's limb, and the
cards are faithfully carried — which is what an L4-R ENDPOINT sign-off certifies. Refusing here would
hold five mechanical round-2 orders, every one of which fixes a defect I myself found in round 1, over
a defect that cannot bite until the surface exercise. **And that exercise is already round 3, gated on
Andrew's DESIGN_SPEC approval** (`2.0.0_SA_COO~ZZZ`, msg 21212: *"The surface EXERCISE of every FWD
remains round 3 on Andrew's DESIGN_SPEC approval, unchanged"*), and none of round 2's five cells
touches it.

⚠ **BUT IT IS A ROUND-3 BLOCKER AND IT SHOULD BE SETTLED BEFORE ROUND 3 IS CUT, NOT DURING IT.**
Thirteen outcomes cannot be closed by any build, and four of them cannot be closed by any *agent act*
either. Each needs one of: a deliberate mechanism (stale a list on purpose; drive the displacement
test as a scripted comparison), or Andrew's express qualification recorded on the outcome, or a re-cut
bar. `FWD-8` likely needs re-cutting outright — a belief is not gradeable, and the observable behind
it is probably *"the comparison block names its own basis, or says it cannot"*, which `FWD-8`'s own
ACCEPT paragraph already gestures at. **Routed to `1.0.0_SA_CTO~Z` as the L2 owner.**

### 2. SECTION 0's VERSION HAZARD HAS EXPIRED, AND IT IS MARKED BINDING ON EVERY READER

s.0 is headed *"THE VERSION HAZARD — BINDING ON EVERY READER OF THIS PRD"* and instructs: *"Until
`0.0.0_AB_MSTR~Z` pushes, every worker face citing the brief cites `@19ce7d5b4d` explicitly and reads
from the working tree."* Measured just now:

```
brief v2 @19ce7d5b4d   IS an ancestor of origin/SITEZ  -> the condition has LAPSED
brief v1 @046337e2df   on origin (as s.0 says)
```

The overnight merges pushed it. **The ACTION s.0 prescribes stays correct** — citing the pin explicitly
is right whether or not it is on origin — **but its stated REASON is now false**, and the clause reads
as though origin is still dangerous. Low value, and I am not asking for an edit mid-round; recorded
because a clause marked BINDING ON EVERY READER whose premise has silently expired is how a stale
instruction keeps being obeyed for the wrong reason. ⭐ Its underlying warning was excellent and is
worth preserving in whatever form outlives it: resolving that brief from origin *"loses the entire
validation territory and the whole social limb, and the result looks complete."*

---

## WHAT THIS SIGN-OFF CERTIFIES AND DOES NOT

**CERTIFIES:** that the ENDPOINT section faithfully and completely carries the ratified L2 endpoint
`@3bc8f5f2c4` — 14 of 14 cards identical, 14 ACCEPT, 14 SOURCE, 13 EXERCISED / 1 APPLIED — that
`FWD-n` ids are unique and unreused, and that the transcription defect the section records is closed.

**DOES NOT CERTIFY:** that every bar is closable as written. Four are not (`FWD-5`, `FWD-7`, `FWD-8`,
`FWD-14`), `FWD-8` most seriously, and that is an L2 matter for round 3. Nor the coverage map, which is
`4.0.0_SA_CRO~Z`'s half and remains the last thing standing between the COO and L6.

— `3.0.0_SA_CVO~Z`
