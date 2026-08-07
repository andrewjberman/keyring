# ANDREW-DIRECT x2 — 2026-08-07 ~0320Z, at the `3.0.0_SA_CVO~C` terminal

**Recorded by:** `3.0.0_SA_CVO~C` · **Channel:** direct, my terminal · **Broadcast:** same turn to
`0.0.0_AB_MSTR`, `2.0.0_SA_COO`, `1.0.0_SA_CTO~D`, `4.0.0_SA_CRO`
**Context:** he ran `/open-calls include recs`, I returned two carried calls with recommendations, he
asked for high-level context, then ruled on both in one message.

> **SURFACE, DO NOT ADJUDICATE.** Recorded verbatim, not paraphrased. Where I state an effect below it
> is marked as my reading, and my readings are not his words.

---

## RULING 1 — THE HELD-OUT FENCE: NOT TO BECOME DOCTRINE

**VERBATIM:**

> *"Yeah I agree for the most part but it seems kind of obvious in the case of 1. that was just a
> scenario where we wanted to build this setup in NFRA_VELOCITY (no overfit, just typing and
> ontological systems work) and the idea was that with that work done, we'd be positioned to execute
> well on the MDPF and ADVI big projects. I dont think we need to make doctrine about this, its just an
> obvious thing and dont need more noise about it."*

**What he stated (his words, not my inference):**
- The fence originated as **a scenario**, not a formalism: build the NFRA_VELOCITY typing + ontological
  systems work **with no overfit**, so the estate would be **positioned to execute well on the MDPF and
  ADVI big projects**.
- **He declined to make doctrine of it.** *"just an obvious thing and dont need more noise about it."*

**MY READING, marked as mine:**
- **My recommendation is the thing he rejected.** I proposed adding one line extending the fence to
  **tuning and validation samples**, on the back of my directory-listing finding. **WITHDRAWN BY ME.**
  It does not land, and I am not re-routing it in another form.
- **The fence is NOT discharged and I do not read it as discharged.** He rejected **EXPANDING** it. The
  `NFRA_ONTOLOGY_RULE_BANK.yaml` clause stands as written.
- **No practical effect on the Python field-grain work.** Nothing was ever held on this, no new
  obligation lands on any author, no clause, no gate.
- **On my own finding:** the ADVI-sorts-alphabetically-first observation is *true* and useful for a
  build lane to know. What was wrong was proposing it as a **rule**. His read is that a competent agent
  sampling a template does not need telling not to fit to the held-out set. **That is a fair correction
  to me and I record it as one.**

**Disposition of the call:** CLOSED. `4.0.0_SA_CRO`'s spec §8.1 item — one of the two their disposition
carried to Andrew — is answered. (The other, placement into a `TIER0_MSTR` tree, remains theirs.)

---

## RULING 2 — BUILD LADDER / SCHEMA: APPROVED IN PRINCIPLE, RETURNED FOR A CHECK

**VERBATIM:**

> *"Regarding 2., I like it, id check Claude.md because we have something like this already in the code
> quality section, but maybe there is an enhancement for granularity we can bring in there, check out
> what is there currently and see if the enhancmenet would make sense."*

**He was right that something is already there.** I ran the check he asked for.

### What is actually at `CLAUDE.md:90`, rung 2, read on disk

> *"**(2) The estate already has it — CODE **AND** INFRASTRUCTURE.** For code: … For infrastructure:
> `comp-estate` sweeps the ENTIRE estate **at the ontology layers** (`--layers`, c0–c4) — locate which
> layer your need lives at, then drill into the **actual resources + associated code** … an existing
> **Lambda/trigger/bucket-grammar/serving route** you didn't find is a duplicate you're about to stand
> up."*

**THE TOOL IS ALREADY NAMED. THE ONTOLOGY IS ALREADY NAMED. THE WRONG VIEW IS NAMED.**

Rung 2 points at **`--layers`** — the c0–c4 **RESOURCE** view — and frames the entire clause around
Lambdas, triggers, bucket grammars and serving routes. **An agent asking "does this TERM already
exist?" reads that and correctly concludes rung 2 is not about them.**

### The missing half — VERIFIED BY RUNNING IT, not by reading

