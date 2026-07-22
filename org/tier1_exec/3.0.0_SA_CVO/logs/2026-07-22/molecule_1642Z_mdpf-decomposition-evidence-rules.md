# MOLECULE: `MDPF_DECOMPOSITION_EVIDENCE_RULES_20260722.md` @83800a6cb   (scale: MESO)
**archetype:** VALIDATE

Run by `3.0.0_SA_CVO` on Andrew-direct ~1635Z (*"Give this to CVO to /molecule"*), relayed by
`2.0.0_SA_COO` @163723Z. Target authored by `2.0.0_SA_COO`, 145 lines, 8 rules + 4 standing hazards,
**self-declared BINDING on its own author at decomposition time.**

**Lane confirmation COO asked for:** this is **MINE**, not `~Z`'s. Subject is MDPF decomposition
evidence = main-fabric verify under LD-0325; `~Z` holds NFRA/SYSPARITY/ontology. COO's routing was
correct.

---

## Unit + expected role
A **coordination document** that pre-commits the COO to evidence standards at TO-decomposition time —
the step immediately after the CVO gate in Andrew's 1552Z resumption path. Not code, no runtime, no
consumers that execute it. Its "behavior" is entirely **what it will cause a future COO session to do
or refuse.** That makes Dimension 4 a reading of its *binding force*, not of a code path.

## 1. Composition — what it actually is vs declared
**Declared: "rules binding on me." Actual: matches.** Every rule is stated as a constraint on the
author's own future action, with a live defect cited as its origin. **No declared-vs-actual drift in
the document's self-description.**

**The provenance the author flagged is real and I am treating it as they asked.** R3 is COO grading
COO's own co-sign limbs. R4's live instance is COO's own composite. **I did not go easier on it; §5's
DIG-1 is against R3 specifically.**

## 2. State — N/A as a runtime artifact; live as a RECORD
No S3/DDB state. **But it carries factual claims about live state, and those I read directly:**

| claim in the file | my independent measurement | verdict |
|---|---|---|
| `fact_model_assignment` holds **2 data days** | **2 keys, 2 dates: `2026-07-21`, `2026-07-22`; zero pre-07-21** | **EXACT** |
| `bd` does double duty (firm alias **and** custody enum) | `mdpf-daily-trigger:76-84,404-411` — `CUSTODY_SOURCE` is a real `bd\|schwab` switch on an SSM param | **CONFIRMED** |
| 3-firm tuples run in production siblings | **independently confirmed DEPLOYED *and* EXERCISED** in my A3: 104 cottonwood rows in `opal-etfs-ownership-daily`, 84 in `opal-assets-daily-aua` | **CONFIRMED, stronger than stated** |
| `PUBLISH_MAP` denominator is `len(PUBLISH_MAP)` | `opal-assets-mdpf-portal-publisher:103,106` | **CONFIRMED** |

**The author's facts are accurate.** Everything below is about **inferences**, not numbers.

## 3. Position in the chain
- **Upstream:** doctrine §7f @f9f6a4c72 (0.7.0) · DE's self-audit @64c3ed4b1 · my A11/axis-D · CTO's
  R1–R13 · Andrew 1552Z.
- **Downstream:** COO's own future TO decomposition — **and nothing else consumes it.** Its whole
  reach is one agent's future behaviour across a reset.
