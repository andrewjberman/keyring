# GENCHI GENBUTSU — go and see for yourself

> **FILENAME IS LEGACY, DELIBERATELY.** This file is `CONTROLS_OVER_CARE.md` because **156 files
> point at that path**. Renaming would manufacture ~100 dangling citations — the exact defect class
> this doctrine exists to prevent. The *title* is the doctrine; the *path* is an address.

*Genchi genbutsu* (現地現物) — "the actual place, the actual thing." Go and look at the real thing
rather than reasoning about it from where you are standing.

**Andrew-direct 2026-08-05:** *"The biggest idea here seems to be aligned with a japanese proverb …
which translates to 'go and see for yourself'. The purpose of the comp-tools was this idea."*

**Scope of this file: PRINCIPLE AND MECHANISM ONLY.** Incidents live in incident records and are
referenced, never retold here (Andrew-direct 2026-08-05 — see "Incidents belong elsewhere" at the
end). Predecessor: 1,289 lines @`913e3365d6`, superseded 2026-08-05 on Andrew-direct instruction.

---

## Why the previous form could not work

Its own body contradicted its own title. The capstone said *every one was caught by a control
failing, none by being careful.* Sixty-five lines later, unpromoted: *"the thing that actually
worked has no gate behind it — somebody read the thing and checked. Not one was caught by a gate."*
Both true; opposite generalisations; **only one reached the title** — against the file's own warning
that *"the estate will fund the mechanism the story names."*

**And the deeper reason prose alone cannot fix this: the failure has no phenomenology.** It never
feels like skipping a check. It feels like knowing. Inference is generative — it arrives first,
cheaply, with confidence attached. Retrieval means stopping to go fetch. By the time *"should I
check?"* surfaces, an answer is already in hand and the check reads as redundant.

**Care operates on the answer you already generated. It does not send you to get a different one.**
Scrutiny and retrieval are different actions, and only one of them was ever going to help. This is
why agents who can name a rule violate it while naming it.

---

## THE BOUNDARY — this file is one of three families, and it is not a superset

> **THIS FILE** holds **HOW YOU FAIL TO SEE THE THING** — the root plus the six ways looking does not
> produce seeing, including how an instrument lies.
> **[`MECHANISM_LAWS.md`](MECHANISM_LAWS.md)** holds **WHERE AN ASSERTION SITS** — fourteen shapes a
> claim comes to be wrong about its own subject, each with an EXPOSING QUESTION and a GATE-OR-TEST.
> **It does not type instrument fallibility, by construction**, so neither file contains the other.
> **Read both.**
> **A THIRD FAMILY HAS NO HOME: HOW A RULE OR ROLE FAILS TO BE ONE** — a rule naming the EVENT instead
> of the PROPERTY, a procedure step naming no actor, a role first exercised by a non-owner. Covered by
> neither file, measured-absent with positive controls, and named here rather than quietly omitted.
>
> *This reciprocal half is written 2026-08-05. `MECHANISM_LAWS.md` had stated the boundary from its
> side and pointed here; this file pointed back **zero** times, so a reader arriving here could not
> learn the other existed. **A one-directional pointer is a reconciliation point** — and my own
> rewrite then deleted the section its side cited, dangling it. Cite the CLAIM, never the section
> number.*

---

## THE ROOT — go and see the thing itself

The recurring failure is almost never *"did not verify."* Everyone verified something. It is:

> **Cheap, direct, decisive evidence was available, and an inference was substituted for it.**

Ask of any load-bearing claim: **what is the thing, and have I looked at it?**

---

## The ten ways you fail to see it *even though you looked*

*(Heading corrected 2026-08-12: it read "six" and enumerated seven. A count in a heading that
disagrees with the list beneath it is this file's own §6 — the label supplying a claim the content
never made — and it survived a 1,289→239-line cut plus every read since.)*

### 1. You looked at a PROXY, not the thing
A digest, a count, a config, an `rc=0`, a symbol's presence. A proxy answers a neighbouring question
at full confidence.
- `rc=0` is a **launch receipt**, not an outcome.
- A hash is a proxy; the columns are the thing. **When you hash to prove sameness, first remove the
  fields whose sameness is the question.**
- Applied-config is not behaviour. A guard nothing calls is a comment with parentheses.
- **A PRODUCER-SIDE TIMER MEASURES THE ARTIFACT; ONLY A CONSUMER-GENERATED STATUS MEASURES THE
  AGENT.** Time-since-last-output tells you about the output. To know whether a worker is alive,
  prefer the signal **only a live worker can produce** — a current, *specific* statement of its next
  concrete step — over any elapsed-time threshold. **A threshold derived from COMPLETED work cannot
  classify work IN PROGRESS: any deep in-flight unit exceeds a percentile drawn from finished ones,
  by construction.** The timer opens the look; freshness-and-specificity closes it. *(Same property as
  §22b's ACK rule one domain over: a producer-side signal is blind to consumer death, and only a
  round trip crosses both.)*
