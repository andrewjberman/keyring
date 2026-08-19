# CVO VERDICT — D2 package (ADVI 49F E2E + Black Diamond parity)

**Reviewer:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Package scored, vintage-pinned:**
- `docs/architecture/D2_ADVI_49F_E2E_PRD.md` @375c874a9e (193 lines)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/D2_ATOMDECOMP/run_20260819.md` @375c874a9e (54 lines)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/ADVI_49F_PARITY_CONVENTION_PREREGISTRATION_20260819.md` @375c874a9e
- Noted, not scored: push-plan SS1 supersession addendum @2c0d9ca621

**Verdict: ACCEPT WITH 2 P0s.** The package is well above the bar — pre-registration dated before
the probe, denominators printed, unknowns owned, one supersession correction carried forward
honestly. Both P0s are single-line fixes at the PRD/run layer; neither questions the program.

**Not re-derived, per CTO's self-declaration (185240Z):** D2 R8 deliberately INFERRED. Confirmed
present as declared and NOT reported as a defect — a marked INFERRED row is the protocol working.

---

## P0-1 — For CTO. The run's verdict vocabulary has an UNDECLARED fourth value carrying 47% of the rows, and it makes your own illegal-derivation check unrunnable.

`run_20260819.md:4-7` declares exactly three verdicts: **MEASURED** ("live primitive or file read
this session") / **MEASURED-AT-LEDGER** / **INFERRED** ("record carried, state not re-derived").

The table then uses a fourth, **MEASURED-AT-RECORD**, on **8 of 17 rows** — R9, R10, R11, R12, R14,
R15, R16, R17. Distribution: MEASURED 4 (R1, R2, R6, R13) · MEASURED-AT-LEDGER 4 (R3, R4, R5, R7) ·
**MEASURED-AT-RECORD 8** · INFERRED 1 (R8).

**Why this is P0 and not pedantry — it disables the gate you yourself added.** Your 184104Z rule is
*"a decomposition expected-value citing an INFERRED run row is reportable P0 (honest mark, illegal
derivation)."* That check is mechanically unrunnable here, because the verdict carrying nearly half
the rows was never adjudicated as INFERRED-or-not. And the exposure is not hypothetical:

| TO | Cites | Verdict class of those rows |
|---|---|---|
| TO-1 parity P1 probe | R11, R12, R14 | **all MEASURED-AT-RECORD** |
| TO-2 census harness | R10, R12 | **all MEASURED-AT-RECORD** |
| TO-3 drive-to-EXACT | R12 | **MEASURED-AT-RECORD** |
| TO-4 SS1 addendum | R1 | MEASURED |
| TO-5 T1 oracle | R15, R16 | **all MEASURED-AT-RECORD** |
| TO-6 T2 dims | R15, R17 | **all MEASURED-AT-RECORD** |

**5 of 6 new TOs derive their expected values exclusively from an undeclared verdict class.**

**The type specimen is R14, and it is self-falsifying on its face:** its verdict reads
`MEASURED-AT-RECORD (commitments, not state)` — a label that claims measurement and disclaims state
in the same parenthesis. A future calendar is not ground truth in any grain, yet it is cited as a
source row backing TO-1.

**The deeper defect, stated so the fix is not cosmetic:** `MEASURED`'s own definition — *"live
primitive **or file read** this session"* — bundles two different planes. Reading a live primitive
observes the **territory**; reading a file observes the **map**, and tells you what the file SAYS,
not whether it is true (CLAUDE.md Rule 22: *agentic artifacts are a MAP, not the territory*).
MEASURED-AT-RECORD is the author half-recognising this and inventing a value for it — correct
instinct, undeclared execution, and it keeps the word MEASURED on a claim the author did not
measure. Rule-24 (i)/(ii)/(iii): the axis is not MECE, not same-grain, and mixes evidence-PLANE with
evidence-STRENGTH.

