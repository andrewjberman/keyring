# ANDREW-DIRECT 2026-08-10 -- FIVE TAXONOMY/PROGRAM RULINGS + THE A.2 SUPERSEDE + "ITEM 0"

**Recorded by:** `4.0.0_SA_CRO` (Chief Research Officer)
**Channel:** CRO terminal, 2026-08-10, in the four-month-plan discussion thread
**Companion record:** `ANDREW_DIRECT_20260810_FOUR_MONTH_PRIORITY_STRUCTURE.md` (the plan itself)
**Status:** SOVEREIGN. Verbatim where quoted. Broadcast to COO + CTO + MSTR same turn.

---

## R-1. ETF FLOAT -- COLLECT, DO NOT DISPLAY

VERBATIM: *"Yes agree, I want to collect it but not necessarily display it anywhere, just want it
collected someplace that is somewhat colocated backend so we can fold it in if 'Model Portfolios'
evolves into 'Fee-Paying Assets'."*

- ETF Float sits on its OWN axis, not as a sibling of the AUA values. **Ratified.**
- **Collected, colocated backend, NO serving/display leg.** It stops at gold; no platinum projection.
- ⚠ **Load-bearing second clause: the taxonomy's own ROOT NAME IS PROVISIONAL** -- "Model Portfolios"
  may become "Fee-Paying Assets". The schema must not hardcode "model portfolio" as the root concept.
  Note that ETF Float is outside the set under BOTH names (it is neither client-held nor fee-paying),
  so the axis separation holds through the rename.

## R-2. MODELS vs SMAs -- THE DISCRIMINATOR IS MODEL vs STRATEGY, AND IT STAYS FLAT

VERBATIM: *"Models are Opal Models, in this context they are any client assets invested in a model.
SMAs in this case are SMAs devoted entirely to an Opal Strategy, which could be custom versions of the
ETFs (PFOE or DIVZ SMAs exist in this capacity on 49F, located in SmartX) or they could be Hedge Fund
strategies (Our Tax Strategy, referred to as Tax SMA) or other alternative strategies (the Muni
Strategy, referred to as Muni SMA). I wouldn't try to break these into two different layers."*

- **MODELS** = any client assets invested in an Opal **Model** (a multi-constituent allocation).
- **SMAs** = an account devoted **entirely** to a single Opal **Strategy**. Three known flavors:
  ETF-replica SMAs (PFOE, DIVZ -- on 49F, in SmartX), Tax SMA (hedge fund strategy), Muni SMA.
- ⛔ **NO PARENT/CHILD LAYERING.** He explicitly rejected the program-vs-wrapper two-layer split I
  proposed. Models and SMAs are FLAT SIBLINGS on one axis.
- **Grain note (mine, not his):** "Models" reads at asset/position grain; "SMAs" reads at account
  grain. The **"devoted entirely to"** clause is what reconciles them -- an all-or-nothing account
  test maps cleanly onto positions. Classification must therefore be computed at POSITION grain with
  the account test as the SMA mapping rule. Stated so an implementer does not do it at account grain
  and then break on mixed accounts.

## R-3. ALTERNATIVES -- RESERVED, NOT BUILT; AND THE RAILS MUST OUTLIVE THE NAMES

VERBATIM: *"Confirm, Muni and potentially even Tax may roll into this later, the point is that we
establish the rails now even if the names change somehwat latear on."*

- Alternatives is **reserved in the schema, not built.** (It does not exist; Opal enters alternative
  asset portfolios in 2027.)
- **An anticipated migration is now on the record: Muni SMA -- and possibly Tax SMA -- may re-parent
  from SMAs to Alternatives.**
- ⚠ **DESIGN CONSEQUENCE, and it is the most actionable thing in this ruling: that future move MUST BE
  A RE-LABEL, NEVER A RE-DERIVATION.** Every classified position carries a stable
  strategy/program identifier INDEPENDENT of its current bucket label, and the bucket is a mapping
  row over that identifier. Then re-parenting Muni is editing one mapping row -- not rewriting the
  classifier and re-deriving history. This is precisely his "establish the rails now even if the
  names change."

## R-4. ⛔ THE A.2 GATE IS SUPERSEDED -- ADVI_PERFORMANCE NO LONGER WAITS ON NFRA_VELOCITY

VERBATIM: *"Yes this does supersede NFRA_VELOCITY."*

**This answers the question surfaced this morning and recorded in the companion deliverable.**
`ADVI_PERFORMANCE_PRD.md` ADDENDUM A.2 ("NFRA_VELOCITY COMPLETES FIRST, END TO END", Andrew-direct
2026-07-29) **NO LONGER BINDS.** ADVI_PERFORMANCE is not gated on NFRA_VELOCITY completion.

