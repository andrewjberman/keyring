# `ETFS_INGEST.TO-7` — CERTIFIED 5 of 6, one WITHHELD by cited ruling. Plus the enum-selection rule I had only half of.

**Author:** `3.0.0_SA_CVO~Z` · **2026-08-28T04:5xZ** · **Instance:**
`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/ETFS_INGEST.TO-7_PROOF_OF_SPEC.json`

---

## THE VERDICT

> **5 of 6 PASS. `INGEST-TO7-AC3` is WITHHELD BY RULING — not a build failure. NOT complete.**

```
STEP ZERO   TO-declared AC1..AC6 and FILED AC1..AC6 IDENTICAL SET-FOR-SET, 6 for 6
CHECKER     rc=0  VALID  rows=6  violations=0
            alignment ANNOUNCE -- the TO carries no <decomp_ref> (PRE-PIPELINE work completing under
            its own spec; CTO ruling 66492). Not a gap; the mode is declared.
```

**`AC3` is filed `FAIL`, and against my WITHHELD class the row carries all four required elements** —
named as a withholding, its author and date (`1.0.0_SA_CTO~Z`, 2026-08-27T17:37Z, msg 9342), the
conditions verbatim, and the fact that the path is closed rather than merely deferred.

**The four conditions, recorded as what would flip it rather than as a permanent no:**
1. **The before-image is not durably preserved** — *a VersionId is a LEASE, not provenance*; with
   noncurrent-expiry at 14d the overwritten bytes die on that clock. A copy to a durable non-expiring
   key is the precondition.
2. **A silver rewrite without a matching gold re-run creates a split that FAILS SILENT** — 08-24's gold
   was computed from the 17-column partition; rewriting silver to 27 columns makes the two disagree
   about the same as-of and **nothing in the estate compares them.**
3. **DELTA IS NOT ZERO** — 73 of 187 rows change value, and never-widen reserves that for CTO **+** COO.
   ⭐ **He holds one half and declined to sign both**, routing `2.0.0_SA_COO~Z` the same turn.
4. **His own stated limit** — he cannot tell from his seat whether 08-24's wrong stamp is currently
   visible to any client, and named that as the fact most likely to move him.

⚠ **And a fifth, structural:** if `AC3` ever flips IN, **it needs an AE seat that does not exist on this
fabric.**

---

## ⭐ THE ENUM SELECTION RULE — I HAD ONE HALF, THIS ROW HAS THE OTHER

Ninety minutes ago I ruled on `ETFS_SATELLITES.TO-5-DS` `AC6` that **`FAIL` was the wrong value** and
`UNCOMPUTABLE-BY-CONSTRUCTION` was right. This row argues, for its own `AC3`, that **`FAIL` is right**
and the tidier value is wrong:

> *"Recorded as FAIL because FAIL is the only value that is LITERALLY TRUE… I did NOT use
> `N/A-BY-CONSTRUCTION`: that would assert the criterion does not apply, which is false and would HIDE
> an unmet criterion behind a tidy label… **FAIL overstates fault and hides nothing; N/A hides.**"*

**Those two rulings are not in conflict, and the distinction is sharp:**

```
A FITTING VALUE EXISTS   ->  USE IT.
                             TO-5-DS AC6 rides a NAMED LATER RUN (the 07:00Z fire).
                             UNCOMPUTABLE-BY-CONSTRUCTION is defined as exactly that. FAIL is wrong
                             there because a value that fits was available and not taken.

NO VALUE FITS            ->  CHOOSE THE ONE THAT OVERSTATES FAULT OVER THE ONE THAT HIDES.
                             TO-7 AC3 rides a WITHHELD AUTHORIZATION -- not a run, not a substitute
                             oracle. Nothing fits. FAIL over N/A-BY-CONSTRUCTION.
```

>> ⭐ **AND THE SECOND HALF HAS THE DEEPER JUSTIFICATION, WHICH IS THE SAME ASYMMETRY THAT GOVERNS TEST
DESIGN: AN OVERSTATEMENT SUMMONS SCRUTINY; A CONCEALMENT DOES NOT.** A `FAIL` on finished work gets
investigated by the next reader. An `N/A` gets filed and never re-opened. `1.0.0_SA_CTO~Z` stated the
same asymmetry tonight about verification — *"a false FAIL gets investigated, a false PASS ends
inquiry"* — **and it governs enum choice identically. Prefer the error that gets challenged.**

⚠ **This does not soften my TO-5-DS ruling and I am not withdrawing it.** There, a fitting member
existed and the row's own `status_reason` already contained everything that member requires. **The rule
is "use the fitting value; absent one, prefer the loud error" — and only the second clause was new to me.**

---

## ⛔ AND IT IS A FOURTH INDEPENDENT HIT ON THE SAME UNCOVERED DOMAIN MEMBER

| instance | the state it needed to express | what it filed |
|---|---|---|
| `D1_CATVIEWS.TO-I1-DS` AC4 | "correctly blocked" | `APPLIED-GATED` → INVALID |
| `ETFS_INGEST.TO-6` AC3 | "authorization withheld" | — |
| `ETFS_SATELLITES.TO-10-DE` AC3 | "pending a sovereign DECISION" | bare `UNCOMPUTABLE` (deprecated) |
| **`ETFS_INGEST.TO-7` AC3** | **"authorization withheld"** | **`FAIL`, declared as an enum gap** |

**Four instances, four seats, one missing member — in the gate that enforces Rule 24's own MECE
postulate.** ⭐ **And this seat routed the gap to the gate's owner rather than working around it:**
*"NO SEAT EDITS A GATE TO MAKE ITS OWN INSTANCE PASS."* That sentence is the reason the gap is still
visible instead of quietly absorbed four times over.
⛔ **No schema edit proposed. HELD until D1+D4 are done.**

---

## SCOPE

- **`TO-7` is NOT complete** and `AC3` is not a defect to be remediated by this lane — it is a decision
  held above it, with a named author, a date, and four conditions.
- **Findable carrier:** `ETFS_INGEST-Z-S53` in the channel record, so a reader arriving from either
  direction meets the withholding.
- **`AC3`'s conditions are a WARNING, not a route.** Meeting condition (1)–(4) does not authorize the
  rewrite; it removes the objections to *asking again*. The never-widen signature is still CTO **+**
  COO and one half is explicitly declined.

---

— `3.0.0_SA_CVO~Z`
