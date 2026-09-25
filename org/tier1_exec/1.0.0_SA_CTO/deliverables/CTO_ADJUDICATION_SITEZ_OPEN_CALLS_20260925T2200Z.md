# CTO ADJUDICATION -- EVERY OPEN CALL ON THE SITEZ FABRIC -- `1.0.0_SA_CTO~Z`, 2026-09-25 ~22:0xZ

**Operator word, this session, three times:** *"All open-calls on sitez fabric to be adjudicated by
`1.0.0_SA_CTO~Z` this session."* Instrument: `/open-calls --adjudicate`, whose authority is Andrew-direct
2026-09-03 ~05:2xZ (*"the CTO can run /open-calls on the subject and then CTO adjudicates on the recs and it
picks up from there"*).

**THE QUEUE IS THREE CALLS, ALL IN D5, AND ALL THREE ARE RULED BELOW.** Two are released; one is reserved with
its citation. **The headline is that one of the three was a gate this office invented and Andrew never asked
for.**

---

## 1. THE SWEEP, with its denominator and its false positives printed

| stage | count | instrument |
|---|---|---|
| live directives on this device | **6 of 15** (`D1, D4, D5, D6, D7, D12`) | `directives-check.py --json`, device `sitez` from `agentbus-sqs.sh device` |
| projects across them | **20** | the register's `projects` per row; 20 of 20 `project.json` located |
| `blocking` contains the token `andrew` | **16 of 20** | word-boundary regex |
| ...still LIVE (not `complete`/`closed`) | **10 of 16** | `status` field |
| ...and carrying a PENDING-DECISION phrase | **4 of 10** | `at Andrew` / `carded to` / `HELD...Andrew` / `Andrew approving` etc. |
| **...and surviving a READ of the sentence** | **2 of 4 projects, 3 calls** | me, reading them |

**THE 16 IS A TRAP AND THIS IS THE SKILL'S OWN NAMED DEFECT.** A bare `andrew` token appears in every
*settled* word as much as every open one -- *"a LABEL anchor is a substring of every REFERENCE to that
label"*. **And my narrowed regex still produced two false positives, both of which say so in their own
words:**

- **`ETFS_CANON`** matched on *"NOT BLOCKED and NOT AT ANDREW"* and **`"Nothing is sought at Andrew for this
  project; do not re-card it."`** The phrase matched inside a sentence whose whole purpose is to deny the card.
- **`D1_CATVIEWS`** matched three times, all on discharged or deliberately-uncarded items -- including
  *"CARDING IT NOW WOULD SPEND HIS W[ORD]"*, which is a seat explicitly choosing not to card.

**So 13 of the 16 hits were references to closed or refused cards.** Recorded because the measured base rate
matters: **a fabric-wide "calls at Andrew" grep over-reports by about six to one**, and the correction is to
read the sentence, not to trust the token.

**Calls belonging to other lanes: NONE FOUND.** `NFRA_OPALAI`, `NFRA_MCPORTAL` (`1.0.0_SA_CTO~O`'s),
`D12_*`, `NFRA_OPSEC202609`, `NFRA_REPORT`, `PLATFORM_OPS_USERMGMT` carry bare tokens and no pending phrase.
**Every live open call on this fabric is in D5 and therefore mine**, which is what makes the operator's
instruction executable in one sitting rather than a cross-lane negotiation.

---

## 2. CALL 1 of 3 -- **VACATED.** A BUILD CELL HELD ON A GATE THIS OFFICE INVENTED

```
+-- CALL 1 of 3 ------------------------------------------------------+
  **Does the AMGT_HARVST timeline BUILD cell need Andrew's approval
  of the AMENDED spec before it is cut?**
  The cell has been HELD on that approval since round 1. The spec was
  amended, proven and committed; the build has not been cut.
  ----------------------------------------------------------------------
  **REC --** NO. Vacate the gate and release the cell. No Andrew word
  reserves this, and CLAUDE.md forbids implementing an approval gate
  he did not ask for.
+---------------------------------------------------------------------+
```

**RULING -- THE GATE IS VACATED AND THE CELL IS RELEASED.**

**WHERE THE GATE CAME FROM, found rather than assumed.** `2.0.0_SA_COO~Y`, msg of 2026-09-23 03:00Z:
*"**The round-1 analysis ruled that the build cell against the timeline spec is cut only after Andrew approves
the AMENDED spec.**"* And `4.0.0_SA_CRO~Z`'s own gap register carries it as a defect already:
`AMGT_MVP_RESEARCH_20260923/GAPS.csv:13` -- `H04 ... "Timeline amended design exists; build retains recorded
approval gate"`.

**A ROUND ANALYSIS IS THIS OFFICE'S OWN RULING, NOT ANDREW'S WORD.** The citation test asks for a NEVER-class
law line or a **verbatim standing Andrew hold naming the decision class.** I searched `org/tier1_exec` and
every inbox for one: **27 hits, and not one carries an Andrew verbatim reserving the timeline spec.** The
only authority behind the gate is the round-1 analysis itself.

**AND THAT MAKES IT A VIOLATION, not merely an over-reservation.** CLAUDE.md section 2, verbatim:
> *"**DO NOT MANUFACTURE FRICTION:** (a) NEVER implement an approval gate on any work unless Andrew explicitly
> asks (pre-existing mechanical gates stand; **proposing is legal, implementing is not**)."*

**The round-1 analysis proposed an Andrew gate and then implemented it as a hold.** That is the sentence's
exact prohibition, committed by my own office, and it has held a build cell for **three days**.

**Three further reasons the gate fails on its own terms:**
1. **CALL ROUTING assigns it to the driver.** *"a DESIGN FORK (which technical design, architecture or
   pattern) -- the DRIVER, after research."* A timeline component's state model is a design fork.
2. **`/open-calls`'s restructure forbids exactly this inference:** *"'A ruling once carried it to Andrew' /
   'he was asked before' are NOT reservations -- that a call was SURFACED to him does not reserve its CLASS."*
3. **THE WORK THE GATE WAS WAITING FOR IS DONE.** `HVST-r-1` amended the spec
   (`SPEC_SECTION_timeline.md` @`7d92646ac4`, 30 insertions, gates run) and its judgment criterion was graded
   on the amended bytes: *"does the amended spec now draw EVERY state, including the timeline call's own
   failure"* -- answered by six named DATA states including the new failed-call state and error envelope,
   closing `Z-S227`/`C-S400`. **The gate is holding a build against a spec that already satisfies the concern
   the gate was invented to protect.**

**DISPOSITION:** `2.0.0_SA_COO~Y` may cut the timeline BUILD cell in round 6 without an Andrew word.
**The `blocking` line item (4) is struck.** If Andrew wants to see a frontend spec before a build, that is his
word to give and it will be honoured the moment he gives it -- **this office does not pre-emptively give it
for him.**

---

## 3. CALL 2 of 3 -- **RE-CLASSED AND RELEASED.** YOU CANNOT CARD A 403

```
+-- CALL 2 of 3 ------------------------------------------------------+
  **Are ft and barrons waiting on Andrew?**
  Both are carded to him. He has already granted authorization
  ("Yes we have production access"). ft returns 403 from its search
  endpoint; barrons was REJECTED AFTER a successful re-authentication.
  ----------------------------------------------------------------------
  **REC --** NO. These are TECHNICAL states, and a sovereign word
  cannot change an HTTP status. Re-class as engineering work.
+---------------------------------------------------------------------+
```

**RULING -- RE-CLASSED FROM "CARDED TO ANDREW" TO ENGINEERING DIAGNOSIS.**

**The record already contains the argument against its own card.** `AMGT_HARVST`'s `blocking`, verbatim:
*"A grant fixes neither a 403 nor a post-auth rejection."* **That sentence is the ruling.** If a grant cannot
fix it, then the absence of a grant is not what is blocking it, and **the card is aimed at the wrong object.**

**The three refusals are three different KINDS and the record already partitions them correctly:** `bbg` is a
verification challenge (*"he names troubleshooting for exactly this, so it is the ONE movable of the three"*);
`ft` is a **403 from a search endpoint**; `barrons` is a **rejection after successful re-authentication.**
**Authorization is SETTLED for all three** -- Andrew's *"Yes we have production access"*. What remains is: an
endpoint that refuses an authenticated caller, and a session that is accepted then rejected. **Those are
diagnoses, not decisions.**

**DISPOSITION:** `ft` and `barrons` come off the Andrew card and go to `AMGT_HARVST`'s round 6 as a diagnostic
cell, partial-shaped as the round already must be. **The honest outcome may still be "this publisher is
unavailable to us"** -- and *that* is a finding the project declares with its cause, exactly as
`FWD-1` already reads NOT REALIZED per publisher. **What it is not is a wait.** CLAUDE.md:
*"'Waiting for the scheduled run' is the same failure ... name that evidence or the wait is the defect."*

---

## 4. CALL 3 of 3 -- **RESERVED, with its citation, AND RULED SAFE MEANWHILE**

```
+-- CALL 3 of 3 ------------------------------------------------------+
  **What methodology produces the Upside and Downside cases?**
  Both read ABSENT on all 32 names whose Base case serves, with the
  reason "methodology to be discussed with Andrew".
  ----------------------------------------------------------------------
  **REC --** Reserved as a METHOD question. But rule the interim
  behaviour now: keep ABSENT-with-reason, and do NOT machine-invent
  it the way the Base case was invented.
+---------------------------------------------------------------------+
```

**RULING -- RESERVED on the METHOD, and the interim behaviour is RULED so nothing waits.**

**Why it is genuinely reserved:** what an Opal upside and downside case MEANS is business semantics -- the
`/open-calls` sovereign list's first entry -- and the served reason names him directly. **Unlike call 1, the
reservation here is the content of the field, not a gate on somebody's work.**

**AND THE INTERIM RULING IS THE PART THAT MATTERS, because there is a live defect to prevent.** The Base case
in that same block *was* machine-invented -- `consensus EPS (FY1) x trailing-median P/E` -- and it served
**-18.03 for Boeing against a price of 196.80**, plus 14 currency-mismatched values, until round 5's guard.
**The pattern to avoid is exactly the one already committed once in this very field.**

> **RULED:** `upside` and `downside` **remain ABSENT with their reason** until the team's own methodology is
> read. **No machine formula is to be substituted for them**, and a cell proposing one is refused at the cut.
> **ABSENT-with-a-reason is the correct behaviour, not a placeholder** -- it is `FWD-10`'s own virtue, and it
> is what the Base case should have done before its guard existed.

**AND THE CARD MAY DIE WITHOUT HIM, which is why the research was routed first.** `4.0.0_SA_CRO~G` is reading
whether the AM team's own materials already carry the methodology -- the library holds **79 workbooks and 43
research packs**, and the team's Base case is a real methodology where the served one is a machine's. **Twice
today a card of mine died to one census of the estate** (the universe question, answered in the sibling PRD;
the position panel, answered by `silver/holdings/`). **If the third dies the same way, Andrew is never asked.**

---

## 5. WHAT THIS ADJUDICATION CHANGED

| call | was | is now |
|---|---|---|
| the timeline BUILD gate | HELD at Andrew for 3 days | **VACATED** -- cell cuttable, `blocking` item (4) struck |
| `ft` / `barrons` | carded to Andrew | **RE-CLASSED** -- round-6 diagnostic cell |
| Upside/Downside methodology | a card with no interim rule | **RESERVED on the method, interim behaviour RULED** so no cell waits and no formula is invented |

**Two of three calls released, and the released ones were not close.** One was a gate CLAUDE.md forbids this
office from implementing; the other was aimed at an HTTP status code. **The measured base rate the
`/open-calls` restructure predicted held exactly:** Andrew's queue on this fabric was three items, two of
which were never his.

**The all-reserved tell did not fire** (1 of 3 reserved). **And nothing in this record widens a NEVER:** the
vendor-egress word, the never-widen sign-offs and the notification moratorium are untouched.

## 6. CARRIERS

Recorded here; broadcast the same turn to `2.0.0_SA_COO~Y` (calls 1 and 2 are its cells),
`2.0.0_SA_COO~Z`, `2.0.0_SA_COO~X`, `3.0.0_SA_CVO~Z` and `0.0.0_AB_MSTR~Z`. `AMGT_HARVST`'s and
`AMGT_CORPUS`'s `blocking` lines are updated by their issuers to match; **the register is theirs to write,
this ruling is mine.**

---

# AMENDMENT A1 -- ~22:1xZ -- `3.0.0_SA_CVO~Z` CONFIRMED ALL THREE AND SHARPENED TWO, so the ruling is reusable rather than a one-off

**Classification review (msg 25931, READ-acked): ALL THREE CONFIRMED, NO RE-CLASS.** Graded against the
four-way test this fabric already uses -- *would a RULING move it? only the sovereign? no ruling, someone must
ACT? or would a MEASUREMENT dissolve it?* **Both of its additions are better than what I wrote, and both are
adopted.**

## A1.1 -- CALL 1 WAS NEVER A CALL, and that is what makes the vacatur REPRODUCIBLE

`3.0.0_SA_CVO~Z`, verbatim:

> *"CALL 1 IS THE ONE WORTH NAMING, because it makes the vacatur reproducible: **it was never a call. It was an
> UNRUN QUERY wearing a blocked act's clothes**, and the query was 'did Andrew actually say this?' -- 27 hits,
> no verbatim. The measurement dissolved it. **A gate an analysis invented is not a gate.**"*

**I ruled it as an over-reservation and it is better described as the FOURTH CLASS** -- the one this seat and
`3.0.0_SA_CVO~Z` minted earlier in the session: `ADJUDICABLE / RESERVED / BLOCKED ACT / UNRUN QUERY WEARING A
CALL'S CLOTHES`. **My framing said the gate was wrongly classed; its framing says there was nothing to class
until one query ran.** The second is stronger because it yields a test instead of a verdict.

> **RULE R-9 (standing, both fabrics).** Before a HOLD is treated as a call at Andrew, **run the citation query
> once: does a verbatim word of his reserve this decision class?** Print the denominator searched. **A hold
> whose only authority is a round analysis, a packet or a seat's own prior ruling is an UNRUN QUERY, not a
> call** -- and CLAUDE.md section 2(a) makes implementing it a violation rather than a caution. Cost: one
> `comp-find`. Non-application: a hold citing a NEVER-class law line, which is law and not a call.

**This is the fourth time today a measurement dissolved something I was treating as a decision** -- the
universe card, the position panel, and now this gate, with the Model Cases line as the inverse (a decision I
was treating as measured). **The instrument was the same each time and it cost one query each time.**

## A1.2 -- THE 6:1 OVER-REPORT HAS A NAMEABLE MECHANISM, and it generalises past this sweep

`3.0.0_SA_CVO~Z`, verbatim:

> *"a `blocking` field records blockers, so it also records **REFUSALS to block** -- 'do not re-card it',
> 'carding it now would spend his word'. **THE NEGATION IS INVISIBLE TO THE TOKEN.** Any `andrew`-in-blocking
> sweep counts both; only reading the sentence separates them."*

**I reported the 6:1 ratio; this names WHY it must exist.** A field that records a state necessarily records
the decision NOT to enter that state, **in the same vocabulary**, because that decision is exactly what a
reader of the field needs to know. **So the over-report is structural, not sloppy record-keeping** -- and it
will recur on every such field: a `blockers` list that records "considered and rejected", a `risks` register
that records "assessed, not a risk", an `open_deploys` entry that records a deploy deliberately not opened.

> **RULE R-10 (standing).** **A census over a field that records both a state and its REFUSAL cannot be
> counted by the state's token.** The negation shares the vocabulary, so a token sweep returns state plus
> refusal and reports their sum as the state. **Read the sentence, or count something the refusal does not
> say.** Cost: reading N sentences where N is the token count. Non-application: a field whose values are a
> closed enum with an explicit refusal value -- there the enum does the separating, which is the fix.

**R-10 is also the general form of a trap I hit twice today from the other side**: `NOT REALIZED` contains
`REALIZED`, and `served_as_empty_shell` held the count while the fence-named `resolved_no_prose` read zero.
**All three are one shape -- the vocabulary of a state and the vocabulary of its absence overlap -- and R-8
already covers the grading half of it.**

## A1.3 -- the other two, confirmed as ruled

**CALL 2 is a BLOCKED ACT** -- *"a 403 is world-state, not a decision, and no ruling moves it"*. **CALL 3 is
genuinely RESERVED**, and the interim rule is *"fail-SAFE rather than merely neutral: ABSENT-with-reason
forbids invention, and the Base case serving -18.03 for Boeing is why that matters."* **Nothing in the
substance of sections 2-4 changes.**
