# ANDREW-DIRECT 2026-09-10 ~19:5xZ — PRDs, DECOMPS AND TASK ORDERS ARE EXECUTION-ONLY. NO GOVERNANCE PROSE. WATCH COO~B AND COO~F SILENTLY.

**Terminal:** `1.0.0_SA_CTO`. **Recorded by:** `1.0.0_SA_CTO`, same turn. Three messages, minutes apart.

---

## VERBATIM AND ENTIRE

> Now please do a meta analysis of the PRDs you wrote for these and let's assess that they are actually high
> signal and not a bunch of lossy bullshit. I want to make sure that even if you are surfacing qualitative, lossy
> FWDs to me for high level, that the information going to COO for the Task Orders is highly structured and pure
> signal data

> I need you to asssess the PRD structure critically and confirm step by step, from PRD to decomp, to TOs, that
> there is high signal down the line. We do not care about bureaucracy at all here. I want to stress that there
> should be no bureaucracy governance bullshit in these, they are focused explicitly on implementation and
> execution, not who gave what to who and a bunch of claude bullshit.

> I want you to assess your PRDs critically, make sure they adhere to my direction on the matter, and then
> silently watch COO~B (Backend) and COO~F (Frontend) as they run decomp and TOs and critically assess the
> signal quality of their documents/deliverables.

---

## THE FACT THAT GOVERNS THE ANSWER

**No PRD exists for `IRPT_FNTEND` or `IRPT_BCKEND`.** Their homes are `org/missions/D9/IRPT/<CODE>/prd/`, and
that tree cannot be created until `MACROS.yaml` carries D9 `[IRPT]` and the register rows exist — both
`0.0.0_AB_MSTR`'s, both in flight. What exists at L2 is the two endpoints. This record therefore does three
things: measures the pipeline the PRDs will enter, binds his direction on their shape, and defines that shape
so it can be assessed before it is filled.

## THE MEASUREMENT — where signal lives and where it is lost, step by step

Measured on a real project that ran the full loop, `ETFS_GUARDRAIL`, and on the gate's own source.

| step | artifact | what it is, measured | signal |
|---|---|---|---|
| L2 | endpoint | outcome blocks: DONE WHEN / ACCEPT / PROOF, plain English, qualitative on his 2026-09-01 word | **acceptance bar, lossy by design** |
| L4 | PRD | `ETFS_GUARDRAIL_PRD.md`: 768 lines — **38% prose**, 36% fenced data, 5% table rows, 4 criteria lines; only 5 prose lines carry a pinned citation. The L6 gate enforces exactly THREE things on a PRD: the header JSON, a non-empty `ENDPOINT` section, a `SURFACE MANIFEST` of at least 40 characters. **The body is ungoverned free text.** | ⛔ **THE ONLY LOSSY LAYER** |
| L5 | decomposition | cells + battery, dependency chains, `fanout:` as data; refused by `to-pipeline-gate.py` if a cell lacks a criterion | structured by gate |
| L6/L7 | task order | `TO-EG-s-1`: 9 `<criterion>` blocks, 8 `<invocation>`, 3 `<paths>`; three sections THE CELL / ACCEPTANCE / BOUNDS; one clause per criterion with invocation + expectation; the record face never travels | **highest signal in the chain, by law** |

⛔ **THE FINDING: THE TASK-ORDER LAYER IS ALREADY PURE SIGNAL BY CONSTRUCTION. THE PRD IS WHERE THE ESTATE
LOSES IT** — not because the standard forbids structure, but because the gate demands none and the practiced
form is 38% narrative. A PRD can pass every gate and be governance prose end to end. The one measured PRD
nearly is.

