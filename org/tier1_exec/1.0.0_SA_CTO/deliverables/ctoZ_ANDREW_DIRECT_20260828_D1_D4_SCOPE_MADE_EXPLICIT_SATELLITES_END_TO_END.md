# ANDREW-DIRECT 2026-08-28 ~01:3xZ — D1 + D4 SCOPE MADE EXPLICIT

**Received at:** the `1.0.0_SA_CTO~Z` terminal (site Z), 2026-08-28 ~01:3xZ
**Recorded by:** `1.0.0_SA_CTO~Z`, same turn as receipt, per `org/XXX.md` ("Andrew-direct
instructions — RECORD + BROADCAST, same turn").
**Channel:** direct terminal message, mid-turn, unprompted.
**Preceding context:** his launch word this session was *"bring tier1 agents on, they need to finish
D1 and D4"* (relayed by `0.0.0_AB_MSTR~Z`, msg 11360). This message narrows what "finish" means.

---

## 1. THE INSTRUCTION — VERBATIM, UNEDITED

> Let's make it extra clear what you guys are meant to be working on. 1.) Finalizing the Asset
> Clasification data flows for "Model Portfolios" and appropriately improving the formatting/design
> of the frontend for that function. 2.) End to end full "Satellites" view mode on "Positioning"
> page, including all backend and api work, and calculations to blend "Characteristics" and
> "Performance" and "Holdings Breakdown" weights of said "Satellite" portfolios which are relally
> just blends of models so we have all the data you need.

⛔ **THE PHRASING IS THE RULING.** Typos (`Clasification`, `relally`) are HIS and are preserved.
Do not quote a cleaned-up version — a tidied quote is a paraphrase wearing quotation marks.

---

## 2. WHAT IS PLAINLY IN IT — the two items, at his own grain

### ITEM 1 — Model Portfolios asset classification (this is D1)
Two halves, and he named both:
- **"Finalizing the Asset Clasification data flows"** — the DATA half.
- **"appropriately improving the formatting/design of the frontend for that function"** — the
  RENDER half. Note the word **improving**: this is not "make it work", it is a QUALITY bar on an
  existing surface. He is asking for design work, not only correctness.

### ITEM 2 — Satellites view mode on Positioning (this is the D4 / `ETFS_SATELLITES` surface)
- **"End to end full"** — his words, and both words carry weight: END TO END (no rung excluded) and
  FULL (not a shell, not a partial book).
- **"including all backend and api work"** — he named the API leg explicitly.
- **"calculations to blend 'Characteristics' and 'Performance' and 'Holdings Breakdown' weights"** —
  THREE named panels, each requiring a blend computation. He enumerated them; this is a declared set.
- **"of said 'Satellite' portfolios which are relally just blends of models"** — a STRUCTURAL claim
  about what a Satellite IS.
- **"so we have all the data you need"** — a SUFFICIENCY claim. See s.4.

---

## 3. THE SUFFICIENCY CLAUSE — the load-bearing half, stated separately because it will be skipped

> "which are relally just blends of models so we have all the data you need"

**This is a sovereign statement that NO NEW DATA ACQUISITION IS REQUIRED for item 2.** A Satellite
portfolio is a blend of models; model data already exists on our planes; therefore Characteristics,
Performance and Holdings-Breakdown for a Satellite are **DERIVABLE BY COMPUTATION** from model-level
data we already hold.

**What it forecloses:** any plan whose first step is "we need a new feed / a new vendor field / a new
pull for satellites." He has pre-answered that. A seat that opens one is working against his word.

**What it does NOT foreclose:** the blend MECHANICS. He said the inputs exist. He did not say the
weighting math, the as-of alignment, or the panel-by-panel aggregation rules are already specified.
Those are ours to build, and two of the three panels do not blend the same way (see s.5).

---

## 4. HOW THIS SITS WITH HIS EXISTING RULINGS ON THIS SURFACE — no conflict found

His 2026-08-27 ~16:1xZ ruling, verbatim: *"an SMA that has a blend of a Satellite and Opal Model is
not a Satellite, they merely are allocating to a Satellite."*

**These are CONSISTENT and the distinction is worth stating so nobody reads a contradiction into it:**

```
A SATELLITE          IS-A    blend of MODELS          <- this message (item 2)
AN SMA               HOLDS-A Satellite (+ a Model)    <- the 08-27 ~16:1xZ ruling
                             => an ALLOCATOR, excluded from the Satellite set
```

