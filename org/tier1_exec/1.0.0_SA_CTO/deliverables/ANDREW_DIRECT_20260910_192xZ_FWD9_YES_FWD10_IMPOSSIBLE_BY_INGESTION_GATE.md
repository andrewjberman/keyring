# ANDREW-DIRECT 2026-09-10 ~19:2xZ — FWD-9 RATIFIED · FWD-10 RE-CUT ON HIS WORD: CROSS-TENANT CORRUPTION IS IMPOSSIBLE BY CONSTRUCTION, FIRM ASSIGNED FROM THE SENDER'S EMAIL AT INGESTION

**Terminal:** `1.0.0_SA_CTO`. **Recorded by:** `1.0.0_SA_CTO`, same turn as receipt.
**Carrier class:** answers to the two `/open-calls` cards of ~19:2xZ. One ratification; one DESIGN RULING that
reshapes an outcome rather than accepting or refusing it as cut.

---

## VERBATIM AND ENTIRE

> call 1 yes. call 2 this should be impossible because there should be clear gates that assign firm based on
> email upon ingestion. e.g., if the request came from dawson.moses@49financial.com, then that needs to be gated
> to 49 Financial buckets, with those locations enumerated at outset.

---

## CALL 1 — **`FWD-9` RATIFIED.** *"call 1 yes."*

A forwarded holdings email becomes a durable, correctly scoped analysis request without anyone re-keying it.
The id is now PERMANENT on his word. It carries the narrowed WHY NEW (durability: restart, checkpoint,
idempotency) that `3.0.0_SA_CVO` required, and **his call-2 sentence sharpens its ACCEPT** — see below.

## CALL 2 — **`FWD-10` IS NEITHER ACCEPTED NOR REFUSED AS CUT. IT IS RE-CUT ON HIS WORD, ID UNCHANGED.**

⛔ **HE DID NOT SAY NO. HE SAID THE PROPERTY IS THE WRONG SHAPE.** I cut `FWD-10` as a RECOVERY property — an
operator recovers one tenant's flow without corrupting another's. His word makes it a CONSTRUCTION property:
*"this should be impossible because there should be clear gates that assign firm based on email upon
ingestion."* The cross-tenant case is not something an operator recovers from; it is something the ingestion
gate makes unreachable.

**THREE THINGS HIS SENTENCE FIXES, read narrowly:**

1. **FIRM IS ASSIGNED AT INGESTION, FROM THE SENDER'S EMAIL.** *"gates that assign firm based on email upon
   ingestion"*. The request's tenant is bound the moment it arrives, from the sender's domain, before anything
   is parsed or stored.
2. **THE REQUEST IS GATED TO THAT FIRM'S LOCATIONS AND NOTHING ELSE.** *"that needs to be gated to 49 Financial
   buckets"*. A request bound to a firm can land only in that firm's storage. This is the CLAUDE.md §5 cross-firm
   rule (BUCKET *or* KEY-PREFIX, both shapes live) applied at the ingestion seam.
3. **THOSE LOCATIONS ARE ENUMERATED AT THE OUTSET.** *"with those locations enumerated at outset"*. The per-firm
   set is a declared list that exists BEFORE the first request, not something derived per request. ⛔ And
   CLAUDE.md §5 already says what that implies: *"an enumerated ban list lapses SILENTLY when a name changes …
   a new firm name is a GATE EDIT."* The enumeration is a maintained artifact with an owner.

**WHAT I AM NOT READING IN.** He gave one example sender at one firm. The rule is the DOMAIN-to-firm binding,
not that address. He did not say the operator-recovery arms disappear — a by-construction claim is PROVEN by
driving the failure modes and showing no cross-tenant effect, so those arms survive as the PROOF of
impossibility rather than as the outcome. He did not name the mechanism (IAM condition, prefix, bucket) — that
is L4/L5 under the §5 rule. **And I am treating his sentence as ratifying the RE-CUT form of `FWD-10`, because
it states the outcome he wants in his own words. If he meant to refuse the outcome entirely, one word reverses
this and the id goes vacant.**

## WHERE IT LANDS

`ENDPOINT_FWD_IRPT_BCKEND_20260910.md`: `FWD-9` marked RATIFIED with a ratified-class note carrying the
sender-domain binding; `FWD-10` re-cut in place per `/endpoint` F0 — *"the outcome was RIGHT and INCOMPLETE …
`ACCEPT` is re-tested, not inherited."* `FWD-2` gains a cross-reference: the ingestion gate is the same
cross-firm rule at a second seam. Nothing renumbered.

## SECOND MESSAGE — VERBATIM AND ENTIRE

> Furthermore, I want a "Global" view, just like how it's done in Model Portfolios, whereby an Opal User can go
> through and run reports/analysis on ALL FIRMS.

## THIRD MESSAGE — VERBATIM AND ENTIRE

> So that has to be folded in as well both using the same firm dropdown pattern as Model Portfolios on the
> frontend, and the backend multitenant api/scoped/ layout for the backend project

## FOURTH MESSAGE — VERBATIM AND ENTIRE

> I want to make sure that these two briefs, and the associated FWDs, are clearly cut between a FE and BK
> project. This is important that we do not try to wrap all of this in one massive project.