- **Discharge:** exercise the path that fails if the claim is false. Read the served value.

### 2. You looked at the DESCRIPTION, not the STATE
**The describing layer drifts from the enforcing layer, and only the enforcing layer is true.**
- A comment is a claim with no vintage and no test. The dangerous one is not false — it is one that
  was true and the ground moved under it, arguing authoritatively in the codebase's own voice for
  the harm it now causes.
- A marker FILE saying ARMED beats a hook COMMENT saying staged.
- A doc describing a tool's behaviour loses to that tool's own source.
- **A description does not have to be WRONG to displace a measurement — only RELEVANT.** Distinct from
  the drift case above: these are **current, correct, and about the question next to yours.** A wrong
  description eventually contradicts something and someone notices; **one that is correct about an
  adjacent fact is permanently self-consistent, so the search terminates and nothing ever corrects it.**
  The tell is that **the story FIT** — which is exactly why nobody looked further.
- **Discharge:** read the enforcing layer — live primitive, marker file, applied config, deployed
  bytes. **A description that fits is not evidence you may stop.**

**2b. The dominant case here: almost everything you read was written by another agent.** Ledgers,
dispositions, registries, logs, handoffs, PRDs, task orders, prior findings.

> **Andrew-direct 2026-08-05:** *"treat recent agentic artifacts as the last agent's understanding
> of state, not a settled baseline. It is not necessarily an error, but it is neither an absolute
> truth, it is a representation, a map, not the territory, and should be handled with a 'go and
> fetch for yourself'."*

**The non-guilt half is load-bearing.** A map is not wrong for being a map. It is a compression of
someone's understanding at a vintage, and the correct response is not doubt — it is **fetching the
territory when the claim carries weight.** Two symmetric errors are ruled out: inheriting an
artifact as truth, *and* discounting a peer's recent work as suspect.
**Discharge:** the question is never *"do I trust this agent"* — it is ***"is this claim carrying
weight, and have I seen the territory."***

> ### ⚠ APPLICABILITY — WHERE "GO AND FETCH FOR YOURSELF" BINDS
> **This rule carried no applicability condition, and that was a defect in the rule, not in the
> principle.** Found by `1.0.0_SA_CTO~B` against `3.0.0_SA_CVO`'s parallel contract (`@c7760548c`) —
> **the same gap existed here, unflagged, and is closed 2026-08-06.**
>
> # A CONTRACT THAT DOES NOT SAY WHERE IT APPLIES WILL BE APPLIED WHERE IT CANNOT HOLD, AND THEN ABANDONED WHOLESALE.
>
> **MEASURED, NOT ARGUED.** A per-row ground-truth fetch is affordable at a **batch/analytic** call
> site (a once-daily runner on a transient box: whole run 3m24s, a ~357-path vertical join ~36s
> serialised, seconds parallelised) — **but affordable because of a property of THAT CONTEXT** (daily
> batch, no latency SLA, nobody waiting), **not a property of the rule.** At a **request-serving**
> call site — a 256 MB Lambda behind API Gateway serving a live page — per-row fetch is a latency and
> cost failure, **and the holder will quietly ignore it.**
>
> **BINDING FORM:**
> - **BATCH / ANALYTIC consumers — FETCH DIRECTLY.** The obligation as written.
> - **SERVING / REQUEST-PATH consumers — FETCH AT PRODUCTION TIME AND CARRY THE VINTAGE FORWARD.**
>   The fetch still happens; it moves off the request path.
>
> **The general form, and it is why this is doctrine and not a footnote: an unscoped obligation is not
> a stricter obligation — it is a weaker one, because the first holder who cannot meet it discards the
> whole rule rather than the inapplicable part.** Pair with §4's executability test: *can the seat that
> needs this execute it alone?*

### 3. You compared the thing TO ITSELF
No outside information entered, so the check certifies any internally consistent lie.
- **Conservation is invariant under a swap, and under a simultaneous both-sides deletion.** A
  reconciliation that ties both sides of the same omission is not a reconciliation.
- An aggregate is never graded on its total, nor on the series you were asked about — two offsetting
  moves produce a clean headline.
