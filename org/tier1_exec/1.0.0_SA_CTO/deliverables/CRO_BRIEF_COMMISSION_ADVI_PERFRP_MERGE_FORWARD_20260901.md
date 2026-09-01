# COMMISSION TO CRO — step-1 brief for ADVI_PERFRP, to enable a MERGE-FORWARD

**From:** `1.0.0_SA_CTO` · **For:** `4.0.0_SA_CRO` · **UTC:** 2026-09-01
**Authority:** Andrew-direct 2026-09-01 at the CTO terminal — *"i am ok with doing it the official
way... we do this properly."*
**Pipeline position:** STEP 1 (CRO brief). Its consumer is STEP 2, `/endpoint --forward`, built
2026-09-01 @`3e2244fee1` per `SPEC_CANONICAL_LOOP_INCORPORATION_20260901.md` §1.2.

---

## 1. WHY A BRIEF FOR A PROJECT THAT IS ALREADY MIDSTREAM

Andrew's diagnosis, and it is the reason this exists: **whole projects were becoming thrashing debug
sessions with no hierarchy.** `ADVI_PERFRP` is the live instance — on 2026-09-01 five seats spent an
afternoon on one producer question and generated **nine hypotheses, all of which died**, with no
frame holding them.

The remedy is a **MERGE-FORWARD**: re-declare where this is going, then reconcile the work in flight
against it. Andrew's own framing, and the git metaphor is exact — the task orders are a divergent
branch, the re-declared endpoint is the new base, **and what makes a merge safe is that you can see
the conflicts.**

`/endpoint --forward` cannot run today: it requires a step-1 brief and **there is none** (479 briefs
in `docs/briefs/`, none for PERFRP — the PRD was grounded on a run, P1–P16, not a brief). **That is
what this commission fills.**

## 2. ⛔ THE ONE CONSTRAINT THAT MAKES THIS WORK RATHER THAN CEREMONY

**AUTHOR THE BRIEF BLIND TO THE CURRENT TASK-ORDER SET.**

>> If the brief is written while looking at what is open, it will describe an endpoint that
   RATIFIES what is open — and the output is the same thrash with a fresh label and a ceremony
   attached. <<

Do not read `org/**/task_orders/ADVI_PERFRP.*`, and do not read the project JSON's `phase` or
`blocking` fields. Those are the *branch*; this brief is the *base*. The reconciliation happens
afterwards and is somebody else's step.

**What you MAY read, and should:** the PRD's own purpose and acceptance sections, the original
recording/screenshots the shape was pinned from, the ratified performance facts, and the served
reality (what a user can actually see today).

## 3. WHAT ALREADY EXISTS — do not re-derive it

- **`docs/architecture/ADVI_PERFRP_PRD.md`** — 279 lines. §1 states the purpose; §7 carries eleven
  acceptance properties; §6 pins the report shape from Andrew's own recording.
- **The purpose, as written:** per-client performance attribution and reporting for 49 Financial,
  **comparable to the Black Diamond Performance Reporting dashboards**, built on our spine and on
  already-ratified performance facts, produced on the canonical schedule, rendered **only** in the
  Books tab (L2/L3/L4) and the Advisor's Book view.
- **Two standing boundaries:** since-inception views cross the 2024 seam only through `ADVI_STITCH`'s
  labelled tier; insurance shows **beside — never inside** — the figures, via `ADVI_INSURE`.
- **BD is the inspiration and the parity oracle, never a dependency.**

⚠ **My honest read, offered so you can disagree with it rather than inherit it:** that purpose
section still looks coherent and still looks right. **I expect this brief to conclude the endpoint
has NOT changed** — and that the failure was in decomposition, not direction. That is a valid and
useful outcome. **Do not treat "unchanged" as a failed brief.**

## 4. WHAT THE BRIEF MUST CARRY (its consumer is a specific skill)

`/endpoint --forward` reads this brief and emits numbered capability outcomes, each traced to a brief
line. So the brief needs:

1. **The outcome territory in prose a capability can be cut from** — what an advisor can DO that they
   cannot do today, not what a system emits.
2. **Enough substance per outcome to be traceable** — `--forward` prints a `SOURCE:` line citing your
   brief; a claim with no line to cite cannot become an outcome.
3. **Where the boundary sits** — what is deliberately NOT this project. `ADVI_STITCH`,
   `ADVI_INSURE`, `ADVI_ROSTERCOLS` and `ADVI_BDPARITY` are separate projects; say what PERFRP
   relies on from them versus what it owns.
4. **The qualitative bar.** Andrew, verbatim: *"This does not have to be a deliverable contract. It
   can be qualitative because we will not know enough about the quantitative mechanics at this
   point."* ⛔ **Do not invent numbers.** A number fabricated at step 1 is treated as ratified by
   every later stage because it is sitting in a document.
   **Qualitative is not vague — the test is disputability.** *"Advisors find it useful"* fails,
   because nobody can contest it. *"An advisor reads a figure here they would otherwise have opened
   Black Diamond for"* passes: it names who, what, and the alternative it displaces, with no number.

## 5. WHAT IS OUT OF SCOPE FOR THIS BRIEF

- **Not a debug report.** The open producer question is live and is not yours to solve or summarise.
- **Not a re-litigation of settled rulings** — the canonical digest form, the deferral of one
  transactions family, the never-widen co-signs already given.
- **Not a decomposition.** No cells, no task orders, no sequencing. That is COO's step and it comes
  after the PRD.
- **Not a status report.** `/exec-sum` exists and was run 2026-09-01.

## 6. WHERE IT GOES AND WHAT HAPPENS NEXT

```
  step 1  YOU          the brief                          -> docs/briefs/
  step 2  1.0.0_SA_CTO /endpoint --forward <brief>        -> qualitative capability outcomes
  step 3  1.0.0_SA_CTO the outcomes written INTO the PRD  -> a named ENDPOINT section
  step 4  2.0.0_SA_COO reconcile the in-flight TOs        -> KEEP / AMEND / RETIRE / ENDPOINT-INCOMPLETE
```

⛔ **The fourth reconciliation bucket is the guard and it is not optional.** A task order that serves
something real which the new endpoint fails to name is **evidence the ENDPOINT is incomplete** — not
evidence the task order is waste. Without that bucket, a re-declared endpoint lets us define away our
open problems, and **the endpoint's author is the party who benefits from a smaller one.**

⚠ **And knowledge outlives the task order that carried it.** The 2026-09-01 session produced real
measurements — an invalid before/after baseline, an observability gap where emitter refusal reasons
are written to local disk and never uploaded, and a false-deny trap in a standard IAM instrument.
**Those must be harvested to the project record before any task order closes**, or we re-buy them
later at full price.

## 7. ONE THING I DO NOT KNOW AND WILL NOT GUESS

Whether the endpoint Andrew wants **now** is the endpoint the PRD describes from 2026-08-24. That is
the entire question this brief exists to put in front of him, and it is his to answer — not mine to
pre-empt and not yours to assume in either direction.