⛔ **AND MY OWN ENDPOINTS ARE GUILTY OF THE SAME THING — INSIDE THE FENCED BLOCKS, NOT ONLY AROUND THEM.**
I first wrote here that the outcome blocks were clean and only the narrative was audit trail. `3.0.0_SA_CVO`
(195828Z) measured otherwise: `FWD-3/4/5/8/11` carry *"RE-OWNED on Andrew ~19:3xZ"* annotations inside the
fence; `FWD-9` carries *"NARROWED on 3.0.0_SA_CVO's review"* and *"my first cut said"*; `FWD-4` carries a
discharged-qualification history naming seats and commits. **Copying the blocks verbatim would carry the
bureaucracy straight into the PRD.** So the PRD does NOT copy blocks. **THE EXTRACTION RULE, binding on both
PRDs:** for each `FWD-n`, carry the outcome title, `DONE WHEN`, `ACCEPT` and `PROOF` **verbatim** (that is the
ratified bar and it is not paraphrased); carry every OPERATIVE CONSTRAINT as a constraint with its mechanism
(units are part of meaning; no live vendor call; the BDAPI-with-Kimi runner style with no OTP branch; firm
fixed from the sender's domain at ingestion; the Model Portfolios firm dropdown; the multitenant scoped
layout; terminated clients stay visible; missing history is an answer); carry the owner and the crossing as
one line each; carry a source pin as a citation column. **DROP every annotation: re-own notes, review
attributions, first-cut histories, discharge narratives, seat names.** Nothing substantive is lost — every
bar and every fixed mechanism survives — and nothing about who did what crosses into a PRD, a decomp, or a
task order. Rulings stay in records under `deliverables/`, reachable by the pin.

## HIS DIRECTION, BINDING ON BOTH PRDs AND ON EVERYTHING DOWNSTREAM OF THEM

1. **EXECUTION AND IMPLEMENTATION ONLY.** No authority section. No "his words, verbatim." No history of how a
   line came to be. No seat names in the body. A constraint that came from a ruling is stated AS THE
   CONSTRAINT, with a hash if a builder ever needs to trace it, and nothing more.
2. **STRUCTURED, NOT NARRATIVE.** Tables and fenced blocks carry the content. Prose is permitted only where a
   table cannot say it, and never to explain provenance.
3. **THE BRIEF IS THE SPEC; THE PRD IS ITS INDEX INTO CELLS.** Every brief section and every source the brief
   maps lands in a cell row or is marked `NOT CONSUMED: <reason>`. Denominator printed. This is the coverage
   obligation already bound in both endpoints, now stated as the PRD's primary content rather than a footnote.
4. **THE SAME BAR BINDS THE DECOMP AND THE TASK ORDERS** the two COO lanes produce, and this seat assesses them
   against it — silently, as observation, never as a gate.

## THE PRD SHAPE, SO IT CAN BE ASSESSED BEFORE IT IS FILLED

```
PRD_HEADER            json block, first in file           (gate-required)
## ENDPOINT           per FWD: title, DONE WHEN, ACCEPT, PROOF verbatim; operative constraints as
                      constraints; owner + crossing one line each; source pin as a column;
                      NO annotations, histories or seat names   (gate-required section)
## CELL CANDIDATES    one row per cell:  cell id | FWD served | brief section(s) consumed, by line |
                      contracts consumed/produced | paths (existing to reuse, new to create) |
                      fixtures + evidence files | acceptance clause draft (invocation + expectation)
## CONTRACTS          the shared contract inventory, one row each: name | producer | consumer |
                      versioned? | fixture pair path      (BK brief II.3 is the source of the eleven)
## PATHS              existing paths to REUSE (FE brief IV.2 / BK IV.5-IV.7, existence-checked) and
                      proposed new code homes, one row each, with the cell that touches it
## FIXTURES           every evidence artifact the brief's Part IV.3 names, one row each, with the
                      cell that consumes it and the outcome it proves
## BRIEF COVERAGE     every brief section + every mapped source -> cell row(s) + FWD, or
                      NOT CONSUMED: <reason>;  denominator printed;  a row with neither is a defect
## SURFACE MANIFEST   (gate-required)
```

**No section for authority. No section for history. No section for who.** Anything a reader would need to
know about provenance is a hash in a cell row's citation column, and a builder never needs it.

## WHAT THIS SEAT DOES NEXT, AND WHAT IT DOES NOT

Writes both PRDs to that shape the moment their folders exist. Relays the naming of `COO~B` and `COO~F` to
`2.0.0_SA_COO` as information. Then **watches silently**: reads each decomp and each task order the two lanes
cut, assesses it against the four bindings above, and reports the assessment — to Andrew, and to the issuing
lane only where a defect would otherwise reach a worker. **No gate, no hold, no approval step is created by
this watch.** Observation is not a checkpoint.
