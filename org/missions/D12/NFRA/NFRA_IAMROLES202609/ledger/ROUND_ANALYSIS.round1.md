# NFRA_IAMROLES202609 — ROUND 1 ANALYSIS (L10 answered)

**archetype:** VALIDATE

| | |
|---|---|
| **Written by** | `1.0.0_SA_CTO~Z` |
| **Written** | 2026-09-10 ~11:5xZ |
| **Answers** | the round-1 slug, `surprise-channel/remediations/REMEDIATION_v1.Z.md` @`fd7a0b3e91` (msg 20919) |
| **Verdict** | **ROUND 1 DOES NOT CLOSE. IT RECUTS** — one judgment criterion FAILS, and this project has the same missing-record blocker as its sibling |
| **Recut owner** | `2.0.0_SA_COO~ZI`, one issuance |

---

## 1. COVERAGE READ, PER OUTCOME

**Denominator: 8 outcomes declared in the PRD header at v0.2.** Derived by reading all 9 task orders
UNSCOPED — **not** from a completion report, because none exists (§5).

| | |
|---|---|
| **COVERED** | **8 of 8** — every outcome has at least one terminal cell |
| **UNCOVERED** | **ZERO** |

**No PRD addendum is owed on coverage grounds** — the uncovered partition is empty, which selects the
round-N analysis route. (A PRD correction *is* owed on other grounds; §4.)

---

## 2. THE ONE FAILED GRADE — `IAMs6-AC5`, AND IT IS CORRECTLY A FAIL

9 of 9 judgment criteria graded: **8 PASS, 1 FAIL.**

`GOVERNANCE_DISPOSITION.md` defines its primary token in terms — *"the disposition is IN-CODE AS A
FACT, NOT A RECOMMENDATION"* — and then applies `IN-CODE` to **eight members the same document
measured as ABSENT**. A reconciling sentence in a different paragraph gives the same token a second,
incompatible intent, so `IN-CODE` means *"is declared"* for one item and *"ought to be declared"* for
eight others.

⛔ **WHY THIS IS A FAIL AND NOT A WORDING NIT, and this seat agrees with the grade:** the coverage
line reads **"10 IN-CODE, 6 exempt."** A governance reader takes that as ten of sixteen undeclared
roles now being declared. **Roughly two are.** The token meant to *carry* the finding is the one that
*erases* it — a taxonomy carrying two intents on one axis, which is Rule 24(iii) exactly.

⭐ **WHAT IS EXPRESSLY NOT WRONG, and the recut must not disturb it:** the six EXEMPT lines are
exemplary — individually reasoned, non-templated, each naming the decision owed **and** why no owner
could be named, with the cell correctly refusing to invent one. **The research is sound; only the
vocabulary that reports it is not.**

**REMEDY: split the token and correct the coverage line. One edit per affected row. It touches no
research and re-opens no measurement.**

---

## 3. THE ROUND'S SIGNATURE — MOST THREADS ARE DOWNSTREAM OF HOW IT WAS *ISSUED*

⛔ **THE HAND-OVER PROMPT IS NOT THE COMMITTED ORDER.** Four of four respawns delivered a worker face
**richer** than the file on disk, and **no gate can catch it, because no gate reads a spawn prompt.**

**The mechanism is a v3 consequence nobody wrote down:** the spine's *"a face is never patched by a
message"* assumes the face travels **once**, at the cut. On this harness a completed worker **cannot
be resumed** (`Z-S4`, measured two ways), so every cell after a slot's first is a **fresh spawn whose
prompt re-states the face** — and a re-stated face is an opportunity to improve it. Improving it
silently forks the record: the worker is held to the better bar, the grader reads the older file.

⭐ **THE LANE'S RESTRAINT WAS CORRECT AND IS RECORDED AS SUCH.** It did **not** retro-amend the
terminal orders, because *amending a completed order so the spec matches what was delivered is
indistinguishable at HEAD from amending it so the spec matches the RESULT.* It carried the delta in a
row instead. **That is the right call and the right reason**, and the grades were taken against the
delivered bar.

**THE FIX FOR THE NEXT CUT IS ONE LINE:** amend the order **before** the spawn, or deliver the file's
face verbatim. `2.0.0_SA_COO~ZI` already names it; it is carried, not re-raised.

---

## 4. THE POPULATION DEFECT — AND IT IS **THIS SEAT'S ARTIFACT**

`Z-S6` / `Z-W3-S2`: the "settled set of 16 undeclared roles" **contains a confirmed false positive.**
`seeking-alpha-scraper-role` is classed LIVE-no-DECLARED and **is declared** at
`infra/aws/terraform/seeking-alpha/main.tf:241`. Found by a worker, confirmed by the issuing lane on
a **different instrument** (a pathspec-scoped Terraform read, 1 hit / 569 files) with a **negative
control** (an undisputedly undeclared role, 0 hits / same 569). **So the set is AT MOST 15.**

⭐ **THE KEEPER IS THE MECHANISM, NOT THE MEMBER: A STABLE COUNT ACROSS THREE VINTAGES IS CONSISTENT
WITH A STABLE MISCLASSIFICATION.** Member identity was established by classing each member against
the same instrument's output at two vintages — which can only show the classifier was **consistent**,
never that it was **correct**. The "two corroborating substrates" **shared the classifier under
test**. It surfaced only because *disposing* of each member forced a per-member read against
Terraform — a different plane from the one that built the set.

