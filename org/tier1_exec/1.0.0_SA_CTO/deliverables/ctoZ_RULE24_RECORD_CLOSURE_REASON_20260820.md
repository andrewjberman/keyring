# RULE-24 RECORD — `closure_reason` (D7 ticket terminal dispositions) — **ADOPTED**

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 · **Status:** **ADOPTED 21:14Z**
**Second read:** `3.0.0_SA_CVO~Z` @`d600f64266` — **VERDICT: PASS, ADOPT**, with one correction required *in* the adopting act (F-A). All of it is folded below.
**Shape ruling:** @`21bd23d943` §2a (two-field split) · **CE input:** @`97e58b0c14` · **v1 authored:** @`1abe7dcba2`

---

## 0. TWO CORRECTIONS TO MY OWN PRIOR RULINGS, folded here

**(a) The `status` value is `closed`, not "ended without fulfillment."** §2a's name was wrong: a
`superseded` ticket **was** fulfilled, just not through this ticket, so naming the status for *unfulfilled*
would have made the ratified value unrepresentable on the axis built to hold it. The split is unchanged;
only my name for the new value was.

**(b) My token census was CASE-SENSITIVE and that hid a third sense of the very token it existed to check.**
I reported `superseded` = 11; `3.0.0_SA_CVO~Z` re-ran it and got **12**. Not an error — a **method defect**.
The extra is **`SUPERSEDED` at `org/XXX.md:403`**, the law-file convention for a **struck clause** — neither
the TO status nor this value, a **genuine third sense**.

> **RULED as method, going forward: a token-hygiene census is CASE-INSENSITIVE. The hazard is SEMANTIC
> occupancy, not string occupancy.** No enum collision; verdict unchanged.

---

## 1. DECLARED LAYER

> **Every reason a ticket reaches a terminal state OTHER THAN completion through this ticket.**

Chosen over *"ended without the requester getting what they asked for"* **because** that alternative would
exclude `superseded` — and that exclusion is the gap CE finding (1) exists to close.

## 2. THE MEMBERS — six, all pointer-bearing values pointered

| Value | Meaning | Mandatory pointer |
|---|---|---|
| `superseded` | **The need was MET ANOTHER WAY** — answered in-thread, artifact appeared by another route | **YES** — name what met it |
| `duplicate` | The need was **RELOCATED** to another ticket | **YES** — the canonical ticket id |
| `withdrawn` | The requester ended it; the need went away | no |
| `out_of_scope` | Opal declines the work | no |
| **`requester_unresponsive`** | The requester never responded and it aged out | no |
| `disputed` | Opal did the work, the requester rejects the outcome, **and Opal will not continue** | **YES** — the rejection (message / event id) |

### 2a. ⛔ F-A — `expired` IS RENAMED TO `requester_unresponsive`, AND Opal-side ageout is NOT TERMINAL

**`3.0.0_SA_CVO~Z` ran my own sharper either-actor test on the one value I failed to run it on.** I applied
it to `withdrawn` and `out_of_scope` and stopped. `expired`'s **definition is requester-bound** ("the
requester never responded") but its **NAME is actor-neutral** — and **the escalation sweep I ruled in this
same wave is about OPAL-side ageout.**

> **THE CONCRETE FAILURE:** whoever wires the sweep's terminal handling reaches for `expired` **exactly as
> its name invites**, and the row then says **THE CLIENT WENT SILENT WHEN IN FACT OPAL DID** — an Opal SLA
> failure recorded as client non-response, **on a client-visible axis.**

This is the banked CRO class: **Rule 24(iii) applies INSIDE a value's wording** — the same shape as
*"ACTIVE = operating AS INTENDED"* smuggling a health axis into a life-position enum.

**RULED — BOTH remedies, not one.** `3.0.0_SA_CVO~Z` offered them as alternatives; they close the hole in
independent ways and the second costs one sentence:
1. **RENAMED `expired` → `requester_unresponsive`.** The name now carries the actor its definition always
   had. This is the cheap moment — **nothing has encoded it yet**, which is exactly why the second read was
   timed same-act rather than as a follow-up.
2. **STATED, because the record is what the implementer reads: OPAL-SIDE AGEOUT IS NOT TERMINAL.** Nobody
   picked it up → it **stays open** and is the escalation sweep's subject. My NOBODY-FORCE-COMPLETES interim
   already implied this; **implying is not saying.**

### 2b. THE TIE-BREAKER — REPLACED. Mine mixed dimensions.

> ~~If another TICKET carries the same request → `duplicate`; if the need was met with no ticket carrying it
> → `superseded`.~~ **— MINE. REPLACED.**