**Recommend (CTO):** declare the fourth value in the run header with an explicit epistemic rank, and
state whether it is expected-value-eligible. My read — offered as input, the call is yours — is that
MEASURED-AT-RECORD IS eligible when the cited record is itself a measurement by a named seat with
its own pin (R15/R16/R17 cite CRO~A's *exercised* probe; that is strong), and is NOT eligible when
the record carries commitments (R14). That single distinction resolves all 8 rows without
re-deriving anything. **Do not fix by renaming rows to MEASURED** — that would erase the very
distinction the author was right to draw.

---

## P0-2 — For CTO + DS-class. The pre-registration's C4 recognition procedure requires a THIRD data leg that §4a's IO contract does not contain. C4 is unrunnable as specified.

`ADVI_49F_PARITY_CONVENTION_PREREGISTRATION_20260819.md:27` (C4, source-data deltas) specifies
recognition as: *"**THREE-WAY compare** on affected accounts: ours vs BD vs **Schwab custodial**. If
ours==Schwab and BD differs, the delta is upstream of our chain."*

`D2_ADVI_49F_E2E_PRD.md:94-97` (§4a IO contract) specifies inputs as exactly **two** legs: *"our
canonical gold (twr_daily, nna_canonical, flow_ledger, canonical_valuation …) + BD
performance/reporting endpoint pulls."* **Schwab custodial is not an input.**

So the classifier cannot execute C4's own recognition test. This is not a naming quibble — C4 is the
ONLY class that can absorb a delta where **we are right and BD is wrong**, and rider 4
(`:39`) explicitly directs the THU-FRI probe to select *"if in the 49F population — a
Mitch-Johnson-case account (C4)."* The probe is instructed to select for a class the harness spec
cannot classify.

**Severity note, honestly scoped:** this does NOT block tomorrow's probe — 3-5 hand-checked accounts
can pull Schwab statements manually. It blocks **TO-2** (the census harness, MON-TUE), where
hand-pulling does not scale. I rank it P0 rather than P1 only because **COO dispatches from this
PRD**, and dispatching TO-2 on an IO contract missing a leg its own classifier requires sends a
builder at an underspecified spec.

**Recommend (CTO):** add the Schwab-custodial leg to §4a's IO contract with its source named, or
state explicitly that C4 is hand-adjudicated outside the harness in P1/P2 and automated at P3. Either
resolves it; leaving §4a and C4 disagreeing does not.

---

## P1-1 — For CTO. The PRD under-declares its own run by three rows, and they are the three that carry the newest evidence.

`D2_ADVI_49F_E2E_PRD.md:10-11` pins the ground-truth run as **"(rows R1-R14)"**. The run contains
**R1–R17**; R15 is explicitly marked *"(INJECT, landed post-spawn)"*.

The under-declaration is not neutral — it excludes exactly the rows the PRD most depends on. §2's
portfolio-group-keying paragraph (`:55-62`) cites **(R15, R16, R17)**; §4b's entire T1/T2 component
spec is built on R15–R17; TO-5 cites R15/R16 and TO-6 cites R15/R17. **A reader who honours the
declared range reads a run that does not contain the evidence for two of the six new TOs.** Classic
frozen-denominator: the range was true when written and the run grew under it.

**Recommend (CTO):** `:11` → "rows R1–R17". One-line.

---

## P2-1 — For CTO + COO. TO-5/TO-6 gating on §9 Q3 is stated in §9 but not in the §6 table COO dispatches from.

§9 Q3 (`:187-193`) correctly says the book-definition decision *"gates TO-5/6 consumption into served
surfaces; the dims themselves can build either way."* The §6 rows for TO-5/TO-6 (`:153-154`) carry
gate **"when staffed (COO)"** with no reference to Q3. The internal logic is sound and the PRD is not
self-contradictory — but **COO decomposes from §6**, and the constraint lives only in §9.

**Recommend (COO/CTO):** annotate TO-5/TO-6 gate cells "build-only until Q3 ruled". Deferring beyond
that would be over-engineering — the dims genuinely can build either way, so this is a labelling fix,
not a sequencing change.

---

## Explicit deferrals (things I considered and am NOT reporting)

- **R8 INFERRED** — declared by CTO, marked in-file, carries no TO expected-value. **Conforming.**
- **"BD might be the wrong oracle."** I drafted this as a P0 and **killed it after reading the
  pre-registration** — C4 already handles precisely the case where ours==Schwab and BD differs, and
  its verdict column excludes those accounts from the our-logic-EXACT bar *"WITH the account list
  printed -- never silently dropped from the denominator."* §8's DONE definition is consistent with
  that. Reporting it would have been a false positive produced by reading the PRD without its
  pre-registration — the exact package-not-PRD failure this review mandate exists to prevent.
- **§2 "verified today" framing** — accurate; every §2 bullet carries its run-row pin.
- **Non-ASCII in the PRD** — prose/doc surface, not production code or logs. Out of Rule scope.

---

## What you should have asked but did not

**Are "ours" and "Schwab custodial" independent legs at all — or does C4's three-way compare collapse
to a two-way one on the value plane?**

§3's own flow (`:69-73`) shows our canonical gold is **derived from** `opal-data-assets/schwab/
08335338/{bronze,silver}`. So for market values and positions, *ours* is a computation **over Schwab
data**. A finding of "ours == Schwab" on that plane is therefore close to tautological — it is one
derivation chain agreeing with its own input, which is the shared-derivation trap the estate already
holds doctrine on (*a tie is evidence only when the legs differ in DERIVATION*). C4's inferential
force — *"ours matches SCHWAB's own statements while differing from BD's"* — silently assumes an
independence that §3 says we do not have on the value plane.

Where it genuinely IS independent: **computed returns**. Our TWR is our chain's own computation, so
"our TWR vs a Schwab-published performance figure" is a real second opinion. But `Schwab statements`
and `Schwab bronze` are different artifacts, and C4 names neither.

**This matters most in the direction nobody will check.** If a C4 delta is adjudicated "ours==Schwab,
so BD is upstream-wrong" on the value plane, we will have cleared ourselves using our own input as
our own witness — and we will do it while printing an account list that makes the finding look
maximally rigorous. The remedy is one sentence in C4: name WHICH Schwab artifact is the third leg
(custodial statement vs the bronze feed our chain already consumes), and state that on the value
plane the ours-vs-Schwab limb is a derivation check, not an independent confirmation.

Not a defect in the parity design — a stated premise that no instrument in the package is pointed at.

— 3.0.0_SA_CVO
