# RULE-24 RECORD — `closure_reason` (D7 ticket terminal dispositions)

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~21:05Z · **Status:** AUTHORED, awaiting `3.0.0_SA_CVO~Z` second read
**Shape ruling:** @`21bd23d943` §2a (two-field split) · **CE input consumed:** `3.0.0_SA_CVO~Z` 2905 @`97e58b0c14`
**Plane:** canonical tree @`123071c5cd`. Source citations verified at HEAD with positive + negative controls (below).

---

## 0. A CORRECTION TO MY OWN SHAPE RULING, forced by CE finding (3)

§2a said `status` gains *"exactly ONE new terminal value for **ended without fulfillment**."* **That name is
wrong, and adopting `superseded` is what exposes it** — a superseded ticket **was** fulfilled, just not
through this ticket. Naming the status for *unfulfilled* would have made the ratified value unrepresentable
on the axis built to hold it.

> **CORRECTED: the new `status` value is `closed` — terminal, NOT completed *through this ticket*.**
> `closure_reason` then explains why it closed without going through completion. The two-field split is
> unchanged; only my name for the new value was wrong.

---

## 1. DECLARED LAYER (CE finding 3 — declared BEFORE the members, because the layer decides the list)

> **Every reason a ticket reaches a terminal state OTHER THAN completion through this ticket.**

`3.0.0_SA_CVO~Z` named three candidate layers and was right that they enumerate differently. I am choosing
this one over *"ended without the requester getting what they asked for"* precisely **because** that
alternative would exclude `superseded` — and excluding it is the gap CE finding (1) exists to close. The
layer is chosen to match what `status` actually partitions.

---

## 2. THE MEMBERS

| Value | Meaning | Mandatory pointer |
|---|---|---|
| `superseded` | **The need was MET ANOTHER WAY** — answered in-thread, resolved by an adjacent ticket, artifact appeared by another route | **YES — name what met it** |
| `duplicate` | **The SAME request** is already tracked by another ticket | **YES — the canonical ticket id** |
| `withdrawn` | The requester ended it; **the need went away** | no |
| `out_of_scope` | Opal declines the work | no |
| `expired` | The requester never responded and it aged out | no |
| `disputed` | Opal did the work, the requester rejects the outcome, **and Opal will not continue** | no |

### 2a. `superseded` is REUSED, NOT RE-COINED — and that is the strongest finding in the set

**Verified at source, not relayed** (`org/XXX.md:520` and `org/ref/TASK_ORDER_PROTOCOL.md:290-291,297`,
Andrew-direct 2026-08-07; positive control = 4 occurrences in the protocol, negative control = 0):

> `superseded` = **the NEED WAS MET ANOTHER WAY** (name what superseded it)
> `cancelled` = **the NEED WENT AWAY** (cite the ruling)
> *"**KEEP THE TWO DISTINCT — they differ on RE-OPEN, which is the only time it matters.** `superseded`
> means the outcome was achieved; re-opening asks 'is the replacement still standing?' `cancelled` means
> the outcome is unwanted; re-opening needs a **fresh authorization**."*

**My original four covered client-withdrew, timed-out and Opal-declines, and had NO member for *"the request
was satisfied, just not through this ticket."*** On live-beta traffic where the same analyst answers in the
Teams thread **and** on the board, that is not an edge case — it is likely the **common** ending.

**And the ratified rationale is load-bearing in this schema specifically, not merely applicable:** the
distinction matters *only* on re-open — and §3 of @`21bd23d943` rules **REOPEN into this very wave.** The one
condition under which the distinction pays is being built alongside it. Re-coining beside a ratified term
would also be the build-ladder rung-2 duplicate the Rule-24 granularity amendment names.

**`withdrawn` is the `cancelled` half**, named for this domain's actor. The ratified pair maps cleanly:
`superseded` transfers verbatim; `cancelled` splits by *who* the need went away for (`withdrawn` = requester,
`out_of_scope` = Opal declines).

### 2b. The self-named gap SPLITS, and only one half is terminal (CE finding 2)

My §2a flagged *"Opal did the work and the requester rejects the outcome."* It is two things:

- **(a) rejects and wants more → NOT TERMINAL.** That is the **REOPEN trigger**, and it belongs on §3's
  requester-class MATRIX action, not here.
- **(b) rejects and Opal will not continue → TERMINAL, genuinely uncovered.** Adopted as **`disputed`**.

**Adopting it undifferentiated would have put a NON-TERMINAL state on a TERMINAL axis** — the same flattening
the split was ruled to prevent, arriving as a *"known gap"* rather than as a value. Naming the split was the
whole remedy.

---

## 3. FOUR-POSTULATE TEST

**(i) MECE — against the declared layer.**
*Mutual exclusion:* one value applies at the moment of termination. **The one real seam is `duplicate` vs
`superseded`**, and I am naming it rather than hoping: both can describe "resolved elsewhere."
**TIE-BREAKER, which makes it decidable:** if **another TICKET carries the same request** → `duplicate`
(ticket identity). If the **need was met without a ticket carrying that request** → `superseded` (need
satisfaction). Two different questions; the tie-breaker picks one.
*Collective exhaustion — hunting the uncovered member, per the CE half:* **`created_in_error`** (a row
created by mistake — internal test rows, mis-clicks) has **no home**. A requester's mistake is `withdrawn`;
**Opal's own mistaken row is uncovered.** ⚠ **NAMED, NOT ADOPTED** — I am flagging it for the second read
rather than silently adding a seventh value, because whether an erroneous row should be a *closure reason*
or should never reach a terminal state at all is a genuine design question I have not settled.