- **A FAITHFUL PORT IS THE STRONGEST POSSIBLE PARITY EVIDENCE AND ZERO EVIDENCE OF CORRECTNESS.** A
  byte-identical port diffed against the source it was ported FROM is self-comparison wearing a
  migration's clothes: agreement is guaranteed by construction, so **every defect in the source arrives
  carrying a green light.** Fidelity (*did it reclassify?*) and correctness (*was the source right?*) are
  different questions, and a faithfully-ported bug answers the fidelity one correctly — an instrument
  honest about its own question, answering the wrong one. New and old agree BECAUSE they share the defect.
  **Discharge:** a port cert states WHICH question it answers, and correctness is grounded OUTSIDE the
  source lineage — read the rule on its own terms against real inputs, never only new-vs-old.
- **Discharge:** diff against a **prior vintage** or **a source the pipeline does not derive from**.
  Diff every constituent series, not the roll-up.

### 4. Your instrument COULD NOT HAVE SAID OTHERWISE
The measurement had no failure mode, so its PASS carried no information.
- A count cannot distinguish *"nothing is there"* from *"I looked in the wrong place."* Zero is
  byte-identical between empty and misaimed.
- **A retrieval failure returns a value.** `grep -c` counts zero matches in an error message;
  `git show HEAD:<untracked>` returns a `fatal:` string that a byte-comparator will happily diff.
  **Put the control on the RETRIEVAL, not the pattern. Print the denominator of every scan you
  reason from.**
- `--query 'length(...)'` on a paginated `list-*` returns the **page** count.
- A positive control **batched with its target** is corrupted by its own presence.
- **A check run on one member of a set does not cover the set.** An instrument can be correct and
  simply never aimed.
- **Discharge:** *could this have failed? did my input reach the governed branch? was this actually
  pointed at the thing I am concluding about?*

**4b. A NEGATIVE CONTROL IS NOT ENOUGH — a result that every hypothesis predicts is not a result.**
If every probe returns the same value *including* your control, the reading is equally consistent
with *"the change failed"* and *"the harness is broken."* Only a **positive** control — a probe that
**cannot** return that value — discriminates. **Ask: which worlds does this rule OUT? If none, you
have not measured.**
⛔ **4b.1 — AND THE POSITIVE CONTROL HAS ITS OWN BLIND SPOT, WHICH IS THE MOST DANGEROUS ONE IN THIS
FILE BECAUSE IT WEARS THIS FILE'S OWN REMEDY: A POSITIVE CONTROL PROVES THE PROBE CAN FIND SOMETHING.
IT DOES NOT PROVE THE PROBE IS ASKING ABOUT THE RIGHT THING.** *Measured: seven variable names probed
for a rendered vintage, all returning **0**, with a positive control returning **6** — clean AND
controlled, which is the most persuasive state a wrong answer can occupy. **The seven names were the
searcher's invention, not the code's.** The real variable was one the guesses could never have
produced.* **A ZERO ABOUT A NAME YOU MADE UP IS NOT A MEASUREMENT OF ANYTHING** — the control was
sound and the SUBJECT was fictional. **Discharge: before trusting an absence, establish that your
query terms came FROM THE CORPUS rather than from your expectation of it — ENUMERATE WHAT IS THERE,
then ask about it. Guessing the names and controlling the probe validates everything except the
question.**

⛔ **4b.2 — A UNIFORM ZERO ACROSS A SET CONTAINING ONE KNOWN-TRUE MEMBER IS A BROKEN INSTRUMENT, NOT A
FINDING.** The cheapest discriminator in this file, and stronger than a synthetic positive control
because the expected answer is already known: **hold out one member whose value you know, and run the
instrument at it.** A predicate too narrow to match anything returns a clean, confident, uniform zero —
**and uniformity across a heterogeneous set is itself the tell.** Real distributions are lumpy; an
instrument reporting the same value for every member is far more likely to be measuring nothing than to
have found a uniform world.
**Discharge:** *which member's answer do I already know, and does the instrument reproduce it?* If no
member's answer is known in advance, **the run is uncalibrated and its zeros carry no weight.**

>> **THIS IS THE DOMINANT DEFECT MODE, not one of seven equals — and the frequency is measured, not
impressionistic.** In a single session, a clean zero from an over-narrow predicate was produced by
**five different seats**: a semantic census returning 0 for every unit including one where the runner
had authored all 24 cells; a lint validating its own typing; a name-scoped enumeration short by 9; a
filter matching nothing; and two enumeration planes whose blind spots intersected. **One seat logged
four instances of it by itself.** In every case the ONLY thing that caught it was a member whose answer
was known in advance. **A known-true case is not a nicety at the end of a run — it is the calibration
without which the run has no verdict.** <<

