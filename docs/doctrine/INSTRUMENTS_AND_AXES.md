# INSTRUMENTS AND AXES

**Earned:** 2026-07-22, the MDPF_REVAMP count-axis incident.
**Sibling to:** `docs/doctrine/CONTROLS_OVER_CARE.md`. That file says *care is not a control*.
**This file says something narrower and nastier: a control can be real, careful, and correctly run —
and still be pointed at the wrong axis, the wrong population, or the wrong basis. It then returns a
PASS that is byte-identical to a true one.**

Incident record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/MDPF_ITEM1_INFLECTION_SPIKE_FINDINGS_20260722.md`
(@accb96eb9) and `org/critical_paths/MDPF_REVAMP_streak_tracker.json` (@bfe00e58f).

---

## 0. The one-line version

> **Before you trust a result, ask what it is OF: which axis, which population, which basis.**
> A rigorous instrument on the wrong axis survives review — that is precisely what makes it dangerous.

---

## 1. IS THE AXIS EVEN THE RIGHT KIND OF AXIS?

CLAUDE.md NEVER#1 says: resolve the trading calendar before calling data stale. The 07-22 incident
found the question **one level up, which nobody had asked in ~429 days of the artifact's life**:

> **Not "is the data stale on this axis" — "IS THIS A TRADING-DAY AXIS AT ALL?"**

The legacy MDPF series carried **21 of 429 datapoints on days the market was closed** (16 holidays, 5
weekend days — including a Saturday as its *most recent* point) and **omitted 20 real trading days**.
Every "spike" users complained about was that one defect: a real move posted onto a wrong day, or
several days' movement collapsed into one print where days were missing.

**Generalize:** every rule of the form *"check X against the axis"* has a silent precondition —
*the axis is well-formed*. Check the precondition once, explicitly, and record that you did.

## 2. IDENTITY-HOLDS IS NOT DAY-CORRECT

The composition identity `global == 49F + inflection` held **EXACTLY, 7 of 7 dates** — while the
entire sum sat on the wrong day.

> **A coherence check passed and still shipped a foreign-day roster.**

Coherence relates quantities **to each other**. It is structurally blind to a transformation applied
**uniformly to all of them** — a shift, a rebasing, a wrong vintage. **Coherence is not correctness**,
and internal consistency is the specific kind of evidence a whole-set error cannot disturb.

## 3. A THRESHOLD THAT HIDES A DEFECT RETURNS AN INDISTINGUISHABLE PASS

Two independent sweeps for the same defect returned CLEAN on `global`. Both were artifacts of the
sweep's own parameters:
- the excursion was **+66 on 7544 = 0.87%**, under a 5% floor;
- the series ran `7544 -> 7620 -> 7555` and never returned to base (a second leg was drifting
  underneath), so an **exact-revert tolerance** rejected it.

Neither negative was evidence about the data. **Both were evidence about the instrument.** It was
caught only by checking composition **directly**, i.e. by not using the sweep.

> **Corollaries.** A detector's floor is part of its output — quote it or the verdict is unreadable.
> Where a threshold hid a real defect once, the repaired clause should be **threshold-free by design**,
> not merely re-tuned. And **name the residual limit of the repaired clause** — the 07-22 fix was
> honestly reported as still blind to a *composed series with a drifting leg*.

## 4. AN INSTRUMENT CAN DEGENERATE — REPORT THE DEGENERACY, NOT ITS OUTPUT

Asked to bound a contamination, a verifier's instrument printed **"407 of 407 contaminated."**
It did not report that number. It reported *why the number was meaningless*: the two series compared
did not share a basis (median disagreement **7.25%**, max 41.5%, only **6 of 407** agreeing within
0.01%, disagreement spanning the entire history). **Value-equality only discriminates a date-stamp
error when the two series share a basis.** On that firm it carried **zero information**.

> **"407" was the instrument failing, not a measurement.**

A less careful pass reports 407 and triggers a false P0. A lazier one reports 0 and ships an exposure.
**The correct output was neither number.** Verdict recorded: **UNBOUNDED-BY-CONSTRUCTION** — worse
than "unmeasured", because no amount of re-running that *class* of test will ever close it.

> **Then make the gap actionable, not merely declared:** the same verifier named the test that WOULD
> reach it (ground the counts against their own source, not a differently-based series) and correctly
> scoped it to another lane. **A declared gap with no route is a complaint; with a route it is work.**

## 5. CORRECTING A WRONG-AXIS ERROR DOES NOT IMMUNIZE THE NEXT CLAIM

The same error recurred **three times in one session, one layer further out each time, and each
recurrence was caught by a different agent**:

| # | The claim | The axis it was blind to | Caught by |
|---|---|---|---|
| 1 | "the revamp fixes every spike" | ran on `model` only; `non_model` is a visible stacked band | COO |
| 2 | the corrected claim, re-generalized | ran on the VALUE axis; the COUNT axis was defective | DS |
| 3 | "06-03 is real, evidenced by +44 accounts" | that count is **imported from the very axis under suspicion** | CVO |

Case 3 is the sharpest: the **conclusion was right** and the **evidence was contaminated**. It was
corrected by *striking the evidence, not the ruling* — the conclusion was re-grounded on an
independent source axis. **Report a right answer reached by a bad route as an error anyway.**

> **Having just fixed a class of error is not protection against committing it again immediately.**

## 6. MANUAL EXECUTION CONCEALS A MISSING AUTOMATION

A feed's silver layer "worked" — because a human had been running the converter by hand. There was no
bronze→silver automation at all.

> **A feed that stops converting is byte-indistinguishable from a feed with no new data.**

Sibling of *a frozen count is indistinguishable from a stable roster*, which appeared the same day, in
a different subsystem, for a different reason. **Both are the general hazard: an absent process and a
quiet process produce the same observation.** Acceptance therefore requires **exercising the path
unattended**, never observing that the artifact exists.

**Consequence for gates:** a hand-staged artifact proves the CODE works; it does not prove **the
production path emits it**. Where the thing being served must come from a scheduled producer,
validating on a hand-staged set is that error committed deliberately, at the gate.

## 7. WHERE A RECORD LIVES IS PART OF WHETHER IT IS TRUE

A hazard was correctly identified, correctly written, and filed in a **superseded co-sign
deliverable** — a document nobody opens at the moment the hazard fires (a routine decommission).

> **"Knowingly chosen" is a property of the RECORD'S REACHABILITY, not of intent at signing time.**

The author described a reachability failure *and committed it in the same sentence*. Ranked carriers:
1. **A gate that denies the act** (e.g. a bucket-policy deny) — fires against any actor, reads nothing.
2. **A commit-time gate** — catches the repo path, misses the console.
3. **A registry row keyed on the artifact path** — necessary, not sufficient; *only fires for someone
   already suspicious*.

**Prose that must be read is the weakest carrier, and the default path is the one where nobody reads it.**

## 7a. A WRONG READING THAT LANDS ON A REAL MECHANISM IS MORE PERSUASIVE THAN ONE THAT DOES NOT

Same day, a second alarm: every object in a feed appeared to carry an `02:00:4xZ` mtime, against a
producer scheduled `cron(0 6)`. It read as a second, unexpected writer.

**It was `aws s3 ls` printing LOCAL time (Eastern/DST, UTC-4) with no timezone marker.** Resolved on
two independent instruments — `ListObjectsV2` returning ISO8601 `2026-07-22T06:00:45.000Z`, and
CloudWatch showing a single stream with last event `06:00:49Z`.

> **What made it dangerous was the coincidence: a real scheduler, `cron(0 2)`, genuinely exists on
> that estate.** So a rendering artifact arrived **pre-corroborated by a real mechanism.**

**Nonsense gets checked. Coincidence gets believed.** A wrong reading that lands on something real
recruits the estate's own truths as supporting evidence — it is the *plausible* misreading, not the
absurd one, that survives review.

**Operationally:** `aws s3 ls` is used fabric-wide for exactly this kind of freshness check and
**prints no timezone**. Prefer `list-objects-v2` (ISO8601 UTC) for any claim about *when*. Neither
agent erred here — one refused to infer from mtimes alone, the other resolved it on two instruments.
**Gate candidate:** lint a timestamp claim sourced from bare `aws s3 ls`.

## 7b. A PROOF THAT MEASURES THE ALREADY-GREEN LEG PASSES FOR THE WRONG REASON

A scheduled overnight run was priced as a "free unattended end-to-end proof" of a pipeline. The leg it
actually exercises — bronze ingest — **had already been proven unattended earlier that day**. Nothing
downstream self-fires. So the run would have re-proven the only green leg and stayed **silent on the
two that were not**, while being reported as end-to-end.

> **It passes for the wrong reason — and a green obtained for the wrong reason is the expensive kind.**

Before banking a scheduled or incidental event as evidence, state **which legs it exercises and which
it cannot**. "End-to-end" is a claim about a path, and a path is only as proven as its least-exercised
segment. *(This ruling was wrong twice in one session before it was corrected — the second time by the
agent who owned the leg in question.)*

## 7c. A SHARED VENDORED MODULE'S BLAST RADIUS IS INVISIBLE FROM ITS OWN SOURCE

A one-line top-level `import` was added to a converter module. That module is vendored **flat into four
Lambda packages**. The import would have raised `Runtime.ImportModuleError` in **all four** — for a feed
only one of them converts — forcing a re-vendor and redeploy of three unrelated pipelines to ship a
single-feed feature. (The identical vendor-closure failure is already in the estate's CHANGELOG.)

> **Nothing in the source file says "four Lambdas embed me." Only the BUILD_MANIFESTs do. An import
> added there is a MULTI-PACKAGE DEPLOY DECISION WEARING THE COSTUME OF A ONE-LINE CHANGE.**

Fixed by making the import **lazy inside the one function that needs it** — blast radius 4 → 1, and the
other three packages become *structurally* unable to break because they never call it. **Prefer a
structural bound over a careful one.**

**Gate candidate:** lint any new top-level import in a module listed in 2+ BUILD_MANIFEST
`vendored_modules[]`.

**Generalize:** before editing any shared/vendored file, ask **who embeds this**, and answer it from the
manifests — not from the file, which cannot tell you.

## 7d. THE ANATOMY OF A LAYERED FALSE VERIFY — four true instruments, one layer too low

A deploy took an entire production converter down (~9 min): `Runtime.ImportModuleError`. **Four
verification signals had reported success. Not one was wrong. Every one answered a question one
layer below the claim being made.**

| The signal | What it actually establishes | What it says nothing about |
|---|---|---|
| `write VERIFIED (size + sha256 match)` | the upload matches the local zip | the zip's **contents** |
| `CodeSha256` changed, `LastUpdateStatus: Successful`, `State: Active` | a file **swapped** | whether it **imports** |
| `vendor-manifest --check parity 8/8` | the copies match their **sources** | **closure over imports** |

This is verification-law #1 — **deployed = downloaded AND imported** — with an anatomy attached.
What caught it was an unrelated probe: it answered a question nobody had thought to ask.

**A LATENT VENDOR GAP IS INVISIBLE UNTIL SOMEBODY REBUILDS.** The offending top-level import landed
in a shared module *hours after* that package's previous deploy, and sat inert for 8 days. **The
agent who rebuilds inherits a break they did not write, as a live outage — and will spend the debug
on their own change.** Latent-vs-introduced is the load-bearing attribution: fix the class, don't
blame the rebuilder.

**THE TELL WAS A NON-EVENT.** The first attempted fix left the zip **byte-identical in size**.
Registering a vendored module requires **three** things — the BUILD_MANIFEST (declaration), the
vendoring script (materialization), and the source-map `files[]` (what the parity gate reads). **A
module in none of them is invisible to a gate that only checks parity between the two it knows
about.** The fix was confirmed by opening the uploaded archive and enumerating it, not by re-reading
the VERIFIED line.

**Gate (approved, build-time):** refuse a build when a vendored module's top-level imports are not
closed over the package (AST import scan vs `files[]`). **It converts the class from a
rebuild-time surprise into a build-time refusal** — and finds already-armed packages *without
anyone rebuilding them*. One such package was confirmed armed by this sweep: its manifest lacked the
module, the file was absent, **and its vendored copy of the shared source was stale — which is the
only reason it had not already broken.**

## 7e. A TEST ASSERTING A PROHIBITION IS A RATCHET AGAINST ITS OWN RETRACTION

A sovereign prohibition was lifted. The lift emptied the enforcing tuple in the code — correctly.
**Four tests then went red, every one of them asserting the hold was still armed:**
`assert "data/black_diamond/" in _comprail.HELD_PREFIXES` → `assert '...' in ()`.

> **A test is an ENFORCING COPY WITH TEETH. It does not enforce the prohibition on the estate — it
> enforces the prohibition on anyone trying to REMOVE it.**

The shape is self-perpetuating: the lift makes the suite red → **the red reads as "the lift broke
something"** → and the cheapest repair is to **put the prohibition back**. The next agent re-arms a
retracted rule believing they are fixing a regression. *(The hold in question had been
half-retracted twice, and both halves left a red test behind.)*

**Compounding failure:** the reds were **invisible for 8 days** because test collection was broken
over the same window. **A retraction whose own regression signal is unreadable cannot be verified by
the person doing it.**

**Therefore:**
1. **A retraction sweep must include TESTS in its denominator.** A sweep scoped to "enforcing copies
   in source" counts a real number of the wrong population.
2. **Retire the armed assertions; preserve the mechanism by declaring the state in a FIXTURE** —
   so the suite still exercises the machinery without asserting the prohibition is on.
3. **Add the negative control the suite never had.** A suite that can only assert *"the hold is on"*
   has **no expressible success state for the hold being OFF** — which is why the retraction had
   nothing to turn green.
4. **Fix the oracle first.** Sequencing the collection repair ahead of the wave is what made every
   later step checkable; before it, the conditions gating the wave were unenforceable.

**Generalize past holds:** any test that asserts a *policy* rather than a *behaviour* becomes a vote
against changing that policy, cast by someone who is no longer in the room.

## 7f. A COMPLETENESS SIGNAL WHOSE DENOMINATOR IS ITS OWN CONFIGURATION

Three independent "everything is present" signals were examined on the eve of adding a third tenant to
a two-tenant system. **All three report GREEN on a three-tenant cycle in which the third tenant is
entirely missing:**

| signal | its denominator | result on a 3-subject cycle |
|---|---|---|
| a source-coverage audit | **hardcoded subject keys** | third subject **absent** — not even *"did not run"* |
| a `keys_staged: 7` marker | **a literal** | `7` |
| a publisher's `all_present` | **`len(PUBLISH_MAP)`** | `9/9 = True` |

> **A GREEN SIGNAL DERIVED FROM A HARDCODED LIST IS NOT EVIDENCE OF COVERAGE. IT IS EVIDENCE THAT THE
> LIST WAS ITERATED.**
> **The guard's subject list and the world's subject list are different objects, and nothing compares
> them. A guard cannot report missing a subject it was never told to look for.**

**Each of the three was written CAREFULLY** — one of them exists *specifically* to prevent silent
omission, and the publisher has a considered soft-fail for a *mapped* key whose source is absent.
**That care does not reach an UNMAPPED subject, which never enters the loop.** Care operates inside the
denominator; the defect is the denominator.

### 7f.1 — THE COUNTERINTUITIVE PART: THE BETTER-WRITTEN PERMISSION REMOVED THE SAFETY NET

| | narrowly-scoped role | wildcard-scoped role |
|---|---|---|
| permission style | **enumerated prefixes** (least-privilege, per-resource) | **wildcard prefix** (still least-privilege by intent) |
| behaviour on a new subject | **BLOCKS** | **PERMITS** |
| failure mode | **LOUD** — access denied on first run | **SILENT + GREEN** — possibly never found |

**The wildcard grant is the better-written policy on the firm axis — a new subject needs no permission
change at all. That is precisely what removes the loud failure.** The narrower grant *accidentally*
functioned as a completeness check the correct one cannot.
> **TIGHTENING PERMISSIONS DOES NOT CATCH A FORGOTTEN SUBJECT — and an enumerated grant that blocks is
> a completeness signal you did not design and must not rely on.**

### 7f.2 — THIS DEFEATS THE COVERAGE-FRACTION RULE UNLESS THE DENOMINATOR IS EXTERNAL

The standing control — *state your coverage fraction against the defect-capable population* (§9 Q4) —
**is satisfied by all three of these signals while they lie**, because each reports its fraction
**against its own denominator**. `9/9` is a true statement about `PUBLISH_MAP`.

> **STRENGTHENED RULE: a coverage fraction is only evidence if its DENOMINATOR IS DERIVED FROM OUTSIDE
> THE INSTRUMENT'S OWN CONFIGURATION.** A denominator the instrument defines cannot measure the
> instrument's blind spot. **Where the subjects are enumerable (tenants, firms, feeds, packages), the
> denominator is the SUBJECT REGISTRY — and the check is a SET-DIFFERENCE against it, not an iteration
> of the local list.**

### 7f.3 — THE CLASS ESCALATES FROM REPORTING TO SAFETY, AND SEVERITY MUST BE ORDERED BY WHICH

A fourth instance turned up in the same sweep, and it is **not** a reporting defect:

| # | signal | denominator | on a 3-subject cycle |
|---|---|---|---|
| 1 | source-coverage audit | hardcoded subject keys | third subject absent |
| 2 | `keys_staged: 7` | a literal | `7` |
| 3 | publisher `all_present` | `len(PUBLISH_MAP)` | `9/9 = True` |
| **4** | **`stale_partners` / `all_fresh`** | **`{"subject_a": …}` — a ONE-ELEMENT dict** | `[]` / `True`, **AND THE PROTECTIVE SKIP NEVER FIRES** |

> **1–3 MIS-STATE WHAT HAPPENED. 4 CHANGES WHAT HAPPENS.**
> A subject outside the protected set does not merely go **unreported** — it goes **UNPROTECTED.**

In the live case the skip exists to stop a downstream job **fabricating a residual off a stale
minuend** — the code says so itself. **That guard simply does not reach a subject the protected set
never contained.** So the same self-referential-denominator defect appears **on a GATE rather than on a
REPORT**, and its consequence is a fabricated value on a served surface rather than an inaccurate
green.

**ORDERING RULE:** when this class is found, **triage by whether the defect mis-states an outcome or
changes one.** A green report on a wrong number is expensive; **a guard that silently excludes a
subject is a different category** and outranks every reporting instance in the same sweep.

**AND A PROCESS FAILURE WORTH THE SAME BILLING:** the reporting defect and the safety defect arrived in
**one commit**. The reviewer banked the reporting one, wrote doctrine from it, and **the safety one did
not surface in the ruling derived from that commit** — caught only because a second reader compared the
ruling against the commit's full contents. **The summary was TRUE ABOUT WHAT IT COVERED, and the thing
it omitted was the thing that mattered.** *Read the commit, not the headline — especially your own
source's headline.*

*(Sibling of §7c — a vendored module's blast radius is invisible from its own source — and of the
absence-has-no-token class: all four are instruments that cannot see past their own declaration.)*

## 8. PROCESS PRINCIPLES THAT PAID OUT THE SAME DAY

- **A FAILURE SIGNAL IS NOT A REASON.** Two instances, same day, two levels:
  - **An exit code is not a reason.** A mutant test "failed" with exit 1 and was nearly banked as proof
    the gate worked. It had failed on a `ModuleNotFoundError`.
  - **`assertRaises` cannot tell you WHICH gate raised.** An author wrote 11 gate tests, all green, then
    neutralised each gate **in the source** and re-ran. One gate was disabled **entirely** — and both of
    its tests **stayed green**. They had always passed for the wrong reason: the mutations happened to
    trip *other* gates. **Two tests naming that gate in their titles were testing something else, and a
    green suite said so confidently.**
  **Check WHICH failure — especially when the failure is the one you wanted.** A test asserting only
  *"something refused"* is satisfied by any refusal, so it measures the SUITE, not the gate it names.
  Assert the discriminating outcome; then mutate each gate individually and confirm **only** its own
  tests go red.
- **AND A PASS SIGNAL IS NOT A REASON EITHER — STATE THE SCOPE A GREEN COVERS, BECAUSE AN UNSTATED
  SCOPE READS AS "EVERYTHING".** Same day, the sign flipped: an author landed 30 mutation-verified
  green tests on a converter. **Every test called the converter DIRECTLY.** Production reaches it
  through `on_success -> lambda_entry -> run_event -> adapter -> manifest_body`. **Nothing crossed
  that seam** — and the defect was not in any gate, it was in the JOIN: the adapter emitted a result
  whose column census was left at its defaults, tripping a parity assertion **on the first real
  conversion, after the data had already landed.**
  > **They tested both ends of a seam and not the seam, then reported a green that was TRUE AND
  > INSUFFICIENT.**
  A mutation-verified suite proves each gate *has teeth*. It says nothing about whether the gates are
  **reachable in the shape production calls them.** *Unit-green plus unit-green does not equal
  seam-green.* Exercise the wired path, and when reporting a pass, **name what it covered.**
- **A CONDITION STATED BEFORE THE WORK IS A SPEC; SPRUNG AT THE GATE IT IS A HOLD.** Sign-off terms
  get published in advance.
- **A RETRACTION THAT SHRINKS A SCARE IS WORTH AS MUCH AS ONE THAT GROWS IT — AND IS MUCH RARER.**
  A "PATTERN — three independent paths" finding was retracted by its own author to **two sites and a
  downstream derivative**, proven by rebuilding the suspect artifact with **no code change** and
  watching it self-heal. Two Tier-1 agents were one message from banking the overstatement as doctrine.
- **A SWEEP THAT PROVES A POPULATION SMALL IS AS VALUABLE AS ONE THAT PROVES IT LARGE.** The value is
  in the **denominator**, not the direction: *56 matches / 14 files / 43 scanned → exactly 2 real sites.*
- **THE PRODUCER'S SELF-REPORT ON THE PRODUCER'S OWN ARTIFACT IS NOT EVIDENCE — INCLUDING A GOOD ONE.**
  Every finding above was independently reproduced before being ruled on. **Bringing a defect in your
  own work instead of quietly fixing it is the behaviour that made the whole chain work.**

---

## 9. THE CHECK

Before recording a PASS, or citing one:

1. **What is this OF?** Which axis, which population, which basis. Name it.
2. **Is the axis well-formed** — not just the values on it?
3. **Could this instrument have returned this answer if the defect were present?** If not, it is
   decorative. **Mutant-prove it against the live defective artifact; RED, or it does not ship.**
4. **What is the denominator, and what is the detector's floor?** Quote both.
5. **Does my evidence come from the thing under suspicion?**
6. **If this is a "works" claim — did I exercise the path, or observe that an artifact exists?**
7. **If this is a debt — is the record where the actor will be standing when it fires?**
