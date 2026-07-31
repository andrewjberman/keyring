# C3 LABELING LAYER -- SPEC v0.1 (DRAFT, ISSUED TO CVO FOR REVIEW)

**Author:** `0.7.0_AE_CloudOps~B` · **Date:** 2026-07-31 · **Status:** **v0.2 -- REVISED AFTER CVO REVIEW (164214Z), re-issued**
**v0.2 changes:** s.2.2 rewritten as a RESOLVED worked example (CVO closed it under the escalation role) + new s.2.2.1/2.2.2 · **s.2.2.2 SOURCE-FIRST added as C3L.6 step 1** -- the third path neither this spec nor the estate had · s.6 requirement **4** added (basis travels with the label at every quote site) · s.10 six questions -> six rulings · C3L.1 cross-fabric rail dependency named · 14/14 upgraded to CVO-verified
**Tasked:** Andrew-direct via `1.0.0_SA_CTO` 163330Z -- *"have 0.7.0~B run the spec based on the text ive sent you and COO. Then have them issue that spec to CVO for review"*
**Arch fences:** `1.0.0_SA_CTO` 163330Z · **Relay:** `2.0.0_SA_COO` 161347Z
**Reviewer:** `3.0.0_SA_CVO`. **CVO REVIEWS; IT DOES NOT CO-AUTHOR.**

> **THIS IS A SPEC. IT BUILDS NOTHING, LABELS NOTHING, WALKS NOTHING.**
> Andrew: *"we need to build the system with 0.7.0~B into the Kimi loop not be doing anything ad hoc."*

---

## 1. Andrew's words, verbatim and in order

> **(1)** "This is another opportunity for a semantic review pipeline, I think it can be built into the Kimi Review cycle. IN essence each c3.ii and potentially c3.i needs a human vs CTO and CVO agreement on the state of each system."
> **(2)** "that is how the lifecycle stage is maintained"
> **(3)** "the part that we have been desigining thus far with 0.7.0~B is the high level signal, but there can be an additional layer of essentially tracking c3 and labeling them. I think the idea is that the CTO and Andrew (human user) go through the various c3 items, and if there is a doubt about it, then CVO investigates and reports back so Andrew and CTO can confirm."
> **(4)** "this needs a dedicated series of TOs wrapped into the project, relay all of this to CTO"
> **(5)** "we need to build the system with 0.7.0~B into the Kimi loop not be doing anything ad hoc"

**(3) CORRECTS (1), and the spec is built on (3).** (1) reads as three flat agreeing parties. (3) names the actual shape: **CTO + Andrew walk the items; CVO investigates ON DOUBT and reports back for those two to confirm.** COO's first relay over-flattened it and self-corrected. **CVO IS AN ESCALATION PATH, NOT A STANDING THIRD SIGNATORY** -- which also matters procedurally: a spec writing CVO into every decision would be CVO reviewing its own workload.

---

## 2. The problem, stated as measured facts

**All 14 landed WS-E1 contract declarations carry `lifecycle_class: UNDECLARED`.** That is not neglect. The ratified rule bank requires:

> `lifecycle_class: "exactly one lifecycle.enum value, PRODUCER-ASSERTED."`
> `"PRODUCER-ASSERTED, NEVER OBSERVER-INFERRED. The observer cannot distinguish never-yet from dead BY LOOKING -- that is the entire problem... Transience cannot be derived; it must be DECLARED."`

**And no mechanism existed by which any producer was ever ASKED.** `~D` could only record the absence of an assertion. The registry demanded a declaration the estate had no way to obtain.

Three ESTATE workstreams hit the same wall from three directions on 2026-07-31:

| | what it hit |
|---|---|
| **E2** | a DELIBERATELY DISARMED pipeline and a NEGLECTED one have an **identical census signature**. E2's own acceptance criterion, followed mechanically, would **RE-ARM a ratified safety disarm**. |
| **E5** | a boundary declaration is **PRODUCER-ASSERTED**; the registration invariant binds SHAPE and can never bind TRUTH. |
| **E3** | Tier-C mechanical signals are never sufficient -- **a deliberate belt and a corpse are identical on every one of them**. |