### ⛔ AND THE PRD IS WORSE THAN THE SET: IT CARRIES THREE IRRECONCILABLE DENOMINATORS

Measured in this seat's own artifact at v0.2:

| line | reads |
|---|---|
| `:70` | "the coverage is zero of **208**" |
| `:101` | "**16 of 208** are governable" |
| `:297-298` | "16 of 208, corroborated across two substrates and re-measured at the merged head (**216** hit(s) / **216** aws node(s))" |
| the FAIL's own evidence | "absent from the fresh **191**-role comp-iam parse" |

**208, 216 and 191 — two of them in a single sentence, presented as corroboration.** This is the
shape the sibling project named as *an artifact that outlived its truth and kept directing*, and it
is directing: the brief, this PRD and the L5 decomposition all carry 16-of-208 as settled.

**THIS IS THIS SEAT'S DEFECT.** The PRD is the L4 artifact and this seat authored it.

⚠ **THE CORRECTION MUST NOT INVENT A NUMBER.** Which of 191/208/216 is right is *not established* —
they may be three different populations (all roles, governable roles, graph nodes) or one
misclassification, and nobody has reconciled them. **The honest edit is to stop asserting a settled
figure and record the disagreement with each reading's vintage and instrument.** Determining the true
denominator is *work*, and it is §5's cell — not a sentence this seat can write today.

---

## 5. WHY ROUND 1 DOES NOT CLOSE — AND THE SECOND REASON IS NOW A PATTERN

Rule 27: **CLOSED needs `COMPLETION_REPORT` + `COMPLETION_GRADES`, every grade `REALIZED`.**

**(i) `IAMs6-AC5` is a FAIL**, so not every grade is REALIZED.

**(ii) ⛔ THERE IS NO `COMPLETION_REPORT` AT ANY ROUND** — `ledger/` was empty before this file. **That
is the identical blocker this seat named on NFRA_OPSEC202609 hours ago, now on a second project.**

⭐ **TWO PROJECTS INDEPENDENTLY REACHING "ALL WORK TERMINAL, ALL FINDINGS DISPOSITIONED, NO COMPLETION
REPORT" IS NOT TWO OVERSIGHTS — IT IS AN UNPROMPTED ARTIFACT.** Nothing asks the COO for it, nothing
refuses without it, and both lanes reached L8 without one. Named here because the sibling's version
read as one lane's miss and a second instance changes what it is.

⚠ **AND NO L8 PACKET WAS EVER SENT FOR THIS ROUND.** `3.0.0_SA_CVO~Z`'s own compile stands as the
round's compile, and that seat flagged — correctly — that where its arithmetic and the lane's
eventual compile disagree, **the disagreement is itself the finding** rather than its own numbers
winning by default. That is the right posture and this seat adopts it: the completion report, when
written, is a **check on** this analysis and not a formality after it.

---

## 6. WHAT THE RECUT MUST CARRY — `2.0.0_SA_COO~ZI`, ONE ISSUANCE

**R2-A — the token split (from `IAMs6-AC5`).** Split `IN-CODE` into its two intents and correct the
coverage line. Cheapest cell in the round and it converts a FAIL into a grade. ⚠ **Touch no research
and do not re-open the six EXEMPT lines** — they are the part that is right.

**R2-B — reconcile the role denominator (from `Z-S1`, `Z-S6`, `Z-W3-S2`).** Establish what 191, 208
and 216 each count, on the instruments that produced them, and what the undeclared population
actually is. ⚠ **The acceptance criterion must require a PER-MEMBER read against a plane that did not
build the set** — the whole finding is that same-instrument agreement across vintages proves nothing.
The false positive was found exactly that way.

**R2-C — the three governance decisions, which are the deliverable rather than a gap.**
`Z-W3-S3/S4/S5`: AWS-service-default roles needing a named exemption owner; **two PRODUCTION
SERVING-PATH roles** carrying a heavier claim; and one role whose honest outcome is **DELETE**, which
the cell's binary IN-CODE/EXEMPT schema cannot express. ⛔ **The schema needs a third value before a
cell can record that outcome** — a binary axis cannot express retirement, and forcing it into EXEMPT
would repeat §2's defect on a different axis.

**NOT IN THE RECUT:** `Z-S3` is **superseded** by this seat's comp-rail repair @`6228c53377`, now on
origin — ⚠ not retroactively, and not on the other fabric until it pulls. `Z-S7` is discharged.

---

## 7. WHAT IS OWED, BY WHOM

| owner | act |
|---|---|
| `2.0.0_SA_COO~ZI` | the round-2 recut — **R2-A**, **R2-B**, **R2-C** in one issuance; and `COMPLETION_REPORT.round1.json`, which no gate will ask for |
| `1.0.0_SA_CTO~Z` | the PRD correction at §4 — stop asserting a settled denominator, record the three readings with vintage and instrument; `COMPLETION_GRADES` when a round's grades are all REALIZED |
| `3.0.0_SA_CVO~Z` | nothing for round 1 — its engagement ended at the slug |
| — | **Nothing is owed by Andrew.** `Z-W3-S3/S4/S5` name decisions with no repo-side owner; whether they escalate is the recut's finding, not a call raised here. |

**Push state:** LOCAL at write time; only `0.0.0_AB_MSTR~Z` pushes.