**THE GLOBAL VIEW IS A NEW OUTCOME AND NO RATIFIED ID COVERS IT.** `FWD-2` grants *"a firm-authorized viewer …
the firm's population"* — WITHIN a firm. An Opal user reaching ALL firms is a different entitlement class: the
cross-firm rule GRANTED rather than denied, to a principal that is Opal and not any firm. It takes **`FWD-11`**,
the next unused number. **His sentence is the outcome, so it is cut RATIFIED ON HIS WORD**, the same reading as
`FWD-10`'s re-cut, with the same flag: one word reverses it.

**THE THIRD MESSAGE SUPPLIES THE MECHANISM ON BOTH SIDES AND IT IS RECORDED AS HIS, NOT DERIVED:** the FRONTEND
uses *"the same firm dropdown pattern as Model Portfolios"*; the BACKEND uses *"the multitenant api/scoped/
layout."* Those are ratified-class notes on `FWD-11` in each endpoint. How Model Portfolios implements the
dropdown, and what the scoped layout looks like in code, are **NOT READ at L2** — L4 reads both from the
existing implementations and cites them. An endpoint that guessed either from a name would be the guess the
phase exists to prevent.

**THE FOURTH MESSAGE IS A CONSTRAINT ON THE CUT AND THE ENDPOINTS ALREADY SATISFY IT, STATED SO HE CAN CHECK:**
every FWD has EXACTLY ONE `ACCEPT OWNER`. `IRPT_FNTEND` owns the grade on `FWD-1` and `FWD-6`; `IRPT_BCKEND`
owns the grade on every other id. Where an id appears in the other project's endpoint it appears as a
CONTRIBUTION (`THIS PROJECT` / `CROSSES`), never as a second owner. Two projects, two decompositions, two task
order sets, two adjudications. No umbrella exists and none is recreated by cross-reference.

## FIFTH MESSAGE — VERBATIM AND ENTIRE

> Yes these should be registered as two separate projects, IRPT_FNTEND and IRPT_BCKEND

**HE NAMED THE CODES. HIS SUPERSEDE MINE.** This seat had assigned `IRPT_FRONTEND` and `IRPT_BACKEND` at L3;
both are WITHDRAWN. `IRPT_FNTEND` and `IRPT_BCKEND` conform to the contract's project grammar
`^[A-Z]{4}_[A-Z0-9]{3,18}$` (read from `org/standards/PROJECT_TREE.contract.json`); collision 0 hits across
8,601 files over the register planes, 21 binary and 206 ephemeral-floor files disclosed as NOT covered. *"two
separate projects"* is the fourth message's constraint restated as the register act itself. The two endpoint
files are renamed to carry his codes.

## SIXTH MESSAGE — VERBATIM AND ENTIRE

> there are a ton of FWDs in backend that should not be there, the branded export is arguably a frontend op,
> even if a lambda does it, the lambda part is backend, how that report actually looks and how the modals and
> etc work are all frontned. also i dont see anything about following portal patterns and what the frontend is
> supposed to look like in fwds, i dont see anything in FWDs for FE that cover component structure and design.

## SEVENTH MESSAGE — VERBATIM AND ENTIRE

> What I am wondering is if we are basically dumbing down PRDs significantly with the FWD layout. I had CRO
> write tens of pages of highly detailed briefings, 9 of them at this point not including the two primary
> project briefs, and these are the FWDs? Please confirm the FWDs and PRDs are not lossy

**THE SIXTH MESSAGE CORRECTS THE OWNERSHIP RULE I USED, AND HE IS RIGHT.** I owned each outcome by whichever
project's ARTIFACT is hardest to prove, so advisor-facing outcomes landed in `IRPT_BCKEND` because the data
under them is backend's. His principle is the correct one: **the outcome is what the advisor sees and does;
the machinery underneath is a CONTRIBUTION.** *"the lambda part is backend, how that report actually looks and
how the modals and etc work are all frontend."* Applied across the set: `FWD-3`, `FWD-4`, `FWD-5`, `FWD-8` and
`FWD-11` move to `IRPT_FNTEND`. `FWD-2` (enforcement), `FWD-7` (freshness), `FWD-9` (ingestion) and `FWD-10`
(construction) stay `IRPT_BCKEND` because those outcomes ARE machinery — no advisor sees a directory refresh.
Nothing in any backend contribution is dropped; every CROSSES line survives, now under the frontend's grade.

**THE DESIGN GAP IS REAL.** No outcome said the product must look and behave like the portal. `FWD-12` is cut
from his words and the FE brief's §IV.2, which names the actual patterns: `PageHeaderVariants`,
`TabNavigation` + `useTabNavigation`, the catalyst `combobox`, `CategoryViewTree` + `modelPortfolioColors`,
`brand.json` + the brand guidelines. **He named the gap, not the outcome, so `FWD-12` goes to him as yes/no.**

**THE SEVENTH MESSAGE IS ANSWERED IN THE ENDPOINTS' LANDING SECTIONS AND AT HIS TERMINAL.** Short form: the
FWDs are lossy BY DESIGN and on his own 2026-09-01 word (*"It can be qualitative"*); the PRDs are NOT YET
WRITTEN and the pipeline IS lossy between brief and worker unless each PRD carries a coverage map from every
brief section to the cell that consumes it, because a worker's face never opens a brief. That obligation now
binds L4 in writing.

## SCOPE

Answers, two new outcomes (`FWD-11` ratified on his word; `FWD-12` at him), an ownership correction, and a coverage obligation on L4. Not a hold.
