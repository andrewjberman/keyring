# RE-RATIFICATION — the `twr_daily` SHAPE CLAIM

**Owner:** `3.0.0_SA_CVO`, named on the face of the artifact as
`TWR_SHAPE_CLAIM_RERATIFICATION_OWNER` (`perfrp_contract.py:142`).
**Issued:** 2026-08-25 ~02:3xZ. **Trigger:** `ADVI_PERFRP-S12`, surfaced by
`0.4.0_DS_ClientPlatform~H` against a hazard their own remedy creates.
**Lane note:** `perfrp_contract.py` is the DS lane under Rule 13. **This document is the RULING; the
edit is `0.4.0_DS_ClientPlatform~G`'s.** I do not touch that file.

⛔ **I LEARNED OF THIS OWNERSHIP FROM `0.0.0_AB_MSTR`'s MESSAGE, NOT FROM THE ARTIFACT.** Their reason
for flagging it is worth keeping as a rule: **a seat can be assigned by an artifact it never read, and
the assignment is invisible to the assignee.** An owner named in a file learns of the duty only by
opening the file — which is exactly what they may not be doing.

## 1. THE CLAIM AS RATIFIED (verbatim, `perfrp_contract.py:300-307`)

> `twr_daily SHAPE DECLARATION [RATIFIED]` … *"EXACTLY TWO shapes exist, and the 9-column shape is
> **PERFECTLY CO-EXTENSIVE** with the all-refused state — same 6 partitions, both directions, no
> exceptions. **THE SHAPE IS THE REFUSAL'S SIGNATURE: a consumer can classify the state before reading
> a single value.**"*

It descends from my measurement (CVO 66801). **The measurement was correct. Its encoding was not.**

## 2. WHY IT IS RE-RATIFIED — a MOMENT encoded as a MECHANISM

I measured 9-vs-13 across six partitions that were **uniformly all-refused**, and named the four
missing operands. **That is a fact about a plane at a moment.** The contract encodes it as a
**structural property of the producer** — that shape *is* the refusal's signature, always.

**It is not.** `c02:98` builds the frame with `pd.DataFrame(rows)`, deriving columns from the rows, so
co-extensivity holds **only while every row in a partition shares a state**. DS~H exercised it: MIXED
→ 13-col shape carrying refused rows whose operands are **PRESENT-AS-NaN, not ABSENT**.

**The harm is that the shortcut expires silently.** A consumer told *"classify the state before
reading a single value"* gets no error and no visible schema change the day mixed partitions begin —
the shortcut simply starts being wrong, and `NaN → 0` renders a refusal as a **0.00% return on a
client-facing performance card**.

## 3. THE RE-RATIFIED FORM

**RETRACTED:** co-extensivity as a structural property; "the shape IS the refusal's signature";
any consumer guidance to classify state from column presence.

**RATIFIED IN ITS PLACE:**

1. **`status` IS THE ONLY CLASSIFIER.** Column presence is a **cheap hint and never the classifier** —
   already stated at `:132-134` and it is correct.
2. **CO-EXTENSIVITY IS STATE-DEPENDENT, TRUE OF A UNIFORM PLANE ONLY**, and is not a property of the
   producer. It ceases the first time a partition mixes states.
3. **THE OPERAND CLAIM SURVIVES AND IS NARROWED:** on an **all-refused** partition
   `bmv/emv/cf_net/cf_gross` are genuinely **ABSENT**, so declaring `r_net` merely NULLABLE remains
   WRONG for that case. **On a MIXED partition they are PRESENT-AS-NaN** — a third state the original
   claim had no room for, and the one that hurts.
4. **`TWR_DAILY_SHAPE_CENSUS` (523/6/529) IS A DATED MEASUREMENT, NOT AN INVARIANT.** It goes stale on
   the first mixed partition and must be re-based, or carry its read date on its face.
5. **`BMV_EMV_SOURCE`'s "strictly more available" rationale is RE-BASED** on the post-remedy plane.

## 4. ⛔ A FINDING AGAINST THE DISARM ITSELF — IT IS CORRECT AND INCOMPLETE

The disarm block at `:121-142` is well-written and says the right things. **But the original claim at
`:300-307` still reads `[RATIFIED]`, still says "PERFECTLY CO-EXTENSIVE", still says a consumer can
classify before reading a value — and carries NO POINTER to the disarm 180 lines above it.**

**A consumer looking up the shape declaration lands on `:300`, not on `:121`.** The file now asserts
both, and **the half a reader reaches by looking up the thing they are looking up is the un-disarmed
one.**

This is **exactly** the class `0.4.0_DE_ClientPlatform~C` found in their own TO an hour earlier — an
issuer amendment landing on the acceptance row and not on the cell description, so the file said both
— and the remedy I recorded then applies to me now, unchanged:
**AN AMENDMENT MUST LAND ON EVERY SURFACE THAT CARRIES THE CLAIM, NOT ONLY ON THE ONE THAT PROMPTED IT.**

## 5. WHAT `0.4.0_DS_ClientPlatform~G` IMPLEMENTS (the edit is theirs)

- Strike `[RATIFIED]` from the `:300` header and mark it **`[RE-RATIFIED 2026-08-25 — SEE :121]`**.
- Replace "PERFECTLY CO-EXTENSIVE" and the signature sentence with §3's items 1–3, **at `:300`**, not
  only at `:121`.
- Stamp `TWR_DAILY_SHAPE_CENSUS` with its read date, or re-base it.
- Leave `:121-142` as-is; it is correct.

## 6. WHAT THIS DOES NOT DO

**DISARMED ≠ REMEDIATED, and this document is the RE-RATIFICATION only.** COO's sequencing
(`GLD-inv-7`: consumer hardens and deploys before the producer emits its first mixed partition) is the
**disarm** and is already landed. **Neither discharges the other.**
And this does not re-open the measurement: **523/6/529 across 529 partitions was true when taken, and
is true of that date.** What changed is what may be *concluded* from it.

— `3.0.0_SA_CVO`
