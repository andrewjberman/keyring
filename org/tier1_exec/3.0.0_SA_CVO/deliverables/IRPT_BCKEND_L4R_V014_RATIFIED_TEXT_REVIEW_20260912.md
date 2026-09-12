# IRPT_BCKEND v0.14 — L4-R ratified-text review

**Reviewer:** `3.0.0_SA_CVO`. **Date:** 2026-09-12 UTC. **Archetype:** VALIDATE.
**Subject:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` v0.14 @`b8e98d5a4d`
**Trigger:** `1.0.0_SA_CTO` msg 96061 — a GENUINE semantic re-review, not a re-stamp.

## Verdict: **SIGNED**

One finding is raised and it is **adjacent to this half, not inside it**, so it does not carry a refusal. It is
stated in full at the end because it is a provenance defect of exactly the class this seat flagged earlier tonight.

## What actually moved

`git diff e6ba5d9878 b8e98d5a4d` on the PRD is **two lines**: the `prd_version` header and the CONTRACTS row
`StatusEnvelope`. **The ENDPOINT section did not move**, so its limb of this seat's v0.13 signature stands on
unchanged bytes rather than being re-asserted.

## The four clauses of the RATIFIED-TEXT half (spine `:164-167`), each graded

**1. ENDPOINT verbatim from the ratified pins — HOLDS.** Unchanged at these bytes; nothing in the diff touches it.

**2. Every operative constraint present — HOLDS, and the row is a SUPERSET.** The prior row's six items all survive
verbatim (`operation + revision`; the nine states; `source dates`; `safe retry/recovery actions`;
`public reason code`; `internal correlation id`). The amendment EXPANDS item 3 and removes nothing.

**3. No annotation, history or seat name inside the SECTION — HOLDS.** The added text is contract prose. No serial,
no date, no message id, no "per ruling" — nothing that would trip the gate's `_top_section` rule.

**4. The CONTRACTS section agrees with the counterpart PRD — HOLDS, and this is the clause the re-review existed
for.** Checked at source over a PRINTED DENOMINATOR rather than at the one row: **212 lines of
`IRPT_FNTEND_PRD.md` scanned, 7 hits** for `StatusEnvelope|source[ _-]?date|business[ _-]?date|source age`.
Dispositioned individually:

| FNTEND line | content | disposition |
|---|---|---|
| 120 | `` | `StatusEnvelope` | consumed | F7, F12 | `` | **no field-level promise** — the row `1.0.0_SA_CTO` quoted, confirmed verbatim |
| 98 | F7 "per-tab lifecycle states, **source ages**, late-response rejection" consuming `C StatusEnvelope` | names the RENDERING duty, promises no presence |
| 99 | F8 consumes `StatusEnvelope` | no field promise |
| 96, 97, 116 | F5 / F6 / `AnalysisRequest`-`AnalysisReport` rows | not `StatusEnvelope` field promises |
| **57** | "IRPT_BCKEND supplies the StatusEnvelope states and **the as-of / revision each result carries**" | **the nearest thing to a contradiction, and it does NOT contradict — see below** |

⭐ **LINE 57 IS NAMED EXPLICITLY BECAUSE A LATER READER WILL FIND IT AND COULD WEAPONISE IT.** Read carelessly,
"the as-of / revision **each result** carries" asserts that every envelope carries an as-of, which the new rule
denies for four states. It does not, and the discriminator is the word **RESULT**: `QUEUED`, `RUNNING`,
`UNAVAILABLE` and `FAILED` are the states in which **no result exists** — they are the absence of a result, not a
result lacking a field. The sentence is scoped to results and the amendment only relaxes non-results, so the two
are consistent. **This is a reading, and it is recorded as a reading so that it can be overturned by argument
rather than rediscovered as a surprise.** `1.0.0_SA_CTO`'s check was scoped to the CONTRACTS row; this line sits
outside it and is the reason the agreement clause is checked against the counterpart PRD as a whole.

## The amendment's own taxonomy — checked, not taken

The enum prints **nine** states. Answer-bearing named: `READY, PARTIAL, STALE, NEEDS_CORRECTION, UNCERTAIN` = 5.
No-answer: `QUEUED, RUNNING, UNAVAILABLE, FAILED` = 4. **5 + 4 = 9, exhaustive by subtraction from the printed
denominator**, which is Rule 24's requirement and is why `QUEUED`/`RUNNING` — neither of them refusals — are
covered by an amendment that arose from a question about refusals.

`business_date` is typed `"string"` and NOT `["string","null"]`, so **absent-never-null is enforced by the type
and not merely by the prose.** `source_dates` stays in the top-level `required` array, so no consumer branches on
the key's existence. Both match the row's text.

## FINDING — adjacent to this half, and NOT a reason to refuse it

⛔ **The generated `docs/contracts/investor-reporting/v1/StatusEnvelope.schema.json` declares
`x-contract.source_pin: "62301f71e0"`, and the rule it now encodes DOES NOT EXIST AT THAT PIN.**

MEASURED, with a positive control so the zero is a measurement:
- `git show 62301f71e0:...IRPT_BCKEND_PRD.md | grep -c 'business date is REQUIRED'` → **0**
- `git show b8e98d5a4d:...IRPT_BCKEND_PRD.md | grep -c 'business date is REQUIRED'` → **1** (the grep works)
- that pinned document declares `"prd_version": "v0.4"` — **ten versions behind the amendment it now carries**

Every property `description` in the schema also cites `@62301f71e0`. The schema's own contract is that "a property
whose quoted source string does not appear in that section at the pin is a fabrication and is refused by the
IB-s-18 battery" — and the battery still PASSES, because the quoted strings are the six ITEM labels
(`"source dates"` etc.), which do appear at v0.4. **So the check the schema names for itself cannot see this: the
strings resolve, the RULE does not.** A later reader resolving the pin to verify the business-date conditional
finds a bare `source dates` and no conditional at all.

**WHY THIS IS NOT A REFUSAL:** this half is the PRD's ENDPOINT + CONTRACTS sections. The generated schema is a
different artifact and is not the object this signature covers. The PRD row — what I sign — is sound. Refusing
the half over an adjacent artifact would be the manufactured friction `1.0.0_SA_CTO` was right to avoid, and
would flip a live round to WITHHELD for a defect that is real but elsewhere.

**OWNER:** `1.0.0_SA_CTO` as the L4 owner and generator of record. **REMEDY:** regenerate with `source_pin`
`b8e98d5a4d` (or whatever pin carries the row at generation time) so the provenance resolves. **CLASS:** the same
one this seat closed twelve of in the step logs six hours ago — a citation that looks pinned, reads as diligence,
and resolves to the wrong vintage. There it was `@HEAD` on untracked carriers; here it is a stale pin on a
tracked one. ⛔ **The generator will re-introduce it on every future amendment unless the pin is derived at
generation time rather than carried**, which is the part worth fixing rather than the one instance.

## Scope limits, stated

This review covers the PRD's ENDPOINT and CONTRACTS sections at `b8e98d5a4d` and the counterpart agreement against
`IRPT_FNTEND_PRD.md` at HEAD. It does NOT grade the 11-of-11 validator exercise `1.0.0_SA_CTO` reports (not re-run
here, and its claim is accepted as the L4 owner's own measurement, not verified by this seat), does not certify the
IB-s-18 battery obligation the weakening moves, and asserts nothing about any cell's implementation.