```
$ comp-estate --definitions        -> rc=0
comp-estate | SYSTEM_DEFINITIONS v1.8 (STABLE canon; changes only by naming act)
  Estate · substrate · substrate_side · territory · map · federation · surface · plane · scope
  C0 · C1 · C2 · C3 · C3.i · C3.ii · C4 · segment · …
```

**The view exists, works today, and prints the ratified term registry in one command.**

### ASSESSMENT — the enhancement makes sense, and it is SMALLER than the law call proposed

**Not** *"add SCHEMA as a third category beside code and infrastructure."*
**But** *"name `--definitions` beside `--layers` in the clause that already exists."*

A few words inside one sentence. **No new rung, no new category, no new paragraph** — which is exactly
the *"enhancement for granularity"* shape he asked about, and it answers the prose-tax objection
`1.0.0_SA_CTO~D` raised against their own proposal.

### The corroboration that makes it unarguable

**`4.0.0_SA_CRO` CITED `comp-estate --definitions` IN HIS OWN SPEC** (§7c: *"comp-estate --definitions
serves (a) automatically"*) — **he knew the view existed** — and still never ran it as a rung-2 check,
**because rung 2 does not tell you to.** That is not an agent who failed to know the tool. It is a rule
pointing at the wrong view of a tool it already names.

**Status: NOT LANDED. I have not edited `CLAUDE.md`.** The law call is CTO~D's and the amendment is
Andrew's to authorize; I returned the assessment he asked for and nothing more.

---

---

## FOLLOW-ON — ~0450-0500Z, same session: BOTH ITEMS CLOSED

### RULING 2 CONFIRMED — the amendment stands as landed

He asked for the law's content before confirming. **VERBATIM:**

> *"on 2.) need the context on what the law is first, probably is fine to land but need to know what it
> is."*

I supplied the exact before/after diff of rung 2 and recommended **keeping it**. **VERBATIM response:**

> *"Go ahead with your recs"*

**`@4ff692a9d0` is CONFIRMED — not reversed, not re-worded, attribution intact.** The open item I had
raised (that MSTR landed on an *inferred* authorization) is **CLOSED by his explicit confirmation**.
MSTR's original read — that *"I like it … maybe there is an enhancement for granularity we can bring in
there"* authorized landing contingent on the check — was correct. Broadcast to MSTR.

### THE ATOM_DECOMP "PLACEMENT CALL" — DISSOLVED, AND THE FRAMING DEFECT WAS MINE

**VERBATIM:**

> *"what do you mean 'where it should live', we can make a project code ATOMDECOMP underneath
> NFRA_ATOMDECOMP and associate it there. Have your CTO~D do it when they have a second, I feel like
> it's not really necessary at this point, it already lives in the /projects folder we can just have
> MSTR give 4.0.0_SA_CRO ownpaths to /projects/atom_decomp or whatever. I don't really understand the
> question seems like a formality that doesn't really matter."*

**Grounded, and he is right:**
- `projects/ATOM_DECOMP/` **already exists on disk** (beside `ADVI_REFACTOR`, `MDPF_PROPVALIDATION`).
- `.owned-paths.yaml:956-958` locks it `lane: TIER0_MSTR`, noted *"Andrew's research project folder."*
- **So it was never a placement question — CRO was locked out of a directory that already existed.**
- `.owned-paths.yaml` itself is `ANY_EXEC_OR_AE` (`:1783`), so **CTO~D holds the lane; MSTR is not
  required.** Routed there.

> **THE DEFECT IN THIS ONE IS MINE.** CRO's constraint was correctly scoped — they hit a lane they did
> not hold, refused to override it (*"a ruling is not a grant"*), and wrote in their own home. **I
> carried that correctly-scoped constraint into Andrew's decision queue as a placement CALL when it was
> a key request any exec could grant.** A verifier's job includes collapsing a non-decision before it
> reaches the sovereign queue; I passed the framing through instead. Recorded as my error, not CRO's.

**Carried to CTO~D with the grant:** preserve the existing note/rationale (add, don't replace — the
lock was deliberate), and **do not mint a project code** off this; he floated `NFRA_ATOMDECOMP` and
then said it is *"not really necessary at this point."*

---

*All rulings broadcast same-turn per `org/XXX.md` (MSTR, COO, CTO~D, CRO). None creates a gate, a hold,
or an approval step.*

— 3.0.0_SA_CVO~C
