# POSN_ASTTAX -- ROUND 2 ANALYSIS (L10, `1.0.0_SA_CTO~Z`)

**archetype:** SCRIBE (ledger) · **written by** `1.0.0_SA_CTO~Z` · **2026-09-11**

**Slug graded:** `surprise-channel/remediations/REMEDIATION_v2.md`@`0f3be24afa` -- the single round-2
L10 slug from `3.0.0_SA_CVO~Z`. Dispositions `adjudications/ADJUDICATION_v3.md`@`0f3be24afa`;
L9.r2 + L10.r2 stamps co-committed.

**VERIFIED AT THE PIN BEFORE GRADING, not accepted on the slug's report:** REMEDIATION_v2 carries
**15 rows, 3 REMEDIATED / 12 OPEN**, 0 malformed; ADJUDICATION_v3 carries 6; the order census reads
**2 open of 8**, exactly `TO-S2-1` and `TO-S3-1`. Every figure the slug stated is the figure measured.

---

## 1. THE VERDICT: round 2 CLOSES, and its most valuable output is a NO-GO

Round 2 was **seven cells: five executed, two deliberately UNRUN.** It closes not because everything
was done but because **the work that remained was correctly refused.**

⭐ **THE ROUND'S PRINCIPAL RESULT IS THAT `TO-S7-1` SAID NO.** It was cut to verify that the
`asset_class` allocation chain carries the ratified five-class vocabulary; it ran that verification
and returned **NO-GO**. That is a cell doing exactly its job. A verification cell that returns NO is
not a failed cell -- **it is the only kind of cell that can stop a bad act**, and it stopped one.

⛔ **AND THE PREMISE THE ROUND WAS BUILT ON IS FALSIFIED, WHICH IS THE FINDING THAT OUTLIVES IT.**
`C-RETAG-SAFETY` says the retag is a landmine because a fixed-key dict raises `KeyError` and **blanks
the page for all four partner firms.** Measured: **0 of 17 hops RAISE.** `AT2-s-6` hardened the
generator and killed the KeyError. A retag today would NOT blank the page -- it would render
`Commodities`/`Structured` as the literal string `'Unknown'` and **silently zero the weight.**
**THE HAZARD GOT QUIETER, NOT SAFER** -- strictly worse for detection than the blanking it replaced.
⚠ **VINTAGE BOUND:** the 17/3/14 figures are pinned to `TO-S7-1`'s run. `3.0.0_SA_CVO~Z` records that
`S1` later repaired a benchmark hop, so the RATIO is historical. **The VERDICT is not** -- the CVO
re-confirmed against current controls that `Commodities`/`Structured` still display as `Unknown`.

**`TO-S2-1` CANNOT SEE ITS OWN FAILURE.** Its `S2-AC5` is "confirm the page still renders", which
post-`s-6` returns the SAME observation in the healthy world and the broken one. Cutting it as written
would have produced **a PASS over a live regression.**

**VXX is the entire live blast radius** -- the only held member of the retag set. A second, independent
defect stands alongside: `seed-etf-constituents.py`'s unconditional full-item put would revert both
`AT2-s-5`'s writes and any retag (LATENT, no automatic trigger).

## 2. FWD STATE: 0 of 6 newly REALIZED, and that is correct

Round 2 was pre-surface correctness and investigation work. **No `FWD` is graded REALIZED by this
round** and none should be: nothing here is a surface a person has used. Round 1 graded 0 of 6 and the
addendum recorded why that negative result was its value; round 2 is the same shape one layer deeper.

## 3. THE TWO UNRUN CELLS -- CARRIED FORWARD EXPLICITLY, NOT LAUNDERED

`TO-S2-1` (the retag) and `TO-S3-1` stay `staged` and UNRUN. `2.0.0_SA_COO~Z` declined to mark them
cancelled or superseded, in its own words: *"a terminal status without a real pointer is rot with a
tidier label."* **That judgment is endorsed here and is the right one.** They are not done, the need
did not go away, and no successor exists yet to point at.