> **A MECHANICAL SIGNAL CANNOT EXPRESS INTENT, AND AN INSTRUMENT THAT CANNOT SEE INTENT WILL CONFIDENTLY RECOMMEND UNDOING A DELIBERATE ACT.**

The rule bank states the same thing at the root: one "absent" symbol stands for **at least four states** -- never-existed, deleted, absent-by-design (a trough), and not-yet-occurred. **Absence is not a state; it is a set of states, and an existence check cannot partition it.** Re-observation does not help: sampling harder makes you *more confident and no more correct*.

**Andrew's ruling supplies the missing channel.**

## 2.1 Why MAINTAINED beats INFERRED -- with a measured failure

The alternative considered was scavenging intent out of residue (ledgers, Terraform rationale, commit messages). **It failed its own positive control on 2026-07-31**: a hyphen-vs-underscore predicate under-counted a target **4 hits against a true 13**, and without that loud failure four of five targets would have read *"none known."*

> **SCAVENGING IS OBSERVER INFERENCE WEARING A RECORDS COSTUME.** It reads like evidence because its inputs are documents, but the judgement being made is still the observer's.

Andrew's design **produces the record instead of inferring it.** That is this spec's core justification, and it has a measured failure standing behind it.

---

## 2.2 THE CANONICAL CASE, DOGFOODED -- `aggregator`

*Andrew-direct, permitting this as a case study: "It is fine to use inflection in this context... If these cases are being dogfooded as case studies, that is fine" (via CTO 163600Z, correcting a fence drawn too wide).*
**This section REASONS ABOUT the case. It does not measure it.** Every fact below is CTO's and COO's report, cited as theirs; nothing here was re-derived by me, and s.12 states what that means.

> **THIS CASE IS RESOLVED. It is presented as a WORKED EXAMPLE WITH A KNOWN ANSWER, not as an open
> question** -- CVO investigated it at 162413Z under this spec's own escalation role and closed it
> (s.2.2.1). Shipping it as live-and-open would make this spec's founding example stale at issue: the
> stale-record class, inside the document arguing against it.

**The item, as it stood.** A caller self-identifying as `aggregator` drives a full gold chain **daily**. Three EventBridge rules for that chain were **deliberately DISABLED** in a ratified safety disarm. The question the estate could not answer from live state:

> **Is `aggregator` the sanctioned successor path the disarm deliberately left open -- or a route that SURVIVED a disarm aimed at the other three?**

**Why no instrument could separate those.** The two readings have **identical live signatures**, and three independent instruments were tried:

| instrument | what it returned | why it cannot decide |
|---|---|---|
| **rule census** (142, denominator closed by measurement) | the three rules DISABLED | a sanctioned successor and a survivor both leave three disabled rules |
| **Lambda resource policy** | names only the three DISABLED rules | **true and completely misleading** -- a same-account IAM principal needs no resource-policy statement, so `aggregator`'s absence from it is not evidence of anything |
| **repo source search** | no caller found | invisible to text search either way |

> **THE RESOURCE-POLICY ROW IS THE WHOLE SPEC IN ONE LINE: a correct instrument, correctly read, returning a true answer to a question it cannot answer.** It is not broken and it is not lying. It simply has no channel for intent, so its silence gets read as a verdict.

**Why it is the canonical specimen.** Three properties, and the third is the one that matters:

1. **The missing thing is INTENT, not data.** More measurement produces more confidence and no more correctness -- the rule bank's own sampling-harder warning, live.
2. **The two readings have opposite consequences.** Sanctioned successor -> leave it alone. Survivor -> it is an ungoverned daily production path. **A mechanical acceptance criterion ("zero unscheduled production pipelines") would re-arm the disarm** -- the E2 finding, arriving through this exact item.
3. **COO and CTO INDEPENDENTLY classified it as a C3.ii state-of-system question before this spec existed.** The specimen was not selected to fit the design; the design was named to fit specimens like it.

**How the layer would resolve it.** Not by measuring harder -- by **asking the governance level that knows**:

```
  walk surfaces `aggregator` (C3.ii, state-of-system in doubt)
        │
        ├─ CTO + Andrew: was this route sanctioned by the disarm?
        │        │
        │        ├─ AGREED ──────────► lifecycle_class asserted + intent_source = walk record
        │        │                      + revalidate_by set
        │        │
        │        └─ DOUBT ──► CVO investigates the disarm's ratification record,
        │                      reports back ──► Andrew + CTO CONFIRM
        ▼
   E2's deliberate-hold DERIVES from that assertion -- it does not scavenge (s.8),
   so the acceptance criterion can no longer re-arm what was deliberately disarmed.
```

### 2.2.1 WHAT ACTUALLY HAPPENED -- and the third path neither this spec nor the estate had

**The answer was AUTHORED IN THE ARTIFACT'S OWN SOURCE.** CVO (escalation role, 162413Z) read
`inf-gold-trigger/lambda_function.py:243-262`. The function **enumerates four armed paths including the
silver aggregator direct invoke**, states that *"Disabling the rules is a PLACEBO... THE DOORS ARE NOT
THE CHOKEPOINT,"* and **moves the control INTO the function.** Live env measured, negative-controlled:
the release sentinel MATCHES, under a standing daily release co-signed Andrew+CTO+COO since 07-16.

**VERDICT: NEITHER successor NOR survivor.** The disarm was never aimed at stopping the chain; the
aggregator route was **known and enumerated**; the daily run is **the authorized normal state.** The
question was mis-framed as a binary, and both branches were wrong.

> **THE SEPARATION THIS SPEC DESIGNS FOR IS WHAT PRODUCED THIS ANSWER: THE SPEC AUTHOR DID NOT
> MEASURE; THE ESCALATION PATH DID.** s.2.2 said it would not go and find out, and it did not. The
> fence held, the doubt escalated, the escalation resolved it in ~8 minutes. That is the loop in this
> document working before the layer exists.

### 2.2.2 THE DESIGN CONSEQUENCE -- READ THE SOURCE FIRST

This spec offered **two** paths: measure harder (fails), or ask governance (the walk). **The
resolution came from a third that neither had:**

> ### **READ WHAT THE AUTHOR ALREADY WROTE.**

**C3L.6 makes source-reading the FIRST step on doubt** -- before anything escalates to Andrew+CTO.
Cost here: ~8 minutes. Without it, the walk **spends the two scarcest people in the fabric on
questions whose answers are already written down** -- and **the failure is silent, because a
governance answer to an already-authored question is indistinguishable from a governance answer to a
genuinely open one.** Both look like a walk working.

**This strengthens the thesis rather than weakening it.** The aggregator intent was recoverable *only*
because one diligent author wrote it into the function. That is **luck**. Nothing required them to,
nothing would have flagged its absence, and the next artifact will not be so lucky.

> **INTENT IS AUTHORED SOMEWHERE; THE ESTATE'S HABIT IS TO LOOK FOR IT IN LIVE STATE.**
> **THE WALK GENERALISES ONE AUTHOR'S DILIGENCE FROM LUCK INTO MECHANISM.**

And the three canonical properties survive intact: the missing thing was still **INTENT** (no amount
of instrument-layer measurement would have reached it -- all three instruments were correct and all
three were mute); the two readings still had **opposite consequences**; and COO and CTO still
classified it as a C3.ii state-of-system question **independently, before this spec existed.**

---

## 3. What the walk is

**A recurring, human-in-the-loop pass over C3 items that PRODUCES the producer assertion the registry requires.**

```
        ┌──────────────────────── THE C3 WALK ────────────────────────┐
        │                                                             │
        │   CTO + ANDREW walk the C3 items                            │
        │        │                                                    │
        │        ├── agreed ──────────────► ASSERTION                 │
        │        │                                                    │
        │        └── DOUBT ──► CVO investigates ──► reports back ──►  │
        │                                     (Andrew + CTO CONFIRM)  │
        └─────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
                   WRITES INTO THE WS-E1 REGISTRY
                    (no parallel store -- see s.4)
```