**4c. THE ANTI-CORRELATED VERDICT — the cleanest pass is sometimes the most complete failure.**
The least intuitive member, so it needs its mechanism:
- **Orphan watcher.** It `mv`s the message to `read/` **before** echoing into a dead pipe. So a probe
  reads *process exists* **and** *inbox empty* — the strongest REACHABLE verdict — **and both limbs
  hold *because* the agent is deaf.** The verdict is *produced by* the failure, which is why it also
  survives a random-input control.
- **Name-resolution probe.** `command -v` reported 93 of 93 tools resolving; **zero ran.** All
  existed because the provisioner ran; all were dead because they shared one broken prefix. **The
  pass read 100% healthy precisely because the breakage was total and single-caused.**
- **Test:** when a result is unusually clean, ask whether a *total* failure would produce exactly
  this reading. **Exercise the tool; never resolve its name.**

### 5. Your WITNESS was your own OUTPUT
The check *had* an outside source — and it was not outside. An artifact a prior run of the thing under
test PRODUCED is not a second opinion: agreement is guaranteed by construction, and the more of it you
gather, the more convincing the nothing becomes. Distinct from #3 because this witness *looks*
independent — different file, format, prefix, vintage — and is not.
- **COVERAGE IS NOT INDEPENDENCE. N self-comparisons carry the information of ZERO.** A full-history
  green over thousands of dates whose witnesses are all the transform's own emissions is worth strictly
  less than ONE date whose witness was produced independently. **Ask what PRODUCED the thing you are
  checking against, never how many of them there are** — and note the exercise you were *asked* for can
  be the worthless one.
- **A candidate witness that matches your output PERFECTLY is evidence that it IS your output.** The
  populations most needing a check are exactly those with no independent witness left.
- ⚡ **THE INVERSION — a difference can be the CREDENTIAL: *the thing that made it fail byte-equality is
  what qualifies it as a witness.*** An artifact byte-identical to what the transform emits is
  (probably) that emission; one differing only INCIDENTALLY (record order, formatting, timestamp) while
  agreeing on every VALUE was produced independently and can adjudicate. **So do not discard a
  near-match as noise — interrogate the difference. Incidental difference + total value agreement is
  the signature of a genuine second source.**
- **Discharge:** before comparing, establish the PROVENANCE of the comparison side — what wrote it,
  when, from which input. Where no independent witness exists and none can be manufactured, the claim
  is **DECLARED-UNVERIFIABLE: it may be USED, never CITED as grounded.**

### 6. The LABEL supplied a claim the CONTENT never made
The other five are ways the INSTRUMENT fails. This one is a CORRECT measurement wearing a name that
misdescribes it — you looked, you measured right, and you still concluded wrong, **and the number's
correctness is exactly what made it persuasive.** **A name, title or label describes ONE axis and is
SILENT on the others; the reader supplies the missing axis from the words without noticing. THE
SILENCE IS NOT READ AS SILENCE — IT IS READ AS AGREEMENT.**
- A served field whose NAME asserts a property its COMPUTATION does not carry hands every consumer a
  right number and a wrong conclusion. No downstream check can catch it: the value is not wrong.
- A chart title accurate on the VALUE axis and silent on the POPULATION axis reads as authoritative
  about both, and a build derived from it inherits the presumption instead of the filter.
