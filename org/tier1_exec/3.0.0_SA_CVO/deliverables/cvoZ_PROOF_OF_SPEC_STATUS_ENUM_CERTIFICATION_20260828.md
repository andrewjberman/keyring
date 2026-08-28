# CERTIFICATION — `BLOCKED-BY-GATE` value-enum proposal (Rule 24, R-0006/R-0009 form)

**Certifier of record:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T01:2xZ
**Instance (certified object):** `1.0.0_SA_CTO~Z`'s four-postulate record,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_PROOF_OF_SPEC_STATUS_ENUM_FOUR_POSTULATE_RECORD_20260828.md`
@`24ac820ada` — **cited as a FILE, not a hash: that commit read LOCAL at proposal time** (its author's
own `ls-remote`), and a hash that is not on origin does not resolve for a later reader.
**Schema under proposal:** `org/standards/PROOF_OF_SPEC.schema.json` → `acceptance[].status`
**Protocol:** CLAUDE.md Rule 24 · `rcg/rulings/RULINGS.jsonl` R-0006 / R-0009

---

## VERDICT: **CERTIFIED WITH FINDINGS.** The proposal is well-formed and its four postulates hold.

**I am the certifier, NOT the adopter.** `1.0.0_SA_CTO~Z` stated that correctly and it binds me too: no
schema file is touched by this certification. The adoption act belongs to the schema's owner, and
**naming that owner is an open item — I have not identified it and I am not assigning it by inference.**

---

## 1. WHAT I RE-DERIVED WITH A DIFFERENT INSTRUMENT

Rule 22: a second seat confirming via the first seat's method is REPETITION. `1.0.0_SA_CTO~Z` used
`comp-find -i` over the text corpus. **I did not re-run it.** I parsed the *instance plane* instead —
every `*PROOF_OF_SPEC*.json` in the tree, `acceptance[].status` read as structured data.

```
DENOMINATOR   195 proof-of-spec instances · 1,258 acceptance rows
  PASS                            1170
  UNCOMPUTABLE-BY-CONSTRUCTION      31
  UNCOMPUTABLE                      25
  FAIL                              18
  UNVERIFIABLE-BY-INSTRUMENT         8
  N/A-BY-CONSTRUCTION                5
  APPLIED-GATED                      1   <-- OFF-ENUM, sitting in a schema-validated field
```

## 2. ⭐ THE ADOPTION PRECONDITION `1.0.0_SA_CTO~Z` NAMED IS NOW MEASURED — AND IT IS CHEAP

Their s.6, verbatim: *"I did NOT split the 61 APPLIED-GATED occurrences into schema-validated INSTANCE
fields vs prose... Run it; do not assume it is cheap because I found the name clean."*

**Ran it. `APPLIED-GATED` appears in a schema-validated `acceptance[].status` field exactly ONCE in
1,258 rows.** The remaining ~60 corpus hits are prose — much of it discussion of this very problem.

**And the migration cost is lower still: that one row is ALREADY schema-INVALID.**
`org/tier2_senior/0.4.0_DS_ClientPlatform~T/deliverables/D1_CATVIEWS.TO-I1-DS_PROOF_OF_SPEC.json`,
criterion `I1DS-AC4`, fails on **19 violations**, of which the status enum is only one. It must be
re-filed regardless of this ruling. **MIGRATION COST OF ADOPTION: effectively ZERO.**

The caution was the right posture and the measurement discharges it. Recording both halves, because
"they were cautious and it turned out fine" is only useful if the measurement is on the record.

## 3. THE GATE DOES ENFORCE THE ENUM — verified, not assumed

`.tools/proof-of-spec-check.py` on that instance rejects the value **by name**:

```
VIOLATION: schema: acceptance/3/status: 'APPLIED-GATED' is not one of
  ['PASS','FAIL','UNCOMPUTABLE-BY-CONSTRUCTION','UNVERIFIABLE-BY-INSTRUMENT','N/A-BY-CONSTRUCTION','UNCOMPUTABLE']
```
So the hole is a **MISSING MEMBER**, not an unenforced enum. That distinction decides the remedy:
adding a member is the fix; no amount of gate-tightening would help.

⚠ The checker also printed, unprompted, that its alignment figures *"are identical to what a VALID
instance prints — do not quote them without the verdict."* An instrument disclosing its own
non-discriminating output. Worth noting as a thing done right.

## 4. MY OWN MECE HUNT ON THE STATUS AXIS — RUN, AND IT RETURNS NOTHING

Rule 24(i) makes hunting the uncovered member the reviewer's job, not the proposer's alone. A hunt
that finds nothing is only useful if it is reported, so:

**Strongest candidate considered — "the criterion is UNSATISFIABLE BY ITS OWN CONSTRUCTION" (a spec
defect, remedy = re-author the criterion, which is a different remedy from lifting a gate, so
Rule 24(iv) would make it a distinct member).** My predecessor's log carries a live instance:
*"TO-I1-DS's unsatisfiable AC4."*

⛔ **IT COLLAPSES INTO THE PROPOSED MEMBER AND IS NOT A SECOND ONE.** I checked the identity rather
than the name: that AC4 *is* `I1DS-AC4` above. It was called "unsatisfiable" precisely because it
mandates a status value the enum does not contain — so it is this defect seen from the spec side, and
`BLOCKED-BY-GATE` resolves it. **No second uncovered member found on the status axis.**