**It keyed a STRUCTURAL fact (does another ticket exist) against two values that differ SEMANTICALLY (was
the need met).** Decidable, never deadlocks — **and it misfires on the case this record handles best**: an
analyst answers in-thread **and** an adjacent ticket exists → both conditions fire → ticket-identity wins →
marked `duplicate` → and its **mandatory CLIENT-FACING pointer sends the client to a ticket that will itself
close as `superseded`.** **A pointer chain to nothing, on the one value whose pointer the client sees.** It
also works against the ratified rationale the adoption rests on, since the pair differs **on re-open** and a
structural key routes to the wrong re-open question.

> **ADOPTED — same dimension for both: was the need SATISFIED (`superseded`) or merely RELOCATED to another
> ticket (`duplicate`)?**

Tested against my own cases: duplicate-of-still-open-TCK-B → same answer; answered-in-thread-with-no-other-
ticket → same answer; **answered-in-thread-WITH-an-adjacent-ticket → differs, and gives the better answer**,
because *"is the replacement still standing?"* is the question worth asking there. Both pointer requirements
survive unchanged.

### 2c. `disputed` GAINS A MANDATORY POINTER — the unknown-unknown, adopted

**`disputed` is the only member that asserts a claim about the CLIENT'S STATE OF MIND, and it was the only
evidence-bearing value with no mandatory pointer.** `superseded` and `duplicate` must name their referent
because **a claim about the world needs one**; `disputed` is **a claim about a PERSON**, is client-visible
under W-C, and was assertable with nothing cited. **It now carries a pointer to the rejection (message or
event id)** — same reason as the other two and a stronger one: **it is the one value a client could read and
disagree with.**

### 2d. `created_in_error` — NOT ADOPTED, and the fork recorded so nobody re-derives it

**Not a coverage question — a postulate (iii) question.** Every other member answers *"why did this REQUEST
end without completion here"*; this answers *"was there a request at all."* **The six are statements Opal
makes about A CLIENT'S REQUEST; this is a statement Opal makes about ITS OWN DATA.** A data-quality event
does not belong on a lifecycle-outcome axis.

**Reachability supports it:** `requester` is **server-derived**, so an internal test row's requester is the
internal actor, and **W-C's READ-OWN filter makes such a row structurally invisible to any client.**

⚠ **THE HONEST BOUND, recorded rather than hidden:** that covers test rows and mis-clicks. It does **not**
cover **an analyst mis-filing ON BEHALF OF a client via CREATE**, which **is** client-visible. Read: that
case is `withdrawn` or `out_of_scope` on its merits — **and if it is neither, it is the single case that
would justify a seventh value.** Recorded as a fork, not a gap.

---

## 3. FOUR-POSTULATE TEST

**(i) MECE.** Mutual exclusion holds on the §2b dimension (satisfied vs relocated vs the four non-delivery
reasons). Collective exhaustion against the declared layer: the CE hunt produced one candidate
(`created_in_error`), adjudicated **off-axis** at §2d, with its one surviving fork named.

**(ii) SAME GRAIN.** Every value is a reason at the grain of **one ticket's termination**.

**(iii) INTENT COHERENCE — one intent: WHY.** Actor is absent from every value and derives from `events[]`.
**The either-actor test is now run on ALL SIX**, not four: `withdrawn` (requester only — Opal cannot
withdraw; that is `out_of_scope`), `out_of_scope` (Opal only), **`requester_unresponsive` (requester only —
fixed by F-A; Opal-side ageout is not terminal at all)**, `superseded`/`duplicate`/`disputed` (Opal records
the disposition). **The actor is a FUNCTION of the reason, not an independent axis.**

**(iv) STATE COHERENCE.** Every value is an attribute on a **non-key** field, so one remedy moves them all.
⚠ **Passes BECAUSE OF the shape ruling** — on a single-axis design these would sit on the **GSI hash key**
and adding one later would be a partition-key migration.

---

## 4. WHY `superseded` IS IMPORTABLE AND THE MEMORY SET'S `WITHDRAWN` WAS NOT

I asked `3.0.0_SA_CVO~Z` directly whether adopt-here / warn-there holds. **It holds — but my stated reason
was wrong in a way that would license a wrong move, and the reason is what gets carried forward.**

> ~~My test: "ratified + declared different grain = rung 2."~~ **INSUFFICIENT.** `TO-pending` is equally
> ratified, and adopting it for a ticket at a declared different grain would be wrong — **my test as stated
> passes it.**

> **THE ACTUAL DISCRIMINATOR — WHAT PROPERTY YOU IMPORT:**
> **A term's MEANING can transfer across axes. A term-set's COMPLETENESS never can.**

**Cheap test for the first — state the definition without naming its home axis.** *"The need was met another
way"* survives with no axis named → **portable**. *"Active, GO given"* cannot be stated without the TO
lifecycle → **not portable**.

