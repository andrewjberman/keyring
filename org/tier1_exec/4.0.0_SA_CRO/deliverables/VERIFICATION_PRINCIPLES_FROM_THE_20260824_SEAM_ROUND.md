# VERIFICATION PRINCIPLES — extracted from the 2026-08-24 seam round

**Author:** `4.0.0_SA_CRO` (base) · **2026-08-24** · **Scope: CRO fabric**, offered wider as candidates.

**Written to the editing test in CLAUDE.md: a principle earns its place by being ACTIONABLE WITHOUT
ITS INCIDENT.** Each item below is stated as a mechanism first. The instance that produced it is a
citation, never the content — several would have been unusable if written the other way round.

**Provenance:** one evening, six seats, ~40 cross-seat reviews. Every principle here was produced by
a SECOND READER, none by the author of the thing it corrects — including the two produced against
this coordinator.

---

## 1. A mutant row names its EXPECTED RULE. A reject for the wrong reason is a FAILED control.

A mutant list that says only *"this must reject"* **cannot distinguish a control FIRING from a
control being BYPASSED BY A LOUDER FAILURE.** Run pass/fail, every row can go green while the rule
each row exists to test never engages.

**Test:** for each row, name the keyword you expect to fail. If the row cannot name one, it is not
yet a control.

*Instance: a harness checking only admit-vs-reject produced four false passes, all rejecting for the
same wrong reason. The specification defect was upstream of the harness — the mutant list had never
named expected rules, so a clean sweep would have been reported.*

## 2. "Name which rule fired" is satisfiable by a value that names NOTHING.

Where a schema composes, a root-level keyword (`unevaluatedProperties` and its kin) **co-fires on
every rejection**, because failing sub-schemas emit no annotations. Any control demanding *a named
reason* is then satisfied by that root artifact — **which is the wrong-reason ambiguity the control
exists to prevent, arriving inside the control.**

**Rule: the reported reason must be the NON-CASCADE rule — the specific failing keyword, never the
root artifact.** A control that accepts a cascade value has established that *something* failed,
which is what it already knew.

## 3. REASONED → PLACED → MEASURED. Only the third step is evidence.

Placing a remedy on a well-reasoned hazard is correct and should not wait. **But it is not
verification, and the gap between placement and measurement is where a program records a fix it does
not have.**

*Instance: a customer-identifier leak was reasoned by one seat, placed by the coordinator, and only
then measured by a third seat pushing an actual record through — ADMIT, zero errors. Every step was
right; only the last one was evidence.*

## 4. A self-check by an author over the author's own intent is GREENEST exactly when the author's model is what is wrong.

Structural self-asserts compare **what you wrote** to **what you meant**. They never meet a record.
So they pass most confidently in precisely the case where the author's model — not the author's
typing — is the defect.

**Test: has this instrument ever met an artifact it did not author?**

*Instance: a schema passed 3/3 self-asserts while being structurally unable to admit ANY record of
the family it had just been extended to admit.*

## 5. A schema whose validation depends on a HARNESS INJECTING A DIALECT works for its author and fails for its consumer.

The author's harness supplies what the artifact omits, so the omission is invisible from the author's
side and fatal from every other side.

**Generalised: the consumer's harness is the shape reality has. An author-side green is a claim about
the author's environment.** This is why a second implementation finds what a second reading cannot.

## 6. A required denominator whose defining set is UNPUBLISHED is not a strict contract. It is an UNSATISFIABLE one.

And the seat that hits it **looks non-compliant while being blocked** — the two are indistinguishable
from outside.

**The discriminator that resolves it: an EMPTY set published as zero is a perfectly good denominator.
An UNPUBLISHED set is not.** Those are different states and only one blocks anyone. If your contract
requires a count over a set only another seat can name, that seat owes the enumeration — including
when the honest enumeration is empty.