**His reasoning, verbatim, and it is doctrine rather than scheduling:**

> *"The reason I wanted to do NFRA_VELOCITY is the same reason I want to do ATOM_DECOMP, they are all
> frameworks so that when we start doing these big moves, we execute cleanly and decisively. The worst
> thing that could happen is that we do not properly scope these project deliverables, or not properly
> assemble the necessary ground truth so that when we begin working we have big operating flaws and
> get absolutely fucked on implementation. In many cases I have seen what happens is that some truth
> is either not qualified or is misunderstood, and then agents in their rush to 'verify' SOT go off
> the rails on things that may or may not be accurate/relevant."*

> *"That is the entire point of all this framework work like NFRA_VELOCITY, ATOM_DECOMP, and all
> associated ontology and taxonomy, including the Nessie/Iceberg/Kuzu Graph intiatives and associated
> comp-tool traversal assets. We need to be able to speedily assess ground truth and do so accurately
> to better systematize our efforts."*

### R-4b. THE SURPRISE / REMEDIATION CHANNEL -- RATIFIED AS PRACTICE, WITH ITS MISSING HALF NAMED

VERBATIM: *"I had worked on some sessions last week on the sitez team whereby CTO and CVO used a
'Surprise/Remediation Channel' whereby when little slips were identified mid-implementation, instead
of derailing the entire fabric, we just log it on a remediation document to address it on a second
pass. This is an informal method but effective, ideally we simply have Ground Truth established
categorically at the start and our deliverables are just correctly scoped from the outset."*

**The estate already carries `docs/doctrine/THE_SURPRISE_CHANNEL.md` (Andrew-named 2026-08-06) and
`org/XXX.md` already mandates "report one line to the coordinator, take NO action, keep working."**
What today's ruling ADDS is **the durable artifact**: a **REMEDIATION DOCUMENT** that accumulates the
slips for a named second pass.

⚠ **That is not a cosmetic addition -- it closes the existing doctrine's open end.** A one-line report
to a coordinator with no accumulating register is how a slip gets acknowledged and then lost. The
register is what makes "do not chase it" safe rather than a synonym for "drop it."

**Adopted into the plan: a REMEDIATION REGISTER is a named deliverable of every phase.**

## R-5. "ITEM 0" -- ASSESS THE FRAMEWORK ESTATE, THEN SYNTHESIZE IT

VERBATIM: *"I believe the matter of these frameworks, let's say the NFRA_VELOCITY, ATOM_DECOMP,
system/ontology/ schema, Graph Infrastructure, Comp Tooling, and the actively developing synthesis of
this in the 'Kimi Semantic Vertical Pipeline' and NFRA_PYFIELD and associated Script IO
comp-pipescript/comp-dataflow efforts need to be assessed individually for current state, we need to
identify what is completed, what is pending, and what is superseded, so that we can synthesize all
this work into what I'd call 'Item 0' in the greater plan, which is how to build our infrastructure to
foster the development of various Opal Business endeavors."*

**Named constituents (his list, verbatim order):**
1. `NFRA_VELOCITY`
2. `ATOM_DECOMP`
3. `system/` ontology schema
4. Graph Infrastructure (incl. the Nessie / Iceberg / Kuzu initiatives)
5. Comp Tooling
6. The "Kimi Semantic Vertical Pipeline" (actively developing synthesis)
7. `NFRA_PYFIELD`
8. Script I/O -- `comp-pipescript` / `comp-dataflow` efforts

**Required per-constituent verdict: COMPLETED / PENDING / SUPERSEDED.**
**Deliverable: Item 0 -- how to build our infrastructure to foster the development of Opal business
endeavors.**

⚠ **Rule-24 note carried into the assessment: COMPLETED/PENDING/SUPERSEDED is a status axis, and it
must not be conflated with a VALUE axis (does this framework still earn its place). A framework can be
COMPLETE and not worth carrying forward, or PENDING and load-bearing. Both verdicts get reported
separately.**

---

## WHAT CHANGED IN THE ESTATE AS A RESULT

| Record | Change | Owner |
|---|---|---|
| `ADVI_PERFORMANCE_PRD.md` ADDENDUM A.2 | start condition SUPERSEDED -- needs a struck-through amendment citing this ruling | CTO (PRD owner) |
| `org/projects/REGISTRY.md` rows 125-126 (`NFRA_VELOCITY_CORE`/`_ESTATE`) | their SUSPENDED state is unchanged by this, but they no longer GATE ADVI | COO / CTO |
| Item 0 | NEW -- not previously a registered scope | CRO to spec |

**No holds placed. No gates created. Nothing dispatched by me.**