**Population.** C3.ii **certainly**; C3.i **"potentially"** (Andrew's own hedge -- kept as a hedge, see s.10 Q1). The distinction is load-bearing and comes from the ratified ontology:

- **C3.i DETERMINISTIC STRUCTURES** -- *discovered*, view-compiled, recomputed on source change.
- **C3.ii SEMANTIC VERTICALS** -- **DECLARED, NEVER DISCOVERED.** "The legislated business." A vertical exists only by a **naming act**.

> **C3.ii IS ALREADY THE DECLARED-NOT-DISCOVERED LAYER. That is why Andrew put the labeling there and why it fits without forcing:** a layer whose members exist by legislation is the natural home for an assertion that cannot be derived. The walk is a naming act about *lifecycle*, on a layer already constituted by naming acts.

---

## 4. Where it writes -- REGISTRY IS THE STORE, WALK IS THE WRITER

> **BINDING (CTO arch-gate, folded by COO @904fba4672): THE WALK WRITES INTO THE WS-E1 REGISTRY. IT DOES NOT BUILD A PARALLEL INTENT STORE.**
> Any design creating a second home for intent is **wrong by construction** -- the twin-canon hazard the rule bank exists to prevent, and the single most likely way this spec goes wrong.

**The fields already exist.** `contract_record.required` is `[intent_source, obligation, lifecycle_class, revalidate_by, locality]`. The walk populates three of them and invents nothing:

| field | what the walk supplies |
|---|---|
| `lifecycle_class` | exactly one of `PERMANENT · TRANSIENT · EVENT_CREATED · DORMANT · LEGACY · RETIRED · UNDECLARED` |
| `intent_source` | the walk record -- see the binding argument below |
| `revalidate_by` | the maintenance clock -- see s.5 |

### 4.1 The walk SATISFIES `intent_from_above`, and this is the load-bearing argument

The rule bank rejects a self-sourced declaration outright:

> `intent_source`: *"WHERE the obligation comes from -- a governance level ABOVE the artifact... An **intent_source naming the artifact itself IS the denominator-is-its-own-configuration defect and is REJECTED at declaration**."*

**A CTO+Andrew agreement is a governance level above the artifact.** It is not the artifact's own config, not its key name, not its directory position, and not an inference from its observed absence -- each of which the rule bank names as a rebuild of *"the comp-legacywriter name-pattern stopgap with more syntax."*

> **THIS IS WHY THE WALK IS LEGITIMATE AND SCAVENGING IS NOT, AND THE DIFFERENCE IS NOT EFFORT -- IT IS DIRECTION.** Scavenging reads UP from the artifact; the walk asserts DOWN from governance. The rule bank does not merely prefer the second; it rejects the first.

**Proposed `intent_source` value form:** a resolvable pointer to the walk record (the dated walk entry + its participants), never a free-text "agreed". **CVO Q3.**

---

## 5. MAINTAINED, not SET -- and it needs no new mechanism

Andrew's operative word is **"maintained."** A one-time intent annotation rots invisibly: measured 2026-07-31, an 18-day-old corpus record had **one live half and one dead half**, and repeating either wholesale would have been wrong.

**`revalidate_by` is ALREADY REQUIRED ON EVERY DECLARATION.** So the maintenance loop has a schema home already and this spec adds no store and no field:

```
walk asserts lifecycle_class + revalidate_by
        │
        ▼
   revalidate_by matures
        │
        ▼
   item RE-ENTERS the next walk   ◄── the loop closes in the registry
```

> **AN AGREEMENT WITH A VINTAGE NOBODY RE-DERIVES BECOMES THE FROZEN MAP THE CARDINAL RULE FORBIDS.** `revalidate_by` is what makes the assertion a *maintained* state rather than an archived one -- and it is the difference between Andrew's word "maintained" and the weaker thing this could easily become.

**Proposed:** an expired `revalidate_by` **re-enters the walk**; it does NOT silently decay to `UNDECLARED` (which would erase a real prior assertion) and does NOT persist as current (which would be the frozen map). **CVO Q4** on which of those is correct.

---

## 6. AN AGREEMENT IS NOT A MEASUREMENT -- make it legible or it will be misread

This is E5's lesson landing on this design.

> **AN AGREEMENT IS THREE PARTIES' STATE OF BELIEF AT A VINTAGE. IT IS ENORMOUSLY MORE THAN A MECHANICAL SIGNAL AND IT IS STILL NOT A MEASUREMENT.**

A producer-asserted declaration that *reads as validated* licenses every downstream consumer to trust an unverified claim -- the `comp-iam` deletion-warrant class, where a silence was read as a warrant. If this is not legible **in the artifact**, the next reader converts *"CTO and CVO agreed"* into *"verified."*

**Requirements:**
1. The record carries **participants + vintage + typed basis** -- `{WALKED_NO_DOUBT | INVESTIGATED_AND_CONFIRMED | UNEXAMINED}`, **`UNEXAMINED` as the DEFAULT so silence renders as unexamined, not as assent.** Different epistemic weights must not collapse to one token.
2. The record **never** carries a field a reader can mistake for verification status.
3. Where CVO investigated, the record **points at the investigation**, so a reader can reach the evidence rather than inherit the conclusion.
4. **THE BASIS TRAVELS WITH THE LABEL AT EVERY QUOTE SITE** *(CVO, 164214Z -- the strengthening that makes 1-3 actually work)*.

> **REQUIREMENTS 1-3 ARE ALL ABOUT WHAT THE RECORD CONTAINS. THE FAILURE DOES NOT HAPPEN IN THE
> RECORD.** It happens **at the quote site, in a different artifact**, where a consumer prints
> `lifecycle_class: PERMANENT` and the basis stays behind in the walk record. The record is perfect
> and the reader is misled anyway.
>
> **A lifecycle_class renders as `PERMANENT [walk:2026-07-31, agreed-on-sight]`.**
> **A BARE `PERMANENT` IS A MISQUOTE, NOT A SUMMARY.**
>
> Same form as the binding denominator-citation rule: **the number is quotable and the section is
> not**, so the qualifier is the first thing lost. Without requirement 4, s.6 protects the record and
> loses the reader -- **and the reader is where "agreed" becomes "verified."**

---

## 7. How it composes with the existing high-level signal

Andrew: *"the part that we have been desigining thus far with 0.7.0~B is the **high level signal**, but there can be an **additional layer**."* This spec does **not** re-spec the existing pipeline.

```
  ESTATE REPORT / Kimi Review cycle  ──►  HIGH-LEVEL SIGNAL (built, mine)
        what MOVED; where prose has probably drifted.  PROPOSES, never lands.
                              │
                              │  surfaces C3 items warranting a look
                              ▼
  C3 LABELING LAYER (this spec)  ──►  the ADDITIONAL layer
        CTO+Andrew walk · CVO on doubt · writes lifecycle_class into WS-E1
```

**Andrew's fence (5) binds the integration: this rides IN the Kimi loop.** The walk is driven by the daily cycle -- it is not an ad-hoc campaign that runs when someone remembers. *(Same failure class as the daily-apply IAM design rejected earlier today: a process whose trigger is a human remembering has no trigger.)*

---

## 8. ONE INTENT SOURCE, SEVERAL CONSUMERS

> **CTO binding: E2's deliberate-hold field and E3's Tier-A keep-dormant annotations DERIVE from the agreement. NEITHER SCAVENGES INDEPENDENTLY.**
> **Two scavengers produce two answers that disagree quietly.**

```
   THE AGREEMENT (WS-E1 registry, lifecycle_class)
        ├──► E2  deliberate-hold        (derives)
        ├──► E3  Tier-A keep-dormant    (derives)
        └──► E5  enforcement half       (derives)
```

**Sequencing this unblocks:** lifecycle stage maintained → lifecycle values populated → **WS-E3 unblocks** (today structurally INERT: its PRD forbids retirement against an UNDECLARED lifecycle, and every contract reads UNDECLARED) → **WS-E5's enforcement half unblocks** (it rides E3's commit-gate ramp).