- **Discharge, by whether the name can move.** Where it CAN: rename. Where it CANNOT (a served key —
  NEVER#3): **register the divergence at the canonical term registry, so the truth is reachable where
  the reader actually asks.** *A characterisation that lives only in a cert protects the certifier and
  nobody downstream.* And when a BUILD is derived FROM a name, **the axis the name is silent on is
  measured AT SOURCE, never inferred from the words** — one look settles what a presumption was holding.
- **The family, and it reaches past labels:** *an instrument or a label answers a NARROWER question
  than the one the reader asked, and nothing in the output says so.* Same shape as an oracle whose
  silence means nothing until its own firing rate is known, and a value pin that cannot see a
  population change.

### 7. Nobody sent it back — an unexercised claim survives on its DIRECTION, not its truth

The four modes above explain why you failed to see. This explains why **the resulting claim was
never challenged**, which is what lets an unlooked-at claim reach a law file, a register, or Andrew.

**Review is direction-sensitive, and only one of three directions reliably draws scrutiny:**

| direction of the claim | how it reads | challenged? |
|---|---|---|
| **unflattering to someone else** | an accusation | **YES** — the subject pushes back |
| **generous to someone else** | fairness | no — nobody argues they deserve less credit |
| **critical of yourself or your own tools** | rigour, humility | no — challenging it looks like defensiveness |

**So an unexercised claim lives longest in exactly the two directions that feel most virtuous.** The
same asymmetry runs one layer up: **a SELF-CORRECTION arrives pre-credentialed** — costliness-to-self
is read as evidence of correctness, so its *direction* goes unexamined by author and reader alike.
**Correcting your own number against your apparent interest can still push toward the outcome you
were arguing against.**

- **A claim that an instrument is WEAK reads as rigour; that it is SOUND reads as complacency** — so
  fabricated defects in your own tooling are the least-audited claims you can make.
- **A broken retrieval does not merely mislead you — it MANUFACTURES A FINDING ABOUT THE INSTRUMENT
  whose signal it deleted**, and that finding then travels in the least-audited direction above. (The
  retrieval mechanism itself is §4; only this consequence is new.) **So before reporting that a tool
  failed to signal something, re-run it with nothing between you and its output.**
- **Discharge:** *which direction does this point, and would anyone here be motivated to check it?*
  If the answer is no, **you are the only control**, so exercise it before it is repeated.

**Escalation ordering — a wrong reading dies with the turn; a BANKED finding propagates.** The cost
of an unexercised claim is set by how far it travels, so the exercise bar rises with the audience:
highest for anything entering a register, a doctrine file, or a message to Andrew. **Conferring
standing on someone else's unexercised claim is itself an act requiring exercise.**

### 8. Your QUESTION framed the population, and the answer was precisely correct about the wrong one

**An investigation framed as "what went wrong" enumerates DEVIATIONS and ANOMALIES — and omits the
actor ENTITLED to have done exactly this.** The routine authorised explanation is the one a
fault-shaped question cannot see, and it is usually the correct one.

**This is not §4 (an instrument that could not have said otherwise) and not a wrong denominator you
chose.** The candidate set here is *competent, MECE inside its own frame, and complete* — the frame
is what excluded the answer, and the frame came from the question. Care cannot catch it, because
care is spent enumerating the population the question named.

- **THE TEST, before the candidate list is written: WHO IS AUTHORISED TO DO THIS? ASK THEM FIRST.**
  *Then* enumerate the unauthorised. One question, asked in the other order.
- **Recognising this class in someone else's output does not immunise you against it in your own** —
  two of its instances were written hours apart by seats that had each read the other's.
- **Discharge:** *is my candidate set a list of who could have DEVIATED, or of who could have ACTED?*
  If the second list is missing, the enumeration has not started.

Record (four measured instances, one night): `org/tier1_exec/2.0.0_SA_COO/deliverables/FAULT_FRAMED_ENUMERATION_OMITS_THE_ENTITLED_20260825.md`.

### 9. The ABSENCE was the encoded ruling, and you read it as a gap

**A missing entry in a registry is not evidence of a gap. THE ABSENCE MAY BE THE DECISION.** A
raise-rather-than-default, an unlisted key, an acceptance with no exercise oracle — each can be the
mechanism *carrying* a ruling rather than the place one has not been made yet.

**The dangerous half is the REMEDY, not the misread.** Filling the gap does not merely waste effort;
**it manufactures a false fact** — a business term minted into an infrastructure vocabulary, a
fee-taking fact about a client base that does not exist, un-doable remediation raised in the
sovereign's name on a critical path.

**Why it recurs: a PRESENT-BUT-WRONG entry announces itself** — someone reads it and disagrees. **AN
ABSENCE ANNOUNCES NOTHING**, so the reader supplies the explanation, and *"nobody got to it yet"* is
always available and always plausible. **The gap reading wins because it is the only reading that
suggests an action.**

- **THE TEST, one question before filing any absence as a finding: WOULD THE ENTRY, IF PRESENT,
  ASSERT SOMETHING TRUE?** If it would state a fact nobody can source, **the absence IS the
  assertion**, and the guard that refuses to default is the mechanism carrying it.
- **This is the constructive twin of *"a 404 in the wrong bucket is the wrong question asked
  cleanly"*** (CLAUDE.md Rule 21): that rule says a MEASURED absence may be an instrument artifact;
  **this says a REAL absence may be a DECISION.** Neither is a gap, and they fail toward different
  wrong acts.
- **Discharge:** name what the entry would say, then find its source. No source, no gap.

Record (three measured instances in ~90 minutes, found by three different seats each owning the
surface — none looking for a pattern; surfaced by `3.0.0_SA_CVO` 69356, who authored one of them):
`org/tier1_exec/1.0.0_SA_CTO/deliverables/` this session.

### 10. The SET YOU MEASURED was not the SET YOU WERE CLAIMING ABOUT

**Four shapes, one mechanism, one remedy.** In each the tool ran correctly and returned a well-formed,
fast, plausible answer **about a different population than the claim.**

| shape | the divergence |
|---|---|
| **numerator / denominator** | the two halves of a fraction count DIFFERENT populations (*"30 of 64"* -- 30 detail files against a 64-model roster; true coverage 22) |
| **sample as population** | a handful measured, the whole asserted (*"EVERY lane returns zero"* -- three sampled, others returned 10, 9 and 1) |
| **location from memory** | measured inside a path/file/ref supplied by recall rather than resolved (a grep of the wrong bundle; an `ls-tree` under a guessed prefix) |
| **self-inclusion** | **the measurer's own output is in the measured set** -- a log naming four projects made all four read as active TODAY |

- ⛔ **A PRINTED DENOMINATOR DOES NOT DISCHARGE THIS.** *"30 of 64"* HAD a denominator; it was printed; it
  was still wrong. **The denominator rule ensures a denominator EXISTS, not that both halves describe the
  same population.**
- ⛔ **NOR DOES NAMING THE SUBJECT** (the discharge above). A claim can name its file perfectly and still be
  about the wrong SET -- that discharge reaches the location shape and none of the other three.
- **THE TEST, checkable in the moment: STATE THE SET YOU MEASURED AND THE SET YOU ARE CLAIMING ABOUT, AND SEE
  WHETHER THEY ARE THE SAME SENTENCE.** *What is this number OF, and is that what I ran against?*
- **Self-inclusion has no natural tell and needs its own question:** *am I in this population?* An agent that
  writes about a set and then measures that set is inside it, **and nothing in the output says otherwise.**

> **NOT IN THIS CLASS -- A CONFOUND IS A DIFFERENT AXIS AND TAKES THE OPPOSITE REMEDY.** *"Tilde lanes return
> zero, therefore the tilde is the cause"* had a **CORRECT** population; the error was CAUSAL ATTRIBUTION --
> two variables moved together and the visible one got the blame. **A wrong set is fixed by naming the
> population. A CONFOUND is fixed by finding a case where the two variables SEPARATE** -- and until someone
> does, the correlation stays perfect. *Named here so it is not filed as a fifth member; it belongs to the
> inference family and is not yet written up.*

*Class pitched by `1.0.0_SA_CTO` at five members titled on its most vivid instance; **corrected to four and
retitled on the mechanism by `3.0.0_SA_CVO`, who ran the four postulates on it** -- the five-member form
failed (i) MECE and (iii) intent coherence, and the original title named an EXEMPLAR SURFACE rather than a
TRIGGER CONDITION, which is the F-010 defect about to be installed into fresh doctrine. **A seat about to
include its own log in a population is not thinking "denominator."***

### THE ONE DISCHARGE THAT WORKS FOR ALL NINE — put the SUBJECT in the CLAIM, not in the description of the search

Every failure above is a claim about a *thing*, and in every one the searcher knew which thing they meant and
the reader could not. **The remedy is a sentence shape, not a habit:**

| form | property |
|---|---|
| *"I searched the override log"* | **UNCHECKABLE.** The subject lives in the searcher's head. |
| *"0 hits in `org/to-pos-override-audit.log`, field 2"* | **CHECKABLE — and its wrongness is VISIBLE to a second reader.** |

**IT REQUIRES NO CARE, NO NEW TOOL, AND NO GATE.** It moves the subject out of the author's head and into the
sentence, **where the one person who cannot catch the error stops being the only person who could.**

- **Name the PATH, the REF, the FIELD, the BUCKET, the PREFIX, the PLANE — inside the claim**, beside the
  number, not in a preamble about what you did.
- **This is the denominator rule's twin.** The denominator says *how many were in scope*; this says *what
  scope was*. **A denominator over an unnamed population is a frame around nothing.**
- **Corollary for a zero: never supply a location from memory and then measure inside it.** Search the whole
  tree and filter (`git ls-tree -r --name-only <ref> | grep -i <token>`), rather than passing a prefix you
  believe. **An assumed location converts a real question into a well-formed measurement of the wrong place,
  and the answer comes back clean, fast, and in the direction that ends the search.**

> ⛔ **WHY THIS IS ENVIRONMENTAL AND NOT A COMPETENCE PROBLEM: this estate holds many near-identically-named
> artifacts across several planes at once** — local / tracking / remote refs, repo / deployed / executing
> bytes, and whole FAMILIES of audit logs whose names differ by one word. **THE WRONG ONE IS ALWAYS RIGHT
> THERE, AND IT ALWAYS ANSWERS.** *When one seat does this it is carelessness. When five do it in one night
> it is a property of the environment* — and the environment is not going to stop having sibling names.

**Measured, one night, ten instances across five seats** — a wrong entry-chunk, a guessed path prefix twice,
three guessed FIELD names, a positive control that fired on a SIBLING log, a hand-authored artifact
classified from a summary, and a stale-ref read. **EVERY ONE WAS CAUGHT BY A SECOND READER. NONE BY THE
AUTHOR** — which is the whole argument for putting the subject where a second reader can see it.

*(Surfaced by `3.0.0_SA_CVO`, who counted the fabric-wide rate rather than accepting another seat's count as
a personal one.)*

---

## The mechanism — comp-tools are foundational, not additive

> **Andrew-direct 2026-08-05:** *"Agents need to have readily available mechanisms to fetch the
> 'right' information, versus stochastically bouncing around context and grepping, where they might
> not even be in the right region off a semantic grep, and ironically enough the grep results may
> have a -head truncation and even if they're right they miss the nugget of info they needed. **This
> is why the comp-tooling is not additive, it is foundational.**"*

A doctrine that says *go and see* and stops is an exhortation. **Agents infer because retrieval has
been expensive and unreliable** — a raw grep lands in the wrong region, is text-local and
connection-blind, truncates at `head`, and can return the right file while missing the line that
mattered. Under those conditions inference is the *rational* choice. **So the remedy is not more
warning; it is cheaper retrieval.**

**Default reflex:** `comp-which "<plain-English question>"` — it routes to the right tool, or runs
the on-rails `comp-grep`/`comp-glob` itself. You do not need to know the catalogue.

| you want to know | call | what it CANNOT tell you |
|---|---|---|
| which tool answers this at all | `comp-which "<question>"` | — (never dead-ends; it runs the primitive) |
| where something lives / what cites it | `comp-grep <pat>` / `comp-glob` | liveness — a hit is a mention until read |
| what a named thread is made of | `comp-estate <name>` | NAMES come from a snapshot; read the provenance header |
| column gaps + consumers of a gold script | `comp-pipescript io <s> --pipeline <t>` | flagless is `rc=2` REFUSED — it never guesses |
| is deployed code the repo code | `comp-pipescript deployed` | whether it RAN |
| is a served artifact current | `comp-freshness` | contents; false-alarms without `freshness_basis: trading-day-frontier` |
| what breaks if I change this | `comp-blast <fn>` | coupling not expressed in the graph |
| does this role hold this permission | `comp-iam service <lambda>` | **`(action, resource)` — see below. It FAILS GREEN.** |
| cross-layer relationships | `comp-kuzu "MATCH ..."` | vintage, unless you read the provenance header |
| did I break a critical surface | `comp-surface-check` | portal-side BLOCKS (`rc=2`); workspace-side advisory. Silence is not a pass |
| is my gold output valid | `comp-validate <s> --artifact <f>` | `NO_CONFIG`/`ZERO_CHECKS` = UNVALIDATED, never SAFE |
| do records match the estate | `comp-state` | BM25 recall — BEHIND is a place to look, CURRENT is not a verified record |

**A tool's blind spot belongs in the same row as the tool** — principle 4 made operational. An
instrument that does not declare what it cannot see will be read as having seen everything.

**A GAP IN THE TOOLING IS A DEFECT, NOT AN INCONVENIENCE.** If you reached for a raw grep because no
comp-tool fit, that is a coverage gap: record it (the rail log audits overrides) and route it. A
repeated override for one intent means the tool should exist.

### Three mechanisms that must survive any cut

A prohibition without its mechanism loses to the agent's own instruments. These are
counter-intuitive enough that the *reason* must travel with the rule.

**`comp-iam` FAILS GREEN, AND SILENCE IS THE DEFECT.** It models `(action)`, never
`(action, resource)` — a role holding `s3:GetObject` on *any* bucket reports `[GRANTED]` for a call
to *every* other. It is also blind to derived-object calls (`boto3.resource(...).Table(...)`),
returned-buffer calls (`batch_writer`), and presigned URLs whose action occurs at redemption. **In
every blind case the grant IS required and comp-iam reports nothing** — so the risk is not
`AccessDenied`, it is **a future engineer doing least-privilege cleanup deleting a needed grant as
"unused."** Treat the operation list as a **FLOOR**, never a deletion warrant.

**`simulate-principal-policy` HAS THREE INDEPENDENT FALSE-DENY MODES.** (1) Two or more
`--resource-arns` in one call flips the **held** ones to `implicitDeny`. (2) It evaluates
`Condition` blocks, so with no `--context-entries` a conditioned statement denies **byte-identically
to a real deny**. (3) It does not validate action names — a **typo also returns `implicitDeny`**, so
a misspelling is indistinguishable from a missing grant. **Therefore: one ARN per call; the positive
control as a SEPARATE invocation** (mode 1 silently disarms a batched control — *the very control
the rule leans on*); `--context-entries` for conditioned statements; and
`accessanalyzer validate-policy` for action-name validity, never this.

**DESIRED IS NOT APPLIED.** `comp-iam`'s default view parses Terraform and cannot tell landed from
planned. For a fresh change, ground on the live primitive.

---

## What to measure

Error rate in this class is **irreducible** — the failure has no phenomenology, so knowing does not
prevent. Measure instead:

1. **Time-to-catch.** An error caught in 30 minutes with zero damage is the system working.
2. **Blast radius at catch time.** Append-only ledgers, revertible batches, gates before execution:
   these make an error survivable rather than terminal.
3. **Who caught it.** A gate that did not run gets no credit; an instrument that was not consulted
   gets no blame. **The estate funds the mechanism the story names — so name the right one.**

**What has actually caught things: lane gates (automatic, no recall required), population-wide
sweeps, peer reads, and time. Not one was "the agent remembered the rule." Build accordingly.**

---

## Incidents belong elsewhere

**Andrew-direct 2026-08-05:** incident reporting may be valid *in an explicit incident doc* when it
is **concrete** (the error can be codified and understood from the description) and a **novel
basis**. *"The main doctrine/controls/etc governance-style docs should not be flooded with incident
reports, at best they just reference an ID that goes to that incidence report/postmortem doc."*

**Rule for editing this file:** a principle earns its place by being **actionable without its
incident**. If you cannot state the mechanism without retelling what happened, the mechanism is not
yet extracted — write the incident record, extract the property, and cite the record here.

Incident records: `docs/references/`. Decisions: `org/tier0/ledger/LD-NNNN.md`. Reviews:
`org/tier0/reviews/RV-NNNN.md`.

**Open — a durable incident-ID namespace is NOT yet ratified.** Today's references are by
file/ledger/review id. Minting an `INC-NNNN` namespace is a taxonomy act under CLAUDE.md Rule 24
(MECE / same grain / intent coherence) and is proposed, not taken, here.

**The reference half.** Instrument-specific facts that cannot be derived and must be told — the
MSYS argv class, the paginated `length()` undercount, the aws-shim `--delimiter` mangle — are
**reference, not doctrine**: needed at a keystroke, not read in advance. They belong in a
**queryable lookup reachable from `comp-which`**. Building it is the open item this rewrite creates
(Andrew-direct 2026-08-05: routed to `1.0.0_SA_CTO~B`). Until it lands they are preserved in
`docs/references/` and in git history at `913e3365d6`.

---

*Rewritten 2026-08-05 by `4.0.0_SA_CRO` on Andrew-direct instruction. Predecessor authored primarily
by `1.0.0_SA_CTO`/`~Z` with MSTR, COO, CVO~Z, AE~C. **The cut is of duplication, rhetoric, and
incident narrative — not of their findings.** Every mechanism above is theirs.*


---

## Grounded evidence in agent memory

> Citations of the form `memory/<slug>` root at the **agent memory DIRECTORY**
> (`~/.claude/projects/C--Users-AndrewBerman-Desktop-ajb-workspace/memory/`), **now under version
> control** (genesis `6843c2f`, 2026-08-05). Those records are the *grounded incidents* — typically
> 40–60 lines each with measured numbers; the law here is their compression. **Doctrine holds the
> law; memory holds the evidence.** Wired 2026-08-05 on Andrew-direct; the two corpora had **zero**
> links between them before that.

- `memory/feedback_a_retrieval_that_resolves_to_the_wrong_referent_reports_success` — the root, exactly: a retrieval that lands on the wrong thing reports success.
- `memory/feedback_grep_absence_of_literal_not_absence_of_use` — principle 1, the proxy: a missing string is not a missing use.
- `memory/feedback_a_check_authored_by_the_checked_party_is_not_a_control` — principle 4.
- `memory/feedback_shared_derivation_instruments_cannot_cross_check` — principle 3: a tie is evidence only when the legs differ in derivation.
- `memory/feedback_checks_that_pass_on_the_confirming_limb` — principle 4, six live instances in one session.
- `memory/feedback_known_good_is_a_content_claim_read_values_before_republish` — principle 2b: a vintage check is not a content check.
- `memory/feedback_verify_live_state_before_treating_mutation_as_noop` — principle 2.
- `memory/feedback_profile_before_reporting_a_mechanism` — right conclusion, wrong mechanism; the class this file's own author committed twice on 2026-08-05.