**(ii) SAME GRAIN.** Every value is a reason at the grain of **one ticket's termination**. No cohort-level or
program-level value sits on the axis.

**(iii) INTENT COHERENCE — one axis, one intent: WHY.**
The actor is deliberately **absent from every value**, per §1 of @`21bd23d943` (actor derives from
`events[]`). ⚠ **I applied the sharper test — is a second axis hiding inside a value's WORDING?** `withdrawn`
implies the requester; `out_of_scope` implies Opal. **The discriminating question is whether either value
could be reached by EITHER actor** — because if so, the wording would be encoding actor as a hidden
dimension. It cannot: Opal cannot `withdraw` (that is `out_of_scope`), and a requester cannot declare
`out_of_scope`. **The actor is a FUNCTION of the reason, not an independent axis**, so intent coherence
holds and the actor stays derived.

**(iv) STATE COHERENCE — the stability frame.** Every value is an attribute on a **non-key** field, so adding
any later is the identical cheap act: **one remedy moves them all.** ⚠ **This postulate passes *because of*
the shape ruling** — on a single-axis design where these were `status` values, they would sit on the **GSI
hash key** and adding one later would be a partition-key migration. **The split is what makes (iv) pass.**

---

## 4. TOKEN-HYGIENE CENSUS — run, not claimed

Word-boundary occupancy over the canon (`CLAUDE.md`, `org/XXX.md`, `org/ref/TASK_ORDER_PROTOCOL.md`,
`docs/doctrine/CONTROLS_OVER_CARE.md`; denominator = 4 files, all present; negative control = 0):

```
superseded        11      <- COLLISION, deliberate (see below)
duplicate          5      <- collision, benign (generic English usage, no ratified enum)
expired            1      <- benign
withdrawn          0
out_of_scope       0
disputed           0
closure_reason     0
created_in_error   0
```

⚠ **THE `superseded` COLLISION IS THE POINT OF THE CENSUS, AND IT IS HANDLED DELIBERATELY.** Eleven hits,
and they are the **ratified TASK-ORDER status** — the same word on two schemas, in the same week that
`WITHDRAWN` landing on two schemas drew a warning from both `2.0.0_SA_COO~Z` and `3.0.0_SA_CVO~Z`.

**Applying my own banked test — NAME THE REMEDY:** TO-`superseded` is fixed by a COO/issuer **status flip on
a task order**; ticket-`superseded` is fixed by an **API state transition on a ticket row**. Different acts,
different surfaces → **different axes wearing one word.**

**So why adopt it here when we warned against copying `WITHDRAWN`?** Because the two cases differ on the
thing that matters: **`WITHDRAWN` was warned against because copying it would have caused the ticket axis to
UNDER-COVER** (the memory axis had no "Opal withdrew" counterpart, for a reason that does not hold here).
**`superseded` is the opposite — its SEMANTICS transfer exactly**, Andrew ratified that meaning, and
declining to reuse it would be re-coining beside a ratified term. **Reusing a ratified term with its ratified
meaning at a declared different grain is rung 2; copying a term whose singularity was axis-specific is the
defect.** The grain is declared here so a future reader cannot cross-cite the two filings.

---

## 5. THE POINTER IS PART OF THE VOCABULARY (CE finding 4)

`org/XXX.md:520`, verbatim: ***"a terminal status without its pointer is the rot with a tidier label."***

**RULED: the pointer is a PER-VALUE FIELD REQUIREMENT**, enforced at the transition write — `superseded` MUST
name what met the need; `duplicate` MUST carry the canonical ticket id. A pointerless `duplicate` is that rot
**and W-C makes it client-facing**: the client sees their request marked duplicate **with no path to where it
actually lives.** **The client projection MUST carry the pointer for any value that has one.**

---

## 6. INTERNAL-RECORDED IS NOT CLIENT-RENDERED (CE finding 5) — the sharpest catch in the set

**My split fixed the INTERNAL record and left the CLIENT-FACING defect exactly where it was.** The client
tabs are Open / In Progress / Completed, and **a second terminal `status` value has no tab.** Rendered under
Completed, a `withdrawn` or `out_of_scope` ticket **still reads to the client as resolved** — the original
P0, now with better internal data behind it.

**RULED — the CORRECTNESS constraint, which is mine:**
1. **A `status=closed` ticket MUST NOT render under Completed.**
2. **It MUST NOT carry an AI resolution summary** — an AI summary of a resolution that never happened is
   precisely the P0's harm. **The single exception is `superseded`**, where an outcome genuinely was
   delivered: there the summary **and its pointer** are truthful and useful.

**CARDED TO ANDREW — the PRODUCT decision, which is his:** the client-facing **tab label** for the closed
state, and whether a client sees `closure_reason` at all or only the tab. Per @`21bd23d943` §2, what a client
sees is his enumeration (C2/C3/C4) and I do not widen it. **I rule that it must not read as resolved; I do
not rule what it reads as.**

---

## 7. WHAT THIS RECORD DOES NOT DO

It does not adopt. **`3.0.0_SA_CVO~Z` holds the second read**, and their boundary is right: the record is my
authoring act, the verification is theirs. Two items are flagged **for** that read rather than settled:
**`created_in_error`** (§3(i)) and the **`duplicate`/`superseded` tie-breaker** (§3(i)) — both are places
where I would rather be checked than be confident.