**And the `WITHDRAWN` warning was never about copying a TERM.** It was against importing the memory set's
**CE property** — *"these four cover it there, so they cover it here"* — and **CE is evaluated against the
DECLARED LAYER by construction, so it is axis-bound and can never transfer.**

**The two were never in tension: one imports MEANING, the other would have imported COMPLETENESS.** This is
the companion to the banked **NAME-THE-REMEDY** test, and it is the formulation that generalizes.

---

## 5. THE POINTER IS PART OF THE VOCABULARY

`org/XXX.md:520`, verbatim: ***"a terminal status without its pointer is the rot with a tidier label."***
Per-value field requirement enforced at the transition write, and **the client projection carries the
pointer for any value that has one** — a pointerless `duplicate` means the client sees their request marked
duplicate **with no path to where it actually lives.**

## 6. INTERNAL-RECORDED IS NOT CLIENT-RENDERED

**My split fixed the internal record and left the client-facing defect where it was.** Client tabs are
Open / In Progress / Completed; a second terminal `status` has **no tab**, and rendered under Completed a
`withdrawn` ticket **still reads to the client as resolved** — the original P0 with better internal data
behind it.

**RULED (correctness, mine):** a `status=closed` ticket **MUST NOT render under Completed**, and **MUST NOT
carry an AI resolution summary** — an AI summary of a resolution that never happened is precisely the P0's
harm. **Sole exception `superseded`**, where an outcome genuinely was delivered and the summary + pointer
are truthful.

**CARDED (product, Andrew's):** the client-facing **tab label**, and whether a client sees `closure_reason`
at all. **I rule that it must not read as resolved; I do not rule what it reads as.**

---

## 7. PROVENANCE NOTE — this record's own adopting COMMIT MESSAGE is corrupted; the record is not

⛔ **F-010 FIRED IN THE ADOPTING COMMIT @`f834702451`, AND IT IS A VARIANT THE RULE AS WRITTEN DOES NOT
COVER.** This note lives in the file rather than in a commit message for the same reason CLAUDE.md's own
F-010 provenance note does: **the commit history is the thing that is misleading.**

**The content below is INTACT** (verified: 4 occurrences of the old token, 4 of the rename, negative control
0) because this file was authored with the Write tool. **Only the commit message is damaged**, and it cannot
be rewritten — shared branch, NEVER#7 forbids rebase.

**What happened:** the message body wrapped a value name in **backticks** as markdown emphasis, and I piped
the body through **`printf` with DOUBLE-QUOTED arguments**. The shell performed **command substitution at
FILE-BUILD time** — it executed the token, the command did not exist (two `command not found` lines on
stderr), and **spliced the empty output into the file.** The committed line reads
*"withdrawn and out_of_scope and stopped.  is DEFINED requester-bound"* — **the sentence explaining which
value failed the test no longer names the value.**

> **THE VARIANT: F-010 prescribes `-F <file>` because *"-F routes the body into a file the shell never
> parses."* I USED `-F`. That flag protects the COMMIT INVOCATION and says nothing about how the FILE IS
> BUILT — I let the shell parse the content one step earlier, so `-F` protected the step that was already
> safe.**
>
> **A rule that names its remedy by the FLAG rather than by the PROPERTY leaves the property reachable from
> another direction.** The property is *the body is never shell-parsed, at any step* — not *pass `-F`*.

**Why it bit here and not on the six earlier commits this session:** those built their message files with
the **Write tool**, which does no shell parsing at all. On the seventh I switched to `printf` for speed.
**The ordinary shape of this class is abandoning the safe tool for a faster one late in a long session** —
not an exotic input.

⚠ **AND THE LOUD FAILURE WAS LUCK, NOT SAFETY.** It surfaced only because the token happened not to be a
command. **`date`, `pwd`, `whoami`, `ls` would have silently spliced real stdout into the permanent
record with no stderr at all** — which is exactly why CLAUDE.md says historical incidence of this class is
**unknowable**.

**Corrected practice at this seat:** message files are authored with the **Write tool** or a
**single-quoted** heredoc. Never double-quoted `printf`, never a double-quoted heredoc, **regardless of
whether the commit uses `-F`.**

---

## 8. ADOPTION

**ADOPTED** on `3.0.0_SA_CVO~Z`'s PASS, with F-A landed as **both** remedies, the tie-breaker replaced, the
`disputed` pointer added, `created_in_error` adjudicated off-axis, and the census method corrected.
`2.0.0_SA_COO~Z` and `0.5.0_AE_OpalETL~Z`: **the hold lifts — W-C's tab mapping and W-D's filing may now
encode these six.** The interim **NOBODY FORCE-COMPLETES** continues to bind until the values are live.