## 7. Printing a denominator makes a number CHECKABLE. It does not make it RIGHT. Audit the PREDICATE.

The denominator discipline is necessary and it is not sufficient. A printed count with an unaudited
predicate is a well-formed answer to a question nobody asked.

**Test: what did the predicate MATCH — not, what did it COUNT?**

*Instance: a substring match on a token answered a question about EVENTS and over-reported by 2.3×.
It was caught only because the author re-derived its own published figure three ways.*

## 8. THE DEFECT EXISTED ONLY IN THE JOIN.

Two artifacts, each individually correct, each authored carefully, composing into a defect **that is
present in neither document and in both.** Neither author can see it from their own side, because
from each side nothing is wrong.

**Consequence for seam review, and it is the practical one: a seam review where both sides verify
their own half and agree IS NOT A SEAM REVIEW.** You are checking whether the JOIN is correct, not
whether each side is. Read the counterpart's artifact against yours and ask what is true of the PAIR
that is true of neither member.

**Corollary — audit at the grain you intend to CONCLUDE at.** A pair-grain audit that concludes at
edge grain reports a surface covered when only one of its edges was named. *(This coordinator
committed exactly that error in the audit written to catch it.)*

## 9. Correcting a claim upstream DOES NOT correct the copies already made from it.

Not even your own. **A wrong claim from a coordinator does not read as a claim — it reads as CONTEXT,
and context is not re-derived.**

**The remedy is not care. It is the re-check sweep, run by every recipient INCLUDING THE FINDER.**

*Instance: the seat that CAUGHT a false claim had written it into its own plan nine minutes earlier,
from the summary, before its own source read produced the correction. Its words: "reading the source
did not immunise the cell already written from the summary."*

## 10. Severity has a DIRECTION, and the loud one is the safe one.

A defect that makes a **lawful** thing REJECT is self-announcing and gets found in hours. A defect
that makes an **unlawful** thing PASS is silent, and is discovered by whoever is harmed.

**When a fix closes one and a completion claim covers both, the one still open is the dangerous
one** — and the fix's own success is what makes nobody look.

## 11. A COMMENT IS NOT A CONTROL.

A field typed permissively, documented restrictively, is **a boundary with no control on it** — not a
control that failed.

**Test: walk every control past the hazard. If they all report PASS because the hazard is structurally
well-formed, the boundary is held by prose.**

*Instance: two objects with OPPOSITE data classifications shared one type. Five controls passed. The
only thing between that and a customer-data leak was a `$comment`.*

## 12. Fixing the INSTANCE is what produces the next finding. Rule the CLASS.

Three instances of one shape were fixed in one evening, each found by a different reader, **each
after the previous fix had been accepted.**

**When a remedy lands on one field, one row, one call site — ask what the CLASS is and scope the
remedy there.** The seat best placed to name the adjacent cell is usually the one that just had the
first one fixed against it.

## 13. "Correct by construction" is a property of TODAY'S DESIGN. It is not a control.

It is held in place by nothing except the design continuing to be what it is, and it is unfalsifiable
from outside the implementation.

**Take the structural constraint even when the construction-side guarantee is real** — otherwise one
side's continued correctness is the only thing holding a boundary, and no instrument fires when it
changes.

*Offered by the seat whose own emitter was the correct-by-construction one, arguing against itself.*

---

## The one that is not a principle, and is the reason for the other twelve

**EVERY defect in this round was found by a SECOND READER. NONE by the author.** Author-side rigour
was uniformly high — positive and negative controls, printed denominators, self-corrections filed
before anyone else could. **It was not sufficient in a single instance.**

*The author is structurally the last person able to see what their own fix did not cover.* Not
through carelessness — through having the model that produced the artifact.


---

# PART II — the overnight round, 2026-08-25 00:00–04:30Z

