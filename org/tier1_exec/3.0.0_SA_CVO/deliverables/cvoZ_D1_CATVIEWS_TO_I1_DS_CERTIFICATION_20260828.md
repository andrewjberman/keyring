# `D1_CATVIEWS.TO-I1-DS` — CERTIFIED ON THE MERITS: 3 PASS + 1 APPLIED-GATED, instance CORRECTLY INVALID

**Author:** `3.0.0_SA_CVO~Z` · **2026-08-28T04:3xZ** · **Instance:**
`org/tier2_senior/0.4.0_DS_ClientPlatform~T/deliverables/D1_CATVIEWS.TO-I1-DS_PROOF_OF_SPEC.json`
**Standing:** `1.0.0_SA_CTO~Z`'s interim control — *file the TRUE values, accept the INVALID, never alter
evidence to satisfy the grammar; CVO certifies on the merits with the defect cited.*

---

## THE VERDICT

> **3 PASS + 1 APPLIED-GATED. Instance INVALID on VOCABULARY grounds only. CERTIFIED ON THE MERITS.**
> **Never a bare 4/4, and never a FAIL.**

```
STEP ZERO      TO <expected_criteria>  I1DS-AC1,AC2,AC3,AC4   FILED  AC1,AC2,AC3,AC4
               IDENTICAL SET-FOR-SET, 4 for 4. Coverage closed at this seat.
CHECKER  rc=1  violations=2, acceptance rows=4
               1. acceptance/3/status  'APPLIED-GATED' not in the status enum
               2. spec_ref/group       'I1' not in [A,B,C,D,W,M,X,T,OTHER]
SUBSTANCE      0 of 2 violations touch a measurement, a denominator, a control or a claim.
```

**The partition passes 0-to-2.** Every violation is the grammar refusing a value; none is the
instrument disagreeing with the world.

---

## ⛔ I MUST CORRECT MY OWN BANKED VERDICT ON THIS TO

**I hold a note reading "TO-I1-DS FAILED the partition 13-to-6."** That was true **of the superseded
instance**. `0.4.0_DS_ClientPlatform~T` re-filed 19 violations → 2, and the residue is **purely
vocabulary**. Carrying my earlier verdict forward would have refused certification on the strength of a
measurement of a document that no longer exists — **the stale-carrier failure, in my own queue notes,
against the very TO whose re-filing fixed it.**

---

## WHY `APPLIED-GATED` IS THE RIGHT VALUE AND BOTH LEGAL ALTERNATIVES ARE WRONG

**The TO MANDATES it**, twice and by name — `:146` *"`D1-i-2` is reported **APPLIED-GATED**"*, `:178`
*"**AC4's expected terminal status is APPLIED-GATED, NOT PASS.**"*

```
PASS   would assert an apply that MUST NOT have happened (the NO-SHIP fence, lifted only by
       Andrew's by-name word)
FAIL   would assert a criterion that failed, when it was CORRECTLY GATED
```

>> **THE ENUM HAS NO MEMBER FOR "CORRECTLY BLOCKED."** A criterion whose honest verdict is *"correctly
did not run"* is not a failure of the TO, and there is no way to say so in the vocabulary the gate
accepts. **The instance is therefore correctly invalid, and editing it into validity would be exactly
the "edit the evidence to satisfy the instrument" act ruled against tonight.**

⭐ **AND IT IS AN UNCOVERED DOMAIN MEMBER, NOT A ONE-OFF — TWO SEATS FOUND IT INDEPENDENTLY.**
`0.4.0_DS_ClientPlatform~P` hit the same gap on `TO-6` `AC3` with *"authorization withheld."* **Two
seats, two TOs, one missing member — in the gate that ENFORCES Rule 24's own MECE postulate.** Rule 24
(i) says *hunt the uncovered member*; the schema that polices it has one.

---

## ⚠ THE TWO VIOLATIONS ARE NOT THE SAME KIND OF GAP, AND FLATTENING THEM WILL COST A FIX

This is the one thing I am adding that the record does not already carry:

| # | violation | kind | can it be made valid today? |
|---|---|---|---|
| 1 | `APPLIED-GATED` | **HARD gap** — no enum member expresses "correctly blocked" | **No.** Requires a schema change |
| 2 | `group: 'I1'` | **SOFT gap** — `OTHER` exists and would validate | **Yes — at the cost of erasing which group it is** |

⛔ **The predictable failure: someone reports "2 vocabulary violations", writes `OTHER` for #2, watches
the count drop 2 → 1, and reads that as progress.** It is not — it trades a true value for a valid one
on the violation that was never the problem, while the gap that actually blocks the TO is untouched.
**#2 should stay `I1` for the same reason #1 stays `APPLIED-GATED`.**

---

## SCOPE — WHAT THIS CERTIFICATE DOES NOT SAY

- **No schema edit is proposed or endorsed.** It is HELD until D1+D4 are done; that is `1.0.0_SA_CTO~Z`'s
  standing position and I am not reopening it. The build ladder and the moratorium both point the same way.
- **`D1-i-2` has not executed and must not.** `AC4` certifies that it was correctly *not* performed —
  no re-pin, no `safe-apply`, no pin advance, and none proposed as ready.
- **Not a D1 closure.** `D1_CATVIEWS.TO-P1-AE` remains open on the ~13:30Z scheduled fire, and
  **D1 has had no Andrew smoke test at all** — see the D4 adjudication; his 04:2xZ eye was on Satellites.
- **The assessment behind this is `0.4.0_DS_ClientPlatform~T`'s and it is corroboration, not
  repetition** — the predecessor read the downloaded zip, that seat read the BUILD INPUT (`git show
  <ref>:build_package.py` → AST `literal_eval`), with positive and negative controls on every read, and
  **the two instruments disagreed**, which is what a second instrument is for.

---

— `3.0.0_SA_CVO~Z`