⭐ **THEY ROUTE ONLY ON ANDREW'S NAMED WORD.** The gate's L10 precondition -- his own LD-0521, *"We do
not route until the job is over"* -- mechanically refused the slug while they were non-terminal.
Three seats refused the two available escapes: flipping the cells terminal (**the driver would have
been the beneficiary of shrinking its own denominator**) and the audited override (**converting his
word by agent judgment**). He then ruled the exception himself, on a named case.
⛔ **SCOPE OF THAT PERMISSION IS NARROW AND IS RECORDED AS SUCH: LD-0521 IS NOT AMENDED** and still
binds every other round on both fabrics. Nobody may cite this round as precedent.

## 4. WHAT ROUND 3 MUST CARRY -- the CTO's recut input

1. ⛔ **`C-RETAG-SAFETY` NEEDS RE-FOUNDING, NOT RE-SEQUENCING.** Its stated mechanism is FALSIFIED.
   The constraint is still right that the retag is unsafe and **right for a different reason than it
   states.** A constraint whose stated mechanism is dead will be mis-applied by the next cell that
   reads it -- and "the page still renders" is precisely the check that dead mechanism invites.
2. ⛔ **STEP (2) MUST NAME A BAR, NOT AN ACT.** It reads "verify the chain", which is a task. Written
   as an act **it invited this seat's own withdrawn error** -- reading a completed verification cell
   as a passed one. It must read as a CONDITION with a threshold.
3. ⛔ **`S2-AC5` NEEDS A CRITERION THAT FAILS IN THE BROKEN WORLD** -- the served value and the
   weight, never "the page renders".
4. The **re-seed revert**, and `TO-S7-1`'s two disclosed unmeasured gaps (the FRONTEND hop, `portal/`
   outside the worker's cone with 29,577 UNREADABLE printed; two enumerated-but-untested sibling
   consumers). Both can only STRENGTHEN a NO-GO; neither is measured and neither is treated as if it
   were.

**The recut is `2.0.0_SA_COO~Z`'s in ONE issuance.** Twelve OPEN remediation records and four
`DECOMP_INVALIDATING` dispositions (C-S30..33) travel with it.

## 5. CORRECTIONS THIS SEAT OWES, RECORDED RATHER THAN DROPPED

- ⛔ **`C-S34` corrects msg 21505 and it is right.** This seat told the CVO that `W8-S2` was NOT among
  the gate-blocked rows because the proposed-dispositions file listed C-S13/S18/S19/S21 and showed
  W8-S2 only as a citation. **Proposed `C-S21` explicitly adjudicated `W8-S2`.** The error: this seat
  read each entry's OWN id and never read what the entry ADJUDICATED -- **the wrong field, read
  carefully.** The disposition is now `DECOMP_INVALIDATING` via C-S30..33.
- **`POSN_ASTTAX-Z-W8-S2`** was not disarmed by this seat and the reason was stated to the CVO rather
  than left as a silent wait: the hazard is REAL and UNREMEDIATED (the seeder writes only on CREATE),
  and its remedy is a producer change declined under Andrew's session scope. ⚠ **Whoever disarms it
  must MEASURE THE WORKTREE, NOT JUST HEAD** -- `seed-etf-constituents.py` carries uncommitted bytes
  preserved at `5c9e329a21`, and the difference is invisible unless you look.

## 6. GATE-OWNER REVIEW OF THE ROUTING EXCEPTION (`e602581190`)

`3.0.0_SA_CVO~Z` implemented Andrew's permission as a mechanical exception in a gate this seat owns.
**Reviewed and APPROVED, verified rather than accepted.** It is not an override: it is a
CONTENT-ADDRESSED SINGLE-CASE KEY, pinned on project, round, order-count, exact filing paths, the
authority message id, the canonical hash of each authorized row, and the hashes of BOTH unchanged
order blobs -- read from an immutable record at a pinned commit, with every failure path returning
BIND.
**Six negative probes run by this seat, all REFUSED:** different project, different path, one-byte
mutated row, different open-order set, wrong total, unknown row id. 103 self-test arms still pass.
⭐ **It cannot be reused and it self-destructs if either unrun order is touched** -- which is a better
shape than the override it declined to use, because an override is a blanket per-commit escape and
this is a key cut for one lock.

---

**Round 2 is CLOSED at L10.** The PROJECT is not closed; it closes when every FWD grades REALIZED,
which needs a surface that does not exist yet.

**Push state:** LOCAL at write time. `0.0.0_AB_MSTR~Z` pushes origin/SITEZ; this seat does not push.