- **Position smell:** this is a **single-point-of-failure record with exactly one consumer who is also
  its author.** If that session resets and does not re-read it, the document has no independent
  enforcer. That is the *acknowledged* reason it exists ("a bound whose only carrier is a message is a
  clock with no keeper") — **but writing it down converts a message-carrier into a file-carrier, not
  into a gate.** No mechanism reads this file. **Rated WATCH-1.**
- **Seams to hand to `/seams`:** (i) this file → CTO's R1–R13 (two rule-sets, no reconciliation
  mechanism); (ii) this file → my `/verify` verdict (R7's predicate, now stale — see DIG-2).

## 4. Behavior — what it will actually cause
Exercised as far as a document can be: **I applied its own rules to its own content.**
- R2 applied to R1's table: **passes** — R1 correctly classifies its own denominators.
- R2 applied to R3's disposition: **fails** — see DIG-1.
- R1 applied to R1: **partially fails** — see DIG-3.

**A rule-set that survives being applied to itself is stronger than one that has not been tried.
This one survives 6 of 8.**

## 5. Semantic quality + smell pass

### >> DIG-1 — R3's second example is CLASSIFIED BACKWARDS, and striking it would REMOVE THE DETECTOR FOR THE WORST DEFECT I FOUND. <<
R3 says the limb *"every pre-07-21 Global value is byte-identical with Cottonwood absent"* is
**TRUE BY CONSTRUCTION** (cottonwood has no pre-07-21 model data) and should therefore be **STRUCK as
non-probative**.

**The number is right. The inference rests on a hidden assumption:**
> *"cottonwood has no pre-07-21 data"* ⟹ *"cottonwood's presence in the fold has no pre-07-21 effect."*

**That assumption is FALSE under the all-or-nothing null rule** (`dim_mdpf_aggregate_aua_timeseries.py:1226-1240`):
`None if None in (m49, nm49, minf)` — **a null term nulls the entire row.** So:

| build | pre-07-21 global row |
|---|---|
| cottonwood **absent from the fold** | the computed number |
| cottonwood **in the fold contributing nulls** (what R2 mandates) | **`None`** |

**These are not byte-identical. The limb FAILS — and what it catches is precisely my §7 finding
(a naive N-firm fold nulls the entire pre-07-21 global history).**

> **R3's own criterion does not apply: this limb's falsifier is REACHABLE, and it is the most serious
> defect in the plan. Striking it removes the only limb pointed at it.**

**The irony is worth naming precisely because the rule is good:** R3 exists to strike limbs that
*"would pass with a broken pipeline."* It was applied to a limb that would **fail** with the specific
breakage the plan is about to introduce.

**HONEST DEPENDENCY — this cuts both ways and I will not overstate it.** My §7 is a **derived
prediction about unbuilt code**. If S2a is built with **pre-onboarding-absence = ZERO** (the fix I
proposed), cottonwood contributes 0 pre-07-21, the row computes identically, and **COO's "true by
construction" becomes CORRECT.**
> **Therefore the real finding is that R3's disposition is PREMATURE, not simply wrong: it cannot be
> settled until the fold's null-handling is decided. Classify it after that decision, not before.**
`grounding: SOURCE-CONFIRMED dim_mdpf_aggregate_aua_timeseries.py:1226-1240 @d1454d183` + S3 measurement
(`fact_model_assignment` = 2 dates, both ≥ 07-21).

### DIG-2 — R7's factual predicate is STALE, and it is the file's own hazard #4 happening to the file
R7 reads: *"8 are unverified and A11 has already FAILED."* **My `/verify` completed 12 of 12 at
`399d6f834`**, which is *the same commit this document was pushed under*. **R7's blocking condition is
discharged; its principle stands.**
**This is exactly the fourth standing hazard the file itself lists** — *"a cascade sourced from a
message cannot detect its own supersession"* — **occurring to this document, about my work, inside
minutes.** No fault: COO wrote an accurate number that my next action invalidated. **It is the
strongest possible evidence for the hazard being real, and it argues the open question COO poses
(*"who reaches the agents already carrying it?"*) deserves a mechanism rather than a note.**
`grounding: SOURCE-CONFIRMED 399d6f834`

### DIG-3 — R1 overstates the READ fraction: sound WITHIN a file, config-bound ACROSS files
R1: *"Only the READ fraction is evidence, because a file's length is a fact about the world."*
**True of the denominator. Not true of the population.** *Which files* get read — "the three densest"
— **is an enumerated list somebody chose**, and is therefore subject to R1's own critique: a file
nobody thought to list is invisible to the fraction **and to any review of it.**
> **"`X` is 31% read" is evidence about `X`. "Phase 0 is 10%/33%/31% read" is NOT evidence about
> Phase 0** — it is evidence about three files chosen by the instrument.
R1 should carry the file-set as a **fourth, config-derived denominator that FAILS §7f**, exactly as it
does for axes A/C/D. **As written it promotes the read fraction from "sound per file" to "the one
sound axis," which is the promotion §7f exists to prevent.**
`grounding: SOURCE-CONFIRMED the target file :20-29`

### WATCH-1 — the carrier is a file with one consumer who is also its author
See Dimension 3. Converting a message-bound into a file-bound removes the reset-death failure mode
**but installs no enforcer.** Nothing reads this file at decomposition time. **The document is
correct that it is "the carrier"; it is not yet a gate**, and its own R-series is the kind of content
CTO's R1–R13 got a numbered ledger for.

### WATCH-2 — two unreconciled rule-sets with colliding numbering
CTO's **R1–R13** and this file's **R1–R8** both bind decomposition, both are called "R*n*", and
**nothing reconciles them.** *"R2"* now means the coverage-denominator rule here and *"Cottonwood joins
the trading-day axis"* in CTO's plan. **A future TO citing "R2" is ambiguous.** Cheap fix, real
collision, and precisely the "two records of the same thing with no gate keeping them in agreement"
seam MSTR and I have both hit today.

### NOTE-1 — R5's corollary is the sharpest line in the document
> *"During a hold, work stops hitting walls — so axis discovery stops too. The enumeration is the one
> thing that should still be running."*
**All four axes were discovered by a failure, not by a review** — I can confirm mine was found by
accident, in DynamoDB, while verifying something else. **If discovery is failure-driven and a hold
suppresses failures, a hold silently suppresses discovery.** I endorse this without reservation and
think it belongs in CTO's plan, not only here.

### NOTE-2 — R8's factual basis is stronger than R8 claims
R8 cites the sibling tuples as *running*. **I verified them deployed AND exercised** (§2). R8 may
state that at full strength. **One citation-hygiene point:** `opal-assets-daily-emitter:696` is a
**repo** line; the **deployed** artifact carries it at **`:620`** (deployed is HEAD-minus-80,
additions only, tuple byte-identical). Per CLAUDE.md, a line citation without a vintage is not a
citation.

---

## Smell findings

| Smell | Rating | Evidence | Why it caught my eye |
|---|---|---|---|
| R3 ex.2 classified backwards; striking it removes the §7 detector | **DIG** | target `:57-59` vs `dim_mdpf_aggregate_aua_timeseries.py:1226-1240` | A rule for striking limbs-that-cannot-fail, applied to a limb that would catch the worst live defect |
| R7's predicate stale (8 unverified → 0) | **DIG** | target `:104` vs `399d6f834` | The file's own hazard #4, happening to the file, about my work |
| R1 promotes the READ fraction past its own critique | **DIG** | target `:20-29` | The file-SET is a chosen list — R1's exact objection, unapplied to itself |
| Carrier has one consumer who is also its author | **WATCH** | Dimension 3 | A file-bound is not a gate; nothing reads it at decomposition time |
| `R1–R8` here vs `R1–R13` in CTO's plan, unreconciled | **WATCH** | both docs | "R2" already means two different binding things |
| R5's hold-suppresses-discovery corollary | **NOTE** | target `:90-92` | Correct, non-obvious, and belongs upstream in the plan |
| R8 understates its own evidence; `:696` is a repo line | **NOTE** | my A3 | Citation-vintage hygiene on an otherwise stronger-than-stated claim |

## Assessment
**A genuinely good document with accurate facts and three inference defects, one of which is
consequential.** It survives being run against its own rules 6 of 8 — a higher bar than most evidence
standards clear, and I applied that test *because* the author asked me not to go easy on their own file.

**The consequential one is DIG-1.** If R3's disposition were carried into decomposition as written, the
byte-identity limb would be **struck as non-probative** — and that limb is the one thing pointed at the
pre-07-21 null-wipe. **The correct action is not to reclassify it now in the other direction either;
it is to DEFER the classification until S2a's null-handling is decided**, because the same limb is
genuinely non-probative under one design and genuinely load-bearing under the other.

**Routes:** DIG-1 → **COO + CTO** (it changes a co-sign limb's disposition and couples to my §7
stop-before-build). DIG-2 → COO (record refresh; the mechanism question is MSTR's message-only-bounds
sweep). DIG-3 → COO (amend R1). WATCH-2 → CTO+COO (numbering collision). **No gate rendered — this is
characterization; the formal verdict machinery is `/verify-channel`'s.**

## Knowledge-parity delta + residual
**Believed→true:** R7's "8 unverified" → **0 unverified, 12 of 12 @399d6f834**. R8's tuples
"declared" → **deployed + exercised**. `fact_model_assignment` = 2 days → **confirmed exactly**.
**Corrected by me:** nothing in COO's file — it is COO's record and I do not edit another agent's
deliverable; all three DIGs are **routed**, per XXX.md core-document discipline.
**NOT exercised:** R4's `publisher/producer logic NOT COVERED BY ANYONE` cell — I did not verify that
nobody covers it, and *"nobody covers it"* is an absence claim I would need a stated denominator to
make. **It stands as COO's claim, unverified by me.** R6's `1,225 distinct data days` figure is COO's;
I did not re-measure it.

## Compiler Tools
| Tool | Result |
|---|---|
| `comp-which` (A10 routing) | routed to `pipescript`; used it |
| `pipescript --resource` | *"no thread references json/mdpf/inflection/aggregate-aua-timeseries.json"* — confirmed A10 |
| raw `aws s3api` (rail-checked ×3) | partition enumeration; **no comp-tool enumerates per-table partition dates** — `comp-freshness` returns EXISTS/FRESH on a named artifact. **Coverage gap worth a tool.** |
| `aws lambda get-function` | deployed-artifact download for A3 (deploy-verify, operational) |

-- `3.0.0_SA_CVO`, 2026-07-22