One level down is composition; one level up is allocation. The 08-27 exclusion of blends removes
**allocators**, and it does not touch the fact that the Satellite itself is composed of models.
His ~22:5xZ derived-registry ruling (*"Does it say 'Opal Satellite' in the name? Add it and track
henceforth"*) is likewise untouched — that governs MEMBERSHIP; this governs the CALCULATION over the
members.

---

## 5. WHAT I AM SURFACING RATHER THAN ADJUDICATING

⛔ Per `org/XXX.md`: *"The receiving agent does NOT adjudicate scope. SURFACE, DO NOT ADJUDICATE."*
Each item below is a question, not a ruling.

**(a) THE ONE THAT MATTERS MOST — does item 2 re-centre D4?**
The fabric seated three lanes ~30 minutes before this message, with D4's critical path understood as
`ETFS_POSITIONING` promote-condition (ii) — *"GICS replaced for sub-categories on frontend"*. **That
work appears in NEITHER of his two items.** Item 2 names the SATELLITES view mode end-to-end.
- Does item 2 SUPERSEDE the ETFS GICS condition-(ii) work, or run BESIDE it?
- His condition-(ii) word (2026-08-24) has not been withdrawn; this message does not mention it.
- **I am not resolving this. It goes to Andrew as an open call** — and per "latest + most-restrictive
  binds", a reader must not assume either answer from this record.
- ⚠ NOTE THE ASYMMETRY: reading it as SUPERSEDE and being wrong idles committed work; reading it as
  BESIDE and being wrong spends seats on work he did not ask for. Neither error is free.

**(b) "Model Portfolios" in item 1 — which register members?**
D1's declared members are `D1_CATVIEWS` + `D1_NAMEDISCOVERY`. "Asset Clasification data flows" reads
onto `D1_CATVIEWS`; "formatting/design of the frontend" reads onto its render surface. Whether
`D1_NAMEDISCOVERY` is inside "that function" is not stated. Its three cut TOs are seated at
`0.4.0_DS_ClientPlatform~Q` and are unblocked either way, so **nothing stalls on this question** —
it affects reporting, not execution.

**(c) "improving the formatting/design" is a QUALITY bar with no stated acceptance.**
It is the one clause in the message with no measurable criterion. D4's completion bar is already his
smoke test (*"I dont want to see comp-closure on the directives item until i smoke it and its
definitively done"*); item 1's design half plausibly resolves the same way — **by his eye, not by an
instrument.** Not assumed here; named as the likely shape so a seat does not invent a metric.

**(d) The three panels are not one calculation, and the decomp must not treat them as one.**
He enumerated **Characteristics**, **Performance**, **Holdings Breakdown**. Flagging as an
architecture observation, for the decomp owner, NOT as a ruling:
- **Holdings Breakdown** blends by POSITION — union the models' holdings, weight by model weight, and
  the same security appearing in two models must COMBINE, not double-list.
- **Characteristics** blends by WEIGHTED AVERAGE over holdings — and not every characteristic is
  linear in weight (a yield averages; a duration averages; a ratio generally does not).
- **Performance** blends by RETURN over a TIME SERIES, where the model weights themselves may move
  across the window. A single as-of weight vector is the wrong instrument for a period return.
**Three different aggregation kinds under one sentence.** Rule 24 postulate (ii) (SAME GRAIN) and
(iv) (STATE COHERENCE — name what one remedy does NOT move) both bite here: one "blend" cell would
be a grain error, and the remedy for one panel moves neither of the other two.

---

## 6. STANDING OBLIGATIONS THIS RECORD DISCHARGES

| Obligation | Status |
|---|---|
| DURABLE record, verbatim, channel + time | THIS FILE |
| BROADCAST to COO + MSTR (+ live seats) so `latest + most-restrictive` can bind | same turn as this commit |
| SURFACE, do not adjudicate | s.5 — four items, all posed as questions |
| Do not manufacture a gate | Nothing here gates anyone; the seated lanes keep working |

**Push state of this record:** stated in the broadcast, measured, never defaulted.

---

*Recorded by `1.0.0_SA_CTO~Z`. Source: Andrew, direct, at this terminal. Nothing in s.2–s.5 is his
word except what appears inside quotation marks in s.1 and s.3–s.4.*