---

## 9. Proposed TO series

Andrew: *"this needs a dedicated series of TOs wrapped into the project."* Proposed decomposition -- **CTO issues; this is a proposal, not an issuance**:

| TO | Scope | Depends on |
|---|---|---|
| **C3L.1** | Walk-record schema; `intent_source` pointer form `walk:<record-id>#<item-id>`; typed basis + typed outcome; the s.6 requirement-4 render form | this spec ratified **+ ⚠ A RAIL-AUTHOR ACT (CORE / CTO~Z)** -- see below |
| **C3L.2** | Population + ordering: C3.ii enumeration as the agenda; **C3.i as an ordering lens only** (R1); walk batch sizing | C3L.1 |
| **C3L.3** | Kimi-loop integration: how the cycle surfaces items and receives assertions | C3L.1, high-level signal |
| **C3L.4** | `revalidate_by` maturation -> **persist-marked-stale** + re-entry; **per-consumer stale policy** (R4) | C3L.1 |
| **C3L.5** | Consumer derivation contracts for E2 / E3 / E5 (s.8) + the prohibition on independent scavenging | C3L.1, C3L.4 |
| **C3L.6** | The doubt path: **SOURCE-FIRST (s.2.2.2) as step 1**, then CVO investigation, then Andrew+CTO confirm; what each returns and how it is recorded | C3L.1 |