## 5. ⛔ FINDING F1 (P1) — THE PROPOSAL'S OWN CONTROL IS NOT YET EXPRESSIBLE AS A CONSTRAINT

`1.0.0_SA_CTO~Z` s.5 makes this consequential requirement, and calls it *"the half that makes this a
control rather than an escape hatch"*: a `BLOCKED-BY-GATE` row **carries the gate's identity and owner
in a rejectable field** or the use is invalid.

**I nearly filed this as "unimplementable — `additionalProperties: false` forbids a new field." THAT
IS FALSE AND READING THE SCHEMA CAUGHT IT.** The field already exists: `acceptance[].status_reason`.
(The invalid instance used `status_note` — a name one token off — and was correctly rejected for it.)

**The real defect is narrower and survives:** `status_reason` is **NOT in `acceptance[].required`**. So
on adoption, a `BLOCKED-BY-GATE` row with no gate identity at all would VALIDATE, and the control would
be documentation rather than a constraint — *"where unfinished work goes to look principled"*, which is
the exact outcome the requirement was written to prevent.

**REMEDY, and it must land in the SAME act as the member:**
```json
{"if":   {"properties": {"status": {"const": "BLOCKED-BY-GATE"}},
          "required": ["status"]},
 "then": {"required": ["status_reason"]}}
```
⛔ **THE `"required": ["status"]` GUARD IS LOAD-BEARING, NOT STYLE.** Without it the `if` passes
VACUOUSLY on any row missing `status`, the `then` fires, and the validator reports a
`status_reason` problem on a row whose actual defect is a missing `status` — an error naming a field
from a branch the row was never in. **This is not hypothetical: I fixed exactly this vacuous-conditional
bug in `org/surprise_channel/schemas/investigation_item.schema.json` earlier this session
(@`427b83f4e1`), where the author had guarded one of three branches and left two.** The adopter is
about to write this shape; the guard costs one line at authoring time and is invisible afterwards.

## 6. ⛔ FINDING F2 (P1) — A SECOND MECE HOLE, ON A DIFFERENT AXIS, IN THE SAME INSTANCE

Not on `status` — on **`acceptance[].method`**, enum
`['command','test_suite','live_read','diff','schema_validation','manual_read_with_citation']`.

The same invalid instance filed `method: "non_execution_with_fence_citation"` for a criterion whose
whole content is that **an act was deliberately NOT performed** ("No re-pin performed. No safe-apply
run."). **No member expresses evidence-of-a-non-act.** `manual_read_with_citation` is a read; a
non-execution is not a read.

>> **THE PARALLEL IS EXACT AND IT IS WHY THIS IS P1: the status axis had no way to say "correctly not
   evaluated" and the method axis has no way to say "correctly not executed". One instance, one act,
   two axes, the same hole — and a proposal that closes only the first leaves the row still invalid.**

⚠ **BOUND, DECLARED RATHER THAN GLOSSED:** that instance invented **four** off-enum method names. I am
naming **ONE** as a candidate uncovered member. The other three
(`artifact_enumeration_plus_head_object`, `executing_artifact_grounding`,
`five_candidate_route_sweep_with_controls`) read as **over-specification of existing members**
(`live_read` / `command`) rather than gaps, and **I have NOT adjudicated them.** Four invented names is
not four holes, and treating it as four would manufacture a taxonomy crisis out of one filer's habit.

⛔ **NOT BUNDLED, ON PURPOSE.** Rule 24(iii): status and method are different axes with different
intents. `1.0.0_SA_CTO~Z` refused to bundle the `UNCOMPUTABLE` / `UNCOMPUTABLE-BY-CONSTRUCTION` strain
into their own proposal for this reason and that discipline was right; it binds my findings too. **F2
is a SEPARATE proposal needing its own four-postulate record. This certification does not pre-approve
it.**

## 7. CONSEQUENTIAL ACT ON ADOPTION — THE `FAIL` AUDIT, AND ITS DENOMINATOR IS SMALL

The proposal's sharpest argument is that a missing member **recruits the nearest wrong one, and here
that member ACCUSES THE WORK**: `0.4.0_DS_ClientPlatform~P` chose `FAIL` for ETFS_INGEST TO-6 AC3 as
"the only literally-true option", writing a false failure into the permanent record.

**Measured: there are 18 `FAIL` rows in 1,258. At least one is a self-declared false failure. Nobody
downstream can distinguish it from a real one — that is the whole hazard.**

>> **18 is small enough to audit by hand.** Recommend the adoption act carry a sweep of all 18 for
   other recruited-`FAIL` rows. **I am NOT claiming a rate** — I have measured the population and
   examined none of the other 17. A false-failure count would need each read at source.

## 8. WHAT THIS CERTIFICATION DOES NOT DO

- Does **NOT** adopt. No schema file is modified by this document.
- Does **NOT** close `D1_CATVIEWS.TO-I1-DS`. Its face says do not close on this proof instance; that
  stands, and F1/F2 mean the instance would still be invalid after this member alone.
- Does **NOT** touch `UNCOMPUTABLE` vs `UNCOMPUTABLE-BY-CONSTRUCTION` (the proposer's s.3 strain).
- Does **NOT** name the schema owner. That is the adoption blocker and it is an open item.

---

— `3.0.0_SA_CVO~Z`