**Thirteen principles above came from six seats reviewing each other. These came from two external
adversarial passes plus the instruments built in response to them — and the pattern shifted:
Part I's defects were mostly in seat plans, PART II's ARE ALMOST ALL IN COORDINATOR PLACEMENTS AND
IN THE INSTRUMENTS BUILT TO CATCH THEM.**

## 14. A UNIFORM, CONFIDENT, WELL-FORMED ANSWER IS AN INSTRUMENT SIGNATURE, NOT A DEFECT SIGNATURE.

*N of N failing is not N independent corruptions. It is one systematic difference.*

**Test: before reporting a total or near-total failure, ask what single cause would produce exactly
this uniformity** — and test that cause first.

*Instances, same night: `sha256sum` reported 5 of 5 published files failing their own filename (a
newline-normalisation difference, artifacts fine); a bare `except` produced "all 14 rejected".
Both were caught by the author declining to send, on this reasoning alone.*

## 15. A DIGEST WITHOUT ITS NORMALISATION IS NOT AN IDENTITY.

The algorithm prefix says *how* it was hashed and still not *what* was hashed. LF-normalised text and
raw bytes give different digests for the same file, and on a CRLF platform that is every file.

**Publish both, each labelled.** Publishing only one makes the artifact unverifiable with the other
party's standard tool — which is how a correct mechanism generates confident false findings.

## 16. A VALIDITY CHECK CANNOT SEE A DELETION THAT REMOVES VALID CONTENT.

Syntax passes. Schema parses. The self-test passes **on what remains**. Every check asks whether what
is left is valid; **none asks whether something left.**

**The only instrument that sees it is a size delta**, which is why byte counts belong in every report
rather than being noise. *Instance: 7,535 bytes and a document's central object deleted, both controls
green, caught solely because the author prints byte counts by habit.*

## 17. A REPLACE THAT MATCHES NOTHING IS A NO-OP THAT REPORTS SUCCESS.

String-based patching fails silently when the target has moved. The edit "succeeds", the file is
unchanged, and the next verification reads the old state as the new one.

**Patch by index or by a pattern you assert on first, and verify the specific change** — never a
generic marker, which a neighbouring edit can satisfy.

*Committed twice in one file in one hour, plus a verification that returned a false green by finding
a marker left by an unrelated earlier correction.*

## 18. PROVENANCE IS NOT CORRECTNESS.

A ruling is binding; **a coordinator's translation of it into a contract is not.** A faithful citation
can still alter subject, grain, authority, timing, failure direction, or scope.

**A placement records BOTH the decision it descends from AND the interpretation applied**, or a
reviewer can only check that the edge exists — never whether the translation drifted.

*Found by an external reviewer, in an instrument I had built to catch coordinator defects and had
exempted one class of my own placements from.*

## 19. AXES FIX FUSION. THEY DO NOT FIX CARDINALITY.

Separating conflated dimensions is necessary and does not touch *"one claim = one evidence record."*
A claim resting on two runs is not supported by one honest record of either.

**And the cardinality must declare its CONTEXT KEY — "3 distinct" is not a requirement until it says
3 distinct WHAT.**

*Three rounds of correct de-fusing left the overclaiming incentive untouched, because nobody had
questioned the record-per-claim assumption.*

## 20. AN ARTIFACT MUTATED IN PLACE IS AN ARTIFACT ITS CONSUMERS CANNOT TRUST.

Publication must be transactional: draft → checks → digest → immutable version → **then** the pointer
moves. Consumers hold the prior version until the new one passes.

**The broken file is the visible failure; the SILENT one is a partially-edited file that still
parses** — read, adopted, and reported against a shape that was mid-flight, with nothing to show it
happened.

---

## The Part II observation, and it is about the coordinator

**Every principle in Part II except 14 and 16 came from a defect in something I built or placed.**
Two external passes found five; the instruments I built in response then found four more in each
other and in themselves.

*The seats reviewed each other rigorously all night and were right almost every time. The reviewer
nobody had was mine.*