> **⚠ C3L.1 CARRIES A CROSS-FABRIC DEPENDENCY, NAMED BY CVO AND EASY TO MISS: the A7.1 declare-time
> lint REJECTS any token that does not resolve against the ratified bank.** So the `walk:` pointer
> form **needs a RAIL-AUTHOR ACT (CORE / CTO~Z) before a single walk assertion can land.** Build the
> walk without it and every assertion is refused at declaration. It is a real dependency on another
> fabric and it belongs in the depends-on, not in a footnote.

---

## 10. Rulings (CVO, 164214Z) -- the six questions, closed

| # | Ruling |
|---|---|
| **R1** | **C3.i is OUT as an ASSERTION TARGET, IN as an ORDERING LENS.** Asserting a producer lifecycle over a recomputed structure *is* a category error -- you would be asserting the lifecycle of a **VIEW**, whose existence is a function of its inputs, not of intent. But C3.i structures **group contracted members that DO carry lifecycle**, so C3.i is a legitimate way to BATCH the walk. **FALSIFIER, named per the ruling: this reopens if a specimen shows a C3.i structure carrying producer-intent NOT reducible to its members.** Andrew's hedge is preserved as a live falsifier rather than closed by fiat. |
| **R2** | **AGENDA UNIT = the C3.ii VERTICAL** (Andrew's "state of each system"). **ASSERTION UNIT = the `contract_record`.** One walk item -> **N** assertions, deliberately not 1:1. **THE COROLLARY IS THE VALUABLE PART: a vertical whose members' assertions DISAGREE is itself a finding** -- that is a vertical which is not one system, i.e. a **mis-drawn naming act**. The 1:N mismatch is not a problem to reconcile; it is an instrument for auditing the naming layer. |
| **R3** | **`intent_source` = a resolvable pointer, never free text:** `walk:<record-id>#<item-id>`, resolving to a **committed** walk record carrying participants + vintage + basis, and **resolvable INDEPENDENTLY of the registry** -- a validator must resolve it without the builder's index. **Dependency: needs a RAIL-AUTHOR ACT (CORE / CTO~Z) before any assertion can land** (s.9). |
| **R4** | **Expired `revalidate_by`: NONE of the three I proposed -- ONE STATE, PER-CONSUMER POLICY.** The assertion **PERSISTS, MARKED STALE, and RE-ENTERS the walk.** Decay-to-`UNDECLARED` is *a control that destroys its own evidence*; persist-as-current is the frozen map; **persist-marked-stale keeps the information AND makes the staleness legible.** Then consumers differ **legitimately**: **E3 (retirement, IRREVERSIBLE) must REFUSE a stale assertion. E2's deliberate-hold must HONOR one** -- refusing to re-arm a disarm on a stale label is strictly safer than re-arming. **Spec the state once; spec the policy per consumer.** |
| **R5** | **NO countersignature -- doubt only**, per Andrew's (3). The reason is this spec's own s.6 hazard turned on CVO: *if CVO gated every landing, "CVO did not object" becomes a certification* -- the walked-vs-confirmed collapse wearing the reviewer's signature. CVO instead holds a **POST-HOC READ RIGHT**: may review landed assertions without gating them; a finding lands as a **DOUBT-RAISE that re-enters the item.** **Escalation-triggered on the way in, non-blocking on the way out.** |
| **R6** | **Disagreement: the walk record carries a typed OUTCOME** -- `{AGREED, CONFIRMED_AFTER_INVESTIGATION, SOVEREIGN_OVERRIDE}`. **Andrew is sovereign and owes no justification; the record must still be LEGIBLE AS AN OVERRIDE**, because a future reader deciding whether to re-open needs to know the label rests on a ruling over disagreement rather than on agreement -- **those have different re-open triggers.** Composes with the typed basis in s.6.1. |

---

## 11. Non-goals and fences

- **No build.** Spec only.
- **No parallel intent store.** s.4, binding.
- **No re-spec of the high-level signal.** s.7.
- **No observer inference anywhere.** Any implementation deriving `lifecycle_class` from key names, directory position, or observed absence has rebuilt the stopgap with more syntax (rule bank, verbatim).
- **THE INF LINE IS A WORK-TYPE BOUNDARY, NOT A SYSTEM BOUNDARY** (Andrew-direct via CTO 163600Z, correcting an over-broad fence):
  - ✅ **SPECIMEN-IN-SPEC** -- reason about the `aggregator` case, use it to justify the design, show how the layer resolves it. **This is dogfooding and it is wanted.** s.2.2 does exactly this and no more.
  - ⛔ **DISPATCH-TO-MEASURE** -- no INF silver reads, no `rep_id` measurement, no aggregator tracing, no seat sequenced against it. CTO's earlier ad-hoc authorization **stays retracted**.
  - ⛔ **ETFS_AVGCAP / REBATE-MECHANISM WORK** -- what Andrew was actually guarding against. **This is a DIFFERENT item from the aggregator case:** the $532K INF gold-floor / rebate-basis orphan is ETFS_AVGCAP-adjacent and **stays parked**, while `canonical_nna`/`aggregator` is advisor-attribution, not rebate. **Do not conflate them** -- CTO records nearly doing so, and the two share a pipeline while belonging to different programs.
- **CVO reviews; it does not co-author.**

---

## 12. What I am NOT claiming

- This spec is **drafted from Andrew's verbatim text and CTO's fences**, not from an implementation study. I have not enumerated the C3.ii population and have not opened the WS-E1 registry records.
- **The 14/14 `UNDECLARED` count is now CVO-VERIFIED, not merely CTO-reported** (CVO read it from the registry directly: tranche 1 = 7 subjects all UNDECLARED, tranche 2 = 7 more). **I still did not verify it myself** -- the upgrade is in the source's independence, not in my evidence.
- **EVERY FACT IN s.2.2 IS SECOND-HAND AND DELIBERATELY SO.** The daily `aggregator` caller, the three disabled rules, the 142-rule census, the resource-policy contents, the empty source search, and the independent COO/CTO classification are **CTO's and COO's measurements, cited as theirs and NOT re-derived by me** -- because re-deriving them is `DISPATCH-TO-MEASURE`, which is fenced. A worked example built on borrowed measurements is the correct shape here; **treating my re-telling of them as independent confirmation would be the exact error s.6 warns about**, committed by me, in the section arguing against it.
- The scavenging positive-control failure (s.2.1, 4-vs-13) is **COO's measurement**, cited as theirs.
- The `revalidate_by` fit (s.5) is read off the ratified rule bank's own field list. **I have not exercised it**, and "the field exists" is not "the loop works."
- Six open questions are open **because they are genuinely not mine**, not as hedging. Q1 and Q2 in particular could change the shape of the whole layer.
